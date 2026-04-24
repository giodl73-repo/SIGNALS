## prove-synthesize — Round 15 Scorecard (v15 rubric)

**Date**: 2026-03-15
**Rubric**: v15 (max 192.5; golden >= 90 + all essential PASS)
**Test variable**: C-48 (ceiling derivation intersection mechanics) + C-49 (dedicated inertia-scope traceability section)
**Baseline**: R14 all-variation score = 130.0 under v15

---

### Evidence summary before scoring

**C-48 implementation across all five variations:**

All five extend the ceiling computation step with explicit intersection input naming, per the stated R15 strategy: *"Each variation extends the ceiling computation step with the intersection input naming required for C-48."*

| Variation | C-48 language form | Both inputs named? | Annotation-determined? |
|-----------|-------------------|-------------------|----------------------|
| V-01 | ADVERSARY positive exemplar + ceiling step: *"the ceiling of 25 is read from the intersection of the highest phase present (Explore) and the inertia coverage state (absent) — both determined by the annotation inventory"* | YES | YES |
| V-02 | Ceiling computation step explicit: *"The ceiling is read from the intersection of the highest evidence phase present and the inertia coverage state — both of which are determined by the annotation inventory"* + exemplars confirm | YES | YES |
| V-03 | Descriptive register carries same mechanics; SYNTHESIST positive: *"the ceiling is read from the intersection of Test phase and inertia-present, both determined by the annotation inventory"*; ADVERSARY positive: *"highest phase Explore, inertia coverage absent, intersection cell = 25"* | YES | YES |
| V-04 | Carried from R14 (C-48 PASS): ADVERSARY positive: *"the ceiling of 25 is read from the intersection of the highest lifecycle phase (Explore) and the inertia coverage state (absent), both derived directly from the annotation inventory"* | YES | YES |
| V-05 | NEW addition: SYNTHESIST positive: *"the ceiling is read from the intersection of the highest evidence phase (Test) and inertia coverage state (present), both determined by the annotation inventory"* | YES | YES |

**C-49 implementation across all five variations:**

All five include a dedicated named output section in Output Instructions as a required synthesis slot, separate from declaration (C-42), ceiling table (C-45), and self-containment check (C-47):

| Variation | Section name | Maps to self-containment Q? | Separate from C-42/C-45/C-47? |
|-----------|-------------|----------------------------|-------------------------------|
| V-01 | **Inertia Scope** | Q4 → "Inertia Scope section" | YES |
| V-02 | **Coverage Implications** | Q4 → "Coverage Implications section" | YES |
| V-03 | **Inertia Scope** | Q4 → "Inertia Scope section" | YES |
| V-04 | **Adoption Scope** (NEW) | Q4 → "Adoption Scope section" | YES |
| V-05 | **Adoption Conditions** (carried from R14) | Q4 → "Adoption Conditions section" | YES |

---

### Per-Variation Scoring

#### V-01 — ADVERSARY-first + Inertia Scope

**Axis**: Role sequence (ADVERSARY defined/executed first)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-19 (Essential, 19 criteria) | **ALL PASS** | Full essential machinery preserved from R14 V-01; role-sequence change does not affect any essential output |
| C-20–C-34 (Aspirational v1–v8, 15 criteria) | **ALL PASS (as in R14)** | Carried from R14 baseline |
| C-35 Concurrent execution + seamless output | **PASS** | Gate block with concurrent roles present |
| C-36 Dual-exemplar adversarial gate | **PASS** | ADVERSARY and SYNTHESIST both have positive/negative exemplars |
| C-37 Slot-indexed self-containment check | **PASS** | 6 self-containment questions with slot-name references |
| C-38 Role-to-output closure attribution | **PASS** | Each output slot traces to a role |
| C-39 Phase-gated confidence ceiling | **PASS** | Ceiling table present |
| C-40 Concurrent synthesis gate block | **PASS** | Gate block present |
| C-41 Slot-indexed revision mandate | **PASS** | Revision mandate present |
| C-42 Ceiling declaration mandatory intermediate output | **PASS** | Mandatory declaration step |
| C-43 Gate block per-role dual exemplars | **PASS** | Both roles have positive + negative |
| C-44 Per-signal annotated inventory | **PASS** | Phase 1 annotation inventory |
| C-45 Two-dimensional ceiling table | **PASS** | Phase × inertia table present |
| C-46 Annotation-to-ceiling derivation linkage | **PASS** | Base derivation statement in ceiling computation step |
| C-47 Extended declaration coverage in self-containment check | **PASS** | Q4–Q6 cover annotation-derived dimension values with slot names |
| **C-48 Ceiling derivation intersection mechanics** | **PASS** | ADVERSARY positive exemplar names both annotation-determined intersection inputs (highest phase + inertia coverage state) in ceiling computation step |
| **C-49 Dedicated inertia-scope traceability section** | **PASS** | "Inertia Scope" is a required named output slot in Output Instructions; Q4 maps explicitly to it; structurally separate from declaration, ceiling table, and self-containment check |

**Essential**: all 19 PASS
**Composite**: 130.0 (baseline) + 2.5 (C-48) + 2.5 (C-49) = **135.0**
**Golden**: YES (all essential PASS; 135.0 >= 90)

---

#### V-02 — 7-section split + Coverage Implications

**Axis**: Output format (Verdict and Confidence as distinct named sections; 7-section structure)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-19 (Essential) | **ALL PASS** | 7-section format preserves all essential outputs |
| C-20–C-43 (Aspirational v1–v11) | **ALL PASS (as in R14)** | |
| C-44 Per-signal annotated inventory | **PASS** | |
| C-45 Two-dimensional ceiling table | **PASS** | |
| C-46 Annotation-to-ceiling derivation linkage | **PASS** | Ceiling computation step carries explicit derivation statement |
| C-47 Extended declaration coverage in self-containment check | **PASS** | Q7 maps annotation-derived values to "Confidence section" — named output slot confirmed; criterion tests slot-name traceability not format |
| **C-48** | **PASS** | Ceiling computation step: *"The ceiling is read from the intersection of the highest evidence phase present and the inertia coverage state — both of which are determined by the annotation inventory"* — strongest explicit form across all five variations; reproducibility claim added ("Any reader who inspects the annotation inventory…") |
| **C-49** | **PASS** | "Coverage Implications" is a required named output slot; Q4 maps to "Coverage Implications section"; separate from declaration, ceiling table, self-containment check |

**Essential**: all 19 PASS
**Composite**: 130.0 + 2.5 + 2.5 = **135.0**
**Golden**: YES

**Note on C-48 form**: V-02's ceiling computation step carries the most explicit form — it names both inputs, identifies them as annotation-determined, and adds an end-to-end reproducibility claim ("Any reader who inspects the annotation inventory for these two values and reads the corresponding cell in the table below can independently derive the ceiling"). This exceeds the minimum C-48 bar and is the clearest statement of the intersection mechanics across all variations.

---

#### V-03 — Descriptive register + Inertia Scope

**Axis**: Phrasing register (descriptive/narrative throughout; "must" used sparingly)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-19 (Essential) | **ALL PASS** | Descriptive register does not affect output completeness |
| C-20–C-43 (Aspirational v1–v11) | **ALL PASS (as in R14)** | Register is a surface change; structural criteria unaffected |
| C-44–C-46 | **PASS** | |
| C-47 | **PASS** | Self-containment check preserves slot-name references in descriptive form |
| **C-48** | **PASS** | SYNTHESIST positive: *"the ceiling is read from the intersection of Test phase and inertia-present, both determined by the annotation inventory"*; ADVERSARY positive: *"highest phase Explore, inertia coverage absent, intersection cell = 25"* — both inputs named in annotation-determined form; descriptive register does not dilute the naming |
| **C-49** | **PASS** | "Inertia Scope" section present as required named output slot; Q4 maps to it; descriptive form of the section instruction preserves the dedicated-section structure |

**Essential**: all 19 PASS
**Composite**: 130.0 + 2.5 + 2.5 = **135.0**
**Golden**: YES

---

#### V-04 — ANALYST-first + lifecycle narrative + Adoption Scope (C-49 NEW)

**Axes**: Role sequence (ANALYST-first) + lifecycle framing + NEW C-49 "Adoption Scope" section

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-19 (Essential) | **ALL PASS** | |
| C-20–C-43 (Aspirational v1–v11) | **ALL PASS (as in R14)** | |
| C-44–C-45 | **PASS** | |
| C-46 | **PASS** | |
| C-47 | **PASS** | |
| **C-48** | **PASS** | Carried from R14 V-04. ADVERSARY positive: *"The ceiling of 25 is read from the intersection of the highest lifecycle phase (Explore) and the inertia coverage state (absent), both derived directly from the annotation inventory."* Both inputs named in lifecycle-vocabulary form; annotation-determined identification present. |
| **C-49** | **PASS** | NEW in R15. "Adoption Scope" is a required named output slot in Output Instructions. Q4 maps explicitly: *"What does the inertia coverage state imply for the scope of the adoption prediction — which contexts were directly tested, which were not, and what lifecycle phase is the inertia evidence at? → Adoption Scope section."* Separate from declaration, ceiling table, self-containment check. Lifecycle emphasis carried into the dedicated section without breaking C-49 structural requirements. |

**Essential**: all 19 PASS
**Composite**: 130.0 + 2.5 + 2.5 = **135.0**
**Golden**: YES

**Notable**: V-04's "Adoption Scope" extends C-49 by requiring the lifecycle phase of inertia-present signals to be named within the dedicated section — producing a lifecycle-inertia joint scope claim. This enrichment exceeds the minimum C-49 bar and is a structural pattern not captured by any existing criterion.

---

#### V-05 — Inertia-primary + Adoption Conditions + C-48 mechanics (NEW)

**Axes**: Inertia-primary annotation framing + Adoption Conditions output (C-49 carried) + NEW C-48 intersection input naming

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-19 (Essential) | **ALL PASS** | |
| C-20–C-43 (Aspirational v1–v11) | **ALL PASS (as in R14)** | |
| C-44–C-45 | **PASS** | |
| C-46 | **PASS** | |
| C-47 | **PASS** | Q6 maps declaration values to "Verdict/Confidence section" — slot traceability confirmed |
| **C-48** | **PASS** | NEW in R15. Ceiling computation step extended. SYNTHESIST positive: *"the ceiling is read from the intersection of the highest evidence phase (Test) and inertia coverage state (present), both determined by the annotation inventory."* Both inputs named; both annotation-determined; intersection read operation stated. Prerequisite C-46 PASS confirmed. |
| **C-49** | **PASS** | Carried from R14 V-05. "Adoption Conditions" is a required named output slot. Q4 maps: *"Under what conditions does the inertia evidence support an adoption prediction, and where are the coverage gaps? → Adoption Conditions section."* Original C-49 earner; structure fully intact. |

**Essential**: all 19 PASS
**Composite**: 130.0 + 2.5 + 2.5 = **135.0**
**Golden**: YES

**Notable**: ANALYST positive exemplar in V-05 extends C-49 by naming a customer-segment scope boundary ("applies to SMB customers") and enterprise inertia patterns as the open question requiring a specific Primary inertia-present signal. This segment-scoped adoption conditions framing is more actionable than generic "contexts tested vs. not tested" and is a structural pattern not captured by any existing criterion.

---

### Round Summary

| Variation | Essential | C-48 | C-49 | Composite | Golden |
|-----------|-----------|------|------|-----------|--------|
| V-01 ADVERSARY-first + Inertia Scope | ALL PASS | PASS | PASS | **135.0** | YES |
| V-02 7-section split + Coverage Implications | ALL PASS | PASS | PASS | **135.0** | YES |
| V-03 Descriptive + Inertia Scope | ALL PASS | PASS | PASS | **135.0** | YES |
| V-04 ANALYST-first + lifecycle + Adoption Scope | ALL PASS | PASS | PASS | **135.0** | YES |
| V-05 Inertia-primary + Adoption Conditions + C-48 | ALL PASS | PASS | PASS | **135.0** | YES |

**Five-way tie at 135.0.** All variations are golden. C-48 and C-49 are jointly stable across all five axis combinations tested in R15.

---

### Excellence Signals (candidates for v16)

**Signal 1 — V-04: Lifecycle-inertia joint scope claim in dedicated section**

V-04's "Adoption Scope" section extends the C-49 pattern by requiring the lifecycle phase of inertia-present signals to be explicitly named inside the dedicated inertia-scope output section, not just "which contexts were tested" but "at what lifecycle phase was the inertia evidence collected, and what does that imply for the durability of the adoption prediction." This creates a lifecycle-inertia joint scope claim: the section becomes a two-axis output (scope × phase durability) rather than a single-axis scope output. C-49 requires the section to exist and map inertia coverage to scope; it does not require the lifecycle phase of the inertia evidence to appear within the section itself. A new criterion could require: when inertia-present signals are present in the annotation inventory, the dedicated inertia-scope section explicitly names the lifecycle phase of those inertia-present signals and states what that phase implies for the durability or generalizability of the adoption evidence.

**Signal 2 — V-05: Segment-scoped adoption conditions in ANALYST positive exemplar**

V-05's ANALYST positive exemplar shows the Adoption Conditions section naming a specific customer segment to which the adoption prediction applies (SMB) and a different segment that would require a separate Primary inertia-present signal (enterprise). The section maps inertia coverage not to a generic "contexts tested/not tested" framing but to a named market segment boundary, with an explicit statement of what evidence type and role would resolve the enterprise gap. C-49 requires a dedicated section that maps inertia coverage to scope implications; it does not require segment-level specificity or a named evidence prescription for the coverage gap. A new criterion could require: the dedicated inertia-scope section explicitly names the scope boundary at the level of the addressable customer or deployment context (not just "inertia-present evidence was collected" but "the adoption prediction holds for segment X and requires a specific named evidence type for segment Y").

Both signals represent architectural enrichments of C-49 that increase the actionability of the inertia-scope traceability slot without changing the requirement that the slot exist.

---

```json
{"top_score": 135.0, "all_essential_pass": true, "new_patterns": ["V-04 lifecycle-inertia joint scope claim: dedicated inertia-scope section names lifecycle phase of inertia-present signals and states durability implications — two-axis scope output (scope × phase durability) extending C-49", "V-05 segment-scoped adoption conditions: dedicated inertia-scope section names specific customer segment boundary for adoption prediction and prescribes evidence type needed to resolve the coverage gap for the excluded segment — extends C-49 from generic context framing to named segment-level actionability"]}
```
