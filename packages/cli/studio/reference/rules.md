# Rule names and fixes for check findings

The per-rule fixes for `findings[].rule` returned by check (`studio.py check` / `nolang check` / `nolang_draft_check`, and the render-time lint), generated from the two ledgers, check's `draft_check/rules.py` and the product's `quality_rules.py`. Silence a rule that does not fit the piece with `lint off=<rule>,…` in the root.

- `empty_cut` place a picture or a card
- `shrunk` change the width or the text size (widen the frame / drop `width:` to fit the text / shorten the wording)
- `offcanvas` (severe) move the position inward
- `duplicate_text` a card with the same text as the subtitle → put short key words on screen instead. A card that shows the speech itself (lyric-video lines, speech bubbles) takes `.hide_subtitle` (the subtitle band leaves while the card shows and comes back after it; with `lint off` the two stay side by side)
- `text_overload` more text than the cut's length lets the viewer read → trim the wording to short key words; show it in turns on the words instead of all at once (close the earlier card with `[<#name]`; do not split the cut)
- `spoiler` a heading shows a speech word early → bring it in on its word's mark
- `still_stretch` nothing moves for 6+ seconds (a picture's kb does not count as motion) → add marks on words
- `long_still` (info) the screen does not change while speech runs 3+ seconds → mark a word in that span
- `cut_head_gap` the cut's head is empty for 1.2+ seconds → place the head elements without marks
- `entrance_in_fadeout` it enters too late before the transition or fade out to be read → move the word earlier (a short stamp landing on the last word reads in time and rides the transition — that is fine)
- `entrance_in_transition` a word mark's entrance finishes inside the previous transition's window → add `[silence:+0.4s]` at the head of the first speech to push the word past the window (check says the seconds needed)
- `count_in_fadeout` the count reaches its final value only at the outgoing transition — a wrong mid-count number rides the switch → fire the count on an earlier word, shorten its `ms=`, or add `[silence:+…]` at the last speech's tail (check says the seconds needed)
- `no_closer` the last cut has no big closing line
- `same_picture` the same picture for 15+ seconds → swap to another picture, diagram or card on a word inside the cut (do not split the cut)
- `blank_band` a third of the screen is bare ground at the cut's head → lay a full-bleed picture, or put a card on the band
- `transition_label_flash` the panel curtain's label rides the band, so it is readable only while the band holds (the sweeps take 0.7 s; the rest of the ms is the hold — 100 ms at 800) → lengthen the panel to the ms check names, or cut the label to a glance (a number + one short word)
- `double_exit` a cut that ends on a transition also has a whole-cut out, so the scene fades and then the transition runs (it dies twice) → to end on a fade, make the transition `transition cut`; if the transition carries the scene, drop the section's out (for a transition inherited from the root, the machine turns it into a cut)
- `persistent_chrome` persistent layers (progress / chapter numbers / running totals) belong only in videos of 3+ minutes — in a short video the cost of occupying a screen edge outweighs them, so drop it
- `sparse_cut` 4+ seconds with few elements → add a picture or a card
- `palette_drift` inline colors in hues off every root palette hue (tints and shades of a palette hue do not count) → add the hue to the root's `palette`
- `low_contrast` little contrast between text and its ground (also after a dimmed `dim` / focus sibling or `recolor`) → dim deeper
- `overlap` text of the same family overlaps (warn even with `overlap:` declared; hiding another family's text is the severe occluded) → move the stamp / card off the other text
- `title_on_close` the first cut's title is never closed and remains in the last frame → `[<#name]` (to restate the name at the close, make a new layer in the closing cut)
- `leaks_into_next_cut` (info) other layers exit before the transition and only the out-less layer remains into the next cut's head (the default is that everyone rides the transition alive — only the author's out divides who stays and who goes) → to align them, write out on the other layers too, or drop this one's out
- `orphan_line` the wrap's last line is 1–2 characters (「本気だっ / た。」) → tighten the wording, shrink the text, or break with `[br]`
- `overridden` the engine changed a written value (with a cause) — subject_clear: place the text off the picture's subject / icon_square and late_admission: the engine's alignment (no fix needed)
- `transition_over_speech` the transition overlaps speech
- `se_dense` sound effects are dense (`sfx off`)
- `running_total` a running-total card's value decreases across cuts → copy the totals written in the plan
- `font_not_pinned` the font could not be resolved as in production and was measured with the default font (run check where the DB is; bring the font description closer to a catalog font)
- `synthetic_bold` the family has no bold face (there is no browser synthetic bold) → pick a family with weights via `font-family:` or drop the font-weight
- `ghost_dissolve` in a 400 ms+ dissolve, the previous cut's large text or picture shows through into the next cut (a layer without out, or a transition dissolving from before the boundary) → `transition dissolve {duration: .4, overlap: .4}` (text with out finishes fading by the boundary); pictures and cards without out take `[<#name fade]` at the cut's end
- `photo_hidden` a veil of opacity 0.7+ covers 90%+ of a full-bleed photo for 3+ seconds (the photo washes out / sinks dark) → move the photo to one side (text on the ground side), or cap the veil at 0.6 and put a band / board only under the text
