Reading the Round 5 scorecard for patterns not yet encoded, then writing v6.

**Patterns extracted from Round 5:**

1. **V-02's coverage map immutability declaration** — V-02 earns the strongest C-17 signal with: *"This map is finalized before Stage 1 begins. It cannot be modified after any stage executes. A coverage audit populated after all stages complete is not a commitment; it is a record. This is a commitment."* C-17 requires prospective declaration but is silent on immutability. A map declared in advance but lacking a formal lock can be post-hoc adjusted without detectable violation. The explicit lock — stating that modification after execution begins is prohibited — makes tampering structurally visible. This is C-19.

2. **V-03's `[invoked at: ...]` inline annotation format** — V-03 embeds stage applicability scope directly in each rule declaration (`CALIBRATION RULE [...] [invoked at: Stage 4, Stage 5]`) rather than in a separate coverage table. C-17 allows "equivalent structure" and a separate map satisfies it. But the inline form is architecturally tighter: you cannot read the rule without reading its scope, and the map cannot drift from the rules it describes. A separate coverage table is a document that references the rules; inline annotations make coverage inseparable from rule identity. This is C-20.

3. **V-01's interrogative invocation form** — V-01 invokes CALIBRATION at synthesis as: `CALIBRATION RULE invoked: two distinct confidence levels present above?` C-16 requires invocation at every applicable stage but is silent on form. A passive tag (`CALIBRATION RULE invoked`) signals the rule was remembered; an interrogative tag compels a binary answer and makes non-compliance structurally visible — the executor cannot mark the field without answering the question. This is C-21.

Denominator: 11 → 14.

---

```markdown
---
skill: quest-rubric
skill_target: campaign-evidence
date: 2026-03-16
version: 6
---

# Rubric: campaign-evidence

Evaluates whether the skill ran the full evidence campaign and produced a complete evidence brief with confidence levels and falsification status.

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

---

## Scoring

```
composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/14 * 10)
```

**Golden threshold**: all 4 essential pass AND composite ≥ 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | ≥ 80, all essential | Ship-ready output |
| Silver | ≥ 60, all essential | Usable with gaps |
| Bronze | all essential pass | Minimum viable brief |
| Fail | any essential miss | Not useful |
```

---

**What changed from v5 → v6:**

- **C-19** — Coverage map immutability explicitly declared. Sourced from V-02's lock language: *"It cannot be modified after any stage executes."* C-17 requires prospective declaration but permits a map with no formal lock; C-19 requires the immutability constraint be stated explicitly, making the map a commitment rather than a document.

- **C-20** — Rule scope embedded inline in rule declaration. Sourced from V-03's `[invoked at: ...]` annotation format. C-17's "equivalent structure" language was satisfied by a separate coverage table; C-20 closes the gap by requiring scope be part of the rule body itself, so coverage and rule identity cannot drift.

- **C-21** — Interrogative invocation at critical rules. Sourced from V-01's `CALIBRATION RULE invoked: two distinct confidence levels present above?` pattern. C-16 requires invocation at every applicable stage but is silent on form; C-21 requires at least one critical invocation be expressed as a yes/no verification question, turning a passive tag into a structural compliance test.

Denominator: 11 → 14.
