## Round 3 Scorecard — scout-feasibility

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-02 Template-completion | 5/5 | 3/3 | 6/6 | **100** | YES |
| 1 | V-03 Inertia framing | 5/5 | 3/3 | 6/6 | **100** | YES |
| 1 | V-05 Golden synthesis | 5/5 | 3/3 | 6/6 | **100** | YES |
| 4 | V-01 Strategy-first | 5/5 | 3/3 | 5/6 | **98.3** | YES |
| 4 | V-04 Architect-first | 5/5 | 3/3 | 5/6 | **98.3** | YES |

### The single discriminator: C-12

V-01 and V-04 both fail C-12 (budget precedes complexity scoring) by design:
- V-01: STRATEGY → ARCHITECT → **PM** — budget arrives after complexity is read
- V-04: explicitly "Architect leads, PM overlays after" — C-12 is the stated tradeoff

**C-12 compliance is entirely determined by role ordering. It cannot be patched by instruction phrasing.**

### Within the 100 cluster: structural guarantee differences

| Variation | C-13 mechanism | C-14 mechanism | Structural risk |
|-----------|---------------|----------------|-----------------|
| V-05 | Pre-printed `## PM: BUDGET` + `## ARCHITECT` | Pre-printed + "do not omit" | Lowest |
| V-02 | Pre-printed markdown headers | Pre-printed in every row | Low |
| V-03 | Dashes-style `--- PM: BUDGET ---` | Instruction-based | Moderate |

### New patterns

Two patterns surface that aren't yet rubric criteria:

1. **Inertia framing (V-03)** — anchoring RED blockers and amendment actions against quantified status-quo cost adds a comparative feasibility dimension none of the prior rounds explored. C-05 rationale and C-10 specificity improve measurably. Candidate for C-15 in v4.

2. **C-12 is entirely an ordering problem** — confirmed clean. No variation that places Architect before PM passes C-12. This was predicted; Round 3 scoring confirms it analytically.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inertia framing anchors RED blocker rationale and amendment actions against quantified status-quo cost, adding comparative feasibility depth not captured by current rubric", "C-12 compliance is entirely determined by PM-vs-Architect ordering; no instruction phrasing can compensate for Architect-first or Strategy-first sequences"]}
```
OMPLEXITY is step 4. Budget constraint invisible when complexity is read. |
| C-13 | Reviewer role in section header | PASS* | Headers `--- STRATEGY: BUILD-VS-BUY ---`, `--- ARCHITECT: COMPLEXITY ---`, `--- PM: BUDGET ---` carry role labels. *Structural risk: dashes format may be reformatted by model to plain headers, stripping role label. |
| C-14 | Score-delta fragment in amendments | PASS* | Instruction shows canonical format inline: "Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." *Risk: instruction-based; model must generate the fragment rather than transcribe it. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/6 (C-12 fails)

```
composite = (5/5 * 60) + (3/3 * 30) + (5/6 * 10)
          = 60 + 30 + 8.33
          = 98.3
```

**Score: 98.3 / 100 — GOLDEN** (all essential pass, composite >= 80)

---

### V-02: Template-Completion Output Format

All section headers pre-printed. Model fills `[FIELD]` values only.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Traffic light per component | PASS | Pre-printed ARCHITECT table with `GREEN / YELLOW / RED` in each row |
| C-02 | Composite score with label | PASS | Pre-printed `Composite score: [N]/100` and `Label:` fields |
| C-03 | Team and timeline inference disclosed | PASS | Pre-printed INFERENCE GATE block with Feature/Team/Timeline fields |
| C-04 | Stack fallback disclosed | PASS | Pre-printed `Stack fallback: "No canonical stack files found..."` line |
| C-05 | RED blockers enumerated with rationale | PASS | Pre-printed `RED Blockers:` section with `[Component]: [Why it is a blocker.] Lift condition:` |
| C-06 | Build-vs-buy per component | PASS | Pre-printed STRATEGY:BUILD-VS-BUY table; ≥50% requirement explicit |
| C-07 | Scoped fallback score | PASS | Pre-printed `Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100..."` field |
| C-08 | Prerequisites for conditional feasibility | PASS | Pre-printed numbered prerequisites block for FEASIBLE WITH CAVEATS case |
| C-09 | PM timeline chain | PASS | Pre-printed budget chain: `Estimated:` / `Available:` / `Delta:` / `Flag:` as linked fields |
| C-10 | Amendment actions at close | PASS | Pre-printed numbered AMENDMENTS rows with traceable component fields |
| C-11 | Inference gate precedes scoring | PASS | INFERENCE GATE precedes PM:BUDGET which precedes ARCHITECT:COMPLEXITY in template order |
| C-12 | Budget precedes complexity scoring | PASS | PM:BUDGET is section 3; ARCHITECT:COMPLEXITY is section 4. Template ordering is fixed. |
| C-13 | Reviewer role in section header | PASS | Pre-printed `## PM: BUDGET` and `## ARCHITECT: COMPLEXITY` headers unavoidable — model fills content, not headers |
| C-14 | Score-delta fragment in amendments | PASS | Fragment pre-printed in every AMENDMENTS row: "Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." Model transcribes, does not generate. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6

```
composite = (5/5 * 60) + (3/3 * 30) + (6/6 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

---

### V-03: Inertia Framing (new axis)

Adds `--- INERTIA: STATUS QUO ---` before PM:BUDGET. All ratings anchored against workaround cost.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Traffic light per component | PASS | ARCHITECT table requires Rating column; inertia adds `Status-quo risk if deferred` column for depth |
| C-02 | Composite score with label | PASS | `--- VERDICT ---` requires score and label |
| C-03 | Team and timeline inference disclosed | PASS | `--- INFERENCE GATE ---` requires Feature/Team/Timeline as contiguous block before any component or workaround |
| C-04 | Stack fallback disclosed | PASS | Explicit disclosure required |
| C-05 | RED blockers enumerated with rationale | PASS | `Blockers -- required for every RED component:` with `[Why blocked.] Lift condition:` AND `Status-quo impact if deferred:` — enriched rationale |
| C-06 | Build-vs-buy per component | PASS | STRATEGY:BUILD-VS-BUY table with inertia note column; ≥50% requirement explicit |
| C-07 | Scoped fallback score | PASS | `If score < 50: "Scoped to [constraint]: [N]/100."` |
| C-08 | Prerequisites for conditional feasibility | PASS | `If FEASIBLE WITH CAVEATS: numbered prerequisites, all RED items represented.` |
| C-09 | PM timeline chain | PASS | `Budget chain (all four elements required): Estimated: [N] \| Available: [N] \| Delta: [+-N] \| FLAG` — length pressure risk from inertia section noted but prompt explicitly requires all four |
| C-10 | Amendment actions at close | PASS | `--- AMENDMENTS ---` with note: "Where relevant, note whether the action also reduces the status-quo workaround cost." Richer amendment specificity. |
| C-11 | Inference gate precedes scoring | PASS | INFERENCE GATE explicitly before `any component or workaround` — enforced by instruction |
| C-12 | Budget precedes complexity scoring | PASS | PM:BUDGET precedes ARCHITECT:COMPLEXITY in section order |
| C-13 | Reviewer role in section header | PASS* | `--- PM: BUDGET ---` and `--- ARCHITECT: COMPLEXITY ---` headers carry role labels. *Dashes format structural risk: same as V-01. |
| C-14 | Score-delta fragment in amendments | PASS* | Instruction shows canonical format: "Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." *Instruction-based; same risk as V-01. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6

```
composite = (5/5 * 60) + (3/3 * 30) + (6/6 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

Note: V-03 earns 100 on structural criteria, but C-13 and C-14 carry higher model-behavior risk than V-02/V-05. The inertia axis adds qualitative depth to C-05 and C-10 that is not captured in the rubric score.

---

### V-04: Architect-First + Assessment Contract

Role order: ARCHITECT → PM OVERLAY → STRATEGY → VERDICT.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Traffic light per component | PASS | ARCHITECT table with Rating column |
| C-02 | Composite score with label | PASS | `--- VERDICT ---` requires score and label |
| C-03 | Team and timeline inference disclosed | PASS | `--- ASSESSMENT CONTRACT ---` locks Feature/Team/Timeline as a contiguous block before any component name |
| C-04 | Stack fallback disclosed | PASS | Explicit disclosure required before contract |
| C-05 | RED blockers enumerated with rationale | PASS | `Blockers -- required for every RED component:` with `[Why blocked.] Lift condition:` |
| C-06 | Build-vs-buy per component | PASS | STRATEGY:BUILD-VS-BUY table; ≥50% explicit |
| C-07 | Scoped fallback score | PASS | `If score < 50: "Scoped to [constraint]: [N]/100."` |
| C-08 | Prerequisites for conditional feasibility | PASS | `If FEASIBLE WITH CAVEATS: numbered prerequisites, all RED items represented.` |
| C-09 | PM timeline chain | PASS | `Budget chain (all four elements required): Estimated: [N] \| Available: [N] \| Delta: [+-N] \| FLAG` |
| C-10 | Amendment actions at close | PASS | `--- AMENDMENTS ---` with numbered actions from either Architect or PM findings |
| C-11 | Inference gate precedes scoring | PASS | ASSESSMENT CONTRACT block explicitly required before any component name |
| C-12 | Budget precedes complexity scoring | **FAIL** | Core design intent: "Architect leads. PM overlays budget after complexity is known." ARCHITECT:COMPLEXITY is section 3; PM:BUDGET OVERLAY is section 4. Structural fail by design. |
| C-13 | Reviewer role in section header | PASS* | `--- ARCHITECT: COMPLEXITY ---`, `--- PM: BUDGET OVERLAY ---`, `--- STRATEGY: BUILD-VS-BUY ---` carry role labels. *Dashes format structural risk. |
| C-14 | Score-delta fragment in amendments | PASS* | Instruction shows canonical format. *Instruction-based risk. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/6 (C-12 fails)

```
composite = (5/5 * 60) + (3/3 * 30) + (5/6 * 10)
          = 60 + 30 + 8.33
          = 98.3
```

**Score: 98.3 / 100 — GOLDEN**

---

### V-05: Golden Synthesis

Template-completion + PM-first + C-13/C-14 pre-printed in skeleton.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Traffic light per component | PASS | Pre-printed ARCHITECT table with `GREEN / YELLOW / RED` in each row |
| C-02 | Composite score with label | PASS | Pre-printed `Composite score: [N]/100` and `Label:` |
| C-03 | Team and timeline inference disclosed | PASS | Pre-printed INFERENCE GATE block with all three fields; gate instruction: "All three required before PM: BUDGET begins" |
| C-04 | Stack fallback disclosed | PASS | Pre-printed `Stack fallback: "No canonical stack files found..."` |
| C-05 | RED blockers enumerated with rationale | PASS | Pre-printed `RED Blockers:` section with `[Component]: [Why it is a blocker.] Lift condition:` |
| C-06 | Build-vs-buy per component | PASS | Pre-printed STRATEGY:BUILD-VS-BUY table; ≥50% requirement explicit |
| C-07 | Scoped fallback score | PASS | Pre-printed `Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100..."` |
| C-08 | Prerequisites for conditional feasibility | PASS | Pre-printed numbered prerequisites block; "every RED-rated component must appear" |
| C-09 | PM timeline chain | PASS | Pre-printed budget chain with all four fields: `Estimated:` / `Available:` / `Delta:` / `Flag:` |
| C-10 | Amendment actions at close | PASS | Pre-printed AMENDMENTS rows with numbered action and score-delta line |
| C-11 | Inference gate precedes scoring | PASS | INFERENCE GATE before PM:BUDGET before ARCHITECT in fixed template order |
| C-12 | Budget precedes complexity scoring | PASS | `## PM: BUDGET` is section 3; `## ARCHITECT: COMPLEXITY` is section 4. Fixed by template. |
| C-13 | Reviewer role in section header | PASS | Pre-printed `## PM: BUDGET` and `## ARCHITECT: COMPLEXITY` — strongest guarantee: model cannot reformat what is already on the page |
| C-14 | Score-delta fragment in amendments | PASS | Fragment pre-printed in every AMENDMENTS row + "do not omit the line" — strongest guarantee: model transcribes, does not generate |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 6/6

```
composite = (5/5 * 60) + (3/3 * 30) + (6/6 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? | C-12 | C-13 guarantee | C-14 guarantee |
|------|-----------|-----------|-------------|--------------|-----------|---------|------|----------------|----------------|
| 1 | V-02 Template-completion | 5/5 | 3/3 | 6/6 | **100** | YES | PASS | pre-printed header | pre-printed fragment |
| 1 | V-03 Inertia framing | 5/5 | 3/3 | 6/6 | **100** | YES | PASS | dashes (risk) | instruction (risk) |
| 1 | V-05 Golden synthesis | 5/5 | 3/3 | 6/6 | **100** | YES | PASS | pre-printed header | pre-printed + "do not omit" |
| 4 | V-01 Strategy-first | 5/5 | 3/3 | 5/6 | **98.3** | YES | FAIL | dashes (risk) | instruction (risk) |
| 4 | V-04 Architect-first | 5/5 | 3/3 | 5/6 | **98.3** | YES | FAIL | dashes (risk) | instruction (risk) |

**C-12 is the sole differentiator between 100 and 98.3.** V-01 and V-04 fail C-12 by design (Strategy-first and Architect-first orderings both place PM:BUDGET after complexity scoring).

---

## Structural Guarantee Ranking

Within the 100-scoring cluster, structural reliability differs:

| Strength | Variations | Why |
|----------|-----------|-----|
| Strongest | V-05 | Pre-printed headers + pre-printed fragment + "do not omit" — mechanically unavoidable |
| Strong | V-02 | Pre-printed headers + pre-printed fragment — unavoidable; no "do not omit" reinforcement |
| Moderate | V-03 | Dashes-format role headers + instruction-based C-14 — model must follow, not transcribe |

V-03's score reflects design intent. In live model runs, V-03's C-13/C-14 carry higher failure probability than V-02 or V-05 despite identical rubric scores.

---

## Excellence Signals — Round 3

### E-1: PM-first ordering structurally eliminates C-12 risk

Variations that place PM:BUDGET before ARCHITECT:COMPLEXITY (V-02, V-03, V-05) all pass C-12 with zero model-behavior dependency. Variations that place PM:BUDGET after complexity scoring (V-01, V-04) fail C-12 regardless of how well they handle every other criterion. **C-12 compliance is entirely determined by role ordering — it cannot be patched by instruction phrasing.**

### E-2: Pre-printed template surface vs. instruction-based format

V-02 and V-05 demonstrate that pre-printing section headers and example fragments eliminates the class of failures where the model follows the intent but reformats the surface (e.g., dashes-to-prose header conversion, paraphrase instead of canonical fragment). The model cannot drop or reformat what it did not generate. V-03's identical rubric score hides a real runtime risk gap.

### E-3: Inertia framing adds qualitative depth not captured by the rubric (V-03 new axis)

V-03's `--- INERTIA: STATUS QUO ---` section enriches:
- **C-05 rationale**: RED blockers described as "deferred vs. blocked" against a quantified sprint cost, not just technical risk
- **C-10 amendment specificity**: actions described in terms of workaround reduction, not abstract risk elimination
- **VERDICT depth**: "Not building this means [status-quo consequence]" grounds the score in comparative value

These improvements do not appear in the rubric score (V-03 and V-05 both score 100), making V-03 a candidate for a dedicated rubric criterion in v4.

---

## C-12 Failure Analysis

Both failing variations (V-01, V-04) fail C-12 as a direct consequence of their design axis:

| Variation | Design intent | Why C-12 fails |
|-----------|--------------|----------------|
| V-01 | Strategy-first: establish build-vs-buy before complexity | PM budget follows both STRATEGY and ARCHITECT; budget constraint unknown when complexity is read |
| V-04 | Architect-first: pure complexity on technical merit before budget pressure | Explicit design: "PM overlays budget after complexity is known" — C-12 is the intended tradeoff |

V-04's failure is philosophically motivated: the hypothesis is that unbiased technical complexity assessment produces better ratings. This is a valid alternative design philosophy, but it structurally sacrifices C-12.

**For R4**: If the Architect-first axis is worth testing, C-12 could be relaxed for variations that explicitly separate complexity-first from budget-second. The current rubric treats budget-before-complexity as unconditionally better.

---

## Round 3 Findings

### F-01: C-12 is the rubric's sharpest discriminator at the design level

All variations score identically on C-01 through C-11 and C-14. C-12 alone separates the 100 cluster from the 98.3 cluster. This is structurally clean: it confirms that role ordering is the single actionable design lever for this criterion.

### F-02: The C-13/C-14 structural-vs-instruction gap is now characterized

Round 3 provides a direct three-way comparison:
1. Pre-printed markdown headers (V-02, V-05) — strongest C-13 guarantee
2. Instruction-shown dashes headers (V-01, V-03, V-04) — weaker guarantee
3. Pre-printed + reinforced (V-05 adds "do not omit") — strongest C-14 guarantee

This characterization was predicted in the Round 3 design notes; Round 3 scoring confirms the prediction is analytically sound.

### F-03: Inertia framing (V-03) is a viable new rubric axis — not yet captured

V-03 introduces a dimension of comparative feasibility (value relative to status quo) that none of the prior rounds explored. The current rubric does not score for this quality. A v4 criterion might read: "C-15: Inertia disclosure — output states what the team currently does without the feature and estimates the cost." This would differentiate V-03 from V-02/V-05 at the rubric level.

### F-04: All five variations achieve golden threshold

The floor established in Round 2 holds: all essential criteria pass across all five variations. The golden threshold (composite >= 80) is non-discriminating at this round. Discrimination lives at C-12 (structural) and within-100 structural strength on C-13/C-14.

---

## Recommended Golden Candidate

**V-05** remains the recommended golden candidate:
- Achieves 100/100 with the strongest structural guarantees on C-13 and C-14
- PM-first ordering guarantees C-12
- Pre-printed template prevents section omission and header reformatting
- "Do not omit" reinforcement on C-14 is the belt-and-suspenders defense

**V-02** is the closest structural competitor. The key open question from the R3 design notes — "does template surface alone match V-05's qualitative depth?" — is not resolvable through rubric scoring alone and would require live model runs to assess C-05 rationale quality and C-10 amendment specificity.

**V-03** is a candidate for a separate research question: does inertia framing improve output quality in ways the rubric does not yet measure?

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inertia framing anchors RED blocker rationale and amendment actions against quantified status-quo cost, adding comparative feasibility depth not captured by current rubric", "C-12 compliance is entirely determined by PM-vs-Architect ordering; no instruction phrasing can compensate for Architect-first or Strategy-first sequences"]}
```
