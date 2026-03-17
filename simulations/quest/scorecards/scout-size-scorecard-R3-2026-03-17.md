# scout-size R3 — Quest Scorecard

**Rubric**: v3 (17 criteria) | **Date**: 2026-03-17 | **Variations**: V-01 through V-05

---

## Scoring Key

| Symbol | Meaning | Composite weight |
|--------|---------|-----------------|
| PASS | Criterion met by prompt structure | Full credit |
| PARTIAL | Mechanism present but incomplete | Treated as FAIL for composite |
| FAIL | Criterion not addressed | 0 credit |
| PASS* | Default pass — criterion requires AMEND context not present | Full credit |

---

## Per-Criterion Scores

### Essential Criteria (60 pts — 12 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-01** Complexity tier LOW/MEDIUM/HIGH/XL | PASS | PASS | PASS | PASS | PASS | All variations enforce exact vocabulary |
| **C-02** Sprint range (N–M, not point estimate) | PASS | PASS | PASS | PASS | PASS | All variations have "N–M sprints" with anti-examples |
| **C-03** Surface area quantified by integration points | PASS | PASS | PASS | PASS | PASS | All variations require table with Total row |
| **C-04** Inertia check names workaround and cost | PASS | PASS | PASS | PASS | PASS | All variations have INERTIA CHECK with Workaround/Maintenance cost/Cost direction |
| **C-05** Confidence stated with basis | PASS | PASS | PASS | PASS | PASS | All variations have CONFIDENCE section with Basis field |

**Essential result**: 5/5 for all variations — all clear the Golden threshold requirement.

---

### Recommended Criteria (30 pts — 10 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-06** Team signal names specializations | PASS | PASS | PASS | PASS | PASS | All name disciplines; V-02 weaker example ("1 backend, 0.5 PM") but still passes |
| **C-07** Complexity rating justified with driver | PASS | PASS | PASS | PASS | PASS | All have "Primary driver" field |
| **C-08** AMEND modifies stated output | PASS* | PASS* | PASS* | PASS* | PASS | V-01 through V-04 default-pass (no AMEND mechanism); V-05 has AMEND INSTRUCTION in Step 7 |

**Recommended result**: 3/3 for all variations.

---

### Aspirational Criteria (10 pts — 1.11 pts each, 9 total)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-09** Sizes what is NOT included | FAIL | FAIL | FAIL | FAIL | PASS | V-01–V-04 SIGNAL BOUNDARY names artifact type, not analysis scope. V-05 self-check forces the model to add an explicit exclusion/assumption before writing |
| **C-10** Break-even signal | FAIL | FAIL | FAIL | FAIL | PASS | Only V-05 self-check (item C-10) enforces this; no section instruction covers it in any other variation |
| **C-11** Named specializations include ownership scope | PASS | FAIL | PASS | PASS | PASS | V-02 example ("1 backend engineer, 0.5 PM") gives no ownership; V-01/V-03/V-04/V-05 explicitly require ownership per role with passing example |
| **C-12** Confidence names specific unknowns that would change rating | PASS | PASS | PASS | PASS | PASS | V-01/V-03/V-04/V-05 via OPEN UNKNOWNS; V-02 via Gap + "What would raise it" in CONFIDENCE |
| **C-13** Synthesis integrates signals (not juxtaposition) | PASS | PASS | PASS | PASS | PASS | All require cross-dimensional conclusion; most name the anti-pattern |
| **C-14** Open unknowns in dedicated section with typed fields | PASS | FAIL | PARTIAL | PASS | PASS | V-02: unknowns embedded in confidence prose only. V-03: dedicated section exists but CONFIDENCE also has Gap (no "do not list here" guard) — structural separation is present but leaky. V-01/V-04/V-05 explicitly prohibit unknowns from confidence section |
| **C-15** Synthesis confirms/revises a prior stated hypothesis | FAIL | PASS | FAIL | PASS | PASS | Only V-02/V-04/V-05 have PRELIMINARY HYPOTHESIS block before analysis sections |
| **C-16** AMEND cascades to synthesis when dimension is cited | PASS* | PASS* | PASS* | PASS* | PASS | V-01–V-04 default-pass (no AMEND mechanism). V-05: explicit AMEND INSTRUCTION inside Step 7 requires re-reading synthesis and updating or reaffirming when amended dimension appears there |
| **C-17** Aspirational sections name their failure mode | PASS | PASS | PASS | PASS | PASS | V-01: synthesis says "Restating sections in sequence… is juxtaposition"; unknowns says "generic placeholder… fails." V-02: "Writing a synthesis that ignores the hypothesis is post-hoc rationalization." V-03/V-05: explicit `> FAILURE MODE FOR THIS SECTION:` callouts inside sections. V-04: synthesis says "Ignoring the hypothesis… is post-hoc rationalization" |

**Note on V-03 C-14**: Scored as PARTIAL → FAIL for composite. Dedicated section exists and typed fields are present, but CONFIDENCE still carries a Gap field with no prohibition — the structural separation is incomplete. V-01 and V-04 are strictly cleaner.

---

## Aspirational Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|-|------|------|------|------|------|
| C-09 | — | — | — | — | ✓ |
| C-10 | — | — | — | — | ✓ |
| C-11 | ✓ | — | ✓ | ✓ | ✓ |
| C-12 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-13 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-14 | ✓ | — | — | ✓ | ✓ |
| C-15 | — | ✓ | — | ✓ | ✓ |
| C-16 | ✓* | ✓* | ✓* | ✓* | ✓ |
| C-17 | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Pass count** | **6/9** | **5/9** | **5/9** | **7/9** | **9/9** |

---

## Composite Scores

```
composite = (essential_pass / 5 × 60) + (recommended_pass / 3 × 30) + (aspirational_pass / 9 × 10)
```

| Variation | Essential | Recommended | Aspirational | **Composite** | Band |
|-----------|-----------|-------------|--------------|---------------|------|
| V-01 | 60.0 (5/5) | 30.0 (3/3) | 6.67 (6/9) | **96.67** | Gold |
| V-02 | 60.0 (5/5) | 30.0 (3/3) | 5.56 (5/9) | **95.56** | Gold |
| V-03 | 60.0 (5/5) | 30.0 (3/3) | 5.56 (5/9) | **95.56** | Gold |
| V-04 | 60.0 (5/5) | 30.0 (3/3) | 7.78 (7/9) | **97.78** | Gold |
| **V-05** | **60.0 (5/5)** | **30.0 (3/3)** | **10.0 (9/9)** | **100.00** | **Gold** |

---

## Ranking

1. **V-05** — 100.00 (all 17 criteria)
2. **V-04** — 97.78 (misses C-09, C-10)
3. **V-01** — 96.67 (misses C-09, C-10, C-15)
4. **V-02** — 95.56 (misses C-09, C-10, C-11, C-14) — tied with V-03
4. **V-03** — 95.56 (misses C-09, C-10, C-15, C-14 partial)

---

## Excellence Signals — V-05

Three structural mechanisms elevated V-05 from V-04's 97.78 to 100:

**1. Pre-write self-check as enforcement gate for section-less criteria**
C-09 (scope exclusion) and C-10 (break-even) have no dedicated section in any variation — including V-05. But V-05's 17-criterion self-check forces the model to verify both before writing the artifact, with "Fix any violation before writing." This is the only mechanism that can address criteria that don't map to a section. The pattern: *enumerate all criteria in a checklist with a fix mandate, not just in section instructions.*

**2. AMEND INSTRUCTION co-located inside synthesis**
V-05 places the AMEND cascade requirement inside Step 7 (synthesis), co-located with the synthesis generation itself: "If the amended dimension appears in the synthesis conclusion, update the conclusion or explicitly reaffirm it." No earlier variation did this — AMEND was either absent (V-01–V-03) or not connected to synthesis (V-04). Co-location prevents the failure mode where the model acknowledges an amendment in the amended section and then forgets to revisit synthesis.

**3. Mutually reinforcing trio: hypothesis → unknowns section → synthesis**
V-05 is the first variation where all three mechanisms are active simultaneously. The preliminary hypothesis constrains what synthesis can conclude. The typed unknowns section makes gaps visible before synthesis is written. The failure-mode callouts inside both sections enforce quality at generation time. These three mechanisms create a closed loop: the hypothesis predicts, the unknowns explain residual uncertainty, and synthesis must reconcile both — no dimension can change silently without the structure catching it.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-write 17-criterion self-check with fix mandate addresses criteria (C-09 scope exclusion, C-10 break-even) that have no dedicated section — the only mechanism that enforces section-less aspirational criteria", "AMEND INSTRUCTION co-located inside synthesis step requires re-evaluation of synthesis when amended dimension appears in conclusion — prevents silent contradiction that earlier AMEND mechanisms left open", "hypothesis-revision + typed unknowns section + failure-mode callouts form a closed loop: hypothesis constrains synthesis, unknowns section constrains confidence gap, callouts enforce quality at generation — all three must be active simultaneously for the structure to be self-reinforcing"]}
```
