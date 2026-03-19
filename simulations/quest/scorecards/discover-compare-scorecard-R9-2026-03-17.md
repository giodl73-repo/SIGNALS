## discover-compare R9 — Scorecard

### Summary

| Variation | Axis | C-24 | C-09 | Composite | Golden |
|-----------|------|------|------|-----------|--------|
| V-01 | Grand composite | **PASS** | PASS | **100.00** | YES |
| V-02 | Add-C-only sub-ledger | **PARTIAL** | PASS | **99.71** | NO |
| V-03 | All-paths bare HALT | **PARTIAL** | PASS | **99.71** | NO |
| V-04 | Register-gated ordering | **PASS** | PASS | **100.00** | YES |
| V-05 | V-02 + V-04 combined | **PARTIAL** | PASS | **99.71** | NO |

---

### Key Resolutions

**V-01 C-24: PASS** — All three AMEND paths carry token-name enumeration ledgers before their HALT instructions. The "each path" requirement is satisfiable. 17/17 = 100.00 ceiling confirmed.

**V-02 vs V-03 C-24: both PARTIAL at equal score** — C-24 partial is path-agnostic. Asymmetric depth (V-02: one path full + two absent) and uniform breadth (V-03: all paths bare-halt) score identically. C-24 has no sub-grades within PARTIAL — breadth vs depth does not move the score.

**V-04 C-09: PASS (same as V-01)** — V-01's always-first does not carry a latent C-09 PARTIAL risk for engineering runs. Both forms are C-09 PASS. No super-PASS state exists. Register-gated ordering is a structural clarification, not a C-09 correction.

**V-04 C-23: PASS** — Conditional routing instruction does not add C-23 risk. Exec branch is unambiguously recommendation-first.

**V-05 interaction test: no interaction detected** — C-23 matches V-04 (PASS); C-24 matches V-02 (PARTIAL). Register-gating instruction is orthogonal to AMEND path gate scoring.

**Projected vs. Actual**: 5/5 confirmed.

---

### Two New Patterns

1. **register-gated-routing-valid** — conditional recommendation/matrix ordering by REG value satisfies C-23 and C-09 simultaneously via a single routing block; orthogonal to all other criteria (confirmed V-04)
2. **c24-partial-path-agnostic** — C-24 PARTIAL is a flat discrete state regardless of coverage distribution; no sub-grades within the PARTIAL band (confirmed V-02 = V-03)

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["register-gated-routing-valid: conditional recommendation/matrix ordering by REG value (exec->reco-first, engineering->matrix-first) satisfies C-23 and C-09 simultaneously via a single routing block; orthogonal to all other criteria including C-24 gate structure (confirmed V-04)", "c24-partial-path-agnostic: C-24 PARTIAL is a flat discrete state regardless of coverage distribution -- asymmetric depth (one path full, two absent: V-02) and uniform breadth (all paths bare-halt: V-03) score identically; C-24 has no sub-grades within the PARTIAL band (confirmed V-02 = V-03)"]}
```
t, engineering->matrix-first) satisfies C-23 and C-09 simultaneously via a single routing block before the output sections; the routing instruction is orthogonal to all other criteria including C-24 gate structure (confirmed V-04)
2. **c24-partial-path-agnostic** — C-24 PARTIAL is a flat state regardless of how partial coverage is distributed across AMEND paths; asymmetric depth (one path full, others absent) and uniform breadth (all paths bare-halt) score identically; C-24 has no sub-grades within the PARTIAL band (confirmed V-02 = V-03)

---

### Per-Variation Detail

---

#### V-01 — Grand composite (first v7 17/17)

**Axis**: R8 V-02 (phase-label-free) + R8 V-05 (recommendation-first) + all-path AMEND sub-ledgers

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | FEAS/INERT/RISK/COMP tokens present for both A and B |
| C-02 | PASS | Separate INERT-A and INERT-B phases, each with own TOKEN RECALL + FAULT |
| C-03 | PASS | 4-row decision matrix with Option 0/A/B columns |
| C-04 | PASS | Explicit recommendation slot: Option A / B / Neither / Conditional |
| C-05 | PASS | "If INERT-A = HIGH and INERT-B = HIGH: state Build neither is a candidate recommendation" |
| C-06 | PASS | "Distinct from RISK-A or explain overlap" instruction for RISK-B |
| C-07 | PASS | Three concrete AMEND paths with slot structure |
| C-08 | PASS | "Option 0: ANCHOR[0]" as named column in matrix |
| C-09 | PASS | REG-framed directives throughout; recommendation leads all registers (R8 V-05 confirmed PASS) |
| C-10 | PASS | LEDGER GATE lists all 10 tokens; blocking HALT present |
| C-11 | PASS | FAULT: "compare against ANCHOR[0] only -- Option A vs Option B comparison is an error" at each inertia phase |
| C-12 | PASS | REG + ANCHOR[0] token block + `---` divider before first FEAS directive |
| C-13 | PASS | TOKEN RECALL + "do not paraphrase" co-located at INERT-A and INERT-B |
| C-14 | PASS | FAULT: label co-located with TOKEN RECALL at each inertia phase |
| C-15 | PASS | REG token declared before ANCHOR[0] token |
| C-16 | PASS | "HALT -- do not proceed if any token is absent" in LEDGER GATE |
| C-17 | PASS | All content is directives and token slots; no explanatory prose |
| C-18 | PASS | Single-line FAULT encodes positive mandate (compare against ANCHOR[0] only) + negative prohibition (A vs B is error) |
| C-19 | PASS | Add-C: TOKEN RECALL + FAULT inline; Weight: TOKEN RECALL + FAULT inline; Override: TOKEN RECALL + FAULT inline |
| C-20 | PASS | Add-C recalls ANCHOR[0]; Weight recalls ANCHOR[0]; Override recalls REG only |
| C-21 | PASS | All three AMEND paths carry dual-polarity FAULT |
| C-22 | PASS | No PHASE N headers; structure via token block + `---` dividers only |
| C-23 | PASS | Recommendation precedes matrix in output (exec register aligned) |
| C-24 | **PASS** | Add-C: `Add-C ledger: FEAS-C [ ] INERT-C [ ] RISK-C [ ] COMP-C [ ]` + HALT; Weight: `Weight ledger: ANCHOR[0] [ ] WEIGHT [ ]` + HALT; Override: `Override ledger: REG [ ] REG-override [ ]` + HALT -- all three paths enumerate tokens before halt |

**Essential: 4/4 = 60.00 | Recommended: 3/3 = 30.00 | Aspirational: 17/17 = 10.00 | Composite: 100.00**

---

#### V-02 — Add-C-only sub-ledger (C-24 partial diagnostic)

**Axis**: Add-C path has mini-ledger + HALT; Weight and Override paths have TOKEN RECALL + FAULT only (no blocking gate, no token enumeration)

All criteria identical to V-01 except C-24.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-19 | PASS | All paths have inline TOKEN RECALL + FAULT + slot declaration; path self-containment satisfied without requiring blocking gates |
| C-20 | PASS | Same path-scoped recall as V-01 |
| C-21 | PASS | All three AMEND paths carry dual-polarity FAULT |
| C-24 | **PARTIAL** | Add-C: full mini-ledger + HALT (path-level pass); Weight: no blocking gate (outside C-24 domain per rubric); Override: no blocking gate (outside C-24 domain) -- "each AMEND path" requirement for PASS not satisfied; partial credit for one-path full coverage |

**Essential: 4/4 = 60.00 | Recommended: 3/3 = 30.00 | Aspirational: 16.5/17 = 9.71 | Composite: 99.71**

---

#### V-03 — All-paths bare HALT, no enumeration

**Axis**: All three AMEND paths carry a blocking HALT instruction but no token-name enumeration before any halt

All criteria identical to V-01 except C-24.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-19 | PASS | Add-C/Weight/Override each have inline TOKEN RECALL + FAULT + HALT; self-contained paths |
| C-24 | **PARTIAL** | All three paths carry blocking HALT but no token enumeration before halt -- satisfies C-24's literal partial condition uniformly ("blocking instruction present but without token enumeration = partial") at every path; same discrete score as V-02 despite different coverage distribution |

**C-24 discrimination vs V-02**: V-03 (all paths bare-halt) = V-02 (one path full + two no-gate). C-24 PARTIAL is path-agnostic -- breadth of partial coverage does not outweigh depth of single-path full coverage within the PARTIAL band. Both score 0.5/1.0 for C-24. C-24 has no sub-grades within PARTIAL.

**Essential: 4/4 = 60.00 | Recommended: 3/3 = 30.00 | Aspirational: 16.5/17 = 9.71 | Composite: 99.71**

---

#### V-04 — Register-gated recommendation ordering

**Axis**: Conditional routing block -- exec: recommendation first then matrix; engineering/general: matrix first then recommendation. All-path AMEND sub-ledgers preserved from V-01.

All criteria identical to V-01 except routing instruction added before output sections.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-09 | PASS | Routing explicitly routes engineering to DECISION MATRIX first (Feasibility row leads); exec gets RECOMMENDATION first; both register paths satisfy their respective C-09 framing requirements -- no regression from V-01's PASS; no super-PASS state exists |
| C-23 | PASS | exec path: RECOMMENDATION before DECISION MATRIX (C-23 pass condition satisfied); routing instruction is conditional but exec branch is unambiguously recommendation-first |
| C-24 | PASS | All-path mini-ledger + halt preserved from V-01 -- Add-C/Weight/Override all enumerate tokens before halt; routing instruction does not affect AMEND gate structure |

**C-09 resolution**: V-04 does not score C-09 higher than V-01. V-01's always-first carries no latent C-09 PARTIAL risk for engineering register runs -- the criterion is satisfied by REG-framed language throughout, not by output ordering alone. Register-conditional ordering is a structural clarification, not a C-09 correction.

**Essential: 4/4 = 60.00 | Recommended: 3/3 = 30.00 | Aspirational: 17/17 = 10.00 | Composite: 100.00**

---

#### V-05 — V-02 + V-04 combined

**Axis**: Register-gated ordering (V-04) + Add-C-only sub-ledger (V-02); Weight and Override paths have no blocking gate

All criteria follow from V-02 and V-04 independently. Interaction test.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-23 | PASS | exec path recommendation-first (same as V-04) -- routing instruction unchanged; Add-C-only sub-ledger does not affect C-23 |
| C-24 | PARTIAL | Add-C: full mini-ledger + HALT; Weight/Override: no blocking gate -- same as V-02; routing instruction does not affect AMEND path gate structure |

**Interaction test result**: C-23 matches V-04 (PASS); C-24 matches V-02 (PARTIAL). No interaction detected. Register-gating instruction is structurally orthogonal to AMEND path gate coverage. C-23 and C-24 are confirmed independent axes.

**Essential: 4/4 = 60.00 | Recommended: 3/3 = 30.00 | Aspirational: 16.5/17 = 9.71 | Composite: 99.71**

---

### Final Rankings

| Rank | Variation | Composite | Notes |
|------|-----------|-----------|-------|
| 1 | V-01 | **100.00** | First grand composite achieving all 17 v7 criteria |
| 1 | V-04 | **100.00** | Register-gated routing; explicit C-09 engineering alignment without criterion cost |
| 3 | V-02 | **99.71** | Add-C-only sub-ledger; C-24 PARTIAL |
| 3 | V-03 | **99.71** | All-paths bare HALT; C-24 PARTIAL (equal to V-02) |
| 3 | V-05 | **99.71** | V-02 + V-04 combined; C-23 PASS + C-24 PARTIAL |

**Golden candidates**: V-01 and V-04 (both 100.00). V-04 is the preferred form going forward: adds explicit register-conditional ordering that makes engineering alignment structurally visible (routing block before output sections) without any criterion cost on any of the 17 aspirational criteria.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["register-gated-routing-valid: conditional recommendation/matrix ordering by REG value (exec->reco-first, engineering->matrix-first) satisfies C-23 and C-09 simultaneously via a single routing block; orthogonal to all other criteria including C-24 gate structure (confirmed V-04)", "c24-partial-path-agnostic: C-24 PARTIAL is a flat discrete state regardless of coverage distribution -- asymmetric depth (one path full, two absent: V-02) and uniform breadth (all paths bare-halt: V-03) score identically; C-24 has no sub-grades within the PARTIAL band (confirmed V-02 = V-03)"]}
```
