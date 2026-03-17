Three new aspirational criteria extracted from the R3 scorecard:

**C-16 — Artifact timestamps in STATUS found section** (R3 Pattern A, from V-01)
V-01 showed `<ns>/<artifact> <date>` per-entry format. C-02 only requires enumerability; C-16 requires temporal audit without re-running. A reader who can count signals but can't assess staleness cannot act on the dashboard.

**C-17 — STORY prohibition list** (R3 Pattern B, from V-03)
V-03 achieved C-04 PASS via an explicit PERMITTED/NOT PERMITTED list banning bullets, artifact filenames, tables, confidence restatement, and per-gap enumeration. C-12 governs *where* prose lives; C-17 governs *how* STORY's internal purity is defended against regression.

**C-18 — STORY three-question sequential structure** (R3 Pattern C, from V-03)
V-03 mandated: (1) what case do signals make together, (2) what do gaps leave uncertain, (3) what is the team's real exposure. C-04 tests that synthesis happens; C-18 tests that synthesis is verifiable and reproducible across runs and authors.

**Key design note in the rubric:** C-17 and C-18 are jointly necessary for C-04 structural reliability. A prohibition list without a question sequence permits structured silence. A question sequence without prohibitions permits enumeration labeled as synthesis. V-01 and V-02 got C-04 PARTIAL for three rounds because neither mechanism was present.

Updated: **18 criteria, 180 points max** (`output/dist` and scorecard reference table will need updating separately).
s found are listed per namespace, not summarized as "signals exist."
The output must be enumerable — a reader must be able to count signals by namespace
without re-running the skill.

**C-03 — Missing signals explicitly named**
Gaps are named, not silenced. If a namespace has no signals, that absence must
appear as a named entry, not an omission. Silence on gaps is FAIL.

**C-04 — Narrative arc synthesizes signals together**
The synthesis section interprets what the signals mean *together* — not a flat list
with a label. A list labeled "narrative" without cross-signal reasoning is PARTIAL.
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

## Tier 3 — Aspirational (C-09–C-18)
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

---

## Notes on R3 Additions

**C-16 is a temporal audit criterion, not an enumeration criterion.**
C-02 PASS means a reader can count signals by namespace. C-16 PASS means a reader
can also assess whether any signal is stale — answering "do we have a scout signal"
is different from "do we have a *current* scout signal." V-01 demonstrated this with
`<ns>/<artifact> <date>` format. Variations that list filenames only score C-02 PASS,
C-16 PARTIAL.

**C-17 and C-18 together close the C-04 reliability gap.**
V-01 and V-02 both achieved C-04 PARTIAL across multiple rounds because synthesis
instructions were advisory rather than structural. V-03 achieved C-04 PASS by
combining prohibition (C-17) with a mandated question sequence (C-18). Neither
criterion alone is sufficient: a prohibition list without a question structure permits
well-formed silence; a question structure without prohibitions permits structured
enumeration dressed as synthesis. Both must be present for C-04 structural reliability.
