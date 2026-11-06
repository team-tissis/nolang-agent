# compare · tts-compare (hf 全力版の全量の写し — 音声合成の乗り換え、Flash か Lite か・3 モデルを 3 色で通す暗い比較の 10 場面) — canvas 1920x1080

見せる作り: 全編の暗い地 (漂う 2 つの光・点の格子・周辺減光)・3 モデルを灰 / 青 / 青緑で通す凡例と色の四角・場面の頭の同じ見出し (番号 + 章名 + 罫 + mask から上がる 1 行) と下端の注記・下端の章の進行 (9 本の帯が章の尺で伸びる)・題つきの板の def で組む図 (語ごとに伸びる横棒と縦棒・倍額の破線の枠・token の箱 ×32 と目安の線・点の数直線と差の括弧・97% のドーナツ・63 → 4 のマスの格子)・結論の 3 枚の札・切替なしで前の場面が上へ抜ける場面替え・字幕なし・音の層 (BGM + 語に結んだ効果音 + 場面替えのパッド)

```design.txt
#v2
# 学ぶ作り: 全編に敷く暗い地 (ゆっくり漂う 2 つの光・点の格子・周辺減光) の上で、3 モデルを 3 色 (灰 / 青 / 青緑) で通して比べる 10 場面
# 場面の頭は同じ見出しの def (番号 + 章名 + 罫 + mask から上がる 1 行) と右上の凡例・下端の注記・下端の章の進行 (9 本の帯が章の尺で伸びる)
# 図は題つきの板 (def) の子で組む: 横棒 (幅は値 × 縮尺)・倍額の破線の枠・縦棒・点の数直線・token の箱 ×32・ドーナツ・63 マスの格子・結論の 3 枚の札
# 場面替えは切替を書かず、前の場面が上へ少し抜けて消え (section の out)、次の場面が組み上がる。字幕は無い (hf の作り)
# hf tts tts-compare (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1920x1080 bg=#070B12
theme dark
palette lab=#7C8799 g31=#4F586A gf=#2F7FD6 gl=#1FB88C from=#9AA3B5 t1=#EEF2F8 t2=#B6BFCE t3=#8B96A8 c31=#A3ACBD c31f=#5F687B flash=#4DA3FF lite=#2FDCAA amber=#FFB547 ref=#D3D9E4 ink=#06101C note=#A9B3C3 a=#2FDCAA b=#4DA3FF
# 書体は説明文で: 和文は癖のない角ゴシックの 3 太さ (本文 Bold / 副題と注記 Medium / 札と軸 SemiBold 相当)・数字は端正なゴシックの Bold / ExtraBold・番号は等幅
font "癖のない現代的な角ゴシック体の太字 (Bold)、IT 資料向け"
fonts r="癖のない標準的なゴシック体の Medium、副題と注記が端正で読みやすい"
fonts sb="癖のない標準的なゴシック体の太字 (Bold)、札と軸の字が端正で読みやすい"
fonts i="癖のない標準的なゴシック体の太字 (Bold)、数字と英字が端正で読みやすい"
fonts n="癖のない標準的なゴシック体の極太 (ExtraBold)、大きな数字が端正でくっきり"
fonts m="等幅のプログラミング用書体の SemiBold"
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
run f { color: $flash }
run l { color: $lite }
run fd { color: $flash; font-family: i }
run ld { color: $lite; font-family: i }
run d { font-family: i }
run b { color: $t2 }
run w { color: $t1 }
run s { font-size: 0.77em }
run a6 { color: $amber; font-family: n; font-size: 1.75em }
p { color: $t1 }
div { border: none }
motion fup { in: {y:22, opacity:0, duration:0.55, ease:'power3.out'} }
motion fups { in: {y:10, opacity:0, duration:0.55, ease:'power3.out'} }
motion fin { in: {opacity:0, duration:0.45, ease:'power1.out'} }
motion bpop { in: {scale:0.6, opacity:0, duration:0.45, ease:'back.out(2.2)'} }
motion brd { in: {y:30, scale:0.985, opacity:0, duration:0.7, ease:'power3.out'} }
cue chap(p, c) = [!#p recolor,#98A3B5 {duration: .35}][!#c recolor,#EEF2F8 {duration: .35}]
bgm#music(fade: 250,3600; duck: -6.5) 知的で落ち着いたミニマルなシンセの曲、浮遊感のあるパッドと静かなシンセベルのフレーズ、淡々とした控えめなビート、暗いデータ解説向け

# 全編の地: 暗い放射の地・左上の青と右下の青緑の光 (全編でゆっくり逆向きに漂う)・点の格子 (ゆっくり上へ)・周辺減光
div#bg_base(inset: 0; background: radial(#0F1828,#0A0F18@45%,#070B12@75%,68%,18%); z-index: back; in: none)
div#bg_g1(left: -420px; top: -640px; width: 1500px; height: 1500px; background: radial(#4DA3FF21,#4DA3FF00@62%,50%,50%); z-index: back; in: none; main: keys(at=0 x=0 y=0 | at=1 x=300 y=170 ease=sine.inOut),window=0,117500,forwards)
div#bg_g2(left: 1000px; top: 380px; width: 1500px; height: 1500px; background: radial(#2FDCAA17,#2FDCAA00@62%,50%,50%); z-index: back; in: none; main: keys(at=0 x=0 y=0 | at=1 x=-340 y=-150 ease=sine.inOut),window=0,117500,forwards)
div#bg_grid(left: -40px; top: -40px; width: 2001px; height: 1161px; pattern: dots,27,#FFFFFF0F; z-index: back; in: none; main: keys(at=0 y=0 | at=1 y=-40 ease=none),window=0,117500,forwards)
div#bg_vig(inset: 0; background: radial(#00000000,#00000000@55%,#00000099,50%,48%); z-index: back; in: none)

# 場面の見出し: 番号 (等幅・青緑) + 章名 + 伸びる罫 + mask から上がる 1 行 (場面の頭の 0.3 秒後から組み上がる)
def header(n, k, h) = div(left: 88px; top: 60px; width: 1650px; height: 114px; in: none)
  p#n(left: 0px; top: 3px; font-size: 22px; font-family: m; color: $lite; letter-spacing: .06em; delay: 300ms; in: {x:-16, opacity:0, duration:.45, ease:'power3.out'}; content: {n})
  p#k(left: 40px; top: 3px; font-size: 22px; font-family: r; color: $t2; letter-spacing: .08em; delay: 360ms; in: {x:-10, opacity:0, duration:.45, ease:'power3.out'}; content: {k})
  div#rule(left: .k.right+14; top: 15px; width: 64px; height: 2px; background: #FFFFFF2E; delay: 400ms; in: {scaleX:0, pivot:'left', duration:.6, ease:'power3.out'})
  p#h(left: 0px; top: 45px; font-size: 52px; line-height: 1.22; letter-spacing: .01em; delay: 420ms; in: mask_rise {duration: 0.85, ease: 'power4.out'}; content: {h})
# 右上の凡例 (色の四角 + モデル名 ×3)
def legend = div(left: 1179px; top: 64px; width: 654px; height: 36px; delay: 700ms; in: {y:-8, opacity:0, duration:.4, ease:'power2.out'})
  div#s1(left: 0px; cy: 50%; width: 18px; height: 18px; border-radius: 4px; background: $c31f; border: 2px solid #FFFFFF40)
  p#t1(left: 28px; cy: 50%; font-size: 22px; font-family: r; color: $t2) 3.1 Flash preview（現行）
  div#s2(left: .t1.right+26; cy: 50%; width: 18px; height: 18px; border-radius: 4px; background: $flash)
  p#t2(left: .s2.right+10; cy: 50%; font-size: 22px; font-family: r; color: $t2) 3.8 Flash
  div#s3(left: .t2.right+26; cy: 50%; width: 18px; height: 18px; border-radius: 4px; background: $lite)
  p#t3(left: .s3.right+10; cy: 50%; font-size: 22px; font-family: r; color: $t2) 3.8 Flash-Lite
# 下端の注記 (数字の出典を 1 行で)
def note(t) = p(left: 88px; top: 942px; width: 1744px; font-size: 26px; line-height: 1.5; font-family: r; color: $note; delay: 800ms; in: {opacity:0, duration:.6, ease:'power1.out'}; content: {t})
# 題つきの板 (半透明の地 + 細い縁 + 深い影・題 + 副題 + 罫)。題だけの板は box
def board(t, s, rw) = div(border-radius: 22px; background: linear(#FFFFFF0D,#FFFFFF06,180); border: 2px solid #FFFFFF1A; box-shadow: 0px 34px 90px #0000006B; in: brd)
  p#t(left: 34px; top: 27px; font-size: 30px; font-family: sb; letter-spacing: .02em; content: {t})
  p#s(left: .t.right+16; top: 33px; font-size: 22px; font-family: r; color: $t3; content: {s})
  div#rule(left: 34px; top: 78px; width: {rw}; height: 2px; background: #FFFFFF1A)
def box(t, rw) = div(border-radius: 22px; background: linear(#FFFFFF0D,#FFFFFF06,180); border: 2px solid #FFFFFF1A; box-shadow: 0px 34px 90px #0000006B; in: brd)
  p#t(left: 34px; top: 27px; font-size: 30px; font-family: sb; letter-spacing: .02em; content: {t})
  div#rule(left: 34px; top: 78px; width: {rw}; height: 2px; background: #FFFFFF1A)
# 候補の板 (色の四角 + モデル名 + NEW の札 + 売り + 導入価格の注記)
def cand(m, d, c, bd) = div(width: 712px; height: 206px; border-radius: 22px; background: linear(#FFFFFF0D,#FFFFFF06,180); border: 2px solid {bd}; box-shadow: 0px 34px 90px #0000006B; in: {y:20, scale:0.985, opacity:0, duration:.7, ease:'power3.out'})
  div#sw(left: 34px; top: 36px; width: 22px; height: 22px; border-radius: 4px; background: {c})
  p#m(left: 70px; top: 21px; font-size: 46px; font-family: i; letter-spacing: -.01em; content: {m})
  p#tag(right: 34px; top: 33px; font-size: 18px; font-family: m; letter-spacing: .08em; color: $ink; background: {c}; border-radius: 8px; padding: 6px 12px) NEW
  p#d(left: 34px; top: 99px; font-size: 26px; font-family: r; color: $t2; content: {d})
  p#d2(left: 34px; top: 148px; font-size: 21px; font-family: r; color: $amber; opacity: .9; in: fin) 2026 年末まで導入価格
# 丸のチェック (青緑の輪 + 描かれるチェック)
def chk = div(width: 40px; height: 40px)
  shape#o(left: 0px; top: 0px; width: 40px; height: 40px; border-radius: 50%; background: #2FDCAA24; border: 2px solid $lite)
  icon#k(cx: 50%; cy: 50%; font-size: 24px; name: check; weight: bold; color: $lite; delay: 200ms; in: draw {duration: 0.4})
# 結論の札 (番号の丸 + 題)
def card(no, t) = div(width: 562px; height: 640px; border-radius: 24px; background: linear(#FFFFFF0E,#FFFFFF06,180); border: 2px solid #FFFFFF1A; box-shadow: 0px 34px 90px #0000006B; in: brd)
  p#no(left: 34px; top: 30px; width: 46px; font-size: 24px; font-family: n; line-height: 1; color: $ink; background: $lite; border-radius: 148px; padding: 12px 0px; text-align: center; in: {scale:0.4, opacity:0, duration:.45, ease:'back.out(2.2)'}; content: {no})
  p#t(left: 94px; cy: 54px; font-size: 28px; font-family: sb; color: $t2; content: {t})

# 01 title — 3 本の波形が左から描かれて流れ、題が mask から 2 行で上がり、副題と 3 つのモデルの札・読む語で Flash / Lite が光る
section#title(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.34, ease:'power1.inOut'})
group#wave(left: 0px; top: 0px; width: 1920px; height: 1080px; main: keys(at=0 x=0 | at=1 x=-60 ease=none),window=0,4700,forwards)
  shape#w31(path: "M0 881 L12 881 L24 881 L36 882 L48 882 L60 882 L72 884 L84 884 L96 885 L108 885 L120 885 L132 887 L144 887 L156 887 L168 888 L180 888 L192 888 L204 890 L216 890 L228 891 L240 891 L252 891 L264 891 L276 893 L288 891 L300 891 L312 891 L324 890 L336 888 L348 887 L360 887 L372 885 L384 885 L396 885 L408 885 L420 887 L432 887 L444 890 L456 891 L468 893 L480 894 L492 896 L504 897 L516 897 L528 897 L540 896 L552 894 L564 891 L576 888 L588 885 L600 882 L612 879 L624 876 L636 873 L648 872 L660 869 L672 867 L684 864 L696 863 L708 860 L720 857 L732 852 L744 849 L756 843 L768 839 L780 833 L792 828 L804 822 L816 819 L828 815 L840 813 L852 812 L864 813 L876 815 L888 818 L900 822 L912 827 L924 831 L936 837 L948 842 L960 848 L972 851 L984 855 L996 858 L1008 861 L1020 864 L1032 866 L1044 869 L1056 870 L1068 873 L1080 876 L1092 881 L1104 884 L1116 888 L1128 893 L1140 896 L1152 899 L1164 902 L1176 903 L1188 905 L1200 903 L1212 903 L1224 900 L1236 899 L1248 896 L1260 893 L1272 891 L1284 890 L1296 888 L1308 888 L1320 888 L1332 890 L1344 891 L1356 893 L1368 896 L1380 897 L1392 900 L1404 902 L1416 903 L1428 903 L1440 905 L1452 905 L1464 905 L1476 903 L1488 903 L1500 902 L1512 902 L1524 902 L1536 902 L1548 902 L1560 902 L1572 902 L1584 902 L1596 900 L1608 900 L1620 899 L1632 897 L1644 896 L1656 894 L1668 893 L1680 890 L1692 888 L1704 885 L1716 884 L1728 882 L1740 881 L1752 879 L1764 879 L1776 878 L1788 878 L1800 878 L1812 878 L1824 878 L1836 879 L1848 879 L1860 879 L1872 879 L1884 881 L1896 881 L1908 881 L1920 881"; background: none; border: 3px solid #8B96A8; opacity: .45; delay: 100ms; in: draw {duration: 2.6, ease: 'power2.out'})
  shape#wf(path: "M0 881 L12 881 L24 882 L36 882 L48 882 L60 884 L72 884 L84 884 L96 882 L108 882 L120 882 L132 882 L144 882 L156 882 L168 882 L180 884 L192 884 L204 884 L216 884 L228 884 L240 882 L252 882 L264 881 L276 879 L288 879 L300 879 L312 879 L324 879 L336 879 L348 879 L360 878 L372 876 L384 872 L396 867 L408 861 L420 854 L432 846 L444 839 L456 833 L468 827 L480 824 L492 822 L504 821 L516 822 L528 822 L540 825 L552 827 L564 827 L576 828 L588 830 L600 831 L612 834 L624 839 L636 846 L648 854 L660 864 L672 876 L684 887 L696 899 L708 909 L720 917 L732 923 L744 924 L756 926 L768 924 L780 921 L792 918 L804 915 L816 914 L828 914 L840 915 L852 918 L864 921 L876 923 L888 924 L900 926 L912 924 L924 923 L936 920 L948 917 L960 915 L972 915 L984 917 L996 921 L1008 926 L1020 933 L1032 941 L1044 947 L1056 951 L1068 954 L1080 954 L1092 950 L1104 944 L1116 936 L1128 926 L1140 917 L1152 906 L1164 899 L1176 891 L1188 884 L1200 878 L1212 873 L1224 867 L1236 860 L1248 852 L1260 845 L1272 836 L1284 828 L1296 821 L1308 815 L1320 810 L1332 809 L1344 810 L1356 815 L1368 819 L1380 827 L1392 834 L1404 840 L1416 846 L1428 851 L1440 855 L1452 857 L1464 858 L1476 860 L1488 861 L1500 863 L1512 864 L1524 867 L1536 870 L1548 873 L1560 876 L1572 878 L1584 879 L1596 879 L1608 879 L1620 878 L1632 876 L1644 875 L1656 875 L1668 875 L1680 875 L1692 876 L1704 878 L1716 881 L1728 882 L1740 884 L1752 885 L1764 887 L1776 887 L1788 887 L1800 887 L1812 887 L1824 885 L1836 885 L1848 884 L1860 884 L1872 884 L1884 882 L1896 882 L1908 881 L1920 881"; background: none; border: 3px solid $flash; opacity: .55; delay: 300ms; in: draw {duration: 2.6, ease: 'power2.out'})
  shape#wl(path: "M0 881 L12 881 L24 881 L36 881 L48 881 L60 879 L72 879 L84 879 L96 878 L108 879 L120 879 L132 879 L144 879 L156 879 L168 878 L180 875 L192 872 L204 867 L216 864 L228 860 L240 857 L252 855 L264 854 L276 851 L288 849 L300 846 L312 842 L324 839 L336 837 L348 837 L360 842 L372 848 L384 858 L396 869 L408 882 L420 893 L432 903 L444 909 L456 915 L468 918 L480 921 L492 924 L504 929 L516 933 L528 939 L540 942 L552 945 L564 944 L576 938 L588 930 L600 921 L612 914 L624 908 L636 906 L648 909 L660 917 L672 926 L684 935 L696 941 L708 944 L720 944 L732 939 L744 933 L756 926 L768 920 L780 915 L792 912 L804 908 L816 902 L828 893 L840 878 L852 858 L864 836 L876 812 L888 791 L900 773 L912 761 L924 755 L936 756 L948 762 L960 770 L972 777 L984 783 L996 789 L1008 792 L1020 798 L1032 806 L1044 816 L1056 830 L1068 848 L1080 864 L1092 881 L1104 891 L1116 897 L1128 899 L1140 894 L1152 887 L1164 881 L1176 876 L1188 875 L1200 879 L1212 885 L1224 894 L1236 903 L1248 911 L1260 915 L1272 918 L1284 921 L1296 923 L1308 927 L1320 933 L1332 941 L1344 951 L1356 960 L1368 968 L1380 971 L1392 971 L1404 963 L1416 954 L1428 941 L1440 927 L1452 915 L1464 905 L1476 896 L1488 890 L1500 884 L1512 878 L1524 872 L1536 866 L1548 858 L1560 852 L1572 848 L1584 846 L1596 846 L1608 848 L1620 852 L1632 858 L1644 863 L1656 867 L1668 869 L1680 870 L1692 870 L1704 869 L1716 869 L1728 869 L1740 869 L1752 870 L1764 872 L1776 873 L1788 875 L1800 875 L1812 876 L1824 876 L1836 876 L1848 878 L1860 878 L1872 879 L1884 879 L1896 881 L1908 881 L1920 881"; background: none; border: 3px solid $lite; opacity: .85; delay: 500ms; in: draw {duration: 2.6, ease: 'power2.out'})
div#t_bar(left: 120px; top: 204px; width: 44px; height: 2px; background: $lite; delay: 100ms; in: {scaleX:0, pivot:'left', duration:.6, ease:'power3.out'})
p#t_kick(left: 180px; top: 190px; font-size: 22px; font-family: r; color: $t2; letter-spacing: .08em; delay: 200ms; in: {opacity:0, duration:.6, ease:'power1.out'}) 社内共有 ｜ ナレーション音声 (TTS) の乗り換え検討
p#t_l1(left: 112px; top: 236px; font-size: 92px; line-height: 1.18; letter-spacing: .01em; delay: 300ms; in: mask_rise {duration: 1, ease: 'power4.out'}) 音声合成の乗り換え、
p#t_flash(left: 112px; top: 344px; font-size: 138px; line-height: 1.16; color: $flash; delay: 420ms; in: mask_rise {duration: 1, ease: 'power4.out'}) Flash
p#t_ka1(left: 495px; top: 376px; font-size: 104px; line-height: 1.16; color: $t2; delay: 420ms; in: mask_rise {duration: 1, ease: 'power4.out'}) か
p#t_lite(left: 615px; top: 344px; font-size: 138px; line-height: 1.16; color: $lite; delay: 420ms; in: mask_rise {duration: 1, ease: 'power4.out'}) Lite
p#t_ka2(left: 888px; top: 376px; font-size: 104px; line-height: 1.16; color: $t2; delay: 420ms; in: mask_rise {duration: 1, ease: 'power4.out'}) か
p#t_sub(left: 120px; top: 590px; font-size: 30px; font-family: r; color: $t2; delay: 1250ms; in: fup) Gemini TTS ── 現行の 3.1 Flash preview から、どこへ乗り換えるか
# モデルの札 3 枚 (色の四角 + 名 + 現行 / 新)
p#t_c1(left: 120px; top: 652px; font-size: 26px; font-family: sb; background: #FFFFFF0D; border: 2px solid #FFFFFF2E; border-radius: 14px; padding: 16px 24px 16px 50px; delay: 1550ms; in: {y:16, opacity:0, duration:.55, ease:'power3.out'}) 3.1 Flash preview  {s}現行{/}
  div#sw(left: 18px; cy: 50%; width: 20px; height: 20px; border-radius: 4px; background: $c31f; border: 2px solid #FFFFFF40; overlap: t_c1)
p#t_c2(left: 483px; top: 652px; font-size: 26px; font-family: sb; background: #FFFFFF0D; border: 2px solid #FFFFFF2E; border-radius: 14px; padding: 16px 24px 16px 50px; delay: 1670ms; in: {y:16, opacity:0, duration:.55, ease:'power3.out'}) 3.8 Flash  {s}新{/}
  div#sw(left: 18px; cy: 50%; width: 20px; height: 20px; border-radius: 4px; background: $flash; overlap: t_c2)
p#t_c3(left: 723px; top: 652px; font-size: 26px; font-family: sb; background: #FFFFFF0D; border: 2px solid #FFFFFF2E; border-radius: 14px; padding: 16px 24px 16px 50px; delay: 1790ms; in: {y:16, opacity:0, duration:.55, ease:'power3.out'}) 3.8 Flash-Lite  {s}新{/}
  div#sw(left: 18px; cy: 50%; width: 20px; height: 20px; border-radius: 4px; background: $lite; overlap: t_c3)

# 02 背景 — 現行の板 ($923 は「月額」で上がる) → 2 本の曲線の矢印が描かれ候補の板 2 枚 → 比べる軸 (破線の枠と 2 つの札)
section#bg(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h2(n: "01"; k: "背景"; h: "乗り換え先を、コストと品質で決める")
# 下端の章の進行 (9 本・全編に残る sticky)。章ごとに帯が伸び、今の章の名が白くなる
div#prog.sticky(left: 88px; top: 1014px; width: 1744px; height: 39px; delay: 200ms; in: {y:10, opacity:0, duration:.6, ease:'power2.out'})
  p#lab(left: "0;195;390;585;780;975;1170;1365;1560"; top: 0px; font-size: 18px; font-family: r; color: $lab; letter-spacing: .06em) ×9 背景;単価;実測;月額;品質;声色;使い方;再合成;結論
  div#track(left: "0;195;390;585;780;975;1170;1365;1560"; top: 32px; width: 184px; height: 4px; border-radius: 3px; background: #FFFFFF1A) ×9
progress#pf1(left: 88px; top: 1046px; width: 184px; height: 4px; background: $t2; until: cut)
board#cur(left: 88px; top: 250px; width: 760px; height: 640px; t: "現行"; s: "ナレーション音声 (TTS)"; rw: 692px; delay: 300ms)
  p#tag(right: 34px; top: 30px; font-size: 18px; font-family: m; letter-spacing: .08em; color: $c31; background: #FFFFFF14; border-radius: 8px; padding: 6px 12px) NOW
  p#model(left: 34px; top: 111px; font-size: 44px; font-family: i; letter-spacing: -.01em) Gemini 3.1 Flash preview
  p#msub(left: 34px; top: 171px; font-size: 24px; font-family: r; color: $t3) 動画生成サービスのナレーションに使用中
  p#ml(left: 34px; top: 244px; font-size: 26px; font-family: r; color: $t2) 月額
  p#big(left: 34px; top: 304px; font-size: 168px; font-family: n; line-height: 1.1; in: {y:26, opacity:0, duration:.6, ease:'power3.out'}) $923
  p#per(left: .big.right+10; top: 392px; font-size: 64px; color: $t3; in: {y:26, opacity:0, duration:.6, ease:'power3.out'}) / 月
  div#fl(left: 34px; top: 558px; width: 692px; height: 2px; background: #FFFFFF14; in: fups)
  p#fk(left: 34px; top: 578px; font-size: 22px; font-family: r; color: $t3; in: fups) 単価 (100 万 token あたり)
  p#fv(right: 34px; top: 572px; font-size: 24px; font-family: r; color: $t2; in: fups) 入力 {d}$1{/} ・ 出力 {d}$20{/}
# 現行 → 候補 2 枚への曲線の矢印 (描かれてから頭が弾む)
shape#a2a(path: "M867 570 C950 570 980 353 1086 353"; background: none; border: 3px solid $t3; in: draw {duration: 0.7, ease: 'power2.inOut'})
shape#a2b(path: "M867 570 C950 570 980 590 1086 590"; background: none; border: 3px solid $t3; in: draw {duration: 0.7, ease: 'power2.inOut'})
shape#a2h1(points: "1104,353 1083,342 1083,365"; background: $t3; in: bpop)
shape#a2h2(points: "1104,590 1083,579 1083,600"; background: $t3; in: bpop)
p#s02q(left: 872px; top: 598px; width: 220px; font-size: 24px; font-family: sb; color: $t2; text-align: center; in: fups) 乗り換え候補
cand#cf(left: 1120px; top: 250px; m: "Gemini 3.8 Flash"; d: "売りは 多話者・タグ・方言"; c: $flash; bd: #4DA3FF73)
cand#cl(left: 1120px; top: 486px; m: "Gemini 3.8 Flash-Lite"; d: "出力単価が 3 モデルで最安"; c: $lite; bd: #2FDCAA73)
# 比べる軸 (破線の枠 + 灰の札 2 つ)
shape#axes(left: 1120px; top: 730px; width: 712px; height: 160px; path: rect,r=0.14; background: none; border: 2px solid #FFFFFF2E; dash: 4,4; in: fin)
p#axl(left: 1155px; cy: 810px; font-size: 24px; font-family: r; color: $t3; in: fin) 比べる軸
p#ax1(left: 1278px; cy: 810px; font-size: 30px; font-family: sb; color: $t2; background: #FFFFFF0F; border: 2px solid #FFFFFF2E; border-radius: 148px; padding: 15px 30px; in: bpop) コスト
p#ax2(left: ax1.right+22; cy: 810px; font-size: 30px; font-family: sb; color: $t2; background: #FFFFFF0F; border: 2px solid #FFFFFF2E; border-radius: 148px; padding: 15px 30px; in: bpop) 品質
note#n2 対象: 動画生成サービスのナレーション音声 (TTS)。金額はすべて USD。

# 03 単価 — 出力単価の横棒 3 本 ($1 = 25 px) が語ごとに伸び、「2027年」で倍額の破線の枠が右へ払われ「倍額」で札
section#price(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h3(n: "02"; k: "単価"; h: "出力単価は {d}$20{/} から {fd}$9{/} ・ {ld}$6{/} へ")
legend#lg3
div#pd1.sticky(left: 88px; top: 1046px; width: 184px; height: 4px; background: $t2; in: none)
progress#pf2(left: 284px; top: 1046px; width: 184px; height: 4px; background: $t2; until: cut)
board#b3(left: 88px; top: 244px; width: 1744px; height: 680px; t: "単価"; s: "100 万 token あたり"; rw: 1676px; delay: 250ms)
  p#x2(right: 34px; top: 22px; font-size: 22px; font-family: sb; color: $amber; background: #FFB5471F; border: 2px solid #FFB54780; border-radius: 148px; padding: 9px 18px; in: {scale:0.7, opacity:0, duration:.45, ease:'back.out(2.2)'}) 2027 年 1 月から ×2 (倍額)
  p#ch(left: "35;435;686"; top: 108px; font-size: 22px; font-family: r; color: $t3) ×3 モデル;入力;出力
  div#sep(left: 34px; top: "308;464"; width: 1676px; height: 2px; background: #FFFFFF0F) ×2
  div#lab(left: 34px; top: "192;348;504"; width: 390px; height: 75px; delay: 300ms; in: {y:12, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.1}}) ×3
    div#sw(left: 0px; top: 10px; width: 18px; height: 18px; border-radius: 4px; background: "$c31f;$flash;$lite")
    p#m(left: 30px; top: 0px; font-size: 28px; font-family: sb) 3.1 Flash preview;3.8 Flash;3.8 Flash-Lite
    p#s(left: 30px; top: 46px; font-size: 20px; font-family: r; color: $t3) 現行;2026 年末まで導入価格;2026 年末まで導入価格
  p#iv(left: 435px; cy: "230;386;542"; font-size: 40px; font-family: i; delay: 450ms; in: {y:12, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.1}}) ×3 $1;$0.5;$0.5
  p#n27(left: 528px; cy: "390;546"; font-size: 26px; font-family: i; color: $amber; in: {scale:0.6, opacity:0, duration:.45, ease:'back.out(2.2)', stagger:{each:.15}}) ×2 → $1
  shape#g(left: "1028;914"; top: "356;512"; width: "342;228"; height: 60px; path: rect,r=0.15; background: #FFB54712; border: 2px solid $amber; dash: 4,3; in: wipe {dir: 'right', duration: 0.75, ease: 'power2.inOut'}) ×2
  div#f(left: 686px; top: "206;362;518"; width: "761;342;228"; height: 48px; border-radius: 8px; background: "linear($g31,#5F687B,90);linear($gf,#4DA3FF,90);linear($gl,#2FDCAA,90)"; in: {scaleX:0, pivot:'left', duration:.85, ease:'power3.out'}) ×3
  p#hv(right: "312;731;845"; cy: "230;386;542"; font-size: 32px; font-family: i; color: "$t1;$ink;$ink"; in: {opacity:0, duration:.3}) ×3 $20;$9;$6
  p#gv(left: "1388;1160"; cy: "386;542"; font-size: 32px; font-family: i; color: $amber; in: {x:-12, opacity:0, duration:.55, ease:'power3.out'}) ×2 $18;$12
  p#gd(left: "1455;1227"; cy: "387;543"; font-size: 20px; font-family: r; color: $amber; opacity: .85; in: {x:-12, opacity:0, duration:.55, ease:'power3.out'}) ×2 2027 年 1 月〜
note#n3 ※ 3.8 系は 2026 年末までの導入価格。2027 年 1 月に倍額 (Flash {b}$1 / $18{/}、Lite {b}$1 / $12{/})。

# 04 実測 — 3 つの数字が語ごとに上がる板 → token の箱 32 個が左から並び、「公式の目安」で 25 の線と超えた 7 個が琥珀に (琥珀の箱 ×7 を同じ所に重ねて出す)
section#measure(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h4(n: "03"; k: "実測"; h: "見積もりの土台は、4 日間の実測ログ")
div#pd2.sticky(left: 284px; top: 1046px; width: 184px; height: 4px; background: $t2; in: none)
progress#pf3(left: 478px; top: 1046px; width: 184px; height: 4px; background: $t2; until: cut)
board#b4a(left: 88px; top: 244px; width: 1744px; height: 330px; t: "実測"; s: "4 日間のログ"; rw: 1676px; delay: 250ms)
  div#st(left: "-3;567;1140"; top: 105px; width: 554px; height: 180px; in: {y:14, opacity:0, duration:.55, ease:'power3.out'}) ×3
    div#bl(left: 0px; top: 0px; width: 2px; height: 180px; background: #FFFFFF14; opacity: "0;1;1")
    p#k(left: 44px; top: 10px; font-size: 24px; font-family: r; color: $t2) 合成の回数;文字数;音声の長さ
    p#v(left: 44px; top: 50px; font-size: 108px; font-family: n; line-height: 1) 25,432;104;53.9
    p#u(left: .v.right+12; top: 108px; font-size: 38px; font-family: sb; color: $t2) 回;万文字;時間
board#b4b(left: 88px; top: 604px; width: 1744px; height: 320px; t: "音声 1 秒あたりの token"; s: "実測 vs 公式の目安"; rw: 1676px)
  p#lead(left: 34px; top: 112px; font-size: 108px; font-family: n; line-height: 1; in: fup) 32
  p#lu(left: 34px; top: 230px; font-size: 24px; font-family: r; color: $t2; in: fup) token / 秒 (実測)
  div#blk(left: "365;407;449;491;533;575;617;659;701;743;785;827;869;911;953;995;1037;1079;1121;1163;1205;1247;1289;1331;1373"; top: 156px; width: 34px; height: 58px; border-radius: 6px; background: #EEF2F8D1; in: {scaleY:0.3, opacity:0, pivot:'bottom', duration:.3, ease:'power2.out', stagger:{each:0.033}}) ×25
  div#bo(left: "1415;1457;1499;1541;1583;1625;1667"; top: 156px; width: 34px; height: 58px; border-radius: 6px; background: #EEF2F8D1; in: {scaleY:0.3, opacity:0, pivot:'bottom', duration:.3, ease:'power2.out', stagger:{each:0.033}}) ×7
  div#ba(left: "1415;1457;1499;1541;1583;1625;1667"; top: 156px; width: 34px; height: 58px; border-radius: 6px; background: $amber; in: {opacity:0, duration:.25, stagger:{each:0.04}}) ×7
  div#mk(left: 1410px; top: 122px; width: 3px; height: 128px; background: $ref; in: {scaleY:0, opacity:0, pivot:'bottom', duration:.45, ease:'power3.out'})
  p#ml(left: 1422px; top: 112px; font-size: 22px; font-family: sb; color: $ref; in: {opacity:0, duration:.45}) 公式の目安 25
  p#ol(left: 1420px; top: 228px; font-size: 22px; font-family: sb; color: $amber; in: fups) 目安を超える分
note#n4 ※ 音声は 1 秒あたり 32 token (公式の目安は 25)。

# 05 月額 — 目盛りと参考の破線 2 本 (Fish / ElevenLabs) の上で 3 本の横棒 ($1 = 0.77 px)・「2027年」で凡例が弾み、倍額後の破線の枠が語ごとに払われる
section#monthly(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h5(n: "04"; k: "月額"; h: "月額は {d}$923{/} から {fd}$416{/} ・ {ld}$278{/} へ")
legend#lg5
div#pd3.sticky(left: 478px; top: 1046px; width: 184px; height: 4px; background: $t2; in: none)
progress#pf4(left: 674px; top: 1046px; width: 184px; height: 4px; background: $t2; until: cut)
board#b5(left: 88px; top: 244px; width: 1744px; height: 680px; t: "月額の見込み"; s: "USD / 月"; rw: 1676px; delay: 250ms)
  div#gleg(left: 1240px; top: 26px; width: 470px; height: 30px; delay: 600ms; in: fin)
    shape#s1(left: 0px; cy: 50%; width: 18px; height: 18px; path: rect,r=0.25; background: none; border: 2px solid $amber; dash: 3,2)
    p#t1(left: 28px; cy: 50%; font-size: 22px; font-family: r; color: $t2) 2027 年 1 月〜 (倍額後)
    div#s2(left: 262px; cy: 50%; width: 3px; height: 22px; background: $ref)
    p#t2(left: 278px; cy: 50%; font-size: 22px; font-family: r; color: $t2) 参考: 他社の月額
  div#gv(left: "395;624;855;1085;1316;1545"; top: 116px; width: 2px; height: 470px; background: #FFFFFF12; delay: 400ms; in: {opacity:0, duration:.5}) ×6
  p#gt(left: "357;587;818;1047;1278;1508"; top: 596px; width: 75px; font-size: 20px; font-family: i; color: $t3; text-align: center; delay: 400ms; in: {opacity:0, duration:.5}) ×6 $0;$200;$400;$600;$800;$1000
  div#lab(left: 34px; top: "174;315;456"; width: 345px; height: 75px; delay: 300ms; in: {y:12, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.1}}) ×3
    div#sw(left: 0px; top: 10px; width: 18px; height: 18px; border-radius: 4px; background: "$c31f;$flash;$lite")
    p#m(left: 30px; top: 0px; font-size: 28px; font-family: sb) 3.1 Flash preview;3.8 Flash;3.8 Flash-Lite
    p#s(left: 30px; top: 46px; font-size: 20px; font-family: r; color: $t3) 現行;導入価格;導入価格
  shape#rf(left: "431;1067"; top: 128px; width: 3px; height: 458px; path: line_v; border: 2px solid $ref; dash: 7,5; in: draw {duration: 0.8, ease: 'power2.out'}) ×2
  p#rt(left: "441;1077"; top: 94px; font-size: 21px; font-family: sb; color: $ref; in: {opacity:0, duration:.5}) ×2 参考 Fish $32;参考 ElevenLabs v3 定価 $584
  shape#g(left: "873;714"; top: "323;464"; width: "477;320"; height: 60px; path: rect,r=0.15; background: #FFB54712; border: 2px solid $amber; dash: 4,3; in: wipe {dir: 'right', duration: 0.8, ease: 'power2.inOut'}) ×2
  div#f(left: 394px; top: "188;329;470"; width: "1062;479;320"; height: 48px; border-radius: 8px; background: "linear($g31,#5F687B,90);linear($gf,#4DA3FF,90);linear($gl,#2FDCAA,90)"; in: {scaleX:0, pivot:'left', duration:.9, ease:'power3.out'}) ×3
  p#hv(right: "302;885;1044"; cy: "212;353;494"; font-size: 32px; font-family: i; color: "$t1;$ink;$ink"; in: {opacity:0, duration:.3}) ×3 $923;$416;$278
  p#gl(right: "411;728"; cy: "353;494"; font-size: 32px; font-family: i; color: $amber; in: {opacity:0, duration:.3}) ×2 $831;$556
  p#gd(right: "497;813"; cy: "354;495"; font-size: 20px; font-family: r; color: $amber; opacity: .8; in: {opacity:0, duration:.3}) ×2 2027 年〜
note#n5 ※ 見込み額。2027 年からは Flash {b}$831{/}、Lite {b}$556{/}。参考: ElevenLabs v3 定価 {b}$584{/}、Fish {b}$32{/}。

# 06 品質 — 左の板: 一致率の縦棒 3 本が並んで伸び「同じ水準」の札・雑音 0 件にチェック / 右の板: 遅延の横棒・「ライト」で最速の札と光・長文の最大の横棒
section#quality(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h6(n: "05"; k: "品質"; h: "品質は同じ。速度は {l}Lite{/} が最速")
legend#lg6
div#pd4.sticky(left: 674px; top: 1046px; width: 184px; height: 4px; background: $t2; in: none)
progress#pf5(left: 868px; top: 1046px; width: 184px; height: 4px; background: $t2; until: cut)
board#b6a(left: 88px; top: 244px; width: 800px; height: 680px; t: "読み取り一致率"; s: "本番テキスト 80 本"; rw: 730px; delay: 250ms)
  p#eq(right: 34px; top: 22px; font-size: 22px; font-family: sb; color: $lite; background: #2FDCAA1F; border: 2px solid #2FDCAA80; border-radius: 148px; padding: 9px 18px; in: {scale:0.7, opacity:0, duration:.45, ease:'back.out(2.2)'}) 3 モデルで同じ水準
  div#base(left: 54px; top: 424px; width: 692px; height: 2px; background: #FFFFFF2E)
  div#ab(left: "101;335;566"; top: "194;195;195"; width: 130px; height: "231;230;230"; border-radius: 10px 10px 4px 4px; background: "linear($g31,#5F687B,0);linear($gf,#4DA3FF,0);linear($gl,#2FDCAA,0)"; in: {scaleY:0, pivot:'bottom', duration:.9, ease:'power3.out', stagger:{each:.12}}) ×3
  p#av(cx: "165;399;630"; cy: 160px; font-size: 40px; font-family: i; color: "$t1;$flash;$lite"; in: {y:8, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.12}}) ×3 0.856;0.850;0.851
  p#xl(cx: "165;399;630"; cy: 454px; font-size: 22px; font-family: sb; color: $t2; delay: 400ms; in: fin) ×3 3.1 Flash pre.;3.8 Flash;3.8 Flash-Lite
  div#nl(left: 34px; top: 558px; width: 730px; height: 2px; background: #FFFFFF14)
  p#nk(left: 34px; top: 574px; font-size: 22px; font-family: sb; color: $t2; in: fin) 雑音の検出
  div#z(left: "116;350;581"; top: 614px; width: 105px; height: 40px; in: {scale:0.7, opacity:0, duration:.45, ease:'back.out(2.2)', stagger:{each:.12}}) ×3
    chk#ck(left: 0px; top: 0px)
    p#v(left: 51px; cy: 50%; font-size: 34px; font-family: i) 0
    p#u(left: 78px; cy: 50%; font-size: 22px; font-family: r; color: $t2) 件
board#b6b(left: 918px; top: 244px; width: 914px; height: 680px; t: "遅延"; s: "中央値 (秒) ・ 短いほど速い"; rw: 844px; delay: 370ms)
  div#ll(left: 34px; top: "143;236;326"; width: 240px; height: 30px; delay: 400ms; in: fin) ×3
    div#sw(left: 0px; cy: 50%; width: 18px; height: 18px; border-radius: 4px; background: "$c31f;$flash;$lite")
    p#m(left: 30px; cy: 50%; font-size: 26px; font-family: sb) 3.1 Flash pre.;3.8 Flash;3.8 Flash-Lite
  div#lb(left: 285px; top: "135;228;318"; width: "419;306;266"; height: 44px; border-radius: 8px; background: "linear($g31,#5F687B,90);linear($gf,#4DA3FF,90);linear($gl,#2FDCAA,90)"; in: {scaleX:0, pivot:'left', duration:.9, ease:'power3.out', stagger:{each:.12}}) ×3
  p#lv(left: "717;605;564"; cy: "158;251;341"; font-size: 30px; font-family: i; color: "$t1;$flash;$lite"; in: {opacity:0, duration:.3, stagger:{each:.12}}) ×3 4.55 秒;3.32 秒;2.89 秒
  p#fast(left: 705px; cy: 340px; font-size: 22px; font-family: sb; color: $lite; background: #2FDCAA1F; border: 2px solid #2FDCAA80; border-radius: 148px; padding: 9px 18px; in: {scale:0.5, opacity:0, duration:.45, ease:'back.out(2.2)'}) 最速
  div#sl(left: 34px; top: 420px; width: 844px; height: 2px; background: #FFFFFF14)
  p#sh(left: 34px; top: 436px; font-size: 22px; font-family: sb; color: $t2; in: fin) 長文 (60 字以上) の最大
  div#xl(left: 34px; top: "497;551;605"; width: 240px; height: 30px; in: {opacity:0, duration:.3, stagger:{each:.1}}) ×3
    div#sw(left: 0px; cy: 50%; width: 18px; height: 18px; border-radius: 4px; background: "$c31f;$flash;$lite")
    p#m(left: 30px; cy: 50%; font-size: 26px; font-family: sb) 3.1 Flash pre.;3.8 Flash;3.8 Flash-Lite
  div#xb(left: 285px; top: "500;554;608"; width: "440;237;179"; height: 24px; border-radius: 6px; background: "linear($g31,#5F687B,90);linear($gf,#4DA3FF,90);linear($gl,#2FDCAA,90)"; in: {scaleX:0, pivot:'left', duration:.8, ease:'power3.out', stagger:{each:.1}}) ×3
  p#xv(left: "738;536;477"; cy: "512;566;620"; font-size: 24px; font-family: i; color: "$t1;$flash;$lite"; in: {opacity:0, duration:.3, stagger:{each:.1}}) ×3 17.2 秒;9.3 秒;7.0 秒
note#n6 ※ 品質ベンチ: 本番のテキスト 80 本を 3 モデルで合成。長文 (60 字以上) の遅延の最大は {b}17.2 / 9.3 / 7.0 秒{/}。

# 07 声色 — 点の数直線: 「0.885」で青緑の点が左から滑り込み、「同じ声」で灰の点 0.81 と差の括弧・チェック → 30 の点の格子 → 注意の板 (声の高さが段で下がる線)
section#voice(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h7(n: "06"; k: "声色"; h: "{f}Flash{/} と {l}Lite{/} は、同じ声として扱える")
div#pd5.sticky(left: 868px; top: 1046px; width: 184px; height: 4px; background: $t2; in: none)
progress#pf6(left: 1064px; top: 1046px; width: 184px; height: 4px; background: $t2; until: cut)
board#b7a(left: 88px; top: 244px; width: 1000px; height: 680px; t: "声の類似度"; s: "同じ声・同じ文で比較"; rw: 932px; delay: 250ms)
  div#vc(left: "233;572"; top: 111px; width: "222;198"; height: 76px; border-radius: 16px; border: 2px solid #FFFFFF2E; background: #FFFFFF0A; delay: 300ms; in: {scale:0.8, opacity:0, duration:.45, ease:'back.out(2.2)', stagger:{each:.12}}) ×2
    shape#w(left: 27px; cy: 50%; width: 66px; height: 16px; path: "wave,n=3"; background: none; border: "3px solid $flash;3px solid $lite")
    p#t(left: 110px; cy: 50%; font-size: 32px; font-family: i; color: "$flash;$lite") Flash;Lite
  p#eqs(left: 486px; cy: 148px; font-size: 44px; font-family: i; color: $t3; delay: 500ms; in: fin) ↔
  div#ax(left: 75px; top: 381px; width: 850px; height: 4px; border-radius: 3px; background: #FFFFFF24; delay: 500ms; in: fin)
  div#tm(left: "74;357;641;924"; top: 393px; width: 2px; height: 10px; background: #FFFFFF40; delay: 500ms; in: fin) ×4
  p#tk(left: "45;329;612;896"; top: 411px; width: 60px; font-size: 20px; font-family: i; color: $t3; text-align: center; delay: 500ms; in: fin) ×4 0.70;0.80;0.90;1.00
  div#mg(left: 282px; top: 240px; width: 210px; height: 165px)
    p#v(cx: 50%; top: 6px; font-size: 44px; font-family: n; line-height: 1; in: {y:10, opacity:0, duration:.55, ease:'power3.out'}; delay: 150ms) 0.81
    p#k(cx: 50%; top: 52px; font-size: 20px; font-family: r; color: $t2; in: {y:10, opacity:0, duration:.55, ease:'power3.out'}; delay: 150ms) 別テキストの揺れ
    div#stem(cx: 50%; top: 96px; width: 2px; height: 34px; background: #8B96A8; delay: 50ms; in: {scaleY:0, pivot:'bottom', duration:.4, ease:'power2.out'})
    div#dot(cx: 50%; top: 128px; width: 30px; height: 30px; border-radius: 15px; background: #8B96A8; in: {scale:0.2, opacity:0, duration:.45, ease:'back.out(2.2)'})
  div#mt(left: 495px; top: 240px; width: 210px; height: 165px; in: {x:-180, duration:.9, ease:'power3.out'})
    p#v(cx: 50%; top: 6px; font-size: 44px; font-family: n; line-height: 1; color: $lite; in: {y:10, opacity:0, duration:.55, ease:'power3.out'}; delay: 150ms) 0.885
    p#k(cx: 50%; top: 52px; font-size: 20px; font-family: r; color: $t2; in: {y:10, opacity:0, duration:.55, ease:'power3.out'}; delay: 150ms) Flash {d}↔{/} Lite
    div#stem(cx: 50%; top: 96px; width: 2px; height: 34px; background: $lite; delay: 50ms; in: {scaleY:0, pivot:'bottom', duration:.4, ease:'power2.out'})
    div#dot(cx: 50%; top: 128px; width: 30px; height: 30px; border-radius: 15px; background: $lite; box-shadow: 0px 0px 0px 8px #2FDCAA2E; in: {scale:0.2, opacity:0, duration:.45, ease:'back.out(2.2)'})
  p#gs(cx: 494px; top: 460px; font-size: 22px; font-family: sb; color: $lite; in: fups) 揺れ (0.81) より近い
  div#same(left: 34px; top: 590px; width: 932px; height: 75px; in: fups)
    div#ln(left: 0px; top: 0px; width: 932px; height: 2px; background: #FFFFFF14)
    chk#ck(left: 0px; top: 18px)
    p#t(left: 57px; cy: 38px; font-size: 30px) 同じ声として扱える
# 差の括弧 (0.81 から 0.885 まで・描かれる)
shape#gap(path: "M477 684 L477 698 L687 698 L687 684"; background: none; border: 3px solid $lite; in: draw {duration: 0.55, ease: 'power2.out'})
board#b7b(left: 1118px; top: 244px; width: 714px; height: 316px; t: "話者の対応"; s: "本番 {d}↔{/} 3.8 組み込み"; rw: 645px)
  div#d30(left: "126;174;222;270;318;366;414;462;510;558;126;174;222;270;318;366;414;462;510;558;126;174;222;270;318;366;414;462;510;558"; top: "113;113;113;113;113;113;113;113;113;113;156;156;156;156;156;156;156;156;156;156;200;200;200;200;200;200;200;200;200;200"; width: 30px; height: 30px; border-radius: 15px; background: $lite; box-shadow: 0px 0px 0px 4px #2FDCAA24; in: {scale:0.2, opacity:0, duration:.35, ease:'back.out(2.2)', stagger:{each:0.022}}) ×30
  p#m30(left: 34px; top: 249px; width: 645px; font-size: 24px; font-family: r; color: $t2; text-align: center; in: fups) 本番の話者 {w}30 人{/} は、3.8 の組み込み {w}30 声{/} と一致
# 注意の板 (琥珀の縁と地): 3.1 の線から段で下がる 3.8 の線 + 0.71〜0.76 倍
box#b7c(left: 1118px; top: 590px; width: 714px; height: 334px; t: "注意 ── 男声の低音化"; rw: 645px; border: 2px solid #FFB5478C; background: linear(#FFB5471A,#FFB54708,180))
  p#t(color: $amber)
  p#p31(left: 51px; top: 94px; font-size: 18px; font-family: i; color: $c31; in: fin) 3.1
  p#p38(left: 168px; top: 188px; font-size: 18px; font-family: i; color: $amber; in: fin) 3.8
  p#wv(left: 314px; top: 110px; font-size: 52px; font-family: n; line-height: 1.05; color: $amber; in: fups) 0.71〜0.76{s}倍{/}
  p#wk(left: 314px; top: 174px; width: 300px; font-size: 24px; font-family: r; line-height: 1.45; color: $t2; in: fups) 3.8 で基本周波数が下がる男声がある
shape#pl1(path: "M1169 717 L1269 717"; background: none; border: 3px solid #8B96A8; in: draw {duration: 0.5, ease: 'power2.out'})
shape#pdrop(path: "M1269 717 C1277 717 1277 773 1286 773"; background: none; border: 2px solid $amber; in: draw {duration: 0.45, ease: 'power2.in'})
shape#plow(path: "M1286 773 L1386 773"; background: none; border: 3px solid $amber; in: draw {duration: 0.5, ease: 'power2.out'})
note#n7 ※ 類似度: 同じ声・同じ文で Flash と Lite を比較 ({b}0.885{/})。別テキストでの揺れは {b}0.81{/}。

# 08 使い方 — 3 枚の板が語ごとに: 97% のドーナツ (12 時から描かれる弧) / 単一話者の人の形 / Flash の売り 3 行に取り消し線と「未使用」の札
section#usage(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h8(n: "07"; k: "使い方"; h: "{f}Flash{/} の売りは、いまの使い方では使っていない")
div#pd6.sticky(left: 1064px; top: 1046px; width: 184px; height: 4px; background: $t2; in: none)
progress#pf7(left: 1258px; top: 1046px; width: 184px; height: 4px; background: $t2; until: cut)
box#b8a(left: 88px; top: 250px; width: 540px; height: 660px; t: "言語"; rw: 471px)
  shape#ring(left: 126px; top: 138px; width: 286px; height: 286px; border-radius: 50%; background: none; border: 34px solid #FFFFFF1A)
  p#p97(cx: 268px; top: 238px; font-size: 86px; font-family: n; line-height: 1; in: fups) 97%
  p#ja(cx: 268px; top: 328px; font-size: 24px; font-family: r; color: $t2) 日本語
  p#ft(left: 0px; top: 591px; width: 540px; font-size: 24px; font-family: r; color: $t2; text-align: center; in: fin) ナレーションの {w}97%{/} が日本語
shape#arc97(path: "M357.0 405.0 C426.6 405.0 483.0 461.4 483.0 531.0 C483.0 600.6 426.6 657.0 357.0 657.0 C287.4 657.0 231.0 600.6 231.0 531.0 C231.0 470.5 274.0 418.5 333.5 407.2"; overlap: b8a.p97,b8a.ja; background: none; border: 34px solid $lite; in: draw {duration: 1.2, ease: 'power2.inOut'})
box#b8b(left: 690px; top: 250px; width: 540px; height: 660px; t: "話者"; rw: 471px)
  svg#pr(left: 195px; top: 166px; width: 150px; height: 230px; part: person; in: {scale:0.7, opacity:0, duration:.45, ease:'back.out(2.2)'})
  p#bw(cx: 270px; cy: 448px; font-size: 56px; in: fups) 単一話者
  p#ft(left: 0px; top: 591px; width: 540px; font-size: 24px; font-family: r; color: $t2; text-align: center; in: fin) 1 本のナレーションを 1 人の声で読む
box#b8c(left: 1292px; top: 250px; width: 540px; height: 660px; t: "{f}Flash{/} の売り"; rw: 471px)
  group#fes(left: 34px; top: 146px; width: 471px; height: 330px; display: flex; flex-direction: column; gap: 20px)
    div#fe(flex: 1; width: 471px; border-radius: 14px; background: #4DA3FF14; border: 2px solid #4DA3FF59; in: {y:12, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.12}}) ×3
      p#n(left: 26px; cy: 50%; font-size: 34px) 多話者;タグ;方言
      p#un(right: 26px; cy: 50%; font-size: 22px; font-family: sb; color: $t2; border: 2px solid #FFFFFF2E; border-radius: 8px; padding: 4px 12px; in: {scale:0.6, opacity:0, duration:.45, ease:'back.out(2.2)'}) 未使用
  p#ft(left: 0px; top: 591px; width: 540px; font-size: 24px; font-family: r; color: $t2; text-align: center; in: fin) いずれも現在の使い方では使っていない
note#n8 ※ 使い方の実態: 日本語 97%、単一話者。Flash の売り (多話者・タグ・方言) は使っていない。

# 09 再合成 — 使える率の縦棒 3 本 (目盛り 0〜100%) が語ごとに伸びる → 内容ブロック 63 → 4: 63 マスが並び、59 マスが沈んで 4 マスが琥珀に残る
section#retry(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.34, ease:'power1.inOut'})
header#h9(n: "08"; k: "再合成"; h: "失敗テキストも、3.8 なら使える率が上がる")
legend#lg9
div#pd7.sticky(left: 1258px; top: 1046px; width: 184px; height: 4px; background: $t2; in: none)
progress#pf8(left: 1454px; top: 1046px; width: 184px; height: 4px; background: $t2; until: cut)
board#b9a(left: 88px; top: 244px; width: 1060px; height: 680px; t: "使える率"; s: "失敗テキスト 120 本を再合成"; rw: 992px; delay: 250ms)
  shape#yg(left: 135px; top: "137;242;347;452;557"; width: 861px; height: 3px; path: line_h; border: 2px solid #FFFFFF17; dash: 4,4; delay: 400ms; in: {opacity:0, duration:.5}) ×5
  p#yt(left: 52px; width: 60px; cy: "137;242;347;452;557"; font-size: 20px; font-family: i; color: $t3; text-align: right; delay: 400ms; in: {opacity:0, duration:.5}) ×5 100%;75%;50%;25%;0%
  div#vb(left: "233;488;746"; top: "410;254;288"; width: 160px; height: "147;303;269"; border-radius: 10px 10px 4px 4px; background: "linear($g31,#5F687B,0);linear($gf,#4DA3FF,0);linear($gl,#2FDCAA,0)"; in: {scaleY:0, pivot:'bottom', duration:.9, ease:'power3.out'}) ×3
  p#vv(cx: "312;567;825"; cy: "371;212;248"; font-size: 48px; font-family: i; color: "$t1;$flash;$lite"; in: fups) ×3 35%;72%;64%
  p#xl(cx: "312;567;825"; cy: 584px; font-size: 22px; font-family: sb; color: $t2; delay: 500ms; in: fin) ×3 3.1 Flash pre.;3.8 Flash;3.8 Flash-Lite
board#b9b(left: 1178px; top: 244px; width: 654px; height: 680px; t: "内容ブロック"; s: "内容を理由に合成が止まった本数"; rw: 585px)
  div#from(left: 112px; top: 117px; width: 195px; height: 150px; in: {scale:0.7, opacity:0, duration:.45, ease:'back.out(2.2)'})
    p#n(cx: 50%; top: 0px; font-size: 112px; font-family: n; line-height: 1; color: $from) 63
    p#u(cx: 50%; top: 123px; font-size: 24px; font-family: sb; color: $t2) 本
  div#to(left: 436px; top: 117px; width: 90px; height: 150px; in: {scale:0.6, opacity:0, duration:.45, ease:'back.out(2.2)'})
    p#n(cx: 50%; top: 0px; font-size: 112px; font-family: n; line-height: 1) 4
    p#u(cx: 50%; top: 123px; font-size: 24px; font-family: sb; color: $t2) 本
# 残る 4 マス (hf の KEEP = 先頭 4 つ) は別の ×4 で持ち、沈む 59 マスと分けて動かす
  div#kc(left: "162;200;237;275"; top: "314;314;314;314"; width: 30px; height: 30px; border-radius: 6px; background: #FFB54799; in: {scale:0.4, opacity:0, duration:.25, ease:'power2.out', stagger:{each:0.011}}) ×4
  div#cell(left: "312;350;387;425;462;162;200;237;275;312;350;387;425;462;162;200;237;275;312;350;387;425;462;162;200;237;275;312;350;387;425;462;162;200;237;275;312;350;387;425;462;162;200;237;275;312;350;387;425;462;162;200;237;275;312;350;387;425;462"; top: "314;314;314;314;314;351;351;351;351;351;351;351;351;351;389;389;389;389;389;389;389;389;389;426;426;426;426;426;426;426;426;426;464;464;464;464;464;464;464;464;464;501;501;501;501;501;501;501;501;501;539;539;539;539;539;539;539;539;539"; width: 30px; height: 30px; border-radius: 6px; background: #FFB54799; in: {scale:0.4, opacity:0, duration:.25, ease:'power2.out', stagger:{each:0.011}}) ×59
  div#cs(left: 236px; top: 594px; width: 22px; height: 22px; border-radius: 4px; background: $amber)
  p#ct(left: 268px; cy: 604px; font-size: 26px; font-family: sb; color: $t2) 1 マス = 1 本
shape#arr9(path: "M1491 444 L1569 444"; background: none; border: 4px solid #8B96A8; in: draw {duration: 0.4, ease: 'power2.out'})
shape#arr9h(points: "1587,444 1569,432 1569,456"; background: #8B96A8; in: {scale:0.3, opacity:0, duration:.45, ease:'back.out(2.2)'})
note#n9 ※ 失敗テキスト 120 本の再合成。使える率 3.1 {b}35%{/} → Flash {b}72%{/} / Lite {b}64%{/}。内容ブロックは {b}63 本 → 4 本{/}。

# 10 結論 — 3 枚の札が語ごとに: 使い分け (主力 Lite → 失敗したら → 切り札 Flash) / 月額 ($923 に線・約 $300・2027 年でも $600 弱) / 品質・速度 (チェック 2 つ・確認の札が光る)・最後に要約の 1 行と罫 → 黒へ溶ける
section#verdict(stagger: {each:0})
header#h10(n: "09"; k: "結論"; h: "{l}Lite{/} を主力に、{f}Flash{/} は切り札に")
div#pd8.sticky(left: 1454px; top: 1046px; width: 184px; height: 4px; background: $t2; in: none)
progress#pf9(left: 1648px; top: 1046px; width: 184px; height: 4px; background: $t2; until: cut)
card#c1(left: 88px; top: 262px; no: "1"; t: "使い分け")
  div#rm(left: 34px; top: 116px; width: 494px; height: 168px; border-radius: 16px; background: #2FDCAA1A; border: 2px solid #2FDCAA8C; in: {y:16, opacity:0, duration:.55, ease:'power3.out'})
    p#k(left: 22px; cy: 33px; font-size: 22px; font-family: r; color: $t2) 主力
    p#v(left: 22px; cy: 84px; font-size: 40px; color: $lite) 3.8 Flash-Lite
    p#d(left: 22px; cy: 132px; font-size: 22px; font-family: r; color: $t2) 通常の合成は Lite で行う
  p#ra(left: 112px; cy: 322px; font-size: 22px; font-family: r; color: $t2; in: {opacity:0, duration:.3}) 失敗したら
  div#rs(left: 34px; top: 362px; width: 494px; height: 168px; border-radius: 16px; background: #4DA3FF14; border: 2px solid #4DA3FF73; in: {y:16, opacity:0, duration:.55, ease:'power3.out'})
    p#k(left: 22px; cy: 33px; font-size: 22px; font-family: r; color: $t2) 切り札
    p#v(left: 22px; cy: 84px; font-size: 40px; color: $flash) 3.8 Flash
    p#d(left: 22px; cy: 132px; font-size: 22px; font-family: r; color: $t2) 失敗したときの再合成に使う
shape#arr10(path: "M177 560 L177 605"; background: none; border: 3px solid #8B96A8; in: draw {duration: 0.35, ease: 'power2.out'})
shape#arr10h(points: "177,614 168,602 185,602"; background: #8B96A8; in: {scale:0.3, opacity:0, duration:.45, ease:'back.out(2.2)'})
card#c2(left: 680px; top: 262px; no: "2"; t: "月額")
  p#fr(left: 34px; cy: 176px; font-size: 60px; font-family: i; color: $c31; in: {y:12, opacity:0, duration:.55, ease:'power3.out'}) $923
  div#fs(left: 30px; top: 174px; width: 162px; height: 4px; background: $c31; overlap: fr; in: {scaleX:0, pivot:'left', duration:.4, ease:'power2.out'})
  p#ar(left: 40px; cy: 242px; font-size: 34px; color: $t3; in: {opacity:0, duration:.3}) ↓
  div#to(left: 34px; top: 270px; width: 495px; height: 135px; in: {y:18, scale:0.94, opacity:0, pivot:'0% 100%', duration:.6, ease:'power3.out'})
    p#ya(left: 0px; cy: 98px; font-size: 44px; color: $lite) 約
    p#n(left: 57px; cy: 68px; font-size: 120px; font-family: n; line-height: 1; color: $lite) $300
    p#per(left: .n.right+12; cy: 100px; font-size: 26px; font-family: r; color: $t2) / 月
  div#y27(left: 34px; top: 440px; width: 494px; height: 90px; in: {y:10, opacity:0, duration:.55, ease:'power3.out'})
    div#ln(left: 0px; top: 0px; width: 494px; height: 2px; background: #FFFFFF14)
    p#t(left: 0px; cy: 48px; font-size: 32px; font-family: sb; color: $t2) 2027 年でも {a6}$600{/} 弱
card#c3(left: 1270px; top: 262px; no: "3"; t: "品質・速度")
  div#q1(left: 34px; top: 117px; width: 494px; height: 84px; in: {y:12, opacity:0, duration:.55, ease:'power3.out'})
    chk#ck(left: 0px; top: 21px)
    p#t(left: 54px; cy: 20px; font-size: 32px) 品質は同じ
    p#s(left: 54px; cy: 62px; font-size: 21px; font-family: r; color: $t3) 一致率・雑音ともに同じ水準
  div#q2(left: 34px; top: 228px; width: 494px; height: 84px; in: {y:12, opacity:0, duration:.55, ease:'power3.out'})
    chk#ck(left: 0px; top: 21px)
    p#t(left: 54px; cy: 20px; font-size: 32px) 速度は {l}Lite{/} が最速
    p#s(left: 54px; cy: 62px; font-size: 21px; font-family: r; color: $t3) 遅延の中央値 2.89 秒
  div#cau(left: 34px; top: 488px; width: 494px; height: 120px; border-radius: 16px; background: #FFB5471A; border: 2px solid #FFB54799; in: {y:14, scale:0.985, opacity:0, duration:.7, ease:'power3.out'})
    p#k(left: 22px; cy: 36px; font-size: 22px; font-family: sb; color: $amber) 確認すること
    p#v(left: 22px; cy: 80px; font-size: 30px) 男声の低音化だけ確認
p#el(left: 88px; cy: 951px; font-size: 24px; font-family: r; color: $t2; in: {opacity:0, duration:.6, ease:'power1.out'}) 音声合成の乗り換え ── {l}Lite{/} 主力 ＋ {f}Flash{/} 切り札
div#er(left: 645px; top: 951px; width: 1188px; height: 2px; background: #FFFFFF2E; in: {scaleX:0, pivot:'left', duration:1, ease:'power3.out'})
```

```timeline.txt
#v2
cast n = "明るく澄んだ20代後半から30代の女性のナレーター、落ち着いた明瞭な語りで社内向けの解説を淡々と読む"
silence head=0ms tail=0ms

# title — 波形が描かれ題が上がる・「フラッシュ」「ライト」の語でその語が光る
*** title
bgm music
se hit -3.7dB +200ms
@n: [silence:1.6s]音声合成の乗り換え。[!#t_flash glow,#4DA3FFD9 {blur: 24}][=#t_flash +350ms]フラッシュか、[!#t_lite glow,#2FDCAAD9 {blur: 24}][=#t_lite +350ms]ライトか。[silence:0.3s]

# bg — 「月額」で $923・「新しい」で矢印と候補の板 2 枚・「比べます」で比べる軸
*** bg
se pad -2.5dB
@n: [silence:0.5s][!#prog.lab[1] recolor,#EEF2F8 {duration: .35} -500ms]現行の3.1フラッシュ プレビューは、[>#cur.big -300ms][>#cur.per -300ms][♪accent -2.5dB +550ms][>#cur.fl +900ms][>#cur.fk +900ms][>#cur.fv +900ms]月額923ドル。[>#a2a -150ms][>#a2b -50ms][>#s02q +100ms][>#cf +200ms][>#cl +400ms][>#a2h1 +450ms][>#a2h2 +530ms][>#cf.d2 +900ms][>#cl.d2 +900ms][♪chime -3.1dB]新しい3.8の2モデルと[>#axes -450ms][>#axl -450ms][>#ax1 -100ms][>#ax2 +60ms]比べます。[silence:0.3s]

# price — 「20ドル」「フラッシュ」「ライト」で横棒が 1 本ずつ伸び、「2027年」で倍額の破線の枠と → $1・「倍額」で札
*** price
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[1] #prog.lab[2] -500ms]出力の単価は、100万トークンあたり、[>#b3.f[1] -50ms][>#b3.hv[1] +400ms][♪swell -3.7dB]20ドルから、[>#b3.f[2]][>#b3.hv[2] +450ms]フラッシュ9ドル、[>#b3.f[3]][>#b3.hv[3] +450ms]ライト6ドルに。[silence:0.25s]
@: ただし[>#b3.g[1] +400ms][>#b3.g[2] +580ms][>#b3.n27[*] +900ms][>#b3.gv[1] +950ms][>#b3.gd[1] +950ms][>#b3.gv[2] +1130ms][>#b3.gd[2] +1130ms]2027年1月には、[>#b3.x2 -50ms][♪tense -1.9dB]倍額になります。[silence:0.3s]

# measure — 数字が語ごとに上がり、「32トークン」で箱が左から並び「公式の目安」で 25 の線と超えた分が琥珀に
*** measure
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[2] #prog.lab[3] -500ms]4日間の実測は、[>#b4a.st[1] -450ms][>#b4a.st[2] +900ms][♪accent -2.5dB +900ms]2万5432回、[>#b4a.st[3] -400ms]53.9時間ぶんの音声。[silence:0.25s]
@: [>#b4b +330ms]1秒あたり[>#b4b.lead -200ms][>#b4b.lu -200ms][>#b4b.blk[*] -100ms][>#b4b.bo[*] +725ms][♪swell -3.7dB]32トークンと、[>#b4b.mk -100ms][>#b4b.ml -100ms][>#b4b.ba[*] +100ms][>#b4b.ol +300ms]公式の目安より多めです。[silence:0.3s]

# monthly — 現行の棒と参考の破線は頭に・「フラッシュ」「ライト」で棒・「2027年」で凡例が弾み、金額の語で倍額後の枠
*** monthly
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[3] #prog.lab[4] -500ms][>#b5.f[1] +250ms][>#b5.hv[1] +750ms][>#b5.rf[1] +750ms][>#b5.rf[2] +900ms][>#b5.rt[*] +950ms]月額の見込みは、[>#b5.f[2]][>#b5.hv[2] +500ms][♪swell -3.7dB]フラッシュ416ドル、[>#b5.f[3]][>#b5.hv[3] +500ms]ライト278ドル。[silence:0.25s]
@: [!#b5.gleg.t1 punch {scale: 1.08, duration: .5} +110ms][♪tense -1.9dB +210ms]2027年からは、[>#b5.g[1] -350ms][>#b5.gl[1] -50ms][>#b5.gd[1] -50ms]831ドルと[>#b5.g[2] -350ms][>#b5.gl[2] -50ms][>#b5.gd[2] -50ms]556ドルです。[silence:0.3s]

# quality — 「一致率」で縦棒 3 本と同じ水準の札・「雑音」で 0 件・「遅延」で横棒・「ライト」で最速の札と光と長文の棒
*** quality
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[4] #prog.lab[5] -500ms]本番のテキスト80本では、[>#b6a.ab[*] -150ms][>#b6a.av[*] +350ms][>#b6a.eq +1000ms]一致率は同じ水準で、[>#b6a.nk -200ms][>#b6a.z[*]][♪pop -3.1dB +350ms]雑音もゼロ件。[silence:0.25s]
@: [>#b6b.lb[*] +230ms][>#b6b.lv[*] +730ms]遅延の中央値は、[>#b6b.sh -350ms][>#b6b.xl[*] -300ms][>#b6b.xb[*] -200ms][>#b6b.xv[*] +100ms][>#b6b.fast +250ms][!#b6b.lb[3] glow,#2FDCAABF {blur: 17} +200ms][=#b6b.lb[3] +600ms][♪chime -3.1dB +200ms]ライトが2.89秒で最速です。[silence:0.3s]

# voice — 「0.885」で点が滑り込み「同じ声」で 0.81 と括弧とチェック → 30 の点 → 「男性」で注意の板・「低め」で線が下がる
*** voice
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[5] #prog.lab[6] -500ms]声の類似度は[>#b7a.mt]0.885で、[>#b7a.mg -550ms][>#gap -100ms][>#b7a.gs +150ms][>#b7a.same +450ms][♪pop -3.1dB +200ms]同じ声として扱えます。[silence:0.25s]
@: [>#b7b -550ms][>#b7b.d30[*] -200ms][>#b7b.m30 +250ms]ただ、[>#b7c -150ms][>#pl1 +300ms][>#b7c.p31 +400ms][>#b7c.p38 +400ms][♪tense -1.9dB]男性の声は、3.8で[>#pdrop -200ms][>#plow +200ms][>#b7c.wv][>#b7c.wk +200ms]低めになるものがあります。[silence:0.3s]

# usage — 「日本語」でドーナツ・「単一話者」で人の形と売りの板・「使っていません」で取り消し線と未使用の札
*** usage
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[6] #prog.lab[7] -500ms]使い方は、[>#b8a -450ms][>#arc97 -50ms][>#b8a.p97 +250ms][>#b8a.ft +800ms]日本語が97%で、[>#b8b -450ms][>#b8b.pr -150ms][>#b8b.bw][>#b8b.ft +350ms][>#b8c +190ms][>#b8c.fes.fe[*] +440ms]単一話者。フラッシュの売りは、[!#b8c.fes.fe[1].n strike,#B6BFCE][!#b8c.fes.fe[2].n strike,#B6BFCE +140ms][!#b8c.fes.fe[3].n strike,#B6BFCE +280ms][>#b8c.fes.fe[1].un +100ms][>#b8c.fes.fe[2].un +240ms][>#b8c.fes.fe[3].un +380ms][!#b8c.fes.fe[1].n recolor,#EEF2F873 +150ms][!#b8c.fes.fe[2].n recolor,#EEF2F873 +290ms][!#b8c.fes.fe[3].n recolor,#EEF2F873 +430ms][>#b8c.ft +500ms][♪pop -3.1dB +150ms]使っていません。[silence:0.3s]

# retry — 「35%」「フラッシュ」「ライト」で縦棒・「63本」で 63 マス・「4本」で矢印と 4、59 マスが下から沈み 4 マスが濃い琥珀で残る
*** retry
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[7] #prog.lab[8] -500ms]失敗テキストを合成し直すと、使える率が[>#b9a.vb[1]][>#b9a.vv[1] +500ms][♪swell -3.7dB]35%から、[>#b9a.vb[2]][>#b9a.vv[2] +500ms]フラッシュ72%、[>#b9a.vb[3]][>#b9a.vv[3] +500ms]ライト64%に。[silence:0.25s]
@: [>#b9b -170ms]内容ブロックも、[>#b9b.from -100ms][>#b9b.kc[*] -50ms][>#b9b.cell[*] -6ms]63本から[>#arr9 -350ms][>#arr9h -50ms][>#b9b.to][!#b9b.cell[*] to,{opacity:0.14, scale:0.72, duration:0.3, ease:'power1.in', stagger:{each:0.005, from:'end'}} +50ms][!#b9b.kc[*] to,{backgroundColor:'#FFB547', scale:1.12, duration:0.3} +400ms][♪accent -2.5dB +450ms]4本に。[silence:1.0s]

# verdict — 札 3 枚が語ごとに組み上がり、最後に要約の 1 行と罫・黒へ溶けて終わる
*** verdict
se pad -2.5dB
@n: [silence:0.5s][chap #prog.lab[8] #prog.lab[9] -500ms]結論です。[>#c1 -450ms][>#c1.no -300ms][>#c1.rm][♪chime -3.1dB]ライトを主力に、[>#arr10 -350ms][>#arr10h -50ms][>#c1.ra -300ms][>#c1.rs]フラッシュは失敗時の切り札に。[silence:0.25s]
@: [>#c2 -450ms][>#c2.no -300ms][>#c2.fr +50ms]月額は923ドルから[>#c2.fs -150ms][>#c2.ar][>#c2.to +150ms][♪accent -2.5dB +700ms]約300ドルへ。[>#c2.y27]2027年でも600ドル弱です。[silence:0.25s]
@: [>#c3 -450ms][>#c3.no -300ms][>#c3.q1 -50ms][♪chime -3.1dB -150ms]品質は同じで、[>#c3.q2 +50ms]速度はライトが最速。[>#c3.cau -100ms][!#c3.cau glow,#FFB54773 {blur: 23} +500ms][=#c3.cau +950ms]男性の声の低音化だけ、[>#er +700ms][>#el +800ms]確認しましょう。[silence:2.8s]
fade out,900ms
```
