Written to `simulations/quest/rubrics/program-plan-rubric-v4-2026-03-14.md`.

---

**What changed in v4:**

Two new aspirational criteria from R3 excellence signals, plus pass condition tightening on C-14 and C-15:

| ID | Criterion | Source pattern |
|----|-----------|----------------|
| C-18 | **Column header frames displacement impossibility** | V-01 failed C-15 despite per-actor rationale because its header said "Why this position" (positive-belonging framing). All passing variations (V-02 through V-05) had headers phrased around displacement impossibility or consequence — "cannot run earlier", "what breaks if moved earlier". The header is load-bearing: it keeps the forcing function visible at every row. |
| C-19 | **Multi-hop downstream consequence cascade** | V-05's entries traced 2-3 ordered downstream consequences across arc-layer boundaries. V-03/V-04 had single-consequence entries and still scored 135/135 under v3 — meaning C-19 opens territory above the v3 ceiling. V-05 is the only R3 variation that retroactively passes it. |

**Pass condition tightening:**
- C-14: Verb form clarified as flexible ("defeats," "breaks that pattern by requiring," "counters" are equivalent). Structural criterion is presence of both elements, not lexical form.
- C-15: Position rationale alone is now explicitly insufficient. Must include a consequence-of-displacement clause. Compact form (one sentence) passes. V-01's fail archetype: had rationale, no "what breaks if moved" reasoning.

**Scoring:**
- Aspirational: 9 × 5 → 11 × 5 = **55 pts**
- Total: 135 → **145 pts**
- Golden threshold: 108 → **116** (~80% of max)
- R3 retroactive: V-03/V-04 score 140/145 (pass C-18, fail C-19); V-05 scores **145/145** (cascade present). C-19 is the new ceiling gap.
requires a consequence-of-displacement clause per actor. Compact
  form (one sentence combining position reason and displacement consequence) is sufficient. Source:
  R3-H02 resolution + V-01 fail pattern.

**Scoring adjustment:** aspirational grows from 45 pts (9 x 5) to 55 pts (11 x 5). Total moves
to **145**. Golden threshold adjusts from 108 to **116** (~80% of max). R3's V-03 and V-04
(135/135) retroactively score 140/145; V-05 (135/135) retroactively scores 145/145 -- the C-19
cascade is what R4 variations should close.

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

## Aspirational Criteria (55 pts total)

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
| C-17 | **What-happens-if-removed clause** | depth | The arc-strategy step requires the model to answer "what happens if any gate is removed?" as part of producing the strategy statement. This forcing function distinguishes genuine arc reasoning (model can explain the consequence) from restatement (model paraphrases the artifact list). Pass if the arc-strategy instruction contains this clause or equivalent; fail if the strategy step only asks for a summary of what was prioritized. |
| C-18 | **Column header frames displacement impossibility** | reliability | The actor table column header is phrased to ask why the actor *cannot be positioned earlier* or *what breaks if moved*, rather than why the actor *belongs* at that position. Displacement-impossibility framing keeps the forcing function visible at every row and drives consequence-of-displacement reasoning in each cell without relying on the model carrying an earlier instruction. Pass if the column header contains a displacement-impossibility clause (e.g., "cannot run earlier", "what breaks if moved earlier", "what is lost if displaced", "and what breaks if moved"); fail if the header names positive belonging only (e.g., "Why this position", "Rationale", "Position justification") without a consequence or impossibility clause. |
| C-19 | **Multi-hop downstream consequence cascade** | depth | At least one actor table entry traces a chain of two or more ordered downstream consequences -- not a single consequence but an explicit sequence across arc layers (e.g., "Moved later: design targets wrong problem -> review critiques a design anchored in assumptions -> prove tests a hypothesis without market grounding"). A multi-hop chain demonstrates causal chain awareness across the arc, not just first-order impact. Pass if at least one entry contains an ordered sequence of two or more downstream consequences using explicit sequencing (arrows, "then", "which means", numbered steps); fail if all entries contain single-consequence-of-displacement statements only, even if those statements are well-reasoned. The cascade must cross at least one arc-layer boundary (consequence in one namespace layer causing a problem in a later namespace layer). Single-actor cascades are sufficient; not every actor entry needs a cascade, only one. |

Weight per aspirational: 5 pts (11 criteria x 5 = 55 pts)

---

## Scoring Worksheet

```
Essential:    C-01 [ ] C-02 [ ] C-03 [ ] C-04 [ ] C-05 [ ]
              Pass count: ___ / 5   -> ___ * 12 = ___ pts (of 60)

Recommended:  C-06 [ ] C-07 [ ] C-08 [ ]
              Pass count: ___ / 3   -> ___ * 10 = ___ pts (of 30)

Aspirational: C-09 [ ] C-10 [ ] C-11 [ ] C-12 [ ] C-13 [ ]
              C-14 [ ] C-15 [ ] C-16 [ ] C-17 [ ] C-18 [ ]
              C-19 [ ]
              Pass count: ___ / 11  -> ___ * 5  = ___ pts (of 55)

Composite score: ___ / 145

Golden: all essential pass AND composite >= 116  ->  [ ] YES  [ ] NO
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
  a summary of what was prioritized does not pass C-17.
- **C-18**: Evaluated on the variation text -- specifically the column header text for the actor
  table's justification column. The boundary case: "Why this position" fails; "Why this position
  (what breaks if moved earlier)" passes; "Why this actor cannot run earlier" passes; "Position
  rationale" fails; "Justification" fails. The key test: does the header direct the model toward
  *displacement impossibility or consequence* rather than *position belonging*? Headers phrased
  as "why cannot" or "what breaks if" pass; headers phrased as "why this" or "rationale" without
  a consequence clause fail. V-01's failure (header "Why this position", entries had rationale
  but no displacement consequence) is the archetype for this fail pattern.
- **C-19**: Evaluated on the variation output -- the actor table entries themselves. A cascade
  requires two or more ordered consequences using explicit sequencing (arrows, "then", numbered
  steps, "which means"). A single consequence restated in multiple clauses does not count. The
  chain must cross at least one arc-layer boundary (e.g., a consequence in the design layer that
  causes a problem in the validation layer). Single-actor cascades are sufficient; not every actor
  entry needs a cascade, only one. V-05's evidence ("Moved later: design is anchored in the
  author's assumptions -> review critiques a design targeting the wrong problem -> prove
  investigates a hypothesis without market grounding. Scout gates protect all downstream layers
  simultaneously.") is the archetype for a passing cascade.

---

## Version Delta

### v3 -> v4

| Change | Detail |
|--------|--------|
| Updated C-14 pass condition | Verb form clarified as flexible -- "defeats," "breaks that pattern by requiring," "counters" are equivalent. Criterion is structural (both elements present), not lexical. Source: R3-H01 resolution. |
| Updated C-15 pass condition | Tightened: position rationale alone is insufficient (V-01 had rationale, failed C-15 -- the gap is absence of displacement-consequence reasoning). Pass now requires a consequence-of-displacement clause per actor in addition to position rationale. Compact form (one sentence) sufficient; prose depth not required. Source: R3-H02 resolution. |
| Added C-18 | Column header frames displacement impossibility -- from R3 finding: all C-15-passing variations (V-02 through V-05) phrased their column header around displacement impossibility or consequence; V-01's "Why this position" header drove rationale-without-consequence entries. Header formulation is load-bearing for C-15 reliability. |
| Added C-19 | Multi-hop downstream consequence cascade -- from R3 finding: V-05 traced 2-3 ordered downstream consequences per actor entry while V-03/V-04 had single-consequence entries; all scored 135/135 under v3. C-19 opens territory above the v3 ceiling. V-05 is the only R3 variation that retroactively passes C-19 (145/145). |
| Aspirational tier | 9 criteria x 5 pts -> 11 criteria x 5 pts = 55 pts |
| Total points | 135 -> 145 |
| Golden threshold | composite >= 108 -> composite >= 116 (same ~80% of max) |
| R3 best scores retroactive | V-03: 140/145 (pass C-18, fail C-19); V-04: 140/145 (pass C-18, fail C-19); V-05: 145/145 (pass C-18, pass C-19 -- multi-hop cascade present, "scout gates protect all downstream layers simultaneously"). C-19 cascade is the new ceiling gap. |

### v2 -> v3

| Change | Detail |
|--------|--------|
| Added C-14 | Naive-competitor framing -- from R2 finding: contrast opener primes principled arc reasoning; strongest C-09 discriminator in R2 |
| Added C-15 | Why-this-position column -- from R2 finding: actor table justification column produces C-09-passing causal logic inline, eliminating need for separate arc-strategy step |
| Added C-16 | Unified handoff+threshold gate template -- from R2 finding: single format string combining actor+threshold+artifact hits C-07+C-12+C-13 with no instruction density cost |
| Added C-17 | What-happens-if-removed clause -- from R2 finding: forcing function that distinguishes genuine arc reasoning from restatement; validates C-09 more reliably |
| Aspirational tier | 5 criteria x 5 pts -> 9 criteria x 5 pts = 45 pts |
| Total points | 115 -> 135 |
| Golden threshold | composite >= 92 -> composite >= 108 (same ~80% of max) |
| R2 best score retroactive | V-05 scores 125/135 (C-14 fail, C-15 fail -- no contrast opener or justification column) |

### v1 -> v2

| Change | Detail |
|--------|--------|
| Added C-11 | Skill catalog grounded inline -- from R1 finding: V-04 was the only golden because it enumerated all 47 skills; all others referenced external catalog and failed C-03 |
| Added C-12 | Actor-role framing for gates -- from R1 finding: V-04's actor-ordering implied artifact-grounded transitions without extra instruction |
| Added C-13 | Quantified gate syntax instructed -- from R1 finding: V-05 achieved both C-09 and C-10 because it embedded `>=N` syntax in the requirement; V-04 did not |
| Aspirational tier | 2 criteria x 5 pts -> 5 criteria x 5 pts = 25 pts |
| Total points | 100 -> 115 |
| Golden threshold | composite >= 80 -> composite >= 92 |
