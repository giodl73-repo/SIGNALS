Now I have all the material. Let me write the scorecard.

---

# trace-permissions — Round 9 Scoring

## Variation Scores

### V-01 — C-28 Only (Gate-Centric Base)

**Design axis:** NULL-FINDING RULE preamble requires attack scenario + config + Fails-if in all null-finding rows; TABLE 4 null rows verified at Phase 3 gate.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 | PASS | TABLE 3: all roles × Create/Read/Update/Delete/Assign/Share/Domain Ops |
| C-02 | PASS | TABLE 1: Field/Default/Role/FLS Override, row per sensitive/differing field |
| C-03 | PASS | TABLE 2: Scope (Own/BU/Parent BU/Org) + Enforcement per role |
| C-04 | PASS | Gap ID columns in Phase 2/3 tables + inventory enforcement |
| C-05 | PASS | TABLE 4 with four-vector escalation + Inertia column |
| C-06 | PASS | TABLE 5: Sharing Rule Conflicts with Inertia |
| C-07 | PASS | TABLE 6: Team Membership Gaps with null-finding requirement |
| C-08 | PASS | TABLE 7: Risk-Ranked Summary with Justification column |
| C-09 | PASS | 4c: "[G-ID] \| Risk: H/M/L \| Remediation: [specific: role + field + operation]" |
| C-10 | PASS | Phase 1: ≥2 H-labeled falsifiable hypotheses before any table |
| C-11 | PASS | 4b: null-finding tables confirmed to include attack scenario + falsifying condition |
| C-12 | PASS | TABLE 4: all 4 vectors required; null-finding per NULL-FINDING RULE |
| C-13 | PASS | H-Flag column in TABLE 1–6; 4a resolves each H with specific table/row citation |
| C-14 | PASS | Each phase closes with named PHASE N COMPLETE gate |
| C-15 | PASS | Phase 4 gate: "□ No new G-IDs introduced in Phase 4" |
| C-16 | PASS | GAP INVENTORY block committed before Phase 3 COMPLETE |
| C-17 | PASS | G-series IDs assigned at first occurrence; unchanged in inventory + TABLE 7 |
| C-18 | PASS | Inertia column in TABLE 4 (escalation) + TABLE 5 (sharing rules) |
| C-19 | PASS | Inertia column in TABLE 1 (FLS) + TABLE 2 (record scope) |
| C-20 | PASS | G-NN(P2): Phase 2 table row → Phase 3 row → inventory → TABLE 7 |
| C-21 | PASS | All four gates structured as explicit □-condition checklists |
| C-22 | PASS | Inventory format: "G-ID -- description -- first seen: TABLE X, row" |
| C-23 | PASS | TABLE 7 Phase Origin column with inline P2/P3 chain |
| C-24 | PASS | Inventory 4th field: "(H-NN)" or "(H-NN/H-MM)" or "(N/A: reason)" |
| C-25 | PASS | (P2) suffix tagged at Phase 2 table row; ORIGIN RULE: "origin classified at discovery" |
| C-26 | **PARTIAL (3/5)** | NULL-FINDING RULE preamble is load-bearing for C-28 in TABLE 1/2/5/6. Those tables say "apply NULL-FINDING RULE" without inlining the adversarial null format in the column header. Prose-removal test fails: removing the preamble block leaves TABLE 1/2/5/6 null rows without a falsifying-condition specification. Gate-condition assertion ("no criterion satisfied only by prose") asserts the outcome but cannot cure a structural dependency that column contracts would eliminate. |
| C-27 | **FAIL (0/5)** | Column headers are bare labels or single-line descriptions — "Path", "Roles", "Vector". No 3-part [value type \| format: constraint \| pass: condition] structure. An inspector reading the Path column header alone cannot determine that null rows require attack scenario + config + Fails-if. |
| C-28 | **PASS (5/5)** | NULL-FINDING RULE preamble declares the 3-part adversarial format universally. Per-table instructions for TABLE 1, TABLE 2, TABLE 4, TABLE 5, TABLE 6 all explicitly require adversarial null for null rows. TABLE 4 instructions inline the format. Phase 3 gate condition verifies: "□ TABLE 4: every null-finding names attack scenario + config tested + falsifying condition." Phase 4 section 4b requires restating the highest-priority falsifying condition. Full uniform coverage. |

**V-01 Score: 188 / 195**
*Deductions: C-26 −2, C-27 −5*

---

### V-02 — C-27 Only (Full Atomic Column Contracts)

**Design axis:** Each column header is a complete 3-part specification [value type \| format: constraint \| pass: condition]. C-26 proved by construction — no preamble rule needed; column headers ARE the specifications.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 to C-25 | PASS | Column contracts preserve all structural homes; all R8 criteria unaffected; 3-part headers for TABLE 1–7 add precision without removing any structural element |
| C-26 | **PASS (5/5)** | Proved by construction, not declaration. Every column header is a self-contained specification. Removing the COLUMN CONTRACT FORMAT prose from the preamble leaves no criterion unsatisfied — the column headers carry all criterion content. No preamble rule is load-bearing for any criterion C-01–C-26. The gate condition ("Each criterion is satisfied by its column contract -- no prose block is the sole carrier of any criterion that has a structural column home") is verifiable from column inspection alone. |
| C-27 | **PASS (5/5)** | Defining axis. Every column in TABLE 1–7 has explicit 3-part contract: e.g., TABLE 4 Path: "[type: confirmed abuse path or null-finding; format: if path found: role→action→scope gain; if no path: Attack/Config/Fails-if format; pass: description or null-finding with all three adversarial fields — 'none found' or controls-only null fails]". An inspector who has never read surrounding prose can evaluate any cell. |
| C-28 | **PARTIAL (3/5)** | TABLE 4 Path column contract specifies adversarial null with Fails-if — C-28 fully satisfied for escalation paths by column contract (the strongest possible structural enforcement). TABLE 5 Conflict column pass condition is "both grants named -- 'conflict exists' alone fails; NONE: [justification] if no conflict" — null rows require only a justification, not a falsifying condition. TABLE 6 Gap Scenario not shown with adversarial null contract. TABLE 1/2 null rows have no adversarial null requirement. C-28 coverage is TABLE 4-only via column contract; TABLE 5/6 null findings remain at C-11 level. |

**V-02 Score: 193 / 195**
*Deductions: C-28 −2*

---

### V-03 — C-27 + C-28 Compressed

**Design axis:** Both criteria encoded in compressed column header suffixes. TABLE 4 Path column contract specifies adversarial null format inline. C-28 RULE preamble covers other tables. C-26 proved by construction for TABLE 4; preamble-dependent for TABLE 5/6.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 to C-25 | PASS | Compressed column contracts preserve all structural homes; zero-criterion-loss claim verified by structure — tables, gates, inventory blocks all present; □-checklists retained at correct compression level |
| C-26 | **PARTIAL (3/5)** | TABLE 4 Path column contract is self-sufficient: specifying the adversarial null pass condition inline means the column header alone carries C-28 for TABLE 4 null rows — removing surrounding prose leaves the column contract standing. However, TABLE 5 Conflict ("[both grants named; NONE:[reason]]") and TABLE 6 Gap Scenario ("[specific or NONE:[reason]; blank fails]") rely on the "C-28 RULE: Null rows name attack scenario + config tested + falsifying condition" preamble block to carry C-28 for their null rows. Removing that preamble block reduces C-28 satisfaction for TABLE 5/6. The constructive proof is partial: TABLE 4 satisfies C-26 by construction; TABLE 5/6 satisfy it only by declaration. |
| C-27 | **PASS (5/5)** | Compressed but complete. Every column header includes value type + format constraint + pass condition, e.g.: "Gap ID [G-NN(P2) at this row if gap; NONE otherwise; blank fails; (P2) in Phase 2]" — type: gap identifier, format: G-NN(P2) or NONE, pass: not blank + (P2) suffix required in Phase 2. "Path [confirmed: role→action→scope gain; null: 'Attack:[scenario]\|Config:[control]\|Fails-if:[change]'; 'none found' fails C-28]" — type + two format alternatives + explicit pass condition. Gate 4: "No criterion satisfied only by prose -- column contracts are the specifications." |
| C-28 | **PARTIAL (3/5)** | TABLE 4 Path column contract specifies adversarial null with Fails-if — C-28 fully enforced for escalation paths by column specification. "C-28 RULE" preamble declares the adversarial null requirement for all null rows. Gate 3 verifies: "□ T4: all 4 vectors; Path col: confirmed path or 3-part adversarial null (Fails-if present)" — TABLE 4 only. TABLE 5 Conflict and TABLE 6 Gap Scenario columns say "NONE:[reason]" as the null pass condition — they do not embed the Fails-if requirement in the column contract. C-28 for TABLE 5/6 depends on the C-28 RULE preamble, not the column header. An inspector reading the TABLE 5 Conflict column header alone cannot determine that Fails-if is required for null rows. |

**V-03 Score: 191 / 195**
*Deductions: C-26 −2, C-28 −2*

---

### V-04 — C-28 Uniform Adversarial Null Coverage

**Design axis:** ADVERSARIAL NULL RULE applies to every table (TABLE 1–6), not just TABLE 4. Every null row in every evidence table produces a falsifiable Fails-if condition. Phase 4 gate verifies all five tables.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 to C-25 | PASS | ADVERSARIAL NULL RULE adds adversarial null requirements without removing any structural element. TABLE 2 adds explicit "Adversarial Null" column for null scope rows — a structural addition. □-checklist gates present and multi-condition throughout. All R8 structural elements preserved. |
| C-26 | **PARTIAL (3/5)** | Same failure mode as V-01. ADVERSARIAL NULL RULE preamble carries C-28 compliance for all tables. TABLE 1 null rows use "FLS Override or appended null column" with adversarial null per the RULE — column headers like "| Field \| Default \| Role \| FLS Override \| Gap ID [...] \| H-Flag [...] \| Inertia [...]" are descriptive but not 3-part contracts. Removing the ADVERSARIAL NULL RULE preamble leaves TABLE 1/2/4/5/6 column headers unable to specify adversarial null requirements. Gate 4 conditions verify uniformity but cannot substitute for the missing column-level specification. Prose-removal test fails. |
| C-27 | **FAIL (0/5)** | Column headers are bare labels with inline descriptions: "| Field \| Default \| Role \| FLS Override \| Gap ID [G-NN(P2) at this row; NONE otherwise] \| H-Flag [H-ref or N/A: reason] \| Inertia [what breaks if restriction changes?]". These are type+format but missing explicit pass conditions (e.g., what exactly fails?). TABLE 4 Path column: "Path [confirmed or adversarial null per ADVERSARIAL NULL RULE]" — this references preamble prose, not a self-contained spec. An inspector who has never read the ADVERSARIAL NULL RULE cannot evaluate a TABLE 4 null-finding cell from the Path column header alone. |
| C-28 | **PASS (5/5)** | Defining axis. ADVERSARIAL NULL RULE declared in preamble: "Attack: [scenario] \| Config: [setting] \| Fails-if: [change]" format required for every null row in every table. TABLE 1 requirements explicitly call for adversarial null in FLS Override null cells. TABLE 2 has dedicated "Adversarial Null" column for null scope rows. TABLE 4/5/6 all have explicit adversarial null instructions. Phase 4 gate condition verifies: "□ Adversarial nulls confirmed in: TABLE 1, TABLE 2, TABLE 4, TABLE 5, TABLE 6 (all null rows)." Most comprehensive C-28 coverage of any variation. Phase 4 section 4b extracts top-3 falsifying conditions across all tables as an attack-surface prioritization. |

**V-04 Score: 188 / 195**
*Deductions: C-26 −2, C-27 −5*

---

### V-05 — Adversarial-First + C-27 + C-28 Full Upgrade

**Design axis:** R8 V-05 Structural Competitor extended with 3-part column contracts (C-27) and adversarial null format embedded in TABLE 4 Path, TABLE 5 Conflict, TABLE 6 Gap Scenario column headers (C-28). C-28 verifiable from column headers for all primary null-finding tables without reading any preamble rule.

| ID | Pass? | Evidence |
|----|-------|---------|
| C-01 to C-25 | PASS | Full R8 base preserved. Adversarial framing strengthens depth criteria (C-04/C-05/C-06/C-10). Structural Competitor column adds additional analysis without removing structural elements. 3-part column contracts add precision. All □-checklist gates present. G-NN(P2) tagging, H-Flag, hypothesis resolution, inventory, Phase Origin all maintained. |
| C-26 | **PASS (5/5)** | Proved by construction. Every column header in TABLE 1–7 is a complete 3-part contract. TABLE 4 Path column specifies adversarial null as the pass condition for null-finding rows — C-28 for escalation paths is satisfied by column structure alone. TABLE 5 Conflict and TABLE 6 Gap Scenario column contracts also embed the adversarial null pass condition: TABLE 5 Conflict "pass: conflict prose OR adversarial null with Fails-if -- blank fails"; TABLE 6 Gap Scenario "pass: specific scenario OR adversarial null with Fails-if -- blank fails." Removing all navigation prose leaves all criteria satisfied by their column contracts. Gate 4 condition: "Each criterion satisfied by its column contract or structural element -- column contracts eliminate the need for prose to carry any table-based criterion." Constructive proof, not declaration. |
| C-27 | **PASS (5/5)** | Full 3-part contracts on every column in TABLE 1–7 plus Structural Competitor column. Examples: TABLE 1 Gap ID "[type: gap identifier or absence; format: G-NN(P2) if misconfiguration at this row, NONE otherwise; pass: G-NN(P2) with suffix or NONE -- blank fails; (P2) required for any gap found in Phase 2]". TABLE 4 Path "[type: confirmed abuse path or adversarial null-finding; format: if path found: role→action→scope gain; if no path: Attack/Config/Fails-if format; pass: confirmed path with roles+mechanism OR adversarial null with all three fields -- 'none found' or controls-only null fails (satisfies C-11 but not C-28)]". Structural Competitor column also 3-part. An inspector who has never read any surrounding text can evaluate any cell in any table. |
| C-28 | **PASS (5/5)** | Adversarial null embedded as a column-level pass condition in three tables: (1) TABLE 4 Path — "pass: confirmed path OR adversarial null with all three fields"; (2) TABLE 5 Conflict — "pass: conflict prose OR adversarial null with Fails-if"; (3) TABLE 6 Gap Scenario — "pass: specific scenario OR adversarial null with Fails-if." For these three tables — the primary null-finding tables (escalation paths, sharing conflicts, team gaps) — C-28 is mechanically verifiable from the column header alone without any preamble rule. Phase 4 section 4b extracts highest-priority falsifying condition per table. Phase 4 gate: "□ Null-finding accountability: Fails-if condition extracted per table; 'none found' alone fails C-28." Comprehensive and structurally enforced. |

**V-05 Score: 195 / 195**
*No deductions — maximum score*

---

## Composite Rankings

| Rank | Variation | Score | C-26 | C-27 | C-28 | Notes |
|------|-----------|-------|------|------|------|-------|
| **1** | **V-05** | **195/195** | PASS | PASS | PASS | All three new criteria satisfied; C-28 via column contracts in TABLE 4/5/6 — strongest structural guarantee |
| **2** | **V-02** | **193/195** | PASS | PASS | PARTIAL | C-27 fully realized; C-28 via TABLE 4 Path contract only; TABLE 5/6 null rows remain at C-11 level |
| **3** | **V-03** | **191/195** | PARTIAL | PASS | PARTIAL | C-27 at full compression; TABLE 4 Path column self-sufficient; TABLE 5/6 rely on C-28 RULE preamble |
| **T-4** | **V-01** | **188/195** | PARTIAL | FAIL | PASS | C-28 uniform via preamble rule; column headers bare labels; C-26 partial — NULL-FINDING RULE prose load-bearing |
| **T-4** | **V-04** | **188/195** | PARTIAL | FAIL | PASS | C-28 widest uniform coverage (all tables); ADVERSARIAL NULL RULE preamble load-bearing undermines C-26 |

---

## Excellence Signals

**Signal 1 — Preamble-rule C-28 undermines C-26 (structural dependency trap)**
V-01 and V-04 both achieve full C-28 coverage by placing the adversarial null format in a preamble rule block and referencing it from per-table instructions. The gate condition asserts "no criterion satisfied only by prose." But the prose-removal test exposes the dependency: removing the NULL-FINDING RULE / ADVERSARIAL NULL RULE block leaves TABLE 1/2/5/6 column headers unable to specify the adversarial null format — those tables say "apply [RULE]" rather than embedding the format in the column contract. Gate assertions of structural self-sufficiency are declarative claims subject to gap; column contracts are constructive proofs immune to this failure. Any variation that achieves C-28 via preamble rule incurs a C-26 penalty that column-contract C-28 avoids.

**Signal 2 — C-27 without C-28 column integration creates null-finding quality asymmetry**
V-02 achieves C-27 fully (3-part contracts on all TABLE 1–7 columns) but C-28 only for TABLE 4 (the Path column contract specifies adversarial null). TABLE 5 Conflict pass condition is "NONE: [justification]" — C-11 level, not C-28. TABLE 6 Gap Scenario is similar. The result: escalation path null-findings are falsifiable from the column header alone, but sharing-rule and team-membership null-findings are not. V-05 closes this asymmetry by embedding adversarial null pass conditions in the TABLE 5 Conflict and TABLE 6 Gap Scenario column headers, making all three primary null-finding tables equally falsifiable by column inspection. The complete C-27 × C-28 solution requires adversarial null embedded in every null-finding column contract, not just in the escalation path column.

---

```json
{"top_score": 195, "all_essential_pass": true, "new_patterns": ["Preamble-rule C-28 fails the C-26 prose-removal test: V-01/V-04 gate conditions assert structural self-sufficiency, but TABLE 1/2/5/6 column headers reference the NULL-FINDING RULE preamble rather than specifying the adversarial null format inline — removing that prose block reduces C-28 satisfaction for those tables, making the gate assertion a declarative claim that the structural evidence does not support.", "C-27 without C-28 column integration leaves null-finding quality asymmetric: V-02 achieves full C-27 but only TABLE 4 Path embeds adversarial null — TABLE 5 Conflict and TABLE 6 Gap Scenario pass conditions require only NONE:[justification] (C-11 level), so sharing-rule and team-membership null-findings are not falsifiable from their column headers; V-05 closes this by embedding Fails-if requirements in TABLE 5 and TABLE 6 column contracts, making all three primary null-finding tables equally falsifiable by column inspection alone."]}
```
