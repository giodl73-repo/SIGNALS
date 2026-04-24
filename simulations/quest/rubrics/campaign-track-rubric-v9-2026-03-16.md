Reading the scorecard carefully, I find two new structural patterns from V-05 that are distinct from C-25 through C-28. Each names a pass condition that could discriminate a future variation.

**C-29 — Order-dependent item annotation** (behavior)
V-05 adds a terminal closing note that explicitly names `verdict_after` as "the only order-dependent item" and instructs "verify it last." This is structurally distinct from C-25 (which governs the two-pass mechanism itself) — C-29 governs the terminal checklist's own meta-annotation of which items carry ordering constraints and why.

**C-30 — Postcondition-linked contract annotation** (format)
V-05 extends the Phase 3 active-role header with: "Both contracts are active at this phase. Both artifacts are required to satisfy the Phase 3 postcondition." This is distinct from C-26 (naming both contracts) and C-27 (conjunction postcondition gate) — C-30 requires the header annotation to explicitly bridge the two, connecting the active-role declaration to the postcondition semantics in a single normative statement.

Aspirational count goes from 15 to 17; max from 110 to 116.

---

# Quest Rubric — campaign-track — v9

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

**C-25 -- Two-pass delta update** *(from R8 V-01)* | aspirational | behavior
Phase 3 Step B writes `verdict_after = "NOT YET REACHED"` as a declared placeholder; a named Post-Phase-4 update step then overwrites it with the actual `verdict_verb`; the terminal checklist item for `verdict_after` is order-dependent with explicit "placeholder fails after Phase 4 completes" language. Pass: declared two-pass protocol section present; Phase 3 Step B writes the placeholder with normative language; Post-Phase-4 update step present as a named section; terminal `verdict_after` item states order dependency and names the placeholder as a fail condition once Phase 4 has run. A single-pass judgment call or missing Post-Phase-4 update section fails.

**C-26 -- Dual-contract active-role annotation** *(from R8 V-02)* | aspirational | format
The Phase 3 active-role header names both the Phase 3 Contract and the Session Delta Contract; a normative rule declares that naming one contract and omitting the other is a structural defect. Pass: `## Dual-Contract Annotation Rule` section present with normative language; Phase 3 header explicitly names both active contracts. A header that names only one contract, or a rule section without a conforming Phase 3 header, fails.

**C-27 -- Conjunction progression gate** *(from R8 V-03)* | aspirational | behavior
Phase 3 postcondition is `status.md AND delta.md BOTH present`; an explicit statement declares that writing `status.md` alone does not satisfy the postcondition. Pass: Phase 3 postcondition names both artifacts with conjunction language ("AND", "BOTH"); normative statement present that single-artifact completion does not satisfy the gate; GATE statement uses conjunction. A postcondition that names only `status.md`, or a conjunction without the single-artifact-failure statement, fails.

**C-28 -- Empty-list sentinel type-tightening** *(from R8 V-05)* | aspirational | correctness
Output fields that may produce an empty list are typed with a named sentinel value (e.g., `["NONE"]`) rather than a bare empty list (`[]`); the sentinel is declared as the canonical empty representation; a truly empty list is stated as a contract violation for that field. Pass: at least one list-typed output field carries a declared named sentinel; the contract states that `[]` (untyped empty) fails for that field; the sentinel value appears in the Empty-State section as the prescribed value for zero-signal conditions. A field that permits bare empty lists without a sentinel declaration, or a sentinel present without a stated `[]`-failure condition, fails.

**C-29 -- Order-dependent item annotation** *(from R8 V-05)* | aspirational | behavior
The terminal checklist explicitly identifies which items carry ordering constraints — naming them as order-dependent, stating what prior steps must have completed before verification, and instructing "verify last" (or equivalent). Pass: at least one terminal checklist item annotated as order-dependent; annotation names the specific prior steps that must precede it (e.g., "after Phase 4 and the Post-Phase-4 Delta Update have both completed"); annotation states that verifying the item before its dependencies is a checklist protocol violation. A checklist with no ordering annotations, a generic "verify in sequence" without naming the dependency chain, or an order-dependent item with no "verify last" instruction fails.

**C-30 -- Postcondition-linked contract annotation** *(from R8 V-05)* | aspirational | format
The active-role annotation for a multi-contract phase explicitly bridges the contract listing to the phase postcondition in a single normative statement: "Both contracts are active at this phase. Both artifacts are required to satisfy the [Phase N] postcondition." Pass: phase annotation names both active contracts AND includes an explicit sentence linking both artifacts to the phase postcondition by name; the linkage is normative (states requirement), not descriptive. Naming both contracts without the postcondition linkage (C-26 alone), or stating a conjunction postcondition gate without the header annotation (C-27 alone), does not satisfy this criterion. Both elements must appear as a unified statement.

---

## Scoring Model

| Tier | Points each | Criteria |
|------|-------------|----------|
| Essential | 10 | C-01..C-05 (5 criteria) |
| Recommended | 5 | C-06..C-08 (3 criteria) |
| Aspirational | 3 | C-09..C-16, C-22..C-30 (17 criteria) |

**Max**: `5×10 + 3×5 + 17×3 = 116`

**Baseline** (all five variations pass all criteria): `50 + 15 + 51 = 116`

New differential criteria in v9: C-29, C-30 — 3 pts each, max +6 over v8.
