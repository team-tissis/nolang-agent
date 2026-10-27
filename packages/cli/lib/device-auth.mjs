import { existsSync } from "node:fs";
import { setTimeout as sleep } from "node:timers/promises";
import { CliError, EXIT } from "./errors.mjs";

// backend の migration が登録する NoLang CLI 専用の public client。秘密値ではない。
export const DEVICE_CLIENT_ID = "3ef941bb-cd19-552f-8a42-0229d64b3627";
export const DEVICE_GRANT = "urn:ietf:params:oauth:grant-type:device_code";

export function loginMethod(flags, { env = process.env, isTTY = process.stdin.isTTY, platform = process.platform, inContainer = existsSync("/.dockerenv") } = {}) {
  if ([flags.device, flags.browser, flags["no-browser"]].filter(Boolean).length > 1) {
    throw new CliError("--device / --browser / --no-browser は同時に指定できません", { exit: EXIT.USAGE });
  }
  if (flags["no-browser"] && flags.background) throw new CliError("--no-browser は単独で完了するため --background は不要です", { exit: EXIT.USAGE });
  if (flags.device) return "device";
  if (flags.browser || flags["no-browser"]) return "browser";
  const remote = env.SSH_CONNECTION || env.SSH_TTY || env.REMOTE_CONTAINERS || env.CODESPACES || inContainer;
  const headless = platform === "linux" && !env.DISPLAY && !env.WAYLAND_DISPLAY;
  return flags.background || !isTTY || remote || headless ? "device" : "browser";
}

export function validateDeviceAuthorization(body) {
  if (typeof body.device_code !== "string" || !body.device_code || typeof body.user_code !== "string" || !body.user_code ||
      !Number.isFinite(body.expires_in) || body.expires_in <= 0 ||
      (body.interval != null && (!Number.isFinite(body.interval) || body.interval <= 0))) {
    throw new CliError("デバイス認可の応答に必要な値がありません", { exit: EXIT.NETWORK });
  }
  let uri;
  try { uri = new URL(body.verification_uri); } catch { /* 下でエラーにする */ }
  if (!uri || uri.username || uri.password || !(uri.protocol === "https:" ||
      (uri.protocol === "http:" && ["localhost", "127.0.0.1", "[::1]"].includes(uri.hostname)))) {
    throw new CliError("デバイス認可の verification_uri が安全な URL ではありません", { exit: EXIT.NETWORK });
  }
  return { ...body, interval: body.interval ?? 5 };
}

// RFC 8628: 最初の問い合わせ前も interval を待つ。slow_down は以後も 5 秒加算、通信障害は backoff。
export async function pollDeviceAuthorization(pending, post, { now = Date.now, wait = sleep, signal, check = async () => {} } = {}) {
  let interval = pending.interval * 1000;
  for (;;) {
    await check();
    const remaining = pending.expires_at - now();
    if (remaining <= 0) throw new CliError("デバイス認可の期限が切れました。auth login からやり直してください", { exit: EXIT.AUTH });
    await wait(Math.min(interval, remaining), undefined, { signal });
    if (now() >= pending.expires_at) continue;
    await check();
    try {
      const tokens = await post(pending.token_endpoint, {
        grant_type: DEVICE_GRANT, device_code: pending.device_code, client_id: pending.client_id,
      }, { signal });
      if (typeof tokens.access_token !== "string" || !tokens.access_token) {
        throw new CliError("token 応答に access_token がありません", { exit: EXIT.AUTH });
      }
      return tokens;
    } catch (error) {
      if (signal?.aborted) throw error;
      const code = error.data?.error;
      if (code === "authorization_pending") continue;
      if (code === "slow_down") { interval += 5000; continue; }
      if (error.exit === EXIT.NETWORK) { interval *= 2; continue; }
      if (code === "access_denied") throw new CliError("ログインの許可がキャンセルされました", { exit: EXIT.AUTH });
      if (code === "expired_token") throw new CliError("デバイス認可の期限が切れました。auth login からやり直してください", { exit: EXIT.AUTH });
      throw error;
    }
  }
}
