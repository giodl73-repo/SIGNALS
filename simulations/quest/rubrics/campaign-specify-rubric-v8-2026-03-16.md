Here is the complete v8 rubric:

---

**What changed from v7** — 3 new criteria + 1 criterion tightening:

| | |
|---|---|
| **C-27 tightened** | Pass condition now explicitly requires a formal `### Voice Compliance Audit` section with preamble enumeration. Bullet entries in a flat Additional index do not pass — aligning the written criterion with the intent ("formally classifies its contents… structurally named element") and how R7 applied it. |
| **C-32** | *Compliance categorization declaration in COMPLETION INDEX preamble.* V-05 adds "Each section classifies a distinct category of compliance state" beyond V-03's enumeration. Naming sections without declaring their categorical purpose does not pass. |
| **C-33** | *Per-audience verdicts in Voice Compliance Audit section.* C-27 + C-28 interaction: when both the formal section and per-audience gate verdicts exist, the audit section must record exec/dev/maker results separately. Combined single-line result fails. |
| **C-34** | *Step 0c contract anchor embedded in gate parenthetical Pass condition.* C-28 + C-29 interaction: when parenthetical criteria and Step 0c naming co-exist, the Step 0c contract name must appear inside the parenthetical Pass condition itself. Behavioral criteria without contract attribution fail. |

**Scoring formula**: `aspirational_pass / 26 * 10` (denom 23 → 26)

**R7 scores under v8:**

| Variation | Asp (of 26) | Composite | Earned |
|-----------|-------------|-----------|--------|
| V-01 | 21/26 | 98.1 | C-28 |
| V-02 | 21/26 | 98.1 | C-29 |
| V-03 | 21/26 | 98.1 | C-27 |
| V-04 | 22/26 | 98.5 | C-28, C-29 |
| V-05 | 24/26 | 99.2 | C-27, C-28, C-29, C-32 |

V-05 leads at 99.2. C-33 and C-34 remain unearned across all R7 variations — they require per-audience verdicts inside the Voice Compliance Audit section and Step 0c names inside the parenthetical Pass criteria, neither present in any R7 output. The R8 ceiling is 26/26.
nd the gate-criterion specificity gap that remain open at R7's 24/26 ceiling.

| Change | Pattern Source | What it addresses |
|--------|----------------|-------------------|
| C-27 pass condition tightened | R7 scorecard consistently fails bullet entries; v7 "formally classifies its contents... structurally named element" always required a formal section | Pass condition now explicitly requires a formal `### Voice Compliance Audit` section with preamble enumeration; bullet entries in a flat Additional index do not pass |
| C-32 (new) | V-05 C-27 refinement ("Each section classifies a distinct category of compliance state" present in V-05, absent in V-03) | Compliance categorization declaration in COMPLETION INDEX preamble — the preamble not only enumerates the four named sections but explicitly declares that each section classifies a distinct category of compliance state; section naming without categorization purpose does not pass |
| C-33 (new) | C-27 + C-28 interaction: per-audience gate verdict granularity projected to the audit record | Per-audience verdicts in Voice Compliance Audit section — when the formal Voice Compliance Audit section (C-27) and per-audience gate Pass/Fail (C-28) both exist, the audit section records individual verdicts for exec, dev, and maker separately; a combined single-line gate result does not pass |
| C-34 (new) | C-28 + C-29 interaction: Step 0c contract name embedded inside the parenthetical Pass criterion | Step 0c contract anchor embedded in gate parenthetical Pass condition — when parenthetical per-audience gate criteria (C-28) and Step 0c naming in Step 3 (C-29) both exist, the parenthetical Pass condition for each audience explicitly names the applicable Step 0c contract (e.g., "Pass (Step 0c exec voice contract satisfied: ...)"); parenthetical criteria without contract attribution do not pass |

**Scoring formula updated**: aspirational denominator 23 → 26.

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 26 * 10)
```

R7 variation scores under v8:

| Variation | Essential | Rec | Asp (of 26) | Composite | Criteria earned in R7 |
|-----------|-----------|-----|-------------|-----------|----------------------|
| V-01 | 5/5 | 3/3 | 21/26 | 98.1 | C-28 |
| V-02 | 5/5 | 3/3 | 21/26 | 98.1 | C-29 |
| V-03 | 5/5 | 3/3 | 21/26 | 98.1 | C-27 |
| V-04 | 5/5 | 3/3 | 22/26 | 98.5 | C-28, C-29 |
| V-05 | 5/5 | 3/3 | 24/26 | 99.2 | C-27, C-28, C-29, C-32 |

V-05 leads R7 at 99.2. No variation earns C-33 or C-34 — C-33 requires per-audience verdicts inside the Voice Compliance Audit section, and C-34 requires Step 0c contract names inside the parenthetical Pass criteria, neither of which appears in any R7 variation. The R8 target ceiling is 26/26: a variation that adds C-33 and C-34 to V-05's unified structure.

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
| C-27 | **Voice gate audit row in COMPLETION INDEX as formal classified section** | structure | aspirational | The COMPLETION INDEX contains a formally classified Voice Compliance Audit section: the preamble enumerates it by name alongside the other sections (e.g., Artifact Existence Record, Phase Gate Audit, Citation Audit, Voice Compliance Audit), and the section carries a structural header at the same heading level as the other COMPLETION INDEX sections. A voice gate result recorded as a bullet in a flat Additional index does not pass, even if the bullet names the result state. |
| C-28 | **Per-audience Pass/Fail in voice differentiation gate** | structure | aspirational | The voice differentiation gate issues independent Pass/Fail verdicts for each audience version — exec gate, dev gate, and maker gate each carry their own labeled result with parenthetical Pass/Fail criteria stating the observable behavioral standard (e.g., `Pass (opening names a business cost...) / Fail (opens with product description...)`), and an independence declaration confirms each audience gate must pass separately. A gate that uses "check" rather than "gate" labels, evaluates all three openings jointly, or carries only plain Pass/Fail without parenthetical behavioral criteria does not pass. |
| C-29 | **Contract-derived gate criteria with named rewrite anchor** | traceability | aspirational | The voice differentiation gate: (a) derives its expected-frame criteria by name from the Step 0c voice contracts in Step 3 (e.g., "frame of the Step 0c exec voice contract"), and (b) directs the rewrite instruction in Step 4 to the specific Step 0c contract for the failing audience as the revision anchor (e.g., "Return to the Step 0c contract for that audience as your revision anchor"). Both locations must name Step 0c; a single-location reference — or Step 3 using generic frame labels without naming Step 0c — does not pass. |
| C-30 | **Inline gate blocks carry step-pair annotation** | structure | aspirational | Each Phase 0 gate block in the skill body includes the step-pair transition in its inline label (e.g., `--- GATE 1 (0a→0b): Do not advance to Step 0b until... ---`), creating a verifiable correspondence between on-page gate labels and the COMPLETION INDEX gate audit row. Gate blocks labeled with a number only (e.g., `--- GATE 1: Do not advance...`) without step-pair notation do not pass. |
| C-31 | **Doubly-anchored voice contract traceability** | traceability | aspirational | The Step 0c voice contracts are referenced in two structural locations: (1) as production anchors in the pitch audience writing instructions, and (2) as named enforcement criteria within the voice differentiation gate check (e.g., the gate explicitly cites each audience's Step 0c contract as the frame being verified). Single-location references — production guidance only or gate criteria only — do not pass. |
| C-32 | **COMPLETION INDEX preamble declares compliance categorization purpose** | depth | aspirational | The COMPLETION INDEX preamble enumerates the four named sections AND explicitly declares that each section classifies a distinct category of compliance state (or equivalent statement of categorical purpose). Section enumeration without the categorization declaration does not pass — "The index has four named sections: ..." alone is insufficient; the preamble must additionally state what role those sections collectively serve in the compliance record. |
| C-33 | **Voice Compliance Audit section records per-audience verdicts** | depth | aspirational | When the formal Voice Compliance Audit section (C-27) and per-audience gate Pass/Fail (C-28) are both present, the Voice Compliance Audit section records the gate outcome per-audience — exec, dev, and maker each listed separately with individual verdicts. A combined single-line voice gate result does not pass. This criterion is only reachable when both C-27 and C-28 are earned; a variation that passes C-27 without C-28 cannot meet the per-audience granularity requirement. |
| C-34 | **Step 0c contract anchor embedded in gate parenthetical Pass condition** | traceability | aspirational | When parenthetical per-audience gate criteria (C-28) and Step 0c contract naming in Step 3 (C-29) are both present, the parenthetical Pass condition for each audience explicitly names the applicable Step 0c contract as the compliance source — e.g., "Pass (Step 0c exec voice contract satisfied: opening names a business cost...)" rather than "Pass (opening names a business cost...)". Parenthetical criteria that state behavioral observable standards without naming the Step 0c contract do not pass. This criterion is only reachable when both C-28 and C-29 are earned. |
