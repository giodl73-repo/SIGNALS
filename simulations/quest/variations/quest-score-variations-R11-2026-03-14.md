Written to `simulations/quest/rubrics/quest-score-rubric-v11-variations-R11-2026-03-15.md`.

---

## R11 Design Summary

**Five complete variations targeting C-28 and C-29 exclusively.**

### Variation axes

| V | Axis | Hypothesis | Expected verdicts |
|---|------|------------|-------------------|
| V-01 | Baseline -- R11 full stack | N_aspirational=22, 29-row roster, trigger-ID cascade ("C-07 auto-PASS fires"), Variation col 4 | C-28 PASS, C-29 PASS → 100.00 |
| V-02 | **Output format** -- regression table column order | Variation appended col 5 after Mechanism (Criterion\|Prior\|Current\|**Mechanism\|Variation**) | C-27 PASS, C-28 PARTIAL → 99.77 |
| V-03 | **Phrasing register** -- cascade declaration form | "C-28 auto-PASS when no prior-round data is available" (condition, not trigger ID) | C-29 PARTIAL → 99.77 |
| V-04 | **Lifecycle emphasis** -- auto-PASS block omits cascade entry | C-28 declaration entirely absent; C-29 auto-PASS present | C-11 FAIL + C-29 FAIL → 99.09 |
| V-05 | **V-02 × V-03 combination** | Col 5 regression + condition-not-trigger-ID cascade | C-28 PARTIAL + C-29 PARTIAL → 99.55 |

### Key structural decisions

**C-28 evidence ladder:** V-02 PARTIAL (col 5) → V-05 PARTIAL (col 5) → V-01 PASS (col 4)

**C-29 evidence ladder:** V-04 FAIL (absent) → V-03 PARTIAL (condition) → V-05 PARTIAL (condition) → V-01 PASS (trigger ID named)

**V-04 controlled co-failure:** removing the C-28 cascade declaration causes C-11 FAIL + C-29 FAIL simultaneously -- one structural decision, two correlated verdicts, labeled transparently in the axis. This mirrors R10's design where C-27 PARTIAL and C-28 FAIL co-fired from a single column-removal decision.

**C-07 cascade note in V-01/V-02:** updated to "C-27 and C-28 also auto-PASS" (vs. R10's "C-27 also auto-PASS") -- the expanded cascade chain is now explicit in the C-07 declaration.

**Three-scale diagnostic questions for C-28 and C-29** added to all 5 rosters, with FAIL/PARTIAL/PASS contrasting examples using actual column-order text and actual declaration text as examples.
