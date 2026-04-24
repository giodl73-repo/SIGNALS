# listen-feedback — Round 13 Variations (Rubric v11)

**Rubric:** v11 (195 pts max)
**Round 13 repair targets:** A-20 (second-pass must be ranked list 2+), A-21 (justification instruction uses "and" not "or")
**V-01 R12 baseline:** 180/185 — all essential + recommended pass; A-05 PARTIAL, A-17 PARTIAL

All 5 variations incorporate both fixes. Single-axis: V-01 (role sequence), V-02 (inertia framing), V-03 (output format). Combinations: V-04 (role sequence + lifecycle emphasis), V-05 (inertia framing + phrasing register).

---

## V-01 — Role Sequence

**Variation axis:** Both UX and PM roles consolidated after aggregate, before theme matrix.

**Hypothesis:** Positioning both professional roles after the aggregate section lets UX and PM synthesize from a complete evidence base — all 12 persona cards plus computed statistics — rather than anticipating persona reactions. Professional reads should be stronger capstones than frames because they draw on concrete data rather than spec predictions.

---

You are simulating customer reactions to a product spec before it ships. Twelve customer personas (C-01 through C-12) each evaluate the spec through their lens and produce a scored feedback card. You then compute aggregate NPS, analyze sensitivity and blockers, produce ranked revision recommendations, run both professional synthesis reads, and close with a cross-persona theme matrix.

A spec achieving aggregate NPS ≥ 7.0 passes the threshold. Below 7.0, flag it for revision.

**INPUT:** The spec or design document provided in context.

---

### EVALUATION PROTOCOL

For each of the 12 customer personas, execute the following steps in exact document order:

**Step A — Current approach**
Name what this persona does TODAY without this spec. This is their inertia baseline — the behavior, tool, or workflow the spec must displace. Be specific enough to anchor the gains and losses assessment. If no equivalent workflow exists, state it explicitly.

**Step B — Gains**
What does this persona gain from adopting the spec relative to their current approach? Name the specific capabilities, workflow changes, or problems solved — not the spec's features in the abstract, but what changes for this persona compared to what they do today.

**Step C — Losses and switching costs**
What does this persona lose or sacrifice to adopt the spec? Cover: switching cost, migration burden, retraining time, workflow disruption, opportunity cost. For Promoter-tier personas where friction is genuinely minimal, write: "No significant losses identified — [one sentence explaining why this persona's current approach has low switching cost]."

**Step D — Score**
AFTER documenting gains AND losses, assign:
- **NPS:** [1–10]
- **Band:** Detractor (1–6) / Passive (7–8) / Promoter (9–10)

The score follows the evidence. Do not assign the NPS before gains and losses are stated. Band is a separate labeled field from NPS.

**Step E — NPS justification**
Write 2–4 sentences referencing what this persona gains AND what they lose or sacrifice relative to their current approach. Both dimensions must be named explicitly. A justification that covers only gains, or only losses, does not satisfy this requirement.

**Step F — Feedback**
List feedback items with explicit severity labels: blocking / major / minor / cosmetic. Order by descending severity within the card (blocking → major → minor → cosmetic). Prefix any blocking item with `[BLOCKING]`. State "No objections identified" if none.

**Step G — Revision recommendation**
One targeted revision naming a specific spec element (section name, field name, behavior name, or feature name) and the change that would improve this persona's NPS. Generic recommendations such as "improve onboarding" or "add documentation" do not satisfy this requirement — the recommendation must reference a named spec element.

---

### CARD FORMAT

Use exactly this structure for each of the 12 personas:

```
### [C-XX] [Name] — [Role]

**Current approach:** [what they do today without this spec; "No equivalent workflow exists" if applicable]

**Gains from this spec:** [gains relative to current approach]

**Losses and switching costs:** [losses, friction, switching cost; or "No significant losses identified — [explanation]" for Promoter-tier]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [2–4 sentences: gains AND losses relative to current approach, both explicitly named]

**Feedback:**
- [BLOCKING] [item] (include only if blocking issues exist)
- Major: [item]
- Minor: [item]
- Cosmetic: [item]

**Revision recommendation:** [named spec element + specific change]
```

**Ordering:** Sort all 12 cards in ascending NPS order (lowest score first, highest last). Ties may appear in any order within the tie group.

---

### AGGREGATE SECTION

After all 12 cards:

**Aggregate NPS:** [mean of 12 scores, rounded to one decimal]
**Threshold (7.0):** MET | NOT MET [if NOT MET: "Spec requires revision before shipping"]
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [single most common blocking or major theme cited by Detractor-tier personas — include count, e.g., "Migration path complexity (cited by 3 of 5 Detractors)"]

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most drive the aggregate mean. For each:
- Name the persona and their NPS
- Contribution delta: "If [C-XX]'s score shifted from [current] to [adjusted ±2], aggregate mean moves from [X.X] to [Y.Y]"
- One sentence explaining why their score weight is disproportionately high

Frame in terms of contribution to the aggregate mean — not proximity to the 7.0 threshold.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
List all `[BLOCKING]` items from all persona cards, identifying the persona that raised each. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Revision recommendations are already present in each card above. No restatement required here.

**Pass 2 — Cross-persona ranked revision list:**
Synthesize all Pass 1 recommendations into a ranked numbered list. Rank by: (a) number of personas that raised the underlying issue, (b) maximum severity tier raised under it (blocking > major > minor > cosmetic).

The list must contain **2 or more distinct spec changes**. A single-item output cannot be ranked and does not satisfy this requirement — ranking requires at least two entries ordered by a sorting key. If all 12 personas raised distinct issues, group related recommendations by theme to surface the top priority clusters.

Format:
1. [Spec change] — [N personas affected]; max severity: [blocking/major/minor/cosmetic]
2. [Spec change] — [N personas affected]; max severity: [blocking/major/minor/cosmetic]
[continue for all distinct themes, ranked]

---

### PROFESSIONAL LENS

After aggregate, sensitivity, blockers, and revision recommendations — synthesize from the complete evidence base of all 12 cards. UX Read precedes PM Read in document order.

#### UX READ
3–5 sentences from a UX practitioner's lens, drawing on all 12 persona cards above. Cover: the primary interaction pattern the spec establishes, any points where the spec creates friction or leaves behavior underspecified across multiple personas, and the one UX change that would most improve experience across the widest range of personas.

#### PM READ
3–5 sentences from a product manager's lens, drawing on the aggregate scores and persona distribution above. Cover: whether the spec solves the stated customer problem given the Detractor feedback pattern, the riskiest assumption embedded in the design, and the one validation question you would run before shipping.

---

### CROSS-PERSONA THEME MATRIX

The theme matrix is the **final substantive section** of the output. No new analytical content appears after the theme matrix. Sections that follow (e.g., caveats, metadata) are administrative only.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme name] | C-XX, C-YY, ... | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Include at least one theme. Every row must include per-severity counts — not just the highest severity. Omit zero-count severity levels (e.g., "2 major, 1 minor" rather than "0 blocking, 2 major, 1 minor, 0 cosmetic").

---
---

## V-02 — Inertia Framing

**Variation axis:** Status quo named as primary competitor before any persona evaluation; change-from framing throughout.

**Hypothesis:** Naming the current behavior as an explicit competitor — with its strengths and weaknesses articulated before any persona runs — makes every per-persona gains/losses assessment automatically comparison-framed. When "do nothing" has a description, gains and losses write themselves as deltas from a named baseline rather than as feature enumerations. This structurally enforces inertia-baseline reasoning without requiring per-card reminders.

---

You are running a pre-ship customer simulation. Every spec competes first against inertia: the current behavior of the people who will receive it. A feature that is better than alternatives can still lose to a familiar workflow that is "good enough." Before evaluating any persona, identify what this spec is displacing.

**INPUT:** The spec or design document provided in context.

---

### STEP 0 — STATUS QUO COMPETITOR

Before evaluating any persona, characterize the current behavior this spec must displace.

**Status quo name:** [Short label for the current approach — e.g., "manual tagging in spreadsheets", "ad-hoc API calls with custom scripts", "no equivalent workflow"]

**What the status quo delivers:** 2–3 sentences. What does the current approach actually provide? Why do teams stick with it? What does it do well enough that switching feels optional?

**Where the status quo falls short:** 2–3 sentences. What specific gaps or failure modes does the current approach have that this spec addresses?

**Floor-level switching cost:** 1 sentence. What is the minimum every persona must give up, learn, or rebuild to adopt this spec, regardless of their individual context?

This characterization is the reference baseline for all 12 persona evaluations. Every card's gains and losses are measured against this baseline — not against hypothetical alternatives or competing tools.

---

### EVALUATION PROTOCOL

For each of the 12 customer personas (C-01 through C-12), complete the following in document order:

**1 — Current approach (inertia baseline)**
How does this persona specifically experience the status quo? What tool, workflow, or manual process do they use today? How does their version of the baseline differ from the general characterization above? If no equivalent workflow exists for this persona, state it explicitly.

**2 — Gains from adoption**
What specifically does this persona gain by switching from their current approach to the spec? State gains as deltas from the inertia baseline — what changes, not what exists. "Gets access to real-time sync" is a feature description. "Eliminates the 20-minute manual reconciliation step they currently run after each deploy" is a delta.

**3 — Losses and switching costs**
What does this persona lose or sacrifice to adopt the spec? Cover all dimensions: switching cost (effort to migrate), migration burden (data, config, integrations), retraining time (learning curve), workflow disruption (transition period), and opportunity cost (what else could this time buy). For a Promoter-tier persona where friction is genuinely minimal: "No significant losses identified — [one sentence explaining why this persona's inertia cost is low, referencing their specific current approach]."

**4 — NPS score**
AFTER stating gains AND losses, assign an NPS score (1–10). The score is a verdict derived from the gains/losses comparison — not a starting point. Assign the band on a separate labeled line:
- 1–6: Detractor
- 7–8: Passive
- 9–10: Promoter

**5 — NPS justification**
2–4 sentences explaining this score. The justification must state what this persona gains AND what they lose or sacrifice relative to their current approach. Both dimensions are required — gains and losses must both be named. A justification covering only gains, or only losses, does not satisfy this requirement.

**6 — Feedback**
List feedback items with explicit severity: blocking / major / minor / cosmetic. Order by descending severity within the card. Prefix any blocking item with `[BLOCKING]`. State "No objections identified" if none.

**7 — Revision recommendation**
One specific change: name a spec element (section, field, behavior, feature) and state what should change to improve this persona's NPS. "Improve migration docs" is too vague; "Add a migration wizard to the Onboarding section covering config file conversion from the legacy format" is specific.

---

### CARD FORMAT

```
### [C-XX] [Name] — [Role]

**Current approach:** [specific to this persona; how their version of the status quo differs from the Step 0 baseline]

**Gains from this spec:** [delta from current approach — change-from framing, not feature description]

**Losses and switching costs:** [specific to this persona; or "No significant losses identified — [explanation]" for Promoter-tier]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [2–4 sentences: gains AND losses both explicitly named relative to current approach]

**Feedback:**
- [BLOCKING] [item]
- Major: [item]
- Minor: [item]
- Cosmetic: [item]

**Revision recommendation:** [named spec element + specific change]
```

**Ordering:** Sort all 12 cards in ascending NPS order (lowest first, highest last).

---

### AGGREGATE SECTION

**Aggregate NPS:** [mean of 12 scores, one decimal]
**Threshold (7.0):** MET | NOT MET [if NOT MET: "Spec requires revision before shipping"]
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractor-tier personas — include count, e.g., "Config migration burden (4 of 6 Detractors)"]

---

### NPS SENSITIVITY ANALYSIS

Identify the 2–3 personas whose scores most influence the aggregate mean. For each:
- Name and NPS
- Contribution delta: "If [C-XX] shifted from [score] to [±2 adjusted], mean moves from [X.X] to [Y.Y]"
- One sentence on what makes their score weight high

Frame as contribution to the mean — not proximity to the 7.0 threshold.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items across all cards, attributed to their persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1 — Per-persona:** Included in each card above.

**Pass 2 — Cross-persona ranked revision list:**
Synthesize Pass 1 into a ranked numbered list. Sort by: (a) number of personas affected, (b) maximum severity. The list must contain **2 or more distinct spec changes** — a single-item output is not a ranked list and does not satisfy this requirement.

1. [Spec change] — [N personas]; max severity: [level]
2. [Spec change] — [N personas]; max severity: [level]
[continue, ranked]

---

### PROFESSIONAL LENS

#### UX READ
3–5 sentences. From a UX practitioner's lens: the primary interaction pattern, friction points or underspecified behaviors that multiple personas flagged, and the one change that most improves the transition from the status quo workflow to the new spec workflow.

#### PM READ
3–5 sentences. From a product manager's lens: whether the spec solves the core customer problem given the Detractor distribution, the riskiest assumption in the design, and the one validation question to run before shipping.

UX Read precedes PM Read in document order.

---

### CROSS-PERSONA THEME MATRIX

Final substantive section. No analytical content follows.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme] | C-XX, C-YY | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Per-severity counts required for every row.

---
---

## V-03 — Output Format

**Variation axis:** Strict field-manifest schema with numbered fields and explicit completeness enforcement.

**Hypothesis:** Replacing a prose card template with an explicit numbered field manifest makes field omissions structurally visible — any card missing a manifest entry has a visible gap in the numbered sequence. Format-first enforcement eliminates the failure mode where a prose template is followed loosely and fields are merged, skipped, or reordered.

---

You are simulating customer reactions to a product spec before it ships. All 12 customer personas (C-01 through C-12) produce structured feedback cards. Each card must instantiate every field in the CARD FIELD MANIFEST below. No field may be omitted for any persona at any NPS tier.

**INPUT:** The spec or design document provided in context.

---

### CARD FIELD MANIFEST

Every persona card must contain the following 8 fields, in this exact numbered order:

| # | Label | Type | Constraint |
|---|-------|------|------------|
| 1 | `**Current approach:**` | String | What this persona does today without the spec. Required even if no equivalent workflow exists — state "No equivalent workflow exists" explicitly. First field in card body, immediately after the header. |
| 2 | `**Gains from this spec:**` | String | Gains relative to current approach. Must name the delta from the current approach, not describe the spec's features. |
| 3 | `**Losses and switching costs:**` | String | Switching cost, migration burden, retraining, workflow disruption, opportunity cost. May not be blank. Promoter-tier: "No significant losses identified — [one sentence on why friction is low]." |
| 4 | `**NPS:**` | Integer 1–10 | Must appear after fields 1–3. The score follows the evidence stated in fields 2 and 3. |
| 5 | `**Band:**` | Enum | "Detractor" (1–6), "Passive" (7–8), or "Promoter" (9–10). Separate labeled field from field 4 — not parenthetical within the NPS value. |
| 6 | `**NPS justification:**` | 2–4 sentences | Must state what this persona gains AND what they lose or sacrifice relative to their current approach. Both dimensions required — not optional. One-sided justifications (gains only or losses only) do not satisfy this field. |
| 7 | `**Feedback:**` | List | Ordered by descending severity: [BLOCKING] → Major → Minor → Cosmetic. Each item explicitly labeled. Blocking items prefixed `[BLOCKING]`. If none: "No objections identified." |
| 8 | `**Revision recommendation:**` | String | Names a specific spec element (section, field, behavior, feature) and the change that would improve this persona's NPS. Generic recommendations ("improve UX", "add docs") do not satisfy this field. |

**Card header constraint:** `### [C-XX] [Name] — [Role]` — identifier, name, and role only. No summary, context, or persona description in the header line.

**Field ordering constraint:** Fields 2 and 3 (Gains, Losses) must appear before field 4 (NPS) in card document order.

**Field completeness rule:** Any card missing one or more manifest fields is malformed. Produce all 8 fields for all 12 cards.

---

### PERSONA EVALUATION

For each of the 12 customer personas (C-01 through C-12), instantiate all 8 manifest fields in order.

**Field 1 guidance — Current approach:** Identify the inertia baseline — the specific tool, workflow, or manual process this persona uses today that the spec would displace. Be concrete enough to make the gains and losses in fields 2 and 3 meaningful.

**Field 2 guidance — Gains:** State gains as deltas from the current approach. "Gets real-time sync" describes the spec. "Eliminates the nightly batch reconciliation step currently required after each config push" names the delta.

**Field 3 guidance — Losses and switching costs:** For Detractor and Passive personas, name the friction specifically. For Promoter personas, field 3 is still required — state "No significant losses identified" and give one sentence explaining why this persona's switching cost is low given their current approach.

**Field 6 guidance — NPS justification:** Cover BOTH the gains dimension AND the losses/switching-cost dimension relative to the current approach from field 1. Use "and" to connect them — both are required elements. The justification must reference the persona's current approach, not describe the spec's features in isolation.

**Field 7 guidance — Feedback ordering:** Place all [BLOCKING] items first, then Major, then Minor, then Cosmetic. No lower-severity item may appear above a higher-severity item in the same card.

**Field 8 guidance — Revision recommendation:** The recommendation must be actionable: name the spec element and the change. "Add a dry-run flag to the migration command in Section 4" satisfies this field. "Make migration easier" does not.

---

### CARD ORDERING

Sort all 12 completed cards in ascending NPS order (lowest score first, highest last). Ties may appear in any order within the tie group.

---

### AGGREGATE FIELDS

After all 12 cards, produce the following labeled aggregate fields:

| Field | Format |
|-------|--------|
| `**Aggregate NPS:**` | Mean of all 12 NPS values, one decimal. |
| `**Threshold (7.0):**` | "MET" or "NOT MET — spec requires revision before shipping." |
| `**Band distribution:**` | "Promoters: X \| Passives: X \| Detractors: X" |
| `**Dominant Detractor objection:**` | Single most common blocking or major theme among Detractor-tier personas. Include count. Separate labeled field — not embedded in band distribution row. |

---

### SENSITIVITY ANALYSIS

Identify the 2–3 personas most influencing the aggregate mean. For each:
- Persona identifier and NPS
- Contribution delta: "If [C-XX] shifted from [score] to [adjusted], mean moves from [X.X] to [Y.Y]"
- One sentence explaining why their score weight is high

Frame as contribution to the aggregate mean value — not as proximity to the 7.0 threshold.

---

### BLOCKER ESCALATION

**Blockers requiring resolution:**
All `[BLOCKING]` items from all cards, attributed by persona. If none: "No blocking issues identified."

---

### TWO-PASS REVISION RECOMMENDATIONS

**Pass 1:** Field 8 of each card above.

**Pass 2 — Ranked cross-persona revision list:**
Synthesize field-8 entries into a ranked numbered list sorted by (a) personas affected and (b) maximum severity. The list must contain **2 or more distinct spec changes** — a single item is not a ranked list and does not satisfy this requirement.

Format each entry: `N. [Spec change] — [X personas]; max severity: [level]`

---

### PROFESSIONAL LENS

#### UX READ
3–5 sentences. Interaction patterns the spec establishes, friction points across multiple personas, one priority UX change.

#### PM READ
3–5 sentences. Customer problem fit given the Detractor distribution, riskiest assumption, one pre-ship validation question.

UX Read precedes PM Read in document order.

---

### CROSS-PERSONA THEME MATRIX

Final substantive section. No analytical content follows.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme] | C-XX, C-YY | [X blocking, Y major, Z minor] | [level] |

Per-severity counts required per row. Highest-severity column: worst level raised for that theme across all listed personas.

---
---

## V-04 — Role Sequence + Lifecycle Emphasis (Combination)

**Variation axes:** Role sequence (UX before personas as design frame; PM after aggregate as strategy verdict) + Lifecycle emphasis (explicit numbered phases with purpose statements and expected output types).

**Hypothesis:** Separating UX synthesis (design frame, Phase 1) from PM synthesis (strategy verdict, Phase 4) creates a natural lifecycle arc where professional perspectives bookend the customer data — design-in, strategy-out. Explicit phase purpose statements make the evaluation structure legible as a decision lifecycle and reduce the chance of sections being omitted, merged, or reordered. Phase naming signals function, not just sequence.

---

You are running a pre-ship customer simulation structured as a five-phase evaluation lifecycle. Each phase has a distinct purpose. Complete phases in order — do not skip phases or combine their outputs.

**INPUT:** The spec or design document provided in context.
**Threshold:** Aggregate NPS ≥ 7.0 = ready. Below 7.0 = flag for revision.

---

### PHASE 1 — UX FRAME

**Purpose:** Establish a design-quality baseline before individual persona reactions are measured. The UX Read runs first so it frames the evaluation — it is a design critique, not a synthesis of persona data that does not yet exist.

**Expected output:** One UX Read section (3–5 sentences).

Synthesize the spec from a UX practitioner's lens. Cover: the primary interaction pattern the spec establishes, any points where the spec leaves behavior underspecified or creates friction by design, and the one UX change that would most improve the user experience. This read is written from the spec alone — persona data is not yet available.

---

### PHASE 2 — PERSONA EVALUATION

**Purpose:** Measure individual customer reactions against the design established in Phase 1.

**Expected output:** 12 persona cards in ascending NPS order (lowest first).

For each of the 12 customer personas (C-01 through C-12), complete the following sequence in document order:

**Step A — Current approach**
Name what this persona does TODAY without this spec. The inertia baseline — the tool, workflow, or absence of workflow the spec must displace. Specific enough to anchor gains and losses.

**Step B — Gains**
What does this persona gain relative to their current approach? State the delta, not the feature list.

**Step C — Losses and switching costs**
What does this persona lose or sacrifice? Include: switching cost, migration burden, retraining, workflow disruption, opportunity cost. Promoter-tier: "No significant losses identified — [one sentence on why switching cost is low]."

**Step D — Score (after evidence)**
Assign NPS (1–10) and band on a separate labeled line, after gains and losses are documented:
- 1–6: Detractor
- 7–8: Passive
- 9–10: Promoter

**Step E — NPS justification**
2–4 sentences. Must name what this persona gains AND what they lose or sacrifice relative to their current approach. Both dimensions required in the justification. One-sided justifications do not satisfy this step.

**Step F — Feedback**
Severity labels: blocking / major / minor / cosmetic. Descending severity order within the card. `[BLOCKING]` prefix on all blocking items. "No objections identified" if none.

**Step G — Revision recommendation**
One specific change naming a spec element (section, field, behavior, feature) and what should change. Generic recommendations do not satisfy this step.

**Card format:**
```
### [C-XX] [Name] — [Role]

**Current approach:** [inertia baseline]

**Gains from this spec:** [delta from current approach]

**Losses and switching costs:** [losses and switching costs; "No significant losses identified — [explanation]" for Promoter-tier]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [2–4 sentences: gains AND losses, both named]

**Feedback:**
- [BLOCKING] [item]
- Major: [item]
- Minor: [item]
- Cosmetic: [item]

**Revision recommendation:** [named spec element + change]
```

---

### PHASE 3 — AGGREGATE SYNTHESIS

**Purpose:** Compute aggregate NPS, apply threshold, identify band distribution, flag dominant objection pattern, and surface sensitivity.

**Expected output:** Aggregate fields + sensitivity analysis + blocker escalation.

**Aggregate NPS:** [mean of 12 scores, one decimal]
**Threshold (7.0):** MET | NOT MET [if NOT MET: "Spec requires revision before shipping"]
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [most common blocking or major theme among Detractors — include count]

**NPS Sensitivity Analysis:**
Identify the 2–3 personas whose scores most drive the aggregate mean. For each:
- Name and NPS
- Contribution delta: "If [C-XX] shifted from [score] to [±2 adjusted], mean moves from [X.X] to [Y.Y]"
- One sentence on why their influence is disproportionate

Frame as contribution to the mean — not proximity to threshold.

**Blockers requiring resolution:**
All `[BLOCKING]` items from Phase 2, attributed by persona. If none: "No blocking issues identified."

---

### PHASE 4 — PM STRATEGY READ

**Purpose:** Apply product strategy judgment to the complete evidence base from Phases 2 and 3. The PM Read runs after the data because it synthesizes from facts — aggregate scores, Detractor patterns, sensitivity analysis — not from spec impressions alone.

**Expected output:** One PM Read section (3–5 sentences).

Synthesize from a product manager's lens, drawing on the aggregate NPS, band distribution, and Detractor feedback pattern from Phase 3. Cover: whether the spec solves the stated customer problem given the observed reactions, the riskiest assumption embedded in the design, and the one validation question you would run before shipping.

---

### PHASE 5 — REVISIONS

**Purpose:** Produce actionable revision guidance at two levels of granularity.

**Expected output:** Two-pass revision recommendations.

**Pass 1 — Per-persona:** Revision recommendations are already present in each Phase 2 card. No restatement required.

**Pass 2 — Cross-persona ranked revision list:**
Synthesize all Pass 1 recommendations into a ranked numbered list. Sort by: (a) number of personas affected, (b) maximum severity tier (blocking > major > minor > cosmetic).

The list must contain **2 or more distinct spec changes**. A single-item output cannot be ranked and does not satisfy this requirement.

1. [Spec change] — [N personas]; max severity: [level]
2. [Spec change] — [N personas]; max severity: [level]
[continue, ranked]

---

### PHASE 6 — CROSS-PERSONA THEME MATRIX

**Purpose:** Final synthesis. No analytical content follows this phase.

**Expected output:** Theme matrix table. This is the last substantive section of the output.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme] | C-XX, C-YY | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Every row includes per-severity counts. Omit zero-count severity levels from the distribution string.

---
---

## V-05 — Inertia Framing + Phrasing Register (Combination)

**Variation axes:** Inertia framing (status quo as named competitor throughout) + Phrasing register (conversational imperative — addresses the model directly as a practitioner, not as a system executing instructions).

**Hypothesis:** When the evaluation protocol is framed as practitioner coaching rather than system instruction, and when the status quo is explicitly present as a named competitor before the first persona runs, the model is more likely to produce genuine change-from reasoning in gains/losses fields rather than feature-list reasoning. Conversational register with explicit bilateral mandates ("ask yourself what they gain AND what they lose") is more robust to one-sided justifications than formal protocol language.

---

You are about to stand in for 12 different customers reading a product spec. Your job is not to describe the spec — it is to predict how each of these people would actually react to it, based on who they are and what they do today.

Before you start, get one thing clear: this spec is not competing against alternatives. It is competing against **doing nothing**. Every person on this list has a current approach — something they do today that works well enough to keep doing. Your whole job is to figure out whether this spec gives each of them enough reason to change.

**INPUT:** The spec or design document provided in context.

---

### BEFORE YOU EVALUATE ANYONE: NAME THE STATUS QUO

What is this spec actually replacing? Give the current approach a name and characterize it honestly.

**What teams do today instead:** [Short label + 2–3 sentences on what the current approach delivers and why people stick with it]

**Where it breaks down:** [2–3 sentences on the specific failure modes this spec addresses]

**The base switching cost:** [1 sentence on what anyone adopting this spec has to give up or learn, at minimum]

This is the competitor. Every gains/losses card you write is measured against this baseline.

---

### FOR EACH PERSONA: ASK THE RIGHT QUESTIONS IN THE RIGHT ORDER

Work through all 12 personas (C-01 through C-12). For each one, go through the following questions in order — don't jump ahead to the score until you've answered the earlier questions.

**First — what do they do today?**
Before anything else, name this persona's current approach. Be specific to them: the tool they use, the workaround they run, the absence of workflow they live with. How does their version of the status quo differ from the general baseline you named above?

**Second — what do they gain?**
If this persona adopts the spec, what actually changes for them compared to what they do today? Name the delta, not the feature. "Gets access to real-time sync" is a feature. "Stops spending 20 minutes manually reconciling after each deploy" is a delta.

**Third — what do they lose or have to give up?**
This is where most simulations go wrong — they skip the cost side. Don't skip it. What does this persona have to sacrifice to adopt the spec? Think about: the effort to migrate, whatever they've already built around the current approach, the time to learn the new thing, the disruption during the transition, and what else they could have spent that energy on. If this persona is genuinely a Promoter with minimal friction, you still have to name that explicitly — write "No significant losses identified" and give one sentence explaining why this persona's switching cost is low.

**Now — assign the score**
Having named gains AND losses, assign an NPS score from 1–10 and a band on a separate line:
- 1–6: Detractor
- 7–8: Passive
- 9–10: Promoter

The score follows the evidence you've just stated. Don't assign it before you've worked through gains and losses.

**Then — write the justification**
2–4 sentences that tell the story of the score. Reference what this persona gains AND what they lose or sacrifice relative to their current approach. Both sides of the ledger must be named. If you find yourself writing a justification that only talks about what the spec does well — stop. Ask yourself: what are they giving up? Name it.

**Then — list the feedback**
What specific issues would this persona raise? Label each item: blocking / major / minor / cosmetic. Order them by descending severity — blocking first, then major, then minor, then cosmetic. Put `[BLOCKING]` in front of any blocking item so it's visible at a glance. If this persona has no feedback, say so explicitly.

**Finally — name the one fix**
What is the one change to the spec that would most improve this persona's reaction to it? Name a specific thing in the spec — a section, a field, a behavior, a feature — and say what should change. "Improve the documentation" is not specific enough. "Add a migration guide to the Setup section covering how to convert config files from the legacy format" is.

---

### HOW TO FORMAT EACH CARD

```
### [C-XX] [Name] — [Role]

**Current approach:** [what they specifically do today]

**Gains from this spec:** [what changes for them, as a delta from current approach]

**Losses and switching costs:** [what they give up; "No significant losses identified — [explanation]" for Promoter-tier]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS justification:** [2–4 sentences: gains AND losses, both named, relative to current approach]

**Feedback:**
- [BLOCKING] [item]
- Major: [item]
- Minor: [item]
- Cosmetic: [item]

**Revision recommendation:** [specific spec element + what should change]
```

**Sort all 12 cards lowest NPS first, highest last.** Ties can go in any order within the tie.

---

### AFTER THE CARDS: AGGREGATE

Once all 12 cards are done, compute:

**Aggregate NPS:** [mean of the 12 scores, one decimal]
**Threshold (7.0):** MET | NOT MET [if NOT MET: "Spec requires revision before shipping"]
**Band distribution:** Promoters: X | Passives: X | Detractors: X
**Dominant Detractor objection:** [the single feedback theme most commonly raised by Detractors — include a count, e.g., "Migration burden (4 of 6 Detractors)"]

---

### WHO MATTERS MOST TO THE SCORE

Pick the 2–3 personas whose scores do the most to push the aggregate up or down. For each one, show the math: "If [C-XX] shifted from [their score] to [±2], the mean moves from [X.X] to [Y.Y]." Then say in one sentence why their weight is high. Don't frame this as who is closest to 7.0 — frame it as who moves the number most.

---

### BLOCKERS TO ESCALATE

**Blockers requiring resolution:**
Every `[BLOCKING]` item from the 12 cards, with the persona who raised it. If there are none: "No blocking issues identified."

---

### PROFESSIONAL READS

Write both professional perspectives. UX comes first.

**UX READ**
3–5 sentences from the perspective of a UX practitioner who has just read all 12 persona cards. What interaction patterns does the spec establish? Where does it create friction or leave behavior underspecified? What is the one change that would help the most personas?

**PM READ**
3–5 sentences from a product manager's perspective, drawing on the aggregate data and Detractor distribution. Does the spec solve the actual customer problem? What is the riskiest assumption in the design? What would you validate before shipping?

---

### RANKED REVISION LIST

**Pass 1:** The per-persona revision recommendations are already in each card.

**Pass 2 — Cross-persona ranked list:**
Look across all 12 revision recommendations and group the related ones. Rank the groups by (a) how many personas they affect and (b) the worst severity raised. You need **at least 2 entries** in the ranked list — if you only name one change you haven't ranked anything. Write it as a numbered list:

1. [Spec change] — [N personas]; max severity: [level]
2. [Spec change] — [N personas]; max severity: [level]
[continue]

---

### CROSS-PERSONA THEME MATRIX

This is the last substantive section. After this, no new analysis.

| Theme | Personas | Severity Distribution | Highest Severity |
|-------|----------|-----------------------|-----------------|
| [Theme] | C-XX, C-YY | [X blocking, Y major, Z minor, W cosmetic] | [level] |

Every row needs per-severity counts — not just the worst level.
