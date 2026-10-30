# Sound effects — the loudness hierarchy and the by-name sound table

Catalog sound effects are all normalized to a momentary max of -23 LUFS (voice is -17). Left as is, the click for a new row and a climax
fanfare play at the same loudness. Videos that sound natural (measured on hf) span 9 dB: decoration -25 to -28 / events -22 to -24 / climaxes -16 to -20.
So:

| Tier | What sounds | How to write | Loudness |
|---|---|---|---|
| Decoration | pops of boxes and pictures, transition swishes, count-ups | automatic (`sfx on`); if you write one yourself, `-8dB` (a transition sound `-12dB`) | appearance -8 dB, transitions -12 dB, emphasis -5 dB (automatic defaults) |
| Events | impacts, falls, pickups, warnings, transformations, confirmations | `[♪"名"]` (0 dB) | 0 dB |
| Climaxes | fanfares, stings (ジャン!), booms (ドーン), cheers, result reveals | `[♪"名" +3dB]` (once or twice per video) | +3 to +5 dB |

Rules:

- **At most 3 per cut** (automatic sounds don't count). Don't answer a motion finding with a sound (fix motion with motion). If the lint `se_dense` fires (8+ in 5 seconds), cut some.
- Automatic sounds are added by compile to the timeline it renders as `[♪"…" -8dB]` (at a transition boundary, the sound of that transition's `切替音` family — e.g. `se "カメラモーション03-09(中高　リバーブ)" -12dB -200 to=800` for a 400 ms dissolve at the head of the next cut; transitions under 400 ms get no automatic sound) (your timeline.txt does not change; only at the front of your own marks, `[>#名]` and `[!#名 count|check|pop|…]` — marks the defaults added get none). Per element, the declaration `se: "音"` swaps the sound and `se: none` removes it (a removed sound still counts as played for thinning — removing the head of a run does not move the sound to the next element). Write `se=` on a transition and only that one shot plays.
- Text, diagrams and arrows make no sound on appearance (a click on every text entrance sounded cheap and plinky). On a word where the author wrote `[♪]`, that word's automatic sound does not play (no doubling). Identical automatic sounds at the same instant fold into one shot.
- **Automatic sounds (`sfx on`) are thinned per cut by compile**: one shot per word, and across words the same sound stops playing from the second word in a row (the count restarts at a word with a different sound). Even in a build where every sentence head gets the same pop (`cut { stagger: sentence }` + `in: card`), the pop plays only at the head of the run. The author's `[♪]` / `se` are never thinned, and no automatic sound is layered on that word (it does count toward a same-sound run).
- **The loudness of a shot is placed by the engine from the floor**: the engine adds the gain that puts the asset's max 2 LU above the floor at the instant of firing (voice if present, else music, else silence) (+8 dB during speech; clamp −6 to +9). The author's `-6dB` is relative on top of that, meaning "a little below the floor". Write 0 dB and it will be heard. Ambience (`to=end`) is not floor-relative.
- **Cut sounds longer than 3 seconds** (`se_long`). The mixer plays across scenes to the end, so a 23-second chime keeps ringing under the next 3 cuts. When a shot with no written length intent (`to=` `peak=` `start=` `fade=`) lands on an asset over 3.5 seconds, the engine cuts it at 3 seconds and eases out over 600 ms (insurance for when a description-matched shot lands on an ambience loop). An end stopped with `to=` eases out over 300 ms unless you write the tail of fade= (no abrupt cutoff). Identical sounds at the same instant (word + offset) are folded into one shot by the engine.
  A sound with a peak: align the peak to the word with `peak=山の秒` and end with `to=` or `fade=0,600`: `[♪"ドラムロール" peak=4.4s]` = the 4.4-second peak lands on the word (it starts playing 4.4 seconds earlier).
- To layer, offset and lower: `[♪"打撃　パンチ03-1(ドライ)"][♪"打撃　パンチ03-4(ディレイ)" -4dB +160]` (hf's impact + reverb).
- Writing by name keeps retrieval stable (the names in the tables below exist under the same names in LOCAL / STG / PROD). Sounds not in the tables are written as descriptions (`[♪"氷がピキピキと凍る音"]`).
  The length of a description-matched sound shows in the src.json pin (`duration_ms`) or in check's `se_long`.

## BGM: listen to candidates and choose (engine)

The description on a `bgm` line pulls an embedding search window (top cos; at a spread of 0.03-0.05, rank 1 is effectively a tie-break), and when the video has a request text,
20-second excerpts of the top 5 tracks are played to Gemini 3.8 Flash in 3 different orders and tracks with 2+ votes win (`_pick_bgm_by_listening` in adapters,
libs/ai/bgm_listen_pick.py). 10-14 bench (human ears as ground truth, 10 queries): rank-1 match 2 / 10 → listen-and-pick 7 / 10. Without a request text it is 3 / 10, so
in the studio the run dir's `request.txt` (placed by stream_make.sh) or src.json's settings.title serves as context. With no context, nothing to listen to, or a split vote,
a picker (Jev) chooses by description from the same discovery window as sound effects (top-40 cos + name match + vocabulary match) (`_resolve_sound_effect_by_pick`).
Named picks (display-name matches) skip the listening.

## Listening check (`studio.py listen <project>`)

Pass each cut's audio of the rendered video (voice + BGM + sound-effect mix), the firing table (id, seconds, name, dB, role, description) and the speech to Gemini 3.8 Flash, and have it return
`keep / drop / replace / repeat / too_quiet / too_loud` as an enum per firing. Each cut is heard twice with the table order reversed; **`repeat` on 1 vote,
`drop` on 2 matching votes** are recorded into the drops of `listen.json` → the next `render` removes that firing from the VC (`--apply` re-renders right away).
`replace` stays a suggestion even on 2 matching votes (the same description lands on the same sound — rewrite the description as onomatopoeia + one source). `too_quiet / too_loud` are not adopted
(10-14 measurement: Flash answers keep for buried sounds; loudness is handled by the engine's floor / anchor). One call p50 4.5 s / 2-3 yen per video.
A second or later listen carries the previous drops over without showing them in the table. Results land in `out/listen_report.md` (a verdict table of all firings).

## Sounds tied to pictures (ambience and foley) — where hf still leads

In the p8 verdicts over 20 videos, only hf was praised for sound (6 times: the balance of water and ambience, the sizzle of pouring, the "ペタペタ" text with its sound effect). NoLang got 0, and
the measured src had 0 `se` lines, 1-7 uses of `[♪]`, and ambience (long `to=` sounds) in 5 / 20 videos. What is missing is not the number of sounds but sounds tied to the picture:

- **Ambience**: one at the head of a full-picture cut (`se "早朝の商店街の環境音、遠くの鳥" -8dB to=6s fade=300,1500`; cut it at the cut's length; change it whenever the place changes). Loudness −8 dB: p9's −12 to −16 dB sank below the BGM (−33), and the floor in voiceless moments sat 8 LU lower than hf (hf's story floor is 7-10 LU under the voice).
- **Foley**: one on the word of an action inside the picture (`[♪"グラスに酒を注ぐ澄んだ音" -6dB]`; steam, water, fire, footsteps, paper).
- **Onomatopoeia text**: `[♪]` on the same word (`p#名(…) ペタペタ` + `[♪"ペタペタと貼る音"]`) — never the text alone or the sound alone.
- Decorative pops (`sfx on`) win no praise. story / cinematic may go `sfx off` and keep only ambience and foley.

## Transition sounds (`切替音 …`)

Every transition of 400 ms or more except `cut` / `none` gets its matching `切替音` automatically, at −12 dB (quieter than the pops, well under the voice; quick melts under 400 ms stay silent unless you write `se=`; a family written without a dB plays at the same −12 dB): a family of real catalog sounds chosen for that kind of motion (one smooth swell whose loudest moment the engine lands on the transition's peak, so it never sounds early or late). A `panel` band moves twice (sweeps in, holds, sweeps out), so its sound is built on the spot for that band: one swelling sound is split at its peak, its swell lands on the moment the band covers the screen and its fall plays again as the band leaves, each part as long as that band's own cover and leave (the band families below). Write `se=` on a transition only to change that default; then another `切替音` family, or any other catalog sound, plays on the same peak. To keep the automatic one but change its loudness, write its family (`se="切替音 ふわっ" -4dB`; `se="切替音 帯" -4dB` on a panel keeps both parts) — a written family plays exactly as the automatic one would (same peak alignment, same length), only its loudness changes.

| Transition | Automatic | Variants |
|---|---|---|
| `panel` | `切替音 帯` (a light whoosh) split in two: in on the cover, out on the leave | fitted to the band's own ms |
| `wipe` `push` `slide` `zoom` · `dissolve` with `dir=` | `切替音 掃き` (a quick whoosh) | `短` ≤ 600 ms · `長` longer |
| `dissolve` | `切替音 ふわっ` (a soft, airy whoosh with a gentle tail) | `短` ≤ 600 ms · `長` longer |
| `dip` | `切替音 暗転` (a low, deep whoosh) | `短` ≤ 600 ms · `長` longer |
| `flash` | `切替音 閃光` (a bright shining ping) | `短` ≤ 900 ms · `長` longer |

To give a film its own transition voice, write a family name alone — `se="切替音 ポロロン"` — and the engine picks the version fitting each transition's direction and length (also for the automatic families above: `se="切替音 掃き"` on a dissolve). A one-shot family sound is also cut to the transition: it stops 600 ms after the window ends (300 ms fade), so a long-tailed asset never outlasts the switch; the band's two parts are sized from the band. **`se=none` makes a transition silent** — put it on the root `transition=` of a quiet film (cinematic, story, anything the ambience carries): a whoosh on every cut of a hushed scene is noise, and the picture and ambience carry the join; sound only the one turn that deserves it. These families are the catalog's own scene-change sounds (one series each, so every version shares the timbre); each lands its loudest moment on the transition's peak. One family per film, two at most (a different one for chapter bands).

| Family | Sound | Fits | Versions |
|---|---|---|---|
| `切替音 ポロロン` | a xylophone run | variety, kids, cheerful explainers | `上へ` / `下へ` (`dir=down`) × `短` / `長` |
| `切替音 テレレーン` | a bright synth-bell run with a ringing tail | TV variety, a new topic | `上へ` / `下へ` × `短` / `長` |
| `切替音 ピロロ` | an electronic trill | games, apps, pop and playful | `上へ` / `下へ` |
| `切替音 シュワーン` | a tonal whoosh traveling across | TV energy, news, sports, tech | `左へ` / `右へ` / `中央` |
| `切替音 シュッ` | a short swish | quick, plain pace | one |
| `切替音 ブワッ` | a soft rushing swell | a flashback, a mood shift (`dissolve`) | one |
| `切替音 キラキラ` | a shimmering chime | elegant, magical, a discovery | `短` / `長` |
| `切替音 キラーン` | a whoosh into a sparkle | a reveal, a bright answer | one |
| `切替音 シャララン` | a harp-like glissando | gentle, warm, a happy turn | one |
| `切替音 ドーン` | a deep impact | dramatic, a shock, a chapter opening (`panel`, `dip`) | `短` / `長` |
| `切替音 リバース` | a reverse swell that stops on the peak | just before a reveal (`zoom`, `flash`) | `短` / `長` |
| `切替音 グリッチ` | crackling digital noise | tech, cyber, unease | `短` / `長` |
| `切替音 パラパラ` | a book's pages flipping | study, history, a story (`slide`, `push`) | one |
| `切替音 カシャ` | a camera shutter | photos, a snapshot | one |
| `切替音 ポン` | a round pop | cute, light | one |
| `切替音 パチン` | a finger snap | a quick switch, "and then —" | one |
| `切替音 拍子木` | wooden clappers (two strikes) | Japanese, period, a curtain (`panel`) | one |

`短` / `長` for these families = the time from the transition's start to its peak (half a wipe / dissolve / dip, a third of a flash, a band's sweep in): `短` up to 0.3 s.

Band families split in two on a `panel` (in on the cover, out on the leave — fitted to that band's ms); on any other transition they play once on the peak. `ブワッ` above is one too. Pick one for the film's chapter bands:

| Family | Sound | Fits |
|---|---|---|
| `切替音 帯` | a light whoosh (the default) | any chapter band |
| `切替音 フォン` | a low, soft whoosh | calm, serious, business |
| `切替音 シャーッ` | a curtain drawn | a stage, a story's next act |
| `切替音 ビュン` | anime speed lines, falling pitch | energetic, anime, sports |
| `切替音 ピュイーン` | a bright electronic rise | TV variety, a new topic |
| `切替音 ギュイン` | a flashy synth whoosh | games, hype, tech |
| `切替音 ピシュン` | a thin, high digital sweep | tech, cyber, data |
| `切替音 ザザッ` | 8-bit noise | retro games |
| `切替音 鈴` | a shake of kagura bells | Japanese, shrines, seasons |
| `切替音 シャカッ` | a slow shaker | soft, cozy, lifestyle |
| `切替音 ヒューイ` | a slide whistle | comedy, a silly turn |

## Sounds by name (use → catalog name, length, peak position)

`peak` is the second where the momentary level is highest (absent = a short sound that plays from the head). `±` is a loudness guide.

### Decoration (same family as the automatic sounds, -5 dB)

| Use | Name | Length | Notes |
|---|---|---|---|
| Appearance of boxes, pictures, copies (pop) | `オノマトペ 弾ける01-1（ドライ）` | 1.8 s | the automatic pop |
| Count-up click | `アソート効果音05-14` | 1.7 s | the automatic click (count) |
| Swish (fast swing) | `風切り１-２` | 0.4 s | the automatic sound of `in=travel` |
| Whoosh as the screen moves sideways | `カメラモーション06-1(中)` | 1.0 s | for wipe / slide |
| Opening hit (noise sweep) | `ノイズスイープ03-04(ドライ)` | 0.6 s | second 0 of the video |
| Small cue at a scene head | `ひらめき02-1（高）` | 1.7 s | hf's step |
| Small sparkle | `キラリン 21` | 2.2 s | where a card gets its ✓ |
| Stamp | `判子を押す` | 0.5 s | the automatic stamp |
| Electronic confirm (beep) | `決定音` | 0.5 s | UI |
| Phone notification | `スマートフォン UIサウンド01-09（スピーカー）` | 2.0 s | |
| Shutter | `カメラのシャッター音` | 0.6 s | |
| Page turn | `ノートをめくる音` | 6.5 s | peak 1.7 s, `to=2s` |

### Events (0 dB)

| Use | Name | Length | Notes |
|---|---|---|---|
| Heavy impact | `打撃　パンチ03-1(ドライ)` | 0.5 s | layer `03-4(ディレイ)` -4dB at +160 ms for reverb |
| Impact reverb | `打撃　パンチ03-4(ディレイ)` | 1.6 s | for layering |
| Light impact (comical) | `戦闘08` | 0.2 s | |
| Falling over (thud) | `SNES 格闘06-12（倒れる）` | 1.8 s | |
| Landing (plop) | `SNES 格闘06-11（着地）` | 1.8 s | |
| Lifting (rising whistle) | `スライドホイッスル01-1（短 上昇）` | 1.8 s | |
| Success chime | `正解01-2` | 2.0 s | the automatic ok (the `$ok` color) |
| Ding-ding (correct) | `クイズ　ボタン01-4(シングル)` | 1.3 s | |
| Failure buzzer | `クイズ　ブザー02-2(短)` | 0.3 s | the automatic bad (the `$bad` color) |
| Warning (short alarm) | `アラーム01-3` | 2.2 s | |
| Warning (siren) | `警告音 サイレン05-01（速 中）` | 3.7 s | peak 0.5 s, `to=2s` |
| Attention (ping) | `注目 1` | 2.4 s | |
| Insight (ding) | `ピーン！/閃き３` | 0.8 s | |
| Level-up / heal | `レベルアップ、回復` | 0.8 s | |
| Power-up | `パワーアップ01` | 0.6 s | |
| Item pickup | `SNES アクション01-16（アイテム）` | 1.8 s | |
| Money / treasure | `お金・財宝・アイテムゲット` | 2.1 s | |
| Loose coins | `小銭をチャラチャラ` | 1.6 s | |
| Transformation (shing!) | `オノマトペ シャキーン01-1（長）` | 2.7 s | for something light, `05-4（軽 ディレイ）` 5.7 s |
| Power-down / stop | `DJのスピン・スクラッチ風SE` | 2.3 s | a record grinding to a halt |
| Glass breaking | `コップが割れる` | 1.4 s | breaks a silence |
| Explosion | `爆発06` | 1.0 s | |
| Door | `ドア05` | 0.7 s | |
| Diving into water | `水に飛び込む` | 3.1 s | |
| Chime (bell) | `チャイム12` | 2.0 s | |
| Letdown (trombone) | `フレーズ04-1` | 7.1 s | `to=2.5s` |
| Laughter | `爆笑3～6名` | 4.5 s | `to=2s` |

### Climaxes (+3 to +5 dB, once or twice per video)

| Use | Name | Length | Notes |
|---|---|---|---|
| Surprise (sting) | `ジャン！・驚き` | 1.0 s | also for a title's appearance |
| Fanfare | `フレーズ01-1` | 3.1 s | the "呼べる!!" kind of moment |
| Cheers + applause | `歓声 イェイ01-4（高 拍手）` | 2.6 s | layer at -4dB, +120 ms after the fanfare |
| Applause (short) | `拍手04-3（短）` | 3.9 s | `to=2s` |
| Drumroll → cymbal | `結果発表01-2` | 8.0 s | build-up → reveal; `peak=` puts the peak on the reveal word |
| Drumroll (plain) | `ドラムロール` | 6.2 s | peak 4.4 s → `[♪"ドラムロール" peak=4.4s]` |
| Deep bass impact (boom) | `オノマトペ 衝撃13-2（長）` | 8.8 s | peak 0.5 s, long reverb → `to=2.5s fade=0,800` |
| Heartbeat (tense build-up) | `心臓の鼓動音` | 5.3 s | peak 3.3 s, `to=3.5s` |
| Game clear | `ベルのゲームクリア音` | 3.7 s | |

### Long sounds (ambience, loops) — `to=` required

| Use | Name | Length | Notes |
|---|---|---|---|
| Clock ticking | `時計 秒針01-1（ドライ ループ）` | 7.7 s | `to=` only for the build-up |
| Wind | `風03` | 4.4 s | |
| Footsteps | `足音` | 14.0 s | |
| Typing | `キーボード` | 23.9 s | |
| Sparkles (long) | `オノマトペ キラキラ01-2（短）` | 9.0 s | 9 seconds even though named 「短」 |

**Leave music loudness and ducking to the engine defaults**: just `bgm#music 説明`; during speech the music sits 11 LU under the voice, in long pauses (over 1 second) and at the tail it automatically steps 2 dB forward (duck −2, attack 200 / release 500; it does not come back up in sentence breaks under 0.6 s), and after the last word it steps forward and fades away. Do not write `volume:` (the default +7dB = 9 LU under the voice = hf's loudness; lower it too far and the music becomes inaudible behind the speech). For an instant where ambience should stand out, stop the music with `[<#名]`. `bgm#名(duck: off)` is only for when the music is the lead.

A track shorter than its layer's length repeats on a cycle (the default; the track's tail fade becomes the seam as is, so pick a long track for a long video). Lowering / restoring the BGM on a word is the marks `[!#music to,{volume:-13dB, duration:.1}]` … `[!#music to,{volume:0dB, duration:.6}]` (dB from the track's default loudness; they stay attached to the word even when the speech length shifts); a build-up measured from the tail is the root's `bgm#名(keys: "end-6s:-9|end-4s:0") 説明`. To change tracks, write a mark-only line `[<#名]` at the end of the previous cut → `bgm 名2 -1500` at the head of the next cut (with `bgm#名2 説明` in the design root; -1500 = a crossfade overlapping the previous track's fade-out by 1.5 seconds); for an impact cut, write only `[<#名 -400]` at the end of the previous cut and let the ambience carry it. Unwritten fades are 1.5 s / 2 s (at a switch the previous track's last 2 seconds overlap the next track's first 1.5 seconds; at the tail the track plays through 1/3 of the silence after the last word (default 3 s) before fading — write a shorter silence and the afterglow shrinks too).
