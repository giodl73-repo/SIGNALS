**5 variations written** to `simulations/quest/variations/review-design-variations-R3-2026-03-14.md`.

---

## Summary

| Var | Axis | C-12 | C-13 | C-14 | Hypothesis |
|-----|------|------|------|------|------------|
| **V-01** | inertia-framing | PASS | **FAIL** (labeled prose) | PASS (F-01–F-08) | Isolates C-14 — labeled prose + complete F-IDs |
| **V-02** | output-format | PASS | PASS (expert table) | **FAIL** (no F-IDs) | Isolates C-13 — all-table, no F-IDs |
| **V-03** | inertia-framing | PASS | PASS (expert table) | PASS (+F-08 only) | Minimal V-05 R2 fix — single F-ID addition |
| **V-04** | combined (format + inertia) | PASS | PASS | PASS | Tables + F-01–F-08 + explicit block-gate instructions |
| **V-05** | combined (lifecycle + inertia + format) | PASS | PASS | PASS + F-09 | V-04 + BLOCK 1.5 coverage verification + F-09 |

---

## Design Bets

**V-01 vs V-02**: Both should miss exactly one of C-13/C-14 and score identically — confirms the two criteria are independent failure modes (`~1.43 pts each`).

**V-01 vs V-03**: V-01 uses labeled prose + F-01–F-08; V-03 uses expert table + F-01–F-08. The only difference is C-13. Delta should be exactly `1.43 pts`.

**V-03 vs V-04**: Adds block-gate "do not proceed" language at every boundary. Should both score 100 — tests whether gate language produces any measurable lift or is cosmetic.

**V-04 vs V-05**: V-05 adds BLOCK 1.5 (coverage verification) + F-09. C-14 pass condition covers "every structural block" — BLOCK 1.5 may or may not count as a mandatory structural block, making this a rubric edge-case bet. If F-09 counts toward C-14, V-05 is the most defensible C-14 PASS form.
viewer drift or add scoring uplift beyond V-04?

**Baseline changes R2 → R3:** All R2 variations scored 100 on the v2 rubric. R3 rubric adds C-12/C-13/C-14; aspirational denominator is now /7. C-12 is already satisfied by all R2 variations (Block 2.5 exists). C-13 fails V-01/V-02/V-03 from R2 (labeled prose). C-14 fails all R2 variations (no F-ID for unique catches). The primary fix is F-08 for unique catches + expert trace in table form.

---

## V-01 | Inertia Framing — Complete F-ID Registry (F-01–F-08), Labeled-Prose Expert Trace
**Axis**: inertia-framing
**Hypothesis**: Extending the R2 F-ID registry with F-08 (BLOCK 4 omitted entirely) closes C-14 by ensuring every structural block has a named halt condition. Expert trace stays in labeled-prose form — C-13 FAIL by design. This variation isolates C-14: it should pass C-14 while failing C-13, confirming that (1) C-14 does not require table form and (2) C-13 specifically requires table columns, not just labeled fields.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 named stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — finding row with Sev cell empty or non-P1/P2/P3
F-03  Expert without signal       — domain expert in BLOCK 1 with Signal detected field missing or empty
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — amend in BLOCK 5 scoped to full review instead of specific reviewer+section
F-06  Pyramid inverted, silent    — BLOCK 2.5 shows P1 > P2 or P2 > P3 with no rationale written before BLOCK 3
F-07  Incomplete expert trace     — BLOCK 1 expert entry missing Expert added or Reason field
F-08  Missing unique catches      — BLOCK 4 omitted entirely
```

Halt and restructure immediately if any of F-01 through F-08 fires.

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

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

Findings raised by exactly one reviewer:
> UNIQUE ([Reviewer]): [finding]

If none: write `No unique catches.`

This block is mandatory — F-08 fires if it is omitted entirely.

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

## V-02 | Output Format — All-Table Structure, No F-IDs
**Axis**: output-format
**Hypothesis**: Converting every output block to structured table form provides C-12 (pyramid gate as dedicated block) and C-13 (expert trace as table columns) via visual completeness enforcement — empty cells are impossible to hide. No F-IDs are used. C-14 FAILS by design — confirming that named F-IDs are required for C-14 even when table structure is complete. This variation isolates the C-13 mechanism from the C-14 mechanism and establishes the exact scoring gap between all-table-no-F-IDs vs. all-table-plus-F-IDs.

You are running a multi-expert design review. The input is a design artifact. All output is in structured table form — no block may be rendered as prose bullets or labeled fields. Produce the six blocks below in order.

---

**BLOCK 1 — EXPERT ROSTER**

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table — scan the full design before filling. Add 1 to 5 rows. Every row must have all three cells populated before proceeding to BLOCK 2.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

If no content signals are found: single row `| No signals detected | None | — |`

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
- `Sev`: P1, P2, or P3 only. Any other value is a format error — correct it before moving on.
- `Section`: specific section, component, or decision name. "The design" or "overall" are not valid.
- P1 rows: Section always required.
- P2 rows: Section required for >= 50% of rows.
- No findings: row `| — | — | No findings. |`

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION**

This block must appear between BLOCK 2 and BLOCK 3. Count findings from BLOCK 2 and fill the Status column before proceeding.

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row:

| Note | — |
|------|---|
| Rationale | [name the design area and the risk concentration that explains the inverted distribution] |

Do not proceed to BLOCK 3 until the Status column is complete.

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS**

This block is always required. If no findings overlap, write the no-consensus row.

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.

---

**BLOCK 4 — UNIQUE CATCHES**

This block is always required. If no unique catches exist, write the empty row.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`

---

**BLOCK 5 — AMEND PATHWAY**

One entry per P1 finding. Scope is per-section only — never "full review."

```
Finding:  [P1 summary]
Section:  [specific section or component to change]
Action:   [what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only — never "full review"]
```

If zero P1 findings: `No P1 findings — no amend actions required.`

---

## V-03 | Inertia Framing — Minimal V-05 Extension (F-08 Only)
**Axis**: inertia-framing
**Hypothesis**: The R2 V-05 variation (expert trace table + F-01–F-07) misses C-14 by exactly one F-ID: the unique catches block has no named halt condition. Adding F-08 (BLOCK 4 omitted entirely) is the minimum change to close C-14 on the strongest R2 baseline. This variation tests whether a single targeted F-ID addition produces 100 on the R3 rubric without any other structural changes — validating that V-05 was already complete except for this one gap.

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
F-08  Missing unique catches      — BLOCK 4 omitted entirely
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

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

```
Type    | Reviewer     | Finding
--------|--------------|------------------------------------------
UNIQUE  | [reviewer]   | [finding not raised by any other reviewer]
```

If none: row `UNIQUE | none | —`
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

## V-04 | Combined (Output-Format + Inertia) — Complete F-01–F-08 + All-Table + Explicit Block-Gate Instructions
**Axis**: combined (output-format + inertia-framing)
**Hypothesis**: Layering complete F-IDs (F-01–F-08, every block covered for C-14) on top of full table structure (expert trace table for C-13, pyramid gate table for C-12) with explicit "do not proceed" gate instructions at every block boundary produces the strongest enforcement form: named halt conditions make skips detectable (C-14), table columns make omissions visible (C-13), and block-gate transitions prevent sequencing errors. This is the combined test of whether F-IDs + tables + gates creates measurable uplift over V-03 (F-IDs + tables without gate language).

You are running a multi-expert design review. Read the failure mode registry first. Produce all six blocks in order. Do not proceed to the next block until the current block's gate condition is satisfied.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell in any finding row is empty or non-P1/P2/P3
F-03  Expert without signal       — Signal detected cell empty in any domain expert row (BLOCK 1)
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — Re-run in BLOCK 5 scoped to "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row written before BLOCK 3
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any domain expert row (BLOCK 1)
F-08  Missing unique catches      — BLOCK 4 omitted entirely
```

Halt and restructure immediately if any F fires.

---

**BLOCK 1 — EXPERT ROSTER** *(Gate: all domain expert rows must have three populated cells before BLOCK 2 begins; F-03, F-07)*

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table — scan the full design before filling. Entries: 1 to 5 rows required.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

Gate: Every row requires Signal detected, Expert added, and Reason cells populated. F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty. Do not begin BLOCK 2 with any empty cells in this table.

If no content signals are found: single row `| No signals detected | None | — |`

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(Gate: all 6 stock disciplines must appear, all Sev cells P1/P2/P3; F-01, F-02)*

Stock disciplines first (all 6 in roster order), then domain experts. One table per reviewer.

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

Gate: Confirm all 6 stock discipline tables are present (F-01 fires if missing). Confirm no Sev cell is empty or non-P1/P2/P3 (F-02 fires on violation). Do not begin BLOCK 2.5 until both conditions hold.

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(Gate: Status column must be complete and Rationale row written if inverted before BLOCK 3 begins; F-06)*

This block is positioned between BLOCK 2 and BLOCK 3. Count findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`. Proceed to BLOCK 3.
- NO: Status cells for inverted levels read `inverted`. Add a Rationale row before BLOCK 3 — F-06 fires if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual P1/P2 concentration] |

Gate: Status column must be fully populated. Rationale row must be present if any Status cell reads `inverted`. Do not begin BLOCK 3 without completing this block.

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(Gate: block must appear; F-04)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.

Gate: This block is mandatory. F-04 fires on omission regardless of review content. Do not skip to BLOCK 4.

---

**BLOCK 4 — UNIQUE CATCHES** *(Gate: block must appear; F-08)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`

Gate: This block is mandatory. F-08 fires on omission even when catches are empty. Do not skip to BLOCK 5.

---

**BLOCK 5 — AMEND PATHWAY** *(Gate: Re-run must name specific section — "full review" fires F-05)*

```
Finding:  [P1 summary]
Section:  [specific section or component to change]
Action:   [what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only — never "full review"]
```

One entry per P1 finding. An amend scoped to "full review" fires F-05 — halt and re-scope.
If zero P1 findings: `No P1 findings — no amend actions required.`

---

## V-05 | Combined (Lifecycle + Inertia + Output-Format) — Coverage Verification Block + F-09 + Full F-ID Set
**Axis**: combined (lifecycle-emphasis + inertia-framing + output-format)
**Hypothesis**: Adding an explicit BLOCK 1.5 (Coverage Verification) between expert selection and finding generation forces a roster commitment: every reviewer listed in BLOCK 1 must appear in BLOCK 2, and the list is produced before any finding is written. F-09 (coverage unverified — BLOCK 1.5 omitted or count mismatch) extends the F-ID registry to a 9th halt condition covering the roster-to-findings transition. This tests whether an explicit lifecycle confirmation step prevents mid-review reviewer drift (a stock discipline silently dropped mid-output) while preserving all C-12/C-13/C-14 passes from V-04.

You are running a multi-expert design review. Read the failure mode registry first. Produce the seven blocks in order. Do not proceed to the next block until the current block's gate condition is satisfied.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell in any finding row is empty or non-P1/P2/P3
F-03  Expert without signal       — Signal detected cell empty in any domain expert row (BLOCK 1)
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — Re-run in BLOCK 5 scoped to "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row written
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any domain expert row (BLOCK 1)
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted or reviewer count in BLOCK 1.5 does not match BLOCK 1 total
```

Halt and restructure immediately if any F fires.

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

Domain expert table — scan the full design before filling. Entries: 1 to 5 rows required.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty.

If no content signals are found: single row `| No signals detected | None | — |`

---

**BLOCK 1.5 — COVERAGE VERIFICATION** *(F-09: block must appear; total reviewer count must match BLOCK 1)*

List every reviewer scheduled to run in BLOCK 2. This is the commitment table: a reviewer not on this list does not run. A reviewer on this list who does not appear in BLOCK 2 fires F-01.

| # | Reviewer | Role | Status |
|---|----------|------|--------|
| 1 | Architect | Stock | scheduled |
| 2 | Code-Quality | Stock | scheduled |
| 3 | Documentation | Stock | scheduled |
| 4 | Testing | Stock | scheduled |
| 5 | Process | Stock | scheduled |
| 6 | Implementation | Stock | scheduled |
| [7+] | [domain expert name from BLOCK 1] | Domain | scheduled |

Gate: Total rows = 6 stock + number of domain expert rows from BLOCK 1. Every row reads `scheduled`. F-09 fires if this block is omitted or if count does not match BLOCK 1.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all reviewers from BLOCK 1.5 must appear; F-02: Sev column P1/P2/P3 only)*

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

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: inverted Status with no Rationale row fires halt; block positioned between BLOCK 2 and BLOCK 3)*

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

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.
F-04 fires on omission.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
F-08 fires on omission.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run must name specific section — "full review" fires F-05)*

```
Finding:  [P1 summary]
Section:  [specific section or component to change]
Action:   [what to add, remove, or clarify]
Re-run:   [reviewer name(s)] on [section scope only — never "full review"]
```

One entry per P1 finding. F-05 fires on full-review scope.
If zero P1 findings: `No P1 findings — no amend actions required.`
