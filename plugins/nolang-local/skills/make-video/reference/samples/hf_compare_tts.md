# compare · tts-compare (hf 全力版の全量の写し — 音声合成の乗り換え、Flash か Lite か・3 モデルを 3 色で通す暗い比較の 10 場面) — canvas 1280x720

見せる作り: 全編の暗い地 (漂う 2 つの光・点の格子・周辺減光)・3 モデルを灰 / 青 / 青緑で通す凡例と色の四角・場面の頭の同じ見出し (番号 + 章名 + 罫 + mask から上がる 1 行) と下端の注記・下端の章の進行 (9 本の帯が章の尺で伸びる)・題つきの板の def で組む図 (語ごとに伸びる横棒と縦棒・倍額の破線の枠・token の箱 ×32 と目安の線・点の数直線と差の括弧・97% のドーナツ・63 → 4 のマスの格子)・結論の 3 枚の札・切替なしで前の場面が上へ抜ける場面替え・字幕なし・音の層 (BGM + 語に結んだ効果音 + 場面替えのパッド)

```design.txt
#v2
# 学ぶ作り: 全編に敷く暗い地 (ゆっくり漂う 2 つの光・点の格子・周辺減光) の上で、3 モデルを 3 色 (灰 / 青 / 青緑) で通して比べる 10 場面
# 場面の頭は同じ見出しの def (番号 + 章名 + 罫 + mask から上がる 1 行) と右上の凡例・下端の注記・下端の章の進行 (9 本の帯が章の尺で伸びる)
# 図は題つきの板 (def) の子で組む: 横棒 (幅は値 × 縮尺)・倍額の破線の枠・縦棒・点の数直線・token の箱 ×32・ドーナツ・63 マスの格子・結論の 3 枚の札
# 場面替えは切替を書かず、前の場面が上へ少し抜けて消え (section の out)、次の場面が組み上がる。字幕は無い (hf の作り)
# hf tts tts-compare (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1280x720 bg=#070B12
theme dark
palette lab=#7C8799 g31=#4F586A gf=#2F7FD6 gl=#1FB88C from=#9AA3B5 t1=#EEF2F8 t2=#B6BFCE t3=#8B96A8 c31=#A3ACBD c31f=#5F687B flash=#4DA3FF lite=#2FDCAA amber=#FFB547 ref=#D3D9E4 ink=#06101C note=#A9B3C3 a=#2FDCAA b=#4DA3FF
# 書体は説明文で: 和文は癖のない角ゴシックの 3 太さ (本文 Bold / 副題と注記 Medium / 札と軸 SemiBold 相当)・数字は端正なゴシックの Bold / ExtraBold・番号は等幅
font "癖のない現代的な角ゴシック体の太字 (Bold)、IT 資料向け"
fonts r="癖のない標準的なゴシック体の Medium、副題と注記が端正で読みやすい"
fonts sb="癖のない標準的なゴシック体の太字 (Bold)、札と軸の字が端正で読みやすい"
fonts i="癖のない標準的なゴシック体の太字 (Bold)、数字と英字が端正で読みやすい"
fonts n="癖のない標準的なゴシック体の極太 (ExtraBold)、大きな数字が端正でくっきり"
fonts m="等幅のプログラミング用書体の SemiBold"
shadow_default 0
sfx off
# hf の作り: 見出し・板の題・凡例・注記は場面の頭に置き、台詞が後から読む (spoiler)・注記は場面の頭に 1 行で全文 (all_at_once)・図だけの板で写真は使わない (text_only_cut)
# hf の作り: 凡例・板の副題・注記・章の進行は 12〜17 px (1080 換算 18〜26 px) の小さな字 (small_text)・題の副題と売りの板の足は短く出る (flash_text)
lint off=spoiler,all_at_once,text_only_cut,small_text,flash_text
# hf の作り: 題のヒット (3.6 秒) と注意の単音 (6.7 秒) は余韻ごと最後まで鳴らす (warn se_long が 4 件残る)
sound hit = "シャーンと広がるシンセのヒット音、柔らかい立ち上がりで余韻が長い"
sound pad = "シュワーンと広がる浮遊感のあるシンセパッドの短い音、場面転換向け"
sound accent = "中音域の木琴のような短く柔らかい音、余韻はほぼ無い"
sound chime = "シンプルで落ち着いた電子のチャイム、柔らかい立ち上がり"
sound swell = "ヒュンと滑らかに上昇するサイン波の短い音"
sound tense = "ポーンと響く緊張感のあるシンセの単音、余韻が長い"
sound pop = "ピコンという短いシステム音風の電子音"
svg person = """<svg viewBox="0 0 150 230"><circle cx="75" cy="58" r="40" fill="#2fdcaa"/><path d="M8 226 C 8 150, 40 118, 75 118 C 110 118, 142 150, 142 226 Z" fill="#2fdcaa"/></svg>"""
run f = color=$flash
run l = color=$lite
run fd = color=$flash font=i
run ld = color=$lite font=i
run d = font=i
run b = color=$t2
run w = color=$t1
run s = size=0.77em
run a6 = color=$amber font=n size=1.75em
p { color: $t1 }
div { padding: 0px; border: none; box-shadow: none; border-radius: 0px; background: none }
motion fup = in=y=15,opacity=0,duration=550 ease=power3.out
motion fups = in=y=7,opacity=0,duration=550 ease=power3.out
motion fin = in=opacity=0,duration=450 ease=power1.out
motion bpop = in=scale=0.6,opacity=0,duration=450 ease=back(2.2)
motion brd = in=y=20,scale=0.985,opacity=0,duration=700 ease=power3.out
cue chap(p, c) = [!#p recolor,#98A3B5,duration=350][!#c recolor,#EEF2F8,duration=350]
bgm#music(fade: 250,3600; duck: -6.5) 知的で落ち着いたミニマルなシンセの曲、浮遊感のあるパッドと静かなシンセベルのフレーズ、淡々とした控えめなビート、暗いデータ解説向け

# 全編の地: 暗い放射の地・左上の青と右下の青緑の光 (全編でゆっくり逆向きに漂う)・点の格子 (ゆっくり上へ)・周辺減光
div#bg_base(inset: 0; background: radial(#0F1828,#0A0F18@45%,#070B12@75%,68%,18%); z-index: back; in: none)
div#bg_g1(left: -280px; top: -427px; width: 1000px; height: 1000px; background: radial(#4DA3FF21,#4DA3FF00@62%,50%,50%); z-index: back; in: none; main: keys(at=0 x=0 y=0 | at=1 x=200 y=113 ease=sine.inOut),window=0,117500,forwards)
div#bg_g2(left: 667px; top: 253px; width: 1000px; height: 1000px; background: radial(#2FDCAA17,#2FDCAA00@62%,50%,50%); z-index: back; in: none; main: keys(at=0 x=0 y=0 | at=1 x=-227 y=-100 ease=sine.inOut),window=0,117500,forwards)
div#bg_grid(left: -27px; top: -27px; width: 1334px; height: 774px; pattern: dots,27,#FFFFFF0F; z-index: back; in: none; main: keys(at=0 y=0 | at=1 y=-27 ease=none),window=0,117500,forwards)
div#bg_vig(inset: 0; background: radial(#00000000,#00000000@55%,#00000099,50%,48%); z-index: back; in: none)

# 場面の見出し: 番号 (等幅・青緑) + 章名 + 伸びる罫 + mask から上がる 1 行 (場面の頭の 0.3 秒後から組み上がる)
def header(n, k, h) = div(left: 59px; top: 40px; width: 1100px; height: 76px; in: none)
  p#n(left: 0px; top: 2px; font-size: 15px; font-family: m; color: $lite; letter-spacing: .06em; delay: 300; in: {x:-11, opacity:0, duration:.45, ease:'power3.out'}; content: {n})
  p#k(left: 27px; top: 2px; font-size: 15px; font-family: r; color: $t2; letter-spacing: .08em; delay: 360; in: {x:-7, opacity:0, duration:.45, ease:'power3.out'}; content: {k})
  div#rule(left: .k.right+9; top: 10px; width: 43px; height: 1px; background: #FFFFFF2E; delay: 400; in: {scaleX:0, pivot:'left', duration:.6, ease:'power3.out'})
  p#h(left: 0px; top: 30px; font-size: 35px; line-height: 1.22; letter-spacing: .01em; delay: 420; in: mask_rise,850,ease=power4.out; content: {h})
# 右上の凡例 (色の四角 + モデル名 ×3)
def legend = div(left: 786px; top: 43px; width: 436px; height: 24px; delay: 700; in: {y:-5, opacity:0, duration:.4, ease:'power2.out'})
  div#s1(left: 0px; cy: 50%; width: 12px; height: 12px; border-radius: 3px; background: $c31f; border: 1px solid #FFFFFF40)
  p#t1(left: 19px; cy: 50%; font-size: 15px; font-family: r; color: $t2) 3.1 Flash preview（現行）
  div#s2(left: .t1.right+17; cy: 50%; width: 12px; height: 12px; border-radius: 3px; background: $flash)
  p#t2(left: .s2.right+7; cy: 50%; font-size: 15px; font-family: r; color: $t2) 3.8 Flash
  div#s3(left: .t2.right+17; cy: 50%; width: 12px; height: 12px; border-radius: 3px; background: $lite)
  p#t3(left: .s3.right+7; cy: 50%; font-size: 15px; font-family: r; color: $t2) 3.8 Flash-Lite
# 下端の注記 (数字の出典を 1 行で)
def note(t) = p(left: 59px; top: 628px; width: 1163px; font-size: 17px; line-height: 1.5; font-family: r; color: $note; delay: 800; in: {opacity:0, duration:.6, ease:'power1.out'}; content: {t})
# 題つきの板 (半透明の地 + 細い縁 + 深い影・題 + 副題 + 罫)。題だけの板は box
def board(t, s, rw) = div(border-radius: 15px; background: linear(#FFFFFF0D,#FFFFFF06,180); border: 1px solid #FFFFFF1A; box-shadow: 0px 23px 60px #0000006B; in: brd)
  p#t(left: 23px; top: 18px; font-size: 20px; font-family: sb; letter-spacing: .02em; content: {t})
  p#s(left: .t.right+11; top: 22px; font-size: 15px; font-family: r; color: $t3; content: {s})
  div#rule(left: 23px; top: 52px; width: {rw}; height: 1px; background: #FFFFFF1A)
def box(t, rw) = div(border-radius: 15px; background: linear(#FFFFFF0D,#FFFFFF06,180); border: 1px solid #FFFFFF1A; box-shadow: 0px 23px 60px #0000006B; in: brd)
  p#t(left: 23px; top: 18px; font-size: 20px; font-family: sb; letter-spacing: .02em; content: {t})
  div#rule(left: 23px; top: 52px; width: {rw}; height: 1px; background: #FFFFFF1A)
# 候補の板 (色の四角 + モデル名 + NEW の札 + 売り + 導入価格の注記)
def cand(m, d, c, bd) = div(width: 475px; height: 137px; border-radius: 15px; background: linear(#FFFFFF0D,#FFFFFF06,180); border: 1px solid {bd}; box-shadow: 0px 23px 60px #0000006B; in: {y:13, scale:0.985, opacity:0, duration:.7, ease:'power3.out'})
  div#sw(left: 23px; top: 24px; width: 15px; height: 15px; border-radius: 3px; background: {c})
  p#m(left: 47px; top: 14px; font-size: 31px; font-family: i; letter-spacing: -.01em; content: {m})
  p#tag(right: 23px; top: 22px; font-size: 12px; font-family: m; letter-spacing: .08em; color: $ink; background: {c}; border-radius: 5px; padding: 4px 8px) NEW
  p#d(left: 23px; top: 66px; font-size: 17px; font-family: r; color: $t2; content: {d})
  p#d2(left: 23px; top: 99px; font-size: 14px; font-family: r; color: $amber; opacity: .9; in: fin) 2026 年末まで導入価格
# 丸のチェック (青緑の輪 + 描かれるチェック)
def chk = div(width: 27px; height: 27px)
  shape#o.ellipse(left: 0px; top: 0px; width: 27px; height: 27px; background: #2FDCAA24; border: 1.5px solid $lite)
  icon#k(cx: 50%; cy: 50%; font-size: 16px; name: check; weight: bold; color: $lite; delay: 200; in: draw,400)
# 結論の札 (番号の丸 + 題)
def card(no, t) = div(width: 375px; height: 427px; border-radius: 16px; background: linear(#FFFFFF0E,#FFFFFF06,180); border: 1px solid #FFFFFF1A; box-shadow: 0px 23px 60px #0000006B; in: brd)
  p#no(left: 23px; top: 20px; width: 31px; font-size: 16px; font-family: n; line-height: 1; color: $ink; background: $lite; border-radius: 99px; padding: 8px 0px; text-align: center; in: {scale:0.4, opacity:0, duration:.45, ease:'back.out(2.2)'}; content: {no})
  p#t(left: 63px; cy: 36px; font-size: 19px; font-family: sb; color: $t2; content: {t})

# 01 title — 3 本の波形が左から描かれて流れ、題が mask から 2 行で上がり、副題と 3 つのモデルの札・読む語で Flash / Lite が光る
section#title(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.34, ease:'power1.inOut'})
group#wave(left: 0px; top: 0px; width: 1280px; height: 720px; main: keys(at=0 x=0 | at=1 x=-40 ease=none),window=0,4700,forwards)
  shape#w31(path: "M0 587 L8 587 L16 587 L24 588 L32 588 L40 588 L48 589 L56 589 L64 590 L72 590 L80 590 L88 591 L96 591 L104 591 L112 592 L120 592 L128 592 L136 593 L144 593 L152 594 L160 594 L168 594 L176 594 L184 595 L192 594 L200 594 L208 594 L216 593 L224 592 L232 591 L240 591 L248 590 L256 590 L264 590 L272 590 L280 591 L288 591 L296 593 L304 594 L312 595 L320 596 L328 597 L336 598 L344 598 L352 598 L360 597 L368 596 L376 594 L384 592 L392 590 L400 588 L408 586 L416 584 L424 582 L432 581 L440 579 L448 578 L456 576 L464 575 L472 573 L480 571 L488 568 L496 566 L504 562 L512 559 L520 555 L528 552 L536 548 L544 546 L552 543 L560 542 L568 541 L576 542 L584 543 L592 545 L600 548 L608 551 L616 554 L624 558 L632 561 L640 565 L648 567 L656 570 L664 572 L672 574 L680 576 L688 577 L696 579 L704 580 L712 582 L720 584 L728 587 L736 589 L744 592 L752 595 L760 597 L768 599 L776 601 L784 602 L792 603 L800 602 L808 602 L816 600 L824 599 L832 597 L840 595 L848 594 L856 593 L864 592 L872 592 L880 592 L888 593 L896 594 L904 595 L912 597 L920 598 L928 600 L936 601 L944 602 L952 602 L960 603 L968 603 L976 603 L984 602 L992 602 L1000 601 L1008 601 L1016 601 L1024 601 L1032 601 L1040 601 L1048 601 L1056 601 L1064 600 L1072 600 L1080 599 L1088 598 L1096 597 L1104 596 L1112 595 L1120 593 L1128 592 L1136 590 L1144 589 L1152 588 L1160 587 L1168 586 L1176 586 L1184 585 L1192 585 L1200 585 L1208 585 L1216 585 L1224 586 L1232 586 L1240 586 L1248 586 L1256 587 L1264 587 L1272 587 L1280 587"; background: none; border: 1.7px solid #8B96A8; opacity: .45; delay: 100; in: draw,2600,power2.out)
  shape#wf(path: "M0 587 L8 587 L16 588 L24 588 L32 588 L40 589 L48 589 L56 589 L64 588 L72 588 L80 588 L88 588 L96 588 L104 588 L112 588 L120 589 L128 589 L136 589 L144 589 L152 589 L160 588 L168 588 L176 587 L184 586 L192 586 L200 586 L208 586 L216 586 L224 586 L232 586 L240 585 L248 584 L256 581 L264 578 L272 574 L280 569 L288 564 L296 559 L304 555 L312 551 L320 549 L328 548 L336 547 L344 548 L352 548 L360 550 L368 551 L376 551 L384 552 L392 553 L400 554 L408 556 L416 559 L424 564 L432 569 L440 576 L448 584 L456 591 L464 599 L472 606 L480 611 L488 615 L496 616 L504 617 L512 616 L520 614 L528 612 L536 610 L544 609 L552 609 L560 610 L568 612 L576 614 L584 615 L592 616 L600 617 L608 616 L616 615 L624 613 L632 611 L640 610 L648 610 L656 611 L664 614 L672 617 L680 622 L688 627 L696 631 L704 634 L712 636 L720 636 L728 633 L736 629 L744 624 L752 617 L760 611 L768 604 L776 599 L784 594 L792 589 L800 585 L808 582 L816 578 L824 573 L832 568 L840 563 L848 557 L856 552 L864 547 L872 543 L880 540 L888 539 L896 540 L904 543 L912 546 L920 551 L928 556 L936 560 L944 564 L952 567 L960 570 L968 571 L976 572 L984 573 L992 574 L1000 575 L1008 576 L1016 578 L1024 580 L1032 582 L1040 584 L1048 585 L1056 586 L1064 586 L1072 586 L1080 585 L1088 584 L1096 583 L1104 583 L1112 583 L1120 583 L1128 584 L1136 585 L1144 587 L1152 588 L1160 589 L1168 590 L1176 591 L1184 591 L1192 591 L1200 591 L1208 591 L1216 590 L1224 590 L1232 589 L1240 589 L1248 589 L1256 588 L1264 588 L1272 587 L1280 587"; background: none; border: 2px solid $flash; opacity: .55; delay: 300; in: draw,2600,power2.out)
  shape#wl(path: "M0 587 L8 587 L16 587 L24 587 L32 587 L40 586 L48 586 L56 586 L64 585 L72 586 L80 586 L88 586 L96 586 L104 586 L112 585 L120 583 L128 581 L136 578 L144 576 L152 573 L160 571 L168 570 L176 569 L184 567 L192 566 L200 564 L208 561 L216 559 L224 558 L232 558 L240 561 L248 565 L256 572 L264 579 L272 588 L280 595 L288 602 L296 606 L304 610 L312 612 L320 614 L328 616 L336 619 L344 622 L352 626 L360 628 L368 630 L376 629 L384 625 L392 620 L400 614 L408 609 L416 605 L424 604 L432 606 L440 611 L448 617 L456 623 L464 627 L472 629 L480 629 L488 626 L496 622 L504 617 L512 613 L520 610 L528 608 L536 605 L544 601 L552 595 L560 585 L568 572 L576 557 L584 541 L592 527 L600 515 L608 507 L616 503 L624 504 L632 508 L640 513 L648 518 L656 522 L664 526 L672 528 L680 532 L688 537 L696 544 L704 553 L712 565 L720 576 L728 587 L736 594 L744 598 L752 599 L760 596 L768 591 L776 587 L784 584 L792 583 L800 586 L808 590 L816 596 L824 602 L832 607 L840 610 L848 612 L856 614 L864 615 L872 618 L880 622 L888 627 L896 634 L904 640 L912 645 L920 647 L928 647 L936 642 L944 636 L952 627 L960 618 L968 610 L976 603 L984 597 L992 593 L1000 589 L1008 585 L1016 581 L1024 577 L1032 572 L1040 568 L1048 565 L1056 564 L1064 564 L1072 565 L1080 568 L1088 572 L1096 575 L1104 578 L1112 579 L1120 580 L1128 580 L1136 579 L1144 579 L1152 579 L1160 579 L1168 580 L1176 581 L1184 582 L1192 583 L1200 583 L1208 584 L1216 584 L1224 584 L1232 585 L1240 585 L1248 586 L1256 586 L1264 587 L1272 587 L1280 587"; background: none; border: 2.3px solid $lite; opacity: .85; delay: 500; in: draw,2600,power2.out)
div#t_bar(left: 80px; top: 136px; width: 29px; height: 1.3px; background: $lite; delay: 100; in: {scaleX:0, pivot:'left', duration:.6, ease:'power3.out'})
p#t_kick(left: 120px; top: 127px; font-size: 15px; font-family: r; color: $t2; letter-spacing: .08em; delay: 200; in: {opacity:0, duration:.6, ease:'power1.out'}) 社内共有 ｜ ナレーション音声 (TTS) の乗り換え検討
p#t_l1(left: 75px; top: 157px; font-size: 61px; line-height: 1.18; letter-spacing: .01em; delay: 300; in: mask_rise,1000,ease=power4.out) 音声合成の乗り換え、
p#t_flash(left: 75px; top: 229px; font-size: 92px; line-height: 1.16; color: $flash; delay: 420; in: mask_rise,1000,ease=power4.out) Flash
p#t_ka1(left: 330px; top: 251px; font-size: 69px; line-height: 1.16; color: $t2; delay: 420; in: mask_rise,1000,ease=power4.out) か
p#t_lite(left: 410px; top: 229px; font-size: 92px; line-height: 1.16; color: $lite; delay: 420; in: mask_rise,1000,ease=power4.out) Lite
p#t_ka2(left: 592px; top: 251px; font-size: 69px; line-height: 1.16; color: $t2; delay: 420; in: mask_rise,1000,ease=power4.out) か
p#t_sub(left: 80px; top: 393px; font-size: 20px; font-family: r; color: $t2; delay: 1250; in: fup) Gemini TTS ── 現行の 3.1 Flash preview から、どこへ乗り換えるか
# モデルの札 3 枚 (色の四角 + 名 + 現行 / 新)
p#t_c1(left: 80px; top: 435px; font-size: 17px; font-family: sb; background: #FFFFFF0D; border: 1px solid #FFFFFF2E; border-radius: 9px; padding: 11px 16px 11px 33px; delay: 1550; in: {y:11, opacity:0, duration:.55, ease:'power3.out'}) 3.1 Flash preview  {s}現行{/}
  div#sw(left: 12px; cy: 50%; width: 13px; height: 13px; border-radius: 3px; background: $c31f; border: 1px solid #FFFFFF40; overlap: t_c1)
p#t_c2(left: 322px; top: 435px; font-size: 17px; font-family: sb; background: #FFFFFF0D; border: 1px solid #FFFFFF2E; border-radius: 9px; padding: 11px 16px 11px 33px; delay: 1670; in: {y:11, opacity:0, duration:.55, ease:'power3.out'}) 3.8 Flash  {s}新{/}
  div#sw(left: 12px; cy: 50%; width: 13px; height: 13px; border-radius: 3px; background: $flash; overlap: t_c2)
p#t_c3(left: 482px; top: 435px; font-size: 17px; font-family: sb; background: #FFFFFF0D; border: 1px solid #FFFFFF2E; border-radius: 9px; padding: 11px 16px 11px 33px; delay: 1790; in: {y:11, opacity:0, duration:.55, ease:'power3.out'}) 3.8 Flash-Lite  {s}新{/}
  div#sw(left: 12px; cy: 50%; width: 13px; height: 13px; border-radius: 3px; background: $lite; overlap: t_c3)

# 02 背景 — 現行の板 ($923 は「月額」で上がる) → 2 本の曲線の矢印が描かれ候補の板 2 枚 → 比べる軸 (破線の枠と 2 つの札)
section#bg(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h2(n: "01"; k: "背景"; h: "乗り換え先を、コストと品質で決める")
# 下端の章の進行 (9 本・全編に残る sticky)。章ごとに帯が伸び、今の章の名が白くなる
div#prog.sticky(left: 59px; top: 676px; width: 1163px; height: 26px; delay: 200; in: {y:7, opacity:0, duration:.6, ease:'power2.out'})
  p#lab(left: "0;130;260;390;520;650;780;910;1040"; top: 0px; font-size: 12px; font-family: r; color: $lab; letter-spacing: .06em) ×9 背景;単価;実測;月額;品質;声色;使い方;再合成;結論
  div#track(left: "0;130;260;390;520;650;780;910;1040"; top: 21px; width: 123px; height: 3px; border-radius: 2px; background: #FFFFFF1A) ×9
progress#pf1(left: 59px; top: 697px; width: 123px; height: 3px; background: $t2; until: cut)
board#cur(left: 59px; top: 167px; width: 507px; height: 427px; t: "現行"; s: "ナレーション音声 (TTS)"; rw: 461px; delay: 300)
  p#tag(right: 23px; top: 20px; font-size: 12px; font-family: m; letter-spacing: .08em; color: $c31; background: #FFFFFF14; border-radius: 5px; padding: 4px 8px) NOW
  p#model(left: 23px; top: 74px; font-size: 29px; font-family: i; letter-spacing: -.01em) Gemini 3.1 Flash preview
  p#msub(left: 23px; top: 114px; font-size: 16px; font-family: r; color: $t3) 動画生成サービスのナレーションに使用中
  p#ml(left: 23px; top: 163px; font-size: 17px; font-family: r; color: $t2) 月額
  p#big(left: 23px; top: 203px; font-size: 112px; font-family: n; line-height: 1.1; in: {y:17, opacity:0, duration:.6, ease:'power3.out'}) $923
  p#per(left: .big.right+7; top: 261px; font-size: 43px; color: $t3; in: {y:17, opacity:0, duration:.6, ease:'power3.out'}) / 月
  div#fl(left: 23px; top: 372px; width: 461px; height: 1px; background: #FFFFFF14; in: fups)
  p#fk(left: 23px; top: 385px; font-size: 15px; font-family: r; color: $t3; in: fups) 単価 (100 万 token あたり)
  p#fv(right: 23px; top: 381px; font-size: 16px; font-family: r; color: $t2; in: fups) 入力 {d}$1{/} ・ 出力 {d}$20{/}
# 現行 → 候補 2 枚への曲線の矢印 (描かれてから頭が弾む)
shape#a2a(path: "M578 380 C633 380 653 235 724 235"; background: none; border: 2px solid $t3; in: draw,700,power2.inOut)
shape#a2b(path: "M578 380 C633 380 653 393 724 393"; background: none; border: 2px solid $t3; in: draw,700,power2.inOut)
shape#a2h1(points: "736,235 722,228 722,243"; background: $t3; in: bpop)
shape#a2h2(points: "736,393 722,386 722,400"; background: $t3; in: bpop)
p#s02q(left: 581px; top: 399px; width: 147px; font-size: 16px; font-family: sb; color: $t2; text-align: center; in: fups) 乗り換え候補
cand#cf(left: 747px; top: 167px; m: "Gemini 3.8 Flash"; d: "売りは 多話者・タグ・方言"; c: $flash; bd: #4DA3FF73)
cand#cl(left: 747px; top: 324px; m: "Gemini 3.8 Flash-Lite"; d: "出力単価が 3 モデルで最安"; c: $lite; bd: #2FDCAA73)
# 比べる軸 (破線の枠 + 灰の札 2 つ)
shape#axes(left: 747px; top: 487px; width: 475px; height: 107px; path: rect,r=0.14; background: none; border: 1px solid #FFFFFF2E; dash: 4,4; in: fin)
p#axl(left: 770px; cy: 540px; font-size: 16px; font-family: r; color: $t3; in: fin) 比べる軸
p#ax1(left: 852px; cy: 540px; font-size: 20px; font-family: sb; color: $t2; background: #FFFFFF0F; border: 1px solid #FFFFFF2E; border-radius: 99px; padding: 10px 20px; in: bpop) コスト
p#ax2(left: ax1.right+15; cy: 540px; font-size: 20px; font-family: sb; color: $t2; background: #FFFFFF0F; border: 1px solid #FFFFFF2E; border-radius: 99px; padding: 10px 20px; in: bpop) 品質
note#n2 対象: 動画生成サービスのナレーション音声 (TTS)。金額はすべて USD。

# 03 単価 — 出力単価の横棒 3 本 ($1 = 25 px) が語ごとに伸び、「2027年」で倍額の破線の枠が右へ払われ「倍額」で札
section#price(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h3(n: "02"; k: "単価"; h: "出力単価は {d}$20{/} から {fd}$9{/} ・ {ld}$6{/} へ")
legend#lg3
div#pd1.sticky(left: 59px; top: 697px; width: 123px; height: 3px; background: $t2; in: none)
progress#pf2(left: 189px; top: 697px; width: 123px; height: 3px; background: $t2; until: cut)
board#b3(left: 59px; top: 163px; width: 1163px; height: 453px; t: "単価"; s: "100 万 token あたり"; rw: 1117px; delay: 250)
  p#x2(right: 23px; top: 15px; font-size: 15px; font-family: sb; color: $amber; background: #FFB5471F; border: 1px solid #FFB54780; border-radius: 99px; padding: 6px 12px; in: {scale:0.7, opacity:0, duration:.45, ease:'back.out(2.2)'}) 2027 年 1 月から ×2 (倍額)
  p#ch(left: "23;290;457"; top: 72px; font-size: 15px; font-family: r; color: $t3) ×3 モデル;入力;出力
  div#sep(left: 23px; top: "205;309"; width: 1117px; height: 1px; background: #FFFFFF0F) ×2
  div#lab(left: 23px; top: "128;232;336"; width: 260px; height: 50px; delay: 300; in: {y:8, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.1}}) ×3
    div#sw(left: 0px; top: 7px; width: 12px; height: 12px; border-radius: 3px; background: "$c31f;$flash;$lite")
    p#m(left: 20px; top: 0px; font-size: 19px; font-family: sb) 3.1 Flash preview;3.8 Flash;3.8 Flash-Lite
    p#s(left: 20px; top: 31px; font-size: 13px; font-family: r; color: $t3) 現行;2026 年末まで導入価格;2026 年末まで導入価格
  p#iv(left: 290px; cy: "153;257;361"; font-size: 27px; font-family: i; delay: 450; in: {y:8, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.1}}) ×3 $1;$0.5;$0.5
  p#n27(left: 352px; cy: "260;364"; font-size: 17px; font-family: i; color: $amber; in: {scale:0.6, opacity:0, duration:.45, ease:'back.out(2.2)', stagger:{each:.15}}) ×2 → $1
  shape#g(left: "685;609"; top: "237;341"; width: "228;152"; height: 40px; path: rect,r=0.15; background: #FFB54712; border: 1.3px solid $amber; dash: 4,3; in: wipe,right,750,ease=power2.inOut) ×2
  div#f(left: 457px; top: "137;241;345"; width: "507;228;152"; height: 32px; border-radius: 5px; background: "linear($g31,#5F687B,90);linear($gf,#4DA3FF,90);linear($gl,#2FDCAA,90)"; in: {scaleX:0, pivot:'left', duration:.85, ease:'power3.out'}) ×3
  p#hv(right: "208;487;563"; cy: "153;257;361"; font-size: 21px; font-family: i; color: "$t1;$ink;$ink"; in: {opacity:0, duration:.3}) ×3 $20;$9;$6
  p#gv(left: "925;773"; cy: "257;361"; font-size: 21px; font-family: i; color: $amber; in: {x:-8, opacity:0, duration:.55, ease:'power3.out'}) ×2 $18;$12
  p#gd(left: "970;818"; cy: "258;362"; font-size: 13px; font-family: r; color: $amber; opacity: .85; in: {x:-8, opacity:0, duration:.55, ease:'power3.out'}) ×2 2027 年 1 月〜
note#n3 ※ 3.8 系は 2026 年末までの導入価格。2027 年 1 月に倍額 (Flash {b}$1 / $18{/}、Lite {b}$1 / $12{/})。

# 04 実測 — 3 つの数字が語ごとに上がる板 → token の箱 32 個が左から並び、「公式の目安」で 25 の線と超えた 7 個が琥珀に (琥珀の箱 ×7 を同じ所に重ねて出す)
section#measure(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h4(n: "03"; k: "実測"; h: "見積もりの土台は、4 日間の実測ログ")
div#pd2.sticky(left: 189px; top: 697px; width: 123px; height: 3px; background: $t2; in: none)
progress#pf3(left: 319px; top: 697px; width: 123px; height: 3px; background: $t2; until: cut)
board#b4a(left: 59px; top: 163px; width: 1163px; height: 220px; t: "実測"; s: "4 日間のログ"; rw: 1117px; delay: 250)
  div#st(left: "-2;378;760"; top: 70px; width: 369px; height: 120px; in: {y:9, opacity:0, duration:.55, ease:'power3.out'}) ×3
    div#bl(left: 0px; top: 0px; width: 1px; height: 120px; background: #FFFFFF14; opacity: "0;1;1")
    p#k(left: 29px; top: 7px; font-size: 16px; font-family: r; color: $t2) 合成の回数;文字数;音声の長さ
    p#v(left: 29px; top: 33px; font-size: 72px; font-family: n; line-height: 1) 25,432;104;53.9
    p#u(left: .v.right+8; top: 72px; font-size: 25px; font-family: sb; color: $t2) 回;万文字;時間
board#b4b(left: 59px; top: 403px; width: 1163px; height: 213px; t: "音声 1 秒あたりの token"; s: "実測 vs 公式の目安"; rw: 1117px)
  p#lead(left: 23px; top: 75px; font-size: 72px; font-family: n; line-height: 1; in: fup) 32
  p#lu(left: 23px; top: 153px; font-size: 16px; font-family: r; color: $t2; in: fup) token / 秒 (実測)
  div#blk(left: "243;271;299;327;355;383;411;439;467;495;523;551;579;607;635;663;691;719;747;775;803;831;859;887;915"; top: 104px; width: 23px; height: 39px; border-radius: 4px; background: #EEF2F8D1; in: {scaleY:0.3, opacity:0, pivot:'bottom', duration:.3, ease:'power2.out', stagger:{each:0.033}}) ×25
  div#bo(left: "943;971;999;1027;1055;1083;1111"; top: 104px; width: 23px; height: 39px; border-radius: 4px; background: #EEF2F8D1; in: {scaleY:0.3, opacity:0, pivot:'bottom', duration:.3, ease:'power2.out', stagger:{each:0.033}}) ×7
  div#ba(left: "943;971;999;1027;1055;1083;1111"; top: 104px; width: 23px; height: 39px; border-radius: 4px; background: $amber; in: {opacity:0, duration:.25, stagger:{each:0.04}}) ×7
  div#mk(left: 940px; top: 81px; width: 2px; height: 85px; background: $ref; in: {scaleY:0, opacity:0, pivot:'bottom', duration:.45, ease:'power3.out'})
  p#ml(left: 948px; top: 75px; font-size: 15px; font-family: sb; color: $ref; in: {opacity:0, duration:.45}) 公式の目安 25
  p#ol(left: 947px; top: 152px; font-size: 15px; font-family: sb; color: $amber; in: fups) 目安を超える分
note#n4 ※ 音声は 1 秒あたり 32 token (公式の目安は 25)。

# 05 月額 — 目盛りと参考の破線 2 本 (Fish / ElevenLabs) の上で 3 本の横棒 ($1 = 0.77 px)・「2027年」で凡例が弾み、倍額後の破線の枠が語ごとに払われる
section#monthly(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h5(n: "04"; k: "月額"; h: "月額は {d}$923{/} から {fd}$416{/} ・ {ld}$278{/} へ")
legend#lg5
div#pd3.sticky(left: 319px; top: 697px; width: 123px; height: 3px; background: $t2; in: none)
progress#pf4(left: 449px; top: 697px; width: 123px; height: 3px; background: $t2; until: cut)
board#b5(left: 59px; top: 163px; width: 1163px; height: 453px; t: "月額の見込み"; s: "USD / 月"; rw: 1117px; delay: 250)
  div#gleg(left: 827px; top: 17px; width: 313px; height: 20px; delay: 600; in: fin)
    shape#s1(left: 0px; cy: 50%; width: 12px; height: 12px; path: rect,r=0.25; background: none; border: 1.3px solid $amber; dash: 3,2)
    p#t1(left: 19px; cy: 50%; font-size: 15px; font-family: r; color: $t2) 2027 年 1 月〜 (倍額後)
    div#s2(left: 175px; cy: 50%; width: 2px; height: 15px; background: $ref)
    p#t2(left: 185px; cy: 50%; font-size: 15px; font-family: r; color: $t2) 参考: 他社の月額
  div#gv(left: "263;416;570;723;877;1030"; top: 77px; width: 1px; height: 313px; background: #FFFFFF12; delay: 400; in: {opacity:0, duration:.5}) ×6
  p#gt(left: "238;391;545;698;852;1005"; top: 397px; width: 50px; font-size: 13px; font-family: i; color: $t3; text-align: center; delay: 400; in: {opacity:0, duration:.5}) ×6 $0;$200;$400;$600;$800;$1000
  div#lab(left: 23px; top: "116;210;304"; width: 230px; height: 50px; delay: 300; in: {y:8, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.1}}) ×3
    div#sw(left: 0px; top: 7px; width: 12px; height: 12px; border-radius: 3px; background: "$c31f;$flash;$lite")
    p#m(left: 20px; top: 0px; font-size: 19px; font-family: sb) 3.1 Flash preview;3.8 Flash;3.8 Flash-Lite
    p#s(left: 20px; top: 31px; font-size: 13px; font-family: r; color: $t3) 現行;導入価格;導入価格
  shape#rf(left: "287;711"; top: 85px; width: 2px; height: 305px; path: line_v; border: 1.3px solid $ref; dash: 7,5; in: draw,800,power2.out) ×2
  p#rt(left: "294;718"; top: 63px; font-size: 14px; font-family: sb; color: $ref; in: {opacity:0, duration:.5}) ×2 参考 Fish $32;参考 ElevenLabs v3 定価 $584
  shape#g(left: "582;476"; top: "215;309"; width: "318;213"; height: 40px; path: rect,r=0.15; background: #FFB54712; border: 1.3px solid $amber; dash: 4,3; in: wipe,right,800,ease=power2.inOut) ×2
  div#f(left: 263px; top: "125;219;313"; width: "708;319;213"; height: 32px; border-radius: 5px; background: "linear($g31,#5F687B,90);linear($gf,#4DA3FF,90);linear($gl,#2FDCAA,90)"; in: {scaleX:0, pivot:'left', duration:.9, ease:'power3.out'}) ×3
  p#hv(right: "201;590;696"; cy: "141;235;329"; font-size: 21px; font-family: i; color: "$t1;$ink;$ink"; in: {opacity:0, duration:.3}) ×3 $923;$416;$278
  p#gl(right: "274;485"; cy: "235;329"; font-size: 21px; font-family: i; color: $amber; in: {opacity:0, duration:.3}) ×2 $831;$556
  p#gd(right: "331;542"; cy: "236;330"; font-size: 13px; font-family: r; color: $amber; opacity: .8; in: {opacity:0, duration:.3}) ×2 2027 年〜
note#n5 ※ 見込み額。2027 年からは Flash {b}$831{/}、Lite {b}$556{/}。参考: ElevenLabs v3 定価 {b}$584{/}、Fish {b}$32{/}。

# 06 品質 — 左の板: 一致率の縦棒 3 本が並んで伸び「同じ水準」の札・雑音 0 件にチェック / 右の板: 遅延の横棒・「ライト」で最速の札と光・長文の最大の横棒
section#quality(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h6(n: "05"; k: "品質"; h: "品質は同じ。速度は {l}Lite{/} が最速")
legend#lg6
div#pd4.sticky(left: 449px; top: 697px; width: 123px; height: 3px; background: $t2; in: none)
progress#pf5(left: 579px; top: 697px; width: 123px; height: 3px; background: $t2; until: cut)
board#b6a(left: 59px; top: 163px; width: 533px; height: 453px; t: "読み取り一致率"; s: "本番テキスト 80 本"; rw: 487px; delay: 250)
  p#eq(right: 23px; top: 15px; font-size: 15px; font-family: sb; color: $lite; background: #2FDCAA1F; border: 1px solid #2FDCAA80; border-radius: 99px; padding: 6px 12px; in: {scale:0.7, opacity:0, duration:.45, ease:'back.out(2.2)'}) 3 モデルで同じ水準
  div#base(left: 36px; top: 283px; width: 461px; height: 1px; background: #FFFFFF2E)
  div#ab(left: "67;223;377"; top: "129;130;130"; width: 87px; height: "154;153;153"; border-radius: 7px 7px 3px 3px; background: "linear($g31,#5F687B,0);linear($gf,#4DA3FF,0);linear($gl,#2FDCAA,0)"; in: {scaleY:0, pivot:'bottom', duration:.9, ease:'power3.out', stagger:{each:.12}}) ×3
  p#av(cx: "110;266;420"; cy: 107px; font-size: 27px; font-family: i; color: "$t1;$flash;$lite"; in: {y:5, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.12}}) ×3 0.856;0.850;0.851
  p#xl(cx: "110;266;420"; cy: 303px; font-size: 15px; font-family: sb; color: $t2; delay: 400; in: fin) ×3 3.1 Flash pre.;3.8 Flash;3.8 Flash-Lite
  div#nl(left: 23px; top: 372px; width: 487px; height: 1px; background: #FFFFFF14)
  p#nk(left: 23px; top: 383px; font-size: 15px; font-family: sb; color: $t2; in: fin) 雑音の検出
  div#z(left: "77;233;387"; top: 409px; width: 70px; height: 27px; in: {scale:0.7, opacity:0, duration:.45, ease:'back.out(2.2)', stagger:{each:.12}}) ×3
    chk#ck(left: 0px; top: 0px)
    p#v(left: 34px; cy: 50%; font-size: 23px; font-family: i) 0
    p#u(left: 52px; cy: 50%; font-size: 15px; font-family: r; color: $t2) 件
board#b6b(left: 612px; top: 163px; width: 609px; height: 453px; t: "遅延"; s: "中央値 (秒) ・ 短いほど速い"; rw: 563px; delay: 370)
  div#ll(left: 23px; top: "95;157;217"; width: 160px; height: 20px; delay: 400; in: fin) ×3
    div#sw(left: 0px; cy: 50%; width: 12px; height: 12px; border-radius: 3px; background: "$c31f;$flash;$lite")
    p#m(left: 20px; cy: 50%; font-size: 17px; font-family: sb) 3.1 Flash pre.;3.8 Flash;3.8 Flash-Lite
  div#lb(left: 190px; top: "90;152;212"; width: "279;204;177"; height: 29px; border-radius: 5px; background: "linear($g31,#5F687B,90);linear($gf,#4DA3FF,90);linear($gl,#2FDCAA,90)"; in: {scaleX:0, pivot:'left', duration:.9, ease:'power3.out', stagger:{each:.12}}) ×3
  p#lv(left: "478;403;376"; cy: "105;167;227"; font-size: 20px; font-family: i; color: "$t1;$flash;$lite"; in: {opacity:0, duration:.3, stagger:{each:.12}}) ×3 4.55 秒;3.32 秒;2.89 秒
  p#fast(left: 470px; cy: 227px; font-size: 15px; font-family: sb; color: $lite; background: #2FDCAA1F; border: 1px solid #2FDCAA80; border-radius: 99px; padding: 6px 12px; in: {scale:0.5, opacity:0, duration:.45, ease:'back.out(2.2)'}) 最速
  div#sl(left: 23px; top: 280px; width: 563px; height: 1px; background: #FFFFFF14)
  p#sh(left: 23px; top: 291px; font-size: 15px; font-family: sb; color: $t2; in: fin) 長文 (60 字以上) の最大
  div#xl(left: 23px; top: "331;367;403"; width: 160px; height: 20px; in: {opacity:0, duration:.3, stagger:{each:.1}}) ×3
    div#sw(left: 0px; cy: 50%; width: 12px; height: 12px; border-radius: 3px; background: "$c31f;$flash;$lite")
    p#m(left: 20px; cy: 50%; font-size: 17px; font-family: sb) 3.1 Flash pre.;3.8 Flash;3.8 Flash-Lite
  div#xb(left: 190px; top: "333;369;405"; width: "293;158;119"; height: 16px; border-radius: 4px; background: "linear($g31,#5F687B,90);linear($gf,#4DA3FF,90);linear($gl,#2FDCAA,90)"; in: {scaleX:0, pivot:'left', duration:.8, ease:'power3.out', stagger:{each:.1}}) ×3
  p#xv(left: "492;357;318"; cy: "341;377;413"; font-size: 16px; font-family: i; color: "$t1;$flash;$lite"; in: {opacity:0, duration:.3, stagger:{each:.1}}) ×3 17.2 秒;9.3 秒;7.0 秒
note#n6 ※ 品質ベンチ: 本番のテキスト 80 本を 3 モデルで合成。長文 (60 字以上) の遅延の最大は {b}17.2 / 9.3 / 7.0 秒{/}。

# 07 声色 — 点の数直線: 「0.885」で青緑の点が左から滑り込み、「同じ声」で灰の点 0.81 と差の括弧・チェック → 30 の点の格子 → 注意の板 (声の高さが段で下がる線)
section#voice(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h7(n: "06"; k: "声色"; h: "{f}Flash{/} と {l}Lite{/} は、同じ声として扱える")
div#pd5.sticky(left: 579px; top: 697px; width: 123px; height: 3px; background: $t2; in: none)
progress#pf6(left: 709px; top: 697px; width: 123px; height: 3px; background: $t2; until: cut)
board#b7a(left: 59px; top: 163px; width: 667px; height: 453px; t: "声の類似度"; s: "同じ声・同じ文で比較"; rw: 621px; delay: 250)
  div#vc(left: "155;381"; top: 74px; width: "148;132"; height: 51px; border-radius: 11px; border: 1px solid #FFFFFF2E; background: #FFFFFF0A; delay: 300; in: {scale:0.8, opacity:0, duration:.45, ease:'back.out(2.2)', stagger:{each:.12}}) ×2
    shape#w(left: 18px; cy: 50%; width: 44px; height: 11px; path: "wave,n=3"; background: none; border: "$flash,2;$lite,2")
    p#t(left: 73px; cy: 50%; font-size: 21px; font-family: i; color: "$flash;$lite") Flash;Lite
  p#eqs(left: 324px; cy: 99px; font-size: 29px; font-family: i; color: $t3; delay: 500; in: fin) ↔
  div#ax(left: 50px; top: 254px; width: 567px; height: 3px; border-radius: 2px; background: #FFFFFF24; delay: 500; in: fin)
  div#tm(left: "49;238;427;616"; top: 262px; width: 1px; height: 7px; background: #FFFFFF40; delay: 500; in: fin) ×4
  p#tk(left: "30;219;408;597"; top: 274px; width: 40px; font-size: 13px; font-family: i; color: $t3; text-align: center; delay: 500; in: fin) ×4 0.70;0.80;0.90;1.00
  div#mg(left: 188px; top: 160px; width: 140px; height: 110px)
    p#v(cx: 50%; top: 4px; font-size: 29px; font-family: n; line-height: 1; in: {y:7, opacity:0, duration:.55, ease:'power3.out'}; delay: 150) 0.81
    p#k(cx: 50%; top: 35px; font-size: 13px; font-family: r; color: $t2; in: {y:7, opacity:0, duration:.55, ease:'power3.out'}; delay: 150) 別テキストの揺れ
    div#stem(cx: 50%; top: 64px; width: 1.3px; height: 23px; background: #8B96A8; delay: 50; in: {scaleY:0, pivot:'bottom', duration:.4, ease:'power2.out'})
    div#dot(cx: 50%; top: 85px; width: 20px; height: 20px; border-radius: 10px; background: #8B96A8; in: {scale:0.2, opacity:0, duration:.45, ease:'back.out(2.2)'})
  div#mt(left: 330px; top: 160px; width: 140px; height: 110px; in: {x:-120, duration:.9, ease:'power3.out'})
    p#v(cx: 50%; top: 4px; font-size: 29px; font-family: n; line-height: 1; color: $lite; in: {y:7, opacity:0, duration:.55, ease:'power3.out'}; delay: 150) 0.885
    p#k(cx: 50%; top: 35px; font-size: 13px; font-family: r; color: $t2; in: {y:7, opacity:0, duration:.55, ease:'power3.out'}; delay: 150) Flash {d}↔{/} Lite
    div#stem(cx: 50%; top: 64px; width: 1.3px; height: 23px; background: $lite; delay: 50; in: {scaleY:0, pivot:'bottom', duration:.4, ease:'power2.out'})
    div#dot(cx: 50%; top: 85px; width: 20px; height: 20px; border-radius: 10px; background: $lite; box-shadow: 0px 0px 0px 5px #2FDCAA2E; in: {scale:0.2, opacity:0, duration:.45, ease:'back.out(2.2)'})
  p#gs(cx: 329px; top: 307px; font-size: 15px; font-family: sb; color: $lite; in: fups) 揺れ (0.81) より近い
  div#same(left: 23px; top: 393px; width: 621px; height: 50px; in: fups)
    div#ln(left: 0px; top: 0px; width: 621px; height: 1px; background: #FFFFFF14)
    chk#ck(left: 0px; top: 12px)
    p#t(left: 38px; cy: 25px; font-size: 20px) 同じ声として扱える
# 差の括弧 (0.81 から 0.885 まで・描かれる)
shape#gap(path: "M318 456 L318 465 L458 465 L458 456"; background: none; border: 1.7px solid $lite; in: draw,550,power2.out)
board#b7b(left: 745px; top: 163px; width: 476px; height: 211px; t: "話者の対応"; s: "本番 {d}↔{/} 3.8 組み込み"; rw: 430px)
  div#d30(left: "84;116;148;180;212;244;276;308;340;372;84;116;148;180;212;244;276;308;340;372;84;116;148;180;212;244;276;308;340;372"; top: "75;75;75;75;75;75;75;75;75;75;104;104;104;104;104;104;104;104;104;104;133;133;133;133;133;133;133;133;133;133"; width: 20px; height: 20px; border-radius: 10px; background: $lite; box-shadow: 0px 0px 0px 3px #2FDCAA24; in: {scale:0.2, opacity:0, duration:.35, ease:'back.out(2.2)', stagger:{each:0.022}}) ×30
  p#m30(left: 23px; top: 166px; width: 430px; font-size: 16px; font-family: r; color: $t2; text-align: center; in: fups) 本番の話者 {w}30 人{/} は、3.8 の組み込み {w}30 声{/} と一致
# 注意の板 (琥珀の縁と地): 3.1 の線から段で下がる 3.8 の線 + 0.71〜0.76 倍
box#b7c(left: 745px; top: 393px; width: 476px; height: 223px; t: "注意 ── 男声の低音化"; rw: 430px; border: 1px solid #FFB5478C; background: linear(#FFB5471A,#FFB54708,180))
  p#t(color: $amber)
  p#p31(left: 34px; top: 63px; font-size: 12px; font-family: i; color: $c31; in: fin) 3.1
  p#p38(left: 112px; top: 125px; font-size: 12px; font-family: i; color: $amber; in: fin) 3.8
  p#wv(left: 209px; top: 73px; font-size: 35px; font-family: n; line-height: 1.05; color: $amber; in: fups) 0.71〜0.76{s}倍{/}
  p#wk(left: 209px; top: 116px; width: 200px; font-size: 16px; font-family: r; line-height: 1.45; color: $t2; in: fups) 3.8 で基本周波数が下がる男声がある
shape#pl1(path: "M779 478 L846 478"; background: none; border: 2.2px solid #8B96A8; in: draw,500,power2.out)
shape#pdrop(path: "M846 478 C851 478 851 515 857 515"; background: none; border: 1.4px solid $amber; in: draw,450,power2.in)
shape#plow(path: "M857 515 L924 515"; background: none; border: 2.2px solid $amber; in: draw,500,power2.out)
note#n7 ※ 類似度: 同じ声・同じ文で Flash と Lite を比較 ({b}0.885{/})。別テキストでの揺れは {b}0.81{/}。

# 08 使い方 — 3 枚の板が語ごとに: 97% のドーナツ (12 時から描かれる弧) / 単一話者の人の形 / Flash の売り 3 行に取り消し線と「未使用」の札
section#usage(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h8(n: "07"; k: "使い方"; h: "{f}Flash{/} の売りは、いまの使い方では使っていない")
div#pd6.sticky(left: 709px; top: 697px; width: 123px; height: 3px; background: $t2; in: none)
progress#pf7(left: 839px; top: 697px; width: 123px; height: 3px; background: $t2; until: cut)
box#b8a(left: 59px; top: 167px; width: 360px; height: 440px; t: "言語"; rw: 314px)
  shape#ring.ellipse(left: 84px; top: 92px; width: 191px; height: 191px; background: none; border: 23px solid #FFFFFF1A)
  p#p97(cx: 179px; top: 159px; font-size: 57px; font-family: n; line-height: 1; in: fups) 97%
  p#ja(cx: 179px; top: 219px; font-size: 16px; font-family: r; color: $t2) 日本語
  p#ft(left: 0px; top: 394px; width: 360px; font-size: 16px; font-family: r; color: $t2; text-align: center; in: fin) ナレーションの {w}97%{/} が日本語
shape#arc97(path: "M238.0 270.0 C284.4 270.0 322.0 307.6 322.0 354.0 C322.0 400.4 284.4 438.0 238.0 438.0 C191.6 438.0 154.0 400.4 154.0 354.0 C154.0 313.7 182.7 279.0 222.3 271.5"; overlap: b8a.p97,b8a.ja; background: none; border: 23px solid $lite; in: draw,1200,power2.inOut)
box#b8b(left: 460px; top: 167px; width: 360px; height: 440px; t: "話者"; rw: 314px)
  svg#pr(left: 130px; top: 111px; width: 100px; height: 153px; part: person; in: {scale:0.7, opacity:0, duration:.45, ease:'back.out(2.2)'})
  p#bw(cx: 180px; cy: 299px; font-size: 37px; in: fups) 単一話者
  p#ft(left: 0px; top: 394px; width: 360px; font-size: 16px; font-family: r; color: $t2; text-align: center; in: fin) 1 本のナレーションを 1 人の声で読む
box#b8c(left: 861px; top: 167px; width: 360px; height: 440px; t: "{f}Flash{/} の売り"; rw: 314px)
  div#fe(left: 23px; top: 97px; width: 314px; height: 220px; display: flex; flex-direction: column; gap: 13px; border-radius: 9px; background: #4DA3FF14; border: 1px solid #4DA3FF59; in: {y:8, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.12}}) ×3
    p#n(left: 17px; cy: 50%; font-size: 23px) 多話者;タグ;方言
    p#un(right: 17px; cy: 50%; font-size: 15px; font-family: sb; color: $t2; border: 1px solid #FFFFFF2E; border-radius: 5px; padding: 3px 8px; in: {scale:0.6, opacity:0, duration:.45, ease:'back.out(2.2)'}) 未使用
  p#ft(left: 0px; top: 394px; width: 360px; font-size: 16px; font-family: r; color: $t2; text-align: center; in: fin) いずれも現在の使い方では使っていない
note#n8 ※ 使い方の実態: 日本語 97%、単一話者。Flash の売り (多話者・タグ・方言) は使っていない。

# 09 再合成 — 使える率の縦棒 3 本 (目盛り 0〜100%) が語ごとに伸びる → 内容ブロック 63 → 4: 63 マスが並び、59 マスが沈んで 4 マスが琥珀に残る
section#retry(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h9(n: "08"; k: "再合成"; h: "失敗テキストも、3.8 なら使える率が上がる")
legend#lg9
div#pd7.sticky(left: 839px; top: 697px; width: 123px; height: 3px; background: $t2; in: none)
progress#pf8(left: 969px; top: 697px; width: 123px; height: 3px; background: $t2; until: cut)
board#b9a(left: 59px; top: 163px; width: 707px; height: 453px; t: "使える率"; s: "失敗テキスト 120 本を再合成"; rw: 661px; delay: 250)
  shape#yg(left: 90px; top: "91;161;231;301;371"; width: 574px; height: 2px; path: line_h; border: 1px solid #FFFFFF17; dash: 4,4; delay: 400; in: {opacity:0, duration:.5}) ×5
  p#yt(left: 35px; width: 40px; cy: "91;161;231;301;371"; font-size: 13px; font-family: i; color: $t3; text-align: right; delay: 400; in: {opacity:0, duration:.5}) ×5 100%;75%;50%;25%;0%
  div#vb(left: "155;325;497"; top: "273;169;192"; width: 107px; height: "98;202;179"; border-radius: 7px 7px 3px 3px; background: "linear($g31,#5F687B,0);linear($gf,#4DA3FF,0);linear($gl,#2FDCAA,0)"; in: {scaleY:0, pivot:'bottom', duration:.9, ease:'power3.out'}) ×3
  p#vv(cx: "208;378;550"; cy: "247;141;165"; font-size: 32px; font-family: i; color: "$t1;$flash;$lite"; in: fups) ×3 35%;72%;64%
  p#xl(cx: "208;378;550"; cy: 389px; font-size: 15px; font-family: sb; color: $t2; delay: 500; in: fin) ×3 3.1 Flash pre.;3.8 Flash;3.8 Flash-Lite
board#b9b(left: 785px; top: 163px; width: 436px; height: 453px; t: "内容ブロック"; s: "内容を理由に合成が止まった本数"; rw: 390px)
  div#from(left: 75px; top: 78px; width: 130px; height: 100px; in: {scale:0.7, opacity:0, duration:.45, ease:'back.out(2.2)'})
    p#n(cx: 50%; top: 0px; font-size: 75px; font-family: n; line-height: 1; color: $from) 63
    p#u(cx: 50%; top: 82px; font-size: 16px; font-family: sb; color: $t2) 本
  div#to(left: 291px; top: 78px; width: 60px; height: 100px; in: {scale:0.6, opacity:0, duration:.45, ease:'back.out(2.2)'})
    p#n(cx: 50%; top: 0px; font-size: 75px; font-family: n; line-height: 1) 4
    p#u(cx: 50%; top: 82px; font-size: 16px; font-family: sb; color: $t2) 本
# 残る 4 マス (hf の KEEP = 先頭 4 つ) は別の ×4 で持ち、沈む 59 マスと分けて動かす
  div#kc(left: "108;133;158;183"; top: "209;209;209;209"; width: 20px; height: 20px; border-radius: 4px; background: #FFB54799; in: {scale:0.4, opacity:0, duration:.25, ease:'power2.out', stagger:{each:0.011}}) ×4
  div#cell(left: "208;233;258;283;308;108;133;158;183;208;233;258;283;308;108;133;158;183;208;233;258;283;308;108;133;158;183;208;233;258;283;308;108;133;158;183;208;233;258;283;308;108;133;158;183;208;233;258;283;308;108;133;158;183;208;233;258;283;308"; top: "209;209;209;209;209;234;234;234;234;234;234;234;234;234;259;259;259;259;259;259;259;259;259;284;284;284;284;284;284;284;284;284;309;309;309;309;309;309;309;309;309;334;334;334;334;334;334;334;334;334;359;359;359;359;359;359;359;359;359"; width: 20px; height: 20px; border-radius: 4px; background: #FFB54799; in: {scale:0.4, opacity:0, duration:.25, ease:'power2.out', stagger:{each:0.011}}) ×59
  div#cs(left: 157px; top: 396px; width: 15px; height: 15px; border-radius: 3px; background: $amber)
  p#ct(left: 179px; cy: 403px; font-size: 17px; font-family: sb; color: $t2) 1 マス = 1 本
shape#arr9(path: "M994 296 L1046 296"; background: none; border: 2.7px solid #8B96A8; in: draw,400,power2.out)
shape#arr9h(points: "1058,296 1046,288 1046,304"; background: #8B96A8; in: {scale:0.3, opacity:0, duration:.45, ease:'back.out(2.2)'})
note#n9 ※ 失敗テキスト 120 本の再合成。使える率 3.1 {b}35%{/} → Flash {b}72%{/} / Lite {b}64%{/}。内容ブロックは {b}63 本 → 4 本{/}。

# 10 結論 — 3 枚の札が語ごとに: 使い分け (主力 Lite → 失敗したら → 切り札 Flash) / 月額 ($923 に線・約 $300・2027 年でも $600 弱) / 品質・速度 (チェック 2 つ・確認の札が光る)・最後に要約の 1 行と罫 → 黒へ溶ける
section#verdict(stagger: {each:0})
header#h10(n: "09"; k: "結論"; h: "{l}Lite{/} を主力に、{f}Flash{/} は切り札に")
div#pd8.sticky(left: 969px; top: 697px; width: 123px; height: 3px; background: $t2; in: none)
progress#pf9(left: 1099px; top: 697px; width: 123px; height: 3px; background: $t2; until: cut)
card#c1(left: 59px; top: 175px; no: "1"; t: "使い分け")
  div#rm(left: 23px; top: 77px; width: 329px; height: 112px; border-radius: 11px; background: #2FDCAA1A; border: 1px solid #2FDCAA8C; in: {y:11, opacity:0, duration:.55, ease:'power3.out'})
    p#k(left: 15px; cy: 22px; font-size: 15px; font-family: r; color: $t2) 主力
    p#v(left: 15px; cy: 56px; font-size: 27px; color: $lite) 3.8 Flash-Lite
    p#d(left: 15px; cy: 88px; font-size: 15px; font-family: r; color: $t2) 通常の合成は Lite で行う
  p#ra(left: 75px; cy: 215px; font-size: 15px; font-family: r; color: $t2; in: {opacity:0, duration:.3}) 失敗したら
  div#rs(left: 23px; top: 241px; width: 329px; height: 112px; border-radius: 11px; background: #4DA3FF14; border: 1px solid #4DA3FF73; in: {y:11, opacity:0, duration:.55, ease:'power3.out'})
    p#k(left: 15px; cy: 22px; font-size: 15px; font-family: r; color: $t2) 切り札
    p#v(left: 15px; cy: 56px; font-size: 27px; color: $flash) 3.8 Flash
    p#d(left: 15px; cy: 88px; font-size: 15px; font-family: r; color: $t2) 失敗したときの再合成に使う
shape#arr10(path: "M118 373 L118 403"; background: none; border: 2px solid #8B96A8; in: draw,350,power2.out)
shape#arr10h(points: "118,409 112,401 123,401"; background: #8B96A8; in: {scale:0.3, opacity:0, duration:.45, ease:'back.out(2.2)'})
card#c2(left: 453px; top: 175px; no: "2"; t: "月額")
  p#fr(left: 23px; cy: 117px; font-size: 40px; font-family: i; color: $c31; in: {y:8, opacity:0, duration:.55, ease:'power3.out'}) $923
  div#fs(left: 20px; top: 116px; width: 108px; height: 3px; background: $c31; in: {scaleX:0, pivot:'left', duration:.4, ease:'power2.out'})
  p#ar(left: 27px; cy: 161px; font-size: 23px; color: $t3; in: {opacity:0, duration:.3}) ↓
  div#to(left: 23px; top: 180px; width: 330px; height: 90px; in: {y:12, scale:0.94, opacity:0, pivot:'0% 100%', duration:.6, ease:'power3.out'})
    p#ya(left: 0px; cy: 65px; font-size: 29px; color: $lite) 約
    p#n(left: 38px; cy: 45px; font-size: 80px; font-family: n; line-height: 1; color: $lite) $300
    p#per(left: .n.right+8; cy: 67px; font-size: 17px; font-family: r; color: $t2) / 月
  div#y27(left: 23px; top: 293px; width: 329px; height: 60px; in: {y:7, opacity:0, duration:.55, ease:'power3.out'})
    div#ln(left: 0px; top: 0px; width: 329px; height: 1px; background: #FFFFFF14)
    p#t(left: 0px; cy: 32px; font-size: 21px; font-family: sb; color: $t2) 2027 年でも {a6}$600{/} 弱
card#c3(left: 847px; top: 175px; no: "3"; t: "品質・速度")
  div#q1(left: 23px; top: 78px; width: 329px; height: 56px; in: {y:8, opacity:0, duration:.55, ease:'power3.out'})
    chk#ck(left: 0px; top: 14px)
    p#t(left: 36px; cy: 13px; font-size: 21px) 品質は同じ
    p#s(left: 36px; cy: 41px; font-size: 14px; font-family: r; color: $t3) 一致率・雑音ともに同じ水準
  div#q2(left: 23px; top: 152px; width: 329px; height: 56px; in: {y:8, opacity:0, duration:.55, ease:'power3.out'})
    chk#ck(left: 0px; top: 14px)
    p#t(left: 36px; cy: 13px; font-size: 21px) 速度は {l}Lite{/} が最速
    p#s(left: 36px; cy: 41px; font-size: 14px; font-family: r; color: $t3) 遅延の中央値 2.89 秒
  div#cau(left: 23px; top: 325px; width: 329px; height: 80px; border-radius: 11px; background: #FFB5471A; border: 1px solid #FFB54799; in: {y:9, scale:0.985, opacity:0, duration:.7, ease:'power3.out'})
    p#k(left: 15px; cy: 24px; font-size: 15px; font-family: sb; color: $amber) 確認すること
    p#v(left: 15px; cy: 53px; font-size: 20px) 男声の低音化だけ確認
p#el(left: 59px; cy: 634px; font-size: 16px; font-family: r; color: $t2; in: {opacity:0, duration:.6, ease:'power1.out'}) 音声合成の乗り換え ── {l}Lite{/} 主力 ＋ {f}Flash{/} 切り札
div#er(left: 430px; top: 634px; width: 792px; height: 1px; background: #FFFFFF2E; in: {scaleX:0, pivot:'left', duration:1, ease:'power3.out'})
```

```timeline.txt
#v2
cast n = "明るく澄んだ20代後半から30代の女性のナレーター、落ち着いた明瞭な語りで社内向けの解説を淡々と読む"
silence head=0 tail=0

# title — 波形が描かれ題が上がる・「フラッシュ」「ライト」の語でその語が光る
*** title
bgm music
se hit -3.7dB +200
@n: [silence:1.6s]音声合成の乗り換え。[!#t_flash glow,#4DA3FFD9,blur=24][=#t_flash +350]フラッシュか、[!#t_lite glow,#2FDCAAD9,blur=24][=#t_lite +350]ライトか。[silence:0.3s]

# bg — 「月額」で $923・「新しい」で矢印と候補の板 2 枚・「比べます」で比べる軸
*** bg
se pad -2.5dB
@n: [silence:0.5s][!#prog.lab[1] recolor,#EEF2F8,duration=350 -500]現行の3.1フラッシュ プレビューは、[>#cur.big -300][>#cur.per -300][♪accent -2.5dB +550][>#cur.fl +900][>#cur.fk +900][>#cur.fv +900]月額923ドル。[>#a2a -150][>#a2b -50][>#s02q +100][>#cf +200][>#cl +400][>#a2h1 +450][>#a2h2 +530][>#cf.d2 +900][>#cl.d2 +900][♪chime -3.1dB]新しい3.8の2モデルと[>#axes -450][>#axl -450][>#ax1 -100][>#ax2 +60]比べます。[silence:0.3s]

# price — 「20ドル」「フラッシュ」「ライト」で横棒が 1 本ずつ伸び、「2027年」で倍額の破線の枠と → $1・「倍額」で札
*** price
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[1] #prog.lab[2] -500]出力の単価は、100万トークンあたり、[>#b3.f[1] -50][>#b3.hv[1] +400][♪swell -3.7dB]20ドルから、[>#b3.f[2]][>#b3.hv[2] +450]フラッシュ9ドル、[>#b3.f[3]][>#b3.hv[3] +450]ライト6ドルに。[silence:0.25s]
@: ただし[>#b3.g[1] +400][>#b3.g[2] +580][>#b3.n27[*] +900][>#b3.gv[1] +950][>#b3.gd[1] +950][>#b3.gv[2] +1130][>#b3.gd[2] +1130]2027年{1月|いちがつ}には、[>#b3.x2 -50][♪tense -1.9dB]倍額になります。[silence:0.3s]

# measure — 数字が語ごとに上がり、「32トークン」で箱が左から並び「公式の目安」で 25 の線と超えた分が琥珀に
*** measure
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[2] #prog.lab[3] -500]4日間の実測は、[>#b4a.st[1] -450][>#b4a.st[2] +900][♪accent -2.5dB +900]2万5432回、[>#b4a.st[3] -400]53.9時間ぶんの音声。[silence:0.25s]
@: [>#b4b +330]1秒あたり[>#b4b.lead -200][>#b4b.lu -200][>#b4b.blk[*] -100][>#b4b.bo[*] +725][♪swell -3.7dB]32トークンと、[>#b4b.mk -100][>#b4b.ml -100][>#b4b.ba[*] +100][>#b4b.ol +300]公式の目安より多めです。[silence:0.3s]

# monthly — 現行の棒と参考の破線は頭に・「フラッシュ」「ライト」で棒・「2027年」で凡例が弾み、金額の語で倍額後の枠
*** monthly
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[3] #prog.lab[4] -500][>#b5.f[1] +250][>#b5.hv[1] +750][>#b5.rf[1] +750][>#b5.rf[2] +900][>#b5.rt[*] +950]月額の見込みは、[>#b5.f[2]][>#b5.hv[2] +500][♪swell -3.7dB]フラッシュ416ドル、[>#b5.f[3]][>#b5.hv[3] +500]ライト278ドル。[silence:0.25s]
@: [!#b5.gleg.t1 punch,1.08,duration=500 +110][♪tense -1.9dB +210]2027年からは、[>#b5.g[1] -350][>#b5.gl[1] -50][>#b5.gd[1] -50]831ドルと[>#b5.g[2] -350][>#b5.gl[2] -50][>#b5.gd[2] -50]556ドルです。[silence:0.3s]

# quality — 「一致率」で縦棒 3 本と同じ水準の札・「雑音」で 0 件・「遅延」で横棒・「ライト」で最速の札と光と長文の棒
*** quality
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[4] #prog.lab[5] -500]本番のテキスト80本では、[>#b6a.ab[*] -150][>#b6a.av[*] +350][>#b6a.eq +1000]一致率は同じ水準で、[>#b6a.nk -200][>#b6a.z[*]][♪pop -3.1dB +350]雑音もゼロ件。[silence:0.25s]
@: [>#b6b.lb[*] +230][>#b6b.lv[*] +730]遅延の中央値は、[>#b6b.sh -350][>#b6b.xl[*] -300][>#b6b.xb[*] -200][>#b6b.xv[*] +100][>#b6b.fast +250][!#b6b.lb[3] glow,#2FDCAABF,blur=17 +200][=#b6b.lb[3] +600][♪chime -3.1dB +200]ライトが2.89秒で最速です。[silence:0.3s]

# voice — 「0.885」で点が滑り込み「同じ声」で 0.81 と括弧とチェック → 30 の点 → 「男性」で注意の板・「低め」で線が下がる
*** voice
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[5] #prog.lab[6] -500]声の類似度は[>#b7a.mt]0.885で、[>#b7a.mg -550][>#gap -100][>#b7a.gs +150][>#b7a.same +450][♪pop -3.1dB +200]同じ声として扱えます。[silence:0.25s]
@: [>#b7b -550][>#b7b.d30[*] -200][>#b7b.m30 +250]ただ、[>#b7c -150][>#pl1 +300][>#b7c.p31 +400][>#b7c.p38 +400][♪tense -1.9dB]男性の声は、3.8で[>#pdrop -200][>#plow +200][>#b7c.wv][>#b7c.wk +200]低めになるものがあります。[silence:0.3s]

# usage — 「日本語」でドーナツ・「単一話者」で人の形と売りの板・「使っていません」で取り消し線と未使用の札
*** usage
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[6] #prog.lab[7] -500]使い方は、[>#b8a -450][>#arc97 -50][>#b8a.p97 +250][>#b8a.ft +800]日本語が97%で、[>#b8b -450][>#b8b.pr -150][>#b8b.bw][>#b8b.ft +350][>#b8c +190][>#b8c.fe[*] +440]単一話者。フラッシュの売りは、[!#b8c.fe[1].n strike,#B6BFCE][!#b8c.fe[2].n strike,#B6BFCE +140][!#b8c.fe[3].n strike,#B6BFCE +280][>#b8c.fe[1].un +100][>#b8c.fe[2].un +240][>#b8c.fe[3].un +380][!#b8c.fe[1].n recolor,#EEF2F873 +150][!#b8c.fe[2].n recolor,#EEF2F873 +290][!#b8c.fe[3].n recolor,#EEF2F873 +430][>#b8c.ft +500][♪pop -3.1dB +150]使っていません。[silence:0.3s]

# retry — 「35%」「フラッシュ」「ライト」で縦棒・「63本」で 63 マス・「4本」で矢印と 4、59 マスが下から沈み 4 マスが濃い琥珀で残る
*** retry
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[7] #prog.lab[8] -500]失敗テキストを合成し直すと、使える率が[>#b9a.vb[1]][>#b9a.vv[1] +500][♪swell -3.7dB]35%から、[>#b9a.vb[2]][>#b9a.vv[2] +500]フラッシュ72%、[>#b9a.vb[3]][>#b9a.vv[3] +500]ライト64%に。[silence:0.25s]
@: [>#b9b -170]内容ブロックも、[>#b9b.from -100][>#b9b.kc[*] -50][>#b9b.cell[*] -6]63本から[>#arr9 -350][>#arr9h -50][>#b9b.to][!#b9b.cell[*] to,{opacity:0.14, scale:0.72, duration:0.3, ease:'power1.in', stagger:{each:0.005, from:'end'}} +50][!#b9b.kc[*] to,{backgroundColor:'#FFB547', scale:1.12, duration:0.3} +400][♪accent -2.5dB +450]4本に。[silence:1.0s]

# verdict — 札 3 枚が語ごとに組み上がり、最後に要約の 1 行と罫・黒へ溶けて終わる
*** verdict
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[8] #prog.lab[9] -500]結論です。[>#c1 -450][>#c1.no -300][>#c1.rm][♪chime -3.1dB]ライトを主力に、[>#arr10 -350][>#arr10h -50][>#c1.ra -300][>#c1.rs]フラッシュは失敗時の切り札に。[silence:0.25s]
@: [>#c2 -450][>#c2.no -300][>#c2.fr +50]月額は923ドルから[>#c2.fs -150][>#c2.ar][>#c2.to +150][♪accent -2.5dB +700]約300ドルへ。[>#c2.y27]2027年でも600ドル弱です。[silence:0.25s]
@: [>#c3 -450][>#c3.no -300][>#c3.q1 -50][♪chime -3.1dB -150]品質は同じで、[>#c3.q2 +50]速度はライトが最速。[>#c3.cau -100][!#c3.cau glow,#FFB54773,blur=23 +500][=#c3.cau +950]男性の声の低音化だけ、[>#er +700][>#el +800]確認しましょう。[silence:2.8s]
fade out,900
```
