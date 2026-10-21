"""studio の品質の台帳 — studio の段 (timed = 見積りの尺で解いた VC の check・frames = 描いた frame と音) の規則と、
studio の直しの列 (stream の直し役に回す規則)。

製品の規則 (`domain_services/video_draft/quality_rules.py`) は製品の段 (compile / layout / render)。studio の規則は loop の
たびに入れ替わるので製品の台帳に入れない。名は `LintRule` で、2 つの台帳で衝突させず和が `LintRule` と同じ集合 (test)。level は規則が出す最も重い段 (場合で
1 段下げて出す規則がある — 例: offcanvas は出ていく途中なら info)。直しを回すかは level でなく `studio` の列が決める。
SKILL.md の「規則の名と直し方」の行は `skill_line()` が 2 つの台帳から作る (test が SKILL.md と突き合わせる)。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from domain_services.video_draft.quality_rules import Rule

# 規則の名は製品の `LintRule` (StrEnum) の値そのまま (test が 2 つの台帳の和 = LintRule を縛る)。製品の台帳 (`PRODUCT_RULES`)
# はこの file の module import では読まない — repo を持たない client (plugin の skill) は API (`GET drafts/rules/`) から受ける
DefectLevel = Literal["DEFECT", "severe", "warn", "info"]

StudioStage = Literal["timed", "frames"]
StudioAction = Literal["fix", "record"]  # stream の直し役に回すか・著者の責任に残すか


@dataclass(frozen=True)
class StudioRule:
    """skill の台帳の 1 行。mutable = 根の `lint off=` で黙らせられるか (severe の指摘は黙らない)。fix = 著者への直し方。"""

    name: str
    level: DefectLevel
    stage: StudioStage
    studio: StudioAction
    mutable: bool
    fix: str


def _rule(
    name: str,
    level: DefectLevel,
    studio: StudioAction,
    fix: str,
    *,
    stage: StudioStage = "timed",
    mutable: bool = True,
) -> StudioRule:
    return StudioRule(name=name, level=level, stage=stage, studio=studio, mutable=mutable, fix=fix)


STUDIO_RULES: tuple[StudioRule, ...] = (
    # 画面の作り (cut の中身・主役・余白)
    _rule("empty_cut", "warn", "fix", "絵か札を置く"),
    _rule(
        "text_only_cut",
        "warn",
        "record",
        "全面の絵を板の下に敷くか、絵か人物を 1 枚置く (意図なら `lint off=text_only_cut`)",
    ),
    _rule("sparse_cut", "warn", "fix", "4 秒以上で要素が少ない → 絵か札を足す"),
    _rule("blank_band", "warn", "fix", "cut の頭で画面の 1/3 が地のまま → 絵を全面に敷くか帯に札を"),
    _rule("cut_head_gap", "warn", "fix", "cut 頭が 1.2 秒以上空く → 頭の要素は印なしで置く"),
    _rule(
        "empty_board",
        "warn",
        "fix",
        "板が 1 秒以上空 (小札だけも空・icon は中身) → 中身 (3 字以上の文字・絵・icon) を板と一緒に出す — 著者が書いた `[>#板]` は"
        "消す (印の無い板は最初の中身の語で出る) か中身の最初の句へ寄せる・compile が書いた板の印なら先に出る子の印を中身の語へ・"
        "または板の頭に中身の 1 つ目を置く",
    ),
    _rule("no_closer", "warn", "fix", "最後の cut に大きな締めの一言が無い"),
    _rule(
        "title_on_close",
        "warn",
        "fix",
        "最初の cut の題が閉じられず最後の frame に残る → `[<#名]` (締めで名を言い直すなら締めの cut に新しい層)",
    ),
    _rule("same_picture", "warn", "fix", "同じ絵が 15 秒以上 → 場面ごとに絵を替える"),
    _rule("running_total", "warn", "record", "累計の札の値が cut を跨いで減る → plan に書いた累計を写す"),
    _rule("duplicate_media", "warn", "record", "片方を別素材にするか削る"),
    _rule("duplicate_text", "warn", "record", "字幕と同文の札は `.hide_subtitle`"),
    _rule("unused_section", "info", "record", "使わないなら section を削る"),
    _rule("palette_drift", "warn", "record", "palette 外の色が多い"),
    _rule("stacked_labels", "warn", "record", "前の札を `[<#名]` で消すか 1 枚にまとめる"),
    _rule(
        "text_on_photo",
        "info",
        "record",
        "文字の下に板か帯を敷くか文字を大きく太く (縁取り・影・全面の幕は機械的に足さない)",
    ),
    _rule(
        "photo_hidden",
        "warn",
        "record",
        "全面の写真の 9 割以上に濃さ 0.7 以上の幕が 3 秒以上掛かる (写真が白く飛ぶ / 暗く沈む) → 写真を片側の枠へ (文字は地の側)"
        " か、幕を 0.6 までにして文字の下にだけ帯 / 板",
    ),
    _rule("mouth_provisional", "info", "record", "warm の後の check で実測の点に替わる"),
    _rule("aspect_mismatch", "info", "record", "切り抜き・人物は fit=contain。全面に敷く絵は枠の比率の絵にする"),
    # 文字の読み (大きさ・濃淡・重なり・はみ出し)
    _rule("small_text", "warn", "record", "design の size= を上げる (字幕は台詞を `@|` で折る / 短くする)"),
    _rule(
        "low_contrast",
        "warn",
        "fix",
        "文字と地の差が小さい (沈めた `dim` / focus の兄弟・`recolor` の後も) → 沈める濃さを上げる",
    ),
    _rule(
        "overlap",
        "warn",
        "record",
        "同じ族の文字どうしが重なる (`overlap:` を宣言しても warn・別の族の文字を隠すのは severe の occluded) → 判子・札を相手の文字から外す",
    ),
    _rule("text_gap", "warn", "fix", "同じ行の文字の隙間が 8 px 未満 → `left: 相手.right+16` で並べる"),
    _rule(
        "covered_text",
        "warn",
        "fix",
        "文字の section を絵より後の行へ移すか位置をずらす (覆う演出なら `overlap 相手`)",
    ),
    _rule(
        "hidden_layer",
        "severe",
        "fix",
        "上に見せたい層を後に書く / `z=front` (隠す演出なら前面側に `overlap 相手`)",
    ),
    _rule("caption_collision", "severe", "fix", "section の位置 / size を字幕帯より上に収める"),
    _rule("offcanvas", "severe", "fix", "位置を内側に"),
    _rule("zoom_clips", "warn", "record", "倍率を下げる・寄る先を小さく・切れる札を寄る先から離す"),
    _rule("child_overflow", "warn", "record", "親を広げる / 子の size を下げる / 子の位置を内側へ"),
    _rule("subtitle_overflow", "warn", "fix", "`[subtitle]` の w= / h= を広げる・size を下げる・`[br]` で 2 行に"),
    _rule(
        "orphan_line",
        "warn",
        "record",
        "折り返しの最後の行が 1〜2 字 (「本気だっ / た。」) → 文言を詰める・字を小さく・`[br]` で切る",
    ),
    _rule(
        "font_not_pinned",
        "warn",
        "record",
        "台帳に書体の pin か TTF が無く既定 font で測った (DB のある所で check を回す)",
    ),
    _rule("font_version_mismatch", "warn", "record", "cache の TTF が catalog の版と違う (check が引き直す)"),
    _rule("script_font_digits", "warn", "record", "数字は本文の書体に (font= を外す)"),
    # 時間 (出る時刻・動き・切替)
    _rule("spoiler", "warn", "fix", "見出しが台詞の語を先に見せる → 語の印で出す"),
    _rule("all_at_once", "warn", "record", "句ごとに出す (文字を語で分けて `[>#名]` を語の前に)"),
    _rule("still_stretch", "warn", "fix", "6 秒以上動かない (絵の kb は動きに数えない) → 語に印を足す"),
    _rule("long_still", "info", "record", "台詞が 3 秒以上続く間に画面が変わらない → その間の語に印"),
    _rule("short_layer", "warn", "record", "出す / 消す印の +N を離す"),
    _rule("flash_text", "warn", "record", "出す印を早める / 閉じる印を遅らせる / 文言を短くする"),
    _rule("offset_window", "severe", "fix", "ずれ (+N / -N) を小さく・印を前後の語へ移す", mutable=False),
    _rule("pause_in_sentence", "warn", "record", "間を置くなら文を切る (。)・絵は前の語から出す"),
    _rule(
        "caption_gap",
        "warn",
        "record",
        "字幕 lane が閉じた台詞の前に `[>#subtitle]` を開き直す (台詞を札に出すなら札に `hide_subtitle`)",
    ),
    _rule("entrance_in_fadeout", "warn", "fix", "切替や fade out の 0.8 秒前より後に出す → 語を前へ"),
    _rule("entrance_in_transition", "warn", "record", "最初の台詞の頭に `[silence:+0.4s]` を足して語を窓の後へ出す"),
    _rule("transition_over_speech", "warn", "fix", "切替が台詞に掛かる"),
    _rule(
        "ghost_dissolve",
        "warn",
        "fix",
        "400 ms 以上の dissolve で前の cut の大きな文字・絵が次の cut に透ける (out の無い層か、境界より前から溶ける切替)"
        " → `overlap=` を尺と同じに (out のある文字は境界までに消え終わる)・out の無い絵や札は cut 末の `[<#名 fade]`",
    ),
    _rule("dip_black_frame", "warn", "fix", "dip は黒 frame → dissolve か wipe"),
    _rule(
        "leaks_into_next_cut",
        "info",
        "record",
        "切替の前に他が out で消え、out の無い層だけが次の cut の頭に残る (根の要素は engine が既定の fade で揃える"
        " — 残るのは子・写し・自分で閉じた層) → cut 末に `[<#名 fade]`",
    ),
    _rule(
        "cut_tail_orphan",
        "warn",
        "record",
        "この cut で出すなら最後の台詞行の前へ・次の cut で出すなら `***` の後へ",
    ),
    # 音・読み
    _rule("se_dense", "warn", "record", "効果音が密 (`sfx off`)"),
    _rule("se_long", "warn", "record", '`[♪"…" peak=4.4s]` で山を語に合わせる・`to=` か `fade=` で切る'),
    _rule("month_reading", "warn", "record", "月日に読み `{9月5日|くがついつか}`"),
    _rule("count_year", "warn", "record", "年号は数えずに書く"),
    _rule("voiceless_line", "warn", "record", "間は `[silence:2s]`"),
    _rule("manner_voice", "warn", "record", "manner は言い方だけ (声の高さ・囁き・怒鳴りは書かない)"),
    _rule("same_voice", "warn", "record", "説明文を変えるか、別の声を引いて `id=` で決める"),
    _rule("bgm_gap", "info", "record", "BGM と声の差の目安 (意図した比なら `lint off=bgm_gap`)", stage="frames"),
)

# 製品の規則のうち studio の直し役に回す物 (直しの列)。2 回直しても残れば severe のまま受け入れて描く (判断 16)
PRODUCT_RULES_FIXED: frozenset[str] = frozenset({"overflow", "occluded", "shrunk", "text_over_subject"})

# SKILL.md の「規則の名と直し方」に載せる規則 (この順)
SKILL_RULES: tuple[str, ...] = (
    "empty_cut",
    "shrunk",
    "offcanvas",
    "duplicate_text",
    "spoiler",
    "still_stretch",
    "long_still",
    "cut_head_gap",
    "entrance_in_fadeout",
    "no_closer",
    "same_picture",
    "blank_band",
    "dip_black_frame",
    "sparse_cut",
    "palette_drift",
    "low_contrast",
    "overlap",
    "title_on_close",
    "leaks_into_next_cut",
    "orphan_line",
    "overridden",
    "transition_over_speech",
    "se_dense",
    "running_total",
    "month_reading",
    "font_not_pinned",
    "font_version_mismatch",
    "ghost_dissolve",
    "photo_hidden",
)


def _product_rules() -> tuple[Rule, ...]:
    """製品の台帳 (repo がある時だけ — studio の local の check・SKILL.md の行・test)。"""
    from domain_services.video_draft.quality_rules import PRODUCT_RULES  # noqa: PLC0415 — repo 無しの client は読まない

    return PRODUCT_RULES


def _rows() -> dict[str, Rule | StudioRule]:
    return {**{str(rule.name): rule for rule in _product_rules()}, **{rule.name: rule for rule in STUDIO_RULES}}


def known_rule_names() -> frozenset[str]:
    """2 つの台帳の和 (= `LintRule` の全部・test が縛る) — studio の compile が `lint off=` の照合に使う名。"""
    return frozenset(_rows())


def fixed_rules() -> frozenset[str]:
    """studio の直しの列が fix の規則 (stream の直し役に回す)。製品の台帳のうち直し役に回す物は `PRODUCT_RULES_FIXED` (台帳の
    名だけで決まるので repo が無くても同じ)。spoiler (見出しが台詞の語を先に見せる) は著者 / 担当の責任に残す — 直し役は印を後ろへ
    ずらすか題を中立化するだけで、見せ方の判断にならない。"""
    return (PRODUCT_RULES_FIXED | frozenset(rule.name for rule in STUDIO_RULES if rule.studio == "fix")) - {"spoiler"}


def is_mutable(name: str) -> bool:
    """根の `lint off=` で黙らせられる規則か (台帳に無い名は KeyError — 出す規則は台帳に載せる)。"""
    return _rows()[name].mutable


def skill_line() -> str:
    """SKILL.md の「規則の名と直し方」の行 (`SKILL_RULES` の順・warn でない規則は段を添える)。"""
    rows = _rows()
    entries = [
        f"`{name}`" + ("" if rows[name].level == "warn" else f" ({rows[name].level})") + f" {rows[name].fix}"
        for name in SKILL_RULES
    ]
    return (
        "規則の名と直し方 (2 つの台帳 `scripts/studio_rules.py` と製品の `quality_rules.py` から生成・型に合わない規則は根の"
        " `lint off=規則,…`): " + "・".join(entries) + "。"
    )
