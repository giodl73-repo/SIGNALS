Reading the Round 6 scorecard for patterns not yet encoded in v6.

**Patterns extracted from Round 6:**

**V-01's universal binary invocation format** — V-01 earns the strongest C-21 signal by applying binary `[ Yes / No ]` form to every rule invocation, not only the critical ones: ATTRIBUTION, SEQUENCING, CALIBRATION, FALSIFICATION all carry the checkbox. C-21 requires interrogative form at "at least one critical rule" — a minimum that leaves attribution and sequencing invocations as passive tags. Extending binary form universally means any rule invocation can fail visibly, not just the designated critical ones. The governance system becomes uniformly verifiable rather than selectively verifiable. This is C-22.

**V-03's stage-indexed invocation trail** — V-03 appends `[Stage N of 5]` to every invocation tag. C-16 requires zero-gap invocation coverage but does not specify how a reader verifies completeness — verification requires reading every stage and matching each to the coverage map. The `[Stage N of 5]` suffix makes completeness verifiable by arithmetic: a reader can count invocations for a given rule, compare to the denominator, and detect any silent gap without parsing the full brief. The completeness claim becomes a countable assertion rather than an interpretive one. This is C-23.

**V-04's per-stage entry and exit conditions** — V-04 attaches explicit entry/exit conditions to all five stages. Entry conditions declare what must be true before a stage may execute (preventing premature advancement); exit conditions declare what the stage must produce before the next stage may begin (preventing partial completion). Stage sequencing governed only by narrative order can be silently violated — a stage that technically appears in the output may have run with missing inputs or incomplete outputs. Formal entry/exit conditions make each stage boundary a verifiable gate, not a convention. This is C-24.

Denominator: 14 → 17.

---

```markdown
---
skill: quest-rubric
skill_target: campaign-evidence
date: 2026-03-16
version: 7
---

# Rubric: campaign-evidence

Evaluates whether the skill ran the full evidence campaign and produced a complete
evidence brief with confidence levels and falsification status.

---

## Essential Criteria (60 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **All five prove skills executed** | behavior | Output shows evidence from all five stages: prove-hypothesis, prove-websearch, prove-intelligence, prove-analysis, prove-synthesize — each contributes a named section or labeled artifact block. Missing any one stage fails. |
| C-02 | **Confidence level assigned per finding** | correctness | Every significant finding carries an explicit confidence level (e.g., High / Medium / Low or numeric) — not a single summary rating but per-claim labels. At least 3 distinct findings must carry individual confidence ratings. |
| C-03 | **Falsification status declared** | correctness | The brief includes a falsification section or per-hypothesis status — at minimum "supported", "refuted", or "indeterminate" for each hypothesis. A brief with no falsification status at all fails. |
| C-04 | **Evidence brief is self-contained** | format | The output is a single coherent document (not a collection of raw dumps). It has a title, topic context, and synthesized narrative — a reader unfamiliar with the run can understand what was investigated and what was found. |

## Recommended Criteria (30 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Source attribution per claim** | depth | Claims are linked to their source stage (e.g., "per web search", "per intelligence review"). At least 70% of material claims carry stage attribution. |
| C-06 | **Synthesis section distinguishes consensus from conflict** | depth | The synthesize stage output explicitly identifies where prove-websearch and prove-intelligence agree vs. diverge, not just lists findings side-by-side. |
| C-07 | **Confidence levels are calibrated, not uniform** | correctness | Confidence ratings vary across findings — a brief where every finding is "Medium" fails this criterion. Distribution must show at least two distinct levels used meaningfully. |

## Aspirational Criteria (10 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Gaps and open questions surfaced** | coverage | The brief closes with an explicit list of what remains unknown or under-evidenced after the full campaign, enabling a follow-up investigation to pick up cleanly. |
| C-09 | **Decision readiness signal included** | behavior | The brief includes a final verdict on whether the evidence is sufficient to proceed (e.g., "Ready to commit", "Needs more investigation on X") — not just findings but an actionable posture statement. |
| C-10 | **Hypotheses declared post-evidence** | correctness | Hypotheses are finalized or formally stated *after* the web search and intelligence stages complete — not pre-committed before evidence gathering. Falsification decisions grounded in actual findings rather than confirmed against pre-anchored assumptions. A campaign that states hypotheses only in prove-hypothesis *before* any evidence gathering fails this criterion. |
| C-11 | **Explicit calibration anti-pattern guard** | correctness | The brief or its process includes an explicit check against uniform confidence ratings — e.g., a stated rule or reviewer note that "if all findings carry the same confidence level, calibration is insufficient." A bare scale definition without an anti-uniformity guard does not pass. |
| C-12 | **Decision readiness compressed to a single verdict sentence** | behavior | The decision readiness signal (C-09) is expressed as one actionable sentence that names a posture and, if not ready, names the specific gap — e.g., "Ready to proceed" or "Needs more investigation on regulatory approval timeline before committing." Multi-paragraph readiness discussions do not pass; the compression itself is the signal. |
| C-13 | **Named rules declared at preamble and invoked at point of use** | correctness | The brief's governing rules (falsification, attribution, calibration) are declared as named identifiers in a preamble or header block and then explicitly invoked by name at the step where they apply — not only embedded as inline prose warnings. A brief with unnamed in-place notes but no declared rule identifiers does not pass. |
| C-14 | **Hypothesis reordering rationale stated** | correctness | When the campaign places hypothesis declaration after evidence gathering (C-10), the brief explicitly states *why* — a rationale sentence such as "A hypothesis anchored before evidence gathering is a bias, not a hypothesis." Passing C-10 by reordering stages without encoding the underlying principle does not pass this criterion. |
| C-15 | **Evidence-first sequencing formalized as a named rule** | correctness | When the campaign uses evidence-first ordering (C-10), the sequencing decision is declared as a named rule (e.g., SEQUENCING RULE) in the preamble alongside the other governance rules — not left as an unnamed structural convention. The rule must be referenceable by identifier at each stage it governs. An evidence-first campaign where the sequencing choice is structural but unnamed does not pass; the decision must be promotable to a rule that any reader can cite by name. |
| C-16 | **Zero-gap rule invocation — no applicable stage left untagged** | correctness | Every declared governance rule is invoked by name at every stage where it applies — no stage silently applies a rule without an explicit invocation tag. A brief where rules are declared at the preamble but invoked only at synthesis, or invoked at some applicable stages but not all, does not pass. Full invocation coverage means: ATTRIBUTION at every evidence-gathering stage, CALIBRATION at analysis and synthesis, FALSIFICATION at hypothesis declaration and synthesis, SEQUENCING at every stage whose ordering the rule governs. |
| C-17 | **Coverage mapping declared prospectively, before stage execution** | correctness | The rule-to-stage coverage map (or equivalent structure) is declared at the brief's outset — before any evidence stage runs — committing to which rules apply at which stages. A coverage audit assembled retrospectively after all stages complete does not pass; the commitment must precede execution so gaps cannot be concealed by post-hoc fills. A pre-declared matrix where any cell can be verified against actual stage output passes; an audit table populated after the fact does not. |
| C-18 | **All governance rules occupy peer tier in preamble** | correctness | Every declared governance rule appears at the same structural tier in the preamble — none elevated as primary while others are demoted to secondary notes or inline prose. A preamble that lists CALIBRATION, FALSIFICATION, and ATTRIBUTION as named rules but embeds SEQUENCING only as a structural convention, or vice versa, does not pass. Rule parity means any reader can cite any rule by identifier without needing to know which rules were originally primary. The test: remove all rule labels — if the resulting prose treats any rule's content differently from the others, parity is absent. |
| C-19 | **Coverage map immutability explicitly declared** | correctness | The coverage map includes an explicit statement that it is finalized before Stage 1 begins and cannot be modified after any stage executes. C-17 requires prospective declaration but is silent on immutability; a map created in advance but lacking a formal lock can be silently adjusted post-hoc without detectable violation. The immutability declaration — distinguishing a commitment from a record — makes tampering structurally visible. A prospective coverage map that does not include an explicit "cannot be modified after execution begins" clause does not pass. |
| C-20 | **Rule scope embedded inline in rule declaration** | correctness | Each governance rule declaration includes its stage applicability scope as an inline annotation (e.g., `[invoked at: Stage 1, Stage 2, Stage 5]`) within the rule body itself — not as a separate coverage table that references the rules from a distance. A separate coverage map satisfies C-17 but allows the map and the rules to drift independently; inline scope annotations make coverage inseparable from rule identity. A brief where any rule's applicability scope is declared only in a separate block, not within the rule declaration, does not pass. |
| C-21 | **Interrogative invocation at critical rules** | correctness | At least one critical governance rule (CALIBRATION or FALSIFICATION) is invoked at its most critical stage via a verification question rather than a passive tag — e.g., `CALIBRATION RULE invoked: two distinct confidence levels present above?` A passive invocation tag signals the rule was remembered; an interrogative tag compels a binary answer and makes non-compliance structurally visible — the executor cannot close the field without answering. A brief where all rule invocations are passive tags, with no stage carrying an interrogative verification form, does not pass. |
| C-22 | **Universal binary invocation format across all rules** | correctness | Every governance rule invocation — not only CALIBRATION and FALSIFICATION but also ATTRIBUTION and SEQUENCING — uses a binary yes/no verification form (e.g., `[ Yes / No ]`). C-21 requires interrogative form at least one critical rule; this criterion extends the requirement universally. The distinction: selective binary invocation leaves attribution and sequencing gaps addressable via passive tags; universal binary form means any invocation of any rule can fail visibly. A brief where any rule invocation at any applicable stage uses a passive tag rather than a binary verification does not pass. |
| C-23 | **Stage-indexed invocation trail** | correctness | Every rule invocation carries a stage-index suffix (e.g., `[Stage N of 5]`) making the invocation trail countable and auditable. C-16 requires zero-gap coverage but does not specify how completeness is verified — without indexing, a reader must parse every stage and cross-reference the coverage map to detect a gap. Stage-indexed invocations make completeness verifiable by arithmetic: count invocations per rule, compare to the declared denominator, identify any missing stage without interpretation. A brief satisfying C-16 by narrative convention but lacking stage-index suffixes does not pass; the countability itself is the signal. |
| C-24 | **Per-stage entry and exit conditions declared** | correctness | Each of the five evidence stages carries an explicit entry condition (what must be true before the stage may execute) and an exit condition (what the stage must produce before the next stage may begin). Stage sequencing governed only by narrative order or rule invocations can be silently violated — a stage appearing in output may have run with missing inputs or produced incomplete output. Formal entry/exit conditions make each stage boundary a verifiable gate: entry conditions prevent premature advancement; exit conditions prevent partial completion. A brief where any stage lacks both an entry condition and an exit condition does not pass. |

---

## Scoring

```
composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/17 * 10)
```

**Golden threshold**: all 4 essential pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | >= 80, all essential | Ship-ready output |
| Silver | >= 60, all essential | Usable with gaps |
| Bronze | all essential pass | Minimum viable brief |
| Fail | any essential miss | Not useful |
```
