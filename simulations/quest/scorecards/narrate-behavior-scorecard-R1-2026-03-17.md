---

# narrate-behavior — Round 8 Scorecard

**Rubric**: narrate-behavior-rubric-v8 (28 criteria: 4 essential, 3 recommended, 21 aspirational)
**Variations**: V-36 through V-40 (base: V-35, R7 champion, predicted 80/80 under v8)
**Date**: 2026-03-17

---

## Pre-Scoring Note

V-35 was confirmed 80/80 under v7 and predicted 80/80 under v8 by implementing C-26/C-27/C-28 directly. All five R8 variations inherit V-35's structural core — the full disposition traceability chain, TRIAGE GATE, COVERAGE CITATION INDEX, BACK-ANNOTATE, dual-purpose EXIT GATE B-IDs, BOUNDARY REGISTRY, DISCOVERY PATHWAY AUDIT with unconditional ratio. The R8 goal is v9 excellence signal exploration, not v8 threshold reaching.

---

## Essential Criteria (40 pts)

| Criterion | V-36 | V-37 | V-38 | V-39 | V-40 |
|-----------|------|------|------|------|------|
| **C-01** Declared Execution Sequence | PASS | PASS | PASS | PASS | PASS |
| **C-02** Single Unified Report | PASS | PASS | PASS | PASS | PASS |
| **C-03** Findings Ranked by Blast Radius | PASS | PASS | PASS | PASS | PASS |
| **C-04** At Least One Spec Gap or Violation | PASS | PASS | PASS | PASS | PASS |
| **Essential subtotal** | **40/40** | **40/40** | **40/40** | **40/40** | **40/40** |

**C-01 evidence**: All variations declare sequence explicitly before any section. V-38/V-40 extend to `INERTIA SURFACE -> S1 -> ...`; C-01 checks simulation sections appear in declared order — INERTIA SURFACE is a pre-simulation compilation step (analogous to TRIAGE GATE), not a simulation section, so C-01 is satisfied.

**C-04 evidence**: REPORT REQUIRE across all variations mandates "1+ spec-gap or contract-violation with specific spec location." Multiple sub-skill sections drive FINDING TABLE population with typed rows.

---

## Recommended Criteria (30 pts)

| Criterion | V-36 | V-37 | V-38 | V-39 | V-40 |
|-----------|------|------|------|------|------|
| **C-05** Finding Schema: Source + Location + Impact | PASS | PASS | PASS | PASS | PASS |
| **C-06** Cross-Sub-Skill Coverage | PASS | PASS | PASS | PASS | PASS |
| **C-07** Remediation Guidance Present | PASS | PASS | PASS | PASS | PASS |
| **Recommended subtotal** | **30/30** | **30/30** | **30/30** | **30/30** | **30/30** |

**C-05**: Pre-committed FINDING TABLE schema carries Sub-Skill (source), Spec/Contract Location, and Impact as separate named columns across all variations. V-38/V-40 add A-NN column additively — all required columns preserved.

**C-07**: Remediation column present as distinct field in all pre-committed schemas, with "concrete action" requirement stated in column rules.

---

## Aspirational Criteria (cap 10 pts; threshold: any 11 of 21)

| Criterion | V-36 | V-37 | V-38 | V-39 | V-40 |
|-----------|------|------|------|------|------|
| **C-08** Severity Classification | PASS | PASS | PASS | PASS | PASS |
| **C-09** Empty Sub-Skill Disposition | PASS | PASS | PASS | PASS | PASS |
| **C-10** Pre-Committed Finding Table Schema | PASS | PASS | PASS | PASS | PASS |
| **C-11** Exit Gate Per Sub-Skill Section | PASS | PASS | PASS | PASS | PASS |
| **C-12** Report-Level Post-Conditions | PASS | PASS | PASS | PASS | PASS |
| **C-13** Downstream-Anchored Simulation | PASS | PASS | PASS | PASS | PASS |
| **C-14** Inertia-as-Spec-Gap Mapping | PASS | PASS | PASS | PASS | PASS |
| **C-15** Boundary Registry as Structural Artifact | PASS | PASS | PASS | PASS | PASS |
| **C-16** Inertia-Boundary Cross-Reference | PASS | PASS | PASS | PASS | PASS |
| **C-17** Severity/Blast-Radius Column Independence | PASS | PASS | PASS | PASS | PASS |
| **C-18** Boundary Registry Type Field | PASS | PASS | PASS | PASS | PASS |
| **C-19** Pre-Registry Inertia Discovery Pipeline | PASS | PASS | PASS | PASS | PASS |
| **C-20** Dual-Purpose B-IDs Exit Gate Field | PASS | PASS | PASS | PASS | PASS |
| **C-21** Back-Annotation of S1-S2 Findings | PASS | PASS | PASS | PASS | PASS |
| **C-22** Discovery Pathway Audit in REPORT | PASS | PASS | PASS | PASS | PASS |
| **C-23** Unconditional Discovery-Pathway-Ratio REQUIRE | PASS | PASS | PASS | PASS | PASS |
| **C-24** Exhaustive Inertia-Disposition Completeness | PASS | PASS | PASS | PASS | PASS |
| **C-25** Inertia-Disposition Coverage Score | PASS | PASS | PASS | PASS | PASS |
| **C-26** Covered-Disposition Spec-Citation Registry | PASS | PASS | PASS | PASS | PASS |
| **C-27** Investigation Triage Gate as Structural Artifact | PASS | PASS | PASS | PASS | PASS |
| **C-28** Full Disposition Traceability Chain | PASS | PASS | PASS | PASS | PASS |
| **Criteria passed** | 21/21 | 21/21 | 21/21 | 21/21 | 21/21 |
| **Aspirational subtotal** | **10/10** | **10/10** | **10/10** | **10/10** | **10/10** |

### Key C-28 analysis — per variation

C-28 requires DEFINITIONS to declare all four artifact targets and REPORT to enumerate per-artifact counts:

- **V-36/V-37**: Artifact routing declared in DEFINITIONS ("FINDING -> FINDING TABLE, COVERED -> COVERAGE CITATION INDEX, INVESTIGATION -> FINDING TABLE + TRIAGE GATE, NONE -> inline"). REPORT has CCI table and TRIAGE GATE table (counts derivable) plus REQUIRE checks for both. INVESTIGATION dual-routing explicitly declared. PASS.
- **V-38/V-40**: ASSUMPTION CATALOG RECONCILIATION in REPORT makes per-artifact counts explicit: final catalog total, sum of A-NNs-assigned, unassigned count. Strengthens C-28 beyond DEFINITIONS-only declaration. PASS (stronger than V-36/V-37).
- **V-39/V-40**: ASSUMPTION CONSERVATION section in REPORT gives explicit N_inertia_rows + N_covered + N_none = N_total with residual check. Per-artifact row counts are enumerated numerically. Strongest C-28 realization. PASS.

### Key C-20 analysis — condensed phrasing (V-37)

V-37 DEFINITIONS bullet: `EXIT GATE B-IDs (dual-purpose): S1-S2: list boundaries-to-register; S3-S5: list B-IDs referenced` — the dual-purpose semantics are explicitly documented even in condensed form. C-20 requires the executor instructions to state dual-purpose semantics explicitly. PASS.

### Key C-24 analysis — INERTIA SURFACE strengthening (V-38, V-40)

V-38/V-40 REPORT REQUIRE: "Every A-NN from INERTIA SURFACE carries one of 4 dispositions; A-NNs-assigned fields from all EXIT GATEs cover all catalog entries (including new discoveries)" plus ASSUMPTION CATALOG RECONCILIATION arithmetic. This converts C-24's aggregate completeness check from a prose obligation to a verifiable equation. C-24 criterion is satisfied (and strengthened beyond threshold). PASS.

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | Criteria passing |
|-----------|-----------|-------------|--------------|-----------|------------------|
| V-36 | 40 | 30 | 10 | **80** | 28/28 |
| V-37 | 40 | 30 | 10 | **80** | 28/28 |
| V-38 | 40 | 30 | 10 | **80** | 28/28 |
| V-39 | 40 | 30 | 10 | **80** | 28/28 |
| V-40 | 40 | 30 | 10 | **80** | 28/28 |

**Golden threshold**: all essential pass + composite >= 80. **All five variations: GOLDEN.**

---

## Ranking

All variations tie at 80/80. Secondary ranking by structural novelty (v9 candidate signal density):

| Rank | Variation | Score | Axis | New Signal Candidates |
|------|-----------|-------|------|-----------------------|
| 1 | **V-40** | 80/80 | INERTIA SURFACE + conservation + utilization matrix | `pre-simulation-inertia-surface-catalog`, `assumption-conservation-arithmetic`, `cross-artifact-utilization-matrix` |
| 2 | **V-38** | 80/80 | INERTIA SURFACE pre-catalog | `pre-simulation-inertia-surface-catalog` |
| 3 | **V-39** | 80/80 | Contract-first + conservation arithmetic | `assumption-conservation-arithmetic` |
| 4 | **V-36** | 80/80 | Contract-first role sequence | (none — confirms V-35 patterns hold under inverted upstream ordering) |
| 5 | **V-37** | 80/80 | Condensed phrasing | (none — confirms structural enforcement is load-bearing, not elaboration) |

---

## R8 Open Questions — Resolved

| Question | Verdict | Evidence |
|----------|---------|---------|
| Does condensed phrasing preserve all 21 aspirational criteria? | **YES** | V-37 passes all 28 criteria. Elaboration is not load-bearing — EXIT GATE format, BOUNDARY REGISTRY, TRIAGE GATE, CCI, and REQUIRE blocks carry all structural enforcement. |
| Is INERTIA SURFACE C-01-compatible? | **YES** | V-38/V-40 declare INERTIA SURFACE before S1 in execution sequence. It is a pre-simulation compilation step (analogous to TRIAGE GATE), not a simulation section. C-01 checks simulation sections appear in declared order; INERTIA SURFACE precedes S1 and does not displace it. |
| Does A-NN column in FINDING TABLE conflict with C-10? | **NO** | A-NN is additive. All required columns (Sub-Skill, Location, Type, Blast Radius, Severity, Impact, Remediation) are present. C-10 pre-committed schema is extended, not replaced. |
| Does conservation arithmetic satisfy C-28 more completely than DEFINITIONS-only? | **YES** | V-39/V-40 REPORT enumerates explicit per-artifact counts (N_inertia_rows, N_covered, N_none, N_total) and verifies a residual equation. C-28's "REPORT can enumerate per-artifact counts" is satisfied mechanically, not interpretively. |
| Is CROSS-ARTIFACT UTILIZATION MATRIX distinct from C-22? | **YES** | C-22 DISCOVERY PATHWAY AUDIT groups by registry type (contract-boundary / permission-grant / inertia-boundary). The utilization matrix groups by B-ID, showing which artifact tables (FT/CI/TG) each individual boundary participates in. These are orthogonal views: one identifies discovery pathway yield, the other identifies per-boundary spec-coverage health profile. |
| Does V-40's combination produce artifact conflicts? | **NO** | A-NN and B-ID are distinct ID spaces. INERTIA SURFACE, conservation arithmetic, and utilization matrix write to distinct REPORT sections (ASSUMPTION CATALOG RECONCILIATION, ASSUMPTION CONSERVATION, CROSS-ARTIFACT UTILIZATION MATRIX). No shared resource contention. |

---

## Excellence Signals — V-40 (R8 Champion)

Three new patterns identified from V-40 that are not captured by any v8 criterion:

### SIGNAL-1: `pre-simulation-inertia-surface-catalog`
**Source**: V-38, V-40 (V-38 introduces it; V-40 confirms it composes with conservation and utilization matrix)

**Pattern**: An INERTIA SURFACE section executes before S1, assigning A-NN IDs to all observable status-quo assumptions before any simulation section begins. Section INERTIA blocks consume the catalog (validate entries, assign dispositions, add new discoveries with "discovered-in: SN" annotation). REPORT ASSUMPTION CATALOG RECONCILIATION verifies: pre-cataloged + discovered = final catalog total, and sum of A-NNs-assigned = final catalog total (unassigned must be 0).

**Why it strengthens v8**: C-24 requires an aggregate completeness check in REPORT REQUIRE — currently satisfied by the prose obligation "every named INERTIA assumption carries one disposition." The A-NN catalog converts this to an arithmetic identity: catalog total = sum of assigned. A missing assignment is detectable by subtraction, not by reading all INERTIA blocks. C-24 moves from prose-dependent to structurally auditable.

**Why it is distinct**: No existing v8 criterion requires pre-simulation assumption enumeration. C-24 works section-by-section with EXIT GATE A-NNs-assigned as the aggregate mechanism. The INERTIA SURFACE is a new structural artifact (a pre-simulation catalog) not required by any C-08 through C-28 criterion.

---

### SIGNAL-2: `assumption-conservation-arithmetic`
**Source**: V-39, V-40 (V-39 introduces it; V-40 confirms it composes with INERTIA SURFACE)

**Pattern**: A conservation equation is defined in DEFINITIONS and verified in REPORT: `N_inertia_rows + N_covered + N_none = N_total`. Each term is tracked through EXIT GATE fields (Inertia F-IDs for FINDING + INVESTIGATION; COVERED entries in CCI; NONE-count per section). A nonzero residual names specific unrouted assumptions — the reporting form is: `Residual: [0 -- conservation holds | N -- ROUTING FAILURE: [list unrouted A-NNs]]`.

**Why it strengthens v8**: C-28 requires DEFINITIONS to declare artifact routes and REPORT to enumerate per-artifact counts. Conservation arithmetic adds a cross-artifact equality constraint: the sum of counts across all artifact targets must equal total named assumptions. This catches routing failures (an assumption with no artifact entry) that per-artifact count checks alone cannot catch — an assumption absent from all three artifact tables produces no count violation but does produce a nonzero residual.

**Why it is distinct**: C-28's pass condition is satisfied by the presence of per-artifact tables with counts. Conservation arithmetic is an additive correctness verification on top of C-28 — a "sum-to-total" check that makes routing completeness verifiable by arithmetic rather than by inspection.

---

### SIGNAL-3: `cross-artifact-utilization-matrix`
**Source**: V-40 only

**Pattern**: After TRIAGE GATE and before disposition summary, REPORT assembles a CROSS-ARTIFACT UTILIZATION MATRIX: one row per B-ID, three boolean columns (FT, CI, TG marking presence in FINDING TABLE / COVERAGE CITATION INDEX / TRIAGE GATE), and a Profile field (FT only / CI only / TG only / FT+CI / FT+TG / CI+TG / FT+CI+TG). Utilization interpretation block summarizes: CI-only count (fully spec-defended boundaries), FT-only count (gap-surface-only boundaries), TG-containing count (ambiguity concentration), and highest-risk boundary.

**Why it strengthens v8**: C-22 DISCOVERY PATHWAY AUDIT groups by registry type — it answers "which discovery pathway (contract vs inertia) yields more findings?" The utilization matrix answers a different question: "for each individual boundary, what is its spec-coverage health profile?" A boundary that appears in all three artifact tables has confirmed spec-gaps, confirmed spec-coverage, and unresolved ambiguity simultaneously — a full mixed profile. A boundary appearing only in CI is fully spec-defended. These boundary health profiles are actionable implementation guidance that the type-aggregated C-22 table cannot surface.

**Why it is distinct**: C-22 aggregates by registry type; the utilization matrix aggregates by B-ID. Orthogonal dimensions. C-22 reveals discovery pathway breadth across the registry; the utilization matrix reveals coverage depth per boundary. A registry can have high C-22 inertia-boundary yield but all boundaries might be CI-only (fully defended) — the utilization matrix catches this whereas C-22 does not.

---

## Verdict

**V-40 is the R8 champion** (80/80, GOLDEN). V-35 saturates v8 as predicted; R8 explores v9 territory. All five R8 variations confirm that V-35's structural foundation is robust under three independent axes (role order, phrasing register, inertia framing) and two combinations. Three new excellence signal candidates are confirmed valid for v9 codification.

```json
{"top_score": 80, "all_essential_pass": true, "new_patterns": ["pre-simulation-inertia-surface-catalog", "assumption-conservation-arithmetic", "cross-artifact-utilization-matrix"]}
```
