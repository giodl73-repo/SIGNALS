## Round 19 Scoring — topic-new (v17 rubric, denominator 49)

---

### Baseline Analysis

All five variations inherit the full pre-R19 criterion stack (C-01–C-53). The differentiation is entirely in C-54–C-57. Key base characteristics:

| Feature | V-01 base (R18 V-01) | V-02 base (R18 V-04) | V-03 base (R18 V-05) | V-04 base (R18 V-04) | V-05 base (R18 V-05) |
|---------|---------------------|---------------------|---------------------|---------------------|---------------------|
| OVERRIDE MISSION (C-49) | YES (added in R19) | NO | YES (inherited) | YES (added in R19) | YES (inherited) |
| BEFORE/AFTER FER (C-54) | compact 2-col table | full 4-row/entry | full 4-row/entry | full 4-row/entry | full 4-row/entry |
| PCR FER citations (C-55) | NO | YES | YES | YES | YES |
| IR-NN enumeration (C-56) | YES (added in R19) | NO | YES (added in R19) | YES (added in R19) | YES (added in R19) |
| Exhaustive FER decl (C-57) | NO | YES | YES | YES | YES |

---

### Criterion-by-Criterion Evaluation

#### C-01 through C-48 — uniform across all variations

All five variations share the same schema architecture (STAKEHOLDER SCHEMA, FIELD SCHEMA, COVERAGE SCHEMA, INERTIA REGISTER, FER, PCR, per-phase exit gates, IR-NN verbatim at exit, stakeholder-most-harmed column, schema-ID citations, no inline prose constraints). Base: **40 PASS each**.

**C-49 — override mission declaration**

- V-01: PASS — "The defaults being overridden by this skill: IR-01...IR-05. Every block that follows exists to prevent these defaults from applying." Named OVERRIDE MISSION block present.
- V-02: FAIL — No OVERRIDE MISSION. Prompt opens directly with INERTIA REGISTER. Override purpose undeclared.
- V-03: PASS — Inline blockquote: "These are the defaults this skill overrides: IR-01...IR-05. Every block that follows exists to prevent these defaults from applying."
- V-04: PASS — Named OVERRIDE MISSION with enumeration sentence + table. Full declaration.
- V-05: PASS — Named OVERRIDE MISSION with enumeration sentence + table + "every schema, every gate, and every exit condition is an override instrument."

**C-50 — pipeline prohibition clause**

- All: PASS — All have "Do not begin Phase 1 until you have read every row" in pipeline overview header.

**C-51 — independence instruction command register + result recording**

- All: PASS — All Phase 1 exit gates: "Stop. Do not advance until you have run BOTH of the following checks as separate acts. Record both results."

**C-52 — second-person failure example framing**

- All: PASS — All FER entries frame malformed output as "Output you accepted: '...'"

**C-53 — command register override directive**

- All: PASS — All phases open with "Stop. You are overriding IR-NN: '...text...' Stakeholder Most Harmed: ..."

**C-54 — labeled BEFORE/AFTER comparison**

- V-01: PASS — FER table has two labeled columns "Output You Accepted (sequential — THIS IS WRONG)" and "What Independent Checking Catches" — one row per FER entry. Structural contrast is visible by column inspection. Compact form satisfies the labeled side-by-side requirement; trajectory condensed but present.
- V-02 through V-05: PASS — Full 4-row-per-entry BEFORE/AFTER format (output state / row count check / completeness check / result rows per example).

**C-55 — PCR consequence entries cross-cite FER-NN**

- V-01: FAIL — PCR has no FER citations at all. PCR-01: "gap detection fails" — no FER reference. PCR-02: "Design Lead cannot parse readiness" — no FER reference. Silent omission throughout.
- V-02: PASS — PCR-01: "Skip failure recognizable by FER-01 output inspection." PCR-02: "Skip failure recognizable by FER-02 output inspection." Both detectable entries cite FER-NN.
- V-03: PASS — Same FER-01/FER-02 citations at PCR-01/PCR-02.
- V-04: PASS — Same. PCR header explicitly names the requirement.
- V-05: PASS — Same. PCR header names exhaustive coverage requirement plus structural-inspection property.

**C-56 — IR-NN closed-list enumeration in opener**

- V-01: PASS — "The defaults being overridden by this skill: **IR-01, IR-02, IR-03, IR-04, IR-05**" as compact enumeration sentence before INERTIA REGISTER. Sentence + override table present.
- V-02: FAIL — No OVERRIDE MISSION, no enumeration. Model enters INERTIA REGISTER without closed list; must discover enumeration by parsing register rows.
- V-03: PASS — "These are the defaults this skill overrides: **IR-01, IR-02, IR-03, IR-04, IR-05**" as inline sentence only (no table). Closed list in one read before INERTIA REGISTER.
- V-04: PASS — Enumeration sentence + override table in named OVERRIDE MISSION block.
- V-05: PASS — Enumeration sentence + override table. Most explicit form.

**C-57 — exhaustive PCR FER declaration (every entry either FER-NN or explicit no-FER note)**

- V-01: FAIL — PCR has no FER citations and no "No FER entry" notes on any row. Silent omission on PCR-01 through PCR-04 is structurally indistinguishable from missing citations.
- V-02: PASS — PCR-01: FER-01 citation. PCR-02: FER-02 citation. PCR-03: "No FER entry (structural absence — no isolated block to inspect; failure is absence of a phase boundary, not an output state)." PCR-04: "No FER entry (file-path verification — gate checks file existence at declared path, not table output state)." PCR header explicitly names the rule.
- V-03: PASS — PCR-01/PCR-02 cite FER-01/FER-02. PCR-03: "No FER entry (structural absence, not output-state failure)." PCR-04: "No FER entry (file-path check, not table-output inspection)." Header names the structural requirement.
- V-04: PASS — Same row-level declarations as V-02 plus PCR header: "Silent omission is not permitted."
- V-05: PASS — Same plus PCR header names "Exhaustive FER coverage requirement" as structural property: "FER coverage is auditable by structural inspection of this table, not by content inference."

---

### Composite Score Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01–C-48 (40 criteria) | 40 | 40 | 40 | 40 | 40 |
| C-49 | 1 | 0 | 1 | 1 | 1 |
| C-50 | 1 | 1 | 1 | 1 | 1 |
| C-51 | 1 | 1 | 1 | 1 | 1 |
| C-52 | 1 | 1 | 1 | 1 | 1 |
| C-53 | 1 | 1 | 1 | 1 | 1 |
| C-54 | 1 | 1 | 1 | 1 | 1 |
| C-55 | 0 | 1 | 1 | 1 | 1 |
| C-56 | 1 | 0 | 1 | 1 | 1 |
| C-57 | 0 | 1 | 1 | 1 | 1 |
| **Total pass** | **47** | **47** | **49** | **49** | **49** |
| **Score (/10)** | **9.59** | **9.59** | **10.0** | **10.0** | **10.0** |

---

### Variation Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 (tied) | **V-03** | 10.0 | Minimal C-56 form (inline sentence only) + full V-05 base. All 49 pass. |
| 1 (tied) | **V-04** | 10.0 | Combined C-56 + C-55 + C-57 on R18 V-04 base. All 49 pass. |
| 1 (tied) | **V-05** | 10.0 | Full integration. PCR header names exhaustive coverage as structural property. All 49 pass. |
| 4 (tied) | **V-01** | 9.59 | Has C-56 (opener), lacks C-55 and C-57 (no PCR FER treatment). Symmetric gap to V-02. |
| 4 (tied) | **V-02** | 9.59 | Has C-55 + C-57 (PCR), lacks C-49 and C-56 (no opener). Symmetric gap to V-01. |

**Structural note on V-01/V-02 symmetry**: Both fail exactly two criteria at opposite structural ends. V-01 closes the opener gap but leaves the PCR terminal layer silent. V-02 closes the PCR terminal layer but leaves the opener unframed. This confirms C-56 and C-57 are structurally independent: neither can substitute for the other.

---

### Excellence Signals (from V-03, V-04, V-05)

**ES-1 — Minimal inline sentence is sufficient for C-56 closed-list forward index**

V-03 implements C-56 as a single blockquote sentence with no table: "These are the defaults this skill overrides: IR-01, IR-02, IR-03, IR-04, IR-05." This achieves full C-56 compliance at minimum token cost, proving the operative mechanism is the compact enumerable list delivered before register parsing begins — not the surrounding table structure that V-01/V-04/V-05 carry. The sentence form isolates the forward-index function from the override-description function (which the table handles). C-56 and the OVERRIDE MISSION table are separable.

**ES-2 — PCR header structural rule converts row-level to table-level auditability**

V-04 and V-05 place an explicit structural rule in the PCR header: "Every entry either cites a FER-NN ID ... or carries an explicit 'No FER entry ([reason])' note. Silent omission is not permitted." This converts C-57 from a row-scanning requirement (check each row for FER declaration) into a table-level structural property (the header asserts the coverage rule; the rows execute it). V-05 extends this further: "FER coverage is auditable by structural inspection of this table, not by content inference" — naming the structural-inspection property explicitly. A model reading the PCR header before the rows enters the table knowing silence is prohibited, rather than discovering row-by-row coverage.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["Minimal inline sentence sufficient for C-56 forward index — compact 'These are the defaults: IR-01...' sentence delivers closed list without table; isolates the forward-index mechanism from the override-description table, proving the sentence is the operative element", "PCR header structural rule converts C-57 from row-scanning to table-level auditability — naming exhaustive FER coverage as a required property in the header (with silent omission explicitly prohibited) lets the model confirm coverage by structural inspection rather than inferring which rows should have citations"]}
```
