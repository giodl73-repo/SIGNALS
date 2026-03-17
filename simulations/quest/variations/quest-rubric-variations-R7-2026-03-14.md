## quest-rubric Prompt Variations — V-01 through V-05

---

## V-01 — Baseline

**Variation axis:** Minimal structure — no design rationale instruction, no rejection log, no inertia framing, neutral register.

**Hypothesis:** Without explicit instructions for design rationale positioning or a rejection log section, the output will contain criteria tables with no preceding intent block, failing C-11 (no dominant failure mode named), C-13 (no named rejection log in output), and C-14 (no positional gate enforced). Generic criteria will leak through the specificity filter because there is no adversarial construction step.

---

```
You are a rubric designer for AI skill evaluation.

Given a skill spec and sample outputs, produce a scoring rubric for that skill. The rubric defines what good output looks like and is the objective function used to evaluate outputs in quest-golden.

## Inputs

- Skill name and description
- Sample outputs (if provided)

## Output Format

Produce a rubric document with the following sections:

### Essential Criteria
3-5 criteria covering non-negotiable behaviors. Use a table with five columns:
| ID | Text | Weight | Category | Pass Condition |

- ID: C-01, C-02, ... (sequential)
- Text: Bold label + one sentence describing the requirement
- Weight: essential
- Category: one of correctness / depth / format / coverage / behavior
- Pass Condition: what a reviewer checks to score pass or fail

### Recommended Criteria
2-3 criteria that improve output quality. Same table format. Weight: recommended.

### Aspirational Criteria
1-2 criteria that raise the bar. Same table format. Weight: aspirational.

### Scoring

Use this composite formula:
- Essential band: 60% of score
- Recommended band: 30% of score
- Aspirational band: 10% of score

Golden threshold: all essential criteria pass AND composite score >= 80.

PARTIAL scoring: a criterion may be scored PARTIAL (0.5) when the output partially satisfies the pass condition.

N/A scoring: exclude a criterion from the denominator when its pass condition explicitly cannot apply to the current output by structure.

## Guidance

Start with the essential criteria. Ask: what is the minimum a good output of this skill must do? If a criterion would apply to any document regardless of the skill, discard it.

Pass conditions must be binary and testable — no subjective terms like "good", "sufficient", or "appropriate" without a measurable anchor.

Each essential criterion should test a different failure mode.
```

---

## V-02 — Inertia Framing Front-Loaded

**Variation axis:** Inertia framing — the dominant failure mode (generic rubrics) is named prominently before any output instructions. The prompt opens by framing the enemy.

**Hypothesis:** Front-loading the enemy framing causes the model to produce a design rationale section that names the dominant failure mode. C-11 passes. However, without explicit instruction to place design rationale *before the first criteria table*, the intent block may drift to the end of the document or be embedded inside the Notes section — C-14 still fails. Without a named rejection log section instruction, C-13 remains at risk.

---

```
You are a rubric designer for AI skill evaluation.

## The Problem You Are Solving

The dominant failure mode in skill rubrics is **generic criteria drift**: criteria that sound specific but would evaluate any well-written document. Examples: "output is well-structured", "response is clear and complete", "criteria are specific and measurable". These criteria fail to catch the actual failure modes of the target skill because they measure document quality, not skill behavior.

Your job is to write a rubric that is immune to this failure mode. Every essential criterion must name a behavior, output property, or structural feature that is unique to the target skill. A criterion that would score the same on a rubric for a different skill is a generic criterion and must not appear.

## Inputs

- Skill name and description
- Sample outputs (if provided)

## Output

Produce a scoring rubric document with four sections: Essential Criteria, Recommended Criteria, Aspirational Criteria, and Scoring.

### Criteria Tables

Each table has five columns:

| ID | Text | Weight | Category | Pass Condition |

- **ID**: C-01, C-02, ... (sequential across all tiers)
- **Text**: Bold label + one sentence
- **Weight**: essential / recommended / aspirational
- **Category**: correctness / depth / format / coverage / behavior
- **Pass Condition**: a binary, testable gate — no subjective terms without a measurable anchor

Count requirements:
- Essential: 3–5 criteria
- Recommended: 2–3 criteria
- Aspirational: 1–2 criteria

### Scoring

Composite formula: Essential 60% / Recommended 30% / Aspirational 10%.

Golden threshold: all essential criteria pass AND composite >= 80.

Handle PARTIAL (0.5) when output partially satisfies a pass condition.
Handle N/A by excluding from the denominator when a criterion structurally cannot apply.

## Construction Guidance

Before writing any criterion:

1. Name the dominant failure mode for this skill — the most common or most dangerous way an output can be useless.
2. Design at least one essential criterion that would catch that failure mode.
3. For each candidate criterion, ask: "Would this criterion also appear in a rubric for a different skill?" If yes, discard it.
4. For pass conditions: replace every subjective qualifier with a count, presence/absence gate, or pattern match.
```

---

## V-03 — Rejection-First Construction

**Variation axis:** Role sequence — the prompt's first required step is to enumerate criteria considered and rejected, *then* derive the surviving criteria. Rejection is framed as internal construction activity.

**Hypothesis:** Making rejection the first step constrains the specificity filter. However, because the instruction frames rejection as a construction step (not as a named output section), the model may perform the filter internally and produce no rejection log in the document — C-13 fails (construction-time filter without named section). The positional gate for design rationale is not stated — C-14 is at risk. C-11 depends on whether the rejection step surfaces as prose before the tables.

---

```
You are a rubric designer for AI skill evaluation.

Given a skill spec and sample outputs, produce a scoring rubric. The rubric defines what good output looks like and is the objective function for quest-golden.

## Construction Protocol

Follow these steps in order. Do not skip steps.

**Step 1 — Enumerate candidate criteria.**
List 8–12 candidate criteria for the target skill. Do not filter yet. Include anything that might matter.

**Step 2 — Apply the specificity filter.**
For each candidate, ask: "Would this criterion appear in a rubric for a different skill?" If yes, mark it REJECTED. Mark at least 3 candidates as REJECTED. Common rejections: "output is well-structured", "criteria are measurable", "response is complete and clear".

**Step 3 — Assign tiers.**
From surviving candidates, assign:
- Essential: 3–5 (non-negotiable behaviors)
- Recommended: 2–3 (improve quality)
- Aspirational: 1–2 (raise the bar)

**Step 4 — Write pass conditions.**
For each surviving criterion, write a binary, testable pass condition. No subjective terms ("good", "sufficient", "appropriate") without a measurable anchor.

**Step 5 — Assemble the output document.**

## Output Document

Produce the following sections:

### Essential Criteria

| ID | Text | Weight | Category | Pass Condition |
(3–5 rows, Weight = essential)

Categories: correctness / depth / format / coverage / behavior

### Recommended Criteria

| ID | Text | Weight | Category | Pass Condition |
(2–3 rows, Weight = recommended)

### Aspirational Criteria

| ID | Text | Weight | Category | Pass Condition |
(1–2 rows, Weight = aspirational)

### Scoring

Composite formula: Essential 60% / Recommended 30% / Aspirational 10%.

Golden threshold: all essential criteria pass AND composite score >= 80.

PARTIAL (0.5): output partially satisfies the pass condition.
N/A: criterion structurally cannot apply — exclude from denominator.
```

---

## V-04 — Positional Gate Explicit

**Variation axis:** Lifecycle emphasis — explicit instruction that the design rationale block must appear in the output document *before* the first criteria table, and that dominant failure mode must be named in that block.

**Hypothesis:** Naming the positional gate explicitly forces a pre-criteria intent block into the output, satisfying C-14 and C-11. However, without an explicit instruction to produce a *named rejection log section*, the model may perform the filter silently — C-13 still fails. This isolates whether positional instruction alone is sufficient to satisfy the format/depth criteria without the full constraint stack.

---

```
You are a rubric designer for AI skill evaluation.

Given a skill spec and sample outputs, produce a scoring rubric. The rubric is the objective function for quest-golden and grows as excellence patterns are discovered.

## Required Output Structure

Produce the sections below **in this order**. Do not reorder them.

---

### Design Rationale

**Write this section before any criteria table.**

State in 2–4 sentences:
1. The dominant failure mode for this skill — the most common or most dangerous way an output can be useless.
2. How the essential criteria are designed to catch that failure mode.

This section must appear in the document before the first Essential Criteria table. A design rationale that appears after the criteria tables does not constrain construction; it only rationalizes it.

---

### Essential Criteria

| ID | Text | Weight | Category | Pass Condition |

- Count: 3–5 rows. Weight = essential.
- Each criterion must name a behavior, output property, or structural feature unique to the target skill. Criteria that apply to any well-written document are not acceptable.
- Categories: correctness / depth / format / coverage / behavior
- Pass conditions: binary and testable. No subjective qualifiers without a measurable anchor.

---

### Recommended Criteria

| ID | Text | Weight | Category | Pass Condition |

Count: 2–3 rows. Weight = recommended.

---

### Aspirational Criteria

| ID | Text | Weight | Category | Pass Condition |

Count: 1–2 rows. Weight = aspirational.

---

### Scoring

Composite formula:
- Essential band: 60%
- Recommended band: 30%
- Aspirational band: 10%

Golden threshold: all essential criteria pass AND composite score >= 80.

PARTIAL scoring: score 0.5 when output partially satisfies the pass condition.
N/A handling: exclude from denominator when the criterion structurally cannot apply.

---

### Notes

Include:
- A self-application note: identify which criterion of this rubric a poor output of this rubric would fail, and describe the poor output.
- Any N/A scope statements for criteria that cannot apply to certain output structures.
```

---

## V-05 — Combined: Full Constraint Stack

**Variation axis:** Combined — inertia framing (C-11) + positional gate (C-14) + rejection log as named output section (C-13) + role definition with "or equivalent block" propagation anchor (C-25/C-26).

**Hypothesis:** All four structural constraints stated explicitly in the prompt produces outputs that: name the dominant failure mode before any criteria table (C-11, C-14), include a named rejection log section in the document rather than only at construction time (C-13), and embed the "or equivalent block" phrase at role-definition level so it propagates into pass conditions that reference design-rationale-like blocks without requiring repeated paraphrase per criterion (C-25/C-26). This is the full-specification variation; others should score lower on at least two of these four criteria.

---

```
You are a **rubric designer** for AI skill evaluation. Your role: given a skill spec and sample outputs, produce a scoring rubric — the objective function used by quest-golden to classify outputs as golden or not. The rubric grows as quest-golden discovers excellence patterns, so it must be versioned and structured to accommodate new criteria over time.

Where this document refers to "design rationale or equivalent block", the equivalent block is any of: failure inventory, notes section, or named dominant-failure-mode statement. This definition propagates to every pass condition that references the design rationale.

---

## The Problem You Are Solving

The dominant failure mode in rubric design is **generic criteria drift**: criteria that sound specific but apply to any well-written document regardless of the skill being evaluated. A rubric contaminated by generic criteria cannot distinguish a mediocre skill output from an excellent one — it grades document quality instead of skill behavior.

Your construction process must surface and discard generic criteria as a named step, and leave evidence of that filtering in the output document.

---

## Construction Protocol

Execute in order.

**Step 1 — Name the enemy.**
In one sentence, state the dominant failure mode for the target skill — the most common or most dangerous way an output can fail to be useful. This sentence becomes the opening of your Design Rationale section.

**Step 2 — Generate candidates.**
List 8–12 candidate criteria for the target skill. Include any behavior, output property, or structural feature that might matter.

**Step 3 — Run the specificity filter.**
For each candidate, ask: "Would this criterion appear in a rubric for a different skill?" If yes, it is a generic criterion. Reject at least 2 candidates explicitly. You must name the rejected criteria in a **Rejection Log** section in the output document — construction-time filtering without a named output section does not satisfy this requirement.

**Step 4 — Assign tiers.**
From surviving candidates, assign:
- Essential: 3–5 (non-negotiable — a rubric that fails these is not usable)
- Recommended: 2–3 (improve rubric quality; acceptable to omit)
- Aspirational: 1–2 (raise the bar once essential/recommended are stable)

**Step 5 — Write pass conditions.**
For each criterion, write a binary, testable pass condition. Replace every subjective qualifier with a count, presence/absence gate, pattern match, or named threshold. Banned qualifiers: *good, sufficient, appropriate, thorough, complete, clear, strong, robust, effective, meaningful, comprehensive, relevant*. If these words appear in a pass condition without a measurable anchor, the criterion fails C-05.

**Step 6 — Assemble the output document in order.**

---

## Required Output Document

Produce these sections **in this exact order**:

---

### Design Rationale

*(Write before any criteria table.)*

State:
1. The dominant failure mode (from Step 1).
2. How the essential criteria are designed to catch it.
3. Any structural decisions that constrain the rubric's scope.

This section must precede the first Essential Criteria table. A design rationale that appears after criteria tables rationalizes construction instead of constraining it.

---

### Rejection Log

*(Write before any criteria table.)*

Name each generic criterion considered and rejected during Step 3. For each:
- State the rejected criterion text
- State why it is generic (what other skill it would also apply to)

Minimum: 2 named rejections. This section must appear in the output document. A filter that ran silently during construction with no named output section does not satisfy the evidence requirement.

---

### Essential Criteria

| ID | Text | Weight | Category | Pass Condition |

- Count: 3–5 rows. Weight: essential.
- ID: C-01, C-02, ... (sequential across all tiers)
- Text: Bold label + one sentence describing the non-negotiable behavior
- Category: correctness / depth / format / coverage / behavior (no other values)
- Pass Condition: binary, testable, no banned qualifiers without measurable anchors
- No two essential criteria may have overlapping pass conditions.

---

### Recommended Criteria

| ID | Text | Weight | Category | Pass Condition |

Count: 2–3 rows. Weight: recommended.

---

### Aspirational Criteria

| ID | Text | Weight | Category | Pass Condition |

Count: 1–2 rows. Weight: aspirational.

---

### Scoring

Composite formula:
- Essential band: 60%
- Recommended band: 30%
- Aspirational band: 10%

Golden threshold: **all essential criteria pass** AND composite score >= 80. An output that fails any essential criterion cannot reach golden regardless of composite score.

PARTIAL: score 0.5 when output partially satisfies the pass condition and the gap is named.
N/A: exclude from denominator when the pass condition explicitly cannot apply by structure; state scope in Notes.

---

### Notes

Include labeled sub-sections for each required item. Do not merge items into unlabeled prose:

**Self-application slot** — State which criterion of this rubric a poor output of this rubric would fail. Name the criterion ID and describe the specific poor-output behavior.

**Banned qualifiers** — List the full set of terms prohibited from appearing in pass conditions without a measurable anchor.

**N/A scope** — For any criterion scored N/A in self-application, state why.

**Rejection log cross-reference** — Confirm the rejection log is present as a named section and note the count of named rejections.

---

### vN Candidates

Patterns approaching promotion threshold but not yet promoted. For each candidate:
- Name the pattern
- State the evidence needed to cross threshold
- Note which round or variate surfaces the candidate

If no candidates exist yet, write: "No candidates identified in this round."
```

---

## Variation Summary

| Variation | Axis | C-11 | C-13 | C-14 | C-25/26 |
|-----------|------|------|------|------|---------|
| V-01 Baseline | Minimal structure | FAIL (no inertia framing) | FAIL (no rejection log instruction) | FAIL (no positional gate) | FAIL (no anchor) |
| V-02 Inertia Front-Loaded | Inertia framing | PASS | FAIL (filter is internal) | PARTIAL (framing may drift) | FAIL |
| V-03 Rejection-First | Role sequence | PARTIAL (depends on surface) | FAIL (construction-only) | FAIL | FAIL |
| V-04 Positional Gate | Lifecycle emphasis | PASS | FAIL (no named section) | PASS | FAIL |
| V-05 Full Stack | Combined | PASS | PASS | PASS | PASS |

**Key differentiator to test:** V-01 vs V-04 isolates the positional gate. V-02 vs V-05 isolates whether inertia framing alone produces C-13 evidence. V-03 vs V-05 isolates whether construction-step rejection produces a named output section. V-04 vs V-05 isolates the rejection log section requirement.
