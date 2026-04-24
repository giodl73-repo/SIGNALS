Reading the scorecard, I identify two new excellence patterns from the R9 PASS+ signals (V-05 extended forms), which are structurally distinct from C-29 and C-30 themselves:

**C-31** — from V-05's C-29 PASS+: the terminal closing note goes beyond naming what is order-dependent to explaining *why* — naming the specific upstream dependency (Phase 4 `verdict_verb`) that creates the ordering constraint. Causal explanation vs. bare assertion.

**C-32** — from V-05's C-30 PASS+: the Phase 3 header goes beyond bridging both contracts to the postcondition to naming the specific failure path ("A model that writes status.md and advances to Phase 4 without delta.md has not satisfied the Phase 3 postcondition"). Named failure scenario at the declaration site.

Aspirational count goes from 17 to 19; max from 116 to 122.

---

# Quest Rubric — campaign-track — v10

## Essential Criteria

**C-01 -- Four-phase structure** | essential | format
Prompt declares exactly four named phases in order: registration, planning, analysis, narration (or labeled equivalents). Pass: four labeled phase sections present and sequenced. Fewer phases, merged phases, or unlabeled sections fail.

**C-02 -- Artifact-per-phase discipline** | essential | format
Each phase produces exactly one named artifact written to disk at a declared path. Pass: four artifact names present, each unique, each with a write path. Phases that produce no artifact or share an artifact fail.

**C-03 -- Nine-namespace coverage table** | essential | coverage
Phase 3 output includes a coverage table with exactly nine namespace rows. Each row carries: namespace label, planned signal count, collected signal count, missing signal count, zero-signal flag. Pass: all nine namespace rows present; each row has all five fields; table is a structured artifact, not prose. Fewer rows, missing fields, or prose substitutes fail.

**C-04 -- Readiness verdict from enumerated set** | essential | correctness
Final readiness verdict is drawn from exactly the three-token set: `READY | NOT READY | CONDITIONALLY READY`. Pass: enumerated set declared; verdict constrained to it; no other verdict tokens admitted. Free-text verdicts or sets with additional tokens fail.

**C-05 -- Narrative verdict with evidence** | essential | depth
Phase 4 produces a narrative verdict that names: verdict token (from enumerated set), hypothesis mutation (s0 + current state), echo findings, and at least three next-signal recommendations. Pass: all four components present in Phase 4 output. A bare verdict token with no supporting evidence fails.

---

## Recommended Criteria

**C-06 -- Artifact write paths** | recommended | format
Every phase section ends with an explicit "Write to:" line naming the full artifact path including topic variable and date. Pass: all four phases have declared write paths matching the `simulations/{namespace}/{topic}-{artifact}-{date}.md` pattern. Phases with implicit or missing paths fail.

**C-07 -- Coverage ratio and readiness statement** | recommended | format
Numeric ratio (X/N) + labeled readiness verdict (READY / NOT READY / CONDITIONALLY READY).

**C-08 -- Cross-namespace signal balance** | recommended | coverage
Per-namespace breakdown; zero-signal namespaces flagged explicitly.

---

## Aspirational Criteria

**C-09 -- Echo integration** | aspirational | depth
Unexpected findings called out distinctly from planned coverage. Pass: at least one explicit echo entry with "if none: NONE" fallback.

**C-10 -- Dual-session delta** | aspirational | behavior
Session delta section: signals added, verdict change summary.

**C-11 -- Role-gated phases** *(from R1 V-01)* | aspirational | correctness
Each phase assigns a distinct named AI persona (Registrar / Planner / Analyst / Narrator). Pass: four distinct role labels, consistent assignment — Registrar does not synthesize, Narrator does not plan. Generic "Assistant" labels fail.

**C-12 -- Explicit progression gates** *(from R1 V-01)* | aspirational | behavior
Phase ordering enforced as a hard constraint via "do not proceed until [artifact X] is written" gates. Pass: at least one explicit gate statement between adjacent phases. A bare numbered list with no gating language fails.

**C-13 -- Empty-state as named section** *(from R1 V-01)* | aspirational | behavior
Zero-signal first-invocation documented as a dedicated labeled section addressing each phase individually. Pass: distinct section present with per-phase behavior. A single buried sentence fails.

**C-14 -- Per-role prohibition lists** *(from R2 V-01)* | aspirational | correctness
Each assigned persona carries an explicit enumerated list of disallowed behaviors — named forbidden actions, not just a role description. Pass: at least two roles with one or more named prohibited actions each. Implicit prohibition inferred from role title alone fails.

**C-15 -- Typed output contracts per phase** *(from R2 V-04)* | aspirational | format
Each phase's output artifact specifies exact value types or format contracts: cell values typed as integers, verdict fields typed as one of an enumerated set, required fields named. Pass: at least two phases with typed output specifications. Narrative descriptions without type/value constraints fail.

**C-16 -- Terminal completion checklist** *(from R3 V-05)* | aspirational | behavior
A terminal section with per-phase PASS conditions that gates final dashboard emission. Distinguishes targeted phase re-run ("re-run Phase X only") from full campaign restart. Pass: terminal section present; each phase has named PASS condition; targeted re-run language present; consolidated dashboard emitted only when all terminal items pass. A bare summary with no gating conditions fails.

**C-22 -- Prohibition-count parity** *(from R6 V-01)* | aspirational | correctness
All four roles carry the same declared count of forbidden actions, and that count is stated as a structural constraint — not just a coincidence of implementation. The symmetry makes compliance mechanically auditable: checking one role's count tells you the valid count for all others, and any deviation is a visible defect. Pass: explicit parity rule declared (e.g., "exactly N forbidden actions — no more, no fewer") with N >= 3; all four role blocks confirm the same count; count is verifiable without reading action content. Unequal counts across roles, undeclared count, or parity rule present without all four roles conforming all fail.

**C-23 -- Full-phase type coverage** *(from R6 V-02)* | aspirational | format
A declared rule that all four phases must have typed output contracts, with partial coverage (fewer than four phases typed) explicitly stated as structurally invalid. The rule is normative, not advisory — a phase without a typed contract is an incomplete phase, not an optional gap. Pass: rule statement present asserting that partial-phase typing is invalid + all four phase contracts present with type constraints (enumerated token sets, integer declarations, format strings, or per-field fail conditions). A prompt that types two or three phases without declaring the coverage rule, or that declares the rule without delivering all four contracts, fails.

**C-24 -- Field-level terminal checklist** *(from R6 V-03)* | aspirational | behavior
The terminal completion checklist itemizes named output fields as the unit of verification — not phases. Each item declares: the field name, the required constraint (type, value set, or non-null condition), and the fail action if the field does not satisfy the constraint. Pass: at least three terminal checklist items structured as field-level checks (field + constraint + fail action); items cover fields from at least two different phase artifacts. A checklist that checks "Phase X complete" as a single line without naming specific output fields fails.

**C-25 -- Two-pass write protocol** *(from R8 V-05)* | aspirational | behavior
The Session Delta Contract implements a two-pass write mechanism: Pass 1 writes a placeholder delta.md at the Phase 3 boundary; Pass 2 updates it after Phase 4 completes with the final verdict comparison. The constraint that `verdict_after` is a "post-Phase-4 only write" is named explicitly. Pass: both passes declared; placeholder mechanism named; post-Phase-4 update instruction present. Single-pass write or unmarked update fails.

**C-26 -- Dual-contract Phase 3 naming** *(from R8 V-05)* | aspirational | format
Phase 3 section header explicitly names both active output contracts: the primary Phase 3 Contract (for status.md) and the Session Delta Contract (for delta.md). Pass: both contract names present in the Phase 3 header or opening material; neither is implied. Naming only one contract, or naming neither, fails.

**C-27 -- Conjunction postcondition gate** *(from R8 V-05)* | aspirational | behavior
Phase 3 gate statement enforces a conjunction constraint: "Do not proceed to Phase 4 until BOTH [artifact-A] AND [artifact-B] satisfy their contracts." Pass: GATE statement at Phase 3 boundary uses explicit conjunction (both/and) naming both required artifacts. A gate that checks only one artifact or uses disjunction fails.

**C-28 -- Session delta verdict fields** *(from R8 V-05)* | aspirational | format
The Session Delta Contract declares exactly three typed fields: `verdict_before` (set at Phase 3 close, sourced from Phase 3 readiness verdict), `verdict_after` (set post-Phase 4), and `verdict_changed` (boolean derived from comparison). Pass: all three fields named with types or sourcing annotations in the delta contract specification; `verdict_changed` stated as a derived boolean. Missing fields or untyped fields fail.

**C-29 -- Order-dependent item annotation** *(from R8 V-05)* | aspirational | behavior
The terminal checklist section contains a closing note — at the end of the terminal section itself, not in a pre-terminal section — that explicitly names `verdict_after` as "the only order-dependent item" and instructs "verify it last." Structural position is load-bearing: a model executing the checklist in sequence must encounter the ordering rule at the verification site. Pass: closing note present inside the terminal section naming `verdict_after` as uniquely order-dependent and instructing last-verification. Placement in a pre-terminal section, a preamble, or elsewhere in the prompt fails.

**C-30 -- Postcondition-linked contract annotation** *(from R8 V-05)* | aspirational | format
The Phase 3 active-role header bridges both contract names to the postcondition semantics in a single normative statement: "Both contracts are active at this phase. Both artifacts are required to satisfy the Phase 3 postcondition." This annotation must appear at the header itself — not only at the GATE statement (C-27). Pass: header contains the postcondition bridge statement connecting both active contracts to the Phase 3 postcondition. A header that names both contracts (C-26) without explicitly linking them to the postcondition fails.

**C-31 -- Order-constraint causal explanation** *(from R9 V-05)* | aspirational | depth
The terminal closing note, beyond naming `verdict_after` as the only order-dependent item (C-29), provides a causal explanation: it names the specific upstream dependency — the Phase 4 field or artifact value — that makes `verdict_after` order-dependent. This makes the ordering rule derivable from first principles rather than an asserted constraint. Pass: terminal closing note names the upstream Phase 4 value (e.g., `verdict_verb`) that `verdict_after` depends on and states that this value is unavailable until after the campaign's last artifact write. A closing note that names the ordering constraint without explaining its cause fails.

**C-32 -- Named failure scenario at postcondition header** *(from R9 V-05)* | aspirational | correctness
The Phase 3 active-role header, beyond bridging both contracts to the postcondition (C-30), names the specific failure path in a normative statement: the exact sequence of actions that constitutes a postcondition violation. Pass: header contains a statement of the form "A model that [specific action sequence] has not satisfied the Phase 3 postcondition" — identifying the failure path by naming the artifact written and the premature advance taken. A header that states only the requirement (both artifacts required) without naming the failure mode fails.

---

*Scoring: 5 essential × 10 + 3 recommended × 5 + 19 aspirational × 3 = **122 max***
