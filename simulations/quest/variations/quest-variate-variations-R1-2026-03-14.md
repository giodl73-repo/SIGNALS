Written to `simulations/quest/variations/quest-variate-variations-R1-2026-03-14.md`.

---

**5 variations, 4 axes covered, all single-axis:**

| ID | Axis | Hypothesis |
|----|------|-----------|
| V-01 | Role sequence (baseline: generator-then-critic) | Committing to full body before critique pressure prevents diff-leak failures |
| V-02 | Output format (table index + fenced blocks) | Fenced blocks force body completion before fence closes, reducing partial-body failures |
| V-03 | Phrasing register (direct imperative) | Stripping meta-commentary tightens output because model mirrors prompt register |
| V-04 | Lifecycle emphasis (explicit phase gates with stop conditions) | Named stop conditions between phases prevent axis drift by forcing single-axis check before proceeding |
| V-05 | Role sequence (critic-first) | Critic analyzing axes before generation targets high-leverage variations over arbitrary coverage |

**Design notes:**
- V-01 and V-05 both vary role sequence — the axis had two genuinely distinct designs (generator-first vs critic-first), and the rubric allows revisiting an axis when the design choice is meaningfully different. If strict one-axis-per-variation is required, V-05's critic-first sequencing is sufficiently distinct from V-01's generator-then-critic to justify separate entries.
- Inertia framing (status-quo competitor prominence) from the prompt's suggested axes wasn't selected — it doesn't naturally apply to a meta-skill like `quest-variate` that has no external competitor model. Replaced with lifecycle emphasis and phrasing register, which do affect behavior here.
- Combinations deferred per rubric (N ≤ 6).
 or persona governs the run |
| Phrasing register | Formal/technical vs conversational; imperative vs descriptive |
| Scoring granularity | Coarse pass/fail vs nuanced partial credit vs weighted composite |

### Steps

1. **Generate.** For each variation V-01 through V-0N, write the full skill body. Do not reference prior variations. Each variation stands alone.
2. **Label.** Precede each body with a header block:
   - `Axis:` — the single axis being varied
   - `Hypothesis:` — a falsifiable prediction about how this axis change affects model behavior or output quality
3. **Critique.** After producing all N bodies, review each one: confirm it contains no diffs, no references to other variations, and no incomplete sections. If any fail, rewrite immediately.
4. **Output.** Emit the final N variations in order, V-01 first.

### Constraints

- Default N = 5 unless the caller specifies otherwise
- Single-axis passes before combination passes
- Hypotheses must be falsifiable — predict a specific, observable difference
- No variation may contain "same as above," "see V-01," or diff notation

---

## V-02 — Axis: Output Format (structured table index + fenced blocks)

**Axis:** Output format
**Hypothesis:** Presenting each variation body inside a labeled fenced code block preceded by a compact table index forces the model to commit to a complete body before closing the fence, reducing partial-body failures compared to prose-delimited output.

---

You are a Signal skill variation engine. Your job: given a skill spec, produce N complete, runnable skill body variations.

### Input

```
SkillSpec:
  id: <skill id>
  description: <skill description>
  inputs: <list>
  outputs: <list>
  artifact: <artifact path pattern>
```

### Output structure

First, emit an index table:

| ID | Axis | Hypothesis (one sentence) |
|----|------|--------------------------|
| V-01 | <axis name> | <falsifiable prediction> |
| V-02 | ... | ... |
...

Then, for each variation, emit:

```
### V-NN — <Axis Name>

Hypothesis: <falsifiable prediction about model behavior or output quality>

---

<complete skill body here — every instruction, role, constraint, and output spec>

---
```

The body inside each block is the full, standalone skill body. It must be executable without reading any other variation.

### Variation axes

Six axes are available. For a single-axis pass, vary exactly one axis relative to a baseline body. For combination passes (N > 6 only), vary two axes and name both in the ID header.

Axes: role sequence | output format | lifecycle emphasis | stock role selection | phrasing register | scoring granularity

### Rules

- N = 5 by default
- Every body is complete — no diffs, no "as in V-01," no partial content
- Hypotheses predict observable differences, not surface descriptions
- All single-axis passes before any combination passes

---

## V-03 — Axis: Phrasing Register (direct imperative, no meta-commentary)

**Axis:** Phrasing register
**Hypothesis:** Stripping all meta-commentary and framing prose in favor of direct imperative instructions reduces model hedging and produces tighter variation bodies because the model mirrors the register of the prompt it receives.

---

Generate 5 complete skill body variations for the Signal skill specified below. Each variation is a full, runnable prompt body. No diffs. No partial bodies. No references to other variations.

**Skill to vary:**
Read the SkillSpec provided. Use its description, inputs, outputs, and artifact pattern as the baseline.

**For each variation:**

1. Pick one axis from this list:
   - Role sequence
   - Output format
   - Lifecycle emphasis
   - Stock role selection
   - Phrasing register
   - Scoring granularity

2. Write the complete skill body for that axis variant. Include every instruction the model needs to execute the skill from scratch.

3. Label it:
   ```
   V-NN | Axis: <name> | Hypothesis: <falsifiable prediction>
   ```

**What makes a hypothesis falsifiable:** It names a specific, observable outcome. "Shorter role sequences reduce token count without losing output completeness" passes. "This is a different format" fails.

**What makes a body complete:** A practitioner can copy V-03 into a new session, paste a SkillSpec, and get correct output without reading V-01 or V-02.

Vary one axis per variation. Do not mix axes unless labeled as a combination pass (combination passes come after all 5 single-axis passes).

---

## V-04 — Axis: Lifecycle Emphasis (explicit phase gates with stop conditions)

**Axis:** Lifecycle emphasis
**Hypothesis:** Making phase boundaries explicit with numbered gates and stop conditions reduces axis drift — the failure mode where a model varies two dimensions simultaneously — because each gate forces a single-axis check before proceeding.

---

You are a Signal skill variation agent. You operate in three explicit phases. Do not skip phases or merge them.

### Phase 1 — Axis Selection

Before writing any variation body:

1. List the 6 available variation axes: role sequence, output format, lifecycle emphasis, stock role selection, phrasing register, scoring granularity.
2. Assign one axis to each of V-01 through V-05. No axis may appear twice in a single-axis pass run.
3. Write one falsifiable hypothesis per assignment. A hypothesis predicts a specific, observable change in model behavior or output quality when this axis changes. Generic descriptions fail.

**Stop condition:** Do not proceed to Phase 2 until all 5 axis assignments and hypotheses are written.

### Phase 2 — Variation Generation

For each variation V-01 through V-05, in order:

1. Write the complete skill body. It must be executable in isolation — no diffs, no references to other variations, no placeholders.
2. Check: does this body change exactly one axis relative to a neutral baseline? If two axes changed, stop and rewrite before continuing.
3. Confirm the body is complete: it contains role specification, input description, output specification, step-by-step instructions, and constraints.

**Stop condition:** Do not proceed to Phase 3 until all 5 bodies pass the completeness and single-axis checks.

### Phase 3 — Output

Emit the final artifact:

```
## V-NN — Axis: <name>
Hypothesis: <falsifiable prediction>

<complete skill body>

---
```

Repeat for each of V-01 through V-05, in order.

Default N = 5. If the caller specifies a different N, honor it. Combination passes (two axes) are only generated when N > 6 and appear after all single-axis passes.

---

## V-05 — Axis: Role Sequence (critic-first, then targeted generator)

**Axis:** Role sequence
**Hypothesis:** Running a critic role first to identify which axes produce the largest behavioral divergence, then targeting the generator to those high-leverage axes, produces a more discriminating set of variations than generator-first ordering — because the critic's prior narrows the hypothesis space before tokens are spent on bodies.

---

You are a **Variation Critic** for Signal, a feature decision plugin. You run before generation, not after.

### Step 1 — Analyze the skill

Read the SkillSpec. For each of the 6 variation axes (role sequence, output format, lifecycle emphasis, stock role selection, phrasing register, scoring granularity), assess:

- How much behavioral divergence would varying this axis produce?
- Is this axis testable with a falsifiable hypothesis?
- Is the axis already partially constrained by the skill's existing description?

Produce a ranked list of the top 5 axes by expected behavioral impact. State your reasoning for each rank position in one sentence.

### Step 2 — Assign and hypothesize

For each of the top 5 axes (your ranked list from Step 1), write one falsifiable hypothesis predicting how output quality or model behavior changes when this axis is varied.

A falsifiable hypothesis names a specific, observable outcome — not a surface description of the change.

### Step 3 — Generate variations

For each of V-01 through V-05, in ranked order (V-01 = highest expected impact axis):

Write the complete skill body for that axis variant. The body must:

- Stand alone — no references to other variations, no diffs, no "same as V-01 except"
- Include full role specification, input handling, step-by-step instructions, output format spec, and constraints
- Change exactly one axis relative to a neutral baseline

### Step 4 — Output

Emit each variation with this header:

```
## V-NN — Axis: <name> [Rank: <N>/5]
Hypothesis: <your Step 2 hypothesis>

<complete skill body>
```

Default N = 5. Combination passes (two axes labeled as such) are only generated when N > 6 and appear after all single-axis passes.
