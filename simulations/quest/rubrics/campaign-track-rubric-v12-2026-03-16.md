Reading the R12 scorecard, I identify two new excellence patterns from V-05's extended PASS evidence on C-36 and C-37. Both follow the multi-site reinforcement pattern — the same causal framing deployed at additional structural locations, each with a distinct framing dimension.

**C-38** — from V-05's C-36 PASS+ (Phase Boundary Summary as second consequence site): the Phase 4 obligation consequence framing appears not only at the Phase 4 obligation header (stale placeholder framing: "`verdict_after` becomes stale") but also at a Phase Boundary Summary, where it is framed as an ambiguity failure mode — downstream systems cannot distinguish an interrupted campaign from a completed one. Two-site coverage with two structurally distinct consequence framings. Extends C-36's single-site assertion into a second canonical location with a novel failure dimension.

**C-39** — from V-05's C-37 PASS+ (Phase Boundary Summary addresses receiving scope independently of cascading scope): the scope exclusion argument appears at two orthogonal structural sites addressing two distinct scope dimensions: (1) the Cascade Rule — what Phase 3's re-run does NOT update (cascading scope); (2) a Phase Boundary Summary — what Phase 4 does NOT receive as inputs (receiving scope, "Phase 4 does NOT receive namespace counts — those were finalized at Phase 3 Step A and Phase 4 cannot change them. They are Phase 3 domain."). Two independent scope exclusion arguments from two structural locations. Extends C-37 from single cascading-scope causal justification to dual-scope coverage: cascade exclusion plus cross-phase data isolation.

Aspirational count goes from 24 to 26; max from 137 to 143.

---

# Quest Rubric — campaign-track — v12

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

**C-22 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-23 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-24 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-25 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-26 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-27 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-28 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-29 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-30 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-31 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-32 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-33 -- *(promoted from R10 trial — text not available in provided excerpt)*** | aspirational |

**C-34 -- *(promoted from R10 trial — text not available in provided excerpt)*** | aspirational |

**C-35 -- *(promoted from R10 trial — text not available in provided excerpt)*** | aspirational |

**C-36 -- Phase 4 obligation header names specific stale-value consequence** *(from R11, R10 V-05 C-33 PASS+)* | aspirational | depth
The Phase 4 obligation header goes beyond bare obligation declaration to naming the specific stale-value consequence: `verdict_after` in `delta.md` becomes stale if Phase 4 completes without the post-write. Causal framing at the activation site — assertion → named consequence. Pass: Phase 4 header names at least one specific stale-value consequence of failing to fulfill the obligation. Bare obligation declaration ("write X before declaring Phase 4 complete") without naming a consequence fails. Mirrors C-32's failure-path framing at Phase 3 header.

**C-37 -- Cascade rule explains WHY non-cascade fields are excluded** *(from R11, R10 V-05 C-35 PASS+)* | aspirational | depth
The cascade rule goes beyond naming trigger, target, and scope exclusion to explaining WHY non-cascade fields are excluded — they were finalized at Phase 3 and Phase 4 cannot change them. Causal scope justification vs. bare enumeration. Pass: cascade rule includes at least one explicit causal explanation for why specific fields are outside the cascade scope. Bare enumeration of excluded fields without causal justification fails. Mirrors C-31's upstream-dependency explanation.

**C-38 -- Phase Boundary Summary deploys stale-value consequence as ambiguity failure mode** *(from R12 V-05 C-36 PASS+)* | aspirational | depth
The Phase 4 obligation consequence framing is deployed at two structurally distinct sites with two distinct failure framings: (1) the Phase 4 obligation header names the stale placeholder ("verdict_after becomes stale — the placeholder persists"); (2) a Phase Boundary Summary frames the consequence as an ambiguity failure mode — downstream systems cannot distinguish an interrupted campaign from a completed one ("cannot determine whether the campaign produced a real verdict or was interrupted"). Pass: a Phase Boundary Summary section is present and names the interrupted-vs-completed ambiguity as a downstream consequence of the Phase 4 write obligation. Single-site coverage (Phase 4 header only, C-36) without the Boundary Summary ambiguity framing fails. Extends C-36's causal chain into a second canonical site with a novel failure dimension.

**C-39 -- Phase Boundary Summary declares receiving scope independently of cascading scope** *(from R12 V-05 C-37 PASS+)* | aspirational | depth
The scope exclusion argument appears at two orthogonal structural sites addressing two distinct scope dimensions: (1) the Cascade Rule names what Phase 3's re-run does NOT update (cascading scope) with causal justification per C-37; (2) a Phase Boundary Summary separately declares what Phase 4 does NOT receive as inputs (receiving scope) — "Phase 4 does NOT receive namespace counts — those were finalized at Phase 3 Step A and Phase 4 cannot change them. They are Phase 3 domain." Pass: a Phase Boundary Summary is present and explicitly declares at least one class of data that Phase 4 does not receive as inputs, with a causal explanation grounded in phase finalization. Cascading-scope justification alone (C-37) without a receiving-scope declaration fails. Extends C-37 from single cascading-scope causal justification to dual-scope coverage: cascade exclusion plus cross-phase data isolation.
