**validate-inertia R17 — scored. Written to `validate-inertia-scorecard-R17-2026-03-17.md`.**

---

## Results: V-81 through V-85

| Variation | C-45 | C-46 | Score | Predicted | Match |
|-----------|------|------|-------|-----------|-------|
| V-81 (ceiling) | PASS (10) | PASS (10) | **460/460** | 460 | YES |
| V-82 (C-46 partial) | PASS (10) | PARTIAL (5) | **455/460** | 455 | YES |
| V-83 (C-45 partial, both-named) | PARTIAL (5) | PASS (10) | **455/460** | 455 | YES |
| V-84 (no non-propagation) | PASS (10) | FAIL (0) | **450/460** | 450 | YES |
| V-85 (one function, both directions) | PARTIAL (5) | PASS (10) | **455/460** | 450 | **NO** |

**4/5 match.**

---

**V-85 mismatch — C-45 PARTIAL, not FAIL.**

The variation predicted C-45 FAIL (0) and score 450. The rubric is unambiguous: "A block body that names the self-documenting function without the self-enforcing function earns PARTIAL." V-85 names the self-documenting function explicitly. FAIL requires neither function named. Score by rubric: 455.

This collapses the designed 455-pair + 450-pair into a **455-triple** (V-82, V-83, V-85) with only V-84 at 450. Three distinct structural paths all earn 455:
- V-82: PASS+PARTIAL (duality complete, one independence direction missing)
- V-83: PARTIAL+PASS (both named, distinctness absent)
- V-85: PARTIAL+PASS (one named, other absent — different C-45 partial shape)

**V-84 remains the unique 450 proof** that C-45 PASS does not imply C-46 PASS.

**R18 gap identified:** No variation achieves genuine C-45 FAIL (0 pts). A block body naming *neither* closure function while satisfying C-46 would be the missing shape.

```json
{"top_score": 460, "all_essential_pass": true, "new_patterns": ["C-45 PARTIAL has two structurally distinct paths: both-named-not-distinct (V-83) and one-named-not-other (V-85) -- rubric assigns PARTIAL to both, producing a 455-triple rather than the designed 455-pair+450-pair", "V-85 prediction error: rubric assigns C-45 PARTIAL (not FAIL) when one function is named without the other -- FAIL requires neither function named; V-85 scores 455 not 450", "C-46 satisfiable without duality vocabulary: V-85 passes C-46 using functional criterion descriptions rather than duality labels -- bidirectionality is the requirement, not use of the self-documenting/self-enforcing names", "V-84 is the unique 450 variation and sole proof that C-45 PASS does not imply C-46 PASS -- duality naming does not discharge independence declaration"]}
```
55-pair+450-pair", "V-85 prediction error: rubric assigns C-45 PARTIAL (not FAIL) when one function is named without the other -- FAIL requires neither function named; V-85 scores 455 not 450", "C-46 satisfiable without duality vocabulary: V-85 passes C-46 using functional criterion descriptions rather than duality labels -- bidirectionality is the requirement, not use of the self-documenting/self-enforcing names", "V-84 is the unique 450 variation and sole proof that C-45 PASS does not imply C-46 PASS -- duality naming does not discharge independence declaration"]}
```

---

## V-81: Ceiling -- C-45 PASS + C-46 PASS (460/460)

**C-45 examination:**
Block body names both closure functions with explicit "structurally distinct roles" framing:
"The gate architecture closure has two functions serving structurally distinct roles. The produced
architecture label... serves a self-documenting function... The block instruction body serves a
self-enforcing function... These are structurally distinct roles -- the self-documenting label
function certifies that the block body declared the constraints; the self-enforcing block body
function enforces compliance by making the prohibitions present before execution."
Both functions named. Structural distinctness declared. Neither can collapse into the other.

**C-46 examination:**
Non-propagation paragraph declares both directions:
1. "Satisfying the produced-label certification requirement (C-43:...) does not discharge the
   split-gate prohibition requirement (C-44:...)" -- C-43 does not imply C-44.
2. "Satisfying the split-gate prohibition requirement (C-44:...) does not discharge the
   produced-label certification requirement (C-43:...)" -- C-44 does not imply C-43.
Both directions present.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-44 | PASS (440) | V-76 baseline held constant |
| C-45 | **PASS (10)** | Both functions named with "structurally distinct roles" framing; neither can collapse into the other |
| C-46 | **PASS (10)** | Both non-propagation directions declared: C-43 does not discharge C-44; C-44 does not discharge C-43 |

**Score: 460/460. Prediction confirmed.**

---

## V-82: C-46 PARTIAL -- Mirror Non-Propagation Direction Omitted (455/460)

**C-45 examination:**
Duality paragraph identical to V-81 -- both functions named with "structurally distinct roles"
framing. C-45 PASS.

**C-46 examination:**
Non-propagation paragraph declares only one direction:
"Satisfying the produced-label certification requirement (C-43:...) does not discharge the
split-gate prohibition requirement (C-44:...)" -- direction present.
Mirror direction ("C-44 does not discharge C-43") absent.
Rubric: "Declaring one direction of non-propagation without its mirror earns PARTIAL."

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-44 | PASS (440) | V-76 baseline |
| C-45 | **PASS (10)** | Identical to V-81: both functions, structurally distinct declared |
| C-46 | **PARTIAL (5)** | One direction only: "C-43 does not discharge C-44" -- mirror "C-44 does not discharge C-43" absent |

**Score: 455/460. Prediction confirmed.**

---

## V-83: C-45 PARTIAL -- Both Functions Named, Not Declared Structurally Distinct (455/460)

**C-45 examination:**
Block body duality paragraph names both functions:
"The gate architecture closure has two functions. The produced architecture label... serves a
self-documenting function... The block instruction body serves a self-enforcing function..."
Both functions present. "Structurally distinct roles" framing is absent -- no declaration that
these are distinct roles serving different purposes, no statement that one cannot discharge the
other.
Rubric: "A block body that names both functions without declaring them as structurally distinct
roles earns PARTIAL."

**C-46 examination:**
Non-propagation paragraph declares both directions:
"C-43:... does not discharge the split-gate prohibition requirement (C-44:...)"
"C-44:... does not discharge the produced-label certification requirement (C-43:...)"
Both directions present. C-46 PASS.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-44 | PASS (440) | V-76 baseline |
| C-45 | **PARTIAL (5)** | Both functions named ("self-documenting," "self-enforcing") but no "structurally distinct roles" framing -- no declaration that neither discharges the other |
| C-46 | **PASS (10)** | Both directions: "C-43 does not discharge C-44" and "C-44 does not discharge C-43" both present |

**Score: 455/460. Prediction confirmed.**

**V-82 vs V-83 structural differentiation:**
V-82 PARTIAL axis: C-46 -- non-propagation paragraph missing mirror direction.
V-83 PARTIAL axis: C-45 -- duality paragraph missing structural distinctness declaration.
Both score 455. Rubric discriminates by locating the failure: closure-vocabulary level (C-45)
vs. non-propagation completeness level (C-46).

---

## V-84: C-45 PASS + C-46 FAIL -- Duality Declared, No Non-Propagation (450/460)

**C-45 examination:**
Block body duality paragraph identical to V-81 -- both functions named with "structurally distinct
roles" framing:
"The gate architecture closure has two functions serving structurally distinct roles..."
"These are structurally distinct roles -- the self-documenting label function certifies that the
block body declared the constraints; the self-enforcing block body function enforces compliance..."
C-45 PASS.

**C-46 examination:**
No non-propagation paragraph of any kind. After the C-45 duality paragraph, block body closes
with a horizontal rule and moves to the exact-copy rule. Neither direction of non-propagation
("C-43 does not discharge C-44" or "C-44 does not discharge C-43") appears anywhere in the
block body. Zero directions declared.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-44 | PASS (440) | V-76 baseline |
| C-45 | **PASS (10)** | Identical to V-81: "structurally distinct roles" framing, both functions named |
| C-46 | **FAIL (0)** | No non-propagation language of any kind -- neither direction declared |

**Score: 450/460. Prediction confirmed.**

**V-84 critical proof:** C-45 PASS does not imply C-46 PASS. Naming the gate closure as a
duality of structurally distinct roles does not discharge the requirement to explicitly declare
the non-propagation between C-43 and C-44. V-84 is the only variation at 450 and the definitive
test for this independence.

---

## V-85: C-45 PARTIAL + C-46 PASS -- One Function Named, Both Non-Propagation Directions (455/460)

**C-45 examination:**
Block body duality paragraph names ONLY the self-documenting function:
"The produced architecture label (the 'CITATION ARCHITECTURE DECLARED' label required below)
serves a self-documenting function: it certifies that the block instruction body named all three
axes by label and declared partial axis coverage a gate failure."
The self-enforcing block body function is never named. Block body proceeds directly to
non-propagation language.
Rubric C-45 pass condition: "A block body that names the self-documenting function without the
self-enforcing function earns PARTIAL."
C-45 PARTIAL (5).

**Prediction discrepancy:** Variation design labeled this C-45 FAIL (0 pts) and predicted 450.
The rubric is unambiguous: naming one function without the other earns PARTIAL, not FAIL. FAIL
applies when neither function is named. V-85 names the self-documenting function explicitly.
The variation designer's annotation ("naming only one of the two structural roles earns FAIL")
does not match the rubric pass condition. Score per rubric: PARTIAL (5 pts). Actual: 455.

**C-46 examination:**
Non-propagation paragraph declares both directions using functional criterion descriptions
(without using duality labels "self-documenting" / "self-enforcing"):
1. "Satisfying the produced-label certification requirement (the produced architecture label cites
   the block instruction body as the explicit source of both gate components...) does not discharge
   the split-gate prohibition requirement (the block instruction body names both split-gate failure
   modes...)" -- direction: label-certification does not imply block-prohibition.
2. "Satisfying the split-gate prohibition requirement (the block instruction body names both
   split-gate disqualifiers) does not discharge the produced-label certification requirement (the
   produced architecture label cites the block body as the source of both gate components)."
   -- mirror direction.
Both directions present. C-46 rubric requires bidirectionality, not duality vocabulary. C-46 PASS.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-44 | PASS (440) | V-76 baseline |
| C-45 | **PARTIAL (5)** | Self-documenting function named; self-enforcing function not named -- rubric assigns PARTIAL for naming one without the other |
| C-46 | **PASS (10)** | Both directions declared via criterion descriptions: label-cert does not discharge block-prohibition; block-prohibition does not discharge label-cert |

**Score: 455/460. Prediction: 450. MISMATCH.**

**V-85 vs V-83 (both 455, both C-45 PARTIAL + C-46 PASS):**
V-83 PARTIAL shape: both functions named but structural distinctness declaration absent.
V-85 PARTIAL shape: only one function named (self-documenting present; self-enforcing absent).
Same score. Different structural diagnosis within C-45.

**V-85 C-46 pattern:** Satisfies C-46 without ever using the duality vocabulary. Non-propagation
declared through full functional descriptions of each criterion rather than their duality labels.
Confirms that C-46 is a bidirectionality requirement, not a vocabulary requirement.

---

## Summary Table

| Variation | C-01--C-44 | C-45 | C-46 | Total | Predicted | Match |
|-----------|-----------|------|------|-------|-----------|-------|
| V-81 (ceiling) | 440 | PASS (10) | PASS (10) | **460** | 460 | YES |
| V-82 (C-46 partial) | 440 | PASS (10) | PARTIAL (5) | **455** | 455 | YES |
| V-83 (C-45 partial, both-named) | 440 | PARTIAL (5) | PASS (10) | **455** | 455 | YES |
| V-84 (no non-propagation) | 440 | PASS (10) | FAIL (0) | **450** | 450 | YES |
| V-85 (one function, both directions) | 440 | PARTIAL (5) | PASS (10) | **455** | 450 | **NO** |

**4/5 match. 1 mismatch (V-85: rubric gives 455 vs. predicted 450).**

---

## Excellence Signals

**V-81 ceiling -- C-45+C-46 conjunction required:**
V-81 achieves 460 by combining full duality declaration (both functions, structurally distinct)
with full bidirectional non-propagation. The ceiling requires both independently: C-45 naming
the duality is necessary but not sufficient (V-84: C-45 PASS + C-46 FAIL = 450); C-46 declaring
independence is necessary but not sufficient (V-82: C-45 PASS + C-46 PARTIAL = 455; V-85:
C-45 PARTIAL + C-46 PASS = 455). Only the full conjunction earns 460.

**455-triple pattern (V-82, V-83, V-85):**
Three distinct structural paths converge at 455 via different criterion combinations:
- V-82: PASS+PARTIAL (duality complete, one independence direction missing)
- V-83: PARTIAL+PASS (both named, distinctness absent, both independence directions present)
- V-85: PARTIAL+PASS (one named, other absent, both independence directions present)
The rubric assigns the same PARTIAL to two distinct C-45 failure shapes (V-83 and V-85),
producing a 455-triple. Failure-mode attribution remains possible at equal totals by reading
which C-45 shape failed.

**Rubric correction surface -- C-45 FAIL condition:**
No R17 variation achieves genuine C-45 FAIL. The rubric's two PARTIAL conditions cover all
one-function and both-named-not-distinct cases. A variation targeting C-45 FAIL (0 pts) would
need a block body where neither closure function is named -- no "self-documenting function"
and no "self-enforcing function" language. V-85 was designed as the FAIL case but reaches
PARTIAL because the self-documenting function is named. R18 could target this gap with a
variation naming neither function while satisfying C-46 independently.
