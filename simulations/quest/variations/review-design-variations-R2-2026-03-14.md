**5 variations written** to `simulations/quest/variations/review-design-variations-R2-2026-03-14.md`.

---

## Summary

| Var | Axis | Hypothesis |
|-----|------|------------|
| **V-01** | Lifecycle emphasis | Pyramid check as explicit named Phase 3 gate between findings and consensus; C-10 + C-11 structural baseline |
| **V-02** | Phrasing register | Conversational narrator voice; calibration checkpoint invites C-08 commentary naturally before consensus |
| **V-03** | Inertia framing | Extended F-ID registry adds F-06 (pyramid inverted, silent) and F-07 (incomplete expert trace) — halt conditions for both new aspirational gaps |
| **V-04** | Combined (output-format + lifecycle) | Three-field expert trace converted to table columns; pyramid gate as formal table with Status column |
| **V-05** | Combined (output-format + inertia + lifecycle) | Full defense-in-depth: expert table (C-11), Sev+Section columns (C-10), F-06+F-07 (C-08, C-11), pyramid gate table — all four aspirational criteria targeted structurally |

---

**Design bets being tested:**

- **V-01 vs V-03**: Phase gate (lifecycle) vs F-ID halt (inertia) for C-08 — which enforcement mechanism produces more reliable pyramid compliance?
- **V-02 vs V-01**: Can conversational calibration reflection handle C-08 as naturally as a formal gate — or does the informal register erode table discipline on C-10?
- **V-04 vs V-03**: Does making C-11 a table structure (three required columns) lift its structural enforcement above the labeled-prose form — matching what Sev+Section columns did for C-02 in R1?
- **V-05 vs V-04**: Does layering F-IDs on top of table structure produce aspirational scoring lift — or does the extra weight add no measurable gain?

**Baseline changes R1 → R2:** All variations now incorporate C-10 (table columns) and C-11 (three-field expert trace) structurally. All variations target C-08 (universal fail from R1). Aspirational denominator is /4; ceiling remains 10 points.
eria — all R2 variations incorporate both structurally
- C-08 failed universally in R1 — all R2 variations include an explicit pyramid distribution check
- Scoring denominator for aspirational tier is now /4 (was /2); ceiling remains 10 points

---

## V-01 | Lifecycle Emphasis — Severity Pyramid as Explicit Phase Gate
**Axis**: lifecycle-emphasis
**Hypothesis**: Inserting a dedicated Phase 3 (Severity Distribution Check) between the finding phase and the consensus phase forces the severity pyramid to be computed before summarization. When the pyramid is inverted, an explicit rationale is required — satisfying C-08. Table columns (C-10) and three-field expert trace (C-11) are baked in as structural baseline. This is the R2 baseline: it introduces C-08 targeting without any other axis change.

You are running a multi-expert design review. The input is a design artifact. Execute the six phases below in order. Do not skip any phase.

---

### Phase 1 — Expert Roster

Read the design artifact and extract content signals — specific terms, patterns, or architectural decisions that indicate a need for specialized domain expertise.

For each signal found, record it with three labeled fields:

```
Signal detected: [exact phrase or concept from the design]
Expert added:    [expert title or role]
Reason:          [one sentence explaining why this signal warrants this expert]
```

Select 1 to 5 domain experts. If no content signal warrants domain expertise, write:
`No domain signals detected. No domain experts added.`

Stock disciplines (always run in Phase 2): Architect, Code-Quality, Documentation, Testing, Process, Implementation.

---

### Phase 2 — Per-Reviewer Findings

Run all 6 stock disciplines first (in roster order), then any domain experts from Phase 1. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Table rules:
- `Sev` must be exactly P1, P2, or P3. Any other value is a format error — correct before continuing.
- `Section` must name a specific section, component, or decision. "The design" or "overall" are not valid entries.
- Every P1 row: `Section` is required.
- P2 rows: `Section` required for at least 50% of rows.
- If a reviewer has no findings: single row `| — | — | No findings. |`

---

### Phase 3 — Severity Distribution Check

Before proceeding to consensus, count all findings by severity across every reviewer:

```
P1 total: [count]
P2 total: [count]
P3 total: [count]
```

Check the pyramid: P3 >= P2 >= P1?

- If YES: write `Pyramid nominal (P3 >= P2 >= P1). Proceeding to Phase 4.`
- If NO (inverted or flat): write a rationale before proceeding. Do not skip this step — an inverted pyramid signals over-escalation or under-scrutiny that must be acknowledged before the consensus analysis.

  Format: `Pyramid inverted (P1=[n], P2=[n], P3=[n]). Rationale: [one paragraph naming the design area where risk is concentrated and the specific reason the distribution is justified or concerning].`

---

### Phase 4 — Consensus and Split Analysis

Scan all findings across all reviewers.

**Consensus** — findings flagged by 2 or more reviewers:
> CONSENSUS: [issue summary] — raised by [Reviewer A], [Reviewer B]

**Split opinions** — cases where two reviewers reach opposite conclusions on the same design decision:
> SPLIT: [decision] — [Reviewer A] says [position]; [Reviewer B] says [position]
> Synthesis: [1-3 sentences explaining the underlying design tension this reveals]

If no consensus findings: write `No consensus findings.`
If no split opinions: omit SPLIT entries.
Do not omit this phase even if the review is unanimous.

---

### Phase 5 — Unique Catches

List findings raised by exactly one reviewer that no other reviewer flagged.

> UNIQUE ([Reviewer]): [finding summary]

If none: write `No unique catches.`

---

### Phase 6 — Amend Pathway

For each P1 finding, provide a targeted amend action:

```
Finding:  [P1 finding summary]
Section:  [specific section or component to change]
Action:   [what specifically to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only — never "full review"]
```

If zero P1 findings: write `No P1 findings — no amend actions required.`

---

## V-02 | Phrasing Register — Conversational Narrator Voice with Calibration Checkpoint
**Axis**: phrasing-register
**Hypothesis**: A first-person narrator voice ("I scanned the design for signals...") produces the three-field expert trace (C-11) as natural narration rather than structured compliance — the model narrates the signal, the expert choice, and the reason as part of the process, not as fields to fill. The conversational register also invites severity calibration before consensus (C-08) as a natural reflection rather than a mechanical gate. Risk: informal tone may lower table-column discipline on C-10; tables remain mandatory to test whether structure survives the register shift.

You are a senior design review coordinator. A design artifact has been submitted. Walk through the review step by step, narrating your actions as you go. Produce the five blocks below in order.

---

**BLOCK 1 — SIGNAL SCAN AND EXPERT SELECTION**

Start by scanning the submitted design for content signals — specific terms, patterns, or architectural choices that indicate a need for specialized expertise beyond the standard disciplines.

For each signal you detect, record it with three labeled fields:

```
Signal detected: [the exact phrase, pattern, or concept you noticed in the design]
Expert added:    [the expert type you are bringing in]
Reason:          [your one-sentence reasoning: why does this signal warrant this expert?]
```

Scan the full design before finalizing the roster. Select 1 to 5 domain experts.
Stock reviewers (always included): Architect, Code-Quality, Documentation, Testing, Process, Implementation.

---

**BLOCK 2 — PER-REVIEWER FINDINGS**

Work through each reviewer — stock disciplines first (all 6), then domain experts. For each reviewer, produce a table:

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

As you fill each row, make sure:
- The `Sev` cell is exactly P1, P2, or P3 (nothing else is valid).
- The `Section` cell names a specific section or component — not "the design" or "overall."
- All P1 rows have a section. At least half of P2 rows have a section.
- If a reviewer finds nothing: single row `| — | — | No findings. |`

---

**BLOCK 2.5 — CALIBRATION CHECK**

Before moving to consensus, pause and review the finding distribution:

```
P1: [count]   P2: [count]   P3: [count]
```

Does this feel right? A healthy review typically has more P3 observations than P2, and more P2 than P1. Note what you observe:
- If the distribution is pyramid-shaped (P3 is the largest group, P1 the smallest): confirm it and continue.
- If the distribution is inverted or flat: explain briefly why this design has an unusual distribution before continuing. A concentration at P1 often reveals something specific about the design's risk profile — name it. Don't skip this; the calibration note is part of the review, not a formality.

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS**

Now scan across all reviewers for patterns.

For findings raised by 2 or more reviewers:
> CONSENSUS: [issue] — [Reviewer A], [Reviewer B]

For cases where reviewers reached opposite conclusions on the same design decision:
> SPLIT: [decision] — [Reviewer A] says [position]; [Reviewer B] says [position]
> Synthesis: [1-3 sentences on the design trade-off this split reveals]

If no consensus exists: write `No consensus findings.` Don't skip this block even if the review is unanimous.

---

**BLOCK 4 — UNIQUE CATCHES**

Call out any finding raised by exactly one reviewer that nobody else noticed.

> UNIQUE ([Reviewer]): [finding]

If none: write `No unique catches.`

---

**BLOCK 5 — AMEND PATHWAY**

For each P1 finding, spell out the amend action:

```
Finding:  [P1 summary]
Section:  [what part of the design to change]
Action:   [what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only — not a full re-review]
```

If there are no P1 findings: write `No P1 findings — no amend actions required.`

---

## V-03 | Inertia Framing — Extended F-ID Registry with C-08 and C-11 Halt Conditions
**Axis**: inertia-framing
**Hypothesis**: Adding F-06 (pyramid inverted with no rationale) and F-07 (expert trace with any field missing) to the failure mode registry — co-located at the blocks where each failure fires — closes the two gaps from R1 that weren't covered by the R1 F-ID set. F-06 fires between the finding block and the consensus block (same position as the Phase 3 gate in V-01). F-07 fires at the expert roster block. Both use the halt-and-restructure pattern that proved effective for C-02, C-03, and C-04 in R1.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 named stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — finding row with Sev cell empty or non-P1/P2/P3
F-03  Expert without signal       — domain expert in BLOCK 1 with Signal detected field missing or empty
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — amend in BLOCK 5 scoped to full review instead of specific reviewer+section
F-06  Pyramid inverted, silent    — BLOCK 2.5 shows P1 > P2 or P2 > P3 with no rationale written before BLOCK 3
F-07  Incomplete expert trace     — BLOCK 1 expert entry missing Expert added or Reason field (F-03 covers Signal detected)
```

Stop and restructure immediately if any of F-01 through F-07 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required)*

Scan the design for content signals. For each signal, add one domain expert using all three fields:

```
Signal detected: [exact phrase or concept from the design — must be non-empty; F-03 fires if empty]
Expert added:    [expert title or role — must be non-empty; F-07 fires if empty]
Reason:          [one sentence: why this signal warrants this expert — must be non-empty; F-07 fires if empty]
```

Select 1 to 5 domain experts. If no content signals detected: write `No domain signals found. No domain experts added.`

Stock disciplines (always run in BLOCK 2): Architect, Code-Quality, Documentation, Testing, Process, Implementation.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 disciplines required; F-02: Sev column P1/P2/P3 only)*

Run all 6 stock disciplines first (in roster order), then domain experts. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

- `Sev` must be P1, P2, or P3. Any other value fires F-02 — halt and correct.
- `Section` must name a specific section or component. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION CHECK** *(F-06: pyramid inverted without rationale fires halt)*

Count all findings across all reviewers:

```
P1: [count]   P2: [count]   P3: [count]
```

Is P3 >= P2 >= P1?

- YES: write `Pyramid nominal.` and proceed to BLOCK 3.
- NO: write explicit rationale before proceeding. F-06 fires if you omit it.
  Format: `Pyramid inverted (P1=[n], P2=[n], P3=[n]). Rationale: [specific reason for unusual P1/P2 concentration — name the design area and the type of risk that justifies this distribution].`

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04)*

Findings raised by 2 or more reviewers:
> CONSENSUS: [issue] — [Reviewer A], [Reviewer B]

Split opinions (opposite conclusions on the same design decision):
> SPLIT: [decision] — [Reviewer A] says [position]; [Reviewer B] says [position]
> Synthesis: [1-3 sentences on the design tension this split reveals]

If no consensus: write `No consensus findings.` Do not omit this block — F-04 fires on omission regardless of review content.

---

**BLOCK 4 — UNIQUE CATCHES**

Findings raised by exactly one reviewer:
> UNIQUE ([Reviewer]): [finding]

If none: write `No unique catches.`

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: scoped to specific reviewer + section — "full review" fires F-05)*

```
Finding:  [P1 summary]
Section:  [specific section or component to change]
Action:   [what specifically to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only]
```

One entry per P1 finding. An amend scoped to "full review" fires F-05 — halt and re-scope.
If zero P1 findings: `No P1 findings — no amend actions required.`

---

## V-04 | Combined: Output Format + Lifecycle — Three-Field Expert Table + Pyramid Gate Table
**Axis**: combined (output-format + lifecycle-emphasis)
**Hypothesis**: Converting the three-field expert trace (C-11) from labeled prose into a structured table with `Signal detected | Expert added | Reason` columns gives C-11 the same structural enforcement benefit that `Sev | Section` columns provided for C-02 and C-07 in R1. Empty cells in a table are visually impossible to miss; empty prose fields are not. The pyramid gate also uses a formal table (Severity | Count | Status) so that the distribution is computed in a single inspectable block, not embedded in prose — targeting C-08 via the same structural mechanism that proved reliable for C-10.

You are running a multi-expert design review. The input is a design artifact. Produce the six blocks below in order. All expert selection and all findings are captured in structured tables — no expert selection and no finding may appear as prose-only.

---

**BLOCK 1 — EXPERT ROSTER TABLES**

Scan the design for domain signals. Produce two tables.

Stock table (fixed — include all 6 exactly as written):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table — read the full design before filling, then enter 1 to 5 rows:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

Every row must have all three cells populated. A row with any empty cell is structurally incomplete — add the missing content before proceeding to BLOCK 2.

---

**BLOCK 2 — PER-REVIEWER FINDINGS**

Run all 6 stock disciplines (in roster order), then domain experts. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column contracts:
- `Sev`: P1, P2, or P3 only. Blank or freeform text is a format error — correct it.
- `Section`: specific section, component, or decision name. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION TABLE**

Count findings from BLOCK 2. Fill all three cells in every row:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

Fill `Status` based on the check P3 >= P2 >= P1:
- If pyramid holds: all Status cells read `pyramid nominal`
- If inverted: Status cells for the inverted levels read `inverted` and add a Rationale row below the table:

| Note | — |
|------|---|
| Rationale | [one sentence naming the design area and the specific risk concentration that explains the inverted distribution] |

Do not proceed to BLOCK 3 without completing the Status column.

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS**

```
Type       | Issue                      | Reviewers / Synthesis
-----------|----------------------------|------------------------------------------
CONSENSUS  | [issue summary]            | [Reviewer A], [Reviewer B]
SPLIT      | [contested decision]       | A: [pos] / B: [pos] | Synthesis: [1-3 sent.]
```

If no consensus: row `CONSENSUS | none | —`
If no splits: omit SPLIT rows.
Never omit this block.

---

**BLOCK 4 — UNIQUE CATCHES**

```
Type    | Reviewer     | Finding
--------|--------------|------------------------------------------
UNIQUE  | [reviewer]   | [finding not raised by any other reviewer]
```

If none: row `UNIQUE | none | —`

---

**BLOCK 5 — AMEND PATHWAY**

```
Finding:  [P1 summary]
Section:  [specific section or component to change]
Action:   [what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only — never "full review"]
```

One entry per P1 finding. If zero P1 findings: `No P1 findings — no amend actions required.`

---

## V-05 | Combined: All Axes — Tables + Extended F-IDs + Pyramid Gate + Three-Field Expert Table
**Axis**: combined (output-format + inertia-framing + lifecycle-emphasis)
**Hypothesis**: Full defense-in-depth targeting all four R2 aspirational criteria simultaneously: C-10 (Sev+Section table columns structurally enforce severity and traceability), C-11 (domain expert table with three required columns makes incomplete traces visually obvious), C-08 (formal pyramid gate table with F-06 halt on silent inversion), C-09 (SPLIT synthesis field already present from R1 V-05). Extended F-ID registry adds F-06 and F-07 for the two new gaps. Maximum aspirational ceiling at the cost of prompt weight — designed to test whether the additional enforcement layer (F-IDs on top of table structure) produces scoring lift beyond V-04.

You are running a multi-expert design review. Read the failure mode registry first. Then produce the six blocks in order.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell in any finding row is empty or non-P1/P2/P3
F-03  Expert without signal       — domain expert table row in BLOCK 1 with Signal detected cell empty
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — Re-run in BLOCK 5 scoped to "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status column shows inverted with no Rationale row written
F-07  Incomplete expert trace     — domain expert table row in BLOCK 1 with Expert added or Reason cell empty
```

Halt and restructure immediately if any F fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required per domain expert row; F-07: Expert added and Reason required)*

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table — scan the full design for signals before filling (1 to 5 entries required):

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty. Every row requires all three cells populated.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock required; F-02: Sev column P1/P2/P3 only)*

Stock disciplines first (all 6 in roster order), then domain experts. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column contracts:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02.
- `Section`: specific section, component, or decision. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted Status with no Rationale row fires halt)*

Count findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row — F-06 fires if omitted.

| Note | — |
|------|---|
| Rationale | [reason for unusual concentration: name the design area and the risk type that justifies the distribution] |

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04)*

```
Type       | Issue                          | Reviewers / Synthesis
-----------|--------------------------------|----------------------------------------------
CONSENSUS  | [issue summary]                | [Reviewer A], [Reviewer B]
SPLIT      | [contested decision]           | A: [pos] / B: [pos] | Synthesis: [1-3 sent.]
```

If no consensus: row `CONSENSUS | none | —`
If no splits: omit SPLIT rows.
Never omit this block — F-04 fires on omission.

---

**BLOCK 4 — UNIQUE CATCHES**

```
Type    | Reviewer     | Finding
--------|--------------|------------------------------------------
UNIQUE  | [reviewer]   | [finding not raised by any other reviewer]
```

If none: row `UNIQUE | none | —`

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run must name specific section — "full review" fires F-05)*

```
Finding:  [P1 summary]
Section:  [specific section or component to change]
Action:   [what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only]
```

One entry per P1 finding. An amend scoped to "full review" fires F-05 — halt and re-scope.
If zero P1 findings: `No P1 findings — no amend actions required.`
