Written to `simulations/quest/variations/draft-pitch-variations-R1-2026-03-14.md`.

---

## draft-pitch — Variations R1 Summary

**5 variations across 4 axes:**

| ID | Axis | Hypothesis | Criteria targeted |
|----|------|------------|------------------|
| **V-01** | Inertia framing (single) | Leading with "what teams do instead" forces cost-first opening; C-09 impossible to miss | C-03, C-09 |
| **V-02** | Role sequence (single) | Strategy-before-PM locks positioning decisions before prose; PM becomes validator not author | C-03, C-07 |
| **V-03** | Output format — slot structure (single) | Labeled slots with embedded criteria prevent structural omissions at generation time | C-01, C-02, C-04 |
| **V-04** | Conversational register + compressed lifecycle | Second-person, single-pass format; faster coverage of essentials with less overhead | C-01, C-02, C-03, C-04 |
| **V-05** | Inertia-led + Strategy-first + Formal register | Highest-ceiling combination; Step 2 lockdown + proof audit targets all 9 criteria | C-03, C-07, C-08, C-09 |

**Key design choices:**
- V-03's slot structure is the safety net — hardest for a model to produce a structurally incomplete output
- V-05's S-4 "Exec Opening Test" makes C-03 a self-check inside generation, not just a scoring criterion after the fact
- V-04 trades C-08 depth for speed — good baseline, not the golden candidate
- V-01 and V-02 are cleanest for isolating which single factor most reliably produces a passing exec version
e compliance question that was never asked -- until week 6 of implementation. Every version of the pitch must be built on top of the answer to that question.

---

**Produce three versions.** Each version has four required parts: Hook, What It Does, Why It Matters, Call to Action. Do not omit any part in any version.

---

### EXEC VERSION

**Audience**: VP or Director. They have 90 seconds. They care about cost, risk, and productivity -- not how it works.

- **Hook**: Open with a cost or risk statement. Not a feature. Not a technology description. The first sentence must name a consequence teams face today without this tool (wasted time, late-stage rework, compliance gaps, missed market windows). If your first sentence describes what the tool does, rewrite it.
- **What It Does**: One sentence. Outcome-framing only. "Signal gives every developer the investigation they needed before they started building."
- **Why It Matters**: Two to three sentences. ROI or risk framing. Connect to a cost the exec already owns.
- **Call to Action**: One specific ask. Not "learn more." A decision, a demo slot, a budget line.

---

### DEV VERSION

**Audience**: Engineer who will actually use it. They are skeptical of PM decks. They want to know what they would type.

- **Hook**: A concrete scenario. Not a business case. "You're about to implement X. Here's what happens next."
- **What It Does**: Show the interaction. A command, a file, an artifact. The reader should be able to answer "what would I actually type or do?" after reading this section. Do not repeat exec ROI framing.
- **Why It Matters**: What problem in their daily workflow does this eliminate? Name the specific friction.
- **Call to Action**: One action they can take today. Try it, install it, run one command.

---

### MAKER VERSION

**Audience**: Non-technical contributor -- designer, writer, PM, researcher. No acronyms. No namespace references. No internal jargon. The framing is "can I do this?" not "here is how it's architected."

- **Hook**: A question they have already asked themselves. "Have you ever shipped a feature and then found out users didn't want it?"
- **What It Does**: Plain language. If you find yourself using a technical term, replace it with what it does for a person.
- **Why It Matters**: Connect to their work, not engineering work.
- **Call to Action**: Something they can do or propose without needing an engineer's approval.

---

### WHAT SIGNAL IS NOT

Write a short section titled "What Signal Is NOT." Rule out at least two adjacent categories. Examples: "Signal is not a test runner. It does not execute your code." / "Signal is not a documentation generator. It does not produce API docs." Be specific. Vague anti-positioning ("Signal is not just another AI tool") does not count.

---

**Output**: Write the full artifact. Use headings: `## Exec Version`, `## Dev Version`, `## Maker Version`, `## What Signal Is NOT`.
**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-02 — Single Axis: Role Sequence (Strategy Runs Before PM)

**Axis**: Role sequence -- Strategy role writes the narrative arc first; PM role validates and sources proof points second
**Hypothesis**: Running Strategy first produces stronger outcome framing because positioning decisions are locked before prose is written. PM's job becomes validation + sourcing, not narrative construction. Expected to improve C-03 and C-07.

---

### Prompt Body

You are writing a pitch deck narrative for: `{topic}`.

This skill runs two sequential passes. Do not skip or merge the passes.

---

**Pass 1 -- Strategy: Narrative Architecture**

You are acting as the Strategy role. Your job is to design the narrative spine before any prose is written.

Step 1: Load prior signals.
- Check `simulations/scout/positioning/` for `{topic}-positioning-*.md`
- Check `simulations/scout/competitors/` for `{topic}-competitors-*.md`
- List what you found (or note "no prior signals").

Step 2: Answer three questions. Write your answers before writing any pitch content.
1. What is the single most important outcome this product delivers? (One sentence, no features.)
2. Who is the primary competitor -- not a named tool, but what teams do instead today?
3. What is the one thing Signal is definitively NOT? (Ruling out an adjacent category.)

Step 3: Draft the narrative arc in outline form only:
- Exec arc: Problem (cost) -> Primary competitor (inertia) -> Solution (outcome) -> Proof -> Ask
- Dev arc: Scenario -> Interaction -> Friction eliminated -> Next step
- Maker arc: Question they already have -> Plain description -> Their work benefit -> Their action

---

**Pass 2 -- PM: Draft and Validate**

You are acting as the PM role. You have Strategy's narrative arc. Now write the full pitch.

Rules:
- Follow the arc. Do not reframe the strategy decisions.
- For each proof point you include, identify its source: an artifact path, a data file, or a direct claim from prior signals. If you cannot source it, flag it as UNVERIFIED.
- The exec version's first sentence must name a cost or risk. Read it back after writing it. If it mentions a feature or technology, rewrite it.

Write all three versions in full. Use the four required parts in each version: Hook, What It Does, Why It Matters, Call to Action.

Then write the "What Signal Is NOT" section. Pull the ruling-out statement from Strategy's Pass 1 answer #3, and add one more category.

---

**Output format**:
```
## Strategy Pass (outline only -- not shipped)
[arc decisions here]

## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
## PM Validation Notes
[sourced proof points and UNVERIFIED flags]
```

**Save artifact** (exec + dev + maker + anti-positioning only, not the strategy pass):
`simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-03 — Single Axis: Output Format (Explicit Slot Structure)

**Axis**: Output format -- each section is a labeled slot with explicit pass/fail criteria embedded in the prompt
**Hypothesis**: Structural slot format makes C-01 and C-02 pass mechanically (model cannot skip a slot). Embedding the criterion at the point of writing surfaces failures at generation time rather than at scoring time.

---

### Prompt Body

You are writing a pitch deck narrative for: `{topic}`.

First, check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- Note: "Signals found: [list]" or "No prior signals."

Now complete each labeled slot below. Every slot is required. Leaving a slot empty is a fail.

---

**[SLOT: EXEC-HOOK]**
_Criterion_: First sentence names a cost, risk, or productivity consequence. It does not name a feature or describe the tool.
Write 1-2 sentences.

**[SLOT: EXEC-WHAT]**
_Criterion_: One sentence. Outcome framing only.
Write 1 sentence.

**[SLOT: EXEC-WHY]**
_Criterion_: ROI or risk framing. Connects to a cost the exec already owns.
Write 2-3 sentences.

**[SLOT: EXEC-CTA]**
_Criterion_: One specific ask. A decision, a slot, a budget line. Not "learn more."
Write 1 sentence.

---

**[SLOT: DEV-HOOK]**
_Criterion_: A concrete engineering scenario. Not a business case.
Write 1-2 sentences.

**[SLOT: DEV-WHAT]**
_Criterion_: Shows a command, artifact, or workflow step. Reader can answer "what would I type?"
Write 2-4 sentences. Include at least one concrete example (command, file path, artifact name).

**[SLOT: DEV-WHY]**
_Criterion_: Names a specific friction in the developer's daily workflow, not general productivity claims.
Write 2-3 sentences.

**[SLOT: DEV-CTA]**
_Criterion_: One action the developer can take today without PM approval.
Write 1 sentence.

---

**[SLOT: MAKER-HOOK]**
_Criterion_: A question the maker role has already asked themselves. No jargon.
Write 1-2 sentences.

**[SLOT: MAKER-WHAT]**
_Criterion_: Plain language only. No acronyms, no namespace names, no CLI references.
Write 2-3 sentences.

**[SLOT: MAKER-WHY]**
_Criterion_: Connects to the maker's work (design, writing, research), not engineering work.
Write 2-3 sentences.

**[SLOT: MAKER-CTA]**
_Criterion_: Something they can do or propose without needing an engineer.
Write 1 sentence.

---

**[SLOT: ANTI-POSITIONING]**
_Criterion_: Names at least two specific adjacent categories this tool is NOT. Vague statements ("not just another AI tool") do not pass.
Format: bulleted list, 2-4 items, each with a one-line explanation.

---

After completing all slots, assemble the final artifact under these headings:

```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-04 — Combined: Conversational Register + Compressed Lifecycle

**Axes**: Phrasing register (conversational, first-person, imperative) + lifecycle emphasis (single-pass, no phases, lighter cognitive overhead)
**Hypothesis**: Removing the phase structure and using direct second-person address produces faster, less templated output while still covering essentials. Trade-off: may produce shallower proof sourcing (C-08 risk) but faster structural coverage (C-01/C-02/C-03/C-04).

---

### Prompt Body

Write a pitch deck narrative for: `{topic}`.

Quick check first: is there a positioning or competitor signal in `simulations/scout/`? If yes, use it. If not, skip and continue.

---

**Three versions. One pass. All required.**

---

**Exec version** -- your reader is a VP with 90 seconds and no patience for feature lists.

Open with what it costs teams today when they don't have this. Don't open with what the tool does -- open with what's broken. Then tell them what Signal fixes in one sentence (outcome only). Then make it real: ROI, risk reduction, or productivity numbers if you have them sourced. Close with one ask -- specific, actionable, something they can say yes to in the meeting.

One thing to check before you move on: read your first sentence back. Does it mention a feature or how the tool works? If yes, rewrite it. The exec version fails if it opens with features.

---

**Dev version** -- your reader is an engineer who has sat through too many PM pitches.

Start with a scenario they recognize: "You're about to implement something. Here's what you do today. Here's what changes." Show them what they'd actually run or open. A command. A file name. An artifact that comes back. Skip the business case -- they'll reject it on sight. Tell them what daily friction goes away. Close with the one thing they can do right now to try it.

---

**Maker version** -- your reader might be a designer, a researcher, or a PM. They are not reading the dev version. Write like you're explaining it to someone smart who doesn't know what a namespace is.

Start with a question they've already had -- something that happened to them. Describe what Signal does in language that doesn't require a terminal. Connect it to their actual work. Close with something they can do or propose without filing a ticket.

---

**What Signal Is NOT** -- two or three bullets. Be specific. Name actual adjacent categories (test runner, documentation generator, code assistant) and say clearly what Signal doesn't do. "Not just another AI tool" is not specific enough.

---

**Format and save**:
Use headings `## Exec Version`, `## Dev Version`, `## Maker Version`, `## What Signal Is NOT`.
Save to `simulations/draft/pitches/{topic}-pitch-{date}.md`.

---

## V-05 — Combined: Inertia-Led + Strategy-First Sequence + Formal Register

**Axes**: Inertia framing (primary competitor foregrounded throughout) + role sequence (Strategy writes arc, PM drafts) + formal/structured register
**Hypothesis**: Strongest combination for C-03, C-07, and C-09. Strategy-first enforces positioning decisions before prose; inertia-led framing ensures exec version opens correctly; formal register produces citable, traceable claims. Highest expected composite score but also most complex prompt.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

This is a structured two-role execution. Follow the steps precisely.

---

### Step 1: Signal Intake

Load all available prior signals for `{topic}`:

```
simulations/scout/positioning/{topic}-positioning-*.md
simulations/scout/competitors/{topic}-competitors-*.md
simulations/scout/requirements/{topic}-requirements-*.md
```

For each file found, extract:
- Primary competitor (the real one -- what teams do instead of using this tool)
- Whitespace claim (what no competitor owns)
- Outcome statement (what this product delivers, in one phrase)

If no prior signals exist, proceed with: Primary Competitor = "teams doing nothing / the review that never happened", Whitespace = "pre-implementation signal gathering", Outcome = "know what you know before you commit."

---

### Step 2: Strategy -- Positioning Lockdown

Before writing any pitch content, answer the following. These answers govern all three versions.

**S-1: Primary Competitor Statement**
Complete: "The real competition is not [named tool]. It is ___." This framing must appear in the exec version.

**S-2: Outcome Statement (one sentence)**
Complete: "Signal gives [audience] ___." No features. No technology. A consequence they care about.

**S-3: Anti-Positioning Ruling**
Name two specific categories Signal is NOT. Format: "[Category] -- Signal does not [specific function]."

**S-4: Exec Opening Test**
Draft the first sentence of the exec version here. Apply the test: does it name a cost, risk, or productivity consequence teams face today? If yes, proceed. If it names a feature or the tool itself, rewrite it until it passes.

---

### Step 3: PM -- Full Draft

Using Strategy's answers from Step 2, write all three pitch versions in full.

**Exec Version requirements:**
- First sentence: the cost or risk statement from S-4
- What It Does: the outcome statement from S-2
- Why It Matters: ROI or risk framing; name the primary competitor from S-1 explicitly
- Call to Action: one specific ask (decision, demo slot, budget line)

**Dev Version requirements:**
- Hook: a concrete engineering scenario (not a business case)
- What It Does: at least one concrete interaction -- command, artifact name, or workflow step; reader can answer "what would I actually type?"
- Why It Matters: specific friction eliminated from developer's daily workflow
- Call to Action: one action available today without PM approval

**Maker Version requirements:**
- Hook: a question the maker has already asked themselves; no jargon, no acronyms
- What It Does: plain-language description only; no namespace references, no CLI terminology
- Why It Matters: connection to the maker's work (not engineering work)
- Call to Action: something they can do or propose without filing a ticket

---

### Step 4: Anti-Positioning Section

Write the "What Signal Is NOT" section using S-3's rulings plus one additional category. Format as a bulleted list. Each bullet: "[Category]. Signal [specific thing it does not do]."

Minimum: three bullets. No vague statements.

---

### Step 5: Proof Point Audit

Before saving, review the exec and dev versions. For each factual claim (numbers, statistics, outcomes), annotate it with one of:
- `[source: {artifact-path}]` -- linked to a specific file in simulations/
- `[source: prior signal]` -- attributed to a loaded scout artifact
- `[UNVERIFIED -- needs sourcing]` -- flagged for PM action before delivery

Remove unverified claims from the final artifact or replace them with hedged language ("evidence from technique experiments suggests...").

---

### Output Format

```markdown
## Exec Version
[full exec pitch]

## Dev Version
[full dev pitch]

## Maker Version
[full maker pitch]

## What Signal Is NOT
[bulleted anti-positioning]
```

Strategy pass (Steps 1-2) and proof audit (Step 5) are working notes -- do not include in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`
