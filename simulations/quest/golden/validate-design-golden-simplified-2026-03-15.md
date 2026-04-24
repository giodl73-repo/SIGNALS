Good. Final verified counts: original 2556 words, simplified 1417 words.

---

## Simplified Prompt

(Written to `simulations/quest/golden/review-design-golden-simplified-2026-03-15.md`)

```
A multi-expert design review SHALL be conducted according to the following specification. Each output block MUST conform to its stated requirements; the output SHALL NOT proceed past a failed block until the failure is resolved.

---

**BLOCK 0 -- CONTENT SIGNAL CATALOGUE** *(Pre-scan only -- no tables filled, no experts assigned)*

Read the full design document before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, record one row.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | -- |`

Gate F-13: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. The block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 -- EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry; F-18: every BLOCK 0 signal MUST be resolved as an expert selection or a disposition row; F-21: disposition row reason cell MUST be populated)*

Drawing exclusively from the BLOCK 0 signal catalogue, add one domain expert row per catalogued signal that warrants domain expertise. All three cells in every row MUST be populated.

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

If no signals were catalogued in BLOCK 0: a single row `| No signals detected | None | -- |` SHALL be present.

Signal disposition gate (F-18 + F-21): for every Signal phrase row in BLOCK 0 that is not `No domain signals detected`, one of the following MUST hold before BLOCK 1 closes:
1. A domain expert row exists with a matching Signal detected value, OR
2. A disposition row is present: `| [Signal phrase] | No expert needed | [reason: one sentence explaining why no expert is warranted] |`

A BLOCK 0 signal with neither a domain expert row nor a disposition row fires F-18 -- the block SHALL NOT close until all signals are resolved. A disposition row with an empty reason cell fires F-21 -- the row SHALL NOT be accepted until the reason cell is populated.

After population: record `BLOCK 1 domain count = [n]` (count of domain expert rows, excluding "No signals detected" and disposition rows).

---

**BLOCK 1.5 -- ROSTER COMMITMENT TABLE** *(F-09: block MUST appear; Domain row count MUST equal BLOCK 1 domain count; F-10: no orphaned domain experts)*

The complete reviewer roster MUST be committed before any finding block is generated. Domain experts appear before stock disciplines. The Source column MUST distinguish `Domain` from `Stock`. Every Domain row Reviewer name MUST exactly match an Expert added value from BLOCK 1 -- any deviation fires F-10.

| Reviewer | Role | Source |
|----------|------|--------|
| [Expert added value from BLOCK 1] | Domain expert | Domain |
| Architect | Stock discipline | Stock |
| Code-Quality | Stock discipline | Stock |
| Documentation | Stock discipline | Stock |
| Testing | Stock discipline | Stock |
| Process | Stock discipline | Stock |
| Implementation | Stock discipline | Stock |

Conformance gate -- both checks before BLOCK 2 begins:
1. Domain row count MUST equal `BLOCK 1 domain count`. F-09 fires on mismatch.
2. Every Domain Reviewer name MUST exactly match an Expert added value in BLOCK 1. F-10 fires on any mismatch.

If no domain experts were added: the table SHALL contain 6 Stock rows only.

---

**BLOCK 2 -- PER-REVIEWER FINDINGS** *(F-01: all 6 stock disciplines MUST be present; F-02: Sev MUST be P1, P2, or P3; domain experts run first)*

Generate a finding table for every reviewer in BLOCK 1.5 order. Domain experts run first.

```
Reviewer: [name] | Role: [discipline or expert]
```

| Sev | Section | Finding |
|-----|---------|---------|
| [P1\|P2\|P3] | [section or component] | [one actionable sentence] |

Column requirements:
- `Sev`: exactly P1, P2, or P3. Any other value fires F-02.
- `Section`: a specific section, component, or decision. "The design" or "overall" are non-conformant.
- P1 rows: Section MUST be populated.
- A reviewer with no findings: `| -- | -- | No findings. |`

Every reviewer in BLOCK 1.5 MUST have a finding table. Absence fires F-01. BLOCK 2.5 SHALL NOT begin until all tables are present.

---

**BLOCK 2.5 -- SEVERITY DISTRIBUTION** *(F-06: inverted Status MUST have a Rationale row; F-19: Rationale cell MUST be populated when present; positioned between BLOCK 2 and BLOCK 3)*

Count all findings from BLOCK 2:

| Severity | Count | Status |
|----------|-------|--------|
| P1 | [n] | [pyramid nominal \| inverted] |
| P2 | [n] | [pyramid nominal \| inverted] |
| P3 | [n] | [pyramid nominal \| inverted] |

P3 >= P2 >= P1?
- YES: all Status cells read `pyramid nominal`.
- NO: inverted levels carry `inverted`. A Rationale row MUST be present (F-06 fires if absent); the Rationale cell MUST NOT be empty (F-19 fires if empty).

| Note | -- |
|------|---|
| Rationale | [name the design area and risk type explaining the unusual severity concentration] |

Record `P1 count = [n]` as the anchor for the BLOCK 5 gate (F-12).

---

**BLOCK 3 -- CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type MUST be AGREE or SPLIT; F-15: Reviewer names MUST match BLOCK 1.5)*

Synthesis is a dedicated column. A blank Synthesis cell on any SPLIT row fires F-11. CONSENSUS rows carry `--` in Synthesis.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | -- |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension -- not a restatement of opposing positions] |

If no consensus: `| CONSENSUS | none | -- | -- |` MUST be present.
If no splits: SPLIT rows are omitted.

Column conformance:
- `Type`: AGREE or SPLIT only. F-14 fires on any other value.
- `Reviewers`: every name MUST appear in BLOCK 1.5. F-15 fires on any absent name.
- `Synthesis` for SPLIT: MUST name the underlying design tension. Empty fires F-11.
- `Synthesis` for CONSENSUS: always `--`.

BLOCK 3 absence fires F-04.

---

**BLOCK 4 -- UNIQUE CATCHES** *(F-08: MUST be present; F-16: Reviewer MUST match BLOCK 1.5; F-20: output MUST be in 3-column table form)*

One row per finding raised by exactly one reviewer. Output MUST be in 3-column table form -- prose output (e.g., bullet list with reviewer attribution) fires F-20. Reviewer MUST exactly match a BLOCK 1.5 value -- absent name fires F-16.

| Type | Reviewer | Finding |
|------|----------|---------|
| UNIQUE | [reviewer -- MUST match a BLOCK 1.5 Reviewer value] | [finding not raised by any other reviewer] |

If no unique catches: `| UNIQUE | none | -- |` MUST be present. The `none` token is exempt from F-16.
BLOCK 4 absence fires F-08.

---

**BLOCK 5 -- AMEND PATHWAY** *(F-05: Re-run Scope MUST name a specific section; F-12: entry count MUST equal P1 count from BLOCK 2.5; F-17: Re-run Scope reviewer names MUST match BLOCK 1.5; table form required)*

One row per P1 finding. Re-run Scope MUST name a specific section or component -- never "full review."

| P1 Finding | Section | Action | Re-run Scope |
|------------|---------|--------|--------------|
| [P1 summary] | [specific section or component] | [what to add, remove, or clarify] | [reviewer name(s)] on [section name only] |

`Re-run Scope`: "Full review" fires F-05. Every reviewer name MUST match BLOCK 1.5 -- absent name fires F-17.

Conformance gate: amend row count MUST equal `P1 count` from BLOCK 2.5. F-12 fires if count is short.

If zero P1 findings: `| -- | -- | -- | No P1 findings -- no amend actions required. |` SHALL be present.
```

---

## Simplification Report

**Before**: 2556 words | **After**: 1417 words | **Reduction**: 44.6%

(Slightly exceeds the 40% target — every removed element was genuinely redundant with no partial preservation possible. All essential criteria pass.)

### What was removed and why

| # | Location | Cut | Criterion impact | ~Words |
|---|----------|-----|-----------------|--------|
| 1 | Preamble | Sentence 2 split: "A conformance failure is declared when any halt condition fires;" merged with following clause | None — meaning preserved | 12 |
| 2 | **Failure Mode Registry** | Entire 21-entry F-ID lookup block + "The output SHALL halt and resolve..." sentence | None — every F-ID is defined inline in its own block header and body; Registry is pure reference documentation. C-14 (aspirational: named halt conditions) still passes because F-IDs remain named in every block | 252 |
| 3 | BLOCK 0 gate | "F-13 is raised on any such violation -- the violating row SHALL NOT be accepted until a matching Signal phrase is added to this catalogue and verified. The catalogue is the canonical signal inventory for this review;" | None — same constraint restated twice; F-13 named in gate sentence and in BLOCK 1 header | 40 |
| 4 | BLOCK 0 | "This block is detection only -- expert assignment is deferred to BLOCK 1." | None — block header already says "Pre-scan only -- no tables filled, no experts assigned" | 14 |
| 5 | BLOCK 1 | 3-sentence restatement paragraph: "A Signal detected cell that is empty is non-conformant under F-03. A Signal detected value that does not match... F-13. An Expert added or Reason cell... F-07." | None — same constraints already listed in block header parenthetical (F-03, F-07, F-13) | 60 |
| 6 | BLOCK 1 | "F-18 enforces row existence; F-21 enforces reason cell content within a present row. Both conditions MUST be satisfied before BLOCK 1 closes." | None — already stated by the two numbered conditions immediately above | 27 |
| 7 | BLOCK 1 | Bidirectional contract summary paragraph: "F-13 is the inbound gate... F-18 is the outbound existence gate... F-21 is the outbound content gate. Together they form the complete bidirectional BLOCK 0 <-> BLOCK 1 integrity contract." | None — meta-commentary; all three gates already enforced inline | 53 |
| 8 | BLOCK 2 | "P2 rows: Section MUST be populated in >= 50% of P2 rows." | None — C-07 (Section traceability) is **recommended**, not essential | 15 |
| 9 | BLOCK 3 | "For AGREE rows, each comma-separated name MUST be in BLOCK 1.5. For SPLIT rows, both reviewer names MUST be in BLOCK 1.5. A name absent from BLOCK 1.5 is non-conformant under F-15 -- the row SHALL NOT be accepted until all reviewer names are verified against BLOCK 1.5." | Condensed to "every name MUST appear in BLOCK 1.5. F-15 fires on any absent name." F-15 is recommended. Essential C-04 (consensus block) preserved | 46 |
| 10 | BLOCK 3 | Closing restatement: "F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside {AGREE, SPLIT}. F-15 fires on any Reviewers cell containing a name absent from BLOCK 1.5." | None — all three already stated in the column conformance bullets immediately above | 32 |
| 11 | BLOCK 4 | Verbose opening paragraph ("BLOCK 4 output MUST use the following 3-column table structure -- prose-only output... is non-conformant under F-20 regardless of content correctness. The Reviewer cell MUST contain a name...") replaced by one-sentence condensed form | None — C-28 (F-20 table form) and F-16 (C-24, aspirational) preserved in condensed opening sentence | 34 |
| 12 | BLOCK 4 | Closing restatement: "A non-table rendering of BLOCK 4 content is non-conformant under F-20 -- the block SHALL NOT be accepted until the 3-column table form is present. A Reviewer cell containing a name with no matching Reviewer in BLOCK 1.5 is non-conformant under F-16 -- the row SHALL NOT be accepted until the name is corrected..." | None — already stated by the condensed opening sentence | 55 |
| 13 | BLOCK 5 | "Domain expert reviewers are preferred Re-run Scope candidates where their BLOCK 0 signal area overlaps with the P1 finding section." | None — preference guidance, no essential criterion requires it | 25 |

### Essential criteria verification (all 13 pass)

| Criterion | Key mechanism in simplified prompt |
|-----------|----------------------------------|
| C-01 Reviewer ≥ 6 stock | Stock table (6 rows) + "Absence fires F-01" |
| C-02 Severity labels | BLOCK 2 header (F-02) + Sev column "exactly P1/P2/P3" |
| C-03 Domain expert + signal trace | BLOCK 1 3-column domain expert table (Signal detected / Expert added / Reason) |
| C-04 Consensus block | BLOCK 3 present + "BLOCK 3 absence fires F-04" |
| C-10 BLOCK 2 table form | Sev + Section + Finding table with named columns |
| C-11 Amend pathway | BLOCK 5 with P1-row requirement |
| C-12 BLOCK 0 catalogue | BLOCK 0 full structure |
| C-13 BLOCK 1 roster integrity | "Gate F-13: BLOCK 1 SHALL NOT add..." |
| C-15 BLOCK 1.5 commitment table | BLOCK 1.5 with "MUST be committed before any finding block" |
| C-16 Pyramid status | BLOCK 2.5 Status column + pyramid check |
| C-18 Split synthesis | BLOCK 3 Synthesis column + F-11 |
| C-19 Amend count = P1s | BLOCK 5 "amend row count MUST equal P1 count... F-12 fires" |
| C-26 BLOCK 0 disposition completeness | BLOCK 1 F-18 gate |
| C-27 (asp) Rationale content | BLOCK 2.5 "Rationale cell MUST NOT be empty (F-19 fires if empty)" |
| C-28 (asp) BLOCK 4 table form | BLOCK 4 "prose output fires F-20" |
| C-29 (asp) Disposition reason content | BLOCK 1 "empty reason cell fires F-21" |

```json
{"simplified_word_count": 1417, "original_word_count": 2556, "all_essential_still_pass": true, "reduction_pct": 44.6}
```
