The complete v6 rubric is written to `simulations/quest/rubrics/program-plan-rubric-v6-2026-03-14.md`.

---

**v6 summary — two new criteria from R5 excellence signals:**

| ID | Criterion | Source | Discriminates |
|----|-----------|--------|---------------|
| **C-22** | Gate template embeds cascade-if-removed clause | R5-H04: V-04's gate format string contains "removing this gate: [cascade]" as a required element | V-04 passes; V-01/V-02/V-03/V-05 fail |
| **C-23** | Arc-strategy names first-gate cascade explicitly | R5 cross-variation: V-04 and V-05 specify "first gate (scout handoff)" in Step 8; V-01/V-02/V-03 use generic "any gate" | V-04 and V-05 pass; V-01/V-02/V-03 fail |

**Design principle behind both:** The same load-bearing-instruction insight that produced C-17 → C-18 → C-20 (each stricter placement of a forcing function) now extends to gates. C-17 says "include a what-if-removed clause somewhere." C-22 says "put it in the gate format string where it fires at every boundary." C-23 says "anchor Step 8 to the first gate specifically, which has the highest-leverage cascade."

**Scoring:** 165 total (75 pts aspirational, 15 x 5). Golden threshold: 132.

**R5 retroactive:**
- V-04: **165/165** (only variation to pass both C-22 and C-23)
- V-05: **160/165** (passes C-23, fails C-22)
- V-01/V-02/V-03: **155/165** (fail both)
 handoff) is removed"); V-01/V-02/V-03 fail ("what happens if any gate is removed" without first-gate anchoring). Source: R5 cross-variation finding. |

**Scoring:** 75 pts aspirational (15 x 5) -> **165 total** -> golden threshold **132** (~80% of max).

R5 retroactive scores:

| Variation | Score | Notes |
|-----------|-------|-------|
| V-01 | 155/165 | Fail C-22 (no cascade clause in gate template), fail C-23 (no first-gate specificity in Step 8) |
| V-02 | 155/165 | Fail C-22, fail C-23 |
| V-03 | 155/165 | Fail C-22, fail C-23 |
| V-04 | 165/165 | Pass C-22 ("removing this gate: [cascade]" in gate template) + pass C-23 ("first gate (scout handoff)" in Step 8) |
| V-05 | 160/165 | Fail C-22 (no cascade clause in gate template), pass C-23 ("first gate (scout handoff)" in Step 8) |

---

## Essential Criteria (60 pts total)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-01 | **Valid YAML structure** | correctness | Output is valid YAML with a top-level `stages` key. Each stage has at minimum: `name` (string), `skills` (list), `gate` (string), and the echo stage has `auto: true`. No syntax errors. |
| C-02 | **Echo stage contract** | correctness | The last stage is named `echo`, has an empty `skills` list (or `skills: []`), and is marked `auto: true`. No other stage is named `echo`. |
| C-03 | **All referenced skills are valid** | correctness | Every skill listed in any stage's `skills` array is a real Signal plugin skill (from the 47-skill catalog across 9 namespaces). No invented, misspelled, or hallucinated skill names. |
| C-04 | **Gates are present and non-trivial** | correctness | Every non-echo stage has a `gate` value that expresses a real condition (not empty string, not "done", not "proceed"). Gate states what signals or artifacts must exist before advancing. |
| C-05 | **Skills are ordered by dependency** | correctness | Scout-namespace skills appear before draft-namespace skills; draft before review or prove; the sequence does not require artifacts that have not yet been produced by an earlier stage. |

Weight per essential: 12 pts (5 criteria x 12 = 60 pts)

---

## Recommended Criteria (30 pts total)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-06 | **Stages group skills meaningfully** | depth | Each stage represents a coherent phase of work (e.g., "discovery", "validation", "synthesis") -- not one skill per stage and not all skills dumped in one stage. Grouping reflects logical workflow cohesion. |
| C-07 | **Gate conditions reference artifacts** | depth | At least half of the non-echo gates name specific artifact types or signal counts (e.g., "scout-feasibility artifact present", "3+ scout signals present") rather than stating abstract completion. |
| C-08 | **Stage names are descriptive** | format | Stage names are human-readable labels that communicate the phase intent (e.g., `discovery`, `evidence`, `validation`) -- not generic (`stage1`, `step2`) and not skill names reused as stage names. |

Weight per recommended: 10 pts (3 criteria x 10 = 30 pts)

---

## Aspirational Criteria (75 pts total)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-09 | **Strategic pacing across signal types** | depth | The plan shows deliberate signal-building strategy: early stages produce breadth signals (scout, draft), middle stages produce depth signals (prove, review), late stages synthesize (topic). The program reflects a coherent evidence arc, not just topological sort. |
| C-10 | **Gates are quantified where possible** | behavior | At least one gate specifies a minimum signal count or threshold (e.g., `gate: ">=2 scout signals and draft-spec artifact present"`). Quantified gates are machine-checkable in principle. |
| C-11 | **Skill catalog grounded inline** | reliability | The variation enumerates all valid skill names organized by namespace inline in the prompt -- not by reference to an external file. This eliminates hallucination risk for C-03 at the source rather than relying on post-hoc validation. Pass if all 47 skills are listed inline; fail if the prompt delegates to "see plugin-plan.md" or "use the catalog." |
| C-12 | **Actor-role framing for gates** | depth | Gate conditions are written in actor-role transition language (e.g., "researcher needs X before designer can proceed", "PM sign-off requires Y") rather than abstract artifact checklists alone. Actor framing naturally grounds gates in workflow transitions and produces C-07-passing conditions without additional instruction. |
| C-13 | **Quantified gate syntax instructed** | behavior | The variation embeds a concrete `>=N signal_type` syntax example directly inside the gate-writing instruction (not only in a general examples section). The inline example drives machine-checkable threshold syntax in output, producing C-10-passing gates reliably. |
| C-14 | **Naive-competitor framing** | reliability | The variation opens by naming the failure mode it is designed to defeat and the structural choice that defeats it. Pass if the variation contains an explicit contrast statement naming (a) a specific failure mode (e.g., "flat skill lists", "dependency-free stage ordering", "abstract gates") AND (b) the structural choice that addresses it. The verb form is flexible: "defeats that by," "breaks that pattern by requiring," "counters this by enforcing" are all equivalent -- the criterion is structural (both elements present), not lexical. Fail if only the failure mode is named without the structural response, or if only what the variation does is described without identifying the failure mode it defeats. |
| C-15 | **Why-this-position column in actor table** | depth | The actor ordering table includes a justification column where each entry contains both (a) a reason the actor belongs at that position AND (b) a consequence-of-displacement clause naming what breaks, fails, or is ungrounded if the actor is moved. Compact form is sufficient: a single sentence combining both elements (e.g., "Moved later: design targets an unvalidated problem") passes. Position rationale alone is insufficient (R3 finding: V-01 had rationale, failed C-15). Fail if entries contain position rationale only without a consequence-of-displacement clause, or if the column is present but entries are left blank. Prose depth is not required; one consequence-of-displacement sentence per actor passes. |
| C-16 | **Unified handoff+threshold gate template** | behavior | The variation specifies a single required gate format string that combines all three elements: actor names, `>=N` threshold, and artifact type (e.g., "[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present"). A unified template hits C-07, C-12, and C-13 simultaneously with no instruction density cost. Pass if a single format string incorporating all three elements appears in the gate-writing instruction; fail if these elements are specified separately or the template omits any one of them. |
| C-17 | **What-happens-if-removed clause** | depth | The arc-strategy step requires the model to answer "what happens if any gate is removed?" as part of producing the strategy statement. This forcing function distinguishes genuine arc reasoning (model can explain the consequence) from restatement (model paraphrases the artifact list). Pass if the arc-strategy instruction contains this clause or equivalent; fail if the strategy step only asks for a summary of what was prioritized. Note: C-22 and C-23 are stricter forms of this same forcing function -- a variation can pass C-17 while failing C-22 or C-23. |
| C-18 | **Column header frames displacement impossibility** | reliability | The actor table column header is phrased to ask why the actor *cannot be positioned earlier* or *what breaks if moved*, rather than why the actor *belongs* at that position. Displacement-impossibility framing keeps the forcing function visible at every row and drives consequence-of-displacement reasoning in each cell without relying on the model carrying an earlier instruction. Pass if the column header contains a displacement-impossibility clause (e.g., "cannot run earlier", "what breaks if moved earlier", "what is lost if displaced", "and what breaks if moved"); fail if the header names positive belonging only (e.g., "Why this position", "Rationale", "Position justification") without a consequence or impossibility clause. |
| C-19 | **Multi-hop downstream consequence cascade** | depth | At least one actor table entry traces a chain of two or more ordered downstream consequences -- not a single consequence but an explicit sequence across arc layers (e.g., "Moved later: design targets wrong problem -> review critiques a design anchored in assumptions -> prove tests a hypothesis without market grounding"). A multi-hop chain demonstrates causal chain awareness across the arc, not just first-order impact. Pass if at least one entry contains an ordered sequence of two or more downstream consequences using explicit sequencing (arrows, "then", "which means", numbered steps); fail if all entries contain single-consequence-of-displacement statements only, even if those statements are well-reasoned. The cascade must cross at least one arc-layer boundary (consequence in one namespace layer causing a problem in a later namespace layer). Single-actor cascades are sufficient; not every actor entry needs a cascade, only one. |
| C-20 | **Header embeds cascade notation and depth requirement** | reliability | The column header extends displacement-impossibility framing (C-18) to also specify cascade notation format (-> arrows) and minimum cascade depth (2+ ordered consequences crossing arc-layer boundaries) directly in the header text. The header is the most instruction-efficient placement because it fires as a visible reminder at every row during table construction, eliminating reliance on model memory of a separate instruction block. Pass if the header contains both a displacement-impossibility clause (C-18) AND an explicit cascade specification naming arrow notation and minimum depth -- e.g., "cannot run earlier -- and what cascade breaks downstream (use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries)"; fail if the cascade notation specification exists only in a separate instruction block, a post-table check, or is absent. A header that passes C-18 but omits cascade notation and depth fails C-20. Source: R4 finding -- V-01 (header embeds cascade requirement, 145/145) > V-02/V-03 (post-table cascade instruction, 140/145). |
| C-21 | **All actor entries demonstrate cascade depth** | depth | Every actor entry in the variation's actor table template demonstrates a -> cascade of 2+ ordered consequences crossing arc-layer boundaries -- not just one entry (C-19), but all entries. Full-table cascade coverage means every row serves as a cascade template with no single-consequence entries to anchor against. Pass if all actor entries in the variation's own actor table use -> notation with 2+ ordered downstream consequences crossing at least one arc-layer boundary; fail if any actor entry is single-consequence even if at least one entry passes C-19. A variation that passes C-19 (one cascade entry) but leaves remaining entries as single-consequence fails C-21. Source: R4 finding -- V-01 and V-05 (all six entries have 3-hop -> chains, 155/155 retroactive) vs. V-02/V-03/V-04 (all entries single-consequence, 140/155 retroactive). Note: 2-hop per row satisfies C-21 per criterion letter (R5-H03 resolution); 3-hop is above-minimum. |
| C-22 | **Gate template embeds cascade-if-removed clause** | behavior | The gate format string itself contains a required cascade-if-removed element at every non-echo gate -- e.g., "[Delivering actor] hands off to [Receiving actor] when >=N artifact_type -- removing this gate: [cascade consequence chain]". This extends C-17's what-happens-if-removed forcing function from a standalone arc-strategy step into every stage boundary, making cascade-consequence reasoning structural rather than deferred. Pass if the gate format string (in the gate-writing instruction, not only in Step 8 or an examples section) contains a cascade-if-removed clause as a required element; fail if cascade-if-removed reasoning exists only in the arc-strategy step. Source: R5-H04 resolution -- V-04 produces the strongest C-17 pass because "removing this gate: [cascade]" is embedded in the gate template itself; V-01/V-02/V-03/V-05 pass C-17 through Step 8 only, leaving each individual gate without a structural cascade-reasoning requirement. |
| C-23 | **Arc-strategy names first-gate cascade explicitly** | depth | The arc-strategy instruction (Step 8 or equivalent) requires the model to trace the multi-hop consequence cascade specifically for the first gate (scout handoff) removal, not just "any gate" in the abstract. First-gate specificity anchors arc-strategy reasoning in the most consequential cascade -- removing the first gate destabilizes all downstream arc layers simultaneously and is therefore the highest-leverage illustration of why gate ordering matters. Pass if the arc-strategy instruction contains an explicit "first gate" or "scout handoff" cascade specification (e.g., "what is the multi-hop consequence cascade if the first gate (scout handoff) is removed"); fail if the instruction only asks about "any gate" without first-gate anchoring, even if C-17 otherwise passes. Source: R5 cross-variation finding -- V-04 and V-05 both include "specifically, what is the multi-hop consequence cascade if the first gate (scout handoff) is removed" in Step 8; V-01/V-02/V-03 use "what happens if any gate is removed" without first-gate specificity. |

Weight per aspirational: 5 pts (15 criteria x 5 = 75 pts)

---

## Scoring Worksheet

```
Essential:    C-01 [ ] C-02 [ ] C-03 [ ] C-04 [ ] C-05 [ ]
              Pass count: ___ / 5   -> ___ * 12 = ___ pts (of 60)

Recommended:  C-06 [ ] C-07 [ ] C-08 [ ]
              Pass count: ___ / 3   -> ___ * 10 = ___ pts (of 30)

Aspirational: C-09 [ ] C-10 [ ] C-11 [ ] C-12 [ ] C-13 [ ]
              C-14 [ ] C-15 [ ] C-16 [ ] C-17 [ ] C-18 [ ]
              C-19 [ ] C-20 [ ] C-21 [ ] C-22 [ ] C-23 [ ]
              Pass count: ___ / 15  -> ___ * 5  = ___ pts (of 75)

Composite score: ___ / 165

Golden: all essential pass AND composite >= 132  ->  [ ] YES  [ ] NO
```

---

## Notes for Scorers

- **C-01**: Check YAML validity first. If YAML is invalid, score C-01 fail and note -- remaining
  criteria may still be partially assessable from intent.
- **C-02**: Echo stage is a hard contract. If missing or misplaced, C-02 fails regardless of
  otherwise good structure.
- **C-03**: Use the 47-skill catalog in `plugin-plan.md` as the authority for valid skill names.
  Namespace-qualified names (`scout:feasibility`) and unqualified names (`feasibility`) both
  acceptable if unambiguous.
- **C-05**: Dependency order is assessed by namespace layer (scout -> draft -> review/prove -> topic),
  not strict alphabetical. Within a namespace, order is flexible.
- **C-07**: "References artifacts" means the gate text includes artifact type names, not that it
  invokes the artifact system at runtime. This is a plan, not an executor.
- **C-11**: This is a prompt-design criterion evaluated on the variation, not the output. Check
  whether the variation text itself contains an inline listing of skills by namespace. A pointer
  like "refer to plugin-plan.md" fails; a block like "valid scout skills: feasibility, market,
  naming, ..." passes.
- **C-12**: Actor framing is assessed in the gate text of the output. Look for role-transition
  language ("before X can proceed", "Y needs Z to hand off") in addition to artifact references.
  Pure artifact lists without role context do not pass C-12.
- **C-13**: Distinguished from C-10 by scope: C-10 checks whether any output gate is quantified;
  C-13 checks whether the *variation* contains an embedded `>=N` syntax example inside its
  gate-writing instruction. A variation can pass C-13 but still fail C-10 (if the instruction
  is present but the model ignored it).
- **C-14**: Evaluated on the variation text, not the output. The contrast statement must name a
  *specific* failure mode (e.g., "flat skill lists", "dependency-free stage ordering", "abstract
  gates") -- not a generic claim like "this is better than naive approaches." The failure mode
  named should be the one the variation's structural choices actually defeat. The verb form is
  flexible: "defeats," "breaks that pattern by requiring," "counters," "addresses" are all
  equivalent. Both elements must be present (failure mode + structural response).
- **C-15**: Evaluated on the variation text. An actor table where each entry has both a position
  reason AND a consequence-of-displacement clause passes. Position rationale alone fails (R3
  finding: V-01 had rationale, failed C-15 -- the gap is absence of "what breaks if moved"
  reasoning). Compact form is sufficient (R3 finding: V-03's one-sentence consequence entries
  passed). Prose depth is not required.
- **C-16**: The template must appear *inside* the gate-writing instruction, not only in an
  examples section. A format string that omits actor names (threshold + artifact only) passes
  C-13 but not C-16. All three elements -- actor, threshold, artifact -- must appear in one
  required format.
- **C-17**: Evaluated on the variation text. The clause can take any form ("explain what would
  break if this gate were removed", "state the consequence of skipping this gate", etc.) as long
  as it requires the model to reason about gate removal consequences. A step that only asks for
  a summary of what was prioritized does not pass C-17. Note: C-22 and C-23 are stricter forms
  of this same forcing function -- a variation can pass C-17 while failing C-22 or C-23.
- **C-18**: Evaluated on the variation text -- specifically the column header text for the actor
  table's justification column. The boundary case: "Why this position" fails; "Why this position
  (what breaks if moved earlier)" passes; "Why this actor cannot run earlier" passes; "Position
  rationale" fails; "Justification" fails. The key test: does the header direct the model toward
  *displacement impossibility or consequence* rather than *position belonging*? Headers phrased
  as "why cannot" or "what breaks if" pass; headers phrased as "why this" or "rationale" without
  a consequence clause fail.
- **C-19**: Evaluated on the variation output -- the actor table entries themselves. A cascade
  requires two or more ordered consequences using explicit sequencing (arrows, "then", numbered
  steps, "which means"). A single consequence restated in multiple clauses does not count. The
  chain must cross at least one arc-layer boundary (e.g., a consequence in the design layer that
  causes a problem in the validation layer). Single-actor cascades are sufficient; not every actor
  entry needs a cascade, only one.
- **C-20**: Evaluated on the variation text -- specifically the column header. Distinguished from
  C-18: C-18 requires displacement-impossibility framing; C-20 requires that same header to *also*
  specify cascade notation format (-> arrows) and minimum depth (2+ ordered consequences, arc-layer
  crossing). A header passes C-18 but fails C-20 if it contains "cannot run earlier" without
  cascade specification. Post-table cascade checks do not substitute: the header must be the
  location of the cascade specification.
- **C-21**: Evaluated on the variation text -- all actor entries in the actor table template.
  Distinguished from C-19: C-19 requires at least one cascade entry; C-21 requires every entry
  to be a cascade. Inspect each actor row in the variation's table. If any row is single-consequence
  (even one), C-21 fails. Note: 2-hop per row satisfies C-21 per criterion letter (R5-H03
  resolution); 3-hop is above-minimum.
- **C-22**: Evaluated on the variation text -- specifically the gate format string in the
  gate-writing instruction. The cascade-if-removed clause must appear inside the format string
  itself (e.g., "-- removing this gate: [cascade chain]"), not only in Step 8 or a separate
  instruction block. A variation that passes C-17 through Step 8 alone fails C-22. The format
  string must contain all four elements: delivering actor, receiving actor, threshold+artifact,
  AND cascade-if-removed. A C-16-passing format string (first three elements only) without
  cascade-if-removed fails C-22. Source: R5-H04 -- V-04 is the only R5 variation to embed
  "removing this gate: [cascade]" in the gate template; V-01/V-02/V-03/V-05 pass C-17 via
  Step 8 but leave individual gates without a cascade-reasoning requirement.
- **C-23**: Evaluated on the variation text -- specifically the arc-strategy instruction (Step 8
  or equivalent). The criterion distinguishes first-gate specificity from generic any-gate
  instruction. "What happens if any gate is removed" passes C-17 but fails C-23. "What is the
  multi-hop consequence cascade if the first gate (scout handoff) is removed" passes both C-17
  and C-23. The phrase "first gate" or "scout handoff" (or equivalent identifying the earliest
  boundary) must appear in the arc-strategy instruction. Source: R5 cross-variation finding --
  V-04 and V-05 include first-gate specificity; V-01/V-02/V-03 do not. The first gate is the
  highest-leverage cascade illustration because its removal propagates across all downstream arc
  layers simultaneously.

---

## Version Delta

### v5 -> v6

| Change | Detail |
|--------|--------|
| Added C-22 | Gate template embeds cascade-if-removed clause -- from R5-H04 resolution: V-04's gate format string contains "removing this gate: [cascade]" as a required element, producing the strongest C-17 pass by making cascade-consequence reasoning structural at every stage boundary. The load-bearing-instruction principle (C-17, C-18, C-20) generalizes: the gate format string is to gate content what the column header is to actor table row content. V-04 passes; V-01/V-02/V-03/V-05 fail. |
| Added C-23 | Arc-strategy names first-gate cascade explicitly -- from R5 cross-variation finding: V-04 and V-05 both anchor Step 8 with "specifically, what is the multi-hop consequence cascade if the first gate (scout handoff) is removed", producing more precise arc-strategy statements than generic "any gate" instruction. First-gate specificity forces the highest-leverage cascade illustration (all downstream layers simultaneously destabilized). V-04 and V-05 pass; V-01/V-02/V-03 fail. |
| Aspirational tier | 13 criteria x 5 pts -> 15 criteria x 5 pts = 75 pts |
| Total points | 155 -> 165 |
| Golden threshold | composite >= 124 -> composite >= 132 (same ~80% of max) |
| R5 best scores retroactive | V-04: 165/165 (pass C-22 + pass C-23 -- gate-template cascade and first-gate arc-strategy); V-05: 160/165 (fail C-22, pass C-23 -- first-gate arc-strategy without gate-template cascade clause); V-01/V-02/V-03: 155/165 (fail C-22, fail C-23). C-22 and C-23 are the new ceiling gap for R6. |

### v4 -> v5

| Change | Detail |
|--------|--------|
| Added C-20 | Header embeds cascade notation and depth requirement -- from R4 finding: V-01 (header embeds "use -> arrows, 2+ ordered consequences, crossing arc-layer boundaries", 145/145) outperforms V-02/V-03 (post-table cascade instruction, 140/145). The C-18 header-loading principle generalizes to cascade depth: whatever requirement belongs in every row belongs in the header. R4-H01 and R4-H02 resolution. |
| Added C-21 | All actor entries demonstrate cascade depth -- from R4 finding: V-01 and V-05 (all entries have 3-hop -> chains) both reach the 145/145 ceiling; V-02/V-03/V-04 (all entries single-consequence) score 140/145. C-19 requires at least one cascade; C-21 requires all entries to be cascades. Full-table cascade coverage is the maximum-density form of the demonstrated-entry pattern. R4-H04 resolution. |
| Aspirational tier | 11 criteria x 5 pts -> 13 criteria x 5 pts = 65 pts |
| Total points | 145 -> 155 |
| Golden threshold | composite >= 116 -> composite >= 124 (same ~80% of max) |

### v3 -> v4

| Change | Detail |
|--------|--------|
| Updated C-14 pass condition | Verb form clarified as flexible -- "defeats," "breaks that pattern by requiring," "counters" are equivalent. Criterion is structural (both elements present), not lexical. Source: R3-H01 resolution. |
| Updated C-15 pass condition | Tightened: position rationale alone is insufficient. Pass now requires a consequence-of-displacement clause per actor in addition to position rationale. Source: R3-H02 resolution. |
| Added C-18 | Column header frames displacement impossibility -- from R3 finding: header formulation is load-bearing for C-15 reliability. |
| Added C-19 | Multi-hop downstream consequence cascade -- from R3 finding: V-05 traced 2-3 ordered downstream consequences per actor; all scored 135/135 under v3. C-19 opens territory above the v3 ceiling. |
| Aspirational tier | 9 criteria x 5 pts -> 11 criteria x 5 pts = 55 pts |
| Total points | 135 -> 145 |
| Golden threshold | composite >= 108 -> composite >= 116 |

### v2 -> v3

| Change | Detail |
|--------|--------|
| Added C-14 | Naive-competitor framing -- from R2 finding: contrast opener primes principled arc reasoning |
| Added C-15 | Why-this-position column -- from R2 finding: actor table justification column produces C-09-passing causal logic inline |
| Added C-16 | Unified handoff+threshold gate template -- from R2 finding: single format string combining actor+threshold+artifact |
| Added C-17 | What-happens-if-removed clause -- from R2 finding: forcing function distinguishing genuine arc reasoning from restatement |
| Aspirational tier | 5 criteria x 5 pts -> 9 criteria x 5 pts = 45 pts |
| Total points | 115 -> 135 |
| Golden threshold | composite >= 92 -> composite >= 108 |

### v1 -> v2

| Change | Detail |
|--------|--------|
| Added C-11 | Skill catalog grounded inline -- from R1 finding: V-04 only golden because it enumerated all 47 skills inline |
| Added C-12 | Actor-role framing for gates -- from R1 finding |
| Added C-13 | Quantified gate syntax instructed -- from R1 finding: V-05 embedded `>=N` syntax in requirement |
| Aspirational tier | 2 criteria x 5 pts -> 5 criteria x 5 pts = 25 pts |
| Total points | 100 -> 115 |
| Golden threshold | composite >= 80 -> composite >= 92 |
