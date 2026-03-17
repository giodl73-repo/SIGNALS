Good — V-05 shows four patterns not visible in the V-01–V-04 scorecard: stability trajectory dimension in Phase 0, named defeat blocks, voice differentiation as a save gate, and scout signal routing annotation. Combined with V-04's per-artifact inline gates and V-01's intra-phase advancement gates, I have five distinct new excellence patterns for v4.

---

# Scoring Rubric: campaign-specify (v4)

## What changed from v3

Five new aspirational criteria extracted from R3 excellence signals across V-01 through V-05. Each targets a different structural enforcement mechanism — not content quality but *forcing functions* that prevent criterion decay under model context pressure.

| New ID | Pattern Source | What it measures |
|--------|----------------|------------------|
| C-16 | V-04/V-05 recommendation structure | Do Nothing defeat as a named structural block, separate from the comparative defeat of other options |
| C-17 | V-05 Step 0b + Phase 2 recommendation | Do Nothing stability trajectory — whether inaction is stable or worsening — cited in the defeat block |
| C-18 | V-01 Phase 0 gate language | Explicit intra-Phase 0 advancement gate — "do not advance until X complete" between steps within Phase 0 |
| C-19 | V-04 per-artifact write gates | Per-artifact inline write gates during execution (three gates, one per artifact at production point) vs. a single end-of-skill completion check |
| C-20 | V-05 Phase 3 save gate | Voice differentiation as a save gate — the pitch artifact cannot be saved until a verification check confirms distinct opening frames, with a conditional rewrite trigger |

**Scoring formula updated**: aspirational denominator 7 → 12.

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
```

R3 variation scores under v4:

| Variation | Essential | Rec | Asp (of 12) | Composite | New criteria earned |
|-----------|-----------|-----|-------------|-----------|---------------------|
| V-01 | 5/5 | 3/3 | 8/12 | 96.7 | C-18 |
| V-02 | 5/5 | 3/3 | 7/12 | 95.8 | — |
| V-03 | 5/5 | 3/3 | 6/12 | 95.0 | — |
| V-04 | 5/5 | 3/3 | 9/12 | 97.5 | C-16, C-19 |
| V-05 | 5/5 | 3/3 | 10/12 | 98.3 | C-16, C-17, C-20 |

V-05 is now the sole 100-minus leader. C-17 and C-20 remain unearned by any R3 variation and define the R4 target ceiling. C-19 (per-artifact gates) is only earned by V-04 — V-05 uses an end-of-skill table instead, passing C-11 but not C-19. No variation earns all five new criteria.

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
| C-16 | **Do Nothing defeat as named structural block** | structure | aspirational | The Recommendation section contains a dedicated, labeled "Defeating Do Nothing" block (or equivalent named header) that is structurally separate from the comparative defeat of other options. Inline defeat language embedded in a combined recommendation paragraph does not pass — the Do Nothing defeat must be independently traceable by label. |
| C-17 | **Do Nothing stability trajectory in defeat block** | depth | aspirational | The Do Nothing analysis includes an explicit stability dimension: whether the cost of inaction is stable or worsening over time. The Phase 2 defeat block must reference this stability assessment (e.g., "Do Nothing is not stable: [cite assessment]" or "this cost compounds over time"). A static one-time cost citation without trajectory argument does not pass. The stability dimension must appear in both Phase 0 (where it is established) and Phase 2 (where it is cited). |
| C-18 | **Intra-Phase 0 advancement gates** | reliability | aspirational | Phase 0 contains at least one explicit "do not advance" gate between its internal steps — not just an umbrella gate between phases. At minimum: the model must not proceed from the inertia cost step to the voice contract step until all three audience inertia costs are complete. The gate must use explicit advancement-blocking language ("do not advance to [next step] until [condition] complete"). Advisory field labels or sequential ordering alone do not pass. |
| C-19 | **Per-artifact inline write gates** | reliability | aspirational | A write gate appears immediately after each artifact production step — three gates total, one per artifact, collocated with the production instruction for that artifact. Each gate triggers an immediate write if the artifact is missing before the next phase begins. An end-of-skill completion check covering all three artifacts does not pass this criterion (that satisfies C-11, not C-19). C-19 requires the gate to fire at the point of production, not after all phases complete. |
| C-20 | **Voice differentiation as save gate** | reliability | aspirational | Before the pitch artifact is saved to disk, an explicit verification step checks whether the three pitch versions have distinct opening frames. The check must include a conditional rewrite trigger: if two or more versions share the same opening frame, the model must rewrite until distinct before saving. A post-write reminder that does not block saving does not pass; a verification check without a rewrite trigger does not pass. Both the check and the rewrite condition are required. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.
