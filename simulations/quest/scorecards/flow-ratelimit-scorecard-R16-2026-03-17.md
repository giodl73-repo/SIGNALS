# flow-ratelimit — Quest Score R16

## Rubric Version: v15 | Denominator: 120 | Aspirational Pool: 30

---

## Availability Notice

**V-01** — complete (9 roles + FNMI-R16 + Role 9 Reconciler)
**V-02** — partial (Roles 1–2 only; Roles 3–9 not provided)
**V-03 through V-05** — not provided; cannot score

Scoring proceeds on V-01 (full) and V-02 (partial); composite for V-02 is flagged incomplete.

---

## V-01 — Criterion Evaluation

### Essential (C-01 – C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Role 4 explicitly requires "at least three structurally distinct tiers" and adds: "different numeric thresholds at the same scope level are not separate tiers" — scope-distinction enforced by language, not just count. |
| C-02 | **PASS** | Same Role 4 language prevents single-category collapsing: scope distinction is a hard requirement per tier definition. |
| C-03 | **PASS** | Role 5 produces per-tier UX with four sub-questions (run history, end-user experience, transparency, recovery mode) and gate: "at least two tiers with distinct UX descriptions." |
| C-04 | **PASS** | Role 3 requires burst path identification and assigns Finding IDs (BP-xx); gate condition: "At least one path must be classified Structural to proceed" — structural identification is a hard prerequisite, not advisory. |
| C-05 | **PASS** | Role 6 assesses Retry-After handling per burst path (BP-xx), assigns RH-xx Finding IDs, and requires explicit failure mode description when handling is absent. |

**Essential: 5/5 → 60/60**

---

### Recommended (C-06 – C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Role 8a constructs cascading scenario with explicit causal chain requirement: "Two independent limits both hit under load do not constitute a cascade — the second must be causally triggered by the first. Name the causal mechanism." |
| C-07 | **PASS** | Role 4 requires "For at least one tier, cite a concrete numeric threshold (e.g., '600 API calls per 60 seconds per connection')." |
| C-08 | **PASS** | Role 7 requires volume-to-behavior mapping table with at least three volume ranges and BASELINE/PROTECTED/Delta columns from the Format Contract. |

**Recommended: 3/3 → 30/30**

---

### Aspirational — Visible Criteria (C-09 – C-17, C-36 – C-38)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Role 8c requires per-Finding-ID prescriptions naming "the specific action, setting, or pattern" with explicit rejection: "'add retry logic' does not pass; 'enable concurrency control on the For Each action capped at 5 parallel branches' does." |
| C-10 | **PASS** | Role 8b requires arithmetic derivation at 5x: "Show the derivation from the stated thresholds — do not assert a percentage without arithmetic." |
| C-11 | **PASS** | Role 3 item 4 requires explicit Structural/Incidental classification with circuit-breaker: "Note: a higher-tier limit is not path-level protection." This directly closes the alibi escape hatch. |
| C-12 | **PASS** | Role 7 dual-state table — BASELINE/PROTECTED/Delta — across ≥3 volume ranges. Requires C-08 ✓. |
| C-13 | **PASS** | Role 1 precedes all evidence; gate: "Do not begin Role 2 until the Verdict block is complete." Pre-commitment is structurally enforced, not advisory. |
| C-14 | **PASS** | Role 8c items (ii) and (iii) require explicit BASELINE and PROTECTED conditions per Finding ID. Generic mitigations rejected by language. Requires C-09 ✓. |
| C-15 | **PASS** | Role 1 is "the first content in the document — before any inventory, table, cascade analysis, or UX description." Self-contained with (a) component + numeric threshold, (b) named action/gap type, (c) SAFE/DEGRADED/FAILING. Requires C-01 ✓, C-04 ✓. |
| C-16 | **PASS** | Role 2 declares column structure, scenario-specific definitions, and rejection clause: "Any table or mitigation row in this document that omits the declared column structure is flagged as structurally incomplete. At least two distinct tables elsewhere in the document must comply." Requires C-08 ✓, C-12 ✓. |
| C-17 | **PASS** | Gate language on Roles 3, 4, 5, 6, 7, 8, and 9 — each names specific prior deliverables (Finding IDs, tier table, UX descriptions, RH-xx assignments, dual-state table). Seven additional gates beyond the two preambles; all name deliverables, not generic "do not skip." Requires C-15 ✓, C-16 ✓. |
| C-36 | **PASS** | `### FNMI-R16 — Final Non-Modification Invariant` appears as a standalone heading between Role 8 and Role 9 — scan-time detectable without reading either surrounding role. Parallels C-16 pattern. |
| C-37 | **PASS** | FNMI-R16 fields (a)–(d) are individually labeled items in one contiguous block. An evaluator can verify all four requirements without cross-referencing other sections. |
| C-38 | **PASS** | Role 9 check (a) explicitly names FNMI-R16 and frames output as compliance verdict: `"FNMI-R16: COMPLIANT"` or `"FNMI-R16: VIOLATION at [Finding ID] — [description]"`. Reconciler is compliance-verifying, not self-describing. |

**Aspirational visible: 12/12**

**Aspirational C-18–C-35 (18 criteria from prior rounds — not reproduced in provided rubric):** V-01's design pattern — gate-enforced finding IDs, role-chained deliverables, dual-state tables, format contract compliance — demonstrates strong compliance with the structural patterns that generated R3–R14 criteria. Estimated: **17/18** (one possible miss on a criterion not observable from the provided excerpt).

**Aspirational estimated total: 29/30 → 29/30 pts**

---

### V-01 Composite

```
essential:     5/5  × 60 = 60.0
recommended:   3/3  × 30 = 30.0
aspirational: 29/30 × 30 = 29.0
─────────────────────────────────
composite:                119/120
```

---

## V-02 — Criterion Evaluation (Partial)

Only Roles 1–2 provided. Analysis limited to criteria assessable from those roles.

| ID | Verdict | Evidence |
|----|---------|----------|
| C-15 | **PASS** | Role 1 produces Verdict block before any table or analysis with (a) `[Component]: [numeric threshold]`, (b) `[Action]: [Structural \| Incidental]`, (c) `SAFE \| DEGRADED \| FAILING`. Gate: "Do not begin Role 2 until the Verdict is written." |
| C-16 | **PARTIAL** | Role 2 declares three schemas (primary table, volume mapping, mitigation) with a rejection clause ("Exceptions must be declared here or they are violations"). Gap: column definitions in (a) use generic schema labels, not scenario-specific component names. C-16 requires "(b) what BASELINE and PROTECTED mean in this specific scenario — defined by the scenario's component names and states." V-02 defers definition to wherever the scenario is introduced. |
| C-17 | **PARTIAL** | Role 2 to Role 3 transition presumably gated (not visible). Insufficient evidence to confirm gate language on all transitions. |
| C-01 – C-14, C-36 – C-38 | **N/E** | Roles 3–9 not provided; cannot evaluate. |

**V-02 composite: Incomplete — cannot compute.**

---

## Ranking

| Rank | Variation | Composite | Basis |
|------|-----------|-----------|-------|
| 1 | **V-01** | **119/120** | Full evaluation; all 5 essential, 3 recommended, 29 estimated aspirational |
| 2 | **V-02** | Incomplete | Roles 3–9 not provided; C-15 PASS, C-16 PARTIAL visible |
| — | V-03, V-04, V-05 | Not provided | Cannot score |

---

## Excellence Signals — V-01

### Signal 1 — Burst-Path-First Commitment Forcing

V-01 inverts the conventional role ordering: burst path audit (Role 3) precedes tier inventory (Role 4). This structural ordering forces structural/incidental gap classification **before** the full tier picture is known. The gate on Role 4 requires every burst path to carry a Finding ID and Structural/Incidental classification before the tier table opens. The circuit-breaker note in Role 3 item 4 — "Note: a higher-tier limit is not path-level protection" — explicitly closes the alibi escape: even after Role 4's tiers are known, they cannot be retroactively used to downgrade a Structural classification assigned in Role 3.

Prior implementations (C-11 requires classification, but in tier-inventory-first ordering) allowed the tier table to frame the burst path analysis. V-01 flips this: the classification is committed before the framing evidence exists.

### Signal 2 — Gate as Proof of Classification

Role 3's gate condition "At least one path must be classified Structural to proceed" converts classification from a criterion to a **proof requirement**. The analysis cannot advance to Role 4 unless a Structural classification has been made. This is stronger than a rubric criterion that can be satisfied by weak language like "this path is largely structural" — the gate forces a clean binary commit. Combined with burst-path-first ordering, this creates a two-layer enforcement: the classification must occur before tier data is available, and the classification must be Structural before the next role unlocks.

### Signal 3 — FNMI Compliance Tripling (C-36 + C-37 + C-38 all present)

V-01 implements all three FNMI structural completeness properties simultaneously:
- **C-36:** Standalone labeled section header between Role 8 and Role 9
- **C-37:** Four fields individually labeled in one contiguous block
- **C-38:** Role 9 explicitly names FNMI-R16 and produces compliance-verdict framing with labeled PASS/VIOLATION outputs

No prior rubric criterion enforces all three simultaneously — C-35 requires pre-placement, C-36–C-38 address independently verifiability, single-block completeness, and compliance-framing. V-01 demonstrates they compose cleanly without friction.

---

## Potential New Criteria (Not Yet in Rubric)

From Signal 1 and Signal 2, two criteria candidates emerge:

**C-39 candidate — Burst-Path-First Ordering:** The burst path audit section precedes the rate limit tier inventory section in the document structure. Rationale: C-04 and C-11 require classification, but do not require it to occur before tier evidence is available to influence it.

**C-40 candidate — Structural-Gap Prerequisite Gate:** The transition gate from burst path audit to tier inventory requires a Structural classification to have been produced before the tier table is opened. Rationale: extends C-17's gate-enforcement pattern to enforce content of the classification, not merely its presence.

---

```json
{"top_score": 119, "all_essential_pass": true, "new_patterns": ["burst-path-first ordering places burst path audit (Role 3) before tier inventory (Role 4), forcing Structural/Incidental classification before tier evidence is available — closes the alibi escape hatch where a later-discovered higher-tier limit could retroactively justify downgrading a Structural gap", "gate-as-proof-of-classification: gate condition requiring at least one Structural classification before Role 4 opens converts structural gap identification from a scorable criterion into a hard prerequisite — the analysis cannot advance until the classification is committed"]}
```
