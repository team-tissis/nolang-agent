// 終了コード: 0 成功 / 1 原稿の欠陥・生成の失敗 / 2 使い方の誤り / 3 未ログイン / 4 接続・サーバーの異常
export const EXIT = { OK: 0, FAIL: 1, USAGE: 2, AUTH: 3, NETWORK: 4 };

export class CliError extends Error {
  constructor(message, { exit = EXIT.FAIL, data } = {}) {
    super(message);
    this.exit = exit;
    this.data = data;
  }
}
