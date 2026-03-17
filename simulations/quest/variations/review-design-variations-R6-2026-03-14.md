## Round 6 Variations — review-design

Written to `simulations/quest/variations/review-design-variations-R6-2026-03-14.md`.

---

### Variation Table

| Var | Axis | New Bet |
|-----|------|---------|
| **V-01** | phrasing-register | Formal declarative language throughout (MUST/SHALL/non-conformant) |
| **V-02** | output-format | BLOCK 3 as 4-column table: `Type \| Issue \| Reviewers \| Synthesis` |
| **V-03** | lifecycle-emphasis | BLOCK 0 pre-scan catalogue separates detection from expert mapping |
| **V-04** | combined (lifecycle + output-format) | BLOCK 0 pre-scan + 4-column BLOCK 3 + full F-01–F-12 stack |
| **V-05** | combined max | Formal register + BLOCK 0 + 4-column BLOCK 3 + full F-01–F-12 stack |

---

### Design Rationale

**Baseline**: R5 V-05 already carries C-18 (F-11), C-19 (F-12), and C-20 (BLOCK 5 table). All three v6 aspirational criteria are baked in. R6 must push *new* axes.

**V-01 (phrasing-register)** — the one axis never isolated. R2's conversational register degraded C-08 enforcement. Does formal declarative ("MUST", "SHALL", "non-conformant") produce stronger adherence than imperative ("Run every reviewer", "Halt and restructure")? Structure unchanged from R5-V05 — register is the single variable.

**V-02 (BLOCK 3 4-column)** — the blank-cell argument extended to synthesis. Currently `Reviewers / Synthesis` is a merged cell with an inline `— Synthesis:` marker. Column separation puts synthesis in its own cell: F-11 fires on blank Synthesis column, same visibility mechanism as Sev column for F-02 and Re-run Scope column for F-05.

**V-03 (BLOCK 0 pre-scan)** — two-pass structure. BLOCK 1 requires simultaneous scan + fill today. A dedicated BLOCK 0 detection pass catalogues all signals first; BLOCK 1 is restricted to that catalogue. Targets C-03/C-11/C-13 accuracy — tests if decoupling detection from mapping reduces missed signals.

**V-04** combines V-03 + V-02: pre-scan (better detection) and synthesis column (better synthesis enforceability) target distinct failure surfaces — tests if they're additive.

**V-05** is the full R6 ceiling: all three axes stacked, intended as the extraction source for v7 criterion candidates.
1?
- V-03 isolation: Does a pre-scan pass improve domain expert coverage (C-03/C-11/C-13) by decoupling signal detection from table filling?
- V-04 vs V-02+V-03: Are BLOCK 0 and 4-column BLOCK 3 additive improvements or do they target overlapping failure modes?
- V-05 vs V-04: Does formal declarative language stack with structural improvements, or is its effect absorbed when structure is already maximal?

---

## V-01 | Phrasing Register — Formal Declarative Throughout
**Axis**: phrasing-register
**Hypothesis**: R5 V-05 uses imperative commands throughout ("Run every reviewer", "Halt and restructure immediately"). This variation rewrites all instructions using formal declarative specification language: "MUST", "SHALL", "is non-conformant", "A conformance failure is raised when." The structural blocks, table forms, F-ID registry, and all enforcement mechanisms are unchanged from R5 V-05. The single variable is register. R2's conversational register degraded C-08 enforcement — the question is whether formal declarative (opposite end of the register spectrum) produces measurably stronger adherence than imperative. Expected score: 100 on v6. If scores on C-18/C-19/C-20 improve vs R5 V-05, register is a meaningful variable; if identical, register is orthogonal.

A multi-expert design review SHALL be conducted according to the following specification. Each output block MUST conform to its stated requirements. A conformance failure is declared when any halt condition fires; the output SHALL NOT proceed past a failed block until the failure is resolved.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks present in BLOCK 2
F-02  Unseveritied finding        — any finding row contains a Sev value other than P1, P2, or P3
F-03  Expert without signal       — Signal detected cell is empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 is absent from the output
F-05  Full-review amend           — Re-run Scope cell in BLOCK 5 contains "full review"
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status is inverted and no Rationale row is present
F-07  Incomplete expert trace     — Expert added or Reason cell is empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 is absent from the output
F-09  Coverage unverified         — BLOCK 1.5 is absent, or Domain row count in BLOCK 1.5 does not equal BLOCK 1 domain count
F-10  Orphaned domain expert      — a Domain row in BLOCK 1.5 carries a Reviewer name with no matching Expert added value in BLOCK 1
F-11  Split without synthesis     — a SPLIT row in BLOCK 3 has an empty or absent Synthesis field
F-12  Amend count mismatch        — BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated)*

The full design document SHALL be scanned for content signals before the domain expert table is populated. Each detected signal MUST produce exactly one domain expert row. All three cells in every row MUST be populated.

Stock table (fixed — SHALL NOT be modified):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

A Signal detected cell that is empty is non-conformant under F-03. An Expert added or Reason cell that is empty is non-conformant under F-07.
If no content signals are detected: a single row `| No signals detected | None | — |` SHALL be present.

After population: the count of domain expert rows (excluding the "No signals detected" row) SHALL be recorded as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain row count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

The complete reviewer roster MUST be committed before any finding block is generated. Domain experts SHALL appear before stock disciplines. The Source column MUST distinguish `Domain` from `Stock`. Every Domain row MUST carry a Reviewer name that exactly matches an Expert added value from the BLOCK 1 domain expert table — any deviation is non-conformant under F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

One Domain row MUST be added per domain expert from BLOCK 1, positioned above the Stock rows, using the exact Expert added value as the Reviewer name.

Conformance gate — both checks SHALL be resolved before BLOCK 2 begins:
1. The count of Domain rows in this table MUST equal `BLOCK 1 domain count`. F-09 is raised on mismatch.
2. Every Domain row Reviewer name MUST exactly match an Expert added value in BLOCK 1. F-10 is raised on any mismatch.

If no domain experts were added in BLOCK 1: no Domain rows SHALL be present. The table SHALL contain 6 Stock rows only.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3)*

A finding table MUST be generated for every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers SHALL run first.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column conformance requirements:
- `Sev`: SHALL contain exactly one of P1, P2, or P3. Any other value is non-conformant under F-02.
- `Section`: SHALL name a specific section, component, or decision. The values "the design" or "overall" are non-conformant.
- P1 rows: Section MUST be populated.
- P2 rows: Section MUST be populated in >= 50% of P2 rows.
- A reviewer with no findings: a single row `| — | — | No findings. |` MUST be present.

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any reviewer fires F-01. BLOCK 2.5 SHALL NOT begin until all finding tables are present.

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: an inverted Status MUST be accompanied by a Rationale row; positioned between BLOCK 2 and BLOCK 3)*

All findings from BLOCK 2 SHALL be counted:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

Conformance: P3 >= P2 >= P1?
- YES: all Status cells SHALL read `pyramid nominal`. Proceed to BLOCK 3.
- NO: inverted levels SHALL carry Status `inverted`. A Rationale row MUST be present — F-06 is raised if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual severity concentration] |

`P1 count = [n from P1 row]` SHALL be recorded. This value is the anchor for the BLOCK 5 conformance gate (F-12).

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: every SPLIT row Synthesis field MUST be populated)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent. naming the underlying design tension] |

If no consensus: a row `| CONSENSUS | none | — |` MUST be present.
If no splits: SPLIT rows SHALL be omitted.

Split synthesis conformance: every SPLIT row Synthesis field MUST name the underlying design tension — not a restatement of opposing positions. An empty or absent Synthesis field is non-conformant under F-11. The block SHALL NOT be closed until all SPLIT row Synthesis fields are populated.

BLOCK 3 absence fires F-04 regardless of review content.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: MUST be present — absence fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If no unique catches: a row `| UNIQUE | none | — |` MUST be present.
BLOCK 4 absence fires F-08.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; table form required)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component — never "full review." Domain expert reviewers are preferred Re-run Scope candidates where their thematic area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Re-run Scope`: MUST contain reviewer name(s) and section scope. "Full review" is non-conformant under F-05.

Conformance gate before closing: the count of amend rows (excluding the "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised if BLOCK 5 entry count < P1 count — missing entries SHALL be added before the block closes.

If zero P1 findings: a row `| — | — | — | No P1 findings — no amend actions required. |` SHALL be present.

---

## V-02 | Output Format — BLOCK 3 as 4-Column Synthesis Table
**Axis**: output-format
**Hypothesis**: The current BLOCK 3 table merges reviewer positions and synthesis into a single `Reviewers / Synthesis` cell for SPLIT rows, using an inline marker `— Synthesis: [text]`. This mirrors the pre-C-10 finding format: requirements stated in a single column are hideable. A 4-column BLOCK 3 table (`Type | Issue | Reviewers | Synthesis`) separates synthesis into a structurally distinct cell. F-11 fires on a blank `Synthesis` column cell for SPLIT rows — the same blank-cell visibility argument that applied to `Sev` in C-10 and `Re-run Scope` in C-20. Expected score: 100 on v6. The bet: column separation of synthesis materially improves C-09 and C-18 output quality over the inline marker form.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell empty or non-P1/P2/P3 in any finding row
F-03  Expert without signal       — Signal detected cell empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — Re-run Scope cell in BLOCK 5 contains "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row before BLOCK 3
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted, or Domain row count in BLOCK 1.5 does not match domain expert count in BLOCK 1
F-10  Orphaned domain expert      — BLOCK 1.5 contains a Domain row whose Reviewer name has no matching Expert added value in BLOCK 1
F-11  Split without synthesis     — BLOCK 3 contains a SPLIT row whose Synthesis column cell is empty or absent
F-12  Amend count mismatch        — BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
```

Halt and restructure immediately if any of F-01 through F-12 fires.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required)*

Scan the full design for content signals before filling the domain expert table. Add 1 to 5 rows. Every row requires all three cells populated.

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [exact phrase or concept from the design] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty. F-07 fires if Expert added or Reason is empty.
If no content signals detected: single row `| No signals detected | None | — |`

After filling: count domain expert rows (exclude "No signals detected" row). Record as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block must appear; Domain row count must match BLOCK 1 domain count; F-10: no orphaned domain experts)*

Commit the full reviewer roster before any finding is generated. Domain experts are listed first, then stock disciplines. Source column distinguishes `Stock` from `Domain`. Every Domain row must carry a Reviewer name that exactly matches an Expert added value from BLOCK 1 — any mismatch fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Add one Domain row per domain expert from BLOCK 1, placed above the Stock rows. Use the exact Expert added value as the Reviewer name.

Gate — run both checks before BLOCK 2:
1. Count Domain rows. Must equal `BLOCK 1 domain count`. F-09 fires on mismatch.
2. For each Domain row, confirm Reviewer name matches an Expert added value in BLOCK 1. F-10 fires on any mismatch.

If no domain experts in BLOCK 1: no Domain rows. Table has 6 Stock rows only.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines required; F-02: Sev P1/P2/P3 only; domain experts run first)*

Run every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers run first. One table per reviewer.

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

Gate: Every reviewer in BLOCK 1.5 must have a finding table. A missing reviewer fires F-01. Do not begin BLOCK 2.5 until all finding tables are present.

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

Record `P1 count = [n from P1 row]`. This count is the anchor for the BLOCK 5 gate (F-12).

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required; F-11: SPLIT Synthesis cell must be populated)*

Synthesis is a dedicated column for SPLIT rows. A blank Synthesis cell fires F-11. CONSENSUS rows carry `—` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | — |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension — not a restatement of opposing positions] |

If no consensus: row `| CONSENSUS | none | — | — |`
If no splits: omit SPLIT rows entirely.

Column contracts:
- `Synthesis` for SPLIT rows: must name the underlying design tension. A restatement of the opposing positions is not sufficient. An empty Synthesis cell fires F-11 — halt and write the synthesis before continuing.
- `Synthesis` for CONSENSUS rows: always `—`.

F-04 fires if this block is omitted. F-11 fires on any SPLIT row with an empty Synthesis cell.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
F-08 fires if omitted entirely.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run Scope "full review" fires F-05; F-12: entry count must equal P1 count from BLOCK 2.5; table form required)*

One row per P1 finding. Re-run Scope must name the specific section or component only. Domain-first ordering in BLOCK 2 means domain expert reviewers are preferred Re-run Scope candidates when their thematic area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column contracts:
- `Re-run Scope`: reviewer(s) + section scope only. "Full review" fires F-05 — halt and re-scope.

Gate before closing: count amend rows (exclude the "no P1 findings" row). Must equal `P1 count` from BLOCK 2.5. F-12 fires if BLOCK 5 entry count < P1 count — halt and add the missing entries.

If zero P1 findings: row `| — | — | — | No P1 findings — no amend actions required. |`

---

## V-03 | Lifecycle Emphasis — BLOCK 0 Pre-Scan Pass
**Axis**: lifecycle-emphasis
**Hypothesis**: BLOCK 1 currently requires simultaneous scan + table fill: the model must detect content signals and immediately map each one to an expert. This single-pass structure may cause signal detection to be compressed or bypassed under table-filling pressure. A dedicated BLOCK 0 pre-scan pass catalogues all content signals first — without filling any tables — producing a signal inventory that BLOCK 1 then draws from exclusively. BLOCK 1 is restricted: no domain expert may be added whose signal is not present in the BLOCK 0 catalogue. The bet: two-pass structure (detect, then map) produces more complete domain expert coverage (C-03/C-11/C-13) and reduces the chance that a signal is detected but not acted on. Full R5-V05 stack (F-01–F-12, domain-first, BLOCK 5 table, Source column) is included at baseline. Expected score: 100 on v6.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell empty or non-P1/P2/P3 in any finding row
F-03  Expert without signal       — Signal detected cell empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — Re-run Scope cell in BLOCK 5 contains "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row before BLOCK 3
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted, or Domain row count in BLOCK 1.5 does not match domain expert count in BLOCK 1
F-10  Orphaned domain expert      — BLOCK 1.5 contains a Domain row whose Reviewer name has no matching Expert added value in BLOCK 1
F-11  Split without synthesis     — BLOCK 3 contains a SPLIT row whose Synthesis field is empty or absent
F-12  Amend count mismatch        — BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
```

Halt and restructure immediately if any of F-01 through F-12 fires.

---

**BLOCK 0 — CONTENT SIGNAL CATALOGUE** *(Pre-scan only — no tables filled, no experts assigned)*

Read the full design document. For every phrase, concept, or decision that signals a specialized domain not covered by the 6 stock disciplines, record one row. This is a detection pass only — expert assignment happens in BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals detected: row `| No domain signals detected | — |`

Gate: BLOCK 1 may only add domain experts whose signals appear in this catalogue. An expert in BLOCK 1 whose signal is absent from BLOCK 0 is non-conformant — BLOCK 0 is the canonical signal inventory.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required; signals must trace to BLOCK 0)*

Draw from the BLOCK 0 signal catalogue. For each catalogued signal that warrants a domain expert, add one row. Every row requires all three cells populated.

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [signal phrase from BLOCK 0 catalogue] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty or does not match a BLOCK 0 catalogue entry. F-07 fires if Expert added or Reason is empty.
If no signals were catalogued in BLOCK 0: single row `| No signals detected | None | — |`

After filling: count domain expert rows (exclude "No signals detected" row). Record as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block must appear; Domain row count must match BLOCK 1 domain count; F-10: no orphaned domain experts)*

Commit the full reviewer roster before any finding is generated. Domain experts are listed first, then stock disciplines. Source column distinguishes `Stock` from `Domain`. Every Domain row must carry a Reviewer name that exactly matches an Expert added value from BLOCK 1 — any mismatch fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Add one Domain row per domain expert from BLOCK 1, placed above the Stock rows. Use the exact Expert added value as the Reviewer name.

Gate — run both checks before BLOCK 2:
1. Count Domain rows. Must equal `BLOCK 1 domain count`. F-09 fires on mismatch.
2. For each Domain row, confirm Reviewer name matches an Expert added value in BLOCK 1. F-10 fires on any mismatch.

If no domain experts in BLOCK 1: no Domain rows. Table has 6 Stock rows only.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines required; F-02: Sev P1/P2/P3 only; domain experts run first)*

Run every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers run first. One table per reviewer.

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

Gate: Every reviewer in BLOCK 1.5 must have a finding table. A missing reviewer fires F-01. Do not begin BLOCK 2.5 until all finding tables are present.

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

Record `P1 count = [n from P1 row]`. This count is the anchor for the BLOCK 5 gate (F-12).

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required — omission fires F-04; F-11: SPLIT rows require synthesis)*

| Type | Issue | Reviewers / Synthesis |
|------|-------|-----------------------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] |
| SPLIT | [contested decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent. naming the underlying design tension] |

If no consensus: row `| CONSENSUS | none | — |`
If no splits: omit SPLIT rows.

Split synthesis requirement: every SPLIT row Synthesis field must name the underlying design tension — not merely restate the opposing positions. An empty or absent Synthesis field fires F-11. Halt and write the synthesis before continuing.

F-04 fires on omission. F-11 fires on any SPLIT row with an empty Synthesis field.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
F-08 fires if omitted entirely.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run Scope "full review" fires F-05; F-12: entry count must equal P1 count from BLOCK 2.5; table form required)*

One row per P1 finding. Re-run Scope must name the specific section or component only. Domain experts from BLOCK 0 signal areas are preferred Re-run Scope candidates when their thematic area overlaps with the P1 section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column contracts:
- `Re-run Scope`: reviewer(s) + section scope only. "Full review" fires F-05 — halt and re-scope.

Gate before closing: count amend rows (exclude the "no P1 findings" row). Must equal `P1 count` from BLOCK 2.5. F-12 fires if BLOCK 5 entry count < P1 count — halt and add the missing entries.

If zero P1 findings: row `| — | — | — | No P1 findings — no amend actions required. |`

---

## V-04 | Combined (Lifecycle + Output-Format) — BLOCK 0 Pre-Scan + 4-Column BLOCK 3 + Full Stack
**Axis**: combined (lifecycle-emphasis + output-format)
**Hypothesis**: Combines V-03's BLOCK 0 pre-scan catalogue with V-02's 4-column BLOCK 3 synthesis table. Pre-scan decouples signal detection from expert mapping, improving domain expert coverage quality. The 4-column BLOCK 3 separates synthesis from reviewer positions, making F-11 (C-18) structurally enforceable via blank-cell detection rather than inline text inspection. These address distinct failure surfaces: BLOCK 0 targets C-03/C-11/C-13 (expert selection accuracy); 4-column BLOCK 3 targets C-09/C-18 (synthesis quality). Full F-01–F-12 enforcement stack, domain-first ordering, Source column, and BLOCK 5 4-column table from R5-V05 are included at baseline. Expected score: 100 on v6. Tests whether scan improvement and synthesis structural improvement are additive.

You are running a multi-expert design review. Read the failure mode registry before generating any output. Halt and restructure immediately if any failure mode fires.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks in BLOCK 2
F-02  Unseveritied finding        — Sev cell empty or non-P1/P2/P3 in any finding row
F-03  Expert without signal       — Signal detected cell empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 omitted entirely
F-05  Full-review amend           — Re-run Scope cell in BLOCK 5 contains "full review" instead of specific section
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status shows inverted with no Rationale row before BLOCK 3
F-07  Incomplete expert trace     — Expert added or Reason cell empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 omitted entirely
F-09  Coverage unverified         — BLOCK 1.5 omitted, or Domain row count in BLOCK 1.5 does not match domain expert count in BLOCK 1
F-10  Orphaned domain expert      — BLOCK 1.5 contains a Domain row whose Reviewer name has no matching Expert added value in BLOCK 1
F-11  Split without synthesis     — BLOCK 3 contains a SPLIT row whose Synthesis column cell is empty or absent
F-12  Amend count mismatch        — BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
```

Halt and restructure immediately if any of F-01 through F-12 fires.

---

**BLOCK 0 — CONTENT SIGNAL CATALOGUE** *(Pre-scan only — no tables filled, no experts assigned)*

Read the full design document. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, record one row. This is a detection pass only.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals detected: row `| No domain signals detected | — |`

Gate: BLOCK 1 may only add domain experts whose signals appear in this catalogue.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required; signals must trace to BLOCK 0)*

Draw from the BLOCK 0 signal catalogue. For each catalogued signal that warrants a domain expert, add one row. Every row requires all three cells populated.

Stock table (fixed — do not modify):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [signal phrase from BLOCK 0 catalogue] | [expert title or role] | [one sentence: why this signal warrants this expert] |

F-03 fires if Signal detected is empty or does not match a BLOCK 0 catalogue entry. F-07 fires if Expert added or Reason is empty.
If no signals were catalogued in BLOCK 0: single row `| No signals detected | None | — |`

After filling: count domain expert rows (exclude "No signals detected" row). Record as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block must appear; Domain row count must match BLOCK 1 domain count; F-10: no orphaned domain experts)*

Commit the full reviewer roster before any finding is generated. Domain experts are listed first, then stock disciplines. Source column distinguishes `Stock` from `Domain`. Every Domain row must carry a Reviewer name that exactly matches an Expert added value from BLOCK 1 — any mismatch fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Add one Domain row per domain expert from BLOCK 1, placed above the Stock rows. Use the exact Expert added value as the Reviewer name.

Gate — run both checks before BLOCK 2:
1. Count Domain rows. Must equal `BLOCK 1 domain count`. F-09 fires on mismatch.
2. For each Domain row, confirm Reviewer name matches an Expert added value in BLOCK 1. F-10 fires on any mismatch.

If no domain experts in BLOCK 1: no Domain rows. Table has 6 Stock rows only.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines required; F-02: Sev P1/P2/P3 only; domain experts run first)*

Run every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers run first. One table per reviewer.

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

Gate: Every reviewer in BLOCK 1.5 must have a finding table. A missing reviewer fires F-01. Do not begin BLOCK 2.5 until all finding tables are present.

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

Record `P1 count = [n from P1 row]`. This count is the anchor for the BLOCK 5 gate (F-12).

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required; F-11: SPLIT Synthesis cell must be populated)*

Synthesis is a dedicated column. A blank Synthesis cell for a SPLIT row fires F-11. CONSENSUS rows carry `—` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | — |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension — not a restatement of opposing positions] |

If no consensus: row `| CONSENSUS | none | — | — |`
If no splits: omit SPLIT rows entirely.

Column contracts:
- `Synthesis` for SPLIT rows: must name the underlying design tension. Restatement of opposing positions is not sufficient. Empty Synthesis cell fires F-11 — halt and write synthesis before continuing.
- `Synthesis` for CONSENSUS rows: always `—`.

F-04 fires if this block is omitted. F-11 fires on any SPLIT row with an empty Synthesis cell.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: block must appear — omission fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If none: row `| UNIQUE | none | — |`
F-08 fires if omitted entirely.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run Scope "full review" fires F-05; F-12: entry count must equal P1 count from BLOCK 2.5; table form required)*

One row per P1 finding. Re-run Scope must name the specific section or component only. Domain experts from BLOCK 0 signal areas are preferred Re-run Scope candidates when their thematic area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column contracts:
- `Re-run Scope`: reviewer(s) + section scope only. "Full review" fires F-05 — halt and re-scope.

Gate before closing: count amend rows (exclude the "no P1 findings" row). Must equal `P1 count` from BLOCK 2.5. F-12 fires if BLOCK 5 entry count < P1 count — halt and add the missing entries.

If zero P1 findings: row `| — | — | — | No P1 findings — no amend actions required. |`

---

## V-05 | Combined Maximum — Formal Register + BLOCK 0 + 4-Column BLOCK 3 + Full Stack
**Axis**: combined (phrasing-register + lifecycle-emphasis + output-format)
**Hypothesis**: Maximum R6 form. Formal declarative register throughout (V-01 axis). BLOCK 0 pre-scan catalogue before BLOCK 1 (V-03 axis). 4-column BLOCK 3 with dedicated Synthesis column (V-02 axis). Full F-01–F-12 enforcement stack, domain-first ordering, Source column (C-16), F-10 orphan detection (C-17), F-11 split synthesis (C-18), F-12 amend count parity (C-19), BLOCK 5 4-column amend table (C-20). Each axis targets a distinct failure surface: register (adherence quality), pre-scan (detection coverage), column separation (synthesis enforceability). This is the intended extraction source for v7 rubric criteria — any new structural pattern that achieves consistent output improvement over V-04 is a C-21+ candidate. Expected score: 100 on v6.

A multi-expert design review SHALL be conducted according to the following specification. Each output block MUST conform to its stated requirements. A conformance failure is declared when any halt condition fires; the output SHALL NOT proceed past a failed block until the failure is resolved.

**Failure Mode Registry**

```
F-01  Missing discipline          — fewer than 6 stock discipline blocks present in BLOCK 2
F-02  Unseveritied finding        — any finding row contains a Sev value other than P1, P2, or P3
F-03  Expert without signal       — Signal detected cell is empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     — BLOCK 3 is absent from the output
F-05  Full-review amend           — Re-run Scope cell in BLOCK 5 contains "full review"
F-06  Pyramid inverted, silent    — BLOCK 2.5 Status is inverted and no Rationale row is present
F-07  Incomplete expert trace     — Expert added or Reason cell is empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      — BLOCK 4 is absent from the output
F-09  Coverage unverified         — BLOCK 1.5 is absent, or Domain row count in BLOCK 1.5 does not equal BLOCK 1 domain count
F-10  Orphaned domain expert      — a Domain row in BLOCK 1.5 carries a Reviewer name with no matching Expert added value in BLOCK 1
F-11  Split without synthesis     — a SPLIT row in BLOCK 3 has an empty Synthesis column cell
F-12  Amend count mismatch        — BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 — CONTENT SIGNAL CATALOGUE** *(Pre-scan only — no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only — expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | — |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. The catalogue is the canonical signal inventory for this review.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected MUST be populated and MUST trace to BLOCK 0; F-07: Expert added and Reason MUST be populated)*

Drawing exclusively from the BLOCK 0 signal catalogue, one domain expert row SHALL be added per catalogued signal that warrants domain expertise. All three cells in every row MUST be populated.

Stock table (fixed — SHALL NOT be modified):

| Reviewer | Role |
|----------|------|
| Architect | Stock |
| Code-Quality | Stock |
| Documentation | Stock |
| Testing | Stock |
| Process | Stock |
| Implementation | Stock |

Domain expert table:

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|
| [signal phrase from BLOCK 0 catalogue] | [expert title or role] | [one sentence: why this signal warrants this expert] |

A Signal detected cell that is empty or does not match a BLOCK 0 catalogue entry is non-conformant under F-03. An Expert added or Reason cell that is empty is non-conformant under F-07.
If no signals were catalogued in BLOCK 0: a single row `| No signals detected | None | — |` SHALL be present.

After population: the count of domain expert rows (excluding the "No signals detected" row) SHALL be recorded as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 — ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain row count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

The complete reviewer roster MUST be committed before any finding block is generated. Domain experts SHALL appear before stock disciplines. The Source column MUST distinguish `Domain` from `Stock`. Every Domain row MUST carry a Reviewer name that exactly matches an Expert added value from the BLOCK 1 domain expert table — any deviation is non-conformant under F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

One Domain row MUST be added per domain expert from BLOCK 1, positioned above the Stock rows, using the exact Expert added value as the Reviewer name.

Conformance gate — both checks SHALL be resolved before BLOCK 2 begins:
1. The count of Domain rows MUST equal `BLOCK 1 domain count`. F-09 is raised on mismatch.
2. Every Domain row Reviewer name MUST exactly match an Expert added value in BLOCK 1. F-10 is raised on any mismatch.

If no domain experts were added in BLOCK 1: no Domain rows SHALL be present. The table SHALL contain 6 Stock rows only.

---

**BLOCK 2 — PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; domain experts run first)*

A finding table MUST be generated for every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers SHALL run first.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [§section or component] | [one actionable sentence] |

Column conformance requirements:
- `Sev`: SHALL contain exactly one of P1, P2, or P3. Any other value is non-conformant under F-02.
- `Section`: SHALL name a specific section, component, or decision. The values "the design" or "overall" are non-conformant.
- P1 rows: Section MUST be populated.
- P2 rows: Section MUST be populated in >= 50% of P2 rows.
- A reviewer with no findings: a single row `| — | — | No findings. |` MUST be present.

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any reviewer fires F-01. BLOCK 2.5 SHALL NOT begin until all finding tables are present.

---

**BLOCK 2.5 — SEVERITY DISTRIBUTION** *(F-06: an inverted Status MUST be accompanied by a Rationale row; positioned between BLOCK 2 and BLOCK 3)*

All findings from BLOCK 2 SHALL be counted:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

Conformance: P3 >= P2 >= P1?
- YES: all Status cells SHALL read `pyramid nominal`. Proceed to BLOCK 3.
- NO: inverted levels SHALL carry Status `inverted`. A Rationale row MUST be present — F-06 is raised if absent.

| Note | — |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual severity concentration] |

`P1 count = [n from P1 row]` SHALL be recorded. This value is the anchor for the BLOCK 5 conformance gate (F-12).

---

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated)*

Synthesis is a dedicated column. A blank Synthesis cell for any SPLIT row fires F-11. CONSENSUS rows SHALL carry `—` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | — |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension — not a restatement of opposing positions] |

If no consensus: a row `| CONSENSUS | none | — | — |` MUST be present.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Synthesis` for SPLIT rows: MUST name the underlying design tension. A restatement of the opposing positions is non-conformant. An empty Synthesis cell is non-conformant under F-11 — the block SHALL NOT be closed until all SPLIT row Synthesis cells are populated.
- `Synthesis` for CONSENSUS rows: SHALL always be `—`.

BLOCK 3 absence fires F-04 regardless of review content.

---

**BLOCK 4 — UNIQUE CATCHES** *(F-08: MUST be present — absence fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If no unique catches: a row `| UNIQUE | none | — |` MUST be present.
BLOCK 4 absence fires F-08.

---

**BLOCK 5 — AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; table form required)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component — never "full review." Domain expert reviewers are preferred Re-run Scope candidates where their BLOCK 0 signal area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Re-run Scope`: MUST contain reviewer name(s) and section scope. "Full review" is non-conformant under F-05.

Conformance gate before closing: the count of amend rows (excluding the "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised if BLOCK 5 entry count < P1 count — missing entries SHALL be added before the block closes.

If zero P1 findings: a row `| — | — | — | No P1 findings — no amend actions required. |` SHALL be present.
