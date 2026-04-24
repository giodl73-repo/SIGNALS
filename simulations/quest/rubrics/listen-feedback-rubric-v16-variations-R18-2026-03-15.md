# listen-feedback — Round 18 Variations (Rubric v16)

**Rubric:** v16 (235 pts max)
**R17 baseline preserved:** All prior criteria C-01–C-05, R-01–R-03, A-01–A-28
**Round 18 primary target:** A-29 — CI or variance annotation includes the computation formula

Single-axis: V-01 (output format — formula-first two-part CI block), V-02 (phrasing register — fill-in formula template), V-03 (lifecycle emphasis — named statistical derivation phase).
Combinations: V-04 (formula-first block + named derivation phase + numbered manifests), V-05 (derivation phase + inertia sub-fields + conjunctive field enforcement + failure mode annotation).

---

## V-01 — Output Format: Formula-First Two-Part CI Block

**Variation axis:** Output format — the statistical spread annotation uses a mandatory two-part labeled structure: a `Formula:` sub-line states the derivation method, then a `Computed:` sub-line states the numeric result. A bare interval occupies one line; the formula-first structure requires two lines, making A-29 positionally verifiable by counting lines rather than parsing content.

**Hypothesis:** The bare-interval failure mode recurs because a single output line can hold both the CI value and the formula as an afterthought — or omit the formula entirely without producing a structural gap. A two-part sub-structure per statistical field eliminates this: the `Formula:` line must appear before the `Computed:` line. Omitting the formula leaves an empty labeled position, which is detectable by structure rather than by reading the values. V-02 from R17 showed the formula inline within a bracket expression; that form admitted the bare-interval pattern in prior rounds. Formula-first ordering makes the derivation method primary, not incidental.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) produce structured feedback cards. You compute aggregate NPS (threshold: 7.0) and aggregate adoption likelihood (adoption bar: 65%). A spec must clear both thresholds to be considered ready. The statistical spread section uses a formula-first two-part structure — formula stated before the computed value.

**INPUT:** The spec or design document provided in context.

---

### STEP 0 — STATUS QUO BASELINE

Before evaluating any persona, characterize what this spec is displacing. This baseline is the reference for all per-card gains and losses — without a named baseline, gains and losses become feature descriptions rather than delta computations.

**What the status quo delivers:** [2–3 sentences. What does the current approach actually provide? Why do teams stick with it?]

**Where the status quo falls short:** [2–3 sentences. What specific gaps or failure modes does the current approach have that this spec addresses?]

**Floor-level switching cost:** [1 sentence. The minimum every persona must give up, learn, or rebuild to adopt this spec.]

**Persona-specific workflow disruption:** [1 sentence. Which persona types bear the highest transition friction vs. the lowest?]

This baseline is the reference for all per-card gains, losses, and adoption assessments.

---

### EVALUATION PROTOCOL

For each persona, complete the following numbered fields in document order. **Omitting any numbered field for any card constitutes an incomplete card.**

1. **Current approach** — What this persona does TODAY without this spec. The specific tool, workflow, or absence of workflow. **First field in card body.** State explicitly if no equivalent workflow exists.
2. **Gains from this spec** — What changes for this persona relative to Field 1? State the delta from their current approach. Must draw from Step 0 "Where the status quo falls short:" — not a feature list. *(Paired with Field 3 — neither is complete without the other.)*
3. **Losses and switching costs** — What does this persona lose or sacrifice? Cover: switching cost, migration burden, retraining, workflow disruption, opportunity cost. Must draw from Step 0 "Floor-level switching cost:" and "Persona-specific workflow disruption:". *(Paired with Field 2 — neither is complete without the other.)* Promoter-tier: "No significant losses identified — [one sentence on why switching cost is low for this persona]."
4. **Willingness to adopt** — Behavioral adoption likelihood (0–100%). Adoption bar: 65%. Annotate: "Clears adoption bar (>=65%)" or "Adoption risk (<65%)."
5. **NPS score** — Assign NPS (1–10) after Fields 2–4 are complete. Separate labeled line.
6. **Band** — Detractor (1–6), Passive (7–8), Promoter (9–10). **Separate labeled field from Field 5.** Without Field 6 as a distinct field, band classification is lost when NPS values are extracted for aggregate analysis.
7. **NPS justification** — 2–4 sentences. Must name what this persona gains AND what they lose relative to Field 1. Both dimensions required. Must reference at least one named spec element.
8. **Feedback** — Severity: `[BLOCKING]` / Major / Minor / Cosmetic. Descending order within card. Prefix all blocking items `[BLOCKING]`. "No objections identified" if none.
9. **Revision recommendation** — One targeted change naming a specific spec element and what should change. Generic recommendations ("improve onboarding") do not satisfy this field.

**Completeness enforcement:** Produce all 9 fields for all 12 cards. Any card missing one or more fields is malformed.

---

### CARD FORMAT

```
### [C-XX] [Name] — [Role]

**Current approach:** [what they do today]

**Gains from this spec (paired with Losses):** [delta from current approach]

**Losses and switching costs (paired with Gains):** [losses; or "No significant losses identified — [explanation]"]

**Willingness to adopt:** [0–100%] — [Clears adoption bar (>=65%) | Adoption risk (<65%)]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [2–4 sentences: gains AND losses, both named; at least one named spec element]

**Feedback:**
- [BLOCKING] [item]
- Major: [item]
- Minor: [item]
- Cosmetic: [item]

**Revision recommendation:** [named spec element + specific change]
```

**Ordering:** Sort all 12 cards ascending by NPS (lowest first, highest last). Ties may appear in any order.

---

### AGGREGATE SECTION

**Aggregate NPS:** [mean of 12 NPS values, one decimal]
**Threshold (7.0):** MET | NOT MET — if NOT MET: "Spec requires revision before shipping"
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count, e.g., "Migration burden (4 of 5 Detractors)"]
**Adoption summary:** Clears adoption bar (>=65%): X of 12 | Below adoption bar (<65%): X of 12
**Adoption threshold (65%):** MET | NOT MET

**Statistical spread:**
- **Formula:** 95% CI = mean ± 1.96 · (SD / √12), where SD = sqrt(sum of squared deviations / 11)
- **Computed:** SD = [X.XX]; 95% CI [lower, upper] (±1.96·[SD value]/√12)

The `Formula:` sub-line is required. The `Computed:` sub-line must include the formula in parenthetical form alongside the numeric bounds — a bare interval without the formula parenthetical does not satisfy this field. Both sub-lines must be present; a bare CI value without a preceding formula line constitutes an incomplete statistical spread section.

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each persona, produce exactly **two direction-specific sub-bullets** in order — +1 first, -1 second. **Both bullets are required; a combined "±X" notation that presents a single symmetric value does not satisfy this section.** The +1 and -1 directions have asymmetric consequences near the 7.0 threshold: a Detractor shifting to Passive changes band distribution and may flip threshold status; a Passive shifting to Promoter does not.

**[C-XX] [Name] — NPS [N]:** [one sentence on why this persona's score weight is disproportionately high]
- **+1 direction:** If score shifts from [N] to [N+1], aggregate mean moves from [X.X] to [Y.Y]
- **-1 direction:** If score shifts from [N] to [N-1], aggregate mean moves from [X.X] to [Z.Z]

Repeat this two-bullet block for each identified high-influence persona. A reviewer verifies completeness by counting: each entry must contain exactly 2 direction bullets.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Field 9 of each card above.

**Pass 2 — Cross-persona tiered revision list:**
Synthesize all Field-9 entries into a tiered ranked list. Sort by: (a) personas affected, (b) maximum severity. Then assign each entry to an implementation cost tier:

**Low-cost revisions** (copy, label, messaging, or configuration changes):
1. [Spec change] — [X personas]; max severity: [level]

**High-cost revisions** (workflow redesign, architecture, integration, or new capability):
1. [Spec change] — [X personas]; max severity: [level]

Must contain 2 or more distinct spec changes total. If all items fall into one tier, produce a single labeled tier.

---

### PROFESSIONAL LENS

UX Read precedes PM Read in document order. UX observation must precede PM synthesis — PM strategic framing anchors UX reading if PM precedes UX, suppressing friction signals before they are independently recorded.

#### UX READ
3–5 sentences from a UX practitioner's lens. Cover: primary interaction pattern, friction or underspecified behavior across multiple personas, one priority change that reduces switching cost for the widest range of personas.

#### PM READ
3–5 sentences from a product manager's lens. Cover: customer problem fit given the Detractor and adoption-risk distribution, riskiest assumption, one pre-ship validation question.

#### CONVERGENCE STATEMENT
Required after both reads. Name: (a) the specific finding where UX and PM agree; (b) the specific point where they diverge. If no divergence, name the strongest shared conclusion and note the absence of divergence.

---

### CROSS-PERSONA THEME MATRIX

Final substantive section. No analytical content follows.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme name] | C-XX, C-YY, ... | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Per-severity counts required per row. Omit zero-count severity levels.

---

Write the artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input.

---
---

## V-02 — Phrasing Register: Fill-In Formula Template

**Variation axis:** Phrasing register — the aggregate statistical spread field instruction shows the required output in fill-in template form, with the computation formula as a required placeholder to populate. The template `95% CI [___] (±1.96·___/√12)` structurally cannot be satisfied by a bare interval: the parenthetical placeholder is part of the required format, not an optional annotation.

**Hypothesis:** Prior CI omissions arose from instructions that described what to compute without specifying the required output form. A template that shows `(±1.96·SD_value/√12)` as a required parenthetical converts the formula from descriptive guidance into a structural fill-in obligation: the evaluator must populate the SD value inside the formula, making the formula the form of the output, not commentary on it. An output that reads `95% CI [6.2, 7.8]` leaves a visible template gap; `95% CI [6.2, 7.8] (±1.96·0.9/√12)` fills all placeholders. The template form makes omission detectable without reading for meaning.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) produce structured feedback cards. The aggregate section includes statistical spread in a specific required output format — see the AGGREGATE SECTION below.

**INPUT:** The spec or design document provided in context.
**Threshold:** Aggregate NPS >= 7.0 = ready. Below 7.0 = flag for revision.

---

### STEP 0 — STATUS QUO BASELINE

Before evaluating any persona, characterize what this spec displaces. This baseline is the reference for all per-card gains and losses — without a named baseline, gains and losses become feature descriptions rather than delta computations.

**What the status quo delivers:** [2–3 sentences. What does the current approach actually provide? Why do teams stick with it?]

**Where the status quo falls short:** [2–3 sentences. What specific gaps does the current approach have that this spec addresses?]

**Floor-level switching cost:** [1 sentence. The minimum every persona must give up, learn, or rebuild to adopt this spec.]

**Persona-specific workflow disruption:** [1 sentence. Which persona types bear the highest vs. lowest transition friction?]

---

### EVALUATION PROTOCOL

For each of the 12 customer personas, complete the following fields in document order. **Omitting any numbered field for any card constitutes an incomplete card.**

1. **Current approach** — What this persona does TODAY without this spec. First field in card body. State explicitly if no equivalent workflow exists.
2. **Gains from this spec** — Delta from Field 1. State the change, not the feature list. Draw from Step 0 "Where the status quo falls short:". *(Paired with Field 3 — Field 2 is incomplete without Field 3.)*
3. **Losses and switching costs** — What this persona loses or sacrifices. Draw from Step 0 "Floor-level switching cost:" and "Persona-specific workflow disruption:". *(Paired with Field 2 — Field 3 is incomplete without Field 2.)* Promoter-tier: "No significant losses identified — [one sentence on why friction is low]."
4. **Willingness to adopt** — Adoption likelihood (0–100%). Adoption bar: 65%. Label: "Clears adoption bar (>=65%)" or "Adoption risk (<65%)."
5. **NPS score** — Integer 1–10, after Fields 2–4. Separate labeled line.
6. **Band** — Detractor (1–6) / Passive (7–8) / Promoter (9–10). Separate labeled field from Field 5.
7. **NPS justification** — 2–4 sentences naming gains AND losses relative to Field 1. Both dimensions required. Must reference at least one named spec element.
8. **Feedback** — `[BLOCKING]` / Major / Minor / Cosmetic. Descending severity within card. Prefix blocking items `[BLOCKING]`. "No objections identified" if none.
9. **Revision recommendation** — Named spec element + specific change. Generic recommendations do not satisfy this field.

**Ordering:** Sort all 12 completed cards ascending by NPS (lowest first, highest last).

---

### CARD FORMAT

```
### [C-XX] [Name] — [Role]

**Current approach:** [what they do today]

**Gains from this spec (paired with Losses and switching costs):** [delta from current approach]

**Losses and switching costs (paired with Gains from this spec):** [losses; or "No significant losses identified — [explanation]"]

**Willingness to adopt:** [0–100%] — [Clears adoption bar (>=65%) | Adoption risk (<65%)]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [gains AND losses, both named; named spec element cited]

**Feedback:**
- [BLOCKING] [item]
- Major: [item]
- Minor: [item]
- Cosmetic: [item]

**Revision recommendation:** [named spec element + specific change]
```

---

### AGGREGATE SECTION

Produce the following fields. The statistical spread field uses a required output template — populate all placeholders.

**Aggregate NPS:** [mean of 12 NPS scores, one decimal]

**Threshold (7.0):** MET | NOT MET — if NOT MET: "Spec requires revision before shipping"

**Band distribution:** Promoters: [X] | Passives: [X] | Detractors: [X]

**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count of Detractors citing it]

**Adoption summary:** Clears adoption bar (>=65%): [X] of 12 | Below adoption bar (<65%): [X] of 12

**Standard deviation:** SD = [X.XX]

**95% confidence interval:** 95% CI [[lower], [upper]] (±1.96·[SD_value]/√12)

> **Required output format for the CI field:** The parenthetical formula `(±1.96·[SD_value]/√12)` must be populated with the actual computed SD value and appear immediately after the bracket interval. A CI that reads only `95% CI [6.2, 7.8]` without the formula parenthetical is an incomplete field. The SD value inside the formula must match the SD field above — these two fields are linked: an evaluator who omits the formula also loses the cross-check between SD and CI. Correct form: `95% CI [6.2, 7.8] (±1.96·0.9/√12)`.

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each, produce two direction-specific bullets in this order — +1 first, -1 second. **Both bullets are required; a collapsed "±X" figure does not satisfy this section.**

**[C-XX] [Name] — NPS [N]:** [one sentence explaining disproportionate influence]
- **+1 direction:** If score shifts from [N] to [N+1], aggregate mean moves from [X.X] to [Y.Y]
- **-1 direction:** If score shifts from [N] to [N-1], aggregate mean moves from [X.X] to [Z.Z]

Repeat this two-bullet block for each identified high-influence persona. Each entry must contain exactly 2 direction bullets; a reviewer verifies by counting.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Field 9 of each card above.

**Pass 2 — Cross-persona tiered revision list:**
Rank by: (a) personas affected, (b) maximum severity. Apply implementation cost tiers:

**Low-cost revisions** (copy, label, messaging, configuration):
1. [Spec change] — [X personas]; max severity: [level]

**High-cost revisions** (workflow, architecture, integration, new capability):
1. [Spec change] — [X personas]; max severity: [level]

Must contain 2 or more distinct spec changes total.

---

### PROFESSIONAL LENS

UX Read precedes PM Read in document order. UX observation must precede PM synthesis — PM strategic framing anchors UX reading if PM precedes UX, suppressing friction signals before they are independently recorded.

#### UX READ
3–5 sentences. Primary interaction pattern, friction across multiple personas, one priority change.

#### PM READ
3–5 sentences. Customer problem fit given the Detractor distribution, riskiest assumption, one pre-ship validation question.

#### CONVERGENCE STATEMENT
Required. Name where UX and PM agree and where they diverge. If no divergence, name the strongest shared conclusion.

---

### CROSS-PERSONA THEME MATRIX

Final substantive section.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme name] | C-XX, C-YY, ... | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Per-severity counts required per row. Omit zero-count severity levels.

---

Write the artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input.

---
---

## V-03 — Lifecycle Emphasis: Named Statistical Derivation Phase

**Variation axis:** Lifecycle emphasis — statistical computation is a named phase (PHASE 4: STATISTICAL DERIVATION) that executes before the aggregate section, with formula statement as its first required sub-step. The phase gate means the formula cannot be omitted because it is the required input to the phase, not an annotation on the output.

**Hypothesis:** CI formulas are omitted when the instruction frames them as annotations to a result already in hand — "add the CI formula after the mean." A named derivation phase reverses this: the formula is stated first (Step 4.1), SD is computed second (Step 4.2), the CI is applied third (Step 4.3), and the combined result is reported fourth (Step 4.4). The formula is the starting point of the phase, not a parenthetical on the output line. An evaluator who enters Phase 4 must state the formula before they can exit it — the formula is structurally prior, not structurally optional. Without the named phase boundary, the formula instruction competes with output content for the evaluator's attention; the phase gate makes formula derivation the exclusive work of a distinct named step.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) produce structured feedback cards. The output follows four named phases. Statistical computation runs in PHASE 4 before the aggregate section is written, with formula derivation as the first required step of that phase.

**INPUT:** The spec or design document provided in context.
**Threshold:** Aggregate NPS >= 7.0 = ready. Below 7.0 = flag for revision.

---

### PHASE 1 — STATUS QUO BASELINE

Characterize what this spec displaces. All per-card gains and losses in PHASE 2 are delta computations against this baseline.

**What the status quo delivers:** [2–3 sentences. What does the current approach provide? Why do teams use it?]

**Where the status quo falls short:** [2–3 sentences. What gaps does the current approach have that this spec addresses?]

**Floor-level switching cost:** [1 sentence. Minimum every persona bears to adopt this spec.]

**Persona-specific workflow disruption:** [1 sentence. Highest vs. lowest friction by persona type.]

---

### PHASE 2 — PERSONA CARDS (12 required)

For each of the 12 customer personas, complete the following fields in document order. **Omitting any numbered field constitutes an incomplete card.**

1. **Current approach** — What this persona does TODAY. First field in card body. Explicit if no equivalent workflow exists.
2. **Gains from this spec** — Delta from Field 1. Draw from Phase 1 "Where the status quo falls short:". *(Paired with Field 3 — neither is complete without the other.)*
3. **Losses and switching costs** — What this persona sacrifices. Draw from Phase 1 "Floor-level switching cost:" and "Persona-specific workflow disruption:". *(Paired with Field 2 — neither is complete without the other.)* Promoter-tier: "No significant losses identified — [one sentence]."
4. **Willingness to adopt** — Likelihood (0–100%). Adoption bar: 65%. Label result.
5. **NPS score** — Integer 1–10. After Fields 2–4.
6. **Band** — Detractor (1–6) / Passive (7–8) / Promoter (9–10). Separate field from Field 5.
7. **NPS justification** — 2–4 sentences: gains AND losses named, relative to Field 1; named spec element cited.
8. **Feedback** — `[BLOCKING]` / Major / Minor / Cosmetic. Descending severity. Prefix blocking items `[BLOCKING]`. "No objections identified" if none.
9. **Revision recommendation** — Named spec element + specific change.

**Card header:** `### [C-XX] [Name] — [Role]` — identifier, name, role only.
**Ordering:** Sort all 12 completed cards ascending by NPS (lowest first).

```
### [C-XX] [Name] — [Role]

**Current approach:** [...]

**Gains from this spec (paired with Losses and switching costs):** [...]

**Losses and switching costs (paired with Gains from this spec):** [...]

**Willingness to adopt:** [0–100%] — [threshold annotation]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [...]

**Feedback:**
- [BLOCKING] [item]
- Major: [item]
- Minor: [item]
- Cosmetic: [item]

**Revision recommendation:** [...]
```

---

### PHASE 3 — PROFESSIONAL LENS

UX Read precedes PM Read. **UX observation must precede PM synthesis — PM strategic framing anchors UX reading if PM precedes UX, suppressing friction signals before they are independently recorded.**

#### UX READ
3–5 sentences. Primary interaction pattern, friction across multiple personas, one priority change.

#### PM READ
3–5 sentences. Customer problem fit given Detractor distribution, riskiest assumption, one pre-ship validation question.

#### CONVERGENCE STATEMENT
Required. Name where UX and PM agree. Name where they diverge. If no divergence, state that and name the strongest shared conclusion.

---

### PHASE 4 — STATISTICAL DERIVATION

Execute steps 4.1 through 4.4 in order before writing the aggregate section. Do not skip steps or merge them.

**Step 4.1 — State the CI formula:**
The 95% confidence interval for a sample of n = 12 is computed as:
`95% CI = mean ± 1.96 · (SD / √12)`
where SD is the sample standard deviation computed over 11 degrees of freedom.

**Step 4.2 — Compute SD:**
From the 12 NPS scores in Phase 2, compute:
`SD = sqrt(sum of (xi − mean)^2 / 11)` over all 12 personas.
State: `SD = [computed value]`

**Step 4.3 — Apply the formula:**
Lower bound = mean − 1.96 · (SD / 3.464), rounded to one decimal.
Upper bound = mean + 1.96 · (SD / 3.464), rounded to one decimal.
State: `CI lower = [value]; CI upper = [value]`

**Step 4.4 — Produce the combined statistical spread annotation:**
Report as: `95% CI [lower, upper] (±1.96·[SD_value]/√12)`
This is the required output form. The parenthetical `(±1.96·[SD_value]/√12)` must include the actual computed SD value — a bare interval without the formula parenthetical is an incomplete Phase 4 output.

---

### PHASE 5 — AGGREGATE SECTION

Using the Phase 4 statistical derivation, produce the following:

**Aggregate NPS:** [mean, one decimal]
**Threshold (7.0):** MET | NOT MET — if NOT MET: "Spec requires revision before shipping"
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count]
**Adoption summary:** Clears adoption bar (>=65%): X of 12 | Below adoption bar (<65%): X of 12
**Statistical spread:** [Phase 4 Step 4.4 output — `95% CI [lower, upper] (±1.96·[SD_value]/√12)`]

---

### PHASE 6 — SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each, produce exactly two direction-specific sub-bullets. **Both bullets required; a collapsed "±X" figure does not satisfy this section.**

**[C-XX] [Name] — NPS [N]:** [one sentence on disproportionate influence]
- **+1 direction:** If score shifts from [N] to [N+1], aggregate mean moves from [X.X] to [Y.Y]
- **-1 direction:** If score shifts from [N] to [N-1], aggregate mean moves from [X.X] to [Z.Z]

Repeat two-bullet block for each identified persona. Each entry must contain exactly 2 direction bullets.

---

### PHASE 7 — BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### PHASE 8 — TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Field 9 of each card in Phase 2.

**Pass 2 — Cross-persona tiered revision list:**
Rank by (a) personas affected, (b) maximum severity. Apply implementation cost tiers:

**Low-cost revisions** (copy, label, messaging, configuration):
1. [Spec change] — [X personas]; max severity: [level]

**High-cost revisions** (workflow, architecture, integration, new capability):
1. [Spec change] — [X personas]; max severity: [level]

Must contain 2 or more distinct spec changes total.

---

### PHASE 9 — CROSS-PERSONA THEME MATRIX

Final substantive section. No analytical content follows.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme name] | C-XX, C-YY, ... | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Per-severity counts required per row. Omit zero-count severity levels.

---

Write the artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input.

---
---

## V-04 — Combination: Formula-First CI Block + Named Derivation Phase + Numbered Manifests

**Variation axes:** Output format (formula-first two-part CI block from V-01) + lifecycle emphasis (named statistical derivation phase from V-03) + numbered field manifests at persona card level (A-13/A-23) and aggregate level (A-26) with explicit completeness enforcement rules at all tiers.

**Hypothesis:** V-01 makes A-29 positionally verifiable at the output level — the formula line must be present or its position is empty. V-03 makes A-29 sequentially enforced at the process level — the formula is the required input to a named phase, not the output. Combining both closes two independent failure modes: the output-level gap (bare interval with no formula line) and the process-level gap (formula described but skipped). Numbered manifests extend positional verifiability to the entire output: card completeness is verified by counting to 9, aggregate completeness by counting to A6, statistical derivation by verifying both sub-lines are present. The combination means any omission produces a structural gap detectable by counting rather than reading.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) produce structured feedback cards using the PERSONA CARD MANIFEST below. The aggregate section follows the AGGREGATE MANIFEST. Statistical spread uses a formula-first two-part structure derived in a named derivation phase. **Omitting any numbered field at any tier constitutes a malformed output.**

**INPUT:** The spec or design document provided in context.
**Threshold:** Aggregate NPS >= 7.0 = ready. Below 7.0 = flag for revision.

---

### STEP 0 — STATUS QUO BASELINE

Before evaluating any persona, characterize what this spec displaces. Without a named baseline, gains and losses become feature descriptions rather than delta computations.

**What the status quo delivers:** [2–3 sentences. What does the current approach actually provide? Why do teams stick with it?]

**Where the status quo falls short:** [2–3 sentences. What specific gaps does the current approach have that this spec addresses?]

**Floor-level switching cost:** [1 sentence. The minimum every persona must give up, learn, or rebuild.]

**Persona-specific workflow disruption:** [1 sentence. Highest vs. lowest friction by persona type.]

---

### PERSONA CARD MANIFEST

Every persona card must instantiate all 9 fields in this numbered order. **Omitting any numbered field for any persona constitutes an incomplete card and must be corrected before the output is considered valid.**

| # | Label | Constraint |
|---|-------|------------|
| 1 | `**Current approach:**` | What this persona does today without the spec. Required even if no equivalent workflow exists — state "No equivalent workflow exists" explicitly. **First field in card body.** Without this field, Fields 2 and 3 have no baseline — gains and losses become feature descriptions, and NPS justification cannot be verified as inertia-comparative. |
| 2 | `**Gains from this spec (paired with Losses and switching costs):**` | Delta from Field 1. Draw from Step 0 "Where the status quo falls short:". Neither Field 2 nor Field 3 is complete without the other — completing Gains without Losses constitutes an incomplete card. |
| 3 | `**Losses and switching costs (paired with Gains from this spec):**` | What this persona loses or sacrifices. Draw from Step 0 "Floor-level switching cost:" and "Persona-specific workflow disruption:". Neither Field 3 nor Field 2 is complete without the other — completing Losses without Gains constitutes an incomplete card. Promoter-tier: "No significant losses identified — [one sentence grounding this in Step 0 switching cost]." |
| 4 | `**Willingness to adopt:**` | Adoption likelihood (0–100%). Adoption bar: 65%. Annotate: "Clears adoption bar (>=65%)" or "Adoption risk (<65%)". |
| 5 | `**NPS:**` | Integer 1–10. Must appear after Fields 2–4. Score follows evidence. |
| 6 | `**Band:**` | "Detractor" (1–6), "Passive" (7–8), or "Promoter" (9–10). **Separate labeled field from Field 5.** Without Field 6 as a distinct field, band classification is lost when NPS values are extracted for aggregate analysis. |
| 7 | `**NPS justification:**` | 2–4 sentences. Must name gains (Field 2) AND losses (Field 3) relative to Field 1. Both dimensions required. Must reference at least one named spec element. |
| 8 | `**Feedback:**` | Descending severity: `[BLOCKING]` first, then Major, then Minor, then Cosmetic. `[BLOCKING]` prefix on all blocking items. "No objections identified" if none. |
| 9 | `**Revision recommendation:**` | Named spec element + specific change. Generic recommendations do not satisfy this field. |

**Card header:** `### [C-XX] [Name] — [Role]` — identifier, name, and role only.
**Completeness enforcement rule:** Any card missing one or more manifest fields is malformed. Produce all 9 fields for all 12 cards.

**Card ordering:** Sort all 12 completed cards ascending by NPS (lowest first, highest last). **Without ascending-NPS ordering, Detractor-tier personas are buried in document sequence — their contribution to the aggregate mean requires cross-referencing rather than being immediately visible at the top of the output.** Ties may appear in any order.

---

### STATISTICAL DERIVATION PHASE

Execute before writing the aggregate section. Do not skip steps or merge them. The formula is stated first; the numeric result follows from it.

**Step D.1 — State the CI formula:**
`95% CI = mean ± 1.96 · (SD / √12)`
SD is the sample standard deviation over 11 degrees of freedom.

**Step D.2 — Compute SD:**
`SD = sqrt(sum of (xi − mean)^2 / 11)` over the 12 persona NPS scores.
State: `SD = [value]`

**Step D.3 — Apply:**
Lower = mean − 1.96 · (SD / 3.464); Upper = mean + 1.96 · (SD / 3.464).
State: `CI lower = [value]; CI upper = [value]`

**Step D.4 — Produce the A6 formula annotation:**
`95% CI [lower, upper] (±1.96·[SD_value]/√12)`
This is the required output form for aggregate field A6. The parenthetical must include the actual computed SD value. A bare interval is an incomplete Step D.4 output.

---

### AGGREGATE MANIFEST

After all 12 persona cards, produce the following fields in this numbered order. **Omitting any numbered aggregate field constitutes an incomplete aggregate section and must be corrected before the output is considered valid.**

| # | Field | Format |
|---|-------|--------|
| A1 | `**Aggregate NPS:**` | Mean of 12 NPS values, one decimal. |
| A2 | `**Threshold (7.0):**` | "MET" or "NOT MET — spec requires revision before shipping." |
| A3 | `**Band distribution:**` | "Promoters: X \| Passives: X \| Detractors: X" |
| A4 | `**Dominant Detractor objection:**` | Single most common blocking or major theme among Detractor-tier personas, with count (e.g., "Config migration burden (4 of 5 Detractors)"). Separate labeled field — not embedded in A3. |
| A5 | `**Adoption summary:**` | "Clears adoption bar (>=65%): X of 12 \| Below adoption bar (<65%): X of 12" |
| A6 | `**Statistical spread:**` | Two-part formula-first structure: (a) `**Formula:** 95% CI = mean ± 1.96·(SD/√12)` on one labeled line; (b) `**Computed:** SD = [value]; 95% CI [lower, upper] (±1.96·[SD_value]/√12)` on a second labeled line. Both lines required. A bare interval without the formula line constitutes an incomplete A6. |

**Aggregate completeness enforcement rule:** All 6 aggregate fields (A1–A6) must be present. Counting to A6 in document order verifies completeness without parsing labels.

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each, produce exactly **two direction-specific sub-bullets** — +1 first, -1 second. **Both bullets required; a collapsed "±X" figure does not satisfy this section.** The +1 and -1 directions are asymmetric near the 7.0 threshold — a Detractor-to-Passive shift changes band distribution and may cross the threshold; a Passive-to-Promoter shift does not.

**[C-XX] [Name] — NPS [N]:** [one sentence on disproportionate influence]
- **+1 direction:** If score shifts from [N] to [N+1], aggregate mean moves from [X.X] to [Y.Y]
- **-1 direction:** If score shifts from [N] to [N-1], aggregate mean moves from [X.X] to [Z.Z]

Repeat two-bullet block for each identified high-influence persona. A reviewer verifies completeness by counting: each entry must contain exactly 2 direction bullets.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Field 9 of each card above.

**Pass 2 — Cross-persona tiered revision list:**
Rank by: (a) personas affected, (b) maximum severity. Assign to implementation cost tiers:

**Low-cost revisions** (copy, label, messaging, configuration):
1. [Spec change] — [X personas]; max severity: [level]

**High-cost revisions** (workflow, architecture, integration, new capability):
1. [Spec change] — [X personas]; max severity: [level]

Must contain 2 or more distinct spec changes total. If all items fall into one tier, produce a single labeled tier and explain why.

---

### PROFESSIONAL LENS

UX Read precedes PM Read. **UX observation must precede PM synthesis — PM strategic framing anchors UX reading if PM precedes UX, suppressing friction signals before they are independently recorded.**

#### UX READ
3–5 sentences. Primary interaction pattern, friction across multiple personas, one priority change.

#### PM READ
3–5 sentences. Customer problem fit given Detractor distribution, riskiest assumption, one pre-ship validation question.

#### CONVERGENCE STATEMENT
Required after both reads. Name where UX and PM agree and where they diverge. If no divergence, name the strongest shared conclusion and note the absence of divergence.

---

### CROSS-PERSONA THEME MATRIX

Final substantive section. No analytical content follows.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme name] | C-XX, C-YY, ... | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Per-severity counts required per row. Omit zero-count severity levels.

---

Write the artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input.

---
---

## V-05 — Combination: Derivation Phase + Inertia Sub-Fields + Conjunctive Field Enforcement + Failure Mode Annotation

**Variation axes:** Lifecycle emphasis (named statistical derivation phase from V-03) + inertia framing (Step 0 with 4 named sub-fields cross-referenced in Field 2 and Field 3, A-16/A-24) + conjunctive gains/losses field instructions naming each other by label (A-21) + failure mode annotation on A-29 constraint (A-27 applied to the formula requirement: names the output failure that a bare CI prevents from being detected).

**Hypothesis:** A-29 failures arise from two distinct patterns: (1) the formula is absent from the instruction, and (2) the formula is present in the instruction but absent from the output because the instruction described it as an annotation rather than as a process step. V-03 addresses pattern 2 via a named derivation phase. A-27 addresses pattern 1 differently: naming the output failure that a bare CI creates converts the formula requirement from a format constraint into a self-explaining contract. A reader who understands that "a CI without its computation formula cannot be verified against different score inputs — the evaluator cannot tell whether ±1.96·SD/√12 or a different method was used" is less likely to satisfy the constraint superficially. The three inertia enforcement layers (A-17 bilateral instruction, A-21 conjunctive framing, A-24 named sub-field cross-reference) are retained from R17 V-05 as structural enforcement on gains/losses; the A-29 failure mode annotation is the new layer targeted at Round 18.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) evaluate the spec. Every gains/losses assessment is a delta computation against the named status quo baseline in Step 0. All per-persona gains and losses must trace back to specific Step 0 sub-fields. Statistical spread uses a named derivation phase with formula-first ordering.

**INPUT:** The spec or design document provided in context.
**Threshold:** Aggregate NPS >= 7.0 = ready. Below 7.0 = flag for revision.

---

### STEP 0 — STATUS QUO BASELINE

Before evaluating any persona, characterize what this spec is displacing. **Without a named baseline, gains and losses become feature descriptions rather than delta computations, and NPS justifications cannot be verified as inertia-comparative.**

**What the status quo delivers:** [2–3 sentences. What does the current approach actually provide? Why do teams stick with it? What does it do well enough that switching feels optional?]

**Where the status quo falls short:** [2–3 sentences. What specific gaps or failure modes does the current approach have that this spec addresses? Name them — these are the gains that matter.]

**Floor-level switching cost:** [1 sentence. What is the minimum every persona must give up, learn, or rebuild to adopt this spec, regardless of individual context?]

**Persona-specific workflow disruption:** [1 sentence. Which persona types bear the highest transition friction, and which bear the lowest? Name the contrast.]

---

### EVALUATION PROTOCOL

For each of the 12 customer personas, complete the following fields in document order:

**Field 1 — Current approach**
How does this persona specifically experience the status quo from Step 0? What tool, workflow, or manual process do they use today? If no equivalent workflow exists, state it explicitly.

**Field 2 — Gains from this spec** *(paired with Field 3, Losses and switching costs)*
What does this persona gain by switching from Field 1 to the spec? State gains as deltas computed from Step 0 "Where the status quo falls short:" — what the status quo cannot provide that this persona now gets. **Neither Field 2 nor Field 3 is complete without the other: completing Gains without completing Losses constitutes an incomplete card.** Gains that cannot be grounded in a named Step 0 failure mode are feature descriptions, not delta computations.

**Field 3 — Losses and switching costs** *(paired with Field 2, Gains from this spec)*
What does this persona lose or sacrifice to adopt the spec? Compute losses from Step 0 "Floor-level switching cost:" (the base cost all personas bear) and "Persona-specific workflow disruption:" (the additional friction this persona's role carries). **Neither Field 3 nor Field 2 is complete without the other: completing Losses without completing Gains constitutes an incomplete card.** Promoter-tier: "No significant losses identified — [one sentence grounding this conclusion in this persona's relationship to Step 0 'Floor-level switching cost:']."

**Field 4 — Willingness to adopt**
Adoption likelihood (0–100%). Adoption bar: 65%. Annotate: "Clears adoption bar (>=65%)" or "Adoption risk (<65%)."

**Field 5 — NPS score (after evidence)**
Assign NPS (1–10) and band on a separate labeled line, after Fields 2–4 are complete:
- 1–6: Detractor
- 7–8: Passive
- 9–10: Promoter

**Field 6 — NPS justification**
2–4 sentences. Must name gains (Field 2) AND losses (Field 3) relative to Field 1. Both dimensions required. Must reference at least one named spec element.

**Field 7 — Feedback**
Severity: `[BLOCKING]` / Major / Minor / Cosmetic. Descending order within card. `[BLOCKING]` prefix on blocking items. "No objections identified" if none.

**Field 8 — Revision recommendation**
One specific change naming a spec element and what should change to improve this persona's NPS. Generic recommendations do not satisfy this field.

---

### CARD FORMAT

```
### [C-XX] [Name] — [Role]

**Current approach:** [specific to this persona; how their experience of Step 0 differs from the general characterization]

**Gains from this spec (paired with Losses and switching costs):** [delta from Field 1 computed from Step 0 "Where the status quo falls short:"]

**Losses and switching costs (paired with Gains from this spec):** [losses computed from Step 0 "Floor-level switching cost:" and "Persona-specific workflow disruption:"; or "No significant losses identified — [Step 0 grounding]" for Promoter-tier]

**Willingness to adopt:** [0–100%] — [threshold annotation]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [gains AND losses, both named, relative to Field 1; at least one named spec element]

**Feedback:**
- [BLOCKING] [item]
- Major: [item]
- Minor: [item]
- Cosmetic: [item]

**Revision recommendation:** [named spec element + specific change]
```

**Ordering:** Sort all 12 cards ascending by NPS (lowest first). Ties may appear in any order.

---

### STATISTICAL DERIVATION PHASE

Execute before the aggregate section. Steps must be completed in order. The formula is the starting point; the numeric value follows from it.

**Step S.1 — State the CI formula:**
The output of this phase must take the form: `95% CI [lower, upper] (±1.96·[SD_value]/√12)`.

**Without the formula parenthetical `(±1.96·[SD_value]/√12)` alongside the interval, the CI annotation cannot be verified against different score inputs — a reader cannot confirm whether the interval was computed as ±1.96·SD/√12 or via a different method. A bare interval converts the statistical annotation from a reproducible computation into a black-box figure. The formula is not an annotation on the CI; it is the CI's derivation method, which must be transparent for the annotation to be auditable.**

Formula: `95% CI = mean ± 1.96 · (SD / √12)`, where SD = sample standard deviation over 11 degrees of freedom.

**Step S.2 — Compute SD:**
`SD = sqrt(sum of (xi − mean)^2 / 11)` over the 12 persona NPS scores.
State: `SD = [computed value]`

**Step S.3 — Apply the formula:**
Lower = mean − 1.96 · (SD / 3.464); Upper = mean + 1.96 · (SD / 3.464); round to one decimal.
State: `CI lower = [value]; CI upper = [value]`

**Step S.4 — Write the required annotation:**
`95% CI [lower, upper] (±1.96·[SD_value]/√12)` — populate SD_value with the result from Step S.2. This exact form carries to the aggregate section.

---

### AGGREGATE SECTION

**Aggregate NPS:** [mean of 12 scores, one decimal]
**Threshold (7.0):** MET | NOT MET — if NOT MET: "Spec requires revision before shipping"
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count]
**Adoption summary:** Clears adoption bar (>=65%): X of 12 | Below adoption bar (<65%): X of 12
**Statistical spread:** [Step S.4 output — `95% CI [lower, upper] (±1.96·[SD_value]/√12)`]

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each, state both the +1 direction and the -1 direction as **separate numeric figures**:

**[C-XX] [Name] — NPS [N]:** [why this persona's score weight is disproportionately high]
- **If shifted to [N+1]:** aggregate mean moves from [X.X] to [Y.Y]
- **If shifted to [N-1]:** aggregate mean moves from [X.X] to [Z.Z]

**Why both directions must be stated separately:** Without the +1 and -1 figures as distinct values, a spec that survives a best-case swing but fails under a worst-case one cannot be detected from this output. A +1 shift on a Detractor-tier persona may move the aggregate above the 7.0 threshold; a -1 shift on that same persona does not cross a band boundary in the opposite direction if the aggregate is already below threshold. Collapsing both into ±X hides this asymmetry: "±0.08" presents both directions as equivalent when they are structurally distinct events with opposite decision consequences.

Repeat this block for each high-influence persona.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Each card's Field 8 above.

**Pass 2 — Cross-persona tiered revision list:**
Rank by: (a) personas affected, (b) maximum severity. Assign to implementation cost tiers:

**Low-cost revisions** (copy, label, messaging, or configuration changes):
1. [Spec change] — [X personas]; max severity: [level]

**High-cost revisions** (workflow redesign, architecture, integration, new capability):
1. [Spec change] — [X personas]; max severity: [level]

Must contain 2 or more distinct spec changes total. If all items fall into one tier, produce a single labeled tier and state why.

---

### PROFESSIONAL LENS

UX Read precedes PM Read. **UX observation must precede PM synthesis — PM strategic framing anchors UX reading if PM precedes UX, suppressing friction signals before they are independently recorded.**

#### UX READ
3–5 sentences. Primary interaction pattern, friction across multiple personas, one priority change that reduces switching cost for the widest range of personas.

#### PM READ
3–5 sentences. Customer problem fit given Detractor distribution and Step 0 baseline, riskiest assumption, one pre-ship validation question.

#### CONVERGENCE STATEMENT
Required after both reads.
- **Where UX and PM agree:** Name the specific finding or recommendation both reads converge on.
- **Where UX and PM diverge:** Name the specific point of disagreement and what the divergence reveals about the design trade-off.

If the reads agree on everything, name the strongest shared conclusion and note the absence of divergence.

---

### CROSS-PERSONA THEME MATRIX

Final substantive section. No analytical content follows.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme name] | C-XX, C-YY, ... | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Per-severity counts required per row. Omit zero-count severity levels.

---

Write the artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input.
