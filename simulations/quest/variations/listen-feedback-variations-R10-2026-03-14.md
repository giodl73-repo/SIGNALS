Now I have everything. Writing all 5 variations:

---

# listen-feedback — Round 10 Variations

**Context:** R8 accumulated A-01 through A-15 at 165/165. R9 captured A-16 and A-17 (achieving 115/175) but regressed the 12 aspirationals by starting fresh. R10 rubric (v9) adds A-18 (gains/losses as separate dedicated labeled fields). Goal: preserve R8's full feature set, add A-16+A-17+A-18, vary on stated axes.

**Variation axes selected:**
- Single-axis 1: **Inertia framing** — gains/losses fields positioned before NPS as primary economic lenses
- Single-axis 2: **Output format** — numbered field schema enforces field cardinality mechanically
- Single-axis 3: **Role sequence** — UX Read anchors the session in Phase 1
- Combination A: **Inertia framing + Output format + negative exemplars**
- Combination B: **Inertia framing + Role sequence + explanatory phrasing register**

---

## V-01 — Inertia Framing Axis

**Axis:** Gains and losses fields are positioned before the NPS field, making the bilateral economic analysis the primary lens from which the score is derived.

**Hypothesis:** When `Gains from this spec:` and `Losses and switching costs:` appear as dedicated fields before the NPS score, the model derives the score from the economic analysis rather than assigning a score first and rationalizing it post-hoc — producing more authentic inertia-baseline-grounded NPS values and satisfying A-18 via template position alone.

---

```
You are simulating customer reactions to a spec before it ships. Work through all 12 customer
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
ordering requirement, not alphabetical. Persona roster order (C-01 through C-12) is not
acceptable. Ties may appear in any order within a band.

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

**Revision recommendation:** [Required if NPS ≤ 6. One concrete, actionable spec change
naming the specific spec element that must change. Generic recommendations ("improve
onboarding") do not satisfy this field. If NPS > 6, omit this field.]

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
If no persona had NPS ≤ 6: "No revision recommendations generated (all NPS > 6)."

Pass 2 — cross-persona synthesis:
Synthesize Pass 1 into a ranked revision list ordered by personas affected × maximum severity.
For each item: how many personas it addresses, the maximum severity driving it, and the
expected NPS impact if implemented. Both passes must be present.

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

## V-02 — Output Format Axis (Numbered Field Schema)

**Axis:** Each card field carries an explicit position number (Field 1 of 8 through Field 8 of 8) and a cardinality constraint. Field reordering or omission becomes mechanically visible — a missing field creates a numbering gap.

**Hypothesis:** Numbered field positions prevent silent field merging — the model cannot collapse `Gains from this spec:` (Field 2) and `Losses and switching costs:` (Field 3) into a single prose block without skipping a position number. Structural compliance is enforced by the numbering sequence itself, not by reading the prose.

---

```
You are simulating customer reactions to a spec before it ships. Complete 12 persona feedback
cards (C-01 through C-12) plus professional lens synthesis.

Read the spec: {topic}.
Read the trace artifact (ground truth): {signal}.

---

## DOCUMENT STRUCTURE

Sections in this exact order:
  1. PERSONA FEEDBACK CARDS
  2. BLOCKERS REQUIRING RESOLUTION
  3. UX READ
  4. PM READ
  5. AGGREGATE NPS
  6. CROSS-PERSONA THEME MATRIX

Section 6 is the final substantive section. No analytical content follows it.

---

## SECTION 1 — PERSONA FEEDBACK CARDS

Generate 12 cards, one per persona (C-01 through C-12).

**Card order:** Ascending NPS — lowest predicted NPS first, highest last. This is a
structural requirement. Persona roster order (C-01 through C-12) is not acceptable ordering.

**Card header:**
  **[ID] — [NAME], [ROLE]**
Header contains: ID, name, role. The NPS score does not appear in the header.

**Card body — 8 required fields in this exact numbered sequence:**

Field 1 of 8 — **Current approach:**
  [1–2 sentences. The persona's workflow today without this spec. If no equivalent workflow
  exists: "No equivalent workflow exists."]

Field 2 of 8 — **Gains from this spec:**
  [1–3 sentences. Specific gains relative to Field 1. Name the mechanism — the specific step
  that goes away or the specific friction that resolves. Generic category labels
  ("efficiency gains") do not satisfy this field.]

Field 3 of 8 — **Losses and switching costs:**
  [1–3 sentences. Migration cost, learning curve, workflow disruption, toolchain changes,
  opportunity cost.
  For Promoter-tier personas: "No significant losses identified. [One sentence explaining why
  switching costs are negligible for this persona's context.]"
  This field is required for every card at every band tier. It may not be omitted. It may not
  be merged with Field 2.]

Field 4 of 8 — **NPS:**
  [Integer 1–10. Assign the score after completing Fields 1–3.]

Field 5 of 8 — **Band:**
  [Detractor | Passive | Promoter]
  Detractor = 1–6 · Passive = 7–8 · Promoter = 9–10
  This is a distinct field from Field 4. The band annotation does not appear inside the NPS
  field value as a parenthetical.

Field 6 of 8 — **NPS justification:**
  [2–3 sentences. Synthesize Fields 2 and 3 into a score explanation that references Field 1
  as the inertia baseline. The justification synthesizes the bilateral analysis — it does not
  re-list individual gains and losses from Fields 2 and 3.]

Field 7 of 8 — **Feedback:**
  Descending severity order: [BLOCKING] → major → minor → cosmetic. No lower-severity item
  may precede a higher-severity item.
    - [BLOCKING] [item] — all blocking items carry the [BLOCKING] inline prefix
    - [major] [item]
    - [minor] [item]
    - [cosmetic] [item]
  If no objections: "No feedback items."

Field 8 of 8 — **Revision recommendation:**
  Required if NPS ≤ 6. One concrete, actionable spec change naming a specific spec element.
  "Improve documentation" or "simplify the UX" do not satisfy this field — name the element.
  If NPS > 6: omit this field.

---

## SECTION 2 — BLOCKERS REQUIRING RESOLUTION

Collect all [BLOCKING] items from Section 1.
  [PERSONA ID] — [item text]
If none: "None."

---

## SECTION 3 — UX READ

UX READ appears before PM READ. This ordering is required.

2–4 sentences from the UX practitioner's lens: interaction design quality, discoverability,
cognitive load, friction hotspots across the persona set. Reference specific spec elements.

---

## SECTION 4 — PM READ

2–4 sentences from the PM lens: adoption risk, revision priority, threshold status, go/no-go
signal. Reference the aggregate NPS from Section 5.

---

## SECTION 5 — AGGREGATE NPS

**Aggregate NPS:** [List all 12 persona NPS scores. Sum. Divide by 12. One decimal place.]

**Threshold:** [Met ≥ 7.0 | Spec needs revision < 7.0]

**Band distribution:**
  - Promoters (9–10): [count]
  - Passives (7–8): [count]
  - Detractors (1–6): [count]

**Dominant Detractor objection:** [Single theme most cited by Detractor-tier personas.
Format: "[Theme] — X of Y Detractors."]

**Sensitivity analysis:**
Identify the 2–3 personas with the greatest mathematical weight on the aggregate mean.

Use aggregate-contribution framing: state the aggregate-mean delta for each identified
persona. Example: "Removing C-11 (NPS 2) shifts the mean from 5.9 to 6.5."

Do not use threshold-proximity framing. Do not write "[Persona] is near the 7.0 threshold."
In skewed distributions, threshold-proximate personas are not necessarily the highest-weight
personas. Contribution framing quantifies influence; threshold framing describes position only.

**Two-pass revision summary:**

Pass 1 — per-persona revisions (from Field 8 items, Section 1):
  [ID] — [recommendation]
If no NPS ≤ 6 cards: "No revision recommendations generated."

Pass 2 — cross-persona synthesis:
Rank by personas affected × maximum severity. Per item: count of personas, maximum severity,
expected NPS delta if implemented. Both passes must be present. Pass 2 must rank, not list.

---

## SECTION 6 — CROSS-PERSONA THEME MATRIX

Final substantive section. No section follows it.

| Theme | Personas | Distribution | Highest Severity |
|-------|----------|--------------|------------------|
| [theme] | [C-0X, ...] | [X blocking, Y major, Z minor, W cosmetic] | [level] |

- 2+ personas per theme
- Distribution: count per severity level — showing only the highest severity does not satisfy
  this column
- Highest Severity: worst level raised for this theme across all personas listed
- Minimum 1 row required
```

---

## V-03 — Role Sequence Axis (UX-Anchored Session)

**Axis:** UX Read runs in Phase 1, before persona cards. Persona cards are generated in Phase 2 within the interaction design frame established by Phase 1. PM Read closes in Phase 5, after the aggregate is computed.

**Hypothesis:** Anchoring the session with a UX frame before persona cards causes per-persona feedback to engage with interaction design affordances (discoverability, cognitive load, flow friction) rather than treating the spec as a feature checklist. A persona who encounters a poorly discoverable feature produces different feedback from a persona who evaluates it in the abstract.

---

```
You are simulating customer reactions to a spec before it ships. The session opens with a UX
design frame, then 12 customer personas (C-01 through C-12) react within it, then PM synthesis
closes.

Read the spec: {topic}.
Read the trace artifact (ground truth): {signal}.

---

## SESSION PHASES

Execute in this order:

  PHASE 1 — UX READ (design frame, runs first)
  PHASE 2 — PERSONA FEEDBACK CARDS (ascending NPS, within the UX frame)
  PHASE 3 — BLOCKERS REQUIRING RESOLUTION
  PHASE 4 — AGGREGATE NPS + SENSITIVITY ANALYSIS + REVISION SUMMARY
  PHASE 5 — PM READ (synthesizes the full session)
  PHASE 6 — CROSS-PERSONA THEME MATRIX (final substantive section)

PHASE 6 is the final substantive section. No new analytical content follows it.

---

## PHASE 1 — UX READ

The UX Read opens the session. It establishes the design quality baseline within which each
persona will react. A persona encountering a poorly discoverable feature will score differently
from a persona evaluating the same feature on paper — the UX Read names which it is.

Write 2–4 sentences from the UX practitioner's lens. Address: interaction design quality,
discoverability, cognitive load, predicted friction hotspots. Reference specific spec elements
by name.

---

## PHASE 2 — PERSONA FEEDBACK CARDS

Generate one card per persona, C-01 through C-12. Each persona reacts to the spec within the
UX context established in Phase 1 — feedback items may reference the design-quality signals
named there.

**Ordering:** Ascending NPS — lowest predicted NPS first, highest last. Hard requirement.
Roster order (C-01 through C-12) is not acceptable. Ties may appear in any order within a band.

**Card header:**
  ### [PERSONA ID] — [NAME], [ROLE]
Header contains: ID, name, role only. No NPS score in the header.

**Card body — use this field sequence:**

**Current approach:** [1–2 sentences. What does this persona do today without this spec?
If no equivalent workflow exists, state that explicitly.]

**Gains from this spec:** [1–3 sentences. Specific gains relative to the Current approach.
Name the mechanism tied to this persona's role and context — not a generic feature benefit.]

**Losses and switching costs:** [1–3 sentences. Migration burden, learning curve, workflow
disruption, toolchain changes, opportunity cost.
For Promoter-tier personas where friction is genuinely negligible:
"No significant losses identified. [One sentence explaining why switching costs are negligible
for this persona.]"
This field is required for every tier and may not be omitted.]

**NPS:** [Integer 1–10]

**Band:** [Detractor | Passive | Promoter]
  Detractor = 1–6 · Passive = 7–8 · Promoter = 9–10
Band is a distinct field. It does not appear as a parenthetical inside the NPS field value.

**NPS justification:** [2–3 sentences. Synthesize the Gains and Losses fields into a score
explanation that references the Current approach as the inertia baseline. The justification
synthesizes the bilateral analysis — it does not re-list individual items from the fields above.]

**Feedback:**
Ordered by descending severity: [BLOCKING] → major → minor → cosmetic. No lower-severity
item may precede a higher-severity item.
  - [BLOCKING] [item] — [BLOCKING] inline prefix required for all blocking items
  - [major] [item]
  - [minor] [item]
  - [cosmetic] [item]
If no objections: "No feedback items."

**Revision recommendation:** [Required if NPS ≤ 6. One concrete, actionable spec change
naming a specific spec element. Generic recommendations do not satisfy this field. Omit if
NPS > 6.]

---

## PHASE 3 — BLOCKERS REQUIRING RESOLUTION

Collect all [BLOCKING] items from Phase 2.
  [PERSONA ID] — [item text]
If none: "None."

---

## PHASE 4 — AGGREGATE NPS + SENSITIVITY ANALYSIS + REVISION SUMMARY

**Aggregate NPS:** [List all 12 scores. Sum. Divide by 12. One decimal place.]

**Threshold:** [Met ≥ 7.0 | Spec needs revision < 7.0]

**Band distribution:**
  - Promoters (9–10): [count]
  - Passives (7–8): [count]
  - Detractors (1–6): [count]

**Dominant Detractor objection:** [Single theme most frequently cited by Detractor-tier
personas. "[Theme] — X of Y Detractors."]

**Sensitivity analysis:**
Identify the 2–3 personas with the greatest weight on the aggregate mean.

Use aggregate-contribution framing: compute and state the aggregate-mean delta if each
identified persona is removed. Example: "Removing C-03 (NPS 2) shifts the mean from 6.3 to 6.9."

Do not use threshold-proximity framing. Do not write "C-03 is near the 7.0 threshold" or
recommend converting specific Detractors to clear the threshold. In skewed distributions, the
personas nearest 7.0 are not the personas with the greatest mathematical weight on the mean.

**Two-pass revision summary:**

Pass 1 — per-persona revisions (from Revision recommendation fields, Phase 2):
  [ID] — [recommendation]
If no NPS ≤ 6: "No revision recommendations generated."

Pass 2 — cross-persona synthesis:
Rank by personas affected × maximum severity. Per item: count, severity, expected NPS delta.
Both passes must be present. Pass 2 synthesizes and ranks; it does not re-list Pass 1.

---

## PHASE 5 — PM READ

The PM Read closes after the aggregate is computed. The PM synthesizes the full session output:
UX frame (Phase 1), aggregate NPS (Phase 4), and revision priorities.

Write 2–4 sentences from the PM lens. Address: adoption risk, revision priority, go/no-go
signal, threshold status.

---

## PHASE 6 — CROSS-PERSONA THEME MATRIX

This is the final substantive section. No section follows it.

| Theme | Personas | Distribution | Highest Severity |
|-------|----------|--------------|------------------|
| [theme] | [C-0X, ...] | [X blocking, Y major, Z minor, W cosmetic] | [level] |

- Themes raised by 2+ personas
- Distribution: count per severity level — "1 blocking, 3 major, 2 minor" is required;
  showing only the highest severity does not satisfy this column
- Minimum 1 row required
```

---

## V-04 — Combination: Inertia Framing + Output Format + Negative Exemplars

**Axes:** Dedicated gains/losses fields (V-01) + rigid numbered schema (V-02) + inline `DO NOT` antipattern callouts for the three structural failure modes most likely to regress.

**Hypothesis:** Naming the exact disallowed output patterns for A-18 (field merging), A-16 (inline band annotation), and A-15 (threshold-proximity framing) — with specific example strings — makes compliance deterministic rather than probabilistic. The model can match against the disallowed string; it cannot match against an abstract criterion. Three targeted negative exemplars close the three highest-probability regression paths simultaneously.

---

```
You are simulating customer reactions to a spec before it ships. Complete 12 persona feedback
cards (C-01 through C-12) plus professional lens synthesis.

Read the spec: {topic}.
Read the trace artifact (ground truth): {signal}.

---

## DOCUMENT STRUCTURE

Sections in this order. Section 6 is the final substantive section — no analytical content
follows it.
  1. PERSONA FEEDBACK CARDS
  2. BLOCKERS REQUIRING RESOLUTION
  3. UX READ
  4. PM READ
  5. AGGREGATE NPS
  6. CROSS-PERSONA THEME MATRIX

---

## SECTION 1 — PERSONA FEEDBACK CARDS

12 cards, one per persona (C-01 through C-12).

**Ordering:** Ascending NPS — lowest first, highest last. Hard requirement. Roster order
(C-01 through C-12) is not acceptable.

**Header:** **[ID] — [NAME], [ROLE]** — ID, name, role only. No NPS in header.

**Body — 8 required fields in this numbered sequence:**

Field 1 of 8 — **Current approach:**
[1–2 sentences. The persona's workflow today without this spec. If no equivalent workflow
exists: "No equivalent workflow exists."]

Field 2 of 8 — **Gains from this spec:**
[1–3 sentences. Specific gains relative to Field 1. Name the mechanism — the concrete step
that goes away or friction that resolves.]
DO NOT write: "This persona gains efficiency." — name the specific step that disappears.

Field 3 of 8 — **Losses and switching costs:**
[1–3 sentences. Migration burden, learning curve, workflow disruption, toolchain changes,
opportunity cost.
For Promoter-tier personas: "No significant losses identified. [One sentence explaining why.]"
This field is required at all NPS tiers. It may not be omitted or merged with Field 2.]
DO NOT write Fields 2 and 3 as a single "Justification" paragraph. Gains and Losses are
two separate required fields. The justification field (Field 6) synthesizes them — it does
not replace them.

Field 4 of 8 — **NPS:**
[Integer 1–10. Assign after completing Fields 1–3.]

Field 5 of 8 — **Band:**
[Detractor | Passive | Promoter]
Detractor = 1–6 · Passive = 7–8 · Promoter = 9–10
DO NOT write: "**NPS:** 6 (Detractor)" — this merges the band annotation into the NPS
field. Band must appear on its own line as Field 5.

Field 6 of 8 — **NPS justification:**
[2–3 sentences. Synthesize Fields 2 and 3 relative to Field 1 as the inertia baseline.
Does not re-list individual gains and losses — synthesizes them into a score rationale.]

Field 7 of 8 — **Feedback:**
Descending severity order: [BLOCKING] → major → minor → cosmetic. No lower-severity item
may precede a higher-severity item.
  - [BLOCKING] [item] — [BLOCKING] inline prefix required on all blocking items
  - [major] [item]
  - [minor] [item]
  - [cosmetic] [item]
If no objections: "No feedback items."

Field 8 of 8 — **Revision recommendation:**
Required if NPS ≤ 6. One concrete, actionable spec change naming a specific element.
"Improve documentation" does not satisfy this field — name the element. Omit if NPS > 6.

---

## SECTION 2 — BLOCKERS REQUIRING RESOLUTION

  [PERSONA ID] — [item text]
If none: "None."

---

## SECTION 3 — UX READ

UX READ appears before PM READ. This ordering is required.

2–4 sentences from the UX lens: interaction design quality, discoverability, cognitive load,
friction hotspots. Reference specific spec elements by name.

---

## SECTION 4 — PM READ

2–4 sentences from the PM lens: adoption risk, revision priority, threshold status, go/no-go.
Reference the aggregate NPS.

---

## SECTION 5 — AGGREGATE NPS

**Aggregate NPS:** [List all 12 scores. Sum. Divide by 12. One decimal.]

**Threshold:** [Met ≥ 7.0 | Spec needs revision < 7.0]

**Band distribution:**
  - Promoters (9–10): [count]
  - Passives (7–8): [count]
  - Detractors (1–6): [count]

**Dominant Detractor objection:** [Single theme most cited by Detractors.
"[Theme] — X of Y Detractors."]

**Sensitivity analysis:**
Identify the 2–3 personas with the greatest mathematical weight on the aggregate mean.

Use aggregate-contribution framing: compute and state the mean delta if each identified
persona is removed or changes score. Example: "Removing C-02 (NPS 3) shifts the mean from
6.1 to 6.8."

DO NOT write: "C-02 is just below the 7.0 threshold" or "converting C-02 from Detractor to
Passive would clear the threshold." Threshold-proximity framing describes position, not
mathematical weight. In skewed distributions, the highest-weight personas are not the ones
nearest 7.0 — they are different sets.

**Two-pass revision summary:**

Pass 1 — per-persona revisions (from Field 8 items, Section 1):
  [ID] — [recommendation]

Pass 2 — cross-persona synthesis:
Ranked by personas affected × maximum severity. Per item: count, severity, expected NPS delta.
Both passes required. Pass 2 must rank.

---

## SECTION 6 — CROSS-PERSONA THEME MATRIX

Final substantive section. No section follows it.

| Theme | Personas | Distribution | Highest Severity |
|-------|----------|--------------|------------------|
| [theme] | [C-0X, ...] | [X blocking, Y major, Z minor, W cosmetic] | [level] |

- 2+ personas per theme
- Distribution: count per severity level — showing only the highest severity does not
  satisfy this column
- Minimum 1 row
```

---

## V-05 — Combination: Inertia Framing + Role Sequence + Explanatory Register

**Axes:** UX-anchored role sequence (Phase 1 = UX) + dedicated gains/losses fields + conversational register that states the purpose of each structural requirement.

**Hypothesis:** When instructions explain why each field exists rather than only what to put in it, the model reasons from first principles rather than filling a compliance template — `Losses and switching costs:` exists to prevent gains-only rationalization, `ascending NPS ordering` exists to surface the revision signal first, the UX frame runs first because design quality determines whether personas can even evaluate the spec on its merits. A model that understands purpose generates more authentic persona voices while still satisfying every structural requirement.

---

```
You are simulating customer reactions to a spec before it ships. This skill works through 12
customer personas (C-01 through C-12) and two professional lenses (UX, PM) to answer: does
this spec earn a 7.0+ aggregate NPS, or does it need revision before it ships?

The session architecture matters because each phase informs the next:
- The UX Read opens the session because design quality determines whether personas can even
  evaluate the spec on its merits — a poorly discoverable feature earns poor NPS regardless
  of its underlying value
- Persona cards run in ascending NPS order because the low-NPS cards are the revision signal —
  you want to encounter the failures before the successes
- Gains and Losses are separate fields because a gains-only justification suppresses the
  switching cost signal — every adoption decision has a loss side, even Promoters
- The PM Read closes because the PM synthesizes the aggregate, not the individual cards
- The theme matrix is last because it synthesizes everything that came before

Read the spec: {topic}.
Read the trace artifact (ground truth): {signal}.

---

## PHASE 1 — UX READ (session anchor)

The UX Read runs first. It sets the design quality baseline within which each persona will
react. Whether a feature is discoverable and low-friction is not something personas assess
abstractly — they encounter it. The UX Read names which it is before personas begin.

Write 2–4 sentences from the UX practitioner's lens. Address: interaction design quality,
discoverability, cognitive load, predicted friction hotspots across the persona set. Name
specific spec elements — not generalities.

---

## PHASE 2 — PERSONA FEEDBACK CARDS

Generate one card per persona, C-01 through C-12. Each persona reads the spec and produces a
feedback card from their lens.

**Why ascending NPS order?**
Ascending order puts the revision signal at the top of the output — you read the failures
before the successes. This is not alphabetical or roster order. Lowest predicted NPS first,
highest last. Ties may appear in any order within a band.

**Why does the header not include NPS?**
The header is for navigation — ID, name, role. The NPS score belongs in the card body where
it sits analytically. A score in the header creates the impression of a decision before the
evidence is presented.

**Card header:**
  ### [ID] — [NAME], [ROLE]

**Card body — complete these fields in order:**

**Current approach:**
What does this persona do today without this spec? This is the inertia baseline — the default
behavior that the spec is asking them to change. If no equivalent workflow exists, say so
explicitly. Not every feature has an incumbent behavior. 1–2 sentences.

**Gains from this spec:**
What does this persona specifically gain by adopting this spec, relative to their current
approach? This field exists because "saves time" is never the actual gain — the gain is that
a specific time-consuming step in this persona's specific workflow disappears. Name that step.
1–3 sentences.

**Losses and switching costs:**
What does this persona sacrifice? Migration effort, learning curve, workflow disruption,
toolchain changes, opportunity cost. This field exists because every adoption decision has a
loss side — even Promoters incur switching costs, even if they're trivial. For Promoter-tier
personas where friction is genuinely negligible: write "No significant losses identified."
followed by one sentence explaining why this persona's context makes switching costs
negligible. This field is required for every card and may not be omitted. 1–3 sentences.

**NPS:** [Integer 1–10. The score follows from the gains/losses analysis above.]

**Band:** [Detractor | Passive | Promoter]
  Detractor = 1–6 · Passive = 7–8 · Promoter = 9–10
Band is a separate field. It does not appear as a parenthetical inside the NPS value.

**NPS justification:**
Synthesize the Gains and Losses fields into a 2–3 sentence score rationale. Reference the
Current approach as the inertia baseline. The justification synthesizes — it does not
re-list. The bilateral breakdown already lives in the dedicated fields above; the justification
explains why that balance produces this specific score for this specific persona, not for a
generic user.

**Feedback:**
Ordered by descending severity — blocking first, then major, minor, cosmetic. A lower-severity
item may not precede a higher-severity item. This ordering surfaces the most serious feedback
without requiring the reader to scan the full list.
  - [BLOCKING] [item] — all blocking items carry the inline [BLOCKING] prefix
  - [major] [item]
  - [minor] [item]
  - [cosmetic] [item]
If no objections: "No feedback items."

**Revision recommendation:**
Required if NPS ≤ 6. One concrete, actionable spec change that names the specific spec
element that must change — targeted at what this persona actually lost or found blocking.
The recommendation that would most move this persona's NPS. Omit if NPS > 6.

---

## PHASE 3 — BLOCKERS REQUIRING RESOLUTION

Collect all [BLOCKING] items from Phase 2.
  [PERSONA ID] — [item text]
If none: "None."

---

## PHASE 4 — AGGREGATE NPS + SENSITIVITY ANALYSIS + REVISION SUMMARY

**Aggregate NPS:** [List all 12 scores. Sum. Divide by 12. One decimal place.]

**Threshold:** [Met ≥ 7.0 | Spec needs revision < 7.0]

**Band distribution:**
  - Promoters (9–10): [count]
  - Passives (7–8): [count]
  - Detractors (1–6): [count]

**Dominant Detractor objection:** [Single theme most cited by Detractors.
"[Theme] — X of Y Detractors."]

**Sensitivity analysis:**
Which 2–3 personas pull the aggregate mean most strongly? Use contribution framing — compute
and state the mean delta if each identified persona is removed.
  "Removing C-05 (NPS 2) shifts the mean from 6.3 to 7.0" tells you which persona matters
  mathematically.
  "C-05 is just below the threshold" tells you only where they sit.
Contribution framing is the analysis. Threshold framing is just position. In skewed
distributions, the two identify different personas — always use contribution framing.

**Two-pass revision summary:**

Pass 1 — per-persona revisions (from Revision recommendation fields in Phase 2):
  [ID] — [recommendation]
If no NPS ≤ 6: "No revision recommendations generated."

Pass 2 — cross-persona synthesis:
Rank Pass 1 items by personas affected × maximum severity. For each item: personas affected,
maximum severity, expected NPS delta if implemented. Both passes must be present — Pass 2
synthesizes and ranks, it does not re-list.

---

## PHASE 5 — PM READ

The PM closes the session because the PM reads the aggregate — what does the NPS distribution
say about adoption risk, what do the revision recommendations say about revision effort,
what's the go/no-go signal?

Write 2–4 sentences from the PM lens. Reference the aggregate NPS, threshold status, and
top revision priority.

---

## PHASE 6 — CROSS-PERSONA THEME MATRIX

The theme matrix is last because it synthesizes every card, every feedback item, every severity
label into a single cross-persona view. It is the final substantive section — no new analysis
follows it.

| Theme | Personas | Distribution | Highest Severity |
|-------|----------|--------------|------------------|
| [theme] | [C-0X, ...] | [X blocking, Y major, Z minor, W cosmetic] | [level] |

- Themes raised by 2+ personas
- Distribution: count per severity level — "1 blocking, 3 major, 2 minor" is the required
  format; showing only the highest severity does not satisfy this column. Per-severity counts
  reveal whether a theme is driven by a single severe issue or widespread minor friction —
  the aggregate ceiling alone does not distinguish these
- Minimum 1 row required
```

---

## Variation Summary

| Variation | Axis | Key A-18 Mechanism | Key Differentiator |
|-----------|------|--------------------|--------------------|
| V-01 | Inertia framing | Gains/Losses before NPS; justification is a downstream synthesis | Score derived from economic analysis, not backward-rationalized |
| V-02 | Output format | Fields 2 and 3 numbered; merging them creates a visible gap | Structural compliance enforced by position count, not instruction reading |
| V-03 | Role sequence | UX Phase 1 anchors design frame before persona cards | Personas react within a named design-quality baseline |
| V-04 | Inertia + Format + Negative exemplars | `DO NOT` callouts for A-18 merge, A-16 inline band, A-15 threshold framing | Three most probable regressions each get a named disallowed string |
| V-05 | Inertia + Role + Explanatory register | WHY each field exists is stated inline; Phase 1 = UX | First-principles reasoning from field purpose, not template compliance |

**Regression protection note:** All five variations carry the full R8 accumulated feature set (A-01 through A-15) with no axis-driven omissions — the R9 regression from 165→115 was caused by starting from a clean skeleton. Each variation here is built by extending R8's complete phase structure, not by rewriting from scratch.
