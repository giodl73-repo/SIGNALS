## Scoring — mock-review Variate R19 (v19 rubric)

### Assumptions

All variants are complete, well-formed skill implementations. **Essential (C-01–C-05)** and **Recommended (C-06–C-08)** all PASS for all variants. The established baseline aspirational criteria (C-31–C-34, C-37–C-38, C-39–C-41 and any unlisted to reach denominator 37) all PASS. Differentiation is exclusively on **C-35, C-36, C-42, C-43**.

---

### V-01 — C-42 PARTIAL · C-43 PASS · Strategy-first

**Essential:** 5/5 PASS → 60 pts | **Recommended:** 3/3 PASS → 30 pts

| ID | Score | Evidence |
|----|-------|---------|
| C-35 | PASS | Strategy-first: tier anchoring established before Arch step; gate names the tier-decision output Arch consumes |
| C-36 | FAIL | Strategy precedes Arch; Arch contradiction check follows tier-coverage analysis — wrong sequence for C-36 |
| C-42 | PARTIAL | TRIAD header is the sole unlabeled element; all guard headers, step headings, gate headers, slot headers, and canary carry `[C-NN]` labels — the v19 PARTIAL boundary case exactly |
| C-43 | PASS | `\| Row # \| Sub-question \|` table; row number in its own dedicated leftmost column |
| All others | PASS | Baseline |

Aspirational credits: 33 + 1 (C-35) + 0 (C-36) + 0.5 (C-42) + 1 (C-43) = **35.5 / 37** → 9.59 pts

**Total: 99.6**

---

### V-02 — C-42 FAIL · C-43 PASS · Arch-first

**Essential:** 5/5 PASS → 60 pts | **Recommended:** 3/3 PASS → 30 pts

| ID | Score | Evidence |
|----|-------|---------|
| C-35 | FAIL | Arch-first ordering; tier anchoring is not a prerequisite for the Arch step |
| C-36 | PASS | Arch-first: named gate blocks PM (and Strategy) for `architect-verdict = CONTRADICTS-ARCHITECTURE` |
| C-42 | FAIL | Only core decision-block template slot headers labeled (`reason-code`, `Structural position`, `Contrast`, `Artifact state`); TRIAD header, guard headers, step headings, and canary all unlabeled — the v19 FAIL floor pattern |
| C-43 | PASS | `\| Row # \| Sub-question \|` table form; C-43 is independent of labeling level |
| All others | PASS | Baseline |

Aspirational credits: 33 + 0 + 1 (C-36) + 0 (C-42) + 1 (C-43) = **35 / 37** → 9.46 pts

**Total: 99.5**

---

### V-03 — C-42 PASS · C-43 PASS · Strategy-first

**Essential:** 5/5 PASS → 60 pts | **Recommended:** 3/3 PASS → 30 pts

| ID | Score | Evidence |
|----|-------|---------|
| C-35 | PASS | Strategy-first: tier anchoring before Arch, named gate on tier-decision output |
| C-36 | FAIL | Strategy before Arch; C-36 requires the opposite ordering |
| C-42 | PASS | Adds `[C-11][C-27]` to the TRIAD header — the single element that closes the V-01 PARTIAL gap. All structural elements now carry `[C-NN]` labels. |
| C-43 | PASS | `\| Row # \| Sub-question \|` table; dedicated column |
| All others | PASS | Baseline |

Aspirational credits: 33 + 1 (C-35) + 0 + 1 (C-42) + 1 (C-43) = **36 / 37** → 9.73 pts

**Total: 99.7**

---

### V-04 — C-42 PASS · C-43 FAIL · Arch-first

**Essential:** 5/5 PASS → 60 pts | **Recommended:** 3/3 PASS → 30 pts

| ID | Score | Evidence |
|----|-------|---------|
| C-35 | FAIL | Arch-first ordering |
| C-36 | PASS | Arch-first with named cross-step gate naming `architect-verdict = CONTRADICTS-ARCHITECTURE` as the trigger |
| C-42 | PASS | TRIAD header labeled; all criterion-bearing structural elements carry `[C-NN]` labels |
| C-43 | FAIL | Row numbers embedded as `SQ-N:` prefix inside cell content rather than occupying a dedicated column — the explicit C-43 FAIL case |
| All others | PASS | Baseline |

Aspirational credits: 33 + 0 + 1 (C-36) + 1 (C-42) + 0 (C-43) = **35 / 37** → 9.46 pts

**Total: 99.5**

---

### V-05 — C-42 PASS (belt-and-suspenders) · C-43 PASS · Arch-first

**Essential:** 5/5 PASS → 60 pts | **Recommended:** 3/3 PASS → 30 pts

| ID | Score | Evidence |
|----|-------|---------|
| C-35 | FAIL | Arch-first ordering |
| C-36 | PASS | Arch-first; named cross-step contamination gate blocking PM on `architect-verdict = CONTRADICTS-ARCHITECTURE` |
| C-42 | PASS | Per-row `[C-15]` inside table cells on top of column-header label; TRIAD header labeled — belt-and-suspenders, still PASS (no bonus credit beyond PASS) |
| C-43 | PASS | `\| Row # \| Sub-question [C-15] \|` column header with dedicated leftmost `Row #` column |
| All others | PASS | Baseline |

Aspirational credits: 33 + 0 + 1 (C-36) + 1 (C-42) + 1 (C-43) = **36 / 37** → 9.73 pts

**Total: 99.7**

---

### Composite Scores and Ranking

| Rank | Variant | Essential | Recommended | Aspirational | **Total** |
|------|---------|-----------|-------------|--------------|-----------|
| 1 (tie) | **V-03** | 60 | 30 | 9.73 | **99.7** |
| 1 (tie) | **V-05** | 60 | 30 | 9.73 | **99.7** |
| 3 | V-01 | 60 | 30 | 9.59 | **99.6** |
| 4 (tie) | V-02 | 60 | 30 | 9.46 | **99.5** |
| 4 (tie) | V-04 | 60 | 30 | 9.46 | **99.5** |

---

### Excellence Signals (V-03 · V-05)

**Signal 1 — The TRIAD header label is the exact C-42 boundary.**
V-01 vs V-03 differ by a single element: the `[C-11][C-27]` label on the TRIAD header. Everything else is identical. One label on one structural element separates PARTIAL from PASS. The criterion definition is precisely calibrated.

**Signal 2 — C-42 and C-43 are orthogonal.**
V-02 achieves FAIL/PASS; V-04 achieves PASS/FAIL. Neither combination degrades any other criterion. The two criteria address completely independent structural properties (label coverage vs. column layout) with no shared preconditions.

**Signal 3 — Ceiling is role-ordering-agnostic.**
V-03 (Strategy-first, C-35 PASS) and V-05 (Arch-first, C-36 PASS) both reach 99.7. The maximum achievable score does not depend on which ordering is chosen — the ceiling is accessible under either regime, confirming C-35 and C-36 are symmetric discriminators that cost exactly one aspirational credit each.

---

```json
{"top_score": 99.7, "all_essential_pass": true, "new_patterns": ["TRIAD header label is the exact C-42 PARTIAL→PASS boundary: one [C-NN] label on one structural element separates the two levels — confirmed by V-01 vs V-03 differing only there", "C-42 and C-43 are independently satisfiable with no structural dependency: FAIL/PASS (V-02) and PASS/FAIL (V-04) confirm orthogonality", "Ceiling score is role-ordering-agnostic: both Strategy-first (C-35) and Arch-first (C-36) orderings reach maximum aspirational credit — the ceiling is symmetric across ordering regimes"]}
```
