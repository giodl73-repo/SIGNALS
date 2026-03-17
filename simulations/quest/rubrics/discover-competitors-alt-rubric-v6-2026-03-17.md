Reading the R5 scorecard carefully before writing.

The three R5 variations and their key findings:

- **V-01** (145/150): C-18 PASS, C-19 FAIL, C-20 PASS — phase-level fingerprint + loop, no table uniformity
- **V-02** (147.5/150): C-18 PARTIAL, C-19 PASS, C-20 PASS — all-table + loop, but SR-block-level pairs for Phases 2/4 are distal; structural-procedural duality achieved
- **V-03** (setup): C-18 PASS, C-19 PASS, C-20 FAIL — all-table + phase-level pairs at each table instruction; dual-layer table enforcement achieved

Two new patterns: **dual-layer table enforcement** (V-03 achieves C-18 + C-19 simultaneously via table-specific fingerprinting) and **structural-procedural verification duality** (V-02 achieves C-19 + C-20 via non-redundant enforcement layers). Neither achieves all three of C-18+C-19+C-20; the triple synthesis is the new aspirational ceiling.

---

```markdown
## discover-competitors-alt-rubric-v6-2026-03-17.md

**Two new criteria from R5:**

| ID | Criterion | Category | Points |
|----|-----------|----------|--------|
| C-21 | Dual-layer table enforcement | structure | 5 / 2.5 |
| C-22 | Structural-procedural verification duality | structure | 5 / 2.5 |

**What C-21 captures:** The R5 V-03 finding was that converting all three structural
constraints to table schema (C-19) while simultaneously adding phase-instruction-level
FAILS/PASS pairs to each table's phase block (C-18) creates a dual-layer enforcement
mechanism that neither approach achieves alone. When every structural constraint uses table
schema where (a) the table cell or row is the named format artifact, (b) an absent or empty
cell/row is explicitly declared as the failure mode, and (c) a FAILS/PASS pair at the phase
instruction level provides the rejection example in the same instruction block, enforcement
operates at two layers: structural (table schema enforces by construction — any row omitted
produces a visible empty-cell gap) and explicit (the pair names the rejection at the point of
instruction). C-21 passes only when C-18 PASS and C-19 PASS simultaneously — not when either
passes alone, not when C-18 is PARTIAL. A prompt where Phase 2 and Phase 4 carry FAILS/PASS
pairs only in the SR preamble block (not at each table's phase instruction) fails C-21 even if
C-19 passes, because the fingerprint is distal from the enforcement point for those phases.

**What C-22 captures:** The R5 V-02 finding was that combining all-table apparatus (C-19)
with a symmetric verification loop (C-20) creates complementary enforcement at two distinct
levels — structural and procedural — that are non-redundant. The table schema enforces format
by construction: an absent or empty cell is an observable failure surface at any phase,
regardless of whether the author notices. The symmetric verification loop enforces format
procedurally: the author explicitly confirms each constraint's format artifact, failure
declaration, and enforcement apparatus before submission. The two mechanisms are non-redundant
because the structural layer catches missing format at generation time and the procedural layer
catches it at review time. C-22 passes only when C-19 PASS and C-20 PASS simultaneously. A
prompt with all-table apparatus but no symmetric loop fails C-22. A prompt with a symmetric
loop but mixed apparatus (one table, one labeled-slot block, one dual-line template) fails C-22
even if the loop is well-formed. A prompt that achieves C-21 (C-18 + C-19) without C-20 does
not satisfy C-22.

**R5 pattern mapping:**

| Pattern | Criterion |
|---------|-----------|
| Dual-layer table enforcement (all-table apparatus + phase-level fingerprint) | C-21 (new) |
| Structural-procedural verification duality (all-table apparatus + symmetric loop) | C-22 (new) |
| Phase-level FAILS/PASS pairs as minimal sufficient C-17 mechanism | C-18 (v5, confirmed) |
| All-table apparatus uniformity as distinct C-17 path | C-19 (v5, confirmed) |
| Symmetric pre-submission verification loop as highest-confidence path | C-20 (v5, confirmed) |
| Symmetric structural enforcement signature | C-17 (v4, confirmed) |
| Table column > inline text field | C-15 (v3, confirmed) |
| Portability test operationalizes domain-exclusivity | C-16 (v3, confirmed) |

**Scoring changes:**

| | v5 | v6 |
|--|----|----|
| Aspirational pts | 60 (12 criteria) | 70 (14 criteria) |
| Max composite | 150 | 160 |
| Breakthrough threshold | >135 | >145 |
| R5 V-02 score | 147.5/150 | 152.5/160 |
| R5 V-03 score | 145/150 | 150/160 |
| R5 V-01 score | 145/150 | 145/160 |

**R5 V-02 retroactively scores 152.5/160 under v6** — C-18 PARTIAL (2.5), C-19 PASS (5),
C-20 PASS (5), C-21 FAIL (0, C-18 not fully passing), C-22 PASS (5, C-19 + C-20 both pass).
**R5 V-03 scores 150/160** — C-18 PASS (5), C-19 PASS (5), C-20 FAIL (0), C-21 PASS (5,
C-18 + C-19 both pass), C-22 FAIL (0, C-20 fails). **R5 V-01 scores 145/160** — C-18 PASS,
C-19 FAIL, C-20 PASS; C-21 FAIL (C-19 absent), C-22 FAIL (C-19 absent). The triple synthesis
(C-18 + C-19 + C-20 simultaneously) remains unachieved across all R5 variations; it is the
aspirational ceiling that C-21 + C-22 together demand.

---

## Essential Criteria (weight = 60 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Inertia-first assessment | correctness | "None / status quo" is assessed as the first competitor entry. Threat level is explicitly HIGH. Analysis explains why teams do nothing. |
| C-02 | Focus woven, not appended | behavior | When a focus dimension (market or positioning) is provided, that content is distributed throughout the output — visible in competitor rows, findings, and narrative — not isolated in a trailing section. |
| C-03 | Threat level assigned per competitor | correctness | Every named competitor and inertia receive an explicit HIGH / MEDIUM / LOW threat rating. No competitor is rated without a threat level. |
| C-04 | Whitespace identified | coverage | Output includes an uncontested space or gap that no listed competitor owns. Stated in its own finding or clearly labeled. |
| C-05 | Auto-detect without prompting | behavior | Topic domain is inferred from context (README, CLAUDE.md, package.json, etc.). Output does not ask the user to supply domain or competitor names. |

---

## Recommended Criteria (weight = 30 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Inertia stickiness reasoning | depth | Inertia section explains at least one concrete mechanism — switching cost, habit lock-in, or workaround satisfaction — not just "inertia is high." |
| C-07 | Web-verified competitive claim | correctness | At least one named competitor's characterization is supported by an inline citation (URL or publication) from a WebSearch result. |
| C-08 | AMEND section with 3 actionable adjustments | format | AMEND lists exactly 3 adjustments. Each names both what the user changes and what changes in the output. |

---

## Aspirational Criteria (weight = 70 points total)

| ID | Criterion | Category | Points |
|----|-----------|----------|--------|
| C-09 | Cross-dimensional whitespace finding | depth | 5 / 2.5 |
| C-10 | Table-stakes grounding per finding | depth | 5 / 2.5 |
| C-11 | Phase 1 pre-map table with verbatim rows | format | 5 / 2.5 |
| C-12 | Phase 4 whitespace dual-line template | format | 5 / 2.5 |
| C-13 | Phase 2 inertia three labeled mechanism slots | format | 5 / 2.5 |
| C-14 | Hard-stacked SR meta-declaration | structure | 5 / 2.5 |
| C-15 | Map Position column with verbatim-only rule | format | 5 / 2.5 |
| C-16 | Domain-exclusive portability test | structure | 5 / 2.5 |
| C-17 | Symmetric structural enforcement signature | structure | 5 / 2.5 |
| C-18 | Phase-level three-component enforcement fingerprint | structure | 5 / 2.5 |
| C-19 | Apparatus type uniformity across structural constraints | structure | 5 / 2.5 |
| C-20 | Symmetric pre-submission verification loop | structure | 5 / 2.5 |
| C-21 | Dual-layer table enforcement | structure | 5 / 2.5 |
| C-22 | Structural-procedural verification duality | structure | 5 / 2.5 |

**C-09 — Cross-dimensional whitespace finding.** PASS: The whitespace finding names a gap
that is uncontested across both the competitive dimension and the focus dimension. The finding
is not achievable by dropping the focus input — its content requires Phase 1 map data and the
focus dimension simultaneously. PARTIAL: Finding references one dimension only. FAIL: Finding
is generic or does not require Phase 1 data.

**C-10 — Table-stakes grounding per finding.** PASS: Each item in the findings section
references at least one named competitor row or Phase 1 map entry by label. No finding is
free-floating. PARTIAL: More than half of findings are grounded; at least one is not. FAIL:
Findings section does not require Phase 1 anchoring.

**C-11 — Phase 1 pre-map table with verbatim rows.** PASS: Phase 1 produces a labeled table
with named rows. A verbatim-only rule is stated explicitly — row labels must appear unchanged
downstream. A FAILS/PASS pair is present (at phase instruction level, in the SR block, or
both) demonstrating an acceptable vs. unacceptable row label. PARTIAL: Table present; verbatim
rule absent or FAILS/PASS pair absent. FAIL: Phase 1 uses a list, narrative, or no structure.

**C-12 — Phase 4 whitespace dual-line template.** PASS: Phase 4 whitespace uses a labeled
two-line template with both required slot labels explicitly stated (e.g., Competitive gap: and
Focus gap:). A FAILS/PASS pair is present at the phase instruction level showing a compliant
vs. non-compliant whitespace entry. PARTIAL: Template present; one label missing or no
FAILS/PASS pair at phase instruction level. FAIL: Whitespace is free-form prose or the
template has a single undifferentiated field.

**C-13 — Phase 2 inertia three labeled mechanism slots.** PASS: Phase 2 inertia uses exactly
three labeled mechanism slots (WORKAROUND SATISFACTION, SWITCHING COST, HABIT LOCK-IN or
equivalent domain-specific labels). Each slot carries its own FAILS/PASS pair at the slot
instruction level requiring mechanism specificity. PARTIAL: Slots present; fewer than three
carry FAILS/PASS pairs, or labels are unlabeled bullet positions. FAIL: Inertia section uses
narrative or a single undifferentiated block.

**C-14 — Hard-stacked SR meta-declaration.** PASS: The SR block contains an explicit
preamble or opening declaration stating that all three primary structural requirements enforce
via the same apparatus type. The declaration names the apparatus (e.g., "named format artifact
+ format-failure declaration + FAILS/PASS rejection example pair" or "table schema with
empty-cell failure surface"). PARTIAL: Meta-declaration present but does not name the
apparatus type or does not cover all three constraints. FAIL: SR block lists constraints
without a unifying meta-declaration.

**C-15 — Map Position column with verbatim-only rule.** PASS: The competitor table includes
an explicit Map Position column. A verbatim-only rule is stated: content in Map Position must
be copied unchanged from a Phase 1 row label. An empty-cell failure is declared — an absent
Map Position entry fails the output. PARTIAL: Column present; verbatim rule or empty-cell
failure declaration absent. FAIL: Competitive positioning is embedded in a prose cell or
inferred column without explicit constraint.

**C-16 — Domain-exclusive portability test.** PASS: The inertia mechanism content is
required to pass a portability test: each mechanism must fail if substituted into a different
product category. A standalone test block with an exact fail condition (e.g., "if this
mechanism reads as true for a social network, it fails") is present. PARTIAL: Portability
requirement stated without a standalone test block or without an exact fail condition. FAIL:
Mechanism content is not required to be domain-exclusive.

**C-17 — Symmetric structural enforcement signature.** PASS: All three structural constraints
(pre-map table / inertia mechanism slots / whitespace template) carry an identical enforcement
apparatus. The SR block or a closing verification element explicitly confirms that the same
apparatus type is present across all three — not by listing each separately but by asserting
symmetry. PARTIAL: Two of three constraints carry identical apparatus; the third is
narratively softer or uses a different mechanism. FAIL: Constraints enforce via heterogeneous
mechanisms with no symmetry assertion.

**C-18 — Phase-level three-component enforcement fingerprint.** PASS: Each of the three
structural constraints carries an identical three-component fingerprint at its phase
instruction — (1) named format artifact, (2) format-failure declaration, (3) explicit
FAILS/PASS rejection example pair — all three components present within or immediately
adjacent to the phase instruction block, not deferred exclusively to the SR preamble. PARTIAL:
One or two constraints carry the full fingerprint at phase instruction level; the remaining
constraint(s) carry the pair only in the SR block. FAIL: No constraint carries all three
components at phase instruction level; fingerprints are SR-block-only or absent.

**C-19 — Apparatus type uniformity across structural constraints.** PASS: All three
structural constraints use the same apparatus type — either all table schema (each constraint
produces a table whose absent or empty cell/row is the observable failure surface) or all
labeled-slot blocks (each constraint produces a named slot whose absence is the failure
surface). Apparatus type is uniform by construction, not by assertion. PARTIAL: Two of three
constraints share an apparatus type; the third uses a different mechanism. FAIL: Each
constraint uses a different apparatus type (one table, one dual-line template, one labeled
block).

**C-20 — Symmetric pre-submission verification loop.** PASS: A PRE-SUBMISSION VERIFICATION
block is present that asks identical sub-questions per constraint for all three structural
constraints: (1) format artifact present? (2) format-failure declared? (3) enforcement
apparatus present? The loop is symmetric — same number of sub-questions for each constraint,
all three constraints covered. PARTIAL: Verification block present but asymmetric — more
sub-questions for one constraint than another, or only two of three constraints covered, or
sub-questions check criterion names rather than enforcement components. FAIL: No verification
block, or verification block is a flat list without per-constraint sub-questions.

**C-21 — Dual-layer table enforcement.** PASS: C-18 PASS and C-19 PASS simultaneously. All
three structural constraints use table schema (satisfying C-19) and each table's phase
instruction block carries the full three-component fingerprint — named format artifact,
format-failure declaration, FAILS/PASS pair — proximate to the instruction (satisfying C-18).
The table cell/row is simultaneously the format artifact named in the fingerprint and the
observable failure surface in the table structure, creating non-redundant dual-layer
enforcement. PARTIAL: Not applicable — C-21 does not award partial credit. C-18 PARTIAL
disqualifies C-21. FAIL: C-18 fails or is partial, or C-19 fails, or apparatus is not table
schema.

**C-22 — Structural-procedural verification duality.** PASS: C-19 PASS and C-20 PASS
simultaneously. All three structural constraints use table schema (satisfying C-19) and a
symmetric pre-submission verification loop is present (satisfying C-20). The two enforcement
layers are non-redundant: the table schema provides structural-level enforcement observable at
generation time; the verification loop provides procedural-level enforcement confirmed at
review time. PARTIAL: Not applicable — C-22 does not award partial credit. FAIL: C-19 fails
(mixed apparatus), or C-20 fails (no symmetric loop or asymmetric loop), or both fail.

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 – C-05 | 12 | 60 |
| Recommended | C-06 – C-08 | 10 | 30 |
| Aspirational | C-09 – C-22 | 5 (2.5 partial) | 70 |
| **Max composite** | | | **160** |

**Breakthrough threshold:** > 145

**Grade bands:**

| Score | Grade |
|-------|-------|
| 155 – 160 | Exceptional |
| 146 – 154.5 | Breakthrough |
| 136 – 145 | Strong |
| 120 – 135 | Passing |
| < 120 | Below bar |
```
