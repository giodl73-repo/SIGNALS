```markdown
# Quest Rubric — campaign-track — v16

Three new aspirational criteria (C-46, C-48, C-49) extracted from R17 excellence signals. Aspirational count: 34 → 37. Max score: 167 → 176.

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
Phase Boundary Summary carries four named assertion surfaces: Cascade Scope, Receiving Scope, Transition Obligation, and Post-Phase-4-to-Dashboard boundary. Pass: all four surfaces present and labeled. Summaries covering three or fewer surfaces fail.

**C-42 -- *(from prior version — text not available in provided excerpt)*** | aspirational |

**C-43 -- PERSONA REGISTRY as governing authority** *(from R15 ES-1)* | aspirational | correctness
A PERSONA REGISTRY section is declared as the single authority for role identity, ownership, and prohibitions. Phase headers cite the registry rather than restate it. Pass: registry declared as authoritative; phase headers reference it by name; role definitions not duplicated inline in phase bodies. A registry present only as a convenience summary with role definitions restated per phase fails.

**C-44 -- Six-component Phase 4 contract** *(from R15 ES-2)* | aspirational | format
Phase 4 output contract enumerates exactly six named components with typed constraints. Receiving Scope in the Phase 3→4 Boundary Summary pins components 5 and 6 as read-only inputs. Pass: six components declared with individual type or value constraints; read-only annotation on components 5 and 6 present in Receiving Scope. Fewer components or missing read-only constraint fail.

**C-45 -- Closure Parity Rule at three exits** *(from R15 ES-3)* | aspirational | behavior
A Closure Parity Rule governing section declares three symmetrical closure statements — one at each of the Phase 1, 2, and 3 exits — in the form: "[ROLE] closes at [artifact] write. [ROLE] does not carry work into Phase [N+1]." Pass: rule declared as a governing section; three closure statements present, one per exiting role; no exiting role omitted. A rule with fewer than three instances or stated only in prose without governing-section status fails.

**C-46 -- Typed prohibition anchoring** *(from R17 V-01/V-04/V-05)* | aspirational | correctness
Each prohibition entry uses a typed three-field format: `action:` + `governed_by:` + `violation_class:`. A Prohibition Type Vocabulary section declares a controlled set of `violation_class` tokens. Pass: typed three-field format present for all prohibition entries across all roles; Prohibition Type Vocabulary section present with a named controlled token set; `violation_class` field enables category-scan without reading prohibition bodies. Inline parenthetical citations or narrative prohibition descriptions without field typing fail.

**C-47 -- *(reserved)*** | aspirational |

**C-48 -- Full registry-component field alignment** *(from R17 V-02/V-05)* | aspirational | correctness
All four role entries in the PERSONA REGISTRY include field-level type annotations that map directly to the role's output artifact or contract fields. Pass: REGISTRAR domain lists Phase 1 input fields with types; PLANNER domain lists namespace coverage contract fields; ANALYST domain lists all Phase 3 and Session Delta Contract fields with types; NARRATOR domain lists all six Phase 4 components with read-only annotations where applicable. Functional-label role descriptions without per-field type mapping fail.

**C-49 -- Phase entry receipt rule** *(from R17 V-03/V-04/V-05)* | aspirational | behavior
An Entry Receipt Rule section, parallel in authority to the Closure Parity Rule, declares receipt statements at Phase 2, 3, and 4 entries in the form: "RECEIPT: [ROLE] received [artifact] from Phase [N] per Phase Boundary Summary, Phase [N]->[N+1]." Phase 1 is explicitly excluded with a stated justification. The Cross-Phase Obligation Index carries three additional receipt rows for a total of 16. Pass: Entry Receipt Rule section present as a governing section; three receipt statements at Phase 2, 3, and 4 entries; Phase 1 exclusion explicitly stated with reason; Cross-Phase Obligation Index reflects 16 rows. A Closure Parity Rule without a complementary Entry Receipt Rule fails.
```
