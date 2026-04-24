Here is the complete v5 rubric:

---

# Quest Rubric — campaign-brief — v5

**20 criteria, 200 points max.** Two new aspirational criteria from R4:

---

**C-19 — Gap reclassification rule from dual-field format** *(R4 Pattern A)*

The `Assumption:` + `Consequence:` structure is a definitional gate, not documentation style. A blocking gap that cannot supply both fields must be reclassified as optional before VERDICT renders — not silently omitted, not retained with empty fields. The logic: if you cannot state what you're assuming and what happens when the assumption fails, the gap's blocking claim lacks grounding. Single-field implementations (`Inertia risk:` only) lack this gate. PARTIAL = dual fields required but reclassification on absence unspecified. PASS = reclassification on missing fields is explicit in the prompt and visible in the output.

This resolves an ambiguity in C-11: C-11 tests that the fields exist; C-19 tests that absence of either field changes the gap's classification.

---

**C-20 — Density ceiling operates on entry count, not line count** *(R4 Pattern B)*

The FULL/COMPRESSED threshold in C-15 counts semantic entries (individual missing-signal gaps), not physical lines or field count. A three-line FULL FORMAT entry (path + `Assumption:` + `Consequence:`) counts as one toward the ceiling, same as a one-line entry. An implementation that applies the ceiling to line count will compress the highest-priority gaps of their structural detail precisely when it matters most. PARTIAL = threshold present but counting unit unspecified. PASS = prompt explicitly states the threshold counts blocking gaps (entries), with per-entry line count orthogonal.

This is distinct from C-15 (ceiling mechanism exists); C-20 requires the mechanism counts the right unit.

---

**Two-criterion chain for blocking gap integrity:** C-11 (fields required) + C-19 (absence triggers reclassification) together enforce that every entry in BLOCKING is genuinely blocking by construction, not by author intent.
t labeled "narrative" without cross-signal reasoning is PARTIAL.
The synthesis must answer: what story do these signals tell as a set?

**C-05 — Topic registered with name, date, intent**
The topic is registered (or confirmed registered) with all three fields present.
Checking registration is PARTIAL. Performing registration as a required output is PASS.

---

## Tier 2 — Recommended (C-06–C-08)
*Separates good from adequate. Miss these and the output is technically complete but not actionable.*

**C-06 — Explicit readiness verdict**
The output includes a terminal, named readiness verdict: ready / not ready / conditional.
A verdict that emerges in prose is PARTIAL. A named verdict block is PASS.

**C-07 — Gap prioritization with inertia framing**
Gaps are not just labeled blocking/optional — each blocking gap includes an explicit
statement of what happens if the team commits without this signal. Labeling without
consequence grounding is PARTIAL. Item-level inertia fields (e.g., `Inertia risk:`,
`Consequence:`) that make the cost of omission visible are PASS.

**C-08 — Visual hierarchy with structural blocks**
Output is organized into named, discrete blocks (e.g., STATUS, STORY, VERDICT).
Prose sections and structured data sections are visually and structurally separated.
Flat markdown with headers is PARTIAL. Named block structure with enforced separation
is PASS.

---

## Tier 3 — Aspirational (C-09–C-20)
*Differentiates strong from good. These criteria capture structural properties that make
the output robust under variation, not just correct in the ideal case.*

**C-09 — Session delta block**
A dedicated DELTA block tracks what changed since the prior run. Present only when
triggered is PARTIAL. Mandatory even on first run — with a defined null value
(e.g., `prior_brief: NONE`) — is PASS. The delta block is the axis of value for
repeated execution; making it optional degrades the skill to a one-shot tool.

**C-10 — Confidence metric (derived, auditable)**
The output includes a derived readiness confidence score. A prose qualifier
("high confidence") is FAIL. A named metric derived from auditable inputs
(e.g., multi-dimension scoring table with defined thresholds) is PASS.
The score must be reproducible: given the same inputs, the same score must result.

**C-11 — Per-gap commit-risk fields**
Each blocking gap entry includes mandatory structured fields that make the inertia
cost explicit (e.g., `Assumption:` + `Consequence:`, or `Inertia risk:`). A prose
description of risk without item-level structure is PARTIAL. Mandatory field structure
that forces reclassification when the consequence field is absent is PASS.

**C-12 — Prose confined to STORY section**
Narrative prose appears only in the designated STORY block. Prose that bleeds into
STATUS, VERDICT, or other structured sections is PARTIAL. Full confinement — all
non-STORY sections contain only structured data — is PASS. Inserting structured tables
into STORY weakens but does not violate this criterion (PARTIAL, not FAIL).

**C-13 — Silence-breaking structural enforcement**
The format is designed so omitting a required field breaks the output pattern visibly —
silence cannot pass. Enforcement through field naming conventions (required keys that
cannot be absent without structural break) is PASS. Relying on author discipline to
fill gaps is PARTIAL.

**C-14 — Confidence block isolation**
*From R2 Pattern A.*
The derived confidence metric (C-10) occupies a dedicated named block (e.g., CONFIDENCE),
separate from STORY. Embedding a scoring table inside STORY is PARTIAL — it preserves
C-10 correctness but creates a structural conflict with C-12 because STORY is designated
for narrative prose (C-04) and a scoring table competes for that role. A standalone
CONFIDENCE block with its own structural boundary, leaving STORY uncontested for
cross-signal synthesis, is PASS.

**C-15 — STATUS density ceiling**
*From R2 Pattern B.*
When per-gap mandatory fields (C-11) are present, a structural mechanism must keep
blocking gap entries scannable regardless of gap count. No ceiling mechanism is
FAIL when blocking gaps exceed ~4 entries (unreadable at scale), PARTIAL when gap
count happens to be low. An explicit ceiling mechanism — e.g., a max-fields-per-gap
contract, a summary roll-up for gap counts above a threshold, or a structured
compression format — is PASS. Presence of the fields alone (C-11) does not satisfy
this criterion; C-15 measures whether the structure degrades gracefully under load.

**C-16 — Artifact timestamps in STATUS found section**
*From R3 Pattern A.*
Each signal entry in the STATUS found section includes a capture date
(e.g., `<ns>/<artifact> <date>` per line). Enumeration without dates is PARTIAL —
the reader can count signals but cannot assess staleness without re-running the skill.
Per-entry timestamps that make freshness auditable at a glance are PASS.
This is distinct from C-02, which only requires enumerability; C-16 measures whether
the enumeration carries enough temporal context for the reader to act on it.

**C-17 — STORY prohibition list**
*From R3 Pattern B.*
The STORY block is bounded by an explicit PERMITTED/NOT PERMITTED constraint list
that structurally prohibits content that would degrade synthesis into enumeration
(e.g., bullets, artifact filenames, confidence level restatement, per-gap enumeration,
embedded tables). Advisory phrasing ("avoid bullets") is PARTIAL — the intent is
signaled but not enforced. An explicit PERMITTED/NOT PERMITTED list that names the
prohibited forms is PASS. This criterion is complementary to C-12 (which governs
where prose lives) and C-04 (which governs what synthesis says): C-17 governs how
STORY's internal purity is structurally defended against regression across runs.

**C-18 — STORY three-question sequential structure**
*From R3 Pattern C.*
The STORY block follows a mandatory sequential structure of three named questions:
(1) what case do the signals make together, (2) what do the gaps leave uncertain,
(3) what is the team's real exposure. Free-form synthesis is PARTIAL — cross-signal
reasoning may emerge but is not guaranteed and cannot be audited for completeness.
A named three-question sequence is PASS: it guarantees coverage of all three dimensions
(evidence, uncertainty, risk) and makes synthesis reproducible across runs and authors.
This criterion is distinct from C-04, which tests that synthesis happens; C-18 tests
that synthesis is structured to be verifiable.

**C-19 — Gap reclassification rule from dual-field format**
*From R4 Pattern A.*
The dual `Assumption:` + `Consequence:` structure is a definitional gate, not a
documentation preference. A blocking gap entry that cannot supply both fields must be
reclassified as optional before VERDICT renders — it must not be silently omitted,
retained with empty fields, or allowed to hold blocking status without logical support.
The logic: if you cannot state what you are assuming and what happens when the assumption
fails, the claim that the gap is blocking lacks grounding. Single-field implementations
(`Inertia risk:` only, as in C-11 PARTIAL) lack this gate because a single field can
be populated with a vague consequence that does not force the distinction. PARTIAL =
dual fields required but reclassification on absence not specified. PASS = prompt
explicitly states that a gap unable to supply both fields must be moved to OPTIONAL,
and the reclassification is visible in the output (not silent). This criterion is
distinct from C-11, which requires the fields; C-19 requires that absence of the
fields triggers a classification change.

**C-20 — Density ceiling operates on entry count, not line count**
*From R4 Pattern B.*
The threshold in C-15 (FULL format if blocking gaps <= N, COMPRESSED if > N) counts
semantic entries — individual missing-signal gaps — not physical lines or total field
count. Multi-line structured entries (e.g., a three-line FULL FORMAT entry with
`path`, `Assumption:`, and `Consequence:` fields) do not count as three entries toward
the threshold; they count as one. An implementation that applies the ceiling to line
count or field count rather than entry count will compress entries that should remain
in FULL FORMAT, stripping the most critical gaps of their structural detail precisely
when detail matters most. PARTIAL = ceiling threshold present but the counting unit is
unspecified or ambiguous (entry count and line count coincide at the current gap volume,
so the distinction has not been tested). PASS = the prompt explicitly specifies that
the threshold counts blocking gaps (entries), and that per-entry line count is
orthogonal to the threshold — a three-line entry and a one-line entry each count as
one toward the ceiling. This is distinct from C-15, which requires a ceiling mechanism;
C-20 requires that the mechanism counts the right unit.

---

## Criterion Map

| # | Name | Tier | Introduced |
|---|------|------|------------|
| C-01 | Sub-skills invoked in order | Essential | v1 |
| C-02 | Signals enumerated by namespace | Essential | v1 |
| C-03 | Missing signals explicitly named | Essential | v1 |
| C-04 | Narrative arc synthesizes signals | Essential | v1 |
| C-05 | Topic registered name/date/intent | Essential | v1 |
| C-06 | Explicit readiness verdict | Recommended | v1 |
| C-07 | Gap prioritization / inertia framing | Recommended | v1 |
| C-08 | Visual hierarchy / structural blocks | Recommended | v1 |
| C-09 | Session delta block | Aspirational | v1 |
| C-10 | Confidence metric (derived, auditable) | Aspirational | v1 |
| C-11 | Per-gap commit-risk fields | Aspirational | v2 |
| C-12 | Prose confined to STORY section | Aspirational | v2 |
| C-13 | Silence-breaking structural enforcement | Aspirational | v2 |
| C-14 | Confidence block isolation | Aspirational | v3 |
| C-15 | STATUS density ceiling | Aspirational | v3 |
| C-16 | Artifact timestamps in STATUS found section | Aspirational | v4 |
| C-17 | STORY prohibition list | Aspirational | v4 |
| C-18 | STORY three-question sequential structure | Aspirational | v4 |
| C-19 | Gap reclassification rule from dual-field format | Aspirational | v5 |
| C-20 | Density ceiling operates on entry count, not line count | Aspirational | v5 |

---

## Notes on R4 Additions

**C-19 resolves an ambiguity in C-11.**
C-11 PASS requires "mandatory field structure that forces reclassification when the
consequence field is absent." V-04 and V-05 demonstrated that this reclassification
is only structurally enforceable when both `Assumption:` and `Consequence:` are
required independently — a single composite field (`Inertia risk:`) can be populated
without decomposing the assumption from its consequence. C-19 makes the reclassification
mechanism explicit as its own criterion: C-11 tests field presence; C-19 tests that
absence of either field changes the gap's classification before the VERDICT renders.

**C-20 is an independence criterion, not a stricter ceiling.**
C-15 PASS means a ceiling mechanism exists. C-20 PASS means the ceiling counts the
right unit. A variation can achieve C-15 PASS (mechanism present) while failing C-20
(mechanism applied to lines, not entries) — these are structurally independent. The
R4 finding confirms that three-line FULL FORMAT entries do not degrade C-15 scores,
because entry count and line count are orthogonal. C-20 encodes that independence
as a testable rubric property: the prompt must make the counting unit explicit.

**C-19 and C-11 form a two-criterion chain for blocking gap integrity.**
C-11 tests that mandatory dual fields are required. C-19 tests that a gap failing
those fields is reclassified rather than retained. Together they enforce: every entry
in BLOCKING is genuinely blocking (by construction, not by author intent).

**The jointly-necessary claim for C-17 + C-18 → C-04 is confirmed.**
R4 V-01 (C-17 only), V-02 (C-18 only), and V-04 (C-17 + C-18) closed the experiment:
prohibition alone permits structured silence; structure alone permits enumeration
labeled as synthesis; both together achieve C-04 PASS. No revision to C-17 or C-18
is needed before R5.
