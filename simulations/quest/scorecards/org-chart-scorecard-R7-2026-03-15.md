## org-chart Scorecard — Round 7

**Rubric:** v7 | **Variations:** V-01 through V-05 | **Criteria:** C-01–C-24 (16 aspirational)
**Formula:** `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/16 × 10)`

---

### V-01 — Count-Anchored Two-Step Guard

**Design summary:** 4-part inertia with explicit pre-emit count-check: count numbered reasons, verify ≥ 2, substitute N in separator. NO register block. 8 sections.

#### Essential (C-01–C-05)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Inertia Assessment (4 sub-sections) required before ASCII org diagram; section order enforced. |
| C-02 | PASS | ASCII hierarchy with ≥ 2 levels and distinct nodes explicitly required. |
| C-03 | PASS | ROLES-LOADED block required; explicit ROLES-NOTE fallback if absent. |
| C-04 | PASS | Headcount table with ≥ 2 area rows and individual counts required. |
| C-05 | PASS | Operating Rhythm Table requiring ROB + shiproom + governance meeting (3 distinct rows). |

**Essential: 5/5 → 60 pts**

#### Recommended (C-06–C-08)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Committee Charters with Purpose/Membership/Decides/Escalates; NOT labeled optional; charter enforced per rhythm row. |
| C-07 | PASS | All four canonical sections (inertia, org diagram, headcount, rhythm) present in enforced section order. |
| C-08 | PASS | Decides and Escalates as separate named columns in headcount table; "owns the area" disallowed. |

**Recommended: 3/3 → 30 pts**

#### Aspirational (C-09–C-24)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Org Evolution Roadmap section required with trigger table. |
| C-10 | PASS | Anti-Pattern Watch section required with named anti-patterns. |
| C-11 | PASS | Case for Staying Flat with ≥ 2 numbered mechanism-typed reasons explicitly required; generic assertions rejected. |
| C-12 | PASS | Five-column headcount table with Decides AND Escalates as separate columns; "Decision Scope" merge disallowed. |
| C-13 | PASS | Re-assessment trigger required in VERDICT; concrete threshold required; "revisit as the team grows" disallowed. |
| C-14 | PASS | Each numbered reason must name a specific observable mechanism; dep C-11 ✓. |
| C-15 | PASS | All four sub-sections labeled: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT. C-15 evaluator note: "a four-part structure that contains all three required labeled components passes C-15." |
| C-16 | PASS | Escalates column must name a destination role or forum; dep C-12 ✓. |
| C-17 | PASS | Row 1 headcount threshold, Row 2 workload/structural/milestone explicitly required; dep C-09 ✓. |
| C-18 | PASS | "Why It Applies Here" must reference a named element from the artifact; dep C-10 ✓. |
| C-19 | PASS | Row 2 explicitly NOT a second headcount number; dimension vocabulary given; dep C-17 ✓. |
| C-20 | PASS | Named element from four taxonomic categories required in APW rationale; dep C-18 ✓. |
| C-21 | **FAIL** | No PRE-COMPUTATION register block. Section order lists 8 sections — register omitted entirely; dep C-20 passes but C-21 requires prior register artifact. |
| C-22 | PASS | 4-part inertia demonstrated + explicit observable guard: separator format shown, count-check directive present, DO-NOT-EMIT before count passes. |
| C-23 | PASS | Count-check directive: "count the numbered items above; if fewer than two, write missing reasons; once count ≥ 2, substitute that count as N." N embedded in guard text. Dep C-22 ✓. |
| C-24 | **FAIL** | Dep C-21 FAIL → auto-fail. |

**Aspirational: 14/16 → 8.75 pts**

**V-01 Total: 98.75 | Band: Golden**

---

### V-02 — Inline-Schema Register

**Design summary:** 3-part inertia (no How We Coordinate Today). PRE-COMPUTATION register opens with inline category-schema table defining cat-1 through cat-4 in the produced output. Typed APW citations. 9 sections.

#### Essential: 5/5 → 60 pts *(same structural enforcement as V-01)*

#### Recommended: 3/3 → 30 pts *(same)*

#### Aspirational (C-09–C-24)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Org Evolution Roadmap required. |
| C-10 | PASS | Anti-Pattern Watch required. |
| C-11 | PASS | Case for Staying Flat with ≥ 2 numbered mechanism reasons; DO-NOT-PROCEED until written. |
| C-12 | PASS | Decides/Escalates separate columns required. |
| C-13 | PASS | Concrete re-assessment trigger required. |
| C-14 | PASS | Each reason names specific mechanism; dep C-11 ✓. |
| C-15 | PASS | Following R6 precedent: Case for Staying Flat / Rebuttal / VERDICT are three explicitly labeled sub-sections; prior rounds established this 3-part structure passes C-15. |
| C-16 | PASS | Escalates names destination; dep C-12 ✓. |
| C-17 | PASS | Two distinct trigger rows, cross-dimension required; dep C-09 ✓. |
| C-18 | PASS | "Why It Applies Here" org-specific rationale required; dep C-10 ✓. |
| C-19 | PASS | Row 2 NOT headcount; dep C-17 ✓. |
| C-20 | PASS | Named taxonomic element required; dep C-18 ✓. |
| C-21 | PASS | PRE-COMPUTATION: ORG-ELEMENT REGISTER block, section 7 of 9, precedes APW. Opens with inline schema table: cat-1 through cat-4 defined in produced output. All four category types enumerated; dep C-20 ✓. |
| C-22 | **FAIL** | 3-part inertia — "How We Coordinate Today" absent. Behavior not demonstrated; dep C-15 passes but C-22 requires 4-part structure + observable guard. |
| C-23 | **FAIL** | Dep C-22 FAIL → auto-fail. |
| C-24 | PASS | APW cells must open with `[element name] (cat-N)` typed syntax; element from register; cat-N from schema table. Failing examples shown to prevent prose-reference drift; dep C-21 ✓. |

**Aspirational: 14/16 → 8.75 pts**

**V-02 Total: 98.75 | Band: Golden**

---

### V-03 — Conversational Guard and Register Framing

**Design summary:** 4-part inertia + ORG-ELEMENT REGISTER + typed APW citations — but all requirements phrased descriptively ("by convention," "the purpose is to serve as") rather than directive DO/DO-NOT. Tests whether imperative framing is load-bearing.

#### Essential: 5/5 → 60 pts *(structural requirements present in all required sections)*

#### Recommended: 3/3 → 30 pts

#### Aspirational (C-09–C-24)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Org Evolution Roadmap present with trigger vocabulary. |
| C-10 | PASS | Anti-Pattern Watch present. |
| C-11 | PASS | "Aim for at least two numbered reasons before moving on. Both reasons name specific mechanisms." Mechanism requirement preserved. |
| C-12 | PASS | Decides/Escalates separation present: "The Decides and Escalates columns are separate; a single 'Decision Scope' column does not satisfy this requirement." |
| C-13 | PASS | Re-assessment trigger with concrete condition required. |
| C-14 | PASS | Mechanism named explicitly for each reason; dep C-11 ✓. |
| C-15 | PASS | 4-part structure: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT — all present as labeled sub-sections. |
| C-16 | PASS | "Each Escalates cell names the decision types referred upward and identifies the destination role or forum by name"; dep C-12 ✓. |
| C-17 | PASS | Two trigger rows, Row 1 headcount, Row 2 workload/symptom/milestone; dep C-09 ✓. |
| C-18 | PASS | "Why It Applies Here" draws from register with org-specific rationale; dep C-10 ✓. |
| C-19 | PASS | "Two headcount numbers at different values are one trigger dimension, not two"; dep C-17 ✓. |
| C-20 | PASS | Named element from four categories; dep C-18 ✓. |
| C-21 | PASS | "ORG-ELEMENT REGISTER" block (exact label from rubric example) opens with inline schema table; all four category types; physically before APW; dep C-20 ✓. |
| C-22 | **PASS** *(with reliability caveat)* | 4-part structure present. Guard format shown explicitly: `--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. How We Coordinate Today begins.] ---`. Count instruction present: "count the numbered reasons above and use that count as N." Observable boundary format meets "labeled boundary + explicit instruction" standard. **Caveat:** "by convention" framing is softer than V-01's DO/DO-NOT directives — empirical reliability unverified. |
| C-23 | **PASS** *(with reliability caveat)* | Count instruction present; N substituted in guard. Dep C-22 passes. Same caveat: descriptive framing may reduce model compliance rate vs. directive framing. |
| C-24 | PASS | "A cell that names an element in prose without the typed syntax, or uses a cat-N code that does not match the schema, does not satisfy this requirement"; dep C-21 ✓. |

**Aspirational: 16/16 → 10 pts**

**V-03 Total: 100.0 | Band: Golden**
*Reliability note: C-22 and C-23 are structurally present but empirically uncertain — this variation is designed to TEST whether conversational framing is sufficient. If directive language is load-bearing, C-22/C-23 degrade to FAIL and score drops to 98.75.*

---

### V-04 — Count-Anchored Guard + Inline-Schema Register (Combined)

**Design summary:** Fuses V-01's two-step count-verification guard (C-22, C-23) with V-02's PRE-COMPUTATION inline-schema register (C-21, C-24) on the full C-09–C-20 foundation. 4-part inertia + 9 sections. Full directive framing throughout.

#### Essential: 5/5 → 60 pts

#### Recommended: 3/3 → 30 pts

#### Aspirational (C-09–C-24)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Org Evolution Roadmap required, Row 1 headcount, Row 2 distinct dimension. |
| C-10 | PASS | Anti-Pattern Watch required. |
| C-11 | PASS | "DO list at minimum two numbered reasons here. DO NOT move mechanism-typed content to the How We Coordinate Today sub-section." Explicit content-migration trap guard. |
| C-12 | PASS | Decides/Escalates separate columns; merger disallowed. |
| C-13 | PASS | "the trigger must name a threshold"; "revisit as the team grows" explicitly disallowed. |
| C-14 | PASS | "Generic assertions about team cohesion... without naming a mechanism do not count as reasons"; dep C-11 ✓. |
| C-15 | PASS | 4-part structure: all four labeled sub-sections including How We Coordinate Today. |
| C-16 | PASS | Escalates names destination; "everything not listed under Decides" disallowed; dep C-12 ✓. |
| C-17 | PASS | Two rows, distinct dimensions enforced; dep C-09 ✓. |
| C-18 | PASS | "Why It Applies Here" with org-specific rationale; dep C-10 ✓. |
| C-19 | PASS | "Two headcount thresholds at different values count as one dimension — they do not pass"; dep C-17 ✓. |
| C-20 | PASS | Named taxonomic element in APW rationale; dep C-18 ✓. |
| C-21 | PASS | PRE-COMPUTATION: ORG-ELEMENT REGISTER as section 7; inline category-schema table first; all four categories populated with exact names from prior sections; explicitly required before proceeding to roadmap; dep C-20 ✓. |
| C-22 | PASS | 4-part inertia; two-step count-check guard: "count the numbered items above. If the count is fewer than two, write the missing reasons before continuing. Once the count is at least two, substitute that count as N." DO-NOT-EMIT before count-check; dep C-15 ✓. |
| C-23 | PASS | Count embedded in guard via N substitution; pre-emit verification ensures count accuracy; evaluator can verify guard N against actual numbered reasons; dep C-22 ✓. |
| C-24 | PASS | `[element name] (cat-N)` format required; examples of passing and failing syntax provided; "cat-N code must match the category schema in the PRE-COMPUTATION register"; dep C-21 ✓. |

**Aspirational: 16/16 → 10 pts**

**V-04 Total: 100.0 | Band: Golden**
*Primary 16/16 candidate. Highest reliability: combines both R6 lineage mechanisms under full directive framing.*

---

### V-05 — V-04 + Post-Hoc Section-Ordering Guard

**Design summary:** V-04 architecture plus a SECTION VERIFICATION checklist block at the end of the prompt. Nine numbered checklist items with a "if any item is absent, produce the missing section before proceeding" directive. Tests whether the post-hoc guard adds completeness without causing section compression.

#### Essential: 5/5 → 60 pts

#### Recommended: 3/3 → 30 pts

#### Aspirational (C-09–C-24)

All aspirational criteria: same as V-04. The section-verification block reinforces rather than introduces new requirements. The checklist explicitly mentions:
- Item 2: "Separator line with count emitted?" — reinforces C-22/C-23
- Item 7: "Category schema table emitted? All four categories populated?" — reinforces C-21
- Item 9: "Typed citations with cat-N codes in every Why It Applies Here cell?" — reinforces C-24

**Aspirational: 16/16 → 10 pts**

**V-05 Total: 100.0 | Band: Golden**
*Secondary 16/16 candidate. Reliability note: post-hoc checklist placement (end of prompt, not inline) avoids the V-03/R3 compression trap. Risk: if token pressure causes the model to satisfy checklist items minimally rather than fully, essential criterion content may thin.*

---

## Rankings

| Rank | Variation | Aspirational | Total | Notes |
|------|-----------|-------------|-------|-------|
| 1 | **V-04** | 16/16 | **100.0** | Primary 16/16 target — directive framing, both mechanisms combined, highest reliability |
| 2 | **V-05** | 16/16 | **100.0** | Equal score, additive section checklist; marginal compression risk at end of prompt |
| 3 | **V-03** | 16/16 | **100.0** | Equal score, but C-22/C-23 reliability empirically unverified — descriptive framing is the test axis |
| 4 | **V-01** | 14/16 | **98.75** | Count guard confirmed; register absent, C-21/C-24 fail |
| 5 | **V-02** | 14/16 | **98.75** | Register confirmed; 3-part inertia, C-22/C-23 fail |

---

## Excellence Signals

**From V-04 (the most reliable 16/16 design):**

**1. Two-step pre-emit count-verification protocol**
V-01/R6's single-step `{N}` substitution left a residual risk: the model could write the separator before all reasons were drafted (guard-before-reasons) or substitute an incorrect count without checking. V-01/R7 and V-04 split this into two explicit steps: (1) count the numbered items; (2) if fewer than two, write the missing reasons; (3) only then substitute N and emit. The key structural move is placing the count-check as a PRECONDITION to emission, not a concurrent step.

**2. Inline category-schema table inside the register output**
V-02/R6's register defined cat-N codes only in prompt instructions — requiring the model to carry that definition forward into APW citations from prompt memory. V-02/R7 and V-04 embed the schema table as the opening row of the register block itself (`cat-1 | Areas | ...`). The model writes its cat-N assignments against a definition it just emitted, eliminating prompt-instruction memory dependency. This makes typed citations self-verifying: an evaluator can confirm the cat-N code in any APW cell against the schema table in the same document.

**3. PRE-COMPUTATION naming signals execution semantics**
Labeling the register block "PRE-COMPUTATION: ORG-ELEMENT REGISTER" frames it as a computation step the model must complete before proceeding, not documentary prose. The naming creates an implicit pipeline: compute the register, then use it. This framing distinction is not tested explicitly in R7 but appears in V-02 and V-04 as a structural complement to the inline schema.

---

## New Patterns for R8

- **Two-step pre-emit protocol** generalizes: any criterion requiring a counted or enumerated artifact in the output can benefit from a separate count-check step before the artifact is emitted. The principle is: verify precondition → substitute → emit (not: emit + substitute simultaneously).
- **Schema-in-output (self-documenting reference artifacts)**: when a prompt instructs the model to use a coding system (cat-N, type labels, category codes), embedding the schema definition in the produced output block makes citations machine-verifiable within the same document without requiring the evaluator to consult prompt instructions.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Two-step pre-emit count-verification protocol: separate count-check precondition from guard emission rather than concurrent substitution, preventing guard-before-reasons and count-accuracy failures", "Schema-in-output pattern: embed coding-system definitions (cat-N schema table) inside the register block itself so typed citations are self-verifying against a definition in the same produced document, eliminating prompt-instruction memory dependency"]}
```
