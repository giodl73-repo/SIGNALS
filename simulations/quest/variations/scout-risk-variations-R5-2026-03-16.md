# Quest Variate — scout-risk — Round 5

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence | Analyst-first → Auditor-second produces better interdependency coverage than a single-role pass |
| V-02 | Output format | Strict table schema with explicit column headers produces higher structural compliance than prose |
| V-03 | Phrasing register | Conversational imperative ("you will") with numbered steps reduces omission rate vs. declarative spec |
| V-04 | Inertia framing | Giving inertia its own dedicated section with 3-part anatomy produces a higher-quality inertia entry |
| V-05 | Combined: role sequence + format + enforcement | Two-role table prompt with enumerated forbidden phrases and back-pressure repair loops maximizes rubric coverage |

---

## V-01 — Role Sequence (Analyst → Auditor)

**Axis**: Role sequence — two named roles execute sequentially, each with a distinct scope.
**Hypothesis**: Splitting register construction from interdependency analysis forces the model to treat dependencies as a first-class pass rather than an afterthought.

---

You are running two roles sequentially: **Risk Analyst**, then **Dependency Auditor**. Complete Role 1 in full before beginning Role 2.

---

### ROLE 1 — Risk Analyst

Your job is to construct a risk register for the feature or decision described in the input.

**Step 1 — Inertia Risk**

Before any dimensional risk, you must produce the Inertia Risk entry. This entry is mandatory and must appear first. It cannot be omitted or moved.

The Inertia Risk asks: what is the risk that the status quo was already good enough and this feature was the wrong thing to build? Frame it as a named risk entry using the full anatomy below.

**Step 2 — Dimensional Risks**

Identify risks across the following five dimensions. You must cover at least three:

- **Technical** — implementation unknowns, platform constraints, integration complexity
- **Market** — adoption risk, behavior change required, competitive displacement
- **Compliance** — regulatory exposure, audit surface, data handling obligations
- **Dependency** — third-party services, platform APIs, external team deliverables
- **Timeline** — schedule risk, discovery-to-delivery gaps, dependency-induced delays

**Step 3 — Risk Anatomy**

Each risk entry (including inertia) must contain exactly three fields:

- **Severity**: one of `HIGH`, `MEDIUM`, or `LOW`. No other values.
- **Likelihood**: a condition-qualified statement. State the scenario or trigger under which this risk activates, not just a bare label ("high" alone is not acceptable).
- **Mitigation**: a concrete action, named owner class, or defined control. The following phrases are prohibited — if you find yourself writing any of them, stop and replace: "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "address as needed". Each mitigation must state what to do, not that something should happen.

**Step 4 — Ordering**

After the inertia risk, order remaining entries from highest to lowest severity. For ties, place the risk with higher likelihood first.

**Step 5 — Dimension Labels**

Tag every risk entry with its dimension label (e.g., `[Technical]`, `[Market]`). The inertia risk is tagged `[Inertia]`.

---

### ROLE 2 — Dependency Auditor

You now receive the risk register produced by Role 1. Your job is to produce a dedicated **Risk Interdependencies** section.

**Step 6 — Compound-Risk Mapping**

Review the register and identify every pair of risks where the activation of one changes the severity of another. For each pair:

- Name both risks (by title or number)
- State the severity transition: FROM the current severity TO the escalated severity
- Write each pairing as: "IF [Risk A] activates, [Risk B] escalates from [severity] to [severity]."

You must produce at least three distinct pairings.

If you cannot find three pairings, return to Step 2 and add or refine dimensional risks until three distinct pairings are supported. Do not leave the interdependency section with fewer than three entries.

**Step 7 — Severity Transition Audit**

Scan every pair you have written. Confirm each contains an explicit FROM/TO severity label. Pairs written as "A worsens B" or "A compounds B" without named severity values fail this check — rewrite them.

---

### AMEND Behavior

If the prompt contains an AMEND directive:

- **Focus on one dimension**: Retain the Inertia Risk entry unchanged. Restrict dimensional risks to the named dimension only. All anatomy requirements (severity, likelihood, mitigation) still apply.
- **Adjust severity thresholds**: Recalibrate severity labels per the stated threshold logic. Document the threshold adjustment at the top of the register.

---

## V-02 — Output Format (Strict Table Schema)

**Axis**: Output format — every section rendered as a table with enforced column schema.
**Hypothesis**: Explicit column headers reduce field-omission errors because each column creates a visible obligation for every row.

---

Produce a risk register as structured tables. Do not use prose paragraphs for risk entries. Every risk is a table row.

---

### Table Schema

**Main Register Table**

Use this exact column order:

| # | Dimension | Risk Title | Severity | Likelihood | Mitigation | Mitigation Type |

Column rules:

- **#**: Integer. Row 1 is always the Inertia Risk.
- **Dimension**: One of `Inertia`, `Technical`, `Market`, `Compliance`, `Dependency`, `Timeline`.
- **Risk Title**: 3–8 words, noun-phrase form (e.g., "SDK Migration Breaks Existing Contracts").
- **Severity**: Exactly one of `HIGH`, `MEDIUM`, `LOW`. No other values.
- **Likelihood**: A condition-qualified statement. Must name the scenario or triggering condition under which this risk activates. A bare label ("High", "Possible") is not acceptable — add the named condition.
- **Mitigation**: A concrete action, owner class, or control. Prohibited phrases — none of these may appear in any cell: "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "address as needed". If a cell contains any of these, replace it before submitting.
- **Mitigation Type**: One of `Spike`, `Validate`, `Gate`, `Contract`, `Cut`, `Instrument`. Select the type that best matches the mitigation's mechanism.

---

### Required Register Contents

**Row 1 — Inertia Risk (mandatory)**

Row 1 must be the Inertia Risk. This row is not optional and cannot be placed later in the table. The inertia risk asks: what is the probability that the status quo was already good enough and this build was unnecessary?

**Dimensional Coverage**

After row 1, include risks from at least three of the five dimensions: Technical, Market, Compliance, Dependency, Timeline.

**Ordering**

After the Inertia row, order remaining rows from `HIGH` to `LOW`. Within the same severity, order by likelihood (most likely first).

---

### Interdependency Table

After the main register, produce a second table with this schema:

| Pair | If This Risk Activates | Then This Risk Escalates | From | To |
|------|----------------------|--------------------------|------|----|

Rules:

- Minimum 3 rows. If you cannot identify 3 compound-risk pairs from the main register, return to the main register and add or refine entries until 3 pairs are supportable. Do not submit an interdependency table with fewer than 3 rows.
- **From** and **To** must each contain exactly one of `HIGH`, `MEDIUM`, `LOW`. A row without both values fails the schema.

---

### Mitigation Type Audit

After the interdependency table, include a one-line summary:

> Mitigation types used: [list distinct types]. Count: [N].

If N < 3, return to the main register and revise mitigations until at least 3 distinct types are represented. Do not finalize the register with fewer than 3 distinct mitigation types.

---

### AMEND Behavior

If an AMEND directive is present:

- **Focus on dimension X**: Row 1 (Inertia) is always retained. Rows 2–N cover dimension X only. All column rules remain in force.
- **Adjust severity thresholds**: Add a header row above the table stating the threshold adjustment. Apply the stated logic to all severity values.

---

## V-03 — Phrasing Register (Conversational Imperative)

**Axis**: Phrasing register — numbered steps, "you" framing, plain-English imperatives throughout.
**Hypothesis**: Conversational step-by-step framing reduces skip-rate on structural requirements compared to a specification-style prompt.

---

Your job is to build a risk register for the feature or decision described below. Follow these steps in order. Don't skip steps.

---

**Step 1: Write the Inertia Risk first.**

This one is required — every register starts with it, no exceptions.

Ask yourself: what's the chance the existing solution was already good enough, and building this was a mistake? That's your inertia risk. Give it a title, a severity (use HIGH, MEDIUM, or LOW — nothing else), a likelihood, and a mitigation. Put it at the top.

**Step 2: Add risks across at least three dimensions.**

Cover at least three of these five areas:

- What could go wrong technically? (Unknown implementation complexity, platform limits, integration failures)
- What could go wrong in the market? (No one adopts it, behavior change too hard, incumbents don't move)
- What's the compliance exposure? (Regulatory requirements, data handling obligations, audit surface)
- What dependencies could let you down? (Third-party APIs, external teams, platform availability)
- What could blow up the timeline? (Discovery gaps, late-breaking blockers, cascading delays)

For each risk you write, include all three of:
- **Severity** — HIGH, MEDIUM, or LOW (pick one, no other options)
- **Likelihood** — don't just say "high" or "possible." Name the condition or scenario that makes this risk real. Something like "if we're the first team to use this SDK version" or "if the compliance review finds PII in the schema."
- **Mitigation** — say what you'll actually do. Don't write "monitor closely," "keep an eye on," "revisit later," "consider alternatives," or "address as needed." If you catch yourself typing any of those, stop and replace with a concrete action.

**Step 3: Put them in order.**

After the inertia risk, sort the rest from highest to lowest severity. If two risks have the same severity, put the more likely one first.

**Step 4: Label every risk with its dimension.**

Tag each entry with where it fits: [Inertia], [Technical], [Market], [Compliance], [Dependency], or [Timeline].

**Step 5: Find the compound risks.**

Now read through your register and find pairs of risks where if one activates, another gets worse. Write a dedicated **Interdependencies** section. For each pair, write it like this:

> IF [Risk A] activates, [Risk B] escalates from MEDIUM to HIGH.

You need at least three pairs. If you look at your register and can't find three real pairs, go back to Step 2 and add more specific risks until three pairs are there. Don't skip this — a register with no interdependencies usually means the risks are too vague.

**Step 6: Check your mitigations one more time.**

Go back through every mitigation you wrote. For each one, ask: does this name a type of action? Classify it as one of: Spike, Validate, Gate, Contract, Cut, Instrument. Add the type label to the entry.

Then count how many distinct types you used. If you used fewer than three, go back and revise mitigations until you have at least three different types represented. Don't finalize until you do.

---

**If you got an AMEND instruction:**

- If it says to focus on one dimension — keep the inertia risk, then limit Step 2 to that dimension only. Everything else stays the same.
- If it says to adjust severity thresholds — note the adjustment at the top and apply it consistently. Don't drop the inertia risk.

---

## V-04 — Inertia Framing (Dedicated Section with 3-Part Anatomy)

**Axis**: Inertia framing — inertia risk gets a dedicated section with a 3-part diagnostic anatomy before the dimensional register begins.
**Hypothesis**: Separating inertia into its own framed section with named sub-components produces a more analytically grounded inertia entry than a single risk-row instruction.

---

You are producing a risk register. The register has two parts: the Inertia Section and the Dimensional Register. Complete them in order.

---

### Part 1 — Inertia Section

The inertia risk is not a dimensional risk. It is a structural question: could the status quo have been good enough, making this feature the wrong build? This section is mandatory. It cannot be omitted, summarized, or embedded inside the dimensional register.

Produce the Inertia Section as three named sub-components:

**1a. Current-State Assumption**
What was the team assuming about the current solution's inadequacy that justified building this? State the assumption explicitly.

**1b. Adoption Gap**
What change in user behavior, workflow, or integration does this feature require to deliver its value? The larger the required change, the higher the inertia risk.

**1c. Status Quo Durability**
How long could the current solution have remained viable without this build? If the answer is "indefinitely with minor adjustment," inertia risk is HIGH.

From these three sub-components, produce the Inertia Risk entry:

- **Severity**: HIGH, MEDIUM, or LOW
- **Likelihood**: Name the specific condition under which inertia proves out — e.g., "IF adoption-gap analysis shows users have active workarounds that meet 80%+ of the need."
- **Mitigation**: A concrete action that tests the current-state assumption before or early in the build — not after it ships.

The Inertia Risk entry appears first in the register. Label it `[Inertia]`.

---

### Part 2 — Dimensional Register

After the Inertia Section, produce dimensional risks. Cover at least three of these five dimensions:

- **Technical** — implementation unknowns, platform constraints, integration complexity
- **Market** — adoption risk, behavior change required, competitive displacement
- **Compliance** — regulatory exposure, audit surface, data handling obligations
- **Dependency** — third-party services, platform APIs, external team deliverables
- **Timeline** — schedule risk, discovery-to-delivery gaps, dependency-induced delays

**Risk Anatomy (required for every entry)**

Each risk entry must include:

- **Dimension label**: one of `[Technical]`, `[Market]`, `[Compliance]`, `[Dependency]`, `[Timeline]`
- **Severity**: `HIGH`, `MEDIUM`, or `LOW` — no other values accepted
- **Likelihood**: Expressed as a named triggering condition using IF-THEN form: "IF [named condition], THEN this risk activates." Bare labels ("high", "possible") are not acceptable.
- **Mitigation**: A named action with a type class prefix from: `Spike:`, `Validate:`, `Gate:`, `Contract:`, `Cut:`, `Instrument:`. The following phrases are forbidden — if any appear in a mitigation, replace before submitting: "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "address as needed".
- **Ordering**: After the Inertia entry, order dimensional risks from HIGH to LOW. Ties broken by likelihood.

**Mitigation Type Diversity**

After writing all entries, confirm at least 3 distinct type class prefixes appear across the register. If fewer than 3 are present, revise entries until the diversity threshold is met before proceeding.

---

### Part 3 — Interdependencies

Produce a dedicated section titled **Risk Interdependencies**.

For each compound-risk pair:

> IF [Risk Title A] activates, [Risk Title B] escalates from [FROM severity] to [TO severity].

Minimum: 3 pairs. Each pair must name both risks and include explicit FROM/TO severity values.

If you cannot identify 3 pairs from the current register, return to Part 2 and refine or add risks until 3 pairs are derivable. Do not finalize this section with fewer than 3 pairs.

---

### AMEND Behavior

- **Focus on dimension X**: Retain the full Inertia Section (all 3 sub-components + risk entry). Restrict Part 2 to dimension X only. All anatomy and ordering rules apply.
- **Adjust severity thresholds**: Apply the stated threshold logic to all severity fields. Document the threshold rule at the top of Part 2. The Inertia Section is not subject to threshold adjustment — treat its severity independently.

---

## V-05 — Combined (Role Sequence + Table Format + Maximum Enforcement)

**Axis**: Combined — two roles, table output, enumerated forbidden phrases, back-pressure repair loops, IF-THEN likelihood requirement.
**Hypothesis**: Combining role segmentation with table schema and explicit repair loops maximizes compliance across the full rubric simultaneously.

---

You are running two roles: **Register Builder**, then **Quality Enforcer**. Complete Role 1 fully before beginning Role 2. All output is produced as tables.

---

### ROLE 1 — Register Builder

**Step 1 — Inertia Risk (mandatory row 1)**

Before any other entry, produce the Inertia Risk as the first row of the main register. This row is not optional and cannot be skipped or repositioned.

The inertia risk asks: what is the probability that the status quo was sufficient and this build was unnecessary? Populate every column for this row.

**Step 2 — Dimensional Risks**

Add risks from at least three of: Technical, Market, Compliance, Dependency, Timeline.

**Step 3 — Main Register Table**

Produce the following table. Complete all columns for every row.

| # | Dimension | Risk Title | Severity | Likelihood (IF-THEN) | Mitigation (Type: Action) |
|---|-----------|------------|----------|-----------------------|---------------------------|

Column rules:

- **#**: Row 1 = Inertia Risk. Remaining rows ordered HIGH → MEDIUM → LOW.
- **Dimension**: `Inertia` / `Technical` / `Market` / `Compliance` / `Dependency` / `Timeline`
- **Severity**: Exactly `HIGH`, `MEDIUM`, or `LOW`. No other values. No numeric scores.
- **Likelihood (IF-THEN)**: Must use the form "IF [named condition], THEN this risk activates." Bare labels ("High", "Likely", "~40%") are not acceptable in any row.
- **Mitigation (Type: Action)**: Must begin with a type prefix from `Spike:`, `Validate:`, `Gate:`, `Contract:`, `Cut:`, `Instrument:`. The action following the prefix must be concrete. The following phrases are prohibited anywhere in this column — replace before submitting: "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "address as needed", "watch for", "track this".

**Step 4 — Type Diversity Check**

After completing the table, count distinct type prefixes used. If fewer than 3 distinct types appear, revise the Mitigation column in affected rows until 3 distinct types are present. Do not proceed to Role 2 until this threshold is met.

---

### ROLE 2 — Quality Enforcer

You receive the register from Role 1. Your job is to enforce structural quality and produce the interdependency section.

**Step 5 — IF-THEN Audit**

Scan every row in the Likelihood column. Any cell that contains a bare label without IF/THEN phrasing fails. Rewrite failing cells before proceeding.

**Step 6 — Forbidden Phrase Scan**

Scan every cell in the Mitigation column. Check for the following phrases:

> "monitor closely", "keep an eye on", "revisit later", "consider alternatives", "address as needed", "watch for", "track this"

If any of these appear, replace the affected cell with a concrete action using one of the type prefixes. Do not proceed until the scan returns zero matches.

**Step 7 — Interdependency Table**

Produce the following table:

| Pair # | IF This Risk Activates | THEN This Risk Escalates | From | To |
|--------|------------------------|--------------------------|------|----|

Rules:

- Minimum 3 rows.
- **From** and **To** must each contain exactly one of `HIGH`, `MEDIUM`, `LOW`.
- A row that says "A worsens B" without explicit From/To severity values fails the schema — rewrite it.

If fewer than 3 rows can be populated from the current register, return to Step 2 and add or refine dimensional risks until 3 distinct compound pairs exist. Do not finalize with fewer than 3 rows.

**Step 8 — Mitigation Type Summary**

Produce a one-line summary:

> Types used: [list]. Distinct count: N.

If N < 3, return to Step 4 and revise until N ≥ 3.

---

### AMEND Behavior

If an AMEND directive is present:

- **Focus on dimension X**: Row 1 (Inertia) is always retained unchanged. Rows 2–N are restricted to dimension X. All column rules remain in force for all rows.
- **Adjust severity thresholds**: Add a header row above the main table stating the threshold rule. Apply the stated logic to all Severity cells. Document which rows changed and the original value.

---

## Variation Summary

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| V-01 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ |
| V-02 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| V-03 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| V-04 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| V-05 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

**Key differentiators:**
- V-04 adds C-14 (IF-THEN) through a dedicated inertia anatomy section
- V-05 is the only variation covering C-12 (all likelihoods trigger-qualified) via the Step 5 audit and explicitly requiring IF-THEN in the column header itself
- V-02 and V-03 both achieve strong structural coverage through different delivery mechanisms (schema vs. plain-language steps)
- V-01's Auditor role is the only variation that cleanly isolates interdependency analysis from register construction as separate cognitive passes
