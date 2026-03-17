Reading the scorecard carefully, I find four new patterns from V-05 that are structurally distinct from anything in v7, each naming a specific pass condition that could discriminate a future variation.

The four new criteria are:

- **C-25** — Two-pass delta update (behavior)
- **C-26** — Dual-contract active-role annotation (format)
- **C-27** — Conjunction progression gate (behavior)
- **C-28** — Empty-list sentinel type-tightening (correctness)

Aspirational count goes from 11 to 15; max from 98 to 110.

---

# Quest Rubric — campaign-track — v8

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
Terminal checklist items operate at individual artifact field granularity — each named field independently verifiable — rather than at phase artifact granularity (artifact present, roughly complete). Field-level items are mechanically auditable; phase-level items require judgment. Pass: >= 10 terminal items, each naming a specific artifact field (e.g., `topic_name`, `namespace`, `coverage_ratio`, `verdict_verb`) with a targeted FAIL action that names the re-run phase (e.g., "FAIL action: re-run Phase 1"); at least one item uses array-field notation (e.g., `planned_signals[*].target_skill`). A checklist that lists phases rather than fields, or lists fields without targeted FAIL actions, fails.

**C-25 -- Two-pass delta update** *(from R7 V-05)* | aspirational | behavior
The signal: V-05 writes delta.md in Phase 3 Step B with a typed placeholder for `verdict_after` (because Phase 4 has not yet run), then resolves the placeholder in a named post-Phase-4 update step. The terminal checklist flags "placeholder fails" for `verdict_after` as the only order-dependent constraint — making the two-pass sequence a structural contract, not a side note. The excellence is separation: delta *creation* is Phase 3's responsibility; delta *completion* is Phase 4's postcondition. Pass: Phase 3 writes delta.md with all delta fields including a typed placeholder for `verdict_after`; a distinct post-Phase-4 step names `verdict_after` as the field being resolved with the actual verdict token; terminal checklist has an item for `verdict_after` that explicitly flags placeholder value as a FAIL condition. A delta written entirely post-Phase-4, or one where `verdict_after` is not flagged in the terminal, fails.

**C-26 -- Dual-contract active-role annotation** *(from R7 V-05)* | aspirational | format
The signal: V-05's Phase 3 header names both the Phase 3 Output Contract AND the Session Delta Contract at the execution site — when a phase produces two artifacts, both contracts are announced where the work happens, not only in a consolidated contracts section elsewhere in the prompt. This makes multi-artifact scope visible at the point of execution and prevents a scorer or executor from missing the supplemental contract. Pass: any phase producing two or more artifacts names all associated output contracts in that phase's section header or opening block; the annotation is present at the execution site (phase section), not solely in a dedicated contracts section. A phase that produces two artifacts but names only one contract at the execution site fails, even if the second contract appears elsewhere in the prompt.

**C-27 -- Conjunction progression gate** *(from R7 V-03/V-05)* | aspirational | behavior
The signal: V-03 and V-05's Phase 3 postcondition reads "status.md AND delta.md both present" — the conjunction syntax makes the supplemental artifact (delta.md) non-skippable via the gate itself, rather than leaving it as an appendage after Phase 4. A single-artifact gate cannot enforce supplemental artifacts; only a conjunction gate can. The excellence is the structural mechanism: the gate is what makes the second artifact mandatory, not a separate rule or checklist item. Pass: at least one progression gate uses explicit conjunction syntax naming two or more required artifacts (e.g., "[Artifact A] AND [Artifact B] both present"); at least one named artifact in the conjunction is a supplemental artifact that would be optional under a single-artifact gate. A gate that lists only one artifact, or that references the supplemental artifact only in a post-phase note rather than in the gate condition, fails.

**C-28 -- Empty-list sentinel type-tightening** *(from R7 V-05)* | aspirational | correctness
The signal: V-05's terminal checklist explicitly rejects the string sentinel `"NONE"` for `signals_added` and requires the empty list `[]` for the zero case. Prior versions typed `signals_added` as a list but allowed the string `"NONE"` as a first-invocation fallback — a type inconsistency that makes the field untyped in practice. The excellence is closing that gap: the zero case and the non-zero case share the same declared type, eliminating a hidden sentinel branch. Pass: at least one list-typed field in the output contracts or terminal checklist includes an explicit constraint that rejects string sentinels (e.g., "string 'NONE' fails — use `[]`") and names the empty list as the required zero-case value; the constraint is stated as a hard rule, not an advisory note. A list field that permits string sentinels in any case, or that declares the empty list as preferred without prohibiting string sentinels, fails.

---

## Scoring

| Tier | Points each | Criteria count | Subtotal |
|------|-------------|----------------|---------|
| Essential | 10 | 5 (C-01--C-05) | 50 |
| Recommended | 5 | 3 (C-06--C-08) | 15 |
| Aspirational | 3 | 15 (C-09--C-16, C-22--C-28) | 45 |
| **Max** | | | **110** |
