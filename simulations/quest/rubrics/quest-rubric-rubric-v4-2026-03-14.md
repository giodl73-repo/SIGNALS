Reading the v3 structure carefully before writing v4.

The three R3 excellence patterns to codify:
1. `labeled-gate-headers-unlock-c16` → **C-17**: amend gates require structural subheader labels, not inline prose numbering
2. `named-banned-qualifier-list-unlocks-c12` → **C-18**: rubric prompt must enumerate banned qualifier terms explicitly, not just instruct avoidance
3. `c15-mechanism-agnostic` → **C-19**: co-presence pass conditions test output state only; construction route is irrelevant

C-18 has a self-application implication: v4 must add an explicit banned-qualifier list somewhere in the document to PASS its own C-18. Placing it in the Design Rationale satisfies both C-15 (co-present with rejection log) and C-18.

---

```markdown
---
skill: quest-rubric
version: 4
date: 2026-03-14
---

# Quest Rubric Rubric — v4

## What Changed from v3

Three new aspirational criteria from R3 excellence signals:

| ID | Signal | What it tests |
|----|--------|---------------|
| C-17 | labeled-gate-headers-unlock-c16 | Amend-step gates require structural subheader labels (Gate 1 / Gate 2 / Gate 3), not inline prose numbering — label format is the gate, not content |
| C-18 | named-banned-qualifier-list-unlocks-c12 | Rubric prompt enumerates banned subjective qualifier terms explicitly by name; instruction-only approach ("avoid subjective language") produces PARTIAL on C-12; named list triggers the OR path and produces PASS |
| C-19 | c15-mechanism-agnostic | Co-presence pass conditions test output state only (both items present in section); any construction route that places both items there satisfies the gate; rubrics that specify a required mechanism over-constrain valid outputs |

Also added:
- **Explicit banned-qualifier list** in Design Rationale (C-18 self-application):
  good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate
- **Self-scoring projection** updated for C-17, C-18, C-19
- **v5 candidates** section updated

**Self-scoring projection (v4 against itself):**
- C-17: N/A (this rubric has no amend or revision phase; excluded from denominator)
- C-18: PASS (Design Rationale contains explicit enumerated list of >= 4 banned terms)
- C-19: PASS (C-15 pass condition states output-state gate only, names no required construction mechanism)

---

## Design Rationale

The dominant failure mode for a rubric is that its criteria test generic document quality
rather than the specific behaviors that make outputs of this skill useful or useless. A rubric
that rewards "well-structured output" or "complete response" will score equally well on a
hallucinated rubric and a precisely-calibrated one.

**Inertia filter**: Every criterion was kept only if it would catch a failure that
"output is well-structured" would miss.

**Rejection log** (generic criteria considered and rejected):

- G-01: "Criteria are clearly written" — circular; clear criteria testing the wrong behaviors
  are worse than useless.
- G-02: "Rubric is comprehensive" — no observable signal; comprehensiveness is a conclusion,
  not a gate.
- G-03: "Criteria are high quality" — tautological; restates the goal without specifying what
  high quality means.

**Self-application (C-04 failure point)**: A poor output of this skill would fail C-04 —
its essential criteria would test "is the rubric well-written" rather than naming specific
skill behaviors. A strong output passes all five essential criteria and at least two of
C-06, C-07, C-08.

**Banned qualifier list** (C-18 self-application): The following terms are banned from pass
conditions without a measurable anchor alongside them:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate.

---

## Essential Criteria

These must all pass. A rubric that fails any essential criterion is not usable.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | **All five required fields are present** — Each criterion row contains: ID, Text, Weight, Category, and Pass Condition. No field is left blank or missing. | essential | format | Every row in every criteria table contains all five fields with no field left blank or missing. |
| C-02 | **Weight distribution is within spec** — The rubric contains 3–5 essential criteria, 2–3 recommended criteria, and 1–2 aspirational criteria. | essential | correctness | Count of essential in [3,5]; count of recommended in [2,3]; count of aspirational in [1,2]. |
| C-03 | **Composite score formula and golden threshold are stated correctly** — The rubric declares the composite formula (60/30/10 split) and the golden threshold (all essential pass + composite >= 80). | essential | correctness | Formula present with weights 60, 30, 10 for essential/recommended/aspirational bands; threshold stated as >= 80 with the all-essential-pass precondition. |
| C-04 | **Criteria are skill-specific** — Essential criteria test the actual non-negotiable behaviors of the target skill, not generic document quality (no criteria like "is well-written" or "is complete"). | essential | correctness | At least 3 of the essential criteria name specific behaviors, outputs, or structural properties unique to the target skill; none are purely generic quality signals. |
| C-05 | **Pass conditions are binary and testable** — Every pass condition can be evaluated as pass/fail without subjective judgment; each uses observable signals (counts, presence/absence, specific patterns, measurable thresholds). | essential | behavior | All pass conditions use verifiable criteria; none require subjective assessment ("good", "sufficient", "appropriate" without a measurable anchor). |

---

## Recommended Criteria

These improve rubric usability. A rubric without them is acceptable but weaker.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | **Criteria ordered by weight tier** — Essential criteria appear before recommended, recommended before aspirational. Each tier is clearly separated and labeled. | recommended | format | Sections appear in order: essential → recommended → aspirational, with distinct headers or table sections per tier. |
| C-07 | **Categories drawn from the allowed set** — Every criterion category is one of the five canonical values: correctness, depth, format, coverage, behavior. No invented categories. | recommended | correctness | All category fields contain only: correctness, depth, format, coverage, or behavior; no other values. |
| C-08 | **Essential criteria cover distinct failure modes** — No two essential criteria test the same behavior; together they catch at least four distinct ways an output can fail to be useful. | recommended | coverage | No two essential criteria have overlapping pass conditions; reviewers can identify at least four distinct failure modes caught by the essential set. |

---

## Aspirational Criteria

These raise the bar once essential and recommended are stable.

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | **Rubric is calibrated** — A reviewer using this rubric can correctly classify a mediocre output (scores < 80) and an excellent output (scores >= 80) without ambiguity. At least one essential criterion would catch a real failure in a poor output. | aspirational | depth | Reviewer can produce a concrete example of a poor output that fails >= 1 essential criterion, and a strong output that passes all essential and >= 2 recommended criteria. |
| C-10 | **Evolution hook present** — The rubric acknowledges it should grow as quest-golden discovers excellence patterns; frontmatter includes a version field and the document includes a note about how the rubric should be updated over time. | aspirational | behavior | Frontmatter has version field populated; OR document contains a section/note describing how the rubric should evolve as golden outputs are discovered. |
| C-11 | **Inertia framing in design rationale** — The rubric design rationale names the dominant failure mode for the target skill before listing any criteria. Naming the enemy first anchors every subsequent review decision as a persistent filter rather than a per-criterion afterthought. | aspirational | depth | Design rationale contains an explicit statement of the most common or most dangerous failure mode for the target skill; this statement appears before the first criteria table. |
| C-12 | **Pass conditions use closed-world gates** — Each pass condition is phrased as a binary gate with explicit unacceptable-signal anchors. Subjective terms ("good", "sufficient", "appropriate", "thorough", "complete") do not appear in pass conditions without a measurable anchor alongside them. | aspirational | behavior | No pass condition contains a bare subjective qualifier without a count, threshold, or presence/absence anchor; OR the rubric explicitly lists banned subjective terms and at least 3 pass conditions demonstrate the pattern ("X is present" / "count >= N" / "none of Y"). |
| C-13 | **Rejection log proves the specificity filter ran** — The design rationale or notes section names at least one generic criterion that was considered and rejected, with the rejection stated explicitly. Proving the filter ran is stronger than asserting the intent to run it. | aspirational | depth | Design rationale or notes section contains at least one named example of a rejected generic criterion (e.g., "output is well-structured", "is clear and complete") stated as explicitly rejected, not merely implied. |
| C-14 | **Design rationale precedes criteria tables** — The design rationale section (or equivalent intent block) appears in the output document before the first criteria table. Position is not cosmetic: when inertia framing and failure-mode enumeration are written before the criteria exist, they constrain construction rather than rationalizing it after the fact. V-04 and V-05 had identical content; only V-05 satisfied the positional gate. | aspirational | format | Design rationale section (or equivalent block describing dominant failure mode, rejected criteria, or construction intent) appears before the first Essential criteria table in the document; no criteria table appears above the design rationale text. |
| C-15 | **Self-application and rejection log co-present in design rationale** — The design rationale contains both (1) a self-application result naming at least one essential criterion ID that a concrete poor output would fail, and (2) at least one named rejected generic criterion. Both slots are populated in the same section with zero mutual interference. V-05 was the only R2 variation to achieve both simultaneously; R3 showed that auditor-calibration, interrogative-question, and self-application-gate routes all satisfy the pass condition — the gate is mechanism-agnostic. | aspirational | depth | Design rationale section contains: (1) at least one essential criterion ID cited as the failure point for a described poor output, AND (2) at least one explicitly rejected generic criterion named by its text; both items present in the same design rationale section, not distributed to separate appendices or notes. |
| C-16 | **Amend step covers all three primary criterion failure modes as distinct gates** — The rubric prompt's amend or revision step addresses all three primary ways a criterion can fail: (1) the criterion text is generic rather than skill-specific, (2) the pass condition is not binary and testable, (3) the criterion duplicates a failure mode already caught by another criterion. Each failure mode is a distinct explicit question, not bundled into freeform editorial guidance. | aspirational | behavior | Amend or revision checklist contains three distinct questions explicitly addressing: (1) generic-vs-specific content, (2) binary-pass-condition testability, (3) redundant-failure-mode overlap; all three present and distinct; none merged into a single open-ended revision prompt. N/A if the skill design includes no revision phase. |
| C-17 | **Amend-step gates use structural subheader labels, not inline prose numbering** — When an amend or revision step presents multiple named gates, each gate must appear as a distinct structural subheader label (e.g., "Gate 1:", "Gate 2:", "Gate 3:") rather than as inline numbered prose within a paragraph. The label format makes each gate independently addressable and scannable; prose numbering conflates the gate identity with the instruction text and prevents gate-level pass/fail assessment. R3 finding: variations that embedded gate numbers in prose paragraphs scored PARTIAL on C-16; variations with structural labels scored PASS. | aspirational | format | Amend or revision step contains >= 3 gate labels as structural subheaders or clearly delineated labeled blocks (e.g., bold header, colon-terminated label on its own line); inline numbered list items within a prose paragraph do not satisfy this criterion. N/A if the skill design includes no revision phase. |
| C-18 | **Banned-qualifier list is explicit and enumerated, not instructional** — The rubric prompt names the disallowed subjective terms explicitly by listing them as a closed vocabulary (e.g., "good / sufficient / appropriate / clear / complete / thorough") rather than only instructing reviewers to "avoid subjective language." An explicit enumerated list is a closed gate; a general instruction is an open filter that each reviewer re-interprets independently. R3 finding: V-04 (8 banned terms) and V-05 (6 banned terms) triggered the C-12 OR path and scored PASS; V-01, V-02, V-03 used the instruction-only approach and scored PARTIAL on C-12. | aspirational | behavior | Rubric prompt or construction section contains an explicit enumerated list of >= 4 banned subjective qualifier terms named individually; the list appears in the construction or design rationale section (not only embedded in a single pass condition); N/A if the skill produces no textual criteria with pass conditions. |
| C-19 | **Co-presence pass conditions are mechanism-agnostic output-state gates** — Pass conditions that require two items to co-exist in the same section (e.g., criterion ID + rejected generic, poor-output example + strong-output example) specify only the output state — both items present in the named section — without naming a required construction mechanism or authoring route. Over-specifying the mechanism rejects valid outputs that achieve the same state through a different path. R3 finding: auditor-calibration route, interrogative-question route, and self-application-gate route all satisfied C-15's literal pass condition because C-15 tests output state only. | aspirational | behavior | Each co-presence requirement in the rubric (any pass condition requiring two distinct items in the same section) is stated as an output-state check (both X and Y appear in section Z) without naming a required construction route; OR the rubric contains a note confirming that multiple construction routes satisfy each co-presence gate. PASS if all co-presence pass conditions in the rubric are mechanism-agnostic; PARTIAL if >= 1 co-presence condition names a required mechanism. |

---

## Scoring

**Composite formula**:
(essential_pass_count / essential_total) × 60
+ (recommended_pass_count / recommended_total) × 30
+ (aspirational_pass_count / aspirational_total) × 10

**Golden threshold**: all essential criteria pass AND composite score >= 80.

PARTIAL on an essential criterion counts as 0.5 pass for score computation but does not
satisfy the all-essential-pass precondition.

**N/A handling**: Structurally inapplicable criteria (e.g., C-16, C-17 for skills with no
revision phase) are excluded from both numerator and denominator of their band.

---

## Notes

**C-15 self-application slot**: A poor output of this rubric would fail C-04 — its criteria
would be generic quality signals ("is clear", "is complete") rather than skill-specific
behavior gates. A strong output passes all five essential criteria and at least C-06 and C-08
from the recommended set.

**C-18 banned-qualifier list**: good / sufficient / appropriate / clear / complete / thorough /
comprehensive / adequate. These terms are banned from pass conditions without a measurable
anchor (count, threshold, presence/absence signal) alongside them.

**C-16/C-17 N/A scope**: Both criteria apply only to rubric prompts that include an amend or
revision phase. A rubric that omits a revision phase is not penalized; both criteria are
excluded from the denominator for that rubric.

**Rejection log** (complete, versioned):
- G-01: "Criteria are clearly written" — circular
- G-02: "Rubric is comprehensive" — no observable signal
- G-03: "Criteria are high quality" — tautological

**Version**: 4. Grows as /quest:golden discovers excellence patterns.

---

## v5 Candidates

Patterns approaching threshold but not yet promoted:

- **amend-step-gate-count-scales-with-skill-complexity**: skills with >= 5 essential criteria
  may require a fourth gate in the amend step (format-consistency check); not enough data yet.
- **rejection-log-minimum-count-scales-with-aspirational-depth**: rubrics with >= 8 aspirational
  criteria may need >= 5 rejection log entries to demonstrate the specificity filter ran at
  sufficient depth; observed in v4 (3 entries, 11 aspirational criteria) but no variation test
  yet.
- **co-presence-section-scope-precision**: C-19 mechanism-agnostic finding may generalize to
  a requirement that co-presence gates name the exact section (not "anywhere in the document")
  to prevent diffuse co-presence that satisfies the letter but not the spirit of the gate.
```

---

**Summary of changes v3 → v4:**

| What | Detail |
|------|--------|
| C-17 added | Amend gates need structural subheader labels; prose numbering produces PARTIAL on C-16 |
| C-18 added | Rubric prompt must enumerate banned terms by name; instruction-only approach produces PARTIAL on C-12 |
| C-19 added | Co-presence pass conditions must test output state only; specifying a construction mechanism over-constrains valid outputs |
| C-15 text updated | Added R3 finding sentence confirming the mechanism-agnostic result (auditor/interrogative/self-application routes all pass) |
| Design Rationale | Added explicit banned-qualifier list (C-18 self-application); v4 self-scores PASS on C-18 |
| Self-scoring | C-17 N/A, C-18 PASS, C-19 PASS — v4 projects to same score as v3 on all prior criteria |
| v5 candidates | Three new near-threshold patterns tracked |
