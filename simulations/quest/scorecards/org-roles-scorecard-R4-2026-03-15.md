## org-roles — Round 4 Scoring (v4 Rubric)

---

### V-01 — Inertia Framing: Dedicated Inertia Specification Phase

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Template has all 6 top-level fields with required sub-fields (`orientation.frame`, `orientation.serves`, `lens.verify_questions`, `lens.simplify_rules`, `expertise.depth`, `expertise.relevance`, `scope`, `collaborates_with`) |
| C-02 | PASS | Phase 2 dedicates a full step to specifying the status-quo claim; Phase 3 adds inertia-advocate whose `verify_questions` are sourced from Phase 2 challenge questions and `frame` must use Phase 2 status-quo claim — explicitly status-quo framing, not generic skepticism |
| C-03 | PASS | Phase 3 STOCK-ROLES lists `pm, architect, strategy, inertia-advocate` |
| C-04 | PASS | Phase 4 and Phase 5 specify `.craft/roles/{area}/` |
| C-05 | PASS | Phase 1 derives experts from domain concerns; gate item 3 requires name, concern link, domain-vocabulary frame, and verify focus |
| C-06 | PASS | `frame` FAILURE MODE: task list; `serves` FAILURE MODE: frame restatement — both with full bad/good pairs showing epistemic viewpoint vs. beneficiary distinction |
| C-07 | PASS | `verify_questions` requires actionable questions answerable by artifact; Phase 5 gate item 5 checks `simplify_rules` as prohibition/elimination; FAILURE MODE annotation with worked examples |
| C-08 | PASS | Template comments: `# FAILURE MODE (type 1): phantom role` and `# FAILURE MODE (type 2): universalist listing` — both prohibitions present |
| C-09 | PASS | Each domain expert must include an inertia-response question uniquely tied to their Phase 1 concern; template requires "second question unique to this role's frame — no other role in this registry would prioritize this question first" |
| C-10 | PASS | Phase 6 template has all five required fields plus "Inertia surface" extension; gate items 2–4 verify each; `total_roles` count verified against Phase 5 output |
| C-11 | PASS | Phase 1 derives domain experts; Phase 3 loads stock roles; instruction: "Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1" |
| C-12 | PASS | `frame`: "FAILURE MODE: task list"; `serves`: "FAILURE MODE: frame restatement"; `simplify_rules`: "FAILURE MODE: scope description masquerading as a constraint" — three negative constraints naming specific failure modes with worked examples by construction |
| C-13 | PASS | Every phase defines its output: Phase 1 → DOMAIN-ANALYSIS block, Phase 2 → INERTIA-SURFACE block with exact sub-fields, Phase 3 → STOCK-ROLES block, Phase 4 → OUTPUT-AREA line, Phase 5 → role file template, Phase 6 → REGISTRY template |
| C-14 | PASS | `# FAILURE MODE (type 1): phantom role` and `# FAILURE MODE (type 2): universalist listing` — both carry explicit type labels |
| C-15 | PASS | Phase 6 template: "FAILURE MODE: heading-only stub — a section header with no required content beneath it is not a complete registry entry and fails C-10 unconditionally" |
| C-16 | PASS | All six phases have GATE checklists: Phase 1 (4 items), Phase 2 (3), Phase 3 (3), Phase 4 (3), Phase 5 (7), Phase 6 (5) |
| C-17 | PASS | Three fields with worked examples: `frame` (bad+good), `serves` (bad+good), `simplify_rules` (bad+good) |
| C-18 | PASS | `frame`, `serves`, `simplify_rules` each have WORKED EXAMPLE (bad) and WORKED EXAMPLE (good) in the same template annotation — three contrastive pairs |
| C-19 | PASS | All output-producing phases have 3+ independently verifiable gate items: Phase 1 (4), Phase 2 (3), Phase 3 (3), Phase 4 (3), Phase 5 (7), Phase 6 (5) |
| C-20 | PASS | Phase 2 prose names the field: "The status-quo claim will be written verbatim into the registry summary as the 'Inertia surface' extension field." Phase 2 runs before Phase 5 (role writing); the field name is communicated to the model before any role file is written |

**Composite:** (5/5 × 60) + (3/3 × 30) + (12/12 × 10) = **100.0 — GOLDEN**

---

### V-02 — Output Format: Standalone FIELD GUIDE

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Template has all 6 top-level fields with required sub-fields |
| C-02 | PASS | Phase 2 adds inertia-advocate with status-quo question pattern confirmed in gate item 3 |
| C-03 | PASS | Phase 2 STOCK-ROLES: pm, architect, strategy, inertia-advocate |
| C-04 | PASS | `.craft/roles/{area}/` |
| C-05 | PASS | Phase 1 derives domain experts from context; gate enforces domain-vocabulary frames |
| C-06 | PASS | FIELD GUIDE BAD/GOOD for `orientation.frame` and `orientation.serves` clearly show epistemic viewpoint vs. beneficiary distinction |
| C-07 | PASS | FIELD GUIDE BAD/GOOD for `simplify_rules`; Phase 4 gate item 5 checks prohibition/elimination |
| C-08 | PASS | FIELD GUIDE has `FAILURE MODE (type 1): phantom role` and `FAILURE MODE (type 2): universalist listing` — both prohibitions present |
| C-09 | PASS | Template requires "Second question unique to this role's frame"; domain experts derived from specific concerns in Phase 1 |
| C-10 | PASS | Phase 5 template has all five required fields plus "Domain risk anchor" extension; gate item 2 verifies all five required fields |
| C-11 | PASS | Phase 1 (context) before Phase 2 (stock roles); no stock role names in Phase 1 block |
| C-12 | PASS | FIELD GUIDE names failure modes for frame ("task list"), serves ("frame restatement"), simplify_rules ("scope description"), collab ("phantom role"), collab ("universalist listing") — five negative constraints |
| C-13 | PASS | Each phase defines explicit output: DOMAIN-ANALYSIS block, STOCK-ROLES block, OUTPUT-AREA line, ROLE FILE TEMPLATE, REGISTRY template |
| C-14 | PASS | FIELD GUIDE: `FAILURE MODE (type 1): phantom role` and `FAILURE MODE (type 2): universalist listing` — both typed |
| C-15 | PASS | Phase 5 template: "FAILURE MODE: heading-only stub — a section header with no required content beneath it is not a complete registry entry and fails C-10 unconditionally." |
| C-16 | PASS | All phases have GATE checklists: Phase 1 (4), Phase 2 (3), Phase 3 (3), Phase 4 (7), Phase 5 (5) |
| C-17 | PASS | FIELD GUIDE has BAD+GOOD for: `frame`, `serves`, `simplify_rules`, `collaborates_with` phantom, `collaborates_with` universalist — five fields with worked examples |
| C-18 | PASS | Five contrastive pairs (BAD+GOOD in same FIELD GUIDE entry per field): frame, serves, simplify_rules, collab phantom, collab universalist |
| C-19 | PASS | All output-producing phases have 3+ items: Phase 1 (4), Phase 2 (3), Phase 3 (3), Phase 4 (7), Phase 5 (5) |
| C-20 | **FAIL** | "Domain risk anchor" appears only in Phase 5's registry template; Phase 4 (role writing) runs before Phase 5 in the step sequence; the model reads Phases 1–4 before encountering the extension field name; "Domain risk anchor" is never mentioned in Phase 0–4 to prime the model before role files are written |

**Composite:** (5/5 × 60) + (3/3 × 30) + (11/12 × 10) = **99.17 — GOLDEN**

---

### V-03 — Lifecycle Emphasis: Phase 0 Extension Contract

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Template has all 6 top-level fields with required sub-fields |
| C-02 | PASS | Phase 2 adds inertia-advocate; gate item 3 confirms "status-quo question pattern" |
| C-03 | PASS | Phase 2 STOCK-ROLES: pm, architect, strategy, inertia-advocate |
| C-04 | PASS | `.craft/roles/{area}/` |
| C-05 | PASS | Phase 1 derives domain experts from actual context; gate requires domain-vocabulary frames |
| C-06 | PASS | Template `frame` and `serves` have FAILURE MODE + WORKED EXAMPLE (bad) + WORKED EXAMPLE (good) pairs showing the epistemic/beneficiary distinction |
| C-07 | PASS | `simplify_rules` FAILURE MODE: "scope description masquerading as a constraint" with paired examples; Phase 4 gate item 5 checks prohibition/elimination |
| C-08 | PASS | Template: `# FAILURE MODE (type 1): phantom role` and `# FAILURE MODE (type 2): universalist listing` — both prohibitions present |
| C-09 | PASS | Domain experts derived from specific concerns with unique verify focus; template requires a "second question unique to this role's frame" |
| C-10 | PASS | Phase 5 template: area, total_roles, stock roles, domain experts with derivation source, coverage gaps, and Phase 0 extension field; gate item 2 verifies all five required fields; gate item 3 verifies extension field |
| C-11 | PASS | Phase 0 + Phase 1 (context) before Phase 2 (stock roles); "Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1" |
| C-12 | PASS | `frame`: "FAILURE MODE: task list"; `serves`: "FAILURE MODE: frame restatement"; `simplify_rules`: "FAILURE MODE: scope description masquerading as a constraint"; collaborates_with: typed failure mode labels — multiple negative constraints naming failure modes with worked examples |
| C-13 | PASS | Phase 0 → EXTENSION-COMMITMENT block (exact fields: field name, population source, purpose); all five subsequent phases define output explicitly |
| C-14 | PASS | Template: `# FAILURE MODE (type 1): phantom role` and `# FAILURE MODE (type 2): universalist listing` — typed labels |
| C-15 | PASS | Phase 5 template: "FAILURE MODE: heading-only stub — a section header with no required content beneath it fails C-10 unconditionally. The heading is structural scaffolding; all six fields (five required plus the Phase 0 extension) are the content." |
| C-16 | PASS | All phases have GATE checklists: Phase 0 (4), Phase 1 (5), Phase 2 (4), Phase 3 (3), Phase 4 (7), Phase 5 (6) |
| C-17 | PASS | `frame`, `serves`, `simplify_rules` each have WORKED EXAMPLE (bad) + WORKED EXAMPLE (good) — three fields with worked examples |
| C-18 | PASS | Three contrastive pairs: `frame`, `serves`, `simplify_rules` — each has both bad and good in the same template annotation |
| C-19 | PASS | All output-producing phases have 3+ items: Phase 0 (4), Phase 1 (5), Phase 2 (4), Phase 3 (3), Phase 4 (7), Phase 5 (6) |
| C-20 | PASS | Phase 0 EXTENSION-COMMITMENT block runs before Phase 1 (context read) and before Phase 4 (role writing) — extension field name is committed by construction in the first step of the skill; Phase 5 template uses the Phase 0 committed field name and Phase 1 derived value |

**Composite:** (5/5 × 60) + (3/3 × 30) + (12/12 × 10) = **100.0 — GOLDEN**

---

### V-04 — Phrasing Register + Lifecycle Emphasis (R3 V-04 + C-20 Fix)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Template has all 6 fields; gate item 3 explicitly checks exact field names `verify_questions` and `simplify_rules` |
| C-02 | PASS | Phase 2 adds inertia-advocate; each domain expert records "Inertia objection this expert must pre-answer" in Phase 1; Phase 5 gate item 10 verifies inertia-response question |
| C-03 | PASS | Phase 2 STOCK-ROLES: pm, architect, strategy, inertia-advocate |
| C-04 | PASS | `.craft/roles/{area}/` |
| C-05 | PASS | Phase 1 derives experts with domain vocabulary; gate items 2–3 enforce specificity |
| C-06 | PASS | `frame` and `serves` each have FAILURE MODE + WORKED EXAMPLE (bad) + WORKED EXAMPLE (good); the examples are the most precise of all variates in showing the epistemic/beneficiary split |
| C-07 | PASS | `verify_questions` has typed failure modes (rhetorical, universal); `simplify_rules` has FAILURE MODE + worked examples; Phase 4 gate item 6 checks prohibition/elimination |
| C-08 | PASS | `collaborates_with` template comments include `# FAILURE MODE (type 1)` + WORKED EXAMPLE (bad/good) and `# FAILURE MODE (type 2)` + WORKED EXAMPLE (bad/good) — most thorough treatment of both prohibitions |
| C-09 | PASS | Template requires unique verify questions per role; domain experts must have inertia-response questions; Phase 4 gate item 10 enforces per-expert inertia-response question |
| C-10 | PASS | Phase 5 template has all five required fields plus "Inertia surface" extension; Phase 5 gate items 2–7 each verify a distinct field |
| C-11 | PASS | Phase 1 before Phase 2; "Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1" |
| C-12 | PASS | Most comprehensive failure-mode labeling of all variates: `name` ("generic label"), `frame` ("task list"), `serves` ("frame restatement"), `verify_questions` types 1 and 2, `simplify_rules` ("scope description"), `expertise.depth` ("label without method"), `collaborates_with` typed |
| C-13 | PASS | All five phases define explicit output formats; Phase 4 template is fully specified including exact field names, annotated constraints, and failure modes per field |
| C-14 | PASS | `# FAILURE MODE (type 1): phantom role` + WORKED EXAMPLE (bad) + WORKED EXAMPLE (good); `# FAILURE MODE (type 2): universalist listing` + WORKED EXAMPLE (bad) + WORKED EXAMPLE (good) — typed labels with contrastive examples |
| C-15 | PASS | Phase 5 template: "FAILURE MODE (C-15): heading-only stub — ... fails C-10 unconditionally. ... A registry that contains only headings provides no audit information to the caller." Explicitly cites C-15. |
| C-16 | PASS | All phases have GATE checklists: Phase 1 (4), Phase 2 (3), Phase 3 (3), Phase 4 (10), Phase 5 (7) |
| C-17 | PASS | Worked examples in: `frame`, `serves`, `simplify_rules`, `expertise.depth`, `collaborates_with` types 1 and 2 — over 5 fields with worked examples |
| C-18 | PASS | Contrastive pairs in: `frame`, `serves`, `simplify_rules`, `collaborates_with` type 1, `collaborates_with` type 2 — five fields with both bad and good in the same annotation |
| C-19 | PASS | All phases have 3+ independently verifiable gate items: Phase 1 (4), Phase 2 (3), Phase 3 (3), Phase 4 (10), Phase 5 (7) |
| C-20 | **FAIL** | "Inertia surface" appears only in Phase 5's registry template; Phase 4 (role writing) runs before Phase 5; Phase 1 records "Inertia objection" per expert but never names the registry field as "Inertia surface"; the model writing role files in Phase 4 has not been told the field name that its Phase 1 content will populate; the hypothesis explicitly acknowledged this risk: "if C-20 cannot be satisfied by adding the extension field to the Phase 5 template alone... a Phase 0 commitment step is needed" |

**Composite:** (5/5 × 60) + (3/3 × 30) + (11/12 × 10) = **99.17 — GOLDEN**

---

### V-05 — Combined: All Four Axes

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Template has all 6 top-level fields with required sub-fields; gate item 3 checks exact field names |
| C-02 | PASS | Phase 2 adds inertia-advocate; Phase 1 records inertia objection per domain expert; Phase 4 gate item 10 verifies inertia-response question per domain expert |
| C-03 | PASS | Phase 2 STOCK-ROLES: pm, architect, strategy, inertia-advocate |
| C-04 | PASS | `.craft/roles/{area}/` |
| C-05 | PASS | Phase 1 derives domain experts with domain vocabulary and verify focus; Phase 1 gate item 3 enforces specificity |
| C-06 | PASS | `frame` and `serves` have FAILURE MODE + WORKED EXAMPLE (bad) + WORKED EXAMPLE (good); FIELD GUIDE covers both fields again as supplemental reference |
| C-07 | PASS | `simplify_rules` FAILURE MODE + contrastive worked example; Phase 4 gate item 6 checks prohibition/elimination; `verify_questions` has typed failure modes (rhetorical, universal) |
| C-08 | PASS | Template: `# FAILURE MODE (type 1): phantom role` and `# FAILURE MODE (type 2): universalist listing`; FIELD GUIDE repeats both with BAD + GOOD pairs — double coverage of both prohibitions |
| C-09 | PASS | Domain experts have specific concerns and verify focus from Phase 1; template requires unique verify questions; domain experts must include inertia-response questions tied to their specific Phase 1 inertia objection |
| C-10 | PASS | Phase 5 template has all five required fields plus Phase 0 committed extension field; Phase 5 gate items 2–7 each verify a distinct field; gate item 4 verifies extension field name matches Phase 0 commitment exactly |
| C-11 | PASS | Phase 0 + Phase 1 (context) before Phase 2 (stock roles); "Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1" |
| C-12 | PASS | `frame`, `serves`, `simplify_rules`, `expertise.depth` each have named failure modes with negative constraints and worked examples; `verify_questions` has typed failure modes; template annotations use "not a generic label," "not a task list," "not a scope description" |
| C-13 | PASS | Phase 0 → EXTENSION-COMMITMENT block (3 required fields); all subsequent phases define output explicitly; Phase 4 role template and FIELD GUIDE fully specified |
| C-14 | PASS | Template: `# FAILURE MODE (type 1): phantom role` and `# FAILURE MODE (type 2): universalist listing`; FIELD GUIDE repeats: `FAILURE MODE (type 1)` and `FAILURE MODE (type 2)` — typed in both locations |
| C-15 | PASS | Phase 5 template: "FAILURE MODE (C-15): heading-only stub — a section header with no required content beneath it fails C-10 unconditionally." Explicitly cites C-15. |
| C-16 | PASS | All phases have GATE checklists: Phase 0 (4), Phase 1 (5), Phase 2 (4), Phase 3 (3), Phase 4 (10), Phase 5 (7) |
| C-17 | PASS | Worked examples in: `frame`, `serves`, `simplify_rules`, `expertise.depth` (WORKED EXAMPLE bad/good), FIELD GUIDE for `collaborates_with` phantom and universalist — six+ fields with worked examples |
| C-18 | PASS | Contrastive pairs (bad+good in same location): `frame`, `serves`, `simplify_rules`, `expertise.depth`, FIELD GUIDE `collaborates_with` phantom, FIELD GUIDE `collaborates_with` universalist — six contrastive pairs, highest count of any variate |
| C-19 | PASS | All output-producing phases have 3+ independently verifiable items: Phase 0 (4), Phase 1 (5), Phase 2 (4), Phase 3 (3), Phase 4 (10), Phase 5 (7) |
| C-20 | PASS | Phase 0 EXTENSION-COMMITMENT runs before Phase 1 and Phase 4 (role writing); Phase 5 registry template uses "the Phase 0 committed name and the Phase 1 derived value"; gate item 4 verifies extension field name matches Phase 0 commitment exactly — unconditional by construction |

**Composite:** (5/5 × 60) + (3/3 × 30) + (12/12 × 10) = **100.0 — GOLDEN**

---

## Score Summary

| Variate | Essential | Recommended | Aspirational | Composite | Band |
|---------|-----------|-------------|--------------|-----------|------|
| **V-01** | 5/5 | 3/3 | 12/12 | **100.0** | GOLDEN |
| **V-02** | 5/5 | 3/3 | 11/12 | **99.17** | GOLDEN |
| **V-03** | 5/5 | 3/3 | 12/12 | **100.0** | GOLDEN |
| **V-04** | 5/5 | 3/3 | 11/12 | **99.17** | GOLDEN |
| **V-05** | 5/5 | 3/3 | 12/12 | **100.0** | GOLDEN |

**C-20 is the sole differentiator**: V-01, V-03, V-05 name the extension field before role writing; V-02 and V-04 name it only in the final registry step (after Phase 4 role writing).

---

## Ranking

**Tier 1 — 100.0:** V-05, V-01, V-03 (all achieve all 20 criteria)

Within Tier 1, secondary ordering by structural depth:
1. **V-05** — most contrastive pairs (6), largest gate (Phase 4: 10 items), Phase 0 + FIELD GUIDE + inertia chain all combined; the only variate that covers `expertise.depth` with a contrastive pair; Phase 5 gate item 4 checks extension field name consistency against Phase 0 commitment
2. **V-01** — novel Phase 2 (dedicated inertia specification) produces the extension field as a named intermediate artifact; inertia-response questions chain directly from Phase 2 challenge questions; Phase 2 explicitly names the "Inertia surface" field before role writing
3. **V-03** — Phase 0 commitment is the cleanest unconditional C-20 satisfaction; 5-item Phase 1 gate is the most thorough context-analysis completion test

**Tier 2 — 99.17:** V-04, V-02 (single FAIL: C-20)

4. **V-04** — most comprehensive failure-mode labeling (6+ named failure modes, including verify_questions types and expertise.depth); five contrastive pairs; 10-item Phase 4 gate; C-15 explicitly cites rubric criterion by ID
5. **V-02** — FIELD GUIDE separation is a clean architectural pattern; five contrastive pairs via the FIELD GUIDE; the two-document approach (template + guide) demonstrates that calibration examples need not live inside the YAML block

---

## Excellence Signals

**From V-05 (top structural depth):**

1. **Extension field name consistency check across phases** — Phase 5 gate item 4 verifies "Extension field name matches the Phase 0 EXTENSION-COMMITMENT exactly (no renaming)"; this closes a silent drift risk where the model picks a name in Phase 0 but writes a slightly different label in Phase 5

2. **Phase 0 extension contract as the unconditional C-20 solution** — committing to the field name before any context is read guarantees the model knows the extension field exists before it writes any role file; no other ordering achieves C-20 by construction; V-03 and V-05 both use this; V-01 gets partial credit by naming the field in Phase 2, but Phase 0 is the strongest form

3. **Contrastive pairs on `expertise.depth`** — adding WORKED EXAMPLE (bad): "Security expertise and system boundary knowledge" / WORKED EXAMPLE (good): "Threat modeling, attack surface enumeration, auth boundary verification via contract diff analysis" to the `depth` field distinguishes domain label from named method; this is the fourth contrastive pair beyond frame/serves/simplify_rules and the one most likely to degrade silently without an example

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Phase 0 extension contract before context read — committing to the registry extension field name in the first step unconditionally guarantees C-20 satisfaction irrespective of when Phase 1 runs; Phase 5 gate item checks extension field name matches Phase 0 commitment exactly to prevent silent drift", "Dedicated inertia specification phase produces a named intermediate artifact (INERTIA-SURFACE block) before stock roles are loaded — the status-quo claim chains through all subsequent phases: Phase 2 claim → Phase 5 inertia-response verify_questions → Phase 6 registry extension field; naming the extension field in Phase 2 prose satisfies C-20 before role writing", "Per-domain-expert inertia objection recorded in Phase 1 creates a four-link chain: domain concern → inertia objection → inertia-response verify_question → registry Inertia surface synthesis; this tightens C-02 quality by making each domain expert responsible for pre-answering a specific status-quo challenge rather than deferring to a generic devil-advocate role"]}
```
