Now I have all five variants. Let me score each against the v13 rubric systematically.

---

# campaign-blueprint — Round 13 Scorecard (v13 Rubric)

## Rubric Baseline Recall

| Layer | Points | Description |
|-------|--------|-------------|
| v11 ceiling (C-01 through C-33) | 203 | All essential criteria + C-31 Req-ID grounding + C-32 gap diagnosis + C-33 conviction hypothesis |
| v12 additions (C-34 + C-35) | +10 | Structural CONVICTION DELTA table + structural CONVICTION GAP DIAGNOSIS table |
| v12 ceiling | **213** | V-04 R12 held this |
| v13 additions (C-36 + C-37) | +10 | Structural TRACEABILITY AUDIT table + three-table structural chain |
| v13 ceiling | **223** | Target for all R13 variants |

---

## Criterion Key (Aspirational, v11–v13)

| Crit | Pts | Test |
|------|-----|------|
| C-33 | 5 | CAMPAIGN CONVICTION HYPOTHESIS as item 0 with named barrier + falsification conditions |
| C-31 | 5 | CONVICTION DELTA each version cites a Req-ID (no impressionistic-only rows) |
| C-32 | 5 | CONVICTION GAP DIAGNOSIS subsection with artifact sub-section naming + scout namespace |
| C-34 | 5 | CONVICTION DELTA: 4-column structural table with in-cell Amplification chain template pre-placed in each data row |
| C-35 | 5 | CONVICTION GAP DIAGNOSIS: 6-column structural table with Register found / Register declared as distinct columns; three artifact rows pre-declared |
| C-36 | 5 | TRACEABILITY AUDIT: 6-column structural table with pre-declared named rows matching SETUP; N+blank Gap = visible structural incompleteness |
| C-37 | 5 | All three structural tables (C-34 + C-35 + C-36) simultaneously in a single variant |

---

## V-01 — Mechanical C-34+C-35+C-36 Union

**Structure:** V-04 R12 body (C-34 + C-35 confirmed) + V-03 R12 TRACEABILITY AUDIT table grafted into REFLECTION.

### C-36 Evaluation

The TRACEABILITY AUDIT table (lines 252–254):

```
| Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
|--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
|        |                             | Y / N                    |                               |            |                 |
```

- Column count: 6 ✓
- Column names exactly match C-36 spec ✓
- Pre-declared row: template placeholder row — no named Req-ID identifiers (blank Req-ID cell)
- Post-table prose: defines each column, including "N row with blank Gap cell is a structural incompleteness" ✓

C-36 FULL / NO CREDIT question: C-36 requires "each row pre-declared as a named entry, matching the scout-requirements friction sources." The rubric explicitly states "V-03 (R12) earns FULL" — and V-03 R12 used this exact form (template placeholder, no named Req-IDs). V-01 replicates that form verbatim. **C-36: FULL** (rubric precedent).

### D13 Column-Count Check

| Table | Columns | Pass? |
|-------|---------|-------|
| CONVICTION DELTA (lines 277–281) | 4: Version \| Conviction established \| Grounding Req-ID(s) \| Amplification chain | C-34 PASS |
| CONVICTION GAP DIAGNOSIS (lines 320–324) | 6: Artifact \| Sub-section \| Register found \| Register declared \| Scout sub-skill \| Evidence needed | C-35 PASS |
| TRACEABILITY AUDIT (lines 252–254) | 6: Req-ID \| Scout-Requirements Friction \| Must-have found \| Must-have text \| Gap \| Scout namespace | C-36 PASS |

C-37: all three pass → **C-37: FULL**

### V-01 Criterion Scores

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-33 | FULL | Item 0: Hypothesis + Falsification conditions, placed before item 1 ✓ |
| C-31 | FULL | Grounding Req-ID(s) column in 4-col CONVICTION DELTA table, per-row requirement ✓ |
| C-32 | FULL | CONVICTION GAP DIAGNOSIS with subsection naming + scout sub-skill column ✓ |
| C-34 | FULL | 4-col table, in-cell template "[Req-ID]'s [specific factual claim]..." pre-placed in each of 3 data rows ✓ |
| C-35 | FULL | 6-col table, Register found / Register declared distinct, three artifact rows pre-declared ✓ |
| C-36 | FULL | 6-col table, V-03 R12 form (earns FULL per rubric precedent) ✓ |
| C-37 | FULL | All three structural tables present simultaneously ✓ |

**V-01 Score: 213 (base) + 5 (C-36) + 5 (C-37) = 223**

---

## V-02 — Pre-Named SETUP-Linked Rows

**Structure:** V-04 R12 base + tighter C-36: TRACEABILITY AUDIT rows pre-named R-01, R-02 with explicit SETUP row-count match directive.

### C-36 Evaluation

The TRACEABILITY AUDIT table (lines 520–524):

```
| Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
|--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
| R-01   | (from SETUP row 1)          | Y / N                    |                               |            |                 |
| R-02   | (from SETUP row 2)          | Y / N                    |                               |            |                 |
(add rows to match SETUP table exactly — do not reduce row count)
```

Pre-table directive (lines 514–518): "Copy each Req-ID and Scout-Requirements Friction from the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP into a named row in the audit table below — one row per SETUP table row. The row count in this table must match the row count in the SETUP table; a missing row is a visible structural incompleteness at a glance."

- 6 columns with correct names ✓
- Rows pre-declared with named identifiers R-01, R-02 ✓
- Explicit SETUP→REFLECTION row-count match stated as structural rule ✓
- Friction pre-populated from SETUP "(from SETUP row 1)" ✓

**C-36: FULL** — and a stronger form than V-03 R12 which earned FULL.

### D13 Column-Count Check

| Table | Columns | Pass? |
|-------|---------|-------|
| CONVICTION DELTA (lines 538–542) | 4 cols, in-cell template pre-placed | C-34 PASS |
| CONVICTION GAP DIAGNOSIS (lines 573–577) | 6 cols, Register found / declared distinct, 3 rows | C-35 PASS |
| TRACEABILITY AUDIT (lines 520–524) | 6 cols, pre-named rows | C-36 PASS |

**C-37: FULL**

### V-02 Criterion Scores

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-33 | FULL | Item 0 with Hypothesis + Falsification, structural placement ✓ |
| C-31 | FULL | Grounding Req-ID(s) column, per-row ✓ |
| C-32 | FULL | CONVICTION GAP DIAGNOSIS subsection + scout sub-skill ✓ |
| C-34 | FULL | 4-col table, in-cell template per data row ✓ |
| C-35 | FULL | 6-col table, Register found/declared distinct columns, 3 pre-declared rows ✓ |
| C-36 | FULL | 6-col table, R-01/R-02 pre-named, row-count match directive ✓ |
| C-37 | FULL | All three structural tables present ✓ |

**V-02 Score: 213 + 5 + 5 = 223**

---

## V-03 — In-Table Structural Failure Signal

**Structure:** V-04 R12 base + C-36 form: RULE sentinel row embedded as first row after headers, before any data rows.

### C-36 Evaluation

The TRACEABILITY AUDIT table (lines 759–762):

```
| Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
|--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
| RULE   | A row with N in col 3 and a blank col 5 is a STRUCTURAL FAIL — not an acceptable omission | — | — | — | — |
|        |                             | Y / N                    |                               |            |                 |
```

- 6 columns ✓
- RULE sentinel row embeds the structural failure rule before any data row — the model encounters the constraint before filling the first cell ✓
- Template data row below sentinel ✓
- Post-table prose: per-column definitions including "Gap: if col 3 = N, state the absent requirement explicitly. Blank + N = STRUCTURAL FAIL" (lines 769–770) ✓

The sentinel row does not add a named Req-ID data row — it is a structural annotation. The underlying data row form is blank-Req-ID (V-03 R12 form which earned FULL). **C-36: FULL.**

The sentinel additionally converts the structural rule from a post-hoc prose reminder into an ontological pre-cell constraint. This is a form improvement over V-03 R12, not a regression.

### D13 Column-Count Check

| Table | Columns | Pass? |
|-------|---------|-------|
| CONVICTION DELTA (lines 776–780) | 4 cols, in-cell template | C-34 PASS |
| CONVICTION GAP DIAGNOSIS (lines 807–811) | 6 cols, Register found/declared, 3 rows | C-35 PASS |
| TRACEABILITY AUDIT (lines 759–762) | 6 cols (RULE row + template row) | C-36 PASS |

**C-37: FULL**

### V-03 Criterion Scores

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-33 | FULL | Item 0 Hypothesis + Falsification ✓ |
| C-31 | FULL | Grounding Req-ID(s) column ✓ |
| C-32 | FULL | CONVICTION GAP DIAGNOSIS subsection + scout sub-skill ✓ |
| C-34 | FULL | 4-col table, in-cell template ✓ |
| C-35 | FULL | 6-col table, Register found/declared distinct, 3 rows ✓ |
| C-36 | FULL | 6-col table, RULE sentinel converts structural rule to pre-cell constraint ✓ |
| C-37 | FULL | All three structural tables ✓ |

**V-03 Score: 213 + 5 + 5 = 223**

---

## V-04 — Maximum-Density Three-Table Chain

**Structure:** All three structural tables at tightest form — C-34 (in-cell template), C-35 (pre-declared rows + distinct-column directive), C-36 (RULE sentinel + R-01/R-02 pre-named + SETUP match).

### C-36 Evaluation

The TRACEABILITY AUDIT table (lines 997–1002):

```
| Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
|--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
| RULE   | N in col 3 + blank col 5 = STRUCTURAL FAIL — not an acceptable omission | — | — | — | — |
| R-01   | (copy from SETUP row 1)     | Y / N                    |                               |            |                 |
| R-02   | (copy from SETUP row 2)     | Y / N                    |                               |            |                 |
(add rows to match SETUP table exactly)
```

- 6 columns ✓
- RULE sentinel row (structural failure rule before data rows) ✓
- Named data rows R-01, R-02 with "(copy from SETUP row X)" explicit linkage ✓
- Row-count match directive ✓
- Post-table prose reinforces each column requirement ✓

**C-36: FULL** — maximum-density form combining V-02 R13 (named rows) + V-03 R13 (sentinel).

### D13 Column-Count Check

| Table | Columns | Pass? |
|-------|---------|-------|
| CONVICTION DELTA (lines 1016–1020) | 4 cols, in-cell template each data row | C-34 PASS |
| CONVICTION GAP DIAGNOSIS (lines 1056–1060) | 6 cols, Register found/declared, 3 rows | C-35 PASS |
| TRACEABILITY AUDIT (lines 997–1002) | 6 cols, RULE + R-01 + R-02 | C-36 PASS |

**C-37: FULL**

### V-04 Criterion Scores

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-33 | FULL | Item 0 with Hypothesis + Falsification, "Complete before item 1" ✓ |
| C-31 | FULL | Grounding Req-ID(s) column, "Required per row — no ungrounded impressionistic claims" ✓ |
| C-32 | FULL | CONVICTION GAP DIAGNOSIS, subsection + specific sub-skill ✓ |
| C-34 | FULL | 4-col table, in-cell template pre-placed; "cell with unfilled bracket fails the row" ✓ |
| C-35 | FULL | 6-col table, Register found/declared "structurally distinct columns"; explicit distinct-column directive: "a combined mismatch description written across both columns does not satisfy either" ✓ |
| C-36 | FULL | 6-col table: RULE sentinel + R-01/R-02 named rows + SETUP match directive — maximum-density form ✓ |
| C-37 | FULL | All three structural tables at maximum enforcement density ✓ |

**V-04 Score: 213 + 5 + 5 = 223**

---

## V-05 — Minimum-Density 223

**Structure:** All three structural tables at minimum prose density. Adjacent explanatory context stripped; tables and column definitions carry the requirement.

### C-36 Evaluation

The TRACEABILITY AUDIT table (lines 1201–1205):

```
| Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
|--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
| R-01   | (from SETUP)                | Y / N                    |                               |            |                 |
| R-02   | (from SETUP)                | Y / N                    |                               |            |                 |
(match SETUP row count exactly)
```

Pre-table prose (lines 1197–1199): "One row per SETUP SCOUT TRACEABILITY TABLE row. Copy Req-ID and Friction before Artifact 1; complete Must-have found, text, Gap, Scout namespace after. N + blank Gap = structural incompleteness."

- 6 columns ✓
- Pre-named R-01, R-02 rows ✓
- SETUP row-count match directive: "(match SETUP row count exactly)" ✓
- N + blank Gap rule stated: "N + blank Gap = structural incompleteness" ✓

Open question resolved: Does minimum-density prose carry C-36? Yes — the table has 6 correct columns, pre-named rows, SETUP linkage. The N+blank Gap rule is present (1 line). **C-36: FULL.** Prose is not load-bearing.

### C-35 Evaluation (Minimum-Density Form)

CONVICTION GAP DIAGNOSIS (lines 1234–1238):

```
| Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
| Spec     |  |  |  |  |  |
| Proposal |  |  |  |  |  |
| Pitch    |  |  |  |  |  |
```

Column summary (line 1240): "Register found / Register declared: one word each, distinct columns."

6 columns ✓, Register found / declared distinct ✓, 3 pre-declared rows ✓. **C-35: FULL.**

### C-34 Evaluation (Minimum-Density Form)

CONVICTION DELTA (lines 1210–1214): 4-column table, in-cell template pre-placed in each data row. Single instruction: "Replace all bracketed tokens with campaign values. Unfilled bracket = row fail." **C-34: FULL.**

### D13 Column-Count Check

| Table | Columns | Pass? |
|-------|---------|-------|
| CONVICTION DELTA | 4 cols, in-cell template | C-34 PASS |
| CONVICTION GAP DIAGNOSIS | 6 cols, Register found/declared, 3 rows | C-35 PASS |
| TRACEABILITY AUDIT | 6 cols, R-01/R-02 named, SETUP match | C-36 PASS |

**C-37: FULL**

### V-05 Criterion Scores

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-33 | FULL | Item 0: Hypothesis + Falsification present, compressed form still structurally complete ✓ |
| C-31 | FULL | Grounding Req-ID(s) column in CONVICTION DELTA ✓ |
| C-32 | FULL | CONVICTION GAP DIAGNOSIS section with subsection + scout sub-skill columns ✓ |
| C-34 | FULL | 4-col table, in-cell template, "unfilled bracket = row fail" ✓ |
| C-35 | FULL | 6-col table, Register found/declared distinct, 3 rows, column summary ✓ |
| C-36 | FULL | 6-col table, R-01/R-02 pre-named, SETUP match, N+blank Gap rule ✓ |
| C-37 | FULL | All three structural tables at minimum density ✓ |

**V-05 Score: 213 + 5 + 5 = 223**

---

## Composite Scorecard

| Variant | Base | C-36 | C-37 | Total | Rank |
|---------|------|------|------|-------|------|
| **V-04** — Maximum-Density Three-Table Chain | 213 | +5 | +5 | **223** | 1 |
| **V-02** — Pre-Named SETUP-Linked Rows | 213 | +5 | +5 | **223** | 2 |
| **V-03** — In-Table Structural Failure Signal | 213 | +5 | +5 | **223** | 3 |
| **V-01** — Mechanical C-34+C-35+C-36 Union | 213 | +5 | +5 | **223** | 4 |
| **V-05** — Minimum-Density 223 | 213 | +5 | +5 | **223** | 5 |

All five variants reach the v13 ceiling. Ranking is by structural enforcement density and diagnostic value, not score differential.

---

## Ranking Rationale

**V-04 (Rank 1):** Maximum-density combines every available structural enforcement mechanism simultaneously. RULE sentinel is inside the TRACEABILITY AUDIT table before any data row. Pre-named R-01/R-02 rows carry explicit SETUP linkage. SETUP row-count match is a directive. CONVICTION DELTA has in-cell template per row. CONVICTION GAP DIAGNOSIS has explicit "combined mismatch description does not satisfy either column independently" — the strongest available column-distinctness enforcement. Every structural constraint is ontological (table-encoded), not epistemic (prose-described).

**V-02 (Rank 2):** The pre-named SETUP-linked row form is the structural advance over V-03 R12 that V-01 does not make. Explicit row-ID match between SETUP and REFLECTION closes the lifecycle linkage as a verifiable constraint. Row count mismatch is visible at a glance without prose scanning. RULE sentinel is absent (V-03 R12 base form), which is the only density gap versus V-04.

**V-03 (Rank 3):** RULE sentinel converts the C-36 ontological guarantee into an active pre-cell constraint — the model encounters the structural rule before writing any row, not after. This is a real behavioral improvement over post-table prose instruction. However, it uses the blank-Req-ID template row (V-03 R12 form), not pre-named R-01/R-02 identifiers — the SETUP linkage is weaker than V-02 or V-04.

**V-01 (Rank 4):** Mechanical union of two confirmed R12 passing forms. Proves C-37 is achievable by composition of independently-passing R12 variants. No structural innovation — TRACEABILITY AUDIT is V-03 R12 form (template placeholder, blank Req-ID), CONVICTION DELTA and GAP DIAGNOSIS are V-04 R12 forms. Passes all criteria but contributes no new structural density.

**V-05 (Rank 5):** Diagnostic value is its defining contribution: resolves the open question that adjacent prose is not load-bearing for any of the three structural criteria. Tables alone carry C-34, C-35, and C-36 at minimum density. Structurally complete but the lowest enforcement density — no RULE sentinel, minimal column definitions, no explicit "combined mismatch does not satisfy both" directive in C-35.

---

## Excellence Signals (from V-04)

**1. Structural failure sentinel embedded before data rows**
The RULE sentinel row placed immediately after column headers converts the C-36 ontological guarantee from a rubric description into an active constraint the model encounters before filling the first cell. The structural failure rule is read before the model decides whether a gap is "acceptable."

**2. Pre-named SETUP-linked rows with row-count match directive**
Pre-declaring R-01, R-02 (copy from SETUP row X) inside the REFLECTION table and stating "(add rows to match SETUP table exactly)" makes SETUP→REFLECTION row-level coverage a fill-in constraint rather than a remembered instruction. A missing row is visible by row-count mismatch, not by recalling prose.

**3. Explicit column-distinctness directive for register columns**
The statement "a combined mismatch description written across both columns does not satisfy either column independently" (CONVICTION GAP DIAGNOSIS) is the highest-enforcement form of C-35 — it pre-empts the specific failure mode (single-cell combined description) rather than merely naming the required columns.

**4. Maximum structural density eliminates all epistemic escape routes**
Every verification point is ontological: CONVICTION DELTA cannot be filled without a Req-ID in the template cell; CONVICTION GAP DIAGNOSIS cannot record a gap without Register found and declared in separate columns; TRACEABILITY AUDIT cannot pass without named rows and a blank Gap cell being structurally visible. No phase relies on prose instruction for its enforcement mechanism.

**Open question resolved by V-05:** Adjacent prose is not load-bearing for C-34, C-35, or C-36. Tables carry the structural requirement at minimum density. Prose amplifies enforcement but does not constitute it.

---

```json
{"top_score": 223, "all_essential_pass": true, "new_patterns": ["Structural failure sentinel row embedded before data rows converts ontological rule into active pre-cell constraint encountered before model writes any row", "Pre-named SETUP-linked rows with explicit row-count match directive closes SETUP-to-REFLECTION lifecycle gap as fill-in constraint rather than recalled instruction", "Explicit column-distinctness directive pre-empts the combined-description failure mode for register split criteria", "Minimum-density probe confirms structural tables are self-sufficient — adjacent prose is scoring noise, not load-bearing for any of C-34, C-35, or C-36"]}
```
