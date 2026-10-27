// OAuth の戻り先 URL (`…/callback?code=…&state=…`) から認可コードを取り出す
import { CliError, EXIT } from "./errors.mjs";

export function codeFromCallback(callbackUrl, expectedState, redirectUri) {
  let url;
  try {
    url = new URL(callbackUrl.trim());
  } catch {
    throw new CliError("callback の URL として読めない", { exit: EXIT.USAGE });
  }
  if (url.searchParams.get("state") !== expectedState) throw new CliError("state が合わない (別のログインの URL?)", { exit: EXIT.AUTH });
  if (redirectUri) {
    const expected = new URL(redirectUri);
    if (url.origin !== expected.origin || url.pathname !== expected.pathname || url.username || url.password) {
      throw new CliError("callback の戻り先が開始時と違います", { exit: EXIT.AUTH });
    }
  }
  const error = url.searchParams.get("error");
  if (error) throw new CliError(`認可されなかった: ${error}`, { exit: EXIT.AUTH, data: { error } });
  const code = url.searchParams.get("code");
  if (!code) throw new CliError("callback の URL に code が無い", { exit: EXIT.AUTH });
  return code;
}
