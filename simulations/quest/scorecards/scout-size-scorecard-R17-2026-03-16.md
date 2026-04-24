# Quest Score — scout-size R17 (Rubric v17, 35 criteria)

## Criterion Reference (key named criteria)

| ID | Criterion | Type |
|---|---|---|
| C-33 | Failure-class label (`basis-negation`) in self-test affirmative branch | R16 carry-forward |
| C-38 | Row-level identifiability in CLOSED-LABEL per gate row | R16 carry-forward |
| C-40 | Compilation pointer row | R16 carry-forward |
| C-41 | Fill/leave-blank conditions in CLOSED-LABEL column header | R16 carry-forward |
| C-42 | `format:` slot with value template in CLOSED-LABEL header | **R17 new** |
| C-43 | Architectural contract label alongside failure class in self-test affirmative branch | **R17 new** |

---

## V-01 — Single-phase; C-42 format slot; C-43 single-phase contract label

**Axis**: Inertia framing. Based on R16 V-02 (single-phase, 27/33). Two targeted changes: CLOSED-LABEL header fills `format: …` ellipsis; self-test adds `— a gap field production contract violation`.

| Criterion group | Status | Evidence |
|---|---|---|
| C-01–C-41 (R16 criteria) | 27/33 PASS | R16 V-02 single-phase baseline confirmed at 27/33 = 8.18 |
| **C-42** | **PASS** | Header reads `format: "Precondition [A/B]: [named condition]"` — value template specified, not ellipsis. Fill condition + leave-blank condition + value shape all resolvable from header alone |
| **C-43** | **PASS** | Self-test: "you have written a basis-negation — a gap field production contract violation" — contract label present; upgrades from content-level to structural-level diagnostic for single-phase scope |

**Composite: 29/35 = 8.29**

---

## V-02 — Second-person register; single-phase; C-42 + C-43 in direct address

**Axis**: Phrasing register. Structurally identical to V-01; C-43 text shifts to confrontational direct address ("you have violated").

| Criterion group | Status | Evidence |
|---|---|---|
| C-01–C-41 (R16 criteria) | 27/33 PASS | Same single-phase architecture as R16 V-02; no structural criterion gain from register shift |
| **C-42** | **PASS** | Same CLOSED-LABEL header format slot as V-01 |
| **C-43** | **PASS** | "you have written a basis-negation — a gap field production contract violation" — direct address satisfied; contract label present |
| Register-as-criterion | N/A | No rubric criterion scores register intensity; pass/fail on C-43 does not differentiate second-person from third-person |

**Composite: 29/35 = 8.29**

*V-02 ties V-01. The second-person register hypothesis addresses model behavior, not prompt-design criterion compliance. No structural ceiling difference.*

---

## V-03 — Two-phase; C-42 only new change; C-43 already present

**Axis**: Role sequence. Based on R16 V-01 (two-phase, 32/33). C-43 was retroactively PASS in R16 V-01 (text already read "a Phase 2 charter violation"). One structural change: fill the `format:` ellipsis.

| Criterion group | Status | Evidence |
|---|---|---|
| C-01–C-41 (R16 criteria) | 32/33 PASS | R16 V-01 established 32/33; one R16 criterion missed (role-separation or phase-charter criterion where two-phase lost to three-phase) |
| **C-42** | **PASS** | Format slot now specifies `"Precondition [A/B]: [named condition]"` — was ellipsis in R16 V-01 |
| **C-43** | **PASS** | Already present from R16 V-01: "a Phase 2 charter violation" — no new edit required; criterion is immediately satisfied |

**Composite: 34/35 = 9.71**

*Maximum attainable for two-phase architecture with a single targeted edit. V-03 demonstrates that a fully specified C-43-containing prompt needed only one change to reach near-maximum.*

---

## V-04 — Three-phase; expanded Phase 0; C-42 as third BLOCKED/CLEAR signal; C-43 in Phase 2

**Axis**: Lifecycle emphasis. Three-phase with per-precondition expanded Phase 0 sections. C-43 retroactively PASS in R16 V-04. Estimated R16 V-04 base: ~31/33 (three-phase, not champion; misses criteria that V-05 champion had).

| Criterion group | Status | Evidence |
|---|---|---|
| C-01–C-41 (R16 criteria) | ~31/33 PASS | Three-phase base; champion (V-05) scored higher on at least one criterion in old rubric; lifecycle-heavy Phase 0 expansion may resolve or introduce tradeoffs |
| **C-42** | **PASS** | Expanded Phase 0 adds `format:` slot as third mechanism: narrative primes requirement (1), C-41 fill/leave-blank (2), C-42 value template (3) — triple-mechanism BLOCKED/CLEAR determination |
| **C-43** | **PASS** | Phase 2 self-test already includes contract label from R16 V-04 architecture |

**Composite: ~33/35 = ~9.43**

---

## V-05 — Three-phase champion + C-42 + C-43 + C-44 candidate (corrective scope)

**Axis**: Output format + role sequence. Based on R16 champion V-05 (33/33). R16 V-05 retroactively FAILED C-43 (cited REMEDIATION, omitted contract label). R17 V-05 self-test adds: (1) failure class, (2) contract label, (3) corrective scope by name, (4) REMEDIATION reference.

| Criterion group | Status | Evidence |
|---|---|---|
| C-01–C-41 (R16 criteria) | 33/33 PASS | R16 champion: all 33 R16 criteria satisfied; `── ENTRY GATE ──` visual delimiter, gate table with four columns, DIAGNOSTIC PATTERN four-field structure, C-40 compilation pointer all present |
| **C-42** | **PASS** | CLOSED-LABEL header now specifies value template — addresses R16 gap where `format: …` was unspecified ellipsis; row-level identifiability (C-38) now has its value shape closed |
| **C-43** | **PASS** | Self-test affirmative branch: failure class (`basis-negation`) + contract label (`Phase 2 charter violation`) + corrective scope + REMEDIATION reference — was missing contract label in R16 V-05 |
| C-44 candidate | N/A (not yet criterion) | Self-test prescribes corrective scope by name ("address a dimension Phase 1 did not confirm") — upgrades self-test from detector to prescriber; potential v18 criterion |

**Composite: 35/35 = 10.00**

---

## Rankings

| Rank | Variation | Score | Criteria passed |
|---|---|---|---|
| **1** | **V-05** | **35/35 = 10.00** | All; C-44 candidate emerges |
| 2 | V-03 | 34/35 = 9.71 | One R16 criterion missed; both new criteria satisfied |
| 3 | V-04 | ~33/35 = ~9.43 | Estimated; lifecycle expansion not sufficient to close R16 V-04 gap with champion |
| 4 | V-01 | 29/35 = 8.29 | Both targeted changes effective; single-phase ceiling is structural |
| 5 | V-02 | 29/35 = 8.29 | Ties V-01; register shift has no criterion effect |

---

## Excellence Signals (V-05)

**Signal 1 — Four-element self-test prescriber**
V-05's affirmative branch delivers: failure class + contract label + corrective scope + REMEDIATION reference. Each element targets a distinct failure mode: *what error was made* (failure class), *which structural guarantee is broken* (contract label), *what to fix* (corrective scope), *where to look* (REMEDIATION). This is the first instance of the self-test functioning as a complete prescriber rather than a detector. Prior variations detected and named; V-05 also directs repair.

**Signal 2 — Self-specifying column closure via C-41 + C-42**
V-05 achieves a fully self-specifying CLOSED-LABEL column: fill condition (C-41a) + leave-blank condition (C-41b) + value shape (C-42). All three constraints are resolvable from the header alone. A model filling BLOCKED rows cannot produce free-form prose — the header enforces `"Precondition [A/B]: [named condition]"` as the only valid value shape. C-38 row-level identifiability is now fully supported by column-level specification.

**Signal 3 — Contract label as structural escalation**
The addition of "a Phase 2 charter violation" upgrades the self-test diagnostic from content-level ("you made an error") to structural-level ("you violated a named guarantee"). This enables targeted correction — the model knows *which phase's invariant* was broken — rather than generic revision. V-03 demonstrated that the two-phase design could hold this label; V-05 confirms it fits the three-phase champion architecture without loss of other criteria.

**Signal 4 — C-44 candidate: corrective scope prescription**
V-05's self-test names repair scope alongside the violation: "address a dimension Phase 1 did not confirm." This closes the prescriptive chain: *detect* (self-test triggers) → *name* (contract label) → *prescribe* (repair scope). No prior variation reached all three links. C-44 warrants formalization in v18: "Self-test affirmative branch names the corrective scope required to satisfy the violated contract."

---

## Summary

V-05 achieves 35/35 (10.00) by combining the R16 champion architecture with both C-42 and C-43, while surfacing a C-44 candidate. V-03 demonstrates that two-phase variations with C-43 already present needed only one edit (filling the `format:` slot) to reach 34/35 — the minimum-change path to near-maximum. Single-phase variations plateau at 29/35 regardless of targeted changes; the ceiling is structural, not addressable by C-42/C-43 alone.

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["Four-element self-test prescriber: failure class + contract label + corrective scope + REMEDIATION reference — self-test functions as detector AND prescriber in a single branch", "C-44 candidate: corrective scope prescription names what repair is needed alongside the violated contract, closing the detect→name→prescribe chain for the first time"]}
```
