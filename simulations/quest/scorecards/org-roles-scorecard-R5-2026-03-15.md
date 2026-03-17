## org-roles Scorecard — Round 5 (Rubric v5)

**Date:** 2026-03-16
**Rubric:** v5 (C-01–C-25; 5 essential, 3 recommended, 17 aspirational)
**Formula:** essential/5×60 + recommended/3×30 + aspirational/17×10

---

### Criterion-by-Criterion Evaluation

#### Essential (C-01–C-05)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| **C-01** Role schema completeness | PASS — template shows all 6 fields with correct sub-fields; verify_questions and simplify_rules appear verbatim as YAML keys | PASS — FIELD CONTRACT [FC-1]–[FC-10] enumerates every schema field and sub-field as binding identifiers | PASS — template matches full schema; exact sub-field names in PREPARE retrieve list | PASS — template fills all 6 fields; WORKED EXAMPLEs guide each field | PASS — FIELD CONTRACT + template redundantly cover all 6 fields |
| **C-02** Devil-advocate role | PASS — Phase 3 inertia-advocate: orientation.frame anchored to Phase 1 status-quo claim; verify_questions are Phase 1 why-not-build questions (status-quo-specific, not generic skepticism) | PASS — Phase 3 inertia-advocate: verify_questions from Phase 2 INERTIA-SURFACE challenge questions, which directly challenge feature necessity | PASS — Phase 3 inertia-advocate: verify_questions from Phase 2 challenge questions grounded in domain vocabulary | PASS — Phase 3 inertia-advocate: orientation.frame anchored to Phase 1 status-quo claim; explicit "status-quo challenge lens" descriptor | PASS — Phase 3 inertia-advocate: orientation.frame anchored to Phase 1; verify_questions from Phase 1 challenge questions; strongest grounding chain |
| **C-03** Stock roles present | PASS — Phase 3 lists pm, architect, strategy, inertia-advocate explicitly | PASS — Phase 3 STOCK-ROLES block names all four | PASS — Phase 3 STOCK-ROLES names all four | PASS — Phase 3 lists all four with lens descriptors | PASS — Phase 3 lists all four with lens descriptors |
| **C-04** Output location | PASS — Phase 4 OUTPUT-AREA: .craft/roles/{area}/; Phase 5 writes files there; REGISTRY.md at .craft/roles/{area}/REGISTRY.md | PASS — same path derivation pattern | PASS — same | PASS — same | PASS — same |
| **C-05** Context-derived domain expert | PASS — Phase 2 derives experts explicitly from Phase 1 status-quo challenge; each expert must have "domain-vocabulary frame" sourced from concern vocabulary | PASS — Phase 1 requires domain-vocabulary frame per expert from actual context, not generic templates; [FC-1] prohibits "domain-expert" or "expert-1" names | PASS — Phase 1 requires domain-vocabulary frame from actual context per expert | PASS — Phase 2 derives experts in response to Phase 1 status-quo challenge; frames use concern vocabulary | PASS — Phase 2 derives experts from Phase 1 challenge; FIELD CONTRACT [FC-2] enforces non-generic epistemic viewpoint |

**Essential result: all five → 5/5 → 60 pts each**

---

#### Recommended (C-06–C-08)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| **C-06** Orientation coherence | PASS — template: frame = epistemic viewpoint ("Sees every X through the lens of Y"), serves = beneficiary statement that "Must not restate frame"; WORKED EXAMPLE (bad) shows frame-restatement for serves | PASS — [FC-2] "epistemic viewpoint — NOT a task list"; [FC-3] "beneficiary statement; NOT a restatement of frame"; BAD/GOOD contrastive pairs for both | PASS — same FAILURE MODE structure with WORKED EXAMPLEs for both frame and serves | PASS — WORKED EXAMPLEs for both; "FAILURE MODE: task list" and "FAILURE MODE: frame restatement" labeled | PASS — FIELD CONTRACT [FC-2]/[FC-3] with BAD/GOOD pairs + template FAILURE MODES reinforce both sub-fields |
| **C-07** Lens quality | PASS — verify_questions: "answerable by reading an artifact, running code, or inspecting a measurable outcome"; simplify_rules: "prohibition or elimination ('Skip X unless Y', 'Do not include Z when W')"; WORKED EXAMPLE distinguishes description from constraint | PASS — [FC-4] actionable questions with BAD/GOOD; [FC-5] "opinionated exclusion or scope reduction — 'Skip X unless Y'" with BAD/GOOD | PASS — same constraint structure; FAILURE MODE for simplify_rules names "scope description without exclusion" with WORKED EXAMPLEs | PASS — FAILURE MODE labels + WORKED EXAMPLEs for both verify_questions and simplify_rules | PASS — FIELD CONTRACT [FC-4]/[FC-5] with BAD/GOOD + template redundant annotation |
| **C-08** Collaborates_with accuracy | PASS — "FAILURE MODE (type 1) — PHANTOM ROLE" and "FAILURE MODE (type 2) — UNIVERSALIST LISTING" in template; gate item 5 enforces both | PASS — "CONTRACT VIOLATION (type 1) — PHANTOM" and "CONTRACT VIOLATION (type 2) — UNIVERSALIST" in [FC-10]; both listed as gate failures | PASS — "FAILURE MODE (type 1): PHANTOM ROLE" and "FAILURE MODE (type 2): UNIVERSALIST LISTING" in template | PASS — "FAILURE MODE (type 1): PHANTOM ROLE" and "FAILURE MODE (type 2): UNIVERSALIST LISTING" in template | PASS — "CONTRACT VIOLATION (type 1)" and "CONTRACT VIOLATION (type 2)" in [FC-10] + template; dual mechanism |

**Recommended result: all five → 3/3 → 30 pts each**

---

#### Aspirational (C-09–C-25)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| **C-09** Role differentiation | PASS — template second verify_questions bullet mandates uniqueness during authoring; C-21 coverage makes C-09 satisfaction by construction | PASS — [FC-4] uniqueness requirement in contract + template reminder | PASS — template: "confirm this claim before writing; revise until uniquely attributable" | PASS — template: "no other role in this registry would prioritize this question first — Before writing, confirm" | PASS — [FC-4] contract + template diagnostic instruction; two independent mechanisms |
| **C-10** Registry summary completeness | PASS — Phase 6 template: area, total_roles, stock_roles (named), domain_experts (name+derivation_source), coverage_gaps, inertia_surface — all 5 required fields plus extension | PASS — same structure | PASS — same | PASS — same | PASS — same |
| **C-11** Context-first ordering | PASS — Phase 1 = inertia spec (context read), Phase 2 = domain expert derivation, Phase 3 = stock roles; domain experts before stock roles | PASS — Phase 1 = domain expert derivation, Phase 2 = inertia spec, Phase 3 = stock roles; context-derived experts before stock roles | PASS — Phase 1 = domain expert derivation before Phase 3 stock roles | PASS — Phase 1 = inertia spec, Phase 2 = domain expert derivation, Phase 3 = stock roles | PASS — Phase 1 = inertia spec, Phase 2 = domain expert derivation, Phase 3 = stock roles |
| **C-12** Failure-mode-named field constraints | PASS — "FAILURE MODE: task-list frame" (frame), "FAILURE MODE: frame restatement" (serves), "FAILURE MODE: scope description" (simplify_rules) — three named negative constraints | PASS — [FC-2] "NOT a task list", [FC-3] "NOT a restatement of frame", [FC-5] "NOT a description of what the role does" — four named failure modes in contract | PASS — same three FAILURE MODE labels as V-01 | PASS — "FAILURE MODE: task list", "FAILURE MODE: frame restatement", "FAILURE MODE: scope description — names priority without excluding" — three named | PASS — FIELD CONTRACT failure modes + template FAILURE MODE annotations; redundant naming |
| **C-13** Explicit step output format | PASS — every phase defines output: Phase 0 = EXTENSION-COMMITMENT block format, Phase 1 = INERTIA-SURFACE format, Phase 2 = DOMAIN-ANALYSIS format, Phase 3 = STOCK-ROLES block, Phase 4 = OUTPUT-AREA line, Phase 5 = full YAML template, Phase 6 = REGISTRY.md template | PASS — Phase 0 = EXTENSION-COMMITMENT + FIELD CONTRACT, subsequent phases same | PASS — all phases have WRITE sub-steps with explicit format templates | PASS — all phases have format templates | PASS — Phase 0 = EXTENSION-COMMITMENT + FIELD CONTRACT; all phases have formats |
| **C-14** Collaborates_with typed dual-failure | PASS — "(type 1)" and "(type 2)" explicit labels in template | PASS — "(type 1)" and "(type 2)" in [FC-10] | PASS — "(type 1)" and "(type 2)" in template | PASS — "(type 1)" and "(type 2)" in template | PASS — "(type 1)" and "(type 2)" in [FC-10] and template |
| **C-15** Registry heading-stub failure mode | **PASS** — "FAILURE MODE — HEADING STUB: a section header with no content below it is not a complete registry entry. '## Registry Summary' with no populated fields beneath it fails this step unconditionally." Explicit label + named example | **PASS** — "FAILURE MODE — HEADING STUB: '## Registry Summary' with no populated fields is not a registry. Every field above must contain substantive content." | **PARTIAL** — Gate item 5 "No heading stubs — every section contains substantive content below its header" prevents the failure but does not name the HEADING STUB failure mode explicitly or give a labeled example | **PASS** — "FAILURE MODE — HEADING STUB: writing '## Registry Summary' with no fields populated is not an answer to the diagnostic question." Explicit label. | **PASS** — "FAILURE MODE — HEADING STUB: '## Registry Summary' with no fields populated is not an answer to the diagnostic question. Every field above must contain substantive content that could not have been written without running all prior phases." |
| **C-16** Step completion condition | PASS — every phase has an explicit GATE with verifiable binary conditions | PASS — same | PASS — GATE sub-step per phase | PASS — same | PASS — PREPARE/WRITE/GATE structure; most explicit |
| **C-17** Worked examples in field constraints | PASS — frame: WORKED EXAMPLE (bad)+(good); serves: WORKED EXAMPLE (bad)+(good); simplify_rules: WORKED EXAMPLE (bad)+(good) — 3 fields with concrete examples | PASS — [FC-2], [FC-3], [FC-4], [FC-5] all have BAD/GOOD concrete examples — 4 fields | PASS — same 3 WORKED EXAMPLE pairs as V-01 | PASS — 3 WORKED EXAMPLE pairs (frame, serves, simplify_rules) + verify_questions uniqueness note | PASS — 4 FIELD CONTRACT BAD/GOOD pairs + 3 template WORKED EXAMPLE pairs — most coverage |
| **C-18** Contrastive worked example pairs | PASS — frame (bad+good in same field), serves (bad+good), simplify_rules (bad+good) — 3 contrastive pairs | PASS — [FC-2], [FC-3], [FC-4], [FC-5] each have BAD+GOOD in same item — 4 contrastive pairs | PASS — frame, serves, simplify_rules — 3 pairs in same template locations | PASS — frame, serves, simplify_rules — 3 pairs, all in template field comments | PASS — FIELD CONTRACT 4 pairs + template 3 pairs — highest count |
| **C-19** Enumerated multi-item completion gate | PASS — Phase 0: 3 items; Phase 1: 4 items; Phase 2: 5 items; Phase 3: 3 items; Phase 4: 3 items; Phase 5: 5 items; Phase 6: 5 items | PASS — all gates 3+ items | PASS — all GATE sub-steps 3+ items | PASS — all gates 3+ items | PASS — all PREPARE and GATE sections 3+ independent items |
| **C-20** Domain-specific registry extension | PASS — inertia_surface named in Phase 0 EXTENSION-COMMITMENT before any context read; grounded in Phase 1 INERTIA-SURFACE block; appears in Phase 6 REGISTRY.md template as named field | PASS — inertia_surface in Phase 0 EXTENSION-COMMITMENT; grounded in Phase 2 INERTIA-SURFACE | PASS — inertia_surface in Phase 0; grounded in Phase 2 INERTIA-SURFACE | PASS — inertia_surface in Phase 0; purpose answers diagnostic question before context read | PASS — inertia_surface in Phase 0 PART A; named before FIELD CONTRACT is written; grounded in Phase 1 |
| **C-21** Uniqueness mandate by construction | PASS — template verify_questions second bullet: "must be one that no other role in this registry would prioritize first — confirm before writing: if any other role would ask this question first, revise until this question is uniquely attributable to this role's frame" | PASS — [FC-4]: "confirm this before writing the question"; template: "confirm before writing; revise if any other role would ask this question first" | PASS — template: "must be one that no other role in this registry would prioritize first — confirm this claim before writing" | PASS — template: "This question is uniquely mine: no other role in this registry would prioritize this question first. Before writing, confirm..." | PASS — [FC-4] contract mandate + template instruction ("before writing, confirm — no other role...would prioritize this question first") |
| **C-22** Cross-step artifact count integrity | PASS — Phase 6 template: "COUNT — count the .md files written in Phase 5 before writing this number; do not carry forward the planned count from Phase 3"; gate item 2 requires same | PASS — Phase 6 template: "COUNT — before writing this number, count the .md files written in Phase 5"; gate item 2 enforces cross-step verification | PASS — Phase 6 PREPARE sub-step explicitly: "List all .md files written in Phase 5 (enumerate them); Record the count as PHASE5_COUNT; do not derive it from Phase 3 STOCK-ROLES plus Phase 1 domain expert counts" — strongest mechanism: pre-write input | PASS — Phase 6: "Before writing, count the .md files produced in Phase 5 — this count is total_roles"; gate item 2 requires enumeration | PASS — Phase 6 PREPARE names C-22 failure by type: "Derivation from prior-phase plans without verification is a C-22 failure"; PHASE5_COUNT required before WRITE begins |
| **C-23** Extension field commitment block | PASS — Phase 0 EXTENSION-COMMITMENT: field_name (inertia_surface), population_source (Phase 1, INERTIA-SURFACE block, status-quo claim field), purpose (preserves domain-specific status-quo argument) — all 3 elements in first step | PASS — Phase 0 PART A EXTENSION-COMMITMENT: field_name, population_source (Phase 2, INERTIA-SURFACE block), purpose — all 3 elements in first step | PASS — Phase 0 EXTENSION-COMMITMENT: field_name, population_source (Phase 2, INERTIA-SURFACE block), purpose — all 3 elements in first step | PASS — Phase 0 EXTENSION-COMMITMENT: field_name (inertia_surface), population_source (Phase 2, INERTIA-SURFACE), purpose (answers diagnostic question) — all 3 elements in first step | PASS — Phase 0 PART A EXTENSION-COMMITMENT: all 3 elements; purpose is explicitly the answer to Phase 0 diagnostic question; population_source names Phase 1 |
| **C-24** Schema field name precision gate | PASS — Phase 5 gate item 2: "Every role file uses exact field identifiers `verify_questions` and `simplify_rules` — not shortened forms (`verify`, `simplify`, `questions`, `rules`) — the identifier strings appear verbatim as YAML keys" | PASS — Phase 0 gate item 3 quotes `verify_questions` and `simplify_rules` as EXACT IDENTIFIER values; Phase 5 gate item 2 references [FC-4]/[FC-5] with same literals | PASS — Phase 5 PREPARE: "Phase 0 field identifiers: `verify_questions` and `simplify_rules` (exact strings; retrieve and confirm spelling before beginning Phase 5 output)"; gate item 2 quotes literals — two mechanisms | PASS — Phase 5 gate item 2: "Every file uses exact identifiers `verify_questions` and `simplify_rules` as YAML keys — not shortened or paraphrased variants; the identifier strings appear verbatim" | PASS — Phase 5 PREPARE names identifiers from [FC-4]/[FC-5]; gate quotes both literals; contract shows violations; triple mechanism |
| **C-25** Per-expert attribute gate | PASS — Phase 2 gate item 3: "Each derived expert entry lists all five attributes individually: name, concern link, domain-vocabulary frame, verify focus, inertia-response question — checked per expert, not as a total count; each attribute must be substantive" (5 attributes per expert) | PASS — Phase 1 gate item 3: "Each derived expert entry lists all four attributes individually: name, concern link, domain-vocabulary frame, verify focus — checked per expert, not as a total count; each attribute must be substantive" | PASS — Phase 1 gate item 3: "Each derived expert entry lists all four attributes checked per expert individually — name, concern link, domain-vocabulary frame, verify focus — each entry is complete; a partial entry...does not satisfy this item" | PASS — Phase 2 gate item 3: "Each derived expert entry lists all four attributes checked per expert individually: name, concern link, domain-vocabulary frame, verify focus — a missing attribute in any single expert entry fails this item" | PASS — Phase 2 gate item 3: "Each derived expert entry lists all four attributes checked per expert individually: name, concern link, domain-vocabulary frame, verify focus — checked per expert, not as a total count; a single missing attribute in any entry fails this item" |

---

### Criterion Summary Table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| **C-15** | PASS | PASS | **PARTIAL** | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | PASS | PASS | PASS | PASS |
| C-24 | PASS | PASS | PASS | PASS | PASS |
| C-25 | PASS | PASS | PASS | PASS | PASS |

---

### Score Computation

**V-01:**
- Essential: 5/5 × 60 = **60.00**
- Recommended: 3/3 × 30 = **30.00**
- Aspirational: 17/17 × 10 = **10.00**
- **Composite: 100.00 — GOLDEN**

**V-02:**
- Essential: 5/5 × 60 = **60.00**
- Recommended: 3/3 × 30 = **30.00**
- Aspirational: 17/17 × 10 = **10.00**
- **Composite: 100.00 — GOLDEN**

**V-03:**
- Essential: 5/5 × 60 = **60.00**
- Recommended: 3/3 × 30 = **30.00**
- Aspirational: 16.5/17 × 10 = **9.71** (C-15 PARTIAL = 0.5)
- **Composite: 99.71 — GOLDEN**

**V-04:**
- Essential: 5/5 × 60 = **60.00**
- Recommended: 3/3 × 30 = **30.00**
- Aspirational: 17/17 × 10 = **10.00**
- **Composite: 100.00 — GOLDEN**

**V-05:**
- Essential: 5/5 × 60 = **60.00**
- Recommended: 3/3 × 30 = **30.00**
- Aspirational: 17/17 × 10 = **10.00**
- **Composite: 100.00 — GOLDEN**

---

### Rankings

| Rank | Variation | Score | Band |
|------|-----------|-------|------|
| 1 (tied) | V-01, V-02, V-04, V-05 | 100.00 | GOLDEN |
| 2 | V-03 | 99.71 | GOLDEN |

**Spread: 0.29 pts** — confirms the R5 thesis: the gap between best and worst is < 2 pts, meaning all structural approaches (role sequence, field contract, lifecycle triad, diagnostic framing) satisfy the five new criteria equally when Phase 0 commitment blocks and explicit failure-mode labels are consistently present.

---

### Excellence Signals from the Top Variations

**What separated V-01/V-02/V-04/V-05 from V-03 (the single differentiator):**

The only criterion separating the four tied 100-point variations from V-03 is **C-15: explicit failure mode labeling for the heading stub**. V-03 has a gate item that prevents heading stubs ("No heading stubs — every section contains substantive content below its header") but lacks the named "FAILURE MODE — HEADING STUB" label with a concrete example. The pattern is: a gate item that prevents a failure is weaker than a named failure mode that explains what the failure looks like. The model needs both — the gate enforces it, the label teaches what to avoid.

**Structural patterns from V-05 (the architecturally richest at 100.00):**

1. **Criterion dependency chain**: C-23 → C-20 → C-22 → C-24 form a causal chain satisfied by construction. Phase 0 EXTENSION-COMMITMENT (C-23) names the extension before context is read (C-20). Phase 6 PREPARE names count enumeration as a pre-write input (C-22). Phase 5 PREPARE retrieves field identifiers from the Phase 0 FIELD CONTRACT (C-24). Each criterion's mechanism becomes the prior condition for the next.

2. **Two-mechanism redundancy per new criterion**: every C-21–C-25 criterion is satisfied by a structural mechanism (FIELD CONTRACT or PREPARE sub-step) AND a gate assertion. If the PREPARE is treated as nominal, the gate catches it. If the gate is skipped, the PREPARE already made it a required input.

3. **PREPARE/WRITE/GATE as pre-write input enforcement**: moving C-22 compliance from "gate checks after the registry is written" to "PREPARE enumerates before the first word is written" shifts the verification burden earlier. The model cannot rationalize a self-reported count if it was required to enumerate Phase 5 output before writing begins.

4. **FIELD CONTRACT as Phase 0 structural anchor**: declaring all schema field identifiers as binding string literals before context is read makes identifier precision a pre-read commitment rather than a post-write check. C-24 becomes a structural consequence of the contract architecture.

5. **Explicit failure-mode naming in every output-producing step**: V-01, V-02, V-04, V-05 all include a named "FAILURE MODE — HEADING STUB" section in Phase 6 with a specific verbatim example. This pattern — name the failure, show what it looks like, state it fails — is consistently more reliable than an implicit gate item.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["criterion dependency chain architecture: C-23 grounded in Phase 0 becomes C-20 precondition; Phase 6 PREPARE enumerates before writing satisfies C-22 as pre-write input not post-write gate; Phase 5 PREPARE retrieves Phase 0 identifiers satisfying C-24 as dependency not assertion", "two-mechanism redundancy per aspirational criterion: FIELD CONTRACT structural declaration plus gate assertion covers each of C-21 through C-25 independently so either mechanism catches failure if the other is bypassed", "explicit FAILURE MODE label with verbatim stub example in registry step — naming HEADING STUB with the exact failing header string is structurally stronger than a gate item that implicitly prevents it"]}
```
