Reading the R10 scorecard carefully before extracting signals.

**Excellence signals identified:**

1. **C-39 — Phase-gated confidence ceiling** — Pre-synthesis evidence phase categories constrain the maximum confidence score the synthesizer can assign. Each phase maps to a numeric ceiling; coverage of all phases removes the ceiling. This is the first pre-synthesis constraint mechanism in the series — it fires before reasoning begins, not as calibration guidance afterward.

2. **C-40 — Concurrent synthesis gate block** — When roles execute concurrently (C-35), per-role gate attachment sites disappear (no Step N). The solution is a unified gate block, placed after role definitions and before output instructions, that names each role's failure mode with exemplars indexed by role inside one shared section. Resolves the C-35/C-11 architectural tension.

3. **C-41 — Slot-indexed revision mandate** — Extends C-37 from diagnostic (map questions to slots) to enforcement (revise the named slot if the question fails). V-02 carries this exactly: "If any question cannot be answered from the named paragraph, revise that paragraph before outputting." The trigger condition and the slot-specific remediation action are both named.

**Calibration preview:** V-02 earns C-41 PASS (C-37 PASS prerequisite satisfied; revision mandate present at the enforcement site). V-02 C-40 blocked by C-35 dependency cascade. V-01 earns 0 of 3. V-02 moves from ~97.5 → ~100.0.

---

```markdown
# prove-synthesize-rubric-v11-2026-03-14.md

## prove-synthesize — Rubric v11

**Version**: v11 (2026-03-14)
**Predecessor**: v10 (2026-03-14)
**Golden threshold**: all essential PASS AND composite >= 90
**Max composite**: 172.5

---

## New in v11 — Three Aspirational Criteria from R10 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-39 | Phase-gated confidence ceiling | C-05 | The instruction defines discrete evidence-phase categories and assigns a maximum confidence ceiling to each category. The ceilings are set before synthesis reasoning begins — as a pre-synthesis constraint, not as post-synthesis calibration guidance. Each phase maps to a numeric or ordinal ceiling; a phase covering all evidence types may lift or remove the ceiling. The ceiling constrains the confidence score the synthesizer can assign based on evidence coverage at the time of synthesis. NOT: confidence calibration guidance that appears after synthesis reasoning rather than as a pre-synthesis constraint. NOT: confidence guidance that addresses evidence quality in general terms without defining discrete phase categories with discrete ceiling values. NOT: phase categories defined without associated ceiling values — phase labels alone without confidence bounds do not satisfy this criterion. |
| C-40 | Concurrent synthesis gate block | C-35, C-11, C-30 | When roles execute concurrently (C-35), the instruction includes a unified gate block — structurally distinct from role definitions — that names each role's failure mode with at least one inline exemplar, indexed by role. The gate block is positioned after role definitions and before output instructions. Failure modes and exemplars are co-located inside the shared block; they are not attached to sequential execution steps (which no longer exist in the concurrent paradigm) and not scattered across separate instructions. A reader can find every role's failure mode and exemplar in one location. NOT: per-role gate instructions attached to sequential execution steps — this is the C-11 pattern and does not satisfy C-40. NOT: concurrent role execution (C-35 present) without a unified gate block — failure modes absent, implicit, or distributed across the instruction without a named gate section. NOT: unified gate block present but failure modes not indexed by role — a block that lists failure modes without attributing each to a specific role does not create role-to-failure-mode traceability. |
| C-41 | Slot-indexed revision mandate | C-37 | The self-containment check includes an enforcement instruction: if a reader question cannot be answered from the mapped slot (C-37), the synthesizer must revise that specific named slot before producing output. The instruction names both the trigger condition (question fails against its slot) and the corrective action (revise that paragraph or section). The remediation is slot-specific — it targets the slot that failed, not the synthesis in general. NOT: self-containment check present (C-37) without an enforcement instruction — diagnostic questions mapped to slots but no instruction to act on failure. NOT: revision instruction present without slot specificity — "revise if needed" or "revise before outputting" without identifying which slot must be revised when a question fails. NOT: revision trigger based on overall output quality or general incompleteness rather than the specific slot-to-question correspondence defined in C-37. |

---

## Scoring Delta

| | v8 | v9 | v10 | v11 |
|-|----|----|----|-----|
| Aspirational | 57.5 pts / 23 criteria | 65.0 pts / 26 criteria | 75.0 pts / 30 criteria | **82.5 pts / 33 criteria** |
| Max composite | 147.5 | 155.0 | 165.0 | **172.5** |
| Golden threshold | >= 90 | >= 90 | >= 90 | **>= 90 (unchanged)** |

---

## R10 Calibration Under v11

| Variation | v10 score | C-39 | C-40 | C-41 | v11 score |
|-----------|-----------|------|------|------|-----------|
| V-01 Role-Sequence | ~82.5 | FAIL | FAIL | FAIL | **~82.5** |
| V-02 Per-Rank Prose Slot | ~97.5 | FAIL | FAIL | **PASS** | **~100.0** |
| V-03 Lifecycle Emphasis | ~8.0 | FAIL | FAIL | FAIL | **~8.0** |

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

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-32 | Inline exemplar at anti-pattern gate | C-11, C-30 | The anti-pattern gate for a cognitive role includes a parenthetical or inline instantiation — a concrete worked case — of the named failure mode, bound inside the gate instruction itself. The exemplar names a specific instance (e.g., a signal-count pattern, a concrete form of generic challenge, a specific hedging phrase) rather than restating the abstract description. The exemplar appears at the point of gate definition, not in separate commentary. NOT: failure mode described only in abstract terms at the gate, with no concrete case. NOT: exemplar provided only in commentary or output instructions separate from the gate instruction where the failure mode is defined. |
| C-33 | Format-prohibition names the positive structural requirement | C-12, C-13 | A NOT: clause that prohibits a specific formatting method (e.g., table) simultaneously names the structural element that must appear in the permitted format. The prohibition and the structural requirement are stated in a single constraint, so that bypassing the format prohibition and bypassing the structural requirement are visible as the same violation. NOT: format prohibition without statement of what structure is required in the permitted format. NOT: structural requirement stated in a separate instruction, leaving the prohibition and the slot requirement unconnected. |
| C-34 | Supersession assertion in synthesis mandate | C-05, C-10 | The synthesis mandate includes an explicit supersession claim — the synthesis is stated to supersede, override, or replace the underlying signals, not merely to summarize, integrate, or aggregate them. The claim asserts that the synthesis is the authoritative statement; the signal inventory is subordinate to it. NOT: synthesis mandate that describes the output as a summary, integration, or aggregation of signals without a supersession claim. NOT: self-contained mandate (C-10) present without supersession claim — C-10 asserts reader comprehension without artifacts; C-34 asserts the synthesis displaces the artifacts as the record. |

---

## Full Scoring Table (v11)

| Pool | Max pts | Criteria count |
|------|---------|----------------|
| Essential (C-01 – C-06 + C-09 – C-13 + C-30) | 90.0 | 12 |
| Aspirational v8 (C-07, C-08, C-14 – C-29, C-31) | 57.5 | 23 |
| v9 new (C-32, C-33, C-34) | 7.5 | 3 |
| v10 new (C-35, C-36, C-37, C-38) | 10.0 | 4 |
| v11 new (C-39, C-40, C-41) | **7.5** | **3** |
| **Total** | **172.5** | **45** |

Each aspirational criterion: 2.5 pts. Essential pool unchanged.
```
