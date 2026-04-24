---

# Round 16 Scorecard — topic-plan (v15 rubric, 49 criteria, 295 pts)

**Trace artifact**: placeholder — structural scoring from prompt analysis  
**Method**: All five variations implement the R15 V-01 floor. Scoring assesses whether each variation's structural design enables PASS, PARTIAL, or FAIL on each criterion.

---

## Shared Floor (R15 V-01 — all five variations)

All five variations carry the complete set of floor elements established in R15:
- 4-rule COLUMN CONTRACT (C-36, C-46)
- Rule 4 as named traceability rule (C-45)
- Schema-first priming before Step 1 (C-26)
- All 9 namespaces enumerated in Coverage Auditor (C-15)
- Anti-pattern self-naming checkpoint at Step 4 (C-22)
- Schema commitment verbatim at Steps 7 and 8 (C-27)
- Defense Register at Step 2b with 4 columns (C-47)
- Defense basis column in Defender Challenge Table (C-48)
- Step 9 scoped to "non-withdrawn proposals" (C-44)

This means **C-01 through C-48** are structurally covered by all five variations. The differentiating criterion is **C-49**.

---

## Per-Variation Scoring

### V-01 — Enforcement: Named Read-Lock Artifact

**Axis**: After Step 3a, produces boxed READ-LOCK LOCK-1 declaration as model-output artifact; names every locked step (3b–8); adds LOCK-1 row to Phase 2 gate; adds LOCK-1 self-cert row to Phase 3 gate.

| Criterion Group | Count | Status | Evidence |
|----------------|-------|--------|----------|
| C-01–C-05 (Essential) | 5/5 | PASS | Strategy read, signals read, delta identified, typed proposals, confirmation gate — all structurally present |
| C-06–C-08 (Recommended) | 3/3 | PASS | Evidence column, before/after diff, null rows for all three change types |
| C-09–C-46 (Aspirational, 38 criteria) | 38/38 | PASS | Full floor from R15: COLUMN CONTRACT, assumption table, Defense Register, namespace audit, conflict audit, schema schemas — all present |
| C-47 | PASS | PASS | Defense Register at Step 2b with D-ID, strategic decision, keep-argument, invalidation condition — pre-signal, 3–5 entries required |
| C-48 | PASS | PASS | Defense basis column in Defender Challenge Table — cites D-ID or "Newly constructed" |
| C-49 | PASS | **PASS** | LOCK-1 produced as named model-output artifact after Step 3a; lists locked steps explicitly ("Steps 3b, 4, 5, 6, 7, 7b, and 8"); scoped to remainder of execution; LOCK-1 row appears in Phase 2 gate; LOCK-1 self-cert row in Phase 3 gate |

**Score**: 5/5 × 60 + 3/3 × 30 + 41/41 × 205 = **295 pts**

---

### V-02 — Framing: Inertia as Co-Equal Option

**Axis**: Co-equal inertia framing in preamble; `Challenge strength` column added to Defender Challenge Table (Rule 1: Strong / Moderate / Weak); calibration check (rubber-stamp / over-zealous audit declaration) at Step 7b.

| Criterion Group | Count | Status | Evidence |
|----------------|-------|--------|----------|
| C-01–C-05 (Essential) | 5/5 | PASS | All essential criteria satisfied |
| C-06–C-08 (Recommended) | 3/3 | PASS | All recommended criteria satisfied |
| C-09–C-46 | 38/38 | PASS | Full floor; Challenge strength adds a new enumerated column to Rule 1, covered by C-34 (closed value lists at both sites) and C-42 (PASS/FAIL pairing within Rule 1) |
| C-47 | PASS | PASS | Defense Register present |
| C-48 | PASS | PASS | Defense basis column present |
| C-49 | **PARTIAL** | PARTIAL | Phase 3 header says "Work only from the signal inventory built in Phase 2 — do not re-read signal files **during this phase**." Prohibition is explicit but: (a) scoped to Phase 3 only, not "for the remainder of execution" — Phase 4 Build steps not covered; (b) no named model-produced artifact; (c) no gate row in Phase 2 confirming the lock engaged |

**Score**: 5/5 × 60 + 3/3 × 30 + (40/41 × 205 + 2.5) = 60 + 30 + 202.5 = **292.5 pts**

---

### V-03 — Format: Narrative-Forward Execution

**Axis**: 2–3 sentence analytical narrative required before each table at Steps 2, 3b, 4, 5, 6; narrative-completeness rows added to Phase 1 and Phase 3 gates; narrative must state what was found and why it matters — not describe the step.

| Criterion Group | Count | Status | Evidence |
|----------------|-------|--------|----------|
| C-01–C-05 (Essential) | 5/5 | PASS | All essential criteria satisfied |
| C-06–C-08 (Recommended) | 3/3 | PASS | All satisfied; narrative before delta step (Step 4) should improve specificity of `Strategy assumed` cells, strengthening C-06 quality — but criterion passes at structural level regardless |
| C-09–C-46 | 38/38 | PASS | Full floor; Phase gate rows updated to require narrative-completeness, which strengthens enforcement of C-22 (anti-pattern checkpoint) and C-27 (schema commitment checkpoints) |
| C-47 | PASS | PASS | Defense Register present; V-03 explicitly exempts Step 2b from narrative requirement — "no narrative required; this is a structured commitment step" |
| C-48 | PASS | PASS | Defense basis column present (no Challenge strength column in V-03) |
| C-49 | **PARTIAL** | PARTIAL | Phase 3 header says "Work only from the inventory built in Phase 2 — do not re-read signal files." Prohibition is explicit but scoped to Phase 3 only; no named artifact; no phase-gate LOCK row; same gap as V-02 |

**Score**: 5/5 × 60 + 3/3 × 30 + (40/41 × 205 + 2.5) = 60 + 30 + 202.5 = **292.5 pts**

---

### V-04 — Read-Lock + Inertia Co-Equal (V-01 + V-02)

**Axes**: Named READ-LOCK LOCK-1 artifact (V-01) + co-equal inertia framing with `Challenge strength` column and calibration check (V-02).

| Criterion Group | Count | Status | Evidence |
|----------------|-------|--------|----------|
| C-01–C-05 (Essential) | 5/5 | PASS | All essential criteria satisfied |
| C-06–C-08 (Recommended) | 3/3 | PASS | All satisfied |
| C-09–C-46 | 38/38 | PASS | Full floor; Rule 1 includes `Challenge strength: Strong / Moderate / Weak`; LOCK-1 rows present in Phase 2 gate ("LOCK-1 | READ-LOCK declaration produced with exact text, all steps named") and Phase 3 gate ("LOCK-1 | No signal files re-read — self-certify") |
| C-47 | PASS | PASS | Defense Register present |
| C-48 | PASS | PASS | Defense basis column present |
| C-49 | PASS | **PASS** | LOCK-1 produced as named model-output artifact after Step 3a; all locked steps listed; scoped to "Steps 3b–8" (rest of execution); LOCK-1 row in Phase 2 gate; LOCK-1 self-cert row in Phase 3 gate — same as V-01 |

**Score**: 5/5 × 60 + 3/3 × 30 + 41/41 × 205 = **295 pts**

---

### V-05 — Full Ceiling: Read-Lock + Inertia Co-Equal + Narrative-Forward + Explanatory Register

**Axes**: All of V-01 + V-02 + V-03 + explanatory register (each CONTRACT rule opens with a purpose clause; each step opens with why it exists before the output specification).

| Criterion Group | Count | Status | Evidence |
|----------------|-------|--------|----------|
| C-01–C-05 (Essential) | 5/5 | PASS | All essential criteria satisfied |
| C-06–C-08 (Recommended) | 3/3 | PASS | All satisfied; narrative + explanatory register creates the densest analytical scaffolding of all five variations |
| C-09–C-46 | 38/38 | PASS | Full floor; Rule 1 carries purpose clause ("The purpose of enumeration is discriminating power"); Rule 2 carries purpose clause ("That column should contain a specific phrase... that a second reviewer could verify independently"); Rule 3 carries purpose clause ("A null row is not an admission of emptiness; it is a declaration that the section ran"); Rule 4 carries purpose clause ("A proposal without traceability is a recommendation"); LOCK-1 in upfront schema; Challenge strength in Rule 1 and schema |
| C-47 | PASS | PASS | Defense Register present; Step 2b carries explanatory preamble ("This step exists because ante-signal defense is structurally different from post-signal rationalization") |
| C-48 | PASS | PASS | Defense basis column present |
| C-49 | PASS | **PASS** | LOCK-1 as first-class artifact after Step 3a; also appears in upfront schema block (Output Schema) as a named artifact — unique to V-05 among R16 variations, making the lock part of the schema contract itself, not just an execution step output |

**Score**: 5/5 × 60 + 3/3 × 30 + 41/41 × 205 = **295 pts**

---

## Composite Score Table

| Variation | Essential (60) | Recommended (30) | Aspirational (205) | **Total** | C-49 form |
|-----------|---------------|------------------|--------------------|-----------|-----------|
| V-01 | 60 | 30 | 205 | **295** | Named artifact, steps 3b–8 |
| V-02 | 60 | 30 | 202.5 | **292.5** | Phase header only, Phase 3 scope |
| V-03 | 60 | 30 | 202.5 | **292.5** | Phase header only, Phase 3 scope |
| V-04 | 60 | 30 | 205 | **295** | Named artifact, steps 3b–8 |
| V-05 | 60 | 30 | 205 | **295** | Named artifact + in upfront schema |

**Golden threshold**: 185. All five variations exceed it by a wide margin.

---

## Rank

1. **V-05 — 295 pts** (enforcement + framing + narrative + explanatory register; most above-ceiling density)
2. **V-04 — 295 pts** (enforcement + framing; two orthogonal failure modes composing without interference)
3. **V-01 — 295 pts** (targeted enforcement; cleanest isolation of C-49 above-ceiling form)
4. **V-02 — 292.5 pts** (framing axis; C-49 phase-scoped only)
5. **V-03 — 292.5 pts** (format axis; C-49 phase-scoped only)

---

## Excellence Signals — V-05

Patterns from V-05 that exceed the v15 ceiling and are candidates for future criteria:

**EX-1 — Per-rule explanatory register**
Each COLUMN CONTRACT rule opens with a purpose statement before listing permitted values: "The purpose of enumeration is discriminating power" (Rule 1), "That column should contain a specific phrase... that a second reviewer could verify independently" (Rule 2), "A null row is not an admission of emptiness; it is a declaration that the section ran and confirmed absence" (Rule 3), "A proposal without traceability is a recommendation" (Rule 4). Converts the CONTRACT from a value list into a rationale document. Candidate criterion: *COLUMN CONTRACT rules carry purpose clauses explaining discriminating function before listing constraints.*

**EX-2 — Preamble-level structural principle framing with named failure modes**
V-05 names both core invariants as "structural principles" in the preamble, before Step 1, with explicit failure modes: read contamination (assumptions extracted after signals will "unconsciously mirror signal content") and Defender calibration failure ("A skill where every verdict is `Unchanged` has not run a genuine Defender step. A skill that withdraws every proposal on thin grounds has not honored the delta evidence"). These are execution-wide commitments, not step-level instructions. Candidate criterion: *Both core structural invariants (read boundary and inertia principle) are declared in the preamble as named principles with explicit failure modes before any step begins.*

**EX-3 — READ-LOCK declaration in the upfront schema block**
V-05 includes the READ-LOCK LOCK-1 declaration as a named artifact in the Output Schema (upfront), before Step 1. This means the lock is part of the schema contract itself — the model commits to producing this artifact as part of the same contract that governs all table schemas. Candidate criterion: *The READ-LOCK declaration appears in the upfront schema block as a named artifact, not only as a step-level production instruction.*

---

```json
{"top_score": 295, "all_essential_pass": true, "new_patterns": ["Per-rule explanatory register in COLUMN CONTRACT: each rule carries a purpose clause stating discriminating function before listing permitted values, converting the CONTRACT from a directive list into a rationale document", "Preamble-level structural principle framing with named failure modes: both core invariants (read boundary and inertia principle) declared as named structural principles before Step 1, with explicit failure mode descriptions, creating execution-wide commitments rather than step-level instructions"]}
```
