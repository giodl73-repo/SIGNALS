Scorecard written to `simulations/quest/scorecards/flow-lifecycle-scorecard-R12-2026-03-14.md`.

---

**Summary of R12 results:**

- **Top score**: V-05 at **100** (sole golden — only variation with both C-40 and C-41 PASS)
- **All essential pass**: YES
- **C-40 finding**: Bidirectional closure required. Single-direction Axis D (V-01, V-04) is PARTIAL — the gate fourth check (Axis E) is necessary for PASS. V-02 is the C-40 minimum.
- **C-41 finding**: Axis F alone is sufficient. V-03 passes C-41 independently, confirming orthogonality to C-40.
- **Three-way tie at 99.7**: V-02 (D+E, no F), V-03 (F only), V-04 (D+F, no E) — each cracks exactly one of the two new criteria.

**New patterns pointing to R13:**
1. The B-NN→Exception closure is missing — dark bottlenecks are the symmetric analog to the now-gated dark roles; a Bottleneck Analysis preamble gate check would close the bidirectional Exception↔B-NN loop.
2. The exit gate has a forward B-NN reference (C-37) but no forward Phase reference — adding `Next phase: PHASE N+1` to the exit gate would complete bidirectional Phase→Phase linkage to match C-41's backward entry contract declaration.
 PASS |

All five variations carry the full SECTION A EX-block architecture, Role Registry Gate with domain role sets, TERMINAL table with completeness check, and Gap MISSING: field with IM-ID rationale. Essential ceiling: **60/60** across all five.

---

### Recommended (C-06–C-08) — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Parallel Path Modeling | PASS | PASS | PASS | PASS | PASS |
| C-07 | Edge Case Enumeration | PASS | PASS | PASS | PASS | PASS |
| C-08 | Decision Point Explicitness | PASS | PASS | PASS | PASS | PASS |

FORK/JOIN with labeled join condition, EC-N constructed-answer blocks, DS-[S-ID] supplement blocks with Fallback sub-field. Recommended ceiling: **30/30** across all five.

---

### Aspirational (C-09–C-41) — Detailed Evaluation

**C-09 through C-39**: PASS all five. All R11 criteria fully inherited. See R11 scorecard for criterion-by-criterion evidence. The complete baseline architecture — INCUMBENT BASELINE, Role Registry Gate (three checks), Role Sequence Schedule, Phase-scoped EX blocks, SECTION A/B ordinal structure, CHAIN STATUS with eight directions including Exception→B and Phase-boundary B-NN continuity, Dual-Cite Fail Conditions A/B — is present unchanged in all five R12 variations.

**C-40 — Exception Block Role-Sequence Cross-Reference**

Requires bidirectional closure per design rationale: (a) every EX block carries `Role Ref: R-ID` naming the ROLE SEQUENCE SCHEDULE primary owner for the enclosing phase (Axis D — Exception→Role direction); AND (b) the Role Registry Gate gains a fourth anti-generic check validating that every declared R-ID appears in at least one EX block's `Role Ref:` sub-field (Axis E — Role→Exception direction), with CHAIN STATUS enumerating the `Role→Exception` direction explicitly. The chain closes in both directions; "dark" roles (registry-declared but no EX trace) become named structural violations.

| Variation | Axis D present | Axis E present | CHAIN STATUS Role→Exception | C-40 verdict |
|-----------|:-:|:-:|:-:|------|
| V-01 | YES | NO | NO | **PARTIAL** — Exception→Role direction in blocks; no gate closure; chain runs one way |
| V-02 | YES | YES | YES | **PASS** — Full bidirectional; dark roles detectable; CHAIN STATUS verifies |
| V-03 | NO | NO | NO | **FAIL** — No Role-Ref sub-field in EX blocks |
| V-04 | YES | NO | NO | **PARTIAL** — Exception→Role direction in blocks; Axis E absent; no gate closure |
| V-05 | YES | YES | YES | **PASS** — Full bidirectional; dark roles detectable; CHAIN STATUS verifies |

**C-41 — Phase Entry Contract Prior-Phase Sequential Linkage**

Requires: each PHASE ENTRY CONTRACT carries a named `Prior phase:` sub-field declaring the preceding phase by literal identifier (e.g., "PHASE 1 — Initiation"). PHASE 1 carries NONE/INIT sentinel. This sub-field is structurally distinct from `Prior phase blocked bottleneck:` (R11): one carries a Phase label, the other carries a B-ID — independently verifiable. CHAIN STATUS gains a `Phase-sequence` direction verifying that each entry contract's `Prior phase:` string-matches the preceding phase's block label in document order, making out-of-order rendering detectable by identifier mismatch.

| Variation | Axis F present | CHAIN STATUS Phase-sequence | Sentinel on PHASE 1 | C-41 verdict |
|-----------|:-:|:-:|:-:|------|
| V-01 | NO | NO | N/A | **FAIL** — No Prior-Phase sub-field |
| V-02 | NO | NO | N/A | **FAIL** — No Prior-Phase sub-field |
| V-03 | YES | YES | YES | **PASS** — Prior phase: field + sentinel + CHAIN STATUS direction |
| V-04 | YES | YES | YES | **PASS** — Prior phase: and Prior phase blocked bottleneck: coexist as independent sub-fields |
| V-05 | YES | YES | YES | **PASS** — Full architecture; three-way independence confirmed (Phase label / B-ID / entry condition) |

---

### Aspirational Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 – C-39 (31 criteria) | 31 PASS | 31 PASS | 31 PASS | 31 PASS | 31 PASS |
| C-40 | PARTIAL | PASS | FAIL | PARTIAL | PASS |
| C-41 | FAIL | FAIL | PASS | PASS | PASS |
| **Aspirational PASS total** | **31/33** | **32/33** | **32/33** | **32/33** | **33/33** |

---

## Composite Scores

Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/33 × 10)`

```
V-01: (5/5 × 60) + (3/3 × 30) + (31/33 × 10) = 60 + 30 + 9.39 = 99.4
V-02: (5/5 × 60) + (3/3 × 30) + (32/33 × 10) = 60 + 30 + 9.70 = 99.7
V-03: (5/5 × 60) + (3/3 × 30) + (32/33 × 10) = 60 + 30 + 9.70 = 99.7
V-04: (5/5 × 60) + (3/3 × 30) + (32/33 × 10) = 60 + 30 + 9.70 = 99.7
V-05: (5/5 × 60) + (3/3 × 30) + (33/33 × 10) = 60 + 30 + 10.00 = 100.0
```

---

## Scorecard

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-05 Axes D+E+F | 5/5 | 3/3 | 33/33 | **100.0** | YES |
| 2 | V-02 Axes D+E | 5/5 | 3/3 | 32/33 | **99.7** | No |
| 2 | V-03 Axis F | 5/5 | 3/3 | 32/33 | **99.7** | No |
| 2 | V-04 Axes D+F | 5/5 | 3/3 | 32/33 | **99.7** | No |
| 5 | V-01 Axis D | 5/5 | 3/3 | 31/33 | **99.4** | No |

**C-40 minimum**: V-02 (bidirectional closure required — single-direction Axis D in V-01 and V-04 is PARTIAL, not sufficient).
**C-41 minimum**: V-03 (Prior-Phase sub-field alone is sufficient — independent of Role-Ref architecture).
**Both simultaneously**: V-05 (minimum and maximum; V-04 achieves C-41 + PARTIAL C-40 at 99.7).

---

## C-40 and C-41 Structural Analysis

### C-40 — Bidirectionality determination

V-01 and V-04 both carry Axis D (EX block `Role Ref: R-ID` sub-field) but not Axis E (registry gate fourth check). CHAIN STATUS in both lacks the `Role→Exception` direction. This means:

- A reviewer can navigate: EX-2A → `Role Ref: R-02` → ROLE SEQUENCE SCHEDULE (R-02 owns Phase 2). Chain runs forward.
- A reviewer CANNOT verify: R-02 declared in registry → appears in at least one EX block. Dark roles are invisible.

V-02 and V-05 add the gate fourth check and the `Role→Exception` CHAIN STATUS direction, closing the loop. The design rationale states: "closing the chain bidirectionally (Role→Exception in the gate; Exception→Role in the block)" — the bidirectional closure is the defining structural property, not just the EX block sub-field alone. V-01/V-04 PARTIAL is confirmed.

### C-41 — Independence from C-40

V-03 achieves C-41 (PASS) without any Axis D or E. This confirms C-41 is orthogonal to C-40: the `Prior phase: PHASE N` sub-field in entry contracts operates entirely on the Phase→Phase axis and has no dependency on the exception→role axis. V-04's architecture (D+F, no E) achieves C-41 PASS while leaving C-40 PARTIAL — demonstrating clean composability.

### Architecture of V-05 (maximum density)

V-05 activates a **nine-direction CHAIN STATUS** verifying:
1. Forward (SLA→B): AT-RISK rows cite B-IDs
2. Backward (B→SLA): B-NN blocks name affected SLA nodes
3. Exit gate consistency: PHASE EXIT GATE B-ID → B-NN block
4. Phase-boundary B-NN continuity: exit gate → next entry contract `Prior phase blocked bottleneck:`
5. **Phase-sequence** (C-41 NEW): entry contract `Prior phase:` → preceding phase block label
6. Exception→B: EX block `Bottleneck Ref:` → B-NN block
7. Exception→Role: EX block `Role Ref:` → ROLE SEQUENCE SCHEDULE primary owner for enclosing phase
8. **Role→Exception** (C-40 E-axis NEW): every registry R-ID → at least one EX block Role Ref
9. Dual-cite status: every B-NN Cause → IM-ID string + R-ID string

Every declared artifact is reachable from every other via at most two string comparisons.

---

## Excellence Signals (from V-05 — maximum architectural density)

1. **Dark-role gate enforcement as structural violation class**: The registry gate fourth check creates a new category of detectable structural error — a role declared in the registry but never appearing in an EX block is a "dark role" whose absence is named and gated, not silently omitted. This is structurally analogous to a B-NN declared but never referenced in any exception trace — a "dark bottleneck" — which the current architecture does not yet gate against. The B-NN→Exception direction (each B-NN cited in at least one EX block's Bottleneck Ref) is absent from CHAIN STATUS and from the Bottleneck Analysis preamble, leaving a parallel dark-artifact gap.

2. **Phase→Phase backward declaration as independent traceability axis**: V-04 and V-05 demonstrate that `Prior phase: PHASE N` and `Prior phase blocked bottleneck: B-ID` coexist cleanly in the PHASE ENTRY CONTRACT as orthogonal sub-fields with different traceability targets. The CHAIN STATUS `Phase-sequence` direction and `Phase-boundary B-NN continuity` direction are independently verifiable — one string-matches phase block labels; the other string-matches B-NN block identifiers. This confirms sequential-linkage criteria can be accumulated in the entry contract without structural collision.

3. **Seven-artifact maximum traceability density confirmed**: V-05 confirms that the full seven-artifact system (INCUMBENT BASELINE / ROLE SEQUENCE SCHEDULE / EX blocks with both Bottleneck Ref and Role Ref / PHASE ENTRY CONTRACTs with both Prior phase and Prior phase blocked bottleneck / PHASE EXIT GATEs / B-NN blocks) is architecturally achievable without cross-field interference. Each artifact node is independently populated and independently verifiable. The remaining structural gap is the B-NN→Exception closure: a B-NN may be declared but never cited in any EX block Bottleneck Ref, making its operational trace invisible — the symmetric case of the now-closed Role→Exception direction.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Dark-role gate enforcement generalizes to dark-bottleneck detection: the Role→Exception gate check (C-40 Axis E) makes registry-declared roles with no EX trace detectable as structural violations; the symmetric B-NN→Exception direction — each B-NN must appear in at least one EX block Bottleneck Ref — is currently unchecked; a gate check in the Bottleneck Analysis preamble requiring every B-NN to have at least one EX block Bottleneck Ref citation would close the bidirectional Exception↔B-NN loop and make dark bottlenecks a named structural violation", "Phase→Phase backward declaration in entry contract is orthogonal to B-NN boundary continuity: V-04 confirms that Prior phase: PHASE N (phase-sequence linkage) and Prior phase blocked bottleneck: B-ID (B-NN continuity) coexist as independent sub-fields with separate CHAIN STATUS directions; the prior-phase entry contract slot can accumulate sequential-linkage sub-fields without structural collision, and the exit gate counterpart — Next phase: PHASE N+1 as a forward phase reference — would complete bidirectional Phase→Phase gate-to-gate linkage analogous to how C-37 provides the forward B-NN reference"]}
```
