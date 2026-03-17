## Quest Score — `/discover:causal` Round 6 (Rubric v6)

---

### Scoring Method

| Band | Pts | Formula |
|------|-----|---------|
| Essential (5 criteria) | 60 | 12 pts each |
| Recommended (3 criteria) | 30 | 10 pts each |
| Aspirational (13 criteria) | 10 | pass_count / 13 × 10 |
| **Total** | **100** | |

Golden threshold: all 5 essential pass AND composite ≥ 80.

---

### V-01: Inline Chain Observability Tally

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Mechanism pathway named | **PASS** | Section 4 requires hop-by-hop causal chain X → A → Y with two-hop minimum |
| C-02 | Falsification condition present | **PASS** | F-NN table in Section 1; Section 5 per-hop challenges produce observable conditions |
| C-03 | Inertia check performed | **PASS** | Section 3 explicitly asks and answers status-quo question with baseline rate |
| C-04 | Causal claim is scoped/testable | **PASS** | Section 6 scoped claim template narrows to condition/population/precondition |
| C-05 | AMEND directive produced | **PASS** | Section 6 AMEND block with 4 conditional slots and at minimum Narrow + Mechanism |
| R-01 | Context-specific evidence | **PASS** | Section 2 requires evidence entry OR "None found" with mandatory AMEND slot |
| R-02 | Alternatives/confounders named | **PASS** | Section 5 requires "Alternative at this hop" per hop and Confounder 1 |
| R-03 | Two-hop mechanism chain | **PASS** | "Two hops minimum" explicit in Section 4 |
| A-01 | Mechanism strength qualified | **PASS** | Preliminary in Section 4 (before adversarial), final in Section 5 |
| A-02 | Inertia baseline quantified | **PASS** | Section 3 "Baseline rate: Estimate or bound … Or: 'Unknown.'" |
| A-03 | Adversarial section separated | **PASS** | Section 5 structurally separate from Section 4; gate enforces no adversarial content in S4 |
| A-04 | All classification discrete labels | **PASS** | Observability, confidence, testability, inertia severity, evidence quality all labeled |
| A-05 | Evidence precedes mechanism | **PASS** | Section 2 (evidence + testability refinement) gated before Section 4 |
| A-06 | Dual mechanism strength | **PASS** | Preliminary S4 / final S5; strength_changed flag in frontmatter |
| A-07 | Falsification confidence per row | **PASS** | F-NN table in S1 has High/Medium/Low per row; S5 hop challenges also have per-hop confidence |
| A-08 | Hops cross-reference falsification | **PASS** | Every hop in S4 carries "Falsification connection: [F-NN or I-NN ID]" |
| A-09 | Structural gate checklists | **PASS** | Three binary gate checklists: S1 Gate, S2 Gate, S4 Gate |
| A-10 | Hop observability labeled | **PASS** | Every hop in S4 carries Observable/Partial/Opaque + rationale |
| A-11 | Falsification testability per condition | **PASS** | S1 Unknown at genesis; S2 refinement table gives final Easy/Hard/Unknown per row |
| A-12 | Aggregate observability + AMEND routing | **PASS** | S4 inline tally (counts + pattern label + rationale) with S4 Gate item "AMEND Observability slot flagged as mandatory if Mixed or PredominantlyOpaque" |
| A-13 | Testability refinement yield tracked | **PASS** | S2 yields testability_refined_count + testability_residual_unknown_count + residual IDs; S2 Gate enforces both counts declared; conditional AMEND Testability slot |

**Essential: 5/5 (60 pts) | Recommended: 3/3 (30 pts) | Aspirational: 13/13 (10 pts)**
**Composite: 100.0 | Golden: YES**

---

### V-02: AUDITOR Role

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Mechanism pathway named | **PASS** | ANALYST role maps causal chain with two-hop minimum |
| C-02 | Falsification condition present | **PASS** | FRAMER F-NN table; SKEPTIC final falsification table with per-row confidence |
| C-03 | Inertia check performed | **PASS** | FRAMER Step 5 inertia check with severity label and baseline rate |
| C-04 | Causal claim is scoped/testable | **PASS** | FRAMER (closing) scoped claim template with condition/population/precondition |
| C-05 | AMEND directive produced | **PASS** | FRAMER (closing) AMEND block using AUDITOR's routing declaration |
| R-01 | Context-specific evidence | **PASS** | FRAMER Step 3 requires evidence OR "None found" with mandatory slot |
| R-02 | Alternatives/confounders named | **PASS** | SKEPTIC requires "Alternative at this hop" per hop and Confounder 1 |
| R-03 | Two-hop mechanism chain | **PASS** | "Two hops minimum" in ANALYST section |
| A-01 | Mechanism strength qualified | **PASS** | ANALYST preliminary; SKEPTIC final with "State whether changed from ANALYST preliminary" |
| A-02 | Inertia baseline quantified | **PASS** | FRAMER Step 5 "Baseline rate: Estimate or bound. Or: 'Unknown.'" |
| A-03 | Adversarial section separated | **PASS** | SKEPTIC is a named role structurally separate from ANALYST |
| A-04 | All classification discrete labels | **PASS** | All classification outputs across all roles use discrete label sets |
| A-05 | Evidence precedes mechanism | **PASS** | FRAMER (opening) includes evidence before ANALYST runs |
| A-06 | Dual mechanism strength | **PASS** | ANALYST preliminary before SKEPTIC challenge; SKEPTIC final after |
| A-07 | Falsification confidence per row | **PASS** | SKEPTIC's final falsification table carries High/Med/Low per row; testability column from FRAMER unchanged |
| A-08 | Hops cross-reference falsification | **PASS** | ANALYST hops carry "Falsification connection: [FRAMER F-NN or I-NN ID]" |
| A-09 | Structural gate checklists | **PASS** | Three role gates: FRAMER Gate, ANALYST Gate, SKEPTIC Gate with binary checklists |
| A-10 | Hop observability labeled | **PASS** | ANALYST hops each carry Observable/Partial/Opaque + rationale |
| A-11 | Falsification testability per condition | **PASS** | FRAMER testability-only column (no confidence); refinement table gives final per-row label |
| A-12 | Aggregate observability + AMEND routing | **PASS** | AUDITOR Diagnostic 1: per-hop table, tally, pattern label, "AMEND Observability slot: Required/Not required"; AMEND routing table row 1 |
| A-13 | Testability refinement yield tracked | **PASS** | FRAMER yield fields (refined_count + residual_count + IDs); AUDITOR Diagnostic 2 reproduces yield with quality label; AMEND routing table row 2 |

**Essential: 5/5 (60 pts) | Recommended: 3/3 (30 pts) | Aspirational: 13/13 (10 pts)**
**Composite: 100.0 | Golden: YES**

---

### V-03: Inertia-Inclusive Aggregates

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Mechanism pathway named | **PASS** | Section 4 mechanism chain with two-hop minimum |
| C-02 | Falsification condition present | **PASS** | F-NN pool (S1) and I-NN pool (S2); falsification conditions in both |
| C-03 | Inertia check performed | **PASS** | Section 2 inertia check with severity, baseline rate, and inertia observability |
| C-04 | Causal claim is scoped/testable | **PASS** | Section 6 scoped claim template |
| C-05 | AMEND directive produced | **PASS** | Section 6 AMEND with inertia and observability conditional slots |
| R-01 | Context-specific evidence | **PASS** | Section 3 evidence required OR "None found" |
| R-02 | Alternatives/confounders named | **PASS** | Section 5 per-hop alternatives and Confounder 1 |
| R-03 | Two-hop mechanism chain | **PASS** | Explicit two-hop minimum in Section 4 |
| A-01 | Mechanism strength qualified | **PASS** | Section 4 preliminary / Section 5 final |
| A-02 | Inertia baseline quantified | **PASS** | Section 2 "Baseline rate: Estimate or bound. Or: 'Unknown.'" |
| A-03 | Adversarial section separated | **PASS** | Section 5 structurally separate with gate enforcing no adversarial in S4 |
| A-04 | All classification discrete labels | **PASS** | Both pools, inertia observability, evidence quality — all discrete labels |
| A-05 | Evidence precedes mechanism | **PASS** | Section 3 (evidence + refinement) gated before Section 4 |
| A-06 | Dual mechanism strength | **PASS** | Section 4 preliminary / Section 5 final; strength_changed in frontmatter |
| A-07 | Falsification confidence per row | **PASS** | F-NN table (S1) and I-NN table (S2) both carry High/Medium/Low per row |
| A-08 | Hops cross-reference falsification | **PASS** | S4 hops carry "Falsification connection: [F-NN or I-NN ID from Sections 1-2]" — works across both pools |
| A-09 | Structural gate checklists | **PASS** | Four binary gate checklists: S1, S2, S3, S4 (richest gate count of R6 sectional variations) |
| A-10 | Hop observability labeled | **PASS** | S4 mechanism hops + S2 inertia observability label (Observable/Partial/Opaque) |
| A-11 | Falsification testability per condition | **PASS** | Both F-NN (S1) and I-NN (S2) start Unknown; S3 refinement table gives final per condition for both pools |
| A-12 | Aggregate observability + AMEND routing | **PASS** | S4 "Chain observability aggregate (mechanism hops + inertia)" combined tally, inertia contribution note, pattern label, conditional AMEND note; S4 Gate includes mandatory flag item |
| A-13 | Testability refinement yield tracked | **PASS** | S3 yield with refined_count + residual_unknown_count + pool breakdown (F-NN residual / I-NN residual); pool asymmetry noted as finding; conditional AMEND slot |

**Essential: 5/5 (60 pts) | Recommended: 3/3 (30 pts) | Aspirational: 13/13 (10 pts)**
**Composite: 100.0 | Golden: YES**

---

### V-04: AMEND Routing Matrix

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Mechanism pathway named | **PASS** | Section 4 mechanism chain with hop-by-hop decomposition |
| C-02 | Falsification condition present | **PASS** | Section 1 F-NN table; Section 5 per-hop challenge conditions |
| C-03 | Inertia check performed | **PASS** | Section 2 inertia check with severity and baseline rate |
| C-04 | Causal claim is scoped/testable | **PASS** | Section 6 scoped claim with condition/population/precondition |
| C-05 | AMEND directive produced | **PASS** | Section 7 AMEND block generated from routing matrix results; "Include only triggered slots" |
| R-01 | Context-specific evidence | **PASS** | Section 3 evidence OR "None found"; Row 4 of matrix notes it will trigger Evidence slot |
| R-02 | Alternatives/confounders named | **PASS** | Section 5 per-hop alternatives and Confounder 1 |
| R-03 | Two-hop mechanism chain | **PASS** | Two-hop minimum in Section 4 |
| A-01 | Mechanism strength qualified | **PASS** | Section 4 preliminary / Section 5 final with discrete label |
| A-02 | Inertia baseline quantified | **PASS** | Section 2 "Baseline rate: Estimate or bound. Or: 'Unknown.'" |
| A-03 | Adversarial section separated | **PASS** | Section 5 structurally separate from Section 4 |
| A-04 | All classification discrete labels | **PASS** | All fields use discrete label sets throughout |
| A-05 | Evidence precedes mechanism | **PASS** | Section 3 (evidence + refinement) gated before Section 4 |
| A-06 | Dual mechanism strength | **PASS** | Section 4 preliminary / Section 5 final; strength_changed in frontmatter |
| A-07 | Falsification confidence per row | **PASS** | Section 1 F-NN table has High/Medium/Low per row; Section 5 hop challenges have per-hop confidence |
| A-08 | Hops cross-reference falsification | **PASS** | S4 hops carry "Falsification connection: [F-NN or I-NN ID from Sections 1-2]" |
| A-09 | Structural gate checklists | **PASS** | S3 Gate + S4 Gate (binary checklists); routing matrix in S7 functions as additional explicit gate |
| A-10 | Hop observability labeled | **PASS** | S4 hops each carry Observable/Partial/Opaque + rationale |
| A-11 | Falsification testability per condition | **PASS** | S1 conditions start Unknown; S3 refinement table gives Easy/Hard/Unknown per row |
| A-12 | Aggregate observability + AMEND routing | **PASS** | S4 inline tally + pattern label carried to S7 routing matrix Row 1; routing matrix makes trigger binary and auditable |
| A-13 | Testability refinement yield tracked | **PASS** | S3 yield: refined_count + residual_unknown_count + IDs; "Carry to S7 routing matrix row 2"; S7 Row 2 triggers AMEND Testability slot if count > 0 |

**Essential: 5/5 (60 pts) | Recommended: 3/3 (30 pts) | Aspirational: 13/13 (10 pts)**
**Composite: 100.0 | Golden: YES**

---

### V-05: Dual-Diagnostic Yield Section

| ID | Criterion | Result | Evidence note |
|----|-----------|--------|---------------|
| C-01 | Mechanism pathway named | **PASS** | Section C mechanism chain with two-hop minimum |
| C-02 | Falsification condition present | **PASS** | Section A1 F-NN table; Section E per-hop challenges |
| C-03 | Inertia check performed | **PASS** | Section A3 inertia check with severity and baseline rate |
| C-04 | Causal claim is scoped/testable | **PASS** | Section F scoped claim template |
| C-05 | AMEND directive produced | **PASS** | Section F AMEND using Section D triggers; double-blind gap IDs included if present |
| R-01 | Context-specific evidence | **PASS** | Section A2 evidence OR "None found" |
| R-02 | Alternatives/confounders named | **PASS** | Section E per-hop alternatives and Confounder 1 |
| R-03 | Two-hop mechanism chain | **PASS** | Two-hop minimum in Section C |
| A-01 | Mechanism strength qualified | **PASS** | Section C preliminary (before D and E) / Section E final |
| A-02 | Inertia baseline quantified | **PASS** | Section A3 "Baseline rate: Estimate or bound. Or: 'Unknown.'" |
| A-03 | Adversarial section separated | **PASS** | Section E is structurally separate from Section C; Section D (Diagnostic Yield) intervenes between them |
| A-04 | All classification discrete labels | **PASS** | All sections use fixed discrete sets; D1 yield assessment, D2 observability labels all discrete |
| A-05 | Evidence precedes mechanism | **PASS** | Section A (evidence in A2) + Section B (testability refinement) both gate before Section C |
| A-06 | Dual mechanism strength | **PASS** | Section C preliminary / Section E final; Section D intervenes between them, enriching the rating pair |
| A-07 | Falsification confidence per row | **PASS** | Section A1 F-NN table + A3 I-01 both carry High/Medium/Low per row |
| A-08 | Hops cross-reference falsification | **PASS** | Section C hops carry "Falsification connection: [F-NN or I-NN ID from Section A]"; D2 table also carries this column |
| A-09 | Structural gate checklists | **PASS** | Four binary gate checklists: Section A Gate, B Gate, C Gate, D Gate |
| A-10 | Hop observability labeled | **PASS** | Section C hops carry Observable/Partial/Opaque + rationale; D2 carries these forward |
| A-11 | Falsification testability per condition | **PASS** | A1/A3 start Unknown; Section B gives Easy/Hard/Unknown per row; D1 shows before/after columns |
| A-12 | Aggregate observability + AMEND routing | **PASS** | D2 table with per-hop observability + tally + pattern label + "AMEND Observability triggered: Yes/No"; D3 joint gap analysis uses D2 per-hop labels |
| A-13 | Testability refinement yield tracked | **PASS** | Section B yield (refined_count + residual_count + IDs); D1 before/after table per condition with Refined/Residual Unknown status; "AMEND Testability triggered: Yes/No"; D3 double-blind gap cross-references both D1 and D2 |

**Essential: 5/5 (60 pts) | Recommended: 3/3 (30 pts) | Aspirational: 13/13 (10 pts)**
**Composite: 100.0 | Golden: YES**

---

### Round 6 Summary Table

| Variation | Essential | Rec | Asp (13/13) | Composite | Golden |
|-----------|-----------|-----|-------------|-----------|--------|
| V-01 Inline tally | 5/5 | 3/3 | 13/13 | **100.0** | YES |
| V-02 AUDITOR role | 5/5 | 3/3 | 13/13 | **100.0** | YES |
| V-03 Inertia-inclusive | 5/5 | 3/3 | 13/13 | **100.0** | YES |
| V-04 Routing matrix | 5/5 | 3/3 | 13/13 | **100.0** | YES |
| V-05 Dual-diagnostic yield | 5/5 | 3/3 | 13/13 | **100.0** | YES |

All five variations golden. R6 target achieved.

---

### Excellence Signals

All variations scored 100.0; no differential. The new patterns in R6 that completed the A-12/A-13 coverage are:

**From V-01 (compact A-12):**
The inline tally embedded at the end of the mechanism section — rather than in a standalone summary table — integrates aggregate computation directly into the analytical workflow. The S4 Gate checklist item "AMEND Observability slot flagged as mandatory if Mixed or PredominantlyOpaque" enforces the conditional trigger without a separate section. This shows the gate item is sufficient to convert a compact inline form into a reliable routing mechanism.

**From V-02 (AUDITOR-mediated routing):**
Assigning diagnostic synthesis to a named fourth role (AUDITOR) that sees both FRAMER and ANALYST output simultaneously produces the most explicit AMEND routing declaration of all R6 variations. The AUDITOR routing table separates the diagnostic evaluation act from AMEND construction, making both auditable. This is the only variation where the routing decision is made by a role with no stake in the mechanism or adversarial work — a structural neutrality that reduces confirmation bias.

**From V-03 (inertia in aggregate):**
The "inertia observability" label as a first-class participant in the chain aggregate expands A-12 beyond mechanism hops. It surfaces the structural question: can we actually observe whether Y occurs without X? This is a distinct failure mode (counterfactual unobservability) not captured by mechanism-hop observability alone. The F-NN / I-NN pool asymmetry finding in A-13 is the first explicit design that expects inertia conditions to be disproportionately Unknown-testability — seeding a testable hypothesis for R7.

**From V-04 (routing matrix):**
The 4-row decision table in Section 7 makes every AMEND trigger binary, explicit, and co-located. The "Carry pattern to S7 row 1" and "Carry residual_count to S7 row 2" links between earlier sections and the matrix create a traceable provenance chain. The matrix eliminates prose-conditional AMEND by converting all trigger logic into observable cell values — the strongest structural guarantee of A-12/A-13 routing in R6.

**From V-05 (double-blind gap — top structural innovation):**
Section D's D3 joint gap analysis introduces a new finding type that is not surfaced by either A-12 or A-13 alone: the **double-blind gap** (Opaque hop AND Unknown testability on the same condition). This is the first joint diagnostic in the research program. Additionally, Section D is positioned *between* mechanism (C) and adversarial (E), converting diagnostic findings into Section E priority targets before challenge begins — a structural ordering that makes adversarial effort proportional to gap severity. The before/after table in D1 treats testability refinement as a first-class analytical output rather than a bookkeeping field.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["double-blind gap joint diagnostic (V-05 D3): Opaque hop AND Unknown testability on same condition — neither A-12 nor A-13 surfaces this co-occurrence individually", "diagnostic yield section (V-05 D) positioned between mechanism and adversarial converts A-12+A-13 findings into Section E priority targets before challenge begins", "AUDITOR role (V-02) as structurally neutral diagnostic synthesizer with access to all prior roles simultaneously — produces routing declaration before FRAMER constructs AMEND", "inertia observability label as first-class participant in chain aggregate (V-03) — surfaces counterfactual unobservability distinct from mechanism-hop opacity", "4-row AMEND routing matrix (V-04) making all slot triggers binary, co-located, and traceable to diagnostic provenance"]}
```
