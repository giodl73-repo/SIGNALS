## org-roles — Round 7 Scoring (Rubric v7)

---

### Rubric Summary (v7)

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 pts |
| Recommended | C-06 through C-08 | 30 pts |
| Aspirational | C-09 through C-33 (25 total) | 10 pts |

Formula: `(E/5)*60 + (R/3)*30 + (A/25)*10`

---

### V-01 — Role Sequence: Context-First Inertia Derivation

**Essential (5/5):**

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 5 YAML template defines all six top-level fields with required sub-fields; PREPARE confirms [FC-4] `verify_questions` and [FC-5] `simplify_rules` verbatim |
| C-02 | PASS | Inertia-advocate derived fully in Phase 1 with name, frame, serves, primary_verify_question; verify_questions include status-quo adversarial question; inertia-advocate written first in Phase 5 |
| C-03 | PASS | Phase 3 STOCK-ROLES lists pm, architect, strategy with lens descriptors |
| C-04 | PASS | Phase 4 OUTPUT-AREA: `.roles/{area}/`; area slug from Phase 2 domain vocabulary; gate confirms |
| C-05 | PASS | Phase 2 DOMAIN-ANALYSIS derives experts from concern space; each expert linked to specific concern using domain vocabulary |

**Recommended (3/3):**

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | [FC-2] epistemic-viewpoint + [FC-3] beneficiary; template explicitly marks FAILURE MODE: task-list frame / frame restatement with worked examples |
| C-07 | PASS | [FC-4] min-two actionable questions; [FC-5] opinionated exclusion; template marks FAILURE MODE: scope description; BAD/GOOD examples for both |
| C-08 | PASS | [FC-10] in FIELD-CONTRACT names both prohibitions: CONTRACT VIOLATION (type 1) — PHANTOM; CONTRACT VIOLATION (type 2) — UNIVERSALIST |

**Aspirational (25/25):**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Phase 5 template: "before writing, confirm — no other role in this registry would prioritize this question first; revise until uniquely attributable" — uniqueness required by construction |
| C-10 | PASS | Phase 6 REGISTRY.md template: area, total_roles, stock_roles, domain_experts (name + derivation_source + inertia_gap), coverage_gaps, inertia_surface — all five required fields plus extension |
| C-11 | PASS | Inertia-advocate derived Phase 1 (context read), domain experts Phase 2, stock roles Phase 3 — strict context-before-stock ordering; axis focus of this variation |
| C-12 | PASS | [FC-2] "FAILURE MODE: task description"; [FC-3] "FAILURE MODE: frame restatement"; [FC-5] opinionated exclusion failure named — multiple fields name failure modes explicitly |
| C-13 | PASS | Every phase defines artifact format: INERTIA-DERIVATION block, DOMAIN-ANALYSIS block, STOCK-ROLES, OUTPUT-AREA, YAML template, REGISTRY.md template |
| C-14 | PASS | [FC-10]: "CONTRACT VIOLATION (type 1) — PHANTOM" and "CONTRACT VIOLATION (type 2) — UNIVERSALIST" — typed dual-failure labels |
| C-15 | PASS | Phase 6: "FAILURE MODE — HEADING STUB: '## Registry Summary' with no fields populated is not a registry" — explicit naming ✓ |
| C-16 | PASS | Every output-producing phase has numbered GATE block (phases 0–6) |
| C-17 | PASS | BAD/GOOD examples in [FC-1], [FC-2], [FC-3], [FC-4], [FC-5] — five fields with concrete worked examples |
| C-18 | PASS | [FC-1], [FC-2], [FC-3], [FC-4] each carry BAD + GOOD pair in same field comment — multiple contrastive pairs |
| C-19 | PASS | Every GATE has 4–6 numbered independently verifiable items |
| C-20 | PASS | EXTENSION-COMMITMENT names `inertia_surface` as domain-specific extension; grounded in Phase 1 INERTIA-DERIVATION |
| C-21 | PASS | Template annotation: "before writing, confirm — no other role in this registry would prioritize this question first" — uniqueness mandated at write time per question |
| C-22 | PASS | Phase 6 GATE item 2: "total_roles equals PHASE5_COUNT from the PREPARE enumeration" — explicit cross-step count tie |
| C-23 | PASS | EXTENSION-COMMITMENT has all three elements: field_name=`inertia_surface`, population_source naming Phase 1 + INERTIA-DERIVATION, purpose statement |
| C-24 | PASS | Phase 5 GATE item 2: "Every file uses exact identifiers `verify_questions` and `simplify_rules` per [FC-4] and [FC-5] — both strings appear verbatim as YAML keys" |
| C-25 | PASS | Phase 2 GATE item 3: "name, concern link, inertia gap, domain-vocabulary frame, verify focus — checked per expert, not as a total count" — five attributes per expert |
| C-26 | PASS | FIELD-CONTRACT block with FC-1 through FC-10 as numbered authoritative entries; phases reference FC identifiers |
| C-27 | PASS | Phase 6 PREPARE declares `PHASE5_COUNT`; names "derivation from prior-phase plans without enumeration is a count-bypass failure — the same anti-pattern as C-27 applied to registry counts" |
| C-28 | PASS | [FC-1]: PROHIBITED NAMES: "domain-expert", "expert-1", "generic-expert", "role-1" — explicit named anti-patterns |
| C-29 | PASS | [FC-10] inside FIELD-CONTRACT block uses "CONTRACT VIOLATION (type 1)" and "CONTRACT VIOLATION (type 2)" — violation framing in named contract |
| C-30 | PASS | EXTENSION-COMMITMENT purpose: "answers the Phase 0 diagnostic question — 'what is the strongest argument that the status quo is sufficient for {topic}?'" |
| C-31 | PASS | **Site 1**: [FC-1] PROHIBITED NAMES in Phase 0 contract ✓ **Site 2**: Phase 2 "DO NOT name derived experts with placeholder labels. The following names are PROHIBITED by [FC-1]..." ✓ **Site 3**: Phase 5 GATE item 3: "No role file uses a prohibited name per [FC-1]..." ✓ — three independent checkpoints |
| C-32 | PASS | Phase 6 PREPARE: "Derivation from prior-phase plans without enumeration is a count-bypass failure — the same anti-pattern as C-27 applied to registry counts. Only enumeration of Phase 5 files is valid." — failure class explicitly named |
| C-33 | PASS | Phase 5 YAML template collaborates_with annotation: `# CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry. # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.` — both labels mirrored at write site |

**V-01 Score: (5/5)×60 + (3/3)×30 + (25/25)×10 = 60.0 + 30.0 + 10.0 = 100.00 GOLDEN**

---

### V-02 — Output Format: Per-Role Diagnosis Card Before YAML Writing

**Essential (5/5):** All PASS — schema complete, inertia-advocate in STOCK-ROLES with Phase 1 source, pm/architect/strategy present, correct output path, domain experts context-derived.

**Recommended (3/3):** All PASS — orientation coherence maintained, lens quality enforced, [FC-10] dual prohibition present.

**Aspirational (24.5/25):**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Diagnosis Card requires explicit uniqueness argument: "closest overlap is [role-name], which would ask [different angle] — confirmed distinct"; CROSS-CARD UNIQUENESS SCAN required after all cards |
| C-10 | PASS | REGISTRY.md template: area, total_roles, stock_roles, domain_experts (name + derivation_source), coverage_gaps, inertia_surface ✓ |
| C-11 | PASS | Phase 1 INERTIA-SURFACE (context), Phase 2 DOMAIN-ANALYSIS (domain experts), Phase 3 STOCK-ROLES — context-first ordering preserved |
| C-12 | PASS | [FC-2] "FAILURE MODE: task list / job description"; [FC-3] "FAILURE MODE: frame restatement"; [FC-5] failure mode for scope descriptions — named across multiple fields |
| C-13 | PASS | All phases define explicit artifact structure: INERTIA-SURFACE block, DOMAIN-ANALYSIS block, DIAGNOSIS-CARD format, YAML template, REGISTRY.md template |
| C-14 | PASS | [FC-10]: CONTRACT VIOLATION (type 1) — PHANTOM; CONTRACT VIOLATION (type 2) — UNIVERSALIST ✓ |
| **C-15** | **PARTIAL** | Phase 6 GATE item 5: "No heading stubs — every field has substantive content" — completion condition implicitly prevents stubs; **no explicit "FAILURE MODE — HEADING STUB" label** as in V-01. C-15 PARTIAL condition applies. |
| C-16 | PASS | All phases have numbered GATE blocks |
| C-17 | PASS | BAD/GOOD examples in [FC-1]–[FC-5] |
| C-18 | PASS | Multiple BAD+GOOD contrastive pairs in FC-1 through FC-5 |
| C-19 | PASS | All GATEs have ≥3 numbered items |
| C-20 | PASS | EXTENSION-COMMITMENT designates `inertia_surface` with provenance ✓ |
| C-21 | PASS | Diagnosis Card structure forces explicit uniqueness argument before any YAML is written — strongest mechanism for C-21: per-role pre-YAML uniqueness confirmation |
| C-22 | PASS | Phase 6 GATE item 2: "total_roles equals PHASE5_COUNT from the PREPARE enumeration" ✓ |
| C-23 | PASS | EXTENSION-COMMITMENT: field_name + population_source (Phase 1 + INERTIA-SURFACE) + purpose ✓ |
| C-24 | PASS | Phase 5 GATE item 4: "Every file uses exact identifiers `verify_questions` and `simplify_rules` — both appear verbatim as YAML keys" ✓ |
| C-25 | PASS | Phase 2 GATE item 3: "all four attributes: name, concern link, domain-vocabulary frame, verify focus — checked per expert, not as a count" ✓ |
| C-26 | PASS | FIELD-CONTRACT block FC-1 through FC-10 ✓ |
| C-27 | PASS | Phase 6 PREPARE declares PHASE5_COUNT from Phase 5 enumeration ✓ |
| C-28 | PASS | [FC-1] PROHIBITED NAMES ✓ |
| C-29 | PASS | [FC-10] inside FIELD-CONTRACT uses "CONTRACT VIOLATION (type 1)" and "CONTRACT VIOLATION (type 2)" ✓ |
| C-30 | PASS | EXTENSION-COMMITMENT purpose: "answers the Phase 0 diagnostic question — 'what is the strongest existing-system argument that makes {topic} premature?'" ✓ |
| C-31 | PASS | **Site 1**: [FC-1] PROHIBITED NAMES ✓ **Site 2**: Phase 2 "DO NOT name derived experts with placeholder labels. The following names are PROHIBITED by [FC-1]..." ✓ **Site 3**: Phase 5 GATE item 5: "No role file uses a prohibited name per [FC-1]..." ✓ |
| C-32 | PASS | Phase 6 PREPARE: "Derivation from prior-phase plans without enumeration is a count-bypass failure: the model adds numbers from earlier phases instead of confirming what was actually written." ✓ |
| C-33 | PASS | Phase 5 YAML template: `# CONTRACT VIOLATION (type 1) — PHANTOM` and `# CONTRACT VIOLATION (type 2) — UNIVERSALIST` in collaborates_with annotation ✓ |

**V-02 Score: (5/5)×60 + (3/3)×30 + (24.5/25)×10 = 60.0 + 30.0 + 9.80 = 99.80 GOLDEN**

---

### V-03 — Phrasing Register: Failure-Mode-First Phase Openings

**Essential (5/5):** All PASS — schema complete, inertia-advocate in STOCK-ROLES (four-role stock listing with Phase 1 source), pm/architect/strategy present, correct output path, domain experts from context.

**Recommended (3/3):** All PASS — orientation coherence (failure modes make task-list frame and frame restatement structurally unavoidable), lens quality, [FC-10] dual prohibition.

**Aspirational (25/25):**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Template: "Per [FC-4]: before writing, confirm no other role would prioritize this first" — uniqueness mandated at write time |
| C-10 | PASS | REGISTRY.md template has all required fields; Phase 6 GATE item 5 enforces substantive content |
| C-11 | PASS | Phase 1 INERTIA-SURFACE (context), Phase 2 DOMAIN-ANALYSIS, Phase 3 STOCK-ROLES — context-first ✓ |
| C-12 | PASS | Every phase opens with FAILURE MODES block — this is the strongest C-12 mechanism of all variations; failure modes are the primary framing at each phase boundary |
| C-13 | PASS | All phases define explicit artifact structure ✓ |
| C-14 | PASS | [FC-10]: CONTRACT VIOLATION (type 1) — PHANTOM; CONTRACT VIOLATION (type 2) — UNIVERSALIST ✓ |
| C-15 | PASS | Phase 6 FAILURE MODES opening explicitly names: "HEADING STUB: any field in REGISTRY.md has only a header with no substantive content" — explicit failure mode name ✓ |
| C-16 | PASS | All phases have numbered GATE blocks ✓ |
| C-17 | PASS | BAD/GOOD examples in [FC-1]–[FC-5] ✓ |
| C-18 | PASS | BAD+GOOD contrastive pairs in multiple field-contract entries ✓ |
| C-19 | PASS | All GATEs have ≥3 numbered items ✓ |
| C-20 | PASS | EXTENSION-COMMITMENT with `inertia_surface` ✓ |
| C-21 | PASS | Template annotation: "Per [FC-4]: before writing, confirm no other role would prioritize this first" — write-time uniqueness mandate ✓ |
| C-22 | PASS | Phase 6 GATE item 2 ties total_roles to PHASE5_COUNT from PREPARE enumeration ✓ |
| C-23 | PASS | EXTENSION-COMMITMENT: all three elements present ✓ |
| C-24 | PASS | Phase 5 GATE item 2: exact identifier strings checked ✓ |
| C-25 | PASS | Phase 2 GATE item 3: four named attributes checked per expert individually ✓ |
| C-26 | PASS | FIELD-CONTRACT block FC-1 through FC-10 ✓ |
| C-27 | PASS | Phase 6 PREPARE declares PHASE5_COUNT; names COUNT-BYPASS FAILURE ✓ |
| C-28 | PASS | [FC-1] names [FC-1] as "PLACEHOLDER NAMES — the Phase 0 failure this contract prevents" — failure-mode framing applied to the prohibition itself ✓ |
| C-29 | PASS | [FC-10] inside FIELD-CONTRACT: CONTRACT VIOLATION (type 1) and (type 2) ✓ |
| C-30 | PASS | EXTENSION-COMMITMENT purpose names Phase 0 diagnostic question ✓ |
| C-31 | PASS | **Site 1**: [FC-1] PROHIBITED NAMES ✓ **Site 2**: Phase 2 FAILURE MODES opens with "PLACEHOLDER DERIVATION: domain expert is named with a placeholder per [FC-1] — 'domain-expert', 'expert-1', 'generic-expert' are prohibited in this phase" + derivation block labels it "the PLACEHOLDER DERIVATION failure this phase is designed to prevent" ✓ **Site 3**: Phase 5 FAILURE MODES opens with "PLACEHOLDER NAME IN FILE" + GATE item 3 names it explicitly ✓ |
| C-32 | PASS | Phase 6 FAILURE MODES: "COUNT-BYPASS FAILURE: `total_roles` computed by adding Phase-2 expert count and Phase-3 stock role count rather than enumerating Phase 5 files — this is the count-bypass failure" + PREPARE names "COUNT-BYPASS FAILURE" as the class it prevents ✓ |
| C-33 | PASS | Phase 5 YAML template: `# CONTRACT VIOLATION (type 1) — PHANTOM` and `# CONTRACT VIOLATION (type 2) — UNIVERSALIST` ✓ |

**V-03 Score: (5/5)×60 + (3/3)×30 + (25/25)×10 = 60.0 + 30.0 + 10.0 = 100.00 GOLDEN**

---

### V-04 — Role Sequence + Output Format: Context-First Inertia + Diagnosis Cards

**Essential (5/5):** All PASS — schema complete, inertia-advocate derived Phase 1 and written Phase 5, pm/architect/strategy in Phase 3, correct path, domain experts context-derived.

**Recommended (3/3):** All PASS.

**Aspirational (24.5/25):**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Diagnosis Cards require uniqueness argument AND **inertia relationship field**: "how this role's primary concern challenges the Phase 1 inertia claim" — strongest differentiation mechanism in any variation |
| C-10 | PASS | REGISTRY.md: area, total_roles, stock_roles, domain_experts (name + derivation_source + inertia_gap), coverage_gaps, inertia_surface ✓ |
| C-11 | PASS | Context-first inertia derivation (Phase 1) + domain experts (Phase 2) before stock roles (Phase 3) ✓ |
| C-12 | PASS | Multiple named failure modes across field constraints ✓ |
| C-13 | PASS | All phases have explicit artifact structure ✓ |
| C-14 | PASS | [FC-10]: CONTRACT VIOLATION (type 1) and (type 2) ✓ |
| **C-15** | **PARTIAL** | Phase 6 GATE item 5: "No heading stubs — every field has substantive content" — same as V-02; no explicit "FAILURE MODE — HEADING STUB" label. C-15 PARTIAL. |
| C-16 | PASS | All phases have GATE blocks ✓ |
| C-17 | PASS | BAD/GOOD worked examples in [FC-1]–[FC-5] ✓ |
| C-18 | PASS | BAD+GOOD contrastive pairs in field contract ✓ |
| C-19 | PASS | Multi-item GATE at every phase ✓ |
| C-20 | PASS | EXTENSION-COMMITMENT with `inertia_surface` ✓ |
| C-21 | PASS | Diagnosis Card: uniqueness argument + inertia relationship field — dual confirmation before YAML writing; strongest C-21 implementation |
| C-22 | PASS | Phase 6: PHASE5_COUNT from enumeration ✓ |
| C-23 | PASS | EXTENSION-COMMITMENT: three elements ✓ |
| C-24 | PASS | Phase 5 GATE: exact identifier checks ✓ |
| C-25 | PASS | Phase 2 GATE: five named attributes per expert (name, concern link, inertia gap, domain-vocabulary frame, verify focus) ✓ |
| C-26 | PASS | FIELD-CONTRACT FC-1 through FC-10 ✓ |
| C-27 | PASS | Phase 6 PREPARE declares PHASE5_COUNT; "Derivation from prior-phase plans without enumeration is a count-bypass failure" ✓ |
| C-28 | PASS | [FC-1] PROHIBITED NAMES ✓ |
| C-29 | PASS | [FC-10] CONTRACT VIOLATION (type 1) and (type 2) in FIELD-CONTRACT ✓ |
| C-30 | PASS | EXTENSION-COMMITMENT purpose names Phase 0 diagnostic question ✓ |
| C-31 | PASS | **Site 1**: [FC-1] PROHIBITED NAMES ✓ **Site 2**: Phase 2 "DO NOT name derived experts with placeholder labels. PROHIBITED by [FC-1]..." ✓ **Site 3**: Phase 5 GATE item 5: "No role file uses a prohibited name" ✓ |
| C-32 | PASS | Phase 6 PREPARE: "Derivation from prior-phase plans without enumeration is a count-bypass failure: planning counts are not the same as written-file counts." ✓ |
| C-33 | PASS | Phase 5 YAML template: CONTRACT VIOLATION (type 1) — PHANTOM + (type 2) — UNIVERSALIST ✓ |

**V-04 Score: (5/5)×60 + (3/3)×30 + (24.5/25)×10 = 60.0 + 30.0 + 9.80 = 99.80 GOLDEN**

---

### V-05 — All Axes: Cold Hypothesis + Diagnosis Cards + Failure-Mode-First + Explicit C-31 Site Labels

**Essential (5/5):** All PASS — schema complete, inertia-advocate listed in STOCK-ROLES (four-role) with Phase 1 source for frame and verify_questions, pm/architect/strategy present, correct path, domain experts context-derived.

**Recommended (3/3):** All PASS.

**Aspirational (25/25):**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Diagnosis Card uniqueness argument + CROSS-CARD UNIQUENESS SCAN; `verify_questions` template: "before writing, confirm no other role would prioritize this first" ✓ |
| C-10 | PASS | REGISTRY.md: all five required fields + inertia_surface extension; "FAILURE MODE — HEADING STUB: every field above must have substantive content" ✓ |
| C-11 | PASS | Phase 1 INERTIA-SURFACE (context, COLD-HYPOTHESIS refinement), Phase 2 DOMAIN-ANALYSIS, Phase 3 STOCK-ROLES ✓ |
| C-12 | PASS | Failure-mode-first phase openings — richest C-12 in any variation; every phase opens with FAILURE MODES block as first text ✓ |
| C-13 | PASS | All phases define explicit artifact structure ✓ |
| C-14 | PASS | [FC-10]: CONTRACT VIOLATION (type 1) — PHANTOM; CONTRACT VIOLATION (type 2) — UNIVERSALIST ✓ |
| C-15 | PASS | Phase 6 FAILURE MODES: "HEADING STUB: any field has a header with no substantive content below it" + Phase 6 template annotation: "FAILURE MODE — HEADING STUB: every field above must have substantive content" — explicit at two points ✓ |
| C-16 | PASS | All phases have GATE blocks ✓ |
| C-17 | PASS | BAD/GOOD worked examples in [FC-1]–[FC-5] ✓ |
| C-18 | PASS | BAD+GOOD contrastive pairs in [FC-1] through [FC-5]; WORKED EXAMPLE (bad)/(good) in Phase 5 template ✓ |
| C-19 | PASS | All GATEs have ≥3 numbered items ✓ |
| C-20 | PASS | EXTENSION-COMMITMENT with `inertia_surface` ✓ |
| C-21 | PASS | Diagnosis Card requires uniqueness argument with closest-overlap naming ✓ |
| C-22 | PASS | Phase 6: PHASE5_COUNT from Phase 5 file enumeration ✓ |
| C-23 | PASS | EXTENSION-COMMITMENT: field_name + population_source + purpose all present ✓ |
| C-24 | PASS | Phase 5 GATE item 4: "Every file uses exact identifiers `verify_questions` and `simplify_rules` as YAML keys" ✓ |
| C-25 | PASS | Phase 2 GATE item 3: "four attributes — checked per expert, not count" ✓ |
| C-26 | PASS | FIELD-CONTRACT FC-1 through FC-10 ✓ |
| C-27 | PASS | Phase 6 PREPARE declares PHASE5_COUNT; WRITE references variable ✓ |
| C-28 | PASS | [FC-1] PROHIBITED NAMES ✓ |
| C-29 | PASS | [FC-10] inside FIELD-CONTRACT: CONTRACT VIOLATION (type 1) and (type 2) ✓ |
| C-30 | PASS | EXTENSION-COMMITMENT purpose: "answers the Phase 0 diagnostic question — 'what is the strongest argument that the status quo is sufficient for {topic}?'" ✓ |
| C-31 | PASS | **C-31-SITE-1**: [FC-1] "*** C-31-SITE-1: PROHIBITED NAMES ***" + announces three-site structure ("appearing at three enforcement checkpoints: Site 1, Site 2, Site 3") ✓ **C-31-SITE-2**: Phase 2 FAILURE MODES "C-31-SITE-2 FAILURE — PLACEHOLDER DERIVATION" + derivation block "*** C-31-SITE-2: PROHIBITED: 'domain-expert'..." ✓ **C-31-SITE-3**: Phase 5 FAILURE MODES "C-31-SITE-3 FAILURE — PLACEHOLDER NAME IN FILE" + Diagnosis Card "C-31-SITE-3 pre-check" + name template annotation + GATE item 5 ✓ — most redundant enforcement in any variation |
| C-32 | PASS | Phase 6 PREPARE: "COUNT-BYPASS FAILURE: deriving total_roles from Phase 2 expert count + Phase 3 stock role count (4) instead of Phase 5 file enumeration is the anti-pattern this step names." ✓ |
| C-33 | PASS | Phase 5 YAML template: `# CONTRACT VIOLATION (type 1) — PHANTOM: a role name absent from this registry. # CONTRACT VIOLATION (type 2) — UNIVERSALIST: "all roles" or equivalent.` ✓ |

**V-05 Score: (5/5)×60 + (3/3)×30 + (25/25)×10 = 60.0 + 30.0 + 10.0 = 100.00 GOLDEN**

---

### Score Summary

| V | Essential | Recommended | Aspirational | Composite | Band |
|---|-----------|-------------|--------------|-----------|------|
| **V-01** | 5/5 | 3/3 | 25/25 | **100.00** | GOLDEN |
| **V-02** | 5/5 | 3/3 | 24.5/25 | **99.80** | GOLDEN |
| **V-03** | 5/5 | 3/3 | 25/25 | **100.00** | GOLDEN |
| **V-04** | 5/5 | 3/3 | 24.5/25 | **99.80** | GOLDEN |
| **V-05** | 5/5 | 3/3 | 25/25 | **100.00** | GOLDEN |

**Rank**: V-01 = V-03 = V-05 (100.00) > V-02 = V-04 (99.80)

**Differentiator**: V-02 and V-04 lose 0.20 points on C-15 (PARTIAL). Both use "No heading stubs" as a gate item, which implicitly prevents stubs but does not explicitly name the "HEADING STUB" failure mode as a labeled class. V-01 adds "FAILURE MODE — HEADING STUB: '## Registry Summary' with no fields populated is not a registry." V-03 and V-05 open Phase 6 with FAILURE MODES blocks that name "HEADING STUB" explicitly.

---

### Excellence Signals

**Top variation by design richness: V-05** (100.00; self-documenting enforcement, maximum redundancy)
**Top variation by simplicity-to-score ratio: V-01** (100.00; achieves perfect score without Diagnosis Cards or failure-mode-first)

**Patterns from top-scoring variations that made them better:**

**1. Explicit heading-stub failure mode label in Phase 6 (V-01, V-03, V-05 vs. V-02, V-04)**
V-02 and V-04 trust the gate item ("No heading stubs") to prevent stubs. V-01 names "FAILURE MODE — HEADING STUB" with a description. V-03 names it as a FAILURE MODES block opener. V-05 does both. The naming converts an implicit gate check into an explicit failure class the model can recognize by name. This is the exact same discipline that C-28 applies to placeholder names — the pattern generalizes: every structural anti-pattern that passes superficial review should be named by class, not just excluded by condition.

**2. Enforcement site self-annotation with count announcement (V-05 only)**
`*** C-31-SITE-1: PROHIBITED NAMES ***` followed by "These placeholder anti-patterns appear at three enforcement checkpoints: Site 1 (here): field contract / Site 2: Phase 2 derivation instruction / Site 3: Phase 5 file-writing gate" — the model sees the enforcement architecture as a declared map at the first site, not as a distributed set of unrelated instructions. This makes three-site enforcement self-verifying: the model doesn't need to infer that it's at the right site count; the annotation confirms it.

**3. Inertia-relationship field in Diagnosis Cards (V-04, V-05)**
V-04 and V-05 add: `inertia relationship: [for domain experts: how this role's primary concern challenges the Phase 1 inertia claim]` to each Diagnosis Card. This forces an explicit adversarial statement before any YAML is written — the domain expert's verify questions emerge from a named inertia gap, not just from general domain concern. The inertia hypothesis becomes the structural anchor for each expert's uniqueness argument, producing verify questions that are adversarially grounded by construction.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["enforcement-site self-annotation with count announcement: labeling each prohibition checkpoint with a site number and declaring the full three-site structure at SITE-1 makes the enforcement architecture machine-readable at definition time, so the model encounters not just the prohibition but its own compliance count", "inertia-relationship field in Diagnosis Cards: requiring each domain expert to explicitly articulate how its primary concern challenges the Phase 1 inertia claim before writing verify questions produces an adversarially-grounded uniqueness argument rather than an independently-derived one"]}
```
