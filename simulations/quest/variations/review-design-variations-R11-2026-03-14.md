Written to `simulations/quest/variations/review-design-variations-R11-2026-03-14.md`.

---

## Round 11 Variations -- review-design

### Variation table

| Var | Axis | New Bet |
|-----|------|---------|
| V-01 | behavior | F-25 -- BLOCK 4 Finding cell content completeness |
| V-02 | output-format | F-26 -- BLOCK 5 Section cell content completeness |
| V-03 | lifecycle-emphasis | F-27 -- BLOCK 2 P1 Section named halt |
| V-04 | combined behavior + output-format | F-25 + F-26 stacked |
| V-05 | combined max | F-25 + F-26 + F-27 -- R12 extraction source |

---

### Gap analysis

**Three structural holes in R10 V-05 (F-01 through F-24):**

**F-25 (behavior) -- BLOCK 4 Finding cell content completeness.**
BLOCK 4 enforces table form (F-20), Reviewer identity (F-16), and block presence (F-08). The Finding column -- the informational payload of the unique-catches block -- has no named halt. A UNIQUE row with a present but empty Finding cell passes all three existing halts. F-25 applies the established content-completeness enforcement class (F-11, F-19, F-21, F-23, F-24) to the Finding column. The `none` sentinel in a no-catches row is exempt.

**F-26 (output-format) -- BLOCK 5 Section cell content completeness.**
BLOCK 5 has four columns. Action is gated (F-24). Re-run Scope is gated (F-05/F-17). Row count is gated (F-12). The Section column -- the spatial anchor naming where in the design the change must be made -- has no named halt. An amend row with an empty Section cell passes all current halts: it names what to change (Action) and who reruns (Re-run Scope) but provides no design location. F-26 closes the last unguarded column in BLOCK 5. The "no P1 findings" sentinel row is exempt.

**F-27 (lifecycle-emphasis) -- BLOCK 2 P1 Section named halt.**
BLOCK 2's column conformance already contains the prose requirement: "P1 rows: Section MUST be populated." No named F-ID backs this requirement. A P1 finding row with an empty Section cell passes F-01, F-02, and F-22 -- none fire on column content within a present row. F-27 converts the existing prose MUST into a named F-ID, applying the C-14 enforcement pattern at the column level. Prose MUSTs are skippable; named halts are detectable enforcement events.

---

### Feature matrix

| F-ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| F-25 -- BLOCK 4 Finding cell | YES | NO | NO | YES | YES |
| F-26 -- BLOCK 5 Section cell | NO | YES | NO | YES | YES |
| F-27 -- BLOCK 2 P1 Section named halt | NO | NO | YES | NO | YES |

**Isolation:** V-02/V-03 confirm C-33. V-01/V-03 confirm C-34. V-01/V-02 confirm C-35. All five expected to score 100 on v10 rubric. V-05 is the R12 extraction source.
---|------|------|------|------|------|
| F-25 -- BLOCK 4 Finding cell content completeness | YES | NO | NO | YES | YES |
| F-26 -- BLOCK 5 Section cell content completeness | NO | YES | NO | YES | YES |
| F-27 -- BLOCK 2 P1 Section named halt | NO | NO | YES | NO | YES |

**Isolation logic:**
- V-02 and V-03 carry no F-25 -- confirm C-33 candidate
- V-01 and V-03 carry no F-26 -- confirm C-34 candidate
- V-01 and V-02 carry no F-27 -- confirm C-35 candidate

**V-05 is the R12 extraction source** -- three new F-IDs, one enforcement class (content-completeness-within-structural-presence at F-25/F-26; prose-to-named-halt conversion at F-27), three distinct lifecycle positions (BLOCK 2, BLOCK 4, BLOCK 5), no overlap.

---

### Predicted scoring on v10 rubric

All five variations inherit the R10 V-05 baseline (F-01 through F-24), which already passes all 32 criteria C-01 through C-32 on rubric v10. The three new F-IDs are additive above v10's ceiling. All variations are expected to score **100** on v10.

---

## V-01 | Behavior -- F-25: BLOCK 4 Finding Cell Content Completeness
**Axis**: behavior
**Hypothesis**: BLOCK 4 is gated by F-08 (block presence), F-16 (Reviewer identity), and F-20 (table form). All three can be satisfied by a UNIQUE row whose Finding cell is present but empty -- the row exists (F-08), the Reviewer matches BLOCK 1.5 (F-16), the table form is correct (F-20). The Finding column carries the entire informational value of the unique-catches block. An empty Finding cell defeats that purpose while passing every current halt. F-25 applies the content-completeness enforcement class to the Finding column of BLOCK 4. Tests whether BLOCK 4 Finding cell completeness is independently detectable from existing halts. V-02/V-03 will score 100 without F-25, confirming aspirational. All F-01 through F-24 from R10 V-05 are unchanged.

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
F-25  Empty finding cell          -- Finding cell of a BLOCK 4 unique catch row is present but empty
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
2. A disposition row is present: `| [Signal phrase] | No expert needed | [reason] |`

A BLOCK 0 signal with neither a domain expert row nor a disposition row is non-conformant under F-18. A disposition row whose third cell is empty is non-conformant under F-21. Both conditions MUST be satisfied before BLOCK 1 closes.

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

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any stock discipline reviewer fires F-01. Absence of any domain expert reviewer fires F-22. BLOCK 2.5 SHALL NOT begin until finding tables are present for all stock and domain reviewers.

---

**BLOCK 2.5 -- SEVERITY DISTRIBUTION** *(F-06: an inverted Status MUST be accompanied by a Rationale row; F-19: Rationale cell MUST be populated when present)*

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

A Rationale cell that is present but empty is non-conformant under F-19. F-06 fires on a missing row; F-19 fires on a present row with an empty cell. Both conditions MUST be resolved before BLOCK 3 begins.

`P1 count = [n from P1 row]` SHALL be recorded. This value is the anchor for the BLOCK 5 conformance gate (F-12).

---

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type MUST be AGREE or SPLIT; F-15: Reviewers MUST match BLOCK 1.5; F-23: Issue cell MUST be populated)*

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences: underlying design tension] |

If no consensus: row `| CONSENSUS | none | -- | -- |` MUST be present. The `none` sentinel is exempt from F-23.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: AGREE or SPLIT only. Any other value fires F-14.
- `Issue`: must be substantive. An empty Issue cell fires F-23. The `none` sentinel is exempt.
- `Reviewers`: every name MUST appear in BLOCK 1.5. A name absent from BLOCK 1.5 fires F-15.
- `Synthesis` for SPLIT rows: must name the underlying design tension. Empty Synthesis fires F-11.
- `Synthesis` for CONSENSUS rows: SHALL always be `--`.

BLOCK 3 absence fires F-04.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present; F-16: Reviewer MUST match BLOCK 1.5; F-20: MUST be in 3-column table form; F-25: Finding cell MUST be populated)*

One row SHALL be present per finding raised by exactly one reviewer and not raised by any other. Output MUST use the 3-column table structure. Reviewer MUST exactly match a BLOCK 1.5 value. Finding cell MUST contain a substantive description of what was uniquely caught.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: row `| UNIQUE | none | -- |` MUST be present. The `none` token is exempt from F-16. The `--` sentinel in a no-catches Finding cell is exempt from F-25.

BLOCK 4 absence fires F-08. Non-table rendering fires F-20. Reviewer absent from BLOCK 1.5 fires F-16. A Finding cell that is present but empty is non-conformant under F-25 -- the row SHALL NOT be accepted until the Finding cell contains a specific description. A placeholder (e.g., "TBD", "see above") does not satisfy F-25.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST NOT be "full review"; F-12: entry count MUST equal P1 count; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; F-24: Action cell MUST be populated)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review."

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Action`: SHALL contain a specific corrective instruction. An empty Action cell fires F-24. A filler value (e.g., "TBD", "see above") does not satisfy F-24.
- `Re-run Scope`: MUST name reviewer(s) and section. "Full review" fires F-05. Reviewer absent from BLOCK 1.5 fires F-17.

Conformance gate: amend row count (excluding "no P1 findings" row) MUST equal `P1 count` from BLOCK 2.5. F-12 is raised on mismatch.

If zero P1 findings: row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.

---

## V-02 | Output-Format -- F-26: BLOCK 5 Section Cell Content Completeness
**Axis**: output-format
**Hypothesis**: BLOCK 5 has four columns: P1 Finding, Section, Action (gated by F-24), and Re-run Scope (gated by F-05/F-17). Row count is gated by F-12. Three of four columns have named halts. The Section column -- naming where in the design the change must be made -- has none. An amend row with an empty Section cell names what to change (Action) and who reruns (Re-run Scope) but provides no spatial anchor for locating the change. F-26 applies the present-but-empty enforcement class to the Section column of BLOCK 5. Tests whether BLOCK 5 Section cell completeness is independently detectable. V-01/V-03 will score 100 without F-26, confirming aspirational. All F-01 through F-24 from R10 V-05 are unchanged.

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
F-26  Empty amend section         -- Section cell of a BLOCK 5 amend row is present but empty
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 -- CONTENT SIGNAL CATALOGUE** *(Pre-scan only -- no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only -- expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | -- |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation. The catalogue is the canonical signal inventory; the block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry; F-18: every BLOCK 0 signal MUST be resolved; F-21: disposition row reason cell MUST be populated)*

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

A Signal detected cell that is empty is non-conformant under F-03. A Signal detected value that does not match any Signal phrase in BLOCK 0 is non-conformant under F-13. An Expert added or Reason cell that is empty is non-conformant under F-07.

If no signals were catalogued in BLOCK 0: a single row `| No signals detected | None | -- |` SHALL be present.

Signal disposition gate (F-18 + F-21): for every Signal phrase row in BLOCK 0 that is not `No domain signals detected`, one of the following conditions MUST hold before BLOCK 1 closes:
1. A domain expert row exists with a matching Signal detected value, OR
2. A disposition row is present: `| [Signal phrase] | No expert needed | [reason] |`

A BLOCK 0 signal with neither fires F-18. A disposition row with an empty reason cell fires F-21. Both conditions MUST be satisfied before BLOCK 1 closes.

After population: `BLOCK 1 domain count = [n]` SHALL be recorded.

---

**BLOCK 1.5 -- ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain row count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

The complete reviewer roster MUST be committed before any finding block is generated. Domain experts SHALL appear before stock disciplines. Source column MUST distinguish `Domain` from `Stock`. Every Domain row MUST carry a Reviewer name exactly matching an Expert added value from BLOCK 1 -- any deviation fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Conformance gate:
1. Domain row count MUST equal `BLOCK 1 domain count`. F-09 is raised on mismatch.
2. Every Domain row Reviewer name MUST exactly match an Expert added value in BLOCK 1. F-10 is raised on any mismatch.

If no domain experts were added: no Domain rows SHALL be present. Table SHALL contain 6 Stock rows only.

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

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any stock discipline reviewer fires F-01. Absence of any domain expert reviewer fires F-22. BLOCK 2.5 SHALL NOT begin until all finding tables are present.

---

**BLOCK 2.5 -- SEVERITY DISTRIBUTION** *(F-06: inverted Status MUST have Rationale row; F-19: Rationale cell MUST be populated when present)*

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

Conformance: P3 >= P2 >= P1? NO: inverted levels carry Status `inverted`. A Rationale row MUST be present -- F-06 is raised if absent.

| Note | -- |
|------|---|
| Rationale | [design area and risk type explaining the unusual severity concentration] |

A Rationale cell that is present but empty fires F-19. `P1 count = [n]` SHALL be recorded for the BLOCK 5 conformance gate.

---

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis MUST be populated; F-14: Type MUST be AGREE or SPLIT; F-15: Reviewers MUST match BLOCK 1.5; F-23: Issue MUST be populated)*

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences: underlying design tension] |

If no consensus: row `| CONSENSUS | none | -- | -- |` MUST be present. `none` sentinel is exempt from F-23.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: AGREE or SPLIT only -- any other value fires F-14.
- `Issue`: must be substantive -- empty Issue fires F-23 (none sentinel exempt).
- `Reviewers`: every name MUST appear in BLOCK 1.5 -- absent name fires F-15.
- `Synthesis` for SPLIT: must name the underlying design tension -- empty fires F-11.
- `Synthesis` for CONSENSUS: SHALL always be `--`.

BLOCK 3 absence fires F-04.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present; F-16: Reviewer MUST match BLOCK 1.5; F-20: MUST be in 3-column table form)*

One row SHALL be present per finding raised by exactly one reviewer. Output MUST use the 3-column table structure. Reviewer MUST exactly match a BLOCK 1.5 value.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: row `| UNIQUE | none | -- |` MUST be present. `none` token exempt from F-16.
BLOCK 4 absence fires F-08. Non-table rendering fires F-20. Reviewer absent from BLOCK 1.5 fires F-16.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST NOT be "full review"; F-12: entry count MUST equal P1 count; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; F-24: Action cell MUST be populated; F-26: Section cell MUST be populated)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review."

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Section`: SHALL name the specific design section or component where the change must be made. An empty Section cell is non-conformant under F-26 -- the row SHALL NOT be accepted until the Section cell names a specific design location. The "no P1 findings" sentinel row is exempt from F-26.
- `Action`: SHALL contain a specific corrective instruction. An empty Action cell fires F-24. A filler value (e.g., "TBD", "see above") does not satisfy F-24.
- `Re-run Scope`: MUST name reviewer(s) and section. "Full review" fires F-05. Reviewer absent from BLOCK 1.5 fires F-17.

Conformance gate: amend row count (excluding "no P1 findings" row) MUST equal `P1 count`. F-12 is raised on mismatch.

If zero P1 findings: row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.

---

## V-03 | Lifecycle-Emphasis -- F-27: BLOCK 2 P1 Section Named Halt
**Axis**: lifecycle-emphasis
**Hypothesis**: BLOCK 2's column conformance already contains the prose requirement "P1 rows: Section MUST be populated." This prose MUST has no named F-ID backing it -- a model that produces a P1 row with an empty Section cell passes F-01, F-02, and F-22. The C-14 pattern converts prose requirements into named detectable enforcement events; F-27 applies that pattern at the column level within BLOCK 2. A prose MUST without an F-ID is a skippable instruction; a named halt is an observable enforcement event. Tests whether converting an existing prose requirement to a named halt is independently detectable from content-completeness F-IDs at other blocks. V-01/V-02 will score 100 without F-27, confirming aspirational. All F-01 through F-24 from R10 V-05 are unchanged.

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
F-27  Unsectioned P1 finding      -- Section cell of a BLOCK 2 P1 finding row is empty or absent
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 -- CONTENT SIGNAL CATALOGUE** *(Pre-scan only -- no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only -- expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | -- |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation. The catalogue is the canonical signal inventory; the block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry; F-18: every BLOCK 0 signal MUST be resolved; F-21: disposition row reason cell MUST be populated)*

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

A Signal detected cell that is empty fires F-03. A Signal detected value absent from BLOCK 0 fires F-13. An Expert added or Reason cell that is empty fires F-07.

If no signals were catalogued: row `| No signals detected | None | -- |` SHALL be present.

Signal disposition gate (F-18 + F-21): for every Signal phrase row in BLOCK 0 (excluding `No domain signals detected`), either a matching domain expert row or a disposition row `| [phrase] | No expert needed | [reason] |` MUST be present. Missing resolution fires F-18. Empty disposition reason fires F-21. Both conditions MUST be satisfied before BLOCK 1 closes.

After population: `BLOCK 1 domain count = [n]` SHALL be recorded.

---

**BLOCK 1.5 -- ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain row count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

The complete reviewer roster MUST be committed before any finding block is generated. Domain experts first, then stock disciplines. Source column MUST distinguish `Domain` from `Stock`. Every Domain row MUST carry a Reviewer name exactly matching an Expert added value from BLOCK 1 -- any deviation fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Conformance gate:
1. Domain row count MUST equal `BLOCK 1 domain count`. F-09 is raised on mismatch.
2. Every Domain row Reviewer name MUST exactly match an Expert added value in BLOCK 1. F-10 is raised on any mismatch.

If no domain experts were added: no Domain rows. Table contains 6 Stock rows only.

---

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; F-22: every domain expert in BLOCK 1.5 MUST have a corresponding finding table; F-27: P1 Section cell MUST be populated; domain experts run first)*

A finding table MUST be generated for every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order. Domain expert reviewers SHALL run first.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [section or component] | [one actionable sentence] |

Column conformance requirements:
- `Sev`: SHALL contain exactly one of P1, P2, or P3. Any other value is non-conformant under F-02.
- `Section`: SHALL name a specific section, component, or decision. The values "the design" or "overall" are non-conformant. A Section cell that is empty on a P1 row is non-conformant under F-27 -- the row SHALL NOT be accepted until the Section cell names a specific component or decision. P2 rows: Section MUST be populated in >= 50% of P2 rows.
- A reviewer with no findings: a single row `| -- | -- | No findings. |` MUST be present.

Conformance gate: every reviewer named in BLOCK 1.5 MUST have a corresponding finding table. Absence of any stock discipline reviewer fires F-01. Absence of any domain expert reviewer fires F-22. BLOCK 2.5 SHALL NOT begin until all finding tables are present.

---

**BLOCK 2.5 -- SEVERITY DISTRIBUTION** *(F-06: inverted Status MUST have Rationale row; F-19: Rationale cell MUST be populated when present)*

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

Conformance: P3 >= P2 >= P1? NO: inverted levels carry Status `inverted`. A Rationale row MUST be present -- F-06 is raised if absent.

| Note | -- |
|------|---|
| Rationale | [design area and risk type explaining the unusual severity concentration] |

A Rationale cell that is present but empty fires F-19. `P1 count = [n]` SHALL be recorded for the BLOCK 5 conformance gate.

---

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis MUST be populated; F-14: Type MUST be AGREE or SPLIT; F-15: Reviewers MUST match BLOCK 1.5; F-23: Issue MUST be populated)*

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences: underlying design tension] |

If no consensus: row `| CONSENSUS | none | -- | -- |` MUST be present. `none` sentinel is exempt from F-23.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: AGREE or SPLIT only -- any other value fires F-14.
- `Issue`: must be substantive -- empty Issue fires F-23 (none sentinel exempt).
- `Reviewers`: every name MUST appear in BLOCK 1.5 -- absent name fires F-15.
- `Synthesis` for SPLIT: must name the underlying design tension -- empty fires F-11.
- `Synthesis` for CONSENSUS: SHALL always be `--`.

BLOCK 3 absence fires F-04.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present; F-16: Reviewer MUST match BLOCK 1.5; F-20: MUST be in 3-column table form)*

One row SHALL be present per finding raised by exactly one reviewer. Output MUST use the 3-column table structure. Reviewer MUST exactly match a BLOCK 1.5 value.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: row `| UNIQUE | none | -- |` MUST be present. `none` token exempt from F-16.
BLOCK 4 absence fires F-08. Non-table rendering fires F-20. Reviewer absent from BLOCK 1.5 fires F-16.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST NOT be "full review"; F-12: entry count MUST equal P1 count; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; F-24: Action cell MUST be populated)*

One row SHALL be present per P1 finding. Re-run Scope MUST name the specific section or component -- never "full review."

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Action`: SHALL contain a specific corrective instruction. An empty Action cell fires F-24. A filler value (e.g., "TBD", "see above") does not satisfy F-24.
- `Re-run Scope`: MUST name reviewer(s) and section. "Full review" fires F-05. Reviewer absent from BLOCK 1.5 fires F-17.

Conformance gate: amend row count (excluding "no P1 findings" row) MUST equal `P1 count`. F-12 is raised on mismatch.

If zero P1 findings: row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.

---

## V-04 | Combined (Behavior + Output-Format) -- F-25 + F-26: BLOCK 4 Finding + BLOCK 5 Section
**Axis**: combined (behavior + output-format)
**Hypothesis**: Combines V-01's F-25 (BLOCK 4 Finding cell content completeness) with V-02's F-26 (BLOCK 5 Section cell content completeness). Both apply the present-but-empty enforcement class to previously unguarded content cells at distinct lifecycle positions (BLOCK 4 vs BLOCK 5). Tests whether F-25 and F-26 are additive without interference. V-03 will score 100 without either, confirming both remain aspirational when combined. All F-01 through F-24 from R10 V-05 are unchanged.

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
F-25  Empty finding cell          -- Finding cell of a BLOCK 4 unique catch row is present but empty
F-26  Empty amend section         -- Section cell of a BLOCK 5 amend row is present but empty
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 -- CONTENT SIGNAL CATALOGUE** *(Pre-scan only -- no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only -- expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | -- |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation. Catalogue is the canonical signal inventory; block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match BLOCK 0; F-18: every BLOCK 0 signal MUST be resolved; F-21: disposition row reason MUST be populated)*

Drawing exclusively from the BLOCK 0 signal catalogue. All three cells in every row MUST be populated.

Stock table (fixed):

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

Empty Signal detected fires F-03. Signal absent from BLOCK 0 fires F-13. Empty Expert added or Reason fires F-07.

Signal disposition gate (F-18 + F-21): every BLOCK 0 signal must resolve as an expert row or a disposition row `| [phrase] | No expert needed | [reason] |`. Missing resolution fires F-18. Empty reason fires F-21.

After population: `BLOCK 1 domain count = [n]` SHALL be recorded.

---

**BLOCK 1.5 -- ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Conformance gate: Domain count MUST equal `BLOCK 1 domain count` (F-09). Every Domain Reviewer name MUST exactly match an Expert added value in BLOCK 1 (F-10). If no domain experts: 6 Stock rows only.

---

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; F-22: every domain expert in BLOCK 1.5 MUST have a corresponding finding table; domain experts run first)*

A finding table MUST be generated for every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [section or component] | [one actionable sentence] |

Column conformance:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02.
- `Section`: SHALL name a specific section, component, or decision. "The design" or "overall" are non-conformant. P1 rows: Section MUST be populated. P2 rows: Section MUST be populated in >= 50% of P2 rows.
- A reviewer with no findings: row `| -- | -- | No findings. |` MUST be present.

Conformance gate: absent stock discipline reviewer fires F-01. Absent domain expert reviewer fires F-22. BLOCK 2.5 SHALL NOT begin until all tables are present.

---

**BLOCK 2.5 -- SEVERITY DISTRIBUTION** *(F-06: inverted Status MUST have Rationale row; F-19: Rationale cell MUST be populated)*

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1? NO: inverted status. Rationale row MUST be present (F-06). Empty Rationale cell fires F-19.

| Note | -- |
|------|---|
| Rationale | [design area and risk type] |

`P1 count = [n]` SHALL be recorded.

---

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis MUST be populated; F-14: Type MUST be AGREE or SPLIT; F-15: Reviewers MUST match BLOCK 1.5; F-23: Issue MUST be populated)*

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences: underlying design tension] |

If no consensus: row `| CONSENSUS | none | -- | -- |` MUST be present. `none` sentinel exempt from F-23.
Column conformance: invalid Type fires F-14. Empty Issue fires F-23 (none exempt). Reviewer absent from BLOCK 1.5 fires F-15. Empty SPLIT Synthesis fires F-11. BLOCK 3 absence fires F-04.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present; F-16: Reviewer MUST match BLOCK 1.5; F-20: MUST be in 3-column table form; F-25: Finding cell MUST be populated)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: row `| UNIQUE | none | -- |` MUST be present. `none` exempt from F-16; `--` in Finding cell exempt from F-25.

BLOCK 4 absence fires F-08. Non-table rendering fires F-20. Reviewer absent from BLOCK 1.5 fires F-16. A Finding cell that is present but empty is non-conformant under F-25 -- the row SHALL NOT be accepted until the Finding cell contains a specific description of what was uniquely identified.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST NOT be "full review"; F-12: entry count MUST equal P1 count; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; F-24: Action cell MUST be populated; F-26: Section cell MUST be populated)*

One row SHALL be present per P1 finding.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Section`: SHALL name the specific design section or component. An empty Section cell is non-conformant under F-26 -- the row SHALL NOT be accepted until the Section cell names a specific design location. The "no P1 findings" sentinel row is exempt.
- `Action`: SHALL contain a specific corrective instruction. Empty fires F-24. Filler (e.g., "TBD") does not satisfy F-24.
- `Re-run Scope`: "Full review" fires F-05. Reviewer absent from BLOCK 1.5 fires F-17.

Conformance gate: amend row count MUST equal `P1 count`. F-12 is raised on mismatch.

If zero P1 findings: row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.

---

## V-05 | Combined Max -- F-25 + F-26 + F-27: BLOCK 4 Finding + BLOCK 5 Section + BLOCK 2 P1 Section
**Axis**: combined max
**Hypothesis**: Carries all three new F-IDs from R11: F-25 (BLOCK 4 Finding cell content completeness), F-26 (BLOCK 5 Section cell content completeness), F-27 (BLOCK 2 P1 Section named halt). F-25 and F-26 apply the present-but-empty enforcement class to unguarded content cells. F-27 converts an existing prose MUST into a named F-ID. All three target distinct lifecycle positions (BLOCK 2, BLOCK 4, BLOCK 5) with no overlap. V-04 confirms F-25+F-26 are stackable. V-01/V-02/V-03 provide individual isolation. V-05 is the R12 extraction source. All F-01 through F-24 from R10 V-05 are unchanged.

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
F-25  Empty finding cell          -- Finding cell of a BLOCK 4 unique catch row is present but empty
F-26  Empty amend section         -- Section cell of a BLOCK 5 amend row is present but empty
F-27  Unsectioned P1 finding      -- Section cell of a BLOCK 2 P1 finding row is empty or absent
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 -- CONTENT SIGNAL CATALOGUE** *(Pre-scan only -- no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only -- expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | -- |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation. Catalogue is the canonical signal inventory; block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match BLOCK 0; F-18: every BLOCK 0 signal MUST be resolved; F-21: disposition row reason MUST be populated)*

Drawing exclusively from the BLOCK 0 signal catalogue. All three cells in every row MUST be populated.

Stock table (fixed):

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

Empty Signal detected fires F-03. Signal absent from BLOCK 0 fires F-13. Empty Expert added or Reason fires F-07.

Signal disposition gate (F-18 + F-21): every BLOCK 0 signal must resolve as an expert row or a disposition row `| [phrase] | No expert needed | [reason] |`. Missing resolution fires F-18. Empty reason fires F-21.

After population: `BLOCK 1 domain count = [n]` SHALL be recorded.

---

**BLOCK 1.5 -- ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Conformance gate: Domain count MUST equal `BLOCK 1 domain count` (F-09). Every Domain Reviewer name MUST exactly match an Expert added value in BLOCK 1 (F-10). If no domain experts: 6 Stock rows only.

---

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; F-22: every domain expert in BLOCK 1.5 MUST have a corresponding finding table; F-27: P1 Section cell MUST be populated; domain experts run first)*

A finding table MUST be generated for every reviewer listed in BLOCK 1.5, in BLOCK 1.5 order.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [section or component] | [one actionable sentence] |

Column conformance:
- `Sev`: P1, P2, or P3 only. Any other value fires F-02.
- `Section`: SHALL name a specific section, component, or decision. "The design" or "overall" are non-conformant. A Section cell that is empty on a P1 row is non-conformant under F-27 -- the row SHALL NOT be accepted until the Section cell names a specific component or decision. P2 rows: Section MUST be populated in >= 50% of P2 rows.
- A reviewer with no findings: row `| -- | -- | No findings. |` MUST be present.

Conformance gate: absent stock discipline reviewer fires F-01. Absent domain expert reviewer fires F-22. BLOCK 2.5 SHALL NOT begin until all tables are present.

---

**BLOCK 2.5 -- SEVERITY DISTRIBUTION** *(F-06: inverted Status MUST have Rationale row; F-19: Rationale cell MUST be populated)*

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1? NO: inverted status. Rationale row MUST be present (F-06). Empty Rationale cell fires F-19.

| Note | -- |
|------|---|
| Rationale | [design area and risk type] |

`P1 count = [n]` SHALL be recorded.

---

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis MUST be populated; F-14: Type MUST be AGREE or SPLIT; F-15: Reviewers MUST match BLOCK 1.5; F-23: Issue MUST be populated)*

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences: underlying design tension] |

If no consensus: row `| CONSENSUS | none | -- | -- |` MUST be present. `none` sentinel exempt from F-23.
Column conformance: invalid Type fires F-14. Empty Issue fires F-23 (none exempt). Reviewer absent from BLOCK 1.5 fires F-15. Empty SPLIT Synthesis fires F-11. BLOCK 3 absence fires F-04.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present; F-16: Reviewer MUST match BLOCK 1.5; F-20: MUST be in 3-column table form; F-25: Finding cell MUST be populated)*

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: row `| UNIQUE | none | -- |` MUST be present. `none` exempt from F-16; `--` in Finding cell exempt from F-25.

BLOCK 4 absence fires F-08. Non-table rendering fires F-20. Reviewer absent from BLOCK 1.5 fires F-16. A Finding cell that is present but empty is non-conformant under F-25 -- the row SHALL NOT be accepted until the Finding cell contains a specific description of what was uniquely identified. A placeholder (e.g., "TBD", "see above") does not satisfy F-25.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST NOT be "full review"; F-12: entry count MUST equal P1 count; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; F-24: Action cell MUST be populated; F-26: Section cell MUST be populated)*

One row SHALL be present per P1 finding.

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

Column conformance:
- `Section`: SHALL name the specific design section or component. An empty Section cell is non-conformant under F-26 -- the row SHALL NOT be accepted until the Section cell names a specific design location. The "no P1 findings" sentinel row is exempt.
- `Action`: SHALL contain a specific corrective instruction. Empty fires F-24. Filler (e.g., "TBD") does not satisfy F-24.
- `Re-run Scope`: "Full review" fires F-05. Reviewer absent from BLOCK 1.5 fires F-17.

Conformance gate: amend row count MUST equal `P1 count`. F-12 is raised on mismatch.

If zero P1 findings: row `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.
