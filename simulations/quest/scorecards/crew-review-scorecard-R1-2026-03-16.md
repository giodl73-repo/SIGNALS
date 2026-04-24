## crew-review — Quest Score R1

### Scoring per Variation

---

#### V-01 — Inertia Framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Role selection grounded | PASS | Step 1: explicit registry read + ERROR halt + "do not fabricate" rule |
| C-02 | Matrix structure present | PASS | Step 5 defines 4-column table with explicit headers |
| C-03 | Severity semantics | PASS | Step 4: HIGH/MEDIUM/LOW with definitions; Inertia Advocate severity logic maps to content |
| C-04 | Role-specific lens | PASS | Step 4: "Apply only that role's lens.verify" + explicit "Do not duplicate a finding already raised" |
| C-05 | Concrete recommendations | PASS | Step 4: "names what to do and where in the artifact"; Step 5: "naming a specific surface or next step" |
| C-06 | Depth flag respected | PASS | Step 3: standard = 2–3 additional (3–4 total); `--depth deep` = full registry |
| C-07 | Cross-role signal | PASS | Step 6: required synthesis block, names convergence or conflict |
| C-08 | AMEND present | PASS | Step 7: 3 options (add reviewer, full registry, restrict scope) |
| C-09 | Inertia-advocate leads | PASS | "Before any domain review, the Inertia Advocate speaks first. This is not optional." + 3-blank null hypothesis template |
| C-10 | Finding specificity | PASS | "Find something specific... name the section, field, or component"; Step 5: "specific observation tied to a named artifact surface" |

**Composite**: 5/5 essential (60) + 3/3 recommended (30) + 2/2 aspirational (10) = **100**
**All essential pass**: YES — **Golden**

---

#### V-02 — Output Format

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Role selection grounded | PASS | Phase 1: reads all files; column contract: "Zero fabricated names" |
| C-02 | Matrix structure present | PASS | Schema defined upfront before execution; all 4 columns with types and constraints |
| C-03 | Severity semantics | PASS | Column type: "enum — Exactly one of: HIGH, MEDIUM, LOW. No other values." — strongest enforcement |
| C-04 | Role-specific lens | PARTIAL | No lens-lock instruction; no non-duplication rule; role selection by domain implies differentiation but doesn't enforce it |
| C-05 | Concrete recommendations | PASS | Column constraint: "Must name (1) what to do and (2) where in the artifact. Generic directives... are invalid." |
| C-06 | Depth flag respected | PASS | Phase 2: default 2–4, `--depth deep` = all roles |
| C-07 | Cross-role signal | PASS | Phase 4: "required, 2–3 sentences" |
| C-08 | AMEND present | PASS | Phase 4: "required" AMEND block with 3 options |
| C-09 | Inertia-advocate leads | FAIL | No mention of inertia-advocate or challenger-first mandate anywhere in the prompt |
| C-10 | Finding specificity | PASS | Column constraint: "Must name a specific artifact surface... Generic observations without a named surface are invalid." + Phase 3 per-row validation |

**Composite**: 4.5/5 essential (54) + 3/3 recommended (30) + 1/2 aspirational (5) = **89**
**All essential pass**: NO (C-04 partial) — Not Golden

---

#### V-03 — Phrasing Register

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Role selection grounded | PASS | "Read every file. That directory is your complete reviewer pool — don't invent anyone who isn't there." |
| C-02 | Matrix structure present | PASS | "write the table: \| Role \| Findings \| Severity \| Recommendation \|" — direct 4-column header |
| C-03 | Severity semantics | PASS | "Call it HIGH, MEDIUM, or LOW. Nothing else." + per-level definitions |
| C-04 | Role-specific lens | PASS | Explicit lens-lock step per role: "What does someone in this role actually care about? (one sentence — lock the lens)" forces perspective before finding |
| C-05 | Concrete recommendations | PASS | "Tell them exactly what to do about it and where." |
| C-06 | Depth flag respected | PASS | "pick 2 to 4 roles… `--depth deep`: everyone runs" |
| C-07 | Cross-role signal | PASS | "did any two reviewers agree on the same thing? Name it. Did any two disagree? Name that too." |
| C-08 | AMEND present | PASS | AMEND block with 3 options |
| C-09 | Inertia-advocate leads | PASS | "Put the Inertia Advocate in first." + explicit questions about status quo and switching cost |
| C-10 | Finding specificity | PASS | "Point to something specific — a section title, a named field, a diagram, a stated assumption. Don't be vague." + "Every finding names something in the artifact." |

**Composite**: 5/5 essential (60) + 3/3 recommended (30) + 2/2 aspirational (10) = **100**
**All essential pass**: YES — **Golden**

Note: C-04 is PASS (not PARTIAL) because the per-role lens-lock step is an explicit structural protection — it forces the model to name each role's perspective before any finding is written. The absence of an explicit "no duplication" rule is a minor gap but insufficient to demote to PARTIAL given the lens-lock step.

---

#### V-04 — Role Sequence + Inertia Framing (combination)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Role selection grounded | PASS | Step 1: reads all files, extracts archetype field, ERROR halt if absent |
| C-02 | Matrix structure present | PASS | Step 5: 4-column matrix with explicit headers |
| C-03 | Severity semantics | PASS | Step 4: "Severity: HIGH / MEDIUM / LOW only" |
| C-04 | Role-specific lens | PASS | Step 4: "Apply only that role's lens.verify perspective (read from the role file)" + "Do not repeat a finding already raised by a previous role" — both constraints present |
| C-05 | Concrete recommendations | PASS | Step 4: "Recommendation: what to do + where in the artifact" |
| C-06 | Depth flag respected | PASS | Step 2: archetype-grouped selection, 2–4 total; `--depth deep` = all in archetype order |
| C-07 | Cross-role signal | PASS | Step 6: convergence and conflict naming required |
| C-08 | AMEND present | PASS | Step 7: 3 specific options including skip-challengers toggle |
| C-09 | Inertia-advocate leads | PASS | Step 3: "Challenger bracket (always runs first)" — structural, not instructional; null hypothesis template explicitly required |
| C-10 | Finding specificity | PASS | Step 4: "Name a specific artifact surface in each finding" |

**Composite**: 5/5 essential (60) + 3/3 recommended (30) + 2/2 aspirational (10) = **100**
**All essential pass**: YES — **Golden**

---

#### V-05 — Output Format + Lifecycle Emphasis (combination)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Role selection grounded | PASS | L1–L4: reads all files; "Zero roles may be invented. Pool is now locked." |
| C-02 | Matrix structure present | PASS | R2: explicit 4-column matrix; PHASE 4 entry condition = all rows validated |
| C-03 | Severity semantics | PASS | Per-row validation table: "Exactly HIGH, MEDIUM, or LOW — no other values"; enforced before row is written |
| C-04 | Role-specific lens | PARTIAL | Validation table checks format/correctness but no lens-lock instruction and no non-duplication rule for non-challenger roles; challenger exception exists but domain roles have no equivalent constraint |
| C-05 | Concrete recommendations | PASS | Validation rule: "Names what to do AND where in the artifact — not a generic directive" |
| C-06 | Depth flag respected | PASS | Phase 2 (SELECT): most structured depth handling — S1 checks flag, branches cleanly, exception for challenger archetype |
| C-07 | Cross-role signal | PASS | R3: "required" synthesis block; must name convergence or conflict |
| C-08 | AMEND present | PASS | R4: "required" AMEND block with 4 options (richest of all five variations) |
| C-09 | Inertia-advocate leads | PASS | Phase 3: "Execute roles in this sequence: challenger archetype first." + "For challenger roles: finding must include null hypothesis" |
| C-10 | Finding specificity | PASS | Per-row validation table: "Names a specific artifact surface (section, field, diagram, assumption) — not generic" — enforced at write time |

**Composite**: 4.5/5 essential (54) + 3/3 recommended (30) + 2/2 aspirational (10) = **94**
**All essential pass**: NO (C-04 partial) — Not Golden

---

### Summary Ranking

| Variation | Composite | All Essential | Golden | Rank |
|-----------|-----------|---------------|--------|------|
| V-04 | 100 | YES | YES | 1 |
| V-01 | 100 | YES | YES | 2 |
| V-03 | 100 | YES | YES | 3 |
| V-05 | 94 | NO (C-04) | NO | 4 |
| V-02 | 89 | NO (C-04, C-09) | NO | 5 |

Three-way tie at 100. V-04 edges to rank 1: archetype-derived sequencing makes the challenger-first mandate **structural** (derived from data) rather than **instructional** (relying on the model to remember). V-01 is rank 2 for the cleaner null hypothesis template. V-03 is rank 3: conversational lens-lock works but lacks an explicit non-duplication rule that V-01 and V-04 both carry.

---

### Excellence Signals (from top-scoring variations)

**Signal 1 — Null hypothesis 3-blank template (V-01, V-04)**
The fill-in-the-blank format — "The team currently does [X]... cost is [Y]... worth acting on only if [Z]" — forces the model to extract specific artifact content rather than write a generic "status quo is fine" observation. This makes C-09 pass structurally rather than relying on model judgment about what constitutes a null hypothesis.

**Signal 2 — Lens-lock + non-duplication as a pair (V-01, V-04)**
C-04 requires both positive constraint (review from lens) and negative constraint (no overlap). Lens-lock alone (V-03) reduces duplication risk but does not eliminate it. Non-duplication alone without lens-lock leaves the "what perspective am I in?" question open. The pair is the minimum sufficient condition; either alone is not.

**Signal 3 — Archetype-derived sequencing decouples selection from ordering (V-04)**
Deriving execution order from the `archetype` field in role files means the challenger-first rule is derived from the registry data — not from remembering to execute a specific named role first. This generalizes: any future challenger roles automatically land in position 1 without prompt edits.

**Signal 4 — Per-cell validation table before write (V-02, V-05)**
Expressing output constraints as a validation table (checked per row before committing) is the strongest format enforcement pattern. V-02 and V-05 both use this, which is why they score highest on C-02, C-03, C-05, and C-10 — even when failing C-04. This pattern should be combined with lens-lock + non-duplication in v2 to close the remaining gap.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["null-hypothesis 3-blank template forces artifact-specific inertia row without model discretion", "lens-lock plus explicit non-duplication is the minimum sufficient pair for C-04 pass — either constraint alone is not enough", "archetype-derived execution order makes challenger-first structural rather than instructional and generalizes to any future challenger roles"]}
```
