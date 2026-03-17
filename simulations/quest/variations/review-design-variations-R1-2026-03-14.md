**5 variations written** to `simulations/quest/variations/review-design-variations-R1-2026-03-14.md`.

---

## Summary

| Var | Axis | Hypothesis |
|-----|------|------------|
| **V-01** | Baseline | Linear prose covering all 9 criteria; floor score ~80, aspirational criteria left to chance |
| **V-02** | Output format | Table columns make C-02 (severity) and C-07 (section traceability) structurally impossible to fail |
| **V-03** | Role sequence | Domain experts run first — anchors P1 flags before disciplines review, increases consensus density |
| **V-04** | Inertia framing | F-01..F-05 registry co-located at each enforcement block; fires at the moment each failure mode is most likely |
| **V-05** | Combined (format + inertia + lifecycle) | Table structure + F-IDs + explicit phase gates; highest expected score, highest prompt weight |

**Key design bets to test:**

- **V-02 vs V-01**: Does the table column for `Sev` actually prevent severity omissions, or does the model still skip C-02 on short finding lists?
- **V-03 vs V-01**: Does domain-expert-first ordering produce denser consensus (disciplines validate expert flags) or sparser (disciplines assume expert covered it)?
- **V-04 vs V-01**: Does F-ID co-location at each block outperform a preamble-only registry? The `review-code` golden suggests it does — but that was for a different output structure.
- **V-05 vs V-02+V-04**: Does the three-axis combination improve aspirational scores (C-08 severity pyramid, C-09 split synthesis) or just add weight without gain?
|P3] §[section or component]: [one-sentence finding]
```

Rules:
- Every finding must carry exactly one of: P1, P2, or P3.
- Every P1 finding must name the specific design section, component, or decision it applies to.
- At least 50% of P2 findings must name a specific section.
- If a reviewer has no findings, write: `No findings.`

---

### Step 3 — Consensus Analysis

Scan all findings. Identify any finding flagged by 2 or more reviewers (same issue, possibly different wording).

For each consensus finding:
> CONSENSUS: [issue] — raised by [Reviewer A], [Reviewer B]

For any split opinion (two reviewers reach opposite conclusions on the same design decision):
> SPLIT: [decision] — [Reviewer A] says [position]; [Reviewer B] says [position].
> Synthesis: [1-3 sentences explaining the underlying design tension this reveals]

If no consensus findings exist, write: `No consensus findings.`

---

### Step 4 — Unique Catches

List findings raised by exactly one reviewer that no other reviewer flagged.

> UNIQUE ([Reviewer]): [finding summary]

If no unique catches exist, write: `No unique catches.`

---

### Step 5 — Amend Pathway

For each P1 finding, provide a targeted amend action:

> Finding: [P1 finding summary]
> Change: [what specifically to revise in the design]
> Re-run: [reviewer name(s)] on [section or component only]

Do not instruct a full re-review. Each amend targets the reviewer(s) whose concern applies to the changed section only.

---

## V-02 | Output Format — Table-Driven Findings with Column-Enforced Severity
**Axis**: output-format
**Hypothesis**: Moving findings into tables with a mandatory Sev column makes C-02 (severity on every finding) and C-07 (section traceability) structurally impossible to fail — the table is visually incomplete without both columns populated.

You are running a multi-expert design review. The input is a design artifact. Produce the five output blocks below in order.

---

**BLOCK 1 — EXPERT ROSTER**

```
Mode:    [FULL REVIEW | AMEND RUN]
Input:   [design artifact name or path]
Stock:   Architect | Code-Quality | Documentation | Testing | Process | Implementation
Added:
  Name: [expert]   Signal: [exact text or concept from design that triggered selection]
```

Add 1-5 domain experts. Each `Signal:` field must quote or paraphrase the specific design signal. An entry with an empty or generic Signal fails.

---

**BLOCK 2 — PER-REVIEWER FINDINGS**

One table per reviewer. Run stock disciplines first, then domain experts.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§name or component] | [one actionable sentence] |

Rules enforced by table structure:
- `Sev` column must be P1, P2, or P3 — blank or freeform text is structurally wrong.
- `Section` column must name a specific design section or component — "the design" is not a valid entry.
- P1 rows: Section column always required.
- P2 rows: Section column required for at least half of rows.
- If no findings: append row `| — | — | No findings. |`

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS**

```
CONSENSUS  | [issue summary]  | Flagged by: [Reviewer A], [Reviewer B]
SPLIT      | [decision]       | A: [position] / B: [position]
           |                  | Synthesis: [1-3 sentences on the design tension]
```

If no consensus findings: write `CONSENSUS | none | —`
If no split opinions: omit SPLIT rows.

---

**BLOCK 4 — UNIQUE CATCHES**

```
UNIQUE | [Reviewer] | [finding summary]
```

If none: write `UNIQUE | none | —`

---

**BLOCK 5 — AMEND PATHWAY**

```
Finding:  [P1 finding summary]
Change:   [specific section or decision to revise]
Re-run:   [reviewer(s)] on [scope — section or component only, not full review]
```

One entry per P1 finding. Do not prescribe a full re-review.

---

## V-03 | Role Sequence — Domain Experts Lead, Disciplines Follow
**Axis**: role-sequence
**Hypothesis**: Running domain experts first surfaces the non-obvious risks before stock disciplines anchor on familiar patterns. This changes the consensus landscape — discipline reviewers encountering an expert's P1 flag are more likely to validate it, improving consensus density. C-03 also becomes easier to satisfy because expert signals appear prominently before the discipline block.

You are running a multi-expert design review. The input is a design artifact. You will run domain experts first, then stock disciplines, then consolidate.

---

### Phase 1 — Signal Scan and Expert Selection

Read the design artifact. Extract content signals — specific terms, patterns, or architectural decisions — that indicate domain expertise beyond standard software disciplines.

For each signal found, select one domain expert:

> Signal detected: [exact phrase or concept]
> Expert added: [expert title]
> Reason: [one sentence on why this signal warrants this expert]

Select 1-5 experts. Proceed only after the expert roster is complete.

Stock disciplines (run after experts): Architect, Code Quality, Documentation, Testing, Process, Implementation.

---

### Phase 2 — Domain Expert Review (runs first)

For each domain expert selected in Phase 1:

```
Expert: [name]
Signal that selected them: [from Phase 1]

Findings:
- [P1|P2|P3] §[section]: [finding]
```

Every finding requires a P1/P2/P3 tag. Every P1 finding requires a section reference.

---

### Phase 3 — Stock Discipline Review (runs after experts)

Each of the 6 stock disciplines reviews the design. Disciplines may reference expert findings when they validate or contradict them.

```
Reviewer: [discipline name]

Findings:
- [P1|P2|P3] §[section]: [finding]
```

A discipline reviewer who agrees with an expert's P1 finding should note it: `(aligns with [Expert] finding on §[section])`.

---

### Phase 4 — Consensus and Split Analysis

With domain-expert findings already anchored, scan for:

**Consensus**: findings flagged by 2+ reviewers (experts and disciplines combined).
> CONSENSUS: [issue] — [Reviewer A], [Reviewer B] (and [N] others if applicable)

**Split opinions**: cases where an expert and a discipline reviewer reach opposite conclusions.
> SPLIT: [decision] — [Expert] says [X]; [Discipline] says [Y]
> Synthesis: [1-3 sentences on the design trade-off this split reveals]

If no consensus: `No consensus findings.`

---

### Phase 5 — Unique Catches

Flag findings raised by exactly one reviewer (expert or discipline) that no other reviewer mentioned.

> UNIQUE ([Reviewer]): [finding]

If none: `No unique catches.`

---

### Phase 6 — Amend Pathway

For each P1 finding, specify:

> Finding: [P1 summary]
> Change: [what to revise]
> Re-run: [reviewer(s) whose concern this touches] on [section or component — not full review]

---

## V-04 | Inertia Framing — Failure Mode Registry at Every Enforcement Point
**Axis**: inertia-framing
**Hypothesis**: Naming common failure modes at the moment they are most likely to fire (co-located at each output block, not only in a preamble) prevents the most frequent rubric misses: missing severity tags (C-02), experts without signals (C-03), absent consensus block (C-04).

**Failure Mode Registry**

```
F-01  Missing discipline — fewer than 6 named discipline blocks in output
F-02  Unsourced severity — finding present with no P1/P2/P3 tag
F-03  Expert without signal — domain expert named with no input-signal mapping
F-04  Missing consensus block — review ends after per-reviewer sections
F-05  Full-review amend — amend pathway says "re-run everything"
```

Stop immediately and restructure if any of F-01 through F-05 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: every expert must have a Signal entry)*

```
Stock:  Architect | Code-Quality | Documentation | Testing | Process | Implementation
Added:
  Name: [expert]   Signal: [exact design signal that triggered this selection]
```

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 disciplines required; F-02: P1/P2/P3 on every line)*

Stock disciplines first (all 6), then domain experts.

```
Reviewer: [name]

- [P1|P2|P3] §[section]: [finding]
```

Every finding line must start with [P1|P2|P3]. Every P1 must name a section. At least 50% of P2s must name a section. If no findings: `No findings.`

---

**BLOCK 3 — CONSENSUS ANALYSIS** *(F-04: this block is always required)*

Findings flagged by 2+ reviewers:
> CONSENSUS: [issue] — [Reviewer A], [Reviewer B]

Split opinions (opposite conclusions on same decision):
> SPLIT: [decision] — [A] vs [B]
> Synthesis: [1-3 sentences on the underlying design tension]

If no consensus: write `No consensus findings.` (Do not omit this block — F-04 fires on omission.)

---

**BLOCK 4 — UNIQUE CATCHES**

Findings raised by exactly one reviewer:
> UNIQUE ([Reviewer]): [finding]

If none: `No unique catches.`

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: target specific reviewer on specific section — not full re-review)*

For each P1 finding:
```
Finding:  [P1 summary]
Change:   [specific revision]
Re-run:   [reviewer(s)] on [section or component only]
```

---

## V-05 | Combined — Format Encoding + Inertia Framing + Explicit Lifecycle Phases
**Axis**: combined (output-format + inertia-framing + lifecycle-emphasis)
**Hypothesis**: Three-axis combination closes the remaining rubric gaps: table columns enforce C-02 and C-07 structurally, F-IDs prevent C-03 and C-04 omissions, and explicit phase gates prevent skipping the amend pathway (C-06). Expected to be the highest-scoring variation at the cost of prompt weight.

**Failure Mode Registry**

```
F-01  6 stock disciplines not all present in BLOCK 2
F-02  Finding with no Sev column entry (blank or non-P1/P2/P3)
F-03  Domain expert in BLOCK 1 with empty Signal field
F-04  BLOCK 3 omitted entirely
F-05  Amend in BLOCK 5 scoped to full review instead of affected reviewer
```

Halt and restructure if any F fires.

---

**BLOCK 1 — SETUP** *(F-03)*

```
Mode:    [FULL REVIEW | AMEND RUN]
Input:   [design artifact name]
Stock:   Architect | Code-Quality | Documentation | Testing | Process | Implementation
Added:
  Name: [expert]   Signal: [exact phrase or concept from the design]
```

Read the design. Extract content signals before filling the Added rows. 1-5 experts maximum.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01, F-02)*

Run all 6 stock disciplines, then domain experts. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§name or component] | [one actionable sentence] |

Structural contract:
- `Sev` must be P1, P2, or P3 — any other value is a format error.
- `Section` must name a specific section, component, or decision — not "the design" or "overall."
- P1 rows: Section always required (F-02 extension: P1 with no Section is a traceability failure).
- P2 rows: Section required for >= 50% of rows.
- No findings row: `| — | — | No findings. |`

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required)*

```
Type       | Issue                          | Reviewers / Synthesis
-----------|--------------------------------|----------------------------------------------
CONSENSUS  | [issue summary]                | [Reviewer A], [Reviewer B]
SPLIT      | [contested decision]           | A: [pos] / B: [pos] | Synthesis: [1-3 sent.]
```

If no consensus findings: add row `CONSENSUS | none | —`
If no splits: omit SPLIT rows.
Never omit this entire block — F-04 fires on omission regardless of review content.

---

**BLOCK 4 — UNIQUE CATCHES**

```
Type    | Reviewer    | Finding
--------|-------------|------------------------------------------
UNIQUE  | [reviewer]  | [finding not raised by any other reviewer]
```

If none: single row `UNIQUE | none | —`

---

**BLOCK 5 — AMEND PATHWAY** *(F-05)*

```
Finding:  [P1 finding summary]
Section:  [exact section or component to change]
Action:   [specific revision — what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope — never "full review"]
```

One entry per P1 finding. If zero P1 findings exist, write: `No P1 findings — no amend actions required.`
