## Round 1 Scorecard — draft-pitch

**Rankings:**

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-05 Inertia-led + Strategy-first + Formal | **100** | YES |
| 2 | V-02 Role sequence (Strategy-before-PM) | **90** | YES |
| 2 | V-04 Conversational register + compressed | **90** | YES |
| 4 | V-01 Inertia framing (single axis) | **87.5** | YES |
| 5 | V-03 Slot structure (single axis) | **85** | YES |

All five variations are Golden (all essential pass, composite >= 80). The floor is solid. Discrimination lives in recommended and aspirational.

**The discriminators:** C-08 (traceable proof) and C-09 (inertia as primary competitor). Only V-05 clears both. V-02 also clears both aspirational criteria but drops to 90 on partial C-05/C-06 (dev interaction depth and maker jargon prohibition are implied by arc structure but not explicitly required).

**Excellence signals from V-05:**

1. **Embedded self-check at generation time** — S-4 Exec Opening Test forces the model to draft, test, and rewrite the exec opening *before* downstream prose is written. C-03 becomes a pre-flight check, not a post-scoring criterion.

2. **Positioning lockdown before prose** — S-1/S-2/S-3 must be answered in writing before the PM pass begins. Locked answers become citable inputs; baked preamble context (V-01's approach) can be ignored.

3. **Default fallback values for missing signals** — Signal Intake provides explicit defaults ("Primary Competitor = 'teams doing nothing / the review that never happened'"), making C-09 cold-start safe unconditionally.

**Trace artifact validation:** The trace independently produced "The real competition isn't Cursor or Copilot. It's the meeting that never happened" plus proof citations with PM validation notes — exactly V-05's structure. The trace even flagged SF-04 ("Anti-positioning missing — add before delivery"), which is the class of gap V-05's Step 4 structurally eliminates.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Embedded self-check at generation time: placing the pass criterion at the moment the failing content would be generated (not as a post-draft review) reliably eliminates C-03 regression", "Positioning lockdown before prose: forcing strategy questions to be answered in writing before PM drafts prevents ambient context from being ignored -- locked answers become citable inputs not suggestions", "Default fallback values for missing signals: hardcoding the correct answer (inertia as primary competitor) as an explicit default ensures aspirational criteria pass even in cold-start runs with no prior scout artifacts"]}
```
-------|--------|----------|
| C-01 | All three versions present | PASS | PM pass explicitly writes "all three versions in full" |
| C-02 | Each version has all four elements | PASS | PM pass: "Use the four required parts in each version: Hook, What It Does, Why It Matters, Call to Action." |
| C-03 | Exec version is outcome-first | PASS | PM rule: "The exec version's first sentence must name a cost or risk. Read it back after writing it. If it mentions a feature or technology, rewrite it." -- explicit self-check. |
| C-04 | Anti-positioning section present | PASS | "Write the 'What Signal Is NOT' section. Pull the ruling-out statement from Strategy's Pass 1 answer #3, and add one more category." |
| C-05 | Dev version shows the tool | PARTIAL | Strategy arc includes "Interaction" step, but PM pass does not explicitly require a command, file path, or concrete example. Model must infer interaction depth from the arc alone. |
| C-06 | Maker version is jargon-free | PARTIAL | Maker arc: "Question they already have -> Plain description -> Their work benefit -> Their action" -- "plain description" implied but no explicit jargon prohibition. |
| C-07 | Prior signals consulted | PASS | Strategy Pass 1 explicitly loads prior signals: "List what you found (or note 'no prior signals.')." |
| C-08 | Proof points are specific and traceable | PASS | PM rule: "For each proof point you include, identify its source: an artifact path, a data file, or a direct claim from prior signals. If you cannot source it, flag it as UNVERIFIED." |
| C-09 | Inertia named as primary competitor | PASS | Strategy question 2: "Who is the primary competitor -- not a named tool, but what teams do instead today?" Strategy arc explicitly labels "Primary competitor (inertia)" as a required step. PM arc inherits this. |

**Essential**: 4/4 | **Recommended**: 2/3 | **Aspirational**: 2/2

```
composite = (4/4 * 60) + (2/3 * 30) + (2/2 * 10)
          = 60 + 20 + 10
          = 90
```

**Score: 90 / 100 -- GOLDEN**

---

### V-03: Output Format -- Slot Structure (Single Axis)

Axis: Every section is a labeled slot with the pass criterion embedded at the point of writing.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | 12 labeled slots -- EXEC-*, DEV-*, MAKER-* -- all three versions structurally enforced |
| C-02 | Each version has all four elements | PASS | Four dedicated slots per version: HOOK, WHAT, WHY, CTA for exec, dev, and maker |
| C-03 | Exec version is outcome-first | PASS | [SLOT: EXEC-HOOK] embedded criterion: "First sentence names a cost, risk, or productivity consequence. It does not name a feature or describe the tool." Fails at generation time if violated. |
| C-04 | Anti-positioning section present | PASS | [SLOT: ANTI-POSITIONING] required; criterion: "Names at least two specific adjacent categories this tool is NOT. Vague statements do not pass." |
| C-05 | Dev version shows the tool | PASS | [SLOT: DEV-WHAT] criterion: "Shows a command, artifact, or workflow step" + "Include at least one concrete example (command, file path, artifact name)." |
| C-06 | Maker version is jargon-free | PASS | [SLOT: MAKER-WHAT] criterion: "Plain language only. No acronyms, no namespace names, no CLI references." |
| C-07 | Prior signals consulted | PARTIAL | Quick check mentioned at top ("Note: 'Signals found: [list]' or 'No prior signals.'") but no structured loading step; check is cursory, not architectural. |
| C-08 | Proof points are specific and traceable | FAIL | No slot for proof audit. No sourcing requirement in any exec or dev slot. |
| C-09 | Inertia named as primary competitor | FAIL | No slot requires inertia naming. Exec hook only requires cost/risk framing, not competitive framing. |

**Essential**: 4/4 | **Recommended**: 2.5/3 | **Aspirational**: 0/2

```
composite = (4/4 * 60) + (2.5/3 * 30) + (0/2 * 10)
          = 60 + 25 + 0
          = 85
```

**Score: 85 / 100 -- GOLDEN**

---

### V-04: Conversational Register + Compressed Lifecycle

Axes: Second-person address, single pass, no phase structure.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | "Three versions. One pass. All required." -- exec, dev, maker labeled as sections |
| C-02 | Each version has all four elements | PASS | Each version's prose paragraph covers hook, what, why, CTA sequentially ("Open with... Then... Close with...") |
| C-03 | Exec version is outcome-first | PASS | "Open with what it costs teams today when they don't have this. Don't open with what the tool does." + self-check: "read your first sentence back. Does it mention a feature or how the tool works? If yes, rewrite it." |
| C-04 | Anti-positioning section present | PASS | "What Signal Is NOT -- two or three bullets. Be specific. Name actual adjacent categories." "Not just another AI tool" explicitly called out as insufficient. |
| C-05 | Dev version shows the tool | PASS | "Show them what they'd actually run or open. A command. A file name. An artifact that comes back." |
| C-06 | Maker version is jargon-free | PASS | "Write like you're explaining it to someone smart who doesn't know what a namespace is." |
| C-07 | Prior signals consulted | PASS | "Quick check first: is there a positioning or competitor signal in simulations/scout/? If yes, use it." -- minimal but present and unconditional. |
| C-08 | Proof points are specific and traceable | FAIL | No proof audit step. Conversational register trades sourcing discipline for speed. |
| C-09 | Inertia named as primary competitor | FAIL | Exec instruction leads with cost but does not require "doing nothing" or inertia to be named as primary competitor. |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 0/2

```
composite = (4/4 * 60) + (3/3 * 30) + (0/2 * 10)
          = 60 + 30 + 0
          = 90
```

**Score: 90 / 100 -- GOLDEN**

---

### V-05: Inertia-Led + Strategy-First + Formal Register

Axes: Signal intake with defaults + positioning lockdown (S-1 to S-4) + PM full draft + proof audit.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All three versions present | PASS | Step 3 requires all three versions with full sections |
| C-02 | Each version has all four elements | PASS | Step 3 enumerates Hook, What It Does, Why It Matters, Call to Action for each version with explicit requirements |
| C-03 | Exec version is outcome-first | PASS | S-4 Exec Opening Test: draft first sentence, apply cost/risk test, rewrite until it passes -- self-check embedded at generation time before prose lock-in. Step 3 links exec first sentence back to S-4 output. |
| C-04 | Anti-positioning section present | PASS | Step 4 dedicated anti-positioning with minimum 3 bullets; each bullet format enforced: "[Category]. Signal [specific thing it does not do]." |
| C-05 | Dev version shows the tool | PASS | Step 3: "at least one concrete interaction -- command, artifact name, or workflow step; reader can answer 'what would I actually type?'" |
| C-06 | Maker version is jargon-free | PASS | Step 3: "plain-language description only; no namespace references, no CLI terminology" |
| C-07 | Prior signals consulted | PASS | Step 1 Signal Intake loads from three signal paths; extracts primary competitor, whitespace claim, outcome statement from each found artifact |
| C-08 | Proof points are specific and traceable | PASS | Step 5 Proof Point Audit: annotate each factual claim with [source: artifact-path], [source: prior signal], or [UNVERIFIED]; unverified claims replaced with hedged language before save |
| C-09 | Inertia named as primary competitor | PASS | S-1 forces completion of "The real competition is not [named tool]. It is ___." Step 1 provides explicit default if no signals: "Primary Competitor = 'teams doing nothing / the review that never happened'". Step 3 requires exec Why It Matters to "name the primary competitor from S-1 explicitly." Cold-start safe. |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 2/2

```
composite = (4/4 * 60) + (3/3 * 30) + (2/2 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 -- GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? | C-08 | C-09 |
|------|-----------|-----------|-------------|--------------|-----------|---------|------|------|
| 1 | V-05 Inertia-led + Strategy-first | 4/4 | 3/3 | 2/2 | **100** | YES | PASS | PASS |
| 2 | V-02 Role sequence | 4/4 | 2/3 | 2/2 | **90** | YES | PASS | PASS |
| 2 | V-04 Conversational register | 4/4 | 3/3 | 0/2 | **90** | YES | FAIL | FAIL |
| 4 | V-01 Inertia framing | 4/4 | 2.5/3 | 0.5/2 | **87.5** | YES | FAIL | PARTIAL |
| 5 | V-03 Slot structure | 4/4 | 2.5/3 | 0/2 | **85** | YES | FAIL | FAIL |

**The discriminator between 100 and the field: C-08 and C-09 together.** Only V-05 satisfies both aspirational criteria. V-02 also achieves both aspirational but loses ground on recommended (C-05/C-06 PARTIAL), making V-05 the sole 100 scorer.

---

## Criterion Coverage Heatmap

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 (3 versions) | PASS | PASS | PASS | PASS | PASS |
| C-02 (4 elements) | PASS | PASS | PASS | PASS | PASS |
| C-03 (outcome-first exec) | PASS | PASS | PASS | PASS | PASS |
| C-04 (anti-positioning) | PASS | PASS | PASS | PASS | PASS |
| C-05 (dev shows tool) | PASS | PARTIAL | PASS | PASS | PASS |
| C-06 (maker jargon-free) | PASS | PARTIAL | PASS | PASS | PASS |
| C-07 (prior signals) | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-08 (traceable proof) | FAIL | PASS | FAIL | FAIL | PASS |
| C-09 (inertia as competitor) | PARTIAL | PASS | FAIL | FAIL | PASS |

C-01 through C-04 pass universally -- the prompt design floor is structurally sound. Variation begins at recommended and aspirational.

---

## Excellence Signals -- Round 1

### E-1: Embedded self-check at generation time eliminates C-03 regression

V-05's S-4 Exec Opening Test requires the model to draft, test, and rewrite the exec opening before committing to prose. This is qualitatively different from an instruction that says "make sure you open with a cost" -- it forces the check inside the generation loop, before downstream content is written. V-02 achieves the same effect via "read it back after writing." Both are stronger than V-04's post-draft rewrite instruction, which operates after the version is already written. **Pattern: embed the pass criterion at the moment the failing content would be generated, not as a review step afterward.**

### E-2: Positioning lockdown before prose prevents narrative drift on C-09

V-05 requires S-1/S-2/S-3 answers before any pitch content is written. These answers become constraints the PM pass cannot override. V-02 achieves this via Strategy/PM role separation with explicit "Follow the arc. Do not reframe the strategy decisions." V-01 bakes inertia into context but does not lock it as a required output. The difference: baked context can be ignored; a locked answer written in a prior step becomes a source the model cites. **Pattern: forcing a decision before prose locks it as input rather than suggestion.**

### E-3: Default fallback values for missing signals make C-09 cold-start safe

V-05's Signal Intake specifies exact fallback values if no prior signals are found: "Primary Competitor = 'teams doing nothing / the review that never happened'". C-09 passes unconditionally -- whether or not scout-positioning artifacts exist. V-01 bakes inertia into prompt context, which achieves a similar effect but relies on model inference from preamble rather than a supplied default. **Pattern: hardcoding the correct answer as a fallback is more reliable than relying on model inference from ambient context.**

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate:
- Sole variation achieving 100/100
- All 9 criteria pass: 4 essential + 3 recommended + 2 aspirational
- S-4 self-check is the strongest C-03 mechanism in this round
- Default fallback values ensure C-09 cold-start safety
- Proof audit (Step 5) produces traceable claims with UNVERIFIED flagging before artifact save
- Anti-positioning minimum raised to 3 bullets -- strongest C-04 floor in the round

**V-02** is the closest structural competitor: achieves both aspirational criteria but gives up ground on C-05/C-06 (PARTIAL). The PM pass does not explicitly require a command or file path in the dev section, leaving concrete interaction depth to model inference.

**V-04** is the baseline: achieves full recommended coverage (3/3) but sacrifices both aspirational criteria by design. Rational for first-draft use cases where proof rigor is not yet required.

---

## Round 1 Findings

### F-01: All five variations achieve Golden -- essential criteria are well-specified

Every variation passes all 4 essential criteria. The 60-point essential floor is not discriminating here. Discrimination lives entirely in recommended and aspirational.

### F-02: C-08 (traceable proof) requires a dedicated audit step

C-08 is satisfied only by V-02 and V-05, both of which include an explicit proof-sourcing pass. Embedding sourcing expectations in section instructions (as V-03 implicitly does) is insufficient. The pattern from V-02/V-05: proof sourcing must be a named step, not an inferred expectation.

### F-03: C-09 (inertia as primary competitor) requires an explicit written answer, not ambient context

V-01 bakes inertia into preamble -- produces PARTIAL, not PASS, because preamble context can be ignored. V-02 and V-05 both require an explicit written answer before pitch prose begins. That answer then becomes a citable input, not background noise.

### F-04: The trace artifact confirms V-05 framing as the right golden target

The trace (plugin-draft-pitch-2026-03-14.md) independently produced:
- "The real competition isn't Cursor or Copilot. It's the meeting that never happened." -- matches V-05's S-1 requirement
- "730+ scenarios" and "40% of design bugs" with PM validation notes -- matches V-05's Step 5 proof audit
- SF-04 finding: "Anti-positioning statement missing -- add before delivery" -- flags the structural gap that V-01/V-04 leave open. V-05 eliminates this class of gap via Step 4.

The trace run confirms V-05's structure reflects what a high-quality human-guided run produces naturally.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Embedded self-check at generation time: placing the pass criterion at the moment the failing content would be generated (not as a post-draft review) reliably eliminates C-03 regression", "Positioning lockdown before prose: forcing strategy questions to be answered in writing before PM drafts prevents ambient context from being ignored -- locked answers become citable inputs not suggestions", "Default fallback values for missing signals: hardcoding the correct answer (inertia as primary competitor) as an explicit default ensures aspirational criteria pass even in cold-start runs with no prior scout artifacts"]}
```
