## scout-feasibility Round 1 Scorecard

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 | V-02 PM leads | **100** | YES |
| 2 | V-04 Interrogative | 95 | YES |
| 3 | V-05 Phased+inertia | 95 | YES |
| 4 | V-03 Prose | 83 | NO (C-01 essential fail) |
| 5 | V-01 Baseline | 66 | NO (C-03/C-04 essential fail) |

**3 golden variations out of 5.** V-02 is the only perfect score.

---

### What decided V-02

The single criterion that separates V-02 from V-04/V-05 is **C-09** (hour budget comparison). All three golden variations pass all 5 essential and all 3 recommended. C-09 requires: sum component hours, compare to available hours, flag over/under explicitly. V-05 has both inputs in separate phases but never chains them. V-04 collects available hours but never estimates per-component hours. V-02 does all three: PHASE 1 computes `available_hours = team * weeks * hrs/wk`, PHASE 2 sums estimates and flags over/under, FINDINGS #2 requires the comparison.

### Key pattern: gate beats instruction

V-01 says "DISCLOSE these inferences explicitly." V-02 says "Do not proceed until they are visible." The gate is why C-03/C-04 flip from FAIL to PASS. This is the SF-01/SF-03 fix.

### V-03 confirmed risk

The prose format passes C-05/C-08 most strongly but C-01 fails by design: the rubric requires "each label must be its own field, not embedded in prose" and V-03 explicitly embeds them. 83 composite but not golden.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["gate pattern: 'do not proceed until visible' prevents silent inference where instruction-only disclosure fails", "PM-first ordering makes hour budget structurally unavoidable before complexity scoring", "explicit sum-and-compare chain with over/under flag is required for C-09 -- collecting hours in two phases without the chain still fails"]}
```
ded: 3/3 * 30 = 30
aspirational: 0/2 * 10 = 0
composite: 66
golden: NO (C-03/C-04 essential fail)
```

---

### V-02: PM leads

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Traffic lights per component | essential | PASS | PHASE 2 specifies GREEN/YELLOW/RED per component with gate definitions |
| C-02 Score + label | essential | PASS | FINDINGS #4 |
| C-03 Team/timeline inference disclosed | essential | PASS | PHASE 1: "Write these three lines before proceeding. Do not proceed until they are visible." -- hard gate |
| C-04 Stack fallback disclosed | essential | PASS | SETUP: "Disclose the fallback: name the file used, state what you inferred from it." -- required in same phase as scan |
| C-05 RED blockers with rationale | essential | PASS | FINDINGS #3: "each RED item -- why it is blocked, what would lift it" |
| C-06 Build-vs-buy per component | recommended | PASS | PHASE 3 Strategy |
| C-07 Scoped fallback when < 50 | recommended | PASS | FINDINGS #5 |
| C-08 Prerequisites when caveats | recommended | PASS | FINDINGS #6 "all RED items represented" |
| C-09 Hour budget comparison | aspirational | PASS | PHASE 1 computes available hours; PHASE 2 sums estimated hours + "Flag over-budget or under-budget explicitly"; FINDINGS #2 "Over/under flag" |
| C-10 Amendment list | aspirational | PASS | FINDINGS #7: "3 numbered actions, each traceable to a specific RED or YELLOW component" |

```
essential: 5/5 * 60 = 60
recommended: 3/3 * 30 = 30
aspirational: 2/2 * 10 = 10
composite: 100
golden: YES
```

---

### V-03: Table-free prose

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Traffic lights per component | essential | FAIL | Prose format embeds GREEN/YELLOW/RED in paragraphs; rubric pass condition: "each label must be its own field, not embedded in prose" -- V-03 explicitly uses prose, violating this |
| C-02 Score + label | essential | PASS | "FEASIBILITY VERDICT: Score: [0-100] Label:" -- explicit dedicated section |
| C-03 Team/timeline inference disclosed | essential | PASS | INFERENCE DISCLOSURE: "Write these two sentences verbatim... before any scoring" -- structurally enforced |
| C-04 Stack fallback disclosed | essential | PASS | "If none found: write one sentence naming the fallback file... This sentence is required before analysis begins." |
| C-05 RED blockers with rationale | essential | PASS | RED BLOCKERS: dedicated paragraph per RED item; specific gap + what would change |
| C-06 Build-vs-buy per component | recommended | PASS | Per-component paragraph includes Build/Buy/Use with one-sentence reason |
| C-07 Scoped fallback when < 50 | recommended | PASS | "If NOT FEASIBLE: follow immediately with a scoped alternative." |
| C-08 Prerequisites when caveats | recommended | PASS | "If FEASIBLE WITH CAVEATS: follow with a numbered prerequisite list. Every RED-rated component must be represented." |
| C-09 Hour budget comparison | aspirational | FAIL | No hours anywhere |
| C-10 Amendment list | aspirational | PASS | AMENDMENTS section: "numbered list of 3 actions... must name the specific component it addresses and state what changes" |

```
essential: 4/5 * 60 = 48
recommended: 3/3 * 30 = 30
aspirational: 1/2 * 10 = 5
composite: 83
golden: NO (C-01 essential fail; prose format is structurally incompatible with C-01 pass condition)
```

Note: V-03 demonstrates the predicted C-01 risk. Prose produces the best qualitative rationale
(C-05/C-08) but fails the scanability requirement for traffic lights. Composite would be 83 --
above 80 -- but the essential gate prevents golden.

---

### V-04: Interrogative

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Traffic lights per component | essential | PASS | Q3: "Whether the stack has it: GREEN / YELLOW / RED" per component |
| C-02 Score + label | essential | PASS | Q6: "Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE." |
| C-03 Team/timeline inference disclosed | essential | PASS | Q2: "Do not proceed to Q3 without writing these three values." -- hard gate |
| C-04 Stack fallback disclosed | essential | PASS | Q1: "Required before Q2" -- gated; requires naming fallback file + inference statement |
| C-05 RED blockers with rationale | essential | PASS | Q4: "Do not skip this question if any component is RED"; requires WHY + unblock action |
| C-06 Build-vs-buy per component | recommended | PASS | Q5: Build/Buy/Use per component with reasoning |
| C-07 Scoped fallback when < 50 | recommended | PASS | Q6: "If score < 50: state a scoped alternative... Required." -- "Required" is a structural gate |
| C-08 Prerequisites when caveats | recommended | PASS | Q6: "If FEASIBLE WITH CAVEATS: numbered prerequisite list, all RED items included." |
| C-09 Hour budget comparison | aspirational | FAIL | Q2 collects available hours but no hour estimation per component; no sum-and-compare instruction |
| C-10 Amendment list | aspirational | PASS | Q7: "List 3 numbered actions. Each must name the specific RED or YELLOW component it addresses." |

```
essential: 5/5 * 60 = 60
recommended: 3/3 * 30 = 30
aspirational: 1/2 * 10 = 5
composite: 95
golden: YES
```

---

### V-05: Phased + inertia

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|----------|
| C-01 Traffic lights per component | essential | PASS | PHASE 3: "Traffic light: GREEN / YELLOW / RED" as dedicated per-component field |
| C-02 Score + label | essential | PASS | PHASE 5: "Score: [0-100]. Label:" |
| C-03 Team/timeline inference disclosed | essential | PASS | PHASE 2: "Write these three lines explicitly. Do not proceed to Phase 3 without them." -- hard gate |
| C-04 Stack fallback disclosed | essential | PASS | PHASE 1: "This disclosure is required before Phase 2 begins." -- hard gate |
| C-05 RED blockers with rationale | essential | PASS | PHASE 4: "For every RED component, two required items: Blocker statement + Lift condition" |
| C-06 Build-vs-buy per component | recommended | PASS | PHASE 3: "Build / Buy / Use existing (Strategy role, one-sentence reason)" |
| C-07 Scoped fallback when < 50 | recommended | PASS | PHASE 5: "If score < 50: scoped alternative required." with constraint naming |
| C-08 Prerequisites when caveats | recommended | PASS | PHASE 5: "If FEASIBLE WITH CAVEATS: numbered prerequisites, all RED items represented." |
| C-09 Hour budget comparison | aspirational | FAIL | Available hours in PHASE 2, estimated hours in PHASE 3, but no explicit "sum and compare, flag over/under" instruction -- comparison is implicit, not required |
| C-10 Amendment list | aspirational | PASS | PHASE 6: 3 actions, each naming RED/YELLOW component AND "state what changes in the feasibility score" -- strongest C-10 formulation across all variations |

```
essential: 5/5 * 60 = 60
recommended: 3/3 * 30 = 30
aspirational: 1/2 * 10 = 5
composite: 95
golden: YES
```

---

## Rankings

| Rank | Variation | Composite | Golden | Strengths | Gap |
|------|-----------|-----------|--------|-----------|-----|
| 1 | V-02 PM leads | 100 | YES | Only variation to pass C-09; all 10 criteria pass | None |
| 2 | V-04 Interrogative | 95 | YES | Cleanest C-03/C-04 gates via Q-sequence; Q7 amendment gate | C-09 missing |
| 3 | V-05 Phased+inertia | 95 | YES | Strongest C-10 (score-delta per action); clearest phase structure | C-09 implicit only |
| 4 | V-03 Prose | 83 | NO | Strongest C-05/C-08 rationale quality; passes C-10 | C-01 essential fail |
| 5 | V-01 Baseline | 66 | NO | Establishes floor; C-06/C-07/C-08 pass | C-03/C-04 essential fail |

---

## Excellence Signals (from V-02)

**1. Gate pattern beats instruction pattern for inference disclosure**
V-02: "Write these three lines before proceeding. Do not proceed until they are visible."
V-01: "DISCLOSE these inferences explicitly before using them in any calculation."
The gate structurally prevents SF-01/SF-03. An instruction requests; a gate blocks proceeding
without the output. C-03 and C-04 become structural properties of the output, not intentions.

**2. PM-first ordering makes C-09 structurally unavoidable**
V-02 is the only variation where Phase 1 computes available hours before Phase 2 scores
complexity. In all other variations, the Architect scores first and PM reviews after.
PM-first forces hour estimation as a gate input, not an afterthought.

**3. Explicit sum-and-compare chain with over/under flag**
V-05 collects hours in two phases but never chains them. V-02 adds:
"Sum the estimated hours. Compare to available hours from Phase 1. Flag over-budget or
under-budget explicitly." The three-step instruction -- sum, compare, flag -- is what
locks in the C-09 pass condition.

**4. FINDINGS section mirrors rubric structure**
V-02's numbered FINDINGS (1-7) map directly to C-01 through C-10. When the output
structure is designed to produce rubric-shaped artifacts, every criterion becomes a
required section, not an emergent property of good execution.

---

## C-09 Gap Analysis

C-09 is the only criterion that fails in 4 of 5 variations. Root cause: every variation
collects team size and timeline but only V-02 chains the full calculation:
  available_hours = team * weeks * hrs_per_week
  sum(component_estimated_hours)
  compare -> over/under flag required

The gap is not conceptual -- V-05 has both inputs. The gap is the missing explicit
"compare and flag" instruction in FINDINGS. This is the primary fix target for V-golden.

---

## V-golden Synthesis Target

Combine winning patterns:
- V-02's PM-first phase ordering and explicit hour comparison chain (C-09 fix)
- V-05's PHASE 6 score-delta amendment format: "state what changes in the feasibility
  score if the action is completed" (strongest C-10)
- V-04's Q-gate formulation for C-03/C-04: clean "Required before Q-next" language
- V-02's numbered FINDINGS list mirroring rubric structure

Drop:
- V-03 prose format (C-01 essential fail, structurally incompatible)
- V-01's instruction-only disclosure (superseded by gate pattern)
