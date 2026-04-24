Reading the scorecard to extract the three R10 excellence patterns before writing the updated rubric.

**R10 excellence signals:**

1. **V-05 on C-27 (PASS, only variation)** — PARTIAL-CREDIT MANIFEST table with dual columns (partial boundary + pass condition side-by-side) enables boundary-vs-pass-condition incoherence detection by structural scan without reading any criterion entry. V-01/V-04 registers carry partial boundary only — pass condition column absent, so incoherence is undetectable.

2. **V-04's C-29 implementation (strongest)** — batch register (phase-level) + inline AUDITOR-PRE block (per-criterion) simultaneously. REGISTER REVISION note required when a batch entry needs correction. Phase 4 reproduction check confirms inline blocks match register verbatim. Both enforcement positions active = structural redundancy guard.

3. **V-05's C-29 implementation (forward-then-verify)** — pre-declaration (AUDITOR-PRE blocks) → emitted artifact (PARTIAL-CREDIT MANIFEST) → Phase 4 manifest-row verification confirms emitted boundaries match inline blocks verbatim. C-29 closes the construction gate; V-05's pattern closes the reproduction gate.

**Independence test resolution:** R10 also closes the C-27/C-28 open question — V-05 PASSES C-27 (manifest satisfies boundary-scan detectability) and FAILS C-28 (no DEPENDS_ON declarations anywhere). One passes, the other fails — they are definitively independent criteria. Combined-criterion proposal rejected.

**Denominator:** /21 → /24 (three new criteria: C-30, C-31, C-32).

---

```markdown
## quest-rubric Rubric v11

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/24 × 10)` — denominator /21 → /24

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

**Independence test (v9 open question — status: CLOSED in R10):** ES-R8-3 noted that C-27
and C-28 were introduced as candidates for a single combined criterion. R10 closes the
question: V-05 PASSES C-27 (PARTIAL-CREDIT MANIFEST satisfies structural-scan boundary
detectability) and FAILS C-28 (no per-criterion DEPENDS_ON declarations in any R10
variation). A criterion can satisfy quality-boundary ordering without satisfying
logical-dependency declarations. C-27 and C-28 are definitively independent — the
combined-criterion proposal is rejected.

---

### One criterion from Round 9 excellence signals (carried forward)

Targets **pre-declaration integrity** — the structural property that the PARTIAL-credit
condition is locked in structurally before any Author phase begins, not constructed
post-hoc during evaluation.

**C-29 — AUDITOR-PRE per-criterion pre-declaration of PARTIAL-CONDITION boundary**
Each criterion carries a named AUDITOR-PRE block declaring the partial-credit boundary
before the pass condition, and a named phase gate (STOP CONDITION) prevents any Author
phase from opening until all AUDITOR-PRE declarations are complete. V-01 satisfies via
batch Pre-Declaration Register locked before Phase 2 opens. V-02 satisfies via
per-criterion AUDITOR-PRE block with STOP CONDITION at per-criterion boundary. V-03 gets
PARTIAL: sentence ordering satisfies observability without a named block or structural phase
gate (M-07 open — see below). V-04 satisfies via both paths simultaneously (see C-31).
V-05 satisfies via per-criterion gate plus emitted manifest with Phase 4 verification
(see C-32).

**Open question M-07 (status: open — R10):** V-03 uses a sentence anchor ("Partial credit
(0.5) applies when...") ordered before the pass condition, satisfying observability without
a named `AUDITOR-PRE [C-NN]:` block or phase-boundary STOP CONDITION. The question:
is the named-block structure load-bearing (prevents evaluator skip) or cosmetic (prose
sentence provides equivalent commitment)? A probe where V-03's approach produces a
boundary error that V-02's STOP CONDITION would have caught is required to close this
question.

---

### Three new criteria from Round 10 excellence signals

All three target **verification completeness** — the structural property that pre-declared
partial-credit boundaries are not only gated before Phase 2 opens (C-29) but also
reproduced faithfully in the emitted document and verified closed in Phase 4.

**C-30 — PARTIAL-CREDIT MANIFEST: dual-column partial boundary × pass condition table**
A dedicated table in the emitted document covers all aspirational criteria with columns:
C-NN | Partial boundary | Pass condition. An evaluator can detect boundary-vs-pass-condition
incoherence by structural scan alone — both conditions are visible side-by-side without
reading any criterion entry. V-05 introduces and satisfies this in R10. V-01 and V-04 carry
a pre-declaration register with a partial boundary column only; the incoherence between
partial and full credit is not visually detectable from the register alone, because the pass
condition column is absent. C-27 can be satisfied by per-criterion inline blocks (structurally
present but not cross-criterion scannable); C-30 requires a consolidated cross-criterion
table carrying both conditions simultaneously. PARTIAL: manifest present but pass condition
column missing or covering fewer than all tiers.

**C-31 — Dual-path AUDITOR-PRE: phase-level batch register + per-criterion inline block simultaneously**
The phase-level batch register (C-29 V-01 path) and the per-criterion inline AUDITOR-PRE
block (C-29 V-02 path) are both active simultaneously. A REGISTER REVISION note is required
when a batch entry needs correction at construction time. Phase 4 includes a reproduction
check confirming that every inline block matches its corresponding register entry verbatim.
Neither enforcement position alone satisfies C-31 — both must be active, creating a
structural redundancy guard that prevents a partial-condition boundary from being skipped if
one position is absent or bypassed. V-04 introduces and satisfies this in R10 (strongest
C-29 implementation). C-29 is satisfied by either path alone; C-31 requires both paths
simultaneously. PARTIAL: one path present and the other referenced but not structurally
enforced (e.g., register exists without per-criterion inline blocks, or vice versa).

**C-32 — Forward-then-verify loop: pre-declaration → emitted artifact → Phase 4 manifest verification**
Partial boundaries pre-declared before Phase 2 (via AUDITOR-PRE blocks, satisfying C-29)
are also emitted into the output document as a named artifact (e.g., PARTIAL-CREDIT
MANIFEST), and Phase 4 includes an explicit manifest-row verification step confirming that
every emitted boundary matches its corresponding pre-declared block verbatim. Creates a
closed verification loop: the pre-declaration gate (C-29) prevents construction-time
omission; the emitted artifact creates a document-level permanent record; the Phase 4
verification step confirms reproduction fidelity. V-05 introduces and satisfies this in R10
(forward-then-verify architecture). C-29 alone leaves reproduction fidelity unverified after
Phase 2 closes; C-32 requires the verification loop to complete in Phase 4. PARTIAL: emitted
manifest present but Phase 4 verification step absent or covers fewer than all criteria.
```
