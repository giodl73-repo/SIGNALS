## Round 10 Variations — review-design

Written to `simulations/quest/variations/review-design-variations-R10-2026-03-14.md`.

---

### Variation table

| Var | Axis | New Bet |
|-----|------|---------|
| V-01 | lifecycle-emphasis | F-22 -- BLOCK 2 domain expert finding table coverage |
| V-02 | output-format | F-23 -- BLOCK 3 Issue cell content completeness |
| V-03 | behavior | F-24 -- BLOCK 5 Action cell content completeness |
| V-04 | combined lifecycle + output-format | F-22 + F-23 stacked |
| V-05 | combined max | F-22 + F-23 + F-24 -- R11 extraction source |

---

### Gap analysis

**Three structural holes in R9 V-05:**

**F-22 (lifecycle-emphasis) — BLOCK 2 domain expert finding table coverage.**
F-01 names its halt as "fewer than 6 *stock* discipline blocks present." The BLOCK 2 instruction prose says "a finding table MUST be generated for every reviewer listed in BLOCK 1.5," but no named F-code covers a missing *domain expert* finding table. If a domain expert is in BLOCK 1.5 but absent from BLOCK 2, F-01 doesn't fire (stock count still 6) and the domain perspective silently disappears. F-22 closes the asymmetry between the stock and domain enforcement tiers.

**F-23 (output-format) — BLOCK 3 Issue cell content completeness.**
BLOCK 3 now has halts on three of four columns: F-14 (Type), F-15 (Reviewers), F-11 (Synthesis for SPLIT). The Issue column — what the reviewers agreed or disagreed *about* — has none. A present but empty Issue cell passes all three existing halts while delivering no finding summary. This applies the established content-completeness class (F-11, F-19, F-21) to the last unguarded column in BLOCK 3.

**F-24 (behavior) — BLOCK 5 Action cell content completeness.**
F-12 (count), F-05 (no "full review"), and F-17 (reviewer identity) all pass with a present but empty Action cell. The Action cell carries the prescriptive value of the amend pathway — what to add, remove, or clarify. An empty cell defeats the purpose of BLOCK 5 while satisfying every current halt. F-24 applies the present-but-empty enforcement class (F-19, F-21) to the Action column, completing content-completeness coverage at the amend lifecycle position.

---

### Feature matrix

| F-ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| F-22 -- BLOCK 2 domain expert coverage | YES | no | no | YES | YES |
| F-23 -- BLOCK 3 Issue cell | no | YES | no | YES | YES |
| F-24 -- BLOCK 5 Action cell | no | no | YES | no | YES |

**Isolation logic:**
- V-02/V-03 carry no F-22 → confirm C-30 candidate
- V-01/V-03 carry no F-23 → confirm C-31 candidate
- V-01/V-02 carry no F-24 → confirm C-32 candidate

**V-05 is the R11 extraction source** — three non-overlapping F-IDs, two enforcement sub-classes (coverage-extension: F-22; content-completeness: F-23/F-24), three distinct lifecycle positions.
or filler Action cell defeats the purpose of BLOCK 5 while passing all three current halts. F-24 applies the present-but-empty enforcement class (established by F-19/F-21) to the Action column. Axis: **behavior** -- a new behavioral enforcement on the amend mechanism, targeting the prescriptive content cell rather than the structural or identity cells already covered.

---

### Feature Matrix

| F-ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| F-22 -- BLOCK 2 domain expert finding table | YES | NO | NO | YES | YES |
| F-23 -- BLOCK 3 Issue cell content completeness | NO | YES | NO | YES | YES |
| F-24 -- BLOCK 5 Action cell content completeness | NO | NO | YES | NO | YES |

---

### Predicted scoring on v9 rubric

All five variations inherit the R9 V-05 baseline (F-01 through F-21), which already passes all 29 criteria C-01 through C-29 on rubric v9. The three new F-IDs are additive above v9's ceiling. All variations are expected to score **100** on v9.

**Isolation logic:**
- V-02 and V-03 carry no F-22 → they confirm F-22 is aspirational (C-30 candidate)
- V-01 and V-03 carry no F-23 → they confirm F-23 is aspirational (C-31 candidate)
- V-01 and V-02 carry no F-24 → they confirm F-24 is aspirational (C-32 candidate)

**V-05 is the R11 extraction source** -- three new F-IDs, two enforcement classes (coverage-extension: F-22; content-completeness: F-23/F-24), three distinct lifecycle positions (BLOCK 2, BLOCK 3, BLOCK 5), no overlap between them.

---

## V-01 | Lifecycle-Emphasis -- F-22: BLOCK 2 Domain Expert Finding Table Coverage
**Axis**: lifecycle-emphasis
**Hypothesis**: F-01 fires when fewer than 6 stock discipline blocks are present in BLOCK 2. The BLOCK 2 instruction says "a finding table MUST be generated for every reviewer listed in BLOCK 1.5" -- but F-01's named halt condition references only stock disciplines. A domain expert in BLOCK 1.5 with no BLOCK 2 finding table satisfies F-01 while silently dropping domain coverage. C-01 passes; the domain expert's unique signal perspective is absent from the review. F-22 extends the BLOCK 2 presence enforcement to domain experts specifically, closing the asymmetry between stock and domain reviewer coverage. Tests whether domain expert finding table absence is independently detectable from stock discipline absence. V-02/V-03 will score 100 without F-22, confirming aspirational. All F-01 through F-21 from R9 V-05 are unchanged.

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
F-22  Missing domain expert table -- a domain expert listed in BLOCK 1.5 has no corresponding finding table in BLOCK 2
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

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; F-22: every domain expert in BLOCK 1.5 MUST have a corresponding finding table; domain experts run first)*

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

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any stock discipline reviewer fires F-01. Absence of any domain expert reviewer fires F-22 -- the missing finding table SHALL be added before BLOCK 2.5 begins. F-01 and F-22 together enforce complete BLOCK 2 coverage across both reviewer tiers. BLOCK 2.5 SHALL NOT begin until finding tables are present for all stock and domain reviewers.

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

## V-02 | Output-Format -- F-23: BLOCK 3 Issue Cell Content Completeness
**Axis**: output-format
**Hypothesis**: Three of the four BLOCK 3 columns have named halts: F-14 fires on an invalid Type value; F-15 fires on a phantom Reviewer name; F-11 fires on an empty Synthesis cell for SPLIT rows. The Issue column -- the descriptor that identifies what the reviewers agreed or disagreed about -- has no halt. A BLOCK 3 row with an empty Issue cell passes F-11, F-14, and F-15 while providing no finding summary. The content-completeness enforcement class (F-11 for SPLIT Synthesis, F-19 for pyramid Rationale, F-21 for disposition reason) applies here: a present cell that carries no content is a distinct failure from a missing row. F-23 closes the last open column in BLOCK 3 by naming a halt for empty Issue cells. Tests whether BLOCK 3 Issue cell content completeness is independently detectable from the three existing BLOCK 3 halts. V-01/V-03 will score 100 without F-23, confirming aspirational. All F-01 through F-21 from R9 V-05 are unchanged.

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
F-23  Empty issue cell            -- a BLOCK 3 row has a present but empty Issue cell
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

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type cell MUST be AGREE or SPLIT; F-15: Reviewers names MUST match BLOCK 1.5; F-23: Issue cell MUST be populated)*

Synthesis is a dedicated column. A blank Synthesis cell for any SPLIT row fires F-11. CONSENSUS rows SHALL carry `--` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension -- not a restatement of opposing positions] |

If no consensus: a row `| CONSENSUS | none | -- | -- |` MUST be present. The `none` sentinel token is exempt from the F-23 Issue cell content check.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: SHALL contain exactly AGREE or SPLIT. Any other value is non-conformant under F-14 -- the row SHALL NOT be accepted until the Type cell is corrected.
- `Issue`: SHALL contain a substantive description of the finding or point of contention. An empty Issue cell is non-conformant under F-23 -- the row SHALL NOT be accepted until the Issue cell is populated. The `none` sentinel in a no-consensus row is exempt.
- `Reviewers`: every reviewer name in this column MUST appear in the BLOCK 1.5 Reviewer column. For AGREE rows, each comma-separated name MUST be in BLOCK 1.5. For SPLIT rows, both reviewer names MUST be in BLOCK 1.5. A name absent from BLOCK 1.5 is non-conformant under F-15 -- the row SHALL NOT be accepted until all reviewer names are verified against BLOCK 1.5.
- `Synthesis` for SPLIT rows: MUST name the underlying design tension. A restatement of the opposing positions is non-conformant. An empty Synthesis cell is non-conformant under F-11 -- the block SHALL NOT be closed until all SPLIT row Synthesis cells are populated.
- `Synthesis` for CONSENSUS rows: SHALL always be `--`.

BLOCK 3 absence fires F-04. F-23 fires on any non-sentinel row with an empty Issue cell. F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside {AGREE, SPLIT}. F-15 fires on any Reviewers cell containing a name absent from BLOCK 1.5.

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

## V-03 | Behavior -- F-24: BLOCK 5 Action Cell Content Completeness
**Axis**: behavior
**Hypothesis**: F-12 enforces that BLOCK 5 has one amend row per P1 finding (row-existence enforcement). F-05 enforces that Re-run Scope does not say "full review." F-17 enforces that Re-run Scope reviewer names are in BLOCK 1.5. All three checks can be satisfied with a present but empty Action cell: the row exists (F-12), Re-run Scope names a section (F-05), and the reviewer is in BLOCK 1.5 (F-17). The Action column carries the prescriptive content of the amend pathway -- what to add, remove, or clarify. An empty Action cell defeats the purpose of BLOCK 5 while passing every current halt. F-24 applies the present-but-empty enforcement class (F-19 at BLOCK 2.5, F-21 at BLOCK 1) to BLOCK 5's Action column, completing content-completeness coverage at the amend lifecycle position. Tests whether BLOCK 5 Action cell content completeness is independently detectable from the three existing BLOCK 5 halts. V-01/V-02 will score 100 without F-24, confirming aspirational. All F-01 through F-21 from R9 V-05 are unchanged.

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
F-24  Empty action cell           -- Action cell of a BLOCK 5 amend row is present but empty
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

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; F-24: Action cell MUST be populated; table form required)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review." Domain expert reviewers are preferred Re-run Scope candidates where their BLOCK 0 signal area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Action`: SHALL contain a specific corrective instruction -- what to add, remove, or clarify in the design. An empty Action cell is non-conformant under F-24 -- the row SHALL NOT be accepted until the Action cell contains a specific corrective instruction. A filler value (e.g., "TBD", "see above", or a restatement of the P1 finding) does not satisfy F-24.
- `Re-run Scope`: MUST contain reviewer name(s) and section scope. "Full review" is non-conformant under F-05. Every reviewer name in the Re-run Scope cell MUST exactly match a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-17. The row SHALL NOT be accepted until all Re-run Scope reviewer names are verified against BLOCK 1.5.

Conformance gate before closing: the count of amend rows (excluding the "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised if BLOCK 5 entry count < P1 count -- missing entries SHALL be added before the block closes.

If zero P1 findings: a row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.

---

## V-04 | Combined (Lifecycle + Output-Format) -- F-22 + F-23: Domain Expert Coverage + BLOCK 3 Issue Cell
**Axis**: combined (lifecycle-emphasis + output-format)
**Hypothesis**: Combines V-01's F-22 (BLOCK 2 domain expert finding table coverage) with V-02's F-23 (BLOCK 3 Issue cell content completeness). F-22 targets a coverage-extension gap at BLOCK 2 -- a named halt for domain expert absence that mirrors F-01's stock-discipline halt. F-23 targets a content-completeness gap at BLOCK 3 -- a present Issue cell that is empty. These are at distinct lifecycle positions (BLOCK 2 vs BLOCK 3) and represent distinct enforcement sub-classes (coverage-extension vs content-completeness). Tests whether F-22 and F-23 are additive without interference. V-03 will score 100 without either, confirming both remain aspirational. All F-01 through F-21 from R9 V-05 are unchanged.

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
F-22  Missing domain expert table -- a domain expert listed in BLOCK 1.5 has no corresponding finding table in BLOCK 2
F-23  Empty issue cell            -- a BLOCK 3 row has a present but empty Issue cell
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

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; F-22: every domain expert in BLOCK 1.5 MUST have a corresponding finding table; domain experts run first)*

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

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any stock discipline reviewer fires F-01. Absence of any domain expert reviewer fires F-22 -- the missing finding table SHALL be added before BLOCK 2.5 begins. F-01 and F-22 together enforce complete BLOCK 2 coverage across both reviewer tiers. BLOCK 2.5 SHALL NOT begin until finding tables are present for all stock and domain reviewers.

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

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type cell MUST be AGREE or SPLIT; F-15: Reviewers names MUST match BLOCK 1.5; F-23: Issue cell MUST be populated)*

Synthesis is a dedicated column. A blank Synthesis cell for any SPLIT row fires F-11. CONSENSUS rows SHALL carry `--` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension -- not a restatement of opposing positions] |

If no consensus: a row `| CONSENSUS | none | -- | -- |` MUST be present. The `none` sentinel token is exempt from the F-23 Issue cell content check.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: SHALL contain exactly AGREE or SPLIT. Any other value is non-conformant under F-14 -- the row SHALL NOT be accepted until the Type cell is corrected.
- `Issue`: SHALL contain a substantive description of the finding or point of contention. An empty Issue cell is non-conformant under F-23 -- the row SHALL NOT be accepted until the Issue cell is populated. The `none` sentinel in a no-consensus row is exempt.
- `Reviewers`: every reviewer name in this column MUST appear in the BLOCK 1.5 Reviewer column. For AGREE rows, each comma-separated name MUST be in BLOCK 1.5. For SPLIT rows, both reviewer names MUST be in BLOCK 1.5. A name absent from BLOCK 1.5 is non-conformant under F-15 -- the row SHALL NOT be accepted until all reviewer names are verified against BLOCK 1.5.
- `Synthesis` for SPLIT rows: MUST name the underlying design tension. A restatement of the opposing positions is non-conformant. An empty Synthesis cell is non-conformant under F-11 -- the block SHALL NOT be closed until all SPLIT row Synthesis cells are populated.
- `Synthesis` for CONSENSUS rows: SHALL always be `--`.

BLOCK 3 absence fires F-04. F-23 fires on any non-sentinel row with an empty Issue cell. F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside {AGREE, SPLIT}. F-15 fires on any Reviewers cell containing a name absent from BLOCK 1.5.

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

## V-05 | Combined Max -- F-22 + F-23 + F-24: Domain Expert Coverage + BLOCK 3 Issue + BLOCK 5 Action
**Axis**: combined max
**Hypothesis**: Carries all three new F-IDs from R10: F-22 (BLOCK 2 domain expert finding table coverage), F-23 (BLOCK 3 Issue cell content completeness), F-24 (BLOCK 5 Action cell content completeness). Each targets a distinct lifecycle position (BLOCK 2, BLOCK 3, BLOCK 5) and a distinct enforcement sub-class (coverage-extension at BLOCK 2; content-completeness at BLOCK 3 and BLOCK 5). No two new halts interact -- a model that passes all three independently can fail any subset without cascading. V-04 confirms F-22+F-23 are stackable. V-01/V-02/V-03 provide individual isolation. V-05 is the R11 extraction source. All F-01 through F-21 from R9 V-05 are unchanged.

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
F-22  Missing domain expert table -- a domain expert listed in BLOCK 1.5 has no corresponding finding table in BLOCK 2
F-23  Empty issue cell            -- a BLOCK 3 row has a present but empty Issue cell
F-24  Empty action cell           -- Action cell of a BLOCK 5 amend row is present but empty
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

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; F-22: every domain expert in BLOCK 1.5 MUST have a corresponding finding table; domain experts run first)*

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

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any stock discipline reviewer fires F-01. Absence of any domain expert reviewer fires F-22 -- the missing finding table SHALL be added before BLOCK 2.5 begins. F-01 and F-22 together enforce complete BLOCK 2 coverage across both reviewer tiers. BLOCK 2.5 SHALL NOT begin until finding tables are present for all stock and domain reviewers.

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

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type cell MUST be AGREE or SPLIT; F-15: Reviewers names MUST match BLOCK 1.5; F-23: Issue cell MUST be populated)*

Synthesis is a dedicated column. A blank Synthesis cell for any SPLIT row fires F-11. CONSENSUS rows SHALL carry `--` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension -- not a restatement of opposing positions] |

If no consensus: a row `| CONSENSUS | none | -- | -- |` MUST be present. The `none` sentinel token is exempt from the F-23 Issue cell content check.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: SHALL contain exactly AGREE or SPLIT. Any other value is non-conformant under F-14 -- the row SHALL NOT be accepted until the Type cell is corrected.
- `Issue`: SHALL contain a substantive description of the finding or point of contention. An empty Issue cell is non-conformant under F-23 -- the row SHALL NOT be accepted until the Issue cell is populated. The `none` sentinel in a no-consensus row is exempt.
- `Reviewers`: every reviewer name in this column MUST appear in the BLOCK 1.5 Reviewer column. For AGREE rows, each comma-separated name MUST be in BLOCK 1.5. For SPLIT rows, both reviewer names MUST be in BLOCK 1.5. A name absent from BLOCK 1.5 is non-conformant under F-15 -- the row SHALL NOT be accepted until all reviewer names are verified against BLOCK 1.5.
- `Synthesis` for SPLIT rows: MUST name the underlying design tension. A restatement of the opposing positions is non-conformant. An empty Synthesis cell is non-conformant under F-11 -- the block SHALL NOT be closed until all SPLIT row Synthesis cells are populated.
- `Synthesis` for CONSENSUS rows: SHALL always be `--`.

BLOCK 3 absence fires F-04. F-23 fires on any non-sentinel row with an empty Issue cell. F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside {AGREE, SPLIT}. F-15 fires on any Reviewers cell containing a name absent from BLOCK 1.5.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present -- absence fires F-08 even when catches are empty; F-16: Reviewer MUST match BLOCK 1.5; F-20: output MUST be in 3-column table form)*

One row SHALL be present per finding raised by exactly one reviewer and not raised by any other. BLOCK 4 output MUST use the following 3-column table structure -- prose-only output (e.g., bullet list with reviewer attribution) is non-conformant under F-20 regardless of content correctness. The Reviewer cell MUST contain a name that exactly matches a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-16.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: a row `| UNIQUE | none | -- |` MUST be present. The `none` token is exempt from the F-16 identity check.
BLOCK 4 absence fires F-08. A non-table rendering of BLOCK 4 content is non-conformant under F-20 -- the block SHALL NOT be accepted until the 3-column table form is present. A Reviewer cell containing a name with no matching Reviewer in BLOCK 1.5 is non-conformant under F-16 -- the row SHALL NOT be accepted until the name is corrected to an exact BLOCK 1.5 match.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; F-24: Action cell MUST be populated; table form required)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review." Domain expert reviewers are preferred Re-run Scope candidates where their BLOCK 0 signal area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Action`: SHALL contain a specific corrective instruction -- what to add, remove, or clarify in the design. An empty Action cell is non-conformant under F-24 -- the row SHALL NOT be accepted until the Action cell contains a specific corrective instruction. A filler value (e.g., "TBD", "see above", or a restatement of the P1 finding) does not satisfy F-24.
- `Re-run Scope`: MUST contain reviewer name(s) and section scope. "Full review" is non-conformant under F-05. Every reviewer name in the Re-run Scope cell MUST exactly match a Reviewer value in BLOCK 1.5 -- a name absent from BLOCK 1.5 is non-conformant under F-17. The row SHALL NOT be accepted until all Re-run Scope reviewer names are verified against BLOCK 1.5.

Conformance gate before closing: the count of amend rows (excluding the "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised if BLOCK 5 entry count < P1 count -- missing entries SHALL be added before the block closes.

If zero P1 findings: a row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.
