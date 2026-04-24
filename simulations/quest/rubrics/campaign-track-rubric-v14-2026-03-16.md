Looking at the scorecard, I extract three new excellence patterns:

- **C-40**: Triptych temporal-axis independence labels auditable at header level (header text carries qualifier, not body-only) — origin R14 V-01/V-04/V-05
- **C-41**: Bidirectional Phase Boundary Summary back-reference at four surfaces (obligation block, active-role header, Narrator prohibition, TERMINAL gate) — origin R14 V-02/V-04/V-05
- **C-42**: Production-site provenance annotation — constraint declared at the production step (Phase 3 Step A) with cross-reference to its exclusion site, closing the provenance loop — origin R14 V-03

Aspirational count goes from 28 to 31; max from 149 to 158.

---

# Quest Rubric — campaign-track — v14

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

**C-22–C-37 -- *(from prior versions — text not available in provided excerpt)*** | aspirational |

**C-38 -- Ambiguity failure mode framing at Phase Boundary Summary** *(from R12 V-05)* | aspirational | correctness
Phase Boundary Summary names at least two structurally distinct failure sites and frames the ambiguity failure mode at the phase boundary explicitly. Pass: two or more named failure sites present; stale-value alone is not treated as the sole failure mode; structural distinction between sites is stated. A boundary summary that collapses all failure modes to a single stale-value description fails.

**C-39 -- Receiving scope as independent structural site** *(from R12 V-05)* | aspirational | correctness
The Phase Boundary Summary treats receiving scope as an independent structural site with a named independence claim that distinguishes it from cascading scope. Pass: receiving scope addressed as its own labeled site; independence claim present by name; the distinction from cascade is stated. A summary that subsumes receiving scope under cascading scope or omits the independence claim fails.

**C-40 -- Triptych temporal-axis independence labels auditable at header level** *(from R14 V-01)* | aspirational | format
Each scope-type subsection in the Phase Boundary Summary carries its temporal-axis qualifier in the `####` header text itself (e.g., `#### Cascade Scope (re-run concern)`, `#### Receiving Scope (entry concern)`, `#### Exit Scope (exit concern)`). Pass: all three triptych headers contain temporal labels; a reader scanning the document outline without reading body text can identify the complete temporal taxonomy. Labels present only in body openers or prose sentences, with headers containing bare scope names, fail.

**C-41 -- Bidirectional Phase Boundary Summary back-reference at four surfaces** *(from R14 V-02)* | aspirational | correctness
The Phase Boundary Summary obligation appears as an explicit cross-reference at all four enforcement surfaces: (1) the obligation block declaration, (2) the active-role header, (3) at least one Narrator prohibition entry naming the obligation by path, and (4) the TERMINAL story.md existence gate naming the obligation by path. Pass: all four surfaces present with cited path references (e.g., "Phase Boundary Summary, Phase 3->4"). Two-surface baseline (obligation block + active-role header only) fails.

**C-42 -- Production-site provenance annotation** *(from R14 V-03)* | aspirational | correctness
The finalization boundary constraint is declared at the production site (Phase 3 Step A or equivalent signal-collection step) with an explicit cross-reference to its exclusion site in the Phase Boundary Summary. Pass: annotation present at the production step stating that the value is finalized there and must not be propagated to Phase 4, with a named cross-reference to the Receiving Scope exclusion site (e.g., "do not propagate to Phase 4 — see Receiving Scope (Phase Boundary Summary, Phase 3->4)"); provenance loop is closed. Declaring the constraint only at the exclusion site without annotating the production step fails.
