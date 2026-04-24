```markdown
## quest-rubric Rubric v9

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/20 × 10)` — denominator /18 → /20

---

### Four criteria from Round 7 excellence signals (carried forward)

All four target **partial-credit integrity** — the structural property C-10 tests at the
formula level but not at the criterion level, the reproduction level, or the
inter-boundary semantic level.

**C-23 — Per-criterion PARTIAL-CONDITION block**
V-03 and V-05 demonstrate this. C-10 tells you PARTIAL = 0.5 in the formula; C-23 tells
you what evidence earns 0.5 for *this specific criterion*. Without it, evaluators interpret
partial credit subjectively — violating C-02 at the partial-credit boundary. V-01 and V-04
fail: `verdict_weights` in SA-1 but no per-criterion condition.

**C-24 — Formula consistency across structural positions**
V-02 fails: SA-1 is `essential_pass / N * 60` (binary); FINAL RUBRIC is the weighted form.
Two formula instances disagreeing on type leaves the governing formula ambiguous. V-03 gets
PARTIAL: binary SA-1 formula + prose note + expanded FINAL RUBRIC — intent aligned,
structure divergent.

**C-25 — FINAL RUBRIC anti-collapse formula guard** *(updated in v9 — SA-1 coupling removed)*
The guard was introduced in R7 as: "Reproduce the weighted formula from SA-1 verbatim —
do not collapse to binary counting." R8 exposed that this formulation silently drops the
reproduction mandate when SA-1 is absent (generalization probe). V9 form: **"Reproduce
this formula verbatim at every structural position where a formula appears — do not collapse
to binary counting."** Does not reference a specific prior phase; works when there is no
SA-1. V-04 satisfies the updated criterion (SA-1 present; guard fires correctly). Variations
produced without SA-1 must carry the guard independently.

**C-26 — VERDICT TIER DECLARATION inter-boundary block**
V-02, V-04, V-05 have a named block between `SPEC ANALYST: CLOSED` and `AUTHOR: OPEN`
defining PASS/PARTIAL/FAIL semantics. Evaluator-facing grounding, findable by structure.
V-01 and V-03 embed tier semantics only in SA-1 fields or formula comments.

---

### Two new criteria from Round 8 excellence signals

Both target **structural-scan detectability** — the property that a rubric's quality
guarantees are visible without reading criterion content.

**C-27 — Per-criterion DISCRIMINATES-BETWEEN block**
Each criterion carries a named block at the meta-description layer declaring quality
boundaries (FAILS-AT / PASSES-AT / Boundary). Distinct from CALIBRATION-PAIR content
examples (which show what evidence looks like) and REDUNDANCY-CHECK-TABLE outcome
independence (which tests scoring independence). The DISCRIMINATES-BETWEEN block is
structural: a rubric can be scanned for its presence without reading criterion content.
Absence forces evaluators to infer the boundary from examples alone, reintroducing
subjectivity at the boundary layer — the same failure mode C-23 closes at the
partial-credit boundary. V-03 introduces this pattern; V-05 carries it in full form.

**C-28 — Per-criterion DEPENDS_ON / INDEPENDENT dependency declaration**
Each criterion declares its logical prerequisites (`DEPENDS_ON: [C-NN, ...]`) or its
independence (`INDEPENDENT`). The Auditor section verifies prerequisite criteria pass before
scoring dependent criteria. Makes the dependency graph explicit and detectable by structural
scan. Without it, dependency violations are invisible — a PARTIAL on an upstream criterion
can infect downstream scoring without any audit signal. V-02 introduces the dependency
graph; V-05 carries the full per-criterion form with Auditor ordering verification.

**Independence test (v9 open question):** ES-R8-3 notes that C-27 and C-28 were introduced
as candidates for a single combined criterion. V-05's M-06 probe (boundary × dependency
consistency check) tests whether quality-boundary ordering always entails logical-dependency
declarations and vice versa. If they diverge in at least one case, v9 is correct to split
them. If they collapse, v10 should merge back to a single criterion. The M-06 probe makes
this question executable against future variations.

---

### Failure modes

| FM  | Name                                                              | Caught by |
|-----|-------------------------------------------------------------------|-----------|
| FM-01 | Missing essential criteria block                                | C-01      |
| FM-02 | Uncalibrated partial credit                                     | C-10      |
| FM-03 | Reproduction drift (CM-NN identifiers not copied verbatim)      | C-22      |
| FM-04 | Verdict tier semantics embedded only in prose                   | C-26      |
| FM-05 | Binary formula substituted for weighted form                    | C-24      |
| FM-06 | Redundancy-check table absent                                   | C-17      |
| FM-07 | No CALIBRATION-PAIR per criterion                               | C-19      |
| FM-08 | Auditor phase missing or structurally undetectable              | C-20      |
| FM-09 | Conflicting formula type across structural positions            | C-24      |
| FM-10 | Formula collapse at reproduction without guard                  | C-25      |
| FM-11 | Subjective partial-credit evaluation (no per-criterion condition) | C-23    |
| FM-12 | Floating tier semantics (no dedicated inter-boundary block)     | C-26      |
| FM-13 | Missing quality-boundary block at meta-description layer        | C-27      |
| FM-14 | Undeclared criterion dependency (no DEPENDS_ON / INDEPENDENT)   | C-28      |

---

### R8 Composite Scores under v9

C-25 updated (SA-1 coupling removed): V-04 satisfies the updated form (SA-1 present).
C-27 earned by V-03 and V-05. C-28 earned by V-02 and V-05. V-05 satisfies all 20.

| Variation | A/20      | Composite | Band   |
|-----------|-----------|-----------|--------|
| V-01      | 15/20     | 97.50     | Golden |
| V-02      | 16.5/20   | 98.25     | Golden |
| V-03      | 16.5/20   | 98.25     | Golden |
| V-04      | 17/20     | 98.50     | Golden |
| **V-05**  | **20/20** | **100.00**| **Golden** |

**Baseline: R8 V-05 = 100.00 / Golden. No entering gap for Round 9.**
All 20 aspirational criteria satisfied. Round 9 direction: execute the M-06
independence test — determine whether C-27 and C-28 hold as distinct criteria
under adversarial variation, or collapse into one.
```

---

Three changes from v8:

1. **Formula** — denominator /18 → /20 (two new aspirational criteria)
2. **C-25 updated** — "from SA-1 verbatim" → "at every structural position where a formula appears"; SA-1-free variations must carry the guard independently
3. **C-27 and C-28 added** — DISCRIMINATES-BETWEEN block and DEPENDS_ON/INDEPENDENT declaration, both targeting structural-scan detectability; FM-13 and FM-14 added accordingly
