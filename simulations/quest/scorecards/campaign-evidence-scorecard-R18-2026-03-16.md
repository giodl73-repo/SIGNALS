## Quest Scorecard — campaign-evidence (Round 18)

**Rubric**: v18 | **Date**: 2026-03-17 | **Denominator**: 44 defined criteria (C-01–C-44)

---

### Baseline Assessment (C-01 through C-42)

All five variations carry the full R17 baseline. Spot-checks confirm:

| Block | Criteria | All Variations |
|-------|----------|----------------|
| Essential | C-01–C-04 | PASS — 5-stage campaign, evidence-first, falsifiable hypotheses, self-contained output |
| Recommended | C-05–C-07 | PASS — stage attribution, consensus/conflict synthesis, calibrated confidence |
| Aspirational core | C-08–C-42 | PASS — gaps, decision readiness, named rules, prospective immutable map, inline scope, universal binary, stage-indexed, entry/exit gates, gate record, audit table, checksum, provenance, dual-phase PRE/POST, named table artifacts, preamble apparatus, interrogative headers, rule-named headers, SEQUENCING-ORDER scope, SEQUENCING decomposed to HYPO+ORDER peer rules |

**C-01–C-42: PASS for all five variations.**

---

### New Criteria Assessment

#### C-43 — SEQUENCING-ORDER invocations name live ordering decisions explicitly

| Variation | Result | Evidence |
|-----------|--------|----------|
| **V-01** | **PASS** | Intel-first. PRE-S1 cell: `[Yes/No] -- Intel-first ordered as governed decision`. POST-S1: `Intel-first governed decision executed at S1`. PRE-S2: `S2 Web follows Intel-first governed order declared at S1`. Decision name appears at every applicable boundary. |
| **V-02** | **FAIL** | Web-first default. SEQUENCING-ORDER cells contain `no unordered collection; Web-first declared` — names the ordering but not a live non-default decision. C-43 pass condition requires the rule govern an actual non-default structural choice; confirming a default provides invocation coverage, not governance substance. |
| **V-03** | **FAIL** | Plain `[Yes/No]` cells throughout. No ordering decision named anywhere in invocations. |
| **V-04** | **PASS** | Intel-first. Cells fuse decision name and antipattern guard: `Intel-first ordered as governed decision; no unordered collection`. Decision name present at all four SEQUENCING-ORDER applicable boundaries (S1 PRE+POST, S2 PRE+POST). |
| **V-05** | **PASS** | Intel-first. Same decision-name pattern as V-04. S2 exit condition explicitly requires `Intel-first ordering confirmed in POST cell`. Inertia Baseline table defines SEQUENCING-ORDER's antipattern as "Unordered collection," grounding the decision name against a named failure mode. |

#### C-44 — Binary invocation cells annotated with antipattern-absence guards

| Variation | Result | Evidence |
|-----------|--------|----------|
| **V-01** | **FAIL** | SEQUENCING-ORDER cells carry the governed-decision annotation but not an antipattern-absence guard (says "Intel-first ordered as governed decision," not "no unordered collection"). All other cells (ATTRIBUTION, SEQUENCING-HYPO, CALIBRATION, FALSIFICATION, PROVENANCE) are plain `[Yes/No]` — no antipattern annotation. C-44 requires every cell to name the specific failure mode it guards against. |
| **V-02** | **PASS** | All binary cells annotated. PRE: `[Yes/No] -- no attribution collapse`, `[Yes/No] -- no hypothesis-first mode`, `[Yes/No] -- no unordered collection; Web-first declared`, `[Yes/No] -- no uniform confidence; 2+ distinct levels required`, `[Yes/No] -- no unfalsifiable hypotheses`, `[Yes/No] -- no unconstrained synthesis`. POST cells use absence-verification form: `attribution-collapse antipattern absent?`. Universal coverage across all six rules at all applicable stages. |
| **V-03** | **FAIL** | Plain `[Yes/No]` cells throughout preamble templates. No antipattern annotations. Inertia Baseline table exists but its vocabulary does not flow into the invocation cells. |
| **V-04** | **PASS** | All binary cells annotated with specific antipattern guards. SEQUENCING-ORDER cells fuse both signals: `Intel-first ordered as governed decision; no unordered collection`. Full coverage across all six rules. |
| **V-05** | **PASS** | All binary cells annotated. Crucially, N/A declarations also name excluded antipatterns: `CALIBRATION -- N/A (evidence stage; uniform-confidence antipattern not applicable)` vs V-01–V-04 which use bare `CALIBRATION -- N/A (evidence stage)`. |

#### Beyond-Rubric Signals (C-45 and C-46 — not yet in denominator)

**C-45 — Inertia Baseline table as preamble fixture mapping antipatterns to rules:**
- V-03: **PASS** — full table with antipattern → governing rule → detection point → consequence
- V-05: **PASS** — same table, with added connection: "The invocation cells at each stage guard against the antipattern named here"
- V-01, V-02, V-04: **FAIL** — no Inertia Baseline table

**C-46 — Checksum extensibility narrative embedding the proof as readable context:**
- V-05: **PASS** — full narrative: "The denominator is 47, not 40. The difference of 7 artifacts reflects SEQUENCING-ORDER's independent row... When SEQUENCING was decomposed... 7 new artifacts absorbed automatically without updating any static integer. This is the C-29 extensibility property in live action."
- V-01, V-02, V-03, V-04: **PARTIAL** — checksum section states "Derived from map dimensions; updates automatically when rules or stages are added" but does not reconstruct the architectural history or demonstrate why 47, not 40.

---

### Per-Variation Composite Scores

**Scoring basis:** 44 defined criteria (C-01–C-44); PASS = 1pt, PARTIAL = 0.5pt, FAIL = 0pt; score = (pts / 44) × 100.

| Variation | C-01–C-42 | C-43 | C-44 | Raw Pts | Score |
|-----------|:---------:|:----:|:----:|:-------:|:-----:|
| V-01 | 42 PASS | PASS | FAIL | 43.0 | 97.7 |
| V-02 | 42 PASS | FAIL | PASS | 43.0 | 97.7 |
| V-03 | 42 PASS | FAIL | FAIL | 42.0 | 95.5 |
| V-04 | 42 PASS | PASS | PASS | 44.0 | **100** |
| V-05 | 42 PASS | PASS | PASS | 44.0 | **100** |

*V-05 exceeds the rubric denominator by also passing C-45 (PASS) and C-46 (PASS), and introducing a third sub-signal in N/A declarations not yet captured by any criterion.*

**All essential criteria pass: YES** (C-01–C-04 PASS across all five variations).

---

### Ranking

1. **V-05** — 100 + C-45 PASS + C-46 PASS + N/A antipattern naming
2. **V-04** — 100 (C-43+C-44, no C-45/C-46)
3. **V-01** — 97.7 (C-43 only; decision name present but no antipattern annotations on non-SEQUENCING-ORDER cells)
4. **V-02** — 97.7 (C-44 only; Web-first default prevents C-43 from doing governance work)
5. **V-03** — 95.5 (C-45 only via Inertia Baseline, but plain cells fail both C-43 and C-44)

---

### Excellence Signals from V-05

**Why V-05 is better than V-04:**

1. **Vocabulary fixture → invocation vocabulary**: The Inertia Baseline table names the six failure modes once in the preamble; every binary cell annotation and audit table row draws from that vocabulary. The table is the source of truth; the cells are its invocations. This makes the antipattern column in the audit table derivable from the preamble, not scattered ad hoc.

2. **Extensibility proof as architectural narrative**: The checksum section does not just state "47 = 17×2 + 13×1"; it reconstructs why 47 not 40, names the prior monolithic SEQUENCING rule, explains the rule decomposition step, and shows how 7 artifacts were absorbed without static updates. A first-time reader encountering the prompt understands the design intent without prior context.

3. **Antipattern names in N/A declarations**: Non-applicable cells in V-05 explicitly name the excluded antipattern: `uniform-confidence antipattern not applicable`. This extends C-44's antipattern-grounding from positive invocations into the N/A tier — every cell, positive or negative, now names its guarded failure mode, making the full invocation apparatus homogeneous.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Vocabulary fixture: Inertia Baseline table as preamble section maps each failure mode to its governing rule, detection point, and consequence — binary cell annotations and audit table antipattern column draw vocabulary from this single source rather than embedding it ad hoc", "Extensibility narrative: checksum derivation section reconstructs the architectural history (40→47 shift from SEQUENCING decomposition) as readable prose, proving C-29 extensibility with a concrete example accessible to first-time readers without prior context", "Antipattern-named N/A declarations: non-applicable stage/rule cells explicitly name the excluded antipattern (uniform-confidence antipattern not applicable here) rather than bare stage-type descriptions, making inapplicability as informationally grounded as positive invocations"]}
```
