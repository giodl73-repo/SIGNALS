The golden file is empty — this is a fresh round with no prior artifact. I'll score the five variation templates directly from the design descriptions and the V-01 full template shown in the prompt.

---

# Quest Score — prove-prototype Round 7 (v7 rubric, 190 pts)

**Date**: 2026-03-15
**Rubric version**: v7 (added C-25, C-26)
**Scoring basis**: Template design enforceability — does the structural design compel each criterion?

---

## Point Weights

| Tier | Criteria | Pts/criterion | Total |
|------|----------|--------------|-------|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09, C-10, C-16–C-25 | 7 | 84 |
| Aspirational | C-26 | 6 | 6 |
| Excellence | C-11–C-15 | 2 | 10 |
| **Total** | | | **190** |

---

## V-01 — Five-Role, Multi-Role-Per-Container

**Axis**: Role sequence; DEFINE(FRAMER+CALIBRATOR), EXECUTE(BUILDER+RECORDER), EVALUATE(ANALYST)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** 12 | Phase 1 FRAMER: "Hypothesis is the first substantive element of your output" — enforced by role header |
| C-02 | **PASS** 12 | Phase 2 table: two exclusions minimum, validity rationale co-located in same row |
| C-03 | **PASS** 12 | Phase 3 precedes Phase 5; "criteria are frozen here — BUILDER may not modify them" |
| C-04 | **PASS** 12 | ANALYST role writes comparison (stated in ROLES table: "Comparison"); EXECUTE GATE carries observed vs. null |
| C-05 | **PASS** 12 | ANALYST role writes verdict (stated in ROLES table) |
| C-06 | **PASS** 10 | Phase 5 BUILDER: "state the minimality trade-off in the same block" |
| C-07 | **PASS** 10 | Phase 6 RECORDER: "Include at least one concrete data point per metric" |
| C-08 | **PASS** 10 | ANALYST role writes limits + next step |
| C-09 | **PASS** 7 | ANALYST explicitly listed as writing counter-evidence in ROLES table |
| C-10 | **PASS** 7 | Phase 5: "list all tools, inputs, and steps for replication"; completion line flags PARTIAL replication explicitly |
| C-16 | **PASS** 7 | ANALYST handles both affirmative and null counter-evidence cases (implied by role scope: "counter-evidence") |
| C-17 | **PASS** 7 | Phase 2 table: rationale in same row; Phase 1 confirmed/refuted in same labeled block |
| C-18 | **PASS** 7 | Role prohibitions enforce binary closure; ANALYST role written to produce disposition not silence |
| C-19 | **PASS** 7 | Every phase 1–6 has inline "Execute after Phase N completion line is present in your output" |
| C-20 | **PASS** 7 | Every phase has labeled PHASE N COMPLETE line with named outcome (seen in phases 1–6) |
| C-21 | **PARTIAL** 3.5 | Phases 1–6 fully gated; Phases 7–11 (EVALUATE) template not shown — trailing section gating unverified |
| C-22 | **PASS** 7 | Completion lines embed actual values: "hypothesis = [phrase]", "observed = [value]", "B-00 control = [value]" |
| C-23 | **PASS** 7 | ROLES table + inline role headers both carry explicit "Must Not Write" lists with named content types |
| C-24 | **PASS** 7 | Three structural containers: DEFINE, EXECUTE, EVALUATE — each maps to a distinct stage |
| C-25 | **PASS** 7 | DEFINE holds 2 roles, EXECUTE holds 2 roles; container scan (3 headers) ≠ role scan (5 block labels); orthogonal |
| C-26 | **PASS** 6 | Phase 4 CALIBRATOR establishes B-00 before any build; EXECUTE GATE COMPLETE: "B-00 control measured = [value vs. null prediction]" |
| C-11 | **FAIL** 0 | Template does not explicitly require failure mode identification |
| C-12 | **FAIL** 0 | Effect size not explicitly required |
| C-13–C-15 | **FAIL** 0 | Not addressed |

**V-01 Total: 60 + 30 + 86.5 + 0 = 176.5 / 190**

---

## V-02 — Table-Centric Format

**Axis**: Role labels as column values in tables; container scan reads `## LIFECYCLE: X`; role scan reads `Role` column across rows — orthogonal structural dimensions

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** 12 | Hypothesis is first table row in Define section |
| C-02 | **PASS** 12 | Scope table with exclusions and validity columns |
| C-03 | **PASS** 12 | Measurement table in Define precedes Execute section structurally |
| C-04 | **PASS** 12 | Results Table E-2 includes comparison column |
| C-05 | **PASS** 12 | Verdict row in evaluation table |
| C-06 | **PASS** 10 | Minimality row in Build table |
| C-07 | **PASS** 10 | Raw data row in Results table |
| C-08 | **PASS** 10 | Limitations and next-step rows in evaluation table |
| C-09 | **PASS** 7 | Counter-evidence row in evaluation table |
| C-10 | **PARTIAL** 3.5 | Tools/steps list possible in table cells but table format limits inline step enumeration; replication completeness harder to verify |
| C-16 | **PASS** 7 | Two-row disposition: affirmative row + null case row |
| C-17 | **PASS** 7 | Table format naturally co-locates rationale with anchor in same row |
| C-18 | **PASS** 7 | Table rows enforce binary: each section has affirmative row and null row |
| C-19 | **PARTIAL** 3.5 | Row ordering substitutes for inline gate markers but is not the same structural enforcement; no "Execute after row N" mechanism |
| C-20 | **PASS** 7 | Completion row at bottom of each section's table |
| C-21 | **PARTIAL** 3.5 | Trailing optional rows (limitations, replication) may lack explicit gate markers in table layout |
| C-22 | **PASS** 7 | Completion rows encode actual values from table body |
| C-23 | **PASS** 7 | Role column carries explicit prohibition text per role |
| C-24 | **PASS** 7 | `## LIFECYCLE: X` section headers as structural containers |
| C-25 | **PASS** 7 | Section-level scan vs. row-level role column scan — different structural granularity; orthogonal |
| C-26 | **PASS** 6 | CALIBRATOR row in Define Table D-2 establishes B-00; Results Table E-2 completion row carries B-00 comparison |
| C-11–C-15 | **FAIL** 0 | Not explicitly required |

**V-02 Total: 60 + 30 + 78.5 + 0 = 168.5 / 190**

---

## V-03 — Four Dedicated Containers (CALIBRATE / DESIGN / EXECUTE / ANALYZE)

**Axis**: Isolated CALIBRATE container for B-00 only; EXECUTE holds BUILDER + RECORDER; 4 containers, 5 roles

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** 12 | DESIGN container opens with hypothesis phase |
| C-02 | **PASS** 12 | DESIGN contains scope definition phase |
| C-03 | **PASS** 12 | DESIGN precedes EXECUTE at container level |
| C-04 | **PASS** 12 | ANALYZE container handles comparison phase |
| C-05 | **PASS** 12 | ANALYZE contains verdict phase |
| C-06 | **PASS** 10 | BUILDER minimality trade-off in EXECUTE |
| C-07 | **PASS** 10 | RECORDER raw data in EXECUTE |
| C-08 | **PASS** 10 | ANALYZE contains limits + next-step phases |
| C-09 | **PASS** 7 | ANALYZE counter-evidence phase |
| C-10 | **PASS** 7 | BUILDER replication steps in EXECUTE |
| C-16 | **PASS** 7 | Binary disposition enforced in ANALYZE |
| C-17 | **PASS** 7 | Co-location enforced; ANALYZE phases mirror DESIGN phase structure |
| C-18 | **PASS** 7 | Each ANALYZE phase terminates with explicit binary disposition |
| C-19 | **PASS** 7 | Phase-gating language applied per container boundary |
| C-20 | **PASS** 7 | Completion lines per phase in all containers |
| C-21 | **PARTIAL** 3.5 | Trailing sections in ANALYZE (limitations, replication) not confirmed to carry gate markers |
| C-22 | **PASS** 7 | Completion lines encode values; ANALYZE completion carries B-00 delta |
| C-23 | **PASS** 7 | Role prohibitions stated per role |
| C-24 | **PASS** 7 | Four containers: CALIBRATE, DESIGN, EXECUTE, ANALYZE — each maps to single stage |
| C-25 | **PASS** 7 | EXECUTE holds 2 roles (BUILDER + RECORDER); container scan (4 headers) ≠ role scan (5 labels) |
| C-26 | **PASS** 6 | CALIBRATE dedicated to B-00 isolation; ANALYZE completion carries B-00 delta before verdict |
| C-11–C-15 | **FAIL** 0 | Not explicitly required |

**V-03 Total: 60 + 30 + 86.5 + 0 = 176.5 / 190**

---

## V-04 — Conversational Second-Person Imperatives

**Axis**: SETUP(THINKER+ANCHOR), BUILD(MAKER+WATCHER), CLOSE; conversational register; CLOSE explicitly scoped to all post-evidence sections

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** 12 | THINKER in SETUP writes hypothesis first |
| C-02 | **PASS** 12 | THINKER writes scope exclusions with co-located validity |
| C-03 | **PASS** 12 | SETUP contains measurement criteria before BUILD |
| C-04 | **PASS** 12 | CLOSE handles comparison |
| C-05 | **PASS** 12 | CLOSE handles verdict |
| C-06 | **PASS** 10 | MAKER minimality in BUILD |
| C-07 | **PASS** 10 | WATCHER raw observations in BUILD |
| C-08 | **PASS** 10 | CLOSE explicitly contains limitations + next step |
| C-09 | **PASS** 7 | CLOSE counter-evidence section |
| C-10 | **PASS** 7 | MAKER replication steps in BUILD |
| C-16 | **PASS** 7 | CLOSE binary disposition for counter-evidence |
| C-17 | **PASS** 7 | Conversational prose places rationale immediately adjacent to its anchor — natural co-location without table overhead |
| C-18 | **PASS** 7 | CLOSE uses conversational "either X or Y" binary termination per section |
| C-19 | **PASS** 7 | "Before you do X, complete Y" imperative at each phase; natural gate language in conversational register |
| C-20 | **PASS** 7 | Each phase ends with a labeled completion line |
| C-21 | **PASS** 7 | CLOSE container explicitly absorbs ALL trailing sections (comparison, verdict, counter-evidence, limits, next step, replication); completion line on each — full gate coverage |
| C-22 | **PASS** 7 | Completion lines carry value tokens; CLOSE completion encodes verdict word and B-00 comparison |
| C-23 | **PASS** 7 | SETUP and BUILD role headers carry explicit prohibitions |
| C-24 | **PASS** 7 | Three containers: SETUP, BUILD, CLOSE — each distinct lifecycle stage |
| C-25 | **PASS** 7 | SETUP(2 roles) + BUILD(2 roles); container scan (3 headers) ≠ role scan (4 block labels); orthogonal |
| C-26 | **PASS** 6 | ANCHOR writes B-00 in SETUP before BUILD; CLOSE completion: "observed [X] vs. B-00 [Y], delta [Z]" |
| C-11–C-15 | **FAIL** 0 | Not explicitly required |

**V-04 Total: 60 + 30 + 90 + 0 = 180 / 190**

---

## V-05 — Inertia Framing (B-00 as First Element)

**Axis**: BASELINE(ANCHOR), BUILD(BUILDER+MEASURER), evaluation containers; B-00 is absolute first output element; every completion line carries B-00 comparison

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **FAIL** 0 | B-00 is the absolute first output element — hypothesis appears after baseline; violates "hypothesis must precede any prototype description or result" |
| C-02 | **PASS** 12 | Scope defined in setup phase after BASELINE |
| C-03 | **PASS** 12 | Measurement criteria established before BUILD |
| C-04 | **PASS** 12 | Evaluation container handles comparison |
| C-05 | **PASS** 12 | Evaluation handles verdict |
| C-06 | **PASS** 10 | BUILDER minimality in BUILD |
| C-07 | **PASS** 10 | MEASURER raw data in BUILD |
| C-08 | **PASS** 10 | Evaluation section has limits + next step |
| C-09 | **PASS** 7 | Evaluation counter-evidence |
| C-10 | **PASS** 7 | BUILDER replication steps |
| C-16 | **PASS** 7 | Binary disposition in evaluation |
| C-17 | **PASS** 7 | Co-location enforced per phase |
| C-18 | **PASS** 7 | Binary closures throughout |
| C-19 | **PASS** 7 | Gates per phase |
| C-20 | **PASS** 7 | Completion lines per phase |
| C-21 | **PASS** 7 | "Every completion line from BUILD onward" confirms comprehensive gate coverage — strongest C-21 statement |
| C-22 | **PASS** 7 | Every completion line encodes result values |
| C-23 | **PASS** 7 | Role prohibitions per role |
| C-24 | **PASS** 7 | Four containers; BASELINE, BUILD, and two evaluation stages |
| C-25 | **PASS** 7 | BUILD holds 2 roles (BUILDER+MEASURER); BASELINE holds 1; boundaries differ |
| C-26 | **PASS** 6 | B-00 is first element by design; every completion line from BUILD onward carries B-00 comparison — strongest C-26 |
| C-11–C-15 | **FAIL** 0 | Not explicitly required |

**V-05 Total: 48 + 30 + 90 + 0 = 168 / 190**

---

## Composite Scores and Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Excellence | Total | % |
|------|-----------|-----------|-------------|-------------|------------|-------|---|
| 1 | **V-04** | 60/60 | 30/30 | 90/90 | 0/10 | **180** | 94.7% |
| 2 | **V-01** | 60/60 | 30/30 | 86.5/90 | 0/10 | **176.5** | 92.9% |
| 3 | **V-03** | 60/60 | 30/30 | 86.5/90 | 0/10 | **176.5** | 92.9% |
| 4 | **V-02** | 60/60 | 30/30 | 78.5/90 | 0/10 | **168.5** | 88.7% |
| 5 | **V-05** | 48/60 | 30/30 | 90/90 | 0/10 | **168** | 88.4% |

V-01 and V-03 are tied; V-01 ranks second by virtue of having the most explicit template shown (enforceability is directly verified rather than inferred).

---

## Criterion Analysis

### C-21 is the sole separator between V-04 and V-01/V-03

V-04's CLOSE container is explicitly described as holding ALL post-evidence sections: comparison, verdict, counter-evidence, limitations, next steps, and replication. Every section within CLOSE carries a completion gate. V-01 and V-03 leave trailing section gating unverified because their EVALUATE/ANALYZE templates are not fully shown, and the description does not explicitly claim complete coverage.

### C-25 is satisfied by all five variations

Every variation achieves structural independence between lifecycle containers and role labels by placing at least two roles inside one container (DEFINE, EXECUTE, SETUP, or BUILD). Container scan traverses section headers; role scan traverses block-level labels inside those sections. The scans operate at different granularity in all five designs.

### V-05's C-01 failure is a genuine design conflict

V-05 puts B-00 first to achieve the strongest C-26 framing. But C-01 requires hypothesis as the first substantive element without exception. These two goals are in direct conflict. The correct resolution (demonstrated by V-01, V-03, V-04): hypothesis first, then B-00 baseline in the same DEFINE/SETUP container, then measurement criteria. B-00 can follow immediately after hypothesis without preceding it.

### V-02's table format weakens C-10 and C-19

Table rows do not provide a natural home for "Execute after Phase N gate is present in your output" — an inline sequential constraint. Row ordering enforces sequence implicitly, but C-19 requires co-located explicit markers. Similarly, a replication path is harder to express as table cells than as a numbered inline list.

---

## Excellence Signals (V-04)

**Signal 1 — Terminal container absorbs all trailing sections**: Designating CLOSE as the explicit receiver of ALL post-evidence content (comparison, verdict, counter, limits, next step, replication) achieves C-21 complete gate coverage by construction. No section lives outside a named, gated container.

**Signal 2 — Conversational register enables natural rationale proximity**: Second-person imperative prose places the "why" immediately after the "what" without requiring table scaffolding. C-17 (rationale co-located) is satisfied structurally by the prose form itself, not by a table constraint that must be explicitly designed in.

---

```json
{"top_score": 180, "all_essential_pass": false, "new_patterns": ["terminal-container-absorbs-all-trailing-sections", "B-00-must-follow-hypothesis-not-precede-it"]}
```
