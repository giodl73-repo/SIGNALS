Now I have everything needed. Scoring R15 in full.

---

## /quest:score — validate-inertia R15 (V-71 through V-75)

### Scoring Context

All five variations share the V-66/V-71 baseline for C-01 through C-39: identical phases, CCV, and AMEND. The only axis of variation is the AUDIT ARCHITECTURE DECLARED block gate condition — specifically which gate components (axis enumeration, impossibility statement) reside in the block instruction body vs. the produced architecture label. C-01–C-39 = **390 pts** for all five.

C-40, C-41, and C-42 are the differentiating criteria (10 pts each; 5 pts for PARTIAL).

---

### Criterion Reference — C-40, C-41, C-42

**C-40 PASS:** Gate condition in the block instruction names all three axes by label AND declares partial satisfaction a gate failure.

**C-40 PARTIAL (three conditions):**
1. Gate names fewer than three axes
2. Gate declares partial satisfaction invalid but names no individual axes
3. Gate names all three axes with no partial-failure declaration (the V-68/V-72 shape)

**C-41 PASS:** Full C-40 gate (axis enumeration + impossibility statement) in the block instruction body.

**C-41 PARTIAL:** Per-axis gate present only in the produced architecture label (named condition); OR split shape (mirror V-73) per v15 revision.

**C-41 FAIL:** Neither the named PARTIAL nor split mirror shape.

**C-42 Verdict table (from v15 rubric):**

| Shape | C-41 | C-42 |
|-------|------|------|
| Both in block body (V-71, V-75) | PASS | PASS |
| Axes in body, impossibility in label (V-72) | PARTIAL | PARTIAL |
| Impossibility in body, axes in label — mirror (V-73) | PARTIAL | PARTIAL |
| Both in produced label only (V-74) | PARTIAL (named) | FAIL |

---

### Prediction Table Discrepancy

The variations file contains two sets of predictions that contradict each other:

| Source | V-72 | V-73 | V-74 |
|--------|------|------|------|
| **Summary table (top)** | 410 | 410 | 405 |
| **C-42 scoring reference table (lower)** | 405 (=390+15) | 405 (=390+15) | 400 (=390+10) |

The C-42 reference table is internally consistent with the rubric: C-40 PARTIAL (5) + C-41 PARTIAL (5) + C-42 PARTIAL/FAIL (5/0) = 15/10. The summary table overstates by 5 pts for each, implying C-40 PASS for split shapes — which the rubric explicitly contradicts ("A gate naming all three axes without any partial-failure declaration earns PARTIAL," "A gate that declares partial satisfaction invalid without naming individual axes earns PARTIAL"). Scoring follows the rubric and the C-42 reference table.

---

## V-71: Ceiling — Both Components in Block Body (C-41 PASS + C-42 PASS)

**Block body gate:** All three axes named by label (Axis 1: duality framing, Axis 2: audit format, Axis 3: derivation direction) AND impossibility statement ("A block containing any two of the three axes while omitting the third fails this gate. Partial axis coverage is not partial compliance — it is a gate failure").

**Produced label:** Acknowledges ("The block gate instruction in the block body names all three axes by label and declares partial axis coverage a gate failure") — does not restate the full gate as its exclusive location.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-39 | PASS (390) | Identical baseline |
| C-40 | **PASS (10)** | Block body gate names all three axes by label AND declares partial axis omission a gate failure. Both components present in the block instruction — the gate condition is fully formed at read time |
| C-41 | **PASS (10)** | Full C-40 gate — axis enumeration + impossibility statement — is entirely in the block instruction body. Produced label summarizes without carrying either component as its exclusive location; read-time enforcement fully satisfied |
| C-42 | **PASS (10)** | Both gate components (axis enumeration, impossibility statement) reside in the block instruction body. No split: neither component is exclusively in the produced label. C-41 PASS implies C-42 PASS |

**Score: 420/420**

---

## V-72: Axes in Block Body, Impossibility in Produced Label Only (C-42 PARTIAL test)

**Block body gate:** All three axes named by label (Axis 1, Axis 2, Axis 3 with functional descriptors). **No impossibility statement** in the block body.

**Produced label:** Carries the impossibility statement ("A block containing Axes 1 and 2 but omitting Axis 3 fails its gate. A block containing any two of the three axes while omitting the third fails its gate") — the label is the exclusive location for this gate component.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-39 | PASS (390) | Identical baseline |
| C-40 | **PARTIAL (5)** | Block body gate names all three axes by label — satisfying axis enumeration — but carries no partial-failure declaration. This is C-40 PARTIAL condition 3 explicitly: "A gate naming all three axes without any partial-failure declaration earns PARTIAL." Impossibility in produced label does not convert the block body gate to PASS |
| C-41 | **PARTIAL (5)** | Block body has the harder half of the gate (axis enumeration), providing partial read-time enforcement. Impossibility statement is displaced to the produced label — emit-time only. The full C-40 gate is not in the block body. Genuine-attempt doctrine applies: axis enumeration is the specificity-bearing component; PARTIAL is warranted over FAIL |
| C-42 | **PARTIAL (5)** | Split-gate shape: axis enumeration (Component 1) in block body, impossibility statement (Component 2) exclusively in produced label. C-42 rubric: "axis enumeration is read-time, impossibility is emit-time — the harder structural element achieves read-time placement, only the prohibition is displaced." Named PARTIAL in C-42 verdict table |

**Score: 405/420**

---

## V-73: Impossibility in Block Body, Axes in Produced Label Only (C-42 PARTIAL mirror)

**Block body gate:** Impossibility statement present ("Partial axis coverage is not partial compliance — it is a gate failure. A block containing any two of the three axes while omitting the third fails this gate"). **No axis labels** in the block body gate — the gate uses no "Axis 1/2/3" enumeration.

**Produced label:** Carries all three axis labels (Axis 1: duality framing, Axis 2: audit format, Axis 3: derivation direction). This is the exclusive location for axis enumeration.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-39 | PASS (390) | Identical baseline |
| C-40 | **PARTIAL (5)** | Block body gate declares partial satisfaction a gate failure — impossibility present — but the gate condition uses no individual axis labels. C-40 PARTIAL condition 2: "A gate that declares partial satisfaction invalid without naming individual axes earns PARTIAL." Axis labels in the produced label do not substitute for the gate condition naming them |
| C-41 | **PARTIAL (5)** | Mirror split failure mode. Block body has the impossibility component (prohibitive intent), but axis enumeration is exclusively in the produced label. v15 rubric revises C-41's scoring for this shape from R14's FAIL (V-69) to PARTIAL: the impossibility statement provides read-time enforcement intent, just not specificity. Named in the C-42 verdict table: "Impossibility in body, axes in label only (mirror) → C-41 PARTIAL" |
| C-42 | **PARTIAL (5)** | Mirror split shape: impossibility statement (Component 2) in block body, axis enumeration (Component 1) exclusively in produced label. C-42 rubric: "A gate with impossibility statement in the block body and axis enumeration exclusively in the produced label also earns PARTIAL (mirror split failure mode)" |

**Score: 405/420**

> **Note on V-73 vs. R14 V-69:** R14 scored the mirror shape C-41 FAIL. v15 revises that to PARTIAL via the explicit C-42 verdict table. The structural rationale: C-42's addition made the mirror split a named, explicit shape; once named, genuine-attempt doctrine applies at the C-41 layer as well, since partial read-time enforcement exists (impossibility fires at read time, axis specificity is emit-time only).

---

## V-74: Both Components in Produced Label Only (C-42 FAIL test)

**Block body gate (minimal):** Read-completion trigger only: instructs the model to write "AUDIT ARCHITECTURE DECLARED" before Phase 1. Zero axis enumeration, zero impossibility statement in the block body gate.

**Produced label:** Full per-axis gate — all three axes named by label AND impossibility statement ("A block containing Axes 1 and 2 but omitting Axis 3 fails this gate"). Both components live exclusively in the produced label.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-39 | PASS (390) | Identical baseline |
| C-40 | **PARTIAL (5)** | Block body gate names zero axes. C-40 PARTIAL condition 1: "A gate present but naming fewer than three axes earns PARTIAL." The full per-axis gate lives only in the produced architecture label; the block body instruction is a completion trigger with no axis-level gate content |
| C-41 | **PARTIAL (5)** | Full per-axis gate (all three axes + impossibility) present only in the produced architecture label. This matches the C-41 named PARTIAL condition verbatim: "A per-axis gate present only in the produced architecture label earns PARTIAL." Structurally identical to V-67 (R14) which also earned C-41 PARTIAL at the named condition |
| C-42 | **FAIL (0)** | Both gate components (axis enumeration AND impossibility statement) live exclusively in the produced architecture label. Neither achieves read-time placement. C-42 rubric: "A gate with both components exclusively in the produced label earns PARTIAL on C-41 (named condition); on C-42, no component achieves read-time placement, earning FAIL." This is the critical C-41/C-42 divergence: C-41 earns PARTIAL (named condition) while C-42 earns FAIL |

**Score: 400/420**

> **Divergence proof (V-74):** C-41 PARTIAL (5 pts) via named condition; C-42 FAIL (0 pts). This is the only shape where C-41 and C-42 diverge — the primary differentiation test for the new criterion. A rubric that stopped at C-41 would award 405 (390+5+5+5); with C-42, V-74 earns 400.

---

## V-75: Redundant Full Gate in Both Block Body and Produced Label (C-42 PASS)

**Block body gate:** Identical to V-71 — full three-axis enumeration by label AND impossibility statement in the block instruction body.

**Produced label:** Redundantly restates the full gate — all three axes named by label AND impossibility statement are also present in the produced label in addition to the block body content.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01–C-39 | PASS (390) | Identical baseline |
| C-40 | **PASS (10)** | Block body gate names all three axes by label AND declares partial axis omission a gate failure. Label-side restatement is additional content — irrelevant to C-40's gate condition assessment |
| C-41 | **PASS (10)** | Full per-axis gate (axis enumeration + impossibility statement) present in block instruction body at read time. C-41 asks only whether the gate appears in the block body. The additional presence of the full gate in the produced label is inert to the body-placement verdict — confirmed by V-70 (R14) with identical structure |
| C-42 | **PASS (10)** | Both gate components are present in the block instruction body. The produced label also carrying both components is redundant duplication, not a split. C-42 targets components that are DIVIDED — present in one location and absent from the other. When both components appear in both locations, no split exists; the gate is duplicated, not divided. Duplication is not disqualification |

**Score: 420/420**

---

## Composite Scores

| Variation | C-01–C-39 | C-40 | C-41 | C-42 | Total | Rank |
|-----------|-----------|------|------|------|-------|------|
| V-71 | 390 | PASS (10) | PASS (10) | PASS (10) | **420/420** | 1 (tied) |
| V-75 | 390 | PASS (10) | PASS (10) | PASS (10) | **420/420** | 1 (tied) |
| V-72 | 390 | PARTIAL (5) | PARTIAL (5) | PARTIAL (5) | **405/420** | 3 (tied) |
| V-73 | 390 | PARTIAL (5) | PARTIAL (5) | PARTIAL (5) | **405/420** | 3 (tied) |
| V-74 | 390 | PARTIAL (5) | PARTIAL (5) | FAIL (0) | **400/420** | 5 |

---

## Excellence Signals (from V-71 / V-75)

**1. C-42 FAIL is strictly harder than C-41 PARTIAL for the "both-in-label" shape.** V-74 is the critical differentiation: C-41 earns its named PARTIAL (5 pts) because the full per-axis gate is present — just in the wrong location. C-42 earns FAIL (0 pts) because no gate component achieves read-time placement. The rubric now distinguishes between "gate present but mislocated" (C-41 judgment) and "no component at read time" (C-42 judgment). V-74 earns 5 pts on C-41 and 0 pts on C-42 from the same structural fact — both-in-label is simultaneously a named pass for one criterion and an explicit fail for the other.

**2. v15 revises C-41 mirror-shape from FAIL to PARTIAL.** R14 V-69 (impossibility in body, axes in label) earned C-41 FAIL because genuine-attempt doctrine didn't extend to a gate with no axis specificity. v15 reverses this: V-73 earns C-41 PARTIAL. The structural reason for the revision: C-42's introduction named the mirror split as an explicit shape with a defined PARTIAL verdict. Once the mirror split is a named C-42 shape, applying C-41 FAIL creates an asymmetry — the original split (V-72, axes in body) gets C-41 PARTIAL while the mirror gets C-41 FAIL, despite both being one-component-read-time structures. v15 makes both splits symmetric at C-41 PARTIAL.

**3. Duplication is not division — C-42's invariant.** V-75 places both gate components in the block body AND in the produced label. C-42 PASS. The criterion targets components that are divided between sites; it does not target components that are present at both sites. The label can redundantly restate everything in the block body without triggering a split-gate finding. This invariant (confirmed by V-70 for C-41 in R14) now extends to C-42.

**4. Split symmetry yields scoring symmetry: V-72 and V-73 tied at 405.** The harder structural element (axis enumeration, by R14 ruling) being read-time in V-72, and the weaker element (impossibility) being read-time in V-73, both earn the same 405/420. C-42's symmetric PARTIAL verdict for both split shapes makes the score insensitive to WHICH component is displaced — only whether a split exists (PARTIAL), no split exists (PASS), or neither component is read-time (FAIL on C-42, PARTIAL on C-41).

---

```json
{"top_score": 420, "all_essential_pass": true, "new_patterns": ["C-42 FAIL diverges from C-41 PARTIAL on the both-in-label shape: same structural fact earns different verdicts on the two criteria simultaneously — C-41 judges gate presence (PARTIAL), C-42 judges read-time placement (FAIL)", "v15 revises C-41 mirror-shape ruling from R14 FAIL to PARTIAL for symmetry with the forward split shape, once C-42 names both splits as equivalent PARTIAL shapes", "Split symmetry yields scoring symmetry: V-72 and V-73 both earn 405 regardless of which component is displaced to emit-time, because C-42 PARTIAL applies to any one-component-read-time distribution"]}
```
