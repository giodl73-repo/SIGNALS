**5 variations written** to `simulations/quest/variations/review-design-variations-R4-2026-03-14.md`.

---

## Summary

| Var | Axis | C-15 Bet | Hypothesis |
|-----|------|----------|------------|
| **V-01** | lifecycle-emphasis | **FAIL** (prose list) | Isolates C-15 form-sensitivity — prose pre-commitment vs. required table form |
| **V-02** | output-format | PASS (table, no F-09) | Rubric-boundary bet — is F-09 required for C-14 when BLOCK 1.5 exists? |
| **V-03** | phrasing-register | PASS (table + F-09) | Imperative-first register; tests whether command phrasing adds qualitative enforcement |
| **V-04** | combined (format + lifecycle) | PASS (Source column + F-09) | Source column makes BLOCK 1 -> BLOCK 1.5 linkage explicit at commitment stage |
| **V-05** | combined (lifecycle + inertia + format) | PASS (Source + count gate + F-09 + F-10) | Orphan detection — F-10 catches a reviewer present in BLOCK 1.5 but mismatched from BLOCK 1 |

---

## Design Bets

**V-01 vs V-03** (delta should be 1.25 pts): Prose list vs. table in BLOCK 1.5 — confirms whether C-15 requires table form specifically. If V-01 scores 98.75 and V-03 scores 100, C-15 is form-sensitive.

**V-02 vs V-03** (delta should be 0 or 1.25 pts): Table + no F-09 vs. table + F-09. If C-14's structural-block enumeration is exhaustive, both score 100. If BLOCK 1.5 is implicitly a structural block for C-14, V-02 scores 98.75. This resolves the most ambiguous rubric edge in v4.

**V-03 vs V-04** (both should score 100): Tests whether the Source column is rubric-detectable or purely qualitative enforcement depth.

**V-04 vs V-05** (both should score 100): Tests whether the cross-block count gate + orphan detection (F-10) produces any measurable lift.
cks — BLOCK 1.5 is not in this list. If the enumeration is exhaustive, both score 100. If BLOCK 1.5 is implicitly a structural block for C-14, V-02 scores 98.75 (C-14 FAIL). This resolves whether F-09 is required for C-14 once BLOCK 1.5 exists.

**V-03 vs V-04**: Both should score 100. Tests whether a Source column in BLOCK 1.5 produces any rubric-detectable lift or remains qualitative enforcement only.

**V-04 vs V-05**: Both should score 100. Tests whether cross-block count verification + F-10 orphan detection adds rubric-detectable quality over Source column alone.

---

## V-01 | Lifecycle Emphasis — BLOCK 1.5 as Prose Pre-Commitment List (C-15 FAIL by Design)
**Axis**: lifecycle-emphasis
**Hypothesis**: BLOCK 1.5 appears as a prose numbered list of scheduled reviewers rather than a table. The C-15 pass condition names "a roster commitment TABLE" — the table form is explicit. A prose pre-commitment list fulfills the proactive intent (roster locked before generation begins) but not the structural form requirement. Expected: C-15 FAIL (prose list != table), all other criteria PASS, score = 98.75. This isolates whether C-15 is form-sensitive (table required specifically) or presence-sensitive (any pre-commitment format is sufficient).

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 named stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — finding row with Sev cell empty or non-P1/P2/P3
F-03  Expert without signal       — domain expert row in BLOCK 1 with Signal detected cell empty
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — amend in BLOCK 5 scoped to full review instead of specific reviewer+section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row written before BLOCK 3
F-07  Incomplete expert trace     — domain expert row in BLOCK 1 with Expert added or Reason cell empty
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted or reviewer list is empty
```

Halt and restructure immediately if any of F-01 through F-09 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required)*

Stock disciplines (always run in BLOCK 2, do not modify this list):
- Architect
- Code-Quality
- Documentation
- Testing
- Process
- Implementation

Domain expert table — scan the full design for content signals before filling. Add 1 to 5 rows. Every row requires all three cells populated.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty.
If no content signals detected: single row `| No signals detected | None | — |`

---

**BLOCK 1.5 — REVIEWER PRE-COMMITMENT** *(F-09: this block must appear before BLOCK 2; omission fires F-09)*

The following reviewers are scheduled to run in BLOCK 2. A reviewer not on this list does not run.

Scheduled reviewers:
1. Architect (Stock)
2. Code-Quality (Stock)
3. Documentation (Stock)
4. Testing (Stock)
5. Process (Stock)
6. Implementation (Stock)
[7+. Each domain expert added in BLOCK 1, listed as: N. [Expert name] (Domain)]

List every domain expert from BLOCK 1 as additional numbered entries. F-09 fires if this block is omitted or if the list is empty.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 disciplines required; F-02: Sev column P1/P2/P3 only)*

Run all reviewers from the BLOCK 1.5 list, in listed order. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column contracts:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02 — halt and correct.
- `Section`: specific section, component, or decision name. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted Status with no Rationale row fires halt; block positioned between BLOCK 2 and BLOCK 3)*

Count all findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row — F-06 fires if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual P1/P2 concentration] |

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.
Never omit this block — F-04 fires on omission regardless of review content.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
This block is mandatory — F-08 fires if omitted entirely.

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

---

## V-02 | Output Format — BLOCK 1.5 Full Roster Table, No F-09
**Axis**: output-format
**Hypothesis**: BLOCK 1.5 is a proper two-column roster commitment table (Reviewer | Role) positioned before BLOCK 2 — satisfying the C-15 "roster commitment table" form requirement. F-09 is intentionally absent from the failure mode registry; the registry stops at F-08. The C-14 pass condition enumerates "findings, pyramid gate, consensus, unique catches, amend" as structural blocks — BLOCK 1.5 is not in this enumeration. If the enumeration is exhaustive, C-14 PASSES without F-09 and this variation scores 100. If BLOCK 1.5 is implicitly a structural block for C-14, C-14 FAILS and this scores 98.75. This is the C-14 rubric-boundary bet for R4.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 named stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — finding row with Sev cell empty or non-P1/P2/P3
F-03  Expert without signal       — domain expert row in BLOCK 1 with Signal detected cell empty
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — amend in BLOCK 5 scoped to full review instead of specific reviewer+section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row written before BLOCK 3
F-07  Incomplete expert trace     — domain expert row in BLOCK 1 with Expert added or Reason cell empty
F-08  Missing unique catches      — BLOCK 4 omitted entirely
```

Halt and restructure immediately if any of F-01 through F-08 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required)*

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table — scan the full design for content signals before filling. Add 1 to 5 rows. Every row requires all three cells populated.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty.
If no content signals detected: single row `| No signals detected | None | — |`

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE**

Commit the full reviewer roster before any finding is generated. Every reviewer listed here must produce a finding table in BLOCK 2.

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |
| [domain expert name from BLOCK 1] | Domain |

Add one row per domain expert added in BLOCK 1. Do not begin BLOCK 2 until this table is complete.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines required; F-02: Sev column P1/P2/P3 only)*

Run all reviewers from BLOCK 1.5, in listed order. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column contracts:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02 — halt and correct.
- `Section`: specific section, component, or decision name. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted Status with no Rationale row fires halt; block positioned between BLOCK 2 and BLOCK 3)*

Count all findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row — F-06 fires if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual P1/P2 concentration] |

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.
Never omit this block — F-04 fires on omission.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
This block is mandatory — F-08 fires if omitted entirely.

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

---

## V-03 | Phrasing Register — Imperative-First Register Throughout + BLOCK 1.5 Table + F-09
**Axis**: phrasing-register
**Hypothesis**: All lifecycle instructions use imperative/command phrasing ("HALT immediately," "DO NOT proceed," "VERIFY before continuing," "WRITE this row") rather than the conditional/descriptive register of R3 variations ("fires halt," "always required," "is positioned between"). BLOCK 1.5 is a full roster commitment table; F-09 is included in the registry. Structural content is identical to the minimum winning R3 form (V-03/R3) plus BLOCK 1.5 + F-09. Expected: score = 100. Tests whether imperative vs. descriptive phrasing register produces any qualitative difference in enforcement reliability — a dimension not yet captured by a rubric criterion.

HALT. Before generating any output: read the full failure mode registry. Every F-ID represents a detectable error. If any F-ID fires during generation, STOP and restructure before continuing.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2; HALT if fired
F-02  Unseveritied finding        — Sev cell empty or non-P1/P2/P3 in any finding row; HALT if fired
F-03  Expert without signal       — Signal detected cell empty in any BLOCK 1 domain expert row; HALT if fired
F-04  Missing consensus block     — BLOCK 3 omitted entirely; HALT if fired
F-05  Full-review amend           — BLOCK 5 Re-run scoped to "full review"; HALT if fired
F-06  Pyramid inverted, silent    — BLOCK 2.5 shows inverted with no Rationale row before BLOCK 3; HALT if fired
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any BLOCK 1 domain expert row; HALT if fired
F-08  Missing unique catches      — BLOCK 4 omitted entirely; HALT if fired
F-09  Coverage unverified         — BLOCK 1.5 omitted or empty; HALT if fired
```

DO NOT proceed to BLOCK 1 until you have read all nine entries above.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03, F-07)*

SCAN the full design artifact for content signals. For each signal, ADD one domain expert row. DO NOT add an expert without a detected signal — F-03 fires.

Stock table (FIXED — do not alter):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table — POPULATE before moving to BLOCK 1.5:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

VERIFY: every row has all three cells populated. F-03 fires on empty Signal detected. F-07 fires on empty Expert added or Reason.
If no signals found: WRITE single row `| No signals detected | None | — |`
DO NOT proceed to BLOCK 1.5 with any empty cells in this table.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: MANDATORY — omission fires F-09)*

WRITE the full reviewer roster before generating any finding. A reviewer absent from this table DOES NOT run in BLOCK 2.

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |
| [domain expert from BLOCK 1] | Domain |

ADD one row per domain expert from BLOCK 1. VERIFY: total rows = 6 stock + domain expert count from BLOCK 1. F-09 fires if this block is absent or empty. DO NOT begin BLOCK 2 until this table is complete.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock required; F-02: Sev P1/P2/P3 only)*

RUN every reviewer in BLOCK 1.5 order. WRITE one finding table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

ENFORCE these column contracts:
- `Sev`: P1, P2, or P3 ONLY. Any other value — HALT, correct it, then continue. F-02 fires.
- `Section`: name a specific section, component, or decision. DO NOT write "the design" or "overall."
- P1 rows: Section ALWAYS required.
- P2 rows: Section required for >= 50% of rows.
- No findings: WRITE `| — | — | No findings. |`

DO NOT proceed to BLOCK 2.5 until all reviewers from BLOCK 1.5 have a finding table. A missing reviewer fires F-01.

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted with no Rationale fires halt; MUST appear between BLOCK 2 and BLOCK 3)*

COUNT all findings from BLOCK 2. WRITE the Status cell for every row before continuing.

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

CHECK: P3 >= P2 >= P1?
- YES: WRITE `pyramid nominal` in all Status cells. PROCEED to BLOCK 3.
- NO: WRITE `inverted` in Status cells for violated levels. WRITE a Rationale row — F-06 fires if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the concentration] |

DO NOT begin BLOCK 3 until Status column is complete and Rationale row is written (if required).

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: MANDATORY — omission fires F-04)*

IDENTIFY findings raised by 2+ reviewers. IDENTIFY split opinions (opposite conclusions on the same decision). WRITE both.

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.] |

No consensus: WRITE `| CONSENSUS | none | — |` — DO NOT skip this block. F-04 fires on omission.
No splits: OMIT SPLIT rows only.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: MANDATORY — omission fires F-08 even when catches are empty)*

IDENTIFY findings raised by exactly one reviewer. WRITE them.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

No unique catches: WRITE `| UNIQUE | none | — |` — DO NOT skip this block. F-08 fires on omission.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: SCOPE to specific section — "full review" fires F-05)*

WRITE one amend entry per P1 finding. SCOPE each entry to a specific section only.

```
Finding:  [P1 summary]
Section:  [specific section or component to change]
Action:   [what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only — NEVER "full review"]
```

Full-review scope fires F-05 — HALT and re-scope.
Zero P1 findings: WRITE `No P1 findings — no amend actions required.`

---

## V-04 | Combined (Output-Format + Lifecycle) — BLOCK 1.5 with Source Column + F-09
**Axis**: combined (output-format + lifecycle-emphasis)
**Hypothesis**: BLOCK 1.5 extends the standard Reviewer | Role table with a third Source column distinguishing `Stock` from `Domain` reviewers. Every `Domain` row in BLOCK 1.5 must correspond to a row in the BLOCK 1 domain expert signal table — the Source column makes the linkage structurally visible at the commitment stage. F-09 fires on BLOCK 1.5 omission or a missing Source cell. Expected: score = 100. Tiebreaker test over V-03: does the Source column create earlier-stage detectability for the "expert added without BLOCK 1 signal" failure pattern (C-03, C-11, C-13) beyond what the domain expert table already provides?

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell empty or non-P1/P2/P3 in any finding row
F-03  Expert without signal       — Signal detected cell empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — BLOCK 5 Re-run scoped to "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row before BLOCK 3
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted or Source column missing from any row
```

Halt and restructure immediately if any of F-01 through F-09 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required)*

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table — scan the full design for content signals before filling. Add 1 to 5 rows.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty.
If no content signals detected: single row `| No signals detected | None | — |`

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block must appear; Source column required on every row)*

Commit the full reviewer roster before any finding is generated. Source column distinguishes stock disciplines (`Stock`) from domain experts added in BLOCK 1 (`Domain`). Every Domain row in this table must correspond to a row in the BLOCK 1 domain expert table.

| Reviewer | Role | Source |
|----------|------|--------|
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |
| [domain expert from BLOCK 1] | Domain expert | Domain |

Add one Domain row per domain expert from BLOCK 1. Source must be `Stock` or `Domain` — any other value is a format error. F-09 fires if this block is omitted or if any row is missing the Source cell. Do not begin BLOCK 2 with an incomplete roster table.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(Gate: all reviewers from BLOCK 1.5 must appear; F-01, F-02)*

Run every reviewer listed in BLOCK 1.5, in listed order. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column contracts:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02 — halt and correct before proceeding.
- `Section`: specific section, component, or decision name. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

Gate: Confirm all reviewers in BLOCK 1.5 have a finding table. A missing reviewer fires F-01. Do not begin BLOCK 2.5 until all finding tables are present.

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted Status with no Rationale row fires halt; positioned between BLOCK 2 and BLOCK 3)*

Count all findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row — F-06 fires if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual P1/P2 concentration] |

Gate: Status column must be fully populated. Rationale row must be present if any Status cell reads `inverted`. Do not begin BLOCK 3 until complete.

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.
Gate: This block is mandatory. F-04 fires on omission regardless of review content.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
Gate: This block is mandatory. F-08 fires if omitted entirely.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run must name specific section — "full review" fires F-05)*

```
Finding:  [P1 summary]
Section:  [specific section or component to change]
Action:   [what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only — never "full review"]
```

One entry per P1 finding. An amend scoped to "full review" fires F-05 — halt and re-scope.
If zero P1 findings: `No P1 findings — no amend actions required.`

---

## V-05 | Combined (Lifecycle + Inertia-Framing + Output-Format) — Full Proactive Stack: Source Column + Cross-Block Count Gate + F-09 + F-10
**Axis**: combined (lifecycle-emphasis + inertia-framing + output-format)
**Hypothesis**: BLOCK 1.5 adds both a Source column AND an explicit cross-block count verification gate: count domain-expert rows from BLOCK 1, confirm the count matches Domain rows in BLOCK 1.5. F-09 fires on BLOCK 1.5 omission or count mismatch. F-10 (orphaned domain expert) fires if a Domain row in BLOCK 1.5 has no corresponding Expert added value in the BLOCK 1 domain expert signal table — a reviewer scheduled to run but never traced to a signal. This is the maximal proactive prevention form: roster commitment + source column + count parity + orphan detection. Expected: score = 100. Qualitative bet: F-10 introduces a structurally distinct error class that neither F-03 (missing signal cell) nor F-09 (count mismatch) can catch — an expert present in the signal table but then substituted or renamed in BLOCK 1.5.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell empty or non-P1/P2/P3 in any finding row
F-03  Expert without signal       — Signal detected cell empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — BLOCK 5 Re-run scoped to "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row before BLOCK 3
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted, or Domain row count in BLOCK 1.5 does not match domain expert count in BLOCK 1
F-10  Orphaned domain expert      — BLOCK 1.5 contains a Domain row whose Reviewer name has no matching Expert added value in the BLOCK 1 domain expert table
```

Halt and restructure immediately if any of F-01 through F-10 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required)*

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table — scan the full design for content signals before filling. Add 1 to 5 rows.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty.
If no content signals detected: single row `| No signals detected | None | — |`

After filling this table: count domain expert rows (exclude the "No signals detected" row). Record as `BLOCK 1 domain count = [n]`. This count is used in the BLOCK 1.5 gate.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block must appear; Domain row count must match BLOCK 1 domain count; F-10: no orphaned domain experts)*

Commit the full reviewer roster before any finding is generated. Source column distinguishes `Stock` from `Domain`. Every Domain row must carry a Reviewer name that exactly matches an Expert added value from the BLOCK 1 domain expert signal table — any mismatch fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |
| [Expert added value from BLOCK 1] | Domain expert | Domain |

Add one Domain row per domain expert from BLOCK 1. Use the exact Expert added value as the Reviewer name.

Gate — run both checks before BLOCK 2:
1. Count Domain rows in this table. Must equal `BLOCK 1 domain count`. F-09 fires on mismatch.
2. For each Domain row, confirm Reviewer name matches an Expert added value in BLOCK 1. F-10 fires on any mismatch.

If no domain experts were added in BLOCK 1: no Domain rows. Table has 6 Stock rows only.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all reviewers from BLOCK 1.5 must appear; F-02: Sev P1/P2/P3 only)*

Run every reviewer listed in BLOCK 1.5, in listed order. One table per reviewer.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column contracts:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02 — halt and correct.
- `Section`: specific section, component, or decision name. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

Gate: Every reviewer in BLOCK 1.5 must have a finding table in this block. A missing reviewer fires F-01.

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted Status with no Rationale row fires halt; positioned between BLOCK 2 and BLOCK 3)*

Count all findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row — F-06 fires if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual P1/P2 concentration] |

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.
F-04 fires on omission regardless of review content.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
F-08 fires if omitted entirely.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run must name specific section — "full review" fires F-05)*

```
Finding:  [P1 summary]
Section:  [specific section or component to change]
Action:   [what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only — never "full review"]
```

One entry per P1 finding. An amend scoped to "full review" fires F-05 — halt and re-scope.
If zero P1 findings: `No P1 findings — no amend actions required.`
