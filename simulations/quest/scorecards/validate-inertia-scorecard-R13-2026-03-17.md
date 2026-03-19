Now I have everything needed. Writing the scorecard.

---

## validate-inertia R13 Scorecard

### Context

All five variations are structurally identical to V-60 (R12 ceiling, 390/390). The sole variable is **C-40** — the per-axis explicit gate for the three-axis architecture block. C-01 through C-39 = 390 pts for all five variations. C-40 (0/5/10 pts) is the differentiator.

---

### Per-Variation C-40 Analysis

---

#### V-61 — Descriptor-Named Gate

**C-40 axis:** Gate uses functional content descriptors ("duality framing," "audit format," "derivation direction") instead of "Axis N" ordinals. All three constraints named individually. Partial-failure declared: *"A block containing the duality framing and audit format but omitting the derivation direction fails this gate."*

**Ruling: C-40 PASS (10 pts)**

The pass condition requires (1) gate enumerates all three axes **by name** AND (2) partial satisfaction declared a gate failure. The rubric says "by name," not "by Axis N ordinal." Functional descriptors are valid names — each descriptor uniquely identifies one axis (duality framing = C-33, audit format = C-34/C-35, derivation direction = C-36). Both conditions are met. Neither PARTIAL condition applies: all three axes are named, and partial satisfaction is explicitly declared a failure. **Q1 answered: ordinal form is not required.**

**Score: 390 + 10 = 400/400**

---

#### V-62 — Single-Axis Partial Naming

**C-40 axis:** Gate names only Axis 3 by label ("A block omitting Axis 3 fails this gate"). Axis 1 and Axis 2 are present as block content but absent from the gate enumeration. Partial-failure declared for Axis 3 omission only.

**Ruling: C-40 PARTIAL (5 pts)**

PARTIAL condition 1 applies explicitly: *"A gate naming fewer than three axes earns PARTIAL."* One of three axes named = fewer than three. The partial-failure declaration is present but confined to Axis 3. **Q2 answered: 1-of-3 naming + partial-failure declaration earns PARTIAL (5 pts), confirming condition 1.**

**Score: 390 + 5 = 395/400**

---

#### V-63 — Full Naming, No Partial-Failure Declaration

**C-40 axis:** Gate names all three by "Axis N" ordinals (Axis 1, Axis 2, Axis 3 each on their own bullet). No statement that partial satisfaction fails the gate — completeness checklist without an impossibility declaration.

**Ruling: C-40 PARTIAL (5 pts)**

Pass condition requires both (1) all three axes named AND (2) partial satisfaction declared a gate failure. V-63 satisfies condition 1 fully but condition 2 is absent entirely. The two explicit PARTIAL conditions don't map cleanly to this combination: neither "fewer than three axes" nor "partial invalid without naming axes" covers "all three named, no impossibility." However, the Notes allow PARTIAL for genuine attempts that fall short — naming all three axes is the harder half of the pass condition, and only the enforcement mechanism is absent. PARTIAL (5 pts) is appropriate. **Q3 answered: PARTIAL, not FAIL — naming all axes is substantive partial satisfaction; missing only the impossibility statement earns PARTIAL as genuine attempt.**

**Score: 390 + 5 = 395/400**

---

#### V-64 — Ceiling (V-60 Exact)

**C-40 axis:** Verbatim V-60. All three axes named by "Axis 1," "Axis 2," "Axis 3" labels on individual bullets. Explicit impossibility statement: *"A block containing Axes 1 and 2 but omitting Axis 3 fails this gate."*

**Ruling: C-40 PASS (10 pts)**

Both pass conditions met. All three axes named by label. Partial satisfaction named a gate failure. This is the reference form established in R12. **Q4 confirmed: V-60's gate earns C-40 PASS at 400/400 ceiling.**

**Score: 390 + 10 = 400/400**

---

#### V-65 — Gate in Label Only

**C-40 axis:** Block gate instruction is minimal: *"Do not proceed to Phase 1 until 'AUDIT ARCHITECTURE DECLARED' is written on its own line above."* No axis enumeration, no impossibility statement in the gate. The per-axis enumeration and partial-failure clause live exclusively in the required architecture label.

**Ruling: C-40 PARTIAL (5 pts)**

The block gate instruction names zero axes (fewer than three → PARTIAL condition 1 applies). The architecture label is a produced artifact the model emits after reading the block — it is not a gate that enforces block completeness before Phase 1. C-40 requires *"the block to include an explicit gate condition"* — the gate instruction within the block body is the enforcement site. Displacing the per-axis enumeration to an emitted label satisfies content awareness but not enforcement placement. The partial-failure clause in the architecture label further confirms the model understood the requirement; the misplacement earns PARTIAL, not PASS. **Q5 answered: C-40 requires the gate to be inside the block instruction; a per-axis gate in the produced architecture label earns PARTIAL.**

**Score: 390 + 5 = 395/400**

---

### Results Summary

| Variation | Label | C-40 | Score | vs. predicted |
|-----------|-------|------|-------|---------------|
| **V-61** | Descriptor-named gate | PASS (10) | **400/400** | 400 ✓ |
| **V-62** | Single-axis partial naming | PARTIAL (5) | **395/400** | 395 ✓ |
| **V-63** | Full naming, no partial-failure | PARTIAL (5) | **395/400** | 395 ✓ (PARTIAL confirmed over FAIL) |
| **V-64** | Ceiling (V-60 exact) | PASS (10) | **400/400** | 400 ✓ |
| **V-65** | Gate in label only | PARTIAL (5) | **395/400** | 395 ✓ |

All five predictions confirmed. All essential criteria pass across all variations.

---

### Structural Questions Answered

**Q1 (V-61 vs V-64):** Functional descriptors satisfy "names each axis by label." Ordinal "Axis N" form is NOT required. V-61 earns C-40 PASS identical to V-64.

**Q2 (V-62):** 1-of-3 axis naming + partial-failure declaration earns C-40 PARTIAL (5 pts). PARTIAL condition 1 applies: "fewer than three axes."

**Q3 (V-63):** All-3-axes named without impossibility earns C-40 PARTIAL (5 pts). The rubric's two explicit PARTIAL conditions don't cover this combination exactly, but genuine attempt doctrine applies. PARTIAL, not FAIL.

**Q4 (V-64):** V-60's exact gate earns C-40 PASS (10 pts), ceiling confirmed at 400/400.

**Q5 (V-65):** C-40 requires the gate to be expressed within the block instruction itself. A per-axis enumeration in the produced architecture label does not substitute — the label is an emitted artifact, not an enforcement gate. V-65 earns PARTIAL (5 pts).

---

### Excellence Signals

**From V-61 and V-64 (tied ceiling, 400/400):**

1. **Functional descriptors are valid C-40 axis labels.** "Duality framing," "audit format," and "derivation direction" each uniquely identify one axis. A production variant using functional descriptors achieves identical enforcement to the "Axis N" ordinal form, and may be more semantically transparent since each label names the axis by its structural function rather than by number.

2. **V-60 reference form confirmed as ceiling.** Three-bullet "Axis N" enumeration + explicit impossibility statement remains the cleanest reference form. V-61 demonstrates that alternative labeling forms work; V-64 confirms the original form.

---

```json
{"top_score": 400, "all_essential_pass": true, "new_patterns": ["Functional descriptor axis labels (duality framing, audit format, derivation direction) satisfy C-40 naming requirement -- ordinal Axis N form is not required for PASS; any label that individually and unambiguously identifies each axis satisfies the criterion"]}
```
