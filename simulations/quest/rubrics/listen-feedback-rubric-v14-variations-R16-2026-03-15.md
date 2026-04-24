# listen-feedback — Round 16 Variations (Rubric v14)

**Rubric:** v14 (225 pts max)
**R13 baseline preserved:** C-01–C-05, R-01–R-03, A-01–A-12, A-17, A-18, A-20
**Round 16 new targets:** A-14 (variance annotation), A-15 (willingness to adopt), A-16 (Step 0 sub-fields), A-19 (cost-tiered revisions), A-21 (conjunctive framing), A-22 (convergence statement), A-24 (Step 0 cross-reference), A-25 (epistemic UX rationale), A-26 (numbered aggregate manifest), A-27 (failure mode annotations — new in v14)

Single-axis: V-01 (willingness-to-adopt axis), V-02 (statistical depth), V-03 (professional lens depth).
Combinations: V-04 (numbered manifests + failure mode annotations), V-05 (inertia delta + conjunctive framing + cost-tiered revisions).

---

## V-01 — Willingness-to-Adopt Axis

**Variation axis:** Per-card `Willingness to adopt:` field with a defined 65% adoption threshold — a parallel scoring track that measures behavioral adoption probability independently from NPS satisfaction.

**Hypothesis:** NPS measures how much a persona *likes* the spec; adoption likelihood measures whether they will actually change their behavior. A persona can score 8 NPS but have 30% adoption likelihood because the switching cost is high relative to the marginal gain. Adding a structured adoption field with an explicit threshold (65%) surfaces this friction pattern in each card and aggregates it into an adoption risk count — a signal NPS alone cannot provide. Without the adoption field, a spec can clear the 7.0 NPS threshold while harboring a majority of personas who will not actually change their behavior.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) evaluate the spec and produce scored feedback cards. You compute aggregate NPS (threshold: 7.0) and aggregate adoption likelihood (adoption bar: 65%). A spec must clear both thresholds to be considered ready.

**INPUT:** The spec or design document provided in context.

---

### STEP 0 — STATUS QUO BASELINE

Before evaluating any persona, characterize what this spec must displace.

**What teams do today instead:** [Short label for the current approach + 2–3 sentences on what it delivers and why people stick with it]

**Where it falls short:** [2–3 sentences on the specific gaps this spec addresses]

**Floor-level switching cost:** [1 sentence on the minimum anyone must give up or learn to adopt this spec]

**Persona-specific workflow disruption:** [1 sentence on the transition friction that varies by persona type — teams or individuals who are most disrupted vs. least]

This baseline is the reference for all per-card gains, losses, and adoption likelihood assessments.

---

### EVALUATION PROTOCOL

For each persona, complete the following in document order:

**Step A — Current approach**
Name what this persona does TODAY without this spec — the tool, workflow, or absence of workflow the spec must displace. Be specific enough to anchor gains, losses, and adoption likelihood. If no equivalent workflow exists, state it explicitly.

**Step B — Gains from this spec**
What does this persona gain relative to their current approach? Name the delta — what changes for them compared to what they do today. Feature descriptions ("gets access to real-time sync") do not satisfy this step; delta descriptions ("eliminates the 20-minute manual reconciliation step they run after each deploy") do.

**Step C — Losses and switching costs**
What does this persona lose or sacrifice to adopt? Cover: switching cost, migration burden, retraining time, workflow disruption, opportunity cost. For Promoter-tier personas where friction is genuinely minimal: "No significant losses identified — [one sentence explaining why this persona's switching cost is low]."

**Step D — Willingness to adopt**
After stating gains AND losses, estimate this persona's behavioral adoption likelihood as a percentage (0–100%). The adoption bar is 65%. Annotate whether it clears:
- ≥65%: **Clears adoption bar**
- <65%: **Adoption risk** — switching cost or insufficient gain makes behavior change unlikely

A persona scoring high NPS but below the 65% bar signals high-satisfaction, low-change-probability — the spec is liked but will not change behavior without reducing switching cost. Without this field, that pattern is invisible in the per-card output.

**Step E — NPS score (after evidence)**
Assign NPS (1–10) and band on a separate labeled line, after gains, losses, and adoption likelihood are documented:
- 1–6: Detractor
- 7–8: Passive
- 9–10: Promoter

**Step F — NPS justification**
2–4 sentences. Must name what this persona gains AND what they lose or sacrifice relative to their current approach. Both dimensions required. Must reference at least one named spec element as the basis for the score. One-sided justifications do not satisfy this step.

**Step G — Feedback**
Severity: blocking / major / minor / cosmetic. Order by descending severity within the card. `[BLOCKING]` prefix on all blocking items. "No objections identified" if none.

**Step H — Revision recommendation**
One targeted change naming a specific spec element (section, field, behavior, or feature) and what should change to improve this persona's NPS or adoption likelihood. Generic recommendations ("improve onboarding") do not satisfy this step.

---

### CARD FORMAT

```
### [C-XX] [Name] — [Role]

**Current approach:** [what they do today; "No equivalent workflow exists" if applicable]

**Gains from this spec:** [delta from current approach — change framing, not feature list]

**Losses and switching costs:** [losses, friction, switching cost; "No significant losses identified — [explanation]" for Promoter-tier]

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

**Ordering:** Sort all 12 cards ascending by NPS (lowest first, highest last). Ties may appear in any order within the tie group.

---

### AGGREGATE SECTION

**Aggregate NPS:** [mean of 12 scores, one decimal]
**Threshold (7.0):** MET | NOT MET [if NOT MET: "Spec requires revision before shipping"]
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count, e.g., "Migration burden (4 of 5 Detractors)"]
**Adoption summary:** Clears adoption bar (>=65%): X of 12 | Below adoption bar (<65%): X of 12
**Adoption threshold (65%):** MET | NOT MET [if fewer than 7 of 12 personas clear the bar: "Adoption risk — switching cost reduction recommended before shipping"]

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each:
- Name and NPS
- Contribution delta: "If [C-XX]'s score shifted from [current] to [current ±1], aggregate mean moves from [X.X] to [Y.Y]"
- One sentence on why their score weight is disproportionately high

Frame as contribution to the aggregate mean — not proximity to the 7.0 threshold.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Included in each card above.

**Pass 2 — Cross-persona ranked revision list:**
Synthesize all Pass 1 recommendations into a ranked numbered list. Sort by: (a) number of personas affected, (b) maximum severity. Must contain **2 or more distinct spec changes** — a single-item output cannot be ranked.

Format: `N. [Spec change] — [X personas]; max severity: [level]`

---

### PROFESSIONAL LENS

UX Read precedes PM Read in document order.

#### UX READ
3–5 sentences from a UX practitioner's lens, drawing on all 12 cards. Cover: the primary interaction pattern the spec establishes, friction or underspecified behavior across multiple personas, and the one change that most reduces switching cost across the widest range of personas.

#### PM READ
3–5 sentences from a product manager's lens, drawing on aggregate scores and persona distribution. Cover: whether the spec solves the core customer problem given the Detractor and adoption-risk distribution, the riskiest assumption embedded in the design, and the one validation question to run before shipping.

---

### CROSS-PERSONA THEME MATRIX

Final substantive section. No analytical content follows.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme name] | C-XX, C-YY, ... | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Per-severity counts required per row. Omit zero-count severity levels.

---
---

## V-02 — Statistical Depth Axis

**Variation axis:** Confidence interval and standard deviation on aggregate NPS; ±1-point swing figures on sensitivity analysis — treating the aggregate as a range rather than a point estimate.

**Hypothesis:** A mean NPS of 7.1 and a mean NPS of 7.1 with SD = 1.8 (95% CI: [5.9, 8.3]) carry opposite implications for shipping confidence. The first appears to clear the threshold; the second is within one standard deviation of failing, across its full CI range. Requiring statistical spread annotation forces the aggregate section to convey decision confidence, not just a pass/fail verdict. Coupling this with ±1-point sensitivity swings (the minimum rubric-relevant increment) shows how fragile the aggregate is to single-persona score changes.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) evaluate the spec and produce scored feedback cards. You compute aggregate NPS with statistical spread annotation; the spec passes if mean NPS >= 7.0.

**INPUT:** The spec or design document provided in context.

---

### EVALUATION PROTOCOL

For each of the 12 customer personas, complete the following in document order:

**Step A — Current approach**
Name what this persona does TODAY without this spec. The inertia baseline — the tool, workflow, or absence of workflow the spec must displace. Specific enough to anchor gains and losses. If no equivalent workflow exists, state it explicitly.

**Step B — Gains from this spec**
What does this persona gain relative to their current approach? State the delta from their current approach, not the spec's feature list.

**Step C — Losses and switching costs**
What does this persona lose or sacrifice to adopt? Include: switching cost, migration burden, retraining time, workflow disruption, opportunity cost. Promoter-tier: "No significant losses identified — [one sentence on why friction is low]."

**Step D — NPS score (after evidence)**
Assign NPS (1–10) and band on a separate labeled line, after gains and losses are documented:
- 1–6: Detractor
- 7–8: Passive
- 9–10: Promoter

**Step E — NPS justification**
2–4 sentences. Must name what this persona gains AND what they lose or sacrifice relative to their current approach. Both dimensions required. Must reference at least one named spec element. One-sided justifications do not satisfy this step.

**Step F — Feedback**
Severity: blocking / major / minor / cosmetic. Order by descending severity. `[BLOCKING]` prefix on all blocking items. "No objections identified" if none.

**Step G — Revision recommendation**
One specific change naming a spec element (section, field, behavior, or feature) and what should change. Generic recommendations do not satisfy this step.

---

### CARD FORMAT

```
### [C-XX] [Name] — [Role]

**Current approach:** [what they do today; "No equivalent workflow exists" if applicable]

**Gains from this spec:** [delta from current approach]

**Losses and switching costs:** [losses; "No significant losses identified — [explanation]" for Promoter-tier]

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

**Aggregate NPS:** [mean of 12 scores, one decimal]
**Standard deviation:** SD = [X.X]
**95% Confidence interval:** CI: [mean - 1.96*(SD/3.46), mean + 1.96*(SD/3.46)], both bounds rounded to one decimal. (Note: sqrt(12) = 3.464; use 3.46 as the divisor.)
**Threshold (7.0):** MET | NOT MET [if NOT MET: "Spec requires revision before shipping"; if CI lower bound < 7.0 even when mean >= 7.0: note "CI lower bound below threshold — shipping confidence is marginal"]
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count]

The CI annotation is required. A mean-only aggregate obscures whether the threshold pass is robust or marginal — without the CI, a mean of 7.1 is indistinguishable in confidence from a mean of 8.5.

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each:
- Name and NPS
- Contribution delta: "If [C-XX]'s score shifted from [current] to [current + 1], mean moves from [X.X] to [Y.Y]; if shifted to [current - 1], mean moves from [X.X] to [Z.Z]"
- One sentence on why their score weight is disproportionately high

Show both +1 and -1 directions to capture asymmetric influence. Frame as contribution to the mean — not proximity to the 7.0 threshold.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Included in each card above.

**Pass 2 — Cross-persona ranked revision list:**
Synthesize all Pass 1 recommendations into a ranked numbered list. Sort by: (a) number of personas affected, (b) maximum severity. Must contain **2 or more distinct spec changes**.

Format: `N. [Spec change] — [X personas]; max severity: [level]`

---

### PROFESSIONAL LENS

UX Read precedes PM Read in document order.

#### UX READ
3–5 sentences from a UX practitioner's lens. Cover: primary interaction pattern, friction or underspecified behavior across multiple personas, and the one change that most improves experience across the widest range of personas.

#### PM READ
3–5 sentences from a product manager's lens, drawing on the aggregate scores, CI, and Detractor pattern. Cover: whether the spec solves the core customer problem, the riskiest assumption in the design, and the one validation question to run before shipping. Reference the CI in your assessment of shipping confidence.

---

### CROSS-PERSONA THEME MATRIX

Final substantive section. No analytical content follows.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme name] | C-XX, C-YY, ... | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Per-severity counts required per row. Omit zero-count severity levels.

---
---

## V-03 — Professional Lens Depth Axis

**Variation axis:** UX Read runs before personas as a design-quality frame (with explicit epistemic rationale); PM Read runs after aggregate as a strategy verdict; Convergence Statement required after both reads.

**Hypothesis:** Two professional reads that cover similar ground without synthesis produce no analytical value beyond their individual observations. Separating UX (design frame, runs first from spec alone) from PM (strategy verdict, runs last from evidence base), and requiring a Convergence Statement that maps agreement and divergence, converts the professional lens section into a structured dialectic. The epistemic rationale for UX-before-PM prevents PM framing from anchoring UX observation — without stating why the order matters, a later variation author can reverse it without contradiction.

---

You are running a pre-ship customer simulation in three phases: UX frame, persona evaluation, and evidence synthesis. Phase 1 (UX Read) establishes design quality from the spec alone. Phase 2 (12 persona cards) measures individual reactions. Phase 3 (aggregate + PM Read + Convergence) synthesizes the full evidence base.

**INPUT:** The spec or design document provided in context.
**Threshold:** Aggregate NPS >= 7.0 = ready. Below 7.0 = flag for revision.

---

### PHASE 1 — UX READ (before persona evaluation)

**Run first.** UX observation must precede persona evaluation and PM synthesis. This ordering is epistemic, not stylistic: behavioral friction in a design is most visible before individual persona contexts filter it. If PM Read ran first, its strategic framing would anchor the UX reading — categorizing interaction friction as acceptable trade-offs before that friction is independently recorded. Without this ordering constraint, the failure mode is PM-anchored UX: the UX read confirms the PM frame rather than challenging it.

Write 3–5 sentences from a UX practitioner's lens, reading the spec cold. Cover:
- The primary interaction pattern the spec establishes
- Any points where the spec leaves behavior underspecified or creates friction by design
- The one UX change that would most improve experience across the widest range of users

This read is written from the spec alone — no persona data is available yet.

---

### PHASE 2 — PERSONA EVALUATION

For each of the 12 customer personas (C-01 through C-12), complete the following in document order:

**Step A — Current approach**
Name what this persona does TODAY without this spec — the tool, workflow, or absence of workflow the spec must displace. If no equivalent workflow exists, state it explicitly.

**Step B — Gains from this spec**
What does this persona gain relative to their current approach? State the delta, not the feature list.

**Step C — Losses and switching costs**
What does this persona lose or sacrifice? Include: switching cost, migration burden, retraining, workflow disruption, opportunity cost. Promoter-tier: "No significant losses identified — [one sentence on why friction is low]."

**Step D — NPS score (after evidence)**
Assign NPS (1–10) and band on a separate labeled line, after gains and losses are documented:
- 1–6: Detractor
- 7–8: Passive
- 9–10: Promoter

**Step E — NPS justification**
2–4 sentences. Must name what this persona gains AND what they lose relative to their current approach. Both dimensions required. Must reference at least one named spec element. One-sided justifications do not satisfy this step.

**Step F — Feedback**
Severity: blocking / major / minor / cosmetic. Descending severity order within the card. `[BLOCKING]` prefix on all blocking items. "No objections identified" if none.

**Step G — Revision recommendation**
One specific change naming a spec element (section, field, behavior, or feature) and what should change. Generic recommendations do not satisfy this step.

**Card format:**
```
### [C-XX] [Name] — [Role]

**Current approach:** [what they do today; "No equivalent workflow exists" if applicable]

**Gains from this spec:** [delta from current approach]

**Losses and switching costs:** [losses; "No significant losses identified — [explanation]" for Promoter-tier]

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

### PHASE 3 — AGGREGATE SYNTHESIS

**Aggregate NPS:** [mean of 12 scores, one decimal]
**Threshold (7.0):** MET | NOT MET [if NOT MET: "Spec requires revision before shipping"]
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count]

**NPS Sensitivity Analysis:**
Identify the 2–3 personas whose scores most drive the aggregate mean. For each:
- Name and NPS
- Contribution delta: "If [C-XX]'s score shifted from [current] to [current ±1], mean moves from [X.X] to [Y.Y]"
- One sentence on why their score weight is disproportionately high

Frame as contribution to the mean — not proximity to threshold.

**Blockers requiring resolution:**
All `[BLOCKING]` items from Phase 2 cards, attributed by persona. If none: "No blocking issues identified."

---

### PHASE 3 (CONTINUED) — PM READ (after aggregate)

**Run after aggregate.** PM synthesis draws on evidence, not speculation. The PM Read runs after the full data set — 12 persona cards, aggregate NPS, band distribution, Detractor pattern — because strategic judgment must be grounded in observed reactions, not spec impressions. A PM Read before the data exists is forecasting; a PM Read after the data exists is synthesis.

Write 3–5 sentences from a product manager's lens. Cover:
- Whether the spec solves the stated customer problem, given the Detractor distribution and dominant objection pattern
- The riskiest assumption embedded in the design, identified from what the persona data revealed
- The one validation question you would run before shipping

---

### CONVERGENCE STATEMENT

**Required after both UX Read and PM Read.** Without a convergence statement, the two professional reads are parallel monologues — each useful in isolation but producing no cross-read analytical value.

Address both:
- **Where UX and PM agree:** Name the specific finding or recommendation that both reads converge on. If convergence is strong, explain what that shared conclusion means for shipping readiness.
- **Where UX and PM diverge:** Name the specific point of disagreement. Which read surfaces a concern the other does not? What does that divergence reveal about the design trade-off?

If the reads agree on everything, name the strongest shared conclusion and note that absence of divergence indicates a well-aligned design.

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Included in each Phase 2 card above.

**Pass 2 — Cross-persona ranked revision list:**
Synthesize all Pass 1 recommendations into a ranked numbered list. Sort by: (a) number of personas affected, (b) maximum severity. Must contain **2 or more distinct spec changes**.

Format: `N. [Spec change] — [X personas]; max severity: [level]`

---

### CROSS-PERSONA THEME MATRIX

Final substantive section. No analytical content follows.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme name] | C-XX, C-YY, ... | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Per-severity counts required per row. Omit zero-count severity levels.

---
---

## V-04 — Numbered Manifests + Failure Mode Annotations (Combination)

**Variation axes:** Output format (numbered field manifests at persona card level and aggregate level, with explicit completeness enforcement rules) + failure mode annotations (A-27: at least two structural constraint instructions name the output failure they prevent).

**Hypothesis:** Numbered sequential fields at both the persona card and aggregate levels make the entire output positionally auditable without semantic reading — a reviewer can detect omissions by counting fields rather than parsing labels. Attaching failure-mode causal language to the structural constraints that are most commonly violated converts the protocol from a compliance checklist into a self-explaining contract: an evaluator who understands what breaks when they omit a field is less likely to omit it superficially. The combination targets both the completeness gap (unlabeled or merged fields) and the shallow-compliance gap (fields present but not substantively populated).

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) produce structured feedback cards using the PERSONA CARD MANIFEST below. The aggregate section follows the AGGREGATE MANIFEST. Both manifests have explicit completeness enforcement rules. Omitting any numbered field at any tier constitutes a malformed output.

**INPUT:** The spec or design document provided in context.
**Threshold:** Aggregate NPS >= 7.0 = ready. Below 7.0 = flag for revision.

---

### PERSONA CARD MANIFEST

Every persona card must instantiate all 9 fields in this exact numbered order. **Omitting any numbered field for any persona constitutes an incomplete card and must be corrected before the output is considered valid.**

| # | Label | Constraint |
|---|-------|------------|
| 1 | `**Current approach:**` | What this persona does today without the spec. Required even if no equivalent workflow exists — state "No equivalent workflow exists" explicitly. **First field in card body, immediately after the header.** Without this field, Fields 2 and 3 have no baseline — gains and losses become feature descriptions rather than delta computations, and the NPS justification cannot be verified as inertia-comparative. |
| 2 | `**Gains from this spec:**` | What this persona gains relative to Field 1. State the delta from current approach, not the spec's feature list. |
| 3 | `**Losses and switching costs:**` | What this persona loses or sacrifices. Cover: switching cost, migration burden, retraining, workflow disruption, opportunity cost. May not be blank. Promoter-tier: "No significant losses identified — [one sentence on why switching cost is low]." |
| 4 | `**NPS:**` | Integer 1–10. Must appear after Fields 1–3. The score follows the evidence from Fields 2 and 3 — not a starting estimate. |
| 5 | `**Band:**` | "Detractor" (1–6), "Passive" (7–8), or "Promoter" (9–10). **Separate labeled field from Field 4.** Without Field 5 as a distinct field, band classification is lost when NPS values are extracted for aggregate analysis — band cannot be recovered from the score alone. |
| 6 | `**NPS justification:**` | 2–4 sentences. Must state what this persona gains AND what they lose or sacrifice relative to their current approach. Both dimensions required — one-sided justifications (gains only or losses only) do not satisfy this field. Must reference at least one named spec element. |
| 7 | `**Feedback:**` | List ordered by descending severity: `[BLOCKING]` items first, then Major, then Minor, then Cosmetic. Each item explicitly labeled. Blocking items prefixed `[BLOCKING]` inline. If none: "No objections identified." |
| 8 | `**Willingness to adopt:**` | Percentage (0–100%) + annotation: "Clears adoption bar (>=65%)" or "Adoption risk (<65%)". Adoption bar threshold: 65%. Must appear after Fields 4 and 5. |
| 9 | `**Revision recommendation:**` | Names a specific spec element (section, field, behavior, or feature) and the change that would improve this persona's NPS. Generic recommendations do not satisfy this field. |

**Card header constraint:** `### [C-XX] [Name] — [Role]` — identifier, name, and role only. No summary or context in the header line.

**Field ordering constraint:** Fields 2 and 3 must appear before Field 4 in document order.

**Completeness enforcement rule:** Any card missing one or more manifest fields is malformed. Produce all 9 fields for all 12 cards.

---

### PERSONA EVALUATION

For each of the 12 customer personas (C-01 through C-12), instantiate all 9 manifest fields in numbered order.

**Field 1 guidance:** Identify the specific tool, workflow, or manual process this persona uses today. Be concrete enough to make the gains and losses in Fields 2 and 3 meaningful relative to a named baseline.

**Field 2 guidance:** Name the delta. "Gets real-time sync" describes the spec. "Eliminates the nightly batch reconciliation step currently required after each config push" names the change from the persona's current approach.

**Field 3 guidance:** For Detractor and Passive personas, name the friction specifically. For Promoter personas, Field 3 is still required — state "No significant losses identified" and give one sentence explaining why this persona's switching cost is low given their current approach.

**Field 6 guidance:** Cover BOTH the gains dimension (from Field 2) AND the losses/switching-cost dimension (from Field 3) relative to Field 1. Use "and" to connect them — both are required elements. Must name a spec element as the basis for the score.

**Field 7 guidance:** Place all [BLOCKING] items first, then Major, then Minor, then Cosmetic. No lower-severity item may appear above a higher-severity item in the same card.

**Field 9 guidance:** The recommendation must be actionable: name the spec element and state the change. "Add a dry-run flag to the migration command in Section 4" satisfies this field. "Make migration easier" does not.

---

### CARD ORDERING

Sort all 12 completed cards in ascending NPS order (lowest score first, highest last). **Without ascending-NPS ordering, Detractor-tier personas are buried in document sequence — their contribution to the aggregate mean requires cross-referencing rather than being immediately visible at the top of the output.** Ties may appear in any order within the tie group.

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

Identify the 2–3 personas whose scores most drive the aggregate mean. For each:
- Name and NPS
- Contribution delta: "If [C-XX]'s score shifted from [current] to [current ±1], mean moves from [X.X] to [Y.Y]"
- One sentence on why their score weight is disproportionately high

Frame as contribution to the aggregate mean — not proximity to the 7.0 threshold.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Field 9 of each card above.

**Pass 2 — Cross-persona ranked revision list:**
Synthesize all Field-9 entries into a ranked numbered list. Sort by: (a) personas affected, (b) maximum severity. Must contain **2 or more distinct spec changes** — a single-item output cannot be ranked.

Format: `N. [Spec change] — [X personas]; max severity: [level]`

---

### PROFESSIONAL LENS

UX Read precedes PM Read in document order.

#### UX READ
3–5 sentences. Interaction patterns the spec establishes, friction or underspecified behavior across multiple personas, one priority UX change.

#### PM READ
3–5 sentences. Customer problem fit given the Detractor distribution, riskiest assumption, one pre-ship validation question.

---

### CROSS-PERSONA THEME MATRIX

Final substantive section. No analytical content follows.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme name] | C-XX, C-YY, ... | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Per-severity counts required per row. Omit zero-count severity levels.

---
---

## V-05 — Inertia Delta + Conjunctive Framing + Cost-Tiered Revisions (Combination)

**Variation axes:** Inertia framing (Step 0 with 4 named sub-fields) + conjunctive gains/losses framing (Field 2 instruction names Field 3 by label; Field 3 instruction names Field 2 by label; both reference named Step 0 sub-fields) + cost-tiered revisions (Pass 2 sorted into Low-cost and High-cost tiers).

**Hypothesis:** Three layers of structural enforcement on bilateral gains/losses coverage produce more robust inertia-comparative reasoning than any single layer alone. A-17 (bilateral in prose) is instructional — an evaluator can satisfy it by including a single sentence on losses. A-21 (conjunctive framing) makes the instruction self-referential — gains and losses reference each other. A-24 (Step 0 sub-field cross-reference) makes completion of either field structurally dependent on having consulted a named baseline sub-field. The combination means an evaluator cannot produce a one-sided card without also suppressing a named Step 0 sub-field. Adding implementation-cost tiers to Pass 2 makes revision priorities actionable by both engineering (low-cost: quick wins) and product (high-cost: architecture decisions), not merely by PM.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) evaluate the spec. Every gains/losses assessment is a delta computation against the named status quo baseline in Step 0. All per-persona gains and losses must trace back to specific Step 0 sub-fields.

**INPUT:** The spec or design document provided in context.
**Threshold:** Aggregate NPS >= 7.0 = ready. Below 7.0 = flag for revision.

---

### STEP 0 — STATUS QUO BASELINE

Before evaluating any persona, characterize what this spec is displacing. This baseline is the reference for all per-card gains and losses — without a named baseline, gains and losses become feature descriptions rather than delta computations, and the NPS justifications cannot be verified as inertia-comparative.

**What the status quo delivers:** [2–3 sentences. What does the current approach actually provide? Why do teams stick with it? What does it do well enough that switching feels optional?]

**Where the status quo falls short:** [2–3 sentences. What specific gaps or failure modes does the current approach have that this spec addresses? Name them; these are the gains that matter.]

**Floor-level switching cost:** [1 sentence. What is the minimum every persona must give up, learn, or rebuild to adopt this spec, regardless of individual context?]

**Persona-specific workflow disruption:** [1 sentence. Which persona types bear the highest transition friction, and which bear the lowest? Name the contrast.]

---

### EVALUATION PROTOCOL

For each of the 12 customer personas, complete the following fields in document order:

**Field 1 — Current approach**
How does this persona specifically experience the status quo from Step 0? What tool, workflow, or manual process do they use today? How does their version of the baseline differ from the general characterization above? If no equivalent workflow exists for this persona, state it explicitly.

**Field 2 — Gains from this spec** *(paired with Field 3, Losses and switching costs)*
What does this persona gain by switching from Field 1 to the spec? State gains as deltas computed from Step 0 "Where the status quo falls short:" — what the status quo cannot provide that this persona now gets. Neither Field 2 nor Field 3 is complete without the other: completing Gains without completing Losses constitutes an incomplete card. The gains computation draws from Step 0 "Where the status quo falls short:" — gains that cannot be grounded in a named Step 0 failure mode are feature descriptions, not delta computations.

**Field 3 — Losses and switching costs** *(paired with Field 2, Gains from this spec)*
What does this persona lose or sacrifice to adopt the spec? Compute losses from Step 0 "Floor-level switching cost:" (the base sacrifice all personas bear) and "Persona-specific workflow disruption:" (the additional friction this persona's role carries). Neither Field 3 nor Field 2 is complete without the other: completing Losses without completing Gains constitutes an incomplete card. For Promoter-tier personas where friction is genuinely minimal: "No significant losses identified — [one sentence grounding this conclusion in this persona's relationship to Step 0 'Floor-level switching cost:']."

**Field 4 — NPS score (after evidence)**
Assign NPS (1–10) and band on a separate labeled line, after Fields 2 and 3 are complete:
- 1–6: Detractor
- 7–8: Passive
- 9–10: Promoter

**Field 5 — NPS justification**
2–4 sentences. Must name what this persona gains (Field 2) AND what they lose (Field 3) relative to Field 1. Both dimensions required. Must reference at least one named spec element. One-sided justifications do not satisfy this field.

**Field 6 — Feedback**
Severity: blocking / major / minor / cosmetic. Order by descending severity. `[BLOCKING]` prefix on all blocking items. "No objections identified" if none.

**Field 7 — Revision recommendation**
One specific change naming a spec element (section, field, behavior, or feature) and what should change to improve this persona's NPS. Generic recommendations do not satisfy this field.

---

### CARD FORMAT

```
### [C-XX] [Name] — [Role]

**Current approach:** [specific to this persona; how their experience of the status quo differs from Step 0]

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

**Ordering:** Sort all 12 cards ascending by NPS (lowest first, highest last). Ties may appear in any order.

---

### AGGREGATE SECTION

**Aggregate NPS:** [mean of 12 scores, one decimal]
**Threshold (7.0):** MET | NOT MET [if NOT MET: "Spec requires revision before shipping"]
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count]

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each:
- Name and NPS
- Contribution delta: "If [C-XX]'s score shifted from [current] to [current ±1], mean moves from [X.X] to [Y.Y]"
- One sentence on why their score weight is disproportionately high

Frame as contribution to the mean — not proximity to threshold.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all 12 cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Included in each card's Field 7 above.

**Pass 2 — Cross-persona tiered revision list:**
Synthesize all Field-7 recommendations into a tiered list. First rank by: (a) number of personas affected, (b) maximum severity. Then **categorize each entry by implementation cost tier:**

**Low-cost revisions** (copy, label, messaging, or configuration changes — implementable in ≤1 day without architecture changes):
1. [Spec change] — [X personas]; max severity: [level]
2. [Spec change] — [X personas]; max severity: [level]
[continue ranked within tier]

**High-cost revisions** (workflow redesign, architectural changes, integration work, or new capability development — >1 week implementation):
1. [Spec change] — [X personas]; max severity: [level]
2. [Spec change] — [X personas]; max severity: [level]
[continue ranked within tier]

The tiered list must contain **2 or more distinct spec changes** total across both tiers. A single-item output cannot be ranked. If all items fall into one tier, produce a single tier with that label and explain why no items span both tiers.

---

### PROFESSIONAL LENS

UX Read precedes PM Read in document order. UX observation must precede PM synthesis — PM strategic framing anchors UX reading if PM precedes UX, suppressing friction signals before they are independently recorded.

#### UX READ
3–5 sentences. Primary interaction pattern, friction or underspecified behavior across multiple personas, one priority change that reduces switching cost for the widest range of personas.

#### PM READ
3–5 sentences. Customer problem fit given the Detractor distribution and Step 0 baseline, riskiest assumption, one pre-ship validation question.

---

### CROSS-PERSONA THEME MATRIX

Final substantive section. No analytical content follows.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme name] | C-XX, C-YY, ... | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Per-severity counts required per row. Omit zero-count severity levels.
