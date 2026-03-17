# topic-open Scorecard — Round 1

All 5 variations pass all 5 essential criteria. Ranking:

| Rank | Var | Composite | Key strength |
|------|-----|-----------|--------------|
| 1 | V-05 | **100** | Upfront vocab block + Phase 6 self-check closes every escape route |
| 2 | V-03 | **98** | AMEND phase catches drift after generation; only single-axis with self-correction |
| 3 | V-04 | **97.5** | Strongest C-04 motivation ("load-bearing / most common mistake / silent breakage"); C-10 partial (no item name template) |
| 4 | V-01 | **97** | Hardest upfront constraints; clean imperative register; no self-check |
| 5 | V-02 | **95** | Prose-before-table is best for C-07/C-08; C-04 buried in column defs |

**Golden threshold**: all 5 clear (>= 80, all essential pass).

---

**5 new patterns extracted:**

1. **Upfront vocabulary constraint block** — placing the vocabulary rule before all instructions suppresses C-04 more reliably than inline column definitions. Placement predicts retention.

2. **Self-check checklist** — Phase 6 checkbox items that map directly to rubric criteria catch drift that slipped through instruction reading. V-03/V-05 both demonstrate this; V-05 is more explicit.

3. **AMEND loop as targeted second defense** — "Did any row use high/medium/low?" beats "review your output." Named question forces re-evaluation of the exact failure mode.

4. **Downstream consequence framing** — V-04's "Wrong vocabulary = silent breakage / most common mistake" gives the model a *reason* to care about C-04, not just a rule. Attention follows stakes.

5. **Prose-before-table sequencing** — writing rationale first makes role differentiation emerge from the decision context (C-08 natural, not count-enforced).

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["upfront vocabulary constraint block before any instructions suppresses C-04 substitution more reliably than inline column definitions", "self-check checklist with explicit checkbox items catches vocabulary drift after generation, not just before", "AMEND/self-correction loop as second-layer C-04 defense: targeted re-read question beats generic review instruction", "motivational framing with downstream consequence explanation increases model attention on the hardest criterion", "prose-rationale-before-table sequencing makes role differentiation emerge from decision context rather than requiring count enforcement"]}
```
OT use" in column definitions; three-tier semantics given. Risk: buried inside column defs, not a standalone block — slight drift exposure in long outputs |
| C-05 | PASS | Signal set requirements: "At least one priority = essential (otherwise there is no commit gate)" |
| C-06 | PASS | Signal set requirements: "At least 2 distinct namespaces represented" |
| C-07 | PASS | Part A required before signals; 3 guiding questions; "Write it before choosing signals" sequencing instruction |
| C-08 | PASS | "vary roles across signals to reflect real ownership" + minimum 2 distinct roles constraint |
| C-09 | PASS | Named COMMIT GATE section at end; "do not say 'all essential signals'" callout |
| C-10 | PASS | "artifact filename following: {topic}-{signal}-{date}.md" in column definitions |

**Essential**: 5/5 → 60  **Recommended**: 3/3 → 30  **Aspirational**: 2/2 → 10

**Composite: 95**

_Deduction_: C-04 defense is placed inside column definitions — second-tier placement increases risk of vocabulary drift in a long output. No self-check. Prose-before-table sequencing is V-02's strongest contribution: it makes C-07 and C-08 emerge from the decision context rather than requiring count enforcement.

---

## V-03 — Lifecycle Emphasis (4 named phases + AMEND)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 3 Write 1: explicit row format |
| C-02 | PASS | Phase 3 Write 2: exact path `simulations/{topic}/strategy.md` |
| C-03 | PASS | Fields 1–5 enumerated by number in Phase 2b |
| C-04 | PASS | "STOP — do not use high/medium/low" callout inside field definition + Phase 4 AMEND asks "Did any row use high/medium/low?" — two-layer defense: instruction + self-correction |
| C-05 | PASS | "Minimum 1 signal with priority = essential" in Phase 2b + AMEND check |
| C-06 | PASS | "Minimum 2 distinct namespaces" in Phase 2b constraints |
| C-07 | PASS | Phase 2a dedicated to rationale; 3 guiding questions; 2–4 sentences required |
| C-08 | PASS | "Minimum 2 distinct owner roles" explicit constraint |
| C-09 | PASS | Phase 2c derives gate; Phase 3 template includes Commit Gate section; AMEND checks item names are specific (not "all essential") |
| C-10 | PASS | Template `{topic}-{signal}-{date}.md` in field 3 definition |

**Essential**: 5/5 → 60  **Recommended**: 3/3 → 30  **Aspirational**: 2/2 → 10

**Composite: 98**

_Excellence note_: AMEND phase is V-03's unique contribution — it re-reads the draft and catches violations that slipped through instruction reading. This is the only single-axis design with an explicit self-correction loop. The two-layer C-04 defense (STOP callout + AMEND) is the most robust among V-01–V-04.

---

## V-04 — Inertia Framing (status quo named prominently)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | "Read simulations/TOPICS.md. Append: | {slug} | {description} | {YYYY-MM-DD} | Write the file." |
| C-02 | PASS | Path stated + parenthetical "Not inline in TOPICS.md. Not in a flat directory. At the exact path above." |
| C-03 | PASS | 5-column table defined in OUTPUT 2 |
| C-04 | PASS | "THIS IS LOAD-BEARING" + "Wrong vocabulary = silent breakage" + "This is the most common mistake in topic strategy files" — strongest motivational framing for C-04 in this set |
| C-05 | PASS | "One signal marked essential (otherwise the strategy has no commit gate)" |
| C-06 | PASS | "Two or more distinct namespaces" |
| C-07 | PASS | Section A with 3 guiding questions; 2–4 sentences required |
| C-08 | PASS | "Two or more distinct owner roles" |
| C-09 | PASS | Section C explicitly required; "not 'all essential signals' — the actual names" |
| C-10 | PARTIAL | Table includes "item name" column but `{topic}-{signal}-{date}.md` template never stated; a model may produce readable names that don't follow the convention |

**Essential**: 5/5 → 60  **Recommended**: 3/3 → 30  **Aspirational**: C-09 PASS + C-10 PARTIAL → 7.5

**Composite: 97.5**

_C-10 gap_: Only variation that omits the item name template. The "load-bearing vocabulary" framing for C-04 is V-04's strongest contribution — explaining downstream consequence and naming it the most common mistake increases model attention at exactly the right point.

---

## V-05 — Combination (all four axes)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 5 Write 1; YYYY-MM-DD format explicitly required |
| C-02 | PASS | Phase 5 Write 2 names exact path; self-check "[ ] Strategy path is simulations/{topic}/strategy.md" |
| C-03 | PASS | Phase 3 enumerates all 5 fields; self-check "[ ] Every row has all 5 fields (namespace, skill, item name, owner role, priority)" |
| C-04 | PASS | Upfront vocabulary constraint block before any instructions + self-check "[ ] Every priority value is exactly: essential \| recommended \| optional" — strongest two-layer defense: front-loaded + end-of-output verification |
| C-05 | PASS | Phase 3 checklist "[ ] At least 1 signal with priority = essential" + self-check |
| C-06 | PASS | Phase 3 checklist "[ ] At least 2 distinct namespaces" |
| C-07 | PASS | Phase 2 dedicated with editorial framing: "The rationale is the editorial contract for the signal plan. Without it, the strategy is a table without a reason." |
| C-08 | PASS | "vary across signals to reflect real ownership" + Phase 3 checklist |
| C-09 | PASS | Phase 4 dedicated to commit gate; example form with actual filename pattern; self-check "[ ] Commit Gate names specific item filenames" |
| C-10 | PASS | Template `{topic}-{signal}-{date}.md` in Phase 3 + example in Phase 4 commit gate section |

**Essential**: 5/5 → 60  **Recommended**: 3/3 → 30  **Aspirational**: 2/2 → 10

**Composite: 100**

_Excellence note_: Phase 6 self-check has 5 explicit checkbox items, one per essential criterion. Combined with the upfront vocabulary constraint block, V-05 suppresses each failure mode at two points: before the model generates the content (constraint) and after (verification). No other variation achieves this for all 5 essential criteria simultaneously.

---

## Ranking

| Rank | Var | Composite | Essential | All pass |
|------|-----|-----------|-----------|----------|
| 1 | V-05 | 100 | 5/5 | yes |
| 2 | V-03 | 98 | 5/5 | yes |
| 3 | V-01 | 97 | 5/5 | yes |
| 4 | V-04 | 97.5 | 5/5 | yes (C-10 partial) |
| 5 | V-02 | 95 | 5/5 | yes |

Golden threshold (5 essential + composite >= 80): **V-05, V-03, V-01, V-04, V-02** — all clear.

---

## Excellence Signals

Patterns from the top-scoring variation (V-05) and runners-up that produced the best per-criterion coverage:

1. **Upfront vocabulary constraint block** — placing `essential | recommended | optional` as a standalone constraint *before* any task instructions suppresses C-04 substitution more reliably than embedding the same constraint inside column definitions or field descriptions. Placement matters: a model reading a long skill prompt is most likely to retain the first constraint block it sees.

2. **Self-check checklist with explicit checkbox items** — a Phase 6 (or AMEND phase) that explicitly re-reads the draft and verifies each primary failure mode catches drift that slipped through instruction reading. V-03's AMEND and V-05's Phase 6 both demonstrate this; V-05 uses checkbox syntax that maps directly to rubric criteria.

3. **AMEND/self-correction loop as a second defense layer** — in V-03, the AMEND phase asks "Did any row use high/medium/low?" — a targeted question that forces re-evaluation of the most common failure. This is more effective than a generic "review your output" instruction.

4. **Motivational framing for the hardest criterion** — V-04's "THIS IS LOAD-BEARING / most common mistake / silent breakage" pattern increases model attention on C-04 specifically. Naming the downstream consequence ("commit gate evaluator reads these exact strings") gives the model a reason to care, not just a rule to follow.

5. **Prose-rationale-before-table sequencing** — V-02's "write rationale before choosing signals" instruction makes C-08 role differentiation emerge naturally. When the model first articulates the decision and its stakeholders, it selects signals that reflect real ownership rather than assigning a single generic role to all rows.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["upfront vocabulary constraint block before any instructions suppresses C-04 substitution more reliably than inline column definitions", "self-check checklist with explicit checkbox items catches vocabulary drift after generation, not just before", "AMEND/self-correction loop as second-layer C-04 defense: targeted re-read question beats generic review instruction", "motivational framing with downstream consequence explanation increases model attention on the hardest criterion", "prose-rationale-before-table sequencing makes role differentiation emerge from decision context rather than requiring count enforcement"]}
```
