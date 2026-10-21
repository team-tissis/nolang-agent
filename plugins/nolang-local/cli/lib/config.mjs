// 接続先 (NoLang API の URL) の決め方。`--api` / NOLANG_API_URL / `nolang use` は名前 (TARGETS) か URL を受ける。
// 順は --api → NOLANG_API_URL → `nolang use` で選んだ接続先 → プラグインの接続先 (`defaults.json`) → localhost。
// ログインは接続先を選ばない (前にログインした接続先へ勝手に行かない — 選ぶのは `nolang use` だけ)。
import { CliError, EXIT } from "./errors.mjs";

export const TARGETS = {
  local: "http://localhost:18000",
  dev: "https://api-dev.no-lang.com",
  stg: "https://api-stg.no-lang.com",
  prod: "https://api.no-lang.com",
};
export const FALLBACK_API = TARGETS.local;

// 名前か URL → 末尾の / を落とした URL
export function apiUrl(value) {
  const named = TARGETS[value];
  if (named) return named;
  if (!/^https?:\/\/[^/\s]+/.test(value)) {
    throw new CliError(`接続先は ${Object.keys(TARGETS).join(" / ")} か http(s):// の URL: ${value}`, { exit: EXIT.USAGE });
  }
  return value.replace(/\/+$/, "");
}

// URL → 名前 (TARGETS に無ければ null)
export function targetName(api) {
  return Object.keys(TARGETS).find((name) => TARGETS[name] === api) ?? null;
}

// どの段で決まったか (source) も返す — `nolang use` が見せる
export function chooseApi({ flag, env, selected, packaged } = {}) {
  const [source, raw] = [
    ["flag", flag],
    ["env", env],
    ["use", selected],
    ["plugin", packaged],
    ["fallback", FALLBACK_API],
  ].find(([, value]) => value);
  return { api: apiUrl(raw), source };
}

export function pickApi(options) {
  return chooseApi(options).api;
}
