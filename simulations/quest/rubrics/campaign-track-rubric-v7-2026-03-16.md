Here is the complete v7 rubric. The three new criteria and their design rationale:

---

**C-22 -- Prohibition-count parity** *(correctness)*
The signal: V-01 declared "exactly 5 forbidden actions — no more, no fewer" with structural invalidity for any deviation. The excellence is not the count itself but the *symmetry rule* — auditing one role tells you the valid count for all others, making any violation immediately visible. Pass requires the parity rule declared explicitly + all four role blocks conforming to the same N.

**C-23 -- Full-phase type coverage** *(format)*
The signal: V-02 opened with a normative rule that partial typing is structurally invalid — "a phase without a typed contract is an incomplete phase." C-15 only required two phases; C-23 requires the *coverage rule itself* to be present plus all four contracts delivered. A prompt that types all four phases without declaring the rule doesn't pass — the rule is what makes the coverage auditable.

**C-24 -- Field-level terminal checklist** *(behavior)*
The signal: V-03's terminal section had 22 items each naming a specific artifact field (`topic_name`, `planned_signals[*].target_skill`, `coverage_ratio`, etc.) plus a targeted FAIL action per item. C-16 only required phase-level PASS conditions; C-24 requires field granularity with array-field notation and targeted re-run actions. Phase-level items are judgment calls; field-level items are mechanical.

The max stays at **98 pts** — the scorecard already reflected these three criteria at 3 pts each, absorbing into the existing aspirational pool.
+ gap reason.

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
Each phase assigns a distinct named AI persona (Registrar / Planner / Analyst / Narrator). Pass: four distinct role labels, consistent assignment -- Registrar does not synthesize, Narrator does not plan. Generic "Assistant" labels fail.

**C-12 -- Explicit progression gates** *(from R1 V-01)* | aspirational | behavior
Phase ordering enforced as a hard constraint via "do not proceed until [artifact X] is written" gates. Pass: at least one explicit gate statement between adjacent phases. A bare numbered list with no gating language fails.

**C-13 -- Empty-state as named section** *(from R1 V-01)* | aspirational | behavior
Zero-signal first-invocation documented as a dedicated labeled section addressing each phase individually. Pass: distinct section present with per-phase behavior. A single buried sentence fails.

**C-14 -- Per-role prohibition lists** *(from R2 V-01)* | aspirational | correctness
Each assigned persona carries an explicit enumerated list of disallowed behaviors -- named forbidden actions, not just a role description. Pass: at least two roles with one or more named prohibited actions each. Implicit prohibition inferred from role title alone fails.

**C-15 -- Typed output contracts per phase** *(from R2 V-04)* | aspirational | format
Each phase's output artifact specifies exact value types or format contracts: cell values typed as integers, verdict fields typed as one of an enumerated set, required fields named. Pass: at least two phases with typed output specifications. Narrative descriptions without type/value constraints fail.

**C-16 -- Terminal completion checklist** *(from R3 V-05)* | aspirational | behavior
A terminal section with per-phase PASS conditions that gates final dashboard emission. Distinguishes targeted phase re-run ("re-run Phase X only") from full campaign restart. Pass: terminal section present; each phase has named PASS condition; targeted re-run language present; consolidated dashboard emitted only when all terminal items pass. A bare summary with no gating conditions fails.

**C-22 -- Prohibition-count parity** *(from R6 V-01)* | aspirational | correctness
All four roles carry the same declared count of forbidden actions, and that count is stated as a structural constraint -- not just a coincidence of implementation. The symmetry makes compliance mechanically auditable: checking one role's count tells you the valid count for all others, and any deviation is a visible defect. Pass: explicit parity rule declared (e.g., "exactly N forbidden actions -- no more, no fewer") with N >= 3; all four role blocks confirm the same count; count is verifiable without reading action content. Unequal counts across roles, undeclared count, or parity rule present without all four roles conforming all fail.

**C-23 -- Full-phase type coverage** *(from R6 V-02)* | aspirational | format
A declared rule that all four phases must have typed output contracts, with partial coverage (fewer than four phases typed) explicitly stated as structurally invalid. The rule is normative, not advisory -- a phase without a typed contract is an incomplete phase, not an optional gap. Pass: rule statement present asserting that partial-phase typing is invalid + all four phase contracts present with type constraints (enumerated token sets, integer declarations, format strings, or per-field fail conditions). A prompt that types two or three phases without declaring the coverage rule, or that declares the rule without delivering all four contracts, fails.

**C-24 -- Field-level terminal checklist** *(from R6 V-03)* | aspirational | behavior
Terminal checklist items operate at individual artifact field granularity -- each named field independently verifiable -- rather than at phase artifact granularity (artifact present, roughly complete). Field-level items are mechanically auditable; phase-level items require judgment. Pass: >= 10 terminal items, each naming a specific artifact field (e.g., `topic_name`, `namespace`, `coverage_ratio`, `verdict_verb`) with a targeted FAIL action that names the re-run phase (e.g., "FAIL action: re-run Phase 1"); at least one item uses array-field notation (e.g., `planned_signals[*].target_skill`). A checklist that lists phases rather than fields, or lists fields without targeted FAIL actions, fails.

---

## Scoring

| Tier | Points each | Criteria count | Subtotal |
|------|-------------|----------------|---------|
| Essential | 10 | 5 (C-01--C-05) | 50 |
| Recommended | 5 | 3 (C-06--C-08) | 15 |
| Aspirational | 3 | 11 (C-09--C-16, C-22--C-24) | 33 |
| **Max** | | | **98** |
