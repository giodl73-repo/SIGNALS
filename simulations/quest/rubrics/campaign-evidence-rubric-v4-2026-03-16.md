Scanning the scorecard for patterns that appear in the highest-scoring variates but aren't yet encoded as criteria.

**V-04 excellence patterns not yet captured:**

1. **SEQUENCING elevated to a named rule** — V-04 declares four rules at the preamble (CALIBRATION, FALSIFICATION, ATTRIBUTION, SEQUENCING), putting the evidence-first decision on the same footing as the other governance rules. C-10 requires the reordering; C-14 requires stating why; but neither requires *formalizing the sequencing decision as a named, referenceable rule*. V-02 and V-03 treat sequencing as a structural choice — V-04 treats it as a rule that can be invoked by identifier at every affected stage.

2. **Zero-gap rule invocation** — V-04's C-13 evidence: "No rule applied silently at any stage." V-02 and V-03 earn PARTIAL on C-13 because they declare rules at the preamble but invoke them only at synthesis. C-13 requires declaration + invocation at point of use, but the partial scores show that C-13 can be satisfied incompletely. The stronger pattern is *complete coverage* — every applicable stage carries the relevant invocation tag with no gaps. This is a completeness criterion that C-13 doesn't fully enforce.

These become C-15 and C-16. Aspirational pool goes from 7 to 9, denominator updates accordingly.

---

```markdown
---
skill: quest-rubric
skill_target: campaign-evidence
date: 2026-03-16
version: 4
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

---

## Scoring

```
composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/9 * 10)
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

Two criteria added, one formula change:

- **C-15** captures the V-04 pattern of promoting the sequencing decision from unnamed structural convention to a declared, referenceable rule. C-10 requires the reordering; C-14 requires stating why; C-15 requires treating *that why* as a first-class rule that sits in the preamble and can be cited by identifier at each governed stage. The distinction from C-14 is architectural: C-14 is about encoding a rationale sentence, C-15 is about whether the sequencing principle has a name and a formal place in the rule system.

- **C-16** captures the completeness gap that C-13 alone doesn't enforce. V-02 and V-03 earn PARTIAL on C-13 by invoking rules at synthesis but not at intermediate stages. C-16 closes that gap: every stage where a rule applies carries an explicit tag, no exceptions. The criterion makes zero-gap invocation its own bar rather than leaving it as the strongest interpretation of C-13.

- Formula denominator: `7 → 9` for the aspirational tier.
