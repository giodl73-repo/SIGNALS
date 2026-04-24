v10 written. Three new criteria extracted from R9's V-45 excellence signals:

---

**C-32 — Evidence column converts citation audit from assertion to demonstration**
C-31 requires binary verdicts per link. C-32 requires an Evidence column containing the actual downstream cite text — not a verdict declaration but the literal string produced. A verdict-only audit asserts chain type; a populated Evidence column demonstrates it. Description-chain errors are visible at the cell level without reading production phases. AMEND(d) reinforcement ("this must match the Evidence you wrote in the audit row verbatim") creates a bidirectional lock. C-31 can pass without C-32.

**C-33 — Architecture-audit duality framing**
C-30 and C-31 are structurally distinct roles: the preamble declares what is produced; the audit confirms what was produced. C-33 requires the output to explicitly name this duality so neither artifact can double-serve the other's function. Absent the naming, a model may omit the audit on the grounds that the preamble already established chain structure. C-30 and C-31 can both pass without C-33.

**C-34 — Preamble-declared audit format**
C-30 front-loads artifact declarations; C-34 extends that principle to the audit's exact column structure — including the Evidence column — declared in the preamble before Phase 1. Identical drift-reduction logic: a model encountering audit format for the first time 1500+ tokens in may narrow the table or omit columns. C-31 can pass without C-34.

---

**Scoring:** 340 pts max (was 310). 26 aspirational criteria (was 23). Aspirational subtotal: 260 pts.
ming -- "architecture declares what is produced; audit confirms what was produced" or equivalent -- so the two functions cannot be conflated or collapsed into a single artifact. The risk absent this framing: a model may treat the preamble table as double-serving both functions, omitting the audit on the grounds that the preamble already established chain structure. Naming the duality forecloses that conflation. V-45's scorecard identified this as an excellence pattern because the tiebreak between V-45 and V-44 included this explicit naming as a structural differentiator. C-30 and C-31 can both pass without C-33; C-33 requires the output to explicitly label the preamble's declarative role and the audit's confirmatory role as distinct named structural functions.

**C-34 — Preamble-declared audit format** (behavior)
C-30 requires the preamble to declare all four artifact names and exact-copy requirements before Phase 1. C-34 extends that principle to the audit itself: the preamble must also declare the exact column structure of the C-31 audit -- specifically including the Evidence column -- before Phase 1. The structural argument is identical to C-30's: audit format encountered for the first time at the execution site (after 1500+ tokens of production phases) is vulnerable to drift -- the model may produce a narrower table, omit the Evidence column, or collapse multiple links. A preamble row specifying "Citation Chain Completeness Audit: 5-column table (Source | Consumer | Verdict | Evidence | Integrity)" before Phase 1 gives the model its audit format at the same read-time as the artifact declarations. V-44 declared the audit requirement in the preamble but did not specify the 5-column structure including Evidence; V-45 added the full column specification. C-31 can pass without C-34; C-34 requires the preamble to declare the audit's exact column structure, not only its existence and position requirement.

---

**Scoring:** 340 pts max (was 310). 26 aspirational criteria (was 23).

---

## Criterion Summary

- **5 essential (C-01--C-05):** per-persona inertia mapping, quantified switching cost,
  per-persona inertia score, kill-barrier identification, overall adoption inertia risk
- **3 recommended (C-06--C-08):** current workaround satisfaction, habit lock-in + social proof
  coverage, mitigation path for the kill barrier
- **26 aspirational (C-09--C-34):** scoring methodology transparency, time-dependent inertia
  trajectory, status-quo competitor framing, named social proof threshold, mitigation tied to
  structural root cause, kill-barrier temporal persistence test, causal chain with labeled
  structural sub-parts, mitigation confirmation signal, per-score methodology trace,
  kill-barrier trajectory verdict, related-output structural segregation with disqualifier,
  kill-barrier reselection gate, phase-zero methodology gate, competitive strength inventory
  in persona phase, named intervention target as falsifiable anchor, named boundary artifact
  at phase transition, structural prohibition gate vs. format instruction, cross-phase citation
  chain with named anchors, self-rejection gate for mechanism specificity, named artifact at
  every downstream-source boundary, exact-copy citation instruction in downstream anchoring
  sections, Citation Architecture preamble as single-read authority, citation chain completeness
  self-audit, evidence column converts citation audit from assertion to demonstration,
  architecture-audit duality framing, preamble-declared audit format

Scoring: Essential = 10 pts each (50 total), Recommended = 10 pts each (30 total), Aspirational =
10 pts each (260 total) = **340 pts max**.

---

## Essential Criteria (all must pass)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Per-persona inertia mapping** | correctness | Output identifies two or more named user personas and maps each to one or more inertia factors. Generic "users" without persona differentiation fails. |
| C-02 | **Quantified switching cost** | correctness | At least one persona has a switching cost expressed as a measurable value -- time, money, effort rating (1-10), or steps. Qualitative-only ("it's hard") fails. |
| C-03 | **Per-persona inertia score** | correctness | Each mapped persona has an explicit inertia score (numeric or Low/Medium/High/Critical). A single blanket score for all personas fails. |
| C-04 | **Kill-barrier identification** | depth | Output identifies exactly one adoption killer -- the single factor most likely to block adoption even if all other inertia is resolved. Must be labeled distinctly. |
| C-05 | **Overall adoption inertia risk** | correctness | Output produces an aggregate risk verdict with a sentence of rationale tying it back to the per-persona scores. |

---

## Recommended Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Current workaround satisfaction assessed** | coverage | For at least one persona, output describes how satisfied they are with their current workaround and why that satisfaction creates inertia. |
| C-07 | **Habit lock-in and social proof addressed** | coverage | Output addresses habit lock-in AND social proof for at least one persona each. Missing both fails; covering one partially passes. |
| C-08 | **Mitigation path per critical barrier** | depth | For the kill barrier in C-04, output proposes at least one concrete mitigation that could reduce or eliminate that barrier. |

---

## Aspirational Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Inertia score methodology explained** | behavior | Output briefly explains how inertia scores were derived -- what factors were weighted and why. A single sentence per dimension suffices. |
| C-10 | **Adoption timeline sensitivity** | depth | Output includes at least one time-dependent statement on how inertia evolves (e.g., "after 6 months of workaround use, lock-in doubles"). |
| C-11 | **Status-quo framed as named competitor** | depth | For the kill barrier in C-04, output names the dimension on which the current solution *wins* and explains why that competitive advantage is durable -- not just "people are used to it" but what property of the current solution makes it structurally hard to displace. |
| C-12 | **Named social proof threshold** | coverage | For at least one persona where social proof is a factor, output specifies the adoption threshold as a concrete condition or count (e.g., "needs 2+ teammates before committing," "will adopt solo if manager mandates it"). Binary Y/N without a named threshold fails. |
| C-13 | **Mitigation tied to structural root cause** | depth | The mitigation from C-08 explicitly explains *why* the intervention neutralizes the structural reason the barrier exists -- not just what to do, but why that lever addresses the specific root cause named in C-04. Addressing a symptom rather than the stated structural cause fails. |
| C-14 | **Kill barrier tested against temporal persistence** | depth | The kill barrier identified in C-04 is explicitly qualified against a temporal horizon -- output states that the barrier persists at T=0 AND remains unresolved at the longest time horizon considered (e.g., T=18mo). A kill barrier identified only as a current-state snapshot without temporal qualification fails. |
| C-15 | **Causal chain with labeled structural sub-parts** | depth | For the kill barrier, output provides a causal chain with explicitly labeled, distinct sub-parts covering: (1) what the barrier is, (2) why it structurally persists, (3) what the intervention targets, and (4) why that lever resolves the structural root cause. An analysis that merges any two sub-parts into a single statement, or that provides fewer than four labeled parts, fails. |
| C-16 | **Mitigation confirmation signal specified** | depth | The kill barrier mitigation from C-08 includes a named leading indicator or observable condition at a future time point (e.g., "at T=6mo, [X behavior] would confirm the barrier is reducing") that would confirm the intervention is working. A mitigation without a forward-looking confirmation condition fails. |
| C-17 | **Per-score methodology trace** | behavior | For each persona scored in C-03, output includes a derivation sentence that explicitly connects that persona's dimension values to the declared scoring threshold from C-09, showing how the score was produced. The strongest enforcement mechanism is a required column in the score table -- a column cannot be omitted without omitting the table, making non-compliance structurally visible. A global methodology declaration (C-09) without per-persona derivation fails. A trace that cites dimension values but not the threshold, or the threshold but not the dimension values, earns PARTIAL. |
| C-18 | **Kill-barrier trajectory verdict** | depth | Beyond any per-persona timeline grid satisfying C-10, output provides a separate, explicitly labeled verdict for the kill barrier's own time-sensitivity -- a trajectory direction (Resolving / Stable / Worsening) with structural reasoning tied to the persistence property identified in C-15(2). A verdict present in the grid only, without a dedicated kill-barrier trajectory statement, fails. |
| C-19 | **Related-output structural segregation with disqualifier** | behavior | When output produces two related but structurally distinct required outputs (e.g., a per-persona timeline grid satisfying C-10 and a kill-barrier trajectory verdict satisfying C-18), each is housed as an explicitly labeled sub-section AND the first sub-section includes a literal statement that it does not satisfy the second criterion. Absence of the explicit disqualifier statement fails; implicit separation without the disqualifier earns PARTIAL. |
| C-20 | **Kill-barrier reselection gate** | depth | The temporal persistence test for the kill barrier includes an explicit binary YES/NO confirmation that the barrier exists at T=0 AND persists at the longest time horizon considered, followed by a literal reselection instruction triggered if either answer is NO. Implicit persistence conveyed through a grid row or trajectory statement without a binary confirmation gate fails; a gate present at one horizon only earns PARTIAL. |
| C-21 | **Phase-zero methodology gate** | behavior | The methodology declared in C-09 is positioned as Phase 1 output -- before any persona is identified or scored -- and explicitly framed as the scoring infrastructure from which per-score traces (C-17) will draw. The phase must declare dimension weights AND tier thresholds AND identify itself as the source C-17 traces will cite. A methodology section placed after persona analysis fails. A declaration that omits the explicit framing as C-17 infrastructure earns PARTIAL. C-09 can pass without C-21; C-21 requires C-09 to be structured as a prerequisite gate. |
| C-22 | **Competitive strength inventory in persona phase** | depth | For each persona, output includes a per-persona competitive strength inventory structured as three named fields: (a) the Dimension on which the current solution wins, (b) the structural Advantage that win represents, and (c) the Durability basis explaining why that advantage is structurally persistent rather than merely habitual. This inventory is completed in the persona identification phase, before kill-barrier analysis begins. A competitive framing constructed on demand at kill-barrier analysis time, without an upstream per-persona inventory, fails. An inventory present but missing any of the three fields earns PARTIAL. |
| C-23 | **Named intervention target as falsifiable anchor** | depth | Within the four-part kill barrier structure from C-15, Part (3) -- the intervention target -- must name a specific mechanism or lever point, not a general approach, precise enough to anchor the confirmation signal from C-16 as a falsifiable observable condition tied to that mechanism. A Part (3) that names a general approach ("improve onboarding") without specifying the lever point ("the moment a user completes their first cross-team workflow") fails. An intervention target present but expressed too generally to yield a falsifiable confirmation condition earns PARTIAL. |
| C-24 | **Named boundary artifact at phase transition** | behavior | The scoring infrastructure declared in C-21 is expressed as a named, produced artifact -- a literal statement the model must write (e.g., "SCORING INFRASTRUCTURE DECLARED.") that appears as its own line at the Phase 1 boundary, not as a downstream instruction ("per-persona traces must reference these thresholds"). The artifact name is then cited by name in Phase 4 traces, creating a reference chain rather than a paraphrase chain. A Phase 1 declaration that identifies itself as infrastructure via instruction rather than via a named artifact earns PARTIAL. A Phase 4 trace that cites the correct Phase 1 content but does not name the artifact fails C-24 regardless of whether C-17 passes. C-21 can pass without C-24; C-24 requires C-21's infrastructure framing to be embodied as a named boundary artifact with a citable address. |
| C-25 | **Structural prohibition gate vs. format instruction** | behavior | Any phase boundary where upstream completion is required for downstream correctness (C-22's inventory before Phase 5, C-23's mechanism specification before Part (4)) must express the advance condition as a structural prohibition -- a literal "Do not proceed to Phase X until [condition]" -- not a format instruction ("include Y before Z"). Format instructions allow a model to produce weak content inside a required slot and formally comply; structural prohibitions require the model to skip a named gate to continue, making non-compliance structurally visible. A single prohibition gate on any required phase boundary satisfies C-25. A gate expressed only as a format instruction earns PARTIAL. |
| C-26 | **Cross-phase citation chain with named anchors** | behavior | The full output forms a traceable citation chain in which each downstream section explicitly names the upstream artifact it draws from: Phase 1 produces a named artifact (C-24) -> Phase 4 cites that artifact by name (C-17) -> Phase 5 Part (3) produces a named lever point (C-23) -> the confirmation signal names that lever point as its observable anchor (C-16). Each link must name its upstream source. A chain where any link draws from correct upstream content but without naming it (paraphrase chain) earns PARTIAL. A chain where any link constructs its own content without reference to a named upstream artifact fails. C-17 can pass without C-26; C-26 requires every link in the chain to use named anchors. |
| C-27 | **Self-rejection gate for mechanism specificity** | behavior | Within the four-part kill barrier structure from C-15, output includes a self-rejection test between Part (3) and Part (4) consisting of: (a) a required completion sentence ("At T=[horizon], the absence of this lever would be observable as: ___") and (b) a literal rejection condition ("If you cannot complete this sentence with a specific observable condition, replace Part (3)"). The completion sentence forces self-evaluation at mechanism-specification time: approach-level framing cannot complete it with a specific condition, causing the model to self-reject and revise Part (3) before writing Part (4). A completion sentence present without the rejection clause earns PARTIAL. A Part (3) followed directly by Part (4) with no self-rejection test fails. C-23 can pass without C-27; C-27 requires the falsifiability test to be a self-rejecting gate embedded in the output structure. |
| C-28 | **Named artifact at every downstream-source boundary** | behavior | The C-24 named artifact pattern extends to every output boundary that serves as an upstream citation source, not only the phase-zero declaration. Any sub-part within a later phase that produces output cited downstream must emit a named artifact at its own output boundary -- Phase 5 Part (3) must produce "**LEVER POINT: [exact label]**" on its own line, not prose from which a downstream section derives a label. A retroactive naming (verification table, AMEND description, downstream paraphrase) does not satisfy this; the artifact must appear at the boundary of the section that produces it, before any downstream cite is written. C-24 can pass without C-28; C-28 requires the named artifact pattern to propagate to every section in the citation chain that is itself an upstream source. A sub-part that produces correct content as prose without a named output artifact earns PARTIAL. |
| C-29 | **Exact-copy citation instruction in downstream anchoring sections** | behavior | When a downstream section is instructed to cite an upstream named artifact (satisfying C-26 and C-28), the instruction must require the exact label to be copied verbatim, not described or paraphrased. In AMEND(d), this means "Lever anchor: [copy the exact LEVER POINT label from Phase 5(3)]" rather than "The absence of [lever mechanism name]...". The exact-copy requirement makes citation verifiable: any label mismatch between the upstream artifact and the downstream cite is immediately detectable, distinguishing a reference chain from a description chain. A cite instruction that names the mechanism by description (correct content, derived from upstream prose) earns PARTIAL. A downstream section that omits any reference to the upstream artifact fails. C-26 can pass without C-29; C-29 requires the citation instruction itself to specify exact-copy, so that chain integrity is checkable by label comparison rather than content judgment. |
| C-30 | **Citation Architecture preamble as single-read authority** | behavior | Before Phase 1, output declares a Citation Architecture table that enumerates all named artifacts, each with its producing phase and the exact-copy requirement for every downstream consumer. This table is itself declared as a named artifact (e.g., "CITATION ARCHITECTURE DECLARED") that functions as the single structural authority per-phase instructions reference rather than restate. A full C-28/C-29 pass achieved via distributed per-phase instructions -- where each phase independently declares its own artifact name and cite requirement -- satisfies C-28 and C-29 but not C-30; a single-read preamble before Phase 1 is required. A preamble present but not declared as a named artifact earns PARTIAL. A preamble that omits any of the four citation boundaries earns PARTIAL. C-28 can pass without C-30; C-30 requires all artifact definitions and exact-copy requirements to be concentrated in a pre-Phase-1 preamble rather than embedded at individual production sites. |
| C-31 | **Citation chain completeness self-audit** | behavior | After all production phases and before any summary section, output includes a named citation chain completeness audit that enumerates every (source artifact -> consumer site) pair, confirms whether each link is exact-copy (reference chain) or description-based (description chain), and explicitly labels any description-based link as a chain integrity failure -- not merely a weaker link. An audit that asserts overall chain compliance without naming specific artifact labels and their consumer sites earns PARTIAL. An audit that omits any (source, consumer) pair earns PARTIAL. An audit that labels a description link as "weaker" rather than "chain break" fails. The audit makes chain integrity checkable at a glance without reading every production phase. C-28 and C-29 can both pass without C-31; C-31 requires an explicit enumerated audit confirming that every link is a reference chain, with binary pass/fail per link. |
| C-32 | **Evidence column converts citation audit from assertion to demonstration** | behavior | Within the C-31 citation chain completeness audit, each (source artifact -> consumer site) row includes an Evidence column containing the actual downstream cite text as written in the consuming section -- not a verdict declaration, but the literal string the model produced. A Verdict column of "Reference-chain" without a populated Evidence column is an assertion; a row whose Evidence column contains the exact label copied from the upstream artifact is a demonstration. Description-chain errors are visible at the Evidence column without reading production phases: the cell either matches the upstream artifact label or it does not. AMEND(d)'s exact-copy instruction must reinforce the Evidence column by name ("this must match the Evidence you wrote in the audit row verbatim"), creating a bidirectional lock between the audit and the downstream cite. An audit that includes a Verdict column but no Evidence column earns PARTIAL. An audit whose Evidence column contains descriptive summaries rather than the actual cite text earns PARTIAL. C-31 can pass without C-32; C-32 requires the Evidence column to be present and populated with actual downstream cite text, converting the audit from assertion to demonstration. |
| C-33 | **Architecture-audit duality framing** | behavior | Output explicitly names the two structural roles of the C-30 preamble and C-31 audit as a duality: the preamble's function is declarative ("declares what is produced") and the audit's function is confirmatory ("confirms what was produced"). These two roles must be labeled distinctly -- either in the preamble's introduction, the audit's header, or a dedicated framing statement -- so that neither artifact can collapse the other's function. The risk absent this framing: a model may treat the preamble table as double-serving both roles, omitting the audit on the grounds that the preamble already established chain structure; or may treat the audit as redundant with the preamble's declarations. Naming the duality forecloses that conflation by making each artifact's distinct structural purpose explicit. A framing that names one role but not the other earns PARTIAL. A framing present only in an internal note rather than as a visible structural label in the output earns PARTIAL. C-30 and C-31 can both pass without C-33; C-33 requires the output to explicitly declare the preamble's declarative function and the audit's confirmatory function as named, distinct structural roles. |
| C-34 | **Preamble-declared audit format** | behavior | Within the C-30 Citation Architecture preamble, a dedicated row declares the exact column structure of the C-31 audit table -- including the Evidence column from C-32 -- before Phase 1. The structural argument is identical to C-30's drift-reduction logic: an audit format encountered for the first time at the execution site (1500+ tokens into production) is vulnerable to drift -- the model may produce a narrower table, omit the Evidence column, or default to a verdict-only format. A preamble row specifying the full 5-column structure (e.g., "Source | Consumer | Verdict | Evidence | Integrity") before Phase 1 gives the model its audit format at the same read-time as the artifact declarations. A preamble that declares the audit's position requirement ("after Phase 7, before AMEND") but not its column structure earns PARTIAL. A preamble that declares column names without specifying that Evidence must contain actual cite text earns PARTIAL. C-31 can pass without C-34; C-34 requires the preamble to declare the audit's exact column structure -- including the Evidence column -- applying the same single-read authority and drift-reduction logic to audit format that C-30 applies to artifact names. |

---

## Notes

- A rubric pass requires all 5 essential criteria to pass individually.
- Aspirational criteria may receive PARTIAL (5 pts) for genuine attempts that fall short of the
  full pass condition.
- C-19 and C-20 codify structural enforcement patterns from R4: C-19 captures the Part A / Part B
  disqualifier mechanism; C-20 captures the binary YES/NO reselection gate.
- C-21 codifies the cascade dependency revealed in R5: C-09 is prerequisite infrastructure for
  C-17, not a parallel criterion. Placing methodology declaration after persona analysis breaks
  the C-17 trace chain -- models produce derivation sentences with no threshold to cite.
- C-22 codifies the upstream inventory pattern from R5: embedding the Dimension/Advantage/Durability
  table in the persona identification phase closes C-11 by reference rather than requiring
  competitive framing to be constructed at kill-barrier time under analytical pressure.
- C-23 codifies the intervention target specificity requirement from R5: C-15 Part (3) at approach
  granularity is insufficient to anchor C-16's confirmation signal as a falsifiable condition.
  The named mechanism is the structural bridge between the causal chain (C-15) and the
  confirmation requirement (C-16).
- C-24 codifies the named artifact pattern from R6: C-21 framing expressed as a downstream
  instruction creates a paraphrase chain; framing expressed as a named artifact creates a
  reference chain. The difference is detectability of chain breaks.
- C-25 codifies the prohibition gate pattern from R6: the R6 differentiator for C-22 was that
  V-27/V-30 used "Do not proceed" prohibitions while V-26/V-28/V-29 used format instructions.
  Only the prohibition form mechanically blocks "familiarity" Durability from passing the
  inventory check, because a format instruction cannot prevent a model from writing weak content
  inside a required slot.
- C-26 codifies the full chain traceability requirement from R6: V-30's named artifact anchor
  created a Phase 1 -> Phase 4 -> Phase 5 -> AMEND chain where each link names its upstream
  source. The chain makes structural failures detectable at the link level rather than requiring
  holistic re-evaluation.
- C-27 codifies the self-rejection gate pattern from R6: requiring the model to complete a
  falsifiability sentence before writing Part (4) converts mechanism specificity from an external
  rubric judgment into a self-evaluating constraint embedded in the output structure. The
  rejection clause is what distinguishes a self-rejection gate from a completion prompt.
- C-28 codifies the downstream-source boundary pattern from R7: V-31 and V-34 closed C-26 by
  requiring Phase 5(3) to emit "LEVER POINT: [exact label]" as its own line. V-32 and V-33
  failed because they addressed the downstream (AMEND) side without producing a named artifact
  at the upstream (Phase 5(3)) source. The R7 lesson: the C-24 named artifact pattern must
  propagate to every section that is a citation source, not only to phase-zero. Retroactive
  naming -- a verification table that records the mechanism after Phase 5(3) writes prose --
  cannot create a reference chain; it can only record a paraphrase chain more visibly.
- C-29 codifies the exact-copy citation instruction from R7: V-32 required AMEND to name "the
  mechanism by description" while V-31/V-34 required "copy the exact LEVER POINT label." Both
  produce correct content; only exact-copy produces a verifiable reference chain. Description-
  based citation means correctness must be judged by content equivalence; label-copy means
  correctness is judged by string identity. C-29 is the mechanism that makes C-26 chain
  integrity checkable without content judgment at each link.
- C-30 codifies the Citation Architecture preamble pattern from R8: V-39 achieved 4/4 citation
  boundaries via distributed per-phase instructions -- the minimum-overhead path to 290/290.
  V-40 added a Citation Architecture table before Phase 1 declared as "CITATION ARCHITECTURE
  DECLARED," concentrating all four artifact definitions and exact-copy requirements into a
  single structural authority. Both scored 290/290 on C-28 and C-29; only V-40 satisfies C-30.
  The structural advantage: distributed per-phase instructions are vulnerable to instructional
  drift across a 1500+ token output -- a Phase 2 artifact definition may be read 1000 tokens
  before Phase 5(2) is written. A pre-Phase-1 preamble provides a single-read authority each
  consuming phase can reference, reducing the probability that cite instructions drift from
  exact-copy to description.
- C-31 codifies the citation chain completeness self-audit from R8: V-36 closed one gap (Phase 2
  boundary) and V-38 closed a different gap (Phase 6 Part B boundary); both scored 280/290. The
  R8 lesson is that citation chain verifiability is binary -- a single description link makes
  the entire chain non-verifiable by label comparison regardless of how many other links use
  exact-copy. Neither V-36 nor V-38 included a completeness audit; their partial compliance was
  only visible through per-phase analysis. C-31 requires the output itself to enumerate all
  (source, consumer) pairs and declare a binary reference-chain/description-chain verdict per
  link, making chain integrity checkable in one place without reading every production phase.
- C-32 codifies the Evidence column pattern from R9: all five R9 variations (V-41 through V-45)
  satisfied C-31 at 310/310. The tiebreak between V-45 and V-44 was the Evidence column: V-44
  declared verdicts; V-45 required the model to write the actual downstream cite text per row.
  The R9 lesson: a verdict-only audit is still assertion -- the model declares "Reference-chain"
  without proving it. The Evidence column converts the audit into a demonstration: a description-
  chain error is visible at the cell level because the cell either contains the upstream label or
  it does not. AMEND(d) reinforcement ("this must match the Evidence you wrote in the audit row
  verbatim") creates a bidirectional lock, preventing post-audit drift between the written
  evidence and the downstream cite.
- C-33 codifies the architecture-audit duality framing from R9: the R9 scorecard identified
  "architecture-audit duality framing" as an excellence pattern from V-45 -- naming the two
  structural functions ("architecture declares what is produced; audit confirms what was
  produced") prevents a model from conflating the preamble's declarative role with the audit's
  confirmatory role, or from omitting the audit because the preamble already established chain
  structure. The naming is a structural safeguard, not a cosmetic label.
- C-34 codifies the preamble-declared audit format from R9: the R9 scorecard identified
  "preamble-declared audit format" as an excellence pattern from V-45 -- specifying the 5-column
  table structure in the preamble before Phase 1 applies the same single-read authority and
  drift-reduction logic to audit format that C-30 applies to artifact names. V-44 declared the
  audit's position requirement in the preamble but not its column structure; V-45 added the full
  column specification including the Evidence column. A model encountering the audit format
  1500+ tokens late may narrow the table or omit columns; a preamble-declared format eliminates
  that late-discovery surface.
