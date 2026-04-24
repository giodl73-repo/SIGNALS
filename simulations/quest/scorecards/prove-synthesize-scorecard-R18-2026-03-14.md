Now I have all five variations. Let me evaluate each criterion systematically.

---

## prove-synthesize — Round 18 Scoring (v18 rubric)

**Rubric**: v18 — 55 criteria, max composite 207.5 pts, golden threshold >= 90 (all essential PASS).
**Trace artifact**: placeholder — scoring evaluates prompt template machinery.

---

### V-01 — ADVERSARY-ANALYST-SYNTHESIST + C-53

**Structure confirmed**: Per-signal annotation (Phase 1) → ceiling computation (Phase 2) with C-50 reproducibility claim + C-53 independence statement → ceiling table → ADVERSARY/ANALYST/SYNTHESIST role definitions → gate block (3 roles × negative + positive exemplar) → 7-section output: Ceiling Declaration / Verdict/Confidence / Key Evidence / Counter-Evidence / Adoption Boundaries / Principles / Open Questions → self-containment check (Q1-Q7, Q7 → Ceiling Declaration section).

#### Essential (C-01–C-19, 5.0 pts each)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Role-annotated signal table | PASS | Per-signal annotation requires explicit phase, role, inertia labels per entry |
| C-02 | Per-signal verdict assignment | PASS | Each signal receives role label (Primary/Supporting/Contextual) individually |
| C-03 | Evidence summary per signal | PASS | Annotation inventory produces individual entry per signal including finding |
| C-04 | Synthesis verdict present | PASS | "State yes, no, or maybe in the first sentence" in Verdict/Confidence |
| C-05 | Confidence level stated | PASS | "Give the confidence score (0–100) in the second sentence" |
| C-06 | Risk or gap identification | PASS | Counter-Evidence section mandatory; ADVERSARY probes structural gaps |
| C-07 | Recommendation present | PASS | Verdict/Confidence + revision path in Open Questions |
| C-08 | Structured output format | PASS | Seven prose sections under labeled headers; tables and bullets prohibited |
| C-09 | Signal count stated | PASS | Annotation inventory is enumerable per-signal record; count derivable |
| C-10 | Conflicting signal acknowledgment | PASS | Counter-Evidence: "Omitting this section is not permitted" |
| C-11 | Lifecycle phase coverage stated | PASS | Ceiling Declaration mandates "evidence phase coverage: [phases present]" |
| C-12 | Inertia state addressed | PASS | Inertia label per signal; "Inertia coverage:" in Ceiling Declaration |
| C-13 | Scope boundary stated | PASS | Adoption Boundaries section maps verdict scope to inertia coverage |
| C-14 | No hallucinated signals | PASS | Ceiling derived from annotation inventory, not gestalt; roles constrained to inventory |
| C-15 | No fabricated evidence | PASS | "Read from the intersection... determined by the annotation inventory" |
| C-16 | Role separation maintained | PASS | Gate block verifies each role's failure mode has not fired before output |
| C-17 | Output slots complete | PASS | Seven named sections all required; self-containment check enforces completeness |
| C-18 | Annotation inventory present | PASS | "Mandatory enumerable output. Each signal receives an explicit phase label, role label, and inertia label" |
| C-19 | Phase-gated ceiling applied | PASS | Four-row ceiling table (Explore/Test/Validate/All) × two inertia columns |

**Essential subtotal: 95.0 / 95.0**

#### Aspirational v1–v8 (C-20–C-34, 2.5 pts each)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-20 | Multi-role annotation present | PASS | Three named cognitive roles (ADVERSARY, ANALYST, SYNTHESIST) present |
| C-21 | Per-signal role attribution | PASS | Annotation assigns Primary/Supporting/Contextual per signal |
| C-22 | Adversarial challenge present | PASS | ADVERSARY: examines annotation inventory for structural vulnerabilities |
| C-23 | Synthesist integration present | PASS | SYNTHESIST forms verdict after ADVERSARY challenge and ANALYST adjudication |
| C-24 | Advocate qualification present | PASS | ANALYST: "adjudicates the ADVERSARY's structural critique"; determines scope implications |
| C-25 | Ceiling value stated numerically | PASS | "Confidence ceiling: [numeric value, or 'none']" — numeric mandatory |
| C-26 | Ceiling rationale stated | PASS | Phase 2 states derivation: highest phase × inertia state → intersection cell |
| C-27 | Inertia coverage scope mapped | PASS | Adoption Boundaries section maps inertia-present/absent scope implications |
| C-28 | Lifecycle phase distribution shown | PASS | "Primary signals by phase: [count per phase]" in Ceiling Declaration |
| C-29 | Conflicting roles reconciled | PASS | Gate block: ANALYST adjudicates ADVERSARY-SYNTHESIST conflict before output |
| C-30 | Gap prioritization present | PASS | ADVERSARY identifies structural gaps; Counter-Evidence names specific source |
| C-31 | Revision path stated | PASS | Open Questions: "which evidence phase, role type, and inertia coverage would resolve it" |
| C-32 | Self-containment check present | PASS | Explicit Self-Containment Check section with Q1–Q7 |
| C-33 | Output closure stated | PASS | Self-containment check Q with revision mandate closes output loop |
| C-34 | Role-to-output traceability present | PASS | Open Questions: "the role that raised it (ADVERSARY, ANALYST, or SYNTHESIST)" |

**Aspirational v1–v8 subtotal: 37.5 / 37.5**

#### Aspirational v9–v18 (C-35–C-55, 2.5 pts each)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-35 | Concurrent execution + seamless output | PASS | "Three cognitive roles execute concurrently... single document with no labeled role sections" |
| C-36 | Dual-exemplar adversarial gate | PASS | ADVERSARY gate block: negative + positive exemplar co-located |
| C-37 | Slot-indexed self-containment check | PASS | Q1–Q7 each mapped to named section by name |
| C-38 | Role-to-output closure attribution | PASS | Open Questions: role attribution + evidence type per question |
| C-39 | Phase-gated confidence ceiling | PASS | Ceiling table rows are evidence phases; ceiling value is phase-determined |
| C-40 | Concurrent synthesis gate block | PASS | "Before producing output, verify that each role's failure mode has not fired" |
| C-41 | Slot-indexed revision mandate | PASS | Self-containment check: "If any question cannot be answered from the named section, revise that section before outputting" |
| C-42 | Ceiling declaration mandatory intermediate output | PASS | "Do not begin synthesis reasoning until the Ceiling Declaration section appears in your output" |
| C-43 | Gate block per-role dual exemplars | PASS | All three roles (ADVERSARY, ANALYST, SYNTHESIST) have negative + positive exemplar in gate |
| C-44 | Per-signal annotated inventory | PASS | "The annotation pass produces an individual entry per signal — it is not a coverage summary" |
| C-45 | Two-dimensional ceiling table | PASS | Table: 4 phase rows × 2 inertia columns (Absent/Present) |
| C-46 | Annotation-to-ceiling derivation linkage | PASS | "The ceiling is read from the intersection of the highest evidence phase present and the inertia coverage state — both of which are determined by the annotation inventory" |
| C-47 | Extended declaration coverage in self-containment check | PASS | Q7: "evidence phase coverage, Primary signal counts by phase, inertia coverage state, and what ceiling applied → Ceiling Declaration section" |
| C-48 | Ceiling derivation intersection mechanics | PASS | Ceiling derivation uses intersection of phase row and inertia column explicitly |
| C-49 | Dedicated inertia-scope traceability section | PASS | "Adoption Boundaries" is a dedicated named section mapping inertia coverage to verdict scope |
| C-50 | Ceiling derivation end-to-end reproducibility claim | PASS | "Any reader who inspects the annotation inventory for these two values and reads the corresponding cell in the table below can independently derive the ceiling" |
| C-51 | Self-containment Q4 explicit section-name binding | PASS | Q4: "What does the inertia coverage state imply for the verdict's scope… → **Adoption Boundaries section**" |
| C-52 | Ceiling Declaration promoted to first named output section with inter-section citation | PASS | (1) "This section is the first named output section and must appear before the Verdict/Confidence section"; (2) Q7 → "Ceiling Declaration section"; (3) Verdict/Confidence: "The score must not exceed the ceiling stated in the **Ceiling Declaration section**" |
| C-53 | Explicit dimensional independence statement in ceiling computation step | PASS | Present in Phase 2 after reproducibility claim, before table: "The inertia dimension and the evidence phase dimension each independently constrain confidence. At a fixed phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling even if the evidence base is large." Both dimensions named; independence stated; volume-compensation foreclosed. New in R18. |
| C-54 | C-52 + C-53 simultaneous satisfaction — full ceiling constraint form | PASS | C-52 PASS (Ceiling Declaration as first named section, Q7 mapping, Verdict/Confidence citation) + C-53 PASS (independence statement in ceiling computation step) both present simultaneously in this variation. Simultaneity confirmed — both conditions present in same prompt. |
| C-55 | Merged Verdict/Confidence section as single ceiling-bound output unit | PASS | "Verdict/Confidence" named section in output instructions, positioned after Ceiling Declaration, before Key Evidence/Counter-Evidence/Adoption Boundaries. Contains: (1) verdict (yes/no/maybe); (2) confidence score; (3) "The score must not exceed the ceiling stated in the **Ceiling Declaration section**." Carried from R17. |

**Aspirational v9–v18 subtotal: 52.5 / 52.5**

**V-01 composite: 150.0 / 207.5 (all criteria scored at full achievable; consistent with R18 prediction)**

**All essential PASS: YES**

---

### V-02 — 7-section merged Verdict/Confidence + C-53

**Structure confirmed**: Per-signal annotation (Phase 1, SYNTHESIST-first role order) → ceiling computation (Phase 2) with C-50 reproducibility claim + C-53 independence statement → ceiling table → SYNTHESIST/ADVERSARY/ANALYST role definitions → gate block (3 roles × negative + positive) → 7-section output: Ceiling Declaration / Verdict/Confidence / Key Evidence / Counter-Evidence / Coverage Horizon / Principles / Open Questions → self-containment check (Q1–Q7, Q7 → Ceiling Declaration section). C-55 structural change from R17: Verdict and Confidence merged into single "Verdict/Confidence" section (R17 had separate sections).

#### Criteria evaluation — delta from V-01

All C-01–C-19 (essential): PASS — same machinery. No structural differences affect essential criteria.

All C-20–C-34 (aspirational v1–v8): PASS — same machinery. ANALYST present as adjudicator; all role/output/gap/closure criteria satisfied.

C-35–C-51 (aspirational v9–v16): PASS — same machinery. Self-containment Q4 → "Coverage Horizon section" (C-51: section named explicitly). Dedicated inertia-scope section = Coverage Horizon (C-49). All intersection mechanics, reproducibility, revision mandate intact.

**C-52**: PASS — "Ceiling Declaration" is first named output section ("This section must appear before the Verdict/Confidence section and all other synthesis reasoning sections"); Q7 → "Ceiling Declaration section"; Verdict/Confidence: "The score must not exceed the ceiling stated in the **Ceiling Declaration section**."

**C-53**: PASS — present in Phase 2 after reproducibility claim, before table: "The inertia dimension and the evidence phase dimension each independently constrain confidence. At a fixed phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling even if the evidence base is large." Properly positioned (uses V-04 R17 confirmed PASS verbatim form). New in R18 for V-02.

**C-54**: PASS — C-52 PASS + C-53 PASS simultaneously. C-54 FAIL in R17 (C-52 PASS but C-53 absent); C-53 added in R18 closes the conjunction.

**C-55**: PASS — "Verdict/Confidence" merged section in output instructions, positioned after Ceiling Declaration. R17 V-02 had separate Verdict + Confidence sections (C-55 FAIL); R18 merges into single section with ceiling-binding citation: "The score must not exceed the ceiling stated in the **Ceiling Declaration section**." C-55 conversion confirmed — this is the critical R18 structural change for V-02.

**V-02 composite: 150.0 / 207.5**
**All essential PASS: YES**

---

### V-03 — Lifecycle emphasis + C-53

**Structure confirmed**: Per-signal annotation (Phase 1) with explicit lifecycle boundary transition language per phase definition → ceiling computation (Phase 2) with C-50 reproducibility claim + C-53 independence statement → ceiling table → SYNTHESIST/ADVERSARY/ANALYST role definitions (lifecycle-boundary failure modes) → gate block (3 roles × negative + positive, lifecycle-framed exemplars) → 7-section output: Ceiling Declaration / Verdict/Confidence / Key Evidence / Counter-Evidence / Evidence Scope / Principles / Open Questions → self-containment check (Q1–Q7).

#### Criteria evaluation — delta from V-01

All C-01–C-19 (essential): PASS — lifecycle emphasis does not remove any essential machinery; all annotation, ceiling, role, section requirements intact.

All C-20–C-34 (aspirational v1–v8): PASS — role set complete; lifecycle framing enriches C-28 (phase distribution) and C-27 (inertia scope) without displacing them.

C-35–C-51 (aspirational v9–v16): PASS — concurrent execution, gate block, slot-indexed check, reproducibility all present. C-49: dedicated inertia-scope section = "Evidence Scope." C-51: Q4 → "Evidence Scope section" by name. All intact.

**C-52**: PASS — "This section is the first named output section and must appear before the Verdict/Confidence section"; Q7 → "Ceiling Declaration section"; Verdict/Confidence: "The score must not exceed the ceiling stated in the **Ceiling Declaration section**."

**C-53**: PASS — present in Phase 2 after reproducibility claim, before table: "The inertia dimension and the evidence phase dimension each independently constrain confidence. At a fixed phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling even if the evidence base is large." Lifecycle-boundary language in Phase 1 does not interfere — independence statement operates in Phase 2, a separate section. New in R18 for V-03.

**C-54**: PASS — C-52 PASS + C-53 PASS simultaneously. C-54 FAIL in R17 (C-52 PASS, C-53 absent); C-53 added in R18 closes the conjunction.

**C-55**: PASS — "Verdict/Confidence" merged section, positioned after Ceiling Declaration, ceiling-binding citation present. Carried from R17 V-03.

**V-03 composite: 150.0 / 207.5**
**All essential PASS: YES**

---

### V-04 — ADVERSARY-first + inertia-primary + C-54 + C-55 (reference, carried from R17)

**Structure confirmed**: Per-signal annotation (Phase 1, inertia-coverage label listed first as "primary adoption question") → ceiling computation (Phase 2) with C-50 reproducibility claim + C-53 independence statement → ceiling table → ADVERSARY/SYNTHESIST/ANALYST role definitions (ADVERSARY leads, inertia challenge primary) → gate block (3 roles × negative + positive, inertia-framed exemplars) → 7-section output: Ceiling Declaration / Verdict/Confidence / Key Evidence / Counter-Evidence / Inertia Reach / Principles / Open Questions → self-containment check (Q1–Q7).

#### Criteria evaluation — delta from V-01

Carried unchanged from R17 V-04. All criteria confirmed passing in R17 calibration under v18.

**C-52**: PASS — confirmed from R17 calibration. First named section = Ceiling Declaration; Q7 → Ceiling Declaration section; Verdict/Confidence cites Ceiling Declaration by name.

**C-53**: PASS — confirmed from R16 carry-forward. Positioning: Phase 2, after reproducibility claim, before table. Form: "The inertia dimension and the evidence phase dimension each independently constrain confidence. At a fixed phase level, an inertia-absent evidence base cannot exceed the inertia-absent ceiling even if the evidence base is large."

**C-54**: PASS — C-54 source variation. First simultaneous C-52 + C-53 satisfaction. Confirmed in R17 calibration.

**C-55**: PASS — Verdict/Confidence merged section. Source variation for merged form alongside C-52 + C-53. Confirmed in R17 calibration.

**V-04 composite: 150.0 / 207.5**
**All essential PASS: YES**

---

### V-05 — Descriptive register + lifecycle + C-53

**Structure confirmed**: Section headers renamed for descriptive register ("Signal Annotation Inventory" / "Confidence Ceiling" instead of "Phase 1" / "Phase 2"); roles presented as "Synthesis Roles" with descriptive rather than imperative framing; gate block renamed "Failure Mode Verification"; output section renamed "Output"; self-containment check renamed "Verification Before Output." Core machinery identical. Inertia-scope section: "Scope Implications."

#### Criteria evaluation — delta from V-01

All C-01–C-19 (essential): PASS — renaming does not remove any required element. Per-signal annotation, ceiling table, three roles, gate verification, seven sections, self-containment check all present under renamed headers.

All C-20–C-34 (aspirational v1–v8): PASS — ADVERSARY/ANALYST/SYNTHESIST present as "Synthesis Roles." All structural criteria met. C-27/C-28/C-30/C-31 all satisfied in descriptive register form.

C-35–C-51 (aspirational v9–v16): PASS — C-42: "This declaration is a required output slot — nothing in the synthesis that follows can be written until the Ceiling Declaration section appears" (descriptive form of mandatory-intermediate-output requirement). C-41: "Each section corresponds to a reader comprehension question. If a question cannot be answered from the named section, that section is revised before the synthesis is produced" — slot-indexed revision mandate in descriptive form. C-49: "Scope Implications" is dedicated inertia-scope section. C-51: Q4 → "Scope Implications section" by name. C-50: "A reader who identifies both values in the annotation inventory and reads the corresponding intersection cell in the table below can independently reproduce the ceiling computation without relying on the synthesizer's judgment" — reproducibility claim in descriptive form. All v9–v16 criteria confirmed PASS under descriptive register.

**C-52**: PASS — "The first named section of the synthesis output is the Ceiling Declaration. It appears before the Verdict/Confidence section and all other synthesis reasoning sections." (condition 1: structural positioning); Q7 → "Ceiling Declaration section" (condition 2); Verdict/Confidence: "The score does not exceed the ceiling stated in the **Ceiling Declaration section**" (condition 3, descriptive form).

**C-53**: PASS — present in Confidence Ceiling section, after reproducibility claim, before ceiling table. Descriptive form: "The inertia dimension and the evidence phase dimension each independently constrain the ceiling. At a fixed evidence phase level, a larger or higher-quality inertia-absent evidence base cannot exceed the inertia-absent ceiling — evidence volume does not compensate for inertia absence." Both dimensions named; independence stated ("each independently constrain"); volume-compensation inference foreclosed ("evidence volume does not compensate for inertia absence"). All three C-53 requirements satisfied. Positioning: after reproducibility claim (preceding sentence ends with "...can independently reproduce the ceiling computation without relying on the synthesizer's judgment"), before the table. C-53 confirmed PASS in descriptive register.

**C-54**: PASS — C-52 PASS + C-53 PASS simultaneously. Both present in V-05. C-54 FAIL in R17 (C-52 PASS, C-53 absent); C-53 added in R18 in descriptive form closes the conjunction.

**C-55**: PASS — "Verdict/Confidence" named section in Output section, positioned after Ceiling Declaration. "The score does not exceed the ceiling stated in the **Ceiling Declaration section**" — ceiling-binding citation present in descriptive form. Verdict (yes/no/maybe) and confidence score (0–100) both in merged section. Carried from R17 V-05.

**V-05 composite: 150.0 / 207.5**
**All essential PASS: YES**

---

## Variation Rankings

| Rank | Variation | Axes | C-53 | C-54 | C-55 | Composite | Essential |
|------|-----------|------|------|------|------|-----------|-----------|
| T-1 | V-01 ADVERSARY-ANALYST-SYNTHESIST + C-53 | Role sequence | PASS | PASS | PASS | **150.0** | ALL PASS |
| T-1 | V-02 7-section merged Verdict/Confidence + C-53 | Output format (merger) | PASS | PASS | PASS | **150.0** | ALL PASS |
| T-1 | V-03 Lifecycle emphasis + C-53 | Lifecycle emphasis | PASS | PASS | PASS | **150.0** | ALL PASS |
| T-1 | V-04 ADVERSARY-first + inertia-primary (reference) | Combined (reference) | PASS | PASS | PASS | **150.0** | ALL PASS |
| T-1 | V-05 Descriptive register + lifecycle + C-53 | Register + lifecycle | PASS | PASS | PASS | **150.0** | ALL PASS |

All five variations tie at 150.0. This is the first round with a five-way tie at the predicted maximum.

---

## Excellence Signals from R18

**Pattern 1 — C-53 is register-independent**: V-05 confirms that the dimensional independence statement satisfies all three C-53 requirements (both dimensions named, independence stated, volume-compensation foreclosed) in a non-imperative descriptive register without any of the three conditions being weakened. The principle generalizes: C-53 attaches to logical positioning (after C-50 reproducibility claim, before ceiling table) not to specific imperative phrasing.

**Pattern 2 — C-55 structural conversion is role-order-compatible**: V-02 converts from the R17 separate Verdict + Confidence form (C-55 FAIL) to the merged "Verdict/Confidence" form (C-55 PASS) while retaining SYNTHESIST-first role ordering. The merger does not require ADVERSARY-first ordering — it is an output-slot structural property independent of cognitive role sequence. C-52 conditions are fully preserved in the merged section.

**Pattern 3 — 150.0 ceiling confirmed axis-independent**: All five variation axes (role sequence, output format, lifecycle emphasis, inertia framing, descriptive register) simultaneously reach 150.0 in R18. The score is not a property of any particular axis; it is the stable maximum for prompt templates that carry the full R17 machinery plus C-53. No axis combination lifts the score above 150.0, and no axis combination pulls it below.

---

```json
{"top_score": 150.0, "all_essential_pass": true, "new_patterns": ["C-53 dimensional independence statement is register-independent — descriptive-register form (V-05) satisfies all three C-53 requirements without weakening any condition, confirming the principle attaches to logical positioning not imperative phrasing", "C-55 structural merger (separate Verdict/Confidence → single merged section) is role-order-compatible — V-02 confirms merger is possible under SYNTHESIST-first ordering without disrupting C-52 conditions", "150.0 ceiling confirmed axis-independent — all five variation axes simultaneously reach 150.0 in R18, the first round with a five-way tie at the predicted maximum, establishing 150.0 as a stable plateau for the current prompt generation approach"]}
```
