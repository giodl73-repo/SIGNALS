---

## draft-pitch — Variations R2

**5 variations across 3 single-axis + 2 combined axes:**

| ID | Axis | Hypothesis | Criteria targeted |
|----|------|------------|------------------|
| **V-01** | Self-check mechanism — binary sentence gate | Named standalone output + Y/N test makes C-10 mechanically unbypassable vs. R1's narrative self-check | C-10, C-03 |
| **V-02** | Positioning lock format — fill-in-the-blank templates | Sentence starters force specific completions; partial sentences can't be dismissed as ambient context | C-11, C-09 |
| **V-03** | Default presentation — unconditional DEFAULTS TABLE | Top-level table present before any intake step; C-12 survives intake-step misread | C-12, C-09 |
| **V-04** | Sentence gate + DEFAULTS TABLE (V-01+V-03) | Two simplest structural additions achieve C-10+C-12 with lower complexity than R1 V-05 | C-10, C-12 |
| **V-05** | All three axes + audience-sequenced framing | Audience-first ordering + all enforcement mechanisms = more persuasive output at same quality ceiling | C-10, C-11, C-12, C-08, C-09 |

**Key structural differences from R1:**

| Pattern | R1 V-05 | R2 variant |
|---------|---------|------------|
| C-10 | Narrative self-check ("draft, apply the test") | Binary Y/N gate — explicit YES/NO, mandatory rewrite loop before next step |
| C-11 | Open Q&A ("The real competition is not X. It is ___") | Fill-in-the-blank sentence templates — structure constrains valid completions |
| C-12 | Conditional fallback inside Signal Intake | Unconditional DEFAULTS TABLE at skill top — always loaded, never buried in a conditional |

**Predicted discriminator:** All five variations are predicted to pass C-10/C-11/C-12 (each carries R1 V-05's proven mechanisms for the two axes not being varied). If the aspirational ceiling flattens, discrimination will again fall to C-08 (proof audit step presence). V-01/V-02/V-03 all include proof audit steps, so the field may produce another all-Golden round.

Saved to `simulations/quest/variations/draft-pitch-variations-R2-2026-03-14.md`.
med, isolated output ("EXEC OPENING SENTENCE") combined with a binary pass/fail gate (Y/N + mandatory rewrite) enforces C-10 more mechanically than a narrative self-check. The model cannot skip the gate because it produces a labeled output that the next step references by name.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**Step 1: Signal Intake**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

List signals found, or write: "No prior signals -- using defaults."

If no prior signals: set Primary Competitor = "teams doing nothing / the review that never happened"; set Outcome = "know what you know before you commit"; set Ruling Out = "Signal is not a test runner and not a documentation generator."

---

**Step 2: Positioning Lock**

Before writing any pitch content, answer these three questions. Your answers are locked inputs for Step 4.

1. **Competitor**: "The real competition for teams using {topic} is not a named tool. It is ___." (Complete this sentence.)
2. **Outcome**: "Signal gives {primary audience} ___ they could not get before." (Complete this sentence.)
3. **Ruling out**: Name two specific categories Signal is NOT and one specific function it does not perform in each.

---

**Step 3: EXEC OPENING GATE**

This step produces a single named output. Do not proceed to Step 4 until this gate is passed.

**Write EXEC OPENING SENTENCE:**

> [Write one sentence here. Do not write any other exec content yet.]

**Apply gate test:**

Read the sentence you wrote. Answer: Does this sentence name a cost, risk, or productivity consequence that teams face today -- without mentioning a product feature, technology, or tool name?

- If **YES**: this sentence passes the gate. Continue to Step 4.
- If **NO**: rewrite EXEC OPENING SENTENCE now. Reapply the gate test. Repeat until YES.

**Gate passed. EXEC OPENING SENTENCE is locked.**

---

**Step 4: Full Draft**

Write all three versions using the locked inputs from Step 2 and the locked opening from Step 3.

**Exec Version**:
- **Hook**: Use EXEC OPENING SENTENCE exactly as written in Step 3.
- **What It Does**: Use the Outcome answer from Step 2. One sentence.
- **Why It Matters**: ROI or risk framing. Name the Competitor from Step 2 explicitly: "The alternative is ___."
- **Call to Action**: One specific ask -- decision, demo slot, budget line. Not "learn more."

**Dev Version**:
- **Hook**: A concrete scenario an engineer recognizes. Not a business case.
- **What It Does**: Show at least one concrete interaction -- a command, artifact name, or workflow step. The reader can answer "what would I actually type?"
- **Why It Matters**: Name one specific friction in the developer's daily workflow that this eliminates.
- **Call to Action**: One action available today without PM approval.

**Maker Version**:
- **Hook**: A question the reader has already asked themselves. Zero acronyms. Zero namespace references.
- **What It Does**: Plain English only. If you use a technical term, replace it with what it does for a person.
- **Why It Matters**: Connect to the maker's work -- design, writing, research, decisions. Not engineering work.
- **Call to Action**: Something they can do or propose without filing a ticket.

---

**Step 5: Anti-Positioning**

Write "## What Signal Is NOT" using the Ruling Out answers from Step 2 plus one additional category.

Format: bulleted list. Each bullet: `[Category]. Signal does not [specific function].`

Minimum: three bullets. Vague statements ("not just another AI tool") do not count.

---

**Step 6: Proof Points**

For each factual claim in the exec and dev versions, annotate:
- `[source: {artifact-path}]` if linked to a file in simulations/
- `[source: prior signal]` if attributed to a loaded scout artifact
- `[UNVERIFIED]` if not sourced

Remove or hedge unverified claims before saving.

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

Working notes (Steps 1-3, 6) are not saved to artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-02 -- Single Axis: Positioning Lock Format (Fill-in-the-Blank Templates)

**Axis**: Positioning lock format -- instead of answering open questions, the positioning lock uses sentence-starter templates that force specific completions. Templates are partial sentences; they cannot be answered with ambient inference -- they must be completed in writing.

**Hypothesis**: Sentence-starter templates constrain the shape of valid answers, producing more specific and citable locked outputs than free-form Q&A. A partial sentence cannot be dismissed as background context -- it must be completed. Satisfies C-11 structurally. Fill-in-the-blank defaults make C-12 cold-start safe.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**Step 1: Signal Intake**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`

List signals found: "Signals: [list files]" or "No prior signals."

---

**Step 2: Positioning Lock -- Complete Every Template**

Complete each sentence template below. These are locked inputs. Do not draft any pitch content until all five templates are filled. Partial answers are not acceptable -- every blank must be filled.

**Template A -- The Inertia Statement:**
"Teams working on {topic} skip Signal and instead they ___. The cost of that choice shows up as ___."

**Template B -- The Outcome:**
"With Signal, {primary audience} know ___ before they write the first line of code."

**Template C -- The Competitor Displacement:**
"The real competition is not Cursor, Copilot, or any named tool. It is ___."

**Template D -- Ruling Out #1:**
"Signal is not a ___. It does not ___. A team that needs ___ should use ___ instead."

**Template E -- Ruling Out #2:**
"Signal is not a ___. It does not ___. The confusion happens because ___, but the difference is ___."

If no prior signals were found in Step 1, use these defaults to begin your completions:
- Template A default start: "skip any pre-build investigation and rely on the first meeting's assumptions"
- Template C default: "the meeting that never happened, the spec review that came after the build, the go/no-go that no one called"

---

**Step 3: Exec Opening -- Write and Test**

Write the first sentence of the exec version now. Pull from Template A and Template B to inform it. The sentence must name a cost or risk consequence teams face today -- not a feature, not a technology, not the tool's name.

Write your sentence. Read it back. If it opens with a feature or tool description, rewrite it using the cost/consequence from Template A. Continue only once the opening names a business consequence.

---

**Step 4: Full Draft**

Write all three versions. Use the completed templates as your source material -- they are inputs, not suggestions.

**Exec Version**:
- **Hook**: The exec opening sentence from Step 3.
- **What It Does**: Template B completion. One sentence.
- **Why It Matters**: Template C completion woven into a 2-3 sentence ROI statement. The competitor (Template C) must be named explicitly.
- **Call to Action**: One decision, demo slot, or budget line ask.

**Dev Version**:
- **Hook**: A concrete engineering scenario -- the moment before Signal is used.
- **What It Does**: Show a command, artifact name, or specific workflow step. Format example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I type?"
- **Why It Matters**: The specific friction eliminated -- late-stage rework, undocumented assumptions, go/no-go that never happens.
- **Call to Action**: One command or file path the developer can run today.

**Maker Version**:
- **Hook**: A question the reader has already asked themselves. No acronyms. No tool names. No CLI references.
- **What It Does**: Describe what changes for them in plain English. If you use a namespace name (scout, draft, prove), replace it with what it does.
- **Why It Matters**: Connect to their decision-making work -- not to engineering or infrastructure.
- **Call to Action**: Something they can do or propose in a meeting without needing engineering approval.

---

**Step 5: Anti-Positioning**

Write "## What Signal Is NOT" using Template D and Template E completions as the first two bullets. Add a third bullet for an additional adjacent category.

Each bullet format: `[Category]. Signal does not [specific function]. [One sentence clarifying why the distinction matters.]`

---

**Step 6: Proof Points**

Annotate each factual claim in exec and dev with:
- `[source: {artifact-path}]` -- file reference
- `[source: prior signal]` -- scout artifact attribution
- `[UNVERIFIED -- hedge before delivery]` -- unfounded claims

Remove or hedge all UNVERIFIED claims before saving.

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

Templates (Step 2), exec opening test (Step 3), and proof audit (Step 6) are working notes -- not saved.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-03 -- Single Axis: Default Presentation (Unconditional DEFAULTS TABLE)

**Axis**: Default presentation -- a dedicated SIGNAL DEFAULTS section appears at the very top of the skill, unconditionally, before any intake or conditional logic. The table is always present. Signal intake values override defaults if found; defaults apply as-is if not.

**Hypothesis**: Promoting defaults from a conditional branch inside Signal Intake to an unconditional top-level section means C-12 cannot be skipped by intake-step misread. The defaults are loaded before the first conditional. A cold-start run with no scout artifacts produces correct C-09 framing unconditionally.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**SIGNAL DEFAULTS**

These defaults apply to all runs. Override with scout signal values when available. Use as-is when no scout signals exist.

| Field | Default Value |
|-------|---------------|
| Primary competitor | "teams doing nothing -- the review that never happened" |
| Inertia cost | "features built on assumptions that a 30-minute investigation would have invalidated" |
| Outcome statement | "know what you know before you commit" |
| Ruling out #1 | "Signal is not a test runner. It does not execute your code." |
| Ruling out #2 | "Signal is not a documentation generator. It does not produce specs from existing code." |
| Ruling out #3 | "Signal is not a project manager. It does not assign work, track sprints, or file tickets." |
| Proof fallback | "technique experiments across 730+ scenarios (see simulations/techniques/)" |

---

**Step 1: Signal Intake**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

For each file found, extract:
- Primary competitor override (replaces DEFAULTS table row if found)
- Outcome statement override (replaces DEFAULTS table row if found)
- Ruling out candidates (add to DEFAULTS table rows if found; do not replace)

Write your active values table:

| Field | Active Value | Source |
|-------|-------------|--------|
| Primary competitor | [default or override] | [DEFAULTS / scout file name] |
| Inertia cost | [default or override] | [DEFAULTS / scout file name] |
| Outcome statement | [default or override] | [DEFAULTS / scout file name] |
| Ruling out #1 | [default or from scout] | [DEFAULTS / scout file name] |
| Ruling out #2 | [default or from scout] | [DEFAULTS / scout file name] |

---

**Step 2: Positioning Lock**

Answer in writing before any pitch content is drafted.

1. **Competitor framing**: "The real competition is not a named tool. It is [active Primary competitor value]." (Write this complete sentence.)
2. **Outcome framing**: "Signal gives {primary audience}: [active Outcome statement value]." (Write this complete sentence.)
3. **Anti-positioning ruling**: List active Ruling Out values from the active values table.

---

**Step 3: Exec Opening -- Write and Test**

Write the first sentence of the exec version. It must name a cost or risk consequence before any product feature or technology mention. Use the active Inertia cost value as your source.

Read the sentence. If it opens with a feature or tool description, rewrite it. Continue only after the opening passes.

---

**Step 4: Full Draft**

Write all three versions using active values from Step 1 and locked answers from Step 2.

**Exec Version**:
- **Hook**: Exec opening from Step 3.
- **What It Does**: Outcome framing sentence from Step 2 (answer 2). One sentence.
- **Why It Matters**: 2-3 sentences. Include the competitor framing from Step 2 (answer 1) explicitly.
- **Call to Action**: One specific ask. Decision, demo slot, or budget line.

**Dev Version**:
- **Hook**: A scenario the engineer is already in -- the moment before Signal changes what happens next.
- **What It Does**: Show the interaction. Minimum one concrete example: a command, an artifact name, or a workflow step. Reader answers "what would I type?"
- **Why It Matters**: The specific friction this eliminates from their workflow -- name it directly.
- **Call to Action**: One thing they can run or open today without PM involvement.

**Maker Version**:
- **Hook**: A question they've already had. Zero unexplained acronyms. Zero namespace references.
- **What It Does**: Plain language. No Signal terminology -- translate every internal term to what it does for a person.
- **Why It Matters**: Their work context -- design, writing, research, stakeholder decisions. Not engineering.
- **Call to Action**: Something they can do or propose in a meeting.

---

**Step 5: Anti-Positioning**

Write "## What Signal Is NOT" using the active Ruling Out values from the active values table. Minimum three bullets.

Format: `[Category]. Signal does not [specific function].`

---

**Step 6: Proof Points**

For each factual claim in exec and dev:
- `[source: {artifact-path}]` or `[source: prior signal]` if sourced
- `[UNVERIFIED]` if not sourced; replace with hedged language or the active Proof fallback value before saving

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-04 -- Combined: Binary Sentence Gate + Unconditional DEFAULTS TABLE

**Axes**: Self-check mechanism (V-01 sentence gate) + Default presentation (V-03 DEFAULTS TABLE)

**Hypothesis**: The two structurally simplest additions to a baseline skill -- an unconditional defaults table and a binary sentence gate -- together satisfy C-10 and C-12 with lower prompt complexity than V-05's 5-step structure. C-11 is satisfied by the positioning lock Q&A format (same as R1 V-05). The combined structure is easier to maintain while achieving the same aspirational ceiling.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**SIGNAL DEFAULTS**

Always-on. Override with scout values when found. Use as-is when no scout signals exist.

| Field | Default |
|-------|---------|
| Primary competitor | "teams doing nothing -- the meeting that never happened" |
| Inertia cost | "features built on untested assumptions ship late, get cut, or get returned" |
| Outcome | "know what you know before you commit" |
| Ruling out #1 | "Signal is not a test runner. It does not execute code." |
| Ruling out #2 | "Signal is not a documentation tool. It does not write specs from code." |
| Proof fallback | "technique experiments across 730+ scenarios (simulations/techniques/)" |

---

**Step 1: Signal Intake**

Load:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`

List files found, or: "No prior signals -- using SIGNAL DEFAULTS."

For each file found, note which SIGNAL DEFAULTS rows the signal overrides.

---

**Step 2: Positioning Lock**

Answer these three questions in writing before any pitch content is drafted. These are locked -- the draft step cannot override them.

**Q1 -- Competitor**: "The real competition is not a named tool. It is ___."
(Use active Primary competitor value, or override from scout signal.)

**Q2 -- Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
(Use active Outcome value, or override from scout signal.)

**Q3 -- Ruling out**: List three categories Signal is NOT (use active Ruling Out values from SIGNAL DEFAULTS, override with scout values if found).

---

**Step 3: EXEC OPENING GATE**

Produce one named output before any exec content is drafted.

**Write: EXEC OPENING SENTENCE**
> [Write one sentence here -- nothing else in this step]

**Binary gate:**
Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence teams face today -- without mentioning a feature, tool, or technology?
- **YES** -- sentence passes. Proceed to Step 4.
- **NO** -- rewrite EXEC OPENING SENTENCE. Use the active Inertia cost from SIGNAL DEFAULTS as your anchor. Re-apply binary gate. Repeat until YES.

EXEC OPENING SENTENCE is now locked.

---

**Step 4: Full Draft**

Write all three versions.

**Exec Version**:
- **Hook**: EXEC OPENING SENTENCE (exact, from Step 3).
- **What It Does**: Q2 completion (one sentence).
- **Why It Matters**: ROI framing. Use Q1 competitor explicitly: "The alternative is [Q1 answer]. Signal eliminates that cost before the build starts."
- **Call to Action**: One specific ask.

**Dev Version**:
- **Hook**: A scenario the engineer is in right now.
- **What It Does**: Show at least one command, artifact name, or workflow step. Format example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I type?"
- **Why It Matters**: One specific friction eliminated -- name it.
- **Call to Action**: One runnable action today.

**Maker Version**:
- **Hook**: A question they've already asked. No acronyms, no namespace terms, no CLI references.
- **What It Does**: Plain English. Translate every Signal term to its function for a person.
- **Why It Matters**: Their decision context, not engineering.
- **Call to Action**: Something proposable in a meeting without a ticket.

---

**Step 5: Anti-Positioning**

Write "## What Signal Is NOT" from Q3 Ruling Out values. Minimum three bullets.

Format: `[Category]. Signal does not [specific function].`

---

**Step 6: Proof Points**

Annotate each factual claim:
- `[source: {path}]` or `[source: prior signal]` if sourced
- `[UNVERIFIED]` if not; replace with active Proof fallback value before saving

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

SIGNAL DEFAULTS, positioning lock, sentence gate, and proof audit are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-05 -- Combined: All Three Axes + Audience-Sequenced Framing

**Axes**: Binary sentence gate (V-01) + fill-in-the-blank templates (V-02) + unconditional DEFAULTS TABLE (V-03) + audience-sequenced output framing

**Hypothesis**: Starting from what each audience needs to see first (audience-first sequencing), then applying all three enforcement mechanisms, produces pitch content that feels less templated and more crafted -- while structurally satisfying all five aspirational criteria. The audience-sequenced frame anchors the PM pass in reader psychology, not in structural compliance, so outputs are more persuasive at the same quality ceiling.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**SIGNAL DEFAULTS**

These apply unconditionally. Override with scout signal values when found.

| Field | Default Value |
|-------|---------------|
| Primary competitor | "teams doing nothing -- the review that never happened" |
| Inertia cost | "building on assumptions that a 30-minute investigation would have invalidated" |
| Exec outcome | "know what you know before you commit" |
| Dev friction | "late-stage requirement changes that trace back to questions nobody asked before starting" |
| Maker outcome | "stop finding out you built the wrong thing after you built it" |
| Ruling out #1 | "Signal is not a test runner. It does not execute code or run CI." |
| Ruling out #2 | "Signal is not a documentation generator. It does not produce specs from existing code." |
| Ruling out #3 | "Signal is not a project manager. It does not assign work, track sprints, or file tickets." |
| Proof fallback | "technique experiments across 730+ scenarios in simulations/techniques/" |

---

**Step 1: Signal Intake**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

Write: "Signals found: [list]" or "No prior signals -- SIGNAL DEFAULTS apply."

For each signal found: note which DEFAULTS rows it overrides and what the override value is.

---

**Step 2: Audience Mapping**

Before writing any pitch, answer this question for each audience: "What is the first thing this person needs to believe before they can be moved by any other argument?"

- **Exec**: "The first thing the exec must believe is ___." (Cost, risk, or productivity frame.)
- **Dev**: "The first thing the developer must believe is ___." (That this saves them real time on real problems, not theoretical productivity gains.)
- **Maker**: "The first thing the maker must believe is ___." (That they can actually do this -- "can I do this?" not "is this technically impressive?")

These are the hooks for each version. Write them before drafting.

---

**Step 3: Positioning Lock -- Complete Every Template**

Complete each template before any pitch prose begins. These are locked inputs.

**Template 1 -- Competitor Displacement:**
"Teams building {topic} today don't use Signal. Instead, they ___. The moment that catches up with them is when ___."

**Template 2 -- Outcome:**
"Signal gives {primary audience} ___. They couldn't get this before because ___."

**Template 3 -- Ruling Out:**
Write each active Ruling Out value from SIGNAL DEFAULTS as: "[Category] is not Signal because Signal does not [function]. Teams that need [function] should use [adjacent tool] instead."

**Template 4 -- Inertia Displacement:**
"The real competition for Signal is not a named product. It is ___. That competitor wins by default when ___."

---

**Step 4: EXEC OPENING GATE**

This step produces a single named output. Step 5 cannot begin until this gate passes.

**Write: EXEC OPENING SENTENCE**
> [One sentence only. Nothing else in this step.]

**Binary gate:**
Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence without mentioning a feature, tool, or product?

- **YES** -- proceed.
- **NO** -- rewrite using the active Inertia cost from SIGNAL DEFAULTS. Re-apply gate. Repeat until YES.

EXEC OPENING SENTENCE is locked.

---

**Step 5: Full Draft**

Write each version starting from the audience belief established in Step 2. Use locked template completions from Step 3 as source material.

**Exec Version**
*Target belief from Step 2: [exec belief]. Lead to that belief, then through it.*

- **Hook**: EXEC OPENING SENTENCE (locked, exact).
- **What It Does**: Template 2 completion. One sentence. Outcome framing only.
- **Why It Matters**: Template 1 + Template 4 completions woven into 2-3 sentences. The competitor from Template 4 must be named: "The alternative is not a competing tool -- it is [Template 4 answer]."
- **Call to Action**: One specific decision, demo slot, or budget line. Not "learn more."

**Dev Version**
*Target belief from Step 2: [dev belief]. Open with the scenario, not the pitch.*

- **Hook**: The scenario the developer is in right now. Not a business case. The moment before Signal changes what happens.
- **What It Does**: Show at least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Describe what comes back and why it matters for the next decision. Reader answers "what would I actually type?"
- **Why It Matters**: Name the specific friction eliminated. Use active Dev friction value from SIGNAL DEFAULTS if not overridden. One to two sentences.
- **Call to Action**: One command or file path the developer can use today. No PM required.

**Maker Version**
*Target belief from Step 2: [maker belief]. "Can I do this?" -- answer yes before explaining how.*

- **Hook**: The question they've already had. Zero acronyms. Zero namespace references. Zero CLI terminology. If they don't recognize the vocabulary, they stop reading.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person. Use active Maker outcome from SIGNAL DEFAULTS as the frame.
- **Why It Matters**: Their decision context -- design direction, user research, stakeholder alignment. Not engineering infrastructure.
- **Call to Action**: Something proposable in a meeting without needing to file a ticket or involve engineering.

---

**Step 6: Anti-Positioning**

Write "## What Signal Is NOT" from Template 3 completions. Minimum three bullets.

Format: `[Category]. Signal does not [specific function]. [One sentence clarifying why this distinction matters for {topic} specifically.]`

---

**Step 7: Proof Points**

For every factual claim in exec and dev versions, annotate:
- `[source: {artifact-path}]` -- direct file reference
- `[source: prior signal]` -- scout artifact
- `[UNVERIFIED]` -- flag; replace with hedged language or active Proof fallback value before saving

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

Working notes (SIGNAL DEFAULTS, Steps 1-4, Step 7 audit) are not included in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## R2 Design Notes

**What changed from R1:**

R1 discovered three structural patterns that produce 100: embedded self-check (V-05 S-4), positioning lockdown before prose (V-05 S-1/S-2/S-3), and default fallback values (V-05 Signal Intake). R1's V-05 implements all three in one approach.

R2 asks: are there other structural forms for each pattern that also enforce the criteria -- and what happens when you vary them independently?

**Key structural differences between R2 variations and R1:**

| Pattern | R1 V-05 implementation | R2 variant |
|---------|----------------------|------------|
| C-10 self-check | S-4 narrative ("Draft the sentence here. Apply the test.") | V-01/V-04/V-05: Binary gate with explicit Y/N + mandatory rewrite before next step begins |
| C-11 positioning lock | Open Q&A (S-1/S-2/S-3: complete this sentence) | V-02/V-05: Fill-in-the-blank templates that cannot be partially completed |
| C-12 default presentation | Conditional branch inside Signal Intake ("if no prior signals exist, proceed with...") | V-03/V-04/V-05: Unconditional DEFAULTS TABLE at skill top, loaded before any intake step |

**Predicted scores under v2 rubric:**

| Variation | C-10 | C-11 | C-12 | Predicted composite |
|-----------|------|------|------|---------------------|
| V-01 | PASS (binary gate) | PASS (Q&A, same as R1 V-05) | PASS (conditional defaults) | ~98 |
| V-02 | PASS (narrative test) | PASS (templates, stronger than Q&A) | PASS (inline defaults) | ~98 |
| V-03 | PASS (narrative test) | PASS (Q&A) | PASS (DEFAULTS TABLE, strongest) | ~98 |
| V-04 | PASS (binary gate) | PASS (Q&A) | PASS (DEFAULTS TABLE) | ~100 |
| V-05 | PASS (binary gate) | PASS (templates) | PASS (DEFAULTS TABLE) | ~100 |

**Note on C-10/C-11/C-12 scoring for V-01/V-02/V-03:** Each single-axis variation carries forward R1 V-05's proven mechanisms for the other two criteria. No variation is predicted to fail any of C-10/C-11/C-12. The axis variation is testing *which structural form is strongest* for each criterion, not whether the criterion passes at all.

**Predicted discriminator for R2:** Under v2 rubric, the denominator for aspirational criteria is 5 (not 2). C-10, C-11, C-12 are all now scoreable. If all five aspirational criteria pass in all variations, R2 may not discriminate at aspirational level -- discrimination may return to C-08 (traceable proof) and whether each variation includes a proof audit step.
