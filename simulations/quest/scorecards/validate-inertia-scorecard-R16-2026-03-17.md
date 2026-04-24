**validate-inertia R16 — scored. Written to `validate-inertia-scorecard-R16-2026-03-17.md`.**

---

## Results: V-76 through V-80

| Variation | C-43 | C-44 | Score | Match |
|-----------|------|------|-------|-------|
| V-76 (ceiling) | PASS (10) | PASS (10) | **440/440** | YES |
| V-77 (C-44 partial) | PASS (10) | PARTIAL (5) | **435/440** | YES |
| V-78 (C-43 partial) | PARTIAL (5) | PASS (10) | **435/440** | YES |
| V-79 (C-43 fail) | FAIL (0) | PASS (10) | **430/440** | YES |
| V-80 (V-71 re-run) | PASS (10) | FAIL (0) | **430/440** | YES |

**5/5 predictions confirmed.**

---

**Key findings:**

- **C-43/C-44 closure pair confirmed.** C-43 (label certifies where gate components live) and C-44 (block body prohibits split-gate displacement) are structurally complementary but genuinely independent. V-79 earns C-44 PASS with C-43 FAIL; V-80 earns C-43 PASS with C-44 FAIL — the criteria do not propagate.

- **435 twin pair discriminated correctly.** V-77 fails C-44 (mirror disqualifier missing in block body); V-78 fails C-43 (axis enumeration provenance missing in label). Same total, different structural diagnosis — the rubric localizes the failure to block body level vs. label level.

- **430 complementary inversion discriminated correctly.** V-79 strips label provenance but adds block-body disqualifiers; V-80 keeps label provenance (V-71 shape) but lacks block-body disqualifiers. Primary C-43 vs. C-44 discrimination test for R16.

- **V-80 re-run confirms:** C-42 PASS (both components in block body) does not imply C-44 PASS — having the components present without naming the split-gate shapes as disqualifiers scores C-44 FAIL, not PARTIAL. Zero named = FAIL.

```json
{"top_score": 440, "all_essential_pass": true, "new_patterns": ["C-43+C-44 closure pair: C-43 (label certifies placement) + C-44 (block body prohibits displacement) form self-documenting and self-enforcing gate architecture", "C-43 and C-44 are genuinely independent: label-level and block-body-level failures do not propagate to each other", "435 twin pair: same score via structurally distinct PARTIAL shapes on different axes -- failure-mode attribution persists at equal totals", "430 complementary inversion: same total with opposite failure axes -- rubric discriminates by reading which criterion failed"]}
```
 prohibition language for both shapes.

---

## V-76: Ceiling -- C-43 PASS + C-44 PASS (440/440)

**Block body (C-44 examination):**
Both split-gate disqualifiers explicitly named in the block instruction body:
1. "A block gate instruction body that names all three axes in this block body but displaces
   the impossibility statement exclusively to the produced architecture label is a split-gate
   failure and fails this gate."
2. "A block gate instruction body that declares the impossibility statement in this block body
   but displaces axis enumeration exclusively to the produced architecture label is the mirror
   split-gate failure and also fails this gate."
Also: "Both split-gate configurations are named disqualifiers" and "Displacing either component
exclusively to the produced architecture label fails this gate regardless of which component
is displaced."

**Produced label (C-43 examination):**
Unchanged from V-71: "The block gate instruction in the block body names all three axes by
label and declares partial axis coverage a gate failure."
Cites block body as source of BOTH: axis enumeration ("names all three axes by label") AND
impossibility statement ("declares partial axis coverage a gate failure").

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-42 | PASS (420) | Identical V-71 baseline |
| C-43 | **PASS (10)** | Label "The block gate instruction in the block body names all three axes by label and declares partial axis coverage a gate failure" cites block body as source of axis enumeration ("names all three axes by label") AND impossibility statement ("declares partial axis coverage a gate failure"). Both components have block-body provenance. |
| C-44 | **PASS (10)** | Block body names both split-gate failure modes: axis-body/impossibility-label shape ("a split-gate failure and fails this gate"); impossibility-body/axis-label shape ("the mirror split-gate failure and also fails this gate"). Both shapes present in block instruction body at read time. |

**Score: 440/440. Prediction confirmed.**

---

## V-77: C-44 PARTIAL -- One Split-Gate Shape Named, Mirror Omitted (435/440)

**Block body (C-44 examination):**
Only ONE split-gate disqualifier in the block instruction body:
- "A block gate instruction body that names all three axes in this block body but displaces
  the impossibility statement exclusively to the produced architecture label is a split-gate
  failure and fails this gate."
The mirror shape (impossibility-body/axis-label) is absent. Block body ends at "All three
axes must be declared before Phase 1 begins" with no mirror disqualifier sentence.

**Produced label (C-43 examination):**
Identical to V-76/V-71: "The block gate instruction in the block body names all three axes
by label and declares partial axis coverage a gate failure." C-43 PASS.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-42 | PASS (420) | Identical V-71 baseline |
| C-43 | **PASS (10)** | Label identical to V-76: "The block gate instruction in the block body names all three axes by label and declares partial axis coverage a gate failure." Both axis enumeration and impossibility statement attributed to block body. |
| C-44 | **PARTIAL (5)** | Block body names the axis-body/impossibility-label shape ("displaces the impossibility statement exclusively to the produced architecture label is a split-gate failure") but omits the mirror shape (impossibility-body/axis-label). C-44 requires both named; naming one earns PARTIAL. |

**Score: 435/440. Prediction confirmed.**

**Structural diagnosis:** V-77 and V-78 are the 435 twin pair -- both score 435 through
different partial shapes on different criteria axes. V-77 fails C-44 (mirror missing in
block body); V-78 fails C-43 (axis enumeration missing in label provenance). The rubric
assigns PARTIAL via two structurally distinct diagnoses.

---

## V-78: C-43 PARTIAL -- Label Cites Source of One Gate Component Only (435/440)

**Block body (C-44 examination):**
Both split-gate disqualifiers present -- identical to V-76. C-44 PASS.

**Produced label (C-43 examination):**
Modified to a two-sentence form:
Sentence 1: "The block gate instruction in the block body declares partial axis coverage a
gate failure." -- cites block body as source of impossibility statement (one component cited).
Sentence 2: "The three required axes -- Axis 1 (duality framing), Axis 2 (audit format), and
Axis 3 (derivation direction) -- must all be declared before Phase 1 may begin." -- lists all
three axes without "in the block body" attribution.

C-43 PARTIAL shape: impossibility-statement provenance cited; axis-enumeration provenance uncited.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-42 | PASS (420) | Identical V-71 baseline |
| C-43 | **PARTIAL (5)** | Label attributes impossibility statement to block body ("in the block body declares partial axis coverage a gate failure") but states axis enumeration ("The three required axes...") without citing block body as named source. One component provenance certified; one uncited. C-43 requires both cited. |
| C-44 | **PASS (10)** | Block body contains both split-gate disqualifiers identical to V-76. Both failure mode shapes named at read time. |

**Score: 435/440. Prediction confirmed.**

**V-77 vs V-78 differentiation:**
V-77 PARTIAL axis: C-44 -- block body misses mirror disqualifier sentence.
V-78 PARTIAL axis: C-43 -- label misses block-body attribution for axis enumeration.
Both score 435. The rubric discriminates by locating the failure: block body level vs. label level.

---

## V-79: C-43 FAIL -- Label Names Artifact Without Block Body Provenance (430/440)

**Block body (C-44 examination):**
Both split-gate disqualifiers present -- identical to V-76 and V-78. C-44 PASS.

**Produced label (C-43 examination):**
"...the AUDIT ARCHITECTURE DECLARED block with three co-resident axes (Axis 1: duality
framing, Axis 2: audit format, Axis 3: derivation direction). All three axes are required
before Phase 1; partial axis coverage fails the gate."

Names the artifact and describes its content correctly -- but contains no "in the block body"
phrase or equivalent attribution linking either gate component to the block instruction body
as its source. No placement receipt for either component. C-43 FAIL.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-42 | PASS (420) | Identical V-71 baseline |
| C-43 | **FAIL (0)** | Label states "All three axes are required before Phase 1; partial axis coverage fails the gate" -- names artifact and requirement correctly but contains no citation of block body as source of axis enumeration or impossibility statement. No placement receipt. C-43 pass requires "the block body" (or equivalent) as explicit provenance for BOTH components; label provides provenance for neither. |
| C-44 | **PASS (10)** | Block body contains both split-gate disqualifiers identical to V-76/V-78. C-44 PASS unaffected by label content. |

**Score: 430/440. Prediction confirmed.**

**V-79 vs V-80 complementary inversion:**
V-79: C-43 FAIL + C-44 PASS = 430. Label strips provenance; block body adds disqualifiers.
V-80: C-43 PASS + C-44 FAIL = 430. Label has provenance (V-71 shape); block body lacks disqualifiers.
Same total, opposite failure axis. Primary C-43 vs. C-44 discrimination tests for R16.

---

## V-80: C-43 PASS, C-44 FAIL -- V-71 Shape Re-Confirmed Under v16 (430/440)

**Block body (C-44 examination):**
Structurally identical to V-71 (R15 ceiling). Block instruction body ends at:
"Partial axis coverage is not partial compliance -- it is a gate failure. All three axes must
be declared before Phase 1 begins."
No split-gate disqualifier sentences. Neither shape is named. C-44 FAIL -- both gate components
present in block body (C-42 PASS holds) but neither split-gate configuration named as a
disqualifier. Zero named = FAIL, not PARTIAL (PARTIAL requires at least one named).

**Produced label (C-43 examination):**
Identical to V-71: "The block gate instruction in the block body names all three axes by
label and declares partial axis coverage a gate failure." C-43 PASS unchanged.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-42 | PASS (420) | V-71 shape: both gate components in block body, no split |
| C-43 | **PASS (10)** | Label identical to V-71 ceiling: "The block gate instruction in the block body names all three axes by label and declares partial axis coverage a gate failure." Provides provenance receipt for both components -- same sentence that motivated C-43 criterion extraction from V-71. |
| C-44 | **FAIL (0)** | Block body contains both gate components (C-42 PASS) but names neither split-gate configuration as a disqualifier. C-44 requires explicit read-time prohibition language for both failure modes. V-71 shape has none. C-42 PASS does not imply C-44 PASS. |

**Score: 430/440. Prediction confirmed.**

**V-80 verification purpose:** Confirms (a) C-43 PASS in V-71's label holds under v16 --
the placement receipt sentence is sufficient; (b) having both gate components in the block
body (C-42 PASS) without naming either split-gate shape earns C-44 FAIL, not PARTIAL.

---

## Summary Table

| Variation | C-01--C-42 | C-43 | C-44 | Total | Predicted | Match |
|-----------|-----------|------|------|-------|-----------|-------|
| V-76 (ceiling) | 420 | PASS (10) | PASS (10) | **440** | 440 | YES |
| V-77 (C-44 partial) | 420 | PASS (10) | PARTIAL (5) | **435** | 435 | YES |
| V-78 (C-43 partial) | 420 | PARTIAL (5) | PASS (10) | **435** | 435 | YES |
| V-79 (C-43 fail) | 420 | FAIL (0) | PASS (10) | **430** | 430 | YES |
| V-80 (V-71 re-run) | 420 | PASS (10) | FAIL (0) | **430** | 430 | YES |

**All five predictions confirmed. 5/5 match.**

---

## Excellence Signals

**V-76 ceiling -- C-43/C-44 closure pair:**
C-43 requires the label to CERTIFY placement (provenance receipt: label documents where
components live). C-44 requires the block body to PROHIBIT displacement (self-rejection:
block body names split-gate shapes as disqualifiers at read time). Together the gate
architecture is self-documenting (label proves placement) and self-enforcing (block body
disqualifies split attempts). V-71 achieved C-43 implicitly; V-76 makes C-44 explicit
and closes the pair.

**Criterion independence confirmed:**
C-43 and C-44 are genuinely independent -- label-level and block-body-level failures do not
propagate to the other criterion. V-79 earns C-44 PASS with C-43 FAIL; V-80 earns C-43 PASS
with C-44 FAIL.

**435 twin pair discrimination:**
V-77 and V-78 score identically (435) through structurally distinct partial shapes:
V-77 PARTIAL at C-44 (block body omits mirror disqualifier); V-78 PARTIAL at C-43 (label
omits block-body attribution for axis enumeration). The richer criterion structure enables
failure-mode attribution at equal total scores.

**430 complementary inversion:**
V-79 (C-43 FAIL + C-44 PASS) and V-80 (C-43 PASS + C-44 FAIL) score identically (430)
with opposite failure axes. The rubric discriminates by reading which criterion failed, not
just the sum.

---

```json
{"top_score": 440, "all_essential_pass": true, "new_patterns": ["C-43+C-44 closure pair: C-43 (label certifies placement) + C-44 (block body prohibits displacement) form self-documenting and self-enforcing gate architecture", "C-43 and C-44 are genuinely independent: label-level and block-body-level failures do not propagate to each other", "435 twin pair: same score assigned via structurally distinct PARTIAL shapes on different criteria axes -- failure-mode attribution persists at equal totals", "430 complementary inversion: same total with opposite failure axes -- rubric discriminates by reading which criterion failed"]}
```