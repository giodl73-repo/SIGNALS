Now I have enough. Three distinct excellence patterns are visible in the R4 scorecards that are not captured in any v4 criterion:

1. **V-01 vs V-02 on C-17**: V-01 passes because the stability assessment uses a canonical output form (Form A / Form B) enabling verbatim citation in Phase 2, plus the Completion Check confirms the cite was made. V-02 fails because it produces only a one-word tag — no citeable anchor. This is a new cross-phase citation fidelity pattern.

2. **V-01 on C-18 with two gates**: C-18 passes with "at least one" gate. V-01 earns it with TWO gates (0a→0b, 0b→0c), covering every adjacent transition. Full chain coverage is a stricter new pattern.

3. **V-02's Completion Index on C-11**: V-02's evidence mentions a "Completion Index" — a named, structured post-execution block listing artifacts with paths and existence status. Distinct from write gates (C-19) and the recovery completion check (C-11). New structural pattern.

---

# Scoring Rubric: campaign-specify (v5)

## What changed from v4

Three new aspirational criteria extracted from R4 excellence signals across V-01 and V-02. Each targets a different enforcement gap not closed by C-18, C-19, or C-11.

| New ID | Pattern Source | What it measures |
|--------|----------------|------------------|
| C-21 | V-01 vs V-02 divergence on C-17 | Stability assessment as canonically-worded citeable form — Phase 0 must produce a named output statement (Form A/Form B), not a tag; Phase 2 must cite it verbatim; Completion Check must confirm the citation was made |
| C-22 | V-01 C-18 evidence (two gates, 0a→0b and 0b→0c) | Full intra-Phase 0 gate chain — every adjacent step-to-step transition within Phase 0 is explicitly gated, not just at least one (upgrades C-18's minimum-one requirement to full-coverage requirement) |
| C-23 | V-02 C-11 evidence (Completion Index block) | Post-execution completion index — a named, labeled block listing all three artifacts with target file paths and confirmed existence status, emitted after all write and recovery steps; structurally distinct from write gates (C-19) and the recovery check (C-11) |

**Scoring formula updated**: aspirational denominator 12 → 15.

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 15 * 10)
```

R4 variation scores under v5:

| Variation | Essential | Rec | Asp (of 15) | Composite | New criteria earned |
|-----------|-----------|-----|-------------|-----------|---------------------|
| V-01 | 5/5 | 3/3 | 12/15 | 98.0 | C-21, C-22 |
| V-02 | 5/5 | 3/3 | 10/15 | 96.7 | C-23 |
| V-03 | — | — | — | — | Scorecard incomplete (cut off at C-12) |

V-01 leads R4 at 98.0. C-19, C-20, and C-23 remain unearned by V-01; C-21 and C-22 remain unearned by V-02. No R4 variation earns all fifteen aspirational criteria. C-19 + C-20 + C-21 + C-22 + C-23 together define the R5 target ceiling.

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
| C-19 | **Per-artifact inline write gates** | reliability | aspirational | A write gate appears immediately after each artifact production step — three gates total, one per artifact, collocated with the production instruction for that artifact. Each gate triggers an immediate write if the artifact is missing before the next phase begins. An end-of-skill completion check covering all three artifacts does not pass this criterion (that satisfies C-11, not C-19). C-19 requires the gate to fire at the point of production, not after all phases complete. |
| C-20 | **Voice differentiation as save gate** | reliability | aspirational | Before the pitch artifact is saved to disk, an explicit verification step checks whether the three pitch versions have distinct opening frames. The check must include a conditional rewrite trigger: if two or more versions share the same opening frame, the model must rewrite until distinct before saving. A post-write reminder that does not block saving does not pass; a verification check without a rewrite trigger does not pass. Both the check and the rewrite condition are required. |
| C-21 | **Stability assessment as canonically-worded citeable form** | correctness | aspirational | The Phase 0 stability assessment must be output as a canonically-worded named statement — Form A: "Do Nothing is not stable: [rationale]" or Form B: "Do Nothing is stable: [rationale]" — not a one-word tag, category label, or paraphrase. The canonical form must be structured specifically to enable verbatim citation: Phase 2 must reproduce it verbatim in the defeat block, not summarize or restate it. Additionally, the completion check must confirm the verbatim citation was made. A variation that produces a citeable form in Phase 0 but paraphrases it in Phase 2 does not pass; a variation that produces only a tag (e.g., "worsening") even if Phase 2 expands on it does not pass. All three elements required: canonical output form in Phase 0, verbatim cite in Phase 2, confirmation in completion check. |
| C-22 | **Full intra-Phase 0 gate chain** | reliability | aspirational | Every adjacent step-to-step transition within Phase 0 has an explicit advancement-blocking gate. C-18 requires at least one gate covering the minimum transition (inertia cost step → voice contract step); C-22 requires the full chain — if Phase 0 has N steps, N-1 gates must be present, one for each transition. Each gate uses explicit blocking language ("do not advance to [next step] until [condition] complete"). Partial coverage — gating some transitions but not all — does not pass. A variation that earns C-18 with a single gate does not earn C-22 unless all other Phase 0 transitions are also explicitly gated. |
| C-23 | **Post-execution completion index** | reliability | aspirational | After all phases and recovery steps complete, the skill emits a named, explicitly-labeled completion index block (e.g., "Completion Index" or equivalent header) listing each expected artifact by name, target file path, and confirmed existence status. This block is structurally distinct from: write gates (C-19), which fire at artifact production points; and the recovery completion check (C-11), which triggers rewrites for missing artifacts. The completion index is a receipt — it records what exists, not what to do if something is missing. An unlabeled post-completion summary does not pass. A named block that omits file paths or existence confirmation does not pass. The index must appear as a separate labeled structure after all artifact production and recovery instructions are complete. |
