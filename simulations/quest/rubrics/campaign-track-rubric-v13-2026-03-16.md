Looking at the R13 scorecard, I extract two new excellence patterns:

- **C-38**: Ambiguity failure mode framing at Phase Boundary Summary (two+ structurally distinct sites; stale-value alone fails) — origin R12 V-05 extended evidence
- **C-39**: Receiving scope addressed as independent structural site with named independence claim distinguishing it from cascading scope — origin R12 V-05 extended evidence

Aspirational count goes from 26 to 28; max from 143 to 149.

---

# Quest Rubric — campaign-track — v13

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

**C-38 -- Phase Boundary Summary ambiguity failure mode** *(from R12 V-05)* | aspirational | depth
Phase 4 obligation consequence framing appears at the Phase Boundary Summary as an ambiguity failure mode: downstream systems cannot distinguish an interrupted campaign from a completed one because both states produce the same `verdict_after` placeholder. Pass: ambiguity failure mode framing present at two or more structurally distinct sites (e.g., Phase 4 obligation header and Phase Boundary Summary), each with a distinct framing dimension. Stale-value framing at a single site alone does not satisfy; absence of the "cannot distinguish interrupted from completed" formulation does not satisfy.

**C-39 -- Receiving scope as independent structural site** *(from R12 V-05)* | aspirational | correctness
Phase Boundary Summary addresses receiving scope — what Phase 4 does NOT receive as inputs — independently of cascading scope — what a Phase 3 Step B re-run does NOT update. Pass: two orthogonal structural sites present, each addressing a distinct scope dimension; an explicit independence claim names both scope types and asserts their orthogonality (e.g., "the two arguments address the same boundary from orthogonal directions"). A single prose argument without named scope types or an explicit independence assertion fails; receiving scope mentioned only in passing at the Phase 4 active-role header without a dedicated structural treatment fails.

---

## Scoring Summary

| Category | Per-criterion | Criteria count | Max pts |
|----------|--------------|---------------|---------|
| Essential | 10 | 5 (C-01–C-05) | 50 |
| Recommended | 5 | 3 (C-06–C-08) | 15 |
| Aspirational | 3 | 28 (C-09–C-39) | 84 |
| **Max** | | **36** | **149** |
