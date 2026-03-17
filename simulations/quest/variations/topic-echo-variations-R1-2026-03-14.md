---

## topic-echo — Variations R1

Five complete prompt variations written to `simulations/quest/variations/topic-echo-variations-R1-2026-03-14.md`.

---

### Summary

| # | Axis | Hypothesis |
|---|------|-----------|
| **V-01** | Role sequence | Split Reader / Synthesizer roles reduces summary contamination — reader can only flag, not explain |
| **V-02** | Output format | Table-first inventory forces explicit traceability and contrast columns before prose is written |
| **V-03** | Phrasing register | Conversational imperative drops role overhead; short direct sentences reduce drift |
| **V-04** | Lifecycle emphasis + Inertia framing | Named phases with gates prevent premature artifact generation; inertia lens ("what would doing nothing have missed?") strengthens design impact assessment |
| **V-05** | Role sequence + Output format | Named expert role ("Echo Archaeologist") + mandatory schema + self-check checklist — most structured; highest ceiling on C-02/C-03/C-05 coverage |

---

### Design notes on the axes

**V-01 vs V-05** test the role question from opposite ends: V-01 splits into two generic functional roles; V-05 creates a single named identity with professional standards. If the named role outperforms the split role, the identity frame matters more than the separation of concerns.

**V-02** is the format purist — the table forces every rubric column to be populated mechanically. It is the variation most likely to pass C-03 and C-05 consistently, and the one most likely to produce flat output on C-02 (naming) because the table feels administrative.

**V-03** is the counter-bet: stripping structure and trusting direct imperatives. It will produce the highest variance — best echoes may be most vivid; worst will miss traceability entirely.

**V-04** is the only variation that threads in the plugin's inertia framing from `plugin-plan.md`. The hypothesis is that the "would a team doing nothing have found this?" question naturally forces stronger design impact statements.
nfirms what was expected, it is not an echo item.
2. For each remaining surprise, assign a **named label** — a crystallized title that a future reader could immediately grasp. The name must be specific to the content. Examples of passing names: "The Inverted Adoption Curve", "The Missing Middle", "Compliance as Feature, Not Blocker". Examples of failing names: "Finding 1", "Surprise A", "Unexpected Result".
3. Check for **cross-signal surprises** — did any surprise only become visible when two or more signals were read together? If so, mark it as synthesized and cite both sources.
4. Check **breadth** — do your surprises span at least three distinct namespaces? If not, re-read the signals from underrepresented namespaces before closing.

**Write the artifact** at `simulations/{topic}/{topic}-echo-{date}.md`:

```markdown
# {Topic} Echo — {date}
*Unexpected findings after all essential signals were gathered.*

## Surprises

### {Named Label}
**Source**: {namespace/skill or artifact}
**What we expected**: {prior assumption}
**What we found**: {the surprise}
**Design impact**: {how this changes, challenges, or confirms the design direction}

[repeat for each surprise]

## Patterns
[optional — if two or more surprises point to the same root cause or structural signal, name the pattern here]
```

Aim for 3–6 surprises. More is not better. The echo should be readable in under ten minutes by someone who has never seen the signals.

---

## V-02 — Single axis: Output format (Structured table as inventory step)

**Axis**: Output format — mandate a structured table as the working inventory before the prose artifact is written.

**Hypothesis**: Requiring a table first forces explicit population of source, expectation, and impact columns, reducing the risk of producing surprises that are either untraceable or lack design consequence.

---

You are running `/topic:echo` for topic `{topic}`.

One question drives this skill: **"What did we learn that we didn't expect?"**

Not a summary. Not a status update. A synthesis of surprises — named, sourced, and assessed for what they mean to the design.

---

### Step 1 — Read all signals

Glob `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`. Read every artifact. Note what was unexpected.

---

### Step 2 — Build the surprise inventory table

Before writing the artifact, construct this table in your working memory (you may output it as a scratchpad):

| # | Candidate surprise | Source signal | Expected (what team assumed) | Actual (what signal showed) | Design impact | Include? |
|---|-------------------|--------------|-----------------------------|-----------------------------|---------------|----------|
| 1 | | | | | | yes/no |

**Rules for the Include? column:**
- YES: the finding could not appear in a standard findings document unchanged. Something about it violates a prior assumption.
- NO: the finding confirms what was expected. Drop it.

---

### Step 3 — Name each included surprise

For every row marked YES, assign a **named label**. The label must be specific to the content — a phrase a future reader remembers. Not "Finding 1". Not "Surprise A". Something like "The Phantom Dependency" or "Compliance Unlocks Adoption".

---

### Step 4 — Check the inventory for quality

Before writing, verify:
- [ ] At least one surprise is synthesized across two or more source signals (C-06)
- [ ] Surprises span at least three distinct namespaces (C-07)
- [ ] Every row has a non-empty "Expected" cell — if you cannot state what was assumed, the contrast is not explicit (C-05)

If any check fails, re-read signals from the underrepresented sources.

---

### Step 5 — Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

```markdown
# {Topic} Echo — {date}
*Unexpected findings synthesized from {N} signals across {namespaces listed}.*

## {Named Label}
**Source**: {signal or signals}
**Expected**: {what the team assumed going in}
**Actual**: {what the signal revealed}
**Design impact**: {one or more sentences on how this changes, challenges, or confirms the direction}

[repeat]

## Patterns
[If two or more surprises share a root cause, name the pattern. One sentence. This is optional but high-value.]
```

The echo is institutional memory. Write it for a reader who has never seen the signals and needs to understand why each surprise matters.

---

## V-03 — Single axis: Phrasing register (Direct imperative, conversational)

**Axis**: Phrasing register — conversational and direct rather than role-framed or procedural. Address the AI as a capable colleague, not as a role-player.

**Hypothesis**: Dropping the formal role framing and using short imperative sentences reduces prompt overhead and produces cleaner outputs by removing the cognitive load of maintaining a persona.

---

You are running `/topic:echo` for `{topic}`.

Ask yourself one question: **what did we learn that we didn't expect?**

Do not summarize the signals. Do not write a status update. Find the surprises — the things the signals revealed that the initial strategy didn't predict — and synthesize them into the echo artifact.

---

**Read the signals.** Glob `simulations/{topic}/` and all subdirectories. Read every `{topic}-*-{date}.md` artifact. As you read, keep a running list of anything that surprised you — findings that contradict, complicate, or fundamentally change what the team thought going in.

**Cull aggressively.** A surprise is not a finding. If it confirms what was expected, drop it. If it could appear unchanged in a standard research summary, drop it. Only keep the things where the gap between expectation and reality is real and significant.

**Name each one.** Before you write anything, name each surprise with a specific label — a phrase that crystallizes the insight. "The Missing Middle" is a name. "Finding 3" is not. The name should be memorable enough that someone who reads it six months from now knows exactly what it refers to.

**Trace each one back.** For every surprise, identify which signal it came from — which namespace, skill, or artifact. Surprises with no traceable source are opinions, not echoes. If you can't name the source, dig back through the signals.

**State the design consequence.** For each surprise, answer: so what? How does this change, challenge, or confirm the design direction? One sentence is enough. But it must be stated — never implied.

**Check your breadth.** Do your surprises come from at least three different namespaces? If most come from the same source, you haven't read the full signal set. Go back.

**Look for cross-signal surprises.** Did any finding only become visible because two signals were read together? If so, cite both and explain why neither alone would have revealed it.

**Write the echo.**

`simulations/{topic}/{topic}-echo-{date}.md`

Structure each surprise as:

```
## {Named Label}
Source: {signal or artifact}
Expected: {what was assumed going in}
Found: {what the signal actually showed}
Design impact: {how this changes, challenges, or confirms the direction}
```

End with a Patterns section if any two surprises share a common root. Keep the whole document under 800 words. It should be readable in under ten minutes by someone who wasn't on the team.

---

## V-04 — Combined: Lifecycle emphasis + Inertia framing

**Axis**: Lifecycle emphasis (explicit named phases with gates) + Inertia framing (the "status quo as competitor" lens — what would a team that chose to do nothing have missed?).

**Hypothesis**: Adding the inertia frame forces each surprise to be assessed not just for its design impact but for whether it strengthens or weakens the case against doing nothing — the most important competitive assessment. Explicit phase gates prevent skipping the reading phase to jump straight to artifact generation.

---

You are running `/topic:echo` for topic `{topic}`.

The echo is the final act of a topic investigation. It asks one question: **"What did we learn that we didn't expect?"**

It is not a summary. It is not a gate. It is a reflection — the surprises that only became visible because the team ran the signals. These surprises are what the next team most needs to read before they start.

There is one additional lens to apply: **the inertia question.** For each surprise, ask whether a team that chose to do nothing — that stayed with the status quo, the spreadsheet, the existing process — would have ever discovered this. If the answer is no, the surprise is also an argument for the feature. If the answer is yes, it complicates the case.

---

### Phase 1 — Signal Inventory (gate: do not proceed until complete)

Read all gathered signals for `{topic}`:
- `simulations/{topic}/` (strategy, story, previous echoes)
- `simulations/{topic}/**/{topic}-*-{date}.md` (all namespace artifacts)

For each signal, record:
1. The source (namespace + skill)
2. Whether it revealed anything that contradicts or significantly extends the initial strategy
3. The inertia verdict: would a team doing nothing have discovered this? (yes / no / maybe)

Do not write the artifact. Do not synthesize yet. Gate: you have a complete inventory of all signals.

---

### Phase 2 — Surprise Extraction (gate: do not proceed until complete)

From your inventory:
1. Discard anything that confirms expectations. The echo is not about what went as planned.
2. Discard anything that lacks a traceable source signal.
3. Rank remaining surprises by design impact: how much does this change what should be built, deprioritized, or reconsidered?
4. Keep 3–6 surprises. More dilutes the echo.

Gate: you have a ranked, culled list. Each item has a source and an inertia verdict.

---

### Phase 3 — Echo Writing

Write the artifact at `simulations/{topic}/{topic}-echo-{date}.md`.

Each surprise follows this structure:

```markdown
## {Named Label}

**Source**: {namespace/skill — e.g., "prove/interview", "scout/feasibility"}
**Expected**: {what the team assumed before this signal}
**Found**: {what the signal actually showed}
**Design impact**: {how this changes, challenges, or confirms the design direction — explicit, not implied}
**Inertia signal**: {would a team that chose to do nothing have discovered this? What does the answer mean for the case for this feature?}
```

**Naming rules**: The label must be specific and memorable. It must crystallize the surprise. "The Inverted Adoption Curve" passes. "Unexpected Finding" fails.

---

### Phase 4 — Synthesis check

After writing all surprises:
1. Do any two or more surprises share a root cause or point to the same structural signal? If yes, add a **Patterns** section naming the pattern.
2. Do surprises span at least three namespaces? If not, re-read underrepresented signals.
3. Is at least one surprise synthesized across two or more source signals?

Revise the artifact if any of these checks fail.

---

The echo stands alone. Write it for a reader who has never seen the signals. No jargon without explanation. No references to internal shorthand. When someone joins the team six months from now and reads this document, they should understand why each surprise mattered — and why the team that skipped this step would have shipped something different.

---

## V-05 — Combined: Role sequence + Output format (Named role + mandatory schema)

**Axis**: Role sequence (named expert role — the "Echo Archaeologist") + Output format (mandatory schema with explicit section requirements enforced by checklist).

**Hypothesis**: Giving the AI a named, specific role with a professional identity ("Echo Archaeologist") rather than a generic instruction produces higher-quality naming and contrast, because the role creates a frame of what excellence looks like. The mandatory schema with checklist prevents structural omissions.

---

You are running `/topic:echo` for topic `{topic}`.

---

### Your role: Echo Archaeologist

You are an Echo Archaeologist. Your specialty is reading signal artifacts and extracting the surprises — the findings that only became visible because someone ran the investigation. You are not a summarizer. You do not report what happened. You surface what was not predicted.

An Echo Archaeologist's standard:
- Every finding in your output must be traceable to a source signal. Untraceable findings are not findings; they are opinions.
- Every finding must have a name — not a number or a letter. A name crystallizes the surprise into something a future reader remembers.
- Every finding must answer "so what?" — how does this change, challenge, or confirm the design direction? Impact is not implied. It is stated.
- The best echoes surface surprises that only became visible when two or more signals were read together. This is cross-signal archaeology.

---

### Step 1 — Excavation

Glob and read all signals:
- `simulations/{topic}/` directory
- `simulations/{topic}/**/{topic}-*-{date}.md`

As you read, flag anything that violates prior assumptions. Note the source for each flag. A prior assumption is what the team believed before the signal arrived — reconstruct it from the strategy file or from context clues in the artifact itself.

---

### Step 2 — Curation

From your flagged list:
- Remove any finding that could appear unchanged in a standard research summary. If it doesn't surprise, it doesn't belong.
- Remove any finding you cannot trace to a source signal.
- Keep 3–6 surprises. An echo with twelve items is not sharp — it is a dump.

---

### Step 3 — Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

**Required sections in order:**

#### Header
```markdown
# {Topic} Echo — {date}
*{N} surprises synthesized from {N} signals across {namespace list}.*
```

#### One section per surprise (repeat for each)
```markdown
## {Named Label}
**Source**: {namespace/skill — be specific: "prove/interview Round 2", not just "prove"}
**Expected**: {what the team assumed before this signal existed}
**Found**: {what the signal actually revealed}
**Design impact**: {how this changes, challenges, or confirms the direction — minimum one sentence, maximum three}
```

#### Patterns section (required if applicable, omit only if no pattern exists)
```markdown
## Patterns
{If two or more surprises share a root cause or structural signal, name the pattern and link the surprises.}
```

---

### Step 4 — Self-check before closing

Run this checklist against the artifact before outputting it:

- [ ] **No generic labels**: every surprise has a specific named label, not "Finding N" or "Surprise A"
- [ ] **Every source is named**: namespace + skill is visible for each surprise
- [ ] **Every Expected cell is populated**: if you wrote "N/A" or left it blank, the contrast is missing — go back
- [ ] **Every Design impact is explicit**: "This changes..." or "This confirms..." — not implied
- [ ] **At least one cross-signal surprise**: one finding synthesized from two or more sources
- [ ] **Breadth spans 3+ namespaces**: if all surprises come from one namespace, re-read the rest
- [ ] **Standalone readability**: would a newcomer with no project context understand each surprise? If not, add one sentence of context

If any item fails, revise before outputting the artifact.

---

The echo is institutional memory. The next team that investigates this path will read it before they start. They will use it to avoid repeating the same surprises. Every item you leave vague or untraceable is a lesson they will have to relearn the hard way.
