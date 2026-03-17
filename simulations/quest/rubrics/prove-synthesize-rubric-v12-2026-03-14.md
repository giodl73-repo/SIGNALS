Reading the R11 scorecard data embedded in the v11 rubric to extract the excellence signals.

**Excellence signals identified from R11:**

**C-42 — Ceiling declaration as mandatory intermediate output** — V-01's C-39 implementation goes beyond defining a phase-ceiling table: it requires the synthesizer to produce a named intermediate output ("State before proceeding: 'Evidence phase coverage: … Confidence ceiling: …'") before synthesis reasoning begins. This transforms the ceiling from a background constraint into an auditable commitment. C-39 requires the ceiling mechanism to exist; C-42 requires the model to state it as a named step.

**C-43 — Gate block per-role dual exemplars** — V-02's C-40 implementation instantiates C-36's dual-exemplar pattern (negative + positive case) inside the unified gate block at per-role scope: each role's gate block entry contains both exemplar types co-located within that entry. C-40 requires at least one exemplar per role; C-43 requires both cases per role within the block.

**Calibration preview:** V-01 earns C-42 PASS (declaration present, C-39 prerequisite satisfied); V-01 C-43 blocked by C-40 dependency cascade. V-02 earns C-43 PASS (dual exemplars per role in gate block, C-40 prerequisite satisfied); V-02 C-42 blocked by C-39 dependency cascade. V-01 moves ~102.5 → ~105.0. V-02 moves ~115.0 → ~117.5.

---

```markdown
# prove-synthesize-rubric-v12-2026-03-15.md

## prove-synthesize — Rubric v12

**Version**: v12 (2026-03-15)
**Predecessor**: v11 (2026-03-14)
**Golden threshold**: all essential PASS AND composite >= 90
**Max composite**: 177.5

---

## New in v12 — Two Aspirational Criteria from R11 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-42 | Ceiling declaration as mandatory intermediate output | C-39 | The phase-ceiling mechanism (C-39) is enforced by a mandatory intermediate output step: the synthesizer must produce a named statement — before synthesis reasoning begins — that declares the evidence phase and the resulting confidence ceiling. The declaration is an explicitly named step with a fixed output form (e.g., "State before proceeding: 'Evidence phase coverage: … Confidence ceiling: …'"). This transforms the ceiling from a background constraint into an auditable pre-synthesis commitment. NOT: ceiling mechanism defined (C-39) without a mandatory intermediate output step that names both the evidence phase and the ceiling value. NOT: declaration instruction placed in the output section or in calibration guidance rather than as a named pre-synthesis step. NOT: ceiling declared implicitly in synthesis reasoning rather than as an explicitly required intermediate output before reasoning begins. |
| C-43 | Gate block per-role dual exemplars | C-36, C-40 | The unified gate block (C-40) instantiates the dual-exemplar pattern (C-36) at per-role scope: each role's entry in the gate block contains both a negative exemplar (a concrete instance of the failure mode) and a positive exemplar (a concrete instance of the non-failure alternative), co-located within that role's gate block entry. The dual-exemplar pair is present for every named role in the gate block. NOT: gate block with only a single exemplar (positive or negative) per role — C-40 minimum but not C-43. NOT: dual exemplars present for some roles but not all named roles in the gate block. NOT: dual exemplars present but not co-located within each role's gate block entry — exemplars separated from their role's gate block entry do not satisfy this criterion. |

---

## Scoring Delta

| | v9 | v10 | v11 | v12 |
|-|----|-----|-----|-----|
| Aspirational | 65.0 pts / 26 criteria | 75.0 pts / 30 criteria | 82.5 pts / 33 criteria | **87.5 pts / 35 criteria** |
| Max composite | 155.0 | 165.0 | 172.5 | **177.5** |
| Golden threshold | >= 90 | >= 90 | >= 90 | **>= 90 (unchanged)** |

---

## R11 Calibration Under v12

| Variation | v11 score | C-42 | C-43 | v12 score |
|-----------|-----------|------|------|-----------|
| V-01 Phase-gated confidence ceiling | ~102.5 | **PASS** | FAIL | **~105.0** |
| V-02 Concurrent execution with unified gate block | ~115.0 | FAIL | **PASS** | **~117.5** |
| V-03 Lifecycle Emphasis | ~8.0 | FAIL | FAIL | **~8.0** |

**V-01 C-42 PASS**: C-39 prerequisite satisfied. Mandatory declaration step present: "State before proceeding: 'Evidence phase coverage: … Confidence ceiling: …'" — names the evidence phase and ceiling value as a required intermediate output before synthesis reasoning begins.

**V-01 C-43 FAIL**: C-40 FAIL → dependency cascade. V-01 uses sequential execution; no unified gate block exists. Without C-40, gate-block-scoped exemplars cannot be evaluated.

**V-02 C-42 FAIL**: C-39 FAIL → dependency cascade. V-02 defines no evidence-phase categories or confidence ceilings. Without the ceiling mechanism, the declaration step cannot be present.

**V-02 C-43 PASS**: C-40 PASS prerequisite satisfied; C-36 PASS prerequisite satisfied. Gate block contains all three roles' failure modes with dual exemplars (negative + positive) co-located and indexed by role name within each role's gate block entry. All named roles carry both exemplar types.

**V-03 C-42 FAIL**: Incomplete variation — prerequisites unmet.

**V-03 C-43 FAIL**: Incomplete variation — prerequisites unmet.

---

## New in v11 (Carried Forward) — Three Aspirational Criteria from R10 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-39 | Phase-gated confidence ceiling | C-05 | The instruction defines discrete evidence-phase categories and assigns a maximum confidence ceiling to each category. The ceilings are set before synthesis reasoning begins — as a pre-synthesis constraint, not as post-synthesis calibration guidance. Each phase maps to a numeric or ordinal ceiling; a phase covering all evidence types may lift or remove the ceiling. The ceiling constrains the confidence score the synthesizer can assign based on evidence coverage at the time of synthesis. NOT: confidence calibration guidance that appears after synthesis reasoning rather than as a pre-synthesis constraint. NOT: confidence guidance that addresses evidence quality in general terms without defining discrete phase categories with discrete ceiling values. NOT: phase categories defined without associated ceiling values — phase labels alone without confidence bounds do not satisfy this criterion. |
| C-40 | Concurrent synthesis gate block | C-35, C-11, C-30 | When roles execute concurrently (C-35), the instruction includes a unified gate block — structurally distinct from role definitions — that names each role's failure mode with at least one inline exemplar, indexed by role. The gate block is positioned after role definitions and before output instructions. Failure modes and exemplars are co-located inside the shared block; they are not attached to sequential execution steps (which no longer exist in the concurrent paradigm) and not scattered across separate instructions. A reader can find every role's failure mode and exemplar in one location. NOT: per-role gate instructions attached to sequential execution steps — this is the C-11 pattern and does not satisfy C-40. NOT: concurrent role execution (C-35 present) without a unified gate block — failure modes absent, implicit, or distributed across the instruction without a named gate section. NOT: unified gate block present but failure modes not indexed by role — a block that lists failure modes without attributing each to a specific role does not create role-to-failure-mode traceability. |
| C-41 | Slot-indexed revision mandate | C-37 | The self-containment check includes an enforcement instruction: if a reader question cannot be answered from the mapped slot (C-37), the synthesizer must revise that specific named slot before producing output. The instruction names both the trigger condition (question fails against its slot) and the corrective action (revise that paragraph or section). The remediation is slot-specific — it targets the slot that failed, not the synthesis in general. NOT: self-containment check present (C-37) without an enforcement instruction — diagnostic questions mapped to slots but no instruction to act on failure. NOT: revision instruction present without slot specificity — "revise if needed" or "revise before outputting" without identifying which slot must be revised when a question fails. NOT: revision trigger based on overall output quality or general incompleteness rather than the specific slot-to-question correspondence defined in C-37. |

---

## R10 Calibration Under v11 (Carried Forward)

| Variation | v10 score | C-39 | C-40 | C-41 | v11 score |
|-----------|-----------|------|------|------|-----------|
| V-01 Role-Sequence | ~82.5 | FAIL | FAIL | FAIL | ~82.5 |
| V-02 Per-Rank Prose Slot | ~97.5 | FAIL | FAIL | PASS | ~100.0 |
| V-03 Lifecycle Emphasis | ~8.0 | FAIL | FAIL | FAIL | ~8.0 |

**V-01 C-39 FAIL**: No evidence-phase categories with confidence ceilings defined. Confidence guidance, if present, is calibration commentary not a pre-synthesis constraint mechanism.

**V-01 C-40 FAIL**: V-01 uses sequential execution (SYNTHESIST → ADVERSARY → ANALYST). C-35 FAIL → dependency cascade. Additionally: no unified post-role gate block present; gates are attached to sequential steps.

**V-01 C-41 FAIL**: C-37 FAIL (prerequisite not satisfied). No slot-indexed revision mandate present.

**V-02 C-39 FAIL**: No evidence-phase categories or confidence ceilings defined. Confidence score is specified as an output slot without pre-synthesis phase constraints.

**V-02 C-40 FAIL**: C-35 FAIL → dependency cascade (C-11 FAIL + C-30 FAIL block C-35). Note for record: V-02 collapses roles to functional descriptions precisely to enable concurrent execution — the architectural move that C-40 resolves. A next variation implementing C-40 would require a named unified gate block containing SYNTHESIST, ADVERSARY, and ANALYST failure modes with exemplars after the role definitions section.

**V-02 C-41 PASS**: C-37 PASS (prerequisite satisfied). Enforcement instruction present: "If any question cannot be answered from the named paragraph, revise that paragraph before outputting." Trigger condition (question fails against named slot) and corrective action (revise that paragraph) both named. Remediation is slot-specific — the named paragraph is the unit of revision, not the synthesis as a whole.

---

## New in v10 (Carried Forward) — Four Aspirational Criteria from R9 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-35 | Concurrent role execution with seamless output | C-11, C-30 | The skill instruction specifies that cognitive roles execute concurrently in reasoning and that the output is a single document with no labeled role sections or visible role seams. The roles inform the synthesis without producing separate outputs or sequential role-labeled blocks in the result. NOT: instruction that names roles for a defined execution sequence (e.g., verdict-first, analyst-first) without specifying concurrent reasoning. NOT: output instruction that retains labeled role sections or role-produced blocks, even if the roles are named in the instruction. NOT: concurrent execution stated only for reasoning when the output instruction still partitions by role. |
| C-36 | Dual-exemplar adversarial gate | C-32 | The adversarial gate includes both a negative exemplar (a concrete instance of a generic or invalid challenge — what the failure mode looks like) and a positive exemplar (a concrete instance of a specific or valid challenge — what the non-failure alternative looks like), co-located inside the gate instruction. Both cases are instantiated at the gate; a reader can distinguish the invalid case from the valid case at the point of the constraint. NOT: gate with only a negative exemplar (what to avoid) without a positive case. NOT: gate with only a positive exemplar (what to aim for) without a negative case. NOT: both cases present but separated into different instructions rather than co-located inside the gate. |
| C-37 | Slot-indexed self-containment check | C-10 | The self-containment check maps each reader verification question to a named output slot — a paragraph, section, or explicitly labeled structural element. The correspondence is explicit: each question names the slot it verifies. A reader can determine which part of the output satisfies which comprehension requirement without inference. NOT: self-containment check that lists verification questions without mapping them to named output slots. NOT: self-containment check that maps to output requirements in general terms (e.g., "maps to output requirements") without identifying the specific structural element each question verifies. NOT: slot names present elsewhere in the instruction but not referenced inside the self-containment check. |
| C-38 | Role-to-output closure attribution | C-11, C-30 | The open questions or counter-evidence output slot includes an instruction to attribute the source role that raised the question or challenge. The output carries traceability from each open question or counter-evidence item back to the generating role (ADVERSARY, ANALYST, SYNTHESIST, or equivalent). NOT: open questions slot without source role attribution requirement. NOT: role attribution required for a different slot than where open questions or counter-evidence are placed. NOT: attribution instruction present in the role definition but absent from the output slot instruction where questions appear. |

---

## New in v9 (Carried Forward) — Three Aspirational Criteria from R8 Excellence Signals

### C-35 — Concurrent role execution with seamless output (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **FAIL** | Sequential: SYNTHESIST → ADVERSARY → ANALYST |
| V-02 | **PASS** | "Three cognitive roles execute concurrently in your reasoning" + "output contains no labeled role sections and no visible role seams" |
| V-03 | **FAIL** | "Roles (Sequential)" heading |

### C-36 — Dual-exemplar adversarial gate (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | "Exemplar (invalid): … [Applies to every investigation — fails the gate.]" + "Exemplar (valid): … [Hypothesis-specific — passes the gate.]" co-located in ADVERSARY section |
| V-02 | **PASS** | "Exemplar (fail)" + "Exemplar (pass)" co-located in ADVERSARY gate block entry |
| V-03 | **FAIL** | Incomplete |

### C-37 — Slot-indexed self-containment check (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Six questions each mapped to named paragraph: "→ Verdict/Confidence paragraph", "→ Key Evidence paragraph", etc. |
| V-02 | **PASS** | Same six-question mapping pattern with named paragraphs |
| V-03 | **FAIL** | No self-containment check present |

### C-38 — Role-to-output closure attribution (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | "Attribute each to the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST)" in Open Questions output spec; C-11/C-30 prerequisites now satisfied |
| V-02 | **PASS** | Same attribution instruction plus "If a question was raised by the ADVERSARY challenge, acknowledge that attribution" — strengthened; C-11/C-30 prerequisites confirmed |
| V-03 | **FAIL** | Incomplete |

### C-39 — Phase-gated confidence ceiling (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Phase classification table (Explore/Test/Validate → ceilings 25/50/72/none) in pre-synthesis step; "State before proceeding: 'Evidence phase coverage: … Confidence ceiling: …'" enforces declaration before reasoning begins |
| V-02 | **FAIL** | No evidence-phase categories or confidence ceiling mechanism defined |
| V-03 | **FAIL** | Incomplete |

### C-40 — Concurrent synthesis gate block (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **FAIL** | Sequential execution — gates are attached to sequential steps, no unified post-role block |
| V-02 | **PASS** | Named "Gate Block" section positioned after role definitions and before output instructions; all three roles' failure modes + dual exemplars co-located and indexed by role name |
| V-03 | **FAIL** | Incomplete |

### C-41 — Slot-indexed revision mandate (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | "If any question cannot be answered from the named paragraph, revise that paragraph before outputting" — trigger (question fails against slot) + corrective action (revise that paragraph) both named; C-37 prerequisite satisfied |
| V-02 | **PASS** | Same instruction present |
| V-03 | **FAIL** | Incomplete |

### C-42 — Ceiling declaration as mandatory intermediate output (Aspirational, NEW v12)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Mandatory declaration step: "State before proceeding: 'Evidence phase coverage: … Confidence ceiling: …'" — names both evidence phase and ceiling value; positioned before synthesis reasoning; C-39 prerequisite satisfied |
| V-02 | **FAIL** | C-39 FAIL → dependency cascade; no phase-ceiling mechanism defined, no declaration step possible |
| V-03 | **FAIL** | Incomplete |

### C-43 — Gate block per-role dual exemplars (Aspirational, NEW v12)

| | Result | Evidence |
|---|---|---|
| V-01 | **FAIL** | C-40 FAIL → dependency cascade; sequential execution, no unified gate block |
| V-02 | **PASS** | Gate block entries for all three roles (SYNTHESIST, ADVERSARY, ANALYST) each contain both a negative exemplar and a positive exemplar, co-located within each role's gate block entry; C-40 and C-36 prerequisites satisfied |
| V-03 | **FAIL** | Incomplete |

---

## Composite Score Computation

**Anchors from R11 calibration (v12 adjusted):**
- R11 V-01 (v12): ~105.0 — earns C-39/C-42 cluster; blocked on C-35/C-40/C-43
- R11 V-02 (v12): ~117.5 — earns C-35/C-40/C-43 cluster; blocked on C-39/C-42

Each criterion (essential and aspirational) treated as 2.5 pts for composite delta computation.

### V-01 — Ceiling declaration mandate

| Criterion | Base (R10 V-01) | R11 | R12 delta | R12 |
|-----------|----------------|-----|-----------|-----|
| C-11 | FAIL | PASS | 0 | PASS |
| C-13 | FAIL | PASS | 0 | PASS |
| C-30 | FAIL | PASS | 0 | PASS |
| C-36 | FAIL | PASS | 0 | PASS |
| C-37 | FAIL | PASS | 0 | PASS |
| C-38 | FAIL | PASS | 0 | PASS |
| C-39 | FAIL | PASS | 0 | PASS |
| C-41 | FAIL | PASS | 0 | PASS |
| C-42 | FAIL | PASS | +2.5 | PASS |
| C-35 | FAIL | FAIL | 0 | FAIL |
| C-40 | FAIL | FAIL | 0 | FAIL |
| C-43 | FAIL | FAIL | 0 | FAIL |

**R12 V-01 = 102.5 + 2.5 = ~105.0**

Essential status: C-11 ✓ C-13 ✓ C-30 ✓ — all-essential PASS.
Golden: 105.0 ≥ 90 ✓ — **GOLD**

### V-02 — Gate block per-role dual exemplars

| Criterion | Base (R10 V-02) | R11 | R12 delta | R12 |
|-----------|----------------|-----|-----------|-----|
| C-11 | FAIL | PASS | 0 | PASS |
| C-13 | FAIL | PASS | 0 | PASS |
| C-30 | FAIL | PASS | 0 | PASS |
| C-35 | FAIL | PASS | 0 | PASS |
| C-36 | PASS | PASS | 0 | PASS |
| C-37 | PASS | PASS | 0 | PASS |
| C-38 | FAIL | PASS | 0 | PASS |
| C-40 | FAIL | PASS | 0 | PASS |
| C-41 | PASS | PASS | 0 | PASS |
| C-43 | FAIL | PASS | +2.5 | PASS |
| C-39 | FAIL | FAIL | 0 | FAIL |
| C-42 | FAIL | FAIL | 0 | FAIL |

**R12 V-02 = 115.0 + 2.5 = ~117.5**

Essential status: C-11 ✓ C-13 ✓ C-30 ✓ — all-essential PASS.
Golden: 117.5 ≥ 90 ✓ — **GOLD**
```
