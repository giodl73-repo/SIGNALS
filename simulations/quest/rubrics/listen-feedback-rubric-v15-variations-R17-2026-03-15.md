# listen-feedback — Round 17 Variations (Rubric v15)

**Rubric:** v15 (230 pts max)
**R16 baseline preserved:** All prior criteria C-01–C-05, R-01–R-03, A-01–A-27
**Round 17 primary target:** A-28 — sensitivity analysis states +1 and -1 swing directions as distinct figures

Single-axis: V-01 (output format — two-bullet directional block), V-02 (lifecycle emphasis — threshold-proximity annotation), V-03 (phrasing register — causal band-transition narrative).
Combinations: V-04 (two-bullet directional format + numbered manifests A-23/A-26), V-05 (directional separation + inertia sub-fields + failure mode annotation A-27).

---

## V-01 — Output Format: Two-Bullet Directional Sensitivity Block

**Variation axis:** Output format — each sensitivity entry uses a mandatory two-bullet structure (+1 bullet, -1 bullet), making A-28 directional separation positionally verifiable by counting rather than parsing.

**Hypothesis:** The collapsed ±1 notation recurs because a single prose sentence can hold both directions ("mean moves from X.X to Y.Y"). A two-bullet sub-structure per persona eliminates this: the ±1 form can only occupy one bullet, not two. If either bullet is absent the entry is structurally incomplete — a reviewer detects the omission by counting bullets, not by reading the values. V-01 through V-03 Round 16 all used a single delta sentence that admitted collapse; a two-bullet structure makes that form architecturally impossible.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) evaluate the spec and produce scored feedback cards. You compute aggregate NPS (threshold: 7.0) and aggregate adoption likelihood (adoption bar: 65%). A spec must clear both thresholds to be considered ready.

**INPUT:** The spec or design document provided in context.

---

### STEP 0 — STATUS QUO BASELINE

Before evaluating any persona, characterize what this spec must displace.

**What teams do today instead:** [2–3 sentences: the current approach, what it delivers, and why people stick with it]

**Where it falls short:** [2–3 sentences: the specific gaps this spec addresses]

**Floor-level switching cost:** [1 sentence: the minimum anyone must give up or learn to adopt this spec]

**Persona-specific workflow disruption:** [1 sentence: transition friction that varies by persona type — who is most disrupted vs. least]

This baseline is the reference for all per-card gains, losses, and adoption likelihood assessments.

---

### EVALUATION PROTOCOL

For each persona, complete the following numbered fields in document order. **Omitting any numbered field for any card constitutes an incomplete card.**

1. **Current approach** — What this persona does TODAY without this spec. The specific tool, workflow, or absence of workflow. **First field in card body.** State explicitly if no equivalent workflow exists.
2. **Gains from this spec** — What changes for this persona relative to Field 1? State the delta, not the feature list.
3. **Losses and switching costs** — What does this persona lose or sacrifice? Cover switching cost, migration burden, retraining, workflow disruption, opportunity cost. Promoter-tier: "No significant losses identified — [one sentence on why switching cost is low]."
4. **Willingness to adopt** — Behavioral adoption likelihood (0–100%). Adoption bar: 65%. Annotate: "Clears adoption bar (>=65%)" or "Adoption risk (<65%)."
5. **NPS score** — Assign NPS (1–10) after Fields 2–4 are complete. Separate labeled line.
6. **Band** — Detractor (1–6), Passive (7–8), Promoter (9–10). Separate labeled field from Field 5.
7. **NPS justification** — 2–4 sentences naming what this persona gains AND what they lose relative to Field 1. Both dimensions required. Must reference at least one named spec element.
8. **Feedback** — Severity: blocking / major / minor / cosmetic. Descending order within card. `[BLOCKING]` prefix on all blocking items. "No objections identified" if none.
9. **Revision recommendation** — One targeted change naming a specific spec element and what should change. Generic recommendations do not satisfy this field.

---

### CARD FORMAT

```
### [C-XX] [Name] — [Role]

**Current approach:** [what they do today; "No equivalent workflow exists" if applicable]

**Gains from this spec:** [delta from current approach — change framing, not feature list]

**Losses and switching costs:** [losses; "No significant losses identified — [explanation]" for Promoter-tier]

**Willingness to adopt:** [0–100%] — [Clears adoption bar (>=65%) | Adoption risk (<65%)]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [2–4 sentences: gains AND losses, both named; at least one named spec element cited]

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

**Aggregate NPS:** [mean of 12 NPS scores, one decimal]
**Threshold (7.0):** MET | NOT MET — if NOT MET: "Spec requires revision before shipping"
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count, e.g., "Migration burden (4 of 5 Detractors)"]
**Adoption summary:** Clears adoption bar (>=65%): X of 12 | Below adoption bar (<65%): X of 12
**Adoption threshold (65%):** MET | NOT MET — if NOT MET: "Adoption risk — switching cost reduction recommended before shipping"

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each persona, produce exactly **two direction-specific sub-bullets** — one for +1, one for -1. **Both bullets are required; a collapsed "±X" figure does not satisfy this section.** A +1 shift and a -1 shift are not symmetric near the 7.0 threshold: a Detractor shifting to Passive changes band distribution and may change threshold status; a Passive shifting to Promoter does not.

**[C-XX] [Name] — NPS [N]:** [one sentence on why this persona's score weight is disproportionately high]
- **+1 direction:** If score shifts from [N] to [N+1], aggregate mean moves from [X.X] to [Y.Y]
- **-1 direction:** If score shifts from [N] to [N-1], aggregate mean moves from [X.X] to [Z.Z]

Repeat this two-bullet block for each high-influence persona. A reviewer verifies completeness by counting: each entry must contain exactly 2 direction bullets. Frame each direction as a contribution to the aggregate mean.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Included in Field 9 of each card above.

**Pass 2 — Cross-persona ranked revision list:**
Synthesize all Field-9 recommendations into a ranked numbered list. Sort by: (a) personas affected, (b) maximum severity. Must contain **2 or more distinct spec changes**.

Format: `N. [Spec change] — [X personas]; max severity: [level]`

---

### PROFESSIONAL LENS

UX Read precedes PM Read in document order. Without this ordering, PM strategic framing would anchor the UX reading before friction signals are independently recorded.

#### UX READ
3–5 sentences from a UX practitioner's lens, drawing on all 12 cards. Cover: primary interaction pattern, friction or underspecified behavior across multiple personas, one change that most reduces switching cost across the widest range of personas.

#### PM READ
3–5 sentences from a product manager's lens. Cover: whether the spec solves the core customer problem given the Detractor and adoption-risk distribution, the riskiest assumption in the design, one validation question to run before shipping.

#### CONVERGENCE STATEMENT
Required after both reads. Name: (a) the specific finding where UX and PM agree, and (b) the specific point where they diverge. If no divergence, name the strongest shared conclusion.

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

## V-02 — Lifecycle Emphasis: Threshold-Proximity Annotation per Direction

**Variation axis:** Lifecycle emphasis — each directional swing figure in the sensitivity analysis is annotated with its threshold consequence (clears by +N / fails by -N / crosses threshold boundary), converting the sensitivity section from a numeric exercise into a shipping-decision instrument.

**Hypothesis:** A-28 requires that both directions are stated; it does not require that their decision consequences be named. Near-threshold aggregate means (6.8–7.2) have asymmetric directional consequences: a +1 shift may cross the 7.0 boundary from fail to pass; the corresponding -1 shift on a baseline already below 7.0 does not cross a boundary in the other direction. Without the threshold annotation, a reader must compute the consequence manually — and may not notice the spec is one bad Detractor score away from a revision flag. Annotating each direction with its threshold proximity makes the decision relevance of the asymmetry explicit at the point of observation.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) evaluate the spec. You compute aggregate NPS with statistical spread annotation. The spec passes if mean NPS >= 7.0; the CI annotation indicates whether that pass is robust or marginal.

**INPUT:** The spec or design document provided in context.

---

### EVALUATION PROTOCOL

For each of the 12 customer personas, complete the following in document order:

**Step A — Current approach**
Name what this persona does TODAY without this spec — the tool, workflow, or absence of workflow the spec must displace. Specific enough to anchor gains and losses. State explicitly if no equivalent workflow exists.

**Step B — Gains from this spec**
What does this persona gain relative to their current approach? State the delta from their current approach, not the spec's feature list.

**Step C — Losses and switching costs**
What does this persona lose or sacrifice? Include switching cost, migration burden, retraining, workflow disruption, opportunity cost. Promoter-tier: "No significant losses identified — [one sentence on why friction is low]."

**Step D — NPS score (after evidence)**
Assign NPS (1–10) and band on a separate labeled line, after Steps B and C are complete:
- 1–6: Detractor
- 7–8: Passive
- 9–10: Promoter

**Step E — NPS justification**
2–4 sentences. Must name what this persona gains AND what they lose relative to their current approach. Both dimensions required. Must reference at least one named spec element.

**Step F — Feedback**
Severity: blocking / major / minor / cosmetic. Descending order within the card. `[BLOCKING]` prefix on blocking items. "No objections identified" if none.

**Step G — Revision recommendation**
One specific change naming a spec element and what should change. Generic recommendations do not satisfy this step.

---

### CARD FORMAT

```
### [C-XX] [Name] — [Role]

**Current approach:** [what they do today; "No equivalent workflow exists" if applicable]

**Gains from this spec:** [delta from current approach]

**Losses and switching costs:** [losses; "No significant losses identified — [explanation]" for Promoter-tier]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [2–4 sentences: gains AND losses; at least one named spec element]

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

**Aggregate NPS:** [mean of 12 scores, one decimal]
**Standard deviation:** SD = [X.X]
**95% Confidence interval:** CI: [mean − 1.96×(SD/3.46), mean + 1.96×(SD/3.46)], bounds rounded to one decimal. (sqrt(12) = 3.464; use 3.46.)
**Threshold (7.0):** MET | NOT MET — if NOT MET: "Spec requires revision before shipping"; if mean >= 7.0 but CI lower bound < 7.0: "CI lower bound below threshold — shipping confidence is marginal"
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count]

The CI annotation is required. A mean-only aggregate obscures whether the threshold pass is robust or marginal — a mean of 7.1 is indistinguishable in shipping confidence from a mean of 8.5 without the spread.

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each, state both directional swing figures separately and annotate the threshold consequence of each direction:

**[C-XX] [Name] — NPS [N]:** [why their score weight is disproportionately high]
- **+1 shift (score → [N+1]):** aggregate moves from [X.X] to [Y.Y] — [clears threshold by +[Y.Y − 7.0] | fails threshold by −[7.0 − Y.Y] | crosses threshold from NOT MET to MET]
- **-1 shift (score → [N-1]):** aggregate moves from [X.X] to [Z.Z] — [clears threshold by +[Z.Z − 7.0] | fails threshold by −[7.0 − Z.Z] | crosses threshold from MET to NOT MET]

The threshold annotation makes asymmetric consequences visible. A +1 shift on a Detractor near the boundary may move the aggregate above 7.0; the corresponding -1 shift may not cross any boundary in the other direction because the baseline mean is already below 7.0. Without separate directional figures, that one-way crossing is invisible. Without the threshold annotation, a reader must compute the consequence manually.

Repeat this block for each high-influence persona.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Included in each card's Step G above.

**Pass 2 — Cross-persona ranked revision list:**
Ranked numbered list. Sort by: (a) personas affected, (b) maximum severity. Must contain **2 or more distinct spec changes**.

Format: `N. [Spec change] — [X personas]; max severity: [level]`

---

### PROFESSIONAL LENS

UX Read precedes PM Read in document order. Without this ordering, PM framing would anchor the UX reading before friction signals are independently recorded.

#### UX READ
3–5 sentences from a UX practitioner's lens. Cover: primary interaction pattern, friction or underspecified behavior across multiple personas, one priority change that most improves experience across the widest range of personas.

#### PM READ
3–5 sentences from a product manager's lens, drawing on aggregate scores, CI, and Detractor pattern. Cover: whether the spec solves the core customer problem (reference CI in shipping confidence assessment), the riskiest assumption, one pre-ship validation question.

#### CONVERGENCE STATEMENT
Required after both reads. Name where UX and PM agree and where they diverge. Absence of divergence should be stated, not omitted.

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

## V-03 — Phrasing Register: Causal Band-Transition Narrative per Direction

**Variation axis:** Phrasing register — the sensitivity section narrates each direction as a causal band-transition event ("shifting C-06 from Detractor to Passive, removing them from the D-count") rather than a numeric delta statement, making the structural asymmetry between +1 and -1 visible in prose rather than arithmetic.

**Hypothesis:** A-28 requires separate numeric figures for each direction. V-03 goes further: it requires that each direction be narrated in terms of its band-transition consequence. The asymmetry is not just numerical — it is structural. A Detractor-to-Passive transition changes the D/P/Pr distribution and may flip threshold status; a Passive-to-Promoter transition has no threshold consequence. Collapsing ±1 hides the transition narrative. Even separate numeric figures (A-28) without band-transition narration leave the asymmetry implicit. The causal narrative makes it explicit and forces the evaluator to reason about band consequences, not just compute means.

---

You are running a pre-ship customer simulation in three phases: UX frame, persona evaluation, and evidence synthesis. Phase 1 establishes design quality from the spec alone. Phase 2 measures individual persona reactions. Phase 3 synthesizes the full evidence base and delivers the shipping verdict.

**INPUT:** The spec or design document provided in context.
**Threshold:** Aggregate NPS >= 7.0 = ready to ship. Below 7.0 = flag for revision.

---

### PHASE 1 — UX READ (before persona evaluation)

**Run first.** Behavioral friction in a design is most visible before individual persona contexts filter it. If PM Read ran first, its strategic framing would anchor the UX reading — categorizing interaction friction as acceptable trade-offs before that friction is independently recorded. Without this ordering constraint, the failure mode is PM-anchored UX: the UX read confirms the PM frame rather than challenging it.

Write 3–5 sentences from a UX practitioner's lens, reading the spec cold. Cover:
- The primary interaction pattern the spec establishes
- Any points where the spec leaves behavior underspecified or creates friction by design
- The one UX change that would most improve experience across the widest range of users

This read is from the spec alone — no persona data is available yet.

---

### PHASE 2 — PERSONA EVALUATION

Work through all 12 customer personas (C-01 through C-12), one at a time. For each:

**Current approach** — What does this persona do today without this spec? Name the tool, workflow, or absence of workflow. State explicitly if no equivalent exists.

**Gains from this spec** — What changes for them? State the delta from their current approach, not the feature list.

**Losses and switching costs** — What do they give up? Cover switching cost, migration, retraining, workflow disruption, opportunity cost. Promoter-tier: "No significant losses — [one sentence explaining why their switching cost is low]."

**NPS score** — After gains and losses are documented. Assign 1–10 and band on a separate labeled line:
- 1–6: Detractor
- 7–8: Passive
- 9–10: Promoter

**NPS justification** — 2–4 sentences. Name what this persona gains AND what they sacrifice. Both required. Reference at least one named spec element.

**Feedback** — Severity: blocking / major / minor / cosmetic. Descending order within the card. `[BLOCKING]` inline prefix on all blocking items.

**Revision recommendation** — One specific change naming a spec element and what should change.

Card format:
```
### [C-XX] [Name] — [Role]

**Current approach:** [what they do today; "No equivalent workflow exists" if applicable]

**Gains from this spec:** [delta from current approach]

**Losses and switching costs:** [losses; "No significant losses — [explanation]" for Promoter-tier]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [2–4 sentences: gains AND losses; at least one named spec element]

**Feedback:**
- [BLOCKING] [item]
- Major: [item]
- Minor: [item]
- Cosmetic: [item]

**Revision recommendation:** [named spec element + specific change]
```

**Ordering:** Sort all 12 cards ascending by NPS (lowest first). Ties may appear in any order.

---

### PHASE 3 — AGGREGATE SYNTHESIS

**Aggregate NPS:** [mean of 12 scores, one decimal]
**Threshold (7.0):** MET | NOT MET — if NOT MET: "Spec requires revision before shipping"
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count]

**NPS Sensitivity Analysis:**
Identify the 2–3 personas whose scores most drive the aggregate mean. For each, narrate both directional shifts as distinct band-transition events. Both directions are required; state them separately:

> **[C-XX] [Name] — NPS [N]:** [why this persona's score weight is disproportionately high]
>
> **+1 shift (score → [N+1]):** Aggregate moves from [X.X] to [Y.Y]. [C-XX] moves from [Band] to [Band or stays] — Detractor count: [old D] → [new D]; Passive count: [old P] → [new P]. Threshold status: [unchanged | changes from NOT MET to MET | no threshold consequence — band transition is P→Pr].
>
> **-1 shift (score → [N-1]):** Aggregate moves from [X.X] to [Z.Z]. [C-XX] moves from [Band] to [Band or stays] — Detractor count: [old D] → [new D]; Passive count: [old P] → [new P]. Threshold status: [unchanged | changes from MET to NOT MET].

The band-transition narration reveals the structural asymmetry that collapsed ±1 notation hides. A Detractor-to-Passive transition (caused by a +1 shift on a Detractor-tier persona) changes both band distribution and potentially threshold status. A Passive-to-Promoter transition has no threshold consequence. These are not symmetric events — narrating each direction separately makes this explicit and prevents the evaluator from averaging the two consequences into a single misleading delta.

**Blockers requiring resolution:**
All `[BLOCKING]` items from Phase 2 cards, attributed by persona. If none: "No blocking issues identified."

---

### PHASE 3 (CONTINUED) — PM READ (after aggregate)

**Run after aggregate.** A PM Read before the data is available is forecasting. A PM Read after the full evidence base — 12 persona cards, aggregate NPS, band distribution, Detractor pattern — is synthesis. Strategic judgment must be grounded in observed reactions, not spec impressions.

Write 3–5 sentences from a product manager's lens. Cover:
- Whether the spec solves the stated customer problem given the Detractor distribution and dominant objection pattern
- The riskiest assumption embedded in the design, identified from what the persona data revealed
- The one validation question to run before shipping

---

### CONVERGENCE STATEMENT

**Required after both reads.** Without a convergence statement, UX and PM reads are parallel monologues — each useful in isolation but producing no cross-read analytical value.

- **Where UX and PM agree:** The specific finding or recommendation both reads converge on. If convergence is strong, explain what that shared conclusion means for shipping readiness.
- **Where UX and PM diverge:** The specific point of disagreement. Which read surfaces a concern the other does not? What does that divergence reveal about the design trade-off?

If the reads agree on everything, name the strongest shared conclusion and note the absence of divergence.

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Included in each Phase 2 card above.

**Pass 2 — Cross-persona ranked revision list:**
Ranked numbered list. Sort by: (a) personas affected, (b) maximum severity. 2 or more distinct spec changes required.

Format: `N. [Spec change] — [X personas]; max severity: [level]`

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

## V-04 — Combination: Two-Bullet Directional Format + Numbered Manifests (A-23/A-26)

**Variation axes:** Output format (two-bullet directional sensitivity from V-01) + numbered field manifests at persona card level (A-13/A-23) and aggregate level (A-26), with explicit completeness enforcement rules at all three tiers.

**Hypothesis:** Numbered sequential fields make the entire output positionally auditable: a reviewer can count fields rather than parse labels to detect omissions. Applying the same two-bullet directional structure to the sensitivity section extends positional verifiability to that section: each high-influence persona entry must contain exactly 2 direction bullets, countable without reading their content. The combination makes completeness detectable at three independent checkpoints from a single verification pass — card level (count to 9), aggregate level (count to A5), sensitivity level (count to 2 bullets per persona) — replacing semantic parsing with structural counting at every critical output tier.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) produce structured feedback cards using the PERSONA CARD MANIFEST below. The aggregate section follows the AGGREGATE MANIFEST. Both manifests have explicit completeness enforcement rules. Omitting any numbered field at any tier constitutes a malformed output.

**INPUT:** The spec or design document provided in context.
**Threshold:** Aggregate NPS >= 7.0 = ready. Below 7.0 = flag for revision.

---

### PERSONA CARD MANIFEST

Every persona card must instantiate all 9 fields in this numbered order. **Omitting any numbered field for any persona constitutes an incomplete card and must be corrected before the output is considered valid.**

| # | Label | Constraint |
|---|-------|------------|
| 1 | `**Current approach:**` | What this persona does today without the spec. Required even if no equivalent workflow exists — state "No equivalent workflow exists" explicitly. **First field in card body, immediately after the header.** Without this field, Fields 2 and 3 have no baseline — gains and losses become feature descriptions rather than delta computations, and the NPS justification cannot be verified as inertia-comparative. |
| 2 | `**Gains from this spec:**` | What this persona gains relative to Field 1. State the delta from their current approach, not the spec's feature list. |
| 3 | `**Losses and switching costs:**` | What this persona loses or sacrifices. Cover: switching cost, migration burden, retraining, workflow disruption, opportunity cost. May not be blank. Promoter-tier: "No significant losses identified — [one sentence on why switching cost is low]." |
| 4 | `**NPS:**` | Integer 1–10. Must appear after Fields 1–3. The score follows the evidence from Fields 2 and 3 — not a starting estimate. |
| 5 | `**Band:**` | "Detractor" (1–6), "Passive" (7–8), or "Promoter" (9–10). **Separate labeled field from Field 4.** Without Field 5 as a distinct field, band classification is lost when NPS values are extracted for aggregate analysis — band cannot be recovered from the score alone. |
| 6 | `**NPS justification:**` | 2–4 sentences. Must state what this persona gains AND what they lose relative to Field 1. Both dimensions required — one-sided justifications do not satisfy this field. Must reference at least one named spec element. |
| 7 | `**Feedback:**` | Ordered by descending severity: `[BLOCKING]` items first, then Major, then Minor, then Cosmetic. Each item explicitly labeled. If none: "No objections identified." |
| 8 | `**Willingness to adopt:**` | Percentage (0–100%) + annotation: "Clears adoption bar (>=65%)" or "Adoption risk (<65%)". Adoption bar: 65%. Must appear after Fields 4 and 5. |
| 9 | `**Revision recommendation:**` | Names a specific spec element (section, field, behavior, or feature) and the change that would improve this persona's NPS. Generic recommendations do not satisfy this field. |

**Card header:** `### [C-XX] [Name] — [Role]` — identifier, name, and role only. No summary or context in the header line.

**Completeness enforcement rule:** Any card missing one or more manifest fields is malformed. Produce all 9 fields for all 12 cards.

---

### PERSONA EVALUATION

For each of the 12 customer personas (C-01 through C-12), instantiate all 9 manifest fields in numbered order.

**Field 1 guidance:** Name the specific tool, workflow, or manual process this persona uses today. Concrete enough to make Fields 2 and 3 meaningful as delta computations against a named baseline.

**Field 2 guidance:** Name the delta. "Gets real-time sync" describes the spec. "Eliminates the nightly batch reconciliation step currently required after each config push" names the change from their current approach.

**Field 3 guidance:** For Detractor and Passive personas, name the friction specifically. For Promoter personas, Field 3 is still required — state "No significant losses identified" and give one sentence explaining why this persona's switching cost is low given their current approach.

**Field 6 guidance:** Cover BOTH the gains dimension (from Field 2) AND the losses/switching-cost dimension (from Field 3) relative to Field 1. Must name a spec element as the basis for the score.

**Field 7 guidance:** Place all [BLOCKING] items first, then Major, then Minor, then Cosmetic. No lower-severity item may appear above a higher-severity item in the same card.

**Field 9 guidance:** The recommendation must be actionable: name the spec element and state the change. "Add a dry-run flag to the migration command in Section 4" satisfies this field. "Make migration easier" does not.

---

### CARD ORDERING

Sort all 12 completed cards in ascending NPS order (lowest first, highest last). **Without ascending-NPS ordering, Detractor-tier personas are buried in document sequence — their contribution to the aggregate mean requires cross-referencing rather than being immediately visible at the top of the output.** Ties may appear in any order within the tie group.

---

### AGGREGATE MANIFEST

After all 12 cards, produce the following fields in this numbered order. **Omitting any numbered aggregate field constitutes an incomplete aggregate section and must be corrected before the output is considered valid.**

| # | Field | Format |
|---|-------|--------|
| A1 | `**Aggregate NPS:**` | Mean of all 12 NPS values, one decimal. |
| A2 | `**Threshold (7.0):**` | "MET" or "NOT MET — spec requires revision before shipping." |
| A3 | `**Band distribution:**` | "Promoters: X | Passives: X | Detractors: X" |
| A4 | `**Dominant Detractor objection:**` | Single most common blocking or major theme among Detractor-tier personas. Include count (e.g., "Config migration burden (4 of 5 Detractors)"). Separate labeled field — not embedded in A3. |
| A5 | `**Adoption summary:**` | "Clears adoption bar (>=65%): X of 12 | Below adoption bar (<65%): X of 12" |

**Aggregate completeness enforcement rule:** All 5 aggregate fields (A1–A5) must be present. Counting to A5 in document order verifies completeness without parsing labels.

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each persona, produce exactly **two direction-specific sub-bullets** in this order — +1 first, -1 second. **Both bullets are required; a combined "±X" notation that presents a single symmetric value does not satisfy this section.** The two directions must appear as separate computations because their effects near the 7.0 threshold are asymmetric: a Detractor-to-Passive transition changes band distribution and may flip threshold status; a Passive-to-Promoter transition does not.

**[C-XX] [Name] — NPS [N]:** [one sentence on why this persona's score weight is disproportionately high]
- **+1 direction:** If score shifts from [N] to [N+1], aggregate mean moves from [X.X] to [Y.Y]
- **-1 direction:** If score shifts from [N] to [N-1], aggregate mean moves from [X.X] to [Z.Z]

Repeat this two-bullet block for each identified high-influence persona. A reviewer verifies completeness by counting: each persona entry must contain exactly 2 direction bullets.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Field 9 of each card above.

**Pass 2 — Cross-persona ranked revision list:**
Synthesize all Field-9 entries into a ranked numbered list. Sort by: (a) personas affected, (b) maximum severity. Must contain **2 or more distinct spec changes**.

Format: `N. [Spec change] — [X personas]; max severity: [level]`

---

### PROFESSIONAL LENS

UX Read precedes PM Read in document order. UX observation must precede PM synthesis — PM strategic framing anchors UX reading if PM precedes UX, suppressing friction signals before they are independently recorded.

#### UX READ
3–5 sentences. Interaction patterns the spec establishes, friction or underspecified behavior across multiple personas, one priority UX change.

#### PM READ
3–5 sentences. Customer problem fit given the Detractor distribution, riskiest assumption, one pre-ship validation question.

#### CONVERGENCE STATEMENT
Required after both reads. Name where UX and PM agree and where they diverge. Absence of divergence should be stated, not omitted.

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

## V-05 — Combination: Directional Separation + Inertia Sub-Fields + Failure Mode Annotation (A-16/A-24/A-27 on A-28)

**Variation axes:** Inertia framing (Step 0 with 4 named sub-fields + gains/losses cross-reference, A-16/A-24) + conjunctive gains/losses field instructions (A-21) + failure mode annotation on the sensitivity directional-separation constraint (A-27 applied specifically to A-28: names the output failure that collapsed ±1 notation prevents from being detected).

**Hypothesis:** Three layers of structural enforcement on bilateral gains/losses (A-17 instruction, A-21 conjunctive framing, A-24 Step 0 cross-reference) produce robust inertia-comparative reasoning — an evaluator cannot produce a one-sided card without also suppressing a named Step 0 sub-field. Adding a failure mode annotation to the A-28 constraint (A-27 applied here) converts the directional-separation requirement from a structural rule into a self-explaining contract: an evaluator who understands that "without separate +1 and -1 figures, a spec that survives a best-case swing but fails under a worst-case one cannot be detected" is less likely to collapse the directions superficially. A-27 previously applied the failure-mode rationale concept to UX-before-PM ordering (A-25) and to at least one constraint (A-27 general); V-05 applies it specifically to A-28, closing the explanation gap at the sensitivity section.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) evaluate the spec. Every gains/losses assessment is a delta computation against the named status quo baseline in Step 0. All per-persona gains and losses must trace back to specific Step 0 sub-fields.

**INPUT:** The spec or design document provided in context.
**Threshold:** Aggregate NPS >= 7.0 = ready. Below 7.0 = flag for revision.

---

### STEP 0 — STATUS QUO BASELINE

Before evaluating any persona, characterize what this spec is displacing. This baseline is the reference for all per-card gains and losses — without a named baseline, gains and losses become feature descriptions rather than delta computations, and the NPS justifications cannot be verified as inertia-comparative.

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
What does this persona gain by switching from Field 1 to the spec? State gains as deltas computed from Step 0 "Where the status quo falls short:" — what the status quo cannot provide that this persona now gets. Neither Field 2 nor Field 3 is complete without the other: completing Gains without completing Losses constitutes an incomplete card. Gains that cannot be grounded in a named Step 0 failure mode are feature descriptions, not delta computations.

**Field 3 — Losses and switching costs** *(paired with Field 2, Gains from this spec)*
What does this persona lose or sacrifice to adopt the spec? Compute losses from Step 0 "Floor-level switching cost:" (the base sacrifice all personas bear) and "Persona-specific workflow disruption:" (the additional friction this persona's role carries). Neither Field 3 nor Field 2 is complete without the other: completing Losses without completing Gains constitutes an incomplete card. Promoter-tier: "No significant losses identified — [one sentence grounding this conclusion in this persona's relationship to Step 0 'Floor-level switching cost:']."

**Field 4 — NPS score (after evidence)**
Assign NPS (1–10) and band on a separate labeled line, after Fields 2 and 3 are complete:
- 1–6: Detractor
- 7–8: Passive
- 9–10: Promoter

**Field 5 — NPS justification**
2–4 sentences. Must name what this persona gains (Field 2) AND what they lose (Field 3) relative to Field 1. Both dimensions required. Must reference at least one named spec element.

**Field 6 — Feedback**
Severity: blocking / major / minor / cosmetic. Descending order within the card. `[BLOCKING]` prefix on blocking items. "No objections identified" if none.

**Field 7 — Revision recommendation**
One specific change naming a spec element and what should change to improve this persona's NPS. Generic recommendations do not satisfy this field.

---

### CARD FORMAT

```
### [C-XX] [Name] — [Role]

**Current approach:** [specific to this persona; how their experience of Step 0 differs from the general characterization]

**Gains from this spec (paired with Losses and switching costs):** [delta from Field 1 computed from Step 0 "Where the status quo falls short:"]

**Losses and switching costs (paired with Gains from this spec):** [losses computed from Step 0 "Floor-level switching cost:" and "Persona-specific workflow disruption:"; or "No significant losses identified — [Step 0 'Floor-level switching cost:' grounding]" for Promoter-tier]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [2–4 sentences: gains AND losses, both named, relative to Field 1; at least one named spec element cited]

**Feedback:**
- [BLOCKING] [item]
- Major: [item]
- Minor: [item]
- Cosmetic: [item]

**Revision recommendation:** [named spec element + specific change]
```

**Ordering:** Sort all 12 cards ascending by NPS (lowest first). Ties may appear in any order.

---

### AGGREGATE SECTION

**Aggregate NPS:** [mean of 12 scores, one decimal]
**Threshold (7.0):** MET | NOT MET — if NOT MET: "Spec requires revision before shipping"
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count]

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each, state both the +1 direction and the -1 direction as **separate numeric figures**:

**[C-XX] [Name] — NPS [N]:** [why this persona's score weight is disproportionately high]
- **If shifted to [N+1]:** aggregate mean moves from [X.X] to [Y.Y]
- **If shifted to [N-1]:** aggregate mean moves from [X.X] to [Z.Z]

**Why both directions must be stated separately:** Without the +1 and -1 figures as distinct values, a spec that survives a best-case swing but fails under a worst-case one cannot be detected from this output. A +1 shift on a Detractor-tier persona may move the aggregate above the 7.0 threshold — a Detractor shifting to Passive changes band distribution and threshold status. A -1 shift on that same persona does not cross a band boundary in the opposite direction if the aggregate is already below threshold. Collapsing both into a single ±X value hides this asymmetry: the "±0.08" form presents both directions as equivalent when they are structurally distinct events with opposite decision consequences.

Repeat this block for each high-influence persona. Frame as contribution to the mean.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Included in each card's Field 7 above.

**Pass 2 — Cross-persona tiered revision list:**
Synthesize all Field-7 recommendations into a tiered list. First rank by: (a) personas affected, (b) maximum severity. Then categorize each entry by implementation cost tier:

**Low-cost revisions** (copy, label, messaging, or configuration changes — implementable without architecture changes):
1. [Spec change] — [X personas]; max severity: [level]

**High-cost revisions** (workflow redesign, architectural changes, integration work, or new capability development):
1. [Spec change] — [X personas]; max severity: [level]

Must contain **2 or more distinct spec changes** total. If all items fall into one tier, produce a single labeled tier and explain why.

---

### PROFESSIONAL LENS

UX Read precedes PM Read in document order. UX observation must precede PM synthesis — PM strategic framing anchors UX reading if PM precedes UX, suppressing friction signals before they are independently recorded.

#### UX READ
3–5 sentences. Primary interaction pattern, friction or underspecified behavior across multiple personas, one priority change that reduces switching cost for the widest range of personas.

#### PM READ
3–5 sentences. Customer problem fit given the Detractor distribution and Step 0 baseline, riskiest assumption, one pre-ship validation question.

#### CONVERGENCE STATEMENT
Required after both reads. Without a convergence statement, the two professional reads are parallel monologues.
- **Where UX and PM agree:** Name the specific finding or recommendation both reads converge on.
- **Where UX and PM diverge:** Name the specific point of disagreement. What does the divergence reveal about the design trade-off?

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
