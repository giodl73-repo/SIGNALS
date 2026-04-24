Now I have everything needed. Let me produce the full R20 scorecard.

---

## flow-lifecycle — Round 20 Scorecard (rubric v20)

---

### Scoring Basis

Denominator: 58 | Aspirational: 50 | All essential must PASS

Scoring: PASS = 1pt · PARTIAL = 0.5pt · FAIL = 0pt

---

### Key Discriminating Criteria (R20 Probes)

**C-57 (Gate Defect D-ID Cross-Reference — TARGET / HOLD):**

Each named defect category in the gate sentence must carry a parenthetical D-ID designator — e.g., "an unterminated path (D-01), an uncertified exception handler (D-02), an unresolvable decision owner (D-03)" — linking the gate text row-specifically to the scan-table defect taxonomy.

- **V-01:** R19 V-01 gate already carried "(D-01), (D-02), (D-03)" on every enumerated category. HOLD from R19 confirmed. → **PASS**
- **V-02:** Same gate structure as V-01 (Column Contract axis does not touch gate text). HOLD confirmed. → **PASS**
- **V-03:** Same D-ID gate structure as V-01/V-02. HOLD confirmed. Phase-first framing axis is upstream of gate; gate text unchanged. → **PASS**
- **V-04:** R19 V-04 had plain prose: "an unterminated path, an uncertified exception handler, an unresolvable decision owner" — no D-IDs (C-55 PASS but C-57 would FAIL on v20 rubric). R20 TARGET applied: gate text updated to add parenthetical D-IDs on every inline category. → **PASS**
- **V-05:** R19 V-05 carried D-IDs (full-floor inherited from V-01 structure). HOLD confirmed. AC-31 added to Coverage Scan. → **PASS**

**C-58 (Parenthetical Eligibility Binding Format — TARGET / HOLD):**

Each typed escape code in LT-ID Trace and Entry Trigger column headers must use code-token + immediately-adjacent parenthetical format — "SECONDARY (use only when...)" — without intervening instruction verb or separator.

- **V-01:** R19 V-01 LT-ID Trace header: "SECONDARY (use only when role has no LT-bound trigger, naming why this role exists without any LT anchor)" — parenthetical form, no separator. HOLD confirmed. → **PASS**
- **V-02:** Same column header structure. Column Contract format axis does not alter column header escape code binding. HOLD confirmed. → **PASS**
- **V-03:** Same column header structure. Phase-first framing does not alter escape code column headers. HOLD confirmed. → **PASS**
- **V-04:** R19 V-04 used: "write SECONDARY -- but only when role has no LT-bound trigger at all, and explain why it exists outside any trigger scope" — dash-separator imperative form (C-56 PASS but C-58 FAIL on v20 rubric). R20 TARGET applied: updated to "SECONDARY (use only when...)" parenthetical binding format. → **PASS**
- **V-05:** R19 V-05 carried parenthetical form (full-floor). HOLD confirmed. AC-32 added to Coverage Scan. → **PASS**

**C-34 (Pre-Declaration Role Registry — carry-forward from R19):**
- V-01: PASS (pre-declaration block present)
- V-02: FAIL (no pre-declaration block; role registry first appears at STEP 1 after SQ Declaration)
- V-03: FAIL (role registry at STEP 1)
- V-04: PASS ("Start Here: Domain Role Registry" precedes FM-ID Guidance)
- V-05: PASS (pre-declaration block present)

**C-29 / C-31 (Decision Condition Threshold — carry-forward from R19):**
- V-03: C-29 PARTIAL (abbreviated threshold header), C-31 FAIL (neither mechanism inline)
- All others: PASS on both

---

### Per-Variation Full Scores

#### V-01 — Role Sequence: Pre-Declaration + C-57/C-58 HOLD/PASS

| Group | Score |
|-------|-------|
| Essential C-01–C-05 | 5/5 |
| Recommended C-06–C-08 | 3/3 |
| Aspirational C-09–C-33 | 25/25 |
| C-34 (pre-declaration) | 1/1 PASS |
| C-35–C-41 | 7/7 PASS |
| C-42–C-54 | 13/13 PASS |
| C-55 | 1/1 PASS (HOLD) |
| C-56 | 1/1 PASS (HOLD) |
| **C-57** | **1/1 PASS** — parenthetical D-IDs stable from R19 V-01; AC-31 PASS |
| **C-58** | **1/1 PASS** — parenthetical binding stable from R19 V-01; AC-32 PASS |
| **Total** | **58/58** |

Single-axis test confirms C-57/C-58 are position-invariant relative to role-sequence structural arrangement. D-21/D-22 formalized in taxonomy; AC-31/AC-32 added to Coverage Scan Group B.

---

#### V-02 — Column Contract + C-57/C-58 HOLD/PASS

| Group | Score |
|-------|-------|
| Essential C-01–C-05 | 5/5 |
| Recommended C-06–C-08 | 3/3 |
| Aspirational C-09–C-33 | 25/25 |
| C-34 (pre-declaration) | 0/1 **FAIL** — no pre-declaration block |
| C-35–C-41 | 7/7 PASS |
| C-42–C-54 | 13/13 PASS |
| C-55 | 1/1 PASS (HOLD) |
| C-56 | 1/1 PASS (HOLD) |
| **C-57** | **1/1 PASS** — D-IDs stable in gate text; Column Contract axis does not touch gate sentence; AC-31 PASS |
| **C-58** | **1/1 PASS** — parenthetical binding stable in column headers; Column Contract field definitions are a distinct layer from escape code column headers; AC-32 PASS |
| **Total** | **57/58** |

C-34 carry-forward fail unchanged. C-57/C-58 confirm independence from column-format axis — the Column Contract definition layer does not interact with gate-sentence D-IDs or escape-code column header binding format.

---

#### V-03 — Phase-First Framing + GATE SQ + C-57/C-58 HOLD/PASS

| Group | Score |
|-------|-------|
| Essential C-01–C-05 | 5/5 |
| Recommended C-06–C-08 | 3/3 |
| Aspirational C-09–C-33 (excl. C-29, C-31) | 23/23 PASS |
| C-29 (threshold taxonomy) | 0.5/1 **PARTIAL** — carry-forward from R19 |
| C-31 (dual-mechanism) | 0/1 **FAIL** — carry-forward from R19 |
| C-34 (pre-declaration) | 0/1 **FAIL** — carry-forward from R19 |
| C-35–C-41 | 7/7 PASS |
| C-42–C-54 (GATE SQ) | 13/13 PASS |
| C-55 | 1/1 PASS (HOLD) |
| C-56 | 1/1 PASS (HOLD) |
| **C-57** | **1/1 PASS** — D-IDs stable in gate text; phase-first framing axis is pre-gate; no interaction; AC-31 PASS |
| **C-58** | **1/1 PASS** — parenthetical binding stable; phase framing block does not alter escape code column headers; AC-32 PASS |
| **Total** | **55.5/58** |

Three carry-forward misses (C-29 PARTIAL, C-31 FAIL, C-34 FAIL) unchanged. C-57/C-58 confirm independence from phase-framing and GATE SQ axes. Denominator expansion adds 2 full passes, improving absolute position but not closing the three persistent gaps.

---

#### V-04 — Phrasing Register + Role Sequence + C-57 TARGET + C-58 TARGET

| Group | Score |
|-------|-------|
| Essential C-01–C-05 | 5/5 |
| Recommended C-06–C-08 | 3/3 |
| Aspirational C-09–C-33 | 25/25 |
| C-34 (pre-declaration) | 1/1 PASS |
| C-35–C-41 | 7/7 PASS |
| C-42–C-54 | 13/13 PASS |
| C-55 | 1/1 PASS (HOLD — register-neutral confirmed R19) |
| C-56 | 1/1 PASS (HOLD) |
| **C-57** | **1/1 PASS** — TARGET applied: gate text updated from plain prose to "(D-01), (D-02), (D-03)" parenthetical D-ID form on every inline category; AC-31 PASS |
| **C-58** | **1/1 PASS** — TARGET applied: LT-ID Trace header updated from "write SECONDARY -- but only when..." to "SECONDARY (use only when...)" parenthetical binding format; Entry Trigger header unchanged (DERIVED parenthetical already present); AC-32 PASS |
| **Total** | **58/58** |

Key finding: Conversational register is fully compatible with both parenthetical D-ID cross-references (C-57) and parenthetical eligibility binding (C-58). The two TARGET updates are typographically localized — the gate sentence and LT-ID Trace column header are edited in isolation; no surrounding conversational vocabulary in the document is altered. V-04 convergence to 58/58 confirms that notation formality is a local, targeted property, not a document-register property.

---

#### V-05 — Full Combination Floor + C-57/C-58 HOLD/PASS Stability Confirmation

| Group | Score |
|-------|-------|
| Essential C-01–C-05 | 5/5 |
| Recommended C-06–C-08 | 3/3 |
| Aspirational C-09–C-33 | 25/25 |
| C-34 (pre-declaration) | 1/1 PASS |
| C-35–C-41 | 7/7 PASS |
| C-42–C-54 | 13/13 PASS (GATE SQ + inertia-first + dual-position C-53 + mutual-audit C-49) |
| C-55 | 1/1 PASS (HOLD) |
| C-56 | 1/1 PASS (HOLD) |
| **C-57** | **1/1 PASS** — HOLD confirmed; D-IDs present across all gate categories; D-21 formalized in taxonomy; AC-31 PASS |
| **C-58** | **1/1 PASS** — HOLD confirmed; parenthetical binding present in all escape code headers; D-22 formalized in taxonomy; AC-32 PASS |
| **Total** | **58/58** |

Full-floor formalization pattern extends to R20: explicit addition of D-21/D-22 to Defect Type Taxonomy and AC-31/AC-32 to Coverage Scan Group B is score-neutral for a structure already passing C-57 and C-58. The formalization converts implicit structural coverage into explicit taxonomy entries — same criterion satisfaction, higher verifiability.

---

### Ranking

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| **1** | **V-01** | **58/58** | YES | Single-axis role-sequence; C-57/C-58 HOLD/PASS confirmed axis-independent |
| **1** | **V-04** | **58/58** | YES | Register-neutrality extended to D-ID notation and parenthetical binding; conversational variant fully converged |
| **1** | **V-05** | **58/58** | YES | Full floor; D-21/D-22/AC-31/AC-32 formalization; richest verifiable implementation |
| 4 | V-02 | 57/58 | YES | C-34 carry-forward fail; Column Contract otherwise stable across C-57/C-58 |
| 5 | V-03 | 55.5/58 | YES | Three persistent gaps (C-29 PARTIAL, C-31 FAIL, C-34 FAIL); C-57/C-58 HOLD/PASS confirmed non-interacting |

Three-way tie at 58/58. V-05 ranked first among equals by implementation depth — explicit D-21/D-22 taxonomy entries, GATE SQ, inertia-first ordering, and dual-position C-53 coverage make it the most auditable and complete.

---

### Excellence Signals from Top-Scoring Variations

**1. C-57 and C-58 are strictly local typographic properties.** V-04's TARGET updates confirm that adding parenthetical D-IDs to gate-sentence categories (C-57) and converting dash-separator imperative escape codes to code-token + parenthetical format (C-58) are edits scoped to a single sentence and a single column header respectively. No surrounding structure — role sequence, phase framing, SQ Declaration format, or phrasing register — is altered. Any future variation at any structural axis can satisfy C-57 and C-58 through two isolated point-edits.

**2. Conversational register is fully notation-compatible.** V-04 at 58/58 establishes that parenthetical D-ID cross-references and parenthetical eligibility binding are not register markers for formal schemas — they are typographic binding conventions that appear identically in conversational-register documents. The D-ID parenthetical "(D-01)" and the eligibility parenthetical "(use only when...)" are syntactically neutral; the surrounding sentence register does not interact with them.

**3. The formalization-only upgrade pattern is a proven, scalable mechanism.** V-05 confirms for the third consecutive round (R18 → R19 → R20) that explicitly adding taxonomy entries and scan rows for newly formalized criteria is score-neutral for structures already structurally satisfying those criteria. D-21/D-22/AC-31/AC-32 in V-05 follow the same pattern as D-19/D-20/AC-29/AC-30 (R19) and D-17/D-18/AC-27/AC-28 (R18). The pattern is reliable: the full-floor variation can absorb any new criterion pair via formalization without structural risk.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-57 and C-58 are strictly local typographic properties — parenthetical D-ID cross-references and parenthetical eligibility binding are point-edits to a single gate sentence and a single column header; no structural axis (role sequence, phase framing, column format, phrasing register) interacts with either criterion", "conversational register is fully notation-compatible — parenthetical D-ID and parenthetical eligibility binding appear identically in conversational-register documents; register does not interact with notation formality at the sentence or column-header level"]}
```
