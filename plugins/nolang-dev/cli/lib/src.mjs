// 原稿 (design.txt / timeline.txt) を cut ごとの投入 text に分ける。サーバーの join_stream と同じ並びにする。
import { CliError, EXIT } from "./errors.mjs";

const DESIGN_CUT = /^(?:section|cut)#([A-Za-z_][\w]*)|^\[cut\s+"?([^\]"\s]+)"?/;
const TIMELINE_CUT = /^\*\*\*\s+(\S+)/;
const isComment = (line) => /^#(\s|$)/.test(line.trim()); // `# 注記` (`#v2` と変種の行 `#名.tag(…)` は残す)

function blocks(text, marker) {
  const root = [];
  const cuts = [];
  let current = null;
  for (const line of text.replace(/\r\n/g, "\n").split("\n")) {
    if (isComment(line)) continue;
    const hit = line.trim().match(marker);
    if (hit) cuts.push((current = { name: hit[1] || hit[2], lines: [line] }));
    else (current ? current.lines : root).push(line);
  }
  return { root, cuts };
}

function trimBlank(lines) {
  let start = 0;
  let end = lines.length;
  while (start < end && !lines[start].trim()) start++;
  while (end > start && !lines[end - 1].trim()) end--;
  return lines.slice(start, end);
}

// 2 file → cut ごとの投入 text。1 つ目 = 根の design + 根の timeline (`#v2` を除く) + timeline に無い design の block + cut 1。
// 以後は cut の design block + timeline block。順は timeline の `*** 名` の順
export function splitCuts(design, timeline) {
  const d = blocks(design, DESIGN_CUT);
  const t = blocks(timeline, TIMELINE_CUT);
  if (!t.cuts.length) throw new CliError("timeline.txt に `*** 名` の cut が無い", { exit: EXIT.USAGE });
  const names = new Set(t.cuts.map((c) => c.name));
  const designOf = new Map(d.cuts.map((c) => [c.name, c]));
  const orphans = d.cuts.filter((c) => !names.has(c.name)).flatMap((c) => trimBlank(c.lines));
  const rootTimeline = trimBlank(t.root.filter((line) => line.trim() !== "#v2"));
  return t.cuts.map((cut, index) => {
    const lines = index === 0 ? [...trimBlank(d.root), ...rootTimeline, ...orphans] : [];
    if (designOf.has(cut.name)) lines.push(...trimBlank(designOf.get(cut.name).lines));
    lines.push(...trimBlank(cut.lines));
    return { name: cut.name, text: lines.join("\n") + "\n" };
  });
}

// cut ごとの投入 (start → submit): 投入済みの cut ({name, text}) と今の原稿の cut を突き合わせ、まだ投入していない cut と、
// 投入した後に手元で変わった cut (サーバーには送り直せない) を返す
export function pendingCuts(cuts, submitted) {
  const changed = [];
  for (const [index, done] of submitted.entries()) {
    const now = cuts[index];
    if (!now || now.name !== done.name) {
      throw new CliError(`投入済みの cut ${done.name} が原稿の ${index + 1} 番目に無い (投入した cut の順と名は変えられない)`, { exit: EXIT.USAGE });
    }
    if (now.text !== done.text) changed.push(done.name);
  }
  return { pending: cuts.slice(submitted.length), changed };
}

// design の `canvas WxH` から縦横 (無ければ 16:9)
export function aspectOf(design) {
  const m = design.match(/^canvas\s+(\d+)x(\d+)/m);
  if (!m) return "16:9";
  return Number(m[1]) >= Number(m[2]) ? "16:9" : "9:16";
}
