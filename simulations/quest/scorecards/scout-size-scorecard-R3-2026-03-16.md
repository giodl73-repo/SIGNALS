## Quest Score — scout-size R3

### V-01 — Lifecycle Emphasis (Two-Phase Sensitivity)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | **PASS** | STEP 2 template lists each point individually + "Total: N integration points" required; "general description without named points fails" stated explicitly |
| C-02 | Complexity tier on-scale | **PASS** | STEP 3: "Assign exactly one tier: LOW / MEDIUM / HIGH / XL. 'MODERATE', '3/5', 'complex', 'non-trivial' all fail." |
| C-03 | Inertia check present | **PASS** | STEP 1: workaround named, cost direction (cheaper/comparable/more expensive required), basis sentence — "'It depends' and 'unclear' are not accepted" |
| C-04 | Confidence level with basis | **PASS** | STEP 6 HALF 1: `Confidence: [H/M/L]` + `Basis: [specific evidence]` required; two-half structure separates them structurally |
| C-05 | Signal boundary respected | **PASS** | STEP 7 explicit: remove "task breakdowns, sprint assignments, owner names, or milestone dates" before writing |
| C-06 | Specialist types named | **PASS** | STEP 5: `[specialist types + FTE fractions]`, "'3 engineers' fails (no specialist types)" |
| C-07 | Sprint range | **PASS** | STEP 5: sprint range example, "'Q3 2026' fails (calendar date). '4 sprints' fails (not a range)" |
| C-08 | Primary driver identified | **PASS** | STEP 3: `Primary driver: [the one or two factors most responsible — not a list]` |
| C-09 | Tier sensitivity up + down | **PASS** | STEP 4: both TIER UP and TIER DOWN have Phase 1 templates with [LEVEL] fill |
| C-10 | What would change confidence | **PASS** | STEP 6 HALF 2: `What would raise it: [specific investigation result]` |
| C-11 | Confidence gap named | **PASS** | STEP 6 HALF 2: `Gap: [specific thing NOT yet verified — different from Basis]`; explicit: "These are different questions" |
| C-12 | Single named conditions | **PASS** | Template: `Tier rises to [LEVEL] if [single named condition]`; singularity enforced by phrasing |
| C-13 | Explicit tier destination | **PASS** | `[LEVEL] must be one of: LOW / MEDIUM / HIGH / XL — fill it in. Writing "tier would rise" without a destination fails.` Explicit failure statement present. |
| C-14 | Falsifiable conditions | **PASS** | Phase 2 mandatory: "Settle by: [specific action]"; 4 failing forms + 4 passing forms shown |

**Composite: 60 + 30 + 10 = 100** | Essential: all pass | Golden: YES

---

### V-02 — Output Format (Tier-Transition Table)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | **PASS** | Section 2: bullet list format + "Surface area total: N integration points" |
| C-02 | Complexity tier on-scale | **PASS** | Section 3: "Tier: [exactly one of: LOW / MEDIUM / HIGH / XL]" |
| C-03 | Inertia check present | **PASS** | Section 1: workaround named, cost direction required, reasoning field |
| C-04 | Confidence level with basis | **PASS** | Section 6: `Confidence: [H/M/L]`, `Basis: [what is known]` |
| C-05 | Signal boundary respected | **PASS** | SIGNAL BOUNDARY section + note it "does not replace" program-plan |
| C-06 | Specialist types named | **PASS** | Section 5: passing/failing examples include "3 engineers fails" |
| C-07 | Sprint range | **PASS** | Section 5: passing/failing examples including "Q3 2026" and point estimate as failures |
| C-08 | Primary driver identified | **PASS** | Section 3: `Primary driver: [the one or two factors most responsible]` |
| C-09 | Tier sensitivity up + down | **PASS** | Section 4: UP and DOWN rows in table |
| C-10 | What would change confidence | **PASS** | Section 6: `What would raise it: [specific investigation or result]` |
| C-11 | Confidence gap named | **PARTIAL** | `Gap: [specific thing NOT yet verified — what limits confidence]` is present, but prompt does not explicitly say "Basis and Gap must not restate each other" — no guard against blending; weaker than V-01/V-04/V-05 on this point |
| C-12 | Single named conditions | **PASS** | Named Condition column rule: "one specific scenario. Failing forms: 'several factors', 'if requirements expand'…" |
| C-13 | Explicit tier destination | **PASS** | Dedicated **Destination Tier** column — cell requires LOW/MEDIUM/HIGH/XL; "they must differ" stated |
| C-14 | Falsifiable conditions | **PASS** | **Verify by** column: "names a concrete, actionable investigation"; failing/passing examples in column rules |

**Composite: 60 + 30 + (5.5/6 × 10) = 99.2 → 99** | Essential: all pass | Golden: YES

---

### V-03 — Phrasing Register (Socratic / Workaround-as-Protagonist)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | **PASS** | "HOW MUCH DOES IT TOUCH?" section: individual list + "Total: N integration points" |
| C-02 | Complexity tier on-scale | **PASS** | "Assign one tier: LOW / MEDIUM / HIGH / XL. 'significant', 'non-trivial', 'moderate' all fail." |
| C-03 | Inertia check present | **PASS** | "THE STATUS QUO: THE FEATURE'S PRIMARY COMPETITOR" — workaround, maintenance cost, verdict (cheaper/comparable/more expensive); "'It depends' is not an answer" |
| C-04 | Confidence level with basis | **PASS** | "HOW CONFIDENT ARE YOU?" Question 1: `Confidence: [H/M/L]`, `Basis: [what IS known]` |
| C-05 | Signal boundary respected | **PASS** | Opening declaration + closing SIGNAL BOUNDARY scan |
| C-06 | Specialist types named | **PASS** | "WHO AND HOW LONG?" — `[specialist types + FTE fractions]` with passing example |
| C-07 | Sprint range | **PASS** | "WHO AND HOW LONG?" — sprint range required; "not a calendar date, not a single number" |
| C-08 | Primary driver identified | **PASS** | `Primary driver: [the one or two factors]` |
| C-09 | Tier sensitivity up + down | **PASS** | Question 1 (tier up) and Question 2 (tier down) — both mandatory |
| C-10 | What would change confidence | **PASS** | "What would raise confidence: [the specific investigation that would resolve the gap]" |
| C-11 | Confidence gap named | **PASS** | Question 2: `Gap: [one specific thing NOT yet known]`; "Do not answer Question 2 by restating Question 1" |
| C-12 | Single named conditions | **PASS** | "What **single** condition" — singularity embedded in question phrasing; template uses "one condition" |
| C-13 | Explicit tier destination | **PASS** | `[LEVEL] must be one of: LOW / MEDIUM / HIGH / XL. "Tier would rise" without naming the destination fails.` Embedded in question form. |
| C-14 | Falsifiable conditions | **PASS** | "Colleague test: could a teammate actually investigate this? What would they do?" + `A colleague could settle this by:` required field + "If you cannot answer the colleague test, your condition is a hedge. Replace it." + failing/passing examples |

**Composite: 60 + 30 + 10 = 100** | Essential: all pass | Golden: YES

---

### V-04 — Combined (Table + Two-Phase)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | **PASS** | TABLE 1: numbered rows + "Total row is required. N must be a specific number." |
| C-02 | Complexity tier on-scale | **PASS** | TABLE 2 Complexity tier cell: "Exactly this vocabulary — no other values" |
| C-03 | Inertia check present | **PASS** | INERTIA table: workaround, maintenance cost, cost direction; "choose exactly one of those three words" |
| C-04 | Confidence level with basis | **PASS** | TABLE 3: `Confidence level: [H/M/L]`, `Basis: [what IS known]` |
| C-05 | Signal boundary respected | **PASS** | Signal boundary + SELF-CHECK item: "No task breakdowns or sprint assignments in output" |
| C-06 | Specialist types named | **PASS** | TABLE 2 Team signal: "1 backend engineer, 0.5 PM" — "'3 engineers' fails" |
| C-07 | Sprint range | **PASS** | TABLE 2 Timeline signal: "no calendar dates, no point estimate" |
| C-08 | Primary driver identified | **PASS** | TABLE 2 Primary driver: "The main thing — not a generic list" |
| C-09 | Tier sensitivity up + down | **PASS** | Table rows UP and DOWN; both mandatory |
| C-10 | What would change confidence | **PASS** | TABLE 3 "What would raise it" row: "specific investigation result" |
| C-11 | Confidence gap named | **PASS** | TABLE 3 Gap row: "different question from Basis"; "Do not answer both with the same information" explicit |
| C-12 | Single named conditions | **PASS** | Named Condition column: "one specific scenario. 'Several factors' fails. 'If requirements expand' fails." |
| C-13 | Explicit tier destination | **PASS** | **Dual**: Destination Tier column (table) + "Destination Tier must be explicitly named — 'tier would rise' with no level stated fails C-13" + SELF-CHECK item |
| C-14 | Falsifiable conditions | **PASS** | **Dual**: Phase 2 "Settle by" sub-field required per row + failing/passing examples + SELF-CHECK item; "If you cannot name a settling action, that condition is a hedge. Replace it." |

**Composite: 60 + 30 + 10 = 100** | Essential: all pass | Golden: YES

---

### V-05 — Full Integration (All Axes + Anti-Pattern Tables + 14-Criterion Self-Check)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Surface area enumerated | **PASS** | TABLE: Total row required; "'Several integration points' is not an enumeration" |
| C-02 | Complexity tier on-scale | **PASS** | STEP 2: "No other tier values. 'MODERATE', '3/5', 'complex', 'non-trivial', 'significant' all fail." |
| C-03 | Inertia check present | **PASS** | MANDATORY OPENING: workaround, maintenance cost, cost direction; "'It depends' is not a verdict." |
| C-04 | Confidence level with basis | **PASS** | STEP 5 HALF 1: Confidence + Basis; explicitly separate from Gap |
| C-05 | Signal boundary respected | **PASS** | Opening declaration + SIGNAL BOUNDARY CHECK with 4 labeled items |
| C-06 | Specialist types named | **PASS** | STEP 4: specialist types + FTE fractions; passing/failing examples |
| C-07 | Sprint range | **PASS** | STEP 4: sprint range; passing/failing examples with point estimate and calendar date as failures |
| C-08 | Primary driver identified | **PASS** | STEP 2: `Primary driver: [one or two factors most responsible — not a generic list]` |
| C-09 | Tier sensitivity up + down | **PASS** | STEP 3: TIER UP and TIER DOWN both required |
| C-10 | What would change confidence | **PASS** | STEP 5 HALF 2: "What would raise it" + SELF-CHECK item C-10 |
| C-11 | Confidence gap named | **PASS** | Explicit failing form shown ("surface area is clear but auth layer unverified" — one sentence, fails C-11) vs passing form with distinct halves; SELF-CHECK item C-11 |
| C-12 | Single named conditions | **PASS** | Template `Tier rises to [LEVEL] if [single named condition]`; SELF-CHECK item C-12 |
| C-13 | Explicit tier destination | **PASS** | C-13 anti-pattern table (4 failing forms); "A direction without a destination fails C-13"; SELF-CHECK item C-13 — most explicit enforcement of any variation |
| C-14 | Falsifiable conditions | **PASS** | C-14 anti-pattern table (4 failing forms + replacements); "Settle by" mandatory slot; passing forms for "Settle by"; SELF-CHECK item C-14 — most complete C-14 enforcement |

**Composite: 60 + 30 + 10 = 100** | Essential: all pass | Golden: YES

---

## Ranking

| Rank | ID | Score | Key Differentiator |
|------|----|-------|--------------------|
| 1 | V-05 | 100 | C-13/C-14 anti-pattern tables with replacements + full 14-criterion self-check + explicit C-11 failing/passing forms; maximum self-correction surface |
| 2 | V-04 | 100 | Dual structural handles (table column + Phase 2 sub-field) for both C-13 and C-14; SELF-CHECK against C-13/C-14 explicitly named |
| 3 | V-01 | 100 | Two-phase split is structurally clean; 4 failing + 4 passing Phase 2 examples; Phase 1/Phase 2 separation prevents co-satisfaction |
| 4 | V-03 | 100 | Colleague test is a strong reasoning mechanism; all criteria enforced; slightly more model-dependent than structural approaches |
| 5 | V-02 | 99 | Structural table columns are excellent; C-11 weaker (no explicit "Basis and Gap must not restate each other" guard) |

---

## Excellence Signals from V-05

**1. Anti-pattern table with replacements closes the rule-to-application gap.**
V-05 shows four failing forms of C-14 alongside what to replace each with (`"if requirements expand"` → `"if offline sync is required"`). Rules tell a model what not to do; replacement pairs show exactly what to do instead. This is more actionable than stating the falsifiability rule alone.

**2. The 14-criterion self-check makes compliance a mandatory pre-write step.**
Extending the self-check from ~9 items (R2) to all 14 named criteria — with C-13 and C-14 as labeled items — converts the rubric into a checklist the model runs against its own draft. A model that satisfies C-13 in the template can still fail if the self-check is present; but without the self-check, there is no second verification pass.

**3. Explicit C-11 failing form ("one sentence blending") next to passing form (distinct halves).**
V-05 shows a concrete output that looks correct but fails C-11 (`"Confidence: MEDIUM — surface area is clear but auth layer is unverified"`) and the distinct-halves form that passes. This closes a common failure mode where basis and gap are answered in a single breath — the model learns to recognize the shape of the failure, not just the rule.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Anti-pattern tables with replacements: showing four failing forms of C-13 and C-14 alongside what to replace each with is more actionable than stating the rule alone — models self-checking against 'tier would rise' can identify and fix the failure before output", "Mandatory Settle-by sub-field universally applied: making falsifiability a required output slot in every variation (not just some) creates a generation-time legibility test — if you cannot fill 'Settle by' with a concrete action, the condition is visibly incomplete before the artifact is written", "Explicit C-11 failing form adjacent to passing form: showing a one-sentence blend that looks correct but fails C-11 alongside the distinct-halves form that passes teaches the model the shape of the failure, not just the rule about distinct questions"]}
```
