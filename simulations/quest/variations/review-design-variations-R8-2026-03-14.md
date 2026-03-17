Written to `simulations/quest/variations/review-design-variations-R8-2026-03-14.md`.

---

## Round 8 Variations — review-design

### Variation Table

| Var | Axis | New Bet |
|-----|------|---------|
| **V-01** | lifecycle-emphasis | F-16 — BLOCK 4 phantom catcher (Reviewer vs BLOCK 1.5) |
| **V-02** | output-format | F-17 — BLOCK 5 Re-run Scope reviewer identity vs BLOCK 1.5 |
| **V-03** | behavior | F-18 — BLOCK 0 signal disposition completeness (bidirectional gate) |
| **V-04** | combined lifecycle + output-format | F-16 + F-17 stacked |
| **V-05** | combined max | F-16 + F-17 + F-18 — R9 extraction source |

---

### Gap analysis behind the three axes

**R7 V-05 left three structural holes:**

**Hole 1 — BLOCK 4 Reviewer has no cross-block identity check.**
F-10 (BLOCK 1→BLOCK 1.5) and F-15 (BLOCK 1.5→BLOCK 3) established the identity-integrity pattern. BLOCK 4 is the next downstream block that names reviewers without verification. A UNIQUE catch attributed to a reviewer absent from BLOCK 1.5 is a "phantom catcher." F-16 closes this — same pattern as F-15, one stage later.

**Hole 2 — BLOCK 5 Re-run Scope names reviewers without identity check.**
Re-run Scope targets a reviewer by name for post-amendment re-running. No halt verifies those names exist in BLOCK 1.5. A phantom re-run target is an invalid amend action — the reviewer never ran. F-17 closes this, completing the full identity lifecycle chain: F-10 (BLOCK 1→1.5), F-15 (1.5→BLOCK 3), F-16 (1.5→BLOCK 4), F-17 (1.5→BLOCK 5).

**Hole 3 — BLOCK 0 signals can be silently dropped.**
F-13 enforces the inbound direction: BLOCK 1 may not reference a signal absent from BLOCK 0. The outbound direction is unconstrained: a signal catalogued in BLOCK 0 can vanish in BLOCK 1 with no explanation. F-18 introduces *catalogue disposition completeness* — a new enforcement class (sixth, after structural presence, content completeness, count parity, identity integrity, vocabulary integrity). Every BLOCK 0 signal must either map to a BLOCK 1 expert row or carry an explicit `No expert needed | [reason]` disposition row. F-13 + F-18 together form the first bidirectional BLOCK 0 ↔ BLOCK 1 integrity contract.

---

Each variation is a complete, runnable prompt body based on R7 V-05. V-01/V-02/V-03 isolate a single new axis. V-04 combines F-16 + F-17. V-05 stacks all three for the R8 ceiling and R9 extraction.
nt omission is non-conformant under F-18. This introduces a bidirectional BLOCK 0 <-> BLOCK 1 contract: F-13 enforces the BLOCK 1->BLOCK 0 direction (no signal added in BLOCK 1 without BLOCK 0 entry); F-18 enforces the BLOCK 0->BLOCK 1 direction (no BLOCK 0 signal left without BLOCK 1 resolution).

**Research questions for R8:**
- V-01 isolation: Does F-16 on BLOCK 4 Reviewer identity produce fewer phantom-catcher errors than the current F-08-only enforcement?
- V-02 isolation: Does F-17 on Re-run Scope reviewer identity prevent invalid amend targets without degrading C-06 or C-20?
- V-03 isolation: Does F-18 signal disposition completeness improve BLOCK 0 catalogue coverage quality without over-constraining signal selection?
- V-04 vs V-01+V-02: Are F-16 and F-17 additive (V-04 > both individually), or does one subsume the other?
- V-05 vs V-04: Does F-18 stack additively with F-16+F-17, or does three-halt combination introduce overhead?

---

## V-01 | Lifecycle Emphasis -- F-16 BLOCK 4 Phantom Catcher Detection
**Axis**: lifecycle-emphasis
**Hypothesis**: R7 V-05's BLOCK 4 UNIQUE catch table has a `Reviewer` column, but no halt verifies that named reviewers exist in BLOCK 1.5. F-10 (BLOCK 1.5 vs BLOCK 1) and F-15 (BLOCK 3 vs BLOCK 1.5) both enforce reviewer identity across lifecycle boundaries. BLOCK 4 is the last downstream reviewer-referencing block without equivalent coverage. A UNIQUE catch attributed to a reviewer absent from BLOCK 1.5 is a "phantom catcher" -- the finding is attributed to a reviewer who never ran. F-16 ("BLOCK 4 Reviewer value has no matching Reviewer in BLOCK 1.5") closes this gap, extending the identity-integrity chain one stage further. All F-01 through F-15 are unchanged from R7 V-05. The single variable is whether a named identity halt on BLOCK 4 reduces phantom-catcher errors.

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

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry)*

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

After population: the count of domain expert rows (excluding the "No signals detected" row) SHALL be recorded as `BLOCK 1 domain count = [n]`.

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

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; table form required)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review." Domain expert reviewers are preferred Re-run Scope candidates where their BLOCK 0 signal area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Re-run Scope`: MUST contain reviewer name(s) and section scope. "Full review" is non-conformant under F-05.

Conformance gate before closing: the count of amend rows (excluding the "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised if BLOCK 5 entry count < P1 count -- missing entries SHALL be added before the block closes.

If zero P1 findings: a row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.

---

## V-02 | Output Format -- F-17 BLOCK 5 Re-run Scope Reviewer Identity
**Axis**: output-format
**Hypothesis**: R7 V-05's BLOCK 5 Re-run Scope cell names reviewer(s) for targeted re-running after amendments, but no halt verifies those names exist in BLOCK 1.5. A Re-run Scope naming a reviewer absent from the committed roster targets a phantom reviewer -- the amend action is structurally invalid because the reviewer never participated in the review. F-10 (BLOCK 1.5 vs BLOCK 1), F-15 (BLOCK 3 vs BLOCK 1.5) each enforce reviewer identity at downstream blocks. BLOCK 5 is the last reviewer-referencing block without identity integrity coverage. F-17 ("Re-run Scope names a reviewer absent from BLOCK 1.5") closes this gap, completing the full downstream identity chain from BLOCK 3 through BLOCK 5. All other blocks and F-01 through F-15 are unchanged from R7 V-05. The single variable is whether named identity enforcement on Re-run Scope reduces phantom re-run target errors.

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
F-17  Phantom re-run target       -- Re-run Scope cell in BLOCK 5 names a reviewer with no matching Reviewer value in BLOCK 1.5
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

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry)*

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

After population: the count of domain expert rows (excluding the "No signals detected" row) SHALL be recorded as `BLOCK 1 domain count = [n]`.

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
| Rationale | [name the design area and risk type that explains the unusual P1/P2 concentration] |

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

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present -- absence fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If no unique catches: a row `| UNIQUE | none | -- |` MUST be present.
BLOCK 4 absence fires F-08.

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

## V-03 | Behavior -- F-18 BLOCK 0 Signal Disposition Completeness
**Axis**: behavior
**Hypothesis**: R7 V-05's BLOCK 0 gate enforces a forward constraint: BLOCK 1 SHALL NOT reference a signal absent from BLOCK 0 (enforced by F-13). This is one direction of a bidirectional contract. The reverse is unconstrained: a signal catalogued in BLOCK 0 can be silently skipped in BLOCK 1 -- no expert is added, no explanation is given. This is structurally equivalent to the silent pyramid inversion caught by F-06: a state is reached (signal uncovered) without an explicit conformance declaration. F-18 introduces "catalogue disposition completeness" -- a new enforcement class. Every BLOCK 0 signal row MUST be resolved in BLOCK 1: either a domain expert row is present with that Signal detected value, or an explicit `No expert needed` disposition row is recorded with a stated reason. Silent omission is non-conformant under F-18. This converts the BLOCK 0 <-> BLOCK 1 relationship from a one-directional gate (F-13 only) into a bidirectional contract: F-13 enforces BLOCK 1->BLOCK 0 (signals added in BLOCK 1 must exist in BLOCK 0); F-18 enforces BLOCK 0->BLOCK 1 (signals catalogued in BLOCK 0 must be addressed in BLOCK 1). All F-01 through F-15 are unchanged from R7 V-05. The single variable is whether F-18 reduces undisclosed signal suppression.

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
F-18  Undisposed signal           -- a BLOCK 0 signal row has no corresponding Signal detected row in BLOCK 1 domain expert table and no No expert needed disposition row
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

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry; F-18: every BLOCK 0 signal MUST be addressed or explicitly dismissed)*

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
2. A disposition row is present: `| [Signal phrase] | No expert needed | [reason: one sentence explaining why no expert is warranted] |`

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

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present -- absence fires F-08 even when catches are empty)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer] | [finding not raised by any other reviewer] |

If no unique catches: a row `| UNIQUE | none | -- |` MUST be present.
BLOCK 4 absence fires F-08.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; table form required)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review." Domain expert reviewers are preferred Re-run Scope candidates where their BLOCK 0 signal area overlaps with the P1 finding section.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Re-run Scope`: MUST contain reviewer name(s) and section scope. "Full review" is non-conformant under F-05.

Conformance gate before closing: the count of amend rows (excluding the "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised if BLOCK 5 entry count < P1 count -- missing entries SHALL be added before the block closes.

If zero P1 findings: a row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.

---

## V-04 | Combined (Lifecycle + Output-Format) -- F-16 + F-17: Identity Integrity to BLOCK 4 and BLOCK 5
**Axis**: combined (lifecycle-emphasis + output-format)
**Hypothesis**: Combines V-01's F-16 (BLOCK 4 phantom catcher detection) with V-02's F-17 (BLOCK 5 Re-run Scope reviewer identity). F-16 targets BLOCK 4 -- the only reviewer-attributing block downstream of BLOCK 1.5 without identity integrity coverage prior to R8. F-17 targets BLOCK 5 Re-run Scope -- the only block that names reviewers as targets without verifying their existence in the committed roster. These address distinct failure surfaces at different lifecycle positions: F-16 fires on UNIQUE catch attribution errors; F-17 fires on invalid amend target errors. Together they complete the full downstream identity lifecycle chain begun by F-10 (BLOCK 1->BLOCK 1.5) and F-15 (BLOCK 1.5->BLOCK 3): F-16 covers BLOCK 1.5->BLOCK 4, F-17 covers BLOCK 1.5->BLOCK 5. All F-01 through F-15 from R7 V-05 are unchanged. Tests whether F-16 and F-17 are additive.

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

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry)*

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

After population: the count of domain expert rows (excluding the "No signals detected" row) SHALL be recorded as `BLOCK 1 domain count = [n]`.

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

## V-05 | Combined Maximum -- F-16 + F-17 + F-18: Full R8 Ceiling
**Axis**: combined (lifecycle-emphasis + output-format + behavior)
**Hypothesis**: Maximum R8 form. F-16 (BLOCK 4 phantom catcher) closes the identity-integrity gap at BLOCK 4 -- the last downstream reviewer-attribution block without cross-block verification. F-17 (BLOCK 5 Re-run Scope phantom target) closes the identity-integrity gap at BLOCK 5 -- the last reviewer-referencing cell without cross-block verification. Together F-16 and F-17 complete the full identity lifecycle chain: F-10 (BLOCK 1->BLOCK 1.5), F-15 (BLOCK 1.5->BLOCK 3), F-16 (BLOCK 1.5->BLOCK 4), F-17 (BLOCK 1.5->BLOCK 5). F-18 (BLOCK 0 signal disposition completeness) introduces the first bidirectional BLOCK 0 <-> BLOCK 1 contract: F-13 enforces the inbound direction (BLOCK 1 must draw from BLOCK 0); F-18 enforces the outbound direction (every BLOCK 0 signal must be resolved in BLOCK 1 as an expert selection or explicit disposition). F-18 introduces a new enforcement class -- catalogue disposition completeness -- distinct from all prior classes (structural presence, content completeness, count parity, identity integrity, vocabulary integrity). Each new F-ID targets a distinct failure class with no overlap. Together, F-01 through F-18 cover every structural gap identified through R7. This variation is the intended extraction source for R9 criterion candidates. Expected score: 100 on v7.

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
