// 接続先 (NoLang API の URL) の決め方。プラグインに入った CLI は、そのプラグインの接続先 (`defaults.json`) を
// 前回ログインした接続先より優先する — dev のプラグインから使う時に、前に localhost へログインしたせいで localhost に行かないように。
export const FALLBACK_API = "http://localhost:18000";

export function pickApi({ flag, env, packaged, stored } = {}) {
  const raw = flag || env || packaged || stored || FALLBACK_API;
  return raw.replace(/\/+$/, "");
}
