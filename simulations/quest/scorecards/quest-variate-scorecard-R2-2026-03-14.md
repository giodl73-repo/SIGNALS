## quest-variate R2 — Scoring

Evaluating the 5 variations in `quest-variate-variations-R2-2026-03-14.md` against the v2 rubric.

---

### Essential Criteria (60 pts)

**C-01 — Complete runnable bodies**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Full role, Input block, Variation axes table, 4-step process, Constraints. Standalone. |
| V-02 | PASS | Full role, Input block, 4-step per-variation loop, Constraints. Standalone. |
| V-03 | PASS | Full VariationScientist role, Input block, Experimental design framing, 3-step Protocol, Constraints. Standalone. |
| V-04 | PASS | Full role, Phase 1 with planning table, Phase 2 with generation loop, Phase 3 with artifact emission, Global constraints. Standalone. |
| V-05 | PASS | Full role, Input block, 4-step process with inline checklist, Constraints. Standalone. |

**C-01: PASS → 15/15**

---

**C-02 — Inline axis and hypothesis labels**

All 5 variations have `## V-NN — Axis:`, `**Axis:**`, and `**Hypothesis:**` fields, all non-empty.

**C-02: PASS → 15/15**

---

**C-03 — Single-axis isolation**

| Variation | Axis Changed | Other Axes | Result |
|-----------|-------------|------------|--------|
| V-01 | Role sequence (generate → label → critique → output) | All others at neutral baseline | PASS |
| V-02 | Scoring granularity (per-variation binary self-check) | Role, format, lifecycle, persona all at baseline | PASS |
| V-03 | Stock role selection (VariationScientist named persona) | Other axes at baseline | PASS |
| V-04 | Lifecycle emphasis (3-phase hard stops) | Role, format, persona, scoring at baseline | PASS |
| V-05 | Output format (inline checklist per variation) | Role, lifecycle, persona, scoring at baseline | PASS |

**C-03: PASS → 15/15**

---

**C-04 — N variations produced**

Exactly 5 variations, V-01 through V-05. Default N=5.

**C-04: PASS → 15/15**

**Essential total: 60/60. All 4 essential criteria pass.**

---

### Recommended Criteria (30 pts)

**C-05 — Testable hypotheses**

| Variation | Hypothesis | Result |
|-----------|-----------|--------|
| V-01 | "prevents diff-leak failures because the model commits to a full body before evaluation can interrupt the generation path" — names a specific failure mode and a causal mechanism | PASS |
| V-02 | "confirms completeness before token context drifts to the next variation — reducing the rate of truncated or partially-referenced bodies" — specific observable rate prediction | PASS |
| V-03 | "named roles carry behavioral priors toward systematic, hypothesis-driven work — resulting in more precise axis selection and more falsifiable hypotheses" — observable output quality prediction | PASS |
| V-04 | "structural gates are more reliable than instruction-based warnings" — the structural vs advisory distinction is directly testable by running both and comparing axis drift rate | PASS |
| V-05 | "reduces truncation and axis drift compared to an end-of-run critique pass" — specific comparison prediction with observable outcome | PASS |

**C-05: PASS → 10/10**

---

**C-06 — Non-trivial variation**

All 5 represent genuine design choices a practitioner would consciously select:
- V-01: Commit body before critique vs interleave critique during generation — a real ordering question.
- V-02: End-of-run review vs per-artifact checkpoint — a real quality gate tradeoff.
- V-03: Generic role framing vs named domain expert — a real prompting strategy choice.
- V-04: Advisory instructions vs structural phase gates — a real constraint enforcement choice.
- V-05: Deferred review vs inline checklist — a real completeness verification timing choice.

No surface phrasing changes present.

**C-06: PASS → 10/10**

---

**C-07 — Axis coverage breadth**

5 of 6 axes covered: role sequence (V-01), scoring granularity (V-02), stock role selection (V-03), lifecycle emphasis (V-04), output format (V-05). Phrasing register absent (was V-03 in R1; traded for scoring granularity and stock role axes not covered in R1). Meets the 4-of-6 floor.

**C-07: PASS → 10/10**

**Recommended total: 30/30. All 3 recommended criteria pass.**

---

### Aspirational Criteria (10 pts)

**C-08 — Combination pass handling**

N=5. No combinations produced. No combinations needed.

**C-08: PASS**

---

**C-09 — Baseline variation**

V-01 is explicitly labeled "Role Sequence (baseline)" in the header. The improvements summary states "V-01 explicitly anchors as the baseline." Subsequent variations can be compared against it.

**C-09: PASS**

---

**C-10 — Stop conditions encode constraint structurally**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | Critique step is post-hoc (step 3, after all bodies). No stop condition per variation. |
| V-02 | PARTIAL | "Do not proceed with a failed check outstanding" is instructional, not a labeled STOP CONDITION gate. |
| V-03 | PARTIAL | Protocol 2c says "rewrite before proceeding" but no STOP CONDITION label or structural gate marker. |
| V-04 | PASS | Explicit `**STOP CONDITION:**` blocks after Phase 1 and Phase 2. "STOP AND REWRITE THIS VARIATION" in Phase 2 loop. Constraint is structurally enforced. |
| V-05 | PASS | Inline checklist with `YES / NO` fields and "Do not emit until all three answers are YES" — constraint is structural (emission blocked until checklist completes). |

Artifact demonstrates the pattern strongly in V-04 and V-05. V-01's absence is intentional (testing the opposite approach on the role sequence axis).

**C-10: PASS (2 of 5 implement fully; 2 partial; pattern is represented)**

---

**C-11 — Hypothesis committed before generation begins**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | FAIL | Steps 1 (Generate) → 2 (Label). Hypotheses added after bodies are written — deliberate inversion to test the axis. |
| V-02 | PASS | Per-variation Step 1 (Assign axis and hypothesis) → Step 2 (Write body). |
| V-03 | PASS | Protocol Step 1 produces full planning table with all hypotheses before Protocol Step 2 generates any body. Global up-front phase. |
| V-04 | PASS | Phase 1 (Hypothesis Commitment) gated by STOP CONDITION before Phase 2 (Generation). |
| V-05 | PASS | Per-variation Step 1 (Select axis and hypothesis) → Step 2 (Write body). |

V-01's failure is the correct behavior for testing role sequence — the hypothesis is that generate-before-label works; if V-01 also required label-before-generate it would fail its own axis test. 4/5 demonstrate C-11.

**C-11: PASS**

---

**C-12 — Explicit rewrite trigger**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PARTIAL | Critique arrows ("→ rewrite") are present but informal; no named trigger condition. |
| V-02 | PASS | "If any check fails: rewrite the body before continuing. Do not proceed with a failed check outstanding." Named trigger with named action. |
| V-03 | PARTIAL | "If confirmation fails: rewrite before proceeding" — close but no trigger label; reads instructional. |
| V-04 | PASS | "STOP AND REWRITE THIS VARIATION before continuing to the next. **This is a hard stop, not a warning.**" Named trigger with explicit disavowal of advisory framing. |
| V-05 | PASS | "If any answer is NO, rewrite the body and re-check. Do not emit until all three answers are YES." Named trigger and named blocking condition. |

**C-12: PASS (3 full pass; 2 partial)**

---

**Aspirational total: 5/5 pass → 10/10**

---

### Composite Score

```
Composite = (4/4 * 60) + (3/3 * 30) + (5/5 * 10)
          = 60 + 30 + 10
          = 100
```

**All essential pass. Composite: 100. Classification: Golden.**

---

### Per-Variation Rankings

| Rank | Variation | Notable Strengths | Weakness |
|------|-----------|------------------|----------|
| 1 | **V-04** | C-10/C-11/C-12 all pass; explicit STOP CONDITION blocks; "hard stop, not a warning" language; 3-phase architecture is the clearest structural model | None significant |
| 2 | **V-05** | Inline checklist creates structural completeness gate at emission time; clean 4-step per-variation loop; all aspirational pass | C-11 is per-variation, not global phase — weaker than V-04's global Phase 1 commitment |
| 3 | **V-02** | First to introduce per-variation self-check; C-11/C-12 pass; hypothesis is crisply falsifiable (token drift mechanism) | C-10 PARTIAL — "do not proceed" is advisory phrasing, not a STOP CONDITION gate |
| 4 | **V-03** | VariationScientist framing introduces scientific vocabulary (independent/dependent/control); global planning table before generation | C-10/C-12 PARTIAL — no structural gate labels; rewrite trigger is instructional |
| 5 | **V-01** | Correct baseline; strongest on C-09; hypothesis is well-formed | Intentionally fails C-10, C-11 (tests role sequence axis by doing generate-before-label) — correct for its axis but lowest aspirational profile |

---

### Excellence Signals

**From V-04 (top-scoring):**

1. **Meta-commentary disavowing advisory framing**: "This is a hard stop, not a warning" is a new pattern not captured in any rubric criterion. Naming the contrast explicitly (structural vs advisory) appears to create a stronger enforcement signal than the structural constraint alone. Candidate rubric addition.

2. **3-phase named lifecycle** (Commitment → Generation → Emission) as a reusable skill body architecture for skills that produce N artifacts. The named phases surface a repeatable pattern that applies beyond `quest-variate` to any skill with a plan-before-generate requirement.

---

### Output

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["meta-commentary explicitly disavowing advisory framing ('this is a hard stop, not a warning') strengthens structural constraints beyond the structure itself", "3-phase named lifecycle (Commitment → Generation → Emission) as a reusable architecture for N-artifact skills with plan-before-generate requirements"]}
```
