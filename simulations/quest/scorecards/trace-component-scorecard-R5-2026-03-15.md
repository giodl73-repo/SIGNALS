## trace-component — Round 5 Scoring (v5 Rubric, 140 pts)

---

### Per-Variation Scoring

#### V-01 — Role Sequence: PASS-THROUGH + Targeted Gap Fixes

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Event chain complete | **PASS** (15) | TABLE §1 with consecutive rows, dispatch shown in Trigger column, UNKNOWN token required |
| C-02 | Component tree traversal | **PASS** (15) | TABLE §2 with Carrier Name column, every component from §1 required |
| C-03 | State delta shown | **PASS** (15) | TABLE §3 with before/after/derived selectors |
| C-04 | Re-render list complete | **PASS** (15) | TABLE §4 with YES/NO/UNKNOWN, Skip Mechanism, Upstream Reference columns — all §2 components required |
| C-05 | Side effects | **PASS** (10) | TABLE §5 with MISSING-LOADING/MISSING-ERROR tokens, Upstream Reference column |
| C-06 | Issue flags | **PASS** (10) | All 4 categories required; "none detected" must cite specific §4/§5 rows |
| C-07 | Final UI state | **PASS** (10) | §7 requires `"derived from §3 row '[key]'"` citation for every item |
| C-08 | Optimization opportunities | **PASS** (5) | Mandatory §8 table with Expected Render Reduction column; no-optimization path must cite §4 NO rows |
| C-09 | Framework-portable annotations | **PASS** (5) | §9 Framework Notes for every MAP entry; Role 2 binding enforces neutral vocabulary in core |
| C-10 | Gap-visible format | **PASS** (5) | Explicit table schemas for §1 and §4; missing rows structurally visible |
| C-11 | Cross-section evidence chaining | **PASS** (5) | Upstream Reference column required in §4, §5; §6 requires §4/§5 row citations; §7 requires §3 citation — full chain traceable |
| C-12 | Explicit incompleteness tokens | **PASS** (5) | UNKNOWN in §1/§3/§4; MISSING-LOADING/MISSING-ERROR in §5; completeness stamp aggregates |
| C-13 | Framework-neutral core enforcement | **PASS** (5) | Role 2 binding constraint: "Any MAP term appearing in §1–§7 outside §9 is a vocabulary violation"; Role 3 §11 audits |
| C-14 | Vocabulary Contract as pre-trace artifact | **PASS** (5) | Role 1 produces §0 before trace content; Role 2 bound to it; Role 3 §11 audits for vocabulary leaks |
| C-15 | Machine-readable incompleteness inventory | **PASS** (5) | §10 structured block with all categories; cross-check record required |
| C-16 | PASS-THROUGH designation | **PASS** (5) | Disposition column explicitly declared in §0 four-column table; "mandatory named column — omitting it is a contract failure" |
| C-17 | Active mismatch correction | **PASS** (5) | Role 3 §10 active correction protocol with Corrected/Cross-checked format; cross-check required even with no corrections |

**V-01: 140/140 — GOLDEN**

---

#### V-02 — Output Format: Vocabulary Block + Token Rows + Citation Column

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Event chain complete | **PASS** (15) | TABLE-01 schema declared; "No prose. No rows omitted. Missing rows are Gap Token rows." |
| C-02 | Component tree traversal | **PASS** (15) | TABLE-02 with direction/carrier/signal type columns |
| C-03 | State delta shown | **PASS** (15) | TABLE-03 schema |
| C-04 | Re-render list complete | **PASS** (15) | TABLE-04 with Upstream Ref column required for every row |
| C-05 | Side effects | **PASS** (10) | TABLE-05 with MISSING-LOADING/MISSING-ERROR, Upstream Ref required |
| C-06 | Issue flags | **PASS** (10) | All 4 categories; "none detected" must cite TABLE-04/TABLE-05 rows |
| C-07 | Final UI state | **PASS** (10) | §7 derivation citation required for every item |
| C-08 | Optimization opportunities | **PASS** (5) | TABLE-06 declared in format contract; no-optimization row must cite §4 refs |
| C-09 | Framework-portable annotations | **PARTIAL** (3) | §9 Framework Notes exists; MAP instruction present but no role-blocking to keep core clean |
| C-10 | Gap-visible format | **PASS** (5) | TABLE-01 and TABLE-04 are explicit schemas; "required column left blank must contain gap token" |
| C-11 | Cross-section evidence chaining | **PASS** (5) | Upstream Ref in TABLE-04 (→§3), TABLE-05 (→§1); §6 cites TABLE-04/05; §7 cites §3 — 4 downstream sections |
| C-12 | Explicit incompleteness tokens | **PASS** (5) | Gap Token column in all tables; MISSING tokens in TABLE-05 |
| C-13 | Framework-neutral core enforcement | **PARTIAL** (3) | MAP instruction states constraint; no blocking role prevents jargon in cell values |
| C-14 | Vocabulary Contract as pre-trace artifact | **FAIL** (0) | Vocabulary contract table present and binding stated, but no subsequent audit role or step — "where the audit step is absent does not pass" |
| C-15 | Machine-readable incompleteness inventory | **PASS** (5) | Post-trace stamp with structured block; cross-check record required |
| C-16 | PASS-THROUGH designation | **FAIL** (0) | C-14 fails; depends relationship violated — "Awarding C-16 without C-14 is a scoring error" |
| C-17 | Active mismatch correction | **PASS** (5) | Post-trace stamp has "Corrected: [category] [old] → [new]; additional [TOKEN] at [§N]" format with cross-check clause; C-15 passes so C-17 may score |

**V-02: 126/140 — GOLDEN**

---

#### V-03 — Lifecycle Emphasis: Phase-Gated with Optimization Phase

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Event chain complete | **PASS** (15) | Phase 1 with function name/owner/event type/propagation/timing per handler; UNKNOWN tokens |
| C-02 | Component tree traversal | **PASS** (15) | Phase 2 with carrier names, direction, UNKNOWN tokens |
| C-03 | State delta shown | **PASS** (15) | Phase 3 with before/after/selectors |
| C-04 | Re-render list complete | **PASS** (15) | Phase 4 — every Phase 2 component required with reason and skip mechanism |
| C-05 | Side effects | **PASS** (10) | Phase 5 with owner/timing/loading/error branches; MISSING tokens |
| C-06 | Issue flags | **PASS** (10) | Phase 6 with all 4 categories; "none" conclusions reference Phase 4/5 Registries |
| C-07 | Final UI state | **PASS** (10) | Phase 6 final UI state with `"Phase 3 key '[key]'"` citation per item |
| C-08 | Optimization opportunities | **PASS** (5) | Dedicated Phase 7 mandatory; no-optimization path must cite Phase 4 skipped rows |
| C-09 | Framework-portable annotations | **FAIL** (0) | No §9 Framework Notes / dedicated annotation layer in the variation |
| C-10 | Gap-visible format | **PARTIAL** (3) | Phase registries make missing identifiers visible; per-phase enumeration is structured but no explicit table schemas declared |
| C-11 | Cross-section evidence chaining | **PASS** (5) | Registry-consume headers name specific identifiers from prior registry; Phase 4 consumes Phase 3 keys; Phase 7 cites Phase 4; Phase 6 final UI cites Phase 3 keys |
| C-12 | Explicit incompleteness tokens | **PASS** (5) | UNKNOWN per phase; MISSING-LOADING/MISSING-ERROR in Phase 5; Completeness Inventory |
| C-13 | Framework-neutral core enforcement | **FAIL** (0) | No vocabulary contract; no binding to neutral terms |
| C-14 | Vocabulary Contract as pre-trace artifact | **FAIL** (0) | No pre-trace vocabulary contract |
| C-15 | Machine-readable incompleteness inventory | **PASS** (5) | Structured Completeness Inventory block at end with all four categories |
| C-16 | PASS-THROUGH designation | **FAIL** (0) | C-14 fails; dependency violated |
| C-17 | Active mismatch correction | **FAIL** (0) | Completeness Inventory has no re-scan instruction or correction protocol |

**V-03: 113/140 — GOLDEN** (all essential pass; 113 ≥ 112 threshold)

---

#### V-04 — Phrasing Register: Imperative Per-Criterion Checklist

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Event chain complete | **PASS** (15) | STEP 2: "List EVERY handler... in causal order... consecutive items with dispatch shown... UNKNOWN: [name] — [reason]" |
| C-02 | Component tree traversal | **PASS** (15) | STEP 3: every hop requires from/to/direction/carrier name |
| C-03 | State delta shown | **PASS** (15) | STEP 4: "Use a table" with before/after/selectors and UNKNOWN tokens |
| C-04 | Re-render list complete | **PASS** (15) | STEP 5: every §2 component required with YES/NO, reason, skip mechanism |
| C-05 | Side effects | **PASS** (10) | STEP 6: owner/timing/success-state/error-state with MISSING tokens |
| C-06 | Issue flags | **PASS** (10) | STEP 7: all 4 categories with mandatory "none" citations |
| C-07 | Final UI state | **PASS** (10) | STEP 8: `"[Element] — §3 row '[key]'"` citation required per item |
| C-08 | Optimization opportunities | **PASS** (5) | STEP 9: "Name at least one concrete optimization... expected render reduction... per §4 row N"; explicit no-optimization path with §4 NO rows cited |
| C-09 | Framework-portable annotations | **PARTIAL** (3) | STEP 10 labeled §9 is a dedicated annotation layer; no vocabulary enforcement to keep core neutral |
| C-10 | Gap-visible format | **PARTIAL** (3) | STEP 4 says "Use a table" for state delta; §1 and §4 are list instructions — enumeration possible but no explicit table schema declarations |
| C-11 | Cross-section evidence chaining | **PASS** (5) | STEP 5: "cite the §3 row that caused it"; STEP 7: "Name the §4 row / §5 row"; STEP 8: "cite the §3 state key" — 3 downstream sections with explicit upstream citation mandates |
| C-12 | Explicit incompleteness tokens | **PASS** (5) | UNKNOWN in STEP 2/3/4; MISSING-LOADING/MISSING-ERROR in STEP 6 |
| C-13 | Framework-neutral core enforcement | **FAIL** (0) | No vocabulary contract; STEP 10 annotation layer exists but no binding constraint on STEP 2–8 |
| C-14 | Vocabulary Contract as pre-trace artifact | **FAIL** (0) | No pre-trace vocabulary contract table |
| C-15 | Machine-readable incompleteness inventory | **PASS** (5) | STEP 11 structured stamp block |
| C-16 | PASS-THROUGH designation | **FAIL** (0) | C-14 fails; dependency violated |
| C-17 | Active mismatch correction | **PASS** (5) | STEP 11: "re-read §1–§8 and verify... Corrected: [category] [old] → [new]; missed [TOKEN] at [§N reference]. Cross-checked: counts match." — category/before/after/location present; C-15 passes |

**V-04: 121/140 — GOLDEN**

---

#### V-05 — Combined: Role Sequence + Lifecycle Emphasis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Event chain complete | **PASS** (15) | Phase 1 table with handler/trigger/owner/timing; UNKNOWN tokens |
| C-02 | Component tree traversal | **PASS** (15) | Phase 2 table with carrier names; registry-consume naming Phase 1 components explicitly |
| C-03 | State delta shown | **PASS** (15) | Phase 3 table with before/after/selectors/UNKNOWN |
| C-04 | Re-render list complete | **PASS** (15) | Phase 4 table — every Phase 2 component; Phase 3 Key Ref required |
| C-05 | Side effects | **PASS** (10) | Phase 5 table with MISSING tokens; Phase 1 Ref column required |
| C-06 | Issue flags | **PASS** (10) | Phase 6 all 4 categories; "none" cites Phase 4/5 Registry explicitly |
| C-07 | Final UI state | **PASS** (10) | Phase 6 final state: `"Phase 3 key '[key]'"` required per item |
| C-08 | Optimization opportunities | **PASS** (5) | Phase 7 mandatory table; no-optimization path cites Phase 4 skipped rows |
| C-09 | Framework-portable annotations | **PASS** (5) | §9 Framework Notes for every §0 MAP entry; Role 2 binding enforces neutral core |
| C-10 | Gap-visible format | **PASS** (5) | All phases use table schemas with Phase Registry headers — missing entries structurally visible |
| C-11 | Cross-section evidence chaining | **PASS** (5) | Registry-consume headers name specific identifiers per phase; §4 Phase 3 Key Ref; §5 Phase 1 Ref; §7 Phase 3 derivation; §12 Evidence Chain Audit verifies all links |
| C-12 | Explicit incompleteness tokens | **PASS** (5) | UNKNOWN in Phases 1–4; MISSING tokens in Phase 5; Phase 5 Registry tracks them |
| C-13 | Framework-neutral core enforcement | **PASS** (5) | Role 2 "binding constraint: §1–§7 use only Neutral Equivalents for MAP terms"; Role 3 §11 scans for MAP term leaks and alias violations |
| C-14 | Vocabulary Contract as pre-trace artifact | **PASS** (5) | Role 1 produces §0 before any trace content; Role 2 bound to it; Role 3 §11 audits for vocabulary leaks |
| C-15 | Machine-readable incompleteness inventory | **PASS** (5) | Role 3 §10 structured block; "cross-check record is required even when no corrections are needed" |
| C-16 | PASS-THROUGH designation | **PASS** (5) | §0 Disposition column explicitly declared; "A contract without it fails C-16"; C-14 passes so dependency met |
| C-17 | Active mismatch correction | **PASS** (5) | Role 3 §10 active correction protocol with category/before→after/location format; C-15 passes |

**V-05: 140/140 — GOLDEN**

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | Band |
|-----------|-----------|-------------|-------------|-------|------|
| V-01 | 60/60 | 30/30 | 50/50 | **140/140** | GOLDEN |
| V-05 | 60/60 | 30/30 | 50/50 | **140/140** | GOLDEN |
| V-02 | 60/60 | 30/30 | 36/50 | **126/140** | GOLDEN |
| V-04 | 60/60 | 30/30 | 31/50 | **121/140** | GOLDEN |
| V-03 | 60/60 | 30/30 | 23/50 | **113/140** | GOLDEN |

All variations pass all essential criteria. All five are GOLDEN band (≥112).

---

### Excellence Signals

**From V-01 and V-05 (tied at 140/140):**

**1. PASS-THROUGH as a declared named column, not a prose instruction.** The Disposition column in §0 forces an explicit MAP vs PASS-THROUGH decision for every term before the trace begins. This makes source-navigability preservation structural — the author cannot accidentally alias `useProductStore` to `StateManager` when PASS-THROUGH is a column they must fill, not a rule they must remember.

**2. Mandatory cross-check record even when no corrections are needed.** The `"Cross-checked: counts match body; no corrections required."` output is required regardless of whether corrections were made. This design ensures the correction mechanism is always exercised, not just present as a conditional. A stamp without the cross-check record is incomplete — the protocol is non-skippable.

**3. Citation columns enforced structurally (not just instructed in prose).** Upstream Reference in §4/§5, Phase 3 Key Ref in §4, Phase 1 Ref in §5 are required columns. An empty cell in a required column is visually anomalous; a missing prose citation is invisible. Moving citations from "follow this instruction" to "fill this column" eliminates silent omission.

**4. Blocking role prevents vocabulary leakage structurally.** V-01 and V-05 both use a Role 1 that produces only the vocabulary contract and nothing else, with the subsequent role explicitly bound to it and an audit role scanning for violations. This three-layer structure (produce → bind → audit) is the mechanism that achieves C-13/C-14/C-16 reliably, while V-02's single-layer (produce + instruct) achieves only C-15/C-17 because auditing is absent.

**5. §8 Optimizations as a required section with a mandatory evidence citation path.** Making the optimization section required and giving it a no-optimization exit that must cite §4 NO rows closes both silent-omission paths: omitting the section entirely, and writing an unsupported "no optimization" claim.

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["PASS-THROUGH designation as a named Disposition column in the vocabulary contract makes source-navigability preservation structural — the column forces an explicit decision for every codebase identifier before the trace begins, preventing neutral aliasing without relying on the author to remember a prose rule", "Active correction protocol with mandatory cross-check record required even when no corrections are needed — the protocol is always exercised, turning the completeness stamp from a conditional correction mechanism into a non-skippable audit operation"]}
```
