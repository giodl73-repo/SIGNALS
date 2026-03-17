Reading the scorecard carefully for patterns not yet encoded, then writing v5.

**Patterns extracted from Round 4:**

1. **V-02 vs V-03 divergence on C-16** — V-02 PASSES C-16 via a *prospective* coverage matrix declared before stage execution; V-03 gets PARTIAL because its audit table is retrospective. The rubric encodes C-16 as a completeness requirement but doesn't distinguish between pre-committed and post-hoc verification. A retrospective audit allows performative filling; a prospective matrix makes gaps structurally unambiguous. This is C-17.

2. **V-04's preamble structure** — V-04 places CALIBRATION, FALSIFICATION, ATTRIBUTION, and SEQUENCING at the same rule tier. C-13 requires named rules declared and invoked. C-15 requires SEQUENCING specifically to be formalized. Neither requires that all declared rules occupy *peer tier* in the preamble — a brief could satisfy both by declaring SEQUENCING as a first-class rule while leaving CALIBRATION embedded as a prose note. V-04's distinguishing move is rule parity: any reader can cite any rule by identifier without knowing which were "originally" primary. This is C-18.

Denominator: 9 → 11.

---

```markdown
---
skill: quest-rubric
skill_target: campaign-evidence
date: 2026-03-16
version: 5
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

---

## Scoring

```
composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/11 * 10)
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

**What changed from v4 → v5:**

**C-17** encodes the V-02 vs V-03 divergence. Both attempt C-16 compliance; V-02 passes and V-03 is partial. The distinguishing factor is timing: V-02's matrix pre-commits stage assignments before execution, making gaps structurally visible; V-03's audit table is retrospective, leaving room for performative completion. C-17 isolates prospective commitment as a separate, independently-testable property — a brief can satisfy C-16 (no actual gaps) while failing C-17 (commitment came after the fact).

**C-18** encodes the V-04 preamble architecture. C-13 requires named rules declared and invoked. C-15 requires SEQUENCING to be formalized as a rule. Neither requires that all declared rules stand at equal tier. V-04's preamble achieves structural parity: CALIBRATION, FALSIFICATION, ATTRIBUTION, and SEQUENCING each appear as a peer-level named rule, making the rule system flat and fully traversable by identifier. The test embedded in C-18 — "remove all rule labels; if the resulting prose treats any rule's content differently, parity is absent" — gives an operational check that doesn't require judging intent.
