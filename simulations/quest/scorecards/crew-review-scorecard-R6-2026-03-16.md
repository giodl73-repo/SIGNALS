# crew-review Variate R6 — Scorecard

**Rubric**: crew-review-rubric-v5-2026-03-16.md (max 145, golden ≥ 80 with all essential passing)

---

## Per-Criterion Scoring

### V-01 — Declarative Contract Form

| ID | Weight | Status | Evidence |
|----|--------|--------|----------|
| C-01 | essential | PASS | Property R1: all roles from `.roles/`, unconditional ERROR halts for absent/empty/malformed |
| C-02 | essential | PASS | Property R4: 4-column matrix (Role, Findings, Severity, Recommendation) with row order defined |
| C-03 | essential | PASS | Property R4 Severity: "exactly HIGH, MEDIUM, or LOW; no other values; not blank" |
| C-04 | essential | PARTIAL | No explicit "apply only that role's `lens.verify` perspective" instruction — contract enforces surface-specificity but not per-role lens distinctiveness |
| C-05 | essential | PASS | Property R4 Recommendation: "names (1) what to do and (2) where in the artifact; not generic" |
| C-06 | recommended | PASS | Property R5: standard = 2-3 domain roles; deep = all non-challenger roles |
| C-07 | recommended | PASS | Property R6: synthesis block required with at least one convergence or conflict |
| C-08 | recommended | PASS | Property R7: 4+ specific AMEND options including re-open G1 |
| C-09 | recommended | PASS | Property R2: "output begins with challenger bracket. COMPLETE before any domain reviewer row appears" |
| C-10 | recommended | PASS | Property R4 Findings: "names a specific artifact surface; not abstract observations" |
| C-14 | recommended | PASS | Property R1: ERROR halts unconditional — "no partial output is produced" |
| C-11 | aspirational | PASS | Property R3: 4-slot form (SLOT-A through SLOT-D), all named blanks |
| C-12 | aspirational | FAIL | No Lens column; no lens-lock declaration before findings in the contract |
| C-13 | aspirational | PARTIAL | Property R4 defines column constraints but no explicit "before writing any row, verify" gate — enforcement is implicit in contract satisfaction |
| C-15 | aspirational | PASS | Property R2 is a named structural element with Gate G1; challenger bracket distinct from domain reviewer rows — not an exception clause |
| C-16 | aspirational | PASS | Property R3: per-slot escalation rule with dedicated matrix row, per slot |
| C-17 | aspirational | PASS | G1 enforcement: "no domain reviewer row may appear in the output while G1 is OPEN" — explicit blocking condition |
| C-18 | aspirational | PASS | Property R3 step 3: "This dedicated row is the ONLY valid escalation form. The following forms do NOT satisfy Property R3: A sentence embedded within the challenger row's Findings cell / A note or comment appended below the challenger row / A parenthetical or footnote" |
| C-19 | aspirational | PASS | Property R4 Findings: "not abstract observations" is an anti-pattern exclusion inside the column definition |
| C-20 | aspirational | PASS | G1 states: OPEN or CLOSED (named); closure predicate: 4 conditions (a)–(d) all must hold |
| C-21 | aspirational | PASS | Property R3 steps 3–4 name prohibited forms inside the escalation rule |

**Score**: E=54 (C-04 PARTIAL=6), R=60, A: 0+1.25+2.5+2.5+2.5+2.5+2.5+2.5+2.5+2.5 = 23.75
**Composite: 137.75** — Golden ✓

---

### V-02 — Five-Phase Lifecycle (LOAD / CHALLENGE / REVIEW / VALIDATE / AMEND)

| ID | Weight | Status | Evidence |
|----|--------|--------|----------|
| C-01 | essential | PASS | PHASE 1 LOAD: reads `.roles/`, unconditional ERROR halts |
| C-02 | essential | PASS | PHASE 4 VALIDATE writes 4-column validated matrix |
| C-03 | essential | PASS | PHASE 3 + PHASE 4: "exactly HIGH, MEDIUM, or LOW — no freestyle label, not blank" |
| C-04 | essential | PASS | PHASE 3 step 1: "Apply only that role's `lens.verify` perspective" |
| C-05 | essential | PASS | PHASE 3 step 4 + PHASE 4 validation: "names what to do + where in the artifact — not generic" |
| C-06 | recommended | PASS | PHASE 3: standard = 2-3 non-challenger roles; deep = all non-challenger |
| C-07 | recommended | PASS | PHASE 4: cross-role synthesis required, 2-3 sentences |
| C-08 | recommended | PASS | PHASE 5 AMEND: 4+ options, at least one derived from HIGH finding or unfilled slot in this run |
| C-09 | recommended | PASS | PHASE 2 CHALLENGE: challenger first, G1 gate, null hypothesis 4-slot form |
| C-10 | recommended | PASS | PHASE 3 "name a specific artifact surface" + PHASE 4 validates Findings cell |
| C-14 | recommended | PASS | PHASE 1 ERROR halts: unconditional, no soft fallback |
| C-11 | aspirational | PASS | PHASE 2: 4-slot null hypothesis form (SLOT-A through SLOT-D) |
| C-12 | aspirational | FAIL | Output matrix is 4-column (no Lens column); no explicit lens-lock declaration in output |
| C-13 | aspirational | PASS | PHASE 4 VALIDATE is a visible validation phase with per-cell checks before matrix is written |
| C-15 | aspirational | PASS | "PHASE 2 -- CHALLENGE" is a named discrete phase; "Gate G1 state: OPEN -- domain review is blocked until G1 closes" |
| C-16 | aspirational | PASS | Slot-to-row escalation rule: "Produce a separate, dedicated matrix row"; per-slot |
| C-17 | aspirational | PASS | "Domain review does not begin until G1 transitions to CLOSED" |
| C-18 | aspirational | PASS | Escalation rule steps 3–4: "Do not embed the gap as a sentence within the challenger row's Findings cell. Do not append the gap as a note below the challenger row." |
| C-19 | aspirational | PARTIAL | PHASE 4 validation rules include "not an abstract observation" and "not generic" for Findings/Recommendation cells — anti-pattern language present but inside validation rules, not a formal schema declaration table |
| C-20 | aspirational | PASS | G1 states OPEN/CLOSED named; 5-condition closure predicate (all five must hold) |
| C-21 | aspirational | PASS | Escalation rule steps 3–4 name prohibited forms ("Do not embed… Do not append…") inside the escalation rule definition |

**Score**: E=60, R=60, A: 2.5+0+2.5+2.5+2.5+2.5+2.5+1.25+2.5+2.5 = 21.25
**Composite: 141.25** — Golden ✓

---

### V-03 — Numbered Execution Manifest

| ID | Weight | Status | Evidence |
|----|--------|--------|----------|
| C-01 | essential | PASS | Step 1 LOAD: ERROR halts, role pool from `.roles/` only |
| C-02 | essential | PASS | Step 5 OUTPUT: 5-column table (Slot, Role, Findings, Severity, Recommendation) — superset passes |
| C-03 | essential | PASS | Step 4: "Severity: exactly HIGH, MEDIUM, or LOW -- no other values" |
| C-04 | essential | PASS | Step 4: "Apply only that role's `lens.verify` perspective" |
| C-05 | essential | PASS | Step 4: "Recommendation: one action naming what to do and where" |
| C-06 | recommended | PASS | Step 2 manifest: slots 2-N (standard) = 2-3 non-challenger roles; deep = all non-challenger |
| C-07 | recommended | PASS | Step 5: cross-role synthesis required, references slot numbers |
| C-08 | recommended | PASS | Step 5 AMEND: 4 specific options including re-open G1 |
| C-09 | recommended | PASS | Step 3 Challenger bracket (Slot 1): null hypothesis form, G1 gate |
| C-10 | recommended | PASS | Step 4: "Name a specific artifact surface in each finding" |
| C-14 | recommended | PASS | Step 1 ERROR halts: unconditional, no soft fallback |
| C-11 | aspirational | PASS | Step 3: 4-slot null hypothesis form |
| C-12 | aspirational | FAIL | No Lens column in 5-column schema; no lens-lock declaration before findings |
| C-13 | aspirational | PARTIAL | Step 5 column constraints exist (Slot/Role/Severity typed) but no "before writing any row, verify" per-row validation gate |
| C-15 | aspirational | PASS | "Step 3 -- Challenger bracket (Slot 1)" as a named discrete step; "Domain review is blocked until G1 closes" |
| C-16 | aspirational | PASS | Slot-to-row escalation rule: dedicated matrix row per unfilled slot |
| C-17 | aspirational | PASS | "Domain review does not begin until G1 transitions to CLOSED" |
| C-18 | aspirational | PASS | Escalation rule steps 3–4: "Do not embed as a sentence within the challenger row's Findings cell. Do not append as a note below the challenger row." |
| C-19 | aspirational | FAIL | Step 5 column constraints name positive constraints only — no anti-pattern exclusion in any column definition |
| C-20 | aspirational | PASS | G1 OPEN/CLOSED states named; 4-condition closure predicate |
| C-21 | aspirational | PASS | Escalation rule names prohibited forms inside the rule definition |

**Score**: E=60, R=60, A: 2.5+0+1.25+2.5+2.5+2.5+2.5+0+2.5+2.5 = 18.75
**Composite: 138.75** — Golden ✓

---

### V-04 — Peer-Voice Challenger + State Machine Gate

| ID | Weight | Status | Evidence |
|----|--------|--------|----------|
| C-01 | essential | PASS | Step 1 LOAD: ERROR halts, role pool from `.roles/` |
| C-02 | essential | PASS | Step 4: 4-column table (Role, Findings, Severity, Recommendation) |
| C-03 | essential | PASS | Step 3: "Severity: HIGH / MEDIUM / LOW -- nothing else" |
| C-04 | essential | PASS | Step 3: "Apply only that role's `lens.verify` perspective -- not a generic observer's view" |
| C-05 | essential | PASS | Step 3: "Recommendation: one concrete action naming what to do and where in the artifact" |
| C-06 | recommended | PASS | Step 3: standard = 2-3 non-challenger roles; deep = every non-challenger |
| C-07 | recommended | PASS | Step 4: cross-role synthesis required |
| C-08 | recommended | PASS | Step 4 AMEND: 4 specific options |
| C-09 | recommended | PASS | Step 2 "The challenger gets the floor" — challenger first, null hypothesis form, gate |
| C-10 | recommended | PASS | Step 3: "Name a specific part of the artifact in each finding: a section, field, diagram element, or named assumption" |
| C-14 | recommended | PASS | Step 1 ERROR halts: unconditional, no soft fallback |
| C-11 | aspirational | PASS | Step 2: 4-slot null hypothesis form (SLOT-A through SLOT-D) |
| C-12 | aspirational | FAIL | No Lens column; no explicit lens-lock output declaration |
| C-13 | aspirational | FAIL | Step 4 matrix schema is 4-column with no type annotations; no per-row validation gate |
| C-15 | aspirational | PASS | "Step 2 -- The challenger gets the floor" as a named phase with G1 gate; "The rest of the review is behind Gate G1" |
| C-16 | aspirational | PASS | Step 2 escalation rule: "Log a separate, dedicated matrix row for the gap" — per slot |
| C-17 | aspirational | PASS | "The rest of this review does not run until G1 is CLOSED" |
| C-18 | aspirational | PASS | Escalation step 3: "This row is a full matrix entry -- it is NOT a sentence embedded within the challenger row's Findings cell. It is NOT a note appended below the challenger row. It is NOT a parenthetical comment. A gap finding that is not its own matrix row does not satisfy G1 closure condition 3 and does not close the gate." |
| C-19 | aspirational | FAIL | Step 4 output schema (4-column table) has no anti-pattern exclusions in column definitions |
| C-20 | aspirational | PASS | "G1 has two states: OPEN and CLOSED"; 5-condition closure predicate (all must be simultaneously true) |
| C-21 | aspirational | PASS | Escalation step 3 names prohibited forms inside the rule: NOT embedded sentence, NOT note, NOT parenthetical |

**Score**: E=60, R=60, A: 2.5+0+0+2.5+2.5+2.5+2.5+0+2.5+2.5 = 17.5
**Composite: 137.5** — Golden ✓

---

### V-05 — Verification-First Maximal (Full Stack)

| ID | Weight | Status | Evidence |
|----|--------|--------|----------|
| C-01 | essential | PASS | PHASE 1 L3: unconditional ERROR halts for absent/empty/malformed registry |
| C-02 | essential | PASS | PHASE 5 R2: 5-column matrix (superset of 4 required columns) |
| C-03 | essential | PASS | Output schema: "Severity: enum -- exactly HIGH, MEDIUM, or LOW; NOT: freestyle labels (Critical, Minor, Warning, Blocker, Moderate, Severe); NOT: blank cells; NOT: combinations" |
| C-04 | essential | PASS | PHASE 3 D3 step 1: "Lens cell: 'As a [role], I care about [specific concern from this role's `lens.verify`].' No generic restatement. Concern must be traceable to this role's documented lens." |
| C-05 | essential | PASS | PHASE 3 D3 step 4: "what to do + where -- no generic directive"; schema: "NOT: generic directives; NOT: recommendations without a named artifact location" |
| C-06 | recommended | PASS | PHASE 3 D1: standard = 2-4 roles; deep = all non-challenger |
| C-07 | recommended | PASS | PHASE 5 R3: cross-role synthesis required |
| C-08 | recommended | PASS | PHASE 5 R4: 5 specific AMEND options |
| C-09 | recommended | PASS | PHASE 2 CHALLENGER BRACKET: G1 gate, null hypothesis form, challenger first |
| C-10 | recommended | PASS | Schema Findings column: "NOT: abstract observations without a named surface" enforced per-row |
| C-14 | recommended | PASS | PHASE 1 L3 ERROR halts: unconditional, no soft fallback |
| C-11 | aspirational | PASS | PHASE 2 C2: 4-slot template (SLOT-A through SLOT-D) |
| C-12 | aspirational | PASS | Output schema declares Lens as a 5th column: "string -- one sentence: 'As a [role], I care about [specific concern from `lens.verify`]'"; NOT: generic role restatements; NOT: multi-sentence; enforced per-row by per-row validation gate |
| C-13 | aspirational | PASS | Output schema table declared before phases with explicit type contracts per column; per-row validation gate: "before writing any row, verify all five cells against their constraints including anti-pattern exclusions" |
| C-15 | aspirational | PASS | "PHASE 2 -- CHALLENGER BRACKET" as a named discrete phase; G1 gate enforces domain review cannot begin until CLOSED |
| C-16 | aspirational | PASS | PHASE 2 C4: per-slot escalation to dedicated HIGH matrix row |
| C-17 | aspirational | PASS | "Domain review does not begin until G1 transitions to CLOSED" |
| C-18 | aspirational | PASS | PHASE 2 C4 steps 3–4: "Do not embed this finding as a sentence within the challenger row's Findings cell… Do not append this as a note or comment below the challenger row. An appended note is not a matrix row. It does not satisfy G1 closure condition 3." |
| C-19 | aspirational | PASS | Output schema table includes NOT clauses in every column definition: Lens ("NOT: generic role restatements"), Findings ("NOT: abstract observations without a named surface"), Severity ("NOT: freestyle labels; NOT: blank cells; NOT: combinations"), Recommendation ("NOT: generic directives; NOT: recommendations without a named artifact location") |
| C-20 | aspirational | PASS | PHASE 2: G1 states OPEN/CLOSED named; G1 closure predicate: 4 enumerated conditions all must hold |
| C-21 | aspirational | PASS | PHASE 2 C4 steps 3–4 name prohibited forms inside the escalation rule: "Do not embed… A sentence inside another row's Findings cell is not a dedicated row… Do not append… An appended note is not a matrix row." |

**Score**: E=60, R=60, A: 2.5+2.5+2.5+2.5+2.5+2.5+2.5+2.5+2.5+2.5 = 25
**Composite: 145** — Golden ✓ (perfect score)

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Composite | Golden? | Rank |
|-----------|-----------|-------------|--------------|-----------|---------|------|
| V-05 | 60 | 60 | 25.00 | **145.00** | YES | 1 |
| V-02 | 60 | 60 | 21.25 | **141.25** | YES | 2 |
| V-03 | 60 | 60 | 18.75 | **138.75** | YES | 3 |
| V-01 | 54* | 60 | 23.75 | **137.75** | YES | 4 |
| V-04 | 60 | 60 | 17.50 | **137.50** | YES | 5 |

*C-04 PARTIAL (6 pts). All variations reach golden threshold.

---

## Aspirational Pass Heatmap

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | FAIL | FAIL | FAIL | FAIL | **PASS** |
| C-13 | PART | PASS | PART | FAIL | **PASS** |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PART | FAIL | FAIL | **PASS** |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |

C-12 and C-13/C-19 are the primary differentiators. V-05 is the only variation to clear all three in this round.

---

## Excellence Signals — V-05

**Signal 1: Pre-execution schema as a standalone artifact.**
V-05 declares the full output schema in a separate table — positioned *before* any phase definitions — with typed constraints and anti-pattern exclusions for every column. This is structurally different from all prior rounds, where schema was embedded inside execution steps or a VALIDATE phase. By declaring the schema first, the model holds the complete column contract in context before beginning PHASE 1. This makes C-13 and C-19 satisfied by construction: the schema is consulted at per-row write time, not reconstructed from scattered step instructions.

**Signal 2: Explicit criterion-check table as a named verification phase.**
PHASE 4 VERIFY inserts a mandatory checkpoint between domain review and final render. The model produces a visible YES/NO/PARTIAL table for all 11 aspirational criteria. A NO on any criterion designed to be satisfied triggers phase re-execution. This is the first variation across all six rounds where the skill's own rubric criteria appear in the output as a first-class artifact. The effect: C-20 and C-21 satisfaction moves from "recall during execution" to "checklist confirmation before output" — the same invariant-at-output-time principle that V-01 targeted, but applied to aspirational criteria specifically rather than to the schema.

These two signals work together: the schema handles structural output correctness (column contracts), the criterion-check table handles behavioral correctness (aspirational mechanisms). Together they close the gap that R5's maximal variation left open — the construction-time criteria (C-12, C-13, C-19) that require the model to apply discipline before writing, not detect it after.

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["pre-execution schema declared as standalone artifact before phase definitions, with per-column anti-pattern exclusions covering all five columns", "explicit criterion-check table as PHASE 4 VERIFY with forced phase re-execution on NO, making aspirational criteria first-class visible output artifacts before render"]}
```
