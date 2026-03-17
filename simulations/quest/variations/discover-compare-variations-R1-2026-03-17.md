Written to `simulations/quest/variations/discover-compare-variations-R1-2026-03-17.md`.

---

## discover-compare — Variations R1

Five complete, runnable prompt variations against the v1 rubric (9 criteria).

---

### V-01 — Inertia-First Framing
**Axis**: Inertia framing
**Hypothesis**: Anchoring ANCHOR[0] (status quo) as the first named entity before A or B are touched structurally forces independent inertia verdicts (C-02) and surfaces the build/no-build gate (C-05). The token binding rule makes drift detectable.

Structure: Option 0 definition → Option A analysis (4 dimensions) → Option B analysis (4 dimensions) → matrix with Option 0 column → gate → recommendation → AMEND.

Key C-02 mechanism: VERDICT A and VERDICT B are produced in separate named sections, each carrying an explicit "compare against ANCHOR[0] only — not against Option B/A" instruction.

---

### V-02 — Scored Grid (1–5 Numeric Scale)
**Axis**: Output format
**Hypothesis**: Numeric scoring makes the recommendation derivable from total scores, eliminating "implied recommendation" (C-04 failure mode). Risk differentiation (C-06) becomes visible as a score delta. Option 0 column holds "anchor" / "—" cells at the same weight positions.

Structure: Define status quo → score Option A (4 dimensions, 1–5) → score Option B (4 dimensions, 1–5) → 5-row matrix with totals → gate → recommendation with score-gap reasoning → AMEND.

---

### V-03 — Phase-Explicit with Named Boundary Markers
**Axis**: Lifecycle emphasis
**Hypothesis**: Naming each analysis step as a numbered phase (`PHASE 2A`, `PHASE 2B`) with labeled `> Output:` declarations makes omission structurally visible — a missing output token signals an incomplete phase. Bilateral phases (1A/1B through 4A/4B) make C-01 coverage a count property, not a recall property.

Structure: 8 phases with phase-labeled outputs for each dimension per option; Phase 5 assembles from output tokens; Phases 6–8 gate, recommend, and AMEND.

---

### V-04 — Conversational / Question-Driven Register
**Axis**: Phrasing register
**Hypothesis**: Question framing ("Would teams bother?" "What could go wrong?") encourages the model to reason freshly per option rather than applying a template symmetrically — reducing symmetric inertia (the most common C-02 failure mode). The question "Is either option even worth building?" makes C-05 a natural stopping point.

Structure: Two independent question blocks (one per option) with explicit "independently" markers → table → build/no-build question → explicit recommendation → AMEND.

---

### V-05 — Combined: Phase-Explicit + Inertia-First + Audience-Conditional
**Axes**: Lifecycle emphasis + Inertia framing + Phrasing register
**Hypothesis**: Combining (1) ANCHOR[0] committed at Phase 0 with a binding rule, (2) TOKEN RECALL headers at every inertia and matrix phase, and (3) audience register set at Phase 0 with explicit conditional branching — maximizes aspirational coverage (C-08, C-09) without sacrificing essential criteria reliability. Three-phase enforcement: declare (Phase 0 ANCHOR + register) → recall (Phases 2A/2B/5/7 TOKEN RECALL) → independence constraint on VERDICT sentences.

Structure: Phase 0 dual-purpose (anchor + register) → bilateral phases 1A–4B → Phase 5 matrix (Option 0 column labeled with ANCHOR[0]) → Phase 6 gate → Phase 7 recommendation with register-conditional framing → Phase 8 AMEND with register override path.

---

### Rubric coverage projection

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 bilateral dimensions | PASS | PASS | PASS | PASS | PASS |
| C-02 independent inertia | PASS | PASS | PASS | PASS | PASS |
| C-03 decision matrix | PASS | PASS | PASS | PASS | PASS |
| C-04 explicit recommendation | PASS | PASS | PASS | PASS | PASS |
| C-05 build/no-build gate | PASS | PASS | PASS | PASS | PASS |
| C-06 differentiated risk | PASS | PASS | PASS | PASS | PASS |
| C-07 actionable AMEND | PASS | PASS | PASS | PASS | PASS |
| C-08 Option 0 in matrix | PASS | PASS | PASS | PASS | PASS |
| C-09 audience calibration | — | — | — | partial | PASS |

V-01–V-03: target 8/9 (Option 0 column present; no audience conditioning)
V-04: target 8.5/9 (question framing implies audience sensitivity but no explicit register branch)
V-05: target 9/9 (explicit register declaration with phase-level conditional branching)
 derivable — eliminating the "implied recommendation" failure mode (C-04) and making risk differentiation (C-06) explicit by score delta.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Score each dimension 1–5. Higher is better (more feasible, lower inertia risk, lower overall risk, stronger competitive position).

---

### STEP 1: DEFINE THE STATUS QUO

What exists today in place of either option? One sentence.

Option 0 (Status Quo): {description}

---

### STEP 2: SCORE OPTION A

Evaluate **{option_a}** on each dimension. Score 1–5, then justify in one sentence.

| Dimension | Score (1–5) | Justification |
|---|---|---|
| Feasibility | | Is the team capable, timeline realistic, complexity manageable? |
| Inertia (vs. status quo) | | Would teams do nothing instead of building Option A? 5 = strong pull away from status quo; 1 = status quo wins easily |
| Risk | | 5 = low overall risk; 1 = high overall risk. Name the top risk. |
| Competitive position | | 5 = clear differentiation; 1 = undifferentiated. Name the differentiator. |

Option A total: {sum}/20

---

### STEP 3: SCORE OPTION B

Evaluate **{option_b}** on each dimension independently. Do not score Option B's inertia relative to Option A — score it against the status quo.

| Dimension | Score (1–5) | Justification |
|---|---|---|
| Feasibility | | |
| Inertia (vs. status quo) | | Would teams do nothing instead of building Option B? Score independently of Option A. |
| Risk | | Name Option B's top risk. Must differ from Option A's top risk unless you explain why they are the same. |
| Competitive position | | Name Option B's differentiator. |

Option B total: {sum}/20

---

### STEP 4: COMPARISON MATRIX

| Dimension | Option 0 | Option A | Option B |
|---|---|---|---|
| Feasibility | — | {score}/5 | {score}/5 |
| Inertia (vs. status quo) | anchor | {score}/5 | {score}/5 |
| Risk | — | {score}/5 | {score}/5 |
| Competitive position | baseline | {score}/5 | {score}/5 |
| **Total** | — | **/20** | **/20** |

---

### STEP 5: BUILD/NO-BUILD GATE

If Option A inertia score ≤ 2 AND Option B inertia score ≤ 2: both options face strong inertia from the status quo. State whether "build neither" is the correct recommendation, or identify what condition would change this.

---

### STEP 6: RECOMMENDATION

**Recommendation: Option A / Option B / Neither / Conditional on {X}**

Lead with the recommendation. Then:
- Why this option wins (reference the highest-scoring gap between the two)
- What is given up by not choosing the other option
- If the recommendation is not the highest total score, explain the override reason

---

### AMEND

- **Add Option C** — Score Option C on all four dimensions using the same scale and the same Option 0 baseline. Add a column to the comparison matrix. Update the recommendation.
- **Weight a dimension** — Specify dimension and multiplier (e.g., "inertia 2x"). Apply to both option scores. Show recalculated totals. Update recommendation if the winner changes.
- **Shift audience** — Exec: open with recommendation + top business risk score gap. Engineering: open with feasibility + risk score details. Re-render the output with the specified register.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

## V-03 — Phase-Explicit with Named Boundary Markers

**Axis**: Lifecycle emphasis
**Hypothesis**: Naming each analysis step as a numbered phase with explicit entry/exit conditions structurally enforces C-01 bilateral coverage (the phase names make omission visible) and C-02 independence (phase 2A and 2B are physically separate).

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

Execute each phase in sequence. Each phase has a labeled output. Do not skip phases.

---

**PHASE 0 — STATUS QUO**
Define what teams do today without either option. One sentence.
> Output: `STATUS QUO: {description}`

---

**PHASE 1A — OPTION A: FEASIBILITY**
Is the team capable of building {option_a}? Is the scope realistic? What is the biggest complexity risk?
Rating: GREEN / YELLOW / RED
> Output: `FEASIBILITY-A: {rating} — {one sentence}`

**PHASE 1B — OPTION B: FEASIBILITY**
Is the team capable of building {option_b}? Is the scope realistic? What is the biggest complexity risk?
Rating: GREEN / YELLOW / RED
> Output: `FEASIBILITY-B: {rating} — {one sentence}`

---

**PHASE 2A — OPTION A: INERTIA CHECK**
Compare Option A against the STATUS QUO from Phase 0 — not against Option B.
Question: Would teams keep the STATUS QUO rather than build Option A?
> Output: `INERTIA-A: LOW / MEDIUM / HIGH — {mechanism sentence}`

**PHASE 2B — OPTION B: INERTIA CHECK**
Compare Option B against the STATUS QUO from Phase 0 — not against Option A.
Question: Would teams keep the STATUS QUO rather than build Option B?
> Output: `INERTIA-B: LOW / MEDIUM / HIGH — {mechanism sentence}`

---

**PHASE 3A — OPTION A: RISK**
Name the top 2 risks specific to Option A. Rate each LOW / MEDIUM / HIGH.
> Output: `RISK-A: {risk1 / rating}, {risk2 / rating}`

**PHASE 3B — OPTION B: RISK**
Name the top 2 risks specific to Option B. These should be distinct from Option A's risks. If they are the same, state why.
> Output: `RISK-B: {risk1 / rating}, {risk2 / rating}`

---

**PHASE 4A — OPTION A: COMPETITIVE POSITIONING**
How does Option A position against the market? Name at least one concrete differentiator. Avoid generic phrases like "more competitive" or "better user experience" without specifics.
> Output: `COMPETITIVE-A: {differentiator and positioning statement}`

**PHASE 4B — OPTION B: COMPETITIVE POSITIONING**
How does Option B position against the market? Name at least one concrete differentiator distinct from Option A's.
> Output: `COMPETITIVE-B: {differentiator and positioning statement}`

---

**PHASE 5 — DECISION MATRIX**
Assemble outputs from phases 1–4 into a matrix. Include Option 0 (STATUS QUO) as a column.

| Dimension | Option 0 | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FEASIBILITY-A | FEASIBILITY-B |
| Inertia | this IS the anchor | INERTIA-A | INERTIA-B |
| Risk | N/A | RISK-A | RISK-B |
| Competitive position | baseline | COMPETITIVE-A | COMPETITIVE-B |

---

**PHASE 6 — BUILD/NO-BUILD GATE**
Check INERTIA-A and INERTIA-B.
If both are HIGH: state whether "build neither" applies. If still recommending build, state the condition that overrides inertia.

---

**PHASE 7 — RECOMMENDATION**
State one of: Option A / Option B / Neither / Conditional on {X}.
Add:
- Reason sentence referencing the matrix
- Trade-off sentence naming what is given up
The recommendation must be explicit. "It depends" without resolution is not a recommendation.

---

**PHASE 8 — AMEND**
Three adjustment paths available:

1. **Add Option C** — Execute Phases 1A–4A structure for Option C. Expand the Phase 5 matrix. Update Phase 7 recommendation if evidence changes.
2. **Weight a dimension** — State dimension and weight. Recalculate which option is favored. State if the recommendation changes.
3. **Shift to exec or engineering audience** — Exec: Phase 7 leads with recommendation + business risk. Engineering: Phase 7 leads with feasibility + implementation complexity. Re-render Phases 1–4 output labels with audience-appropriate framing.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

## V-04 — Conversational / Question-Driven Register

**Axis**: Phrasing register
**Hypothesis**: Framing each analysis step as a question to answer (rather than an imperative to execute) produces more natural, non-symmetric analysis — reducing the "symmetric inertia" failure mode where both options receive identical commentary because the prompt treated them as a parallel list.

---

You are helping evaluate two approaches to **{topic}**.

Option A is: {option_a}
Option B is: {option_b}

Work through the questions below. Give a direct answer to each before moving on.

---

**First, what's the current situation?**

Before comparing A and B, describe what teams do today without either option. What problem does the existing approach solve, and how well? Keep it to two sentences. This is the status quo you're comparing against.

---

**Now look at Option A: {option_a}**

*Can it be built?* Is the team capable, the timeline realistic, and the scope manageable? Give a traffic-light rating (green / yellow / red) and say why.

*Would teams bother?* If Option A existed, would teams actually adopt it — or would they keep doing what they do now? Ask this against the status quo you described above, not against Option B. What makes Option A worth the switch? Rate the inertia risk (low / medium / high) and name the specific mechanism.

*What could go wrong?* Name the two biggest risks for Option A specifically. Rate each (low / medium / high).

*Where does it compete?* How does Option A stand out in the market? Name something concrete — speed, cost, ecosystem, lock-in, or switching cost dynamics. "More competitive" without specifics is not an answer.

---

**Now look at Option B: {option_b} — independently**

*Can it be built?* Traffic-light rating and reason.

*Would teams bother?* Ask the same question as above — against the status quo, not against Option A. Option B has its own inertia dynamics. Rate them separately and name the specific mechanism for Option B.

*What could go wrong?* Name Option B's two biggest risks. These should be different from Option A's risks. If they overlap, explain why.

*Where does it compete?* Concrete differentiator for Option B. If Option B positions similarly to Option A, say so and explain the implication.

---

**Now put it in a table**

Lay out what you found side by side. Include the status quo as a column so that inertia is visible as a comparison point, not just a narrative mention.

| | Status Quo | Option A | Option B |
|---|---|---|---|
| Feasibility | — | | |
| Inertia risk | anchor | | |
| Risk | — | | |
| Competitive position | baseline | | |

---

**Is either option even worth building?**

Look at the inertia ratings. If both options face strong inertia (teams would keep the status quo over either), say so explicitly. Could "build neither" be the right answer? You don't have to conclude that, but you have to address it.

---

**What's your recommendation?**

Pick one: Option A, Option B, Neither, or "conditional on X."

Say it plainly. Then say why. Then say what the person choosing this option gives up by not choosing the other one. One sentence each.

---

**How to adjust this analysis**

If you need to go further:

- **Add a third option** — Describe Option C, then answer the same four questions for it using the same status quo baseline. Add it to the table and update the recommendation.
- **Emphasize a specific dimension** — Tell me which dimension matters most and why. I'll re-weight the comparison and show whether the recommendation changes.
- **Change the audience** — If this is for executives, I'll lead with the recommendation and the business risk. If it's for engineers, I'll lead with feasibility and the hardest implementation problems. Tell me which and I'll re-render.

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`

---

## V-05 — Combined: Phase-Explicit + Inertia-First + Audience-Conditional

**Axes**: Lifecycle emphasis + Inertia framing + Phrasing register
**Hypothesis**: Combining (1) a named Option 0 phase that commits an anchor token before any analysis, (2) explicit bilateral phase separation for inertia, and (3) audience-conditional framing at Phase 0 maximizes aspirational coverage (C-08 Option 0 in matrix, C-09 audience calibration) while preserving essential and recommended criteria through structural enforcement.

---

You are running `discover-compare` for: **{topic}**
Option A: {option_a}
Option B: {option_b}

---

**PHASE 0 — OPTION 0: STATUS QUO + AUDIENCE REGISTER**

Part A — Status Quo:
Define what teams do today without either build option. One sentence. This is your inertia anchor.

ANCHOR[0] = {status quo in one sentence}

Inertia strength of status quo: LOW / MEDIUM / HIGH (how well does it meet the need today?)

Binding rule: every inertia analysis below must reference ANCHOR[0] by this token name. Do not paraphrase.

Part B — Audience register (if specified):
- If audience = exec: Phase 7 leads with recommendation + business risk. Phases 2A/2B compress feasibility, expand risk and competitive. Phase 5 table uses business-impact labels.
- If audience = engineering: Phase 7 leads with feasibility + implementation complexity. Phases 2A/2B expand feasibility detail. Phase 5 table uses effort and risk labels.
- If unspecified: use balanced register.

Print: "ANCHOR[0] committed. Register: {exec / engineering / balanced}."

---

**PHASE 1A — OPTION A: FEASIBILITY**
Evaluate {option_a} for buildability. Team capability, timeline, complexity.
Rating: GREEN / YELLOW / RED
Output: `FA: {rating} — {reason}`

**PHASE 1B — OPTION B: FEASIBILITY**
Evaluate {option_b} for buildability independently.
Rating: GREEN / YELLOW / RED
Output: `FB: {rating} — {reason}`

---

**PHASE 2A — OPTION A: INERTIA vs ANCHOR[0]**
TOKEN RECALL: ANCHOR[0] = {reproduce from Phase 0}

Compare Option A only against ANCHOR[0]. Not against Option B.
Would teams keep ANCHOR[0] instead of building Option A? Why or why not?
VERDICT A: LOW / MEDIUM / HIGH — {mechanism specific to Option A}

**PHASE 2B — OPTION B: INERTIA vs ANCHOR[0]**
TOKEN RECALL: ANCHOR[0] = {reproduce from Phase 0}

Compare Option B only against ANCHOR[0]. Not against Option A.
VERDICT B: LOW / MEDIUM / HIGH — {mechanism specific to Option B}

Independence constraint: VERDICT A must not reference Option B. VERDICT B must not reference Option A.

---

**PHASE 3A — OPTION A: RISK**
Top 2 risks specific to Option A. Rating per risk: LOW / MEDIUM / HIGH.
Output: `RA: {risk1/rating}, {risk2/rating}`

**PHASE 3B — OPTION B: RISK**
Top 2 risks specific to Option B. Differentiate from Option A's risks. If identical, explain why.
Output: `RB: {risk1/rating}, {risk2/rating}`

---

**PHASE 4A — OPTION A: COMPETITIVE POSITIONING**
One or more concrete differentiators for Option A in the market. No generic phrases.
Output: `CA: {positioning}`

**PHASE 4B — OPTION B: COMPETITIVE POSITIONING**
One or more concrete differentiators for Option B. Must be distinct from Option A's differentiators unless there is a specific reason for overlap.
Output: `CB: {positioning}`

---

**PHASE 5 — DECISION MATRIX**
TOKEN RECALL: ANCHOR[0] = {reproduce from Phase 0}

Assemble all phase outputs. Option 0 is a named column using ANCHOR[0] as the label.

| Dimension | Option 0: ANCHOR[0] | Option A | Option B |
|---|---|---|---|
| Feasibility | N/A | FA | FB |
| Inertia | this IS the anchor | VERDICT A | VERDICT B |
| Risk | N/A | RA | RB |
| Competitive | baseline | CA | CB |

Apply register from Phase 0 to table labels if exec or engineering was specified.

---

**PHASE 6 — BUILD/NO-BUILD GATE**
If VERDICT A = HIGH AND VERDICT B = HIGH: state "Build neither is a candidate recommendation." Identify the override condition that would change this, or conclude with Neither.
If only one is HIGH: note it as a risk factor for that option but proceed to recommendation.

---

**PHASE 7 — RECOMMENDATION**
TOKEN RECALL: ANCHOR[0] = {reproduce from Phase 0}

Apply register from Phase 0:
- Exec: lead with recommendation + business risk
- Engineering: lead with feasibility + implementation complexity
- Balanced: lead with recommendation + key matrix evidence

State: **Option A / Option B / Neither / Conditional on {X}**
- Recommendation sentence (traceable to Phase 5 matrix)
- Reason sentence
- Trade-off sentence (what is given up by not choosing the other option)

If recommendation diverges from matrix plurality, state the reason explicitly.

---

**PHASE 8 — AMEND**

Three paths:

1. **Add Option C** — Execute Phases 1A–4A for Option C. Use same ANCHOR[0] for inertia. Expand Phase 5 matrix. Update Phase 6 gate and Phase 7 recommendation.
2. **Weight dimension** — State dimension and weight. Re-score matrix under new weights. State if recommendation changes.
3. **Override audience register** — State exec or engineering. Re-render Phases 2A/2B emphasis and Phase 7 framing. Print: "Register override: {new register}."

Output artifact: `simulations/discover/compare/{topic}-compare-{date}.md`
