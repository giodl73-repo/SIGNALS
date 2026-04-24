## crew-review — Quest Score, Round 3

### Scoring Methodology

- **Essential** (C-01–C-05): 5 × 12 pts = 60 max. PASS=12, PARTIAL=6, FAIL=0
- **Recommended** (C-06–C-10): 5 × 10 pts = 50 max. PASS=10, PARTIAL=5, FAIL=0
- **Aspirational** (C-11–C-16): 6 × 2.5 pts = 15 max. PASS=2.5, PARTIAL=1.25, FAIL=0

---

### Per-Criterion Evaluation

#### Essential

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Role selection grounded in .roles/ | PASS | PASS | PASS | PASS | PASS |
| C-02 | Review matrix structure present | PASS | PASS | PASS | PASS | PASS |
| C-03 | Severity uses HIGH/MEDIUM/LOW only | PASS | PASS | PASS | PASS | PASS |
| C-04 | Each role reviews from its own perspective | PASS | PASS | PASS | PASS | PASS |
| C-05 | Recommendations are concrete | PASS | PASS | PASS | PASS | PASS |

Evidence notes:
- All five variations explicitly read `.roles/`, disallow fabrication, and include 4-column matrix with severity constraints. C-02 passes for V-02/V-05 because the 5-column schema is a superset containing all four required columns.

---

#### Recommended

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Depth flag respected | PASS | PASS | PASS | PASS | PASS |
| C-07 | Cross-role signal surfaced | PASS | PASS | PASS | PASS | PASS |
| C-08 | AMEND options listed | PASS | PASS | PASS | PASS | PASS |
| C-09 | Inertia-advocate leads as challenger | PASS | PASS | PASS | PASS | PASS |
| C-10 | Finding specificity: named surface | PASS | PASS | PASS | PASS | PASS |

Evidence notes:
- **C-09**: V-02 passes despite using an exception clause (C-15 fail) because Phase 3 still executes challengers first and includes null hypothesis framing in the Lens cell. The C-15 distinction is mechanism (phase vs. exception), not execution order.
- **C-08**: All variations include named AMEND blocks with 3–4 specific options.

---

#### Aspirational

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-11 | Null hypothesis uses structured template | PASS | FAIL | PASS | PASS | PASS |
| C-12 | Per-role lens-lock declaration | FAIL | PASS | PARTIAL | PARTIAL | PASS |
| C-13 | Typed column contracts with per-row validation | PARTIAL | PASS | FAIL | FAIL | PASS |
| C-14 | Registry ERROR halt on missing/malformed data | PASS | PASS | PASS | PASS | PASS |
| C-15 | Challenger bracket as named execution phase | PASS | FAIL | PASS | PASS | PASS |
| C-16 | Slot-level failure escalation in null hypothesis | PASS | FAIL | PASS | PASS | PASS |

**Evidence notes by criterion:**

**C-11:**
- V-01: 4-slot SLOT-A/B/C/D form with named labels and fill rule. PASS.
- V-02: Challenger Lens cell opens with one-line null hypothesis framing ("As an inertia-advocate, I care about whether the team has a credible alternative today") but no multi-slot fill-in template. FAIL.
- V-03: 4-blank blockquote form with named descriptors (e.g., "what the team does today," "specific cost"). 4 named slots. PASS.
- V-04: PHASE 2 C2 defines 4-slot form; C5 exit condition requires all slots filled or escalated. PASS.
- V-05: 4-slot form in Step 3 SLOT-A/B/C/D with per-slot escalation. PASS.

**C-12:**
- V-01: "Apply only that role's lens.verify perspective" is a process instruction only. No lens statement required in output. Matrix is 4-column with no Lens column. FAIL.
- V-02: Lens is column 2 in 5-column schema with typed constraint and anti-pattern ("no generic restatements"). Per-row validation gate enforces it. PASS.
- V-03: "Lock the lens. One sentence: 'As a [role], I care about [the specific concern]'" is execution step 1, which would appear before findings. C-12 pass condition allows "preceded by." However, no schema column enforces it — a model could absorb the lens into Findings or omit it. PARTIAL.
- V-04: D2.1 "Lens declaration (required before findings)" is labeled required and is a numbered sub-step. Stronger than instruction-only but still no schema column. PARTIAL.
- V-05: Lens is column 2 in 5-column typed schema. Per-row validation gate covers all five columns including Lens. PASS.

**C-13:**
- V-01: Step 2 lists column constraints for Role and Severity inline. Two columns have explicit type constraints. No typed schema table (Column | Type | Constraint format), no per-row validation gate. The constraint is visible for two columns but the mechanism is annotation, not a validation phase. PARTIAL.
- V-02: Full 5-column schema table with Column | Type | Constraint headers. Named per-row validation gate: "before writing any row, verify all five cells against their constraints." PASS.
- V-03: No schema table, no validation gate. Behavioral instructions only. FAIL.
- V-04: Per-role D2 steps specify column requirements (specific surface, exact severity, specific recommendation) but no typed schema table and no named per-row validation gate. FAIL.
- V-05: Full typed schema table + "Per-row validation: before writing any row, verify all five cells satisfy their constraints." PASS.

**C-14:**
- All five: Three-level ERROR halt (absent / empty / malformed) with unconditional stop and explicit ERROR message string. V-04 adds "unconditional, no soft fallback" label. All PASS.

**C-15:**
- V-01: `### CHALLENGER PHASE` and `### DOMAIN PHASE` as explicit named section headers. "CHALLENGER PHASE closes here" before domain begins. PASS.
- V-02: Phase 2 (Select) uses "Include any role with `archetype: challenger` regardless of relevance" — exception clause in a flat selection step. Phase 3 (Review) executes challengers first, but the mechanism is inclusion order within a single execution phase, not a named bracket that must close before domain can begin. FAIL.
- V-03: "Challenger Phase -- runs before anything else" and "Challenger Phase done. Domain Phase starts now." Named phase with explicit verbal closure boundary. PASS.
- V-04: PHASE 2 CHALLENGER BRACKET with entry/exit conditions. "Domain review does not begin until PHASE 2 exits." Strongest phase-gate statement across all variations. PASS.
- V-05: Step 3 header: "Group 1 bracket (challenger -- runs before all other groups)." "Group 1 closes here. Group 2 begins next." as an explicit structural delimiter. Group 1 as a named execution block in a declared archetype queue. PASS.

**C-16:**
- V-01: "A slot that cannot be filled: write `[not stated in artifact]` in that slot, then log a HIGH finding: 'SLOT-[letter]: null hypothesis incomplete — [slot name] not stated in artifact.'" Per-slot, HIGH, logged. PASS.
- V-02: No 4-slot template exists; no per-slot escalation path. FAIL.
- V-03: "Can't fill a blank? That's their HIGH finding. Write `[not stated in artifact]`... and log it." Covers per-blank escalation in conversational form. PASS.
- V-04: C3 slot rules + C5 exit condition "every slot is either filled or escalated." PASS.
- V-05: "Per-slot escalation (applies to each slot individually)... log a **separate** HIGH finding row." Separate row is the strongest escalation form: the unfilled slot becomes an independently scored matrix entry. PASS.

---

### Composite Scores

| Section | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Essential (60 max) | 60 | 60 | 60 | 60 | 60 |
| Recommended (50 max) | 50 | 50 | 50 | 50 | 50 |
| Aspirational (15 max) | 11.25 | 7.5 | 11.25 | 11.25 | 15 |
| **Composite** | **121.25** | **117.5** | **121.25** | **121.25** | **125** |
| Golden (≥80, all essential) | YES | YES | YES | YES | YES |

Aspirational breakdown:

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| C-11 | 2.5 | 0 | 2.5 | 2.5 | 2.5 |
| C-12 | 0 | 2.5 | 1.25 | 1.25 | 2.5 |
| C-13 | 1.25 | 2.5 | 0 | 0 | 2.5 |
| C-14 | 2.5 | 2.5 | 2.5 | 2.5 | 2.5 |
| C-15 | 2.5 | 0 | 2.5 | 2.5 | 2.5 |
| C-16 | 2.5 | 0 | 2.5 | 2.5 | 2.5 |
| **Total** | **11.25** | **7.5** | **11.25** | **11.25** | **15** |

---

### Ranking

1. **V-05** — 125 (all 6 aspirational PASS; first perfect score in this series)
2. **V-01** — 121.25 (C-12 FAIL, C-13 PARTIAL; single-axis inertia frame strong on C-15/C-16 but no lens output mechanism)
2. **V-03** — 121.25 (C-13 FAIL, C-12 PARTIAL; conversational register carries phase structure but cannot enforce schema contracts)
2. **V-04** — 121.25 (C-13 FAIL, C-12 PARTIAL; lifecycle phase model is the strongest C-15 guarantee but lacks typed schema)
5. **V-02** — 117.5 (C-11 FAIL, C-15 FAIL, C-16 FAIL; typed schema + Lens column are the strongest C-12/C-13 vehicle but exception-clause challenger selection is the structural weakness)

Three-way tie at 121.25: each of V-01/V-03/V-04 solves six aspirational criteria but fails the C-12/C-13 pair differently. V-01 fails C-12 entirely (no output mechanism), V-03/V-04 get partial C-12 (instruction-present, schema-absent) but fail C-13 entirely.

---

### Excellence Signals from V-05

**Signal 1 — Lens column in typed schema collapses C-12 into C-13**
V-05's key design insight: rather than treating lens-lock as a behavioral instruction (V-01) or a required execution step (V-04), integrating Lens as column 2 in the output schema makes C-12 and C-13 the same enforcement mechanism. The per-row validation gate covers the Lens cell along with all other columns — one mechanism, two criteria. No variation before V-05 made this connection.

**Signal 2 — Archetype group table as pre-execution data contract**
V-05 Step 2 declares a group assignment table (`Group 1 = archetype: challenger; Group 2 = product; ...`) before any execution begins. This makes execution order a data structure, not an instruction. The challenger's priority is encoded in the queue definition, not in prose ("challengers run first"). "Group 1 closes here. Group 2 begins next." then becomes a structural delimiter rather than a completion marker. This is how V-05 achieves C-15 without needing lifecycle phase headers.

**Signal 3 — Per-slot escalation produces a separate matrix row**
V-04's C5 exit condition is strong — the challenger phase cannot exit with a silent slot. V-05 goes one step further: the escalated finding is not an annotation within the challenger's row but a distinct matrix entry ("log a separate HIGH finding row"). An unfilled slot becomes independently reviewable, independently scored, and independently filterable from the challenger's primary review row. This is the strongest form of C-16 in the series.

---

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["Lens column in typed schema unifies C-12 and C-13 into one enforcement mechanism — per-row validation gate covers Lens alongside Severity, making lens-lock structurally inseparable from column-contract validation", "Execution queue declared as a pre-execution archetype group table — challenger priority encoded as a data structure before review begins, not as an instruction inside the execution flow"]}
```
