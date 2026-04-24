# Campaign-Decide R7 Scorecard — Rubric v7

## Scoring Model

| Band | Criteria | Pts Each | Max |
|------|----------|----------|-----|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-24 (/16) | 0.625 | 10 |
| **Composite** | | | **100** |

C-17 (v7): 6 slots satisfies the criterion when C-21 is in effect.
C-23: column-header schema required for **every** phase (no `| Field | Value |` two-column layouts).
C-24: Because block must carry separate `Phase 1a` and `Phase 1b` slots when C-21 sub-phase split is in effect.

---

## V-01 R7 — V-02 R6 base + 6-slot Because split

**Axis**: C-24 only. V-02 R6 already passes C-23; this variant adds the sub-phase synthesis alignment.

| ID | Result | Evidence Note |
|----|--------|---------------|
| C-01 | PASS | Explicit labeled build/no-build recommendation present |
| C-02 | PASS | Confidence level stated alongside recommendation |
| C-03 | PASS | All six domains (competitors, feasibility, market, hypothesis, web-search, synthesis) represented |
| C-04 | PASS | Inertia/status-quo cost leads competitor section before named rivals |
| C-05 | PASS | Recommendation grounded in per-phase citations |
| C-06 | PASS | Titled sections, summary block, recommendation block present |
| C-07 | PASS | Counter-evidence and risks surfaced |
| C-08 | PASS | Each hypothesis carries explicit confirmed/refuted/inconclusive disposition |
| C-09–C-22 | PASS (all 14) | Inherited from V-02 R6 base; all passed under v6 |
| C-23 | **PASS** | Column headers enumerate required fields per phase (inherited from V-02 R6); no `\| Field \| Value \|` layouts |
| C-24 | **PASS** | Because block split into 6 slots: `Phase 1a (Inertia)`, `Phase 1b (Rivals)`, `Phase 2`, `Phase 3`, `Phase 4`, `Phase 5`; mirrors C-21 structure |
| C-17 (v7) | PASS | 6 slots with C-21 in effect satisfies v7 updated condition |

**Aspirational**: 16/16 → 10.0 pts
**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 10.0
**Composite: 100.0**

---

## V-02 R7 — V-03 R6 base + strict domain-specific column headers all phases

**Axis**: Strict C-23 elimination. V-03 R6 already passes C-24; this variant redesigns all phase tables with domain-specific column headers.

| ID | Result | Evidence Note |
|----|--------|---------------|
| C-01 | PASS | Explicit recommendation present |
| C-02 | PASS | Confidence level stated |
| C-03 | PASS | All six domains represented |
| C-04 | PASS | Inertia-first competitor framing |
| C-05 | PASS | Evidence-to-recommendation traceability via per-phase citations |
| C-06 | PASS | Structured document with titled sections |
| C-07 | PASS | Risks and counter-evidence present |
| C-08 | PASS | Hypothesis dispositions explicit |
| C-09–C-22 | PASS (all 14) | Inherited from V-03 R6 base |
| C-23 | **PASS** | All phases redesigned with domain-specific column headers (e.g., `\| Competitor \| Inertia Force \| Switching Cost \|`); no `\| Field \| Value \|` anywhere |
| C-24 | **PASS** | V-03 R6 base already provides `Phase 1a` / `Phase 1b` Because slots |
| C-17 (v7) | PASS | 6 slots with C-21 in effect; v7 accepts this count |

**Aspirational**: 16/16 → 10.0 pts
**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 10.0
**Composite: 100.0**

---

## V-03 R7 — V-01 R6 base + Phase 5 column tables only (boundary test)

**Axis**: Documents whether C-23 allows partial column adoption. Phases 0–4 remain inline; Phase 5 gets named-column sub-tables.

| ID | Result | Evidence Note |
|----|--------|---------------|
| C-01 | PASS | Recommendation present |
| C-02 | PASS | Confidence stated |
| C-03 | PASS | All six domains covered |
| C-04 | PASS | Inertia-first ordering |
| C-05 | PASS | Traceability present |
| C-06 | PASS | Structured format |
| C-07 | PASS | Risks acknowledged |
| C-08 | PASS | Hypothesis dispositions explicit |
| C-09–C-22 | PASS (all 14) | Inherited from V-01 R6 base |
| C-23 | **FAIL** | C-23 requires column-header schema on **each** phase. Phases 0–4 retain inline `\| Field \| Value \|` layouts. Phase 5 alone does not satisfy the "each phase" absolute condition. No partial credit. |
| C-24 | **FAIL** | V-01 R6 base retains single `Phase 1` Because slot; no 1a/1b synthesis split |
| C-17 (v7) | PASS | 5 slots; C-24 not claimed; liberal v7 reading accepts legacy 5-slot |

**Aspirational**: 14/16 → 8.75 pts
**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 8.75
**Composite: 98.8**

---

## V-04 R7 — V-02 R7 base + Phase 4 "Source Context" column (production-ready)

**Axis**: Combined C-23 + C-24 + Phase 4 quote-fidelity fix. Addresses the quote-compression risk flagged since R6 by adding a dedicated `Source Context` column to Phase 4.

| ID | Result | Evidence Note |
|----|--------|---------------|
| C-01 | PASS | Recommendation present |
| C-02 | PASS | Confidence stated |
| C-03 | PASS | All six domains represented |
| C-04 | PASS | Inertia-first competitor framing |
| C-05 | PASS | Per-phase citations with templated syntax |
| C-06 | PASS | Structured document format |
| C-07 | PASS | Risks and counter-evidence surfaced |
| C-08 | PASS | All hypothesis dispositions explicit |
| C-09–C-22 | PASS (all 14) | Inherited; no regressions introduced by Phase 4 enhancement |
| C-23 | **PASS** | Domain-specific column headers on all phases (from V-02 R7 base); Phase 4 `Source Context` column strengthens rather than weakens schema enforcement |
| C-24 | **PASS** | V-03 R6 base supplies 6-slot Because alignment (via V-02 R7 lineage) |
| C-17 (v7) | PASS | 6 slots with C-21 in effect |
| C-12 (bonus note) | PASS | Phase 4 `Source Context` column directly supports mechanically auditable citation traceability — zero interpretation ambiguity at quote boundary |

**Aspirational**: 16/16 → 10.0 pts
**Essential**: 60 | **Recommended**: 30 | **Aspirational**: 10.0
**Composite: 100.0** ← most robust; no ambiguity edge cases

---

## V-05 R7 — V-05 R6 base + tables + 6-slot + preamble (conversational)

**Axis**: Conversational style upgraded with table-format evidence blocks and 6-slot synthesis. Preamble explains the structural reasoning for the 6-slot split. C-23 scores differently under liberal vs. strict interpretation.

| ID | Result | Evidence Note |
|----|--------|---------------|
| C-01 | PASS | Recommendation present |
| C-02 | PASS | Confidence stated |
| C-03 | PASS | All six domains covered |
| C-04 | PASS | Inertia-first ordering maintained |
| C-05 | PASS | Traceability present |
| C-06 | PASS | Structured format with conversational transitions |
| C-07 | PASS | Risks acknowledged; conversational preamble adds interpretive framing |
| C-08 | PASS | Hypothesis dispositions explicit |
| C-09–C-22 | PASS (all 14) | Inherited from V-05 R6 base |
| C-23 | **PASS (liberal)** / **FAIL (strict)** | Tables replace inline rows. Liberal: table presence satisfies column-header intent. Strict: conversational style retains some `\| Field \| Value \|` two-column layouts at phase-summary level; schema is not domain-specific throughout |
| C-24 | **PASS** | 6-slot synthesis present; preamble explicitly labels why 1a/1b split exists — C-24's most defensible form |
| C-17 (v7) | PASS | 6 slots with C-21 in effect |

**Aspirational (liberal)**: 16/16 → 10.0 pts → **Composite: 100.0**
**Aspirational (strict)**: 15/16 → 9.375 pts → **Composite: 99.4**

---

## Rankings

| Rank | Variant | Composite | Notes |
|------|---------|-----------|-------|
| **1** | **V-04** | **100.0** | Production-ready; all 16 aspirational pass; Phase 4 quote-fidelity fix eliminates last known fragility |
| **1** | **V-01** | **100.0** | Minimal convergence proof; C-24 is a small delta on a C-23-passing base |
| **1** | **V-02** | **100.0** | Strictest C-23 pass; domain-specific columns eliminate all scoring ambiguity |
| **4** | **V-05** | **100.0 / 99.4** | Conversational path; score boundary depends on C-23 interpretation strictness |
| **5** | **V-03** | **98.8** | Boundary test; documents "each phase" is absolute for C-23 — no partial credit |

---

## Excellence Signals

**From V-01** — *Minimal convergence:* Once C-23 is in place, achieving C-24 requires only one structural change: splitting the Because block from 5 to 6 named slots. The prerequisite chain (C-21 → C-17 v7 → C-24) means the Because split is never freestanding — it must mirror evidence structure already present.

**From V-02** — *Domain-specific schema eliminates ambiguity:* Column headers that name the domain fields (`Competitor | Inertia Force | Switching Cost`) are structurally unambiguous. The schema violation is visible without reading any cell content — exactly what C-23 demands. Generic `Field | Value` headers fail by design.

**From V-03** — *Boundary confirmation:* Partial column adoption earns zero C-23 credit. The criterion is all-or-nothing across phases. This is a permanent reference result: any future variant with mixed inline/column coverage for phases will score 98.8, not 99.x.

**From V-04** — *Phase 4 quote-fidelity fix is load-bearing for production use:* The `Source Context` column in Phase 4 resolves the quote-compression risk that has been latent since R6. A template that hits 100.0 under current rubric but carries a known fragility is not production-ready; V-04 closes that gap.

**From V-05** — *Preamble as C-24 reinforcement:* Explaining in prose *why* 6 slots exist (because Phase 1 has inertia and rival sub-phases) is the strongest form of C-24 compliance — it makes the structural alignment explicit and auditable even for human reviewers unfamiliar with v7 rubric history.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Minimal convergence: one Because-block split (5→6 slots) achieves 100.0 on a C-23-passing base — C-24 is a small delta once the column-schema prerequisite is met", "Strict C-23 requires domain-specific column headers per phase (not Field|Value layouts) — schema violation must be structurally visible without reading cell content", "C-23 is each-phase absolute: partial column adoption (one phase with columns, others inline) earns zero credit — no partial scoring at phase boundary", "Phase 4 Source Context column closes the quote-compression fragility latent since R6 — production-ready template addresses known future rubric risk proactively", "Preamble explaining WHY 6 synthesis slots exist is the strongest C-24 form — makes sub-phase alignment explicit and auditable without rubric context"]}
```
