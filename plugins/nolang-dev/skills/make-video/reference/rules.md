# check の findings の規則名と直し方

`nolang check` / `nolang_draft_check` が返す `findings[].rule` (と描画時の lint) の名前ごとの直し方。型に合わない規則は根の `lint off=規則,…` で切れる。

- `empty_cut` 絵か札を置く
- `shrunk` 幅か文字の大きさを変える (枠を広げる / `width:` を外して文字幅にする / 文言を短く)
- `offcanvas` (severe) 位置を内側に
- `duplicate_text` 字幕と同文の札 → 画面は要点の短い語に。台詞そのものを見せる札 (リリックビデオの歌詞・吹き出し) は札に `.hide_subtitle` (見えている間は字幕を描かない
- `lint off` では 2 つ並んだまま)
- `text_overload` cut の尺で読み切れない文字量 → 文言を要点の短い語に刈る・一度に見せず語に合わせて札を入れ替える (前の札は `[<#名]` で閉じる・cut は分けない)
- `spoiler` 見出しが台詞の語を先に見せる → 語の印で出す
- `still_stretch` 6 秒以上動かない (絵の kb は動きに数えない) → 語に印を足す
- `long_still` (info) 台詞が 3 秒以上続く間に画面が変わらない → その間の語に印
- `cut_head_gap` cut 頭が 1.2 秒以上空く → 頭の要素は印なしで置く
- `entrance_in_fadeout` 切替や fade out の 0.8 秒前より後に出す → 語を前へ
- `entrance_in_transition` 語の印の入場が前の切替の窓の中で済む → 最初の台詞の頭に `[silence:+0.4s]` を足して語を窓の後へ (要る秒は check が言う)
- `no_closer` 最後の cut に大きな締めの一言が無い
- `same_picture` 同じ絵が 15 秒以上 → cut の中で語に合わせて別の絵・図・札へ替える (cut は分けない)
- `blank_band` cut の頭で画面の 1/3 が地のまま → 絵を全面に敷くか帯に札を
- `dip_black_frame` dip は黒 frame → dissolve か wipe
- `double_exit` 切替で終わる cut に cut 全体の out も掛かり、場面が fade してから切替が走る (二度消える) → fade で消えたいなら切替を `transition cut` に・切替が場面を運ぶなら section の out を外す (根から継いだ切替なら機械が切替を cut にする)
- `persistent_chrome` 常設の層 (progress / 章番号 / 累計) は 3 分以上の動画だけ — 短い動画では画面の端を 1 本占有する損の方が大きいので外す
- `sparse_cut` 4 秒以上で要素が少ない → 絵か札を足す
- `palette_drift` palette 外の色が多い
- `low_contrast` 文字と地の差が小さい (沈めた `dim` / focus の兄弟
- `recolor` の後も) → 沈める濃さを上げる
- `overlap` 同じ族の文字どうしが重なる (`overlap:` を宣言しても warn・別の族の文字を隠すのは severe の occluded) → 判子・札を相手の文字から外す
- `title_on_close` 最初の cut の題が閉じられず最後の frame に残る → `[<#名]` (締めで名を言い直すなら締めの cut に新しい層)
- `leaks_into_next_cut` (info) 切替の前に他が out で消え、out の無い層だけが次の cut の頭に残る (既定は全員が生きたまま切替に乗る — 残すか消すかを割るのは著者の out だけ) → 揃えるなら他の層にも out を書くか、その out を外す
- `orphan_line` 折り返しの最後の行が 1〜2 字 (「本気だっ / た。」) → 文言を詰める・字を小さく
- `[br]` で切る
- `overridden` engine が書いた値を変えた (cause つき) — subject_clear: 文字を絵の主体の外に置く / icon_square と late_admission: engine の揃え (直さなくてよい)
- `transition_over_speech` 切替が台詞に掛かる
- `se_dense` 効果音が密 (`sfx off`)
- `running_total` 累計の札の値が cut を跨いで減る → plan に書いた累計を写す
- `font_not_pinned` 書体を本番の解決で引けず既定 font で測った (DB のある所で check を回す・書体の説明を catalog の書体に寄せる)
- `synthetic_bold` family に太い face が無い (browser の合成 bold は無い) → 太さのある family を `font-family:` で選ぶか font-weight を外す
- `ghost_dissolve` 400 ms 以上の dissolve で前の cut の大きな文字・絵が次の cut に透ける (out の無い層か、境界より前から溶ける切替) → `overlap=` を尺と同じに (out のある文字は境界までに消え終わる)・out の無い絵や札は cut 末の `[<#名 fade]`
- `photo_hidden` 全面の写真の 9 割以上に濃さ 0.7 以上の幕が 3 秒以上掛かる (写真が白く飛ぶ / 暗く沈む) → 写真を片側の枠へ (文字は地の側) か、幕を 0.6 までにして文字の下にだけ帯 / 板。
