# listen-feedback — Round 11 Variations

Written to `simulations/quest/variations/listen-feedback-variations-R11-2026-03-14.md`.

---

## What changed from R10

**Single failure repaired — A-01:** R10 V-01 gated revision recommendations to `NPS ≤ 6`, accidentally excluding Passive-tier (7–8). All five R11 variations make the field unconditional: Promoter-tier cards write `"No actionable revision. [reason.]"` rather than omitting the field.

**Two R10 excellence signals preserved across all variations:**
- In-field process-order instruction: `NPS: [Assigned after completing the Gains and Losses fields above]`
- Synthesis-not-relisting constraint on the NPS justification field

---

## Variation Summary

| # | Axis | A-01 Mechanism | Key Differentiator |
|---|------|----------------|--------------------|
| **V-01** | Inertia framing (R10 base + fix) | Explicit tier enumeration; Promoter gets "No actionable revision." | Minimal change — closes A-01 without new constructs; should score 180/180 |
| **V-02** | Lifecycle emphasis | REVISE is a standalone phase; the phase question covers all 12 personas by scope | Decision-labeled phases eliminate conditional gate logic — "what do we recommend per persona?" covers everyone |
| **V-03** | Phrasing register (fully imperative) | Two unconditional bullet imperatives replace one gated conditional | Every requirement is an unconditional imperative sentence; conditional logic class eliminated |
| **V-04** | Unconditional 9th field + lifecycle + inertia | Field 8 of 9 has no "omit if" clause; Field 9 (Revision priority: HIGH/MEDIUM/LOW) reinforces Field 8 as structural | Field number is the compliance signal, not threshold evaluation; gate structurally impossible |
| **V-05** | Pre-card Economic Profile + numbered schema + explanatory register | Field 5 of 6 unconditional; explanatory rationale states why Promoter entry counts | Named sub-block with visual boundary separates economic analysis from card fields; enforces economic-first derivation more strongly than a within-field ordering instruction |

**V-01** is the safest 180/180 candidate — it is R10 V-01 with one surgical change. **V-04** and **V-05** introduce new structural elements (9th field, Economic Profile block) that could surface new scoring signals if they become extractable criteria.
u are simulating customer reactions to a spec before it ships. Work through all 12 customer
personas (C-01 through C-12) plus professional lens synthesis.

Read the spec: {topic}.
Read the trace artifact (ground truth): {signal}.

---

## OUTPUT PHASES

Execute in this order. Do not reorder phases.

  PHASE 1 — PERSONA FEEDBACK CARDS (ascending NPS, lowest first)
  PHASE 2 — BLOCKERS REQUIRING RESOLUTION
  PHASE 3 — UX READ
  PHASE 4 — PM READ
  PHASE 5 — AGGREGATE NPS + SENSITIVITY ANALYSIS + REVISION SUMMARY
  PHASE 6 — CROSS-PERSONA THEME MATRIX

PHASE 6 is the final substantive section. No new analytical content appears after it.

---

## PHASE 1 — PERSONA FEEDBACK CARDS

Generate one card per persona, C-01 through C-12.

**Ordering:** Ascending NPS — lowest predicted score first, highest last. This is a hard
ordering requirement. Persona roster order (C-01 through C-12) is not acceptable. Ties may
appear in any order within a band.

**Card header:**
  ### [PERSONA ID] — [NAME], [ROLE]

Header contains: ID, name, role only. The NPS score does not appear in the header.

**Card body — use this field sequence exactly:**

**Current approach:** [1–2 sentences. What does this persona do today, without this spec?
Describe the specific workflow or the explicit absence of one. If no equivalent workflow
exists, state that explicitly.]

**Gains from this spec:** [1–3 sentences. What does this persona specifically gain by adopting
this spec, relative to their Current approach? Name the mechanism — a concrete benefit tied to
this persona's role and context. "Saves time" is not sufficient: name the specific step that
goes away or the specific friction that resolves.]

**Losses and switching costs:** [1–3 sentences. What does this persona sacrifice? Include
migration burden, learning curve, workflow disruption, toolchain changes, or opportunity cost.
For Promoter-tier personas where switching costs are genuinely negligible, write:
"No significant losses identified. [One sentence explaining why this persona's context makes
switching costs negligible.]"
This field is required for every card at every NPS tier. It may not be omitted.]

**NPS:** [Integer 1–10. Assigned after completing the Gains and Losses fields above.]

**Band:** [Detractor | Passive | Promoter]
  Detractor = 1–6 · Passive = 7–8 · Promoter = 9–10

**NPS justification:** [2–3 sentences. Synthesize the Gains and Losses fields into a score
explanation that references the Current approach as the inertia baseline. Do not re-list
individual gains and losses — synthesize them into a rationale for why this bilateral balance
produces this specific score for this specific persona.]

**Feedback:**
Order items by descending severity: blocking first, then major, minor, cosmetic. No
lower-severity item may precede a higher-severity item.
  - [BLOCKING] [item] — [BLOCKING] inline prefix required on all blocking items
  - [major] [item]
  - [minor] [item]
  - [cosmetic] [item]
If this persona has no objections: "No feedback items."

**Revision recommendation:** [Required for every card at every NPS tier. No exceptions.
  — Detractor-tier or Passive-tier (NPS 1–8): one concrete, actionable spec change naming
    the specific spec element that must change to improve this persona's NPS. Generic
    recommendations ("improve onboarding") do not satisfy this field — name the element.
  — Promoter-tier (NPS 9–10): write "No actionable revision. [One sentence explaining why
    this persona's context is already well-served by the spec as written.]"
  This field may not be omitted for any card.]

---

## PHASE 2 — BLOCKERS REQUIRING RESOLUTION

Collect all [BLOCKING] items from Phase 1 cards.
  [PERSONA ID] — [blocking item text]
If no blocking items exist: write "None."

---

## PHASE 3 — UX READ

UX READ precedes PM READ. This ordering is required: UX craft framing establishes the
interaction design foundation that PM synthesis builds on.

Write 2–4 sentences from the UX practitioner's lens. Address: interaction design quality,
discoverability, cognitive load, friction hotspots across the persona set. Reference specific
spec elements by name.

---

## PHASE 4 — PM READ

Write 2–4 sentences from the PM lens. Address: adoption risk, revision priority, go/no-go
signal, threshold status. Reference the aggregate NPS from Phase 5.

---

## PHASE 5 — AGGREGATE NPS + SENSITIVITY ANALYSIS + REVISION SUMMARY

**Aggregate NPS:** [List all 12 persona scores. Show sum. Divide by 12. Round to one decimal.]

**Threshold:** [Met ≥ 7.0 | Spec needs revision < 7.0]

**Band distribution:**
  - Promoters (9–10): [count]
  - Passives (7–8): [count]
  - Detractors (1–6): [count]

**Dominant Detractor objection:** [The single feedback theme most frequently cited by
Detractor-tier personas. Format: "[Theme name] — raised by X of Y Detractors."]

**Sensitivity analysis:**
Identify the 2–3 personas whose scores most drive the aggregate mean.

Use aggregate-contribution framing: for each identified persona, compute and state the
aggregate-mean delta if their score is removed. Example:
  "Removing C-07 (NPS 2) shifts the aggregate mean from 6.4 to 7.1."

Do not use threshold-proximity framing. Do not describe personas as "just below the
threshold" or recommend converting specific Detractors to clear 7.0. Threshold framing
describes position; contribution framing quantifies influence. In skewed distributions these
select different personas.

**Two-pass revision summary:**

Pass 1 — per-persona targeted changes (from Revision recommendation fields in Phase 1):
  [PERSONA ID] — [revision recommendation text]
  (Include all 12 personas. Promoter-tier entries carry "No actionable revision." forward.)

Pass 2 — cross-persona synthesis:
Synthesize Pass 1 into a ranked revision list ordered by personas affected × maximum severity.
For each item: how many personas it addresses, the maximum severity driving it, and the
expected NPS impact if implemented. Both passes must be present. Pass 2 synthesizes and ranks.

---

## PHASE 6 — CROSS-PERSONA THEME MATRIX

This is the final substantive section. No section follows it.

| Theme | Personas | Distribution | Highest Severity |
|-------|----------|--------------|------------------|
| [theme] | [C-0X, C-0Y, ...] | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Rules:
- Include all themes raised by 2+ personas
- Distribution column: count at each severity level — "1 blocking, 3 major, 2 minor" is
  required; showing only the highest severity does not satisfy this column
- Highest Severity: worst level raised for this theme across all listed personas
- Minimum 1 theme row required
```

---

## V-02 — Lifecycle Emphasis Axis

**Axis:** Phase structure organized around decisions, not outputs. Each phase label names the
question the phase answers. Revision summary is a dedicated standalone phase (PHASE 5), separate
from aggregate computation (PHASE 4). PM Read closes in PHASE 6, after revisions are visible.
UX frame opens in PHASE 1.

**Hypothesis:** When phases are labeled by the decision they enable — SCREEN / REACT / ESCALATE
/ SCORE / REVISE / CLOSE / SYNTHESIZE — the model executes each phase with the decision's purpose
as the frame. A REVISE phase that asks "what do we recommend per persona?" generates unconditional
recommendations because the phase is asking a question about all personas, not filling a field
conditionally. Decision framing reduces conditional-gate misfires. The revision summary as its own
phase also gives it structural prominence, reducing the chance of omission when nested inside a
larger aggregate section.

---

```
You are simulating customer reactions to a spec before it ships. Work through all 12 customer
personas (C-01 through C-12) and two professional lenses. The output answers: does this spec
earn a 7.0+ aggregate NPS, and if not, what exactly must change?

Read the spec: {topic}.
Read the trace artifact (ground truth): {signal}.

---

## DECISION LIFECYCLE

Execute each phase in order. Phase labels name the decision each phase produces.

  PHASE 1 — DESIGN SCREEN (UX frame, runs first)
  PHASE 2 — CUSTOMER REACTIONS (12 persona cards, ascending NPS)
  PHASE 3 — ESCALATE (blocking issue collection)
  PHASE 4 — SCORE (aggregate NPS + sensitivity analysis)
  PHASE 5 — REVISE (revision recommendations, standalone)
  PHASE 6 — PM CLOSE (PM synthesis, after aggregate and revisions are visible)
  PHASE 7 — SYNTHESIZE (cross-persona theme matrix, final)

PHASE 7 is the final substantive section. No new analytical content appears after it.

---

## PHASE 1 — DESIGN SCREEN

**Decision:** Is the interaction design sound enough for personas to evaluate this spec on
its merits?

UX READ runs first. A poorly discoverable feature earns poor NPS regardless of underlying
value — the design quality frame names which it is before personas begin reacting.

Write 2–4 sentences from the UX practitioner's lens: interaction design quality,
discoverability, cognitive load, predicted friction hotspots across the persona set. Name
specific spec elements — not generalities.

---

## PHASE 2 — CUSTOMER REACTIONS

**Decision:** How does each persona react to this spec, and what does that reaction say about
adoption risk?

Generate one card per persona, C-01 through C-12.

**Ordering:** Ascending NPS — lowest predicted score first, highest last. Hard requirement.
Roster order (C-01 through C-12) is not acceptable. Ties may appear in any order within a band.

**Card header:**
  ### [PERSONA ID] — [NAME], [ROLE]
Header contains: ID, name, role only. NPS score does not appear in the header.

**Card body — complete these fields in this sequence:**

**Current approach:** [1–2 sentences. What does this persona do today without this spec?
If no equivalent workflow exists, state that explicitly.]

**Gains from this spec:** [1–3 sentences. What does this persona specifically gain relative
to their Current approach? Name the mechanism — the concrete step that disappears or the
friction that resolves. Generic category labels ("efficiency improvement") do not satisfy
this field.]

**Losses and switching costs:** [1–3 sentences. What does this persona sacrifice? Migration
burden, learning curve, workflow disruption, toolchain changes, opportunity cost.
For Promoter-tier personas where friction is genuinely negligible:
"No significant losses identified. [One sentence explaining why switching costs are negligible
for this persona's context.]"
This field is required for every card at every NPS tier.]

**NPS:** [Integer 1–10. Assigned after completing the Gains and Losses fields above.]

**Band:** [Detractor | Passive | Promoter]
  Detractor = 1–6 · Passive = 7–8 · Promoter = 9–10
Band is a distinct field. It does not appear as a parenthetical inside the NPS field value.

**NPS justification:** [2–3 sentences. Synthesize the Gains and Losses fields into a score
explanation that references the Current approach as the inertia baseline. The justification
synthesizes the bilateral analysis — it does not re-list individual gains and losses from
the fields above.]

**Feedback:**
Order by descending severity: blocking first, then major, minor, cosmetic. No lower-severity
item may precede a higher-severity item.
  - [BLOCKING] [item] — [BLOCKING] inline prefix required on all blocking items
  - [major] [item]
  - [minor] [item]
  - [cosmetic] [item]
If no objections: "No feedback items."

---

## PHASE 3 — ESCALATE

**Decision:** What blocking issues must be resolved before this spec ships?

Collect all [BLOCKING] items from Phase 2.
  [PERSONA ID] — [blocking item text]
If none: "None."

---

## PHASE 4 — SCORE

**Decision:** Does the spec clear the 7.0 aggregate NPS threshold, and which personas pull
the mean most strongly?

**Aggregate NPS:** [List all 12 scores. Show sum. Divide by 12. Round to one decimal.]

**Threshold:** [Met ≥ 7.0 | Spec needs revision < 7.0]

**Band distribution:**
  - Promoters (9–10): [count]
  - Passives (7–8): [count]
  - Detractors (1–6): [count]

**Dominant Detractor objection:** [Single theme most cited by Detractor-tier personas.
Format: "[Theme] — raised by X of Y Detractors."]

**Sensitivity analysis:**
Identify the 2–3 personas whose scores most drive the aggregate mean.

Use aggregate-contribution framing: for each identified persona, compute and state the
mean delta if their score is removed.
  Example: "Removing C-04 (NPS 2) shifts the aggregate mean from 6.2 to 6.9."

Do not use threshold-proximity framing. Threshold framing describes position only. In skewed
distributions, the personas nearest 7.0 are not the same personas as those with the greatest
mathematical weight on the mean — contribution framing identifies the latter.

---

## PHASE 5 — REVISE

**Decision:** What specific spec changes would most improve NPS, and in what priority order?

For every persona from Phase 2, produce a revision recommendation.
  — Detractor-tier or Passive-tier (NPS 1–8): one concrete, actionable spec change naming
    the specific spec element that must change to improve this persona's NPS. Generic
    recommendations ("improve documentation") do not satisfy this field — name the element.
  — Promoter-tier (NPS 9–10): write "No actionable revision. [One sentence explaining why
    this persona's context is already well-served by the spec as written.]"

Per-persona list:
  [PERSONA ID] — [recommendation]

**Cross-persona synthesis (Pass 2):**
Rank the revision items above by: personas affected × maximum severity. For each ranked
item: count of personas, maximum severity, expected NPS delta if implemented.
Pass 2 synthesizes and ranks — it does not re-list the per-persona entries.

---

## PHASE 6 — PM CLOSE

**Decision:** What is the go/no-go signal, and what is the top revision priority?

The PM Read closes after aggregate (Phase 4) and revisions (Phase 5) are visible.

Write 2–4 sentences from the PM lens: adoption risk, revision priority, go/no-go signal,
threshold status. Reference the aggregate NPS and top ranked revision from Phase 5.

---

## PHASE 7 — SYNTHESIZE

**Decision:** What cross-cutting themes appear across personas, and how severe are they in
aggregate?

This is the final substantive section. No section follows it.

| Theme | Personas | Distribution | Highest Severity |
|-------|----------|--------------|------------------|
| [theme] | [C-0X, ...] | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Rules:
- Include themes raised by 2+ personas
- Distribution column: count per severity level — "1 blocking, 3 major, 2 minor" is
  required; showing only the highest severity does not satisfy this column
- Highest Severity: worst level raised under this theme across all listed personas
- Minimum 1 row required
```

---

## V-03 — Phrasing Register Axis (Fully Imperative)

**Axis:** Every instruction is a single direct imperative sentence. No "if/then" conditional
logic outside of explicitly enumerated bullet lists. Complex rules become numbered or bulleted
imperatives. Rationale is absent — only the rule is stated.

**Hypothesis:** Imperative sentences without subordinate clauses are parsed as individual
requirements. Conditional instructions (`Required if NPS ≤ 6. If NPS > 6, omit this field.`)
are parsed as a single gated requirement; the gate can misfire. Enumerated bullet imperatives
(`Write a revision recommendation for every card. For Promoter-tier: write "No actionable
revision."`) are parsed as two unconditional rules. The A-01 R10 failure was a gate-misfiring
error — imperative style eliminates the class.

---

```
You are simulating customer reactions to a spec before it ships. Complete all 12 persona
feedback cards and professional lens synthesis.

Read the spec: {topic}.
Read the trace artifact (ground truth): {signal}.

---

## OUTPUT ORDER

Produce these sections in this sequence:
1. PERSONA FEEDBACK CARDS
2. BLOCKERS REQUIRING RESOLUTION
3. UX READ
4. PM READ
5. AGGREGATE NPS
6. CROSS-PERSONA THEME MATRIX

Produce no new analytical content after Section 6.

---

## SECTION 1 — PERSONA FEEDBACK CARDS

Produce one card for each of the 12 personas (C-01 through C-12).

Order cards by ascending NPS — lowest first, highest last.
Do not use roster order (C-01 through C-12).
Do not place a higher-NPS card before a lower-NPS card.
Place ties in any order within a band.

**Card header:**
  ### [ID] — [NAME], [ROLE]
Put the persona ID, name, and role in the header.
Do not put the NPS score in the header.

**Card body — produce these fields in this sequence:**

**Current approach:**
Describe what this persona does today without this spec.
State the specific workflow.
If no equivalent workflow exists, state that explicitly.
Write 1–2 sentences.

**Gains from this spec:**
State the specific gains this persona receives relative to their Current approach.
Name the concrete step that disappears or the friction that resolves.
Do not write generic category labels ("efficiency improvement", "time savings").
Write 1–3 sentences.

**Losses and switching costs:**
State what this persona sacrifices: migration burden, learning curve, workflow disruption,
toolchain changes, opportunity cost.
For Promoter-tier personas: write "No significant losses identified." followed by one sentence
explaining why switching costs are negligible for this persona's context.
Produce this field for every card.
Do not omit it.
Do not merge it with Gains.
Write 1–3 sentences.

**NPS:**
Assign the NPS score after completing the Current approach, Gains, and Losses fields.
Write a single integer 1–10.

**Band:**
Write Detractor, Passive, or Promoter.
Detractor = 1–6. Passive = 7–8. Promoter = 9–10.
Write this as a separate field on its own line.
Do not write the band as a parenthetical inside the NPS field.

**NPS justification:**
Synthesize the Gains and Losses fields into a 2–3 sentence score explanation.
Reference the Current approach as the inertia baseline.
Do not re-list individual gains and losses.
State why the bilateral balance produces this specific score for this specific persona.

**Feedback:**
Order feedback items by descending severity: blocking, then major, then minor, then cosmetic.
Do not place a lower-severity item before a higher-severity item.
Prefix every blocking item with [BLOCKING].
Write:
  - [BLOCKING] [item]
  - [major] [item]
  - [minor] [item]
  - [cosmetic] [item]
If this persona has no objections, write: "No feedback items."

**Revision recommendation:**
Write a revision recommendation for every card.
Do not omit this field for any card.
For Detractor-tier and Passive-tier cards (NPS 1–8):
  Name the specific spec element that must change to improve this persona's NPS.
  Do not write generic recommendations ("improve onboarding", "simplify the UX").
For Promoter-tier cards (NPS 9–10):
  Write: "No actionable revision. [One sentence explaining why this persona's context is
  already well-served by the spec as written.]"

---

## SECTION 2 — BLOCKERS REQUIRING RESOLUTION

Collect every [BLOCKING] item from Section 1.
Write one line per item:
  [PERSONA ID] — [blocking item text]
If no blocking items exist, write: "None."

---

## SECTION 3 — UX READ

Write the UX Read before the PM Read.
This order is required.

Write 2–4 sentences from the UX practitioner's lens.
Address interaction design quality, discoverability, cognitive load, and friction hotspots.
Name specific spec elements.
Do not write generalities.

---

## SECTION 4 — PM READ

Write 2–4 sentences from the PM lens.
Address adoption risk, revision priority, go/no-go signal, and threshold status.
Reference the aggregate NPS from Section 5.

---

## SECTION 5 — AGGREGATE NPS

**Aggregate NPS:**
List all 12 persona NPS scores.
Show the sum.
Divide by 12.
Round to one decimal place.

**Threshold:**
Write "Met" if the aggregate is >= 7.0.
Write "Spec needs revision" if the aggregate is < 7.0.

**Band distribution:**
Write three lines:
  - Promoters (9–10): [count]
  - Passives (7–8): [count]
  - Detractors (1–6): [count]

**Dominant Detractor objection:**
Name the single feedback theme most frequently cited by Detractor-tier personas.
Write: "[Theme] — raised by X of Y Detractors."

**Sensitivity analysis:**
Identify the 2–3 personas whose scores pull the aggregate mean most strongly.
For each: compute the aggregate-mean delta if their score is removed.
Write: "Removing [ID] (NPS [N]) shifts the aggregate mean from [X] to [Y]."
Do not write "[Persona] is near the 7.0 threshold."
Do not recommend converting specific Detractors to clear the threshold.
Use contribution framing. Do not use threshold-proximity framing.

**Two-pass revision summary:**

Pass 1 — per-persona revisions (from Revision recommendation, Section 1):
  [PERSONA ID] — [recommendation]
Include all 12 personas.

Pass 2 — cross-persona synthesis:
Rank Pass 1 items by personas affected × maximum severity.
For each item: count of personas, maximum severity, expected NPS delta if implemented.
Produce both passes.
Pass 2 synthesizes and ranks.
Pass 2 does not re-list Pass 1.

---

## SECTION 6 — CROSS-PERSONA THEME MATRIX

This is the final substantive section.
Produce no new analytical content after it.

| Theme | Personas | Distribution | Highest Severity |
|-------|----------|--------------|------------------|
| [theme] | [C-0X, ...] | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Rules:
- Include themes raised by 2+ personas.
- Distribution: write counts at each severity level. "1 blocking, 3 major, 2 minor" is
  the required format. Writing only the highest severity does not satisfy this column.
- Highest Severity: write the worst severity raised for this theme across all listed personas.
- Produce at least 1 row.
```

---

## V-04 — Combination: Unconditional 9th Field + Lifecycle Phases + Inertia Framing

**Axes:** Unconditional 9-field card (no "omit if" clause anywhere in the template) + lifecycle
decision-labeled phases + gains/losses as dedicated fields before NPS.

**Hypothesis:** The A-01 R10 failure arose from a conditional field: "Required if NPS ≤ 6.
If NPS > 6, omit." Conditional fields create gates that misfire. A 9-field card where Field 8
is labeled "Revision recommendation" with no conditional clause eliminates the gate entirely —
the model fills Field 8 because it is Field 8, not because it evaluated a threshold condition.
Field 9 (Revision priority: HIGH/MEDIUM/LOW) adds a second unconditional structural element
that further anchors the revision recommendation as a non-optional deliverable. Combined with
lifecycle phase labels and inertia-first field ordering, the three highest-probability failure
modes from R10 are closed simultaneously.

---

```
You are simulating customer reactions to a spec before it ships. Complete 12 persona feedback
cards (C-01 through C-12), professional lens synthesis, and cross-persona analysis.

Read the spec: {topic}.
Read the trace artifact (ground truth): {signal}.

---

## DECISION LIFECYCLE

Execute phases in this order. Each label names the decision the phase produces.

  PHASE 1 — UX FRAME (design quality baseline)
  PHASE 2 — CUSTOMER REACTIONS (12 cards, ascending NPS)
  PHASE 3 — BLOCKERS (blocking issue collection)
  PHASE 4 — AGGREGATE SCORE (NPS computation + sensitivity)
  PHASE 5 — PM CLOSE (synthesis after aggregate)
  PHASE 6 — THEME MATRIX (final substantive section)

PHASE 6 is the final substantive section. No analytical content follows it.

---

## PHASE 1 — UX FRAME

Decision: Is the interaction design sound enough for personas to evaluate this spec on its
merits?

UX READ precedes PM READ. This ordering is required.

Write 2–4 sentences from the UX practitioner's lens: interaction design quality,
discoverability, cognitive load, friction hotspots. Reference specific spec elements by name.

---

## PHASE 2 — CUSTOMER REACTIONS

Decision: How does each of the 12 personas react to this spec?

Generate one card per persona, C-01 through C-12.

**Ordering:** Ascending NPS — lowest predicted score first, highest last. Hard requirement.
Roster order (C-01 through C-12) is not acceptable. Ties may appear in any order within a band.

**Card header:**
  ### [PERSONA ID] — [NAME], [ROLE]
Header contains: ID, name, role only. NPS does not appear in the header.

**Card body — 9 required fields in this exact sequence. Every field is required for every
card. No field may be omitted:**

Field 1 of 9 — **Current approach:**
[1–2 sentences. The persona's workflow today without this spec. If no equivalent workflow
exists: "No equivalent workflow exists."]

Field 2 of 9 — **Gains from this spec:**
[1–3 sentences. Specific gains relative to Field 1. Name the mechanism — the concrete step
that goes away or the friction that resolves. Generic labels ("efficiency gains") do not
satisfy this field.]

Field 3 of 9 — **Losses and switching costs:**
[1–3 sentences. Migration burden, learning curve, workflow disruption, toolchain changes,
opportunity cost.
For Promoter-tier personas: "No significant losses identified. [One sentence explaining why
switching costs are negligible for this persona's context.]"
This field is required at all NPS tiers. It may not be omitted. It may not be merged with
Field 2.]

Field 4 of 9 — **NPS:**
[Integer 1–10. Assign the score after completing Fields 1–3. The score follows from the
economic analysis in Fields 2 and 3.]

Field 5 of 9 — **Band:**
[Detractor | Passive | Promoter]
Detractor = 1–6 · Passive = 7–8 · Promoter = 9–10
Distinct field from Field 4. The band annotation does not appear inside the NPS field value
as a parenthetical or bracket.

Field 6 of 9 — **NPS justification:**
[2–3 sentences. Synthesize Fields 2 and 3 relative to Field 1 as the inertia baseline. Does
not re-list individual gains and losses from Fields 2 and 3 — synthesizes them into a
rationale for why this bilateral balance produces this score for this persona.]

Field 7 of 9 — **Feedback:**
Order by descending severity: [BLOCKING] → major → minor → cosmetic. No lower-severity
item may precede a higher-severity item.
  - [BLOCKING] [item] — all blocking items carry the [BLOCKING] inline prefix
  - [major] [item]
  - [minor] [item]
  - [cosmetic] [item]
If no objections: "No feedback items."

Field 8 of 9 — **Revision recommendation:**
[Required for every card. No conditional logic applies. This field is not gated by NPS tier.
  — Detractor-tier or Passive-tier (NPS 1–8): one concrete, actionable spec change naming
    the specific spec element that must change to improve this persona's NPS. Generic
    recommendations ("simplify onboarding") do not satisfy this field — name the element.
  — Promoter-tier (NPS 9–10): write "No actionable revision. [One sentence explaining why
    this persona's context is already well-served by the spec as written.]"]

Field 9 of 9 — **Revision priority:**
[HIGH | MEDIUM | LOW.
  HIGH = blocking severity item present, or persona represents a high-adoption-risk segment.
  MEDIUM = major severity items without blocking; Passive-tier with actionable revision.
  LOW = Promoter-tier "no actionable revision" cards.]

---

## PHASE 3 — BLOCKERS

Decision: What issues must be resolved before this spec ships?

Collect all [BLOCKING] items from Phase 2.
  [PERSONA ID] — [blocking item text]
If none: "None."

---

## PHASE 4 — AGGREGATE SCORE

Decision: Does this spec clear the 7.0 NPS threshold, and which personas drive the mean?

**Aggregate NPS:** [List all 12 scores. Show sum. Divide by 12. Round to one decimal.]

**Threshold:** [Met >= 7.0 | Spec needs revision < 7.0]

**Band distribution:**
  - Promoters (9–10): [count]
  - Passives (7–8): [count]
  - Detractors (1–6): [count]

**Dominant Detractor objection:** [Single theme most cited by Detractor-tier personas.
Format: "[Theme] — raised by X of Y Detractors."]

**Sensitivity analysis:**
Identify the 2–3 personas with the greatest mathematical weight on the aggregate mean.

Use aggregate-contribution framing: compute and state the mean delta if each identified
persona is removed.
  Example: "Removing C-09 (NPS 2) shifts the aggregate mean from 6.5 to 7.1."

Do not use threshold-proximity framing. Threshold framing describes position; contribution
framing quantifies influence. In skewed distributions these identify different personas.

**Two-pass revision summary:**

Pass 1 — per-persona revisions (from Field 8, Phase 2):
  [PERSONA ID] — [recommendation]
  Include all 12 personas. Promoter-tier entries carry "No actionable revision." forward.

Pass 2 — cross-persona synthesis:
Rank by personas affected × maximum severity. For each item: count, severity, expected NPS
delta if implemented. Both passes must be present. Pass 2 synthesizes and ranks.

---

## PHASE 5 — PM CLOSE

Decision: What is the go/no-go signal and top revision priority?

PM Read follows after the aggregate and revision priorities are visible.

Write 2–4 sentences from the PM lens: adoption risk, revision priority, go/no-go signal,
threshold status. Reference the aggregate NPS and top ranked revision from Phase 4.

---

## PHASE 6 — THEME MATRIX

Decision: What cross-cutting themes appear across personas?

This is the final substantive section. No section follows it.

| Theme | Personas | Distribution | Highest Severity |
|-------|----------|--------------|------------------|
| [theme] | [C-0X, ...] | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Rules:
- Include themes raised by 2+ personas
- Distribution: count per severity level — "1 blocking, 3 major, 2 minor" is required;
  showing only the highest severity does not satisfy this column
- Highest Severity: worst level raised for this theme across all personas listed
- Minimum 1 row required
```

---

## V-05 — Combination: Pre-Card Economic Profile + Numbered Schema + Explanatory Register

**Axes:** Each card opens with a named "Economic Profile" sub-block (Current approach +
Gains + Losses) that precedes the numbered card fields. NPS is Field 1 of the card body,
derived from the Economic Profile. Numbered fields 1–6. Explanatory register states why each
structural element exists.

**Hypothesis:** Separating the economic analysis into a named "Economic Profile" block before
the card fields makes two cognitive tasks explicit: (1) analyze the adoption economics, then
(2) generate the feedback card from that analysis. The profile block physically precedes Field 1
(NPS), making it impossible to assign a score before completing the economic analysis. This
enforces economic derivation more strongly than a within-field process-order instruction alone
— the profile block is a named section with a label and visual boundary, not just a field
ordering constraint. The explanatory register states why the Revision recommendation is
required for Promoter-tier cards ("tells the PM which segments are safe to deprioritize"),
making compliance feel motivated rather than bureaucratic.

---

```
You are simulating customer reactions to a spec before it ships. Complete 12 persona feedback
cards (C-01 through C-12) plus professional lens synthesis.

The card structure uses a two-step design: each card begins with an Economic Profile that
captures the adoption economics (what does this persona gain and lose?), and then the card
fields derive from that analysis. This structure exists because NPS scores derived from
gains-only analysis overpredict adoption — every adoption decision has a loss side, and the
Economic Profile forces both sides to be stated before the score is assigned.

Read the spec: {topic}.
Read the trace artifact (ground truth): {signal}.

---

## DOCUMENT STRUCTURE

Sections in this exact order. Section 6 is the final substantive section.

  1. PERSONA FEEDBACK CARDS
  2. BLOCKERS REQUIRING RESOLUTION
  3. UX READ
  4. PM READ
  5. AGGREGATE NPS
  6. CROSS-PERSONA THEME MATRIX

---

## SECTION 1 — PERSONA FEEDBACK CARDS

Generate 12 cards, one per persona (C-01 through C-12).

**Why ascending NPS order?**
Ascending order puts the revision signal at the top — the failures before the successes.
The personas most likely to block adoption are the ones to encounter first. Roster order
(C-01 through C-12) is not acceptable. Lowest predicted NPS first, highest last. Ties may
appear in any order within a band.

**Card header:**
  ### [ID] — [NAME], [ROLE]
Header contains ID, name, role only. The NPS score does not appear in the header — the
header is for navigation; a score in the header implies a decision before the evidence.

**Card structure — Economic Profile first, then the derived card fields:**

--- ECONOMIC PROFILE ---

**Current approach:**
[1–2 sentences. What does this persona do today without this spec? The inertia baseline —
the default behavior the spec is asking them to change. If no equivalent workflow exists,
state that explicitly: "No equivalent workflow exists."]

**Gains from this spec:**
[1–3 sentences. What does this persona specifically gain by adopting this spec, relative to
their Current approach? The gain must be mechanistic: name the specific step in this
persona's workflow that disappears, or the specific friction that resolves. "Saves time" is
not a mechanism; "eliminates the manual re-export step before each deployment" is.]

**Losses and switching costs:**
[1–3 sentences. What does this persona sacrifice? Migration effort, learning curve, workflow
disruption, toolchain changes, opportunity cost. Every adoption decision has a loss side,
even for enthusiastic adopters.
For Promoter-tier personas where losses are genuinely negligible: write
"No significant losses identified. [One sentence explaining why this persona's context makes
switching costs negligible.]"
This field is required for every card at every NPS tier. It may not be omitted or merged
with the Gains field.]

--- CARD FIELDS ---

Field 1 of 6 — **NPS:**
[Integer 1–10. Assign after completing the Economic Profile above. The score follows from
the bilateral economic analysis — gains, losses, and the persona's inertia baseline together
determine predicted adoption willingness.]

Field 2 of 6 — **Band:**
[Detractor | Passive | Promoter]
Detractor = 1–6 · Passive = 7–8 · Promoter = 9–10
Distinct field from Field 1. Band annotation does not appear as a parenthetical inside the
NPS field value. Structural separation makes band data independently accessible for the
aggregate distribution counts without requiring NPS value parsing.

Field 3 of 6 — **NPS justification:**
[2–3 sentences. Synthesize the Economic Profile into a score explanation. Reference the
Current approach as the inertia baseline. The justification synthesizes — it does not
re-list. The Economic Profile carries the economic data; the justification field carries
original synthesis prose explaining why this bilateral balance produces this specific score
for this specific persona, not for a generic user.]

Field 4 of 6 — **Feedback:**
Order by descending severity — blocking, then major, then minor, then cosmetic. No
lower-severity item may precede a higher-severity item. Severity-first ordering surfaces the
most serious feedback without requiring the reader to scan the full list.
  - [BLOCKING] [item] — all blocking items carry the [BLOCKING] inline prefix
  - [major] [item]
  - [minor] [item]
  - [cosmetic] [item]
If no objections: "No feedback items."

Field 5 of 6 — **Revision recommendation:**
[Required for every card at every NPS tier. No conditional logic applies to this field.
  — Detractor-tier or Passive-tier (NPS 1–8): one concrete, actionable spec change naming
    the specific spec element that must change to improve this persona's NPS. Generic
    recommendations ("improve the documentation") do not satisfy this field — name the
    element. The recommendation should target what this persona lost or found blocking.
  — Promoter-tier (NPS 9–10): write "No actionable revision. [One sentence explaining why
    this persona's context is already well-served by the spec as written.]"
  This field exists for every card because even a Promoter entry ("none — spec already
  addresses this persona's primary friction point") tells the PM which segments are safe to
  deprioritize in the revision pass.]

Field 6 of 6 — **Revision priority:**
[HIGH | MEDIUM | LOW.
  HIGH = blocking severity item present, or persona represents a high-adoption-risk segment.
  MEDIUM = major severity items without blocking; Passive-tier with actionable revision.
  LOW = Promoter-tier "no actionable revision" cards.]

---

## SECTION 2 — BLOCKERS REQUIRING RESOLUTION

Collect all [BLOCKING] items from Section 1.
  [PERSONA ID] — [blocking item text]
If none: "None."

---

## SECTION 3 — UX READ

UX READ precedes PM READ. UX craft framing establishes the interaction design baseline —
whether features are discoverable and low-friction — before the PM synthesizes the signal.

Write 2–4 sentences from the UX practitioner's lens: interaction design quality,
discoverability, cognitive load, friction hotspots. Reference specific spec elements by name.

---

## SECTION 4 — PM READ

The PM reads the aggregate signal, after Sections 1–3 are complete.

Write 2–4 sentences from the PM lens: adoption risk, revision priority, go/no-go signal,
threshold status. Reference the aggregate NPS from Section 5.

---

## SECTION 5 — AGGREGATE NPS

**Aggregate NPS:** [List all 12 persona NPS scores. Show sum. Divide by 12. Round to one
decimal place.]

**Threshold:** [Met >= 7.0 | Spec needs revision < 7.0]

**Band distribution:**
  - Promoters (9–10): [count]
  - Passives (7–8): [count]
  - Detractors (1–6): [count]

**Dominant Detractor objection:** [Single theme most cited by Detractor-tier personas.
Format: "[Theme] — raised by X of Y Detractors."]

**Sensitivity analysis:**
Identify the 2–3 personas whose scores pull the aggregate mean most strongly.

Use aggregate-contribution framing: compute and state the mean delta if each identified
persona is removed.
  Example: "Removing C-06 (NPS 2) shifts the aggregate mean from 6.2 to 6.9."

Do not use threshold-proximity framing. "C-06 is near the 7.0 threshold" describes position;
"removing C-06 shifts the mean by 0.7" quantifies influence. In skewed distributions, the
personas nearest 7.0 are not the same as those with the greatest mathematical weight —
always use contribution framing.

**Two-pass revision summary:**

Pass 1 — per-persona revisions (from Field 5, Section 1):
  [PERSONA ID] — [recommendation]
  Include all 12 personas. Promoter-tier entries carry "No actionable revision." forward.

Pass 2 — cross-persona synthesis:
Rank by personas affected × maximum severity. For each item: count, severity, expected NPS
delta if implemented. Both passes must be present. Pass 2 synthesizes and ranks.

---

## SECTION 6 — CROSS-PERSONA THEME MATRIX

The theme matrix is last because it synthesizes every card, every feedback item, every
severity label into a single cross-persona view. It is the final substantive section — no
new analysis follows it.

| Theme | Personas | Distribution | Highest Severity |
|-------|----------|--------------|------------------|
| [theme] | [C-0X, ...] | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Rules:
- Themes raised by 2+ personas
- Distribution: count per severity level — "1 blocking, 3 major, 2 minor" is required;
  showing only the highest severity does not satisfy this column. Per-severity counts reveal
  whether a theme is driven by a single severe issue or widespread minor friction — the
  aggregate ceiling alone cannot distinguish these.
- Highest Severity: worst level raised under this theme across all listed personas
- Minimum 1 row required
```

---

## Variation Summary

| Variation | Axis | A-01 Mechanism | Key Differentiator |
|-----------|------|----------------|--------------------|
| V-01 | Inertia framing (R10 V-01 + fix) | Field enumerated per tier; Promoter tier gets "No actionable revision." — unconditional prose | Minimal change from 175/180 base — closes A-01 without introducing new constructs |
| V-02 | Lifecycle emphasis | REVISE is a standalone phase; phase asks "what do we recommend per persona?" — all 12 covered by phase scope | Phase-decision framing eliminates conditional-gate logic; revision recommendations fall out of the phase question |
| V-03 | Phrasing register (fully imperative) | Two unconditional bullet imperatives replace one gated conditional | Conditional logic eliminated class-wide; every requirement is an unconditional imperative sentence |
| V-04 | Unconditional 9th field + lifecycle + inertia | Field 8 of 9 carries no "omit if" clause; Field 9 (Revision priority) reinforces revision rec as structural, not conditional | Conditional eliminated structurally; field number is the compliance signal, not threshold evaluation |
| V-05 | Pre-card Economic Profile + numbered schema + explanatory register | Field 5 of 6 unconditional; explanatory rationale explains why Promoter entry still counts | Named sub-block enforces economic-first derivation; two cognitive tasks separated by visual boundary |

**A-01 fix note:** All five variations require revision recommendations for all 12 personas.
V-01 uses explicit tier enumeration. V-02 uses phase-scope coverage. V-03 uses bullet
imperatives. V-04 uses an unconditional numbered field. V-05 uses an unconditional field plus
explanatory rationale for why Promoter entries are still required.

**Regression protection:** All five variations carry the complete A-01 through A-18 feature
set. No variation was written from a clean skeleton. Each is built by extending or restructuring
the R10 V-01 phase sequence. The two R10 excellence signals (in-field process-order instruction;
synthesis-not-relisting constraint) are preserved in all variations.

**New structural elements in R11 (V-04, V-05 only):**
- Field 9 of 9: Revision priority (HIGH/MEDIUM/LOW) — unconditional structural anchor for
  Field 8; not in rubric as a graded criterion, but reinforces A-01 compliance
- Pre-card Economic Profile block — named sub-block with visual boundary separating economic
  analysis from card fields; satisfies A-09/A-11/A-17/A-18 via structural positioning
