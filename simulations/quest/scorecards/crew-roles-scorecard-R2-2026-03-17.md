# crew-roles — Quest Score (Round 2, Rubric v2)

## Scoring Matrix

Using the v2 rubric formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)`

---

### V-01 — Vocabulary-Forced-Field (C-11 axis)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All 5 fields | PASS | Template explicitly shows all 5 fields; Phase 3a constraint enforces presence |
| C-02 Inertia-advocate | PASS | Phase 3b includes adversarial orientation.frame + verify must reference pre-characterization specifics |
| C-03 Correct path | PASS | `.craft/roles/{area}/` stated at top |
| C-04 Domain specificity | PASS | Phase 1 vocabulary extraction drives role selection; expertise.relevance structurally anchored |
| C-05 Min 3 roles | PASS | "Minimum: 3 roles including inertia-advocate" |
| C-06 Lens actionability | PASS | Template: verify `?` and imperative simplify |
| C-07 Collaborates_with resolves | PARTIAL | `{role-name}` placeholder — no orphan-check mechanism |
| C-08 Perspective diversity | PASS | PM (product) + Architect (technical) + inertia + domain = 3+ categories |
| C-09 Scope gradient | PARTIAL | Multiple values in template; inertia set to cross-team but gradient not structurally enforced |
| C-10 Inertia domain-grounded | PASS | Phase 3b pre-characterization block + verify must reference specifics from it |
| C-11 Vocabulary-forced-field | PASS | Phase 1 extraction mandatory; constraint on every expertise.relevance field |
| C-12 Inertia pre-characterization | PASS | Phase 3b: 3-question block (current system / migration costs / user habits) before writing |
| C-13 Registry summary table | FAIL | No post-write table in V-01 |

**Score**: 60 + (2.5/3 × 30) + (3.5/5 × 10) = **92**

---

### V-02 — Inertia Pre-Characterization (C-12 axis)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All 5 fields | PASS | Template shows all 5 fields |
| C-02 Inertia-advocate | PASS | Step 1 block gates inertia-advocate; verify constrained to name current system and cost/habit |
| C-03 Correct path | PASS | `.craft/roles/{area}/` stated |
| C-04 Domain specificity | PASS | Explicit instruction: "no generic engineering language" on expertise.relevance |
| C-05 Min 3 roles | PASS | "Minimum 3 roles" |
| C-06 Lens actionability | PASS | Verify `?`; simplify imperative — enforced by examples in constraint text |
| C-07 Collaborates_with resolves | PASS | Template constraint: `{role-name matching another file in this registry}` — explicit match requirement |
| C-08 Perspective diversity | PASS | PM + technical (architect/SRE/security/data) + inertia = 3 categories |
| C-09 Scope gradient | PARTIAL | No gradient requirement stated; inertia scope not explicitly set |
| C-10 Inertia domain-grounded | PASS | Step 1 forces named system, named cost, named habit; verify must reference at least 2 |
| C-11 Vocabulary-forced-field | FAIL | No Phase 1 vocabulary extraction; domain specificity is instruction-only |
| C-12 Inertia pre-characterization | PASS | Step 1 is a full Q1/Q2/Q3 block gating the inertia-advocate |
| C-13 Registry summary table | FAIL | No post-write table |

**Score**: 60 + (3/3 × 30) + (2.5/5 × 10) = **95**

---

### V-03 — Registry Summary Table (C-13 axis)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All 5 fields | PASS | Template shows all 5 fields |
| C-02 Inertia-advocate | PASS | Step 3 rules: orientation.frame must include "challenge/status quo"; verify must ask "why is [current approach] insufficient?" with domain specificity |
| C-03 Correct path | PASS | `.craft/roles/{area}/` stated |
| C-04 Domain specificity | PASS | Expertise template: "specific to this domain and input context" |
| C-05 Min 3 roles | PASS | "Minimum 3 roles total" |
| C-06 Lens actionability | PASS | Verify `?`; simplify constrained to Remove/Collapse/Defer/Merge/Move |
| C-07 Collaborates_with resolves | PASS | Step 4 orphan check: marks `[UNRESOLVED]`, requires fix before delivery |
| C-08 Perspective diversity | PASS | PM + Architect + domain + inertia = 3+ categories |
| C-09 Scope gradient | PASS | Step 4 scope gradient check: if all same, "identify 1–2 roles... and revise" |
| C-10 Inertia domain-grounded | PASS | Inertia rule: "[current approach]" must be domain-specific, not generic |
| C-11 Vocabulary-forced-field | FAIL | No Phase 1 vocabulary extraction phase |
| C-12 Inertia pre-characterization | PARTIAL | Step 1 context analysis identifies "current system" but does not extract migration costs or user habits systematically |
| C-13 Registry summary table | PASS | Step 4 mandatory table + orphan check + scope gradient check before delivery |

**Score**: 60 + (3/3 × 30) + (3.5/5 × 10) = **97**

---

### V-04 — Vocabulary + Inertia Pre-Characterization (C-11 + C-12)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All 5 fields | PASS | Template shows all 5 fields |
| C-02 Inertia-advocate | PASS | Phase 2 block + orientation.frame must name current system; 3 verify questions each referencing Q1/Q2/Q3 |
| C-03 Correct path | PASS | `.craft/roles/{area}/` stated |
| C-04 Domain specificity | PASS | Phase 1 vocabulary structurally anchors expertise.relevance; role names must be vocabulary-derivable |
| C-05 Min 3 roles | PASS | PM + Architect + Inertia + domain roles |
| C-06 Lens actionability | PASS | Template: verify `?`; simplify imperative |
| C-07 Collaborates_with resolves | PARTIAL | `{role-name}` placeholder — no orphan-check mechanism |
| C-08 Perspective diversity | PASS | PM + Architect + inertia + domain = 3+ categories |
| C-09 Scope gradient | PARTIAL | Inertia-advocate set to cross-team; other scope values template-guided but not enforced |
| C-10 Inertia domain-grounded | PASS | Phase 2 vocabulary-linked characterization; all 3 dimensions appear in verify questions |
| C-11 Vocabulary-forced-field | PASS | Phase 1 extraction + constraint on every expertise.relevance; "rename the role" escape hatch |
| C-12 Inertia pre-characterization | PASS | Phase 2 explicit Q1/Q2/Q3 block using Phase 1 vocabulary; each answer must reference a vocab term |
| C-13 Registry summary table | FAIL | No post-write table |

**Score**: 60 + (2.5/3 × 30) + (3.5/5 × 10) = **92**

---

### V-05 — Full Integration (C-11 + C-12 + C-13)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 All 5 fields | PASS | Phase 3 exit condition: "all role files written with all 5 fields present" |
| C-02 Inertia-advocate | PASS | orientation.frame must include current system name verbatim; 3 separate distribution constraints (Q1/Q2/Q3) |
| C-03 Correct path | PASS | `.craft/roles/{area}/` stated |
| C-04 Domain specificity | PASS | Phase 1 vocabulary + Phase 3 exit condition checks vocabulary term in every expertise.relevance |
| C-05 Min 3 roles | PASS | "Minimum 1 domain role beyond stock" = 4+ total |
| C-06 Lens actionability | PASS | Verify `?`; simplify constrained to listed imperative verbs (Remove/Collapse/Defer/Merge/Move) |
| C-07 Collaborates_with resolves | PASS | Phase 4 orphan check: traverses all references, marks `[UNRESOLVED]`, state action taken |
| C-08 Perspective diversity | PASS | PM + Architect + inertia + required domain role = 3+ categories; domain role requirement ensures non-stock perspective |
| C-09 Scope gradient | PASS | Phase 4 Check 2 enforces 2+ distinct scope values; self-correcting before delivery |
| C-10 Inertia domain-grounded | PASS | Phase 2 characterization + orientation.frame verbatim binding + Q1+Q2+Q3 each covered in verify |
| C-11 Vocabulary-forced-field | PASS | Phase 1 exit condition (3+ terms); Phase 3 exit condition verifies all expertise.relevance fields |
| C-12 Inertia pre-characterization | PASS | Phase 2 exit condition: all 3 answers with at least one vocab term each; verify distribution requires Q1, Q2, Q3 separately |
| C-13 Registry summary table | PASS | Phase 4 mandatory table + 2 self-verification checks (orphan + scope) with explicit exit condition |

**Score**: 60 + (3/3 × 30) + (5/5 × 10) = **100**

---

## Rankings

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| 1 | V-05 | 100 | Yes | All 13 criteria pass; phase-gated exit conditions |
| 2 | V-03 | 97 | Yes | Table + scope gradient + C-07 orphan check; C-11/C-12 partial gaps |
| 3 | V-02 | 95 | Yes | Full pre-characterization + all recommended; no vocabulary/table |
| 4 | V-01 | 92 | Yes | Vocabulary + inertia pre-char; no table, C-07 partial |
| 4 | V-04 | 92 | Yes | Vocabulary + inertia pre-char (stronger); no table, C-07 partial |

---

## Excellence Signals from V-05

**1. Phase-gated execution with explicit exit conditions**
Each phase has a named entry requirement and an exit condition that must be met before the next phase starts. This transforms the skill from a template into a verified pipeline — the model cannot skip the vocabulary step or the inertia pre-characterization because the next phase's entry condition depends on them.

**2. Per-dimension verify distribution (not "2 of 3")**
V-05 requires one verify question per dimension (Q1 + Q2 + Q3 separately) rather than "at least 2 of 3." This eliminates the drift path where Q1 (current system name) is referenced twice and Q3 (user habit) is silently dropped. The constraint is additive, not substitutable.

**3. Verbatim current-system binding in orientation.frame**
The orientation.frame constraint `"Challenge every proposal with evidence that [current system] remains sufficient given [migration cost]"` requires the current system name to appear verbatim. Generic orientation language ("Challenge every proposal with why the current approach is sufficient") passes C-02 but fails V-05's stricter inertia frame. This makes C-10 structurally verified by C-02.

**4. Self-verifying phase exit conditions**
Phase 2 exit condition: "all 3 answers written AND at least one vocabulary term present in each." Phase 3 exit condition: "every expertise.relevance field contains a vocabulary term; inertia-advocate's lens.verify references Q1, Q2, and Q3 dimensions." These force the execution to self-audit against quality properties before moving on — not just complete tasks.

**5. Table as structural integration test**
Phase 4 is not merely a summary step — it is a cross-reference traversal and scope-gradient enforcement mechanism with its own exit condition. The table forces the role files to be treated as a linked registry rather than independent files.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase-gated execution with explicit exit conditions per phase", "per-dimension verify distribution requiring Q1+Q2+Q3 each separately rather than 2-of-3 substitution", "verbatim current-system binding in orientation.frame structurally enforcing C-10 via C-02"]}
```
