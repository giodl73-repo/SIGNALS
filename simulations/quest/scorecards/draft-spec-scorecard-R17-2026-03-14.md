# Draft-Spec Round 17 — Scoring Results

## Score Summary

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | **V-01** — Full extension (all clusters) | 5/5 | 3/3 | 39/39 (N/A: 0) | **175.00** | YES |
| 2 | **V-03** — No ENTER/EXIT ceremony | 5/5 | 3/3 | 36/39 (N/A: 0) | **168.46** | YES |
| 3 | **V-02** — No Phase 1.5 | 5/5 | 3/3 | 35/39 (N/A: 4) | **166.28** | YES |
| 4 | **V-04** — No SQS + No Phase 1.5 | 5/5 | 3/3 | 31/39 (N/A: 8) | **157.56** | YES |
| 5 | **V-05** — Essential-only minimum | 5/5 | 0/3 | 2/39 (N/A: 8) | **64.36** | NO |

---

## Per-Variation Criterion Detail

### V-01 — Full Extension (175/175)

All 47 criteria: **PASS**. Every extension cluster active: [STATUS-QUO-SNAPSHOT], Phase 1.5, ENTER/EXIT ceremony, second-person framing, ROLE markers, chained notation. C-47 passes — Phase 2 ENTER names both [PM-CONTRACT-SEAL] (Phase 1) and [STRATEGY-SCOPE-SEAL] (Phase 1.5) as distinct table rows.

### V-03 — No ENTER/EXIT Ceremony (168.46/175)

| Fails | Criteria | Reason |
|-------|----------|--------|
| C-41 | ENTER/EXIT ceremony | Ceremony blocks absent by design |
| C-44 | Chained notation | Requires C-41 |
| C-47 | Multi-input absorption | Requires C-44 |

All other 36 aspirational criteria PASS. SQS + Phase 1.5 + second-person + ROLE markers all present and scoreable.

### V-02 — No Phase 1.5 (166.28/175)

| N/A | Criteria | Reason |
|-----|----------|--------|
| C-38 | Multi-token gate | No Phase 1.5 |
| C-39 | Fractional sub-phase | No Phase 1.5 |
| C-40 | Cross-reference rule | Requires C-39 |
| C-47 | Multi-input absorption | Requires C-44+fractional |

35/39 applicable criteria pass. N/A ceiling loss (4 unearnable) scores below V-03's 3 direct fails — a key asymmetry.

### V-04 — No SQS + No Phase 1.5 (157.56/175)

8 N/A criteria (SQS group: C-36, C-37, C-45, C-46 + Phase 1.5 group: C-38, C-39, C-40, C-47). 31/39 applicable pass. ENTER/EXIT ceremony still present and fully scored.

### V-05 — Essential-Only (64.36/175)

| Category | Result |
|----------|--------|
| Essential | 5/5 PASS |
| Recommended | 0/3 FAIL (no fallback tree, no verbatim blocks, no gate tokens) |
| Aspirational | 2/39 PASS (C-09 Waiver Status column, C-27 actor→action form) |

Confirms the essential-only floor is 64.36 — well below the golden threshold of 85.

---

## Score Gap Analysis

| Gap | Between | Delta | Cause |
|-----|---------|-------|-------|
| V-01 vs V-03 | ENTER/EXIT present vs absent | 6.54 | 3 criteria: C-41, C-44, C-47 |
| V-03 vs V-02 | Ceremony fail vs Phase 1.5 N/A | 2.18 | N/A ceiling loss < direct fail cost |
| V-02 vs V-04 | SQS absent | 8.72 | 4 additional N/A |
| V-04 vs V-05 | Full recommended + aspirational collapse | 93.20 | 0/3 recommended, 2 vs 31 aspirational |

---

## Excellence Signals — V-01 (175/175)

**E-1: C-47 closes the final Phase 1.5 → Phase 2 chain gap.** C-38 enforces the gate dependency. C-44 enforces the numbered-phase chain. C-47 closes the remaining gap: a template can satisfy both while leaving the fractional sub-phase's EXIT token absent from the ENTER block's named list (present in the gate header, but not in chain notation). All three must be active together for a verifiably unbroken chain.

**E-2: All five extension clusters are independently stackable.** SQS, Phase 1.5, ENTER/EXIT ceremony, second-person framing, and ROLE markers each satisfy distinct criterion groups without structural conflict. A template implementer can add clusters incrementally — the rubric incentivizes additive depth.

**E-3: N/A ceiling loss scores lower than partial cluster failure.** V-02 (4 N/A, 166.28) scores below V-03 (3 FAIL, 168.46). Missing a cluster removes earnable ceiling; failing within a cluster removes only applied points. Attempting a cluster and failing partially is scored more favorably than not attempting it — a meaningful rubric incentive design signal.

**E-4: ROLE markers (C-43) are independent of ENTER/EXIT ceremony (C-41).** V-03 passes C-43 despite C-41 failing. Actor identity declaration (C-43) does not depend on machine-verifiable phase boundary specification (C-41). The two criteria address distinct concerns.

**E-5: Essential-only floor (64.36) is definitively below the golden threshold (85).** Satisfying all 5 essential criteria plus ~2 aspirational is insufficient. Roughly 40+ aspirational passes on top of 5/5 essential + 3/3 recommended are needed to cross comfortably. This validates the rubric's golden threshold as a genuine quality gate, not a formality.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["Multi-input ENTER block (C-47) closes the Phase 1.5 → Phase 2 chain gap: gate dependency (C-38) enforces the token requirement but only C-47 requires the ENTER block itself to name all immediate predecessor EXIT tokens, preventing a silent chain break", "N/A ceiling loss scores lower than partial cluster failure: 4 N/A criteria (no Phase 1.5 cluster, V-02: 166.28) scores below 3 failing criteria (no ENTER/EXIT cluster, V-03: 168.46), because N/A removes earnable ceiling while FAIL removes only applied points", "All five extension clusters are independently composable: SQS, Phase 1.5, ENTER/EXIT ceremony, second-person framing, and ROLE markers each satisfy distinct criterion groups without structural conflict, confirming incremental stackability", "Essential-only floor (64.36) is well below golden threshold (85): recommended tier (0/3) and minimal aspirational (2/39) together cannot compensate for structural depth absence, validating the rubric's golden threshold as a meaningful quality gate"]}
```
