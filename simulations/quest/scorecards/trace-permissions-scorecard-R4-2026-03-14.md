Scorecard written. Here are the results:

---

## Round 4 Scorecard — trace-permissions

**Top score: 130/130. All essential pass: YES.**

| Rank | Variation | Score | C-15 |
|------|-----------|-------|------|
| 1 (tie) | V-01 (Source column) | **130/130** GOLDEN | PASS |
| 1 (tie) | V-03 (Gap ID threading) | **130/130** GOLDEN | PASS |
| 1 (tie) | V-04 (Three-level combined) | **130/130** GOLDEN | PASS |
| 1 (tie) | V-05 (Source + inertia) | **130/130** GOLDEN | PASS |
| 5 | V-02 (Inventory gate only) | **125/130** | **FAIL** |

**The single discriminator is C-15 (5 pts).** Four variations pass; V-02 fails.

**Why V-02 fails C-15:** V-02's Requirement C commits a Gap ID inventory before Phase 3 gate and prohibits new IDs in Phase 4 — but Table 7 has no Source column. An output following V-02 contains no per-gap source citation. C-15's pass condition is "must trace to a specific evidence table and row," which requires the citation record in the output, not just a prohibition rule. **Prohibition stops errors; citation provides evidence. C-15 requires evidence.**

**The two new patterns:**

1. **Source column is the minimum sufficient mechanism for C-15** — V-01 (single-axis: Source column only) achieves 130/130. The Source column converts a structural prohibition into a positive output record. All four ceiling-hitting variations share exactly this column.

2. **Prohibition-based vs. citation-based enforcement are structurally distinct** — V-02's inventory gate operates at section-transition granularity (like C-14), preventing new gap injection. C-15 operates at cell granularity — it requires an explicit source citation per gap. A mechanism that closes a list is not the same as a mechanism that records origins. This is the R4 design question answered: V-02's single-axis mechanism is insufficient not because gates are weak, but because gates are the wrong granularity for C-15.

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["Source column in Table 7 is the minimum sufficient mechanism for C-15 -- it converts a structural prohibition into a positive output record (per-gap source citation) that the evaluator can verify; prohibition-only mechanisms (inventory gate without Source column) fail C-15 because they prevent origination errors but do not produce traceable evidence in the output artifact", "Prohibition-based enforcement and citation-based enforcement are structurally distinct: a gate that closes a gap list (V-02 inventory gate) satisfies C-14-granularity provenance but not C-15-granularity provenance -- the rubric requires the citation record, not the rule"]}
```
are unchanged from R3 V-04.

#### C-13 -- Hypothesis-Anchored Evidence Tables

All five variations carry Requirement A (H-flag columns). H-flag is present as the rightmost column in all evidence tables across all variations.

V-05 note: extra inertia columns ("What breaks if this access is removed?", "What change would open this path?", "What triggers this conflict?") are inserted to the LEFT of H-flag in Tables 2, 3, 4, and 5. H-flag remains rightmost. No compliance friction. PASS.

#### C-14 -- Explicit Phase Completion Gate

All five variations carry Requirement B (PHASE N COMPLETE markers). PASS all.

V-02 note: the inventory block must appear immediately before PHASE 3 COMPLETE, strengthening C-14 compliance for Phase 3 beyond R3 V-04.

#### C-15 -- Gap Provenance Enforcement

| Variation | Mechanism | Source column in T7? | Per-gap citation in output? | C-15 |
|-----------|-----------|---------------------|------------------------------|------|
| V-01 | Backward reference column | YES | YES | PASS |
| V-02 | Inventory gate + prohibition | NO | NO | FAIL |
| V-03 | Gap ID threading + Source column | YES | YES | PASS |
| V-04 | Three levels: threading + Source column + inventory gate | YES | YES | PASS |
| V-05 | Source column (single axis) | YES | YES | PASS |

The disqualifying defect for V-02: C-15 requires the output to contain evidence of traceability. A prohibition stops errors; a citation provides evidence. C-15 requires evidence, not just the rule.

---

### Variation Ranking

| Rank | Variation | Score | C-15 mechanism | Structural notes |
|------|-----------|-------|---------------|-----------------|
| 1 | V-01 | 130/130 GOLDEN | Source column (single axis) | Minimum sufficient mechanism; cleanest design |
| 1 | V-03 | 130/130 GOLDEN | Gap ID threading + Source column | Two-level provenance; strongest forward chain |
| 1 | V-04 | 130/130 GOLDEN | All three levels | Maximum enforcement; most mechanically complete |
| 1 | V-05 | 130/130 GOLDEN | Source column + inertia framing | Inertia adds content depth; no compliance cost |
| 5 | V-02 | 125/130 | Inventory gate only | Provenance by prohibition; no citation |

---

### Excellence Signals

**Signal 1 -- Source column is the minimum sufficient mechanism for C-15**

All four 130-scoring variations include `Source (Table + Row)` in Table 7. V-02 omits it and fails C-15. The Source column is the atomic unit for C-15 compliance: it converts a structural prohibition ("gaps must originate in Phase 3") into a positive output record ("this gap came from Table 4, Row 2"). The rubric requires the record, not just the rule.

**Signal 2 -- Prohibition-based enforcement is not citation-based enforcement**

V-02 reveals a fundamental distinction: preventing an error (inventory gate: "no new gaps") and recording provenance (Source column: "this gap came from here") are solving different problems. C-15 is a provenance criterion, not a prohibition criterion. An inventory gate without a Source column achieves the intent but not the evidence. For rubric scoring, evidence is what is scored.

**Signal 3 -- Inertia framing (V-05) is compatible with all structural criteria**

V-05 extra columns do not displace H-flag (remains rightmost) and do not affect Table 7 Source column or Phase 4 structure. The hypothesized compliance friction does not materialize. Inertia framing is additive: it improves analytical depth on C-05/C-06/C-07 without structural cost.

**Signal 4 -- V-04 three-level defense addresses runtime model failure, not rubric failure**

V-04 earns the same 130 as V-01. Additional mechanisms (Gap ID threading + inventory gate) do not add rubric points. Their value is runtime reliability: V-03 and V-04 Gap ID threading makes any spurious Table 7 row mechanically detectable by inspection. Not captured in the rubric but matters for production.

---

### R4 Key Findings

**F-01: Source column is necessary and sufficient for C-15 (against this rubric)**
V-01 single-axis approach achieves 130/130. C-15 is a citation criterion. A prompt that forces source citation passes; one that only prohibits new gaps without requiring citations fails.

**F-02: V-02 inventory gate is C-14 analog for provenance, not C-15 analog**
V-02 operates at section-transition granularity. C-15 is a cell-level criterion (per-gap source citation). V-02 applies the right granularity for C-14 and the wrong granularity for C-15. Future rubric design note: a gate-level provenance criterion (C-16?) would be satisfied by V-02 mechanism.

**F-03: Predicted ceiling confirmed; achievable by four independent mechanisms**
R4 predicted V-04 would hit 130/130. It does. The more informative finding: V-01, V-03, V-05 also hit 130/130 via simpler designs. The rubric does not reward mechanism redundancy -- only output traceability.

**F-04: All essential criteria pass (unchanged from R3)**
The essential and recommended foundation (C-01 through C-07) is stable across all variations and rounds. Discrimination lives exclusively in the aspirational tier.

---

### Recommended Golden Candidate

**V-04** remains the recommended production candidate for structural robustness (three independent C-15 enforcement levels, H-flag, phase gates -- any single mechanism failure is caught by the other two).

**V-01** is the minimum-overhead path to 130/130: Source column alone satisfies C-15.

**V-05** is the candidate for production quality: inertia framing adds analytical depth the rubric does not yet measure.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["Source column in Table 7 is the minimum sufficient mechanism for C-15 -- it converts a structural prohibition into a positive output record (per-gap source citation) that the evaluator can verify; prohibition-only mechanisms (inventory gate without Source column) fail C-15 because they prevent origination errors but do not produce traceable evidence in the output artifact", "Prohibition-based enforcement and citation-based enforcement are structurally distinct: a gate that closes a gap list (V-02 inventory gate) satisfies C-14-granularity provenance but not C-15-granularity provenance -- the rubric requires the citation record, not the rule"]}
```
