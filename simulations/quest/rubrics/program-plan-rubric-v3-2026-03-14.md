Written to `simulations/quest/rubrics/program-plan-rubric-v3-2026-03-14.md`.

---

**What changed in v3:**

Four new aspirational criteria extracted from R2 excellence signals:

| ID | Criterion | Source pattern |
|----|-----------|----------------|
| C-14 | **Naive-competitor framing** | Contrast opener naming a specific failure mode produces C-09-passing arc reasoning more reliably than step-by-step instructions alone. |
| C-15 | **Why-this-position column in actor table** | Per-actor justification column teaches causal arc logic inline, producing C-09 without a separate arc-strategy paragraph. |
| C-16 | **Unified handoff+threshold gate template** | Single format string combining actor+`>=N`+artifact hits C-07+C-12+C-13 simultaneously with no instruction density cost. |
| C-17 | **What-happens-if-removed clause** | Forcing function inside the arc-strategy step that distinguishes genuine causal reasoning from restatement; makes C-09 pass more reliably. |

**Scoring adjustment:** aspirational grows from 25 pts (5 × 5) to 45 pts (9 × 5). Total moves to **135**. Golden threshold adjusts from 92 to **108** (~80% of max). R2's V-05 (115/115) would retroactively score 125/135 — the C-14/C-15 gap is what R3 variations should close.
ring the model to answer "what happens if any gate is removed?" as part of the arc-strategy step forces genuine arc reasoning and distinguishes causal understanding from restatement. C-09 passes more reliably when this clause is present. |

**Scoring adjustment:** aspirational grows from 25 pts (5 × 5) to 45 pts (9 × 5). Total moves to 135. Golden threshold adjusts from 92 to 108 (same ~80% of max). R2's best (V-05, 115/115) would retroactively score 125/135 -- C-14 and C-15 are the new ceiling gap.

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

## Aspirational Criteria (45 pts total)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-09 | **Strategic pacing across signal types** | depth | The plan shows deliberate signal-building strategy: early stages produce breadth signals (scout, draft), middle stages produce depth signals (prove, review), late stages synthesize (topic). The program reflects a coherent evidence arc, not just topological sort. |
| C-10 | **Gates are quantified where possible** | behavior | At least one gate specifies a minimum signal count or threshold (e.g., `gate: ">=2 scout signals and draft-spec artifact present"`). Quantified gates are machine-checkable in principle. |
| C-11 | **Skill catalog grounded inline** | reliability | The variation enumerates all valid skill names organized by namespace inline in the prompt -- not by reference to an external file. This eliminates hallucination risk for C-03 at the source rather than relying on post-hoc validation. Pass if all 47 skills are listed inline; fail if the prompt delegates to "see plugin-plan.md" or "use the catalog." |
| C-12 | **Actor-role framing for gates** | depth | Gate conditions are written in actor-role transition language (e.g., "researcher needs X before designer can proceed", "PM sign-off requires Y") rather than abstract artifact checklists alone. Actor framing naturally grounds gates in workflow transitions and produces C-07-passing conditions without additional instruction. |
| C-13 | **Quantified gate syntax instructed** | behavior | The variation embeds a concrete `>=N signal_type` syntax example directly inside the gate-writing instruction (not only in a general examples section). The inline example drives machine-checkable threshold syntax in output, producing C-10-passing gates reliably. |
| C-14 | **Naive-competitor framing** | reliability | The variation opens by naming the failure mode it is designed to defeat (e.g., "naive variations produce flat skill lists without arc logic; this variation defeats that by..."). This contrast opener primes the model to reason about what makes a plan principled vs. mechanical, producing C-09-passing arc articulation more reliably than step-by-step instructions alone. Pass if the variation contains an explicit contrast statement naming a specific failure mode and the structural choice that defeats it; fail if the opener describes what the variation does without naming what it defeats. |
| C-15 | **Why-this-position column in actor table** | depth | The actor ordering table includes a justification column (e.g., "Why this position") explaining why each actor appears at that point in the arc. This column teaches causal arc logic inline and produces C-09-passing reasoning without requiring a separate arc-strategy paragraph. Pass if the actor table contains a justification column with per-actor rationale; fail if actor ordering is stated without rationale or the column is present but left blank. |
| C-16 | **Unified handoff+threshold gate template** | behavior | The variation specifies a single required gate format string that combines all three elements: actor names, `>=N` threshold, and artifact type (e.g., "[Delivering actor] hands off to [Receiving actor] when >=N artifact_type present"). A unified template hits C-07, C-12, and C-13 simultaneously with no instruction density cost. Pass if a single format string incorporating all three elements appears in the gate-writing instruction; fail if these elements are specified separately or the template omits any one of them. |
| C-17 | **What-happens-if-removed clause** | depth | The arc-strategy step requires the model to answer "what happens if any gate is removed?" as part of producing the strategy statement. This forcing function distinguishes genuine arc reasoning (model can explain the consequence) from restatement (model paraphrases the artifact list). Pass if the arc-strategy instruction contains this clause or equivalent; fail if the strategy step only asks for a summary of what was prioritized. |

Weight per aspirational: 5 pts (9 criteria x 5 = 45 pts)

---

## Scoring Worksheet

```
Essential:    C-01 [ ] C-02 [ ] C-03 [ ] C-04 [ ] C-05 [ ]
              Pass count: ___ / 5   -> ___ * 12 = ___ pts (of 60)

Recommended:  C-06 [ ] C-07 [ ] C-08 [ ]
              Pass count: ___ / 3   -> ___ * 10 = ___ pts (of 30)

Aspirational: C-09 [ ] C-10 [ ] C-11 [ ] C-12 [ ] C-13 [ ]
              C-14 [ ] C-15 [ ] C-16 [ ] C-17 [ ]
              Pass count: ___ / 9   -> ___ * 5  = ___ pts (of 45)

Composite score: ___ / 135
Golden: all essential pass AND composite >= 108  ->  [ ] YES  [ ] NO
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
  is present but the model ignored it). A variation passes both when the instruction is present
  and the output uses the syntax.
- **C-14**: Evaluated on the variation text, not the output. The contrast statement must name a
  *specific* failure mode (e.g., "flat skill lists", "dependency-free stage ordering", "abstract
  gates") -- not a generic claim like "this is better than naive approaches." The failure mode
  named should be the one the variation's structural choices actually defeat.
- **C-15**: Evaluated on the variation text. An actor table with columns like "Actor | Skills |
  Why this position" passes. An actor table with only "Actor | Skills" fails, even if ordering
  is correct. The justification column is the criterion, not the correctness of ordering itself.
- **C-16**: The template must appear *inside* the gate-writing instruction, not only in an
  examples section. A format string that omits actor names (threshold + artifact only) passes
  C-13 but not C-16. All three elements -- actor, threshold, artifact -- must appear in one
  required format.
- **C-17**: Evaluated on the variation text. The clause can take any form ("explain what would
  break if this gate were removed", "state the consequence of skipping this gate", etc.) as long
  as it requires the model to reason about gate removal consequences. A step that only asks for
  a summary of what was prioritized does not pass C-17, even if the output happens to include
  causal reasoning.

---

## Version Delta

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
