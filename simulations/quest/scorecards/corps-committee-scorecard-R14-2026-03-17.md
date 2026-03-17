## Quest Score — corps-committee R14 (v14 Rubric)

---

### Scoring Methodology

| Band | Weight | Criteria | Pts/criterion |
|------|--------|----------|---------------|
| Essential (C-01–C-05) | 60 pts | 5 | 12 pts |
| Recommended (C-06–C-08) | 30 pts | 3 | 10 pts |
| Aspirational (C-09–C-41) | 10 pts | 33 | 0.303 pts |

PASS = full pts · PARTIAL = ½ pts · FAIL = 0 pts

---

### Structural Axis Map

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| BEFORE YOU START register | Descriptive | Descriptive | **Imperative** | Descriptive | **Imperative** |
| FAILS template self-referential (C-40) | **SELF-REF** | examples only | examples only | **SELF-REF** | **SELF-REF** |
| PHASE-1-COMMIT forward annotation (C-41) | Absent | **Present** | Absent | **Present** | **Present** |
| PHASE-1 fill rule C-41 annotation | Absent | **Present** | Absent | **Present** | **Present** |
| Register ambiguity eliminated | No | No | **Yes** | No | **Yes** |

---

### Essential Criteria (C-01–C-05) — All Variations

All five essential criteria are enforced identically across all variations by the shared fill rules.

| ID | Criterion | All Variations | Evidence |
|----|-----------|---------------|---------|
| C-01 | Committee type correctly instantiated | **PASS** | Phase 0 requires committee-type declaration; BEFORE YOU START names ROB / shiproom / arch-board with distinct obligations |
| C-02 | Each participant speaks from their role | **PASS** | ROLE VOICE GUARD table (Mechanism 2) + SEQUENTIAL TIER GATE (Mechanism 1) — dual enforcement present in all variations |
| C-03 | Decisions explicitly recorded | **PASS** | ## STANCE MANIFEST with STANCE INVARIANT mandated; verdict in Phase 5 must match OUTCOME exactly |
| C-04 | Action items captured with owners | **PASS** | ACTION ITEMS table with Owner Role column (Mechanism 1) + OWNERSHIP TALLY with zero-anonymous-items gate (Mechanism 2) |
| C-05 | Dissenting opinion represented | **PASS** | DISSENTING OPINIONS table required; vacuous-satisfaction row mandated when no dissent |

**Essential subtotal — all variations: 60 / 60**

---

### Recommended Criteria (C-06–C-08) — All Variations

| ID | Criterion | All Variations | Evidence |
|----|-----------|---------------|---------|
| C-06 | Formal structure | **PASS** | Phase 0–5 lifecycle enforces header / agenda / discussion / decisions / action items / next steps |
| C-07 | Discussion depth reflects committee type | **PASS** | Tier 1 requires INERTIA-FINDING cite; Tier 2 requires specific condition deliverable (not "address concerns"); Tier 3 requires RESPONDS-TO named concern |
| C-08 | AMEND honored when invoked | **PASS** | Full AMEND fill rules with block-dependency routing table, stale-site marking, RECOMMIT MANIFEST gate |

**Recommended subtotal — all variations: 30 / 30**

---

### Aspirational Criteria — Shared PASS Baseline (C-09–C-39, 30 criteria)

These criteria are satisfied identically across all variations. Notable evidence:

| ID | Status | Key Evidence |
|----|--------|--------------|
| C-09 | PASS | INERTIA-ADVOCATE injection provides outside-in skeptical signal with named INERTIA-FINDING labels — outside-in by construction |
| C-10 | PASS | Phase 0 charter gate declares quorum / scope before simulation; Phase 2 exit commits escalation path |
| C-11 | PASS | "DECLARE YES if found. INJECT Inertia-Advocate as Tier 1 if not found" — injection is the default path |
| C-12 | PASS | Phase 0 attendee list includes provisional annotation for injection-pending roles |
| C-14 | PASS | FAILS [C-02], [C-04], [C-05], [C-07], [C-23], [C-25], [C-33], [C-34] all present with correct IDs; well exceeds 3-entry threshold |
| C-15 | PASS | PHASE-N-ENTER gates in Phase 0 declare charter preconditions; Phase 1 cannot begin until charter constraints committed |
| C-16–C-33 | PASS (18) | Inherited from R12 V-05 baseline: COMMIT seals, TOKEN TRACE CONFIRMATION, three-way status vocabulary, TIER-N-SEQUENCE-COMMIT, AMEND routing graph, stale-site marking, RECOMMIT MANIFEST |
| C-34 | PASS | RECOMMIT MANIFEST emitted before downstream phase resumes; gate explicitly blocks v1 seal after AMEND |
| C-35 | PASS | PHASE-1-COMMIT enumerates sealed tokens as explicit closed set; dropped token produces visible absence |
| C-36 | PASS | CONSUMED / NOT-APPLICABLE / DROPPED vocabulary + count invariant tied to C-35 manifest; REQUIRES: C-35 present |
| C-37 | PASS | C-02: ROLE VOICE GUARD (table) + TIER GATE (sequence commit) — two independent mechanisms. C-04: Owner Role column + OWNERSHIP TALLY — two independent mechanisms |
| C-38 | PASS | FAILS SYNTAX TEMPLATE defines `FAILS [C-NN]: <description>` as canonical positional form; states that omission is syntactically malformed |
| C-39 | PASS | `REQUIRES: C-35` declared immediately before C-36 fill rules |

**Shared aspirational subtotal: 30 × 0.303 = 9.09 pts**

---

### Variable Criteria per Variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-13** — Pre-skeleton imperative block | PARTIAL | PARTIAL | **PASS** | PARTIAL | **PASS** |
| **C-40** — FAILS template self-referential entries | **PASS** | FAIL | FAIL | **PASS** | **PASS** |
| **C-41** — Prerequisite annotation at source block | FAIL | **PASS** | FAIL | **PASS** | **PASS** |

**C-13 evidence by variation:**
- V-01/V-02/V-04 (Descriptive): BEFORE YOU START block exists and names per-type obligations, but uses descriptive framing ("ROB is for…") rather than direct imperative ("If there is no metric, you have not done a ROB"). Satisfies existence requirement; fails register requirement → PARTIAL.
- V-03/V-05 (Imperative): Explicit natural-language fail conditions in direct imperative voice, one per committee type → PASS.

**C-40 evidence by variation:**
- V-01/V-04/V-05 (SELF-REFERENTIAL): FAILS template includes `FAILS [C-38]: FAILS entry missing [C-NN]` and `FAILS [C-39]: REQUIRES: C-35 absent` — citation targets for template violations are embedded in the template itself → PASS.
- V-02/V-03 (CORRECT examples only): Template shows correct form and a MALFORMED example but cites no criterion ID for what that malformed entry violates → FAIL.

**C-41 evidence by variation:**
- V-01/V-03 (Absent): PHASE-1-COMMIT seal exists and closes the token set (satisfying C-35), but no forward annotation identifying which downstream criterion depends on this closed set → FAIL.
- V-02/V-04/V-05 (Present): Inline note on PHASE-1-COMMIT: `[This explicit closed set is the prerequisite for C-36 TOKEN TRACE CONFIRMATION row count = 4]`; fill-rule section echoes the annotation → PASS.

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| **V-05** | 60.00 | 30.00 | 9.09 + 0.303(C-13) + 0.303(C-40) + 0.303(C-41) = **10.00** | **100.0** |
| **V-04** | 60.00 | 30.00 | 9.09 + 0.152(C-13) + 0.303(C-40) + 0.303(C-41) = **9.85** | **99.85** |
| **V-01** | 60.00 | 30.00 | 9.09 + 0.152(C-13) + 0.303(C-40) + 0.000(C-41) = **9.55** | **99.55** |
| **V-02** | 60.00 | 30.00 | 9.09 + 0.152(C-13) + 0.000(C-40) + 0.303(C-41) = **9.55** | **99.55** |
| **V-03** | 60.00 | 30.00 | 9.09 + 0.303(C-13) + 0.000(C-40) + 0.000(C-41) = **9.39** | **99.39** |

**Ranking:** V-05 > V-04 > V-01 = V-02 > V-03

---

### Rank Summary

| Rank | Variation | Score | Delta from V-05 |
|------|-----------|-------|-----------------|
| 1 | V-05 | 100.0 | — |
| 2 | V-04 | 99.85 | −0.15 (C-13 PARTIAL) |
| 3= | V-01 | 99.55 | −0.45 (C-13 PARTIAL + C-41 FAIL) |
| 3= | V-02 | 99.55 | −0.45 (C-13 PARTIAL + C-40 FAIL) |
| 5 | V-03 | 99.39 | −0.61 (C-40 FAIL + C-41 FAIL) |

V-01 and V-02 score identically because each gains one aspirational point (C-40 and C-41 respectively) while both carry the same C-13 PARTIAL penalty. The isolation was clean: neither single-axis variation dominates the other.

V-03's penalty is counterintuitive — its uniform imperative register passes C-13 but forfeits both C-40 and C-41, making it the lowest scorer despite being the only single-axis test that achieves a full PASS on a variation criterion.

---

### Excellence Signals — V-05

Three structural properties distinguish V-05:

**1. Two-sided dependency tracing (C-39 + C-41 combined)**
The prerequisite relationship between C-35 and C-36 is declared at both sites: forward annotation on PHASE-1-COMMIT ("this closed set is the prerequisite for C-36 row count") and `REQUIRES: C-35` before C-36's fill rules. A reviewer evaluating PHASE-1-COMMIT sees the downstream consequence before reaching Phase 2. A reviewer evaluating C-36 sees the upstream requirement stated in-place. Either path surfaces the dependency — one-sided declaration (C-39 alone) is correct but not redundancy-hardened.

**2. Self-documenting FAILS template (C-40)**
The template contains `FAILS [C-38]: FAILS entry missing [C-NN]` and `FAILS [C-39]: REQUIRES: C-35 absent`. Learning the positional form simultaneously teaches what to cite if that form is violated. Without self-referential entries, a reviewer encountering a template violation must already know C-38 or C-39 before they can score it — the self-referential entry eliminates that prior knowledge requirement and makes the template self-auditing.

**3. Register unification at the point of learning (C-13)**
The BEFORE YOU START block uses direct imperative with explicit fail conditions ("If there is no metric, you have not done a ROB") rather than descriptive framing. The distinction: a descriptive block conveys what each type is; an imperative block conveys what a failure looks like before it happens. This is the same principle as the self-referential template — failure anatomy taught at the point of learning, not discovered at the point of scoring.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Two-sided dependency annotation: forward pointer at source block (C-41) paired with REQUIRES at consumption site (C-39) creates bidirectional traceability — a weak source implementation is detectable before reaching the dependent fill rules", "Self-referential FAILS template entries for governing criteria (C-40) eliminate prior-knowledge requirement for violation detection — the template teaches both correct form and the citation target for that form's own violation simultaneously", "Uniform direct-imperative register in BEFORE YOU START block (C-13 full PASS) encodes failure anatomy before fill begins — 'if there is no metric you have not done a ROB' catches the most common defect at the earliest possible intervention point"]}
```
