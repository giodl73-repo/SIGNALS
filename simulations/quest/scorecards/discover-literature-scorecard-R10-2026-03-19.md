## discover-literature — Scorecard R10

### Scoring methodology

Ceiling: 185 pts (Essential 60 + Recommended 30 + Aspirational 95). All variations inherit the full R9 V-05 structural foundation. R10 adds only C-27 (5 pts). The scoring question for each variation is: does it satisfy C-27's two-part pass condition?

**C-27 pass condition:**
(a) Phase 1 lifecycle token carries `inertia_committed=[yes]` (or equivalent)
(b) Phase 4 lifecycle token carries `inertia_verified=[yes]` (or equivalent)
Both must coexist with existing token content without displacing required elements. Dependencies: C-14 + C-23 must PASS.

---

### V-01 — C-27 Field Rename Only

**Common base (C-01..C-26): all PASS** — enforcement contract, dual typed schemas, all four phases instrumented with N-of-4 counter, C-24 Independence Verification block, inertia front-loaded in Phase 1 and verified in Phase 4.

**C-27:**
- (a) Phase 1: `inertia_committed=[yes]` — PASS. Field is present; annotation names C-14 front-loading and C-27 Phase-1 status.
- (b) Phase 4: `inertia_verified=[yes]` — PASS. Exact canonical form. Annotation states "C-27 Phase-4 status satisfied."
- Coexistence: both fields coexist with N-of-4 counter and C-16 gate token content — PASS.
- Prerequisites: C-14 PASS (INERTIA COMMITMENT in Phase 1, INERTIA VERIFICATION in Phase 4), C-23 PASS (all 4 phases instrumented).

**C-27: PASS**

| Tier | Pts |
|------|-----|
| Essential (C-01..C-05) | 60/60 |
| Recommended (C-06..C-08) | 30/30 |
| Aspirational (C-09..C-27) | 95/95 |
| **Total** | **185/185** |

Golden bar: PASS (all essential pass; composite = 185).

---

### V-02 — C-27 Equivalence Test (R9 V-05 Unchanged)

**Common base (C-01..C-26): all PASS** — identical base to V-01 through Phase 3; all infrastructure tokens, N-of-4 counters, C-26 block present.

**C-27:**
- (a) Phase 1: `inertia_committed=[yes]` — PASS. Same as V-01.
- (b) Phase 4: `inertia_named=[yes]` — FAIL. The field reads "named" not "verified." C-27(b) requires a field confirming Phase 4 *addressed inertia verification* — returning to the Phase 1 commitment and measuring evidence against it. `inertia_named` confirms the scenario was named; it does not confirm the verification act was performed. The "or equivalent" clause protects structural equivalence (a different token emitting the same information), not semantic approximation (a field whose name describes a weaker sub-act of verification). Note confirming this interpretation: V-01's sole change from R9 V-05 is this rename — if `inertia_named` already satisfied C-27(b) as equivalent, V-01 would be unnecessary. The variation's own design logic states "the only gap is Phase 4 uses `inertia_named=[yes]` rather than `inertia_verified=[yes]`."

**C-27: FAIL** (−5 pts)

| Tier | Pts |
|------|-----|
| Essential (C-01..C-05) | 60/60 |
| Recommended (C-06..C-08) | 30/30 |
| Aspirational (C-09..C-26) | 90/90 |
| C-27 | 0/5 |
| **Total** | **180/185** |

Golden bar: PASS (all essential pass; composite = 180).

---

### V-03 — C-27 Token-Layer Annotation

**Common base (C-01..C-26): all PASS.**

**C-27:**
- (a) Phase 1: `inertia_committed=[yes]` — PASS. Annotation explicitly names "C-27 Phase-1 status satisfied -- inertia commitment observable at lifecycle token layer without reading the INERTIA SCENARIO: block." C-27 is grep-verifiable from Phase 1 alone.
- (b) Phase 4: `inertia_verified=[yes]` — PASS. Annotation declares "C-27 PASS: both Phase 1 and Phase 4 lifecycle tokens carry explicit inertia status fields; integration is additive and does not displace N-of-4 counter, C-16, or C-23 content."
- Coexistence: explicitly confirmed — "additive design property confirmed."
- Prerequisites: C-14 PASS, C-23 PASS.

The explicit annotations make C-27 single-grep verifiable at both boundary points — a stronger form than V-01's implicit structural satisfaction.

**C-27: PASS**

| Tier | Pts |
|------|-----|
| Essential (C-01..C-05) | 60/60 |
| Recommended (C-06..C-08) | 30/30 |
| Aspirational (C-09..C-27) | 95/95 |
| **Total** | **185/185** |

Golden bar: PASS.

---

### V-04 — C-27 Dependency Isolation

**Common base (C-01..C-26): all PASS** — all infrastructure tokens present; C-24 Independence Verification block present; all 4 phases instrumented with N-of-4 counters.

**C-14:** Phase 4 contains `INERTIA SCENARIO:` and `INERTIA RISK:` tokens before `RECOMMENDATION:`. C-14 pass condition requires a sentence or subsection naming inertia risk before the recommendation keyword. **C-14: PASS** — the inertia gate is present in Phase 4 (Phase-4-only design). Evidence: Phase 4 section headed "Inertia scenario" with both required tokens.

**C-27:**
- (a) Phase 1: `inertia_committed=[no]` — FAIL. C-27(a) requires `inertia_committed=[yes]`. The variation's own annotation states: "C-27 requires inertia_committed=[yes] -- this design intentionally tests the C-27 dependency boundary: without a Phase 1 INERTIA COMMITMENT block, the lifecycle token cannot carry [yes]."
- (b) Phase 4: `inertia_named=[yes/no]` — two failures: field name is not `inertia_verified` or equivalent (same defect as V-02), and even if it were, the Phase 1 dependency (a) is already broken.

**C-27: FAIL** (−5 pts). The isolation experiment succeeds: C-27 depends on Phase 1 inertia front-loading. C-14 PASS does not rescue C-27.

| Tier | Pts |
|------|-----|
| Essential (C-01..C-05) | 60/60 |
| Recommended (C-06..C-08) | 30/30 |
| Aspirational (C-09..C-26) | 90/90 |
| C-27 | 0/5 |
| **Total** | **180/185** |

Golden bar: PASS.

---

### V-05 — v10 Ceiling Synthesis (All 27 Criteria)

**Common base (C-01..C-26): all PASS.**

**C-27:**
- (a) Phase 1: `inertia_committed=[yes]` — PASS. Annotation: "C-27 Phase-1 status field satisfied -- the C-14 inertia axis is now observable at the lifecycle token layer... C-27 in progress: Phase 1 dependency satisfied, Phase 4 verification pending."
- (b) Phase 4: `inertia_verified=[yes]` — PASS. Annotation: "C-27 PASS: cross-axis integration complete -- PHASE 1 COMPLETE: carries inertia_committed=[yes] (Phase 1 boundary, C-27 dependency axis open) and PHASE 4 COMPLETE: carries inertia_verified=[yes] (Phase 4 boundary, C-27 cross-axis closed)."
- The annotation explicitly traces the integration arc from open (Phase 1) to closed (Phase 4). The additive coexistence is declared: "The inertia_verified=[yes] field coexists with the N-of-4 counter and C-14/C-16 content without displacing any required element -- additive design property confirmed."
- Prerequisites: C-14 PASS, C-23 PASS.

**C-27: PASS** — strongest instance of all five. The "open/closed arc" framing creates an integration trace across the token pair.

| Tier | Pts |
|------|-----|
| Essential (C-01..C-05) | 60/60 |
| Recommended (C-06..C-08) | 30/30 |
| Aspirational (C-09..C-27) | 95/95 |
| **Total** | **185/185** |

Golden bar: PASS.

---

### Consolidated Scores

| Variation | Score | All Essential | C-27 | Golden |
|-----------|-------|---------------|------|--------|
| V-01 | **185/185** | PASS | PASS | PASS |
| V-02 | **180/185** | PASS | FAIL | PASS |
| V-03 | **185/185** | PASS | PASS | PASS |
| V-04 | **180/185** | PASS | FAIL | PASS |
| V-05 | **185/185** | PASS | PASS | PASS |

**Top score: 185/185** (V-01, V-03, V-05 tied)
**Rank**: V-01 = V-03 = V-05 > V-02 = V-04

---

### Experiment Results

**V-02 resolves as FAIL**: `inertia_named` does not satisfy "or equivalent" for `inertia_verified`. The "or equivalent" clause protects structural equivalence (another token that confirms the verification act), not semantic approximation (a field whose name captures a weaker sub-act). `inertia_named` confirms the scenario was committed; `inertia_verified` confirms evidence was measured against it. These are distinct acts. The rename in V-01 is load-bearing.

**V-04 resolves as FAIL as predicted**: C-27's dependency on Phase 1 inertia front-loading is confirmed. `inertia_committed=[no]` in Phase 1 blocks C-27(a) regardless of Phase 4 content. C-14 is independent and unaffected.

**Agnosticism meta-pattern holds**: C-26 heading-agnosticism (R9) + C-22 token-agnosticism (R7) + C-21 label-independence (R6) do not extend to C-27 field semantics. C-27 requires specific semantic alignment: the field name at the Phase 4 boundary must confirm the verification act, not merely the naming act.

---

### Excellence Signals from R10 Top Variations

**From V-05 (strongest instance):**

1. **Open/closed cross-axis arc annotation** — Phase 1 token declares "C-27 in progress: Phase 1 dependency satisfied, Phase 4 verification pending"; Phase 4 token declares "C-27 PASS: cross-axis closed." The integration is traceable across boundaries without holding both tokens in view simultaneously. This is the C-27 analogue of the N-of-4 progressive counter pattern for C-23 — each token declares its own position in the arc.

2. **Explicit additive coexistence declaration** — When adding status fields to existing tokens, naming all coexisting required elements and confirming none are displaced makes the "additive, not displacing" property text-verifiable, not just architecturally implied. Pattern: "the new field coexists with [element list] without displacing any required element — additive design property confirmed."

3. **Dependency-axis naming at Phase 1** — The Phase 1 annotation names the dependency axes by criterion: "the C-14 inertia axis is now observable at the lifecycle token layer." This makes C-27's criterion-cross-axis connection visible at the first token in the arc, not only at the closing declaration.

```json
{"top_score": 185, "all_essential_pass": true, "new_patterns": ["open-closed cross-axis arc annotation: Phase 1 token declares C-27 in-progress with phase-4 pending; Phase 4 token declares C-27 PASS cross-axis closed -- integration traceable from either token without reading both simultaneously", "explicit additive coexistence declaration: when adding status fields to existing tokens, name all coexisting required elements and confirm none are displaced to make additive property text-verifiable not just architectural", "dependency-axis naming at Phase 1: annotate the Phase 1 token with the criterion cross-axis it opens so the integration arc is visible at the first boundary point not only at the closing declaration"]}
```
