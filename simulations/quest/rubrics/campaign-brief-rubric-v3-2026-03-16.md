```markdown
# Quest Rubric — campaign-brief — v3
**Date:** 2026-03-16
**Previous:** v2 (13 criteria, 130 points max)
**Changes:** Added C-14, C-15 from Round 2 excellence signals

---

## Rubric Purpose

Evaluate skill variations for the `campaign-brief` orchestration skill.
A `campaign-brief` output is a dashboard that tells the team what signals
exist, what is missing, and whether the topic is ready to commit. The core
diagnostic pair is C-02/C-03. The differentiator is C-04. If orchestration
over plain `topic-status` has no additional value, the skill fails.

---

## Scoring Scale

| Score | Meaning |
|-------|---------|
| PASS | Criterion fully met — structural or explicit evidence |
| PARTIAL | Criterion partially met — likely to emerge but not guaranteed |
| FAIL | Criterion absent or structurally impossible |

| Tier | Points (PASS) |
|------|---------------|
| Essential | 10 |
| Recommended | 10 |
| Aspirational | 10 |

**Max score: 150 (5 Essential + 3 Recommended + 7 Aspirational)**

---

## Tier 1 — Essential (C-01–C-05)
*Minimum for a useful output. Fail any of these and the output is not a dashboard.*

**C-01 — Sub-skills invoked in order**
All four sub-skills (topic-status, scout, signal-check, topic-register or equivalent)
are invoked in a defined sequence. Execution order must be deterministic — implied
sequence is PARTIAL; structural enforcement (gates, named phases, block ordering) is PASS.

**C-02 — Existing signals enumerated by namespace**
Signals found are listed per namespace, not summarized as "signals exist."
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

## Tier 3 — Aspirational (C-09–C-15)
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
```

---

Two notes on the additions:

**C-14 is a resolution criterion, not a new capability.** It resolves the structural conflict between C-10 and C-12 that V-03 and V-05 both hit. A variation can PASS C-10 and C-12 independently while failing C-14 — the criterion captures the interaction, not either property alone.

**C-15 is a load criterion.** It cannot be meaningfully evaluated on variations with ≤3 blocking gaps. Score it PARTIAL by default at low gap counts; reserve PASS for variations that demonstrate an explicit mechanism (the mechanism being present proves intent regardless of current gap count).
