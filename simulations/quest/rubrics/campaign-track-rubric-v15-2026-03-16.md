# Quest Rubric — campaign-track — v15

Three new aspirational criteria (C-43 – C-45) extracted from R15 excellence signals ES-1, ES-2, ES-3. Aspirational count: 31 → 34. Max score: 158 → 167.

---

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

**C-22 through C-39 -- *(from prior versions — text not available in provided excerpt)*** | aspirational |

**C-40 -- Triptych temporal-axis independence labels at header level** *(from R14 V-01/V-04/V-05)* | aspirational | format
Phase headers carry a temporal-axis independence qualifier at the header level itself — not buried in body text only. Pass: at least one phase header contains an auditable qualifier (e.g. bracket label, inline tag) that identifies the axis variation; qualifier readable without entering the body. Qualifiers present only in body prose fail.

**C-41 -- Bidirectional Phase Boundary Summary at four surfaces** *(from R14 V-02/V-04/V-05)* | aspirational | behavior
Phase boundary back-references appear at all four named surfaces: obligation block, active-role header, Narrator prohibition, and TERMINAL gate. Pass: each of the four surfaces carries a back-reference to the prior phase's artifact or closure state. Presence at fewer than four surfaces is partial credit; absence at all surfaces fails.

**C-42 -- Production-site provenance annotation** *(from R14 V-03)* | aspirational | correctness
A constraint is declared at the production step (the phase where the artifact is written) with an explicit cross-reference to the site where that artifact is excluded or superseded, closing the provenance loop. Pass: at least one constraint annotation present at production step with named cross-reference to its exclusion site. Constraints stated only at the exclusion site without back-annotation at production fail.

**C-43 -- Pre-phase persona registry block** *(from R15 V-01)* | aspirational | correctness
All assigned personas are declared in a dedicated registry section before Phase 1 begins. Each registry entry names the persona, its ownership domain, and its enumerated prohibition list. Pass: registry block present before Phase 1; each persona entry includes ownership domain and at least one named prohibition; prohibition lists are not deferred into phase sections. Personas introduced inline within phase sections, or prohibition lists buried inside phase bodies, fail.

**C-44 -- Six-component Phase 4 story artifact** *(from R15 V-01)* | aspirational | depth
Phase 4's output contract extends the C-05 minimum of four components to six by explicitly typing coverage ratio and session delta as required fields with format constraints. Pass: Phase 4 output specification names at least six components; coverage ratio declared as a typed numeric field; session delta declared as a typed field with a named fallback value for first-run invocation (e.g. `DELTA: FIRST RUN`). A Phase 4 that stops at four components or treats ratio/delta as optional narrative fails.

**C-45 -- Inline role-closure statement at phase boundary** *(from R15 V-01)* | aspirational | behavior
At the boundary where one role's phase ends, a single inline closure statement explicitly terminates that role's authority before the next role activates. Pass: at least one phase boundary carries a one-sentence closure statement of the form "[ROLE] closes at artifact write. [ROLE] does not carry work into Phase N+1." or equivalent. Scope boundaries implied only by section numbering or role labels, without an explicit closure sentence, fail.
