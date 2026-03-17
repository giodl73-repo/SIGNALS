## org-roles R3 Scoring — v3 Rubric

---

### Scoring Table

#### V-01 — Phrasing Register: Worked Examples

| ID | Category | Verdict | Evidence |
|----|----------|---------|---------|
| C-01 | Essential | **PASS** | All six top-level fields and sub-fields in template; `verify_questions`/`simplify_rules` exact names used |
| C-02 | Essential | **PASS** | inertia-advocate in stock roles; Phase 2 requires status-quo question "Why is the current approach insufficient…" |
| C-03 | Essential | **PASS** | pm, architect, strategy, inertia-advocate all named in STOCK-ROLES |
| C-04 | Essential | **PASS** | `.craft/roles/{area}/` output path; Phase 4 writes individual `.md` files |
| C-05 | Essential | **PASS** | Phase 1 derives domain experts from context before stock roles; "Do not name PM, Architect…" |
| C-06 | Recommended | **PASS** | frame: perspective statement "Sees X through lens of Y"; serves: beneficiary statement; WORKED EXAMPLE demonstrates divergence |
| C-07 | Recommended | **PASS** | verify_questions: "answerable by reading an artifact or running code"; simplify_rules: "prohibition or elimination" with FAILURE MODE |
| C-08 | Recommended | **PASS** | FAILURE MODE (type 1) phantom and FAILURE MODE (type 2) universalist both present in collaborates_with |
| C-09 | Aspirational | **PASS** | Template says "second question: surfaces a concern unique to this role's frame — no other role would prioritize this question first" |
| C-10 | Aspirational | **PASS** | Phase 5 template has all five fields: area, total_roles, stock role names, domain experts with derivation, coverage gaps |
| C-11 | Aspirational | **PASS** | Phase 1 (domain analysis) precedes Phase 2 (stock roles); stock role names prohibited in Phase 1 |
| C-12 | Aspirational | **PASS** | frame: "FAILURE MODE: task list"; serves: "FAILURE MODE: frame restatement"; simplify_rules: "FAILURE MODE: scope description" — three labeled failure modes |
| C-13 | Aspirational | **PASS** | Every phase defines an artifact format: DOMAIN-ANALYSIS block, STOCK-ROLES block, OUTPUT-AREA line, role file template, REGISTRY.md template |
| C-14 | Aspirational | **PASS** | "FAILURE MODE (type 1): phantom role" and "FAILURE MODE (type 2): universalist listing" both labeled in collaborates_with |
| C-15 | Aspirational | **PASS** | Phase 5: "FAILURE MODE: heading-only stub — a section header with no required content beneath it is not a complete registry entry and fails C-10 unconditionally" |
| C-16 | Aspirational | **PARTIAL** | Phases 1, 2, 4, 5 have "Phase X complete when…" conditions; Phase 3 (OUTPUT-AREA, an output step) has none |
| C-17 | Aspirational | **PASS** | Worked examples on frame, serves, simplify_rules — exactly three fields; each has WORKED EXAMPLE (bad) and WORKED EXAMPLE (good) |

**Essential**: 5/5 × 60 = 60.0 | **Recommended**: 3/3 × 30 = 30.0 | **Aspirational**: 8.5/9 × 10 = 9.44
**V-01 composite: 99.44 — GOLDEN**

---

#### V-02 — Lifecycle Emphasis: Binary Completion Gates

| ID | Category | Verdict | Evidence |
|----|----------|---------|---------|
| C-01 | Essential | **PASS** | All six top-level fields and sub-fields; exact field names in template |
| C-02 | Essential | **PASS** | inertia-advocate listed; GATE item 4 confirms "status-quo question pattern" |
| C-03 | Essential | **PASS** | pm, architect, strategy, inertia-advocate in STOCK-ROLES |
| C-04 | Essential | **PASS** | `.craft/roles/{area}/` path |
| C-05 | Essential | **PASS** | Domain experts derived in Phase 1 before stock roles |
| C-06 | Recommended | **PASS** | frame: "Must not be a task list or job description"; serves: "Must not restate frame" — clear differentiation |
| C-07 | Recommended | **PASS** | verify_questions: "answerable by reading an artifact or running code"; simplify_rules: "prohibition or elimination, not a description" |
| C-08 | Recommended | **PASS** | FAILURE MODE (type 1) and (type 2) present |
| C-09 | Aspirational | **PASS** | "Second question unique to this role's frame" in template |
| C-10 | Aspirational | **PASS** | Phase 5 GATE verifies all five registry fields |
| C-11 | Aspirational | **PASS** | Context analysis Phase 1 before stock roles Phase 2 |
| C-12 | Aspirational | **PASS** | frame: "Must not be a task list or job description" (names "task list"); serves: "Must not restate frame" (names "frame restatement") — two named failure modes |
| C-13 | Aspirational | **PASS** | Every phase defines its output format |
| C-14 | Aspirational | **PASS** | FAILURE MODE (type 1) and (type 2) labeled in collaborates_with |
| C-15 | Aspirational | **PASS** | Phase 5: "FAILURE MODE: heading-only stub — a section header with no content beneath it is not a summary" |
| C-16 | Aspirational | **PASS** | GATE checklist at every phase: Phase 1 (4 conditions), Phase 2 (4), Phase 3 (3), Phase 4 (5), Phase 5 (6) |
| C-17 | Aspirational | **FAIL** | No WORKED EXAMPLE (bad)/WORKED EXAMPLE (good) pairs in any field; negative constraints are label-only ("Must not be a task list") with no illustrative content |

**Essential**: 5/5 × 60 = 60.0 | **Recommended**: 3/3 × 30 = 30.0 | **Aspirational**: 8/9 × 10 = 8.89
**V-02 composite: 98.89 — GOLDEN**

---

#### V-03 — Inertia Framing

| ID | Category | Verdict | Evidence |
|----|----------|---------|---------|
| C-01 | Essential | **PASS** | All six fields and sub-fields; exact field names in template |
| C-02 | Essential | **PASS** | Design contract in preamble elevates inertia-advocate to structural anchor; Step 2 dedicated to inertia-advocate specification; domain-specific status-quo claim required |
| C-03 | Essential | **PASS** | pm, architect, strategy, inertia-advocate in STOCK-ROLES (Step 3) |
| C-04 | Essential | **PASS** | `.craft/roles/{area}/` output path |
| C-05 | Essential | **PASS** | Step 1 derives domain experts from context before stock roles |
| C-06 | Recommended | **PASS** | frame: "epistemic viewpoint, not a task list"; serves: "Must not restate frame" |
| C-07 | Recommended | **PASS** | verify_questions: "answerable by reading an artifact or running code"; simplify_rules: "prohibition or elimination, not a description of good practice" |
| C-08 | Recommended | **PASS** | FAILURE MODE (type 1) phantom and FAILURE MODE (type 2) universalist |
| C-09 | Aspirational | **PASS** | Inertia-response question required for every domain expert — a role-unique question by construction; plus generic "second question unique to frame" instruction |
| C-10 | Aspirational | **PASS** | Step 6 registry template adds "Inertia surface" field beyond the five required — all five fields present plus extras |
| C-11 | Aspirational | **PASS** | Step 1 (domain concerns) → Step 2 (inertia-advocate spec) → Step 3 (stock roles); strongest context-first ordering of all variates |
| C-12 | Aspirational | **PASS** | frame: "epistemic viewpoint, not a task list" (names "task list"); serves: "Must not restate frame"; simplify_rules: "not a description of good practice" — three named failure modes |
| C-13 | Aspirational | **PASS** | Every step defines its output format: DOMAIN-CONCERNS, DOMAIN-EXPERTS-DERIVED, INERTIA-ADVOCATE block, STOCK-ROLES, OUTPUT-AREA, role file, REGISTRY.md |
| C-14 | Aspirational | **PASS** | "FAILURE MODE (type 1): phantom role" and "FAILURE MODE (type 2): universalist listing" in collaborates_with |
| C-15 | Aspirational | **PASS** | Step 6: "FAILURE MODE: heading-only stub — a section header with no content beneath it fails C-10 unconditionally" |
| C-16 | Aspirational | **PARTIAL** | Steps 1, 2, 3, 5, 6 have "Step X complete when…" conditions; Step 4 (OUTPUT-AREA, an output step) has no completion condition |
| C-17 | Aspirational | **FAIL** | No WORKED EXAMPLE pairs in any field; all failure-mode constraints are label-only ("not a task list", "Must not restate frame") |

**Essential**: 5/5 × 60 = 60.0 | **Recommended**: 3/3 × 30 = 30.0 | **Aspirational**: 7.5/9 × 10 = 8.33
**V-03 composite: 98.33 — GOLDEN**

---

#### V-04 — Combined: Worked Examples + Completion Gates

| ID | Category | Verdict | Evidence |
|----|----------|---------|---------|
| C-01 | Essential | **PASS** | All six fields and sub-fields in template; exact field names used |
| C-02 | Essential | **PASS** | inertia-advocate required; GATE item 3 confirms status-quo question pattern |
| C-03 | Essential | **PASS** | pm, architect, strategy, inertia-advocate |
| C-04 | Essential | **PASS** | `.craft/roles/{area}/` path |
| C-05 | Essential | **PASS** | Context-first Phase 1 derivation |
| C-06 | Recommended | **PASS** | frame/serves differentiated with WORKED EXAMPLE (bad) showing serves restating frame |
| C-07 | Recommended | **PASS** | verify_questions: "Not rhetorical"; simplify_rules: WORKED EXAMPLE distinguishes constraint from scope description |
| C-08 | Recommended | **PASS** | FAILURE MODE (type 1) and (type 2) |
| C-09 | Aspirational | **PASS** | "no other role in this registry would prioritize this question first" |
| C-10 | Aspirational | **PASS** | Phase 5 GATE: all five fields verified; stub failure mode named explicitly in Phase 5 instruction |
| C-11 | Aspirational | **PASS** | Phase 1 before Phase 2; stock role names prohibited in Phase 1 |
| C-12 | Aspirational | **PASS** | frame: "FAILURE MODE: task list — frame becomes a job description"; serves: "FAILURE MODE: frame restatement — serves paraphrases frame"; simplify_rules: "FAILURE MODE: scope description — rule describes what to prioritize, not what to remove" |
| C-13 | Aspirational | **PASS** | Every phase has output format template |
| C-14 | Aspirational | **PASS** | "FAILURE MODE (type 1): phantom role" and "FAILURE MODE (type 2): universalist listing" |
| C-15 | Aspirational | **PASS** | "'## Registry Summary' with no required content beneath it fails C-10 unconditionally. The heading is not the summary; all five fields are the summary." |
| C-16 | Aspirational | **PASS** | GATE at every phase: Phase 1 (4), Phase 2 (3), Phase 3 (3), Phase 4 (7), Phase 5 (6) — all output steps covered |
| C-17 | Aspirational | **PASS** | WORKED EXAMPLE (bad)/(good) pairs on frame, serves, simplify_rules — exactly three fields, meeting the ≥3 threshold |

**Essential**: 5/5 × 60 = 60.0 | **Recommended**: 3/3 × 30 = 30.0 | **Aspirational**: 9/9 × 10 = 10.0
**V-04 composite: 100.00 — GOLDEN**

---

#### V-05 — All Four Axes Integrated

| ID | Category | Verdict | Evidence |
|----|----------|---------|---------|
| C-01 | Essential | **PASS** | All six fields; Phase 4 GATE item 3 explicitly checks `verify_questions` (not `verify`) and `simplify_rules` (not `simplify`) — integration correctness enforced structurally |
| C-02 | Essential | **PASS** | inertia-advocate required; GATE item 3 confirms status-quo question; inertia-response question required for every domain expert in Phase 1 |
| C-03 | Essential | **PASS** | pm, architect, strategy, inertia-advocate |
| C-04 | Essential | **PASS** | `.craft/roles/{area}/` path |
| C-05 | Essential | **PASS** | Context-first Phase 1; Phase 1 GATE item 4 prohibits stock role names |
| C-06 | Recommended | **PASS** | frame/serves differentiated with WORKED EXAMPLE pairs; serves example specifically shows zero-additional-signal failure |
| C-07 | Recommended | **PASS** | verify_questions FAILURE MODE (type 1): rhetorical question; FAILURE MODE (type 2): universal question — typed failure modes applied to a second field beyond collaborates_with |
| C-08 | Recommended | **PASS** | FAILURE MODE (type 1) and (type 2) |
| C-09 | Aspirational | **PASS** | "no other role would prioritize this question first" plus required inertia-response question for domain experts — each domain expert has a structurally unique third verify question |
| C-10 | Aspirational | **PASS** | Phase 5 GATE: all five fields; domain experts listed with both derivation source and inertia objection |
| C-11 | Aspirational | **PASS** | Phase 1 → Phase 2 (stock roles); Phase 1 GATE prohibits stock names |
| C-12 | Aspirational | **PASS** | frame, serves, simplify_rules, expertise.depth all carry FAILURE MODE labels — four fields, exceeding the ≥2 threshold; expertise.depth: "label without method — 'security expertise' names a domain but not a technique" |
| C-13 | Aspirational | **PASS** | Every phase has a defined output format |
| C-14 | Aspirational | **PASS** | "FAILURE MODE (type 1): phantom role" and "FAILURE MODE (type 2): universalist listing" both typed |
| C-15 | Aspirational | **PASS** | "FAILURE MODE (C-15): heading-only stub — a section header (`## Registry Summary`) with no required content beneath it is not a complete registry entry and fails C-10 unconditionally." Explicitly references C-15 by name. |
| C-16 | Aspirational | **PASS** | GATE at every phase: Phase 1 (4), Phase 2 (3), Phase 3 (3), Phase 4 (10), Phase 5 (6) — all output steps covered; 10-item Phase 4 GATE is most comprehensive |
| C-17 | Aspirational | **PASS** | WORKED EXAMPLE pairs on frame, serves, simplify_rules, AND collaborates_with — four fields; collaborates_with examples show phantom/universalist failures with concrete before/after role names |

**Essential**: 5/5 × 60 = 60.0 | **Recommended**: 3/3 × 30 = 30.0 | **Aspirational**: 9/9 × 10 = 10.0
**V-05 composite: 100.00 — GOLDEN**

---

### Score Summary

| Variate | Essential | Recommended | Aspirational | Composite | Band |
|---------|-----------|-------------|--------------|-----------|------|
| V-05 | 5/5 | 3/3 | 9/9 | **100.00** | GOLDEN |
| V-04 | 5/5 | 3/3 | 9/9 | **100.00** | GOLDEN |
| V-01 | 5/5 | 3/3 | 8.5/9 | **99.44** | GOLDEN |
| V-02 | 5/5 | 3/3 | 8/9 | **98.89** | GOLDEN |
| V-03 | 5/5 | 3/3 | 7.5/9 | **98.33** | GOLDEN |

**Rank**: V-05 = V-04 > V-01 > V-02 > V-03

V-04 and V-05 tie at 100 within the rubric's pass conditions. V-05 is the aspirational ceiling: it exceeds every threshold (four worked-example fields vs. the three-field minimum; four FAILURE MODE labels in C-12 vs. the two-field minimum) and introduces patterns that no prior variate demonstrated.

---

### Excellence Signals from V-05

**1. Typed failure modes applied to a second field (verify_questions)**
V-03/V-04 established typed failure modes on `collaborates_with`. V-05 extends the pattern: `verify_questions` carries FAILURE MODE (type 1) rhetorical and FAILURE MODE (type 2) universal. Every field with dual failure modes now carries type identifiers — the recovery path is available wherever the model might err.

**2. Worked example on `collaborates_with`**
V-01/V-04 applied worked examples to frame, serves, simplify_rules. V-05 adds a fourth field: `collaborates_with` gets before/after pairs naming actual roles (`- signal:data-quality-monitor` as phantom, `- signal:pm` as valid). The relationship-level failure is shown visually rather than stated as a rule.

**3. Phase 4 GATE field-name integrity check (item 3)**
V-05 explicitly asserts in the Phase 4 completion condition: "Every field uses exact names: `verify_questions` (not `verify`), `simplify_rules` (not `simplify`)." This is the only variate that catches the silent integration failure at GATE time — all others rely on the template using correct names but never verify the model applied them.

**4. Inertia-response question integrated into Phase 1 derivation**
V-03 introduced the inertia-response pattern. V-05 moves it earlier: each domain expert's Phase 1 derivation block includes the anticipated inertia objection alongside the candidate frame. The dialogue structure is created at derivation time, not retrofitted at output time — the model must answer the devil-advocate's objection before it writes a single role file.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["verify_questions typed dual-failure labels (type 1: rhetorical, type 2: universal) — extends typed-failure pattern from collaborates_with to a second field", "worked example on collaborates_with showing phantom and universalist failures with concrete role name pairs", "Phase 4 GATE explicit field-name integrity check for verify_questions/simplify_rules exact names", "inertia-response question integrated into Phase 1 domain expert derivation block — structures the inertia dialogue before role files are written"]}
```
