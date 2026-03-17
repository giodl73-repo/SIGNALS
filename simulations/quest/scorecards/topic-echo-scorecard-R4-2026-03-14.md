## `/quest:score` — topic-echo · Round 4

---

## Rubric Evaluation Summary

R4 tests two specific questions: (1) whether C-13 can be achieved via two structurally distinct enforcement mechanisms (V-01 vs V-03), and (2) whether C-14 can be achieved via an explicit portability test independent of four-mechanism convergence (V-02). V-04 and V-05 both reach 100/100, confirming that the R3-V-05 baseline plus Rule 4 composes without friction and earns C-13 and C-14. The spread is 93.5–100.

---

### V-01 — Single axis: Per-field completion enforcement (C-13)

| ID | Result | Key evidence |
|----|--------|-------------|
| C-01 | PASS | Culling filters present: drop expected, drop untraceable, drop standard-summary items; keep 3–6 |
| C-02 | PASS | Step 3: "content-specific, memorable, not generic"; "Finding 2 fails" |
| C-03 | PASS | Source field labeled `[required — not N/A]`; quality check: "Every source is named (namespace + skill)" |
| C-04 | PASS | Design impact field labeled `[required — not N/A]`; quality check: "Every 'Design impact' is stated explicitly" |
| C-05 | PASS | Expected field labeled `[required — not N/A]`; quality check: "Every 'Expected' cell states the prior assumption" |
| C-06 | PASS | Quality check: "At least one surprise synthesizes two or more signals — cite both sources" |
| C-07 | PASS | Quality check: "Surprises span at least three distinct namespaces" |
| C-08 | **PARTIAL** | No newcomer-reader framing at execution steps. Quality checks contain no stranger reference. Closing: "The echo is only as strong as its weakest field" — field quality focus, not accessibility focus. 800-word ceiling present |
| C-09 | PASS | Quality check: "Add Patterns section if two or more surprises share a root cause" |
| C-10 | **FAIL** | No counterfactual gate; no "Why passive observation missed this" field; culling filters do not include an inertia test |
| C-11 | **PARTIAL** | 800-word ceiling in quality checks; no per-item 120-word cap |
| C-12 | **FAIL** | No anti-hedging directive; schema fields not labeled "stated as a claim" |
| C-13 | **PASS** | Primary axis — each field carries `[required — not N/A]` inline label at write-time; Step 4 instruction: "populate it before moving to the next"; Step 5 is a dedicated field-by-field completion scan; quality check: "Every schema field is populated for every surprise — no missing fields, no N/A" and "Schema is identical across all surprises" |
| C-14 | **FAIL** | No portability test; C-08 PARTIAL, C-10/C-12 FAIL — four-mechanism convergence absent |

**Score: 93.5** — All essential pass: YES

*Note: V-01 succeeds at its primary target (C-13 PASS via inline labeling) but earns no credit outside its axis. Without the four R3-V-05 mechanisms, aspirational ceiling is bounded at 3.5 pts.*

---

### V-02 — Single axis: Portability extraction test per surprise (C-14)

| ID | Result | Key evidence |
|----|--------|-------------|
| C-01 | PASS | Culling filters include: "Drop anything that depends on surrounding context to make sense" — harder C-01 bar than baseline |
| C-02 | PASS | Step 3: "The name must communicate the finding to someone who has never seen the investigation" |
| C-03 | PASS | Source field in schema; quality check: "Every source is named (namespace + skill)" |
| C-04 | PASS | Design impact field; quality check: "Every 'Design impact' is stated, not implied" |
| C-05 | PASS | Expected field: "We assumed X"; quality check: "Every 'Expected' cell is populated" |
| C-06 | PASS | Quality check: "At least one surprise synthesizes two or more signals — cite both sources" |
| C-07 | PASS | Quality check: "Surprises span at least three distinct namespaces" |
| C-08 | **PASS** | "What portable means" preamble commits author to a stranger reader before execution. Step 1: "If I extracted this as a single entry and sent it to a new-hire, could they understand it without any context?" Step 2: "Drop anything that depends on surrounding context to make sense." Step 3: name must reach someone who has never seen the investigation. Step 4 portability test: "A reader who has never seen this project reads only this section." Newcomer framing is present at every step |
| C-09 | PASS | Quality check: "Add Patterns section if two or more surprises share a root cause" |
| C-10 | **FAIL** | No counterfactual gate (Rule 1 absent); no "Why passive observation missed this" field |
| C-11 | **PARTIAL** | 800-word ceiling in quality checks; no per-item 120-word cap |
| C-12 | **FAIL** | No anti-hedging directive; schema fields not labeled "stated as a claim"; no prohibited constructs table |
| C-13 | **PARTIAL** | No inline `[required — not N/A]` labels; no schema contract declaration; no dedicated field-scan step. Portability test implicitly requires populated fields (a surprise with N/A wouldn't pass), but indirect enforcement. Quality checks verify Expected and Design impact individually but no cross-surprise field scan |
| C-14 | **PARTIAL** | Portability test in Step 4 explicitly verifies all three components (finding, unexpectedness, design consequence) and tests context independence. This directly targets C-14's pass condition. However, C-12 FAIL (hedging not prohibited) means surprises can technically pass the portability test's three questions while stated in uncertain voice — "This may suggest X was unexpected" passes the structural test but is not an institutional claim. C-14 PASS requires authoritative, self-contained claims; without C-12, the portability test can be satisfied with weaker epistemic content |

**Score: 94** — All essential pass: YES

*Note: V-02's portability framing earns C-08 PASS (stronger than V-01/V-03) but only PARTIAL on C-14. The portability test is a necessary but not sufficient mechanism for C-14 — claim-only voice (C-12) must be co-present for the extracted surprise to function as an institutional claim, not just a portable observation.*

---

### V-03 — Single axis: Schema contract declaration + cross-surprise uniformity audit (C-13)

| ID | Result | Key evidence |
|----|--------|-------------|
| C-01 | PASS | Standard culling filters: drop expected, drop untraceable, drop standard-summary items |
| C-02 | PASS | Step 3: "content-specific, memorable. 'The Invisible Constraint' passes. 'Finding 2' fails" |
| C-03 | PASS | Source field in schema; quality check |
| C-04 | PASS | Design impact field; quality check |
| C-05 | PASS | Expected field: "We assumed X"; quality check |
| C-06 | PASS | Quality check: "At least one surprise synthesizes two or more signals" |
| C-07 | PASS | Quality check: "Surprises span at least three distinct namespaces" |
| C-08 | **PARTIAL** | 800-word ceiling in quality checks; no newcomer-reader framing during execution steps; closing: "A uniform schema makes the echo scannable" — structural focus, not accessibility focus |
| C-09 | PASS | Quality check: "Add Patterns section if two or more surprises share a root cause" |
| C-10 | **FAIL** | No counterfactual gate; no "Why passive observation missed this" field |
| C-11 | **PARTIAL** | 800-word ceiling only; no per-item cap |
| C-12 | **FAIL** | No anti-hedging directive; schema fields not labeled "stated as a claim" |
| C-13 | **PASS** | Alternative mechanism — schema contract declared before writing ("Fields applied to every surprise: all required — none optional, none N/A") is a public commitment to any reader. Step 6 uniformity audit is systematic: for each field name, read that field in every surprise in sequence and verify populated/not-N/A. Audit also verifies cross-surprise field-name uniformity. Structurally distinct from V-01 (contract + audit vs. inline labels) but achieves the same enforcement outcome |
| C-14 | **FAIL** | No portability test; C-08 PARTIAL, C-10/C-12 FAIL — four-mechanism convergence absent |

**Score: 93.5** — All essential pass: YES

*Note: V-01 and V-03 are mechanistically distinct (inline enforcement vs. contract + audit) but arrive at the same score. C-13 PASS is achieved via either mechanism. The structural audit in V-03 additionally enforces cross-surprise uniformity (field-name consistency) in a way V-01's inline mechanism does not address explicitly — but since both earn C-13 PASS, this is a qualitative distinction within the PASS tier, not a scoring difference.*

---

### V-04 — Combination: R3-V-05 + Rule 4 (C-08+C-10+C-11+C-12+C-13)

| ID | Result | Key evidence |
|----|--------|-------------|
| C-01 | PASS | Rule 1 (counterfactual gate) is stricter than "was it unexpected?" — adds the inertia test. Four culling filters including stranger-understanding test |
| C-02 | PASS | Step 3: "content-specific, memorable, self-explanatory without project context...that the stranger will remember after reading once" |
| C-03 | PASS | Source field `[required — not N/A]`; pre-output check: "Every source is named (namespace + skill)" |
| C-04 | PASS | Design impact field: "stated as a claim"; pre-output check |
| C-05 | PASS | Expected field: "stated as a claim: 'We assumed X'"; pre-output check |
| C-06 | PASS | Pre-output check: "At least one surprise synthesizes two or more signals — cite both sources" |
| C-07 | PASS | Pre-output check: "Surprises span at least three distinct namespaces" |
| C-08 | **PASS** | "Who reads this" section commits author to newcomer stranger before Step 1. Step 1: "Can the stranger understand this without reading the source?" Step 2: "Fail anything the stranger cannot understand." Step 3: "Not 'Finding 3.' Something specific to what this investigation found, that the stranger will remember after reading once." Step 4: "read it as the stranger." Pre-output check: "A stranger with no project context understands every surprise without reading the source signals." Newcomer framing at every execution stage |
| C-09 | PASS | Pre-output check |
| C-10 | **PASS** | Rule 1 is the counterfactual gate. "Why passive observation missed this" is a mandatory fifth schema field labeled `[required — not N/A]`. Pre-output check: "Every surprise fails Rule 1 — no passive team would have found it" and "Every 'Why passive observation missed this' cell is populated and explains the mechanism to a newcomer" |
| C-11 | **PASS** | Rule 3: 120-word per-item cap ("count the words from `**Source**` through end of `**Why passive observation missed this**`. If > 120: cut until you have a claim, not a description") + 800-word total. Per-output checks enforce both |
| C-12 | **PASS** | Rule 2: 8-construct prohibited language table; schema fields labeled "stated as a claim"; pre-output check: "Zero prohibited constructs in any surprise body" and "Every `**Found**` field is a statement of fact" |
| C-13 | **PASS** | Rule 4 adds explicit `[required — not N/A]` inline label to all five schema fields. Step 5 is a dedicated field-by-field scan. Pre-output check: "Every field is populated for every surprise — no N/A, no blank" and "Schema is identical across all surprises — no missing or extra fields." Rule 4 composes with the four R3-V-05 mechanisms without friction |
| C-14 | **PASS** | V-04 (R4) carries all four convergence mechanisms (C-08 PASS + C-10 PASS + C-11 PASS + C-12 PASS). The rubric characterizes C-14 as the emergent property of exactly this convergence: "A portable surprise is simultaneously bounded (C-11), non-hedging (C-12), counterfactually grounded (C-10), and stranger-accessible (C-08). When all four are present, the surprise doesn't need its context to be useful." Rule 4 (C-13) reinforces portability — complete schemas mean every surprise carries its expectation, finding, impact, and counterfactual explicitly, with no inference required from context. C-14 emerges without a portability test |

**Score: 100** — All essential pass: YES

*Note: V-04 (R4) prediction was 100/100 + C-13 PASS. Confirmed. Rule 4 composes cleanly — schema completeness enforcement does not conflict with any of the four R3-V-05 mechanisms. C-14 PASS is emergent from the four-mechanism convergence, confirming the rubric's causal characterization.*

---

### V-05 — Full convergence: R3-V-05 + C-13 + explicit portability test (all six mechanisms)

| ID | Result | Key evidence |
|----|--------|-------------|
| C-01 | PASS | Rule 1 (counterfactual gate) + four culling filters. Step 1 adds "Can it stand alone when extracted from this echo?" as an additional inclusion criterion. No degradation — standalone portability test strengthens C-01 by catching context-dependent items at the culling stage |
| C-02 | PASS | Step 3: "Content-specific, memorable, self-explanatory without project context. The stranger will encounter this name out of context — it must work alone." Portability framing raises naming bar further |
| C-03 | PASS | Source field `[required — not N/A]`; structural check present |
| C-04 | PASS | Design impact: "stated as a claim"; structural check present |
| C-05 | PASS | Expected: "stated as a claim: 'We assumed X'"; structural check |
| C-06 | PASS | Structural check: "At least one surprise synthesizes two or more signals" |
| C-07 | PASS | Structural check: "Surprises span at least three distinct namespaces" |
| C-08 | **PASS** | Same "Who reads this" newcomer commitment as V-04, plus Check B portability test reinforces stranger framing. "Why passive observation missed this" must be explained "without project-internal shorthand." Pre-output check: "A stranger with no project context understands every surprise without reading the source signals." Strongest C-08 enforcement in the R4 set |
| C-09 | PASS | Structural check |
| C-10 | **PASS** | Rule 1 + mandatory fifth field + stranger-accessible CF explanation — identical to V-04 |
| C-11 | **PASS** | Rule 3: 120-word per-item cap + 800-word total. Check A per-item enforcement: "Word count from `**Source**` through end of `**Why passive observation missed this**` is at or under 120 words." Both per-item and total enforced |
| C-12 | **PASS** | Rule 2 + "stated as a claim" field labels + "The stranger needs claims" + pre-output checks — identical to V-04. Check A also scans for prohibited constructs per surprise before proceeding |
| C-13 | **PASS** | Rule 4: `[required — not N/A]` on all five fields + Check A: "All five fields are populated — none is N/A or blank." Step 5 field completion scan. Pre-output check: "Every field is populated for every surprise — no N/A, no blank" and "Schema is identical across all surprises" |
| C-14 | **PASS** | V-05 achieves C-14 both emergently (four-mechanism convergence present, same as V-04) and deliberately (Check B: "Imagine this surprise extracted from the echo. A reader who has never seen this project reads only this section. Does it communicate all three? 1. What the finding is, 2. Why it was unexpected, 3. Why it matters for design. Does it require reading any other surprise, any source signal, or any project background?"). Check B is applied per-surprise before proceeding — it is an authorial step, not an emergent consequence. Pre-output check: "Every surprise passes the portability test — finding, expectation, and design consequence are self-contained." C-14 is converted from emergent to deliberate with no friction |

**Score: 100** — All essential pass: YES

*Note: The predicted V-05 friction risk (six mechanisms degrading essential criteria) did not materialize. Six mechanisms orient toward the same reader — the newcomer stranger — so they reinforce each other. Check B adds one explicit step per surprise; the 120-word cap prevents it from generating over-writing. Mechanisms composed cleanly.*

---

## Rankings

| Rank | Variation | Score | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 |
|------|-----------|-------|------|------|------|------|------|------|------|
| 1 | **V-04** — R3-V-05 + Rule 4 | **100** | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| 1 | **V-05** — R3-V-05 + Rule 4 + Portability test | **100** | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| 3 | **V-02** — Portability extraction test | **94** | PASS | PASS | FAIL | PARTIAL | FAIL | PARTIAL | PARTIAL |
| 4 | **V-01** — Per-field inline labels | **93.5** | PARTIAL | PASS | FAIL | PARTIAL | FAIL | PASS | FAIL |
| 4 | **V-03** — Schema contract + audit | **93.5** | PARTIAL | PASS | FAIL | PARTIAL | FAIL | PASS | FAIL |

---

## Gap Analysis

**V-04 and V-05 both reach 100/100, confirming the R4 hypothesis.** V-04 was predicted to score 100/100 + C-13 PASS. Confirmed. Rule 4 adds schema completeness enforcement to the R3-V-05 baseline without friction. V-05 adds the explicit portability test without friction. Both achieve C-13 PASS and C-14 PASS.

**V-01 and V-03 both earn C-13 PASS via distinct mechanisms.** The R4 structural bet — that inline labeling (V-01) and contract declaration + audit (V-03) would diverge — did not materialize. Both mechanisms achieve the same outcome. The critical shared ingredient is a systematic enforcement step (whether inline or post-write). Neither mechanism is superior within the single-axis test. Both arrive at 93.5.

**V-02's portability test earns C-14 PARTIAL, not PASS.** The explicit extraction test verifies the three structural questions (finding, unexpectedness, design consequence) but cannot enforce epistemic authority. Without Rule 2 (claim-only voice), surprises can satisfy the portability test structurally while remaining hedged observations. C-14's pass condition requires self-contained *institutional claims*, not self-contained *observations*. The portability test is necessary but not sufficient.

**Single-axis variations cap at 93.5–94.** V-01, V-02, V-03 all fail C-10 and C-12. Without the counterfactual field and claim-only voice, aspirational ceiling is bounded regardless of what single mechanism is added. The ceiling gap between 94 and 100 is the cost of missing the four-mechanism convergence.

**C-14 as emergent vs. deliberate.** V-04 and V-05 score identically (100), but qualitatively differ: V-04 achieves C-14 as an emergent property of four-mechanism convergence; V-05 achieves it both emergently and deliberately via Check B. The portability test in V-05 makes C-14 independently verifiable — an author can confirm portability without having to trust that all four mechanisms happened to converge. This has operational value: an author who hasn't mastered all four mechanisms can still enforce C-14 by running Check B.

---

## Excellence Signals from V-04/V-05

**1. Rule 4 (schema completeness) composes without friction.** The predicted risk was that adding a fifth mechanism might create tension with claim-only voice (Rule 2) or length discipline (Rule 3) — an author might over-fill required fields to avoid N/A, inflating word count. The mechanisms do not conflict because the 120-word cap operates after field population; an author who over-writes in a required field is immediately cut at the Check A word-count step. The two mechanisms serve different failure modes: Rule 4 prevents gaps, Rule 3 prevents elaboration.

**2. C-13 enforcement is the structural substrate for C-14.** A portable surprise requires every field to be present and substantive — an incomplete field (N/A in Expected, blank in Why passive observation missed this) breaks portability by requiring the reader to fill in context. Rule 4 ensures all five fields are populated, which eliminates context-dependence at the field level before the portability test runs. Schema completeness and surprise portability are complementary, not separate objectives.

**3. Check B converts C-14 from emergent to deliberate without adding friction.** V-05's portability test (Check B) is a per-surprise extraction simulation that takes approximately 30 seconds per entry. The 120-word cap prevents over-writing in response to the test (authors can't add context to cover portability — they must compress to achieve it). Check B therefore enforces C-14 by requiring synthesis, not elaboration. This is the same cognitive operation as cutting to the claim rather than hedging — Check B and Rule 2 are complementary disciplines.

**4. All six mechanisms share a single unifying reader.** V-05's predicted friction risk (six mechanisms) did not materialize because all six point at the newcomer stranger: Rule 1 (what they couldn't have found passively), Rule 2 (claims they can act on), Rule 3 (short enough to absorb in one reading), Rule 4 (complete enough to need no context), newcomer framing (explained without project-internal shorthand), Check B (portable when extracted to their context). Six mechanisms with one reader produce reinforcement, not conflict.

---

## Cross-Variation Patterns (New in R4)

**C-13 is mechanism-agnostic.** Inline per-field labels (V-01) and schema contract + post-write audit (V-03) both earn C-13 PASS. The distinguishing requirement is a systematic verification step — whether it runs at write-time (inline) or post-write (audit) does not affect the criterion outcome. Both are valid enforcement mechanisms.

**C-14 requires claim voice (C-12) to earn PASS from a portability test.** V-02's portability test earns PARTIAL because surprises without C-12 can structurally satisfy the three portability questions while remaining hedged. C-14's pass condition is "self-contained institutional claim" — the epistemic authority of C-12 is a prerequisite for the portability test to produce PASS rather than PARTIAL.

**The four-mechanism convergence (C-08+C-10+C-11+C-12) is sufficient to produce C-14 without an explicit test.** V-04 (R4) achieves C-14 PASS emergently. The explicit portability test in V-05 is additive — it makes C-14 independently verifiable and deliberate — but not necessary for PASS when the four mechanisms are all present.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-13 is mechanism-agnostic — inline per-field labels (V-01) and schema contract + post-write uniformity audit (V-03) both earn C-13 PASS; the distinguishing requirement is a systematic verification step, not which form it takes", "C-14 requires claim-only voice (C-12) to earn PASS from a portability test — without C-12, surprises can structurally satisfy the portability test's three questions while remaining hedged observations rather than institutional claims; the portability test is necessary but not sufficient for C-14 PASS", "the four-mechanism convergence (C-08+C-10+C-11+C-12) is sufficient for C-14 PASS without an explicit portability test; V-05's Check B converts C-14 from emergent to deliberate, making it independently verifiable for authors who cannot rely on mechanism convergence to produce it automatically"]}
```
