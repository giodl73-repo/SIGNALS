**prove-synthesize-rubric-v14-2026-03-14.md** written. Here's the summary of what changed:

---

**Two new aspirational criteria from R13 excellence signals:**

**C-46 — Annotation-to-ceiling derivation linkage** (extends C-44)
V-04 showed that when a per-signal annotation inventory is present (C-44), the ceiling computation step can include an explicit provenance statement: *"The ceiling computation in the next step is derived from the per-signal annotation inventory, not inferred from a gestalt impression."* This upgrades the ceiling from an asserted declaration (C-42) to a reproducible computation — any reader can independently verify the ceiling by inspecting the annotation table. PASS requires C-44 PASS + explicit "derived not inferred" statement in the ceiling computation step. FAIL if derivation statement is absent or placed outside the ceiling computation step.

**C-47 — Extended declaration coverage in slot-indexed self-containment check** (extends C-37, C-42)
V-01, V-02, and V-04 all extend C-37's Q6 to cover annotation-derived declaration values (Primary counts, inertia state, or both) mapped to the named Verdict/Confidence slot. V-03 satisfies C-37 without any declaration extension and fails C-47, confirming it is a distinct criterion. PASS requires C-37 PASS + C-42 extended with at least one annotation-derived value + a self-containment question explicitly covering those extended values with a named output slot. FAIL if declaration is extended but self-containment check is not.

**Scoring delta:**

| | v13 | v14 |
|--|-----|-----|
| Aspirational | 92.5 pts / 37 criteria | **97.5 pts / 39 criteria** |
| Max composite | 182.5 | **187.5** |

**R13 calibration under v14:**

| Variation | v13 | C-46 | C-47 | v14 |
|-----------|-----|------|------|-----|
| V-01 Role taxonomy | ~125.0 | FAIL | PASS | **~127.5** |
| V-02 Inertia framing | ~125.0 | FAIL | PASS | **~127.5** |
| V-03 Phrasing register | ~122.5 | FAIL | FAIL | **~122.5** |
| V-04 Combined 3-column | ~127.5 | PASS | PASS | **~130.0** |

**C-46 split**: only V-04 earns it — the explicit "derived not inferred" provenance statement is the discriminator. V-01 has C-44 PASS but no derivation linkage statement.

**C-47 split**: V-01, V-02, V-04 earn it (each extends C-37's Q6 to cover their annotation-derived declaration values); V-03 fails (no extended declaration, no Q6 extension).
endency cascade). V-03 earns neither (C-42 not extended with annotation values; no Q6 extension). V-04 moves ~127.5 → ~130.0. V-01/V-02 move ~125.0 → ~127.5. V-03 unchanged (~122.5).

---

```markdown
# prove-synthesize-rubric-v14-2026-03-14.md

## prove-synthesize — Rubric v14

**Version**: v14 (2026-03-14)
**Predecessor**: v13 (2026-03-15)
**Golden threshold**: all essential PASS AND composite >= 90
**Max composite**: 187.5

---

## New in v14 — Two Aspirational Criteria from R13 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-46 | Annotation-to-ceiling derivation linkage | C-44 | When the per-signal annotated inventory is present (C-44 PASS), the ceiling computation step — the step immediately following Phase 1 annotation and preceding synthesis reasoning — explicitly states that the ceiling value is derived from the per-signal annotation inventory rather than inferred from a gestalt impression of evidence quality. The statement creates a reproducibility guarantee: any reader who inspects the annotation table can independently derive the ceiling value without trusting the synthesizer's assertion. The derivation linkage is positioned in the ceiling computation step itself, not in role definitions or general preamble. NOT: ceiling declared (C-42) without attribution to the annotation inventory — ceiling asserted rather than derived. NOT: derivation statement present in general instructions or role definitions but absent from the ceiling computation step. NOT: reference to the annotation inventory that characterizes it as "context" or "input" rather than explicitly naming it as the computational source of the ceiling value. |
| C-47 | Extended declaration coverage in slot-indexed self-containment check | C-37, C-42 | When the C-42 mandatory declaration is extended with annotation-derived values (Primary signal counts from C-44, inertia coverage state from C-45, or both), the slot-indexed self-containment check (C-37) includes a verification question whose scope explicitly covers the annotation-derived dimension values and names the output slot where those values are traceable. The annotation-derived extension is traceable end-to-end: Phase 1 annotation inventory → C-42 declaration → self-containment question → named output slot containing the confidence score and ceiling. NOT: self-containment check present (C-37 PASS) and declaration extended (C-42 with annotation values) but no question in the self-containment check covers the annotation-derived extension. NOT: self-containment question maps confidence score to named slot but omits the annotation-derived dimension values from its stated scope. NOT: annotation-derived values traceable to declaration but not referenced in any self-containment question — traceability chain broken between declaration and self-containment check. |

---

## Scoring Delta

| | v9 | v10 | v11 | v12 | v13 | v14 |
|-|----|-----|-----|-----|-----|-----|
| Aspirational | 65.0 pts / 26 criteria | 75.0 pts / 30 criteria | 82.5 pts / 33 criteria | 87.5 pts / 35 criteria | 92.5 pts / 37 criteria | **97.5 pts / 39 criteria** |
| Max composite | 155.0 | 165.0 | 172.5 | 177.5 | 182.5 | **187.5** |
| Golden threshold | >= 90 | >= 90 | >= 90 | >= 90 | >= 90 | **>= 90 (unchanged)** |

---

## R13 Calibration Under v14

| Variation | v13 score | C-46 | C-47 | v14 score |
|-----------|-----------|------|------|-----------|
| V-01 Role taxonomy (C-44) | ~125.0 | FAIL | **PASS** | **~127.5** |
| V-02 Inertia framing (C-45) | ~125.0 | FAIL | **PASS** | **~127.5** |
| V-03 Phrasing register | ~122.5 | FAIL | FAIL | **~122.5** |
| V-04 Combined 3-column (C-44 + C-45) | ~127.5 | **PASS** | **PASS** | **~130.0** |

**V-04 C-46 PASS**: C-44 prerequisite satisfied. Ceiling computation step contains the explicit statement: "The ceiling computation in the next step is derived from the per-signal annotation inventory, not inferred from a gestalt impression." Derivation linkage positioned in the ceiling computation step between Phase 1 annotation and Phase 2 synthesis reasoning.

**V-04 C-47 PASS**: C-37 PASS and C-42 PASS (extended with phase + Primary counts by phase + inertia state) prerequisites satisfied. Q6 in the slot-indexed self-containment check explicitly maps Phase 1 declaration — covering all three annotation-derived dimension values — to the Verdict/Confidence paragraph. Traceability chain complete: annotation inventory → declaration → Q6 → named output slot.

**V-01 C-46 FAIL**: C-44 PASS prerequisite satisfied. No explicit "derived not inferred" provenance statement present in the ceiling computation step. The declaration is extended to include "Primary signals by phase: [count per phase]" but the ceiling computation step does not state that the ceiling value is derived from the annotation inventory. Derivation linkage absent.

**V-01 C-47 PASS**: C-37 PASS and C-42 PASS (extended with Primary counts by phase) prerequisites satisfied. Q6 maps Primary counts by phase to Verdict/Confidence paragraph — annotation-derived value present in the self-containment question with named output slot. Traceability chain: annotation inventory → declaration → Q6 → named slot complete.

**V-02 C-46 FAIL**: C-44 FAIL → dependency cascade. V-02 uses phase + inertia dimensions but no Primary/Supporting/Contextual role taxonomy; no per-signal role annotation pass present. Without C-44, the derivation linkage requirement cannot be evaluated.

**V-02 C-47 PASS**: C-37 PASS and C-42 PASS (extended with inertia coverage state) prerequisites satisfied. Q6: "Is the phase + inertia declaration traceable to the confidence score? → Verdict/Confidence paragraph" — annotation-derived inertia state is explicitly named in the self-containment question scope with mapped output slot. Traceability chain complete.

**V-03 C-46 FAIL**: C-44 FAIL → dependency cascade. No per-signal role annotation inventory present.

**V-03 C-47 FAIL**: C-42 not extended with annotation-derived values (declaration names phase and ceiling only). Without an extended declaration, no annotation-derived extension exists for the self-containment check to cover. No Q6 extension present.

---

## New in v13 (Carried Forward) — Two Aspirational Criteria from R12 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-44 | Per-signal annotated inventory with role classification | C-39, C-42 | The phase-gated confidence ceiling (C-39) is derived from an explicit per-signal annotated inventory: each signal is individually labeled with both its evidence phase (Explore/Test/Validate) AND a role classification (Primary/Supporting/Contextual — or a structurally equivalent taxonomy distinguishing signals that directly test the hypothesis from those that corroborate or provide context). The annotation inventory is an enumerable mandatory pre-synthesis output, not a coverage summary inferred from overall signal distribution. The ceiling declaration (C-42) is extended to include role-weighted evidence counts (e.g., Primary signal counts per phase), making the ceiling value derivable by inspection of the annotation set. NOT: ceiling declared (C-42) without a per-signal annotation pass — coverage asserted from gestalt impression without an enumerable, per-signal label set. NOT: per-signal phase annotation present but role classification absent — phase-only annotation without a taxonomy distinguishing signal strength or directness does not satisfy this criterion. NOT: annotation inventory present but not positioned as a mandatory pre-synthesis step feeding the C-42 declaration — annotation placed after ceiling computation or independent from it. |
| C-45 | Two-dimensional ceiling table (phase x orthogonal coverage dimension) | C-39 | The phase-gated confidence ceiling table (C-39) is extended with an orthogonal second classification dimension — such as inertia coverage (whether any signal includes a direct comparison to the status-quo competitor) — so that the ceiling is determined by the intersection of both dimensions rather than by phase alone. Distinct ceiling values apply when the second dimension is present vs. absent at the same evidence phase level, demonstrating the second dimension's independent influence. The mandatory declaration (C-42) is extended to name both dimension values alongside the ceiling. NOT: 1D phase-only ceiling table (C-39 minimum) — second dimension absent, ceiling varies only by phase. NOT: second dimension described in narrative guidance without being instantiated as explicit classification states with distinct ceiling values per intersection cell in the table. NOT: two classification dimensions present but the second is a sub-category or qualifier of phase rather than an orthogonal dimension — the test is whether at a single fixed phase level, different values of the second dimension produce different ceilings. |

---

## R12 Calibration Under v13 (Carried Forward)

| Variation | v12 score | C-44 | C-45 | v13 score |
|-----------|-----------|------|------|-----------|
| V-01 Phase-ceiling integration | ~122.5 | FAIL | FAIL | **~122.5** |
| V-02 Output format | ~90.0 | FAIL | FAIL | **~90.0** |
| V-03 Phrasing register | ~122.5 | FAIL | FAIL | **~122.5** |
| V-04 Lifecycle emphasis + Phase ceiling | ~122.5 | **PASS** | FAIL | **~125.0** |
| V-05 Inertia framing + Phase ceiling | ~122.5 | FAIL | **PASS** | **~125.0** |

**V-04 C-44 PASS**: C-39 and C-42 prerequisites satisfied. Phase 1 annotates every signal with both evidence phase (Explore/Test/Validate) and signal role (Primary/Supporting/Contextual) as an enumerable mandatory pre-synthesis step. The C-42 declaration is extended to include "Primary signals by phase: [count per phase]", making the ceiling derivable by inspection of the annotation set rather than asserted from a gestalt impression.

**V-04 C-45 FAIL**: No inertia coverage dimension. The second classification dimension is signal role (Primary/Supporting/Contextual), which does not produce distinct ceiling values at fixed phase level by itself — the ceiling table's final row extends to "All phases with at least one Primary signal in Validate" but inertia-absent vs. inertia-present is not a classification axis. An orthogonal inertia dimension with distinct intersection ceilings is absent.

**V-05 C-44 FAIL**: The pre-synthesis step classifies signals along two dimensions (evidence phase and inertia coverage: absent/present), but does not use the Primary/Supporting/Contextual role taxonomy. The C-42 declaration names inertia coverage state, not Primary signal counts by phase. Role classification is absent from the annotation step.

**V-05 C-45 PASS**: C-39 prerequisite satisfied. The ceiling table uses two orthogonal dimensions: evidence phase (rows) and inertia coverage (columns: absent/present). At Test phase, distinct ceiling values appear: inertia-absent = 45, inertia-present = 60 — confirming independent influence of the inertia dimension at a fixed phase level. The C-42 declaration is extended to name the inertia coverage state (absent/partial/present) alongside phase and ceiling value.

**V-01/V-02/V-03 C-44 FAIL**: No per-signal annotation pass with role classification present. Phase classification is performed at the inventory level (coverage summary), not per-signal with role taxonomy.

**V-01/V-02/V-03 C-45 FAIL**: Ceiling table is 1D (phase only). No orthogonal inertia or equivalent second dimension defined.

---

## New in v12 (Carried Forward) — Two Aspirational Criteria from R11 Excellence Signals

| ID | Name | Extends | Pass Condition Summary |
|----|------|---------|------------------------|
| C-42 | Ceiling declaration as mandatory intermediate output | C-39 | The phase-ceiling mechanism (C-39) is enforced by a mandatory intermediate output step: the synthesizer must produce a named statement — before synthesis reasoning begins — that declares the evidence phase and the resulting confidence ceiling. The declaration is an explicitly named step with a fixed output form (e.g., "State before proceeding: 'Evidence phase coverage: ... Confidence ceiling: ...'"). This transforms the ceiling from a background constraint into an auditable pre-synthesis commitment. NOT: ceiling mechanism defined (C-39) without a mandatory intermediate output step that names both the evidence phase and the ceiling value. NOT: declaration instruction placed in the output section or in calibration guidance rather than as a named pre-synthesis step. NOT: ceiling declared implicitly in synthesis reasoning rather than as an explicitly required intermediate output before reasoning begins. |
| C-43 | Gate block per-role dual exemplars | C-36, C-40 | The unified gate block (C-40) instantiates the dual-exemplar pattern (C-36) at per-role scope: each role's entry in the gate block contains both a negative exemplar (a concrete instance of the failure mode) and a positive exemplar (a concrete instance of the non-failure alternative), co-located within that role's gate block entry. The dual-exemplar pair is present for every named role in the gate block. NOT: gate block with only a single exemplar (positive or negative) per role — C-40 minimum but not C-43. NOT: dual exemplars present for some roles but not all named roles in the gate block. NOT: dual exemplars present but not co-located within each role's gate block entry — exemplars separated from their role's gate block entry do not satisfy this criterion. |

---

## R11 Calibration Under v12 (Carried Forward)

| Variation | v11 score | C-42 | C-43 | v12 score |
|-----------|-----------|------|------|-----------|
| V-01 Phase-gated confidence ceiling | ~102.5 | **PASS** | FAIL | **~105.0** |
| V-02 Concurrent execution with unified gate block | ~115.0 | FAIL | **PASS** | **~117.5** |
| V-03 Lifecycle Emphasis | ~8.0 | FAIL | FAIL | **~8.0** |

**V-01 C-42 PASS**: C-39 prerequisite satisfied. Mandatory declaration step present: "State before proceeding: 'Evidence phase coverage: ... Confidence ceiling: ...'" — names the evidence phase and ceiling value as a required intermediate output before synthesis reasoning begins.

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

## New in v9 (Carried Forward) — Per-Criterion Calibration Tables

### C-35 — Concurrent role execution with seamless output (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **FAIL** | Sequential: SYNTHESIST → ADVERSARY → ANALYST |
| V-02 | **PASS** | "Three cognitive roles execute concurrently in your reasoning" + "output contains no labeled role sections and no visible role seams" |
| V-03 | **FAIL** | "Roles (Sequential)" heading |

### C-36 — Dual-exemplar adversarial gate (Aspirational)

| | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | "Exemplar (invalid): ... [Applies to every investigation — fails the gate.]" + "Exemplar (valid): ... [Hypothesis-specific — passes the gate.]" co-located in ADVERSARY section |
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
| V-01 | **PASS** | Phase classification table (Explore/Test/Validate → ceilings 25/50/72/none) in pre-synthesis step; "State before proceeding: 'Evidence phase coverage: ... Confidence ceiling: ...'" enforces declaration before reasoning begins |
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
| V-01 | **PASS** | Mandatory declaration step: "State before proceeding: 'Evidence phase coverage: ... Confidence ceiling: ...'" — names both evidence phase and ceiling value; positioned before synthesis reasoning; C-39 prerequisite satisfied |
| V-02 | **FAIL** | C-39 FAIL → dependency cascade; no phase-ceiling mechanism defined, no declaration step possible |
| V-03 | **FAIL** | Incomplete |

### C-43 — Gate block per-role dual exemplars (Aspirational, NEW v12)

| | Result | Evidence |
|---|---|---|
| V-01 | **FAIL** | C-40 FAIL → dependency cascade; sequential execution, no unified gate block |
| V-02 | **PASS** | Gate block entries for all three roles (SYNTHESIST, ADVERSARY, ANALYST) each contain both a negative exemplar and a positive exemplar, co-located within each role's gate block entry; C-40 and C-36 prerequisites satisfied |
| V-03 | **FAIL** | Incomplete |

### C-44 — Per-signal annotated inventory with role classification (Aspirational, NEW v13)

| | Result | Evidence |
|---|---|---|
| V-04 (R12) | **PASS** | Phase 1 annotates each signal with evidence phase (Explore/Test/Validate) AND signal role (Primary/Supporting/Contextual) as enumerable mandatory pre-synthesis step; C-42 declaration extended to "Primary signals by phase: [count per phase]"; C-39/C-42 prerequisites satisfied |
| V-01/V-02/V-03/V-05 (R12) | **FAIL** | No per-signal annotation pass with role classification (Primary/Supporting/Contextual or equivalent) present; ceiling computed from phase coverage summary, not derived from enumerable per-signal annotation inventory |

### C-45 — Two-dimensional ceiling table (phase x orthogonal coverage dimension) (Aspirational, NEW v13)

| | Result | Evidence |
|---|---|---|
| V-05 (R12) | **PASS** | Ceiling table uses two orthogonal dimensions: evidence phase (Explore/Test/Validate) and inertia coverage (absent/present); distinct ceilings at Test level: inertia-absent = 45, inertia-present = 60 confirms independent influence; C-42 declaration extended to include inertia coverage state; C-39 prerequisite satisfied |
| V-01/V-02/V-03/V-04 (R12) | **FAIL** | Ceiling table is 1D (phase only); no orthogonal second dimension with distinct intersection ceiling values present |

### C-46 — Annotation-to-ceiling derivation linkage (Aspirational, NEW v14)

| | Result | Evidence |
|---|---|---|
| V-04 (R13) | **PASS** | Ceiling computation step states: "The ceiling computation in the next step is derived from the per-signal annotation inventory, not inferred from a gestalt impression." Explicit derivation linkage positioned in ceiling computation step between Phase 1 annotation and Phase 2 synthesis reasoning; C-44 prerequisite satisfied |
| V-01 (R13) | **FAIL** | C-44 PASS prerequisite satisfied; no explicit "derived not inferred" provenance statement in ceiling computation step; declaration extended with Primary counts but ceiling computation step does not attribute the ceiling value to the annotation inventory |
| V-02 (R13) | **FAIL** | C-44 FAIL → dependency cascade; no per-signal role annotation inventory present |
| V-03 (R13) | **FAIL** | C-44 FAIL → dependency cascade |

### C-47 — Extended declaration coverage in slot-indexed self-containment check (Aspirational, NEW v14)

| | Result | Evidence |
|---|---|---|
| V-04 (R13) | **PASS** | Q6 maps Phase 1 declaration (phase + Primary counts + inertia state) to Verdict/Confidence paragraph — all annotation-derived dimension values covered; C-37 PASS and C-42 extended (all three dimensions) prerequisites satisfied |
| V-01 (R13) | **PASS** | Q6 maps Primary counts by phase to Verdict/Confidence paragraph; C-37 PASS and C-42 extended (Primary counts by phase) prerequisites satisfied; annotation-derived value traceable from inventory → declaration → Q6 → named slot |
| V-02 (R13) | **PASS** | Q6: "Is the phase + inertia declaration traceable to the confidence score? → Verdict/Confidence paragraph"; C-37 PASS and C-42 extended (inertia coverage state) prerequisites satisfied; annotation-derived inertia state named in question scope with mapped slot |
| V-03 (R13) | **FAIL** | C-42 not extended with annotation-derived values (phase + ceiling only); no Q6 covering annotation-derived declaration extension; prerequisite for extended self-containment coverage not met |

---

## Composite Score Computation

**Anchors from R13 calibration (v14 adjusted):**
- R12 V-01 base (v14): ~122.5 — earns full C-35/C-39/C-40/C-41/C-42/C-43 cluster; C-44 through C-47 absent
- R13 V-03 (v14): ~122.5 — confirms register-independence of full criteria battery; no new criteria earned
- R13 V-01 (v14): ~127.5 — base + C-44 (+2.5) + C-47 (+2.5)
- R13 V-02 (v14): ~127.5 — base + C-45 (+2.5) + C-47 (+2.5)
- R13 V-04 (v14): ~130.0 — base + C-44 (+2.5) + C-45 (+2.5) + C-46 (+2.5) + C-47 (+2.5)

Each criterion (essential and aspirational) treated as 2.5 pts for composite delta computation.

### V-04 (R13) — Combined 3-column annotation (phase + role + inertia)

| Criterion | R13 base | C-46 delta | C-47 delta | v14 |
|-----------|----------|------------|------------|-----|
| C-35 | PASS | 0 | 0 | PASS |
| C-36 | PASS | 0 | 0 | PASS |
| C-37 | PASS | 0 | 0 | PASS |
| C-38 | PASS | 0 | 0 | PASS |
| C-39 | PASS | 0 | 0 | PASS |
| C-40 | PASS | 0 | 0 | PASS |
| C-41 | PASS | 0 | 0 | PASS |
| C-42 | PASS | 0 | 0 | PASS |
| C-43 | PASS | 0 | 0 | PASS |
| C-44 | PASS | 0 | 0 | PASS |
| C-45 | PASS | 0 | 0 | PASS |
| C-46 | FAIL | **+2.5** | 0 | **PASS** |
| C-47 | FAIL | 0 | **+2.5** | **PASS** |

**v14 V-04 = 127.5 + 2.5 + 2.5 = ~130.0**

Essential status: C-11 / C-13 / C-30 — all-essential PASS.
Golden: 130.0 >= 90 — GOLD

### V-01 (R13) — Single-axis role taxonomy

| Criterion | R13 base | C-47 delta | v14 |
|-----------|----------|------------|-----|
| C-35 through C-44 | PASS | 0 | PASS |
| C-45 | FAIL | 0 | FAIL |
| C-46 | FAIL | 0 | FAIL |
| C-47 | FAIL | **+2.5** | **PASS** |

**v14 V-01 = 125.0 + 2.5 = ~127.5**

Essential status: all-essential PASS. Golden: 127.5 >= 90 — GOLD

### V-02 (R13) — Single-axis inertia framing

| Criterion | R13 base | C-47 delta | v14 |
|-----------|----------|------------|-----|
| C-35 through C-43 | PASS | 0 | PASS |
| C-44 | FAIL | 0 | FAIL |
| C-45 | PASS | 0 | PASS |
| C-46 | FAIL | 0 | FAIL |
| C-47 | FAIL | **+2.5** | **PASS** |

**v14 V-02 = 125.0 + 2.5 = ~127.5**

Essential status: all-essential PASS. Golden: 127.5 >= 90 — GOLD
```
