## org-roles Round 2 — Scoring

### Evaluation Notes

Scoring evaluates skill instructions as written — whether the instruction structure reliably produces rubric-compliant output. PARTIAL = 0.5 credit in formula.

---

### V-01 — Role Sequence: Context-Analysis-First

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Step 4 template includes all 6 top-level fields + sub-fields including `scope` |
| C-02 | **PASS** | Step 2 explicitly requires: "The inertia-advocate's `verify_questions` must include at least one question of the form: 'Why is the current approach insufficient...?'" |
| C-03 | **PASS** | Step 2 loads pm, architect, strategy, inertia-advocate |
| C-04 | **PASS** | Step 3 derives area slug; Step 4 writes to `.craft/roles/{area}/` |
| C-05 | **PASS** | Step 1 derives domain experts from DOMAIN-CONCERNS before any stock role appears |
| C-06 | **PASS** | Template: `serves` instructs "not a restatement of frame" — negative constraint present |
| C-07 | **PASS** | verify_questions: "specific enough to produce different answers for different artifacts"; simplify_rules: "not a description, a rule" |
| C-08 | **PARTIAL** | Template slots collaborators but no anti-phantom instruction or anti-everyone prohibition |
| C-09 | **PARTIAL** | "Different answers for different artifacts" tests specificity, not cross-role uniqueness — no explicit unique-concern-per-role requirement |
| C-10 | **PASS** | Step 5 REGISTRY.md template has all 5 fields: area, count, stock names, domain expert names+derivation, gaps |
| C-11 | **PASS** | V-01's main axis — Step 1 domain-only with explicit "Do not load PM, Architect, Strategy, or inertia-advocate in this step" |
| C-12 | **PARTIAL** | Two negative constraints (serves: "not a restatement"; simplify: "not a description, a rule") but no labeled FAILURE MODE collapse patterns; no worked examples |
| C-13 | **PASS** | Every step defines output format: DOMAIN-CONCERNS block, DOMAIN-EXPERTS-DERIVED block, STOCK-ROLES-LOADED block, schema template, REGISTRY.md template |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 2.5/3 × 30 = **25** (C-08 PARTIAL)
**Aspirational:** 4/5 × 10 = **8** (C-09 PARTIAL 0.5, C-12 PARTIAL 0.5)
**V-01 Total: 93 — GOLDEN (all essential pass)**

---

### V-02 — Output Format: Explicit Role File Template

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Full fill-in-the-blank template in Step 2 with all fields including inline failure notes |
| C-02 | **PARTIAL** | Inertia-advocate listed in ROLES-PLAN; template guides verify_questions but no explicit instruction requiring "current approach insufficient" framing |
| C-03 | **PASS** | ROLES-PLAN always includes pm, architect, strategy, inertia-advocate |
| C-04 | **PASS** | Output to `.craft/roles/{derived-area-name}/` |
| C-05 | **PASS** | Step 1 identifies domain experts from context |
| C-06 | **PASS** | Template: frame FAILURE = "task list"; serves FAILURE = "restates frame" — named collapse patterns |
| C-07 | **PASS** | Template: verify FAILURE = "rhetorical or unmeasurable"; simplify FAILURE = "restate scope description" |
| C-08 | **PASS** | "Do not list every role (failure: 'works with everyone')" + "Every entry must reference names of other roles in this registry" |
| C-09 | **PASS** | "Question 2: must surface a concern no other role in this registry would surface first" — explicit uniqueness requirement |
| C-10 | **PASS** | Step 3 REGISTRY.md template with all 5 fields including frontmatter |
| C-11 | **FAIL** | ROLES-PLAN in Step 1 lists domain experts AND stock roles simultaneously — domain derivation and stock loading are not separated; C-11 ordering violated by construction |
| C-12 | **PASS** | 7+ named failure modes embedded in template field comments (name, frame, serves, verify×2, simplify, depth, relevance, collaborates_with) |
| C-13 | **PASS** | Every step has explicit output template: ROLES-PLAN, role file template, REGISTRY.md template |

**Essential:** 4.5/5 × 60 = **54** (C-02 PARTIAL)
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 4/5 × 10 = **8** (C-11 FAIL = 0)
**V-02 Total: 92 — NOT GOLDEN (C-02 PARTIAL → all_essential_pass FALSE)**

---

### V-03 — Phrasing Register: Failure-Mode-Named Field Constraints

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PARTIAL** | Field-by-field instructions cover name, frame, serves, verify_questions, simplify_rules, depth, relevance, collaborates_with — but `scope` is never instructed and no file template ensures it |
| C-02 | **PARTIAL** | Inertia-advocate added in Step 3; no explicit instruction requiring status-quo "current approach insufficient" question |
| C-03 | **PASS** | Step 3 adds pm, architect, strategy, inertia-advocate |
| C-04 | **PASS** | "Write one `.md` file per role to `.craft/roles/{area}/`" |
| C-05 | **PASS** | Step 1 context analysis; Step 2 domain expert derivation from concerns |
| C-06 | **PASS** | frame FAILURE MODE: "Task list"; serves FAILURE MODE: "Frame restatement — if `serves` is a paraphrase of `frame`, delete it" — named collapse pattern |
| C-07 | **PASS** | verify: three named FAILURE MODEs (rhetorical, universal, unmeasurable); simplify: two named FAILURE MODEs (scope description, restatement of frame) |
| C-08 | **PASS** | collaborates_with: FAILURE MODE (type 1): phantom role; FAILURE MODE (type 2): everyone listed |
| C-09 | **PASS** | "At least one must surface a concern unique to this role's frame that no other role in this registry would prioritize" |
| C-10 | **PASS** | Step 5 lists all 5 fields; FAILURE MODE: "Heading-only stub — '## Registry Summary' with no content below it fails C-10" |
| C-11 | **PASS** | Step 1: context only + "Do not name PM, Architect, Strategy, or inertia-advocate in this step"; Step 2: domain experts; Step 3: stock roles |
| C-12 | **PASS** | V-03's core axis — 8+ named FAILURE MODEs with labeled collapse patterns across all schema fields |
| C-13 | **PARTIAL** | Requirements for each field are named but no fill-in-the-blank template; completion state per step not defined — Step 5 lists content but no format or completion condition |

**Essential:** 4/5 × 60 = **48** (C-01 PARTIAL 0.5, C-02 PARTIAL 0.5)
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 4.5/5 × 10 = **9** (C-13 PARTIAL 0.5)
**V-03 Total: 87 — NOT GOLDEN (C-01, C-02 PARTIAL → all_essential_pass FALSE)**

---

### V-04 — Role Sequence + Output Format (Combined)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Phase 4 YAML template includes all 6 top-level fields + sub-fields; "Fill in every slot. Do not leave any field empty" |
| C-02 | **PASS** | Phase 2 requires: "inertia-advocate must include at least one verify question of the form: 'Why is the current approach insufficient...?'" |
| C-03 | **PASS** | Phase 2 STOCK-ROLES block: pm, architect, strategy, inertia-advocate |
| C-04 | **PASS** | Phase 3 area slug + Phase 4 writes to `.craft/roles/{area}/` |
| C-05 | **PASS** | Phase 1 DOMAIN-ANALYSIS derives experts from concerns; "not 'domain-expert'" |
| C-06 | **PASS** | Template: serves = "Must name a beneficiary, not restate frame" — negative constraint |
| C-07 | **PASS** | verify: "Not rhetorical or universal"; simplify: "phrased as a prohibition or elimination, not a description of good practice" |
| C-08 | **PASS** | "Every listed role must exist in the full role set. No phantom names." |
| C-09 | **PASS** | Template: "Second question: surfaces a concern unique to this role's frame" — explicit uniqueness instruction |
| C-10 | **PASS** | Phase 5 REGISTRY.md template + completion condition: "all five fields (area, count, stock names, domain expert names+source, gaps) are present" |
| C-11 | **PASS** | Phase 1 domain-only + "Do not name PM, Architect, Strategy, or inertia-advocate in Phase 1"; Phase 2 loads stock roles |
| C-12 | **PARTIAL** | Three negative constraints (serves: "not restate frame"; verify: "not rhetorical or universal"; simplify: "not a description of good practice") — meets minimum but lacks FAILURE MODE labels and worked examples |
| C-13 | **PASS** | Every phase has explicit output template: DOMAIN-ANALYSIS block, STOCK-ROLES block, role file YAML template, REGISTRY.md template with frontmatter |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 4.5/5 × 10 = **9** (C-12 PARTIAL 0.5)
**V-04 Total: 99 — GOLDEN (all essential pass)**

---

### V-05 — Phrasing Register + Lifecycle Emphasis: DO/DO NOT with Completion Conditions

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Phase 3 completion condition: "every file contains all six top-level fields with all required sub-fields filled (not empty strings or placeholder text)" — explicit structural gate |
| C-02 | **PASS** | Phase 2: "DO confirm the inertia-advocate's lens will include at least one question of the form: 'Why is the current approach insufficient...?'" + "DO NOT skip the inertia-advocate. A registry without a devil-advocate role fails C-02 unconditionally." |
| C-03 | **PASS** | Phase 2 STOCK-ROLES-LOADED: pm, architect, strategy, inertia-advocate |
| C-04 | **PASS** | "DO NOT use `default`, `generic`, or `roles` as the area name" |
| C-05 | **PASS** | Phase 1: "DO NOT list concerns that apply to any software product" — domain specificity enforced |
| C-06 | **PASS** | frame: DO NOT = "FAILURE MODE: frame becomes a job description"; serves: DO NOT = "FAILURE MODE: two fields carry identical information; downstream skills...receive no additional signal" |
| C-07 | **PASS** | verify: DO NOT rhetorical (FAILURE MODE: unanswerable) + DO NOT universal (FAILURE MODE: not owned by role's frame); simplify: DO NOT scope description (FAILURE MODE: masquerading as constraint) |
| C-08 | **PASS** | collaborates_with: DO NOT list every role (FAILURE MODE: no structural information); DO NOT list phantom role (FAILURE MODE: silently breaks integration) |
| C-09 | **PASS** | "DO ensure at least one question per role surfaces a concern unique to this role that no other role in the registry would prioritize" — explicit cross-role uniqueness requirement |
| C-10 | **PASS** | Phase 4 lists all 5 fields numerically; "DO NOT write a heading-only stub — FAILURE MODE: '## Registry Summary' with no content below fails C-10 unconditionally"; completion condition: "all five fields present with non-empty content" |
| C-11 | **PASS** | Phase 1 domain-only + "DO NOT name PM, Architect, Strategy, or inertia-advocate in this phase"; Phase 2 loads stock roles — explicit prohibition in phase definition |
| C-12 | **PASS** | 8+ named FAILURE MODEs across all fields (frame, serves, verify×2, simplify, depth, relevance, collaborates_with×2) with labeled collapse patterns; DO/DO NOT structure embeds negative examples by construction |
| C-13 | **PASS** | Every phase has explicit completion condition defining required output state; Phase 3 completion condition enumerates all 6 fields; Phase 4 completion condition enumerates all 5 registry fields — no heading-only steps |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 5/5 × 10 = **10**
**V-05 Total: 100 — GOLDEN (all essential pass)**

---

## Summary Scorecard

| V | Essential (60) | Recommended (30) | Aspirational (10) | Total | Golden? |
|---|---------------|-----------------|------------------|-------|---------|
| V-05 | 60 (5/5) | 30 (3/3) | 10 (5/5) | **100** | YES |
| V-04 | 60 (5/5) | 30 (3/3) | 9 (4.5/5) | **99** | YES |
| V-01 | 60 (5/5) | 25 (2.5/3) | 8 (4/5) | **93** | YES |
| V-02 | 54 (4.5/5) | 30 (3/3) | 8 (4/5) | **92** | NO (C-02 PARTIAL) |
| V-03 | 48 (4/5) | 30 (3/3) | 9 (4.5/5) | **87** | NO (C-01, C-02 PARTIAL) |

**Rank: V-05 > V-04 > V-01 > V-02 > V-03**

---

## Excellence Signals from V-05

**What made V-05 the top scorer:**

1. **Per-phase completion conditions as structural output gates** — instead of relying on a fill-in-the-blank template to enforce C-13, V-05 defines a completion condition for each phase that explicitly names the required output and prohibits advancing without it. This produces stronger C-13 compliance than templates alone because the gate is at the phase boundary, not inside the field instructions.

2. **Rubric-criterion cross-referencing in instructions** — embedding "fails C-02 unconditionally" directly in the skill instruction ties the requirement to the evaluation criterion, making the requirement non-negotiable and telling the model exactly what's at stake. No other variation names a rubric criterion by ID inside the instruction.

3. **DO/DO NOT paired-instruction format with downstream consequence named in FAILURE MODE** — V-05's failure modes go beyond naming the collapse pattern to naming the downstream consequence ("downstream skills that read `serves` separately from `frame` receive no additional signal"; "phantom names silently fail integration"). Consequential failure modes are stronger than pattern-only failure modes.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-phase completion conditions as structural output gates — enforce C-13 without a fill-in-the-blank template by requiring named output state before phase advance", "rubric-criterion cross-referencing — embed criterion IDs ('fails C-02 unconditionally') in skill instructions to make requirements unambiguous and non-negotiable", "consequential failure modes — name the downstream breakage caused by the failure, not just the collapse pattern (e.g., 'phantom names silently fail integration' vs 'do not use phantom names')"]}
```
