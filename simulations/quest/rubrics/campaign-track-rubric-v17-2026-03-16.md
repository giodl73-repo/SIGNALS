Looking at the scorecard, I can extract two fully-described excellence signals (C-50, C-51) and one declared-but-not-excerpted signal (C-52), then promote all three into v17.

Key extraction notes:
- **C-50**: Bidirectional Prohibition Map Rule — receipt_surface field makes prohibition registry bidirectional; V-01/V-04/V-05 pass
- **C-51**: Coverage Quality Tier Column — quality column (REAL|MOCK|INFERRED) + Quality-Aware Readiness Rule; V-02 axis
- **C-52**: Declared as candidate but body not present in excerpt → placeholder

---

```markdown
# Quest Rubric — campaign-track — v17

Three new aspirational criteria (C-50, C-51, C-52) extracted from R18 excellence signals. Aspirational count: 37 → 40. Max score: 176 → 185.

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

**C-41 through C-45, C-47 -- *(from prior versions — text not available in provided excerpt)*** | aspirational |

**C-46 -- Typed 3-field prohibition anchoring** *(from R17 V-02/V-03)* | aspirational | correctness
Each prohibition entry carries exactly three typed fields: action, governed_by, violation_class. Pass: all prohibition entries in all roles carry all three named fields with non-empty values. Entries with fewer fields or untyped narrative prohibitions fail.

**C-48 -- Full registry-component field alignment** *(from R17)* | aspirational | format
Every structured registry (persona registry, prohibition registry, Cross-Phase Obligation Index) declares a complete, consistent field schema that is honored by every row without omission. Pass: schema declared per registry; every row carries every declared field; no sparse rows. Registries with undeclared or partially populated fields fail.

**C-49 -- Phase Entry Receipt Rule (six fixed audit locations)** *(from R17)* | aspirational | behavior
Each of Phases 2, 3, and 4 opens with an Entry Receipt acknowledging the artifact received from the prior phase; each of Phases 1, 2, and 3 closes with an Exit Closure confirming the artifact handed forward. Pass: exactly three entry receipts (Phases 2, 3, 4) and exactly three exit closures (Phases 1, 2, 3) present as named, auditable elements — six fixed audit locations in total. Implicit handoffs or receipt language buried in body prose fail.

**C-50 -- Bidirectional Prohibition Map Rule** *(from R18 V-01/V-04/V-05)* | aspirational | correctness
Each typed prohibition entry in the prohibition registry carries a `receipt_surface` field naming the exact Phase Entry Receipt that acknowledges the boundary from the receiving side, transforming the registry from a one-directional constraint list into a bidirectional boundary map. Pass: all prohibition entries (across all roles) carry `receipt_surface` typed as `Phase [N] entry receipt ([ROLE] received [artifact] from Phase [N-1])`; Prohibition Parity Rule declares 4 fields (action + governed_by + violation_class + receipt_surface); Cross-Phase Obligation Index carries a `receipt_surface` row; terminal section contains an item confirming all prohibition entries carry receipt_surface. Prohibition registries with fewer than 4 fields per entry, or without receipt_surface, fail.

**C-51 -- Coverage Quality Tier Column** *(from R18 V-02)* | aspirational | depth
Phase 3 coverage table includes a `quality` column typed as one of the enumerated set `REAL | MOCK | INFERRED`, applied per namespace row. A Quality-Aware Readiness Rule governs the readiness_verdict derivation from quality composition (e.g. a table heavy in MOCK signals constrains the verdict). A `quality_distribution` summary field propagates read-only from Phase 3 into Phase 4 Component 5. Pass: quality column present in all nine namespace rows with values drawn from the enumerated set; Quality-Aware Readiness Rule declared and linked to readiness_verdict; quality_distribution present in Phase 4 output. Coverage tables without a quality column, or verdicts that ignore quality composition, fail.

**C-52 -- *(from R18 — text not available in provided excerpt)*** | aspirational |
```

---

Three criteria promoted: **C-50** (Bidirectional Prohibition Map Rule — correctness axis, receipt_surface as 4th prohibition field), **C-51** (Coverage Quality Tier Column — depth axis, REAL|MOCK|INFERRED per namespace row), **C-52** (declared candidate, body not in excerpt — placeholder pending next round). Aspirational count 37 → 40, max score 176 → 185.
