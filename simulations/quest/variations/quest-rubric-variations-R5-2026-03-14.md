Written to `simulations/quest/variations/quest-rubric-variations-R5-2026-03-14.md`.

---

## Summary

**5 variations targeting v5 rubric's new criteria (C-20/C-21/C-22) plus the R4 structural gaps.**

### Planning table

| V-ID | Axis | Key design choice | Target criteria |
|------|------|-------------------|----------------|
| V-01 | Role sequence | R4/V-01 promoted + Phase 4 Output Contract Architect added as retroactive section auditor | C-03/C-09/C-10 (Scoring section), C-21 (failure inventory as equivalent block), C-13 still absent |
| V-02 | Output format | All 5 required sections front-loaded as a named contract before any phase instruction | C-20 (output contract names Scoring), C-13/C-14 (Rejection Log + DR as named slots) |
| V-03 | Lifecycle emphasis | Rejection phase expanded to standalone Phase 3 with explicit statement: "construction-time filtering alone does not satisfy this requirement" | C-22 (construction-time filter named insufficient), C-13 (named output section required) |
| V-04 | Phrasing register + Inertia framing | Imperative STOP CONDITIONS + Generic Rubric named and tested at every phase boundary | C-04 (skill-specific), C-12/C-18 (closed-world gates), secondary: Scoring section may be crowded out |
| V-05 | Role sequence + Output format | RubricArchitect role + canonical four-section output contract; failure inventory explicitly named as Design Rationale equivalent block; construction-time filter explicitly named insufficient in Phase 3 | C-20 + C-21 + C-22 simultaneously; v6 candidate "failure-analyst-skeleton-as-canonical-path" formalized |

**Key hypotheses:**
- V-01 vs V-02: retroactive audit (Phase 4) vs. front-loaded contract — which Scoring section placement is more reliable?
- V-03: does the explicit "construction-time filter insufficient" statement in the lifecycle phase produce C-22-satisfying rubrics more reliably than the output contract approach in V-02?
- V-04: does persistent inertia labeling add independent C-04 value beyond V-01's failure-analyst route, or does it crowd out the Scoring section?
- V-05: does formalizing the canonical path achieve C-20/C-21/C-22 simultaneously at the cost of C-08/C-11 analytical depth?
at production as a compliance checklist rather than an analytical exercise; Design Rationale is listed as required before Phase 1 completes, so the model may write a placeholder Design Rationale before the failure analysis informs it; V-01's Design Rationale (written after Phase 1) has higher inertia framing depth than V-02's (written before Phase 1 is done); V-03 and V-04 are the downstream comparators for rejection-log authenticity | All five required sections present in V-02 outputs including Scoring and named Rejection Log; C-03/C-09/C-10/C-13/C-14 PASS; Design Rationale quality metrics (inertia statement depth, failure-mode specificity) lower than V-01; the section list in the prompt header is the structural difference that explains the joint PASS |
| V-03 | Lifecycle emphasis (Rejection phase expanded with explicit output slot; construction-time filter named insufficient) | Expanding the rejection phase to a standalone Phase 3 with an explicit output requirement statement — "this phase has an explicit output requirement; construction-time filtering alone does not satisfy this criterion; the Rejection Log must appear as a named section in your output" — prevents C-22-style ambiguity where construction-time filtering activity produces a PARTIAL rather than a clear PASS or FAIL on C-13; the explicit disqualification statement forces the model to produce a named section, not merely run a silent filter | The "minimum 2 entries" constraint on the Rejection Log may cause forced deletions of legitimate criteria to meet the quota; V-01's failure inventory produces authentic failure-mode evidence as a byproduct of analysis; V-03's prompted quota produces a named section but the entries may be synthetic; V-04 and V-05 achieve rejection log presence via different mechanisms (the comparison tests whether prompted quotas degrade entry authenticity) | C-13 PASS in V-03 (named Rejection Log section present, ≥2 entries, at least one entry explicitly states it failed the construction-time-filter-insufficient test); at least one entry shows quota-fill pattern (named because the constraint required it rather than because the criterion was genuinely generic); V-01 rejection log absent; V-02 rejection log present via output contract |
| V-04 | Phrasing register + Inertia framing (combination: imperative STOP CONDITIONS + Generic Rubric named at every phase boundary) | Combining imperative register (hard STOP CONDITIONS at each phase, "STOP AND REWRITE" failure branches, not advisory language) with persistent inertia framing (Generic Rubric named and tested at each phase boundary — not only at construction time) prevents criteria drift from skill-specific toward generic quality signals across all phases while maintaining the behavioral discontinuity that blocks "proceed and note" bypass; the Generic Rubric is the inertia competitor for quest-rubric the way "status quo / do nothing" is for scout-competitors | Dense inertia labeling before each phase adds repetitive prompt structure; combined with imperative register, the model may fill available output tokens with inertia-check prose rather than criteria content and Scoring section structure; the Scoring section competes for space with the Generic Rubric Filter application that appears before Phase 3 emits; V-05 achieves equivalent inertia containment via role framing rather than inline labels — token-cheaper and less likely to crowd out the Scoring section | C-04 (skill-specific criteria) PASS rate highest in set at V-04; STOP CONDITIONS enforce phase gates; Scoring section present/absent varies across V-04 runs (token pressure competes with the inertia-check prose for output space); V-04 vs V-01 comparison isolates whether persistent inertia labeling adds independent C-04 value beyond the failure-analyst route |
| V-05 | Role sequence + Output format (combination: failure-analyst skeleton as canonical four-section path with explicit output contract) | Formalizing the failure-analyst skeleton (Phase 1 failure inventory → Phase 2 criterion construction + derivation notes → Phase 3 rejection log → Phase 4 rubric table + scoring section) as a canonical path named in both the role description and the output contract achieves C-20/C-21/C-22 compliance simultaneously: Scoring section is a required structural commitment (C-20), the failure inventory is explicitly named as satisfying the Design Rationale "or equivalent block" requirement (C-21), and the Rejection Log is a named output section that explicitly states construction-time filtering alone does not satisfy this gate (C-22) | Combining role sequencing with an explicit output contract creates the most constrained body in the set; the density of structural requirements may cause the model to produce a formulaic rubric that satisfies all structural criteria (C-01/C-02/C-03/C-06/C-13/C-14) but underperforms on analytical depth criteria (C-08 failure-mode distinctness, C-11 inertia framing specificity) because the analytical phases are subordinated to compliance requirements; V-01 produces higher C-08/C-11 quality because Phase 1 is free of output contract pressure; V-03/V-04 are downstream comparators naming V-05 as the site where combined-axis depth tradeoff manifests | C-20/C-21/C-22 all PASS in V-05; highest structural score in the round; C-08 (distinct failure modes) quality measurably lower than V-01 — failure inventory entries are shorter and less analytically grounded; total composite score is the round ceiling; the canonical-path formalization is the v6 candidate "failure-analyst-skeleton-as-canonical-path" evaluated as an experimental body |

---

## V-01 — Axis: Role sequence (Output Contract Architect as final phase)

**Axis:** Role sequence
**Primary effect:** Promoting R4/V-01's failure-analyst skeleton and adding an explicit Phase 4 Output Contract Architect — a checklist role that audits the output for missing sections before emission, including Scoring — prevents C-20's joint-failure pattern (C-03/C-09/C-10 simultaneously) while preserving V-01's failure-inventory route for C-11/C-14 (C-21 satisfied by the "or equivalent block" accommodation)
**Secondary effect:** Phase 4 runs retroactively after Phase 3 generates the rubric table; the model may complete Phase 3 without reserving structural space for the Scoring section, requiring back-patching at Phase 4; this produces awkward output ordering where the Scoring section lands after the rubric table rather than at the canonical position; C-13 (rejection log) still fails because V-01 adds no named rejection log output slot — the failure-analyst failure inventory is not equivalent to a rejection log
**Falsifiability check:** C-03/C-09/C-10 pass in V-01 (Scoring section present, formula stated, calibration example present); C-11/C-14 pass via failure inventory (C-21); Scoring section appears after the rubric table (ordering artifact visible); C-13 FAIL (no named rejection log section); top score higher than R4/V-01's 77.56

---

You are building a scoring rubric for the skill: **{skill_name}**.

You have been given:
- Skill spec: {skill_spec}
- Sample outputs (good and bad): {sample_outputs}

---

### Phase 1 — Failure Analyst

*Prevents: criteria anchored to generic document quality rather than skill-specific silent failures.*

Before writing any criterion, identify the top 6 ways this skill can fail silently. A silent failure is one where the output looks correct but would mislead or fail a consumer who trusted it.

For each failure, name:
- What went wrong
- Why it would not be caught by a generic quality check ("is the output well-structured?")

Format:

```
F-01: <failure name> — <what went wrong> — <why "well-structured output" would miss it>
F-02: ...
```

**STOP CONDITION:** Do not begin Phase 2 until all six failures are named with all three fields populated. A failure entry that restates a generic quality problem ("the output is unclear") is not a silent failure — it must name a behavior specific to this skill.

---

### Phase 2 — Criterion Writer

*Prevents: criteria that would score equally well on a hallucinated output and a correct one.*

Write one criterion per failure identified in Phase 1. Each criterion must:
- Name the specific behavior or structural property it tests (not the generic quality it approximates)
- Reference the failure it addresses, in parentheses (e.g., "Derived from F-03")

Then add any additional criteria required by the rubric structure spec below.

**Weight spec:**
- Essential: 3–5 criteria (the non-negotiables; if any fail, the rubric is unusable)
- Recommended: 2–3 criteria (improve rubric usability; acceptable to be missing but weaker)
- Aspirational: 1–2 criteria (raise the bar once essentials are stable)

**Category values:** correctness / depth / format / coverage / behavior

**Banned qualifiers** — may not appear in any pass condition without a measurable anchor alongside them:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

Write criteria in weight order: essential first, then recommended, then aspirational.

**STOP CONDITION:** Do not begin Phase 3 until criteria count is within spec for all three weight tiers, and no pass condition contains a banned qualifier without a measurable anchor.

---

### Phase 3 — Rubric Assembler

*Prevents: unordered criteria; missing required fields; ill-typed category values.*

Output the rubric as a Markdown table with these five columns, in this order:

| ID | Text | Weight | Category | Pass Condition |

Every row must have all five fields populated. No field may be left blank.

Order: essential rows first, then recommended, then aspirational.

---

### Phase 4 — Output Contract Architect

*Prevents: structural omissions that cause multiple scoring criteria to fail simultaneously regardless of criteria quality.*

Before emitting the final artifact, audit your output against this checklist:

- [ ] **Failure Inventory** — Phase 1 failures (F-01 through F-06) are present in the output document as a named section or block that precedes the rubric table
- [ ] **Rubric Table** — present with all five fields populated for every row
- [ ] **Scoring Section** — the output contains an explicit Scoring section that states:
  - The composite formula: essential band (60%) + recommended band (30%) + aspirational band (10%)
  - The golden threshold: all essential criteria must pass AND composite score >= 80
  - A calibration example: name one essential criterion ID and describe a concrete poor output that would fail it
  - An evolution hook: a statement that this rubric should grow as golden outputs are discovered, with a version field or note

If any section is absent: **add it before emitting.** Omitting the Scoring section is a structural gap that causes C-03 (formula + threshold), C-09 (calibration), and C-10 (evolution hook) to fail simultaneously regardless of how well the criteria themselves are written. No content-level refinement compensates for a missing Scoring section.

---

### Output

Emit in this order:
1. Failure Inventory (Phase 1 — F-01 through F-06, each with all three fields)
2. Derivation Notes (Phase 2 — one line per criterion: "C-NN derives from F-NN: <one sentence>")
3. Rubric Table (Phase 3 — ordered essential → recommended → aspirational)
4. Scoring Section (Phase 4 — formula, threshold, calibration example, evolution hook)

---

## V-02 — Axis: Output format (required sections front-loaded as a named contract)

**Axis:** Output format
**Primary effect:** Listing all five required output sections as a named structural contract at the top of the prompt — before any phase instruction — prevents structural omissions by making each section a pre-committed obligation the model must honor throughout construction; this is the output-contract-completeness-gate v6 candidate: one gate testing whether the output contract names all required sections (Failure Inventory, Rejection Log, Design Rationale, Rubric Table, Scoring) replaces the distributed C-03/C-09/C-10/C-13/C-14 failure pattern with a single root-cause finding
**Secondary effect:** Front-loading the section list causes the model to treat production as a compliance checklist rather than an analytical exercise; Design Rationale is listed as required before Phase 1 completes, so the model may write a placeholder Design Rationale before the failure analysis informs it; V-01's Design Rationale (written after Phase 1) has higher inertia framing depth than V-02's (written before Phase 1 is done); V-03 and V-04 are the downstream comparators for rejection-log authenticity
**Falsifiability check:** All five required sections present in V-02 outputs including Scoring and named Rejection Log; C-03/C-09/C-10/C-13/C-14 PASS; Design Rationale quality metrics (inertia statement depth, failure-mode specificity) lower than V-01; the section list in the prompt header is the structural difference that explains the joint PASS

---

You are building a scoring rubric for the skill: **{skill_name}**.

Inputs:
- Skill spec: {skill_spec}
- Sample outputs (good and bad): {sample_outputs}

---

### Required Output Sections

Your output must contain these five named sections in this order. Treat them as a contract: each section must be present and populated in the final document, regardless of how you construct the rubric internally.

1. **Design Rationale** — appears before the Rubric Table; names the dominant failure mode for this skill and at least one criterion that was considered and rejected, with rejection reason
2. **Failure Inventory** — list of 5–7 distinct ways this skill can fail silently; each entry explains why a generic "well-structured output" check would miss it
3. **Rejection Log** — criteria considered and deleted, with deletion reason per entry; minimum 1 entry; **construction-time filtering alone does not satisfy this requirement** — the log must appear as a named section in your output document
4. **Rubric Table** — criteria in weight order: essential (3–5), recommended (2–3), aspirational (1–2); all five fields (ID, Text, Weight, Category, Pass Condition) populated for every row
5. **Scoring** — composite formula (essential 60% + recommended 30% + aspirational 10%), golden threshold (all essential pass AND composite ≥ 80), calibration example (one criterion ID + poor output example), and evolution hook (version field or note that the rubric should grow as golden outputs are discovered)

Missing any of these five sections is a structural gap. Omitting the Scoring section causes the formula, calibration, and evolution criteria to fail simultaneously regardless of criteria quality.

---

### Phase 1 — Design Rationale

Write the Design Rationale section now. State:
- The dominant failure mode for this skill — the most common or most dangerous way outputs of this skill mislead consumers
- Why the "Generic Rubric" ("output is well-structured, clear, and complete") fails for this skill specifically
- At least one criterion you are tentatively rejecting before you begin construction, and why

This section must appear before the Rubric Table in your output.

---

### Phase 2 — Failure Inventory

List 5–7 ways this skill can fail silently. A silent failure looks correct but misleads a consumer who trusts it.

Format:
```
F-01: <failure name> — <what went wrong> — <why "well-structured output" would not catch it>
```

---

### Phase 3 — Criterion Construction

Write criteria derived from the failures in Phase 2. For each criterion:
- ID (C-01, C-02, ...)
- Text: name the specific behavior tested — not the generic quality it approximates
- Weight: essential / recommended / aspirational
- Category: correctness / depth / format / coverage / behavior
- Pass Condition: binary, observable, measurable

**Weight spec:**
- Essential: 3–5 criteria
- Recommended: 2–3 criteria
- Aspirational: 1–2 criteria

**Banned qualifiers** — may not appear in any pass condition without a measurable anchor:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

Write in weight order: essential first, then recommended, then aspirational.

---

### Phase 4 — Rejection Log

For every criterion you considered and rejected during Phase 3, record:

```
Rejected: "<criterion text>" — Reason: <one sentence>
```

This is a named output section. Recording deletions only in your reasoning does not satisfy this requirement — the log must appear in the artifact.

---

### Phase 5 — Scoring

Write the Scoring section:

**Composite formula:**
(essential_pass / essential_total) × 60
+ (recommended_pass / recommended_total) × 30
+ (aspirational_pass / aspirational_total) × 10

**Golden threshold:** All essential criteria pass AND composite score ≥ 80

**Calibration example:** Name one essential criterion ID and describe, in one sentence, a concrete poor output that would fail it.

**Evolution hook:** State that this rubric should grow as golden outputs are discovered. Include a version field in the document frontmatter.

---

### Constraints
- Emit all five required sections in the order: Design Rationale → Failure Inventory → Rejection Log → Rubric Table → Scoring
- Design Rationale appears before the Rubric Table
- Rejection Log is a named output section — not satisfied by filtering during construction without an output slot
- No criterion in the final table may use a banned qualifier without a measurable anchor

---

## V-03 — Axis: Lifecycle emphasis (Rejection phase expanded; construction-time filter named insufficient)

**Axis:** Lifecycle emphasis
**Primary effect:** Expanding the rejection phase to a standalone Phase 3 with an explicit output requirement statement — "this phase has an explicit output requirement; construction-time filtering alone does not satisfy this criterion; the Rejection Log must appear as a named section in your output" — prevents C-22-style ambiguity where construction-time filtering activity produces a PARTIAL rather than a clear PASS or FAIL on C-13; the explicit disqualification statement forces the model to produce a named section, not merely run a silent filter
**Secondary effect:** The "minimum 2 entries" constraint on the Rejection Log may cause forced deletions of legitimate criteria to meet the quota; V-01's failure inventory produces authentic failure-mode evidence as a byproduct of analysis; V-03's prompted quota produces a named section but the entries may be synthetic; V-04 and V-05 achieve rejection log presence via different mechanisms (the comparison tests whether prompted quotas degrade entry authenticity)
**Falsifiability check:** C-13 PASS in V-03 (named Rejection Log section present, ≥2 entries, at least one entry explicitly states it failed the construction-time-filter-insufficient test); at least one entry shows quota-fill pattern (named because the constraint required it rather than because the criterion was genuinely generic); V-01 rejection log absent; V-02 rejection log present via output contract

---

You are building a scoring rubric for the skill: **{skill_name}**.

Inputs:
- Skill spec: {skill_spec}
- Sample outputs (good and bad): {sample_outputs}

---

### Phase 1 — Failure Analysis

Identify 5–7 ways this skill can fail silently. A silent failure: output looks correct but misleads a consumer who trusted it.

For each:
```
F-01: <failure name> — <what went wrong> — <why "well-structured output" misses it>
```

Before moving to Phase 2: review each entry. If any failure could be caught by "the output is well-structured and complete" — it is not a silent failure. Replace it with a skill-specific one.

**STOP CONDITION:** All failures name a behavior specific to this skill; none describe a generic quality problem.

---

### Phase 2 — Criterion Construction

Write 8–12 criteria. For each:
- ID (C-01, C-02, ...)
- Text: the specific behavior this criterion tests, derived from a named failure (F-NN)
- Weight: essential / recommended / aspirational
- Category: correctness / depth / format / coverage / behavior
- Pass Condition: binary and observable

**Weight spec:**
- Essential: 3–5 criteria (if any fail, the rubric is unusable)
- Recommended: 2–3 criteria
- Aspirational: 1–2 criteria

**Banned qualifiers** — prohibited in pass conditions without a measurable anchor:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

During construction, test each criterion inline:
> Would "output is well-structured, clear, and complete" catch this same failure?
> YES → this criterion is generic. Mark it for deletion. Record the deletion in Phase 3.
> NO → criterion earns its place.

**STOP CONDITION:** At least 3 essential, 2 recommended, and 1 aspirational criterion survive the inline filter. No pass condition contains a banned qualifier without a measurable anchor.

---

### Phase 3 — Rejection Log

**This phase has an explicit output requirement.**

The Rejection Log is a named section in your output document. It is not satisfied by applying the inline filter during Phase 2 and moving on. The log must appear as a named section in the final artifact, explicitly populated with entries.

**Construction-time filter activity alone does not satisfy this requirement.** A rubric that ran the filter during Phase 2 but produces no Rejection Log section in the output fails C-13 (rejection log proves filter ran) regardless of the quality of the filtering activity.

For every criterion marked for deletion during Phase 2, record:
```
Rejected: "<criterion text>" — Reason: <one sentence naming why it fails — e.g., "would be satisfied by any well-structured output">
```

Minimum 2 entries. If you deleted fewer than 2 criteria during Phase 2, revisit your draft criteria list and identify additional generic or duplicative criteria to remove.

**STOP CONDITION:** Rejection Log section is present in your output with a minimum of 2 entries, each containing the criterion text and an explicit deletion reason.

---

### Phase 4 — Rubric Assembly

Assemble the final rubric table from the Phase 2 survivors:

| ID | Text | Weight | Category | Pass Condition |

Order: essential rows first, then recommended, then aspirational. All five fields populated for every row.

Assign sequential IDs (C-01, C-02, ...) in weight-tier order.

---

### Phase 5 — Scoring Section

Write the Scoring section:

**Composite formula:**
(essential_pass / essential_total) × 60
+ (recommended_pass / recommended_total) × 30
+ (aspirational_pass / aspirational_total) × 10

**Golden threshold:** All essential criteria pass AND composite ≥ 80

**Calibration example:** Name one essential criterion by ID. Describe a concrete output of this skill that would fail it in one sentence.

**Evolution hook:** Note that this rubric should grow as excellent outputs are discovered. Add a version field.

---

### Output

Emit in this order:
1. Rubric Table (Phase 4 — essential → recommended → aspirational)
2. Rejection Log (Phase 3 — **named section; minimum 2 entries**)
3. Scoring Section (Phase 5 — formula, threshold, calibration, evolution hook)

Note: the Failure Analysis (Phase 1) and derivation reasoning (Phase 2) are construction artifacts — they do not appear in the final artifact unless you choose to include them as a pre-table notes section.

---

## V-04 — Axes: Phrasing register + Inertia framing (combination)

**Axes:** Phrasing register (imperative STOP CONDITIONS throughout); Inertia framing (Generic Rubric named at every phase boundary)
**Primary effect:** Combining imperative register (hard STOP CONDITIONS at each phase, "STOP AND REWRITE" failure branches rather than advisory language) with persistent inertia framing (Generic Rubric named and tested at each phase boundary, not only at construction time) prevents criteria drift from skill-specific toward generic quality signals across all phases while maintaining the behavioral discontinuity that blocks "proceed and note" bypass
**Secondary effect:** Dense inertia labeling before each phase adds repetitive prompt structure; combined with imperative register, the model may fill available output tokens with inertia-check prose rather than criteria content and Scoring section structure; the Scoring section (required for C-03) competes for space with the Generic Rubric Filter application that appears before Phase 3 emits; V-05 achieves the same inertia containment via role framing rather than inline labels — token-cheaper and less likely to crowd out the Scoring section
**Falsifiability check:** C-04 (skill-specific criteria) PASS rate highest in set at V-04; STOP CONDITIONS enforce phase gates; Scoring section present/absent varies across V-04 runs (token pressure competes with the inertia-check prose for output space); V-04 vs V-01 comparison isolates whether persistent inertia labeling adds independent C-04 value beyond the failure-analyst route

---

You are building a scoring rubric for the skill: **{skill_name}**.

Inputs:
- Skill spec: {skill_spec}
- Sample outputs (good and bad): {sample_outputs}

---

**The problem this rubric must solve.** There is a default rubric that always exists and always fails: *"The output is well-structured, clear, and complete."* Call this the **Generic Rubric**. The Generic Rubric scores a hallucinated output and a correct one identically. Your rubric is only useful if it scores them differently. Every phase below tests your work against the Generic Rubric. This is not optional — it is the primary filter.

---

### Phase 1 — Failure Inventory

*Generic Rubric test: does the Generic Rubric catch these failures? It must not.*

Identify 5–7 ways this skill can fail silently. For each failure, apply the Generic Rubric test inline:

```
F-01: <failure name> — <what went wrong>
  Generic Rubric test: would "well-structured, clear, and complete" catch this? [YES / NO]
```

Any failure that receives YES is a generic failure, not a skill-specific one. **STOP AND REPLACE IT** before continuing.

**STOP CONDITION:** All failures receive NO on the Generic Rubric test. Do not proceed to Phase 2 until every entry passes.

---

### Phase 2 — Criterion Construction

*Generic Rubric test: do your criteria catch what the Generic Rubric misses?*

Write 8–12 criteria. For each, immediately apply the Generic Rubric test:

```
C-01: <criterion text>
  Generic Rubric test: would "well-structured, clear, and complete" satisfy this pass condition? [YES / NO]
  Action: [Keep / Delete — reason if Delete]
```

Delete all YES results. Keep all NO results.

For each surviving criterion, assign:
- Weight: essential / recommended / aspirational
- Category: correctness / depth / format / coverage / behavior
- Pass Condition: binary, observable, measurable

**Weight spec:**
- Essential: 3–5 criteria
- Recommended: 2–3 criteria
- Aspirational: 1–2 criteria

**Banned qualifiers** — may not appear in any pass condition without a measurable anchor:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

**STOP CONDITION:** At least 3 essential, 2 recommended, and 1 aspirational criterion survive. Every pass condition receives NO on the Generic Rubric test. No banned qualifier appears without a measurable anchor. **STOP AND REWRITE** any criterion that fails these checks before continuing.

---

### Phase 3 — Rejection Log and Design Rationale

*Generic Rubric test: does your design rationale name what the Generic Rubric cannot see?*

**Step A — Rejection Log.** For every criterion deleted in Phase 2, record:
```
Rejected: "<criterion text>" — Reason: <one sentence>
```

**Step B — Design Rationale.** Write a short design rationale block that:
- Names the dominant failure mode for this skill (the most dangerous way outputs mislead consumers)
- States the Generic Rubric's specific failure point for this skill (what the Generic Rubric rewards that it should not)
- Names at least one criterion from the Rejection Log by text and explains the rejection

Apply the Generic Rubric test one final time:
> Does this Design Rationale say something the Generic Rubric cannot? If NO — add specificity until YES.

**STOP CONDITION:** Rejection Log has ≥1 entry. Design Rationale names the dominant failure mode and explicitly names ≥1 rejected criterion. Design Rationale precedes the rubric table in the output. **STOP AND REWRITE** if either condition is unmet.

---

### Phase 4 — Rubric Assembly and Scoring

*Generic Rubric test: would any of these criteria pass an output the Generic Rubric endorses but your rubric should reject?*

Assemble the final rubric:

**Design Rationale** (from Phase 3 — this block must appear before the Rubric Table)

**Rubric Table:**
| ID | Text | Weight | Category | Pass Condition |

Order: essential → recommended → aspirational.

Apply the Generic Rubric test one final time to each pass condition:
> Would "well-structured, clear, and complete" satisfy this? YES → revise. **STOP AND REVISE** before emitting.

**Scoring Section:**

Composite formula:
(essential_pass / essential_total) × 60
+ (recommended_pass / recommended_total) × 30
+ (aspirational_pass / aspirational_total) × 10

Golden threshold: All essential criteria pass AND composite ≥ 80

Calibration example: name one essential criterion ID and describe in one sentence a poor output that fails it and that the Generic Rubric would incorrectly endorse.

Evolution hook: note that this rubric should grow as golden outputs are discovered. Add a version field.

**STOP CONDITION:** Scoring section present. Design Rationale precedes Rubric Table. No pass condition satisfies the Generic Rubric test.

---

### Output

Emit in this order:
1. Design Rationale (dominance failure mode + rejected criteria + Generic Rubric failure point)
2. Rejection Log
3. Rubric Table (essential → recommended → aspirational)
4. Scoring (formula, threshold, calibration, evolution hook)

---

## V-05 — Axes: Role sequence + Output format (combination: failure-analyst skeleton as canonical four-section path)

**Axes:** Role sequence (failure-analyst skeleton as canonical path, explicitly named in role definition); Output format (four-section output contract named upfront as the canonical structure)
**Primary effect:** Formalizing the failure-analyst skeleton (Phase 1 failure inventory → Phase 2 criterion construction + derivation notes → Phase 3 rejection log → Phase 4 rubric table + scoring section) as a canonical path named in both the role description and the output contract achieves C-20/C-21/C-22 compliance simultaneously: Scoring section is a required structural commitment (C-20), the failure inventory is explicitly named as satisfying the Design Rationale "or equivalent block" requirement (C-21), and the Rejection Log is a named output section that explicitly states construction-time filtering alone does not satisfy this gate (C-22)
**Secondary effect:** Combining role sequencing with an explicit output contract creates the most constrained body in the set; the density of structural requirements may cause the model to produce a formulaic rubric that satisfies all structural criteria (C-01/C-02/C-03/C-06/C-13/C-14) but underperforms on analytical depth criteria (C-08 failure-mode distinctness, C-11 inertia framing specificity) because the analytical phases are subordinated to compliance requirements; V-01 produces higher C-08/C-11 quality because Phase 1 is free of output contract pressure; V-03/V-04 are downstream comparators naming V-05 as the site where combined-axis depth tradeoff manifests
**Falsifiability check:** C-20/C-21/C-22 all PASS in V-05; highest structural score in the round; C-08 (distinct failure modes) quality measurably lower than V-01 — failure inventory entries are shorter and less analytically grounded; total composite score is the round ceiling; the canonical-path formalization is the v6 candidate "failure-analyst-skeleton-as-canonical-path" evaluated as an experimental body

---

You are a **RubricArchitect** for the Signal plugin. Your job: build a scoring rubric for a given skill using the failure-analyst skeleton — a four-phase canonical path that produces a structurally complete rubric every time it runs. Your professional standard: every rubric you produce contains all four required sections; none are omitted under token pressure or because the criteria are strong enough to stand alone.

**The canonical path.** The failure-analyst skeleton is:
1. **Failure Inventory** — enumerate the top silent failures for the skill (pre-criteria; this block satisfies the Design Rationale "or equivalent block" requirement — it is the dominant-failure-mode statement that precedes the criteria table)
2. **Criterion Construction** — derive criteria from failures; produce derivation notes
3. **Rejection Log** — record criteria considered and deleted, with deletion reasons; this is a named output section, not a construction-time activity; construction-time filtering without a named output section does not satisfy this gate
4. **Rubric Table + Scoring** — criteria in weight order, all five fields, followed immediately by the composite formula, golden threshold, calibration example, and evolution hook

All four sections must appear in the output. Omitting the Scoring section (Section 4) causes the composite formula, calibration, and evolution hook criteria to fail simultaneously regardless of criteria quality.

---

### Input

Provide the following before the skill runs:
- Skill name: {skill_name}
- Skill spec: {skill_spec}
- Sample outputs (good and bad): {sample_outputs}

---

### Phase 1 — Failure Inventory

*This section serves as the Design Rationale equivalent block. It appears before the criteria table and satisfies the requirement that the dominant failure mode be named before criteria are constructed.*

Identify the top 6 silent failures for this skill. A silent failure: output looks correct but misleads a consumer who trusted it.

For each:
```
F-01: <failure name> — <what went wrong> — <why "well-structured output" would miss it>
```

Requirements:
- Each failure names a behavior specific to this skill, not a generic quality problem
- At least one entry names the dominant failure mode — the most common or most dangerous way outputs of this skill mislead consumers; label it with *(dominant)*

**STOP CONDITION:** 6 failures present; at least one marked *(dominant)*; no entry describes a generic quality problem ("output is unclear") without specifying the skill-specific behavior at fault.

---

### Phase 2 — Criterion Construction

*Prevents: criteria that score a hallucinated output and a correct one identically.*

Write criteria derived from Phase 1 failures. For each criterion:
- ID (C-01, C-02, ...)
- Text: the specific behavior tested, with failure source in parentheses (e.g., "Derived from F-02")
- Weight: essential / recommended / aspirational
- Category: correctness / depth / format / coverage / behavior
- Pass Condition: binary, observable, measurable

**Weight spec:**
- Essential: 3–5 criteria
- Recommended: 2–3 criteria
- Aspirational: 1–2 criteria

**Banned qualifiers** — may not appear in any pass condition without a measurable anchor:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

For each criterion, record a one-line derivation note:
```
C-NN ← F-NN: <what the criterion tests and why F-NN would not be caught by a generic check>
```

Apply the specificity filter inline:
> Would "well-structured, clear, and complete" satisfy this pass condition? YES → the criterion is generic. Mark it for Phase 3 deletion. NO → criterion survives.

**STOP CONDITION:** Criteria within spec (3–5 essential, 2–3 recommended, 1–2 aspirational); every pass condition receives NO on the specificity filter; every banned qualifier has a measurable anchor alongside it.

---

### Phase 3 — Rejection Log

*This is Section 2 of the four-section canonical output. It must appear as a named section in the artifact.*

For every criterion marked for deletion in Phase 2, record:
```
Rejected: "<criterion text>" — Reason: <one sentence>
```

**Construction-time filter activity alone does not satisfy this section.** A rubric that applied the inline specificity filter during Phase 2 but produces no named Rejection Log section in the output fails C-13 regardless of how actively the filter ran. The deletion evidence must be placed in this section.

Minimum 1 entry. If no criteria were deleted during Phase 2, you did not run a sufficient specificity filter — revisit Phase 2 and identify at least one criterion that a generic quality check would also catch.

**STOP CONDITION:** Rejection Log section present in output with ≥1 entry containing criterion text and explicit deletion reason.

---

### Phase 4 — Rubric Table and Scoring

*This is Sections 3 and 4 of the four-section canonical output. Both must appear.*

**Rubric Table:**

| ID | Text | Weight | Category | Pass Condition |

Order: essential rows first, then recommended, then aspirational. All five fields populated for every row. Sequential IDs in weight-tier order.

**Scoring Section** *(required; omitting this section causes C-03, C-09, and C-10 to fail simultaneously):*

Composite formula:
(essential_pass / essential_total) × 60
+ (recommended_pass / recommended_total) × 30
+ (aspirational_pass / aspirational_total) × 10

Golden threshold: All essential criteria pass AND composite score ≥ 80

PARTIAL handling: a PARTIAL on an essential criterion counts as 0.5 pass for score computation but does not satisfy the all-essential-pass precondition.

Calibration example: name one essential criterion ID; describe in one sentence a concrete poor output that fails it.

Evolution hook: state that this rubric should grow as excellent outputs are discovered; include a version field in the document.

**STOP CONDITION:** Rubric Table present with all five fields per row. Scoring Section present with formula, threshold, calibration, and evolution hook. Do not emit until both are complete.

---

### Output

Emit the four canonical sections in this order:

**Section 1: Failure Inventory** (Phase 1 — this section precedes the criteria table; it is the Design Rationale equivalent block)

**Section 2: Rejection Log** (Phase 3 — named section; construction-time filtering alone does not satisfy this gate)

**Section 3: Rubric Table** (Phase 4 — essential → recommended → aspirational; all five fields)

**Section 4: Scoring** (Phase 4 — formula, threshold, calibration example, evolution hook)

---

### Global Constraints

- All four sections must be present in every rubric produced by this skill
- Section 1 (Failure Inventory) must appear before Section 3 (Rubric Table) — this is the "design rationale precedes criteria" structural requirement
- Section 2 (Rejection Log) must appear as a named section with explicit entries — not implied by construction activity
- Section 4 (Scoring) must be present — its absence predicts joint failure on formula, calibration, and evolution hook criteria simultaneously
- No criterion in the Rubric Table may use a banned qualifier without a measurable anchor alongside it
