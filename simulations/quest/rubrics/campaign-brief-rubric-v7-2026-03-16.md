Here is the complete v7 rubric:

---

**What changed: v6 → v7**

`21 criteria, 210 pts max` → `23 criteria, 230 pts max`

**C-22 — Zero-signal synthesis mandate** *(R6 Pattern — V-03/V-04/V-05)*

Extends C-21's boundary protection to the 0-signal extreme. C-21 guards sparse (1-2 namespaces); C-22 guards empty `found`. The clause re-routes question 1 from "insufficient data" to characterizing what uniform absence implies — "the gap pattern is the evidence set." PARTIAL = C-21 PASS but no explicit zero-signal handling. PASS = explicit clause in STORY execution note that empty `found` is not grounds for omitting synthesis; question 1 must state what uniform absence implies.

**C-23 — Bounded/unbounded inertia classification at verdict level** *(R6 Pattern — V-05)*

Adds action-posture classification to the verdict layer. C-07 tests item-level inertia fields; C-23 tests that verdict-level `inertia_cost` classifies risk as bounded (recoverable post-commit) or unbounded (irreversible). PARTIAL = `inertia_cost` present but recoverability unclassified. PASS = `inertia_cost` declares `bounded: <why recoverable>` OR `unbounded: <why irreversible>`, enabling the team to act on the verdict block alone.

**Two new structural chains documented in Notes:**
- Synthesis robustness chain: C-18 → C-21 → C-22 (structure mandated → sparse guard → zero guard)
- Verdict action-posture chain: C-06 → C-23 (verdict named → verdict classifies recoverability)

**R7 investigation candidate carried forward:** COMPRESSED format × C-16 timestamp survival.
PARTIAL** — `inertia_cost` present at VERDICT level but bounded/unbounded
  classification absent; risk is named but the team cannot derive their action posture
  without re-reading item-level fields
- **PASS** — `inertia_cost` explicitly classifies risk as `bounded: <residual risk and
  why recoverable>` OR `unbounded: <failure class and why irreversible>`, enabling
  distinct action postures per verdict status (commit-with-monitoring vs do-not-commit)

**Boundary relationships clarified:**
- C-22 is a boundary-condition guard on C-21: C-21 covers sparse coverage (1-2 namespaces);
  C-22 covers zero coverage (0 signals found). They are independent axes.
- C-23 is a scope-level guard on C-07: C-07 tests item-level gap fields; C-23 tests
  verdict-level risk classification. They are structurally independent.

**R7 investigation candidate:**
*COMPRESSED format × C-16 timestamp survival* — whether per-signal timestamps survive
when the COMPRESSED format trigger activates. V-02 confirmed the risk exists; live output
at high gap count needed to falsify.

---

**C-22 — Zero-signal synthesis mandate** *(R6 Pattern — V-03/V-04/V-05)*

When the `found` section of STATUS is empty (zero signals across all namespaces), the
STORY block must not collapse to a non-finding. The LLM failure mode is to write "no
signals found — synthesis not possible" and omit or hollow STORY. But uniform absence is
itself evidence: the gap pattern defines what the team does not know and why they are
not ready. Question 1 must characterize what uniform absence implies — "the absence of
any scout signal indicates the market surface has not been probed at all" is a valid
synthesis; "insufficient data" is not. PARTIAL = sparse-coverage protection present
(C-21 PASS) but no explicit clause for the zero-signal case; synthesis may be vacated on
grounds of empty `found`. PASS = an explicit zero-signal clause in the STORY execution
note declares that empty `found` is not grounds for omitting synthesis — the gap pattern
is the evidence set — and mandates that question 1 characterize what uniform absence
implies rather than reporting absence as a non-answer.

This is distinct from C-21, which guards synthesis when coverage is sparse (1-2
namespaces); C-22 guards synthesis when coverage is zero. Both are boundary conditions
on C-18's structural mandate.

---

**C-23 — Bounded/unbounded inertia classification at verdict level** *(R6 Pattern — V-05)*

The `inertia_cost` field at VERDICT level must classify the aggregate commit risk by
recoverability. Bounded = the team can detect the failure post-commit and course-correct
before it propagates (e.g., "if persona assumptions are wrong, the next campaign signals
will surface the delta"). Unbounded = the failure propagates to an irreversible state
before detection is possible (e.g., "if the regulatory gap is real, commitment triggers
an audit trail that cannot be retracted"). This distinction determines action posture:
bounded inertia means "commit with monitoring"; unbounded inertia means "do not commit
until resolved." A VERDICT with unnamed recoverability forces the team to re-read all
item-level gap fields and synthesize the posture themselves — the verdict is not
actionable on its own. PARTIAL = `inertia_cost` present at VERDICT level but
bounded/unbounded classification absent; risk is named but recoverability is implicit.
PASS = `inertia_cost` declares `bounded: <residual risk and why recoverable>` OR
`unbounded: <failure class and why irreversible>` so the action posture is derivable
from the verdict block alone, without re-reading blocking gap entries.

This is distinct from C-07, which tests that each blocking gap entry carries inertia
framing at the item level; C-23 tests that the verdict-level inertia field classifies
the commit-risk type so the team can act on the verdict without re-synthesizing from
item fields.

---

**Three-criterion synthesis robustness chain:** C-18 (three-question structure) →
C-21 (sparse-coverage guard) → C-22 (zero-coverage guard). Each tests the same mandate
at a progressively more extreme input boundary. All three are structurally independent.

**Two-criterion verdict action-posture chain:** C-06 (verdict named) → C-23 (verdict
classifies recoverability). C-06 tests that a verdict exists; C-23 tests that the verdict
carries enough risk-type information to determine action posture.

---

## Tier 1 — Essential (C-01–C-05)
*Non-negotiable. Miss any of these and the output is structurally incomplete.*

**C-01 — Sub-skills invoked in order**
The output follows the defined block sequence: TOPIC, DELTA, STRATEGY, STATUS,
[BLOCKING-DETAIL], CONFIDENCE, STORY, VERDICT. Blocks out of order or missing are PARTIAL.
Full compliance with the defined sequence, with TOPIC first and VERDICT last, is PASS.

**C-02 — Signals enumerated by namespace**
Found signals in the STATUS block are enumerated per-line with namespace path and date:
`<ns>/<artifact> <date>` per line. A prose description or aggregate count without
per-item enumeration is PARTIAL. Structured per-line enumeration by namespace is PASS.

**C-03 — Missing signals explicitly named**
Gaps are explicitly classified into BLOCKING and OPTIONAL sections with explicit empty-case
statements (e.g., `BLOCKING: none`). Implicit silence about gaps is PARTIAL.
Named gap sections with explicit empty-case handling are PASS.

**C-04 — Narrative arc synthesizes signals**
The STORY block synthesizes found signals into a cross-signal narrative, not a per-signal
summary. Per-signal enumeration inside STORY is PARTIAL. A synthesis that answers what the
signals collectively indicate — with cross-signal reasoning — is PASS. An output labeled
"narrative" without cross-signal reasoning is PARTIAL.
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

## Tier 3 — Aspirational (C-09–C-23)
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

**C-21 — Sparse-coverage synthesis protection**
*From R5 Pattern — V-05.*
When signal breadth is narrow (found signals concentrated in one or two namespaces),
the STORY block must not collapse to a non-finding. A prompt that satisfies C-18 at
typical breadth can silently fail at sparse breadth — the three-question structure is
nominally present but question 1 becomes "insufficient data to synthesize" rather than
"partial evidence points toward X." The sparse case is the high-uncertainty case: it is
precisely when synthesis most needs to commit to a direction. PARTIAL = three-question
mandate present (C-18 PASS) but no explicit guidance for sparse-coverage behavior;
synthesis may be omitted on grounds of thin data. PASS = an explicit sparse-coverage
clause in the STORY execution note maintains the synthesis mandate at narrow signal
breadth — "the structure cannot be omitted on the grounds of sparse data" — and bounds
"brief is permitted" with a direction requirement: "must state what direction even
partial evidence points." This is distinct from C-18, which requires the three-question
structure; C-21 requires that the structure cannot be vacated when coverage is thin.

**C-22 — Zero-signal synthesis mandate**
*From R6 Pattern — V-03/V-04/V-05.*
When the `found` section of STATUS is empty (zero signals across all namespaces), the
STORY block must not collapse to a non-finding. The LLM failure mode is to write "no
signals found — synthesis not possible" and hollow STORY. But uniform absence is itself
evidence: the gap pattern defines what the team does not know and why they are not ready.
Question 1 must characterize what uniform absence implies — "the absence of any scout
signal indicates the market surface has not been probed at all" is a valid synthesis;
"insufficient data" is not. PARTIAL = sparse-coverage protection present (C-21 PASS)
but no explicit clause for the zero-signal case; synthesis may be vacated on grounds of
empty `found`. PASS = an explicit zero-signal clause in the STORY execution note declares
that empty `found` is not grounds for omitting synthesis — the gap pattern is the evidence
set — and mandates that question 1 characterize what uniform absence implies rather than
reporting absence as a non-answer.
This is distinct from C-21, which guards synthesis when coverage is sparse (1-2
namespaces); C-22 guards synthesis when coverage is zero. Both are boundary conditions
on C-18's structural mandate.

**C-23 — Bounded/unbounded inertia classification at verdict level**
*From R6 Pattern — V-05.*
The `inertia_cost` field at VERDICT level must classify the aggregate commit risk by
recoverability. Bounded = the team can detect the failure post-commit and course-correct
before it propagates. Unbounded = the failure propagates to an irreversible state before
detection is possible. This classification determines action posture: bounded inertia
means "commit with monitoring"; unbounded inertia means "do not commit until resolved."
A VERDICT with unnamed recoverability forces the team to re-read all item-level gap
fields and synthesize the posture themselves — the verdict is not actionable on its own.
PARTIAL = `inertia_cost` present at VERDICT level but bounded/unbounded classification
absent; risk is named but recoverability is implicit. PASS = `inertia_cost` declares
`bounded: <residual risk and why recoverable>` OR `unbounded: <failure class and why
irreversible>`, so the action posture is derivable from the verdict block alone, without
re-reading blocking gap entries.
This is distinct from C-07, which tests that each blocking gap entry carries inertia
framing at the item level; C-23 tests that the verdict-level inertia field classifies
the commit-risk type so the team can act on the verdict without re-synthesizing from
item fields.

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
| C-21 | Sparse-coverage synthesis protection | Aspirational | v6 |
| C-22 | Zero-signal synthesis mandate | Aspirational | v7 |
| C-23 | Bounded/unbounded inertia classification at verdict level | Aspirational | v7 |

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

---

## Notes on R5 Addition

**C-21 makes the V-05 sparse-breadth clause non-inert.**
R5 V-03 and V-05 demonstrated that a sparse-coverage clause in the STORY execution
note improves robustness without affecting any v5 criterion. The clause was "structurally
inert" on the v5 rubric — it scored identically to V-04 (200/200). C-21 makes this
robustness property a scored criterion: the clause now closes a testable rubric gap
rather than being a free robustness bonus.

**C-21 is a boundary-condition guard on C-18.**
C-18 requires the three-question structure; C-21 requires the structure cannot be vacated
on grounds of sparse data. A variation can achieve C-18 PASS (structure mandated) while
failing C-21 (no protection against omission when coverage is thin). The two criteria
are structurally independent: C-18 tests structural presence; C-21 tests structural
durability at the input boundary.

**R5 general principles (not new criteria).**
Two patterns from R5 generalize existing criteria rather than add new rubric gaps:

*Output annotation closes the loop on prompt-side enforcement.* Any enforcement rule
present only in an execution note is PARTIAL for its criterion; the rule must produce
output-visible annotation of its effect to achieve PASS. This is the principle behind
C-19: reclassification enforced silently is PARTIAL; reclassification annotated in
output is PASS. The principle generalizes to any enforcement action, but C-19 is
currently the only scored instance.

*Explicit unit specification in structural thresholds removes scale-dependent ambiguity.*
Any threshold that counts instances of a thing must name the type of thing and declare
what is orthogonal to the count. This is the principle behind C-20: "count blocking
gaps" implies entries but the ambiguity is invisible at low gap count and surfaces only
when multi-line entries appear at scale. The principle generalizes to any counting
threshold, but C-20 is currently the only scored instance.

---

## Notes on R6 Additions

**C-22 extends the synthesis robustness chain to the zero-signal boundary.**
C-21 protects synthesis when `found` is sparse (1-2 namespaces); C-22 protects synthesis
when `found` is empty. The two criteria test the same mandate — C-18's three-question
structure must be present and populated — at progressively more extreme input conditions.
C-21 and C-22 are structurally independent: a prompt can carry C-21 PASS (sparse clause
present) while failing C-22 (no explicit zero-signal handling). Together they form a
three-criterion chain: C-18 (structure mandated) → C-21 (sparse guard) → C-22
(zero guard).

**C-22 was inert on v6 (R6 V-03/V-04/V-05 scored 210/210 without it as a criterion).**
The zero-signal clause was already present in R5 V-05 but tested as a robustness
enhancement. R6 confirmed it does not interact with any existing criterion and forms a
genuinely independent axis (sparse vs. zero are distinct input boundaries). C-22 makes
this protection a scored requirement rather than a structural bonus.

**C-23 adds action-posture classification to the verdict layer.**
C-06 tests that a verdict exists; C-07 tests that each blocking gap carries item-level
inertia framing; C-23 tests that the verdict-level `inertia_cost` field classifies the
commit risk as bounded (recoverable) or unbounded (irreversible). The three criteria
operate at three structural levels — verdict presence, item-level fields, verdict-level
classification — and are fully independent: PASS on each does not imply PASS on the
others.

**C-23 was inert on v6 (R6 V-05 scored 210/210 without it as a criterion).**
The bounded/unbounded framing was present in R5 V-05 as a verdict-level enhancement.
R6 confirmed it operates independently of C-06 and C-07, resolves the action-posture
problem (the team can act on the verdict without re-synthesizing from item fields), and
has no interaction effects with other criteria. A second independent instance is not
required before crystallizing as a criterion: the scope-level distinction (item vs.
verdict) is sufficient to establish independence.

**R7 investigation candidate.**
*COMPRESSED format × C-16 timestamp survival* — whether per-signal timestamps survive
when the COMPRESSED format trigger activates. V-02 confirmed the risk: timestamps may be
dropped at high gap count, vacating C-16 precisely when gap density is highest. Live
output at high gap count needed to confirm or reject as a v8 criterion.
