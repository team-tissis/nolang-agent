# Story

Read before building any video that tells something over about 15 s: a launch or promo, an explainer, a pull-request or changelog video, a recap, a music video with a narrative. Most weak films are good motion around no story: a list of features, three cards in a row, a logo, a URL.

Skip it for an edit to an existing project, captions or overlays on footage, and a short single-idea piece (one kinetic line, a map move, a highlight on an image), where the request is the story. When the person gave a script, a storyboard or a reference film, follow theirs. The shape of each kind of film (launch, explainer, music, data, vertical, 3D, character) is in `types/`.

## 1. The one thing

- **What it is**, in one line: "You can now …" for a launch, the one idea the viewer must understand for an explainer, what changed and why it matters for a pull request. A whole release ("2.0", "what's new") is not one thing: take its headline.
- **The one thing to remember** after the film ends, in the viewer's words, not the brand slogan.
- **One viewer doing one real task**, from the moment they need it to the result. That task is the spine, and one real piece of data (a query, a file, a prompt, a number) travels through it from the hook to the payoff. An explainer's spine is one concrete example worked through.
- Keep facts (what it does, real numbers, real labels) apart from creative choices (angle, tone, look). Every claim on screen traces to the source: the site, the PR, the docs or the person's words. Use the person's own copy verbatim.
- What the source does not say stays unsaid: never derive a claim it did not make ("40 min to 2 min" is not "20× faster"), mark an example number as illustrative, and show a screen you cannot get as a labelled placeholder, not a drawn one.

## 2. Three storylines, then one

Write three. They are three different films, not three titles on one film: each has its own **world** (where it happens and what it looks like), its own **device** (what the story is) and its own **form** (how the camera and the cuts carry it). Sketch five or more ideas first, a line each pairing a device with a form (tables below); drop those the subject cannot carry well, and of the rest keep the three that differ most. Make one of the three the bold one you would not have picked first. Each says:

- its name, its device and form in a few words, and in two sentences what the viewer sees and feels;
- the first two seconds, exactly;
- its beats in one line (`hook → … → end card`);
- its look in one line: ground, type, the one material or treatment, taken from the subject or the brand (`look.md`);
- its sound in one line (`sound.md` §1).

The storylines are words: build nothing for any of them before one is picked. Pick a storyline for its story: the one a stranger would follow and remember, with people or a situation they know, ahead of the most striking picture. Picking a storyline picks its look and its sound. Then write the picked one as `SPEC.md`.

- With a storyboard (`storyboard.md`), the picked storyline becomes the board's frames.

| Device                        | What the viewer sees                                                                    |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| A moment in someone's day     | a person, a time stamp, the message that creates the need ("launch is tomorrow")        |
| A character does the work     | a mascot or a cursor carries, drags, draws and reacts; every cut has a cause            |
| The feature as the hook       | the feature happening to a recognisable image in the first half second                  |
| The result first              | the finished output plays, then the camera pulls back to show where it came from        |
| One object across apps        | the thing being made travels from one app into the product, which keeps working on it   |
| Life before and after         | the old way as a scene (one person drowning in tabs), then the new way                  |
| Type carries the argument     | giant kinetic type, colour fields and grids that cut on the beat                        |
| A number lands                | one real number earned by a scene, then made physical                                   |
| A question with the input     | "What if you could make a video from your ⟨website⟩?", the blank filled by a real input |
| The object is the explanation | a machine or model whose working is the idea; the camera tours through it               |

| Form                       | What the viewer sees                                                                         |
| -------------------------- | -------------------------------------------------------------------------------------------- |
| One continuous take        | the camera never cuts; it pushes, pulls and travels from one world into the next             |
| Object-to-object chain     | every shot ends on the thing that opens the next: a button becomes a card becomes a phone    |
| An endless zoom            | the camera dives into a detail that turns out to be the next world, again and again          |
| A flight through one world | a 3D set, a map or a desk the camera travels across; each idea is a stop on the route        |
| Cut on the beat            | hard cuts on the music, type and colour fields changing every half beat                      |
| Match cuts                 | one shape holds while everything around it changes: a circle becomes a lens, a wheel, a logo |
| Split screen to one        | several panes play at once, then collapse into the one that matters                          |
| One frame that rebuilds    | a single composition keeps rearranging itself and never leaves the frame                     |

A pitch where all three are plain cuts between scenes has not tried the forms. Before and after: the new side moves calmly while the old side churns; never mock a named competitor. A recap asks one question first so each piece answers it.

## 3. The hook

The first two seconds are the densest of the film, and frame 0 is the thumbnail: never black, never a logo alone. Open on the feature working on something recognisable, a real moment that creates the need, a question with the input inside it, a sentence whose last word becomes the picture, or the bug itself. Then let the old way fail on screen (the wait, the wall of text, the wrong result) before the product brings relief; the proof is often the same shot improved in front of the viewer. Typing into a prompt box as the opener, with nothing else on screen, is the tell of a generated film; as a story step a few seconds in, it is fine.

## 4. Beats

A common shape for a launch of about 35 s; scale it, let the device bend it, and take another type's shape from its file in `types/`:

| Beat     | Share | Job                                                                                       |
| -------- | ----- | ----------------------------------------------------------------------------------------- |
| Hook     | ~8%   | the world and the need, or the feature already working                                    |
| Tension  | ~12%  | the old way failing on screen, or a gag                                                   |
| Reveal   | ~8%   | the product or idea named as a title, about 20–30% in                                     |
| Proof    | ~40%  | the real task in the real UI as 3–6 verbs (_paste, pick, watch it build, ship_), one each |
| Payoff   | ~20%  | the output arrives, already moving: the biggest visual moment, once, 60–80% in            |
| Claim    | ~8%   | the one thing, in one line                                                                |
| End card | ~8%   | the mark carried in, the name and the call to action land and hold 2–3 s                  |

In each verb beat keep only what the cursor touches and what proves the line; delete the rest of the screen. The process runs fast; the payoff plays at normal speed. Length follows the story (a feature launch is usually 20–45 s); a length in the request is a range, never padded.

## 5. Worlds

A film visits several worlds, each with its own background, light and scale (a desktop, the product on a brand gradient, a white void with a character, live action), never one dark canvas with small UI floating in it. Enter each world through an object already on screen: the thing clicked becomes the next shot. Keep one home stage to return to, one carrier the eye follows, and the palette and type constant across worlds.

## 6. Copy and voice

- Titles take at most 6 words a line, one line on screen at a time, no trailing periods; an explainer's lines may run to about 10. A line holds about 0.3 s a word plus 0.5 s, and the last line at least 2 s.
- Show, don't list: no bullet slides or three-card rows. When similar things repeat, each gets its own idea and layout.
- Real numbers only, from the source. The first line is never "Introducing", "Meet" or the logo; after the pain, "Introducing X" is fine. Never "unlock", "seamless", "supercharge", "game-changer", "revolutionize", "effortless", or "in seconds" unless measured.
- Read the lines alone: a stranger gets the pitch. Watch the pictures alone: they tell the same story.
- No voiceover unless the request or the source calls for one; then the screen never repeats the spoken sentence word for word. Without a voice, large titles and the product's own text carry the words, over music and effects (`sound.md`).

## 8. Tells of a generated film

The defaults a film falls into when nothing is decided are banned by name in `spec.md` ("BANNED by default"): a dark void with small things floating in it, glow and particles, the cream-paper-serif-mono-label look, everything fading and sliding up, three cards in a row, the docked logo. Beyond those, for a story:

- every scene entering the same way, or the same move beat after beat;
- side-by-side panels and floating cards standing in for a scene;
- titles that keep sliding or shrinking after they land; breathing or floating loops standing in for motion on titles and UI (a character's idle breath is acting, `types/character.md`).

When a first render shows any of them, name which, take the replacement from the subject, the brand or the medium, and add it to the BANNED line of `SPEC.md`.


# Explainers, tutorials and "how it works"

One idea the viewer understands by the end (`../story.md` §1). The spine is one concrete example worked through, start to finish, not a tour of facts. Usually 30–90 s.

## Ground it first

Start where the viewer already is: a person, a place or a situation they know, and a question they would ask about it ("why does the astronaut come home younger than her twin?"). The abstract device (a light clock, a graph, a field) enters inside that situation, as the thing that answers the question, and the film returns to the person at the end with the answer. A film that opens on the device alone is a diagram, not an explainer.

## Devices that explain

- **The object is the explanation.** Build a thing whose working is the idea: a machine, a model, a map, a light clock, drawn so it reads as what it is (its material, its mount, where it sits in the scene). Every number on screen comes from it, and the camera tours through it: cutaways, an exploded view, a dive into the part that matters.
- **One diagram that grows.** Start from the simplest true picture and add one part per beat, each appearing when it is named; never a finished diagram dropped on screen at once.
- **Continuous transformation.** Each step morphs out of the last (a bar becomes an axis, a dot becomes a population), so the viewer never loses the thread to a cut.
- **The worked example.** One real input (a sentence, a number, a photo) travels through every step to the answer.

## Shapes of information

Most explainable lines are one of a few shapes, and each has its own picture: a number that lands (`data.md`); a myth turned over (the wrong idea struck through, the right one printed over it); before and after; many things converging into a few groups; a network that densifies; one chosen out of many; steps in order; a real screenshot with the detail circled; a quote set as a poster; a chapter card. Pick the shape first, then the picture, so similar lines get different pictures and every line gets the one that shows it.

## Words

- Narrated: the voice is the clock (`../sound.md` §2). Reveal each part when the voice names it, across the back half of the scene; keep a scene to about 19 spoken words (`../film.md` "Script and pacing").
- Not narrated: large lines carry it, up to about 10 words, each held 0.5 s + 0.3 s a word.
- Labels sit on the part they name, with a leader line when needed, and appear with it. No legends, no bullet slides.

## Getting it right

- Every claim, value and step traces to the source; a number the source did not give is left out or marked illustrative. One data module drives every figure so the numbers agree with each other.
- Check the science or the logic of each step before animating it; a beautiful wrong diagram is worse than none.
- End on the one idea in one line. No brand end card unless asked.

## Tells for this type

A slide of bullets; icons in circles; three cards in a row; the whole diagram at once; a narrator repeating the text on screen word for word.


# Numbers, charts and data stories

## One number at a time

- A number is earned by the scene before it, then made physical: a count that becomes a skyline, a share that becomes a crowd.
- The number is the biggest thing on screen. Tabular figures (`font-variant-numeric: tabular-nums`) so a count-up does not jitter; a count-up runs 1.2–1.6 s, then holds.
- Real data only, from the source, rounded the same way everywhere, with a small source line on screen. One data module drives every figure in the film.

## Charts as pictures

- Build a chart in reading order: the frame and axis, a reference line, then the data drawing in, then one annotation on the point that matters. Annotate on the mark; no legends.
- Highlight one series, grey the rest. A chart with one thing to say says it in its title.
- The same object carries across beats: a bar becomes the ground of the next scene, a line becomes the road the camera follows.
- The camera can dive into the one value that matters, then the rest falls away.

## Tells for this type

A grid of KPI cards; a dashboard; a pie chart; every number counting up at once; numbers with no source.


# Characters, mascots and story shorts

A character gives every transition a cause and gives the film its jokes: it carries the result into the player, rejects its own first try, reads the manual. After Effects characters come in through Lottie (`../runtimes.md`).

## Acting

- Mood changes go through a take: anticipation, a squash, the new face, a settle. A face never snaps from one state to the next.
- Squash and stretch, anticipation, overshoot and follow-through belong to the character. Here an idle breath or blink is life, not a tell; the tells about breathing and bounce in `../motion.md` are about titles and UI.
- Code moves every part at once, on one curve, by the same amount. Offset the parts (head leads, arms follow), vary the amounts, and never move both arms, both eyes or a crowd in unison.
- Contact sells it: feet on the ground, props held by the hand, eyes on what they look at.

## Reads

Each action is one read. Lead the eye to where it will happen, play the action fast, and let its meaning land slowly: hold the reaction. A sign or caption that repeats what the action already shows is the classic failure.

## Build

- A rig is a set of parameters over time: position, squash, arm angles, an eye state and a mouth state per moment. Write mood changes as keyed states (`[[t0,"normal"],[t1,"scared"]]`) the rig eases between.
- Hand-drawn life: redraw the outlines about 12 times a second with a jitter seeded by `Math.floor(t * 12)`, so the line boils while the character holds still, and every render matches.
- A long piece is one chapter per sub-composition, all drawing from the same rig and helpers.


# Motion

## Motion craft

Measured frame by frame from official launch films. These are defaults: a reference the person gave, or a Moment that does otherwise on purpose, wins for its own beat.

- **Moves**: a fast move takes 0.3–0.6 s and carries motion blur on its own ease, peaking at its fastest frame: 6–12 px on text-sized elements, 15–20 px full-frame, horizontal-only on a horizontal move. One move is one tween.
- **Arrive slow, leave clean**: long-tailed ease-outs on arrivals; landing takes longer than leaving. An exit is one smooth motion, never slide, stop, then leave. Entrances that are too snappy read as glitches; slowing the whole video by about a second often fixes it.
- **Ease by role**: an arrival lands on a long tail (`expo.out`, `power4.out`), a camera move or a colour flood eases both ways (`power2.inOut`), a zoom through or an exit accelerates (`power3.in`). The same `power2.out` at 0.5 s on everything is the flat default that makes a film feel generated. Linear only for rotation, progress and constant speed that is the point.
- **Springs** are named by damping ratio: 1.0 never bounces, 0.7-0.85 reads premium, 0.4-0.6 playful, under 0.3 a cartoon. Position and size may bounce; opacity and colour never do. GSAP's `elastic.out(1, 0.5)` and `back.out(1.4)` are the nearest built-ins; a closed-form spring of `t` keeps any frame renderable on its own.
- **Exits** are 40-50% shorter than their entrances. **Overlap**: the next element starts when the previous is 30-50% done; fully sequential looks robotic, all at once looks cheap. **Stagger**: letters a frame apart, words 60-120 ms, list items 40-80 ms.
- **Beat grid**: frames per beat = fps × 60 / BPM; compute each beat from its index and round it, never add a rounded beat repeatedly (at 128 BPM and 30 fps that drifts 2 frames in 32 beats). Cut on the beat, change the layout on the bar.
- **Cuts**: cut at the fastest frame of a move, with matching direction and speed on both sides. A click into a new screen is a match cut on the click's rebound; the new screen comes in slightly large and settles.
- **Titles**: a landed title is dead still; the motion moves to the next element, the camera or the world behind. Vary the entrance within a film, never a fade and slide-up for each:
  - per word: `blur(6px)` → 0 and opacity 0 → 1 in 0.13 s, 0.067 s apart, no translate;
  - per word from light grey to ink, 0.07–0.1 s apart, no position change;
  - the whole line blurring in, 8 px → 0 in 0.13–0.2 s;
  - per letter for a name, 0.1 s apart, opacity 0.3 → 1 with a slight blur;
  - behind the subject: the title between the plate and a matte of the person;
  - one word of the sentence rolling through options like a slot machine, about 0.1 s a roll.
- **Holds**: a line the viewer must read holds about 0.5 s plus 0.3 s a word, the film's last line at least 2 s; a one- or two-word chapter line may hold 0.4 s. Then exit with a blur-out and fade of 0.13–0.25 s, word by word, or with the scene's move.
- **Title size**: 4–9% of the frame height, one or two lines; quiet lines at 2.5–4% against hero words that fill 60–90% of the width. One highlighted word in the accent colour, which carries meaning.
- **Rhythm**: contrast speeds. Montages cut every 0.13–0.8 s; a demo holds one framing for 7–10 s while the UI acts; shots average 1.8–3 s with motion inside them. Hold 0.3–0.75 s before the payoff, which plays at normal speed.
- **Continuous motion that works**: the product's UI working, footage playing, a character acting, a 3D world turning, a slow orbit of a background stage (3–5° a second).
- **Defaults that look generated**: breathing, floating or pulsing loops standing in for motion on titles and UI; titles that keep sliding or scaling after they land; a slow creeping scale on a title or a slow push late in a scene; bounce on UI; click rings; every scene entering the same way; every element fading and sliding up. A character's idle and overshoot are acting, not these (`types/character.md`).

## Transitions with a cause

Use 3–5 kinds in a film, each caused by something on screen. Hard cuts belong inside a scene (punch-ins); at most a third of the seams between beats are hard cuts, and worlds never crossfade into each other. Measured on the official films:

| Transition               | How it is built                                                                                                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zoom through a button    | the camera tracks to the button with blur (0.6 s), then the button scales from ~8% to ~250% of the frame in 0.35 s, strong ease-in; its fill becomes the next frame                 |
| Object becomes the world | a pill or card grows past the frame in 0.65 s, ease-in-out, its radius shrinking; what was around it blurs ~15 px and fades in 0.3 s; the new content fades in while it still grows |
| Morph                    | one container widens into the next (icon card → prompt box, ~110 → ~880 px in 0.2 s `power3.out`) with a horizontal blur 12 → 0                                                     |
| Carry across             | the result shrinks 1 → 0.6 with blur peaking at 6 px mid-move and lands inside the next app as it builds around it                                                                  |
| Colour flood             | the hero object stays while the whole ground changes colour in ~0.4 s `power2.inOut`                                                                                                |
| Whip                     | a horizontal or vertical smear of 0.13–0.3 s; the arriving element lands blurred and sharpens in ~0.13 s                                                                            |
| Iris from the click      | `clip-path: circle()` opens from the clicked point onto the next world in 0.15 s                                                                                                    |
| Dip cut                  | the outgoing frame darkens ~40% for 3 frames before a hard cut, so the cut reads as meant                                                                                           |
| Blur swap on one stage   | out: opacity → 0 with ~8 px blur in 0.13–0.2 s; in: blur → 0 in 0.13 s; the ground never cuts                                                                                       |

| The person says        | Change                                                                         |
| ---------------------- | ------------------------------------------------------------------------------ |
| "too fast"             | Slow every zoom and pan to 0.7× of its speed, nothing else                     |
| "speed this up"        | Speed the content and shorten the beat by the same amount; later beats move up |
| "the titles move"      | Land them, then hold them dead still until they leave                          |
| "it feels like slides" | Enter the next scene through an object on screen; cut a move mid-flight        |


# The spec

Adjectives are where the default look lives. Given "premium, modern, clean", the model fills every gap with its own defaults, and they look the same in every run: a dark void, a glow, small type floating in the middle, everything fading in. Every adjective you turn into a number is a decision taken back from those defaults.

So before any scene, write `SPEC.md` at the project root: the film as a director's brief to yourself, with a number wherever you would have written an adjective. Build from it, check against it, and change it when a review changes the film.

The spec serves the story, never the other way round (`story.md`). A look that turns the story's things into abstract shapes has failed, however striking the frame.

## Turning words into numbers

| The word  | Becomes                                                                                                                                |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| premium   | a material with numbers: satin paper with 2% grain, a product on a seamless sweep with a 0.55 contact shadow, chrome at roughness 0.05 |
| modern    | a camera and a type system: a 30-frame push on one ease, a display face at 9% of the frame height with -2% tracking                    |
| clean     | a grid and a ration: 12 columns, 96 px margins, the accent on one word per shot                                                        |
| dynamic   | cuts on the beat, a layout change on the bar (every 4 beats), one hero move per shot                                                   |
| playful   | springs at damping 0.45-0.6 on position and scale (never on opacity or colour), 10-30% exaggerated poses                               |
| cinematic | a lens and a light: a 35 mm framing, a key from upper left, a rim from behind, 6% vignette                                             |

## Composition numbers

- The hero of a shot fills at least 40% of the frame's height or width. A small object in the middle of an empty frame is never a shot; push in, crop, or give it a world.
- One hero move per shot. Secondary moves travel 50-70% as far, start 100-200 ms after it, and everything else holds still.
- In a story film every shot moves the story: something happens that causes the next shot. Lines read as cause and effect ("so…", "which means…"), not slogans.
- An information card (B-roll over a talking head, a data beat, a vertical explainer card) is different: its information is on screen within about 2.5 s, then it holds, so any paused frame reads as a finished poster.
- Something new every 2-4 s across the film; a new layout every bar when there is music.
- Text meant to be read: at least 28 px at 1080 (2.6% of the short side), held 0.5 s + 0.3 s a word. Too many words: cut words, never shrink type.

## BANNED by default

These are where generated video lands when nothing else is decided. Each is banned unless the brand's own material or the person's reference uses it, and then only as they use it:

- a black or dark navy void as the ground, with small elements floating in its middle;
- glow, bloom, neon, lens flares, glowing orbs and rings; floating particles as decoration;
- purple or blue gradients, mesh gradients, glass cards;
- a cream or off-white paper ground with a serif display, italic accent words, numbered "01 / 02" labels, small monospace caps labels, pill-shaped chips and buttons;
- everything centred; everything fading in at once; every element fading and sliding up;
- text that moves while it is read; titles that keep drifting after they land;
- corner labels, frame borders, corner brackets, HUD readouts as decoration;
- three cards in a row, KPI grids, a title over a dimmed screenshot;
- the logo docked in a corner.

After the first render, name every default it used anyway, from this list or not, add each to the film's BANNED line, and fix them. The list grows with every film.

## A look built from a medium

A look holds together when it is the rules of one medium, not a palette. A risograph look, for example, is five parts and nothing else:

- **paper**: one flat colour with a fibre noise, no gradients;
- **ink A**: every word that must be read and every structural line;
- **ink B**: one fluorescent accent, one focus per frame (the number, the bar, the stamp);
- **overprint**: where the inks overlap a third colour appears, and the B plate sits 3 px off register;
- **halftone**: every gradient is dots.

Motion comes from the same medium: the frame is printed, plate by plate, not faded in. Write any look this way: its parts, what each may carry, and how the medium itself moves (paper is cut and lifted, ink is printed, glass refracts, clay is pressed).


## The LOOK line

With no design spec, the look is the LOOK line of `SPEC.md` (`spec.md`), taken from the brand, the reference or the subject itself: its era, its materials, where it would be shown. Every part is a number (hex, px, %, a named face and weight), the ground and the hero come from a medium rather than from effects, and the BANNED line keeps it off the defaults. Inter, Space Grotesk, Instrument Serif, Geist and JetBrains Mono are where generated design lands; use them when the brand does, not by default. Copy the palette and the faces into the root variables below.

## Video facts

- Full-screen linear gradients on dark grounds band under H.264; use a radial gradient, a solid fill or a solid plus a local glow.
- An accent at 5% opacity disappears in compression: 15–25% for atmosphere, full saturation for the focal element.


## 2. What to look for

First, describe each beat frame in one sentence as a stranger would, naming every object; an object you would have to explain ("those bars are mirrors") is a P0. Then read the beat frames in order: do they tell a story a stranger follows, each one causing the next? Compare each with its shot in `SPEC.md`; what does not match is a note. Then name every default the frames show (`spec.md` "BANNED by default", or one not on the list yet), add each to the BANNED line, and fix them before anything else.

Then go through the sheets once per question:

| Question                      | What it catches                                                                                                                                    |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Does it read as what it is?   | A shape that reads as another object, a material that reads as plastic, a product screen that reads as a mockup, a face or mascot that reads wrong |
| Does the subject separate?    | Subject and ground too close in value, two focal points in one frame, the eye with nowhere to go                                                   |
| Framing and contact           | Crops, text at the edge or under platform UI, collisions at a seam, things floating that should touch                                              |
| Timing as a first-time viewer | A read shorter than its words (`story.md` §6), something that pops on with no move, a jump at a cut, everything moving at once on one curve        |
| Tells                         | Which items of `story.md` §8 and `motion.md` "Defaults that look generated" are on screen                                                          |
| The pictures alone            | With the words covered, do the beat frames still tell the storyline?                                                                               |
| The phone sheet               | Can every line meant to be read be read at 360 px?                                                                                                 |

## 3. Notes and fixes

Write each problem as one line: `t=4.2s · where · problem → exact change · what stays`. Rank them:

- **P0** breaks the read or the contract: unreadable, wrong, broken, a tell in the hero shot.
- **P1** weakens the film: a dead stretch, a soft payoff, a seam that jumps.
- **P2** polish.

Fix every P0 and the P1s worth their time: text first, then timing, then detail. Then snapshot only what you changed, once. A second pass only when a P0 is still open. Never score the film out of 10: a score finds nothing to fix. When a fix does not hold, snapshot the frames on either side of the problem, list every difference, and change only the line that causes it. A film that feels busy: remove a third of the motion and keep the moves that lead the eye.

A fresh pair of eyes, when your host can start a sub-agent: give it only `STORYBOARD.md` and the three sheets, ask for P0 and P1 lines in the format above, and keep editing to yourself. Commit or copy the project before you fix, so a fix that makes things worse can be rolled back.
