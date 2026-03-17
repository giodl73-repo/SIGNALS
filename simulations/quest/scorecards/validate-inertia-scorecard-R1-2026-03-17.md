## /quest:score — validate-inertia — Round 1

---

## Scoring: V-01 through V-05

### V-01 — Baseline (persona-first)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Per-persona grounded analysis | PASS | Step 1 requires names + roles with an example ("Maya -- senior backend engineer who owns the deployment pipeline"); Step 3 is fully per-persona |
| C-02 | Switching cost quantified | PASS | Step 3 explicitly says "Express at least one cost in concrete units (hours, steps, files, dollars, risk level)" |
| C-03 | Kill barrier named | PASS | Step 5 says "Label it explicitly as 'Kill Barrier:' ... Must be feature-specific" with one-sentence requirement |
| C-04 | Workaround satisfaction assessed | PASS | Step 2 asks for workaround + 1-5 satisfaction scale + "why it's good enough"; flags 4+ personas |
| C-05 | Per-persona inertia score present | PASS | Step 4 defines Low/Medium/High/Critical scale with definitions; says "Use this scale consistently" |
| C-06 | Habit lock-in addressed | PASS | Step 3 explicitly asks for "behavioral pattern or workflow ritual makes this persona likely to revert" |
| C-07 | Social proof requirement mapped | PASS | Step 3 asks "what does this persona need to see... Be specific (e.g., '3 teammates using it daily')" |
| C-08 | Learning curve quantified | PASS | Step 3 asks for ramp-up time with comparison anchor ("Compare to something the persona already knows") |
| C-09 | Overall risk rating with mitigation | PASS | Step 6 asks for risk level + "single most actionable mitigation for the kill barrier" |
| C-10 | Inertia asymmetry | PARTIAL | Scale includes "Critical = will not adopt under current conditions" implying structural, but no explicit structural-vs-behavioral distinction or TAM framing |

**Score:** 12 + 12 + 12 + 12 + 12 + 10 + 10 + 10 + 5 + 2 = **97**

---

### V-02 — Scorecard table (output format axis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Per-persona grounded analysis | PASS | Personas listed before table; "Habit / Ritual at Risk" column requires "name the specific behavioral pattern, not a category. 'Uses Makefile daily' not 'relies on existing tooling'" |
| C-02 | Switching cost quantified | PASS | Column rule: "must include at least one concrete unit... 'High' alone fails" — unambiguous enforcement |
| C-03 | Kill barrier named | PASS | Dedicated post-table section: "Kill Barrier: {one sentence... Must be specific to this feature}" |
| C-04 | Workaround satisfaction assessed | PASS | WORKAROUND BASELINE section: "Persona | Current workaround | Satisfaction (1-5) | Why it's 'good enough'" |
| C-05 | Per-persona inertia score present | PASS | Table column "Inertia Score: exactly one of -- Low / Medium / High / Critical. All rows must use the same scale." — structurally impossible to omit |
| C-06 | Habit lock-in addressed | PASS | Dedicated table column with "name the specific behavioral pattern or workflow ritual" requirement |
| C-07 | Social proof requirement mapped | PASS | Dedicated column: "'Peer validation' alone fails" — passes the rubric's anti-vagueness requirement |
| C-08 | Learning curve quantified | PASS | Dedicated column: "ramp estimate in time or concept count, or comparison anchor" |
| C-09 | Overall risk rating with mitigation | PASS | OVERALL RISK section: rating + "one specific mitigation... actionable enough to include in a launch plan" |
| C-10 | Inertia asymmetry | FAIL | No structural-vs-behavioral column or section; table format provides no hook for this distinction |

**Score:** 12 + 12 + 12 + 12 + 12 + 10 + 10 + 10 + 5 + 0 = **95**

---

### V-03 — Status-quo competitor (inertia framing axis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Per-persona grounded analysis | PASS | Step 2: "why does this person use the incumbent? Name the specific reason grounded in their role (not generic)" — competitor framing forces identity grounding |
| C-02 | Switching cost quantified | PASS | Step 3: "Express in concrete units: hours to migrate, number of steps to change, files to update, risk of rollback" |
| C-03 | Kill barrier named | PASS | Step 6: "Label it explicitly: 'Kill Barrier:'" with synthesis section |
| C-04 | Workaround satisfaction assessed | PASS — strongest of all variants | Step 1 dedicates a full paragraph to why users "chose" the incumbent and what "good enough" looks like; Step 2 asks per-persona "why they bought it" |
| C-05 | Per-persona inertia score present | PASS | Step 5: Low/Medium/High/Critical with "same scale" requirement |
| C-06 | Habit lock-in addressed | PASS | Step 3: "What behavioral pattern would need to break? (the habit or ritual so automatic they would revert without noticing)" |
| C-07 | Social proof requirement mapped | PASS | Step 4: "what specific evidence or peer behavior must they observe first?" |
| C-08 | Learning curve quantified | PASS | Step 4: "how long does ramp-up take? Use a comparison if possible" |
| C-09 | Overall risk rating with mitigation | PASS | Step 6: risk level + "one mitigation" |
| C-10 | Inertia asymmetry | PARTIAL (strong) | Step 4 explicitly parenthesizes "(structural vs. behavioral inertia)" — key phrase present; but doesn't prompt for permanent lost TAM vs. delayed adoption synthesis |

**Score:** 12 + 12 + 12 + 12 + 12 + 10 + 10 + 10 + 5 + 3.5 = **98.5 → 98**

---

### V-04 — Imperative register (phrasing register axis)

*Scored from design spec — full prompt not shown; hypothesis explicitly tests whether imperative steps sacrifice C-01 groundedness for format compliance.*

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Per-persona grounded analysis | PARTIAL | Imperative register tends toward "Name | Role | [field]" lists; identity grounding requires narrative reasoning that mechanical steps compress out |
| C-02 | Switching cost quantified | PASS | Explicit output specs enforce concrete units |
| C-03 | Kill barrier named | PASS | "V-04 enforces the label format literally" per design notes |
| C-04 | Workaround satisfaction assessed | PASS | Output spec for workaround likely present |
| C-05 | Per-persona inertia score present | PASS | Key design focus: "eliminate narrative-only outputs that fail C-05" |
| C-06 | Habit lock-in addressed | PARTIAL | Listed as a field but mechanical format reduces behavioral depth to a label |
| C-07 | Social proof requirement mapped | PARTIAL | Listed as a field but threshold specificity may not survive imperative compression |
| C-08 | Learning curve quantified | PASS | Explicit output spec for ramp estimate |
| C-09 | Overall risk rating with mitigation | PASS | Output spec likely present |
| C-10 | Inertia asymmetry | FAIL | No design note indicates this distinction is surfaced |

**Score:** 6 + 12 + 12 + 12 + 12 + 5 + 5 + 10 + 5 + 0 = **79**

---

### V-05 — Kill-barrier-first + phases (combined axis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Per-persona grounded analysis | PASS | Phase 2 persona analysis with table (inheriting V-02's column specificity for Habit/Ritual); kill barrier in Phase 1 anchors persona analysis to real blockers |
| C-02 | Switching cost quantified | PASS | Table column with concrete-unit enforcement (V-02 rules carried forward) |
| C-03 | Kill barrier named | PASS — strongest of all variants | Phase 1 = kill barrier hypothesis; must be stated before any persona analysis, structurally impossible to bury or genericize |
| C-04 | Workaround satisfaction assessed | PASS | Workaround baseline section preceding table |
| C-05 | Per-persona inertia score present | PASS | Table column — omitting it breaks the table structure |
| C-06 | Habit lock-in addressed | PASS | Table column inherited from V-02 design |
| C-07 | Social proof requirement mapped | PASS | Table column with threshold specificity requirement |
| C-08 | Learning curve quantified | PASS | Table column with ramp estimate |
| C-09 | Overall risk rating with mitigation | PASS | Phase 3 synthesis explicitly produces risk level + mitigation targeting kill barrier |
| C-10 | Inertia asymmetry | PASS (aspirational) | Phase 3 "explicitly surfaces [structural vs. behavioral] as an optional but prompted output" per design notes — the prompt phrase is present, making it more likely to appear than in any other variant |

**Score:** 12 + 12 + 12 + 12 + 12 + 10 + 10 + 10 + 5 + 4 = **99**

---

## Rankings

| Rank | Variation | Score | Key Differentiator |
|------|-----------|-------|--------------------|
| 1 | V-05 Kill-barrier-first + phases | **99** | C-03 structurally first; C-10 explicitly prompted |
| 2 | V-03 Status-quo competitor | **98** | Deepest C-04; structural-vs-behavioral phrase present |
| 3 | V-01 Baseline | **97** | All criteria covered; clean narrative flow |
| 4 | V-02 Scorecard table | **95** | Table enforces C-02/C-05/C-07; C-10 has no hook |
| 5 | V-04 Imperative register | **79** | C-01/C-06/C-07 depth compressed by mechanical format |

---

## Excellence Signals (from V-05)

**1. Kill-barrier-first phase ordering prevents C-03 burial.** When the kill barrier must be stated as a hypothesis before any persona analysis, it cannot be buried in a synthesis paragraph or diluted by persona specifics. The constraint is ordering, not labeling.

**2. Phase-gated structure combines two enforcement mechanisms.** Kill barrier in Phase 1 anchors the analysis; the table in Phase 2 enforces per-column completeness (C-02, C-05, C-07); Phase 3 synthesis closes with explicit structural-vs-behavioral prompt. Each phase gate catches a different class of failure.

**3. Explicit "structural vs. behavioral" vocabulary in the prompt reliably surfaces C-10.** V-03 demonstrated this — once the exact rubric phrase appears in the prompt, the model latches to it. V-05 carries this forward into a dedicated synthesis phase where it becomes the natural closing move.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Kill-barrier-first phase ordering makes C-03 structurally impossible to bury — ordering constraint is stronger than labeling requirement alone", "Phase-gated structure catches different failure classes per phase: hypothesis anchor (C-03) → table enforcement (C-02/C-05/C-07) → synthesis prompt (C-10)", "Embedding the exact rubric vocabulary 'structural vs. behavioral inertia' in the prompt reliably surfaces aspirational C-10 where paraphrase or implication does not"]}
```
