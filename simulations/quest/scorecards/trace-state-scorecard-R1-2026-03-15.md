## trace-state Round 1 Scoring — Rubric v17

> Note: No executed trace artifact was provided ("placeholder"). Evaluation is **structural guarantee analysis** — how well each prompt design forces each criterion, not execution quality of a specific run.

---

### V-01 — Reachability-First Layout

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | PASS | Transition table mandates From State / Operation / To State columns; reachability map linkage makes omissions visible by grid-to-table mismatch |
| C-02 | Precondition + Postcondition | PASS | Fill rules: "at least one checkable assertion per row" (pre); "at least one assertion distinct from To State name" (post) |
| C-03 | Invariant Declaration + Per-Step | PASS | STEP 3 declares; INV-01/INV-02 columns in transition table are "never blank" |
| C-04 | Defect Identification | PASS | STEP 8 Findings with labeled types + grid cell / row references |
| C-05 | Domain Plausibility | PASS | Domain role auto-selection; "No generic labels" enforced in STEP 1 |
| C-06 | Consistent Format | PASS | Uniform transition table throughout; reachability map for coverage |
| C-07 | Non-Trivial Invariants | PASS | "Invariants must encode specific business rules"; authority source required (SLA clause, accounting regulation, policy) |
| C-08 | Race Condition Analysis | PARTIAL | Table exists; "or explicitly clear them" escape valve — no mandate for at least one concrete interleaving |
| C-09 | Negative Path Tracing | PASS | STEP 6 table with 4-element structure; "Required elements per row" explicit |
| C-10 | Reachability Annotation | PASS | Strongest C-10 of all five — opening deliverable, every cell labeled TRACED/SKIP/ILLEGAL, total counts required |

**Essential:** 5/5 → 60 | **Recommended:** 2.5/3 → 25 | **Aspirational:** 2/2 → 10
**Composite: 95** | Band: Golden | All essential: ✓

---

### V-02 — Lifecycle Emphasis: Negative Path as First-Class Section

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | PASS | Per-operation code block: Starting state / Ending state / operation name all labeled |
| C-02 | Precondition + Postcondition | PASS | Format labels Preconditions and Postconditions; distinct assertion required |
| C-03 | Invariant Declaration + Per-Step | PASS | STEP 1 invariants; per-operation "check every declared invariant" |
| C-04 | Defect Identification | PASS | STEP 5 Defect Summary table with typed defects |
| C-05 | Domain Plausibility | PASS | Domain expert auto-selection; lifecycle vocabulary specified |
| C-06 | Consistent Format | PASS | OPERATION N and BLOCKED OPERATION N code blocks used consistently throughout |
| C-07 | Non-Trivial Invariants | PASS | "domain-specific business rules, not structural assertions" with qualifying examples |
| C-08 | Race Condition Analysis | PARTIAL | STEP 4 table present; "If no concurrent access possible... state explicitly for each" — no minimum-one mandate |
| C-09 | Negative Path Tracing | PASS | 6-element BLOCKED OPERATION format; minimum two blocked ops; invariant-violation variant required |
| C-10 | Reachability Annotation | FAIL | No reachability section — no coverage grid, no listing of omitted transitions |

**Essential:** 5/5 → 60 | **Recommended:** 2.5/3 → 25 | **Aspirational:** 1/2 → 5
**Composite: 90** | Band: Acceptable | All essential: ✓

---

### V-03 — Phrasing Register: Per-Criterion Call-Outs Embedded

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | PASS | Code block fields labeled `Starting state (C-01a)` and `Ending state (C-01b)` — criterion ID at the exact element |
| C-02 | Precondition + Postcondition | PASS | `Preconditions (C-02a)` and `Postconditions (C-02b)` labeled inline; postcondition must be "distinct from state name" |
| C-03 | Invariant Declaration + Per-Step | PASS | SECTION 2 declares; `Invariant check (C-03): never skip` enforced in every operation block |
| C-04 | Defect Identification | PASS | SECTION 4 dedicated typed defect table; `*(Satisfies: C-04)*` |
| C-05 | Domain Plausibility | PASS | Domain expert roles; domain vocabulary required; no generic labels |
| C-06 | Consistent Format | PASS | SECTION 3 code block format consistent throughout; criterion label embedded |
| C-07 | Non-Trivial Invariants | PASS | Non-qualifying examples named ("state must be valid" blocked); qualifying examples shown; `(Satisfies C-07 if business-rule-sourced)` |
| C-08 | Race Condition Analysis | PASS | SECTION 6 `*(Satisfies: C-08 — one concurrent interleaving with conflict or resolution named)*`; "Identify **at least one** operation that could be invoked concurrently" — minimum-one mandate |
| C-09 | Negative Path Tracing | PASS | SECTION 5 `*(Satisfies: C-09 — all four elements required)*`; 2-column element table with rows numbered (1)–(4) |
| C-10 | Reachability Annotation | PASS | SECTION 7 `*(Satisfies: C-10 — every omitted transition listed; silent omissions do not qualify)*`; traced list + omitted table + rationale options |

**Essential:** 5/5 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 2/2 → 10
**Composite: 100** | Band: Golden | All essential: ✓

---

### V-04 — Combined: Two-Expert Model (Domain Expert + Concurrency Analyst)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | PASS | T2 code block: Starting state / Ending state / operation; all three elements |
| C-02 | Precondition + Postcondition | PASS | "Minimum two per operation" (pre); "minimum one, distinct from state name" (post) |
| C-03 | Invariant Declaration + Per-Step | PASS | D3 Invariant Registry with D3 Gate: "No forward trace begins until invariant registry is complete"; per-op check required |
| C-04 | Defect Identification | PASS | C3 Defect Synthesis table, typed, priority-ordered |
| C-05 | Domain Plausibility | PASS | Domain Expert owns vocabulary; domain state names specified in role definition |
| C-06 | Consistent Format | PASS | T2 code blocks consistent throughout forward path |
| C-07 | Non-Trivial Invariants | PASS | D3: "encode a real business rule that a generic framework would not automatically enforce"; D3 Gate adds structural pressure |
| C-08 | Race Condition Analysis | PASS | C2: "At least one operation must be analyzed with **both interleavings** described" — explicit double-interleaving mandate; Concurrency Analyst owns exclusively |
| C-09 | Negative Path Tracing | PASS | C1: "At least **two** blocked operations; each must include all four elements — no element may be omitted"; explicit `(3) Confirmation: 'State is unchanged. Operation did not execute.'` |
| C-10 | Reachability Annotation | PASS | Closing section: "Every omission requires a rationale"; Owner Section column adds accountability |

**Essential:** 5/5 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 2/2 → 10
**Composite: 100** | Band: Golden | All essential: ✓

---

### V-05 — Combined: Output Format + Inertia Framing + Reachability Audit

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State Transition Completeness | PASS | 3A table: From State / Operation / To State; domain vocabulary required |
| C-02 | Precondition + Postcondition | PASS | Fill rules: "minimum two checkable assertions per row" (pre); "minimum one distinct from To State name" (post) |
| C-03 | Invariant Declaration + Per-Step | PASS | STAGE 2 invariants + "Inertia linkage" adds business-rule depth; INV-01/INV-02 columns "never blank" |
| C-04 | Defect Identification | PASS | FINDINGS table with defect types + STAGE 1 cross-references |
| C-05 | Domain Plausibility | PASS | Domain Expert role; inertia challenge uses domain-specific business examples |
| C-06 | Consistent Format | PASS | 3A structured table format used consistently |
| C-07 | Non-Trivial Invariants | PASS | Inertia linkage: "note which STAGE 1 rows should become new invariants" — business-rule derivation pipeline strengthens invariant quality |
| C-08 | Race Condition Analysis | PARTIAL | 3C table present; "If cleared per operation: specific reason required" — but no minimum-one interleaving mandate, full clearance still possible |
| C-09 | Negative Path Tracing | PASS | 3B: all four elements as labeled column headers; "STAGE 1 Row Ref" column ensures inertia seeds at least one candidate; element definitions given |
| C-10 | Reachability Annotation | PASS | STAGE 4: three tables (traced / negative path / omitted) + coverage summary with counts; "Silent omissions are not acceptable" |

**Essential:** 5/5 → 60 | **Recommended:** 2.5/3 → 25 | **Aspirational:** 2/2 → 10
**Composite: 95** | Band: Golden | All essential: ✓

---

### Ranking

| Rank | Var | Composite | C-08 | C-09 | C-10 | Distinguishing Feature |
|------|-----|-----------|------|------|------|------------------------|
| 1 | **V-03** | **100** | PASS | PASS | PASS | Inline criterion labels eliminate coverage gaps; minimum-one C-08 mandate; parsimony advantage |
| 1 | **V-04** | **100** | PASS | PASS | PASS | Dedicated Concurrency Analyst role; strongest C-09 (two blocked ops + confirmation line) |
| 3 | **V-01** | **95** | PARTIAL | PASS | PASS | C-10 strongest of all (opening deliverable, mandatory counts); C-08 escape valve holds it back |
| 3 | **V-05** | **95** | PARTIAL | PASS | PASS | Inertia→negative-path pipeline novel; C-10 coverage summary with counts; C-08 escape valve same issue |
| 5 | **V-02** | **90** | PARTIAL | PASS | FAIL | Best C-09 format detail (6 elements, "why someone tries this"); C-10 completely absent |

---

### Excellence Signals (from V-03 and V-04)

**1. Inline criterion labels at the point of satisfaction**
V-03's `(Satisfies: C-09 — all four elements required)` and `Starting state (C-01a)` embedded in the format eliminate the gap between abstract rubric awareness and execution. The writer cannot finish a section without seeing which criterion they just satisfied — or failed to satisfy.

**2. Explicit non-qualifying examples for invariants**
V-03 names what doesn't count: `"state must be valid"`, `"entity must exist"`, `"id is not null"`. Negative examples are more constraining than positive examples alone. Combined with the `(Satisfies C-07 if business-rule-sourced)` conditional label, this prevents weak invariants from slipping through.

**3. Minimum-one mandate for C-08 (not an escape valve)**
Both V-03 and V-04 phrase C-08 as "identify at least one operation... **must** be analyzed." V-01/V-02/V-05 allow total clearance with "if no concurrent access, state [reason]." The distinction: mandatory analysis vs. optional analysis. The word "must" changes the default.

**4. Role ownership boundaries with "May not perform" clauses**
V-04's "May not perform: forward path trace, state vocabulary, invariant declaration" is a structural exclusion — the Concurrency Analyst cannot dilute C-08/C-09 by deferring to other sections they don't own. This turns attention constraints into ownership constraints.

**5. Numbered four-element template (not prose description)**
Both V-03 and V-04 use `(1) Invalid starting state... (2) Attempted operation... (3) Resulting state... (4) Error signal` as labeled template rows, not as prose instructions. The difference: a template demands filling, a description invites approximation.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inline-criterion-labels-at-point-of-satisfaction", "non-qualifying-examples-block-weak-invariants", "mandatory-minimum-one-for-c08-not-escape-valve", "role-ownership-with-may-not-perform-boundaries", "numbered-four-element-template-forces-c09-completeness"]}
```
