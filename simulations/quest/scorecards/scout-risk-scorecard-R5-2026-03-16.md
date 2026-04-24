# Quest Score — scout-risk — Round 5

## Scoring Matrix

### V-01 — Role Sequence (Analyst → Auditor)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia mandatory and first | **PASS** | "This entry is mandatory and must appear first. It cannot be omitted or moved." |
| C-02 | Dimensional coverage | **PASS** | "You must cover at least three" of five named dimensions |
| C-03 | Risk anatomy complete | **PASS** | "Each risk entry (including inertia) must contain exactly three fields: Severity, Likelihood, Mitigation" |
| C-04 | Severity scale correct | **PASS** | "one of `HIGH`, `MEDIUM`, or `LOW`. No other values." |
| C-05 | Mitigations actionable | **PASS** | Prohibited phrase list + "Each mitigation must state what to do" |
| C-06 | Dimension-labeled | **PASS** | "Tag every risk entry with its dimension label... inertia risk is tagged `[Inertia]`" |
| C-07 | Likelihood condition-qualified | **PASS** | "State the scenario or trigger under which this risk activates, not just a bare label" |
| C-08 | Ordered by priority | **PASS** | "Order remaining entries from highest to lowest severity. For ties, place higher likelihood first." |
| C-09 | Interdependencies noted | **PASS** | Role 2 requires compound-risk pairs with severity transitions |
| C-10 | AMEND behavior | **PASS** | Explicit AMEND section: focus-one-dimension + severity-threshold, inertia retained |
| C-11 | Zero-generic mitigations | **PASS** | Five specific forbidden phrases listed with "stop and replace" instruction |
| C-12 | All likelihoods trigger-qualified | **PASS** | "a condition-qualified statement" — applies to each risk entry uniformly |
| C-13 | Interdependencies structured section | **PASS** | "produce a dedicated **Risk Interdependencies** section" with ≥3 pairings |
| C-14 | IF-THEN syntactic form | **FAIL** | Requires condition/scenario; does not enforce IF-THEN syntax |
| C-15 | Mitigation type declared | **FAIL** | No mitigation type taxonomy (Spike/Validate/Gate/etc.) anywhere in prompt |
| C-16 | Interdependency count ≥3 | **PASS** | "You must produce at least three distinct pairings" + repair loop back to Step 2 |
| C-17 | Severity-transition labels | **PASS** | "State the severity transition: FROM... TO..."; Step 7 audits for explicit FROM/TO values |
| C-18 | Type portfolio ≥3 distinct | **FAIL** | No type taxonomy → cannot enforce diversity |
| C-19 | Enumerated forbidden phrases | **PASS** | Five specific phrases named by text |
| C-20 | Back-pressure repair loop | **PASS** | "return to Step 2 and add or refine dimensional risks until three distinct pairings are supported" |

**Essential**: 60/60 (all 5 pass)
**Recommended**: 30/30
**Aspirational**: C-09(2)+C-10(2)+C-11(2)+C-12(2)+C-13(2)+C-14(0)+C-15(0)+C-16(2)+C-17(2)+C-18(0)+C-19(2)+C-20(2) = **18/24**

**V-01 Total: 108 / 114 — GOLDEN**

---

### V-02 — Output Format (Strict Table Schema)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia mandatory and first | **PASS** | "Row 1 must be the Inertia Risk. This row is not optional and cannot be placed later." |
| C-02 | Dimensional coverage | **PASS** | "include risks from at least three of the five dimensions" |
| C-03 | Risk anatomy complete | **PASS** | Table schema enforces Severity, Likelihood, Mitigation as explicit columns with column-level rules |
| C-04 | Severity scale correct | **PASS** | "Exactly one of `HIGH`, `MEDIUM`, `LOW`. No other values." |
| C-05 | Mitigations actionable | **PASS** | Five forbidden phrases enumerated in column rule: "none of these may appear in any cell" |
| C-06 | Dimension-labeled | **PASS** | Dimension is an explicit column: "One of `Inertia`, `Technical`, `Market`, `Compliance`, `Dependency`, `Timeline`" |
| C-07 | Likelihood condition-qualified | **PASS** | "Must name the scenario or triggering condition... A bare label is not acceptable" |
| C-08 | Ordered by priority | **PASS** | "`HIGH` to `LOW`; within same severity, order by likelihood (most likely first)" |
| C-09 | Interdependencies noted | **PASS** | Dedicated interdependency table required |
| C-10 | AMEND behavior | **PASS** | AMEND section: focus-one-dimension retains Row 1; severity-threshold adds header row |
| C-11 | Zero-generic mitigations | **PASS** | Column rule lists five prohibited phrases explicitly |
| C-12 | All likelihoods trigger-qualified | **PASS** | Column rule applies to all rows uniformly |
| C-13 | Interdependencies structured section | **PASS** | "second table" with dedicated schema + minimum 3 rows |
| C-14 | IF-THEN syntactic form | **FAIL** | Scenario/condition required but IF-THEN syntax not enforced |
| C-15 | Mitigation type declared | **PASS** | "Mitigation Type" is an explicit schema column; taxonomy enumerated (Spike/Validate/Gate/Contract/Cut/Instrument) |
| C-16 | Interdependency count ≥3 | **PASS** | "Minimum 3 rows... return to the main register and add or refine entries" |
| C-17 | Severity-transition labels | **PASS** | From/To columns in interdependency table; each "must contain exactly one of `HIGH`, `MEDIUM`, `LOW`" |
| C-18 | Type portfolio ≥3 distinct | **PASS** | "If N < 3, return to the main register and revise mitigations until at least 3 distinct types are represented" |
| C-19 | Enumerated forbidden phrases | **PASS** | Five phrases enumerated in Mitigation column rule |
| C-20 | Back-pressure repair loop | **PASS** | Two loops: interdependency count → "return to main register"; type audit → "return to main register and revise" |

**Essential**: 60/60 (all 5 pass)
**Recommended**: 30/30
**Aspirational**: C-09(2)+C-10(2)+C-11(2)+C-12(2)+C-13(2)+C-14(0)+C-15(2)+C-16(2)+C-17(2)+C-18(2)+C-19(2)+C-20(2) = **22/24**

**V-02 Total: 112 / 114 — GOLDEN**

---

### V-03 — Phrasing Register (Conversational Imperative)

> **Note**: Prompt text is truncated — only Steps 1–2 are visible. Assessment is bounded by available text.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Inertia mandatory and first | **PASS** | "This one is required — every register starts with it, no exceptions." |
| C-02 | Dimensional coverage | **PASS** | "Cover at least three of these five areas" with all five listed |
| C-03 | Risk anatomy complete | **PARTIAL** | Anatomy stated for inertia entry; dimensional risk anatomy enforcement not visible (text cut off) |
| C-04 | Severity scale correct | **PARTIAL** | "HIGH, MEDIUM, or LOW — nothing else" visible for inertia; unclear for dimensional entries |
| C-05 | Mitigations actionable | **FAIL** | No prohibited phrase list or mitigation specificity enforcement visible |
| C-06 through C-20 | All remaining | **FAIL / UNKNOWN** | Not present in visible text |

**Essential**: 12+12+8+8+0 = **40** (C-05 fails → capped at 48, cannot reach golden)
**Recommended**: 0
**Aspirational**: 0

**V-03 Visible Score: ~40 / 114 — FAILING (truncation prevents full assessment)**

---

### V-04 — Inertia framing (dedicated section)

> **No prompt text provided.** Cannot score.

---

### V-05 — Combined: role sequence + format + enforcement

> **No prompt text provided.** Cannot score.

---

## Ranking (scoreable variations)

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | **V-02** — Strict Table Schema | **112** | Yes |
| 2 | V-01 — Role Sequence | 108 | Yes |
| 3 | V-03 — Conversational (truncated) | ~40 | No (C-05 fail) |
| — | V-04, V-05 | N/A | Not provided |

---

## Excellence Signals — What V-02 Does That V-01 Doesn't

**Signal 1: Schema encoding vs. instruction encoding for C-15**

V-01 has no mitigation type taxonomy at all. V-02 makes `Mitigation Type` an explicit table column with a named six-item taxonomy. When the type is a column, every row inherits the obligation structurally — the model cannot produce a complete table without filling it. Textual instruction ("each mitigation should name its type") can be silently ignored; a missing column cell cannot. This distinction explains the full +4 pts gap (C-15 + C-18).

**Signal 2: Post-table audit summary as a mandatory output artifact**

V-02 adds a required one-line post-table summary: "Mitigation types used: [list]. Count: [N]." This externalizes the C-18 diversity gate as a visible output the model must produce. The repair loop then has a named trigger ("If N < 3, return to main register and revise"). V-01 has no type audit at all — its back-pressure loop (C-20) covers interdependency count only. V-02 extends back-pressure to type diversity, creating a second self-healing gate.

**Remaining gap (both V-01 and V-02 miss)**

C-14 (IF-THEN syntactic form for likelihoods) is the sole aspirational miss for both top variants. A future variation should test whether explicitly requiring "IF [condition], THEN this risk activates" syntax in the likelihood column/field closes this last 2-point gap.

---

## New Patterns

Both patterns are grounded in V-02 vs. V-01 delta and represent structural observations not yet reified as rubric criteria:

1. **Column-schema encoding mechanically enforces field presence** — expressing a required output field as a named table column (rather than a prose instruction) eliminates voluntary-disclosure failure mode; the model cannot produce a schema-compliant table with a missing column

2. **Mandatory post-section audit summary externalizes gate outcomes** — requiring a visible one-line audit block after each quality gate (type count, interdependency count) creates an auditable output artifact; silent non-compliance becomes structurally impossible rather than merely discouraged

```json
{"top_score": 112, "all_essential_pass": true, "new_patterns": ["Column-schema encoding mechanically enforces field presence — expressing a required output field as a named table column eliminates voluntary-disclosure failure mode; the model cannot produce a schema-compliant table with a missing column", "Mandatory post-section audit summary externalizes gate outcomes — requiring a visible one-line audit block after each quality gate creates an auditable output artifact that makes silent non-compliance structurally impossible"]}
```
