Written to `simulations/quest/variations/topic-echo-variations-R3-2026-03-14.md`.

---

## topic-echo — Variations R3

| # | Axis | Target | Hypothesis |
|---|------|--------|-----------|
| **V-01** | Newcomer-reader orientation throughout | C-08 | R2 showed word limits are necessary but not sufficient for C-08 PASS — the operative mechanism is explicit "write for your successor" framing at every step |
| **V-02** | Pattern-first structure | C-09 | Inverting the structure (patterns before surprises) forces synthesis across the full signal set before any item is written |
| **V-03** | Anti-exemplar culling discipline | C-01 | Concrete "this FAILS" examples train judgment at the hard margin where unexpected-but-discoverable items slip through |
| **V-04** | CF gate + anti-hedging + per-item cap | C-10 + C-11 + C-12 | R2's explicit gap analysis: V-04 reaches 100/100 by adding the 120-word per-item cap as Rule 3 |
| **V-05** | CF gate + anti-hedging + per-item cap + newcomer framing | C-08 + C-10 + C-11 + C-12 | Full convergence — tests whether all four mechanisms coexist without friction |

---

### Design rationale summary

**What R3 is targeting**: R2's top variation (V-04) scored 98/100. No R2 variation cleared all five aspirational criteria. The gaps: C-08 PARTIAL everywhere except V-02, C-10 FAIL in V-02/V-03/V-05, C-11 PARTIAL in V-04, C-11 FAIL in V-01/V-03.

**Three single-axis variations** test untried mechanisms:
- V-01: C-08 as a primary axis (never targeted directly in R1 or R2)
- V-02: C-09 as structural rather than checklist (patterns before surprises)
- V-03: C-01 via anti-exemplars rather than abstract rules

**Two combination variations** test convergence:
- V-04: the R2 gap closed — V-04 (R2) + Rule 3 (120-word per-item cap) = predicted 100/100
- V-05: full convergence — V-04 (R3) + newcomer framing = ceiling test for all five criteria simultaneously

**Key structural bet in V-02**: Pattern identification has always been a Step 5 afterthought. Putting it before Step 1 changes the authorial posture: the author is now reading signals for patterns, not for items. Individual surprises become evidence for a thesis rather than a list.

**Key structural bet in V-03**: The hardest culling error is not "expected finding dressed as surprise" — it's "unexpected but would have been discovered anyway." Abstract rules are insufficient to teach that margin; illustrated failures are not.

**V-04 prediction**: 100/100. The R2 scorecard identified exactly one gap and exactly one fix. V-04 (R3) applies it.

**V-05 risk**: Four enforcement mechanisms may create a complex prompt that degrades C-01 or C-04 performance. If friction appears, it will show as lower essential criteria scores despite higher aspirational coverage.
t do not contribute to a pattern face a higher bar — they must be surprising enough to stand alone. This should also improve C-06 (cross-signal synthesis) because pattern identification requires reading across namespaces before committing to any single source.

**C-01 strategy for R3**: Every prior variation states culling rules abstractly. V-03 (R3) tests whether concrete anti-exemplars — "this item FAILS Filter C, and here is why" — produce stricter discrimination than abstract rules alone. The hypothesis is that the hardest culling errors (unexpected but discoverable items) require illustration to teach, not just naming.

**V-04 (R3) as the gap-closing variation**: The R2 scorecard was explicit — one addition closes V-04's 98/100 gap: the 120-word per-item cap. V-04 (R3) makes that addition as Rule 3, keeping Rules 1 and 2 from R2-V-04 unchanged. Rule 3 does not change the selection or voice standards — it is purely a per-item synthesis check.

**V-05 (R3) as the ceiling test**: If V-04 (R3) achieves 100/100 on C-10, C-11, C-12, the question becomes whether adding C-08 framing is purely additive. V-05 (R3) inserts the newcomer-reader orientation from V-01 (R3) into V-04 (R3)'s structure. The risk is friction: four mechanisms may pull in slightly different directions, producing a more complex prompt that is harder to follow. The gain is all five aspirational criteria in a single variation.

---

## V-01 -- Single axis: Newcomer-reader orientation throughout (C-08)

**Axis**: "Write for your successor" framing embedded at every execution step -- not just the closing statement.

**Hypothesis**: R2's cross-variation analysis showed C-08 requires explicit newcomer-reader language during execution. V-02 (R2) earned the only C-08 PASS by directing the author to write for "someone who was not on the team." Making this orientation the primary axis -- present before reading signals, during culling, during naming, and during writing -- should produce C-08 PASS without relying on word limits or persona framing. If this variation earns C-08 PASS, it confirms that explicit reader orientation is the operative mechanism, not length constraints.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises for a reader who was not on the team.

---

### Who reads this

Before you begin: commit to a specific reader.

Your echo will be read by **someone who was not on this team, cannot access the source signals, and will read this document exactly once -- before they start their own investigation of the same path.**

Every decision you make -- what to include, how to name it, how much to explain -- should serve this reader. They need to know what surprised the team, why it mattered for the design, and what they would have missed without active signal-gathering. They do not need your process. They do not need the raw signal contents. They need the synthesis.

Keep this reader in mind through every step below.

---

### Step 1 -- Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

As you read, note candidate surprises. For each, ask: **Would the stranger understand this without reading the source?** If no -- either because it requires project context, or because the finding has not been synthesized into plain language -- note that it needs work before it belongs in the echo.

---

### Step 2 -- Cull for the stranger

- Drop anything that confirms what was expected. The stranger has read the initial strategy -- confirmed findings are already in it.
- Drop anything you cannot trace to a named source signal.
- Drop anything that cannot stand alone: if understanding it requires reading the source artifact, it has not been synthesized and does not belong in institutional memory.
- Drop anything that could appear unchanged in a standard research summary, retrospective, or findings doc.
- Keep 3-6 surprises. Fewer strong items that the stranger can use beat a longer list only the team can decode.

---

### Step 3 -- Name for the stranger

Assign a **specific named label** to each surviving surprise before writing its body. The name must mean something to the stranger -- content-specific, memorable, and self-explanatory without project context. "The Phantom Dependency" passes. "Finding 2" fails. "The Integration Gap" fails if any project could have had one -- the name must be specific to what this investigation found.

---

### Step 4 -- Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

Each surprise:

```markdown
## {Named Label}
**Source**: {namespace/skill -- cited so the stranger can locate it if they need more}
**Expected**: {what the team assumed before this signal existed -- stated plainly: "We assumed X"}
**Found**: {what the signal revealed -- explained without assuming the stranger ran these signals}
**Design impact**: {how this changes, challenges, or confirms the direction -- explicit, one sentence minimum}
```

**After writing each surprise**: read it as the stranger -- someone who did not run these signals, has no project context, and will read this once. Does it stand alone? Is the finding clear without explanation? Is the design consequence stated, not implied? If not, revise or drop.

---

### Step 5 -- Quality checks

- [ ] A stranger with no project context understands every surprise without reading the source signals
- [ ] Every surprise has a specific named label (content-specific -- not generic, not "Finding N")
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell is populated -- the contrast is visible
- [ ] Every "Design impact" is stated -- not implied
- [ ] Only genuine surprises -- no expected findings dressed as discoveries
- [ ] At least one surprise synthesizes two or more signals -- cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Document is under 800 words (excluding headers)
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

The echo is institutional memory. Its value is measured by what a stranger can take from it -- not by what the team experienced while gathering signals.

---

## V-02 -- Single axis: Pattern-first structure (C-09)

**Axis**: Write the Patterns section first, then derive individual surprises from the patterns. Synthesis happens before items, not after.

**Hypothesis**: In every prior variation, patterns are an afterthought -- the author lists individual surprises, then checks in Step 5 if any two share a root. Pattern-first inverts this: the author must synthesize across the full signal set before committing to any single item. Individual surprises then serve as evidence for patterns rather than patterns being discovered incidentally. This should produce stronger C-09 (pattern ID becomes structural, not checklist), stronger C-06 (cross-signal synthesis is required to identify patterns), and stronger C-01 -- items that do not contribute to a pattern face a higher inclusion bar.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises -- organized by patterns first, then itemized.

---

### The structural inversion

Standard echoes list surprises first, then check if any form patterns. This echo does the opposite: **identify the patterns first, then write the surprises that evidence them.**

Pattern-first forces you to hold the full signal set in mind before committing to any individual item. You cannot write your first surprise until you have decided what the investigation, taken as a whole, actually revealed. An item that does not contribute to a pattern must be surprising enough to stand alone -- the bar for standalone surprises is higher.

This is not a formatting constraint. It is a synthesis discipline.

---

### Step 1 -- Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

Take notes on everything unexpected. Do not write yet. You are looking for patterns, not items.

---

### Step 2 -- Find the patterns

Before writing any individual surprise, ask: **"Across all the signals I just read, what structural truths did this investigation reveal -- not just individual findings, but things that hold across multiple signals?"**

A pattern is not a theme. A pattern connects two or more surprises to a common root cause: "Three separate surprises all trace back to teams underestimating coordination cost" is a pattern. "Several findings relate to onboarding" is a theme.

Identify 1-3 patterns. Name each one. For each, list the surprises that contribute to it.

If you cannot find a pattern connecting two or more surprises, note this explicitly and proceed. A valid echo may have only isolated surprises -- but if you find no patterns, verify you have read signals across at least three namespaces.

---

### Step 3 -- Identify individual surprises

From your pattern map:
1. For each pattern: identify the 1-2 most specific surprises that evidence it. Prefer items derived from multiple signals over single-artifact observations.
2. For any surprise not contributing to a pattern: include only if it is significant enough to stand alone in institutional memory.

For every candidate:
- Drop anything that confirms what was expected.
- Drop anything you cannot trace to a named source signal.
- Drop anything that could appear in a standard research summary.
- Keep 3-6 total.

---

### Step 4 -- Name before you write

Assign a specific named label to each surviving surprise -- content-specific, memorable, not generic.

---

### Step 5 -- Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

```markdown
## Patterns

### {Pattern Name}
{1-2 sentences: what structural truth connects these surprises, and what it means for the design}
**Evidenced by**: {list the Named Labels of surprises below that contribute to this pattern}

---

## Surprises

### {Named Label}
**Source**: {namespace/skill}
**Expected**: {what the team assumed -- "We assumed X"}
**Found**: {what the signal revealed}
**Design impact**: {how this changes, challenges, or confirms the direction -- explicit, one sentence minimum}
**Pattern**: {which named pattern above this contributes to, or "standalone" with one sentence on why it belongs despite no pattern}
```

---

### Step 6 -- Quality checks

- [ ] Patterns section is written before the Surprises section
- [ ] Each pattern named in Patterns connects two or more surprises to a common root (not just a shared theme)
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell is populated
- [ ] Every "Design impact" is stated
- [ ] Every "Pattern" field is populated -- standalone surprises include a one-sentence justification
- [ ] At least one surprise cites two or more sources (cross-signal synthesis)
- [ ] Surprises span at least three distinct namespaces
- [ ] Document under 800 words (excluding headers)

---

The echo is institutional memory. The patterns are its highest-value layer -- they are what the investigation revealed about the problem space, not just about this feature.

---

## V-03 -- Single axis: Anti-exemplar discipline for culling (C-01)

**Axis**: Concrete "this FAILS" examples alongside each culling filter, illustrating the hard margin where interesting but discoverable items slip through.

**Hypothesis**: Prior variations state culling rules abstractly ("drop expected findings", "would a passive team have found this?"). Abstract rules are less discriminating at the hard margin -- items that are unexpected but would have been discoverable through ordinary work. Showing what gets dropped (and why each item fails) trains the author's judgment at exactly the point where errors occur. If this variation produces stricter C-01 compliance than rule-statement-only variations, concrete anti-exemplars outperform abstract criteria for culling discipline.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises that required active investigation to surface.

---

### Step 1 -- Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

List every candidate surprise you notice. Do not filter yet. Apply the four filters in Step 2.

---

### Step 2 -- Cull with the four filters

Apply each filter to every candidate. Cut anything that fails any filter.

---

**Filter A: Not an expected finding**

> Drop anything that confirms what the team planned, assumed, or would have said in the kickoff brief or initial strategy.

| Fails this filter | Why |
|-------------------|-----|
| "Users need onboarding documentation" | Anticipated before any signal was gathered |
| "Large enterprise customers require compliance review" | Part of the initial constraints |
| "The feature performs differently at scale" | Known risk, not a discovery |
| "Teams want simpler setup" | Standard usability concern anticipated before investigation |

Test: "Was this in the initial strategy, requirements, or kickoff materials?" If yes -- cut. An expected finding is not a surprise even if the team observed it with fresh eyes.

---

**Filter B: Traceable to a named source signal**

> Drop anything you cannot trace to a specific namespace/skill artifact.

| Fails this filter | Why |
|-------------------|-----|
| "Teams seemed to struggle with onboarding" | General impression -- no artifact cited |
| "Something in the reviews suggested adoption risk" | Vague -- which namespace, which artifact? |
| "There was a theme of fragility in the feedback" | Not traceable -- cannot be verified |

Test: "Can I name the namespace, skill, and artifact where this came from?" If you cannot name it specifically, the surprise is not verified.

---

**Filter C: Genuinely required active signal-gathering to surface**

> Drop anything a reasonable team would have found through planning, standard development, code review, or normal feedback cycles.

| Fails this filter | Why |
|-------------------|-----|
| "The initial design had an unhandled edge case" | Code review would have caught this |
| "Performance degrades under high load" | Standard load testing would have revealed this |
| "The API has a breaking change in version 3" | Documentation review would have found this |
| "Stakeholders had conflicting requirements" | Routine discovery during requirements gathering |

This is the hardest filter. The test is not "did we expect it?" but "would they have found it anyway -- even without running these signals?" Items that are unexpected but discoverable through ordinary work do not pass.

---

**Filter D: Not a standard research-summary finding**

> Drop anything that could appear unchanged in a research brief, findings doc, project retrospective, or sprint review.

| Fails this filter | Why |
|-------------------|-----|
| "User interviews revealed 3 primary pain points" | Classic research summary entry |
| "Technical feasibility is confirmed with some caveats" | Standard findings doc language |
| "The team identified 5 risks requiring mitigation" | Normal retrospective item |
| "Adoption requires a behavior change from users" | Standard change-management observation |

Test: "Could I find this exact sentence in a document written without any signal-gathering framework?" If yes -- cut.

---

### Step 3 -- Name each surviving surprise

Assign a specific named label -- content-specific, memorable, not generic. The name must crystallize the finding: "The Phantom Dependency" passes. "Finding 1" fails. "The Adoption Barrier" fails if any project could have one -- make it specific to what this investigation found.

---

### Step 4 -- Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

```markdown
## {Named Label}
**Source**: {namespace/skill}
**Expected**: {what the team assumed -- "We assumed X"}
**Found**: {what the signal revealed}
**Design impact**: {how this changes, challenges, or confirms the direction -- explicit, one sentence minimum}
```

---

### Step 5 -- Quality checks

- [ ] Every item passed all four filters -- applied explicitly, not by intuition
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell is populated
- [ ] Every "Design impact" is stated
- [ ] At least one surprise synthesizes two or more signals -- cite both sources
- [ ] Surprises span at least three namespaces
- [ ] Document under 800 words
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

## V-04 -- Combined: Counterfactual gate + Anti-hedging + Per-item cap (C-10 + C-12 + C-11)

**Axes**: R2-V-04's counterfactual gate + anti-hedging + the 120-word per-item cap that closes the R2-V-04 gap.

**Hypothesis**: R2-V-04 scored 98/100 with C-11 PARTIAL -- an 800-word document ceiling but no per-item constraint. The R2 scorecard gap analysis was explicit: "V-04 would reach 100/100 by adding the 120-word per-item cap from V-02/V-05." This variation makes that addition as Rule 3, keeping Rules 1 and 2 from R2-V-04 unchanged. Rule 3 does not change the selection or voice standards -- it is purely a per-item synthesis check. The variation should score 100/100.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises that only active signal-gathering could have surfaced -- stated as claims, within tight bounds.

---

### Three rules that govern this echo

**Rule 1 -- The counterfactual gate**

Every candidate surprise must pass this test before it enters the echo:

> Would a team that skipped all signal-gathering -- relying only on initial strategy, standard planning, and normal development feedback -- have eventually discovered this?

- **No** -- active sensing was required: include it.
- **Yes** -- a passive team would have found it: drop it.

This is stricter than "was it unexpected?" Expected and discoverable-without-effort are different things. The echo is about what the investigation made visible that nothing else would have.

**Rule 2 -- Claim-only voice**

Every surprise is stated as a claim. Prohibited from all surprise entries:

| Banned | Use instead |
|--------|------------|
| "may suggest" | state the claim directly |
| "could potentially" | state the claim directly |
| "seems to indicate" | state the claim directly |
| "it is possible that" | state the claim directly |
| "appears to" | "is" |
| "might be" | "is" |
| "arguably" / "we think" | remove |
| "suggests that" | state the claim directly |

If you cannot state a surprise as a claim, the signal is insufficient -- confirm it more firmly or drop it.

**Rule 3 -- 120 words per surprise body**

Each surprise body (everything from `**Source**` through the end of `**Why passive observation missed this**`) is capped at 120 words. If you exceed 120, you have not finished synthesizing. Find the single thing the surprise claims and write that. Everything else is elaboration you have not yet trimmed.

The full echo (3-6 surprises) should be under 800 words total.

---

### Step 1 -- Read all signals

Glob and read every artifact:
- `simulations/{topic}/`
- `simulations/{topic}/**/{topic}-*-{date}.md`

For each candidate surprise, apply Rule 1 immediately: could a passive team have discovered this? Record the verdict. Do not write yet.

---

### Step 2 -- Cull

1. Fail anything a passive team would have found.
2. Fail anything that confirms what was expected.
3. Fail anything you cannot trace to a named source signal.
4. Keep 3-6 surprises.

---

### Step 3 -- Name each surprise

Assign a specific, content-specific named label before writing. Memorable. Not generic. The name should crystallize the finding into a phrase a future reader recalls without needing to re-read the body.

---

### Step 4 -- Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

Each surprise:

```markdown
## {Named Label}
**Source**: {namespace/skill}
**Expected**: {stated as a claim: "We assumed X"}
**Found**: {stated as a claim: "X is Y / X is false / the constraint is Z"}
**Design impact**: {stated as a claim: "This changes / confirms / invalidates..."}
**Why passive observation missed this**: {what specific signal or method surfaced it, and why planning or normal feedback would not have}
```

**After writing each surprise**: count the words from `**Source**` through the end of `**Why passive observation missed this**`. If the count exceeds 120, cut until you have a claim, not a description.

---

### Step 5 -- Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every surprise fails Rule 1 -- no passive team would have found it
- [ ] Every "Why passive observation missed this" cell is populated -- not "N/A"

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any surprise body
- [ ] Every `**Found**` field reads as a statement of fact, not a possibility

**Length (Rule 3):**
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Structural:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] At least one surprise synthesizes two or more signals -- cite both sources
- [ ] Surprises span at least three distinct namespaces
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

The echo is proof that the investigation was worth running. Every surprise you include is an argument for why passive teams ship the wrong thing.

---

## V-05 -- Full convergence: CF gate + Anti-hedging + Per-item cap + Newcomer framing (all aspirational)

**Axes**: V-04 (R3)'s three rules (counterfactual gate + anti-hedging + 120-word cap) plus V-01 (R3)'s newcomer-reader orientation throughout execution.

**Hypothesis**: V-04 (R3) should achieve C-10 PASS + C-11 PASS + C-12 PASS. Adding V-01 (R3)'s newcomer-reader framing should additionally earn C-08 PASS. The risk: four mechanisms in a single prompt may produce friction between the institutional-memory framing and the three mechanical rules. If V-05 scores higher than V-04 (R3) on C-08 without losing ground on C-10/C-11/C-12, the mechanisms are additive. If friction appears, it will show in C-01 or C-04 degradation.

---

You are running `/topic:echo` for topic `{topic}`.

One question: **"What did we learn that we didn't expect?"**

Not a summary. A synthesis of surprises -- for the next team that walks this path.

---

### Who reads this

Before you begin: commit to your reader.

This echo will be read by **someone who was not on this team, cannot access the source signals, and will read this document exactly once -- before they start their own investigation of the same path.**

They need: what surprised the team, why it mattered for the design, and what they would have missed without active signal-gathering. They do not need raw signal contents. They need the synthesis.

Every rule below serves this reader.

---

### Three rules that govern this echo

**Rule 1 -- The counterfactual gate**

Every candidate surprise must pass this test:

> Would a team that skipped all signal-gathering -- relying only on initial strategy, standard planning, and normal development feedback -- have eventually discovered this?

- **No** -- active sensing was required: include it.
- **Yes** -- a passive team would have found it: drop it.

A surprise that a passive team would find anyway is not institutional memory -- it is planning documentation the stranger will write themselves.

**Rule 2 -- Claim-only voice**

Every surprise is stated as a claim the author stands behind. Prohibited from all entries:

| Banned | Use instead |
|--------|------------|
| "may suggest" | state the claim directly |
| "could potentially" | state the claim directly |
| "seems to indicate" | state the claim directly |
| "it is possible that" | state the claim directly |
| "appears to" | "is" |
| "might be" | "is" |
| "arguably" / "we think" | remove |
| "suggests that" | state the claim directly |

The stranger needs claims. If you cannot assert it, drop it.

**Rule 3 -- 120 words per surprise body**

Each surprise body (from `**Source**` through the end of `**Why passive observation missed this**`) is capped at 120 words. If the stranger who reads this once cannot absorb a surprise in a single reading, it is too long. Under 800 words total.

---

### Step 1 -- Read all signals

Glob and read every artifact: `simulations/{topic}/` and `simulations/{topic}/**/{topic}-*-{date}.md`.

For each candidate surprise, apply Rule 1 immediately: could a passive team have discovered this? Also ask: **Can the stranger understand this without reading the source?** If no -- either because it requires project context, or because the finding has not been synthesized -- note that it needs work before it belongs in the echo.

---

### Step 2 -- Cull

1. Fail anything a passive team would have found.
2. Fail anything that confirms what was expected.
3. Fail anything you cannot trace to a named source signal.
4. Fail anything the stranger cannot understand without reading the source artifact.
5. Keep 3-6 surprises.

---

### Step 3 -- Name for the stranger

Assign a specific named label before writing. The name must mean something to the stranger -- content-specific, memorable, self-explanatory without project context. Not "Finding 3." Not "The Edge Case." Something specific to what this investigation found, that the stranger will remember after reading once.

---

### Step 4 -- Write the artifact

`simulations/{topic}/{topic}-echo-{date}.md`

Each surprise:

```markdown
## {Named Label}
**Source**: {namespace/skill}
**Expected**: {stated as a claim: "We assumed X"}
**Found**: {stated as a claim: "X is Y / X is false / the constraint is Z"}
**Design impact**: {stated as a claim: "This changes / confirms / invalidates..."}
**Why passive observation missed this**: {what specific signal or method surfaced it, and why planning would not have -- explained for the stranger, not the team}
```

**After writing each surprise**: read it as the stranger. Does it stand alone? Is the body at or under 120 words? Are there any hedging constructs? Revise before moving to the next if any check fails.

---

### Step 5 -- Pre-output checks

**Counterfactual (Rule 1):**
- [ ] Every surprise fails Rule 1 -- no passive team would have found it
- [ ] Every "Why passive observation missed this" cell is populated and explains the mechanism to a newcomer

**Voice (Rule 2):**
- [ ] Zero prohibited constructs in any surprise body
- [ ] Every `**Found**` field is a statement of fact

**Length (Rule 3):**
- [ ] Every surprise body is at or under 120 words
- [ ] Total document is at or under 800 words

**Stranger utility:**
- [ ] A stranger with no project context understands every surprise without reading the source signals
- [ ] Every "Why passive observation missed this" is explained in terms accessible to the stranger -- not team-internal shorthand

**Structural:**
- [ ] Every surprise has a specific named label
- [ ] Every source is named (namespace + skill)
- [ ] Every "Expected" cell is populated
- [ ] At least one surprise synthesizes two or more signals
- [ ] Surprises span at least three distinct namespaces
- [ ] Add **Patterns** section if two or more surprises share a root cause

---

The echo is the argument that active signal-gathering was worth the investment. The stranger will use it to decide whether to run the same investigation or trust your findings. Make it worth their trust.
