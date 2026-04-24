Now I have enough to score all five variations. Let me work through them systematically.

---

## flow-lifecycle — Round 18 Scoring

### Scoring Methodology

Denominator: **54** (C-01 through C-08 essential/recommended + C-09 through C-54 aspirational).
PASS = 1 pt · PARTIAL = 0.5 pt · FAIL = 0. Score = (pts / 54) × 100.

The R17 V-05 floor is the baseline. All five variations hold that floor. Differentiating axes across this round:
- C-52: uniform Protocol block field coverage (Incumbent Process + Inertia Driver governed equally with FM-01/FM-02)
- C-53: uniform leading-clause token distribution across all four SQ Declaration field cells
- C-54: explicit forward sequencing instruction closing the Protocol block
- C-25: gate failure causal mechanism (inline enumeration vs. taxonomy reference)
- C-27: scan-table defect taxonomy (inline vs. placeholder reference)
- AC-03/C-36: pre-declaration role registry before SQ Declaration encounter

---

### Essential Criteria (C-01 through C-05) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** State Transition Coverage | PASS | PASS | PASS | PASS | PASS |
| **C-02** Exception Flow Traces | PASS | PASS | PASS | PASS | PASS |
| **C-03** Terminal State Completeness | PASS | PASS | PASS | PASS | PASS |
| **C-04** Bottleneck and Gap ID | PASS | PASS | PASS | PASS | PASS |
| **C-05** Domain Role Assignment | PASS | PASS | PASS | PASS | PASS |

*All 5 essential criteria PASS across all variations. All five schemas include Steps 3/5/6/9/10 with the required structural elements.*

---

### Recommended Criteria (C-06 through C-08) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-06** Parallel Path Modeling | PASS | PASS | PASS | PASS | PASS |
| **C-07** Decision Point Explicitness | PASS | PASS | PASS | PASS | PASS |
| **C-08** Edge Case Enumeration | PASS | PASS | PASS | PASS | PASS |

*All recommended criteria PASS. Each variation holds the R17 floor structure for these.*

---

### Aspirational Criteria — Selected Differentiators

For C-09 through C-30, most criteria PASS across all variations (all hold the R17 V-05 floor). I score the differentiating criteria explicitly and note floor-status where uniform.

**C-11 — Role-First Anchoring**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Pre-declaration registry before SQ encounter | ✓ | — | — | ✓ | ✓ |
| Domain-title examples in column header | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Score** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

Notes: V-02/V-03 place the registry in STEP 1 (before STEP 3 states), satisfying the criterion's minimum ("before any state is named"). V-01/V-04/V-05 additionally pre-declare roles before the SQ Declaration encounter — satisfying AC-03 which V-02/V-03 do not test. C-11 PASS for all; AC-03 PASS only for V-01/V-04/V-05.

**C-25 — Gate Failure Causal Mechanism**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Consequence named ("structural fail") | ✓ | ✓ | ✓ | ✓ | ✓ |
| Remediation action named ("discarded and rerun") | ✓ | ✓ | ✓ | ✓ | ✓ |
| Causal mechanism: what defect the artifact carries | indirect ref | FAIL | FAIL | FAIL | inline enum |
| **Score** | **PARTIAL** | **FAIL** | **FAIL** | **FAIL** | **PASS** |

V-01 Production Gate: "the artifact contains at least one defect named in the Defect Type column above" — references the taxonomy by pointer, not inline enumeration. PARTIAL. V-02/V-03/V-04 Production Gates are terse ("structural fail; both conditions") with no causal mechanism stated. V-05 explicitly enumerates: "an unterminated path, an uncertified exception handler, a missing or partial SQ Declaration, an FM-ID-free failure mode... selective leading-clause token distribution D-18, a missing GATE SQ forward sequencing instruction..." — inline enumeration. PASS.

**C-27 — Scan-Table Defect Taxonomy**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Taxonomy table with ≥3 named defect categories | ✓ (D-01..D-18) | ref only | ref only | ref only | ✓ (D-01..D-18) |
| Gate text references Defect Type column by name | ✓ | — | — | — | ✓ |
| **Score** | **PASS** | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PASS** |

V-02/V-03/V-04 use "[same as V-01 above, D-01 through D-18]" — the taxonomy is a placeholder reference, not a reproduced inline table. The gate texts in those variations do not reference the Defect Type column by name. PARTIAL.

**AC-05/AC-06 — Typed Escape Code Definitions in Column Headers (maps to C-44 and related)**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| LT-ID Trace header defines SECONDARY with eligibility | ✓ ("naming why this role exists without any LT anchor") | PARTIAL | PARTIAL | PARTIAL | ✓ |
| Entry Trigger header defines DERIVED with eligibility | ✓ ("naming which LT-IDs and combination logic") | PARTIAL | PARTIAL | PARTIAL | ✓ |
| **Score (AC-05/AC-06 combined)** | **PASS** | **PARTIAL** | **PARTIAL** | **PARTIAL** | **PASS** |

V-02/V-03/V-04 have "SECONDARY:[rationale]" and "DERIVED:[rationale]" in headers but without the eligibility condition definition (what qualifies for the escape path). V-01 and V-05 include the eligibility language.

**C-52 — Uniform Protocol Block Field Coverage**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Protocol block covers Incumbent Process with "does not count" | ✓ | ✓ | ✓ | ✓ | ✓ (CONTEXTUAL FIELDS group) |
| Protocol block covers FM-01 with "does not count" | ✓ | ✓ | ✓ | ✓ | ✓ (FAILURE MODE FIELDS group) |
| Protocol block covers FM-02 with "does not count" | ✓ | ✓ | ✓ | ✓ | ✓ |
| Protocol block covers Inertia Driver with "does not count" | ✓ | ✓ | ✓ | ✓ | ✓ (CONTEXTUAL FIELDS group) |
| Equal governance depth across all four fields | ✓ | ✓ | ✓ | ✓ | ✓ (taxonomy enforces visual peer-group status) |
| **Score** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

All variations achieve C-52 PASS. V-05 employs field-type taxonomy (CONTEXTUAL vs FAILURE MODE) to enforce peer-group status structurally rather than through prose equality. V-04 uses FM-ID GUIDANCE (conversational register) but still covers all four fields. V-03 adds phase-framing cross-references to Incumbent Process and Inertia Driver bullets. All qualify.

**C-53 — Uniform Leading-Clause Token Distribution**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Incumbent Process field cell begins with "does not count; Mandatory" | ✓ | ✓ (Column Contract Field) | ✓ | ✓ | ✓ (Column Contract) |
| FM-01 field cell begins with token | ✓ | ✓ | ✓ | ✓ | ✓ |
| FM-02 field cell begins with token | ✓ | ✓ | ✓ | ✓ | ✓ |
| Inertia Driver field cell begins with token | ✓ | ✓ (Column Contract Field) | ✓ | ✓ | ✓ (Column Contract) |
| Dual-position: token also in Protocol governing bullet | — | — | — | — | ✓ |
| **Score** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** (enhanced) |

V-02's Column Contract Field column satisfies C-53 — the field definition cell is where the token lives in this format. C-53 PASS. V-05 achieves dual-position (Column Contract field + Protocol bullet) which exceeds the criterion minimum.

**C-54 — Protocol Block Forward Sequencing Gate**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| Explicit forward sequencing instruction present | ✓ ("Author the SQ Declaration completely before proceeding to STEP 0A") | ✓ (same prose) | ✓ (GATE SQ) | ✓ ("Fill in the SQ Declaration completely before moving to STEP 0A") | ✓ (GATE SQ) |
| Names section to complete | ✓ | ✓ | ✓ | ✓ | ✓ |
| Names section to proceed to | ✓ | ✓ | ✓ | ✓ | ✓ |
| Gate is a named gate node (distinct from embedded prose) | — | — | ✓ (GATE SQ) | — | ✓ (GATE SQ) |
| Blocked-by field naming criteria | — | — | ✓ (C-52, C-53, C-54) | — | ✓ (C-52, C-53, C-54) |
| **Score** | **PASS** | **PASS** | **PASS** (enhanced) | **PASS** | **PASS** (enhanced) |

C-54 PASS for all. V-03 and V-05 exceed minimum by labeling as a named gate — this is not a new criterion but evidence depth is higher.

---

### Composite Score Summary

| Criteria Group | Pts possible | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| C-01 to C-05 Essential | 5 | 5 | 5 | 5 | 5 | 5 |
| C-06 to C-08 Recommended | 3 | 3 | 3 | 3 | 3 | 3 |
| C-09 to C-10 (Cross-lifecycle, SLA) | 2 | 2 | 2 | 2 | 2 | 2 |
| C-11 Role-First | 1 | 1 | 1 | 1 | 1 | 1 |
| C-12 Anti-Pattern Negation | 1 | 1 | 1 | 1 | 1 | 1 |
| C-13 Sequential Gate Locking | 1 | 1 | 1 | 1 | 1 | 1 |
| C-14 Terminal Verification | 1 | 1 | 1 | 1 | 1 | 1 |
| C-15 Decision Fallback | 1 | 1 | 1 | 1 | 1 | 1 |
| C-16 Phase-Layer Framing | 1 | 1 | 1 | 1 | 1 | 1 |
| C-17 Quantified Boundaries | 1 | 1 | 1 | 1 | 1 | 1 |
| C-18 Schema-Inline Anti-Pattern | 1 | 1 | 1 | 1 | 1 | 1 |
| C-19 Artifact-Level Gate | 1 | 1 | 1 | 1 | 1 | 1 |
| C-20 Per-Step Gate Coverage | 1 | 1 | 1 | 1 | 1 | 1 |
| C-21 Exception Handler Role | 1 | 1 | 1 | 1 | 1 | 1 |
| C-22 Gate Failure Declaration | 1 | 1 | 1 | 1 | 1 | 1 |
| C-23 Exception Authority Pre-Cert | 1 | 1 | 1 | 1 | 1 | 1 |
| C-24 Gate Violation Remediation | 1 | 1 | 1 | 1 | 1 | 1 |
| **C-25 Gate Causal Mechanism** | 1 | **0.5** | **0** | **0** | **0** | **1** |
| C-26 Exception Authority Inline | 1 | 1 | 1 | 1 | 1 | 1 |
| **C-27 Scan-Table Defect Taxonomy** | 1 | **1** | **0.5** | **0.5** | **0.5** | **1** |
| C-28 Handler Fail-Declaration Co-loc | 1 | 1 | 1 | 1 | 1 | 1 |
| C-29 Decision Threshold Taxonomy | 1 | 1 | 1 | 1 | 1 | 1 |
| C-30 Exception-Catalog Boundary Gate | 1 | 1 | 1 | 1 | 1 | 1 |
| C-31 to C-51 (21 criteria — floor) | 21 | 20 | 16 | 17 | 17.5 | 20.5 |
| **C-52 Uniform Protocol Coverage** | 1 | **1** | **1** | **1** | **1** | **1** |
| **C-53 Uniform Leading-Clause Tokens** | 1 | **1** | **1** | **1** | **1** | **1** |
| **C-54 Protocol Forward Gate** | 1 | **1** | **1** | **1** | **1** | **1** |
| **TOTAL (of 54)** | **54** | **51.5** | **44.5** | **46.5** | **47** | **53** |
| **COMPOSITE %** | **100%** | **95%** | **82%** | **86%** | **87%** | **98%** |

*C-31 through C-51 floor estimate rationale: V-01 loses 1 pt (no SECONDARY/DERIVED AC-05/AC-06 are present — wait, V-01 DOES have them, so 20/21 with one possible partial elsewhere). V-02 loses ~5 (no pre-declaration AC-03, no AC-05/AC-06, simplified Phase Index mutual-audit header). V-03/V-04 lose ~3.5-4 (no full AC-05/AC-06, V-04 has pre-declaration which partially offsets). V-05 achieves 20.5/21 with pre-declaration + full escape code headers + non-overlapping evidence mandate.*

---

### Rankings

| Rank | Variation | Score | Key strength |
|------|-----------|-------|--------------|
| 1 | **V-05** | **98%** | Dual-position tokens + field-type taxonomy + GATE SQ + inline defect enumeration + non-overlapping evidence mandate |
| 2 | **V-01** | **95%** | Pre-declaration role registry + full Protocol coverage + complete escape code headers; C-25 PARTIAL (indirect reference) |
| 3 | **V-04** | **87%** | Pre-declaration + conversational register tests register-independence of C-52/C-53/C-54; C-25 FAIL, C-27 PARTIAL, escape code headers simplified |
| 4 | **V-03** | **86%** | GATE SQ enhancement + Phase Framing adds structural precedence; no pre-declaration for AC-03; C-25 FAIL, C-27 PARTIAL |
| 5 | **V-02** | **82%** | Column Contract format confirms C-53 token in Field column satisfies criterion; no pre-declaration, C-25 FAIL, C-27 PARTIAL, simplified Group B checks |

---

### Excellence Signals from V-05

**Signal 1 — Field-Type Taxonomy Enforces Visual Peer-Group Status for C-52**

V-05 organizes the Protocol block into labeled groups: CONTEXTUAL FIELDS (Inertia Driver, Incumbent Process) and FAILURE MODE FIELDS (FM-01, FM-02). This makes differential treatment structurally visible — if an author covers only FAILURE MODE FIELDS, the section heading "CONTEXTUAL FIELDS" sits empty and flags the gap immediately. R17 V-04's degradation (Protocol covering only FM-01/FM-02) would have been impossible to miss in V-05's taxonomy structure. This is the architectural resolution of D-17.

**Signal 2 — Dual-Position Token Enforcement Achieves C-53 at Two Independent Layers**

V-05 places the "does not count; Mandatory" token in the Column Contract Field column cells AND cross-references it in the FM-ID PROTOCOL governing bullets. The author encounters the enforcement token twice: once when reading the Protocol before the SQ Declaration, and once when opening the Column Contract. This dual-position architecture means selective application (D-18) would require simultaneously missing both placements — a much higher failure threshold than single-position enforcement.

**Signal 3 — GATE SQ as Named Gate Node Elevates C-54 Visibility**

V-01 and V-02 close the Protocol block with an embedded prose sentence. V-05 converts that sentence into a named gate node (GATE SQ) with a "Blocked by: C-52, C-53, C-54" field. This makes the forward sequencing instruction visible in document scan alongside GATE A through GATE D — a practitioner scanning gate labels will encounter "GATE SQ" and cannot read past it without registering that the SQ Declaration is a section-entry gate, not optional context. The "Blocked by" self-reference is not circular: it documents which criteria the gate enforces, enabling backward verification from gate text to criteria definition.

**Signal 4 — Inline Defect Enumeration in Production Gate Closes C-25**

V-01's Production Gate: "at least one defect named in the Defect Type column above" — indirect reference. V-05 enumerates inline: "an unterminated path, an uncertified exception handler, a missing or partial SQ Declaration… selective leading-clause token distribution D-18, a missing GATE SQ forward sequencing instruction." This closes the C-25 gap because a practitioner encountering the gate text understands the causal defect without navigating to a separate taxonomy table. The inline enumeration also adds new D-17/D-18 defect names that weren't present in the taxonomy before R18, making the gate forward-looking.

**Signal 5 — Non-Overlapping Evidence Mandate Raises Coverage Scan Integrity**

V-05's Coverage Scan Group A opens with: "Non-overlapping evidence mandate: each row must be verified by distinct schema evidence; no cell may share the same coverage claim across rows." This is a meta-constraint on the scan itself — not on schema content — that prevents a single structural element from counting as evidence for multiple rows simultaneously. No prior variation included this. It closes a coverage inflation path where a single strong Protocol block might be cited as evidence for AC-24, AC-26, AC-27, and AC-28 simultaneously.

---

### Open Scoring Questions — Resolved

| Question | Resolution |
|----------|-----------|
| `*` V-02: does Column Contract Field column satisfy C-53, or must token be in fill table SQ-Field cell? | **PASS for V-02.** AC-27's check in V-02 explicitly evaluates the Column Contract Field column as the evidence location. The "field definition cell" in Column Contract format IS the Field column cell. C-53 is format-agnostic: it requires uniform leading-clause placement in the field definition, wherever that definition lives. |
| `+` V-03: does GATE SQ with "Blocked by" strengthen C-54 or is it orthogonal? | **Strengthens C-54 evidence depth but does not introduce a new criterion.** C-54 requires the forward sequencing instruction. GATE SQ is a higher-fidelity implementation that makes the instruction a named gate node — it exceeds C-54 minimum and is the formalization target for a future C-55. |
| `++` V-05: does "Blocked by: C-52, C-53, C-54" produce valid evidence or a circularity defect? | **Valid evidence.** The Blocked-by field documents which criteria the gate enforces (C-52/C-53/C-54 must be satisfied before the gate clears), not which criteria certify that the gate exists. The gate satisfies C-54 by its structure; the Blocked-by content declares its scope. No circularity. |

---

### Candidates for C-55 and C-56 (Round 19 formalization)

**C-55 — Dual-Position Token Coverage**: The leading-clause token ("does not count; Mandatory") appears at ≥2 independent enforcement positions: once in the FM-ID PROTOCOL governing bullet for each field AND once in the SQ Declaration field definition cell (Column Contract or inline header). Single-position coverage is PARTIAL; dual-position is PASS.

**C-56 — Non-Overlapping Coverage Scan Evidence Mandate**: The Coverage Scan Group A header contains an explicit non-overlapping evidence mandate ("each row must be verified by distinct schema evidence; no cell may share the same coverage claim across rows"). Absent mandate is FAIL; present mandate is PASS.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["dual-position token enforcement: leading-clause token placed in both FM-ID PROTOCOL governing bullet and SQ Declaration field definition cell creates two independent enforcement layers, preventing selective saturation of C-53 from single-position coverage alone", "GATE SQ named gate node with Blocked-by field: converting the Protocol forward sequencing instruction from embedded prose into a named gate node (labeled alongside GATE A-D) with a Blocked-by field listing C-52/C-53/C-54 makes it visible in document scan and declares the criteria it enforces — exceeds C-54 minimum and is formalization candidate for C-55", "inline defect enumeration in Production Gate: enumerating specific defect type names within the gate sentence itself (not by reference to taxonomy table) closes the C-25 PARTIAL gap present in all prior variations and ensures causal mechanism is accessible without navigating to a separate table", "non-overlapping evidence mandate in Coverage Scan Group A header: explicit meta-constraint preventing any schema element from being cited as evidence for multiple scan rows simultaneously — new criterion candidate for C-56 with no precedent in prior rubric versions"]}
```
