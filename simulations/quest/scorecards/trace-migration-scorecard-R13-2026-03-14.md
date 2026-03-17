# trace-migration — Round 13 Scoring (Rubric v11)

## Scoring Methodology

Baseline: R12 V-04 passes C-01–C-34 at **220 pts**. R13 opens only C-35 and C-36 (5 pts each).

---

## C-35 Analysis — Boundary Protocol Named-Artifact Countability

**Pass condition:** BOUNDARY PROTOCOL must be a named section header at each boundary, making gate coverage verifiable by header scan count (N boundaries = N headers) without reading phase interiors.

| V | Evidence | Result |
|---|----------|--------|
| V-01 | Six `### BOUNDARY PROTOCOL` headers present (PARSE→A, A→B, B1→B2, B2→B3, B3→B4, B4→VERDICT) | **PASS** |
| V-02 | Inline code fences carry EXIT BLOCK + ENTRY REFERENCE inside phase body prose — presence requires reading interiors | **FAIL** |
| V-03 | Six `### BOUNDARY PROTOCOL` headers — identical to V-01 structure | **PASS** |
| V-04 | Six `### BOUNDARY PROTOCOL` headers | **PASS** |
| V-05 | Six headers + PROTOCOL COUNT MANIFEST table at Phase B entry — dual-surface verification | **PASS** |

---

## C-36 Analysis — Pre-Interrogation Status Quo Cost Section

**Pass condition:** A named STATUS QUO COST section with explicit (a)/(b)/(c) three-part structure must appear before Q1 as a structural entry precondition, not embedded inside Q1 as instruction text.

| V | Evidence | Result |
|---|----------|--------|
| V-01 | PARITY BLOCK item 5 reads "See STATUS QUO COST baseline in Q1 — anchor to it." Explicitly positions inertia baseline inside Q1. | **FAIL** |
| V-02 | Named `#### STATUS QUO COST *(Pre-Interrogation)*` section precedes Q1 with labeled (a)/(b)/(c) fields and STATUS QUO GATE | **PASS** |
| V-03 | Named STATUS QUO COST section before Q1 with (a)/(b)/(c) + STATUS QUO GATE | **PASS** |
| V-04 | Named STATUS QUO COST before Q1, infrastructure-oriented framing, (a)/(b)/(c) fields + STATUS QUO GATE | **PASS** |
| V-05 | Named STATUS QUO COST as COST LEDGER table (three rows = three parts, machine-countable), STATUS QUO GATE | **PASS** |

---

## Composite Scores

| V | Baseline | C-35 | C-36 | **Total** | % | Golden |
|---|----------|------|------|-----------|---|--------|
| V-01 | 220 | +5 | +0 | **225** | 97.8% | YES |
| V-02 | 220 | +0 | +5 | **225** | 97.8% | YES |
| V-03 | 220 | +5 | +5 | **230** | 100% | YES |
| V-04 | 220 | +5 | +5 | **230** | 100% | YES |
| V-05 | 220 | +5 | +5 | **230** | 100% | YES |

All five variations pass all essential criteria (C-01–C-05). All five are Golden (≥184/230).

Scores match predicted outcomes exactly — all five predictions confirmed.

---

## Final Rankings

| Rank | Variation | Score | Tiebreak |
|------|-----------|-------|----------|
| 1 | **V-05** | 230/230 | Dual-surface C-35 + machine-countable C-36 — new excellence signals |
| 2 | **V-04** | 230/230 | Operations-first, cross-role inertia chain in B2 |
| 3 | **V-03** | 230/230 | Phrasing register isolation — register independence confirmed |
| 4 | V-01 | 225/230 | Clean C-36 ablation |
| 5 | V-02 | 225/230 | Clean C-35 ablation |

---

## Excellence Signals

**V-03 — Register Independence:** Both C-35 and C-36 hold under declarative register ("this section establishes...," "the boundary below marks..."). Criteria test artifact presence and position, not instruction word-form. The structural mechanisms are register-independent.

**V-04 — Cross-Role Inertia Chain:** Operations-first ordering produces an infrastructure-grounded STATUS QUO COST that generates richer three-part anchors for Commerce and Finance. B2 cross-role causal chain (Operations substrate → Commerce/Finance consequence) exceeds C-30's minimum — inertia framing that spans role boundaries creates dependency evidence no single-role section can produce.

**V-05 — Two New Excellence Signals:**

1. **PROTOCOL COUNT MANIFEST** — a named table at Phase B entry pre-commits all six boundary names, gate names, and gate states. C-35 becomes a two-surface test: header scan count AND manifest row count. A boundary present in headers but absent from the manifest (or vice versa) creates a cross-document inconsistency detectable at Phase B entry without inspecting phase bodies.

2. **COST LEDGER table format** — STATUS QUO COST expressed as a three-row table. C-36's three-part requirement is machine-countable: a table with fewer than three filled rows has a visible structural gap. Prose-form (V-02/V-03/V-04) satisfies C-36 but requires reading to verify; COST LEDGER makes completeness verifiable by row count alone.

**Ablation clarity (V-01, V-02):** The ablation pair confirms C-35 and C-36 are fully orthogonal. V-01 proves C-35 requires section-header format specifically — code-fence bilateral annotation (C-34) is necessary but not sufficient for C-35. V-02 proves C-36 requires pre-Q1 section positioning — Q1-embedded instruction satisfies C-27 but not C-36.

---

```json
{"top_score": 230, "all_essential_pass": true, "new_patterns": ["protocol-count-manifest-dual-surface-c35-verification", "cost-ledger-table-makes-three-part-inertia-machine-countable"]}
```
