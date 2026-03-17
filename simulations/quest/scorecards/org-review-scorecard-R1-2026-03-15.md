## org-review Variations — Score Report (Round 1)

**Rubric**: `simulations/quest/rubrics/org-review-rubric-2026-03-15.md`
**Variations file**: `simulations/quest/golden/org-review-variate-R1-2026-03-15.md`

---

### Scoring Key

| Weight | Points | PASS | PARTIAL | FAIL |
|--------|--------|------|---------|------|
| Essential (×5) | 10 pts each | 10 | 5 | 0 |
| Recommended (×3) | 10 pts each | 10 | 5 | 0 |
| Aspirational (×2) | 10 pts each | 10 | 5 | 0 |
| **Total** | **100** | | | |

---

## V-01 — Role Sequence: Inertia-First

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01 Role Selection | **PASS** | "Read `.craft/roles/signal/`... Do not invent roles" — explicit registry constraint |
| C-02 Review Matrix Structure | **PASS** | Inertia gate lists all four fields explicitly; Step 3 repeats "all four fields: Role, Findings, Severity, Recommendation" |
| C-03 Perspective Fidelity | **PASS** | "Do NOT echo the inertia-advocate's framing." PM vs. architect frames named explicitly. Inertia-first sequence forces subsequent roles to depart from the null baseline structurally |
| C-04 Severity Classification | **PASS** | "Not all findings may share the same level — if they do, re-examine." Self-correcting guard present |
| C-05 Depth Flag Behavior | **PASS** | Standard = most relevant roles; deep = every role in registry with stated count |
| C-06 Verify Questions | **PASS** | Step 2 requires verify question for inertia gate; Step 3 item 4 requires one per remaining reviewer |
| C-07 Simplify Lens | **PASS** | Step 3 item 5: "Apply the simplify lens: what could be removed, collapsed, or clarified" |
| C-08 Cross-Role Summary | **PASS** | Step 4 — agreement, divergence, explicit conflicts, at-risk areas, overall signal (ready/conditional/blocked) |
| C-09 Conflict Detection | **PASS** | "Where do they diverge or contradict each other? Name the conflict explicitly if one exists." |
| C-10 All 5 Org Areas (deep) | **PARTIAL** | Deep runs all registry roles, but "5 org areas" not explicitly enumerated |

**Score: 95 / 100** — All essential: **PASS**

---

## V-02 — Output Format: Strict Markdown Table

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01 Role Selection | **PASS** | "All roles must come from `.craft/roles/signal/`. Do not invent roles." |
| C-02 Review Matrix Structure | **PASS** | Table enforces columns structurally: Role, Findings, Severity, Recommendation, Verify Question. "No empty cells." Missing field is visually obvious |
| C-03 Perspective Fidelity | **PASS** | "Findings must not echo each other across rows." Frame distinctions (PM / architect / inertia-advocate) spelled out within table description |
| C-04 Severity Classification | **PASS** | "Not every row may share the same level... If all rows show the same severity, re-examine." Table makes severity variance scannable at a glance |
| C-05 Depth Flag Behavior | **PASS** | Both modes described in Step 1; deep includes all roles with stated count before table |
| C-06 Verify Questions | **PASS** | Verify Question is a mandatory column in the review matrix table |
| C-07 Simplify Lens | **PASS** | Step 3 produces a second table: Role + Simplify Observation |
| C-08 Cross-Role Summary | **PASS** | Step 4 — 5–8 sentence summary with highest severity, cross-role conflicts, disposition |
| C-09 Conflict Detection | **PASS** | Step 4 names "cross-role conflict (two reviewers recommending incompatible actions)" |
| C-10 All 5 Org Areas (deep) | **PARTIAL** | Registry-enumerated but "5 org areas" not explicitly named |

**Score: 95 / 100** — All essential: **PASS**

---

## V-03 — Inertia Framing: Null Hypothesis as Universal Gate

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01 Role Selection | **PASS** | "All roles must come from `.craft/roles/signal/`." |
| C-02 Review Matrix Structure | **PASS** | Part C contains Severity + Recommendation + Verify Question. Role is the section header. Findings in Part B. All four fields present |
| C-03 Perspective Fidelity | **PASS** | Strongest C-03 in the set — Part A requires each role to answer the null hypothesis question from its own frame: PM (decision sufficiency), architect (technical justification), inertia-advocate (status quo). "Each role's Part A answer must be substantively different from the others." |
| C-04 Severity Classification | **PASS** | "Calibrate independently — do not copy another role's severity." HIGH/MEDIUM/LOW defined |
| C-05 Depth Flag Behavior | **PASS** | Standard = 2–3 most relevant; deep = all roles with stated count |
| C-06 Verify Questions | **PASS** | Part C: "Verify Question: One question from this role's `lens.verify` list." |
| C-07 Simplify Lens | **PARTIAL** | Part B draws on `lens.verify` and `expertise.depth`, but `lens.simplify` is not explicitly invoked as its own output section |
| C-08 Cross-Role Summary | **PARTIAL** | Step 3 "Null Hypothesis Verdict" covers threat level, evidence, gaps, disposition — but scoped only to null hypothesis; no full agreement/divergence map |
| C-09 Conflict Detection | **PARTIAL** | Verdict lists evidence and gaps but does not explicitly name cross-role conflicts between reviewer recommendations |
| C-10 All 5 Org Areas (deep) | **PARTIAL** | No explicit org-area enumeration |

**Score: 80 / 100** — All essential: **PASS**

---

## V-04 — Formal Register + Explicit Lifecycle Phases

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01 Role Selection | **PASS** | "No role may be invented. Every reviewer must have a corresponding file in `.craft/roles/signal/`." Phase 1 Step 1: enumerate all files first |
| C-02 Review Matrix Structure | **PASS** | Phase 2 template: `Findings / Severity / Recommendation / Verify Question / Simplify` — structured block with all four required fields |
| C-03 Perspective Fidelity | **PASS** | Phase 2 step 2c names archetypes (product / technical / challenger) with distinct interpretive filters. Step 2d: "Cross-role finding homogeneity is a defect." |
| C-04 Severity Classification | **PASS** | Step 2e: semantic definitions (HIGH = blocks commitment, MEDIUM = conditions commitment, LOW = advisory). Severity is a function of impact, not a uniform label |
| C-05 Depth Flag Behavior | **PASS** | Phase 1 Step 2/3 — standard uses relevance filter (min 2 roles), deep enumerates all. `{{depth}}` parameter is an explicit input |
| C-06 Verify Questions | **PASS** | Phase 2 step 2g: "Formulate a verify question: one question from `lens.verify`" |
| C-07 Simplify Lens | **PASS** | Phase 2 step 2h: "Apply the simplify lens: name one element the artifact should remove or collapse, drawn from `lens.simplify`." |
| C-08 Cross-Role Summary | **PASS** | Phase 3 synthesis: conflict map, agreement areas, READY/CONDITIONAL/BLOCKED disposition codes |
| C-09 Conflict Detection | **PASS** | Phase 3 step 3b: "two reviewers whose recommendations are incompatible — name the roles in tension and state the decision required to resolve it." |
| C-10 All 5 Org Areas (deep) | **PARTIAL** | All registry roles included on deep runs; 5 org areas not explicitly enumerated |

**Score: 95 / 100** — All essential: **PASS**

---

## V-05 — Parallel Independent Reviews + Structured Prose

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| C-01 Role Selection | **PASS** | "Read `.craft/roles/signal/` to enumerate available reviewers." Registry-sourced. |
| C-02 Review Matrix Structure | **PASS** | Each section template has Role (header), Findings (prose), Severity, Recommendation, Verify Question. All four present |
| C-03 Perspective Fidelity | **PASS** | "Opening frames must be substantively different from each other — they cannot all start from the same concern." Isolation framing ("not seen each other's work") is the strongest structural C-03 guarantee |
| C-04 Severity Classification | **PARTIAL** | Vocabulary consistent (HIGH/MEDIUM/LOW with justification), but no explicit guard against uniformity ("if all show same level, re-examine" absent) |
| C-05 Depth Flag Behavior | **PASS** | Standard = relevance-filtered panel; deep = all roles with stated count |
| C-06 Verify Questions | **PASS** | "Verify Question: One question this reviewer would ask, drawn from their `lens.verify` list." |
| C-07 Simplify Lens | **PASS** | "If I could simplify one thing: One observation from this role's `lens.simplify` principles." |
| C-08 Cross-Role Summary | **PASS** | "Cross-Role Debrief" — alignment, divergence, explicit conflicts, uncovered artifact areas, overall disposition |
| C-09 Conflict Detection | **PASS** | "Explicit conflict (if any): name the roles, name the tension, name the decision." |
| C-10 All 5 Org Areas (deep) | **PARTIAL** | All roles included; 5 org areas not named |

**Score: 90 / 100** — All essential: **PARTIAL** (C-04 partial — missing non-uniformity guard)

---

## Rankings

| Rank | Variation | Score | All Essential Pass | Key Strength |
|------|-----------|-------|--------------------|--------------|
| **1 (tie)** | V-01 | **95** | Yes | Inertia-first sequencing as structural C-03 guarantee |
| **1 (tie)** | V-02 | **95** | Yes | Table structure makes C-02/C-04 impossible to fail silently |
| **1 (tie)** | V-04 | **95** | Yes | Formal phase contracts + defect framing + archetype vocabulary |
| **4** | V-05 | **90** | No (C-04 partial) | Parallel isolation is strongest C-03 guarantee; loses C-04 guard |
| **5** | V-03 | **80** | Yes | Best null-hypothesis framing; weakest on simplify and synthesis |

---

## Excellence Signals (from top-scoring variations)

**V-01 — Inertia-first sequencing**: Running the challenger role before any positive-framing role sets a null hypothesis baseline in the output before the PM or architect speaks. Subsequent reviewers must actively depart from it. This is a sequence-level structural guarantee for C-03, not just a framing instruction.

**V-02 / V-04 — Self-correcting severity guard**: "If all rows show the same severity, re-examine" is a small instruction with large effect. It turns C-04 from a pass/fail check into an active self-correction loop embedded in the prompt itself.

**V-04 — Phase-bound depth flag**: Declaring the depth parameter as `Phase 1 input` with explicit procedures for each value (standard → relevance filter, deep → enumerate all) makes C-05 observable as a state transition rather than an implicit reviewer count difference. The `{{depth}}` placeholder formalizes this further.

**V-04 — Defect language**: "Cross-role finding homogeneity is a defect" is more enforceable than "do not echo." Framing the failure mode as a named defect (rather than a preference) signals to the model that homogeneity is incorrect output, not just suboptimal output.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["inertia-first sequencing — running the challenger role before product/technical roles provides a structural C-03 guarantee by setting a null hypothesis baseline that subsequent roles must actively depart from", "self-correcting severity guard — embedding an explicit re-examine instruction when all reviewers share the same severity level turns C-04 from an external check into an active quality loop inside the prompt", "phase-bound depth flag — declaring depth as a named phase input with per-value procedures makes C-05 observable as a state transition rather than an implicit reviewer count difference"]}
```
