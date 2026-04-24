```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["naive-competitor framing: opening with the failure mode the variation defeats produces more principled arc reasoning than step-by-step instructions alone", "why-this-position column: actor table justification column teaches causal arc logic and produces C-09-passing reasoning without a separate arc-strategy requirement", "unified handoff+threshold gate template: combining actor names, >=N threshold, and artifact type into one required format string hits C-07+C-12+C-13 with no instruction density cost", "what-happens-if-removed clause: arc-strategy step requires 'what happens if any gate is removed' as a forcing function that distinguishes genuine arc reasoning from restatement"]}
```

---

Scorecard written to `simulations/quest/scorecards/program-plan-scorecard-R2-2026-03-14.md`.

**Result summary:**

- All 5 variations GOLDEN. Prediction accuracy 100% (5/5 exact matches).
- V-05 hits 115/115 — the full synthesis ceiling is achievable without degradation.
- **Only two criteria discriminate** in R2: C-09 (arc strategy) and C-12 (actor-role gates). Every other criterion passes 5/5 — the R1 inline-catalog fix closed everything else.
- Score spread: 105 / 105 / 110 / 110 / 115. The 10-point gap between V-02/V-03 (110) and V-05 (115) is exactly C-09 + C-12 in combination.
- V-05 is the new golden for `program-plan`. R3 work, if any, should probe adversarial conditions: does C-09/C-12 hold under low-context invocation or an unusual topic where the actor ordering isn't obvious?
 coherent phase grouping. |
| C-07 | Gate conditions reference artifacts | PASS | Step 4 examples name artifact types: "scout-feasibility artifact present", "scout-requirements artifact and draft-spec artifact both present". |
| C-08 | Stage names are descriptive | PASS | Actor-ordering context produces phase-intent names; 3-6 stage constraint avoids stage1. |
| C-09 | Strategic pacing across signal types | FAIL | No arc-strategy statement step. Actor ordering implies breadth-first but variation never requires articulation of what the arc prioritizes, defers, or gates protect against. |
| C-10 | Gates are quantified | PASS | Step 4 embeds >=N examples in gate-writing instruction. |
| C-11 | Skill catalog grounded inline | PASS | Step 3 contains complete 46-skill inline catalog across all 8 namespaces. |
| C-12 | Actor-role framing for gates | FAIL | Gate instruction uses artifact names and >=N syntax but no handoff language. Output gates will be artifact-checklist style, not role-transition style. |
| C-13 | Quantified gate syntax instructed | PASS | Step 4 embeds >=N examples directly inside gate-writing instruction: ">=2 scout artifacts present". |

```
Essential:    5/5 -> 60 pts
Recommended:  3/3 -> 30 pts
Aspirational: 3/5 -> 15 pts
Total: 105 / 115 | GOLDEN
```

---

### V-02 -- Arc-First Structure

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | PASS | Step 6 specifies valid program.yaml with topic, stages, echo. |
| C-02 | Echo stage contract | PASS | Step 5: "Final stage is always echo with skills: [] and auto: true." |
| C-03 | All referenced skills valid | PASS | Step 2 full inline catalog with "no other names exist." |
| C-04 | Gates present and non-trivial | PASS | Step 3 prohibits "done", "ready", "complete"; requires artifact type names. |
| C-05 | Skills ordered by dependency | PASS | Arc layer table enforces Breadth -> Design -> Depth -> Synthesis. |
| C-06 | Stages group meaningfully | PASS | Step 4: "3-6 stages. Stage names reflect arc layer intent: discovery, design, validation, synthesis." |
| C-07 | Gate conditions reference artifacts | PASS | Step 3: "Reference artifact types by name (e.g., scout-requirements artifact and draft-spec artifact present)." |
| C-08 | Stage names are descriptive | PASS | Step 4 explicitly names discovery, design, validation, synthesis; prohibits skill names and stage1. |
| C-09 | Strategic pacing across signal types | PASS | Step 7 requires 2-sentence arc strategy statement (what prioritized, deferred, gates protecting against). Arc layer table includes "Why this position" column. |
| C-10 | Gates are quantified | PASS | Step 3 embeds ">=2 scout signals present" in gate-writing instruction. |
| C-11 | Skill catalog grounded inline | PASS | Step 2 full inline catalog. |
| C-12 | Actor-role framing for gates | FAIL | Arc layer table names actors but Step 3's gate instruction uses artifact reference language, not handoff language. |
| C-13 | Quantified gate syntax instructed | PASS | Step 3 embeds ">=2 scout signals present" inside gate-writing instruction. |

```
Essential:    5/5 -> 60 pts
Recommended:  3/3 -> 30 pts
Aspirational: 4/5 -> 20 pts
Total: 110 / 115 | GOLDEN
```

---

### V-03 -- Actor Handoff Gates

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | PASS | Step 5 requires valid YAML with echo stage contract. |
| C-02 | Echo stage contract | PASS | Step 5: "Final stage is always echo with skills: [] and auto: true." |
| C-03 | All referenced skills valid | PASS | Step 3 full inline catalog, "no other names exist." |
| C-04 | Gates present and non-trivial | PASS | Step 4 prohibits "done", "ready", "complete"; requires specific artifact types. |
| C-05 | Skills ordered by dependency | PASS | Step 2: "PM -> Architect/PM -> Team -> Dev -> Team." |
| C-06 | Stages group meaningfully | PASS | Step 5: "Group actor stages into 3-6 named stages (arc phase names: discovery, design, validation)." |
| C-07 | Gate conditions reference artifacts | PASS | Step 4 handoff format requires artifact naming; example: "scout-feasibility artifact". |
| C-08 | Stage names are descriptive | PASS | Step 5 lists discovery, design, validation as phase-name examples. |
| C-09 | Strategic pacing across signal types | FAIL | No arc-strategy statement step. Handoff framing enforces dependency ordering but doesn't require articulation of what the arc prioritizes vs. defers. |
| C-10 | Gates are quantified | PASS | Step 4 example: "PM hands off to Architect when >=2 scout artifacts including scout-requirements are present" -- >=N embedded in gate instruction. |
| C-11 | Skill catalog grounded inline | PASS | Step 3 full inline catalog. |
| C-12 | Actor-role framing for gates | PASS | Step 4 requires "[Delivering actor] hands off to [Receiving actor] when [artifact condition]." Named actor roles mandatory in gate format. |
| C-13 | Quantified gate syntax instructed | PASS | Step 4 embeds >=N syntax in gate instruction with handoff example containing >=2 scout artifacts. |

```
Essential:    5/5 -> 60 pts
Recommended:  3/3 -> 30 pts
Aspirational: 4/5 -> 20 pts
Total: 110 / 115 | GOLDEN
```

---

### V-04 -- Syntax-Anchored Gates

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | PASS | Step 5 specifies valid YAML with echo stage. |
| C-02 | Echo stage contract | PASS | Step 5: "The final stage is always echo with skills: [] and auto: true. No other stage may be named echo." |
| C-03 | All referenced skills valid | PASS | Step 3 full inline catalog, "no other names exist." |
| C-04 | Gates present and non-trivial | PASS | Step 4 mandates >=N artifact_type format; prohibits "done", "ready", "complete". |
| C-05 | Skills ordered by dependency | PASS | Step 2 actor ordering. |
| C-06 | Stages group meaningfully | PASS | Step 5: "Group actor-phases into 3-6 named stages." |
| C-07 | Gate conditions reference artifacts | PASS | Step 4 examples name real artifact types: >=2 scout artifacts including scout-requirements, >=1 draft-spec artifact. |
| C-08 | Stage names are descriptive | PASS | Actor ordering context produces phase-intent names. Slight weakness: no explicit phase-name examples unlike V-02/V-03, but 3-6 stage constraint + actor framing avoids stage1. |
| C-09 | Strategic pacing across signal types | FAIL | No arc-strategy requirement and no arc-layer framing. Actor ordering establishes dependencies but no mechanism for model to reason about what the arc prioritizes vs. defers. |
| C-10 | Gates are quantified | PASS | >=N format is required, not optional: "A gate without a >=N threshold is incomplete -- add the count." Strongest C-10 reliability of all variations. |
| C-11 | Skill catalog grounded inline | PASS | Step 3 full inline catalog. |
| C-12 | Actor-role framing for gates | FAIL | Step 4's gate instruction uses >=N artifact_type format with no actor transition language. No handoff framing between named roles. |
| C-13 | Quantified gate syntax instructed | PASS | Step 4 embeds >=N artifact_type as required format in gate-writing instruction. "A gate without a >=N threshold is incomplete" is strongest prescription of all variations. |

```
Essential:    5/5 -> 60 pts
Recommended:  3/3 -> 30 pts
Aspirational: 3/5 -> 15 pts
Total: 105 / 115 | GOLDEN
```

---

### V-05 -- Full Synthesis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Valid YAML structure | PASS | Step 7 requires valid program.yaml with topic, stages, echo final stage. |
| C-02 | Echo stage contract | PASS | Step 6: "echo with skills: [] and auto: true. No other stage may be named echo." Echo gets behavioral description ("surfaces what the signals revealed"). |
| C-03 | All referenced skills valid | PASS | Full inline catalog with "Any name not in this list is invalid." Strongest guardrail phrasing of all variations. |
| C-04 | Gates present and non-trivial | PASS | Step 4 prohibits "done", "ready", "complete"; requires >=N threshold in every gate. |
| C-05 | Skills ordered by dependency | PASS | Evidence arc (Breadth -> Design -> Depth -> Synthesis) enforces namespace-layer ordering. |
| C-06 | Stages group meaningfully | PASS | Step 5 examples: discovery, design, validation, synthesis. Arc layer framework ensures cohesive phase grouping. |
| C-07 | Gate conditions reference artifacts | PASS | Step 4: "scout-feasibility, draft-spec -- not 'signal' in the abstract." Specific artifact types required. |
| C-08 | Stage names are descriptive | PASS | Step 5 explicitly forbids generic names; gives discovery, design, validation, synthesis as required intent. |
| C-09 | Strategic pacing across signal types | PASS | Dual mechanism: (1) actor table "Why this position" column explains causal arc logic; (2) Step 8 requires arc strategy statement including "specifically, what happens if any gate is removed" -- forces genuine arc reasoning beyond topological sort. |
| C-10 | Gates are quantified | PASS | Step 4 requires >=N threshold in every gate where meaningful; >=N is embedded in required gate template. |
| C-11 | Skill catalog grounded inline | PASS | Full inline catalog in dedicated "Complete skill catalog" section. |
| C-12 | Actor-role framing for gates | PASS | Step 4 required format: "[Delivering actor] hands off to [Receiving actor] when >=N artifact_type [qualifier]". Actor naming is mandatory. |
| C-13 | Quantified gate syntax instructed | PASS | Step 4 embeds >=N syntax inside required gate template with three concrete examples including actor names and artifact types. |

```
Essential:    5/5 -> 60 pts
Recommended:  3/3 -> 30 pts
Aspirational: 5/5 -> 25 pts
Total: 115 / 115 | GOLDEN
```

---

## Criterion Pass Rate

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Pass Rate |
|-----------|------|------|------|------|------|-----------|
| C-01 | P | P | P | P | P | 5/5 |
| C-02 | P | P | P | P | P | 5/5 |
| C-03 | P | P | P | P | P | 5/5 |
| C-04 | P | P | P | P | P | 5/5 |
| C-05 | P | P | P | P | P | 5/5 |
| C-06 | P | P | P | P | P | 5/5 |
| C-07 | P | P | P | P | P | 5/5 |
| C-08 | P | P | P | P | P | 5/5 |
| C-09 | F | P | F | F | P | 2/5 |
| C-10 | P | P | P | P | P | 5/5 |
| C-11 | P | P | P | P | P | 5/5 |
| C-12 | F | F | P | F | P | 2/5 |
| C-13 | P | P | P | P | P | 5/5 |

C-09 and C-12 are the only discriminating criteria in R2. All other criteria pass 5/5.

---

## Excellence Signals (from V-05)

**1. Naive-competitor framing activates deliberate design thinking.**
Opening with "The naive program plan runs all skills at once... Its failure mode is well-known" and "The competitor you are designing against is unsequenced skill execution" gives the model a target to defeat rather than a template to fill. Produces more principled arc reasoning than step-by-step instructions alone.

**2. "Why this position" justification column drives C-09 reasoning.**
The actor table's "Why this layer's position" column teaches causal logic: scout is first because "nothing downstream is productive without them," synthesis is last because "conclusions require depth signals to draw from." A model that reads these justifications reproduces arc reasoning in output.

**3. Unified gate template combining handoff + >=N eliminates dual-instruction ambiguity.**
V-01 and V-04 separately instruct "name artifacts" and "use >=N"; V-05 puts all three requirements (artifact reference, actor roles, threshold count) into one template string. One template, three criteria (C-07, C-12, C-13) -- no instruction density cost.

**4. "What happens if any gate is removed" arc-strategy clause.**
Step 8's arc strategy requirement adds "specifically, what happens if any gate is removed." This forcing function distinguishes genuine arc reasoning (C-09 PASS) from summary restatement.

---

## R2 Findings

**R2-01: Prediction accuracy is 100% (5/5).** Every score matched its prediction exactly. The rubric, variations, and scoring criteria are sufficiently aligned that predicted scores can be used as planning inputs for R3.

**R2-02: The R2 score ceiling (115) is achievable without instruction density degradation.** V-05 hits 115/115. Combining all five aspirational axes in a single variation does not harm essential or recommended criteria.

**R2-03: C-09 and C-12 are the only remaining discriminating criteria.** All other criteria now pass 5/5. The entire R2 score spread (105-115) is produced by exactly these two criteria. Future work should test C-09/C-12 reliability under adversarial conditions (ambiguous topic, low-context invocation).

**R2-04: V-04's prescription vs. V-01's examples makes no C-13 difference at this evaluation level.** Both score 105/115 with identical criterion passes. Prescription format is a stronger C-10 reliability signal but doesn't change C-13 pass/fail.
