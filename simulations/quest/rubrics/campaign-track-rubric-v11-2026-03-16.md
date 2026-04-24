Reading the R10 scorecard, I identify two new excellence patterns from the R10 PASS+ signals (V-05 extended forms), both following the assertion→causal-explanation pattern established by C-31/C-32, applied at two new declaration sites. C-33, C-34, and C-35 — tested as new criteria in R10 — are simultaneously promoted to rubric status.

**C-36** — from V-05's C-33 PASS+: the Phase 4 obligation header goes beyond bare obligation declaration to naming the specific stale-value consequence — `verdict_after` in `delta.md` becomes stale if Phase 4 completes without the post-write. Causal framing at the activation site — assertion → named consequence. Mirrors C-32's failure-path framing at Phase 3 header.

**C-37** — from V-05's C-35 PASS+: the cascade rule goes beyond naming trigger, target, and scope exclusion to explaining WHY non-cascade fields are excluded — they were finalized at Phase 3 and Phase 4 cannot change them. Causal scope justification vs. bare enumeration. Mirrors C-31's upstream-dependency explanation.

Aspirational count goes from 19 to 24; max from 122 to 137.

---

# Quest Rubric — campaign-track — v11

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

**C-17 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-18 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-19 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-20 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-21 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-22 -- Prohibition-count parity** *(from R6 V-01)* | aspirational | correctness
All four roles carry the same declared count of forbidden actions, and that count is stated as a structural constraint — not just a coincidence of implementation. The symmetry makes compliance mechanically auditable: checking one role's count tells you the valid count for all others, and any deviation is a visible defect. Pass: explicit parity rule declared (e.g., "exactly N forbidden actions — no more, no fewer") with N >= 3; all four role blocks confirm the same count; count is verifiable without reading action content. Unequal counts across roles, undeclared count, or parity rule present without all four roles conforming all fail.

**C-23 -- Full-phase type coverage** *(from R6 V-02)* | aspirational | format
A declared rule that all four phases must have typed output contracts, with partial coverage (fewer than four phases typed) explicitly stated as structurally invalid. The rule is normative, not advisory — a phase without a typed contract is an incomplete phase, not an optional gap. Pass: rule statement present asserting that partial-phase typing is invalid + all four phase contracts present with type constraints (enumerated token sets, integer declarations, format strings, or per-field fail conditions). A prompt that types two or three phases without declaring the coverage rule, or that declares the rule without delivering all four contracts, fails.

**C-24 -- Field-level terminal checklist** *(from R6 V-03)* | aspirational | behavior
The terminal completion checklist itemizes named output fields as the unit of verification — not phases. Each item declares: the field name, the required constraint (type, value set, or non-null condition), and the fail action if the field does not satisfy the constraint. Pass: at least three terminal checklist items structured as field-level checks (field + constraint + fail action); items cover fields from at least two different phase artifacts. A checklist that checks "Phase X complete" as a single line without naming specific output fields fails.

**C-25 -- Two-pass write protocol** *(from R8 V-05)* | aspirational | behavior
`delta.md` write instructions specify two distinct write passes keyed to phase boundaries: Pass 1 after Phase 3 (coverage and analysis fields); Pass 2 after Phase 4 (verdict fields, specifically `verdict_after`). Pass: write protocol names both passes and their respective write points; each pass identifies which fields are written. A single write instruction covering all fields, or write instructions without named phase boundaries, fails.

**C-31 -- Terminal closing note with upstream-dependency explanation** *(from R9 V-05 C-29 PASS+)* | aspirational | correctness
The terminal closing note goes beyond naming what is order-dependent to explaining why — naming the specific upstream field or phase that creates the ordering constraint. Causal explanation vs. bare assertion. Pass: closing note names the upstream dependency (e.g., Phase 4 `verdict_verb`) that creates the ordering constraint and explains the causal chain. A closing note that asserts ordering without naming the upstream dependency fails.

**C-32 -- Phase 3 header with named failure path** *(from R9 V-05 C-30 PASS+)* | aspirational | behavior
The Phase 3 header goes beyond bridging both contracts to the postcondition to naming a specific failure scenario at the declaration site — a concrete example of what it looks like to violate the postcondition. Pass: Phase 3 header includes a named failure path (e.g., "A model that writes status.md and advances to Phase 4 without delta.md has not satisfied the Phase 3 postcondition"). Bridging language that states the postcondition without a named failure scenario fails.

**C-33 -- Phase 4 obligation header** *(from R10 V-01)* | aspirational | behavior
Phase 4 header declares the `delta.md` post-Phase-4 write as a mandatory obligation before Phase 4 execution begins. Forward declaration at the activation site — the model enters Phase 4 knowing the post-write is mandatory, not optional. Pass: Phase 4 section opens with an explicit obligation statement for the post-Phase-4 `delta.md` write; obligation present at Phase 4 header, not deferred to terminal section only. No obligation declaration, or obligation declared only in the terminal section, fails.

**C-34 -- Terminal section opening protocol** *(from R10 V-02)* | aspirational | behavior
Terminal section opens with an explicit execution-order protocol naming: normal execution order plus the `verdict_after` exception. Brackets the checklist from the opening side; C-31's closing note brackets from the closing side. Pass: terminal section begins with an order statement that names both the normal order and the `verdict_after` exception rule before any checklist items appear. A terminal section that opens directly with checklist items without an order protocol fails.

**C-35 -- Cascade invalidation rule** *(from R10 V-03)* | aspirational | behavior
An explicit cascade invalidation rule naming all three components: trigger condition (Phase 3 Step B re-run), cascade target (`verdict_after` only), and scope exclusion (other `delta.md` fields not affected). Pass: all three components present — trigger, cascade target, and scope exclusion. A cascade mention that names trigger and target without scope exclusion, or that lists scope exclusion without naming the trigger condition, fails.

**C-36 -- Phase 4 obligation header with stale-value consequence** *(from R10 V-05 C-33 PASS+)* | aspirational | correctness
The Phase 4 obligation header goes beyond bare obligation declaration to naming the specific stale-value consequence: `verdict_after` in `delta.md` becomes stale if Phase 4 completes without the post-write. Causal framing at the activation site — assertion → named consequence. Mirrors C-32's failure-path framing at Phase 3 header; extends C-33 from obligation to obligation + consequence. Pass: Phase 4 obligation statement names the specific field that becomes stale (`verdict_after`) and the condition that produces staleness (Phase 4 completing without the post-write). Bare obligation declaration without named stale-value consequence fails.

**C-37 -- Cascade rule with causal scope justification** *(from R10 V-05 C-35 PASS+)* | aspirational | correctness
The cascade rule goes beyond naming trigger, target, and scope exclusion to explaining WHY non-cascade fields are excluded: they were finalized at Phase 3 and Phase 4 cannot change them. Causal scope justification vs. bare enumeration. Mirrors C-31's upstream-dependency explanation; extends C-35 from scope assertion to scope assertion + causal justification. Pass: scope exclusion explanation names the finalization point (Phase 3) as the reason non-cascade fields are excluded from re-verification. Scope exclusion listed without causal justification fails.
