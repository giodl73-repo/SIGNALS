# flow-ratelimit — Quest Score R4

**Rubric**: v4-2026-03-17 | **N_essential=5, N_recommended=3, N_aspirational=11** | **Max=120**

> **Note on scope**: V-01 is the only fully-specified prompt in this round's variate document. V-02–V-05 are estimated from their variation axes and R3 patterns; estimates are labeled as such.

---

## V-01 — Cascading Gate Chain (full prompt, scored in detail)

**Axis**: Role sequence with explicit per-transition gate language naming specific prior-role deliverables at every boundary.

### Essential (C-01–C-05)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Binding Constraint + Ordering | **PASS** | ROLE 1 mandates CLAIM-A with component name + numeric threshold + causal binding sentence. ROLE 3 requires binding-order rationale sentence per component. |
| C-02 | Causal Chain to User Effect | **PASS** | ROLE 4 requires ≥2 directed hops, each naming a mechanism from the allowed list (queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade), chain must terminate at a user-observable effect. |
| C-03 | UX at Each Throttle Tier | **PASS** | ROLE 6 provides the four-field template per tier; rules explicitly reject prose coverage and partial templates. ≥2 tiers required. |
| C-04 | Unprotected Burst Path | **PASS** | ROLE 5 three-control checklist; higher-tier controls don't qualify; STRUCTURAL/INCIDENTAL classification required per unprotected path. |
| C-05 | Retry-After Handling Gap | **PASS** | ROLE 7 evaluates each connector/action, checks `Retry-After-Ms` and `x-ms-ratelimit-remaining` equivalents, names failure mode per gap. |

**Essential: 5/5 → 60 pts**

### Recommended (C-06–C-08)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Cascading Throttle Failure | **PASS** | ROLE 9 mandates two named rate limits with numeric thresholds, explicit causal link, and compounding effect. Disqualifies two independent limits. |
| C-07 | Numeric Rate Limit Specificity | **PASS** | ROLE 3 requires number + unit; [estimated] label permitted for non-public values. |
| C-08 | Volume-to-Behavior Mapping | **PASS** | ROLE 8 structured BASELINE/PROTECTED table at 1x, 2x, 5x; FORMAT CONTRACT schema enforced. |

**Recommended: 3/3 → 30 pts**

### Aspirational (C-09–C-19)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Per-bottleneck Mitigation | **PASS** | ROLE 10 requires specific action/connector/setting; "add retry logic" without location explicitly fails. |
| C-10 | Quantified Impact at Load Spike | **PASS** | ROLE 8 mandates step-by-step arithmetic for 5x BASELINE: % queued >30s and % failing after retries, traceable to ROLE 3 numerics. Qualitative-only cell flagged INCOMPLETE. |
| C-11 | Burst Gap Classification | **PASS** | ROLE 5 mandates explicit STRUCTURAL or INCIDENTAL label with stated justification per unprotected path. |
| C-12 | Dual-state Volume Mapping | **PASS** | ROLE 8 gate requires BASELINE + PROTECTED columns at all three bands before ROLE 9 begins. |
| C-13 | Verdict-before-Evidence | **PASS** | ROLE 1 is gated "write first, before any other output." Gate 2 blocks ROLE 2 until VERDICT claims are present, preventing any evidence role from starting without the verdict. |
| C-14 | Baseline-delta Mitigation | **PASS** | ROLE 10 table requires BASELINE (behavior at bottleneck before mitigation, tied to component + load) and PROTECTED (behavior after, naming exact control + location). Requires C-09 ✓. |
| C-15 | Document-head Global Verdict | **PASS** | ROLE 1 opens before all other roles with a self-contained VERDICT carrying (a) component + threshold, (b) gap location + type, (c) SAFE/DEGRADED/FAILING. Requires C-01, C-04 ✓. |
| C-16 | Format Contract Preamble | **PASS** | ROLE 2 declares BASELINE definition (scenario-specific, not generic), PROTECTED definition (scenario-specific), column schema, and rejection rule. ROLES 8 and 10 both supply compliant tables. Requires C-08, C-12 ✓. |
| C-17 | Cascading Section Gate Enforcement | **PASS** | 8 gated transitions beyond the two preambles (Roles 3–10), each naming specific deliverables from the prior role — e.g., "Rate Limit Registry with numeric threshold and binding-order rationale sentence" (gate to Role 4); "Burst Path Audit with STRUCTURAL/INCIDENTAL and CLAIM-B confirmation" (gate to Role 6); "Volume Map with numeric arithmetic in 5x cell" (gate to Role 9). Requires C-15, C-16 ✓. |
| C-18 | Bidirectional Verdict Revision | **PASS** | Final reconciliation mandates returning to the VERDICT block and inserting `[REVISED — see ROLE N]` inline after each revised claim label, with forward reference. Criterion requires Verdict "contains" markers — reconciliation ensures they are present before the document is final. Requires C-15 ✓. |
| C-19 | Four-Field UX Tier Template | **PASS** | ROLE 6 declares explicit template with labeled fields (a)–(d). Rules explicitly reject partial templates and prose substitution even if all four topics appear. ≥2 distinct tiers required. Declared within the producing role, not only in Format Contract. Requires C-03 ✓. |

**Aspirational: 11/11 → 30 pts**

### V-01 Total: **120 / 120** — GOLD ✓ (all essential pass + composite ≥ 95)

---

## V-02–V-05 — Estimated Scores

*(Variation axes only; full prompts not present in this round's document. Estimates derived from R3 patterns and stated axes.)*

### V-02 — Four-Field UX Template axis (targets C-19 only)

Explicitly targets C-19 via Format-Contract-declared four-field template. Does not target C-17 or C-18.

| Criterion | Estimate | Basis |
|-----------|----------|-------|
| C-01–C-05 | 5/5 PASS | Covered in prior rounds |
| C-06–C-08 | 3/3 PASS | Covered in prior rounds |
| C-09–C-16 | 8/8 PASS | Covered in prior rounds |
| C-17 | **FAIL** | Not targeted; role transitions use sequential instruction without per-deliverable gate language |
| C-18 | **FAIL** | Not targeted; no bidirectional Verdict revision mechanism |
| C-19 | **PASS** | Primary axis — four-field template declared in Format Contract |

**Estimated: 60 + 30 + 9/11 × 30 ≈ 114.5 — GOLD** (all essential pass, but 2 aspirational fail)

---

### V-03 — Bidirectional Verdict Revision axis (targets C-18 only)

Phase lifecycle with live-updating Verdict blocks. Based on R3 V-03 pattern.

| Criterion | Estimate | Basis |
|-----------|----------|-------|
| C-01–C-05 | 5/5 PASS | Covered in prior rounds |
| C-06–C-08 | 3/3 PASS | Covered in prior rounds |
| C-09–C-16 | 8/8 PASS | Covered in prior rounds |
| C-17 | **FAIL** | Phase structure uses sequential mandates, not per-transition deliverable-naming gates |
| C-18 | **PASS** | Primary axis — each phase immediately inserts `[REVISED — see Phase N]` into Verdict block when it revises a claim |
| C-19 | **PARTIAL** | UX tier section likely exists from R3 base but four-field template not Format-Contract-enforced |

**Estimated: 60 + 30 + 9.5/11 × 30 ≈ 115.9 — GOLD**

---

### V-04 — Gate Chain + Bidirectional Revision (targets C-17 + C-18)

Combines V-01's cascading gates with V-03's live-updating Verdict.

| Criterion | Estimate | Basis |
|-----------|----------|-------|
| C-01–C-05 | 5/5 PASS | Covered |
| C-06–C-08 | 3/3 PASS | Covered |
| C-09–C-16 | 8/8 PASS | Covered |
| C-17 | **PASS** | Cascading gate chain from V-01 |
| C-18 | **PASS** | Bidirectional revision from V-03 |
| C-19 | **FAIL** | Not targeted; four-field UX template not declared in Format Contract |

**Estimated: 60 + 30 + 10/11 × 30 ≈ 117.3 — GOLD**

---

### V-05 — All Three + INERTIA Base (targets C-17 + C-18 + C-19)

Full combination with INERTIA framing throughout. INERTIA label strengthens C-12 (INERTIA vs. PROTECTED columns) and C-14 (baseline is explicitly the INERTIA state).

| Criterion | Estimate | Basis |
|-----------|----------|-------|
| C-01–C-05 | 5/5 PASS | Covered |
| C-06–C-08 | 3/3 PASS | Covered |
| C-09–C-16 | 8/8 PASS | Covered, INERTIA framing strengthens C-12 + C-14 |
| C-17 | **PASS** | Cascading gates |
| C-18 | **PASS** | Bidirectional revision |
| C-19 | **PASS** | Four-field template declared and Format-Contract-enforced |

**Estimated: 60 + 30 + 11/11 × 30 = 120 — GOLD**

---

## Round Summary

| Variation | Axis | Score | All Essential | Band |
|-----------|------|-------|---------------|------|
| V-01 | Cascading gate chain | **120** (verified) | ✓ | GOLD |
| V-05 | All three + INERTIA | **~120** (est.) | ✓ | GOLD |
| V-04 | Gate chain + revision | **~117** (est.) | ✓ | GOLD |
| V-03 | Bidirectional revision | **~116** (est.) | ✓ | GOLD |
| V-02 | Four-field UX template | **~115** (est.) | ✓ | GOLD |

---

## Excellence Signals from V-01

**1. Per-transition gate language with deliverable-level specificity**
Each gate names the *content* of prior-role deliverables, not the section header — e.g., "Rate Limit Registry written with at least one numeric threshold and a binding-order rationale sentence for every listed component." This prevents section collapse (writing a placeholder table without the required entries) because the gate condition fails on missing content, not missing section.

**2. Four-field template declared at point of production**
C-19's template appears inside Role 6 with inline failure rules ("fewer than all four fields per tier fails; free prose fails even if all topics mentioned"), reinforcing compliance at the moment of generation rather than relying solely on the Format Contract declared earlier in Role 2. Double-anchoring the template at preamble + production role closes the gap between declaring a standard and applying it.

**3. Reconciliation-sweep bidirectional Verdict revision**
Rather than requiring each evidence role to immediately update the Verdict (which interrupts analytical flow), V-01 adds a named final reconciliation step that mandates scanning all roles for claim revisions and inserting `[REVISED — see ROLE N]` markers. The Verdict is ultimately self-annotating for the reader, and the reconciliation step is explicitly gated after all 10 roles are complete, making it unforgettable without interrupting the sequential analysis.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["Per-transition gate language naming specific prior-role deliverables prevents section collapse by failing the gate on missing content, not missing section headers — extend gate language to every analysis boundary, not only preamble transitions", "Four-field UX template declared inline within the producing role with explicit failure conditions for partial templates and prose substitution, double-anchoring the standard at both Format Contract preamble and point of production", "Post-hoc reconciliation sweep achieves bidirectional Verdict revision marking without interrupting sequential role flow — a named final step that scans all evidence roles and inserts inline markers into the Verdict block is structurally equivalent to live updates and easier to enforce"]}
```
