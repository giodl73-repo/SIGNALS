Written to `simulations/quest/variations/quest-rubric-variations-R6-2026-03-14.md`.

---

## R6 Variations — Summary

**The single target:** C-15 is the only criterion that failed across all R5 variations. The fix is structural: move the self-application statement (criterion ID + poor output) into the Design Rationale section, co-located with the rejected generic criterion — not into Scoring where it has consistently drifted.

### Planning Table

| V-ID | Axis | C-15 Mechanism | Other Targets |
|------|------|----------------|---------------|
| **V-01** | DR-phase self-application gate | Three required items in Phase 1 DR; Item 3 is the self-application; explicit anti-drift note ("not in Scoring") | C-23, C-24 |
| **V-02** | Interrogative question route | Q2 = rejected criterion; Q3 = criterion ID + poor output; both answers in the same DR block by proximity | C-08 depth |
| **V-03** | Combined DR section (merged sub-blocks) | Phase 1 = three sub-blocks: (A) failures, (B) pre-rejected candidates, (C) self-application; B+C co-present in Section 1 | C-21 |
| **V-04** | Output format + DR-phase gate (combination) | Front-loaded contract names self-application as DR required element; Phase 1 reinforces; anti-drift in both | C-23, C-24 |
| **V-05** | Role sequence + DR-phase gate (combination) | RubricArchitect canonical path; Phase 1 gains Sub-section 1B (pre-rejection) + 1C (self-application); "or equivalent block" in role definition | C-21 PASS, C-25 PASS |

### Key Design Decisions

**V-01 vs V-04:** Single mandate vs doubled obligation (phase instruction alone vs contract + phase instruction). Tests whether stating the anti-drift rule twice increases reliability.

**V-02 (interrogative):** Questions force named answers. Q3 must name a specific criterion ID; a general answer scores PARTIAL. Higher analytical depth ceiling but higher PARTIAL risk than V-01/V-04.

**V-03 (combined section):** All three DR sub-blocks in one section by structure. Achieves co-presence without relying on phase-to-phase adherence. Trade-off: denser Phase 1 may reduce per-sub-block depth.

**V-05 (canonical + self-application):** The projection is 100 — C-15 PASS (sub-sections 1B+1C co-present in Section 1), C-21 PASS ("or equivalent block" in role definition), C-25 PASS (phrase explicitly in role definition). All other criteria already passed in R5/V-05.
n contract header forces self-application into DR before any phase runs | C-23, C-24 (front-loaded contract) |
| V-05 | Role sequence + DR-phase self-application gate | RubricArchitect canonical path; Phase 1 (Failure Inventory = DR equivalent block) gains a Self-Application Gate sub-section; pre-rejection note also embedded in Phase 1; "or equivalent block" in role definition | Self-application gate in Phase 1/Section 1, co-present with pre-rejection note | C-21 PASS, C-25 PASS (phrase in role definition) |

**Key hypotheses:**
- V-01 vs V-04: does a phase-level self-application mandate achieve C-15 as reliably as a front-loaded contract obligation?
- V-02: does the interrogative format produce co-presence by proximity (Q2 answer adjacent to Q3 answer), or does the calibration still drift to Scoring?
- V-03 vs V-05: does collapsing all three DR sub-blocks into Section 1 achieve C-15 more reliably than a canonical path that keeps the Rejection Log in Section 2?
- V-05: does adding the self-application gate to Phase 1 of the canonical path achieve simultaneous C-15/C-21/C-25 PASS?

**Falsifiability predictions:**
- V-01: C-15 PASS (Phase 1 DR explicit instruction with anti-drift note); C-24 PASS (front-loaded contract); C-21 PARTIAL (no "or equivalent block" in role definition); C-13 PASS; C-22 PASS
- V-02: C-15 PASS (Q3 answer co-located with Q2 in DR block); C-21 PARTIAL; C-24 PARTIAL (no front-loaded sections block); C-13 PASS; C-22 PASS; risk: Q3 answer may still drift to Scoring if the model treats Q3 as a Scoring calibration question
- V-03: C-15 PASS (sub-blocks B+C co-present in Section 1); C-21 PASS if "or equivalent block" phrase used explicitly; C-24 PARTIAL (no explicit front-loaded Required Sections block before phases); C-13 PASS; C-22 PASS
- V-04: C-15 PASS (front-loaded contract names self-application as DR required element; Phase 1 instruction enforces co-location); C-24 PASS; C-13 PASS; C-22 PASS; C-21 PARTIAL
- V-05: C-15 PASS (self-application gate in Phase 1/Section 1 co-present with pre-rejection note); C-21 PASS ("or equivalent block" in role definition); C-25 PASS; C-24 PASS (canonical sections declared in role preamble); projected score: 100

---

## V-01 — Axis: DR-phase self-application gate

**Axis:** DR-phase self-application gate (single-axis)
**Hypothesis:** Explicitly requiring the self-application statement as a third required item in the Design Rationale phase, with an explicit anti-drift note ("this statement belongs here, not in the Scoring section"), prevents the calibration from drifting to Scoring. Both C-15 slots (Item 2 = rejected criterion, Item 3 = self-application) are co-located in the DR section by phase instruction. Build on R5/V-02's front-loaded contract structure.
**Secondary effect:** The Required Output Sections preamble now explicitly names the self-application as a DR required element, creating a pre-committed obligation before Phase 1 runs. The Scoring section no longer includes a calibration example — the anti-drift constraint moves it to DR, which may cause the Scoring phase to produce a formula-only section with lower C-09 depth.
**Falsifiability check:** C-15 PASS (Phase 1 DR has three explicit required items; Items 2 and 3 co-present in the same Design Rationale section); C-24 PASS (front-loaded Required Output Sections block before any phase instruction); C-13 PASS (named Rejection Log section; construction-time filter named insufficient); C-22 PASS (explicit disqualification in Phase 4); C-21 PARTIAL (no "or equivalent block" language in role definition); C-03 PASS (Scoring section present with formula and threshold); C-09 potential PARTIAL (calibration moved to DR, Scoring section may have weaker calibration depth)

---

You are building a scoring rubric for the skill: **{skill_name}**.

Inputs:
- Skill spec: {skill_spec}
- Sample outputs (good and bad): {sample_outputs}

---

### Required Output Sections

Your output must contain these five named sections in this order. Each section is a structural obligation — it must be present and populated regardless of how you construct the rubric internally.

1. **Design Rationale** — appears before the Rubric Table; contains three required items: (a) dominant failure mode statement, (b) at least one named rejected generic criterion with rejection reason, (c) self-application statement naming one essential criterion ID and a concrete poor output that fails it. The self-application statement belongs in this section, not in Scoring.
2. **Failure Inventory** — 5–7 distinct silent failures; each entry explains why a generic quality check ("output is well-structured and complete") would miss it
3. **Rejection Log** — criteria considered and deleted, with deletion reason per entry; minimum 1 entry; **construction-time filtering alone does not satisfy this requirement** — the log must appear as a named section in your output document
4. **Rubric Table** — criteria in weight order: essential (3–5), recommended (2–3), aspirational (1–2); all five fields (ID, Text, Weight, Category, Pass Condition) populated for every row
5. **Scoring** — composite formula (essential 60% + recommended 30% + aspirational 10%), golden threshold (all essential pass AND composite ≥ 80), N/A handling, and evolution hook (version field or note that the rubric grows as golden outputs are discovered)

Missing any section is a structural gap. Omitting the Scoring section causes the formula, threshold, and evolution hook criteria to fail simultaneously regardless of criteria quality.

---

### Phase 1 — Design Rationale

Write the Design Rationale section. This section must appear before the Rubric Table. It contains three required items — all three must appear in this same section:

**Item 1 — Dominant failure mode.** State the most common or most dangerous way outputs of this skill mislead consumers. Explain specifically why a "Generic Rubric" ("output is well-structured, clear, and complete") would fail to catch this failure.

**Item 2 — Rejected generic criterion.** Before writing any criteria, identify at least one criterion that a careless rubric author would include for this skill but that the Generic Rubric would also satisfy. Name it explicitly by its full text. State the rejection reason in one sentence.

Format:
```
Rejected: "[criterion text]" — Reason: [one sentence naming why it fails the specificity test]
```

**Item 3 — Self-application statement.** Name one essential criterion you anticipate writing for this rubric. State its likely ID (C-01, C-02, etc.). Describe in one sentence a concrete poor output of {skill_name} that would fail this criterion. This statement must appear here, in the Design Rationale — not moved to the Scoring section.

Format:
```
Self-application: [C-NN] — A poor output of this skill would [describe the specific failure in one sentence].
```

**STOP CONDITION:** All three items present in this section before continuing. Do not place the self-application statement (Item 3) in the Scoring section — it belongs here, co-located with the rejected criterion (Item 2).

---

### Phase 2 — Failure Inventory

List 5–7 ways this skill can fail silently. A silent failure: output looks correct but misleads a consumer who trusted it.

Format:
```
F-01: <failure name> — <what went wrong> — <why "well-structured output" misses it>
```

Inline filter: if any failure could be caught by "the output is well-structured and complete" — it is not a silent failure. Replace it with a skill-specific one.

**STOP CONDITION:** All entries name a behavior specific to this skill; none describe a generic quality problem.

---

### Phase 3 — Criterion Construction

Write criteria derived from Phase 2 failures. For each criterion:
- ID (C-01, C-02, ...)
- Text: the specific behavior tested, with failure source in parentheses (e.g., "Derived from F-02")
- Weight: essential / recommended / aspirational
- Category: correctness / depth / format / coverage / behavior
- Pass Condition: binary, observable, measurable

**Weight spec:**
- Essential: 3–5 criteria (if any fail, the rubric is unusable)
- Recommended: 2–3 criteria
- Aspirational: 1–2 criteria

**Banned qualifiers** — may not appear in any pass condition without a measurable anchor alongside them:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

Write in weight order: essential first, then recommended, then aspirational.

Apply the specificity filter inline:
> Would "well-structured, clear, and complete" satisfy this pass condition? YES → the criterion is generic. Mark it for deletion in Phase 4.

**STOP CONDITION:** Criteria count within spec for all three weight tiers; no pass condition contains a banned qualifier without a measurable anchor.

---

### Phase 4 — Rejection Log

For every criterion marked for deletion in Phase 3, record:

```
Rejected: "[criterion text]" — Reason: [one sentence]
```

**Construction-time filter activity alone does not satisfy this requirement.** A rubric that ran the specificity filter during Phase 3 but produces no named Rejection Log section in the output fails C-13 regardless of how thoroughly the filter ran. The deletion evidence must appear as a named section in the output document.

Minimum 1 entry. If no criteria were deleted, you did not apply a sufficient specificity filter — revisit Phase 3.

---

### Phase 5 — Scoring

Write the Scoring section:

**Composite formula:**
(essential_pass / essential_total) × 60
+ (recommended_pass / recommended_total) × 30
+ (aspirational_pass / aspirational_total) × 10

**Golden threshold:** All essential criteria pass AND composite score ≥ 80

**PARTIAL handling:** A PARTIAL on an essential criterion counts as 0.5 pass for score computation but does not satisfy the all-essential-pass precondition.

**N/A handling:** Criteria structurally inapplicable to a specific rubric (e.g., revision-phase criteria for skills with no revision step) are excluded from both numerator and denominator of their band.

**Evolution hook:** State that this rubric should grow as excellent outputs are discovered. Include a version field.

Note: the calibration example (criterion ID + concrete poor output) is in the Design Rationale section. Do not duplicate it here unless you can meaningfully extend it.

---

### Constraints

- Emit all five sections in order: Design Rationale → Failure Inventory → Rejection Log → Rubric Table → Scoring
- Design Rationale contains all three items (dominant failure mode, rejected criterion, self-application statement) — none distributed to other sections
- The self-application statement (criterion ID + poor output) appears in Design Rationale, not Scoring
- Rejection Log is a named output section — not satisfied by filtering during construction without an output slot
- No criterion may use a banned qualifier without a measurable anchor alongside it

---

## V-02 — Axis: Interrogative question route

**Axis:** Phrasing register (interrogative questions replace imperative mandates in the DR phase)
**Hypothesis:** Replacing Phase 1 DR mandates with three directed questions that must be answered co-locates the C-15 slots by proximity: Q2 asks for the rejected generic criterion; Q3 asks which criterion would a poor output fail (requiring a criterion ID + poor output description as the answer). Because Q2 and Q3 are adjacent questions in the same DR block, their answers naturally co-locate in the same section. The interrogative format may also produce more analytically grounded responses than imperative mandates because questions require specific named answers.
**Secondary effect:** The interrogative format may reduce structural predictability — a model answering Q3 in a general way (without naming a specific criterion ID) scores PARTIAL. If Q3 is answered with "C-01 would catch this; a poor output would X," C-15 PASS. If Q3 is answered with "any criterion testing completeness," FAIL. The falsifiability check predicts this risk.
**Falsifiability check:** C-15 PASS if Q3 answer names a criterion ID + poor output in the DR block, adjacent to Q2's rejected criterion; PARTIAL if Q3 names an ID but omits the poor output description; C-13 PASS (named Rejection Log); C-22 PASS (explicit disqualification); C-03 PASS (Scoring section); C-21 PARTIAL (no "or equivalent block" in role); C-24 PARTIAL (no front-loaded contract — DR phase has questions but no pre-declared section manifest); C-08 projected PASS (question format produces more specific failure analysis)

---

You are building a scoring rubric for the skill: **{skill_name}**.

Inputs:
- Skill spec: {skill_spec}
- Sample outputs (good and bad): {sample_outputs}

---

### Phase 1 — Design Rationale

Answer these three questions. Your answers form the Design Rationale section — the analytical foundation that must appear before your criteria table. All three answers must appear in this section.

**Q1: What is the most dangerous failure mode for this skill?**
Name the most common or most dangerous way an output of {skill_name} misleads a consumer who trusts it. Then explain in one sentence why "output is well-structured, clear, and complete" fails to catch this failure.

Your answer:

---

**Q2: What generic criterion would a careless author include for this skill?**
Name one criterion, by its full text, that a careless rubric author would include for {skill_name} but that the Generic Rubric ("output is well-structured, clear, and complete") would also satisfy. Name it explicitly. State in one sentence why it fails the specificity test.

Format:
```
Rejected: "[criterion text]" — Reason: [one sentence]
```

Your answer:

---

**Q3: Which essential criterion would correctly catch the failure you named in Q1?**
Name the criterion by its likely ID (e.g., C-01). Describe in one sentence a concrete poor output of {skill_name} that would fail this criterion — an output that the Generic Rubric would incorrectly endorse but your criterion would correctly reject.

Format:
```
Self-application: [C-NN] — A poor output that fails this criterion would [describe the specific failure].
```

Your answer must name a specific criterion ID and a specific output behavior. A general statement ("any criterion testing X") does not satisfy this question.

---

**STOP CONDITION:** All three questions answered in this section. The answers to Q2 and Q3 must both appear here, in the Design Rationale, before the criteria table. Do not place the Q3 self-application answer in the Scoring section.

---

### Phase 2 — Failure Inventory

List 5–7 ways this skill can fail silently. A silent failure: output looks correct but misleads a consumer who trusted it.

Format:
```
F-01: <failure name> — <what went wrong> — <why "well-structured output" misses it>
```

Review each entry: if a failure could be caught by "the output is well-structured and complete" — replace it with a skill-specific one.

**STOP CONDITION:** All entries name a behavior specific to this skill; none describe a generic quality problem.

---

### Phase 3 — Criterion Construction

Write criteria derived from Phase 2 failures. For each:
- ID (C-01, C-02, ...)
- Text: the specific behavior tested, with failure source in parentheses
- Weight: essential / recommended / aspirational
- Category: correctness / depth / format / coverage / behavior
- Pass Condition: binary, observable, measurable

**Weight spec:**
- Essential: 3–5 criteria
- Recommended: 2–3 criteria
- Aspirational: 1–2 criteria

**Banned qualifiers** — may not appear in pass conditions without a measurable anchor:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

Apply the specificity filter:
> Would "well-structured, clear, and complete" satisfy this pass condition? YES → mark for deletion.

**STOP CONDITION:** Criteria within spec; no pass condition uses a banned qualifier without a measurable anchor.

---

### Phase 4 — Rejection Log

For every criterion deleted in Phase 3, record:

```
Rejected: "[criterion text]" — Reason: [one sentence]
```

**Construction-time filter activity alone does not satisfy this requirement.** Running the filter during Phase 3 without producing a named Rejection Log section in the output fails C-13 regardless of how thoroughly the filter ran. The deletion evidence must appear here.

Minimum 1 entry. If no criteria were deleted, revisit Phase 3.

---

### Phase 5 — Rubric Table

Assemble the final rubric table from Phase 3 survivors:

| ID | Text | Weight | Category | Pass Condition |

Order: essential rows first, then recommended, then aspirational. All five fields populated for every row.

---

### Phase 6 — Scoring

Write the Scoring section:

**Composite formula:**
(essential_pass / essential_total) × 60
+ (recommended_pass / recommended_total) × 30
+ (aspirational_pass / aspirational_total) × 10

**Golden threshold:** All essential criteria pass AND composite score ≥ 80

**PARTIAL handling:** A PARTIAL on an essential criterion counts as 0.5 pass for score computation but does not satisfy the all-essential-pass precondition.

**N/A handling:** Structurally inapplicable criteria are excluded from both numerator and denominator of their band.

**Evolution hook:** State that this rubric should grow as excellent outputs are discovered. Include a version field.

---

### Output

Emit in this order:
1. Design Rationale (Phase 1 — three Q&A answers; all three in this section)
2. Failure Inventory (Phase 2)
3. Rejection Log (Phase 4 — named section; minimum 1 entry)
4. Rubric Table (Phase 5 — essential → recommended → aspirational)
5. Scoring (Phase 6 — formula, threshold, N/A handling, evolution hook)

---

## V-03 — Axis: Combined DR section (merged sub-blocks)

**Axis:** Lifecycle emphasis (Phase 1 becomes a three-sub-block Design Rationale containing all C-15-required co-presence slots)
**Hypothesis:** Collapsing the failure inventory, pre-rejection note, and self-application statement into a single Phase 1 "Design Rationale" section with three explicit sub-blocks (A: failure inventory, B: pre-rejected candidates, C: self-application gate) achieves C-15 co-presence structurally — sub-blocks B and C are in the same section by construction. The Rejection Log in Phase 3 is the formal record duplicating sub-block B entries, but C-15 co-presence is satisfied in Section 1 regardless of Phase 3's position. This also achieves C-21 if the "or equivalent block" phrase is embedded in the phase instruction.
**Secondary effect:** Combining three analytical tasks into Phase 1 may dilute failure analysis depth — the model must simultaneously enumerate failures, identify rejected criteria, and perform self-application, all in one phase. V-01 separates these into distinct phases (DR → Failure Inventory) allowing deeper analysis per phase. Comparison tests depth tradeoff.
**Falsifiability check:** C-15 PASS (sub-blocks B and C co-present in Section 1); C-21 PASS if phase instruction uses "or equivalent block" language for the Failure Inventory; C-24 PARTIAL (no formal Required Sections block before Phase 1; section obligations are embedded in phase instructions rather than front-loaded); C-13 PASS (Phase 3 Rejection Log is a named section with explicit construction-time disqualification); C-22 PASS; C-03 PASS

---

You are building a scoring rubric for the skill: **{skill_name}**.

Inputs:
- Skill spec: {skill_spec}
- Sample outputs (good and bad): {sample_outputs}

---

### Phase 1 — Design Rationale

*This section serves as the Design Rationale equivalent block. It precedes the criteria table and satisfies the requirement that the dominant failure mode be named before criteria are constructed.*

Write this section in three sub-blocks. All three sub-blocks must appear in this section.

**Sub-block A — Failure Inventory.** List 5–7 ways this skill can fail silently. A silent failure: output looks correct but misleads a consumer who trusted it. Mark the most dangerous failure with *(dominant)*.

Format:
```
F-01: <failure name> — <what went wrong> — <why "well-structured output" misses it>    [dominant if applicable]
F-02: ...
```

Review: if any entry could be caught by "the output is well-structured and complete" — replace it.

---

**Sub-block B — Pre-Rejected Candidates.** Before writing any criteria, identify at least one criterion that a careless rubric author would include for {skill_name} but that the Generic Rubric ("output is well-structured, clear, and complete") would also satisfy. This is the early specificity filter — reject generics before construction begins.

Format:
```
Pre-rejected: "[criterion text]" — Reason: [one sentence naming why it fails the specificity test]
```

Minimum 1 entry. This entry will be formally recorded in the Rejection Log (Phase 3); its presence here satisfies the co-presence requirement for design-rationale calibration.

---

**Sub-block C — Self-Application Gate.** Name one essential criterion you anticipate writing for this rubric. State its likely ID. Describe in one sentence a concrete poor output of {skill_name} that would fail this criterion.

Format:
```
Self-application: [C-NN] — A poor output of this skill would [describe the specific failure].
```

This statement appears here, in the Design Rationale, because it derives from failure analysis — not from scoring calibration. Do not place this statement in the Scoring section.

---

**STOP CONDITION:** All three sub-blocks present in this section. Sub-block A has ≥5 failures, at least one marked *(dominant)*. Sub-block B has ≥1 pre-rejected entry with rejection reason. Sub-block C names a criterion ID and a concrete poor output. Do not begin Phase 2 until complete.

---

### Phase 2 — Criterion Construction

Write criteria derived from Phase 1 Sub-block A failures. For each:
- ID (C-01, C-02, ...)
- Text: the specific behavior tested, derived from a named failure (F-NN)
- Weight: essential / recommended / aspirational
- Category: correctness / depth / format / coverage / behavior
- Pass Condition: binary, observable, measurable

**Weight spec:**
- Essential: 3–5 criteria
- Recommended: 2–3 criteria
- Aspirational: 1–2 criteria

**Banned qualifiers** — may not appear in pass conditions without a measurable anchor:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

Apply the specificity filter:
> Would "well-structured, clear, and complete" satisfy this pass condition? YES → mark for deletion in Phase 3.

**STOP CONDITION:** Criteria within spec; no banned qualifier without a measurable anchor.

---

### Phase 3 — Rejection Log

*This is the formal record of criteria deleted during construction. It is a named output section — the deletion evidence must appear here.*

For every criterion marked for deletion in Phase 2 (and the pre-rejected candidate from Phase 1 Sub-block B), record:

```
Rejected: "[criterion text]" — Reason: [one sentence]
```

**Construction-time filter activity alone does not satisfy this requirement.** Running the filter during Phase 2 without producing this named section in the output fails C-13 regardless of how thoroughly the filter ran.

Minimum 1 entry (at minimum, the Phase 1 Sub-block B pre-rejected candidate).

---

### Phase 4 — Rubric Table

Assemble the final rubric:

| ID | Text | Weight | Category | Pass Condition |

Order: essential rows first, then recommended, then aspirational. All five fields populated for every row.

---

### Phase 5 — Scoring

Write the Scoring section:

**Composite formula:**
(essential_pass / essential_total) × 60
+ (recommended_pass / recommended_total) × 30
+ (aspirational_pass / aspirational_total) × 10

**Golden threshold:** All essential criteria pass AND composite score ≥ 80

**PARTIAL handling:** A PARTIAL on an essential criterion counts as 0.5 pass for score computation but does not satisfy the all-essential-pass precondition.

**N/A handling:** Structurally inapplicable criteria are excluded from both numerator and denominator of their band.

**Calibration note:** The self-application example is in Design Rationale Sub-block C. Do not duplicate it here unless you extend it with composite score reasoning.

**Evolution hook:** State that this rubric should grow as excellent outputs are discovered. Include a version field.

---

### Output

Emit in this order:
1. Design Rationale (Phase 1 — all three sub-blocks: Failure Inventory, Pre-Rejected Candidates, Self-Application Gate)
2. Rejection Log (Phase 3 — named section; includes Phase 1 pre-rejected entry)
3. Rubric Table (Phase 4 — essential → recommended → aspirational)
4. Scoring (Phase 5 — formula, threshold, N/A handling, evolution hook)

---

## V-04 — Axes: Output format + DR-phase self-application gate (combination)

**Axes:** Output format (front-loaded Required Sections contract from R5/V-02) + DR-phase self-application gate (from V-01)
**Hypothesis:** The front-loaded Required Sections block creates structural obligations before any phase instruction runs. Adding the self-application statement as a named required element of the Design Rationale section in the contract header creates a pre-committed obligation that persists through all phases. The Phase 1 DR instruction reinforces with three explicit required items. An anti-drift note appears in both the contract and the phase instruction. This is the most structurally locked mechanism for C-15: the obligation is stated twice (once in the contract, once in the phase instruction) and the Scoring section explicitly notes that calibration belongs in DR.
**Secondary effect:** Doubled structural instruction may cause the model to produce a compliant but mechanical DR section — all three items present but written formulaically. The depth tradeoff (V-01 without doubled instruction vs V-04 with doubled instruction) tests whether over-specifying reduces analytical quality.
**Falsifiability check:** C-15 PASS (front-loaded contract names self-application as DR required element; Phase 1 reinforces; anti-drift note present); C-24 PASS (Required Sections block appears before any phase instruction); C-13 PASS; C-22 PASS; C-20 PASS (Scoring named in contract); C-21 PARTIAL (no "or equivalent block" phrase); C-25 N/A (no role definition); projected score: all essential + all recommended + all aspirational except C-21 PARTIAL → 99.58

---

You are building a scoring rubric for the skill: **{skill_name}**.

Inputs:
- Skill spec: {skill_spec}
- Sample outputs (good and bad): {sample_outputs}

---

### Required Output Sections

Your output must contain these five named sections in this order. Each section is a pre-committed structural obligation — present and populated in the final document regardless of internal construction order.

1. **Design Rationale** — appears before the Rubric Table; contains three required items:
   - (a) Dominant failure mode: the most common or dangerous way outputs of this skill mislead consumers
   - (b) Rejected generic criterion: at least one criterion named by text that was rejected because the Generic Rubric would also satisfy it, with rejection reason
   - (c) Self-application statement: one essential criterion ID + a concrete poor output that fails it — **this item belongs in the Design Rationale, not in the Scoring section**
2. **Failure Inventory** — 5–7 distinct silent failures; each entry explains why a generic quality check misses it
3. **Rejection Log** — criteria considered and deleted, with deletion reason; minimum 1 entry; **construction-time filtering alone does not satisfy this requirement** — the log must appear as a named section in the output document
4. **Rubric Table** — criteria in weight order: essential (3–5), recommended (2–3), aspirational (1–2); all five fields populated
5. **Scoring** — composite formula, golden threshold, PARTIAL/N/A handling, evolution hook; calibration example is in Design Rationale, not here

Missing any section is a structural gap. Omitting the Scoring section causes the formula, threshold, and evolution hook criteria to fail simultaneously. Omitting the self-application from the Design Rationale section — or placing it in the Scoring section — causes C-15 to fail regardless of calibration quality.

---

### Phase 1 — Design Rationale

Write the Design Rationale section. This section must appear before the Rubric Table. It contains three required items — all three in this same section:

**Item 1 — Dominant failure mode.** State the most common or most dangerous way outputs of {skill_name} mislead consumers. Explain specifically why "output is well-structured, clear, and complete" would fail to catch this.

**Item 2 — Rejected generic criterion.** Before constructing any criteria, identify at least one criterion a careless author would include for this skill that the Generic Rubric would also satisfy. Name it by full text. State the rejection reason.

Format:
```
Rejected: "[criterion text]" — Reason: [one sentence]
```

**Item 3 — Self-application statement.** Name one essential criterion you anticipate including in this rubric. State its likely ID (C-01, C-02, etc.). Describe in one sentence a concrete poor output of {skill_name} that fails this criterion.

Format:
```
Self-application: [C-NN] — A poor output of this skill would [specific failure in one sentence].
```

**STOP CONDITION:** All three items present before continuing. Item 3 must appear in this section — the contract header (Required Output Sections) specifies this. Do not place Item 3 in the Scoring section.

---

### Phase 2 — Failure Inventory

List 5–7 ways this skill can fail silently. A silent failure: output looks correct but misleads a consumer who trusted it.

Format:
```
F-01: <failure name> — <what went wrong> — <why "well-structured output" misses it>
```

Review: if any entry could be caught by "the output is well-structured and complete" — replace it.

**STOP CONDITION:** All failures name a skill-specific behavior; none describe a generic quality problem.

---

### Phase 3 — Criterion Construction

Write criteria derived from Phase 2 failures. For each:
- ID (C-01, C-02, ...)
- Text: specific behavior tested, with failure source in parentheses
- Weight: essential / recommended / aspirational
- Category: correctness / depth / format / coverage / behavior
- Pass Condition: binary, observable, measurable

**Weight spec:**
- Essential: 3–5 criteria
- Recommended: 2–3 criteria
- Aspirational: 1–2 criteria

**Banned qualifiers** — may not appear in pass conditions without a measurable anchor:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

Apply the specificity filter:
> Would "well-structured, clear, and complete" satisfy this pass condition? YES → mark for deletion.

**STOP CONDITION:** Criteria within spec; no banned qualifier without a measurable anchor.

---

### Phase 4 — Rejection Log

For every criterion deleted in Phase 3, record:

```
Rejected: "[criterion text]" — Reason: [one sentence]
```

**Construction-time filter activity alone does not satisfy this requirement.** A rubric that ran the filter during Phase 3 but produces no named Rejection Log section in the output fails C-13 regardless of filter quality.

Minimum 1 entry. If no criteria were deleted, revisit Phase 3.

---

### Phase 5 — Rubric Table

| ID | Text | Weight | Category | Pass Condition |

Order: essential → recommended → aspirational. All five fields populated for every row.

---

### Phase 6 — Scoring

Write the Scoring section:

**Composite formula:**
(essential_pass / essential_total) × 60
+ (recommended_pass / recommended_total) × 30
+ (aspirational_pass / aspirational_total) × 10

**Golden threshold:** All essential criteria pass AND composite score ≥ 80

**PARTIAL handling:** A PARTIAL on an essential criterion counts as 0.5 pass for score computation but does not satisfy the all-essential-pass precondition.

**N/A handling:** Structurally inapplicable criteria are excluded from both numerator and denominator of their band.

**Evolution hook:** State that this rubric should grow as excellent outputs are discovered. Include a version field.

Reminder: the calibration example (criterion ID + poor output) is in the Design Rationale section, per the Required Output Sections contract.

---

### Constraints

- Emit all five sections in order: Design Rationale → Failure Inventory → Rejection Log → Rubric Table → Scoring
- Design Rationale must contain all three items — none distributed to other sections
- Self-application statement (criterion ID + poor output) appears in Design Rationale, not Scoring — this is stated in both the Required Output Sections contract and Phase 1
- Rejection Log is a named output section — not satisfied by construction-time filtering without an output slot
- No criterion may use a banned qualifier without a measurable anchor

---

## V-05 — Axes: Role sequence + DR-phase self-application gate (combination)

**Axes:** Role sequence (RubricArchitect canonical path, "or equivalent block" phrase in role definition) + DR-phase self-application gate (self-application gate added as Phase 1 sub-section)
**Hypothesis:** Extending R5/V-05's canonical path by adding a Self-Application Gate as a third required sub-section of Phase 1 (the Failure Inventory = DR equivalent block) co-locates the self-application with a pre-rejection note also embedded in Phase 1. Both C-15 slots (pre-rejection sub-section = Item 2; self-application sub-section = Item 1) are in Section 1, the same section. The role description names all three Phase 1 sub-sections as components of "the failure inventory as DR equivalent block," so "or equivalent block" language applies to the full Phase 1 structure. C-15/C-21/C-25 all target simultaneously.
**Secondary effect:** Phase 1 now has three sub-sections (failures, pre-rejection, self-application); the increased density may reduce per-sub-section analytical depth compared to V-03's standalone DR phase. Phase 1 self-application sub-section requires anticipating a criterion ID before any criteria exist — the model must project forward. Projection may produce a placeholder ID (C-01) or a well-calibrated prediction depending on how well the failure analysis informed Phase 1.
**Falsifiability check:** C-15 PASS (self-application gate in Phase 1/Section 1 adjacent to pre-rejection note); C-21 PASS ("or equivalent block" phrase in role definition explicitly naming the failure inventory as DR equivalent); C-25 PASS (phrase appears in role definition); C-24 PASS (canonical sections declared in role preamble); C-13 PASS; C-22 PASS (explicit disqualification in Phase 3); C-03 PASS; projected score: all essential PASS + all recommended PASS + all aspirational PASS = 100

---

You are a **RubricArchitect** for the Signal plugin. Your job: build a scoring rubric for a given skill using the failure-analyst skeleton — a four-phase canonical path that produces a structurally complete rubric every time it runs.

**The canonical path:**
1. **Failure Inventory** (with Pre-Rejection and Self-Application sub-sections) — this section serves as the Design Rationale equivalent block ("or equivalent block"); it appears before the criteria table and satisfies the requirement that the dominant failure mode, rejected generic criteria, and self-application calibration be established before criteria are constructed
2. **Criterion Construction** — derive criteria from failures; record derivation notes
3. **Rejection Log** — the formal record of deleted criteria; a named output section; construction-time filtering without a named output section does not satisfy this gate
4. **Rubric Table + Scoring** — criteria in weight order (all five fields) followed by composite formula, golden threshold, PARTIAL/N/A handling, and evolution hook

All four sections must appear in the output. Omitting Section 4 (Rubric Table + Scoring) causes the composite formula, calibration, and evolution hook criteria to fail simultaneously regardless of criteria quality. The failure inventory (with its pre-rejection and self-application sub-sections) is explicitly named as satisfying the Design Rationale "or equivalent block" requirement.

---

### Input

- Skill name: {skill_name}
- Skill spec: {skill_spec}
- Sample outputs (good and bad): {sample_outputs}

---

### Phase 1 — Failure Inventory

*This section is Section 1 of the four-section canonical output. It is the Design Rationale equivalent block — it precedes the criteria table and establishes the analytical foundation for the rubric. Its three sub-sections together satisfy the design rationale requirement.*

Write this section in three sub-sections.

**Sub-section 1A — Silent Failures.** Identify the top 6 ways this skill can fail silently. A silent failure: output looks correct but misleads a consumer who trusted it. Mark the most dangerous failure with *(dominant)*.

Format:
```
F-01: <failure name> — <what went wrong> — <why "well-structured output" misses it>   [dominant?]
```

Requirements: each entry names a behavior specific to this skill; none describe a generic quality problem ("output is unclear"); at least one is marked *(dominant)*.

---

**Sub-section 1B — Pre-Rejection Note.** Before writing any criteria, identify at least one criterion a careless rubric author would include for {skill_name} that the Generic Rubric ("output is well-structured, clear, and complete") would also satisfy. This is the early specificity filter.

Format:
```
Pre-rejected: "[criterion text]" — Reason: [one sentence naming why it fails the specificity test]
```

Minimum 1 entry. This entry will be formally recorded in the Rejection Log (Section 2) — placing it here establishes its presence in the DR equivalent block.

---

**Sub-section 1C — Self-Application Gate.** Name one essential criterion you anticipate writing for this rubric. State its likely ID. Describe in one sentence a concrete poor output of {skill_name} that fails this criterion. This is the self-application component of the DR equivalent block.

Format:
```
Self-application: [C-NN] — A poor output of this skill would [describe the specific failure].
```

This statement must appear here, in Section 1, co-located with Sub-section 1B's pre-rejected criterion. Both items together satisfy the co-presence requirement. Do not place this statement in the Scoring section.

---

**STOP CONDITION:** Sub-section 1A has 6 entries, at least one marked *(dominant)*. Sub-section 1B has ≥1 pre-rejected entry with rejection reason. Sub-section 1C names a criterion ID and a concrete poor output. All three sub-sections present before continuing.

---

### Phase 2 — Criterion Construction

*Prevents: criteria that score a hallucinated output and a correct one identically.*

Write criteria derived from Phase 1 Sub-section 1A failures. For each:
- ID (C-01, C-02, ...)
- Text: the specific behavior tested, with failure source in parentheses (e.g., "Derived from F-03")
- Weight: essential / recommended / aspirational
- Category: correctness / depth / format / coverage / behavior
- Pass Condition: binary, observable, measurable

**Weight spec:**
- Essential: 3–5 criteria
- Recommended: 2–3 criteria
- Aspirational: 1–2 criteria

**Banned qualifiers** — may not appear in pass conditions without a measurable anchor:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

Record a one-line derivation note per criterion:
```
C-NN ← F-NN: <what the criterion tests and why the Generic Rubric would miss it>
```

Apply the specificity filter:
> Would "well-structured, clear, and complete" satisfy this pass condition? YES → criterion is generic. Mark for Phase 3 deletion.

**STOP CONDITION:** Criteria within spec (3–5 essential, 2–3 recommended, 1–2 aspirational); every pass condition receives NO on the specificity filter; every banned qualifier has a measurable anchor.

---

### Phase 3 — Rejection Log

*This is Section 2 of the four-section canonical output. It must appear as a named section in the artifact.*

For every criterion marked for deletion in Phase 2 (and the Phase 1 Sub-section 1B pre-rejected entry), record:
```
Rejected: "[criterion text]" — Reason: [one sentence]
```

**Construction-time filter activity alone does not satisfy this section.** A rubric that applied the specificity filter during Phase 2 but produces no named Rejection Log section in the output fails C-13 regardless of how actively the filter ran. The deletion evidence must be placed in this section.

Minimum 1 entry (at minimum, the Sub-section 1B pre-rejected candidate).

**STOP CONDITION:** Rejection Log section present with ≥1 entry containing criterion text and explicit deletion reason.

---

### Phase 4 — Rubric Table and Scoring

*This is Sections 3 and 4 of the four-section canonical output. Both must appear.*

**Rubric Table:**

| ID | Text | Weight | Category | Pass Condition |

Order: essential rows first, then recommended, then aspirational. All five fields populated for every row. Sequential IDs in weight-tier order.

**Scoring Section** *(required; omitting this section causes the composite formula, threshold, and evolution hook criteria to fail simultaneously):*

**Composite formula:**
(essential_pass / essential_total) × 60
+ (recommended_pass / recommended_total) × 30
+ (aspirational_pass / aspirational_total) × 10

**Golden threshold:** All essential criteria pass AND composite score ≥ 80

**PARTIAL handling:** A PARTIAL on an essential criterion counts as 0.5 pass for score computation but does not satisfy the all-essential-pass precondition.

**N/A handling:** Structurally inapplicable criteria are excluded from both numerator and denominator of their band.

**Evolution hook:** State that this rubric should grow as excellent outputs are discovered. Include a version field.

Note: the calibration example (criterion ID + poor output) is in Phase 1 Sub-section 1C. Do not move it here.

**STOP CONDITION:** Rubric Table present with all five fields per row. Scoring Section present with formula, threshold, PARTIAL handling, N/A handling, and evolution hook. Do not emit until both are complete.

---

### Output

Emit the four canonical sections in this order:

**Section 1: Failure Inventory** (Phase 1 — all three sub-sections: 1A Silent Failures, 1B Pre-Rejection Note, 1C Self-Application Gate; this section is the Design Rationale equivalent block; it precedes the criteria table)

**Section 2: Rejection Log** (Phase 3 — named section; includes Phase 1 Sub-section 1B entry; construction-time filtering alone does not satisfy this gate)

**Section 3: Rubric Table** (Phase 4 — essential → recommended → aspirational; all five fields)

**Section 4: Scoring** (Phase 4 — formula, threshold, PARTIAL handling, N/A handling, evolution hook)

---

### Global Constraints

- All four sections must be present in every rubric produced by this skill
- Section 1 (Failure Inventory with sub-sections) must appear before Section 3 (Rubric Table) — this is the "design rationale precedes criteria" structural requirement
- Section 1 Sub-section 1B (pre-rejection note) and Sub-section 1C (self-application gate) must both appear in Section 1 — their co-presence in the same section satisfies the C-15 gate
- Section 2 (Rejection Log) must appear as a named section with explicit entries — not implied by construction activity
- Section 4 (Scoring) must be present — its absence predicts joint failure on formula, calibration, and evolution hook criteria simultaneously
- No criterion in the Rubric Table may use a banned qualifier without a measurable anchor alongside it
