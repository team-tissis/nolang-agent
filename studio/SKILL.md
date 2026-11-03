---
name: nolang-draft-studio
description: Write a NoLang video from scratch as draft src (a compressed form of HTML / CSS / GSAP), then finish it with check and render.
---

# NoLang Draft Studio

The writing system — the four compression rules, the studio commands, the asset rules, the grammar differences, the spelling map and what cannot be written — lives in **`libs/ai/llm_prompts/draft_author/reference/spec.md`**. Read it first; everything below assumes it. That directory (below: `REF/`) is the single source of the grammar documents the product's three roles read (`contract.json` names the set): the dictionaries `REF/authoring.md` · `REF/capabilities.md` · `REF/looks.md` · `REF/sounds.md` · `REF/craft.md`, the samples `REF/samples/` and the scaffolds `REF/scaffolds/`. This skill dir's own `reference/` keeps only the dev docs (compare.md · formats.md · stream.md).

## Prerequisites (environment)

- The same dev container that runs the product locally: `/opt/venv` python, Django with the LOCAL DB (`.env`), and the asset catalogs (fonts, speakers, BGM, sound effects, standing pictures) loaded with `manage.py seed`.
- resource-service (svg / html drawing; separate repo `nolang-resource-service`; `PORT=9500 npx tsx bin/server.ts`; reached via `RESOURCE_SERVICE_URL` or localhost:9500). When it is down, render stops with a one-line notice.
- The gpulibs native build (`docker_setup/build_gpulibs.sh`). The render encoder and HLS use CUDA, so a GPU is required (check needs none).
- In a worktree, symlink `.env`, `static/credentials` and `build_gpulibs` from the main checkout. `make link-skills` shows the skill to Claude Code (per clone / worktree).
- The resident server (`studio_server.py start`) is optional. Without it each command boots Django itself (about 7 s slower each). One server per checkout (a second `start` reuses it); it stops itself after 30 idle minutes.
- stream (below) calls the author and the staff via `claude -p`, so the machine must be logged in to the claude CLI (runs on the subscription allowance; one video is worth $0.7–2.7). Environment `ANTHROPIC_API_KEY` / `ANTHROPIC_AUTH_TOKEN` take precedence over the login, so unset them for the author (left set, you get a 0-token response, `author exit 1`, `cut 0`, and the reason in `stream/claude_author.err`).

## Process (resume from the project's state)

- No `brief.md` → read the request and write the brief (format: `reference/formats.md` §brief). If the request has a script, copy it into the brief and use it as-is from then on.
- No `storyboard.md` → write the storyboard from the brief (§storyboard). frame = cut. For each frame decide "the screen's most visible moment", the speech, the changes tied to words, and the length. No grammar at this stage.
- No `studio/` → read the two samples of your type in `REF/samples/` (one winning NoLang src + one `hf_*` port of hf's build) → make the skeleton with `new` → **the design system once in the root** (`palette` `font` `fonts` `motion` `art` plus the `def`s (= classes) for headings, body, cards and boxes (card rows, horizontal bars, flow-chart cards)) → copy the storyboard's frames one by one into `section#名` and `*** 名` (§build).
- No `out/video.mp4` → run `check` down to DEFECT 0 · severe 0 (read the warns and fix what you can) → `render` once.
- Everything there → report (§report). No round trips of reading frames after render to fix things.

## Process rules

- **The brief is law**: one message sentence · audience · arc · format · three look words · voice · must / avoid. Later judgments go back to the brief.
- **The storyboard designs structure, not looks**: each frame has exactly one "what this frame makes clear". A frame's length comes from its speech (4–25 s).
- **Design system first**: as in hf, decide the colors, fonts, text scale, and card / box classes in the root before writing frames. Frame elements apply the classes and write only their differences.
- **Build frame by frame**: 1 frame = a `section#名` design + a `*** 名` speech. Write the frame's "most visible moment" into the design (elements at their fully shown positions and sizes; absolute placement is fine); the entrance is the road there, and the word marks are that moment's changes.
- **Review on check's output**: in the showing-times table, read per frame whether heading → body → changes follow the speech (changes = every mark you wrote · defaults = motion the engine added). Post-render frames are for the report only.

## Loop (one render)

1. Write in the process order (above) → `check` down to DEFECT 0.
2. Reading check: DEFECT = a grammar error (with file:line and the fix; cannot draw) · severe = draws but breaks (fix it) · warn = fix · info = reference. The showing-times table = whether elements are tied to words (its changes column lists every `[!#名]` `[=#名]` you wrote · the defaults column is motion the engine added). The expansion table = def instances' and ×N children's names, boxes and text sizes (marks and position expressions `名.right+8` resolve against these names). `css` warns = dropped declarations (drawn as if absent).
3. `render` once. When a report mentions a visual issue, Read that frame (`out/render_frames/`) and write it with its seconds.
4. For a full-length critique, hand the `tmp/critic/make_sheets.sh out/video.mp4 <dir>` sheets to the subagent `video-compare-opus-medium` (reference/compare.md).
5. Audio runs on `listen` (after render; `--apply` goes as far as redrawing): each cut's audio is played twice to Gemini 3.8 Flash; sounds that do not fit the scene (drops agreed twice) and hammered repeats (repeat) are recorded in `listen.json`, and the next render leaves them out. Loudness is not judged by ear (the engine measures the floor and anchor). Details in `REF/sounds.md`.

Rule names and fixes for check findings: `REF/rules.md` (one rule per line, generated from the two ledgers, check's `draft_check/rules.py` and the product's `quality_rules.py`; silence a rule that does not fit the piece with `lint off=<rule>,…` in the root).

## Making with stream (the product's pipeline — one video from a request)

```bash
bash .agents/skills/nolang-draft-studio/scripts/studio_make.sh tmp/studio/<name> --type concept --aspect 9:16 --request <依頼文の file>
bash .agents/skills/nolang-draft-studio/scripts/studio_make.sh tmp/studio/<name> --edit <video_id> --request-text "<直す点>"   # 完成した動画を直す (下)
```

`studio_make.sh` is the repo's dev entry: it runs the shipped `agent_client/scripts/stream_make.sh` (same flags) with this machine as the run (`scripts/stream_local.py`); with `--remote <api>` it goes to the server like the shipped client.

`--edit <video_id>` edits a finished video instead of writing a new one: the author is skipped, and an editor (Opus · medium · 1 call) reads the video's stored src plus the request and re-emits only the cuts the request touches (per request item it answers patch / rebuild / asset / impossible — `edit/verdict.json`). Untouched cuts submit byte-identical with no staff and no check (they shipped once already); changed cuts get check → fix; only inserted cuts get the staff; a root change re-checks every cut. A rebuild-class item (target seconds, aspect ratio, whole-style conversion) or an editor failure falls back to the author lane with the video as reference (same as `--ref`), and a request with nothing to patch exits 0 after `edit: 変更なし`. `--type` is not needed (aspect follows the parent); `--speech` / `--author-brief` do not combine. Mechanics in `reference/stream.md`.

The author (Opus · low · 1 call) streams the src in cut order; per cut the staff (Opus · medium) finishes it to a professional explainer's density and hierarchy, then check → fix (up to 2) → assets (pictures · voice) → seal → submission, and so it
advances cut by cut. Drawing is the product's DraftStreamRun (`studio.py stream` · one process on this machine) extending the HLS per seal. From the moment the first cut is sealed (90–110 s on a quiet machine)
HLS segments (`static/video_generate/<process>/`) accumulate, and with all cuts done you get `studio/out/video.mp4`. Named definitions (def · motion · run · svg · sound · image · cue) are written in the block of the cut that first uses them,
and only that cut fixes them. The root (settings · cast · the subtitle and BGM opens · persistent layers) is owned by the first cut and freezes when that cut is accepted.
Times are in `stream/run.jsonl` (`first_segment` / `manifest_published` / `final_ready`, plus per cut `staff` `check` `fix` `warm` `submitted` `sealed_ack`); the author's version before the staff is
`solo/author_cut_<名>.txt`, and each cut's doc lives in `weave/<cut>/` (its check findings are the `check` events of `stream/run.jsonl`) (the doc is a window = root + first cut + previous cut + this cut + the cuts that opened still-open spanning layers; definitions outside the window sit behind the root). `--staff none` is no staff (fast, quality drops) · `--staff balanced` (the default; `--seconds` also defaults to `auto` = the author sizes the video to the script, matching `nolang make`) is staff low on cuts 1–2, and from cut 3 on medium only when its predicted finish beats the viewer's arrival at that cut, low otherwise (stall-free start median ~130 → 90 s · a small quality drop · all-medium tails stalled 4 of 10 runs) · `--staff low` also works · `--staff-warn` passes warn findings to the staff too (the default is DEFECT and severe only). Modes bundle the role flags (`--mode light|standard|plus|super`: light = author low, no staff, fix severe · standard = the default · plus = brief author (low), staff balanced with assets, fix warn · super = author high (no brief), staff high with assets, review medium, fix warn — playback starts after 6–10 min and costs twice plus; a role flag written after `--mode` overrides the bundle). Four roles, one flag each ("role name → strength, `none` to drop it"; the same names as `nolang make`): author `--author <effort>` · staff `--staff` · fixer `--fix <defect|severe|warn|none>` (the level of findings it repairs, effort fixed at low: default `severe` = DEFECT and severe findings (hidden text, offscreen …), warns stay unfixed · `defect` = DEFECT and hidden text only · `warn` = the ledger's severe and warn findings too · `none` = no fixer). The review (a director pass over stills after the staff) and the `solo` mode were dropped from the lineup on 10-30 after the mode bench (`stream_run.py --review` survives only as a bench knob); the old `--fix low` is `--fix warn`. By default the staff changes neither pictures nor speech, and pictures and voice are built from the author's version in parallel with the staff (`--staff-assets` lets the staff edit both · `reference/stream.md`). The three roles' prompts are not rule bundles but a professional's brief + grammar + craft (`REF/craft.md`) (10-23 · `reference/stream.md`). Samples default to the two `hf_*` of your type in `REF/samples/` (excluding ones on the request's own topic, same orientation first, first by file name).
To change them: `--samples a.md,b.md` (a previous run's `stream/samples.txt` passes as-is). Quality evidence: the "3 役の prompt" section of `reference/stream.md`.
To hand drawing to the NoLang server: `--remote http://<api> [--token <OAuth access token>]` (assets, drawing and delivery go to the product's draft stream renderer; this machine runs only the author, staff and fixer). The token is an OAuth access token: `NOLANG_TOKEN` from `eval "$(nolang auth env)"`, or the token Claude Code obtained on connecting to NoLang via `/mcp` (OAuth · `mcp.json`) (used automatically when omitted). API keys are refused (403) on these endpoints. Outside the repo (the skill installed as a plugin) only `--remote` works, and check / renames / the rules ledger arrive from the API (the skeletons are `reference/scaffolds/`; plain `python3` suffices). When the plan appears you get `WATCH <url>` (the video page, chasing playback). When a viewer can start playing (status `playable`) you get `PLAYABLE <url>`. A local run (no `--remote`) calls the same receiving ends (submission · warm · check) locally, so the stages and the check findings are identical. The contract is `app_main/docs/feature/video_generate/external_author.md`. If the request carries fixed assets (this photo, this song, this voice), search with the MCP `nolang_assets_search` (scope=mine is your own uploads) and upload local files with `python3 agent_client/scripts/upload_asset.py <file>… --remote <api>` (with the plugin, the skill dir's `scripts/`) (it prints `REF <file> id=<uuid>`; videos wait for finishing, tens of seconds). Write that `ref` (`id=<uuid>` etc.) in the request and the author copies it straight into `image 名 = id=…` / `bgm#名 id=…` / `cast 名 = id=…`.

## Dictionary and how to wait

Read `REF/authoring.md` by section line numbers (Read's `offset` / `limit`): L7 HTML form · L16 Tokens · L33 design.txt · L62 Types · L77 Position · L95 Motion · L106 def and root templates · L167 Subtitles and cuts · L171 timeline.txt · L201 Marks · L220 Timing rules · L229 Cues and transitions · L235 Defects (key names are listed in v2 spelling — `size` `fill` `radius` `shadow` … — but the CSS names `font-size` `background` `border-radius` `box-shadow` … work as written).
render runs in the foreground as `timeout 900 $P $S …`. Sharing the GPU, prefix `STUDIO_RENDER_LOCK=<file>`. If resource-service is down, start it (Prerequisites (environment)).
To compare two videos: `reference/compare.md`.
