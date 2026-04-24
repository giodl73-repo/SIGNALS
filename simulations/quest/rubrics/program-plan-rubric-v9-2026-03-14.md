`simulations/quest/rubrics/program-plan-rubric-v9-2026-03-14.md` written.

---

**v9 summary:**

Four new aspirational criteria extracted from R8 excellence signals:

| ID | Axis | Discriminates |
|----|------|---------------|
| **C-32** | Artifact Consumer Map: non-adjacent consumer traced | V-01/V-04/V-05 pass; V-02/V-03 fail |
| **C-33** | Stage Arc-Uniqueness Register: unique contribution + arc gap per stage | V-02/V-04/V-05 pass; V-01/V-03 fail |
| **C-34** | Gate Threshold Calibration: floor + topic rationale per N | V-03/V-05 pass; V-01/V-02/V-04 fail |
| **C-35** | Gate Semantic Assertion: `asserting:` clause in gate template | V-05 only |

**Scoring:** 205 → 235 pts (27 aspirational × 5). Golden threshold: **188** (~80%).

**R8 retroactive:** V-05 225/235 (ceiling); V-04 215/235; V-01/V-02/V-03 210/235 each.

**Design family positions:**
- C-32 extends C-31 (chain → lattice): non-adjacent consumer map exposes hidden multi-stage coupling
- C-33 pairs with C-28 (displacement ↔ necessity): a stage needs both "cannot move earlier" and "cannot be absent"
- C-34 extends C-10/C-13 (N exists → N justified): threshold calibration makes N an evidence-based decision
- C-35 adds the semantic layer to C-16/C-22/C-24: separates count-satisfied from claim-established

**R9 gap:** C-35 (gate semantic assertion) is the single-variation signal — the natural R9 anchor.
 single-hop tracing leaves invisible.
- C-33 is the necessity-of-presence complement to C-28's displacement-impossibility. C-28 asks "why can't this stage run earlier?"; C-33 asks "why can't this stage be absent?" Together they fully characterize a stage's architectural necessity: it must be where it is AND it must exist at all. C-33 closes the coverage gap between displacement-impossibility and necessity-of-presence.
- C-34 extends the gate quantification family: C-10 verifies N exists; C-13 verifies `>=N` syntax in the instruction; C-34 requires per-gate reasoning for the specific N chosen (a topic-independent minimum floor + a topic-specific rationale). N becomes an evidence-based design decision with a justification, not just a syntactic presence.
- C-35 extends the gate template family (C-16/C-22/C-24) with a semantic assertion layer: the `asserting:` clause within the gate template states what is now true about the evidence state when the threshold passes. This separates *count satisfied* from *claim established*, making gates verifiable at the semantic level rather than only numerically checkable. C-35 is the gate-semantic complement to C-27's gate-to-gate chain and C-31's artifact lineage.

**R9 gap:** C-35 (gate semantic assertion) is the single-variation signal, making it the natural R9 anchor.

**Scoring:** 135 pts aspirational (27 x 5) -> **235 total** -> golden threshold **188** (~80% of max).

**R8 retroactive scores under v9:**

| Variation | Score | Notes |
|-----------|-------|-------|
| V-01 | 210/235 | Pass C-32 (non-adjacent consumer traced); fail C-33 (no arc-uniqueness register), C-34 (no threshold calibration), C-35 (no semantic assertion) |
| V-02 | 210/235 | Pass C-33 (arc-uniqueness register: contribution + arc gap per stage); fail C-32 (no non-adjacent consumer map), C-34 (no threshold calibration), C-35 (no semantic assertion) |
| V-03 | 210/235 | Pass C-34 (threshold calibration: floor + topic rationale per gate); fail C-32, C-33, C-35 |
| V-04 | 215/235 | Pass C-32 + C-33 (V-01 + V-02 combination); fail C-34, C-35 |
| V-05 | 225/235 | Pass all four: C-32 + C-33 + C-34 + C-35 -- CEILING |

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

## Aspirational Criteria (135 pts total)

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
| C-24 | **Gate cascade-if-removed clause embeds `->` notation spec and depth floor** | reliability | The cascade-if-removed clause WITHIN the gate format string specifies both the `->` arrow notation and a minimum cascade depth (2+ hops crossing arc-layer boundaries) directly inside the clause -- e.g., "removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries]". This is the gate-format-string parallel to C-20 extending C-18: C-22 says "put the cascade clause in the gate template"; C-24 says "also specify notation format and depth floor within that clause." The inline specification fires at every gate boundary during construction, eliminating reliance on the model carrying a separate depth-floor instruction. Pass if the cascade-if-removed clause in the gate format string contains both `->` arrow notation AND a minimum-depth specification (e.g., "minimum 2 hops", "2+ ordered consequences", "crossing arc-layer boundaries"); fail if the clause only contains a placeholder (e.g., "[cascade]") without notation or depth requirements, even if C-22 otherwise passes. Source: R6-Signal-1 -- V-01's gate template "removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries]" passes C-22 and C-24; V-02/V-03 pass C-22 (clause present) but fail C-24 (clause lacks notation+depth spec). |
| C-25 | **Gate Cascade Audit table pre-computes all non-echo gate cascades before YAML assembly** | behavior | The variation requires a structured pre-computation table of ALL non-echo gate cascades to be produced as a distinct step before any gate string is written or any YAML stage is assembled. The audit table must cover every non-echo gate and show the cascade consequence chain for each, making cross-gate cascade coherence visible as a group. This is the gate-level analogue of the actor ordering table (which forces actor sequence coherence before stage design): both are mandatory pre-work tables that prevent ungrounded downstream content. Pass if the variation specifies a gate cascade audit table (or equivalent structured pre-computation step) as a required task completed before YAML assembly, covering all non-echo gates with cascade consequence chains; fail if cascade reasoning is only embedded in individual gate strings (C-22) or in the arc-strategy step (C-17/C-23) without a prior full-audit pass. Source: R6-Signal-2 -- V-02's gate cascade audit table forces cross-gate cascade awareness that individual gate-template cascade clauses do not guarantee. |
| C-26 | **Echo stage displacement reasoning** | depth | The variation requires explicit justification for why the echo stage cannot run earlier -- specifically: (a) what arc-completion signal echo emits, and (b) what breaks or is ungrounded if echo fires at an earlier stage (e.g., stage 2 instead of last). Echo displacement reasoning extends the displacement-impossibility pattern (C-18, C-21) to the terminal stage, surfacing that last-position is architecturally required rather than conventional. C-02 verifies structural echo correctness (name, `auto: true`, empty skills); C-26 asks why the position itself is load-bearing. Pass if the variation contains an instruction or example requiring the model to justify echo's last-position by naming both the arc-completion signal it emits and the consequence of earlier placement; fail if echo's position is stated without architectural justification, or if only C-02-style structural constraints are described. Source: R6-Signal-3 -- V-03 introduces echo stage displacement reasoning as a distinct justification step; V-01/V-02/V-04 treat echo's position as structural given, not as a consequence-bearing architectural decision. |
| C-27 | **Gate-to-gate chain: removing gate N names explicit consequence for gate N+1** | depth | For each non-echo gate, the variation requires that removing gate N explicitly names the consequence for the immediately following gate N+1 -- not only the downstream arc consequence (C-22, C-23) but the adjacent propagation: what gate N+1's cascade clause becomes ungrounded or invalid if gate N is absent. This captures adjacent-gate propagation, the missing register between C-22 (intra-gate cascade: what breaks in the arc if this gate is removed) and C-23 (first-gate arc cascade: global arc destabilization). Gate-to-gate chain completes the cascade register: local gate cascade (C-22) -> adjacent propagation (C-27) -> arc-level cascade (C-23). Pass if the variation instructs the model that each gate's cascade-if-removed statement must identify the specific consequence for the next gate -- not only for downstream arc layers; fail if cascade reasoning covers arc-level consequences (C-22 passing) but does not require the model to name what the adjacent gate loses when its predecessor is removed. Source: R6-Signal-4 -- V-05 introduces gate-to-gate chain as a structural requirement; all other R6 variations address arc-level cascade without adjacent-gate propagation. |
| C-28 | **Stage displacement register** | depth | Each stage in the variation's stage table or stage-design step includes a displacement-impossibility justification: (a) why that stage cannot be positioned earlier in the sequence and (b) what breaks, is ungrounded, or becomes unavailable if the stage is moved to an earlier position. This extends the displacement-impossibility pattern from actors (C-15, C-18, C-21) to stages themselves. Actor entries explain why each actor cannot run earlier; stage entries should explain why each stage cannot run earlier. Stage-level displacement reasoning surfaces that stage ordering is architecturally required, not a byproduct of topological sort. Pass if the variation requires each stage entry to contain both elements: (a) a displacement-impossibility justification (cannot run earlier because...) and (b) a consequence-of-displacement clause (moved earlier: X becomes Y / Z is lost); fail if stages contain only a phase description or skill grouping rationale without displacement-impossibility and consequence framing. Compact form is sufficient. A single sentence per stage combining both elements (e.g., "Cannot run earlier: earlier stages have not yet produced the synthesis signals; moved earlier: topic report summarizes an incomplete evidence set") passes. Source: R7-Signal-1 -- V-01 introduces stage displacement registers as a required per-stage element, producing displacement-impossibility reasoning at the stage level that parallels C-15 at the actor level. |
| C-29 | **Stage Cohesion Audit Table pre-computes all stage groupings before YAML assembly** | behavior | The variation requires a structured pre-computation table auditing ALL stage skill groupings -- showing each stage's name, assigned skills, and cohesion rationale -- as a distinct required step before any YAML stage is assembled. The cohesion audit table forces the model to justify each stage's skill selection as a coherent group before committing it to YAML, parallel to the actor ordering table (which forces actor sequence coherence before stage design) and C-25 (which forces gate cascade coherence before gate string assembly). The table must cover all non-echo stages and show why each grouping is internally coherent (not just a dependency-ordering artifact). Pass if the variation specifies a stage cohesion audit table (or equivalent structured pre-computation step) as a required task completed before YAML assembly, covering all non-echo stages with grouping rationale; fail if stage grouping justification exists only within YAML comments, stage-name labels, or post-YAML review steps without a prior full-audit pass. Source: R7-Signal-2 -- V-02 introduces the stage cohesion audit table as a mandatory pre-YAML step, the stage-level analogue of both the actor ordering table and C-25. |
| C-30 | **Skill Omission Register** | reliability | The variation requires an explicit register of skills NOT included in the plan, listing each omitted skill (from the 47-skill catalog) alongside the reason for its exclusion. C-11 surfaces all 47 skills inline to prevent hallucination; C-30 extends that by requiring the model to account for what it chose not to include, surfacing exclusion as a deliberate design decision rather than an implicit non-event. The omission register prevents invisible scope narrowing: a plan that silently omits scout:compliance or prove:interview has made a decision; the register makes that decision visible and auditable. Pass if the variation instructs the model to produce an explicit omission list naming each excluded skill (by name or namespace group) with a brief exclusion justification (e.g., "out of scope for this topic type", "redundant given adjacent skill already present", "requires external data not available at planning time"); fail if skill omissions are implicit, or if the variation only instructs the model to enumerate included skills without accounting for exclusions. The register may be structured as a table, list, or inline annotation block -- format is flexible. Exhaustive coverage of all 47 skills in the register is not required -- grouping by namespace (e.g., "all flow: skills excluded -- out of scope for discovery-phase topic") passes. Source: R7-Signal-3 -- V-03 introduces the skill omission register as a required output element, making exclusion decisions explicit and auditable. |
| C-31 | **Artifact Lineage Chain** | depth | The variation requires explicit tracing of artifact-to-consumer relationships across the full plan: for each stage, which artifacts it produces (by skill and artifact type), and which skills in subsequent stages consume those artifacts. The lineage chain makes the artifact dependency graph visible as a structure rather than inferring it from skill namespace ordering alone. C-05 verifies that skill ordering respects namespace dependencies (scout before draft before review/prove); C-31 requires the model to trace the specific artifact flow -- e.g., "Stage 1: scout:feasibility produces feasibility-signal -> consumed by draft:spec in Stage 2 and prove:hypothesis in Stage 3". Multi-stage lineage chains (artifact produced in stage N, consumed in stage N+2 via intermediate transformation) are the highest-value demonstrations. Pass if the variation requires each non-echo stage to identify: (a) which artifacts it produces and (b) which downstream stages and skills consume each artifact; fail if artifact dependencies are only implied by namespace ordering (C-05 passing) without an explicit per-artifact lineage trace. At minimum, one full artifact lineage chain spanning 3+ stages must be present. Source: R7-Signal-4 -- V-05 introduces the artifact lineage chain as a distinct structural requirement; no other R7 variation traces artifact-to-consumer relationships across the full plan. |
| C-32 | **Artifact Consumer Map: non-adjacent consumers traced** | depth | The variation requires that the artifact lineage trace (C-31) extends beyond direct adjacent-stage consumers to include ALL downstream consumers of each artifact -- specifically non-adjacent consumers (consumers in stage N+2 or later that depend on an artifact from stage N without receiving it via stage N+1 as a direct intermediary). C-31 makes the artifact dependency chain visible; C-32 makes the full dependency lattice visible, exposing hidden multi-stage coupling where one artifact feeds multiple downstream stages simultaneously. A plan that traces "feasibility-signal -> draft:spec (Stage 2)" satisfies C-31 but fails C-32 if feasibility-signal also feeds prove:hypothesis (Stage 4) and that non-adjacent dependency is not traced. Pass if the variation requires that each artifact's consumer trace includes at least one non-adjacent consumer where such coupling exists; fail if the lineage trace terminates at the first downstream consumer for each artifact without checking for non-adjacent dependencies. The complete consumer map reveals hidden cross-arc couplings that a single-hop chain obscures. Source: R8-Signal-1 -- V-01's Artifact Consumer Map extends C-31's single-hop tracing to a full lattice covering all downstream consumers, exposing multi-stage coupling invisible to chain-only lineage. |
| C-33 | **Stage Arc-Uniqueness Register: necessity-of-presence justification** | depth | The variation requires each non-echo stage to carry an arc-uniqueness justification declaring: (a) the unique evidence contribution that stage and only that stage makes to the arc (no other stage produces the same signal type or synthesis), and (b) the arc gap that would exist if this stage were absent (what evidence layer would be missing, expressed as a 2+ hop consequence crossing arc-layer boundaries). C-28 asks "why can't this stage run earlier?" (displacement-impossibility); C-33 asks "why can't this stage be absent?" (necessity-of-presence). Together they fully characterize a stage's architectural necessity. A stage that passes C-28 (cannot move earlier) but has no arc-uniqueness justification (could theoretically be omitted) fails C-33. Pass if the variation requires each stage entry to contain: (a) a unique-contribution statement (what evidence only this stage produces) and (b) an arc-gap statement expressing the consequence of removal as a 2+ hop cross-arc-layer cascade (e.g., "Absent: prove:hypothesis tests an unvalidated hypothesis -> review:design critiques against wrong targets -> topic:report synthesizes unvalidated conclusions"); fail if stages justify their position (C-28) but do not justify their necessity. Compact form is sufficient. Source: R8-Signal-2 -- V-02's Arc-Uniqueness Register closes the coverage gap between displacement-impossibility (C-28) and necessity-of-presence by requiring each stage to declare its irreplaceable arc contribution. |
| C-34 | **Gate Threshold Calibration: N-selection with minimum floor and topic rationale** | behavior | The variation requires per-gate reasoning for the specific N chosen in each `>=N` threshold: (a) a topic-independent minimum floor (the lowest N that could be justified for any topic, e.g., "N >= 2 for scout gates because a single signal is insufficient to establish pattern vs. noise") and (b) a topic-specific rationale (why this particular N fits this particular topic's evidence requirements, e.g., "N = 3 here because the topic involves regulatory complexity requiring triangulation"). C-10 verifies N exists; C-13 verifies `>=N` syntax appears in the instruction; C-34 requires that N is an evidence-based design decision with explicit reasoning, not a placeholder or convention. N becomes a deliberate choice rather than a number inserted to satisfy C-10. Pass if the variation instructs the model to specify both the minimum floor (topic-independent lower bound) and the topic-specific rationale for each gate's N choice; fail if N is required to exist (C-10 passing) and syntax is demonstrated (C-13 passing) but no per-gate reasoning for N's value is required. A single threshold-calibration instruction covering all gates passes if it requires both elements (floor + rationale) per gate. Source: R8-Signal-3 -- V-03's Gate Threshold Calibration forces N to be an evidence-based decision; C-10 and C-13 leave N as a structural presence without requiring the model to justify its specific value. |
| C-35 | **Gate Semantic Assertion: evidence-state claim in gate template** | behavior | The gate format string contains an `asserting:` clause (or equivalent semantic-claim element) that states what is now true about the evidence state when the gate's threshold passes -- not the artifact count (which the threshold already captures), but the epistemic claim that the count establishes. For example: "[Delivering actor] hands off to [Receiving actor] when >=3 scout signals present -- asserting: feasibility is sufficiently established to commit design resources -- removing this gate: [cascade]". The `asserting:` clause separates *count satisfied* from *claim established*, making gates semantically verifiable rather than only numerically checkable. C-16 requires actor+threshold+artifact in the gate template; C-22 adds cascade-if-removed; C-35 adds the semantic claim layer. The prior gate template family (C-16/C-22/C-24) encodes consequence logic; C-35 encodes epistemic state logic. Pass if the gate format string in the gate-writing instruction contains an `asserting:` clause (or semantic equivalent: "establishing:", "meaning:", "this establishes:", "claim:") that names the evidence state established when the threshold passes; fail if the gate template encodes threshold + cascade (C-22 passing) but contains no semantic claim about what the satisfied threshold means for the evidence state. The semantic claim is evaluated against the variation text, not the model output. Source: R8-Signal-4 -- V-05's `asserting:` clause distinguishes evidence-count satisfaction from claim establishment, producing gates that are verifiable at the semantic level; all other R8 variations encode cascade logic without a semantic assertion layer. |

Weight per aspirational: 5 pts (27 criteria x 5 = 135 pts)

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
              C-24 [ ] C-25 [ ] C-26 [ ] C-27 [ ] C-28 [ ]
              C-29 [ ] C-30 [ ] C-31 [ ] C-32 [ ] C-33 [ ]
              C-34 [ ] C-35 [ ]
              Pass count: ___ / 27  -> ___ * 5  = ___ pts (of 135)

Composite score: ___ / 235

Golden: all essential pass AND composite >= 188  ->  [ ] YES  [ ] NO
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
- **C-24**: Evaluated on the variation text -- specifically the cascade-if-removed clause WITHIN
  the gate format string. Distinguished from C-22: C-22 requires the cascade-if-removed clause
  to be present in the gate template; C-24 requires that clause to also specify `->` arrow
  notation AND a minimum depth floor (2+ hops, arc-layer crossing). A gate template that contains
  "removing this gate: [cascade]" passes C-22 but fails C-24 (placeholder with no notation or
  depth spec). A gate template that contains "removing this gate: [A -> B -> C, minimum 2 hops
  crossing arc-layer boundaries]" passes both. The notation and depth spec must appear inside
  the cascade clause within the gate format string, not only in a separate instruction block.
- **C-25**: Evaluated on the variation text -- specifically whether a gate cascade audit table
  (or equivalent structured pre-computation step for ALL non-echo gates) is required BEFORE YAML
  assembly. Distinguished from C-22 and C-27: those criteria embed cascade reasoning into
  individual gate strings or chain requirements; C-25 requires a separate prior-step audit table
  that makes all gate cascades visible as a group before any gate string is written. A variation
  that embeds cascade clauses in every gate template (C-22 passing) but does not require a
  pre-YAML audit table fails C-25. The table must be explicitly scoped to all non-echo gates
  and must precede gate string assembly in the instruction sequence.
- **C-26**: Evaluated on the variation text -- specifically whether the echo stage's last-position
  is required to be justified architecturally (arc-completion signal it emits + consequence of
  earlier placement), not just structurally stated. Distinguished from C-02 (structural echo
  contract: name, auto:true, empty skills) and C-18 (actor table column header framing): C-26
  asks whether the variation treats echo's position as a consequence-bearing architectural
  decision rather than a given. A variation that specifies the echo structural contract (C-02
  passing) without requiring displacement reasoning for echo's position fails C-26. The two
  required elements are: (a) what arc-completion signal echo emits and (b) what breaks if echo
  fires earlier (e.g., at stage 2).
- **C-27**: Evaluated on the variation text -- specifically whether the gate cascade reasoning
  requirement extends to adjacent-gate propagation. Distinguished from C-22 (intra-gate cascade:
  what breaks in the arc when this gate is removed) and C-23 (first-gate arc cascade: global arc
  destabilization). C-27 requires the model to identify what gate N+1's cascade clause becomes
  ungrounded when gate N is absent -- a local, adjacent consequence, not an arc-level one. A
  variation that requires arc-level cascade in every gate template (C-22 passing) but does not
  require naming the adjacent gate consequence fails C-27. The adjacent-gate chain can be
  specified as an additional element in the gate format string, a post-gate-writing check, or a
  dedicated instruction step -- placement is flexible as long as every non-echo gate is covered.
- **C-28**: Evaluated on the variation text -- specifically whether each stage in the stage-design
  step or stage table contains a displacement-impossibility justification. Distinguished from C-06
  (stages group skills meaningfully: internal cohesion) and C-08 (stage names are descriptive:
  label quality). C-28 asks not what a stage contains but why it cannot be placed earlier. Two
  required elements per stage: (a) why it cannot run earlier (what prerequisite is unavailable)
  and (b) what breaks if it is moved earlier (what becomes ungrounded or premature). A stage that
  has a good name and coherent skills but no displacement-impossibility reasoning fails C-28. A
  variation that requires all stages to carry these two elements passes. Compact form is sufficient
  -- one sentence per stage combining both elements passes. A stage cohesion audit table (C-29)
  may include displacement reasoning in its columns, but C-28 also passes if displacement
  reasoning appears inside the stage template instruction without a separate table.
- **C-29**: Evaluated on the variation text -- specifically whether a stage cohesion audit table
  (or equivalent structured pre-computation step for ALL non-echo stages) is required BEFORE YAML
  assembly. Distinguished from C-28 (displacement reasoning per stage, which can appear inside
  stage templates or a table) and C-25 (gate cascade audit table, which covers gates not stages):
  C-29 requires a distinct prior-step audit table scoped to stage skill groupings with cohesion
  rationale, not cascade reasoning. A variation that embeds displacement justification in each
  stage template (C-28 passing) but does not require a pre-YAML stage cohesion audit table fails
  C-29. The table must be explicitly scoped to all non-echo stages and must precede YAML stage
  assembly in the instruction sequence. The table's function is to surface grouping incoherence
  before commitment -- the same forcing function as the actor ordering table and C-25.
- **C-30**: Evaluated on the variation text -- specifically whether an explicit omission register
  is required as part of the output. Distinguished from C-11 (skill catalog grounded inline:
  ensures all 47 skills are listed as valid input reference, preventing hallucination at intake)
  and C-03 (all referenced skills are valid: verifies no invalid skills appear in output). C-30
  measures a third channel: skills that are valid, known, and deliberately excluded. A variation
  that passes C-11 (full catalog inline) and C-03 (no invalid skills in output) but does not
  require an omission register fails C-30. The register must name omitted skills by name or
  namespace group with brief exclusion reasons. Format is flexible (table, list, annotation block).
  Exhaustive coverage of all 47 skills in the register is not required -- grouping by namespace
  (e.g., "all flow: skills excluded -- out of scope for discovery-phase topic") passes. What is
  required is that the model account for the major exclusion decisions, not that every omitted
  skill appear individually.
- **C-31**: Evaluated on the variation text -- specifically whether an explicit artifact lineage
  trace is required as a distinct step or column in the stage-design output. Distinguished from
  C-05 (skills ordered by dependency: namespace-layer ordering verification) and C-09 (strategic
  pacing: arc-level breadth/depth/synthesis strategy). C-31 requires tracing the specific
  artifact-to-consumer chain, not just confirming that namespace ordering is correct. A variation
  that orders skills correctly (C-05 passing) and describes a pacing strategy (C-09 passing) but
  does not trace artifact lineage across stages fails C-31. The key test: does the output contain
  at least one named artifact type with (a) its producer skill and stage and (b) its consumer
  skill(s) and stage(s) explicitly identified? Multi-stage lineage chains (artifact produced in
  stage N, consumed in stage N+2 via intermediate transformation) are above-minimum but not
  required. At minimum: one artifact traced from producer stage to consumer stage across a
  non-adjacent boundary (not just stage N to stage N+1) to demonstrate cross-arc dependency
  awareness.
- **C-32**: Evaluated on the variation text -- specifically whether the artifact lineage
  requirement explicitly calls for non-adjacent consumer tracing, beyond the direct-stage
  consumers satisfied by C-31. Distinguished from C-31 (artifact lineage chain: producer ->
  first consumer) by requiring the full consumer map: every downstream consumer of each artifact,
  including consumers in stages N+2, N+3, etc. that depend on an artifact from stage N without
  it passing through stage N+1 as a relay. A variation that requires C-31-style lineage tracing
  (producer -> consumer, spanning 3+ stages) but does not explicitly require non-adjacent consumer
  enumeration fails C-32. The test: does the variation instruct the model to check whether each
  artifact has consumers beyond the immediately following stage? A variation passes if it
  instructs: "trace all downstream consumers of each artifact, not only the first-stage consumer
  -- identify non-adjacent consumers (stages N+2 or later) that depend directly on artifacts
  from stage N." Format is flexible; the requirement is non-adjacent coverage, not a specific
  table structure.
- **C-33**: Evaluated on the variation text -- specifically whether each stage in the stage-design
  step or audit table contains an arc-uniqueness justification in addition to displacement
  reasoning (C-28). Distinguished from C-28 (displacement-impossibility: why this stage cannot
  run earlier) and C-06 (stages group skills meaningfully: internal grouping cohesion). C-33 asks
  why this stage cannot be absent, not why it cannot run earlier. The two elements required are:
  (a) the unique evidence contribution this stage makes (what signal type or synthesis no other
  stage produces) and (b) the arc gap from removal, expressed as a 2+ hop cross-arc-layer cascade
  (e.g., "Absent: prove:hypothesis tests an unvalidated hypothesis -> review:design critiques
  against the wrong target -> topic:report synthesizes unvalidated conclusions"). A stage that
  passes C-28 (displacement reasoning present) but has no arc-uniqueness justification fails C-33.
  Compact form is sufficient. Source: R8-Signal-2 -- V-02's Arc-Uniqueness Register is the
  necessity-of-presence complement to C-28's displacement-impossibility; a stage is fully
  characterized architecturally only when both questions are answered.
- **C-34**: Evaluated on the variation text -- specifically whether the gate-writing instruction
  requires per-gate N-selection reasoning beyond threshold presence (C-10) and syntax (C-13). The
  two required elements are: (a) a topic-independent minimum floor (the lowest N justifiable for
  any topic using this gate type -- e.g., "scout gates require N >= 2 because a single signal
  cannot establish a pattern") and (b) a topic-specific rationale (why this topic's evidence
  requirements justify the specific N chosen -- e.g., "N = 4 here because regulatory compliance
  topics require triangulation from multiple independent jurisdictions"). A variation that
  demonstrates `>=N` syntax (C-13 passing) and produces quantified output (C-10 passing) but does
  not require per-gate N-reasoning fails C-34. The instruction may be structured as a threshold-
  calibration step, an in-template annotation requirement, or a pre-gate-assembly check -- format
  is flexible. What is required is that both the floor and the topic-specific rationale appear per
  gate, not once globally.
- **C-35**: Evaluated on the variation text -- specifically whether the gate format string in the
  gate-writing instruction contains a semantic assertion element in addition to threshold and
  cascade. Distinguished from C-16 (actor+threshold+artifact in template: structural), C-22
  (cascade-if-removed in template: consequence), and C-24 (notation+depth in cascade clause:
  depth specification). C-35 adds a fourth required gate-template layer: the evidence-state claim
  established when the threshold passes. The boundary case: a gate that reads ">=3 scout signals
  present" satisfies C-10 (quantified) and C-16 (threshold+artifact in template) but says nothing
  about what the count establishes. A gate with `asserting: feasibility is sufficiently
  established to commit design resources` states the epistemic claim. Any semantic-claim keyword
  (`asserting:`, `establishing:`, `this claim:`, `meaning:`) passes; count-only gates without a
  claim clause fail. The semantic claim must appear inside the gate format string in the
  gate-writing instruction, not only as an example in a later section. Source: R8-Signal-4 --
  V-05's `asserting:` clause is the only R8 variation to add the semantic layer; all others encode
  count satisfaction without epistemic claim.

---

## Version Delta

### v8 -> v9

| Change | Detail |
|--------|--------|
| Added C-32 | Artifact Consumer Map: non-adjacent consumers traced -- from R8-Signal-1: V-01 extends C-31's single-hop artifact lineage to a full consumer lattice, tracing each artifact to ALL downstream consumers including non-adjacent ones (stage N+2 or later). C-31 makes the artifact chain visible; C-32 makes the full dependency lattice visible, exposing hidden multi-stage coupling. V-01/V-04/V-05 pass; V-02/V-03 fail. |
| Added C-33 | Stage Arc-Uniqueness Register: necessity-of-presence justification -- from R8-Signal-2: V-02 requires each stage to declare its unique arc contribution AND the arc gap from removal (2+ hop cross-arc-layer cascade). C-28 asks why a stage cannot run earlier (displacement-impossibility); C-33 asks why a stage cannot be absent (necessity-of-presence). Together they fully characterize a stage's architectural necessity. V-02/V-04/V-05 pass; V-01/V-03 fail. |
| Added C-34 | Gate Threshold Calibration: N-selection with minimum floor + topic rationale -- from R8-Signal-3: V-03 requires per-gate reasoning for the specific N chosen: a topic-independent minimum floor and a topic-specific rationale. C-10 verifies N exists; C-13 verifies syntax; C-34 requires N to be an evidence-based design decision with justification. V-03/V-05 pass; V-01/V-02/V-04 fail. |
| Added C-35 | Gate Semantic Assertion: `asserting:` clause in gate template -- from R8-Signal-4: V-05 adds a semantic-claim layer to the gate template, stating what is now true about the evidence state when the threshold passes. C-16/C-22/C-24 encode structural+consequence gate logic; C-35 adds epistemic state logic separating count-satisfied from claim-established. V-05 only (single-variation signal). |
| Aspirational tier | 23 criteria x 5 pts -> 27 criteria x 5 pts = 135 pts |
| Total points | 205 -> 235 |
| Golden threshold | composite >= 164 -> composite >= 188 (same ~80% of max) |
| R8 best scores retroactive | V-05: 225/235 (ceiling -- passes all four new criteria); V-04: 215/235 (passes C-32 + C-33, fails C-34 + C-35); V-01/V-02/V-03: 210/235 (each passes exactly one new criterion -- C-32, C-33, C-34 respectively). C-35 (gate semantic assertion) is the single-variation gap for R9. |

### v7 -> v8

| Change | Detail |
|--------|--------|
| Added C-28 | Stage displacement register -- from R7-Signal-1: V-01 requires each stage to contain displacement-impossibility justification (why it cannot run earlier + what breaks if moved), the stage-level analogue of the actor table's C-15/C-18/C-21 pattern. Displacement-impossibility reasoning was required of actors and of echo (C-26); C-28 extends it to all non-echo stages. V-01 passes; V-02/V-03/V-04 fail; V-05 passes. |
| Added C-29 | Stage Cohesion Audit Table pre-computes all stage groupings before YAML assembly -- from R7-Signal-2: V-02 requires all stage skill groupings to be audited as a structured table before YAML assembly, the stage-level analogue of the actor ordering table and C-25 (gate cascade audit). Forces grouping-coherence verification as a prior step, not within YAML comments. V-02 passes; V-01/V-03/V-04 fail; V-05 passes. |
| Added C-30 | Skill Omission Register -- from R7-Signal-3: V-03 requires an explicit register of excluded skills with reasons, surfacing exclusion as a deliberate auditable design decision. C-11 (catalog inline) prevents hallucination of invalid skills; C-30 requires accounting for valid skills that were deliberately not included. V-03 passes; V-01/V-02/V-04 fail; V-05 passes. |
| Added C-31 | Artifact Lineage Chain -- from R7-Signal-4: V-05 requires explicit artifact-to-consumer tracing across the full plan, making the artifact dependency graph visible as a structure rather than inferring it from namespace ordering alone. C-05 verifies namespace-level ordering; C-31 requires named artifact flow from producer stage to consumer stage. V-05 passes; V-01/V-02/V-03/V-04 fail. |
| Aspirational tier | 19 criteria x 5 pts -> 23 criteria x 5 pts = 115 pts |
| Total points | 185 -> 205 |
| Golden threshold | composite >= 148 -> composite >= 164 (same ~80% of max) |
| R7 best scores retroactive | V-05: 205/205 (ceiling -- passes all four new criteria); V-04: 195/205 (passes C-28 + C-29, fails C-30 + C-31); V-01/V-02/V-03: 190/205 (each passes exactly one new criterion -- C-28, C-29, C-30 respectively). C-31 (artifact lineage chain) is the single-variation gap for R8. |

### v6 -> v7

| Change | Detail |
|--------|--------|
| Added C-24 | Gate cascade-if-removed clause embeds `->` notation spec and depth floor -- from R6-Signal-1: V-01's gate template extends C-22 by embedding arrow notation and 2-hop minimum inside the cascade-if-removed clause ("removing this gate: [A -> B -> C, minimum 2 hops crossing arc-layer boundaries]"). This is the gate-template parallel to C-20 extending C-18: C-22 places the clause in the template; C-24 specifies notation and depth within the clause. V-01/V-04/V-05 pass; V-02/V-03 fail. |
| Added C-25 | Gate Cascade Audit table pre-computes all non-echo gate cascades before YAML assembly -- from R6-Signal-2: V-02 requires all gate cascades to be pre-computed as a structured audit table before any gate string is written, parallel to the actor ordering table that precedes stage design. Forces cross-gate cascade coherence that individual gate-template clauses (C-22) do not guarantee. V-02/V-04/V-05 pass; V-01/V-03 fail. |
| Added C-26 | Echo stage displacement reasoning -- from R6-Signal-3: V-03 requires explicit justification for why echo cannot run earlier: what arc-completion signal it emits and what breaks if it fires at stage 2. Extends displacement-impossibility reasoning (C-18 for actor table, C-21 for actor entries) to the terminal stage, surfacing that last-position is architecturally required not conventional. V-03/V-05 pass; V-01/V-02/V-04 fail. |
| Added C-27 | Gate-to-gate chain: removing gate N names explicit consequence for gate N+1 -- from R6-Signal-4: V-05 requires each gate's cascade-if-removed statement to identify the consequence for the immediately adjacent next gate, capturing adjacent-gate propagation between C-22 (per-gate arc cascade) and C-23 (first-gate arc cascade). Completes the cascade register: local (C-22) -> adjacent (C-27) -> arc-level (C-23). V-05 passes; V-01/V-02/V-03/V-04 fail. |
| Aspirational tier | 15 criteria x 5 pts -> 19 criteria x 5 pts = 95 pts |
| Total points | 165 -> 185 |
| Golden threshold | composite >= 132 -> composite >= 148 (same ~80% of max) |
| R6 best scores retroactive | V-05: 185/185 (ceiling -- passes all four new criteria); V-04: 175/185 (passes C-24 + C-25, fails C-26 + C-27); V-01/V-02/V-03: 170/185 (each passes exactly one new criterion -- C-24, C-25, C-26 respectively). C-27 (gate-to-gate chain) is the single-variation gap for R7. |

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
