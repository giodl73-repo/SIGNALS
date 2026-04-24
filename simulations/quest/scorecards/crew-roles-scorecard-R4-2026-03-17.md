Now I have all the information needed. Let me score each variation against the v4 rubric.

---

## Round 4 Scorecard — crew-roles

**Scoring formula**: `(essential_pass/5 * 60) + (recommended_score/30 * 30) + (aspirational_pass/12 * 10)`

Aspirational denominator = 12. Each full PASS = 0.833 pts; PARTIAL = 0.417 pts.

---

### V-01: Three-Bucket Phase 1

**Axis**: Q-domain-aligned vocabulary distribution via three-bucket Phase 1 (C-20 single axis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | PASS | Template has name (# header), orientation (frame/serves), lens (verify/simplify), expertise (depth/relevance), scope, collaborates_with |
| C-02 | Inertia-advocate present | PASS | Phase 4 specifies inertia-advocate with frame challenging Q1 current system / Q2 migration cost |
| C-03 | Correct output path | PASS | "Write role files to `.roles/{area}/`" in opening instruction |
| C-04 | Domain specificity | PASS | expertise.relevance must reference a Phase 1 vocabulary term from any bucket; vocabulary is extracted from input |
| C-05 | Minimum 3 roles | PASS | Phase 3 table pre-populates pm, architect, inertia-advocate, domain-specialist rows (≥ 3) |
| C-06 | Lens actionability | PASS | Template shows verify items ending `?`; simplify items as imperatives (Remove/Defer/Collapse/Merge/Move) |
| C-07 | Collaborates_with resolves | PASS | Phase 5 CHECK 2 flags UNRESOLVED entries; gate requires zero before PASS |
| C-08 | Perspective diversity | PASS | pm (product) + architect (technical) + inertia-advocate (inertia) + domain-specialist (domain) = 4 categories |
| C-09 | Scope gradient | PASS | Phase 3 SCOPE AUDIT gates on ≥ 2 distinct scope values; CHECK 3 confirms at delivery |
| C-10 | Inertia domain-grounded | PASS | Phase 4 frame requires Q1 (named current system) and Q2 (migration cost) from Phase 2 verbatim; Phase 2 uses domain-extracted bucket terms |
| C-11 | Vocabulary-forced-field | PASS | Phase 1 produces labeled vocabulary; Phase 4 exit condition: "every expertise.relevance references a Phase 1 vocabulary term"; Phase 5 CHECK 4 gates on zero [NO VOCAB TERM] entries |
| C-12 | Inertia pre-characterization | PASS | Phase 2 answers Q1/Q2/Q3 before writing; verify Q1 "names Q1 current system", Q2 "references Q2 migration cost", Q3 "references Q3 user habit" — all 3 dimensions referenced |
| C-13 | Registry summary table | PASS | Phase 5 CHECK 1 requires registry table (Role/Frame/Scope/Collaborates With) before delivery |
| C-14 | Scope-gradient-enforcement | PASS | Phase 3 SCOPE AUDIT: if only 1 scope value, revise 1–2 roles and re-confirm; structural gate, not instruction |
| C-15 | Verification-gate-phase | PASS | "DELIVERY IS BLOCKED" Phase 5 gate bundles all 4 structural checks; each must declare PASS in sequence |
| C-16 | Vocabulary-linked inertia Q&A | PASS | Phase 2 requires bucket-matched vocab annotations; inertia verify questions explicitly reference Q-domain vocab terms; C-11 and C-12 wired through bucket structure |
| C-17 | Pre-write scope audit | PASS | Phase 3 SCOPE AUDIT fires before Phase 4 writing; "Do not write any role file until scope audit passes" |
| C-18 | Vocabulary check in verification gate | PASS | Phase 5 CHECK 4 explicitly gates vocabulary coverage; gate cannot PASS with any [NO VOCAB TERM] entry |
| C-19 | Inertia frame Q-slot template | PASS | Phase 4 inertia-advocate: `orientation.frame` template contains named placeholders `[Q1 current system]` and `[Q2 migration cost]`; "Insert Phase 2 Q1 and Q2 answers verbatim into the brackets" — named slots, not soft instruction |
| C-20 | Q-domain-aligned vocabulary distribution | PASS | Phase 1 bucket structure (Current-System / Migration-Cost / User-Habit); Phase 2 exit: "Q1 term drawn from Current-System Terms; Q2 drawn from Migration-Cost Terms; Q3 drawn from User-Habit Terms; no cross-bucket reuse" — cross-bucket selection fails Phase 2 gate |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 12/12

```
composite = (5/5 * 60) + (3/3 * 30) + (12/12 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

---

### V-02: Post-Answer Domain-Alignment Audit Table

**Axis**: Post-answer domain-alignment audit table at Phase 2 exit (C-20 single axis, complementary angle)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | PASS | Same 5-field template structure as V-01 |
| C-02 | Inertia-advocate present | PASS | Phase 4 specifies inertia-advocate; "Q1 vocab term from the domain-alignment table must appear in the frame text" |
| C-03 | Correct output path | PASS | `.roles/{area}/` in opening |
| C-04 | Domain specificity | PASS | expertise.relevance requires a Phase 1 vocabulary term; vocabulary is input-derived |
| C-05 | Minimum 3 roles | PASS | pm, architect, inertia-advocate, domain-specialist ≥ 3 |
| C-06 | Lens actionability | PASS | Same verify/simplify enforcement as V-01 |
| C-07 | Collaborates_with resolves | PASS | Phase 5 CHECK 2 |
| C-08 | Perspective diversity | PASS | 4 perspective categories present |
| C-09 | Scope gradient | PASS | Phase 3 SCOPE AUDIT with structural revision gate |
| C-10 | Inertia domain-grounded | PASS | Frame requires Q1/Q2 verbatim; Phase 2 Q-domain descriptions anchor to named current system and cost type |
| C-11 | Vocabulary-forced-field | PASS | Phase 1 vocabulary; Phase 4 exit + CHECK 4 gate |
| C-12 | Inertia pre-characterization | PASS | Phase 2 Q1/Q2/Q3 with verify questions using domain-alignment table terms |
| C-13 | Registry summary table | PASS | Phase 5 CHECK 1 |
| C-14 | Scope-gradient-enforcement | PASS | Phase 3 SCOPE AUDIT structural gate |
| C-15 | Verification-gate-phase | PASS | "DELIVERY IS BLOCKED" Phase 5 gate |
| C-16 | Vocabulary-linked inertia Q&A | PASS | Phase 2 vocab annotations per answer; domain-alignment table validates; inertia verify questions use domain-alignment table terms |
| C-17 | Pre-write scope audit | PASS | Phase 3 SCOPE AUDIT precedes Phase 4 writing; "Do not write any role file until scope audit passes" |
| C-18 | Vocabulary check in verification gate | PASS | Phase 5 CHECK 4 vocabulary coverage in the named blocking gate |
| C-19 | Inertia frame Q-slot template | PASS | Phase 4 frame template: "Challenge every proposal with evidence that [Q1 current system] remains sufficient given [Q2 migration cost]"; named placeholders with verbatim fill instruction |
| C-20 | Q-domain-aligned vocabulary distribution | PASS | Phase 2 Q-descriptions constrain domain per answer (Q1: "current-system entity", Q2: "cost category/risk type", Q3: "workflow/behavior"); domain-alignment audit table gates with YES/NO per row; gate condition: all three YES; any NO triggers rewrite with correct-domain term |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 12/12

```
composite = (5/5 * 60) + (3/3 * 30) + (12/12 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

---

### V-03: Dedicated Inertia Frame Fill Phase

**Axis**: Pre-write frame fill as standalone Phase 3 (C-19 upgrade, single axis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | PASS | All 5 fields in template |
| C-02 | Inertia-advocate present | PASS | Phase 5 inertia-advocate; frame references current system and migration cost |
| C-03 | Correct output path | PASS | `.roles/{area}/` |
| C-04 | Domain specificity | PASS | expertise.relevance requires Phase 1 term |
| C-05 | Minimum 3 roles | PASS | pm, architect, inertia-advocate, domain-specialist |
| C-06 | Lens actionability | PASS | Verify/simplify enforcement in template |
| C-07 | Collaborates_with resolves | PASS | Phase 6 CHECK 2 |
| C-08 | Perspective diversity | PASS | 4 categories |
| C-09 | Scope gradient | PASS | Phase 4 SCOPE AUDIT gates ≥ 2 distinct values |
| C-10 | Inertia domain-grounded | PASS | Phase 3 frame fill uses Q1/Q2 verbatim from Phase 2 |
| C-11 | Vocabulary-forced-field | PASS | Phase 1 vocabulary; Phase 5 exit + CHECK 4 gate |
| C-12 | Inertia pre-characterization | PASS | Phase 2 Q1/Q2/Q3; verify questions reference each dimension |
| C-13 | Registry summary table | PASS | Phase 6 CHECK 1 |
| C-14 | Scope-gradient-enforcement | PASS | Phase 4 SCOPE AUDIT structural gate |
| C-15 | Verification-gate-phase | PASS | "DELIVERY IS BLOCKED" Phase 6 gate |
| C-16 | Vocabulary-linked inertia Q&A | PASS | Phase 2 vocab annotations; Phase 5 verify questions reference Phase 2 vocab terms |
| C-17 | Pre-write scope audit | PASS | Phase 4 SCOPE AUDIT before Phase 5 writing; "Do not write any role file until scope audit passes" |
| C-18 | Vocabulary check in verification gate | PASS | Phase 6 CHECK 4 explicitly in blocking gate |
| C-19 | Inertia frame Q-slot template | PASS | Phase 3 is a dedicated INERTIA FRAME FILL phase; template with named `[Q1: current system name]` and `[Q2: migration cost description]` placeholders; completed sentence recorded as named artifact; Phase 5 copies verbatim — no slot instruction to drift |
| C-20 | Q-domain-aligned vocabulary distribution | PARTIAL | Phase 1 uses Systems/Patterns/Key terms buckets (not Q-domain buckets); Phase 2 Q-wording guides correct-domain selection ("What existing system..." / "What concrete cost..." / "What observable workflow...") but no structural bucket constraint or alignment audit table enforces per-Q domain. Same term could satisfy all three answers; wrong-domain selection passes Phase 2 exit condition if it has a `[vocab]` annotation |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 11 PASS + 1 PARTIAL (C-20) = 11.5/12

```
composite = (5/5 * 60) + (3/3 * 30) + (11.5/12 * 10)
          = 60 + 30 + 9.58
          = 99.58
```

**Score: 99.6 / 100 — GOLDEN**

---

### V-04: Three-Bucket + Dedicated Frame Fill

**Axes**: V-01 buckets (C-20) + V-03 frame fill (C-19)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | PASS | All 5 fields in template |
| C-02 | Inertia-advocate present | PASS | Phase 5 inertia-advocate with bucket-sourced vocab frame |
| C-03 | Correct output path | PASS | `.roles/{area}/` |
| C-04 | Domain specificity | PASS | expertise.relevance requires Phase 1 term from any bucket |
| C-05 | Minimum 3 roles | PASS | pm, architect, inertia-advocate, domain-specialist |
| C-06 | Lens actionability | PASS | Verify/simplify enforcement |
| C-07 | Collaborates_with resolves | PASS | Phase 6 CHECK 2 |
| C-08 | Perspective diversity | PASS | 4 categories |
| C-09 | Scope gradient | PASS | Phase 4 SCOPE AUDIT |
| C-10 | Inertia domain-grounded | PASS | Phase 3 frame fill uses Q1/Q2 verbatim; Q1/Q2 are bucket-sourced |
| C-11 | Vocabulary-forced-field | PASS | Phase 1 three buckets; Phase 5 exit + Phase 6 CHECK 4 |
| C-12 | Inertia pre-characterization | PASS | Phase 2 Q1/Q2/Q3 with bucket-specified terms; verify questions reference Q-domain vocab |
| C-13 | Registry summary table | PASS | Phase 6 CHECK 1 |
| C-14 | Scope-gradient-enforcement | PASS | Phase 4 SCOPE AUDIT structural gate |
| C-15 | Verification-gate-phase | PASS | "DELIVERY IS BLOCKED" Phase 6 gate with 4 ordered checks |
| C-16 | Vocabulary-linked inertia Q&A | PASS | Bucket-constrained Phase 2 vocab annotations; inertia verify questions reference Q-domain bucket terms |
| C-17 | Pre-write scope audit | PASS | Phase 4 SCOPE AUDIT precedes Phase 5 writing |
| C-18 | Vocabulary check in verification gate | PASS | Phase 6 CHECK 4 in blocking gate; "Fix defects found in earlier checks before proceeding" |
| C-19 | Inertia frame Q-slot template | PASS | Phase 3 dedicated INERTIA FRAME FILL with named `[Q1: current system name]` / `[Q2: migration cost description]` placeholders; Phase 5 "copy the Phase 3 filled sentence verbatim" |
| C-20 | Q-domain-aligned vocabulary distribution | PASS | Phase 1 three-bucket extraction (Current-System / Migration-Cost / User-Habit); Phase 2 exit: each answer must draw from its named bucket; no cross-bucket reuse permitted; structural gate prevents wrong-domain selection |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 12/12

```
composite = (5/5 * 60) + (3/3 * 30) + (12/12 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

---

### V-05: Full Synthesis

**Axes**: Buckets + alignment audit table + frame fill + phase entry/exit conditions + R3 excellence patterns

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | PASS | All 5 fields in template; vocabulary constraint ties relevance to domain input |
| C-02 | Inertia-advocate present | PASS | Phase 5 inertia-advocate with explicit orientation.frame copied from Phase 3 |
| C-03 | Correct output path | PASS | `.roles/{area}/` |
| C-04 | Domain specificity | PASS | expertise.relevance requires Phase 1 term from any bucket; "if a role's relevance cannot be written using a Phase 1 term, the role is too generic — rename it" |
| C-05 | Minimum 3 roles | PASS | pm, architect, inertia-advocate, domain-specialist |
| C-06 | Lens actionability | PASS | Verify/simplify format; generic verify question explicitly fails ("A generic question fails even if 2 of 3 are specific") |
| C-07 | Collaborates_with resolves | PASS | Phase 6 CHECK 2 |
| C-08 | Perspective diversity | PASS | 4 perspective categories |
| C-09 | Scope gradient | PASS | Phase 4 SCOPE AUDIT with 4-step confirmation procedure |
| C-10 | Inertia domain-grounded | PASS | Phase 3 frame fill; Phase 2 bucket-sourced terms name specific system/cost |
| C-11 | Vocabulary-forced-field | PASS | Phase 1 buckets; Phase 2 annotations + alignment table; Phase 5 exit condition; Phase 6 CHECK 4 — four enforcement layers |
| C-12 | Inertia pre-characterization | PASS | Phase 2 Q1/Q2/Q3; Phase 5 inertia verify questions reference each Q-domain dimension; "generic question fails even if 2 of 3 specific" |
| C-13 | Registry summary table | PASS | Phase 6 CHECK 1 |
| C-14 | Scope-gradient-enforcement | PASS | Phase 4 SCOPE AUDIT structural gate with "re-confirm distinct count ≥ 2" step |
| C-15 | Verification-gate-phase | PASS | "DELIVERY IS BLOCKED" Phase 6; explicit entry/exit conditions; "fix defects found in earlier checks before proceeding" |
| C-16 | Vocabulary-linked inertia Q&A | PASS | Phase 2 bucket constraints and domain-alignment table; Phase 5 verify questions explicitly Q-domain-matched; all three enforcement layers interdependent |
| C-17 | Pre-write scope audit | PASS | Phase 4 SCOPE AUDIT; explicit "Do not write any role file until scope audit passes"; Phase 5 entry requires Phase 4 complete |
| C-18 | Vocabulary check in verification gate | PASS | Phase 6 CHECK 4 in blocking gate; "state which term was added and from which bucket" — traces back to Phase 1 source |
| C-19 | Inertia frame Q-slot template | PASS | Phase 3 dedicated INERTIA FRAME FILL; named placeholders `[Q1: current system name]` and `[Q2: migration cost description]`; "Do not rewrite it. Do not paraphrase it" injunction in Phase 5 |
| C-20 | Q-domain-aligned vocabulary distribution | PASS | Double-layer: Phase 1 three-bucket extraction (prevents wrong-domain selection at source) + Phase 2 domain-alignment audit table (gated YES/NO per row catches miscategorized or inferred terms); gate condition: all YES before proceeding |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 12/12

```
composite = (5/5 * 60) + (3/3 * 30) + (12/12 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-01 Three-bucket Phase 1 | 5/5 | 3/3 | 12/12 | **100** | YES |
| 1 | V-02 Domain-alignment audit table | 5/5 | 3/3 | 12/12 | **100** | YES |
| 1 | V-04 Buckets + frame fill | 5/5 | 3/3 | 12/12 | **100** | YES |
| 1 | V-05 Full synthesis | 5/5 | 3/3 | 12/12 | **100** | YES |
| 5 | V-03 Dedicated frame fill | 5/5 | 3/3 | 11.5/12 | **99.6** | YES |

### The single discriminator: C-20

V-03 scores 99.6 rather than 100 because Phase 1 uses generic vocabulary categories (Systems/Patterns/Key terms) that do not pre-sort by Q-dimension. Phase 2 Q-wording guides toward correct domain but the exit condition only requires a `[vocab]` annotation — not that the annotation draws from a Q-matched domain. A model could satisfy V-03's Phase 2 exit condition by using the same term for Q1 and Q3, or using a cost term for Q1. V-01/V-02/V-04/V-05 all have a structural gate that makes this fail explicitly.

**C-20 compliance is entirely determined by whether Phase 2 has a structural Q-domain constraint**, not by Q-wording guidance alone.

---

## Within the 100 Cluster: Structural Risk Differences

All four top variations score 100, but differ in robustness under model compression:

| Variation | C-20 mechanism | C-19 mechanism | Layers | Structural risk |
|-----------|----------------|----------------|--------|-----------------|
| V-05 | Buckets (prevent) + audit table (catch) | Dedicated Phase 3 + "no rewrite" injunction | 2+1 | Lowest |
| V-04 | Buckets only | Dedicated Phase 3 verbatim copy | 1+1 | Low |
| V-01 | Buckets only | Named placeholders in write phase | 1+inline | Moderate |
| V-02 | Audit table only | Named placeholders in write phase | 1+inline | Moderate |

V-05 is the structurally strongest: it combines both C-20 prevention mechanisms (bucket pre-sorting AND post-answer audit) so that a miscategorized inferred term in Phase 1 would be caught by the Phase 2 audit table even if bucket assignment was imperfect. V-04 closes C-19 more strongly than V-01/V-02 by producing the frame sentence as a pre-write artifact — but uses only buckets for C-20, not the audit table.

---

## Excellence Signals from V-05

Two patterns from V-05 are not yet rubric criteria:

**1. Double-layer enforcement for a single criterion at different execution points**

V-05 enforces C-20 at Phase 1 (bucket extraction: prevents wrong-domain selection by constraining the vocabulary menu by Q-dimension) AND at Phase 2 (domain-alignment audit table: catches any miscategorized term that passed bucket extraction). These are complementary failure modes — bucket misassignment is a Phase 1 failure; audit table catches it at Phase 2 exit. When a criterion has two orthogonal failure modes, two mechanisms at different execution points produce structural resilience that neither mechanism achieves alone.

**2. Q-domain vocab propagation into inertia verify questions**

V-05 Phase 5 wires Q-domain alignment all the way through to the inertia-advocate's lens output: verify question 1 must use Q1's vocab term (from Current-System Terms), question 2 must use Q2's term (from Migration-Cost Terms), question 3 must use Q3's term (from User-Habit Terms). A "generic question fails even if 2 of 3 are specific." C-16 requires each Q&A answer to reference a Phase 1 term — but doesn't require that the verify questions in the output use the Q-matched term. V-05 closes this: Phase 2 domain alignment propagates forward into the lens, not just into the inertia frame.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Double-layer enforcement for a single criterion at different execution points: Phase 1 bucket extraction prevents wrong-domain selection; Phase 2 domain-alignment audit table catches miscategorized terms that passed extraction. Two orthogonal mechanisms covering two distinct failure modes — bucket misassignment and post-selection drift — produce structural resilience neither achieves alone.", "Q-domain vocab propagation into inertia verify questions: each verify question must use the Q-domain-matching vocab term specifically (Q1 term in question 1, Q2 term in question 2, Q3 term in question 3). C-16 wires vocab to Phase 2 Q&A answers; this pattern extends Q-domain alignment forward into the output lens, closing the gap between Phase 2 annotation and Phase 5 delivery."]}
```
