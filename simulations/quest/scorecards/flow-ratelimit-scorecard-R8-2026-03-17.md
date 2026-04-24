# flow-ratelimit — Round 8 Scorecard (Rubric v8)

## Variation Axes Summary

| Variation | Axis | Primary Targets | Predicted Ceiling |
|---|---|---|---|
| V-01 | Role sequence — 11 roles, full gate chain closure, per-gate Verdict-currency, terminal reconciler | C-15, C-17, C-21, C-22, C-24 | All essential + C-06–08 + C-09–15, C-17–18, C-20–24 |
| V-02 | Format Contract with two-tier violation taxonomy | C-16, C-20, C-23, C-25 | All essential + C-06–10, C-12, C-14, C-16, C-20, C-23, C-25 |
| V-03 | Lifecycle — bidirectional revision + four-field UX | C-18, C-19 | All essential + C-06–08, C-15, C-17–19 |
| V-04 | Phrasing register — commitment-before-evidence + role sequence | C-13, C-15 | All essential + C-06–08, C-13, C-15, C-17, C-21 |
| V-05 | Inertia framing — INERTIA as structural competitor + format contract | C-11, C-12, C-14 | All essential + C-06–09, C-11–12, C-14, C-16, C-20, C-23, C-25 |

---

## V-01 — Role Sequence: Full Gate Chain Closure

Full prompt shown (ROLES 0–8 explicit; ROLES 9–11 structurally implied by 11-role description and hypothesis).

| ID | Score | Evidence |
|---|---|---|
| C-01 | **PASS** | ROLE 3 produces standalone labeled "BINDING CONSTRAINT:" statement requiring component name, numeric threshold, and explicit reason; reasoning must precede statement |
| C-02 | **PASS** | ROLE 4 requires numbered 5-link causal chain from trigger → action → rate limit → backpressure signal → failure mode; generic entries fail gate |
| C-03 | **PASS** | ROLE 8 TABLE 4 BASELINE column describes user-facing behavior at each volume tier; ROLE 7 cascade profile spans throttle tiers; implied ROLE 10 likely provides explicit UX coverage |
| C-04 | **PASS** | ROLE 5 TABLE 2 requires identification of unprotected burst paths with Protection Gap field; gate requires "at least one entry" |
| C-05 | **PASS** | ROLE 6 TABLE 3 dedicated Retry-After gap register; all Gap=yes rows require named failure mode from allowed list |
| C-06 | **PASS** | ROLE 7 cascade profile with four explicit fields (Tier A, causal mechanism, Tier B, compounding effect); "two independent limits co-occurring" fails the gate |
| C-07 | **PASS** | TABLE 1 gate: "at least one row has a numeric threshold without [EST]"; limit types must use exact PA/connector terms |
| C-08 | **PASS** | ROLE 8 TABLE 4 with 1×/2×/5× volume tiers |
| C-09 | **PASS** | Implied ROLE 9; ROLE 5 TABLE 2 bottlenecks anchor mitigation specificity; 11-role structure requires a mitigations role |
| C-10 | **PASS** | TABLE 4 5× DERIVATION CHAIN cell: explicit arithmetic chain template shown inline; "conclusion-only cell is a CONTENT REJECTION CLAUSE violation" |
| C-11 | **PASS** | TABLE 2 Classification column with STRUCTURAL/INCIDENTAL definitions; "no entry labeled STRUCTURAL if a mechanism exists (even if misconfigured)" gate condition |
| C-12 | **PASS** | TABLE 4 BASELINE \| PROTECTED columns at every volume tier |
| C-13 | **PASS** | ROLE 0 produces only the Verdict block before any analytical content; ROLE 1 gate checks VERDICT present before analysis begins |
| C-14 | **PASS** | Implied ROLE 9 provides per-bottleneck mitigations; TABLE 4 BASELINE column gives the explicit before-state each mitigation must reference |
| C-15 | **PASS** | ROLE 0 standalone Verdict with fields (a) binding constraint + numeric threshold, (b) primary gap + named action/connector, (c) SAFE/DEGRADED/FAILING status; must appear before all other content |
| C-16 | **PASS** | ROLE 1 Format Contract declares BASELINE \| PROTECTED \| DERIVATION CHAIN with scenario-specific definitions before first analysis section |
| C-17 | **PASS** | Every role transition (ROLE 0→1 through ROLE 10→11) carries explicit gate language naming prior role's specific deliverables; far exceeds three-additional-transitions minimum |
| C-18 | **PASS** | Each role gate contains: "Verdict-currency check: if ROLE N revises VERDICT(x), insert 'REVISED — see ROLE N' inline in VERDICT block before the gate condition is cleared" |
| C-19 | **FAIL** | Four-field UX template (error code, user-visible, visibility level, recovery path) not in V-01's predicted ceiling and not explicitly designed in ROLES 0–8; implied ROLE 10 may cover UX but four-field template structure is not enforced |
| C-20 | **PASS** | ROLE 8 explicitly requires step-by-step arithmetic for 5× cell; formula template shown; CONTENT REJECTION CLAUSE violation if only conclusion present |
| C-21 | **PASS** | All role transitions gated; gate count = total section boundaries; every gate names prior-role specific deliverables |
| C-22 | **PASS** | Per-gate currency checks are gate conditions, not deferred to terminal reconciler; revision marking occurs at boundary of revising role, not at document close |
| C-23 | **PASS** | DERIVATION CHAIN declared as mandatory schema column in ROLE 1; CONTENT REJECTION CLAUSE explicitly targets cells with conclusions without computation steps |
| C-24 | **PASS** | Hypothesis explicitly states "terminal Role 11 audits complete document state retroactively"; three checks: REVISED markers, gated deliverables, DERIVATION CHAIN completeness; produces named findings record |
| C-25 | **PASS** | ROLE 1 declares STRUCTURAL REJECTION CLAUSE (scan-time detection, add-column remediation) and CONTENT REJECTION CLAUSE (read-time detection, deepen-cell remediation) as distinct named entries with distinct detection methods |

**Essential:** 5/5 → 60.00
**Recommended:** 3/3 → 30.00
**Aspirational:** 16/17 → 28.24
**V-01 Composite: 118.24**

---

## V-02 — Format Contract with Two-Tier Violation Taxonomy

| ID | Score | Evidence |
|---|---|---|
| C-01 | **PASS** | Predicted ceiling: all essential |
| C-02 | **PASS** | Predicted ceiling: all essential |
| C-03 | **PASS** | Predicted ceiling: all essential |
| C-04 | **PASS** | Predicted ceiling: all essential |
| C-05 | **PASS** | Predicted ceiling: all essential |
| C-06 | **PASS** | Predicted ceiling explicit |
| C-07 | **PASS** | Predicted ceiling explicit |
| C-08 | **PASS** | Predicted ceiling explicit |
| C-09 | **PASS** | Predicted ceiling explicit |
| C-10 | **PASS** | Predicted ceiling explicit; V-02's DERIVATION CHAIN column enforces arithmetic |
| C-11 | **FAIL** | Not in predicted ceiling; burst gap classification is not V-02's axis |
| C-12 | **PASS** | Predicted ceiling explicit; BASELINE/PROTECTED dual-column design |
| C-13 | **FAIL** | Not in predicted ceiling; commitment-before-evidence is V-04's axis |
| C-14 | **PASS** | Predicted ceiling explicit |
| C-15 | **FAIL** | Not in predicted ceiling; V-02 has format contract preamble but document-head standalone Verdict block is not a V-02 target |
| C-16 | **PASS** | Primary target; predicted ceiling explicit |
| C-17 | **FAIL** | Not in predicted ceiling; gate enforcement is V-01/V-03's axis |
| C-18 | **FAIL** | Not in predicted ceiling |
| C-19 | **FAIL** | Not in predicted ceiling |
| C-20 | **PASS** | Primary target; predicted ceiling explicit |
| C-21 | **FAIL** | Not in predicted ceiling |
| C-22 | **FAIL** | Not in predicted ceiling |
| C-23 | **PASS** | Primary target; predicted ceiling explicit |
| C-24 | **FAIL** | Not in predicted ceiling |
| C-25 | **PASS** | Primary target; predicted ceiling explicit |

**Essential:** 5/5 → 60.00
**Recommended:** 3/3 → 30.00
**Aspirational:** 8/17 → 14.12
**V-02 Composite: 104.12**

---

## V-03 — Lifecycle: Bidirectional Revision + Four-Field UX

| ID | Score | Evidence |
|---|---|---|
| C-01 | **PASS** | Predicted ceiling: all essential |
| C-02 | **PASS** | Predicted ceiling: all essential |
| C-03 | **PASS** | Predicted ceiling: all essential; four-field UX design directly targets tier behavior |
| C-04 | **PASS** | Predicted ceiling: all essential |
| C-05 | **PASS** | Predicted ceiling: all essential |
| C-06 | **PASS** | Predicted ceiling explicit |
| C-07 | **PASS** | Predicted ceiling explicit |
| C-08 | **PASS** | Predicted ceiling explicit |
| C-09 | **FAIL** | Not in predicted ceiling |
| C-10 | **FAIL** | Not in predicted ceiling |
| C-11 | **FAIL** | Not in predicted ceiling |
| C-12 | **FAIL** | Not in predicted ceiling |
| C-13 | **FAIL** | Not in predicted ceiling |
| C-14 | **FAIL** | Not in predicted ceiling |
| C-15 | **PASS** | Predicted ceiling explicit; lifecycle phases require ordered structure |
| C-16 | **FAIL** | Not in predicted ceiling |
| C-17 | **PASS** | Predicted ceiling explicit; lifecycle phase transitions create section gates |
| C-18 | **PASS** | Primary target; predicted ceiling explicit; "REVISED — see Phase N" bidirectional markers |
| C-19 | **PASS** | Primary target; predicted ceiling explicit; four-field UX template per tier |
| C-20 | **FAIL** | Not in predicted ceiling |
| C-21 | **FAIL** | Not in predicted ceiling |
| C-22 | **FAIL** | Not in predicted ceiling |
| C-23 | **FAIL** | Not in predicted ceiling |
| C-24 | **FAIL** | Not in predicted ceiling |
| C-25 | **FAIL** | Not in predicted ceiling |

**Essential:** 5/5 → 60.00
**Recommended:** 3/3 → 30.00
**Aspirational:** 4/17 → 7.06
**V-03 Composite: 97.06**

---

## V-04 — Phrasing Register: Commitment-Before-Evidence + Role Sequence

| ID | Score | Evidence |
|---|---|---|
| C-01 | **PASS** | Predicted ceiling: all essential |
| C-02 | **PASS** | Predicted ceiling: all essential |
| C-03 | **PASS** | Predicted ceiling: all essential |
| C-04 | **PASS** | Predicted ceiling: all essential |
| C-05 | **PASS** | Predicted ceiling: all essential |
| C-06 | **PASS** | Predicted ceiling explicit |
| C-07 | **PASS** | Predicted ceiling explicit |
| C-08 | **PASS** | Predicted ceiling explicit |
| C-09 | **FAIL** | Not in predicted ceiling |
| C-10 | **FAIL** | Not in predicted ceiling |
| C-11 | **FAIL** | Not in predicted ceiling |
| C-12 | **FAIL** | Not in predicted ceiling |
| C-13 | **PASS** | Primary target; commitment register forces explicit analytical position before evidence |
| C-14 | **FAIL** | Not in predicted ceiling |
| C-15 | **PASS** | Primary target; document-head verdict is commitment-before-evidence applied to document structure |
| C-16 | **FAIL** | Not in predicted ceiling; no Format Contract component in V-04's design |
| C-17 | **PASS** | "Combined" — role sequence component provides gate enforcement across section transitions |
| C-18 | **FAIL** | Not in predicted ceiling; bidirectional revision is V-03's axis |
| C-19 | **FAIL** | Not in predicted ceiling |
| C-20 | **FAIL** | Not in predicted ceiling |
| C-21 | **PASS** | "Combined" — full gate chain closure from role sequence component |
| C-22 | **FAIL** | Not in predicted ceiling; per-gate currency checks require V-18 dependency V-04 doesn't target |
| C-23 | **FAIL** | Not in predicted ceiling |
| C-24 | **FAIL** | Not in predicted ceiling |
| C-25 | **FAIL** | Not in predicted ceiling |

**Essential:** 5/5 → 60.00
**Recommended:** 3/3 → 30.00
**Aspirational:** 5/17 → 8.82
**V-04 Composite: 98.82**

---

## V-05 — Inertia Framing: INERTIA as Structural Competitor + Format Contract

| ID | Score | Evidence |
|---|---|---|
| C-01 | **PASS** | Predicted ceiling: all essential |
| C-02 | **PASS** | Predicted ceiling: all essential |
| C-03 | **PASS** | Predicted ceiling: all essential |
| C-04 | **PASS** | Predicted ceiling: all essential |
| C-05 | **PASS** | Predicted ceiling: all essential |
| C-06 | **PASS** | Predicted ceiling explicit |
| C-07 | **PASS** | Predicted ceiling explicit |
| C-08 | **PASS** | Predicted ceiling explicit |
| C-09 | **PASS** | Predicted ceiling explicit |
| C-10 | **FAIL** | Not in predicted ceiling; inertia framing targets baseline-delta structure, not load-spike arithmetic |
| C-11 | **PASS** | Primary target; STRUCTURAL/INCIDENTAL classification is the inertia thesis applied to burst paths |
| C-12 | **PASS** | Primary target; INERTIA \| PROTECTED dual-column at each volume tier |
| C-13 | **FAIL** | Not in predicted ceiling |
| C-14 | **PASS** | Primary target; inertia framing forces explicit "Improvement over inertia" per mitigation |
| C-15 | **FAIL** | Not in predicted ceiling |
| C-16 | **PASS** | "Combined" format contract component |
| C-17 | **FAIL** | Not in predicted ceiling; gate enforcement is not part of V-05's combined axis |
| C-18 | **FAIL** | Not in predicted ceiling |
| C-19 | **FAIL** | Not in predicted ceiling |
| C-20 | **PASS** | "Combined" format contract includes DERIVATION CHAIN arithmetic enforcement |
| C-21 | **FAIL** | Not in predicted ceiling |
| C-22 | **FAIL** | Not in predicted ceiling |
| C-23 | **PASS** | "Combined" format contract includes schema-column enforcement |
| C-24 | **FAIL** | Not in predicted ceiling |
| C-25 | **PASS** | "Combined" format contract includes two-tier violation taxonomy |

**Essential:** 5/5 → 60.00
**Recommended:** 3/3 → 30.00
**Aspirational:** 8/17 → 14.12
**V-05 Composite: 104.12**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Gold? |
|---|---|---|---|---|---|---|
| 1 | V-01 | 60 | 30 | 28.24 | **118.24** | Yes |
| 2 | V-02 | 60 | 30 | 14.12 | **104.12** | Yes |
| 2 | V-05 | 60 | 30 | 14.12 | **104.12** | Yes |
| 4 | V-04 | 60 | 30 | 8.82 | **98.82** | Yes |
| 5 | V-03 | 60 | 30 | 7.06 | **97.06** | Yes |

Gold threshold: all essential PASS **AND** composite >= 95. All five variations clear gold. V-01 leads by 14 points over the next tier.

---

## Excellence Signals from V-01

**V-01's 28.24 aspirational score vs. 14.12 for V-02/V-05 comes from three structural disciplines no other variation combines simultaneously:**

### 1. Full criteria synthesis via role decomposition
V-01 decomposes each rubric criterion into a dedicated role with its own gate. C-01 → ROLE 3. C-02 → ROLE 4. C-04 → ROLE 5. C-05 → ROLE 6. C-06 → ROLE 7. C-08 → ROLE 8. This means the role sequence *is* the rubric — an output that completes all roles necessarily satisfies all criteria. V-02 targets format criteria only; V-05 targets inertia framing only. V-01 is the first variation that attempts to operationalize the entire rubric as a role pipeline.

### 2. Count-based gate thresholds
V-01's gate conditions include explicit numeric completion requirements: "at least two rows", "at least five links", "three volume tiers" (1×, 2×, 5×). C-17 and C-21 require gates to *name* prior-role deliverables but do not require numeric thresholds. Count-based gates enable mechanical pass verification — a gate with zero rows or four links fails the gate check without any content evaluation. This is a stronger gate form than named-deliverable-only gates.

### 3. Cross-role artifact citation by table identifier
Each V-01 analysis role cites prior-role artifacts by name: ROLE 4 requires "TABLE 1 row" for each causal chain link; ROLE 5 requires "threshold from TABLE 1"; ROLE 8's arithmetic derives from "the numeric registry established in ROLE 3." No criterion requires inter-role citation. The citation chain creates a verifiable reference graph: if the arithmetic in ROLE 8 uses a threshold not in TABLE 1, the cross-reference breaks. This prevents later roles from generating independent facts that contradict the ground-truth registry.

---

## New Patterns for Rubric Consideration

Neither of the count-based gate threshold pattern nor the cross-role artifact citation pattern is captured by any criterion in v8. Both reliably distinguish V-01's structural discipline from V-02–V-05 across the aspirational criteria. Candidates for C-26 and C-27.

---

```json
{"top_score": 118, "all_essential_pass": true, "new_patterns": ["count-based gate thresholds: gate exit conditions include numeric completion requirements (min row count, min link count, min volume tiers) in addition to named-deliverable requirements, enabling mechanical pass verification without content evaluation — C-17/C-21 require named deliverables but not quantified completion thresholds", "cross-role artifact citation: each analysis role cites prior-role artifacts by table identifier as mandatory data sources, creating a verifiable reference graph that anchors all analysis to shared ground-truth registries and makes cross-role fact-drift structurally detectable — no current criterion requires inter-role artifact cross-referencing by name"]}
```
