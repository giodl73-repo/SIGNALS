Written to `simulations/quest/variations/review-design-variations-R7-2026-03-14.md`.

---

## Round 7 Variations — review-design

### Variation Table

| Var | Axis | New Bet |
|-----|------|---------|
| **V-01** | lifecycle-emphasis | F-13 named halt on BLOCK 0→BLOCK 1 uncatalogued signal |
| **V-02** | output-format | F-14 vocabulary halt on BLOCK 3 Type column |
| **V-03** | behavior | F-15 cross-block reviewer identity from BLOCK 3 to BLOCK 1.5 |
| **V-04** | combined (lifecycle + output-format) | F-13 + F-14 stacked |
| **V-05** | combined max | F-13 + F-14 + F-15 — extraction source for R8 |

---

### Gap analysis behind the three new axes

**R6 V-05 left three structural holes:**

1. **BLOCK 0 gate has no named F-ID** — the "BLOCK 1 SHALL NOT add any expert whose signal is absent from BLOCK 0" constraint is the only lifecycle gate that fires without a named identifier. Every other cross-block integrity check has one: F-09 (count parity BLOCK 1→BLOCK 1.5), F-10 (identity BLOCK 1→BLOCK 1.5), F-12 (count parity BLOCK 2.5→BLOCK 5). F-13 closes this gap — same pattern as F-10, one lifecycle stage earlier.

2. **BLOCK 3 Type column has no vocabulary halt** — AGREE/SPLIT are the only valid values but no halt fires on invalid entries. F-02 fires when Sev is outside {P1, P2, P3}; F-05 fires when Re-run Scope contains "full review." The Type column is the one constrained-vocabulary column without an equivalent. F-14 introduces a new enforcement class: **constrained-vocabulary integrity** on a categorical column.

3. **BLOCK 3 Reviewers column has no cross-block identity check** — reviewer names appear in the consensus table but no halt verifies they exist in BLOCK 1.5. F-10 caught orphaned experts at BLOCK 1.5 (relative to BLOCK 1). F-15 extends that same identity-integrity pattern one stage later: **phantom reviewer detection** at BLOCK 3 relative to BLOCK 1.5.

**Research question for R7:** Are F-13 and F-14 additive (V-04 > V-01 and V-02 individually)? Does F-15 stack cleanly on top, or does three-halt complexity degrade simpler dimensions?
erts at BLOCK 1.5 relative to BLOCK 1; no equivalent halt covers phantom reviewers in BLOCK 3 relative to BLOCK 1.5.

**V-01 (F-13: BLOCK 0 uncatalogued signal)** — the only lifecycle gate without a named F-ID. F-13 fires when BLOCK 1 references a signal phrase not present in the BLOCK 0 catalogue. Converts the prose SHALL gate into a detectable, precisely localizable enforcement event.

**V-02 (F-14: BLOCK 3 Type vocabulary)** — new enforcement class. F-14 fires when a Type cell in BLOCK 3 contains a value other than AGREE or SPLIT. This is the first F-ID that enforces constrained vocabulary on a categorical column, distinct from all prior classes (structural presence, content completeness, count parity, identity integrity).

**V-03 (F-15: BLOCK 3 phantom reviewer)** — extends identity integrity downstream. F-14 fires when a reviewer name appearing in the BLOCK 3 Reviewers column has no matching Reviewer value in BLOCK 1.5. The same pattern as F-10 (BLOCK 1.5 orphan relative to BLOCK 1), applied one block later in the lifecycle.

**V-04** combines V-01 + V-02: BLOCK 0 integrity (better signal traceability) and BLOCK 3 vocabulary (better type enforcement) address distinct failure surfaces — tests if they are additive.

**V-05** is the full R7 ceiling: all three axes stacked. Intended as the extraction source for R8 criterion candidates. Any new structural pattern that consistently improves output quality over V-04 is a C-24+ candidate.

**Research questions for R7:**
- V-01 isolation: Does a named F-13 halt on BLOCK 0→BLOCK 1 violations produce tighter C-21 compliance than the prose SHALL gate alone?
- V-02 isolation: Does F-14 vocabulary enforcement on the Type column improve C-22 output quality (fewer ad-hoc type values) without degrading other criteria?
- V-03 isolation: Does F-15 phantom reviewer detection reduce BLOCK 3 reviewer discrepancies, and does it interact with F-10?
- V-04 vs V-02+V-03: Are F-13 and F-14 additive improvements, or does one subsume the other's enforcement surface?
- V-05 vs V-04: Does F-15 stack additively with F-13+F-14, or does the three-halt combination introduce overhead that degrades output quality on simpler dimensions?

---

## V-01 | Lifecycle Emphasis — F-13 Named Halt on BLOCK 0→BLOCK 1 Signal Integrity
**Axis**: lifecycle-emphasis
**Hypothesis**: R6 V-05's BLOCK 0 gate reads "BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue." This formal SHALL constraint satisfies C-21 (BLOCK 0 pre-scan with cross-block gate). However, the constraint has no named failure ID. Every other cross-block integrity check in the protocol is backed by a named halt: F-09 (BLOCK 1→BLOCK 1.5 count parity), F-10 (BLOCK 1→BLOCK 1.5 identity integrity), F-12 (BLOCK 2.5→BLOCK 5 count parity). The BLOCK 0→BLOCK 1 gate is the only lifecycle constraint that fires without a named identifier, making violations prose-detectable but not precisely localizable. F-13 ("BLOCK 1 references uncatalogued signal") converts the SHALL constraint into a named enforcement event: the exact Signal detected value that failed the cross-block check can be identified and corrected before the block closes. All structural blocks, table forms, and F-01 through F-12 are unchanged from R6 V-05. The single variable is whether a named F-ID on the BLOCK 0→BLOCK 1 gate measurably tightens C-21 enforcement.

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
F-13  Uncatalogued signal         — a Signal detected value in BLOCK 1 has no matching Signal phrase entry in the BLOCK 0 catalogue
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 — CONTENT SIGNAL CATALOGUE** *(Pre-scan only — no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only — expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | — |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation. The catalogue is the canonical signal inventory for this review; the block SHALL NOT be closed until all rows are resolved.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry)*

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

A Signal detected cell that is empty is non-conformant under F-03. A Signal detected value that does not match any Signal phrase in BLOCK 0 is non-conformant under F-13 — the cell SHALL NOT be accepted until the Signal phrase appears in BLOCK 0. An Expert added or Reason cell that is empty is non-conformant under F-07.
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

---

## V-02 | Output Format — F-14 Vocabulary Halt on BLOCK 3 Type Column
**Axis**: output-format
**Hypothesis**: R6 V-05's BLOCK 3 uses a 4-column table with a `Type` column containing AGREE or SPLIT. The valid vocabulary is stated implicitly by example but no named halt fires when an invalid type appears. Every other constrained-value column in the output architecture has a named halt on invalid values: F-02 fires when Sev is outside {P1, P2, P3}; F-05 fires when Re-run Scope contains "full review." The Type column is the only constrained-vocabulary column without an equivalent halt. F-14 ("BLOCK 3 Type cell contains value other than AGREE or SPLIT") introduces a new enforcement class — constrained-vocabulary integrity on a categorical column — distinct from all prior F-ID classes: structural presence (F-01, F-04, F-08), content completeness (F-11), count parity (F-09, F-12), and identity integrity (F-10). All other blocks are unchanged from R6 V-05. The single variable is whether a named vocabulary halt on the Type column improves BLOCK 3 structural discipline.

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
F-14  Invalid consensus type      — BLOCK 3 contains a Type cell whose value is neither AGREE nor SPLIT
```

Halt and restructure immediately if any of F-01 through F-12 or F-14 fires.

---

**BLOCK 0 — CONTENT SIGNAL CATALOGUE** *(Pre-scan only — no tables filled, no experts assigned)*

Read the full design document. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, record one row. This is a detection pass only — expert assignment happens in BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals detected: row `| No domain signals detected | — |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. The catalogue is the canonical signal inventory for this review.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required; signals must trace to BLOCK 0)*

Drawing exclusively from the BLOCK 0 signal catalogue, one domain expert row SHALL be added per catalogued signal that warrants domain expertise. Every row requires all three cells populated.

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

Commit the full reviewer roster before any finding is generated. Domain experts listed first, then stock disciplines. Source column distinguishes `Stock` from `Domain`. Every Domain row must carry a Reviewer name that exactly matches an Expert added value from BLOCK 1 — any mismatch fires F-10.

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

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required; F-11: SPLIT Synthesis cell must be populated; F-14: Type cell must be AGREE or SPLIT)*

Synthesis is a dedicated column. A blank Synthesis cell for a SPLIT row fires F-11. CONSENSUS rows carry `—` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | — |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension — not a restatement of opposing positions] |

If no consensus: row `| CONSENSUS | none | — | — |`
If no splits: omit SPLIT rows entirely.

Column contracts:
- `Type`: MUST contain exactly AGREE or SPLIT. Any other value fires F-14 — halt and correct the row before continuing.
- `Synthesis` for SPLIT rows: must name the underlying design tension. Restatement of opposing positions is not sufficient. Empty Synthesis cell fires F-11 — halt and write synthesis before continuing.
- `Synthesis` for CONSENSUS rows: always `—`.

F-04 fires if this block is omitted. F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside the {AGREE, SPLIT} vocabulary.

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

## V-03 | Behavior — F-15 Cross-Block Reviewer Identity from BLOCK 3 to BLOCK 1.5
**Axis**: behavior
**Hypothesis**: R6 V-05's BLOCK 3 4-column table has a `Reviewers` column that names individual reviewers in both AGREE rows (comma-separated) and SPLIT rows (A: position / B: position). No cross-block check verifies that these names exist in BLOCK 1.5. A reviewer named in BLOCK 3 who is not in the BLOCK 1.5 roster is a "phantom reviewer" — present in the consensus analysis but never part of the actual review. F-10 caught orphaned experts at the BLOCK 1.5 level (Domain row name not matching any BLOCK 1 Expert added value). F-15 extends the same identity-integrity pattern one lifecycle stage later: a reviewer name appearing in the BLOCK 3 Reviewers column that has no matching Reviewer value in BLOCK 1.5 is non-conformant under F-15. This introduces the fourth distinct block covered by identity-integrity F-IDs: BLOCK 1 (F-03 signal trace), BLOCK 1.5 (F-10 orphan detection), and now BLOCK 3 (F-15 phantom reviewer). All other blocks are unchanged from R6 V-05. The single variable is whether cross-block reviewer identity enforcement at BLOCK 3 reduces phantom-reviewer errors.

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
F-15  Phantom reviewer            — BLOCK 3 Reviewers column contains a name that has no matching Reviewer value in BLOCK 1.5
```

Halt and restructure immediately if any of F-01 through F-12 or F-15 fires.

---

**BLOCK 0 — CONTENT SIGNAL CATALOGUE** *(Pre-scan only — no tables filled, no experts assigned)*

Read the full design document. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, record one row. This is a detection pass only — expert assignment happens in BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals detected: row `| No domain signals detected | — |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. The catalogue is the canonical signal inventory for this review.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected required; F-07: Expert added and Reason required; signals must trace to BLOCK 0)*

Drawing exclusively from the BLOCK 0 signal catalogue, one domain expert row SHALL be added per catalogued signal that warrants domain expertise. Every row requires all three cells populated.

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

Commit the full reviewer roster before any finding is generated. Domain experts listed first, then stock disciplines. Source column distinguishes `Stock` from `Domain`. Every Domain row must carry a Reviewer name that exactly matches an Expert added value from BLOCK 1 — any mismatch fires F-10.

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

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: always required; F-11: SPLIT Synthesis cell must be populated; F-15: all reviewer names in Reviewers column must match BLOCK 1.5)*

Synthesis is a dedicated column. A blank Synthesis cell for a SPLIT row fires F-11. CONSENSUS rows carry `—` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | — |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension — not a restatement of opposing positions] |

If no consensus: row `| CONSENSUS | none | — | — |`
If no splits: omit SPLIT rows entirely.

Column contracts:
- `Reviewers`: every individual reviewer name referenced in this column must appear in the BLOCK 1.5 Reviewer column. For AGREE rows, each comma-separated name must be in BLOCK 1.5. For SPLIT rows, both reviewer names (A and B) must be in BLOCK 1.5. A name with no BLOCK 1.5 match fires F-15 — halt, identify the phantom name, and correct the row.
- `Synthesis` for SPLIT rows: must name the underlying design tension. Restatement of opposing positions is not sufficient. Empty Synthesis cell fires F-11 — halt and write synthesis before continuing.
- `Synthesis` for CONSENSUS rows: always `—`.

F-04 fires if this block is omitted. F-11 fires on any SPLIT row with an empty Synthesis cell. F-15 fires on any Reviewers cell containing a name absent from BLOCK 1.5.

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

## V-04 | Combined (Lifecycle + Output-Format) — F-13 + F-14: Signal Integrity and Type Vocabulary
**Axis**: combined (lifecycle-emphasis + output-format)
**Hypothesis**: Combines V-01's F-13 (BLOCK 0→BLOCK 1 uncatalogued signal halt) with V-02's F-14 (BLOCK 3 Type column vocabulary halt). F-13 targets the BLOCK 0→BLOCK 1 integrity gap: the only lifecycle constraint without a named F-ID. F-14 targets the BLOCK 3 Type column vocabulary gap: the only constrained-value column without a named halt. These address distinct failure surfaces — F-13 at the signal detection lifecycle stage (BLOCK 0 to BLOCK 1), F-14 at the consensus analysis output stage (BLOCK 3 column) — with no overlap in what they enforce. Full F-01 through F-12 enforcement stack, formal declarative register, BLOCK 0 pre-scan, 4-column BLOCK 3, domain-first ordering, Source column, BLOCK 5 4-column amend table from R6 V-05 included at baseline. Expected score: 100 on v7. Tests whether the two new F-ID classes are additive and whether combined deployment reveals any interaction effects.

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
F-13  Uncatalogued signal         — a Signal detected value in BLOCK 1 has no matching Signal phrase entry in the BLOCK 0 catalogue
F-14  Invalid consensus type      — BLOCK 3 contains a Type cell whose value is neither AGREE nor SPLIT
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 — CONTENT SIGNAL CATALOGUE** *(Pre-scan only — no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only — expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | — |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation — the violating row SHALL NOT be accepted until a matching Signal phrase is added to this catalogue. The catalogue is the canonical signal inventory for this review.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry)*

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

A Signal detected cell that is empty is non-conformant under F-03. A Signal detected value that does not match any Signal phrase in BLOCK 0 is non-conformant under F-13. An Expert added or Reason cell that is empty is non-conformant under F-07.
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

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type cell MUST be AGREE or SPLIT)*

Synthesis is a dedicated column. A blank Synthesis cell for any SPLIT row fires F-11. CONSENSUS rows SHALL carry `—` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | — |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension — not a restatement of opposing positions] |

If no consensus: a row `| CONSENSUS | none | — | — |` MUST be present.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: SHALL contain exactly AGREE or SPLIT. Any other value is non-conformant under F-14 — the row SHALL NOT be accepted until the Type cell is corrected.
- `Synthesis` for SPLIT rows: MUST name the underlying design tension. A restatement of the opposing positions is non-conformant. An empty Synthesis cell is non-conformant under F-11 — the block SHALL NOT be closed until all SPLIT row Synthesis cells are populated.
- `Synthesis` for CONSENSUS rows: SHALL always be `—`.

BLOCK 3 absence fires F-04. F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside the {AGREE, SPLIT} vocabulary.

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

---

## V-05 | Combined Maximum — F-13 + F-14 + F-15: Full R7 Ceiling
**Axis**: combined (lifecycle-emphasis + output-format + behavior)
**Hypothesis**: Maximum R7 form. F-13 (BLOCK 0→BLOCK 1 uncatalogued signal) closes the last lifecycle gate without a named F-ID. F-14 (BLOCK 3 Type vocabulary) closes the last constrained-value column without a named halt. F-15 (BLOCK 3 phantom reviewer) extends identity integrity to the consensus block — the same cross-block pattern as F-10 (BLOCK 1.5 orphan from BLOCK 1), applied one lifecycle stage later. Each F-ID targets a distinct failure class: F-13 is a cross-block signal-trace integrity failure; F-14 is a constrained-vocabulary column failure; F-15 is a cross-block reviewer-identity failure. Together, F-01 through F-15 cover every structural gap identified through R6. The complete formal register (C-23), BLOCK 0 pre-scan (C-21), and 4-column BLOCK 3 (C-22) from R6 V-05 are included at baseline. This variation is the intended extraction source for R8 criterion candidates — any new structural property that achieves consistent output improvement over V-04 is a C-24+ candidate. Expected score: 100 on v7.

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
F-13  Uncatalogued signal         — a Signal detected value in BLOCK 1 has no matching Signal phrase entry in the BLOCK 0 catalogue
F-14  Invalid consensus type      — BLOCK 3 contains a Type cell whose value is neither AGREE nor SPLIT
F-15  Phantom reviewer            — BLOCK 3 Reviewers column contains a name that has no matching Reviewer value in BLOCK 1.5
```

The output SHALL halt and resolve any firing conformance failure before continuing.

---

**BLOCK 0 — CONTENT SIGNAL CATALOGUE** *(Pre-scan only — no tables filled, no experts assigned)*

The full design document SHALL be read before any domain expert is assigned. For every phrase, concept, or decision signalling a specialized domain not covered by the 6 stock disciplines, one row SHALL be recorded. This block is detection only — expert assignment is deferred to BLOCK 1.

| Signal phrase | Domain category |
|---------------|-----------------|
| [exact phrase or concept from the design] | [security / data / compliance / accessibility / platform / protocol / ...] |

If no domain signals are detected: row `| No domain signals detected | — |`

Gate: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue. F-13 is raised on any such violation — the violating row SHALL NOT be accepted until a matching Signal phrase is added to this catalogue and verified. The catalogue is the canonical signal inventory for this review; the block SHALL NOT be closed until all detected signals are recorded.

---

**BLOCK 1 — EXPERT ROSTER** *(F-03: Signal detected MUST be populated; F-07: Expert added and Reason MUST be populated; F-13: Signal detected MUST match a BLOCK 0 catalogue entry)*

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

A Signal detected cell that is empty is non-conformant under F-03. A Signal detected value that does not match any Signal phrase in BLOCK 0 is non-conformant under F-13 — the row SHALL NOT be accepted until the Signal phrase appears in the BLOCK 0 catalogue. An Expert added or Reason cell that is empty is non-conformant under F-07.
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

**BLOCK 3 — CONSENSUS AND SPLIT ANALYSIS** *(F-04: MUST be present; F-11: SPLIT Synthesis cell MUST be populated; F-14: Type cell MUST be AGREE or SPLIT; F-15: Reviewers names MUST match BLOCK 1.5)*

Synthesis is a dedicated column. A blank Synthesis cell for any SPLIT row fires F-11. CONSENSUS rows SHALL carry `—` in the Synthesis column.

| Type | Issue | Reviewers | Synthesis |
|------|-------|-----------|-----------|
| CONSENSUS | [issue summary] | [Reviewer A], [Reviewer B] | — |
| SPLIT | [contested decision] | A: [pos] / B: [pos] | [1-3 sentences naming the underlying design tension — not a restatement of opposing positions] |

If no consensus: a row `| CONSENSUS | none | — | — |` MUST be present.
If no splits: SPLIT rows SHALL be omitted.

Column conformance:
- `Type`: SHALL contain exactly AGREE or SPLIT. Any other value is non-conformant under F-14 — the row SHALL NOT be accepted until the Type cell is corrected.
- `Reviewers`: every reviewer name in this column MUST appear in the BLOCK 1.5 Reviewer column. For AGREE rows, each comma-separated name MUST be in BLOCK 1.5. For SPLIT rows, both reviewer names MUST be in BLOCK 1.5. A name absent from BLOCK 1.5 is non-conformant under F-15 — the row SHALL NOT be accepted until all reviewer names are verified against BLOCK 1.5.
- `Synthesis` for SPLIT rows: MUST name the underlying design tension. A restatement of the opposing positions is non-conformant. An empty Synthesis cell is non-conformant under F-11 — the block SHALL NOT be closed until all SPLIT row Synthesis cells are populated.
- `Synthesis` for CONSENSUS rows: SHALL always be `—`.

BLOCK 3 absence fires F-04. F-11 fires on any SPLIT row with an empty Synthesis cell. F-14 fires on any Type cell outside {AGREE, SPLIT}. F-15 fires on any Reviewers cell containing a name absent from BLOCK 1.5.

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
