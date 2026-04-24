Written to `simulations/quest/variations/review-design-variations-R9-2026-03-14.md`.

---

## Round 9 Variations — review-design

### Variation Table

| Var | Axis | New Bet |
|-----|------|---------|
| **V-01** | lifecycle-emphasis | F-19 -- BLOCK 2.5 Rationale cell content completeness |
| **V-02** | output-format | F-20 -- BLOCK 4 unique catches in explicit 3-column table form |
| **V-03** | behavior | F-21 -- No expert needed disposition row reason cell completeness |
| **V-04** | combined lifecycle + output-format | F-19 + F-20 stacked |
| **V-05** | combined max | F-19 + F-20 + F-21 -- R10 extraction source |

---

### Gap analysis

**R8 V-05 left three structural holes, each targeting a distinct enforcement class:**

**Hole 1 — F-19 | BLOCK 2.5 Rationale cell content completeness**
F-06 fires when the Rationale row is absent (row-presence enforcement). If the row is present with an empty cell, nothing fires. C-18/F-11 established the *content-completeness-within-present-structure* enforcement class: present SPLIT row + empty Synthesis fires F-11. F-19 applies the identical pattern at BLOCK 2.5. Axis: **lifecycle-emphasis** — BLOCK 2.5 is a fixed lifecycle position between BLOCK 2 and BLOCK 3; placing the halt here is structurally precise.

**Hole 2 — F-20 | BLOCK 4 explicit table-form halt**
Every other mandatory block now has a table-form criterion: C-10 (BLOCK 2), C-13/C-15 (BLOCK 1/1.5), C-20 (BLOCK 5), C-22 (BLOCK 3). BLOCK 4 uses a 3-column table in the R8 prompt but no named halt fires on prose rendering. The blank-Reviewer-cell argument that motivates F-16 (cell is visible in a table; attribution is hideable in a bullet) applies directly to BLOCK 4's own structural form. F-20 closes this. Axis: **output-format** — the axis is structural form of the block, not its content.

**Hole 3 — F-21 | Disposition row reason cell completeness**
C-26/F-18 requires `No expert needed` disposition rows exist for undisposed BLOCK 0 signals. F-18 fires on a missing row. An empty reason cell in a present row satisfies F-18 while providing no diagnostic value. F-21 fires on an empty reason cell, completing the bidirectional BLOCK 0 ↔ BLOCK 1 contract: F-13 (inbound gate) + F-18 (outbound existence) + F-21 (outbound content). Axis: **behavior** — this is a new behavioral enforcement on a mechanism introduced in a prior round (C-26).

---

### Feature Matrix

| F-ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| F-19 -- BLOCK 2.5 Rationale content | YES | NO | NO | YES | YES |
| F-20 -- BLOCK 4 table form | NO | YES | NO | YES | YES |
| F-21 -- Disposition reason cell content | NO | NO | YES | NO | YES |

---

### Predicted scoring on v8 rubric

All five variations inherit the R8 V-05 baseline (F-01 through F-18), which already passes all 26 criteria C-01 through C-26. The three new F-IDs are additive above v8's ceiling. All variations are expected to score **100** on v8.

**Isolation logic:**
- V-02 and V-03 carry no F-19 → they confirm F-19 is aspirational (C-27 candidate)
- V-01 and V-03 carry no F-20 → they confirm F-20 is aspirational (C-28 candidate)
- V-01 and V-02 carry no F-21 → they confirm F-21 is aspirational (C-29 candidate)

**V-05 is the R10 extraction source** — three new F-IDs, two enforcement classes (content-completeness: F-19/F-21; structural-form: F-20), three distinct lifecycle positions (BLOCK 2.5, BLOCK 4, BLOCK 1), no overlap between them.
m R8 V-05 are unchanged.

A multi-expert design review SHALL be conducted according to the following specification. Each output block MUST conform to its stated requirements. A conformance failure is declared when any halt condition fires; the output SHALL NOT proceed past a failed block until the failure is resolved.

**Failure Mode Registry**

```
F-01  Missing discipline          -- fewer than 6 stock discipline blocks present in BLOCK 2
F-02  Unseveritied finding        -- any finding row contains a Sev value other than P1, P2, or P3
F-03  Expert without signal       -- Signal detected cell is empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     -- BLOCK 3 is absent from the output
F-05  Full-review amend           -- Re-run Scope cell in BLOCK 5 contains "full review"
F-06  Pyramid inverted, silent    -- BLOCK 2.5 Status is inverted and no Rationale row is present
F-07  Incomplete expert trace     -- Expert added or Reason cell is empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      -- BLOCK 4 is absent from the output
F-09  Coverage unverified         -- BLOCK 1.5 is absent, or Domain row count in BLOCK 1.5 does not equal BLOCK 1 domain count
F-10  Orphaned domain expert      -- a Domain row in BLOCK 1.5 carries a Reviewer name with no matching Expert added value in BLOCK 1
F-11  Split without synthesis     -- a SPLIT row in BLOCK 3 has an empty Synthesis column cell
F-12  Amend count mismatch        -- BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
F-13  Uncatalogued signal         -- a Signal detected value in BLOCK 1 has no matching Signal phrase entry in the BLOCK 0 catalogue
F-14  Invalid consensus type      -- BLOCK 3 contains a Type cell whose value is neither AGREE nor SPLIT
F-15  Phantom reviewer            -- BLOCK 3 Reviewers column contains a name that has no matching Reviewer value in BLOCK 1.5
F-16  Phantom catcher             -- BLOCK 4 Reviewer cell contains a name that has no matching Reviewer value in BLOCK 1.5
F-17  Phantom re-run target       -- Re-run Scope cell in BLOCK 5 names a reviewer with no matching Reviewer value in BLOCK 1.5
F-18  Undisposed signal           -- a BLOCK 0 signal row has no corresponding Signal detected row in BLOCK 1 domain expert table and no No expert needed disposition row
F-19  Empty rationale             -- BLOCK 2.5 Rationale cell is present but empty when any Status cell reads inverted
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 -- CONTENT SIGNAL CATALOGUE** *(Pre-scan only -- no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only -- expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | -- |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation -- the violating row SHALL NOT be accepted until a matching Signal phrase is added to this catalogue and verified. The catalogue is the canonical signal inventory for this review; the block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry; F-18: every BLOCK 0 signal MUST be resolved as an expert selection or a disposition row)*

Drawing exclusively from the BLOCK 0 signal catalogue, one domain expert row SHALL be added per catalogued signal that warrants domain expertise. All three cells in every row MUST be populated.

Stock table (fixed -- SHALL NOT be modified):

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

A Signal detected cell that is empty is non-conformant under F-03. A Signal detected value that does not match any Signal phrase in BLOCK 0 is non-conformant under F-13 -- the row SHALL NOT be accepted until the Signal phrase appears in the BLOCK 0 catalogue. An Expert added or Reason cell that is empty is non-conformant under F-07.

If no signals were catalogued in BLOCK 0: a single row `| No signals detected | None | -- |` SHALL be present.

Signal disposition gate (F-18): for every Signal phrase row in BLOCK 0 that is not `No domain signals detected`, one of the following conditions MUST hold before BLOCK 1 closes:
1. A domain expert row exists in the domain expert table with a matching Signal detected value, OR
2. A disposition row is present in the domain expert table: `| [Signal phrase] | No expert needed | [reason: one sentence explaining why no expert is warranted] |`

A BLOCK 0 signal with neither a domain expert row nor a disposition row is non-conformant under F-18 -- the block SHALL NOT be closed until all BLOCK 0 signals are resolved. F-13 is the inbound gate (BLOCK 1 references MUST exist in BLOCK 0); F-18 is the outbound gate (BLOCK 0 entries MUST be resolved in BLOCK 1). Together they form a bidirectional BLOCK 0 <-> BLOCK 1 integrity contract.

After population: the count of domain expert rows (excluding "No signals detected" and disposition rows) SHALL be recorded as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 -- ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain row count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

The complete reviewer roster MUST be committed before any finding block is generated. Domain experts SHALL appear before stock disciplines. The Source column MUST distinguish `Domain` from `Stock`. Every Domain row MUST carry a Reviewer name that exactly matches an Expert added value from the BLOCK 1 domain expert table -- any deviation is non-conformant under F-10.

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

Conformance gate -- both checks SHALL be resolved before BLOCK 2 begins:
1. The count of Domain rows MUST equal `BLOCK 1 domain count`. F-09 is raised on mismatch.
2. Every Domain row Reviewer name MUST exactly match an Expert added value in BLOCK 1. F-10 is raised on any mismatch.

If no domain experts were added in BLOCK 1: no Domain rows SHALL be present. The table SHALL contain 6 Stock rows only.

---

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; domain experts run first)*

A finding table MUST be generated for every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers SHALL run first.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [section or component] | [one actionable sentence] |

Column conformance requirements:
- `Sev`: SHALL contain exactly one of P1, P2, or P3. Any other value is non-conformant under F-02.
- `Section`: SHALL name a specific section, component, or decision. The values "the design" or "overall" are non-conformant.
- P1 rows: Section MUST be populated.
- P2 rows: Section MUST be populated in >= 50% of P2 rows.
- A reviewer with no findings: a single row `| -- | -- | No findings. |` MUST be present.

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any reviewer fires F-01. BLOCK 2.5 SHALL NOT begin until all finding tables are present.

---

**BLOCK 2.5 -- SEVERITY DISTRIBUTION** *(F-06: an inverted Status MUST be accompanied by a Rationale row; F-19: Rationale cell MUST be populated when present; positioned between BLOCK 2 and BLOCK 3)*

All findings from BLOCK 2 SHALL be counted:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

Conformance: P3 >= P2 >= P1?
- YES: all Status cells SHALL read `pyramid nominal`. Proceed to BLOCK 3.
- NO: inverted levels SHALL carry Status `inverted`. A Rationale row MUST be present -- F-06 is raised if absent.

| Note | -- |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual severity concentration] |

A Rationale cell that is present but empty is non-conformant under F-19 -- the block SHALL NOT be closed until the Rationale cell contains a specific design area and risk type explanation. F-06 fires on a missing row; F-19 fires on a present row with an empty cell. Both conditions MUST be resolved before BLOCK 3 begins.

`P1 count = [n from P1 row]` SHALL be recorded. This value is the anchor for the BLOCK 5 conformance gate (F-12).

---

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type cell MUST be AGREE or SPLIT; F-15: Reviewers names MUST match BLOCK 1.5)*

Synthesis is a dedicated column. A blank Synthesis cell for any SPLIT row fires F-11. CONSENSUS rows SHALL carry `--` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension -- not a restatement of opposing positions] |

If no consensus: a row `| CONSENSUS | none | -- | -- |` MUST be present.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: SHALL contain exactly AGREE or SPLIT. Any other value is non-conformant under F-14 -- the row SHALL NOT be accepted until the Type cell is corrected.
- `Reviewers`: every reviewer name in this column MUST appear in the BLOCK 1.5 Reviewer column. For AGREE rows, each comma-separated name MUST be in BLOCK 1.5. For SPLIT rows, both reviewer names MUST be in BLOCK 1.5. A name absent from BLOCK 1.5 is non-conformant under F-15 -- the row SHALL NOT be accepted until all reviewer names are verified against BLOCK 1.5.
- `Synthesis` for SPLIT rows: MUST name the underlying design tension. A restatement of the opposing positions is non-conformant. An empty Synthesis cell is non-conformant under F-11 -- the block SHALL NOT be closed until all SPLIT row Synthesis cells are populated.
- `Synthesis` for CONSENSUS rows: SHALL always be `--`.

BLOCK 3 absence fires F-04. F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside {AGREE, SPLIT}. F-15 fires on any Reviewers cell containing a name absent from BLOCK 1.5.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present -- absence fires F-08 even when catches are empty; F-16: Reviewer MUST match BLOCK 1.5)*

One row SHALL be present per finding raised by exactly one reviewer and not raised by any other. The Reviewer cell MUST contain a name that exactly matches a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-16.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: a row `| UNIQUE | none | -- |` MUST be present. The `none` token is exempt from the F-16 identity check.
BLOCK 4 absence fires F-08. A Reviewer cell containing a name with no matching Reviewer in BLOCK 1.5 is non-conformant under F-16 -- the row SHALL NOT be accepted until the name is corrected to an exact BLOCK 1.5 match.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; table form required)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review." Domain expert reviewers are preferred Re-run Scope candidates where their BLOCK 0 signal area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Re-run Scope`: MUST contain reviewer name(s) and section scope. "Full review" is non-conformant under F-05. Every reviewer name in the Re-run Scope cell MUST exactly match a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-17. The row SHALL NOT be accepted until all Re-run Scope reviewer names are verified against BLOCK 1.5.

Conformance gate before closing: the count of amend rows (excluding the "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised if BLOCK 5 entry count < P1 count -- missing entries SHALL be added before the block closes.

If zero P1 findings: a row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.

---

## V-02 | Output-Format -- F-20: BLOCK 4 Unique Catches in Explicit 3-Column Table Form
**Axis**: output-format
**Hypothesis**: BLOCK 4 is the only mandatory output block whose table form is implicit in the prompt structure but not enforced by a named halt condition. C-10 closed the analogous gap at BLOCK 2; C-22 at BLOCK 3; C-20 at BLOCK 5; C-15 at BLOCK 1.5; C-13 at BLOCK 1. A prose-only BLOCK 4 output (e.g., bullet list of unique catches with reviewer attribution) satisfies C-05 and F-08 while providing no structural detectability for F-16: a blank Reviewer cell in a table is visually obvious; a missing reviewer label in a bullet is not. F-20 closes this by explicitly requiring 3-column table form and naming a halt for non-table output. Tests whether structural form at BLOCK 4 is independently detectable from content requirements (C-05, F-08, F-16). V-01/V-03 will score 100 without F-20, confirming aspirational. All F-01 through F-18 from R8 V-05 are unchanged.

A multi-expert design review SHALL be conducted according to the following specification. Each output block MUST conform to its stated requirements. A conformance failure is declared when any halt condition fires; the output SHALL NOT proceed past a failed block until the failure is resolved.

**Failure Mode Registry**

```
F-01  Missing discipline          -- fewer than 6 stock discipline blocks present in BLOCK 2
F-02  Unseveritied finding        -- any finding row contains a Sev value other than P1, P2, or P3
F-03  Expert without signal       -- Signal detected cell is empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     -- BLOCK 3 is absent from the output
F-05  Full-review amend           -- Re-run Scope cell in BLOCK 5 contains "full review"
F-06  Pyramid inverted, silent    -- BLOCK 2.5 Status is inverted and no Rationale row is present
F-07  Incomplete expert trace     -- Expert added or Reason cell is empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      -- BLOCK 4 is absent from the output
F-09  Coverage unverified         -- BLOCK 1.5 is absent, or Domain row count in BLOCK 1.5 does not equal BLOCK 1 domain count
F-10  Orphaned domain expert      -- a Domain row in BLOCK 1.5 carries a Reviewer name with no matching Expert added value in BLOCK 1
F-11  Split without synthesis     -- a SPLIT row in BLOCK 3 has an empty Synthesis column cell
F-12  Amend count mismatch        -- BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
F-13  Uncatalogued signal         -- a Signal detected value in BLOCK 1 has no matching Signal phrase entry in the BLOCK 0 catalogue
F-14  Invalid consensus type      -- BLOCK 3 contains a Type cell whose value is neither AGREE nor SPLIT
F-15  Phantom reviewer            -- BLOCK 3 Reviewers column contains a name that has no matching Reviewer value in BLOCK 1.5
F-16  Phantom catcher             -- BLOCK 4 Reviewer cell contains a name that has no matching Reviewer value in BLOCK 1.5
F-17  Phantom re-run target       -- Re-run Scope cell in BLOCK 5 names a reviewer with no matching Reviewer value in BLOCK 1.5
F-18  Undisposed signal           -- a BLOCK 0 signal row has no corresponding Signal detected row in BLOCK 1 domain expert table and no No expert needed disposition row
F-20  Prose unique catches        -- BLOCK 4 output is not in the required 3-column table form (Type, Reviewer, Finding)
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 -- CONTENT SIGNAL CATALOGUE** *(Pre-scan only -- no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only -- expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | -- |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation -- the violating row SHALL NOT be accepted until a matching Signal phrase is added to this catalogue and verified. The catalogue is the canonical signal inventory for this review; the block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry; F-18: every BLOCK 0 signal MUST be resolved as an expert selection or a disposition row)*

Drawing exclusively from the BLOCK 0 signal catalogue, one domain expert row SHALL be added per catalogued signal that warrants domain expertise. All three cells in every row MUST be populated.

Stock table (fixed -- SHALL NOT be modified):

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

A Signal detected cell that is empty is non-conformant under F-03. A Signal detected value that does not match any Signal phrase in BLOCK 0 is non-conformant under F-13 -- the row SHALL NOT be accepted until the Signal phrase appears in the BLOCK 0 catalogue. An Expert added or Reason cell that is empty is non-conformant under F-07.

If no signals were catalogued in BLOCK 0: a single row `| No signals detected | None | -- |` SHALL be present.

Signal disposition gate (F-18): for every Signal phrase row in BLOCK 0 that is not `No domain signals detected`, one of the following conditions MUST hold before BLOCK 1 closes:
1. A domain expert row exists in the domain expert table with a matching Signal detected value, OR
2. A disposition row is present in the domain expert table: `| [Signal phrase] | No expert needed | [reason: one sentence explaining why no expert is warranted] |`

A BLOCK 0 signal with neither a domain expert row nor a disposition row is non-conformant under F-18 -- the block SHALL NOT be closed until all BLOCK 0 signals are resolved. F-13 is the inbound gate (BLOCK 1 references MUST exist in BLOCK 0); F-18 is the outbound gate (BLOCK 0 entries MUST be resolved in BLOCK 1). Together they form a bidirectional BLOCK 0 <-> BLOCK 1 integrity contract.

After population: the count of domain expert rows (excluding "No signals detected" and disposition rows) SHALL be recorded as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 -- ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain row count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

The complete reviewer roster MUST be committed before any finding block is generated. Domain experts SHALL appear before stock disciplines. The Source column MUST distinguish `Domain` from `Stock`. Every Domain row MUST carry a Reviewer name that exactly matches an Expert added value from the BLOCK 1 domain expert table -- any deviation is non-conformant under F-10.

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

Conformance gate -- both checks SHALL be resolved before BLOCK 2 begins:
1. The count of Domain rows MUST equal `BLOCK 1 domain count`. F-09 is raised on mismatch.
2. Every Domain row Reviewer name MUST exactly match an Expert added value in BLOCK 1. F-10 is raised on any mismatch.

If no domain experts were added in BLOCK 1: no Domain rows SHALL be present. The table SHALL contain 6 Stock rows only.

---

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; domain experts run first)*

A finding table MUST be generated for every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers SHALL run first.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [section or component] | [one actionable sentence] |

Column conformance requirements:
- `Sev`: SHALL contain exactly one of P1, P2, or P3. Any other value is non-conformant under F-02.
- `Section`: SHALL name a specific section, component, or decision. The values "the design" or "overall" are non-conformant.
- P1 rows: Section MUST be populated.
- P2 rows: Section MUST be populated in >= 50% of P2 rows.
- A reviewer with no findings: a single row `| -- | -- | No findings. |` MUST be present.

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any reviewer fires F-01. BLOCK 2.5 SHALL NOT begin until all finding tables are present.

---

**BLOCK 2.5 -- SEVERITY DISTRIBUTION** *(F-06: an inverted Status MUST be accompanied by a Rationale row; positioned between BLOCK 2 and BLOCK 3)*

All findings from BLOCK 2 SHALL be counted:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

Conformance: P3 >= P2 >= P1?
- YES: all Status cells SHALL read `pyramid nominal`. Proceed to BLOCK 3.
- NO: inverted levels SHALL carry Status `inverted`. A Rationale row MUST be present -- F-06 is raised if absent.

| Note | -- |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual severity concentration] |

`P1 count = [n from P1 row]` SHALL be recorded. This value is the anchor for the BLOCK 5 conformance gate (F-12).

---

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type cell MUST be AGREE or SPLIT; F-15: Reviewers names MUST match BLOCK 1.5)*

Synthesis is a dedicated column. A blank Synthesis cell for any SPLIT row fires F-11. CONSENSUS rows SHALL carry `--` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension -- not a restatement of opposing positions] |

If no consensus: a row `| CONSENSUS | none | -- | -- |` MUST be present.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: SHALL contain exactly AGREE or SPLIT. Any other value is non-conformant under F-14 -- the row SHALL NOT be accepted until the Type cell is corrected.
- `Reviewers`: every reviewer name in this column MUST appear in the BLOCK 1.5 Reviewer column. For AGREE rows, each comma-separated name MUST be in BLOCK 1.5. For SPLIT rows, both reviewer names MUST be in BLOCK 1.5. A name absent from BLOCK 1.5 is non-conformant under F-15 -- the row SHALL NOT be accepted until all reviewer names are verified against BLOCK 1.5.
- `Synthesis` for SPLIT rows: MUST name the underlying design tension. A restatement of the opposing positions is non-conformant. An empty Synthesis cell is non-conformant under F-11 -- the block SHALL NOT be closed until all SPLIT row Synthesis cells are populated.
- `Synthesis` for CONSENSUS rows: SHALL always be `--`.

BLOCK 3 absence fires F-04. F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside {AGREE, SPLIT}. F-15 fires on any Reviewers cell containing a name absent from BLOCK 1.5.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present -- absence fires F-08 even when catches are empty; F-16: Reviewer MUST match BLOCK 1.5; F-20: output MUST be in 3-column table form)*

One row SHALL be present per finding raised by exactly one reviewer and not raised by any other. BLOCK 4 output MUST use the following 3-column table structure -- prose-only output (e.g., bullet list with reviewer attribution) is non-conformant under F-20 regardless of content correctness. The Reviewer cell MUST contain a name that exactly matches a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-16.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: a row `| UNIQUE | none | -- |` MUST be present. The `none` token is exempt from the F-16 identity check.
BLOCK 4 absence fires F-08. A non-table rendering of BLOCK 4 content is non-conformant under F-20 -- the block SHALL NOT be accepted until the 3-column table form is present. A Reviewer cell containing a name with no matching Reviewer in BLOCK 1.5 is non-conformant under F-16 -- the row SHALL NOT be accepted until the name is corrected to an exact BLOCK 1.5 match.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; table form required)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review." Domain expert reviewers are preferred Re-run Scope candidates where their BLOCK 0 signal area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Re-run Scope`: MUST contain reviewer name(s) and section scope. "Full review" is non-conformant under F-05. Every reviewer name in the Re-run Scope cell MUST exactly match a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-17. The row SHALL NOT be accepted until all Re-run Scope reviewer names are verified against BLOCK 1.5.

Conformance gate before closing: the count of amend rows (excluding the "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised if BLOCK 5 entry count < P1 count -- missing entries SHALL be added before the block closes.

If zero P1 findings: a row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.

---

## V-03 | Behavior -- F-21: No Expert Needed Disposition Row Reason Cell Completeness
**Axis**: behavior
**Hypothesis**: C-26 (F-18) requires that every undisposed BLOCK 0 signal carry a `No expert needed` disposition row. The disposition row form is `| [Signal phrase] | No expert needed | [reason] |`. F-18 fires on a missing row but not on a row with an empty reason cell. This is the same structural gap that F-11 closed for SPLIT Synthesis and that F-19 (V-01) closes for BLOCK 2.5 Rationale: row presence is enforced but cell content within a present row is not. F-21 completes the content-completeness coverage of the F-18 bidirectional BLOCK 0 <-> BLOCK 1 contract: F-18 ensures every BLOCK 0 signal is resolved (row presence); F-21 ensures the resolution is substantively stated (cell content). Tests whether disposition row content completeness is independently detectable from row existence. V-01/V-02 will score 100 without F-21, confirming aspirational. All F-01 through F-18 from R8 V-05 are unchanged.

A multi-expert design review SHALL be conducted according to the following specification. Each output block MUST conform to its stated requirements. A conformance failure is declared when any halt condition fires; the output SHALL NOT proceed past a failed block until the failure is resolved.

**Failure Mode Registry**

```
F-01  Missing discipline          -- fewer than 6 stock discipline blocks present in BLOCK 2
F-02  Unseveritied finding        -- any finding row contains a Sev value other than P1, P2, or P3
F-03  Expert without signal       -- Signal detected cell is empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     -- BLOCK 3 is absent from the output
F-05  Full-review amend           -- Re-run Scope cell in BLOCK 5 contains "full review"
F-06  Pyramid inverted, silent    -- BLOCK 2.5 Status is inverted and no Rationale row is present
F-07  Incomplete expert trace     -- Expert added or Reason cell is empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      -- BLOCK 4 is absent from the output
F-09  Coverage unverified         -- BLOCK 1.5 is absent, or Domain row count in BLOCK 1.5 does not equal BLOCK 1 domain count
F-10  Orphaned domain expert      -- a Domain row in BLOCK 1.5 carries a Reviewer name with no matching Expert added value in BLOCK 1
F-11  Split without synthesis     -- a SPLIT row in BLOCK 3 has an empty Synthesis column cell
F-12  Amend count mismatch        -- BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
F-13  Uncatalogued signal         -- a Signal detected value in BLOCK 1 has no matching Signal phrase entry in the BLOCK 0 catalogue
F-14  Invalid consensus type      -- BLOCK 3 contains a Type cell whose value is neither AGREE nor SPLIT
F-15  Phantom reviewer            -- BLOCK 3 Reviewers column contains a name that has no matching Reviewer value in BLOCK 1.5
F-16  Phantom catcher             -- BLOCK 4 Reviewer cell contains a name that has no matching Reviewer value in BLOCK 1.5
F-17  Phantom re-run target       -- Re-run Scope cell in BLOCK 5 names a reviewer with no matching Reviewer value in BLOCK 1.5
F-18  Undisposed signal           -- a BLOCK 0 signal row has no corresponding Signal detected row in BLOCK 1 domain expert table and no No expert needed disposition row
F-21  Empty disposition reason    -- reason cell of a No expert needed disposition row is empty
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 -- CONTENT SIGNAL CATALOGUE** *(Pre-scan only -- no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only -- expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | -- |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation -- the violating row SHALL NOT be accepted until a matching Signal phrase is added to this catalogue and verified. The catalogue is the canonical signal inventory for this review; the block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry; F-18: every BLOCK 0 signal MUST be resolved as an expert selection or a disposition row; F-21: disposition row reason cell MUST be populated)*

Drawing exclusively from the BLOCK 0 signal catalogue, one domain expert row SHALL be added per catalogued signal that warrants domain expertise. All three cells in every row MUST be populated.

Stock table (fixed -- SHALL NOT be modified):

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

A Signal detected cell that is empty is non-conformant under F-03. A Signal detected value that does not match any Signal phrase in BLOCK 0 is non-conformant under F-13 -- the row SHALL NOT be accepted until the Signal phrase appears in the BLOCK 0 catalogue. An Expert added or Reason cell that is empty is non-conformant under F-07.

If no signals were catalogued in BLOCK 0: a single row `| No signals detected | None | -- |` SHALL be present.

Signal disposition gate (F-18 + F-21): for every Signal phrase row in BLOCK 0 that is not `No domain signals detected`, one of the following conditions MUST hold before BLOCK 1 closes:
1. A domain expert row exists in the domain expert table with a matching Signal detected value, OR
2. A disposition row is present in the domain expert table: `| [Signal phrase] | No expert needed | [reason: one sentence explaining why no expert is warranted] |`

A BLOCK 0 signal with neither a domain expert row nor a disposition row is non-conformant under F-18 -- the block SHALL NOT be closed until all BLOCK 0 signals are resolved. A disposition row whose third cell (reason) is empty is non-conformant under F-21 -- the row SHALL NOT be accepted until the reason cell contains a specific explanation. F-18 enforces row existence; F-21 enforces reason cell content within a present row. Both conditions MUST be satisfied before BLOCK 1 closes.

F-13 is the inbound gate (BLOCK 1 references MUST exist in BLOCK 0); F-18 is the outbound existence gate (BLOCK 0 entries MUST be resolved in BLOCK 1); F-21 is the outbound content gate (disposition row reason cells MUST be substantively populated). Together they form the complete bidirectional BLOCK 0 <-> BLOCK 1 integrity contract.

After population: the count of domain expert rows (excluding "No signals detected" and disposition rows) SHALL be recorded as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 -- ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain row count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

The complete reviewer roster MUST be committed before any finding block is generated. Domain experts SHALL appear before stock disciplines. The Source column MUST distinguish `Domain` from `Stock`. Every Domain row MUST carry a Reviewer name that exactly matches an Expert added value from the BLOCK 1 domain expert table -- any deviation is non-conformant under F-10.

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

Conformance gate -- both checks SHALL be resolved before BLOCK 2 begins:
1. The count of Domain rows MUST equal `BLOCK 1 domain count`. F-09 is raised on mismatch.
2. Every Domain row Reviewer name MUST exactly match an Expert added value in BLOCK 1. F-10 is raised on any mismatch.

If no domain experts were added in BLOCK 1: no Domain rows SHALL be present. The table SHALL contain 6 Stock rows only.

---

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; domain experts run first)*

A finding table MUST be generated for every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers SHALL run first.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [section or component] | [one actionable sentence] |

Column conformance requirements:
- `Sev`: SHALL contain exactly one of P1, P2, or P3. Any other value is non-conformant under F-02.
- `Section`: SHALL name a specific section, component, or decision. The values "the design" or "overall" are non-conformant.
- P1 rows: Section MUST be populated.
- P2 rows: Section MUST be populated in >= 50% of P2 rows.
- A reviewer with no findings: a single row `| -- | -- | No findings. |` MUST be present.

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any reviewer fires F-01. BLOCK 2.5 SHALL NOT begin until all finding tables are present.

---

**BLOCK 2.5 -- SEVERITY DISTRIBUTION** *(F-06: an inverted Status MUST be accompanied by a Rationale row; positioned between BLOCK 2 and BLOCK 3)*

All findings from BLOCK 2 SHALL be counted:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

Conformance: P3 >= P2 >= P1?
- YES: all Status cells SHALL read `pyramid nominal`. Proceed to BLOCK 3.
- NO: inverted levels SHALL carry Status `inverted`. A Rationale row MUST be present -- F-06 is raised if absent.

| Note | -- |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual severity concentration] |

`P1 count = [n from P1 row]` SHALL be recorded. This value is the anchor for the BLOCK 5 conformance gate (F-12).

---

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type cell MUST be AGREE or SPLIT; F-15: Reviewers names MUST match BLOCK 1.5)*

Synthesis is a dedicated column. A blank Synthesis cell for any SPLIT row fires F-11. CONSENSUS rows SHALL carry `--` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension -- not a restatement of opposing positions] |

If no consensus: a row `| CONSENSUS | none | -- | -- |` MUST be present.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: SHALL contain exactly AGREE or SPLIT. Any other value is non-conformant under F-14 -- the row SHALL NOT be accepted until the Type cell is corrected.
- `Reviewers`: every reviewer name in this column MUST appear in the BLOCK 1.5 Reviewer column. For AGREE rows, each comma-separated name MUST be in BLOCK 1.5. For SPLIT rows, both reviewer names MUST be in BLOCK 1.5. A name absent from BLOCK 1.5 is non-conformant under F-15 -- the row SHALL NOT be accepted until all reviewer names are verified against BLOCK 1.5.
- `Synthesis` for SPLIT rows: MUST name the underlying design tension. A restatement of the opposing positions is non-conformant. An empty Synthesis cell is non-conformant under F-11 -- the block SHALL NOT be closed until all SPLIT row Synthesis cells are populated.
- `Synthesis` for CONSENSUS rows: SHALL always be `--`.

BLOCK 3 absence fires F-04. F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside {AGREE, SPLIT}. F-15 fires on any Reviewers cell containing a name absent from BLOCK 1.5.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present -- absence fires F-08 even when catches are empty; F-16: Reviewer MUST match BLOCK 1.5)*

One row SHALL be present per finding raised by exactly one reviewer and not raised by any other. The Reviewer cell MUST contain a name that exactly matches a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-16.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: a row `| UNIQUE | none | -- |` MUST be present. The `none` token is exempt from the F-16 identity check.
BLOCK 4 absence fires F-08. A Reviewer cell containing a name with no matching Reviewer in BLOCK 1.5 is non-conformant under F-16 -- the row SHALL NOT be accepted until the name is corrected to an exact BLOCK 1.5 match.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; table form required)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review." Domain expert reviewers are preferred Re-run Scope candidates where their BLOCK 0 signal area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Re-run Scope`: MUST contain reviewer name(s) and section scope. "Full review" is non-conformant under F-05. Every reviewer name in the Re-run Scope cell MUST exactly match a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-17. The row SHALL NOT be accepted until all Re-run Scope reviewer names are verified against BLOCK 1.5.

Conformance gate before closing: the count of amend rows (excluding the "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised if BLOCK 5 entry count < P1 count -- missing entries SHALL be added before the block closes.

If zero P1 findings: a row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.

---

## V-04 | Combined (Lifecycle + Output-Format) -- F-19 + F-20: Rationale Content + BLOCK 4 Table Form
**Axis**: combined (lifecycle-emphasis + output-format)
**Hypothesis**: Combines V-01's F-19 (BLOCK 2.5 Rationale cell content completeness) with V-02's F-20 (BLOCK 4 unique catches explicit table form). F-19 targets a content-completeness gap at BLOCK 2.5 -- a present Rationale row with an empty cell. F-20 targets a structural form gap at BLOCK 4 -- prose output where a table is required. These are at distinct lifecycle positions (BLOCK 2.5 vs BLOCK 4) and represent distinct failure classes (content completeness vs structural form). Tests whether F-19 and F-20 are additive without interference. V-03 will score 100 without either, confirming both remain aspirational. All F-01 through F-18 from R8 V-05 are unchanged.

A multi-expert design review SHALL be conducted according to the following specification. Each output block MUST conform to its stated requirements. A conformance failure is declared when any halt condition fires; the output SHALL NOT proceed past a failed block until the failure is resolved.

**Failure Mode Registry**

```
F-01  Missing discipline          -- fewer than 6 stock discipline blocks present in BLOCK 2
F-02  Unseveritied finding        -- any finding row contains a Sev value other than P1, P2, or P3
F-03  Expert without signal       -- Signal detected cell is empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     -- BLOCK 3 is absent from the output
F-05  Full-review amend           -- Re-run Scope cell in BLOCK 5 contains "full review"
F-06  Pyramid inverted, silent    -- BLOCK 2.5 Status is inverted and no Rationale row is present
F-07  Incomplete expert trace     -- Expert added or Reason cell is empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      -- BLOCK 4 is absent from the output
F-09  Coverage unverified         -- BLOCK 1.5 is absent, or Domain row count in BLOCK 1.5 does not equal BLOCK 1 domain count
F-10  Orphaned domain expert      -- a Domain row in BLOCK 1.5 carries a Reviewer name with no matching Expert added value in BLOCK 1
F-11  Split without synthesis     -- a SPLIT row in BLOCK 3 has an empty Synthesis column cell
F-12  Amend count mismatch        -- BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
F-13  Uncatalogued signal         -- a Signal detected value in BLOCK 1 has no matching Signal phrase entry in the BLOCK 0 catalogue
F-14  Invalid consensus type      -- BLOCK 3 contains a Type cell whose value is neither AGREE nor SPLIT
F-15  Phantom reviewer            -- BLOCK 3 Reviewers column contains a name that has no matching Reviewer value in BLOCK 1.5
F-16  Phantom catcher             -- BLOCK 4 Reviewer cell contains a name that has no matching Reviewer value in BLOCK 1.5
F-17  Phantom re-run target       -- Re-run Scope cell in BLOCK 5 names a reviewer with no matching Reviewer value in BLOCK 1.5
F-18  Undisposed signal           -- a BLOCK 0 signal row has no corresponding Signal detected row in BLOCK 1 domain expert table and no No expert needed disposition row
F-19  Empty rationale             -- BLOCK 2.5 Rationale cell is present but empty when any Status cell reads inverted
F-20  Prose unique catches        -- BLOCK 4 output is not in the required 3-column table form (Type, Reviewer, Finding)
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 -- CONTENT SIGNAL CATALOGUE** *(Pre-scan only -- no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only -- expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | -- |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation -- the violating row SHALL NOT be accepted until a matching Signal phrase is added to this catalogue and verified. The catalogue is the canonical signal inventory for this review; the block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry; F-18: every BLOCK 0 signal MUST be resolved as an expert selection or a disposition row)*

Drawing exclusively from the BLOCK 0 signal catalogue, one domain expert row SHALL be added per catalogued signal that warrants domain expertise. All three cells in every row MUST be populated.

Stock table (fixed -- SHALL NOT be modified):

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

A Signal detected cell that is empty is non-conformant under F-03. A Signal detected value that does not match any Signal phrase in BLOCK 0 is non-conformant under F-13 -- the row SHALL NOT be accepted until the Signal phrase appears in the BLOCK 0 catalogue. An Expert added or Reason cell that is empty is non-conformant under F-07.

If no signals were catalogued in BLOCK 0: a single row `| No signals detected | None | -- |` SHALL be present.

Signal disposition gate (F-18): for every Signal phrase row in BLOCK 0 that is not `No domain signals detected`, one of the following conditions MUST hold before BLOCK 1 closes:
1. A domain expert row exists in the domain expert table with a matching Signal detected value, OR
2. A disposition row is present in the domain expert table: `| [Signal phrase] | No expert needed | [reason: one sentence explaining why no expert is warranted] |`

A BLOCK 0 signal with neither a domain expert row nor a disposition row is non-conformant under F-18 -- the block SHALL NOT be closed until all BLOCK 0 signals are resolved. F-13 is the inbound gate (BLOCK 1 references MUST exist in BLOCK 0); F-18 is the outbound gate (BLOCK 0 entries MUST be resolved in BLOCK 1). Together they form a bidirectional BLOCK 0 <-> BLOCK 1 integrity contract.

After population: the count of domain expert rows (excluding "No signals detected" and disposition rows) SHALL be recorded as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 -- ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain row count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

The complete reviewer roster MUST be committed before any finding block is generated. Domain experts SHALL appear before stock disciplines. The Source column MUST distinguish `Domain` from `Stock`. Every Domain row MUST carry a Reviewer name that exactly matches an Expert added value from the BLOCK 1 domain expert table -- any deviation is non-conformant under F-10.

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

Conformance gate -- both checks SHALL be resolved before BLOCK 2 begins:
1. The count of Domain rows MUST equal `BLOCK 1 domain count`. F-09 is raised on mismatch.
2. Every Domain row Reviewer name MUST exactly match an Expert added value in BLOCK 1. F-10 is raised on any mismatch.

If no domain experts were added in BLOCK 1: no Domain rows SHALL be present. The table SHALL contain 6 Stock rows only.

---

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; domain experts run first)*

A finding table MUST be generated for every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers SHALL run first.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [section or component] | [one actionable sentence] |

Column conformance requirements:
- `Sev`: SHALL contain exactly one of P1, P2, or P3. Any other value is non-conformant under F-02.
- `Section`: SHALL name a specific section, component, or decision. The values "the design" or "overall" are non-conformant.
- P1 rows: Section MUST be populated.
- P2 rows: Section MUST be populated in >= 50% of P2 rows.
- A reviewer with no findings: a single row `| -- | -- | No findings. |` MUST be present.

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any reviewer fires F-01. BLOCK 2.5 SHALL NOT begin until all finding tables are present.

---

**BLOCK 2.5 -- SEVERITY DISTRIBUTION** *(F-06: an inverted Status MUST be accompanied by a Rationale row; F-19: Rationale cell MUST be populated when present; positioned between BLOCK 2 and BLOCK 3)*

All findings from BLOCK 2 SHALL be counted:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

Conformance: P3 >= P2 >= P1?
- YES: all Status cells SHALL read `pyramid nominal`. Proceed to BLOCK 3.
- NO: inverted levels SHALL carry Status `inverted`. A Rationale row MUST be present -- F-06 is raised if absent.

| Note | -- |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual severity concentration] |

A Rationale cell that is present but empty is non-conformant under F-19 -- the block SHALL NOT be closed until the Rationale cell contains a specific design area and risk type explanation. F-06 fires on a missing row; F-19 fires on a present row with an empty cell. Both conditions MUST be resolved before BLOCK 3 begins.

`P1 count = [n from P1 row]` SHALL be recorded. This value is the anchor for the BLOCK 5 conformance gate (F-12).

---

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type cell MUST be AGREE or SPLIT; F-15: Reviewers names MUST match BLOCK 1.5)*

Synthesis is a dedicated column. A blank Synthesis cell for any SPLIT row fires F-11. CONSENSUS rows SHALL carry `--` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension -- not a restatement of opposing positions] |

If no consensus: a row `| CONSENSUS | none | -- | -- |` MUST be present.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: SHALL contain exactly AGREE or SPLIT. Any other value is non-conformant under F-14 -- the row SHALL NOT be accepted until the Type cell is corrected.
- `Reviewers`: every reviewer name in this column MUST appear in the BLOCK 1.5 Reviewer column. For AGREE rows, each comma-separated name MUST be in BLOCK 1.5. For SPLIT rows, both reviewer names MUST be in BLOCK 1.5. A name absent from BLOCK 1.5 is non-conformant under F-15 -- the row SHALL NOT be accepted until all reviewer names are verified against BLOCK 1.5.
- `Synthesis` for SPLIT rows: MUST name the underlying design tension. A restatement of the opposing positions is non-conformant. An empty Synthesis cell is non-conformant under F-11 -- the block SHALL NOT be closed until all SPLIT row Synthesis cells are populated.
- `Synthesis` for CONSENSUS rows: SHALL always be `--`.

BLOCK 3 absence fires F-04. F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside {AGREE, SPLIT}. F-15 fires on any Reviewers cell containing a name absent from BLOCK 1.5.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present -- absence fires F-08 even when catches are empty; F-16: Reviewer MUST match BLOCK 1.5; F-20: output MUST be in 3-column table form)*

One row SHALL be present per finding raised by exactly one reviewer and not raised by any other. BLOCK 4 output MUST use the following 3-column table structure -- prose-only output (e.g., bullet list with reviewer attribution) is non-conformant under F-20 regardless of content correctness. The Reviewer cell MUST contain a name that exactly matches a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-16.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: a row `| UNIQUE | none | -- |` MUST be present. The `none` token is exempt from the F-16 identity check.
BLOCK 4 absence fires F-08. A non-table rendering of BLOCK 4 content is non-conformant under F-20 -- the block SHALL NOT be accepted until the 3-column table form is present. A Reviewer cell containing a name with no matching Reviewer in BLOCK 1.5 is non-conformant under F-16 -- the row SHALL NOT be accepted until the name is corrected to an exact BLOCK 1.5 match.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; table form required)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review." Domain expert reviewers are preferred Re-run Scope candidates where their BLOCK 0 signal area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Re-run Scope`: MUST contain reviewer name(s) and section scope. "Full review" is non-conformant under F-05. Every reviewer name in the Re-run Scope cell MUST exactly match a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-17. The row SHALL NOT be accepted until all Re-run Scope reviewer names are verified against BLOCK 1.5.

Conformance gate before closing: the count of amend rows (excluding the "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised if BLOCK 5 entry count < P1 count -- missing entries SHALL be added before the block closes.

If zero P1 findings: a row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.

---

## V-05 | Combined Maximum -- F-19 + F-20 + F-21: Full R9 Ceiling
**Axis**: combined (lifecycle-emphasis + output-format + behavior)
**Hypothesis**: Maximum R9 form. F-19 closes the content-completeness gap at BLOCK 2.5: a present Rationale row with an empty cell fires F-19. F-20 closes the structural form gap at BLOCK 4: prose-only unique catches output fires F-20, extending the column-enforcement architecture to its last uncovered mandatory block. F-21 closes the content-completeness gap on No expert needed disposition rows: an empty reason cell fires F-21, completing the bidirectional BLOCK 0 <-> BLOCK 1 contract with content-level enforcement on the disposition mechanism. F-19 and F-21 both belong to the content-completeness enforcement class (alongside F-11); F-20 belongs to the structural form enforcement class (alongside C-10, C-22, C-20, C-15, C-13). Three distinct enforcement classes are represented. Each new F-ID targets a distinct lifecycle position and failure class with no overlap. Together F-01 through F-21 cover every structural gap identified through R8. This variation is the intended extraction source for R10 criterion candidates. Expected score: 100 on v8.

A multi-expert design review SHALL be conducted according to the following specification. Each output block MUST conform to its stated requirements. A conformance failure is declared when any halt condition fires; the output SHALL NOT proceed past a failed block until the failure is resolved.

**Failure Mode Registry**

```
F-01  Missing discipline          -- fewer than 6 stock discipline blocks present in BLOCK 2
F-02  Unseveritied finding        -- any finding row contains a Sev value other than P1, P2, or P3
F-03  Expert without signal       -- Signal detected cell is empty in any BLOCK 1 domain expert row
F-04  Missing consensus block     -- BLOCK 3 is absent from the output
F-05  Full-review amend           -- Re-run Scope cell in BLOCK 5 contains "full review"
F-06  Pyramid inverted, silent    -- BLOCK 2.5 Status is inverted and no Rationale row is present
F-07  Incomplete expert trace     -- Expert added or Reason cell is empty in any BLOCK 1 domain expert row
F-08  Missing unique catches      -- BLOCK 4 is absent from the output
F-09  Coverage unverified         -- BLOCK 1.5 is absent, or Domain row count in BLOCK 1.5 does not equal BLOCK 1 domain count
F-10  Orphaned domain expert      -- a Domain row in BLOCK 1.5 carries a Reviewer name with no matching Expert added value in BLOCK 1
F-11  Split without synthesis     -- a SPLIT row in BLOCK 3 has an empty Synthesis column cell
F-12  Amend count mismatch        -- BLOCK 5 entry count (excluding the "no P1 findings" row) is less than BLOCK 2.5 P1 count
F-13  Uncatalogued signal         -- a Signal detected value in BLOCK 1 has no matching Signal phrase entry in the BLOCK 0 catalogue
F-14  Invalid consensus type      -- BLOCK 3 contains a Type cell whose value is neither AGREE nor SPLIT
F-15  Phantom reviewer            -- BLOCK 3 Reviewers column contains a name that has no matching Reviewer value in BLOCK 1.5
F-16  Phantom catcher             -- BLOCK 4 Reviewer cell contains a name that has no matching Reviewer value in BLOCK 1.5
F-17  Phantom re-run target       -- Re-run Scope cell in BLOCK 5 names a reviewer with no matching Reviewer value in BLOCK 1.5
F-18  Undisposed signal           -- a BLOCK 0 signal row has no corresponding Signal detected row in BLOCK 1 domain expert table and no No expert needed disposition row
F-19  Empty rationale             -- BLOCK 2.5 Rationale cell is present but empty when any Status cell reads inverted
F-20  Prose unique catches        -- BLOCK 4 output is not in the required 3-column table form (Type, Reviewer, Finding)
F-21  Empty disposition reason    -- reason cell of a No expert needed disposition row is empty
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 -- CONTENT SIGNAL CATALOGUE** *(Pre-scan only -- no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only -- expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | -- |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation -- the violating row SHALL NOT be accepted until a matching Signal phrase is added to this catalogue and verified. The catalogue is the canonical signal inventory for this review; the block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry; F-18: every BLOCK 0 signal MUST be resolved as an expert selection or a disposition row; F-21: disposition row reason cell MUST be populated)*

Drawing exclusively from the BLOCK 0 signal catalogue, one domain expert row SHALL be added per catalogued signal that warrants domain expertise. All three cells in every row MUST be populated.

Stock table (fixed -- SHALL NOT be modified):

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

A Signal detected cell that is empty is non-conformant under F-03. A Signal detected value that does not match any Signal phrase in BLOCK 0 is non-conformant under F-13 -- the row SHALL NOT be accepted until the Signal phrase appears in the BLOCK 0 catalogue. An Expert added or Reason cell that is empty is non-conformant under F-07.

If no signals were catalogued in BLOCK 0: a single row `| No signals detected | None | -- |` SHALL be present.

Signal disposition gate (F-18 + F-21): for every Signal phrase row in BLOCK 0 that is not `No domain signals detected`, one of the following conditions MUST hold before BLOCK 1 closes:
1. A domain expert row exists in the domain expert table with a matching Signal detected value, OR
2. A disposition row is present in the domain expert table: `| [Signal phrase] | No expert needed | [reason: one sentence explaining why no expert is warranted] |`

A BLOCK 0 signal with neither a domain expert row nor a disposition row is non-conformant under F-18 -- the block SHALL NOT be closed until all BLOCK 0 signals are resolved. A disposition row whose third cell (reason) is empty is non-conformant under F-21 -- the row SHALL NOT be accepted until the reason cell contains a specific explanation. F-18 enforces row existence; F-21 enforces reason cell content within a present row. Both conditions MUST be satisfied before BLOCK 1 closes.

F-13 is the inbound gate (BLOCK 1 references MUST exist in BLOCK 0); F-18 is the outbound existence gate (BLOCK 0 entries MUST be resolved in BLOCK 1); F-21 is the outbound content gate (disposition row reason cells MUST be substantively populated). Together they form the complete bidirectional BLOCK 0 <-> BLOCK 1 integrity contract.

After population: the count of domain expert rows (excluding "No signals detected" and disposition rows) SHALL be recorded as `BLOCK 1 domain count = [n]`.

---

**BLOCK 1.5 -- ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain row count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

The complete reviewer roster MUST be committed before any finding block is generated. Domain experts SHALL appear before stock disciplines. The Source column MUST distinguish `Domain` from `Stock`. Every Domain row MUST carry a Reviewer name that exactly matches an Expert added value from the BLOCK 1 domain expert table -- any deviation is non-conformant under F-10.

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

Conformance gate -- both checks SHALL be resolved before BLOCK 2 begins:
1. The count of Domain rows MUST equal `BLOCK 1 domain count`. F-09 is raised on mismatch.
2. Every Domain row Reviewer name MUST exactly match an Expert added value in BLOCK 1. F-10 is raised on any mismatch.

If no domain experts were added in BLOCK 1: no Domain rows SHALL be present. The table SHALL contain 6 Stock rows only.

---

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; domain experts run first)*

A finding table MUST be generated for every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers SHALL run first.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [section or component] | [one actionable sentence] |

Column conformance requirements:
- `Sev`: SHALL contain exactly one of P1, P2, or P3. Any other value is non-conformant under F-02.
- `Section`: SHALL name a specific section, component, or decision. The values "the design" or "overall" are non-conformant.
- P1 rows: Section MUST be populated.
- P2 rows: Section MUST be populated in >= 50% of P2 rows.
- A reviewer with no findings: a single row `| -- | -- | No findings. |` MUST be present.

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any reviewer fires F-01. BLOCK 2.5 SHALL NOT begin until all finding tables are present.

---

**BLOCK 2.5 -- SEVERITY DISTRIBUTION** *(F-06: an inverted Status MUST be accompanied by a Rationale row; F-19: Rationale cell MUST be populated when present; positioned between BLOCK 2 and BLOCK 3)*

All findings from BLOCK 2 SHALL be counted:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

Conformance: P3 >= P2 >= P1?
- YES: all Status cells SHALL read `pyramid nominal`. Proceed to BLOCK 3.
- NO: inverted levels SHALL carry Status `inverted`. A Rationale row MUST be present -- F-06 is raised if absent.

| Note | -- |
|------|---|
| Rationale | [name the design area and risk type that explains the unusual severity concentration] |

A Rationale cell that is present but empty is non-conformant under F-19 -- the block SHALL NOT be closed until the Rationale cell contains a specific design area and risk type explanation. F-06 fires on a missing row; F-19 fires on a present row with an empty cell. Both conditions MUST be resolved before BLOCK 3 begins.

`P1 count = [n from P1 row]` SHALL be recorded. This value is the anchor for the BLOCK 5 conformance gate (F-12).

---

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type cell MUST be AGREE or SPLIT; F-15: Reviewers names MUST match BLOCK 1.5)*

Synthesis is a dedicated column. A blank Synthesis cell for any SPLIT row fires F-11. CONSENSUS rows SHALL carry `--` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension -- not a restatement of opposing positions] |

If no consensus: a row `| CONSENSUS | none | -- | -- |` MUST be present.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: SHALL contain exactly AGREE or SPLIT. Any other value is non-conformant under F-14 -- the row SHALL NOT be accepted until the Type cell is corrected.
- `Reviewers`: every reviewer name in this column MUST appear in the BLOCK 1.5 Reviewer column. For AGREE rows, each comma-separated name MUST be in BLOCK 1.5. For SPLIT rows, both reviewer names MUST be in BLOCK 1.5. A name absent from BLOCK 1.5 is non-conformant under F-15 -- the row SHALL NOT be accepted until all reviewer names are verified against BLOCK 1.5.
- `Synthesis` for SPLIT rows: MUST name the underlying design tension. A restatement of the opposing positions is non-conformant. An empty Synthesis cell is non-conformant under F-11 -- the block SHALL NOT be closed until all SPLIT row Synthesis cells are populated.
- `Synthesis` for CONSENSUS rows: SHALL always be `--`.

BLOCK 3 absence fires F-04. F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside {AGREE, SPLIT}. F-15 fires on any Reviewers cell containing a name absent from BLOCK 1.5.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present -- absence fires F-08 even when catches are empty; F-16: Reviewer MUST match BLOCK 1.5; F-20: output MUST be in 3-column table form)*

One row SHALL be present per finding raised by exactly one reviewer and not raised by any other. BLOCK 4 output MUST use the following 3-column table structure -- prose-only output (e.g., bullet list with reviewer attribution) is non-conformant under F-20 regardless of content correctness. The Reviewer cell MUST contain a name that exactly matches a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-16.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: a row `| UNIQUE | none | -- |` MUST be present. The `none` token is exempt from the F-16 identity check.
BLOCK 4 absence fires F-08. A non-table rendering of BLOCK 4 content is non-conformant under F-20 -- the block SHALL NOT be accepted until the 3-column table form is present. A Reviewer cell containing a name with no matching Reviewer in BLOCK 1.5 is non-conformant under F-16 -- the row SHALL NOT be accepted until the name is corrected to an exact BLOCK 1.5 match.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; table form required)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review." Domain expert reviewers are preferred Re-run Scope candidates where their BLOCK 0 signal area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Re-run Scope`: MUST contain reviewer name(s) and section scope. "Full review" is non-conformant under F-05. Every reviewer name in the Re-run Scope cell MUST exactly match a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-17. The row SHALL NOT be accepted until all Re-run Scope reviewer names are verified against BLOCK 1.5.

Conformance gate before closing: the count of amend rows (excluding the "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised if BLOCK 5 entry count < P1 count -- missing entries SHALL be added before the block closes.

If zero P1 findings: a row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.
