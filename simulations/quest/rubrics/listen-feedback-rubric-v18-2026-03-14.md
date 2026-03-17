```markdown
# review-customers Rubric — v18

**v18 written.** Two new criteria extracted from Round 20 excellence signals:

---

**A-32 — CI formula enforcement stack complete: A-29 + A-30 + A-31 present simultaneously**
(depth, 5 pts)

Source: V-05 Round 20 Signal 1 — "Full structural enforcement stack eliminates independent
failure categories." Each of A-29, A-30, and A-31 closes one independent failure path for
CI formula omission:

- A-29 (output-format): formula absent from final report is caught — but does not prevent
  the formula from being added as retroactive output decoration after computation
- A-30 (derivation-phase): formula omitted at generation time is caught — but does not
  articulate why omission is detectable as a protocol error
- A-31 (failure mode at constraint): gap in epistemic grounding is closed — but does not
  itself enforce the formula at generation time or in output

When all three are present simultaneously, no independent failure path remains: a
protocol-follower cannot reach D.2 without the formula already stated at D.1 (A-30), cannot
report without the formula in output (A-29), and the constraint instruction itself explains
why omission is a verifiable error (A-31). Exactly two of the three still leaves one path
open — a protocol with A-30 and A-31 but not A-29 permits silent formula omission from the
report; a protocol with A-29 and A-31 but not A-30 permits the formula to appear as output
decoration computed independently of the derivation. The full stack makes compliance
verifiable at two independent checkpoints (generation and inspection) with the failure mode
explained in-line at the constraint itself.

Pass condition: protocol achieves A-29, A-30, and A-31 simultaneously. PARTIAL (3 pts) if
exactly two of the three are present. FAIL if fewer than two are present, or if A-32 is
evaluated on a protocol that has no CI formula enforcement mechanism at all.

---

**A-33 — Bilateral field system complete: A-16 + A-17 + A-21 + A-24 present simultaneously**
(depth, 5 pts)

Source: V-04/V-05 Round 20 bilateral completeness pattern. V-04 is the first variation to
achieve all four bilateral criteria simultaneously, reaching 226/245 — the highest among
V-01–V-04 — driven entirely by bilateral completeness. Each criterion closes one independent
failure path for bilateral analysis:

- A-16 (named sub-fields): prevents Field 1 from being undifferentiated prose — but does
  not enforce that both analysis directions (Gains and Losses) are present
- A-17 (bilateral coverage enforcement): prevents Field 2 without Field 3 — but does not
  require named sub-fields in Field 1, leaving Field 1 structure unconstrained
- A-21 (conjunctive framing): prevents each direction field from being completed without
  naming the other — but does not require named sub-fields in Field 1 or cross-referencing
  specific components
- A-24 (sub-field cross-reference): prevents completion without invoking specific named
  components of Field 1 — but is structurally unreachable unless A-16's named sub-fields
  exist (confirmed by V-02 Round 20: A-17 + A-21 present, A-16 absent → A-24 FAIL)

When all four are present simultaneously, the bilateral field system has structural
completeness: Field 1 has named sub-fields that Fields 2 and 3 must invoke (A-16 prerequisite
for A-24), Field 2 cannot be completed without Field 3 (A-17), and each direction field
explicitly names the other (A-21). The A-16 → A-24 prerequisite chain means bilateral
completion requirements also enforce Field 1 sub-field granularity as a structural side
effect — bilateral completeness and Field 1 specificity are not independently optimizable.

Pass condition: protocol achieves A-16, A-17, A-21, and A-24 simultaneously. PARTIAL (3 pts)
if exactly three of the four are present. FAIL if fewer than three are present.

---

**Score impact:** 31 → 33 aspirational criteria · 155 → 165 pts · max 245 → 255 pts

---

## Essential Criteria (output fails without these)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-01 | **12 persona cards present** | coverage | Output contains exactly 12 persona cards, one per customer persona (C-01 through C-12). Fewer than 12 cards is an automatic fail regardless of other criteria. |
| C-02 | **NPS score and justification per card** | correctness | Each persona card contains a predicted NPS score (1-10) and a 1+ sentence justification linking persona context to the score. |
| C-03 | **Severity-labeled feedback per card** | format | Each persona card lists feedback items with explicit severity labels (blocking / major / minor / cosmetic). At least one feedback item per card unless the persona has no objections, in which case the absence must be stated. |
| C-04 | **Aggregate NPS computed and threshold applied** | correctness | Output computes aggregate NPS as mean of all 12 persona scores. Explicitly states whether threshold of 7.0 is met or not. If below 7.0, output flags spec as needing revision. |
| C-05 | **Cross-persona theme matrix present** | format | Output includes a cross-persona theme matrix (table or equivalent) mapping recurring themes to the personas that raised them. At least one theme is identified. |

---

## Recommended Criteria (output is better with these)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| R-01 | **Blocking issues escalated** | behavior | Any `blocking` severity item is called out in a dedicated summary section (e.g., "Blockers requiring resolution") separate from the per-persona cards. Zero blocking items is acceptable — section may say "none." |

---

## Aspirational Criteria (depth and rigor signals)

PASS = 5 pts · PARTIAL = 3 pts · FAIL = 0 pts

### Foundational (A-01 through A-15, A-18–A-20, A-22–A-23, A-26, A-29)

All well-formed protocol variations are expected to achieve PASS on these criteria. Failure
on a foundational criterion indicates a structural deficit in the base protocol.

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| A-01 | **Persona card ID labeled** | format | Each card is explicitly labeled with its persona ID (C-01 through C-12); positional inference does not satisfy this criterion. |
| A-02 | **NPS scale anchored** | correctness | Output defines or references the 1–10 NPS scale; all scores are integers on the stated scale with no non-integer or out-of-range values. |
| A-03 | **Justification references persona context** | depth | Each NPS justification names a specific persona characteristic (role, workflow constraint, or adoption scenario) driving the predicted score. |
| A-04 | **Severity vocabulary consistent** | format | Only the four canonical labels (blocking / major / minor / cosmetic) appear as severity designators; variant labeling (e.g., "critical") fails. |
| A-05 | **Feedback items actionable** | specificity | Each feedback item names a specific behavior, interaction point, or feature — not a vague sentiment. "Confusing UI" fails; "Permission dialog blocks task completion without explanation" passes. |
| A-06 | **Aggregate NPS formula stated** | correctness | Output states the aggregate formula as "mean of N scores" (or equivalent) prior to reporting the value; a bare number without formula statement fails. |
| A-07 | **Threshold comparison explicit** | correctness | Output contains an explicit pass/fail determination against the 7.0 threshold ("7.3 >= 7.0: threshold met" or equivalent); an implied comparison fails. |
| A-08 | **Theme matrix contains 3+ themes** | coverage | Cross-persona theme matrix lists at least three distinct themes; one or two themes indicate insufficient cross-persona synthesis. |
| A-09 | **Each theme attributed to 2+ personas** | specificity | Every theme in the matrix is attributed to at least two persona cards; a finding attributed to only one card is a per-persona finding, not a cross-persona theme. |
| A-10 | **Blocking items justified** | completeness | Each blocking-severity item includes a one-sentence statement explaining why it is blocking rather than major; severity escalation without justification fails. |
| A-11 | **Score range spans 3+ distinct bands** | coverage | The 12 NPS scores span at least three distinct bands (e.g., <=4, 5–6, >=7) indicating genuine persona differentiation; all scores in a single band fails. |
| A-12 | **Persona cards in declared order** | format | Cards appear in C-01–C-12 order or in a declared alternate order stated at the top of the output; undeclared alternate ordering fails. |
| A-13 | **Section headers delineate output zones** | format | Output uses section headers or equivalent structural markers separating per-persona cards, aggregate analysis, theme matrix, and blocker summary. |
| A-14 | **Feedback items in complete sentences** | format | Each feedback item is a complete sentence (subject + behavior + impact); sentence fragments fail. |
| A-15 | **Aggregate NPS at 1+ decimal precision** | correctness | Aggregate NPS is reported to at least one decimal place (e.g., 7.3, not 7) enabling accurate threshold comparison; integer-only reporting fails. |
| A-18 | **Gains/losses fields explicitly labeled** | format | Fields for gains and losses analysis carry distinct, visible labels in output; positional inference (gains above losses by convention) does not satisfy this criterion. |
| A-19 | **Current approach field present** | format | Output includes a Current approach analysis field (Field 1) prior to gains/losses analysis; omitting the current-state baseline fails. |
| A-20 | **Recommendation field present** | format | Output includes a recommendation field (Field 4) synthesizing the bilateral analysis into a disposition; ending on gains/losses without synthesis fails. |
| A-22 | **Mutual reference uses exact field labels** | specificity | Conjunctive cross-references between direction fields use the exact field label names; pronoun-based references ("the other field") or paraphrases fail. |
| A-23 | **Field completion markers explicit** | format | Each field uses a structural completion marker (closing line, separator, or label) indicating the field is done before the next begins; unmarked run-on field transitions fail. |
| A-26 | **Persona influence weighting present** | depth | Output includes a weighting or influence mechanism indicating which personas carry more weight in the aggregate analysis (e.g., adoption-curve weighting, user-volume weighting); flat-weight aggregation with no weighting rationale fails. |
| A-29 | **CI formula present in output format** | correctness | Output includes the CI formula (+-1.96*SD/sqrt(N)) alongside the confidence interval value in the report; a bare interval without the formula parenthetical fails. |

---

### Differentiating (A-16, A-17, A-21, A-24–A-25, A-27–A-28, A-30–A-33)

These criteria distinguish depth and rigor across protocol variations. Partial credit (PARTIAL,
3 pts) reflects structural enforcement present without the highest-rigor property.

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| A-16 | **Structured 4-sub-field Current approach** | depth | Field 1 (Current approach) contains four named sub-fields: (1) What it delivers, (2) Where it falls short, (3) Floor-level switching cost, (4) Persona-specific workflow disruption. Unstructured prose in Field 1 fails; bilateral output structure without named Field 1 sub-fields fails. |
| A-17 | **Bilateral gains/losses coverage enforced** | depth | Protocol explicitly prohibits completing the Gains field without completing the Losses field (and vice versa); a protocol that allows one-sided analysis fails even if bilateral output sometimes occurs in practice. |
| A-21 | **Conjunctive framing: each field names the other** | depth | Gains field instruction explicitly names the Losses field and vice versa (conjunctive mutual reference by exact label); instructions referencing "the other direction" without naming it fail. |
| A-24 | **Field completion requires invoking named A-16 sub-field** | depth | Protocol requires Fields 2 and 3 to cross-reference specific named sub-fields from A-16's Field 1 structure; cross-reference to unnamed prose fields fails. A-16 is a structural prerequisite — A-24 cannot be satisfied without A-16. |
| A-25 | **UX-before-PM rationale co-located with ordering instruction** | depth | The ordering instruction placing UX review before PM review contains — within the same instruction step — the rationale explaining why this order prevents information contamination. Rationale appearing only in a separate section fails even if accurate. PARTIAL (3 pts) if structural ordering is present with rationale in a separate section; FAIL if ordering instruction is absent. |
| A-27 | **Failure mode annotation co-located with constraint** | depth | Each structural constraint instruction contains — within the same step — an explicit statement of the failure mode the constraint prevents. Failure mode appearing only in a separate rationale section fails. Directly parallels A-25 applied to constraints generally. PARTIAL (3 pts) if structural enforcement is present with failure mode in a separate section; FAIL if no failure mode analysis at all. |
| A-28 | **Directional sensitivity: upward/downward delta reported separately** | depth | NPS sensitivity analysis reports upward and downward score deltas as distinct labeled outputs ("Upward delta (+1): ..." and "Downward delta (-1): ...") enabling per-direction band-crossing detection. A symmetric +/-N figure that suppresses asymmetric band-crossing implications fails. |
| A-30 | **Derivation-phase protocol: CI formula enforced at generation time** | depth | Protocol contains a derivation phase (D.1 state formula -> D.2 compute SD -> D.3 apply -> D.4 report) where the CI formula is an explicit required step prior to computation. A protocol requiring the formula only at output inspection (A-29) but not at derivation time fails; formula omission must be structurally detectable before output exists. Pass requires a derivation phase with formula statement as an explicit required step prior to computation; an output-format instruction alone does not satisfy A-30. |
| A-31 | **CI formula failure mode named at point of constraint** | depth | The CI formula constraint instruction (whether derivation-phase, output-format, or both) contains an explicit statement of the failure mode prevented by requiring the formula: that without the formula parenthetical, a reader cannot verify whether the CI was computed via the correct method. Co-location required — failure mode appearing only in a separate section fails. Directly parallels A-25 applied to the CI formula constraint. |
| A-32 | **CI formula enforcement stack complete (A-29 + A-30 + A-31 simultaneously)** | depth | Protocol achieves A-29, A-30, and A-31 simultaneously, closing all three independent failure paths for CI formula omission: output-format requirement prevents formula absent from report (A-29), derivation-phase requirement prevents formula omitted at computation time (A-30), and co-located failure mode prevents gap in epistemic grounding (A-31). Achieving exactly two of the three still leaves one failure path open. Pass condition: all three present. PARTIAL (3 pts) if exactly two of A-29/A-30/A-31 are present. FAIL if fewer than two are present. |
| A-33 | **Bilateral field system complete (A-16 + A-17 + A-21 + A-24 simultaneously)** | depth | Protocol achieves A-16, A-17, A-21, and A-24 simultaneously, closing all four independent failure paths for bilateral analysis incompleteness: named sub-fields prevent undifferentiated Field 1 prose (A-16), bilateral coverage enforcement prevents one-sided analysis (A-17), conjunctive framing prevents each field from being completed without naming the other (A-21), and sub-field cross-reference requires invoking specific named components (A-24). The A-16 prerequisite chain means bilateral completeness also enforces Field 1 sub-field granularity. Pass condition: all four present. PARTIAL (3 pts) if exactly three of A-16/A-17/A-21/A-24 are present. FAIL if fewer than three are present. |

---

## Scoring Summary

| Source | Points |
|--------|--------|
| C-01 to C-05 (essential, 15 pts each) | 75 pts max |
| R-01 (recommended, 15 pts) | 15 pts max |
| A-01 to A-33 (aspirational, 5 pts each) | 165 pts max |
| **Total** | **255 pts max** |

PASS = 5 pts · PARTIAL = 3 pts · FAIL = 0 pts (aspirational)
```

---

Two criteria added:

**A-32** closes the "triple-lock" observation from Signal 1: each of A-29/A-30/A-31 independently leaves one failure path open; the complete stack leaves none. PARTIAL applies when exactly two of three are present.

**A-33** closes the bilateral completeness pattern visible in V-04/V-05 Round 20 scoring: A-24's A-16 dependency means the four bilateral criteria form a closed system — you cannot satisfy the cross-reference requirement without the named sub-fields that make cross-referencing meaningful. PARTIAL applies when exactly three of four are present.

Score impact: 31 → 33 aspirational · 155 → 165 pts · max 245 → **255 pts**.
