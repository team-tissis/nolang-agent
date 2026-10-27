import assert from "node:assert/strict";
import { test } from "node:test";
import { DEVICE_GRANT, loginMethod, pollDeviceAuthorization, validateDeviceAuthorization } from "../lib/device-auth.mjs";
import { CliError, EXIT } from "../lib/errors.mjs";

const local = { env: {}, platform: "darwin", inContainer: false };
test("手元はエージェントの --background でもブラウザ、SSH・コンテナ・WSL・画面の無い Linux はデバイス認可", () => {
  assert.equal(loginMethod({}, local), "browser");
  assert.equal(loginMethod({ background: true }, local), "browser");
  assert.equal(loginMethod({}, { ...local, platform: "linux", env: { DISPLAY: ":0" } }), "browser");
  for (const context of [
    { env: { SSH_CONNECTION: "remote" } },
    { env: { REMOTE_CONTAINERS: "true" } },
    { env: { WSL_DISTRO_NAME: "Ubuntu" } },
    { inContainer: true },
    { platform: "linux" },
  ]) {
    assert.equal(loginMethod({ background: true }, { ...local, ...context }), "device");
  }
  assert.equal(loginMethod({ browser: true }, { ...local, inContainer: true }), "browser");
  assert.equal(loginMethod({ device: true }, local), "device");
  assert.throws(() => loginMethod({ device: true, browser: true }, local), /同時/);
  assert.throws(() => loginMethod({ "no-browser": true, background: true }, local), /不要/);
});

test("device 応答の期限・interval・確認 URL を検証する", () => {
  const body = { device_code: "secret", user_code: "BCDF-GHJK", verification_uri: "https://example.com/verify/", expires_in: 600 };
  assert.equal(validateDeviceAuthorization(body).interval, 5);
  for (const change of [{ interval: -1 }, { expires_in: 0 }, { verification_uri: "http://example.com" }, { verification_uri: "https://user:pass@example.com" }, { device_code: "" }]) {
    assert.throws(() => validateDeviceAuthorization({ ...body, ...change }));
  }
});

async function poll(errors, expires = 200000) {
  let now = 0;
  const waits = [];
  let calls = 0;
  const pending = { token_endpoint: "https://example.com/token", device_code: "secret", client_id: "client", interval: 5, expires_at: expires };
  const result = pollDeviceAuthorization(pending, async (_url, form) => {
    calls++;
    assert.deepEqual(form, { grant_type: DEVICE_GRANT, device_code: "secret", client_id: "client" });
    const error = errors.shift();
    if (error) throw error;
    return { access_token: "token" };
  }, { now: () => now, wait: async (ms) => { waits.push(ms); now += ms; } });
  return { result, waits, calls: () => calls };
}
const oauthError = (error) => new CliError(error, { exit: EXIT.AUTH, data: { error } });
test("pending は継続、slow_down は以後も 5 秒増加、通信失敗は backoff", async () => {
  const p = await poll([oauthError("authorization_pending"), oauthError("slow_down"), new CliError("offline", { exit: EXIT.NETWORK }), oauthError("authorization_pending")]);
  assert.equal((await p.result).access_token, "token");
  assert.deepEqual(p.waits, [5000, 5000, 10000, 20000, 20000]);
});
test("拒否・サーバー期限切れ・ローカル期限切れで停止する", async () => {
  for (const code of ["access_denied", "expired_token", "invalid_client"]) {
    const p = await poll([oauthError(code)]);
    await assert.rejects(p.result);
    assert.equal(p.calls(), 1);
  }
  const p = await poll([oauthError("authorization_pending")], 6000);
  await assert.rejects(p.result, /期限/);
  assert.equal(p.calls(), 1);
  assert.deepEqual(p.waits, [5000, 1000]);
});
