## discover-causal Scorecard — Round 1

### Scoring Methodology

Point allocation from rubric tier distribution (no per-criterion weights stated; equal within tier assumed):
- **Essential** (C-01–C-05): 12 pts each = 60 pts
- **Recommended** (C-06–C-08): 10 pts each = 30 pts
- **Aspirational** (C-09–C-10): 5 pts each = 10 pts

PASS = full credit, PARTIAL = 50% for essential / variable for recommended, FAIL = 0.

---

### V-01: Baseline prose

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | Three-part step instruction: what/agent/observable indicator. Counter-instruction: "A pathway that reads 'X leads to better outcomes' does not pass." |
| C-02 | Falsification is mechanism break | PASS | 12 | Explicit counter-example ("not 'if metric Y doesn't improve'") + "must reference a specific step in the mechanism pathway above." |
| C-03 | Inertia check performed | PASS | 12 | "This check is required. Do not skip it or treat it as optional." Explicit, near end of prompt — risk of deprioritization under pressure, but structurally required. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | "MORE specific... Restating the original hypothesis does not pass. Broadening it does not pass." |
| C-05 | Context evidence assessed | PASS | 12 | Explicit null case + "Do not cite general research as a substitute for team-specific evidence." |
| C-06 | Pathway is testable | PASS | 10 | Observable indicator per step — structural enforcement via prose checklist. |
| C-07 | Confounder or alternative cause | FAIL | 0 | Not mentioned anywhere in V-01. |
| C-08 | AMEND is actionable | PASS | 8 | Names specific narrowing forms ("narrower scope, bounded population, named mechanism qualifier, or explicit condition") but does not require at least one — guidance, not gate. |
| C-09 | Evidence quality rated | FAIL | 0 | Not asked. |
| C-10 | Multiple causal pathways | FAIL | 0 | Not asked. |
| **Total** | | | **78** | All essential: PASS |

---

### V-02: Pathway table

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | Table with mandatory "Observable indicator" column + min 3 rows + final row = outcome Y. Structural enforcement stronger than V-01 prose. |
| C-02 | Falsification is mechanism break | PASS | 12 | Template format: "The mechanism fails if: [step N does not occur] — observable as: [specific indicator]." Named-step anchor makes the row reference explicit. |
| C-03 | Inertia check performed | PASS | 12 | "If you skip this step, the analysis is incomplete." Step-numbered label (STEP 3) in lifecycle sequence. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | "must be more specific than the original. Restating the original is a failure mode." |
| C-05 | Context evidence assessed | PASS | 12 | Explicit null case + "do not count" general research, note separately. |
| C-06 | Pathway is testable | PASS | 10 | Dedicated "Observable indicator" table column — most structural enforcement of any variation for C-06. |
| C-07 | Confounder or alternative cause | FAIL | 0 | Not mentioned. |
| C-08 | AMEND is actionable | PASS | 8 | "bounded by scope, population, or mechanism qualifier" — names options, similar guidance level to V-01. |
| C-09 | Evidence quality rated | FAIL | 0 | Frontmatter adds `break_point_step` but no evidence quality field. |
| C-10 | Multiple causal pathways | FAIL | 0 | Not asked. |
| **Total** | | | **78** | All essential: PASS |

**V-02 vs V-01 note:** Structurally stronger on C-06 (table column vs prose checklist), but same rubric score because both pass. The table prevents the observable indicator from being omitted in a way prose cannot.

---

### V-03: Inertia-first

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | Three-part per-step instruction + "Minimum: 3 named, observable steps." |
| C-02 | Falsification is mechanism break | PASS | 12 | "The mechanism fails if [step N does not occur], observable as [specific indicator]. A metric shortfall is not a mechanism break." |
| C-03 | Inertia check performed | PASS | 12 | Front-loaded as first section, labeled "most commonly skipped, always required," three ordered assessment questions. Structurally strongest C-03 of all variations. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | "must include at least one: bounded scope, named mechanism qualifier, or inertia-conditioned framing like 'in contexts where the status quo does not already...'" — stronger than V-01: requires one of three specific forms. |
| C-05 | Context evidence assessed | PASS | 12 | "Name it. If none: 'No context-specific evidence found.' Note general evidence separately." |
| C-06 | Pathway is testable | PASS | 10 | Observable indicator per step. If inertia competes, mechanism must explain "what the feature adds or accelerates" — adds context-dependent testability requirement. |
| C-07 | Confounder or alternative cause | FAIL | 0 | Inertia check surfaces status-quo alternative but does not ask for independent confounders. |
| C-08 | AMEND is actionable | PASS | 9 | "must include at least one" of three named options including inertia-conditioned framing — the "at least one" requirement and the `Inertia finding` AMEND field structurally enforce actionability. Stronger than V-01. |
| C-09 | Evidence quality rated | FAIL | 0 | |
| C-10 | Multiple causal pathways | FAIL | 0 | |
| **Total** | | | **79** | All essential: PASS |

---

### V-04: Skeptical advisor

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | "Walk through the causal chain. Name the steps. For each step: what changes, who changes it, how would you know it happened?" + "If you cannot name at least 3 observable intermediate steps... say so." Self-disclosure path is unique to V-04. |
| C-02 | Falsification is mechanism break | PASS | 12 | "Not 'retention goes down' — that is an outcome check... give me that specific break point." Adversarial register adds compliance pressure. Example given. |
| C-03 | Inertia check performed | PASS | 12 | "This is the question teams almost always skip... 'We didn't check' is not acceptable — check now." Behavioral accountability framing — stronger pressure than "required, do not skip." |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | "must be narrower... Do not restate the original. Do not broaden it." |
| C-05 | Context evidence assessed | PASS | 12 | "Not what studies show. Not what analogous products did. What does this team's own data, user behavior, or signal artifact set show?" — sharpest exclusion language of all variations for C-05. |
| C-06 | Pathway is testable | PASS | 10 | "how would you know it happened?" per step. PASS. |
| C-07 | Confounder or alternative cause | PARTIAL | 5 | "If the status quo could plausibly deliver Y through some other route..." — approximates alternative cause identification via the inertia section. Not a dedicated confounder prompt but the adversarial phrasing ("through some other route") is the only instruction across all variations that approaches C-07 territory. |
| C-08 | AMEND is actionable | PASS | 9 | "tighter scope, named conditions, mechanism qualifier, or population boundary. Do not restate the original." Named concrete forms. |
| C-09 | Evidence quality rated | FAIL | 0 | |
| C-10 | Multiple causal pathways | FAIL | 0 | |
| **Total** | | | **84** | All essential: PASS |

---

### V-05: Lifecycle + table + inertia-first

| ID | Criterion | Verdict | Pts | Evidence Note |
|----|-----------|---------|-----|---------------|
| C-01 | Mechanism traced as pathway | PASS | 12 | Table with observable indicator column + INCOMPLETE gate ("PATHWAY INCOMPLETE: mechanism cannot be adequately traced...") — explicit degradation path forces acknowledgment when mechanism is underdeveloped. |
| C-02 | Falsification is mechanism break | PASS | 12 | "The mechanism fails if: [step N does not occur] — observable as: [specific indicator]" + "Column reference: name the row number from the Phase 2 table." Row number tie to table is the most precise falsification anchor. |
| C-03 | Inertia check performed | PASS | 12 | Phase 1 with GATE label + one-line verdict format (INERTIA STATUS: Competing / Not competing / Unclear) + structural gate if competing. |
| C-04 | Causal claim narrowed in AMEND | PASS | 12 | "must include a mechanism qualifier, bounded scope, or inertia-conditioned framing. Restating is a failure mode. Broadening is a failure mode." Strongest explicit AMEND instruction. |
| C-05 | Context evidence assessed | PASS | 12 | Two required outputs: (1) context evidence or explicit null; (2) evidence_gap_steps — names which pathway steps lack support. Strongest C-05 enforcement. |
| C-06 | Pathway is testable | PASS | 10 | Table column + INCOMPLETE gate. |
| C-07 | Confounder or alternative cause | FAIL | 0 | Inertia gate asks about competing explanations but not independent confounders. |
| C-08 | AMEND is actionable | PASS | 10 | "must include a mechanism qualifier, bounded scope, or inertia-conditioned framing" — requires one of three specific concrete forms. Strongest C-08 instruction. |
| C-09 | Evidence quality rated | PARTIAL | 2 | The `evidence_gap_steps` frontmatter field is the closest any variation gets to evidence quality — it distinguishes steps with vs without contextual support. Not a full quality rating, but a structural differentiation proxy. |
| C-10 | Multiple causal pathways | FAIL | 0 | |
| **Total** | | | **82** | All essential: PASS |

---

### Rankings

| Rank | Variation | Score | All Essential Pass | Notes |
|------|-----------|-------|-------------------|-------|
| 1 | **V-04: Skeptical advisor** | **84** | YES | C-07 partial via adversarial inertia framing; sharpest C-05 |
| 2 | **V-05: Combination** | **82** | YES | Strongest C-04/C-08/C-05; partial C-09 via evidence gap |
| 3 | **V-03: Inertia-first** | **79** | YES | Strongest C-03; stronger C-08 than baseline |
| 4 | **V-01: Baseline prose** | **78** | YES | Clean baseline; no structural weaknesses but no standout strengths |
| 5 | **V-02: Pathway table** | **78** | YES | Strongest C-06 structural enforcement; tied with V-01 on score |

Both V-04 (84) and V-05 (82) meet the Golden bar (all essential pass + >= 80).

---

### Excellence Signals from V-04

**What made V-04 the top-scoring variation:**

1. **Adversarial register creates accountability pressure** — "We didn't check is not acceptable" lands differently than "this check is required." The social/behavioral framing raises the cost of omission. This pattern likely improves C-03 compliance in LLM outputs beyond what passive imperatives achieve.

2. **Counter-examples embedded in every key section** — V-04 gives "not retention goes down" before asking for the falsification condition, and "not what studies show" before asking for context evidence. Injecting the failure mode as a negative example immediately before the instruction is a stronger structural guard than stating the correct form once.

3. **Implicit C-07 coverage via "through some other route" framing** — No other variation approaches confounder identification. V-04 achieves a partial by asking whether the status quo delivers Y "through some other route" — getting 5 pts from a criterion that none of the other variations touch.

4. **Self-disclosure path for incomplete mechanisms** — "If you cannot name at least 3 observable intermediate steps, the claim does not yet have a mechanism — say so" gives the model a graceful exit instead of forcing a vague pathway. This pattern likely improves output quality by permitting honest incompleteness rather than confabulated specificity.

5. **C-05 exclusion language is sharpest** — The three-line exclusion ("not what studies show, not what analogous products did, what does THIS team's own data show") is more memorable and harder to violate than a single prohibition.

---

```json
{"top_score": 84, "all_essential_pass": true, "new_patterns": ["adversarial register increases C-03 compliance through behavioral accountability framing ('we didn't check is not acceptable') vs passive imperatives ('this check is required')", "counter-example injection immediately before instruction ('not X — give me Y') is stronger structural guard than stating the correct form once", "implicit C-07 coverage via inertia framing: asking whether status quo produces Y 'through some other route' approximates alternative cause identification without a dedicated section", "self-disclosure path for incomplete mechanisms prevents confabulated pathways: 'if you cannot name 3 steps, say so' produces honest incompleteness rather than vague specificity"]}
```
