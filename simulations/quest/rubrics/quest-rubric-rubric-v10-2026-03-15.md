The scorecard cuts off at V-04. I have what I need from V-01 through V-03. Here is the complete v10 rubric.

---

```markdown
## quest-rubric Rubric v10

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/21 × 10)` — denominator /20 → /21

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

### Two criteria from Round 8 excellence signals (carried forward)

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

**Independence test (v9 open question — status: open):** ES-R8-3 notes that C-27 and C-28
were introduced as candidates for a single combined criterion. V-05's M-06 probe (boundary ×
dependency consistency check) tests whether quality-boundary ordering always entails
logical-dependency declarations and vice versa. R9 V-01 through V-03 all PASS both C-27 and
C-28 — no divergence observed. The question remains open: a probe where one passes and the
other fails is required to close it. Until that probe fires, v10 is correct to keep them split.

---

### One new criterion from Round 9 excellence signals

Targets **pre-declaration integrity** — the structural property that the PARTIAL-credit
boundary is committed before the Author Phase, not reconstructed during evaluation.

**C-29 — AUDITOR-PRE pre-declaration of PARTIAL-CONDITION boundary**
*(Candidate signal ES-R9-1, labeled C-35 in the R9 scorecard; assigned C-29 as next
sequential criterion.)*

Each criterion carries a named `### AUDITOR-PRE [C-NN]` block that declares the
PARTIAL-credit boundary *before* the Author Phase opens. This locks partial interpretation
at declaration time rather than evaluation time. Without pre-declaration, the PARTIAL-
CONDITION block required by C-23 loses its independent grounding anchor: evaluators must
reconstruct the boundary from PASS evidence alone, reintroducing subjective inference at
the boundary layer.

R9 V-01 PASSes C-23 because AUDITOR-PRE is present and its grounding chain is traceable
(lines 313–315). R9 V-02 and V-03 both FAIL C-23 for the same root cause: AUDITOR-PRE is
absent. V-02 finding: "Vocabulary is navigational; the grounding mechanism (AUDITOR-PRE) is
structural." V-03 finding: "the absence of AUDITOR-PRE leaves PARTIAL-CONDITION without an
independent anchor."

Note: C-29 is logically upstream of C-23 — a rubric can satisfy C-23 post-hoc (manually
grounded PARTIAL-CONDITION, no AUDITOR-PRE), but a rubric with C-29 gets C-23 for free.
C-23 remains a separate recommended criterion because it is satisfiable without C-29.

**v10 open question (M-07 probe):** Does AUDITOR-PRE consistently produce tighter
PARTIAL-CONDITION blocks than post-hoc review? If yes, the tighter-boundary property is a
structural guarantee not present in R8 V-05, and C-29 should be elevated to recommended
tier. Test: run matched-pair variations — one with AUDITOR-PRE, one with post-hoc
PARTIAL-CONDITION — and measure boundary specificity. V-01 through V-03 are consistent
with the claim but do not prove tighter specificity.

---

### Failure modes

| FM    | Name                                                              | Caught by |
|-------|-------------------------------------------------------------------|-----------|
| FM-01 | Missing essential criteria block                                  | C-01      |
| FM-02 | Uncalibrated partial credit                                       | C-10      |
| FM-03 | Reproduction drift (CM-NN identifiers not copied verbatim)        | C-22      |
| FM-04 | PARTIAL-CONDITION without independent grounding anchor            | C-29      |
```

---

**Changes from v9 to v10:**

- **Formula denominator:** `/20 → /21` (C-29 added to aspirational pool)
- **C-29 added** — AUDITOR-PRE pre-declaration block; aspirational tier; logically upstream of C-23
- **FM-04 added** — PARTIAL-CONDITION without independent grounding anchor, caught by C-29
- **v9 open question (M-06):** Status updated to "open — no divergence observed in R9, probe not yet fired"
- **v10 open question (M-07):** Does AUDITOR-PRE produce tighter PARTIAL-CONDITION specificity than post-hoc? Closes C-29's tier assignment
