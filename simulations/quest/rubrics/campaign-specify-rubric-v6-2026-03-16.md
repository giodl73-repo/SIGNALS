The subagent analyzed what's on disk but the scorecard was supplied inline. Let me extract patterns directly from it and write the rubric.

Three new patterns in V-04 not captured by any existing criterion:

1. **COMPLETION INDEX gate audit row** — V-04's COMPLETION INDEX includes `"Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)"` alongside artifact rows. C-23 only requires artifact existence. Gate passage confirmation is new.

2. **Citation failure recovery path** — V-04 adds `"(If CITATION MISSING: return to Phase 2 and paste the record before stopping.)"` C-21 leg 3 only requires the CONFIRMED/MISSING declaration; the active recovery instruction is new.

3. **Voice contract backpointer anchoring** — V-04's pitch sections contain `"Use Step 0c [audience] voice contract as anchor"`, creating explicit Phase-0-to-Phase-3 traceability. C-10 measures output differentiation; this measures the structural traceability mechanism itself.

---

# Scoring Rubric: campaign-specify (v6)

## What changed from v5

Three new aspirational criteria extracted from R5 excellence signals in V-04 (the first variation to simultaneously earn C-21, C-22, and C-23). Each targets a gap that only becomes visible when all three R5 mechanisms are co-present.

| New ID | Pattern Source | What it measures |
|--------|----------------|------------------|
| C-24 | V-04 COMPLETION INDEX evidence ("Phase 0 gate chain: 3 gates passed") | COMPLETION INDEX gate audit row — the COMPLETION INDEX extends beyond artifact existence to include a dedicated gate-passage confirmation entry, making it a unified audit record for both artifacts and phase-gate compliance |
| C-25 | V-04 citation check evidence ("If CITATION MISSING: return to Phase 2 and paste the record before stopping.") | Citation failure recovery path — the citation check includes an active recovery instruction directing the model back to the source phase when the citation is absent; a declaration-only check does not pass |
| C-26 | V-04 pitch evidence ("Use Step 0c [audience] voice contract as anchor") | Voice contract backpointer anchoring — each pitch audience section explicitly references the Phase 0 voice contract that governs its register; audience versions produced without a named anchor to a prior-established contract do not pass |

**Scoring formula updated**: aspirational denominator 15 → 18.

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 18 * 10)
```

R5 variation scores under v6:

| Variation | Essential | Rec | Asp (of 18) | Composite | New criteria earned |
|-----------|-----------|-----|-------------|-----------|---------------------|
| V-01 | 5/5 | 3/3 | 12/18 | 96.7 | — |
| V-02 | 5/5 | 3/3 | 11/18 | 96.1 | — |
| V-03 | 5/5 | 3/3 | 11/18 | 96.1 | — |
| V-04 | 5/5 | 3/3 | 17/18 | 99.4 | C-24, C-25, C-26 |

V-04 leads R5 at 99.4. C-20 remains the sole criterion unearned by every variation. C-24, C-25, and C-26 are earned only by V-04. The R6 target ceiling is 18/18: a variation that earns C-20 while holding all seventeen V-04 criteria.

---

## Criteria

### Essential (output is not useful without these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Three artifacts produced** | completeness | essential | The skill produces all three artifacts: spec, proposal, and pitch. All three must exist as written files on disk. Missing any artifact = fail. |
| C-02 | **Spec has all six required sections** | completeness | essential | The spec artifact contains all six sections: Overview, User Problem, Proposed Solution, Constraints, Open Questions, and Self-Review. Missing or empty section = fail. |
| C-03 | **Proposal has 3+ options including do-nothing** | completeness | essential | The proposal artifact contains at least three options. One option must be explicitly named "Do Nothing" (or equivalent). Each option must include description, pros, cons, risk, effort, and a recommendation section with stated rationale. |
| C-04 | **Pitch covers three audience versions** | coverage | essential | The pitch artifact contains exec, developer, and maker versions. Each version has: hook, what it does, why it matters, and call to action. Missing any version = fail. |
| C-05 | **Cross-artifact consistency** | correctness | essential | The feature name, core behavior, and key constraints described in the spec are consistent with those referenced in the proposal and pitch. No contradictions between artifacts on fundamental scope. |

---

### Recommended (output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Spec self-review flags gaps** | depth | recommended | The spec artifact includes a self-review section identifying open questions, ambiguities, or sections needing more detail. At least one gap or open question named. "No gaps found" does not pass. |
| C-07 | **Pitch contains anti-positioning section** | depth | recommended | The pitch artifact includes an anti-positioning section explicitly stating what the feature is NOT, distinct from the three audience versions. |
| C-08 | **Proposal recommendation cites trade-off rationale** | depth | recommended | The proposal recommendation section explicitly references the key trade-off(s) that drove the choice — not just a preference statement. The rationale must be traceable to a specific constraint or risk identified in the options analysis. |

---

### Aspirational (raise the bar once essential/recommended stable)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Scout signal pull-through** | behavior | aspirational | At least one artifact explicitly references or incorporates a scout signal (e.g., requirements from scout-requirements, options informed by scout-feasibility, positioning from scout-positioning). Signals pulled, not invented. |
| C-10 | **Audience voice differentiation** | depth | aspirational | The exec pitch version leads with outcomes/ROI, the dev version leads with the tool/capability, and the maker version uses jargon-free "can I do this?" framing. All three voices are detectably distinct — not the same content reordered. |
| C-11 | **Completion check fail-safe** | reliability | aspirational | The orchestration emits an active recovery instruction after all phases: if any artifact is missing, the skill directs the model to detect and fill the gap before stopping. A passive reminder does not pass; the instruction must trigger a write, not just a warning. |
| C-12 | **Phase 0 audience framing pre-write** | structure | aspirational | A dedicated pre-writing phase establishes voice contracts — the one sentence each audience (exec, dev, maker) cares about most — before the spec is drafted. Voice contracts defined upfront, not inferred during pitch writing. This phase must precede Phase 1 (spec). |
| C-13 | **Namespace-targeted per-phase scout pull** | behavior | aspirational | Each writing phase pulls from the scout sub-namespace most relevant to its artifact: Phase 1 (spec) pulls from `simulations/scout/` broadly; Phase 2 (proposal) targets `scout-feasibility`; Phase 3 (pitch) targets `scout-positioning`. A single generic glob at orchestration start does not pass. |
| C-14 | **Per-audience inertia cost in Phase 0** | depth | aspirational | Phase 0 names the specific cost of inaction for each audience — not just the voice register each uses, but what each audience *loses* if the feature does not ship. The cost must be concrete and audience-specific (e.g., exec: revenue/risk exposure; dev: workaround burden; maker: blocked workflow). Generic value propositions or register labels alone do not pass. |
| C-15 | **Do Nothing as named falsifiable baseline** | correctness | aspirational | The Recommendation section explicitly defeats the Do Nothing option by name, citing a specific cost drawn from the options analysis. Required form: "We chose [X] over Do Nothing because [specific Option 1 cost], and over [Y] because [specific trade-off]." A recommendation that compares only non-default options, or defeats Do Nothing only implicitly, does not pass. |
| C-16 | **Do Nothing defeat as named structural block** | structure | aspirational | The Recommendation section contains a dedicated, labeled "Defeating Do Nothing" block (or equivalent named header) that is structurally separate from the comparative defeat of other options. Inline defeat language embedded in a combined recommendation paragraph does not pass — the Do Nothing defeat must be independently traceable by label. A bold label followed immediately by content on the same line (bold+colon inline pattern) does not pass; the label must stand alone as a dedicated header. |
| C-17 | **Do Nothing stability trajectory in defeat block** | depth | aspirational | The Do Nothing analysis includes an explicit stability dimension: whether the cost of inaction is stable or worsening over time. The Phase 2 defeat block must reference this stability assessment (e.g., "Do Nothing is not stable: [cite assessment]" or "this cost compounds over time"). A static one-time cost citation without trajectory argument does not pass. The stability dimension must appear in both Phase 0 (where it is established) and Phase 2 (where it is cited). |
| C-18 | **Intra-Phase 0 advancement gates** | reliability | aspirational | Phase 0 contains at least one explicit "do not advance" gate between its internal steps — not just an umbrella gate between phases. At minimum: the model must not proceed from the inertia cost step to the voice contract step until all three audience inertia costs are complete. The gate must use explicit advancement-blocking language ("do not advance to [next step] until [condition] complete"). Advisory field labels or sequential ordering alone do not pass. |
| C-19 | **Inline write gates at production points** | reliability | aspirational | The skill includes a collocated write-gate block at each artifact production point (spec, proposal, pitch). Each gate must: (1) confirm the file was written, (2) emit a "write it now" instruction if the file is missing, and (3) block phase advancement ("Do not begin Phase N+1 until [file] exists on disk"). Write-gate logic consolidated at orchestration start or placed in a final completion block does not pass — gates must be collocated with production. |
| C-20 | **Voice differentiation save gate** | reliability | aspirational | After the pitch is drafted and before any final index is emitted, the skill includes an explicit voice-differentiation check gate. The gate must verify that the exec version leads with outcomes, the dev version leads with capability, and the maker version uses jargon-free framing — and must direct the model to revise any version that fails its differentiation test before proceeding. A note or advisory reminder does not pass; the gate must block advancement and specify what constitutes a passing revision. |
| C-21 | **Stability citation lock** | correctness | aspirational | Three-point enforcement: (1) Phase 0 produces a named STABILITY CITATION RECORD block using a canonical output form (Form A or Form B), not a tag or summary; (2) Phase 2's Defeating Do Nothing block includes a verbatim-paste instruction — "copy the Form A or Form B sentence character for character, do not summarize, do not paraphrase"; (3) the Completion Check requires an affirmative "CITATION CONFIRMED / CITATION MISSING" declaration, not a checkbox. All three points must be present. A variation that produces Form A/B but omits the verbatim-paste instruction, or that declares CITATION CONFIRMED/MISSING without the named record block, does not pass. |
| C-22 | **Full intra-Phase 0 gate chain** | reliability | aspirational | Every adjacent non-terminal step-to-step transition within Phase 0 is explicitly gated with "do not advance" language. The terminal step must be identified (labeled `[TERMINAL]` or equivalent). A Phase 0 with N steps requires N−1 gates covering all sequential transitions (e.g., a four-step Phase 0 with one terminal step requires three gates: 0a→0b, 0b→0c, 0c→0d). A Phase 0 that gates only one transition (satisfying C-18's minimum) but leaves others unblocked does not pass. |
| C-23 | **Post-execution completion index** | structure | aspirational | A named, labeled block (e.g., `## COMPLETION INDEX`) listing all three artifacts with target file paths and confirmed existence status (`[exists / missing]` per row) is emitted after all write and recovery steps complete. This block must be structurally distinct from write gates (which fire at production time) and from recovery steps embedded in those gates. A flat checklist or inline list in the final summary does not pass; the block must be independently labeled and structurally separable. |
| C-24 | **COMPLETION INDEX gate audit row** | reliability | aspirational | The COMPLETION INDEX extends beyond artifact existence to include a dedicated gate-passage entry confirming the number of Phase 0 gates traversed (e.g., `Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b \| Gate 2: 0b→0c \| Gate 3: 0c→0d)`). A COMPLETION INDEX that lists only artifact existence rows without gate audit does not pass. The gate audit entry must name each gate individually, not merely assert a count. |
| C-25 | **Citation failure recovery path** | reliability | aspirational | The citation confirmation check includes an active recovery instruction for the failure case: if CITATION MISSING, the model is directed to return to the source phase and paste the citation record before stopping (e.g., "If CITATION MISSING: return to Phase 2 and paste the record before stopping"). A CITATION CONFIRMED/MISSING declaration without a recovery action does not pass. The recovery instruction must name the destination phase and the required action, not merely flag the missing state. |
| C-26 | **Voice contract backpointer anchoring** | structure | aspirational | Each pitch audience section (exec, dev, maker) contains an explicit reference to the Phase 0 voice contract that governs its register (e.g., "Use Step 0c exec voice contract as anchor"). The backpointer must name the source step and the audience — a generic instruction to "be audience-appropriate" does not pass. Pitch sections that produce correct voice differentiation without a named anchor to a prior-established contract also do not pass; traceability is required, not just output quality. |
