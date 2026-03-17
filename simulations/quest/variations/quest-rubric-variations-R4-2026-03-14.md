## Quest Rubric — Variation Set R4 (V-01 through V-05)

---

### V-01 — Single Axis: Role Sequence (Failure Analyst First)

**Axis**: Role sequence — Failure Analyst runs before Criterion Writer  
**Hypothesis**: Leading with failure modes before writing criteria produces criteria anchored to real breakdowns rather than generic quality signals.

```markdown
You are building a scoring rubric for the skill: **{skill_name}**.

You have been given:
- Skill spec: {skill_spec}
- Sample outputs (good and bad): {sample_outputs}

---

## Phase 1 — Failure Analyst

Before writing any criterion, identify the top 5 ways this skill can fail silently.
A silent failure is one where the output *looks correct* but would mislead a consumer
who trusted it.

For each failure, name:
- What went wrong
- Why it would not be caught by a generic quality check ("is the output well-structured?")

Format:
```
F-01: <failure name> — <what went wrong> — <why generics miss it>
F-02: ...
```

Do not proceed to Phase 2 until all five failures are named.

---

## Phase 2 — Criterion Writer

Write one criterion per failure identified in Phase 1. Each criterion must:
- Name the specific behavior it tests (not the generic quality it approximates)
- Reference the failure it was derived from in parentheses

Then add any additional criteria required by the rubric structure (see Required Fields below).

Total criteria: 7–12. The first 3–5 must be **essential**.

---

## Phase 3 — Rubric Assembler

Output the rubric as a Markdown table with these five columns, in this order:

| ID | Text | Weight | Category | Pass Condition |

**Weight values**: essential / recommended / aspirational  
**Category values**: correctness / depth / format / coverage / behavior  
**Pass Condition**: a binary gate — observable, measurable, no banned qualifiers

**Banned qualifiers** (may not appear in a Pass Condition without a measurable anchor):
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

Start with all essential criteria, then recommended, then aspirational.

---

## Output Contract

Produce three sections in order:
1. Failure inventory (Phase 1)
2. Criterion derivation notes (Phase 2, brief — one line per criterion)
3. Final rubric table (Phase 3)

No other sections.
```

---

### V-02 — Single Axis: Output Format (Prose-Anchored, Table Summary Only)

**Axis**: Output format — criteria written in prose paragraphs first; table is a summary index, not the primary artifact  
**Hypothesis**: Prose-first criterion writing produces richer pass conditions because it forces the author to reason through the gate before compressing it to a table cell.

```markdown
You are writing a scoring rubric for the skill: **{skill_name}**.

Inputs:
- Skill spec: {skill_spec}
- Sample outputs: {sample_outputs}

---

## Instructions

Write each criterion as a prose paragraph, then summarize all criteria in a table at the end.

**Criterion paragraph format:**

> **C-NN — [Criterion Name]** (Weight: essential/recommended/aspirational | Category: correctness/depth/format/coverage/behavior)
>
> [2–4 sentences describing what this criterion tests and why it matters for this specific skill.
> Include a concrete example of a passing output and a failing output, each in one sentence.]
>
> **Pass condition:** [A single binary gate. No banned qualifiers. If the condition requires
> counting, state the minimum count. If it requires presence, name the exact item to find.]

Write 3–5 essential criteria first. Then 2–4 recommended. Then 1–2 aspirational if warranted.

**Banned qualifiers** — these words may not appear in a Pass Condition without a measurable anchor alongside them:
good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate

After all prose criteria, output a summary table:

| ID | Criterion Name | Weight | Category | Pass Condition (one line) |

The table is an index. The prose paragraphs are authoritative.

---

## Inertia Check

Before finalizing, ask: would "the output is well-structured and complete" score equally well
on the last output you evaluated? If yes, your pass conditions are generic — revise them.

An inertia-failing criterion rewards a hallucinated rubric and a calibrated one equally.
Eliminate it or sharpen it.

---

## Output

Prose criteria (numbered), then summary table. No other sections.
```

---

### V-03 — Single Axis: Inertia Framing (Status-Quo Competitor Prominent Throughout)

**Axis**: Inertia framing — the status-quo competitor ("output is well-structured") is named and tested at every phase  
**Hypothesis**: Repeatedly naming the competitor throughout the prompt keeps criteria anchored to the specific skill rather than drifting toward generic document quality.

```markdown
You are writing a scoring rubric for the skill: **{skill_name}**.

Inputs:
- Skill spec: {skill_spec}
- Sample outputs: {sample_outputs}

---

## The Problem This Rubric Must Solve

There is a default rubric that always exists and always fails: "The output is well-structured,
clear, and complete." Call this the **Generic Rubric**.

The Generic Rubric scores a hallucinated rubric and a calibrated one identically.
Your rubric is only useful if it scores them differently.

Every criterion you write will be tested against the Generic Rubric Filter:

> *Would "the output is well-structured, clear, and complete" catch this failure?*
> If YES → your criterion is redundant. Delete it.
> If NO → your criterion earns its place.

---

## Phase 1 — Draft Criteria

Write 8–12 criteria. For each, immediately apply the Generic Rubric Filter inline:

```
C-01: [criterion text]
  → Generic Rubric Filter: [YES/NO] [one sentence why]
  → Keep / Delete
```

Delete all YES criteria. Replace them with sharper versions or new criteria until all are NO.

---

## Phase 2 — Classify and Order

For each surviving criterion, assign:
- **Weight**: essential / recommended / aspirational
- **Category**: correctness / depth / format / coverage / behavior

Reorder: essential first, then recommended, then aspirational.

---

## Phase 3 — Write Pass Conditions

For each criterion, write a binary pass condition.

Rules:
- Observable: a human with the output in front of them can determine PASS/FAIL in under 30 seconds
- Measurable: counts, presence/absence, enumerated values — not impressions
- No banned qualifiers without anchors: good / sufficient / appropriate / clear / complete /
  thorough / comprehensive / adequate

Apply the Generic Rubric Filter one final time to each pass condition:
> *Could "the output is well-structured" satisfy this pass condition?*
> If YES → revise.

---

## Output Format

Final rubric table only:

| ID | Text | Weight | Category | Pass Condition |

Preceded by: a one-paragraph **Inertia Statement** naming 2–3 criteria that failed the Generic
Rubric Filter during drafting and were revised, and what they became.
```

---

### V-04 — Combined: Output Format (Numbered List) + Phrasing Register (Conversational/Imperative)

**Axes**: Output format (numbered list criteria, no tables) + Phrasing register (direct imperative, second-person, no technical jargon)  
**Hypothesis**: Dropping tables and using direct imperative language reduces format overhead and produces pass conditions a non-expert can evaluate without interpreting table columns.

```markdown
Write a scoring rubric for this skill: **{skill_name}**

Here's the skill spec: {skill_spec}
Here are sample outputs: {sample_outputs}

---

Your rubric needs to answer one question: given a real output of this skill, can I tell in
under two minutes whether it's good or not?

Write 7–10 criteria. Start with the ones that can't be skipped (essential). Then add the ones
that separate adequate from excellent (recommended). Add aspirational ones only if they catch
failures the others miss.

For each criterion, write it like this:

---

**C-01 — [Name]**  
Weight: essential  
Category: correctness  

What it tests: [one sentence — name the specific behavior, not the generic quality]  

How to check it: [Tell me what to look for. Be specific. If I need to count something, give me
the threshold. If I need to find something, name it exactly. Don't say "looks good" or
"is sufficient" — tell me what to find.]

---

Keep going through all your criteria in this format.

After the last criterion, add a short section called **What This Rubric Won't Catch** — name
1–2 things that are out of scope and explain why they're excluded. This tells the reader what
problems to bring elsewhere.

---

**One rule for the "How to check it" field**: You cannot use these words without a number or
named item alongside them: good, sufficient, appropriate, clear, complete, thorough,
comprehensive, adequate.

Wrong: "The output is complete."  
Right: "The output contains all five required fields: ID, Text, Weight, Category, Pass Condition."

---

Output: criteria list, then the out-of-scope section. That's it.
```

---

### V-05 — Combined: Lifecycle Emphasis (Heavy Amend Phase) + Role Sequence (Validator Runs Alongside Writer)

**Axes**: Lifecycle emphasis (amend/revision phase is explicitly scaffolded with gate labels) + Role sequence (a Validator role runs alongside the Writer, challenging each criterion as it's written)  
**Hypothesis**: Interleaving a Validator role with criterion writing — rather than reviewing at the end — catches inertia drift per-criterion instead of in a batch review where it's more expensive to fix.

```markdown
You are running a two-role process to build a scoring rubric for: **{skill_name}**

Inputs:
- Skill spec: {skill_spec}
- Sample outputs: {sample_outputs}

The two roles are **Writer** and **Validator**. They alternate on each criterion.

---

## Step 1 — Writer: Draft Essential Criteria

Write 3–5 essential criteria. For each:
- ID (C-01, C-02, ...)
- Text (what the criterion tests, specific to this skill)
- Pass condition (binary, observable, measurable)

Do not assign Weight or Category yet.

---

## Step 2 — Validator: Challenge Each Essential Criterion

For each essential criterion from Step 1, the Validator answers:

1. **Inertia test**: Would "this output is well-structured" satisfy this pass condition? YES/NO
2. **Specificity test**: Does the criterion name a behavior specific to {skill_name}, or could
   it apply to any skill? SPECIFIC / GENERIC
3. **Qualifier test**: Does the pass condition contain any of these without a measurable anchor?
   good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate
   CLEAN / FLAGGED

Criteria that fail any test go back to the Writer for revision before proceeding.

---

## Gate 1 — Essential Criteria Approved

All essential criteria must pass all three Validator checks before proceeding.
State: "Gate 1 passed. [N] essential criteria approved."

---

## Step 3 — Writer: Draft Recommended and Aspirational Criteria

Write 3–5 recommended criteria and 1–2 aspirational criteria.
Same format as Step 1.

---

## Step 4 — Validator: Challenge Recommended and Aspirational Criteria

Apply the same three tests from Step 2.
Revise any failures before proceeding.

---

## Gate 2 — All Criteria Approved

State: "Gate 2 passed. [N] total criteria approved ([E] essential, [R] recommended, [A] aspirational)."

---

## Step 5 — Writer: Assemble Final Rubric

Add Weight and Category to all approved criteria.
Output as a Markdown table:

| ID | Text | Weight | Category | Pass Condition |

**Weight values**: essential / recommended / aspirational  
**Category values**: correctness / depth / format / coverage / behavior

---

## Gate 3 — Table Integrity Check

Validator confirms:
- Every row has all five fields (no blanks)
- Weight values are only: essential / recommended / aspirational
- Category values are only: correctness / depth / format / coverage / behavior
- No banned qualifiers appear in Pass Condition without a measurable anchor

State: "Gate 3 passed." or list the rows that need repair.

---

## Output

Validator challenges inline (brief — one line per test), then final rubric table.
Gate declarations must use the exact labels: Gate 1, Gate 2, Gate 3.
```

---

## Variation Index

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Role sequence: Failure Analyst first | Failure-anchored criteria resist inertia drift |
| V-02 | Output format: prose-primary, table as index | Prose forces gate reasoning before compression |
| V-03 | Inertia framing: competitor named throughout | Persistent competitor naming prevents generic drift |
| V-04 | Format (list) + Register (conversational/imperative) | No-table format lowers evaluation friction |
| V-05 | Lifecycle (heavy amend gates) + Role sequence (interleaved Validator) | Per-criterion validation cheaper than batch review |
