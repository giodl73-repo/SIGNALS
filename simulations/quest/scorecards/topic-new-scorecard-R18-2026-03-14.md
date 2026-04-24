## Round 18 Scoring — topic-new (Rubric v16, 47 criteria)

---

### Baseline Analysis

All five variations inherit the full R17 V-01 structure. Before scoring variable criteria, the common pass count is established.

**Common PASS — all 5 variations (criteria C-09 through C-50, excluding C-49):**

| Criteria | Status |
|----------|--------|
| C-09 to C-14: Commit gate, naming, gates, consequence framing, dedicated sections | PASS all |
| C-15: Stakeholder-risk enumeration (INERTIA REGISTER Stakeholder Most Harmed column precedes all phases) | PASS all |
| C-16 to C-20: Schema structure, traceability, temporal consequence layering | PASS all |
| C-21 to C-31: Per-phase gates, row-count gates, schema IDs, pipeline overview, dedicated commit-gate phase, read directive, multi-gate citation, column completeness independence, consequence column, gate-independence instruction, Priority-first column | PASS all |
| C-32 to C-41: Prior-round criteria (v10–v12 baseline, inherited) | PASS all |
| C-42 to C-48: INERTIA REGISTER, phase override directives, verbatim IR-NN at exit, zero inline prose in phases, Stakeholder Most Harmed travels, concrete failure example, PCR with stable IDs | PASS all |
| C-50: Prohibition clause ("Do not begin Phase 1 until you have read every row") | PASS all |

**Common pass total: 41 of 47**

---

### Variable Criteria Matrix (C-49, C-51, C-52, C-53, C-54, C-55)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-49** Override mission opener before all schemas | FAIL | PASS | FAIL | FAIL | PASS |
| **C-51** "Stop." + "Record both results." at independence gate | PASS | FAIL | FAIL | PASS | PASS |
| **C-52** Second-person failure framing "Output you accepted:" | PASS | FAIL | FAIL | PASS | PASS |
| **C-53** Command register at phase entry "Stop. You are overriding IR-NN:" | PASS | FAIL | FAIL | PASS | PASS |
| **C-54** Labeled BEFORE/AFTER trajectory table | PARTIAL | FAIL | PASS | PASS | PASS |
| **C-55** PCR entries cross-cite FER-NN | FAIL | FAIL | FAIL | FAIL | PASS |

**Evidence notes:**

**C-49:**
- V-02/V-05: Dedicated `## OVERRIDE MISSION` block appears before INERTIA REGISTER with explicit "Every block that follows exists to prevent these defaults from applying." PASS.
- V-01/V-03/V-04: Jump directly to INERTIA REGISTER; override mission is implicit in the schema structure, not declared. FAIL.

**C-51:**
- V-01/V-04/V-05: `> **Stop. Do not advance until you have run BOTH of the following checks as separate acts. Record both results.**` — both requirements present. PASS.
- V-02: "Complete and record the row-count check before beginning the column-completeness check" — recording obligation implied but no "Stop." imperative, no "Record both results." explicit clause. FAIL.
- V-03: "Check row count and column completeness as two separate acts. Do not chain these checks." — no "Stop.", no "Record both results." FAIL.

**C-52:**
- V-01/V-04/V-05: FER-01 contains `"Output you accepted: 'S-01 | Product Manager | | ' — SK-03 and SK-04 empty on all rows. This output is malformed."` — second-person, model addressed as agent. PASS.
- V-02: FER-01 reads "Table has 3 rows; SK-01 column is populated; SK-03 and SK-04 cells are empty on all rows" — third-person description. FAIL.
- V-03: SEQUENTIAL PATH column shows "S-01 | Product Manager | | (SK-03 empty, SK-04 empty)" — no "Output you accepted:" framing. FAIL.

**C-53:**
- V-01/V-04/V-05: Phase headers use `**Stop. You are overriding IR-01:**` — halt imperative + second-person present progressive. PASS.
- V-02/V-03: `**This phase overrides IR-01.**` — declarative third-person, informational register. FAIL.

**C-54:**
- V-03/V-04/V-05: Full 4-row labeled BEFORE/AFTER table (Output state → Row count check → Column completeness → Gate result) × (SEQUENTIAL PATH wrong / INDEPENDENT PATH correct). Trajectory visible by column inspection. PASS.
- V-01: Two-column FER table ("Output You Accepted (sequential — THIS IS WRONG)" / "What Independent Checking Catches") shows contrast at outcome level but as a single row — the step-by-step trajectory (check-by-check progression) is not visible by column inspection; only the terminal output state is contrasted. **PARTIAL** (0.5).
- V-02: Plain 4-column FER table; no labeled sequential/independent column split. FAIL.

**C-55:**
- V-05 only: PCR-01 ends "Skip failure recognizable by FER-01 output inspection."; PCR-02 ends "Skip failure recognizable by FER-02 output inspection."; PCR-03/PCR-04 note "No FER entry (structural absence / file-path check)" — honest scoping. PASS.
- V-01/V-02/V-03/V-04: PCR has no FER cross-citations. FAIL.

---

### Composite Scores

Formula: `aspirational_pass / 47 × 10` (PARTIAL = 0.5)

| Variation | Common | C-49 | C-51 | C-52 | C-53 | C-54 | C-55 | Total | Score |
|-----------|--------|------|------|------|------|------|------|-------|-------|
| **V-01** Command register throughout | 41 | 0 | 1 | 1 | 1 | 0.5 | 0 | 44.5 | **9.47** |
| **V-02** Override mission opener | 41 | 1 | 0 | 0 | 0 | 0 | 0 | 42 | **8.94** |
| **V-03** BEFORE/AFTER failure table | 41 | 0 | 0 | 0 | 0 | 1 | 0 | 42 | **8.94** |
| **V-04** Command register + BEFORE/AFTER | 41 | 0 | 1 | 1 | 1 | 1 | 0 | 45 | **9.57** |
| **V-05** Full integration | 41 | 1 | 1 | 1 | 1 | 1 | 1 | **47** | **10.0** |

**Ranking: V-05 > V-04 > V-01 > V-02 = V-03**

---

### Variation-by-Variation Analysis

**V-01 (9.47)** — Command register is the most productive single axis: three criteria (C-51, C-52, C-53) fire simultaneously from a single phrasing commitment. The gap is C-49 (no override-mission opener, the structural purpose frame is absent) and C-55 (PCR is not wired to FER-NN). The C-54 partial reflects that V-01's FER table shows the terminal contrast but not the step-by-step trajectory — the model sees "wrong output state / what catches it" in two columns but cannot trace the sequential-check path by row inspection.

**V-02 (8.94)** — The override-mission opener is the weakest single axis in isolation. C-49 fires but the absence of command register means C-51/C-52/C-53 all fail: the independence gate, failure example, and phase directives remain in informational register. Gaining one criterion while losing three against V-01 exposes C-49 as a framing enhancement rather than a gate-compliance driver.

**V-03 (8.94)** — BEFORE/AFTER table as isolated axis (C-54) exactly ties V-02. The 4-row trajectory table is the most structurally dense single addition (4 rows × 2 columns per FER entry), but it produces only one criterion pass. The absence of command register (C-51/C-53) and second-person framing (C-52) leaves all ambient directives advisory. C-54 is a visualization improvement; it does not address the command-vs-informational gap.

**V-04 (9.57)** — Best score from a combined-axis strategy. Command register (C-51/C-52/C-53) + BEFORE/AFTER table (C-54) compound: the model is halted at the gate, given a recording obligation, and given a visual inspection target. Four criteria fire from two structurally independent channels. The gap (one criterion short of V-05) is entirely C-55 and C-49 — consequence-detection wiring and purpose framing are not addressed.

**V-05 (10.0)** — Perfect score against v16 rubric. All seven new criteria fire without phrasing collision or structural overload. Each addition occupies a distinct structural position: OVERRIDE MISSION precedes all schemas; prohibition clause closes the read directive; Stop. imperative fires at three independent decision points (phase entry × 4, independence gate × 1); second-person BEFORE/AFTER table lives entirely in FER registry; PCR FER cross-citations are the terminal layer. The honest "No FER entry" notes at PCR-03/PCR-04 prevent false cross-citations for structural-absence failures — scoping integrity is maintained.

---

### Excellence Signals from V-05

**ES-1: Purpose frame before constraint frame**
The OVERRIDE MISSION block declares the document's function before any schema is encountered. A model reading V-05 enters INERTIA REGISTER already knowing why the schemas exist. Every gate it subsequently reads is read as an override instrument, not ambient context. This is structurally prior to C-49's mechanical test — the override mission changes the reading register for all 47 subsequent criteria.

**ES-2: Command register compounds across all decision points**
"Stop." appears at phase entry (4 phases × "Stop. You are overriding IR-NN:") and at the independence gate ("Stop. Do not advance..."). No decision point is left in informational register. The phrasing commitment is zero-exception — one pattern, no special cases.

**ES-3: Second-person BEFORE/AFTER table provides two independent recognition channels**
C-52 (second-person) and C-54 (structural contrast) are independent: "Output you accepted:" addresses the model as the agent; the 4-row trajectory table makes the wrong path visible by column inspection. Their combination means the model can self-recognize at the gate by either route — personal address or visual matching — without holding both states in narrative context simultaneously.

**ES-4: PCR FER cross-citation with honest no-FER scoping**
PCR-01/PCR-02 cite FER-01/FER-02 making skip-consequence detection mechanical. PCR-03/PCR-04 explicitly note "No FER entry" with the failure type (structural absence, file-path check). This prevents the pattern from over-claiming — only output-inspection failures get FER entries, preserving the registry's semantic precision.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["OVERRIDE MISSION block before all schema content converts subsequent gates from ambient instruction to override instruments — purpose frame precedes constraint frame", "Stop. imperative applied zero-exception at all decision points (phase entry and independence gate) — no decision point remains in informational register", "Second-person BEFORE/AFTER table compounds two independent recognition channels: column inspection makes trajectory visible without narrative; Output you accepted: addresses model as agent enabling self-recognition", "PCR FER-NN cross-citation with honest no-FER scoping for structural-absence failures — consequence-detection link is mechanical, not inferential; scoping integrity prevents false citations"]}
```
