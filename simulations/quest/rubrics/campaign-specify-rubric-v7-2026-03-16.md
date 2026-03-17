Reading the scorecard carefully to identify the new excellence patterns before writing.

The scorecard surfaces five distinct PASS+ mechanisms not yet captured as standalone criteria:

1. **C-24 V-04 PASS+** — COMPLETION INDEX preamble formally classifies its contents, including the voice gate result as a structurally named element
2. **C-24 V-05 PASS+** — Inline Phase 0 gate blocks carry step-pair annotations matching the COMPLETION INDEX gate audit row
3. **C-20 V-02** — Per-audience Pass/Fail structure in voice gate (three independent verdicts)
4. **C-20 V-03** — Contract-derived gate criteria; rewrite anchor names the Step 0c contract for the failing audience
5. **C-26 V-03/V-05 PASS+** — Voice contracts doubly anchored: production guidance in pitch instructions AND named enforcement criteria in the gate

These become C-27–C-31. Aspirational denominator: 18 → 23.

---

# Scoring Rubric: campaign-specify (v7)

## What changed from v6

Five new aspirational criteria extracted from R6 excellence signals. Each targets a mechanism that only becomes visible when C-20 is co-present with the V-04 COMPLETION INDEX and V-03/V-05 contract traceability patterns.

| New ID | Pattern Source | What it measures |
|--------|----------------|------------------|
| C-27 | V-04 C-20 evidence ("Voice differentiation gate result: distinct / rewritten-to-distinct" in COMPLETION INDEX) | Voice gate audit row in COMPLETION INDEX — the COMPLETION INDEX records the voice differentiation gate outcome as a named audit entry, extending the post-execution record beyond artifacts and phase-gate passage to include voice compliance state |
| C-28 | V-02 C-20 evidence (per-audience criteria with individual Pass/Fail) | Per-audience Pass/Fail in voice differentiation gate — the gate issues independent verdicts for each audience version rather than a single combined check; exec gate / dev gate / maker gate each carry their own Pass/Fail |
| C-29 | V-03 C-20 evidence (gate criteria derived from Step 0c contracts; rewrite directed to "Step 0c contract for that audience") | Contract-derived gate criteria with named rewrite anchor — the voice gate derives its expected-frame criteria by name from the Step 0c voice contracts, and the rewrite instruction directs the model to the specific Step 0c contract for the failing audience as the revision anchor |
| C-30 | V-05 C-24 PASS+ ("inline gate lines include step-pair in their own label") | Inline gate blocks carry step-pair annotation — each Phase 0 gate block in the skill body includes the step-pair in its inline label (e.g., `--- GATE 1 (0a→0b): Do not advance...`), creating a verifiable correspondence between on-page gate labels and COMPLETION INDEX gate audit rows |
| C-31 | V-03/V-05 C-26 PASS+ ("contracts function as production guidance AND enforcement criteria") | Doubly-anchored voice contract traceability — the Step 0c voice contracts are referenced both as production anchors in pitch writing instructions and as named enforcement criteria in the voice differentiation gate check; single-location references do not pass |

**Scoring formula updated**: aspirational denominator 18 → 23.

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 23 * 10)
```

R6 variation scores under v7:

| Variation | Essential | Rec | Asp (of 23) | Composite | New criteria earned |
|-----------|-----------|-----|-------------|-----------|---------------------|
| V-01 | 5/5 | 3/3 | 18/23 | 97.8 | — |
| V-02 | 5/5 | 3/3 | 19/23 | 98.3 | C-28 |
| V-03 | 5/5 | 3/3 | 20/23 | 98.7 | C-29, C-31 |
| V-04 | 5/5 | 3/3 | 19/23 | 98.3 | C-27 |
| V-05 | 5/5 | 3/3 | 20/23 | 98.7 | C-30, C-31 |

V-03 and V-05 lead R6 at 98.7. No variation earns all five new criteria simultaneously. The R7 target ceiling is 23/23: a variation that unifies C-27 (COMPLETION INDEX voice audit row), C-28 (per-audience Pass/Fail), C-29 (contract-derived criteria), C-30 (inline gate step-pair annotation), and C-31 (doubly-anchored contracts) in a single skill.

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
| C-16 | **Structured Recommendation labeled blocks** | structure | aspirational | The Proposal Recommendation section contains at least two independently labeled subsections — one defeating Do Nothing by name and one defeating the strongest competing option — each under its own header (e.g., `#### Defeating Do Nothing`, `#### Defeating [Option Name]`). A recommendation that co-mixes the defeating arguments without structural separation does not pass. |
| C-17 | **Verbatim paste instruction** | reliability | aspirational | The skill includes an explicit instruction to paste the citation record verbatim into the proposal, with an explicit prohibition on summarizing or paraphrasing. An instruction that says "include the record" without prohibiting paraphrase does not pass. |
| C-18 | **Stability Citation Record with form selection** | structure | aspirational | The skill defines at least two citation record forms (e.g., FORM A for direct evidence, FORM B for absence-of-evidence), each requiring complete-sentence prose. A citation record format that accepts tag-only entries (e.g., bullet labels without prose sentences) fails explicitly. |
| C-19 | **Phase 0 gate chain with step labels** | structure | aspirational | Each Phase 0 gate block is labeled with a gate number and names the next step it blocks (e.g., `--- GATE 1: Do not advance to Step 0b until... ---`). Phase 0 that contains progression criteria without labeled gate blocks does not pass. |
| C-20 | **Voice differentiation save gate** | reliability | aspirational | The skill includes a gate collocated with the pitch save instruction that: (1) specifies the expected opening frame for each of the three audience versions; (2) includes a conditional rewrite instruction that activates when any two openings share the same frame; (3) requires re-running the check after rewriting; and (4) explicitly blocks the pitch save until all three openings are frame-distinct. A gate missing any of these four legs does not pass. |
| C-21 | **Citation CONFIRMED/MISSING declaration** | reliability | aspirational | The COMPLETION INDEX includes a dedicated row for citation status using the prescribed declaration form: "CITATION CONFIRMED" or "CITATION MISSING". An implicit or positional record (e.g., leaving the citation field blank) does not pass. |
| C-22 | **Step-pair labels in Phase 0 gate chain header** | structure | aspirational | The Phase 0 header includes a gate chain summary that names each gate with its step-pair transition (e.g., `Gate 1 (0a→0b) | Gate 2 (0b→0c) | Gate 3 (0c→0d)`). A Phase 0 header that names gates without step-pair notation does not pass. |
| C-23 | **COMPLETION INDEX structurally distinct from write gates** | structure | aspirational | The COMPLETION INDEX is introduced by a preamble that explicitly identifies it as a post-execution audit record, distinct from in-phase write gates. A COMPLETION INDEX that appears without such a preamble — or that is formatted as a phase checkpoint rather than a post-run record — does not pass. |
| C-24 | **COMPLETION INDEX gate audit row** | structure | aspirational | The COMPLETION INDEX includes a dedicated entry confirming phase-gate passage (e.g., `Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)`). A COMPLETION INDEX that records artifacts but omits a gate-passage confirmation entry does not pass. |
| C-25 | **Citation failure recovery path** | reliability | aspirational | The citation check includes an active recovery instruction directing the model back to the source phase when the citation is absent (e.g., "If CITATION MISSING: return to Phase 2 and paste the record before stopping."). A declaration-only check — one that names the missing state but gives no recovery action — does not pass. |
| C-26 | **Voice contract backpointer anchoring** | traceability | aspirational | Each pitch audience section explicitly references the Phase 0 voice contract that governs its register (e.g., "Use Step 0c exec voice contract as anchor"). Audience versions produced without a named backpointer to a prior-established voice contract do not pass. |
| C-27 | **Voice gate audit row in COMPLETION INDEX** | structure | aspirational | The COMPLETION INDEX includes a dedicated entry recording the voice differentiation gate outcome as a named result state (e.g., `Voice differentiation gate result: distinct / rewritten-to-distinct`). A COMPLETION INDEX that records artifacts, gate chain passage, and citation status but omits the voice gate result does not pass. |
| C-28 | **Per-audience Pass/Fail in voice differentiation gate** | structure | aspirational | The voice differentiation gate issues independent Pass/Fail verdicts for each audience version — exec gate, dev gate, and maker gate each carry their own labeled result. A gate that evaluates all three openings jointly without per-audience verdicts does not pass. |
| C-29 | **Contract-derived gate criteria with named rewrite anchor** | traceability | aspirational | The voice differentiation gate: (a) derives its expected-frame criteria by name from the Step 0c voice contracts rather than from generic register descriptions, and (b) directs the rewrite instruction to the specific Step 0c contract for the failing audience as the revision anchor (e.g., "Return to the Step 0c contract for that audience as your revision anchor"). A gate with generic expected-frame labels (e.g., "opens with business outcome") that does not name its source contract does not pass. |
| C-30 | **Inline gate blocks carry step-pair annotation** | structure | aspirational | Each Phase 0 gate block in the skill body includes the step-pair transition in its inline label (e.g., `--- GATE 1 (0a→0b): Do not advance to Step 0b until... ---`), creating a verifiable correspondence between on-page gate labels and the COMPLETION INDEX gate audit row. Gate blocks labeled with a number only (e.g., `--- GATE 1: Do not advance...`) without step-pair notation do not pass. |
| C-31 | **Doubly-anchored voice contract traceability** | traceability | aspirational | The Step 0c voice contracts are referenced in two structural locations: (1) as production anchors in the pitch audience writing instructions, and (2) as named enforcement criteria within the voice differentiation gate check (e.g., the gate explicitly cites each audience's Step 0c contract as the frame being verified). Single-location references — production guidance only or gate criteria only — do not pass. |
