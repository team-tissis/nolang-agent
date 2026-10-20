// OAuth の戻り先 URL (`…/callback?code=…&state=…`) から認可コードを取り出す
import { CliError, EXIT } from "./errors.mjs";

export function codeFromCallback(callbackUrl, expectedState) {
  let url;
  try {
    url = new URL(callbackUrl.trim());
  } catch {
    throw new CliError("callback の URL として読めない", { exit: EXIT.USAGE });
  }
  const error = url.searchParams.get("error");
  if (error) throw new CliError(`認可されなかった: ${error} ${url.searchParams.get("error_description") || ""}`.trim(), { exit: EXIT.AUTH });
  if (url.searchParams.get("state") !== expectedState) throw new CliError("state が合わない (別のログインの URL?)", { exit: EXIT.AUTH });
  const code = url.searchParams.get("code");
  if (!code) throw new CliError("callback の URL に code が無い", { exit: EXIT.AUTH });
  return code;
}
