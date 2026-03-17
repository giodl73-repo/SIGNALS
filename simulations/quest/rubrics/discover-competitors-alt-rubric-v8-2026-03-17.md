---
skill: quest-rubric
skill_target: discover-competitors-alt
date: 2026-03-17
version: 8
---

# discover-competitors-alt Rubric — v8

Carry-forward of v7. No new R7 findings to incorporate; all criteria and scoring unchanged.

**Skill description:** Unified competitive analysis skill. Single prompt handles base competitive
analysis AND optional focus dimensions (market sizing, positioning framework) in one coherent
output. Focus is woven throughout, not appended. Inertia competitor (None / status quo) is always
assessed first. AMEND block shifts focus dimension or adjusts depth.

---

## Essential Criteria (weight = 60 points total, 12 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Inertia-first assessment | correctness | "None / status quo" is assessed as the first competitor entry. Threat level is explicitly HIGH. Analysis explains why teams do nothing. |
| C-02 | Focus woven, not appended | behavior | When a focus dimension (market or positioning) is provided, that content is distributed throughout the output -- visible in competitor rows, findings, and narrative -- not isolated in a trailing section. |
| C-03 | Threat level assigned per competitor | correctness | Every named competitor and inertia receive an explicit HIGH / MEDIUM / LOW threat rating. No competitor is rated without a threat level. |
| C-04 | Whitespace identified | coverage | Output includes an uncontested space or gap that no listed competitor owns. Stated in its own finding or clearly labeled. |
| C-05 | Auto-detect without prompting | behavior | Topic domain is inferred from context (README, CLAUDE.md, package.json, etc.). Output does not ask the user to supply domain or competitor names. |

---

## Recommended Criteria (weight = 30 points total, 10 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Inertia stickiness reasoning | depth | Inertia section explains at least one concrete mechanism -- switching cost, habit lock-in, or workaround satisfaction -- not just "inertia is high." |
| C-07 | Web-verified competitive claim | correctness | At least one named competitor characterization is supported by an inline citation (URL or publication) from a WebSearch result. |
| C-08 | AMEND section with 3 actionable adjustments | format | AMEND lists exactly 3 adjustments. Each names both what the user changes and what changes in the output. |

---

## Aspirational Criteria (weight = 90 points total)

Partial credit (2.5 pts) available where noted. Criteria marked with no partial are binary.

| ID | Criterion | Category | Full / Partial |
|----|-----------|----------|----------------|
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
| C-21 | Dual-layer table enforcement | structure | 5 / -- |
| C-22 | Structural-procedural verification duality | structure | 5 / -- |
| C-23 | Bilateral pair structural invariant declaration | structure | 5 / 2.5 |
| C-24 | SR-block-free structural enforcement architecture | structure | 5 / -- |
| C-25 | Explicit constraint designation token in multi-table phases | structure | 5 / 2.5 |
| C-26 | Dual-loop verification architecture | structure | 5 / 2.5 |

---

## Criterion Definitions

**C-09 -- Cross-dimensional whitespace finding.** PASS: The whitespace finding names a gap that
is uncontested across both the competitive dimension and the focus dimension. The finding is not
achievable by dropping the focus input -- its content requires Phase 1 map data and the focus
dimension simultaneously. PARTIAL: Finding references one dimension only. FAIL: Finding is generic
or does not require Phase 1 data.

**C-10 -- Table-stakes grounding per finding.** PASS: Each item in the findings section references
at least one named competitor row or Phase 1 map entry by label. No finding is free-floating.
PARTIAL: More than half of findings are grounded; at least one is not. FAIL: Findings section does
not require Phase 1 anchoring.

**C-11 -- Phase 1 pre-map table with verbatim rows.** PASS: Phase 1 produces a labeled table with
named rows. A verbatim-only rule is stated explicitly -- row labels must appear unchanged
downstream. A bilateral enforcement pair is present (at phase instruction level, in the SR block
or opening declaration, or both) demonstrating an acceptable vs. unacceptable row label.
PARTIAL: Table present; verbatim rule absent or bilateral pair absent. FAIL: Phase 1 uses a list,
narrative, or no structure.

**C-12 -- Phase 4 whitespace dual-line template.** PASS: Phase 4 whitespace uses a labeled
two-line template with both required slot labels explicitly stated (e.g., Competitive gap: and
Focus gap:). A bilateral enforcement pair is present at the phase instruction level showing a
compliant vs. non-compliant whitespace entry. PARTIAL: Template present; one label missing or no
bilateral pair at phase instruction level. FAIL: Whitespace is free-form prose or the template has
a single undifferentiated field.

**C-13 -- Phase 2 inertia three labeled mechanism slots.** PASS: Phase 2 inertia uses exactly
three labeled mechanism slots (WORKAROUND SATISFACTION, SWITCHING COST, HABIT LOCK-IN or
equivalent domain-specific labels). Each slot carries its own bilateral enforcement pair at the
slot instruction level requiring mechanism specificity. PARTIAL: Slots present; fewer than three
carry bilateral pairs, or labels are unlabeled bullet positions. FAIL: Inertia section uses
narrative or a single undifferentiated block.

**C-14 -- Hard-stacked SR meta-declaration.** PASS: The prompt contains an explicit preamble,
opening declaration, or SR block stating that all three primary structural requirements enforce
via the same apparatus type. The declaration names the apparatus (e.g., "named format artifact +
format-failure declaration + bilateral rejection example pair" or "table schema with empty-cell
failure surface"). A dedicated numbered SR block is sufficient but not necessary -- a two-sentence
opening symmetry assertion satisfies this criterion equally. PARTIAL: Meta-declaration present but
does not name the apparatus type or does not cover all three constraints. FAIL: Constraints are
listed without any unifying meta-declaration.

**C-15 -- Map Position column with verbatim-only rule.** PASS: The competitor table includes an
explicit Map Position column. A verbatim-only rule is stated: content in Map Position must be
copied unchanged from a Phase 1 row label. An empty-cell failure is declared -- an absent Map
Position entry fails the output. PARTIAL: Column present; verbatim rule or empty-cell failure
declaration absent. FAIL: Competitive positioning is embedded in a prose cell or inferred column
without explicit constraint.

**C-16 -- Domain-exclusive portability test.** PASS: The inertia mechanism content is required
to pass a portability test: each mechanism must fail if substituted into a different product
category. A standalone test block with an exact fail condition (e.g., "if this mechanism reads as
true for a social network, it fails") is present. PARTIAL: Portability requirement stated without
a standalone test block or without an exact fail condition. FAIL: Mechanism content is not required
to be domain-exclusive.

**C-17 -- Symmetric structural enforcement signature.** PASS: All three structural constraints
(pre-map table / inertia mechanism slots / whitespace template) carry an identical enforcement
apparatus. An SR block, opening symmetry assertion, or closing verification element explicitly
confirms that the same apparatus type is present across all three -- not by listing each
separately but by asserting symmetry. PARTIAL: Two of three constraints carry identical apparatus;
the third is narratively softer or uses a different mechanism. FAIL: Constraints enforce via
heterogeneous mechanisms with no symmetry assertion.

**C-18 -- Phase-level three-component enforcement fingerprint.** PASS: Each of the three
structural constraints carries an identical three-component fingerprint at its phase instruction
-- (1) named format artifact, (2) format-failure declaration, (3) bilateral rejection example pair
(any label format: FAILS/PASS, DO NOT/DO, or equivalent structural framing) -- all three
components present within or immediately adjacent to the phase instruction block, not deferred
exclusively to the SR preamble or opening declaration. The bilateral structure (rejection example
+ acceptance example) is the invariant; the label format is surface. PARTIAL: One or two
constraints carry the full fingerprint at phase instruction level; the remaining constraint(s)
carry the pair only in the SR block or opening declaration. FAIL: No constraint carries all three
components at phase instruction level; fingerprints are centralized-only or absent.

**C-19 -- Apparatus type uniformity across structural constraints.** PASS: All three structural
constraints use the same apparatus type -- either all table schema (each constraint produces a
table whose absent or empty cell/row is the observable failure surface) or all labeled-slot blocks
(each constraint produces a named slot whose absence is the failure surface). When a phase
produces multiple tables, only the explicitly designated structural constraint table counts toward
apparatus uniformity; companion tables labeled as additional framing or explicitly declared
non-substitutable do not dilute apparatus type. Apparatus type is uniform by construction, not by
assertion. PARTIAL: Two of three constraints share an apparatus type; the third uses a different
mechanism. FAIL: Each constraint uses a different apparatus type, or multi-table phase ambiguity
leaves apparatus identity unresolved on reviewer inference.

**C-20 -- Symmetric pre-submission verification loop.** PASS: A post-generation PRE-SUBMISSION
VERIFICATION block (or equivalently-labeled closing loop) is present that asks identical
sub-questions per constraint for all three structural constraints: (1) format artifact present?
(2) format-failure declared? (3) enforcement apparatus present? The loop is symmetric -- same
number of sub-questions for each constraint, all three constraints covered. The presence of an
additional pre-generation loop elsewhere in the prompt does not confuse C-20; label and post-phase
placement are the determinative signals. PARTIAL: Verification block present but asymmetric --
more sub-questions for one constraint, or only two of three constraints covered, or sub-questions
check criterion names rather than enforcement components. FAIL: No verification block, or
verification block is a flat list without per-constraint sub-questions.

**C-21 -- Dual-layer table enforcement.** PASS: C-18 PASS and C-19 PASS simultaneously. All three
structural constraints use table schema (satisfying C-19) and each table phase instruction block
carries the full three-component fingerprint -- named format artifact, format-failure declaration,
bilateral rejection example pair -- proximate to the instruction (satisfying C-18). The table
cell/row is simultaneously the format artifact named in the fingerprint and the observable failure
surface in the table structure, creating non-redundant dual-layer enforcement. PARTIAL: Not
applicable -- C-21 does not award partial credit. C-18 PARTIAL disqualifies C-21. FAIL: C-18
fails or is partial, or C-19 fails, or apparatus is not table schema.

**C-22 -- Structural-procedural verification duality.** PASS: C-19 PASS and C-20 PASS
simultaneously. All three structural constraints use table schema (satisfying C-19) and a
symmetric post-generation verification loop is present (satisfying C-20). The two enforcement
layers are non-redundant: the table schema provides structural-level enforcement observable at
generation time; the verification loop provides procedural-level enforcement confirmed at review
time. PARTIAL: Not applicable -- C-22 does not award partial credit. FAIL: C-19 fails (mixed
apparatus), or C-20 fails (no symmetric loop or asymmetric loop), or both fail.

**C-23 -- Bilateral pair structural invariant declaration.** PASS: The bilateral pair requirement
is stated in structural terms throughout -- both instructions and verification loop use
label-agnostic language. Instructions use "rejection example + acceptance example," "DO NOT/DO,"
or equivalent structural framing rather than "FAILS/PASS label required," AND the verification
loop checks "rejection example pair present?" or "bilateral enforcement pair present?" (not
"FAILS/PASS pair present?"). Both instruction language and loop language must be label-agnostic
for full PASS. PARTIAL: Instructions use a label-agnostic bilateral format (e.g., DO NOT/DO) but
the verification loop retains "FAILS/PASS pair present?" -- the invariant is practiced in
instructions but not declared in the loop. FAIL: Both instructions and verification loop use
"FAILS/PASS" label notation exclusively; the bilateral structure invariant is not stated.

**C-24 -- SR-block-free structural enforcement architecture.** PASS: No numbered SR preamble
block is present. C-14 and C-17 are satisfied entirely through (a) an opening symmetry assertion
(one to two sentences naming all three constraints and their shared apparatus type) and (b)
phase-embedded constraint declarations at each structural constraint phase instruction (e.g.,
"C-13 structural constraint. Apparatus: table schema." immediately before the mechanism table
schema). The opening assertion provides the meta-declaration; the phase-embedded declarations
provide the per-constraint enforcement. PARTIAL: Not applicable -- C-24 is binary. A numbered SR
preamble block is either absent (PASS) or present (FAIL), regardless of whether phase-embedded
declarations are also present. FAIL: A numbered SR preamble block is present.

**C-25 -- Explicit constraint designation token in multi-table phases.** PASS: For each phase
that produces more than one table, two conditions both hold: (a) the structural constraint table
is identified by an explicit designation token -- "(C-13)" in the FAILS pair header, "C-13
structural constraint" in the phase instruction, or equivalent -- naming which table is the
structural constraint for C-19 apparatus uniformity purposes, and (b) any companion tables in the
same phase carry an explicit non-substitutability declaration ("summary table does not substitute
for the mechanism table," "additional table is framing only"). PARTIAL: Designation token present
but companion table non-substitutability not explicitly declared, or vice versa. FAIL: A phase
produces multiple tables with no disambiguation; apparatus identity is left to reviewer inference.
A prompt with no multi-table phases earns PASS by vacuous satisfaction -- C-25 is load-bearing
only when multi-table phases exist.

**C-26 -- Dual-loop verification architecture.** PASS: Both a pre-generation integrity check AND
a post-generation PRE-SUBMISSION VERIFICATION loop are present. The pre-generation loop checks
prompt completeness (for each structural constraint: format artifact declared in prompt?
format-failure declared in prompt? bilateral pair present in prompt?). The post-generation loop
checks output completeness (for each structural constraint: format artifact present in output?
format-failure declared? enforcement apparatus present?). The two loops check different subjects
-- prompt vs. output -- and are non-competing: the post-generation loop satisfies C-20; the
pre-generation loop is additive. C-26 cannot pass if C-20 fails. PARTIAL: A pre-generation loop
is present but checks output correctness (duplicating C-20's subject) rather than prompt
completeness, or covers fewer than all three structural constraints. FAIL: Only one loop present
(either pre-generation or post-generation only), or C-20 fails.

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 -- C-05 | 12 | 60 |
| Recommended | C-06 -- C-08 | 10 | 30 |
| Aspirational | C-09 -- C-26 | 5 (2.5 partial where applicable) | 90 |
| **Max composite** | | | **180** |

**Composite formula:**
- Essential: 60 pts (all-or-nothing per criterion: 12 pts each)
- Recommended: 30 pts (all-or-nothing per criterion: 10 pts each)
- Aspirational: 90 pts (5 pts full, 2.5 pts partial where applicable; no partial for C-21, C-22, C-24)

**Golden threshold:** All 5 essential pass AND composite >= 80

**Breakthrough threshold:** > 165

**Grade bands:**

| Score | Grade |
|-------|-------|
| 175 -- 180 | Exceptional |
| 166 -- 174.5 | Breakthrough |
| 150 -- 165 | Strong |
| 135 -- 149 | Passing |
| < 135 | Below bar |

---

## Pattern Registry (v1 through v7 learnings)

| Pattern | Criterion | First confirmed |
|---------|-----------|----------------|
| Inertia-first ordering | C-01 | v1 |
| Focus woven throughout | C-02 | v1 |
| Bilateral pair structure is C-18 invariant (not FAILS/PASS label) | C-18, C-23 | v6 R6-V03 |
| SR block sufficient but not necessary for C-14/C-17 | C-14, C-17, C-24 | v6 R6-V04 |
| Explicit constraint designation token prevents C-19 ambiguity | C-19, C-25 | v6 R6-V01 |
| Pre-generation loops non-competing with C-20 | C-20, C-26 | v6 R6-V02 |
| Phase-level bilateral pairs as minimal sufficient C-17 mechanism | C-18 | v5 |
| All-table apparatus uniformity as distinct C-17 path | C-19 | v5 |
| Symmetric pre-submission verification loop as highest-confidence path | C-20 | v5 |
| Table column > inline text field | C-15 | v3 |
| Portability test operationalizes domain-exclusivity | C-16 | v3 |
| Dual-layer table enforcement | C-21 | v6 |
| Structural-procedural verification duality | C-22 | v6 |

---

## Version History

| Version | Changes |
|---------|---------|
| v1 | Initial rubric: C-01 to C-08 |
| v2 | C-09 (cross-dimensional whitespace), C-10 (table-stakes grounding) |
| v3 | C-11 to C-13 (phase-level tables), C-14 (SR meta-declaration), C-15 (Map Position), C-16 (portability test) |
| v4 | C-17 (symmetric enforcement signature) |
| v5 | C-18 (phase-level fingerprint), C-19 (apparatus uniformity), C-20 (symmetric loop) |
| v6 | C-21 (dual-layer table), C-22 (structural-procedural duality); max composite 160 |
| v7 | C-23 (bilateral invariant declaration), C-24 (SR-block-free), C-25 (designation token), C-26 (dual-loop); max composite 180. C-11/12/13 text updated to use "bilateral enforcement pair" language. C-14 acknowledges opening assertion path. C-17 lists opening assertion as valid path. C-18 states bilateral structure is invariant. C-19 addresses multi-table disambiguation. C-20 states pre-generation loop non-competing. |
| v8 | Carry-forward of v7. No new R7 findings. Criteria, scoring, and definitions unchanged. |
