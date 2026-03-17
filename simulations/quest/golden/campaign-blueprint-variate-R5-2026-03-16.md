---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-16
round: 5
rubric: campaign-blueprint-rubric-v5-2026-03-16.md
---

# campaign-blueprint — Prompt Variations R5

Five complete, runnable skill body variations. Single-axis first (V-01 through V-02),
then three combinations (V-03 through V-05).

## R5 Context

R4 closed all v4 criteria simultaneously — all three submitted variants reached the 128
v4-ceiling. Retroactive v5 scoring revealed three distinct bands:

| Variant | v5 Score | C-19 | C-20 | C-21 |
|---------|----------|------|------|------|
| V-01 (R4) — FINDINGS Gate Separation | 133 | +5 | 0 | 0 |
| V-02 (R4) — Contract Anchor Reminders | 133 | 0 | +5 | 0 |
| V-03 (R4) — Conviction Staging | 135.5 | 0 | +2.5* | +5 |

*V-03 C-20 PARTIAL: CONVICTION TYPE entry provides per-site reminder, but READ and
PRESERVE are not restated per-site. Commissioner resolution pending.

The v5 ceiling is **143** (135 base + 8 excellence). Reaching it requires all three new
criteria in full. R5 explores whether they can be combined without interference and whether
the combination can be expressed at different density levels.

**R5 variation axes:**

- V-01: C-20 proximity resolution — resolve V-03 (R4)'s C-20 PARTIAL by restating
  READ and PRESERVE per-site alongside CONVICTION TYPE. Minimal change from R4 V-03.
  Single-axis.
- V-02: C-19 + C-21 — R4 V-01 phase gate combined with R4 V-03 conviction typing.
  Typed CONVICTION DELTA audit inside a named phase gate. No per-site reminders.
  Two-axis.
- V-03: Full triple (C-19 + C-20 + C-21) — first attempt at the 143 ceiling. All three
  new criteria combined with the R4 base structure.
- V-04: Full triple + minimal density — same triple combination compressed to skeleton.
  Tests whether 143 is achievable at minimum word count.
- V-05: Full triple + inertia-forward register — same triple combination with phrasing
  that foregrounds the inertia baseline at every phase. Tests whether framing emphasis
  changes narrative quality (C-09) while maintaining structural completeness.

**R5 diagnostic questions:**

1. Does adding READ + PRESERVE alongside CONVICTION TYPE in per-site reminders (V-01)
   earn C-20 FULL — and if so, does V-03 (R4)'s CONVICTION TYPE-only entry still earn
   PARTIAL or is it now clearly insufficient?
2. Do C-19 and C-21 reinforce each other (V-02)? Does the named CAMPAIGN REFLECTION
   phase make the typed CONVICTION DELTA audit more reliable than when FINDINGS is inline?
3. Does the full triple (V-03) reach 143 — or does combining all three criteria introduce
   any structural interference that costs a criterion?
4. Does minimal density (V-04) preserve all three new criteria at minimum word count —
   or does compacting the per-site reminders or the phase header cause any PARTIAL?
5. Does inertia-forward framing (V-05) improve C-09 scoring by making the narrative
   enemy explicit at every decision point — or is framing orthogonal to structural scoring?

---

## V-01 — C-20 Proximity Resolution

**Axis:** Contract proximity anchoring completion

**Hypothesis:** R4 V-03 earned C-20 PARTIAL because the per-site CONVICTION TYPE entry
in the contract matrix provided a conviction-obligation reminder at each artifact site,
but READ and PRESERVE were not restated per-site. The C-20 criterion requires all three
of READ, PRESERVE, and an execution reminder at each site. The minimal fix is to add
explicit `Contract reminder — READ: … PRESERVE: …` lines at each artifact header
identical to R4 V-02, augmented with CONVICTION TYPE. This combination should earn C-20
FULL and retain C-21 FULL. The inline "not before, not during" (C-18 FULL) is preserved
from R4 V-03, keeping C-19 at PARTIAL (no phase-gate structure). Predicted score: ~138.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before writing anything, establish:

1. Topic identity — one sentence: feature name, audience, problem solved.
2. Inertia baseline — one sentence: what users do today without this feature.
   This is the primary competitor for all three artifacts.
3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Not conditional. Run regardless of whether signals are found.

4. Artifact contract matrix — declare all obligations before execution begins:

| Field           | Spec                                                    | Proposal                                                          | Pitch                                                              |
|-----------------|---------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                       | Proposal file; scout-positioning if found                          |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md            | simulations/draft/pitches/{topic}-pitch-{date}.md                  |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening, no new design work     | Recommended option from proposal — crystallize, do not reconsider  |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost            | (final artifact)                                                   |
| CONVICTION TYPE | Factual — asserts what is true; does not argue          | Optionality — evaluates trade-offs against spec facts             | Emotional — converts factual + optionality into per-audience urgency |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; inertia baseline; scout-requirements if found.
                    PRESERVE: (first artifact — no prior decisions to protect).
                    CONVICTION TYPE: Factual — assert what is true; do not argue or persuade.

Sections (all required):

  PURPOSE        — Problem and why it exists. Anchor to the inertia baseline.
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to the inertia baseline.
  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; scout-feasibility if found.
                    PRESERVE: all spec design decisions — do not re-open anything the spec resolved.
                    CONVICTION TYPE: Optionality — evaluate trade-offs against spec facts; do not re-assert facts.

Three options minimum. Option A: do-nothing — state the inertia cost honestly.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; scout-positioning if found.
                    PRESERVE: recommended option from proposal — crystallize it, do not reconsider.
                    CONVICTION TYPE: Emotional — convert factual and optionality conviction into per-audience urgency.

Three versions in full:

EXEC (decision-makers):
  Hook: inertia cost — what keeps happening without this?
  What it does: business outcome from the recommended option.
  Why it matters: risk of continued inertia.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads):
  Hook: capability unlocked.
  What it does: references the technical design from the spec explicitly.
  Why it matters: technical debt or opportunity cost.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only):
  Hook: friction from the inertia baseline.
  What it does: no spec terminology, no proposal jargon.
  Why it matters: time saved, steps removed.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

Write simulations/draft/pitches/{topic}-pitch-{date}.md

FINDINGS (write this block after the pitch file is complete — not before, not during):

  CONVICTION DELTA
    Exec version: what emotional conviction does this establish that the factual and
                  optionality artifacts could not? What urgency is new here?
    Dev version: what emotional conviction does this establish that the factual and
                 optionality artifacts could not? What urgency is new here?
    Maker version: what emotional conviction does this establish that the factual and
                   optionality artifacts could not? What urgency is new here?

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-02 — Phase Gate + Conviction Typing

**Axis:** Structural double-prohibition + conviction typing (C-19 + C-21)

**Hypothesis:** R4 tested phase-gate (V-01, earning C-19) and conviction typing (V-03,
earning C-21) on separate axes. Combined, they should reinforce each other: the named
CAMPAIGN REFLECTION phase makes the double-prohibition structural while conviction typing
makes the audit typed and precise. A typed CONVICTION DELTA audit inside a named phase
gate benefits from both mechanisms simultaneously — the phase gate enforces "when"
(C-19), while conviction typing enforces "what kind of question" (C-21). Per-site
READ/PRESERVE reminders are deliberately omitted to isolate whether C-19 + C-21 together
outperform either alone, without introducing C-20 as a third variable. Predicted score: ~138.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before writing anything, establish:

1. Topic identity — one sentence: feature name, audience, problem solved.
2. Inertia baseline — one sentence: what users do today without this feature.
   This is the primary competitor for all three artifacts.
3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Not conditional. Run regardless of whether signals are found.

4. Artifact contract matrix — declare all obligations before execution begins:

| Field           | Spec                                                    | Proposal                                                          | Pitch                                                              |
|-----------------|---------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                       | Proposal file; scout-positioning if found                          |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md            | simulations/draft/pitches/{topic}-pitch-{date}.md                  |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening, no new design work     | Recommended option from proposal — crystallize, do not reconsider  |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost            | (final artifact)                                                   |
| CONVICTION TYPE | Factual — asserts what is true; does not argue          | Optionality — evaluates trade-offs against spec facts             | Emotional — converts factual + optionality into per-audience urgency |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This artifact asserts what is true about the problem and solution. It does not argue or
persuade — it establishes the factual record that the proposal and pitch draw from.

Sections (all required):

  PURPOSE        — Problem and why it exists. Anchor to the inertia baseline.
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to the inertia baseline.
  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This artifact evaluates options against spec facts; it does not re-assert facts the spec
established. The reader finishes knowing which trade-off is worth taking and why.

Read the spec. PRESERVES: do not re-open any design question the spec resolved.
Pull scout-feasibility if available.

Three options minimum. Option A: do-nothing — state the inertia cost honestly.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This artifact converts factual and optionality conviction into per-audience urgency. It
does not re-argue facts or re-litigate options — both are assumed. Each version amplifies
a different urgency dimension unavailable to the earlier artifacts.

Read the proposal. CARRIES FORWARD: the recommended option is the subject of all three versions.
Pull scout-positioning if available.

Three versions in full:

EXEC (decision-makers) — urgency through cost and risk:
  Hook: inertia cost — what keeps happening without this?
  What it does: business outcome from the recommended option.
  Why it matters: risk of continued inertia.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through capability and craft:
  Hook: capability unlocked.
  What it does: references the technical design from the spec explicitly.
  Why it matters: technical debt or opportunity cost.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through friction relief:
  Hook: friction from the inertia baseline.
  What it does: no spec terminology, no proposal jargon.
  Why it matters: time saved, steps removed.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production
begins, not during pitch production. What follows is reflection on completed artifacts,
not intent declaration or progress annotation.

FINDINGS:

  CONVICTION DELTA
    Exec version: what emotional conviction does this establish that the factual and
                  optionality artifacts could not? What urgency is new here?
    Dev version: what emotional conviction does this establish that the factual and
                 optionality artifacts could not? What urgency is new here?
    Maker version: what emotional conviction does this establish that the factual and
                   optionality artifacts could not? What urgency is new here?

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-03 — Full Triple Combination (C-19 + C-20 + C-21)

**Axis:** All three v5 aspirational criteria simultaneously

**Hypothesis:** The 143 ceiling requires full credit on C-19, C-20, and C-21. No known
structural interference prevents holding all three: the CAMPAIGN REFLECTION phase gate
(C-19) is orthogonal to per-site reminders (C-20) and conviction type labels (C-21). V-03
is the first attempt at the ceiling. Structure: 5-field contract matrix with CONVICTION
TYPE row (C-15 superset, D4 confirmed); per-site contract reminder at each artifact
header restating READ, PRESERVE, and CONVICTION TYPE (C-20 FULL — resolves the R4 V-03
PARTIAL); conviction-typed section headers (C-21 FULL); CAMPAIGN REFLECTION phase gated
after pitch completion (C-19 FULL); typed CONVICTION DELTA audit inside the phase (C-21
strengthens C-13). Predicted score: 143.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before writing anything, establish:

1. Topic identity — one sentence: feature name, audience, problem solved.
2. Inertia baseline — one sentence: what users do today without this feature.
   This is the primary competitor for all three artifacts.
3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Not conditional. Run regardless of whether signals are found.

4. Artifact contract matrix — declare all obligations before execution begins:

| Field           | Spec                                                    | Proposal                                                          | Pitch                                                              |
|-----------------|---------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                       | Proposal file; scout-positioning if found                          |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md            | simulations/draft/pitches/{topic}-pitch-{date}.md                  |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening, no new design work     | Recommended option from proposal — crystallize, do not reconsider  |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost            | (final artifact)                                                   |
| CONVICTION TYPE | Factual — asserts what is true; does not argue          | Optionality — evaluates trade-offs against spec facts             | Emotional — converts factual + optionality into per-audience urgency |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; inertia baseline; scout-requirements if found.
                    PRESERVE: (first artifact — no prior decisions to protect).
                    CONVICTION TYPE: Factual — assert what is true; do not argue or persuade.

Sections (all required):

  PURPOSE        — Problem and why it exists. Anchor to the inertia baseline.
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to the inertia baseline.
  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; scout-feasibility if found.
                    PRESERVE: all spec design decisions — do not re-open anything the spec resolved.
                    CONVICTION TYPE: Optionality — evaluate trade-offs against spec facts; do not re-assert facts.

Three options minimum. Option A: do-nothing — state the inertia cost honestly.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; scout-positioning if found.
                    PRESERVE: recommended option from proposal — crystallize it, do not reconsider.
                    CONVICTION TYPE: Emotional — convert factual and optionality conviction into per-audience urgency.

Three versions in full:

EXEC (decision-makers) — urgency through cost and risk:
  Hook: inertia cost — what keeps happening without this?
  What it does: business outcome from the recommended option.
  Why it matters: risk of continued inertia.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through capability and craft:
  Hook: capability unlocked.
  What it does: references the technical design from the spec explicitly.
  Why it matters: technical debt or opportunity cost.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through friction relief:
  Hook: friction from the inertia baseline.
  What it does: no spec terminology, no proposal jargon.
  Why it matters: time saved, steps removed.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production
begins, not during pitch production. What follows is reflection on completed artifacts,
not intent declaration or progress annotation.

FINDINGS:

  CONVICTION DELTA
    Exec version: what emotional conviction does this establish that the factual and
                  optionality artifacts could not? What urgency is new here?
    Dev version: what emotional conviction does this establish that the factual and
                 optionality artifacts could not? What urgency is new here?
    Maker version: what emotional conviction does this establish that the factual and
                   optionality artifacts could not? What urgency is new here?

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-04 — Full Triple + Minimal Density

**Axis:** All three v5 criteria at minimum word count

**Hypothesis:** R4 V-05 (minimal density) reached 128 at minimum word count — confirming
that structural elements carry the ceiling regardless of ceremony. V-04 extends this: if
the three new structural elements (CONVICTION TYPE row, per-site reminder lines with READ
+ PRESERVE + CONVICTION TYPE, CAMPAIGN REFLECTION phase gate) can each be expressed at
minimum word count without losing their structural character, then 143 is achievable at
any density. The per-site reminder condenses to three labeled lines. The CAMPAIGN
REFLECTION phase header carries the gate and the double-prohibition in one sentence. The
CONVICTION DELTA audit questions are shortened to their essential diagnostic form. If V-04
scores 143, density is not a ceiling constraint. If it falls short, the gap identifies
which compact element failed to signal its structural role. Predicted score: 143.

```
You are running /campaign-blueprint for: {topic}

SETUP — run before Artifact 1:
  Topic identity: one sentence — feature name, audience, problem solved.
  Inertia baseline: one sentence — what users do today without this feature.
  Glob simulations/scout/ for this topic now. List all files by namespace. Unconditional.

  Artifact contract matrix:

| Field           | Spec                                                  | Proposal                                                   | Pitch                                                    |
|-----------------|-------------------------------------------------------|------------------------------------------------------------|----------------------------------------------------------|
| READ            | Topic identity; inertia; scout-requirements if found  | Spec file; scout-feasibility if found                      | Proposal file; scout-positioning if found                |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md        | simulations/draft/proposals/{topic}-proposal-{date}.md     | simulations/draft/pitches/{topic}-pitch-{date}.md        |
| PRESERVE        | (first artifact)                                      | All spec design decisions — no re-opening                  | Recommended option — crystallize only                    |
| CARRIES FORWARD | Feature identity; inertia; design decisions           | Recommended option; do-nothing cost                        | (final)                                                  |
| CONVICTION TYPE | Factual                                               | Optionality                                                | Emotional                                                |

Print the matrix. Do not begin Artifact 1 until it is printed.

---

ARTIFACT 1: SPEC — Factual conviction. Asserts what is true; does not argue.
READ: topic identity; inertia baseline; scout-requirements if found.
PRESERVE: (first artifact — no prior decisions)
CONVICTION TYPE: Factual

Sections: PURPOSE / REQUIREMENTS (MoSCoW) / DESIGN / CONSTRAINTS / OPEN QUESTIONS
Each Must-have anchored to the inertia baseline.

Write simulations/draft/specs/{topic}-spec-{date}.md
GATE: Do not begin Artifact 2 until this file is written to disk.

---

ARTIFACT 2: PROPOSAL — Optionality conviction. Evaluates trade-offs; does not repeat spec facts.
READ: spec file; scout-feasibility if found.
PRESERVE: all spec design decisions — do not re-open anything the spec resolved.
CONVICTION TYPE: Optionality

Three options min including do-nothing (honest inertia cost).
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons citing spec decisions or constraints.

Write simulations/draft/proposals/{topic}-proposal-{date}.md
GATE: Do not begin Artifact 3 until this file is written to disk.

---

ARTIFACT 3: PITCH — Emotional conviction. Converts factual + optionality into per-audience urgency.
READ: proposal file; scout-positioning if found.
PRESERVE: recommended option — crystallize it, do not reopen the choice.
CONVICTION TYPE: Emotional

EXEC: inertia-cost hook / recommended option outcome / risk of inertia / CTA: approve or fund.
DEV: capability hook / references technical design from spec explicitly / opportunity cost / CTA: join beta.
MAKER: friction hook / plain language only, no spec or proposal terminology / time saved / CTA: try it.
Shared: ANTI-POSITIONING — what this is NOT, two sentences.

Write simulations/draft/pitches/{topic}-pitch-{date}.md
GATE: Do not begin Campaign Reflection until this file is written to disk.

---

CAMPAIGN REFLECTION — begins only after the pitch file is on disk. Not before pitch production
starts. Not during pitch production. Reflection on a completed artifact only.

FINDINGS:

  CONVICTION DELTA
    Exec: what emotional conviction does this establish that the factual and optionality artifacts could not?
    Dev: what emotional conviction does this establish that the factual and optionality artifacts could not?
    Maker: what emotional conviction does this establish that the factual and optionality artifacts could not?

  NEAR-DUPLICATE CONTENT
    Name any passage nearly copied from spec or proposal.
    State what changed to make it conviction-bearing.

  RESIDUAL QUESTIONS
    What scout signal would resolve what no artifact answered?
    Recommend a namespace for each.

---

CAMPAIGN CLOSE

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-05 — Full Triple + Inertia-Forward Register

**Axis:** All three v5 criteria with inertia-forward phrasing throughout

**Hypothesis:** V-03 earns structural completeness with neutral phrasing. V-05 tests
whether foregrounding the inertia baseline at every decision point — naming it in the
CAMPAIGN SETUP opening sentence, repeating it in each section's driving question, making
it the explicit "enemy" each conviction type must displace — improves C-09 (narrative
arc) and C-10 (scout signal pull visibility) quality without touching structure. The
structural elements are identical to V-03 (C-19 + C-20 + C-21 all present). The
inertia-forward framing also sharpens the CONVICTION DELTA questions: instead of asking
"what urgency is new here?" it asks "what urgency does the inertia cost create that only
this version can make visceral?" This tests whether framing emphasis shifts quality
scoring while holding the structural ceiling. Predicted score: 143 (or reveals C-09
scoring delta relative to V-03). Predicted score: 143.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The inertia baseline is the campaign's primary subject — not as background, but as the
active competitor every artifact must displace. Establish it before writing anything.

1. Topic identity — one sentence: feature name, audience, problem solved.
2. Inertia baseline — one sentence: what users do today without this feature.
   Every Must-have requirement, every option cost, every pitch hook traces here.
3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Unconditional. Do not gate on signal presence.

4. Artifact contract matrix — declares what each artifact inherits, produces, protects, and carries:

| Field           | Spec                                                    | Proposal                                                          | Pitch                                                                  |
|-----------------|---------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                       | Proposal file; scout-positioning if found                              |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md            | simulations/draft/pitches/{topic}-pitch-{date}.md                      |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening, no new design work     | Recommended option from proposal — crystallize, do not reconsider      |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost            | (final artifact)                                                       |
| CONVICTION TYPE | Factual — names the problem the inertia baseline creates | Optionality — prices the cost of inertia against each alternative | Emotional — makes the inertia cost visceral and per-audience-specific  |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; inertia baseline; scout-requirements if found.
                    PRESERVE: (first artifact — no prior decisions to protect).
                    CONVICTION TYPE: Factual — name the problem the inertia baseline creates; do not argue.

The inertia baseline drives every Must-have requirement. Document the problem it creates
before prescribing what replaces it.

Sections (all required):

  PURPOSE        — What problem the inertia baseline creates and why it persists.
                   State it factually: not "users want X" but "without this, users do Y,
                   which costs them Z."
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have must trace to a specific friction the inertia baseline creates.
  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; scout-feasibility if found.
                    PRESERVE: all spec design decisions — do not re-open anything the spec resolved.
                    CONVICTION TYPE: Optionality — price the cost of inertia against each alternative; do not re-assert spec facts.

Option A is do-nothing — the inertia option. Its cost is not zero. State it honestly
before presenting alternatives so the cost of inertia is the baseline every other option
is measured against.

Three options minimum. Option A: do-nothing — state the inertia cost explicitly and concretely.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; scout-positioning if found.
                    PRESERVE: recommended option from proposal — crystallize it, do not reconsider.
                    CONVICTION TYPE: Emotional — make the inertia cost visceral and per-audience-specific.

Each version opens with the inertia cost as its hook. The audience does not need to be
sold on features — they need to feel why continued inertia is more costly than acting now.
Facts came from the spec. Options came from the proposal. This artifact delivers urgency.

Three versions in full:

EXEC (decision-makers) — urgency through cost and compounding risk:
  Hook: what keeps happening without this — the inertia cost in business terms.
  What it does: the outcome the recommended option delivers, stated as inertia reversal.
  Why it matters: the compounding risk of continued inertia.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through blocked capability:
  Hook: what the inertia baseline prevents engineers from doing or building.
  What it does: references the technical design from the spec explicitly.
  Why it matters: the technical debt or opportunity cost of continued inertia.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through daily friction:
  Hook: the specific daily friction the inertia baseline creates for this audience.
  What it does: no spec terminology, no proposal jargon — only what changes for the maker.
  Why it matters: time saved and steps removed.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production
begins, not during pitch production. What follows is retrospective assessment of completed
artifacts. The question in each sub-field is whether the artifact delivered its declared
conviction type against the inertia baseline.

FINDINGS:

  CONVICTION DELTA
    Exec version: what emotional conviction about the inertia cost does this establish
                  that the factual and optionality artifacts could not make visceral?
    Dev version: what emotional conviction about the inertia cost does this establish
                 that the factual and optionality artifacts could not make visceral?
    Maker version: what emotional conviction about the inertia cost does this establish
                   that the factual and optionality artifacts could not make visceral?

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## Variation Summary

| ID   | Axis                                          | New criteria targeted    | Predicted v5 score |
|------|-----------------------------------------------|--------------------------|--------------------|
| V-01 | C-20 proximity resolution (single-axis)       | C-20 FULL + C-21         | ~138               |
| V-02 | Phase gate + conviction typing (two-axis)     | C-19 + C-21              | ~138               |
| V-03 | Full triple combination                       | C-19 + C-20 + C-21       | 143                |
| V-04 | Full triple + minimal density                 | C-19 + C-20 + C-21       | 143                |
| V-05 | Full triple + inertia-forward register        | C-19 + C-20 + C-21       | 143                |

## C-19 / C-20 / C-21 Coverage by Variation

| ID   | C-19 mechanism                                     | C-20 mechanism                                         | C-21 mechanism                                    |
|------|----------------------------------------------------|--------------------------------------------------------|---------------------------------------------------|
| V-01 | Inline "not before, not during" → PARTIAL          | READ + PRESERVE + CONVICTION TYPE per-site → FULL      | CONVICTION TYPE labels + typed audit → FULL       |
| V-02 | CAMPAIGN REFLECTION phase gate → FULL              | None → NO CREDIT                                       | CONVICTION TYPE labels + typed audit → FULL       |
| V-03 | CAMPAIGN REFLECTION phase gate → FULL              | READ + PRESERVE + CONVICTION TYPE per-site → FULL      | CONVICTION TYPE labels + typed audit → FULL       |
| V-04 | CAMPAIGN REFLECTION phase gate (compact) → FULL    | READ + PRESERVE + CONVICTION TYPE per-site → FULL      | CONVICTION TYPE in section header + typed audit   |
| V-05 | CAMPAIGN REFLECTION phase gate → FULL              | READ + PRESERVE + CONVICTION TYPE per-site → FULL      | CONVICTION TYPE labels (inertia-typed) + typed audit |

## R5 Diagnostic Questions

1. Does restating READ + PRESERVE + CONVICTION TYPE per-site (V-01) earn C-20 FULL —
   confirming that R4 V-03's CONVICTION TYPE-only entry was the cause of the PARTIAL?
2. Do C-19 and C-21 reinforce each other (V-02) such that the typed CONVICTION DELTA
   audit inside a named phase is more reliable than either mechanism alone?
3. Does the full triple (V-03) reach 143 — or does any criterion slip under the combined
   structure (e.g., does the per-site CONVICTION TYPE reminder in V-03 satisfy C-20 FULL
   the same way the READ + PRESERVE framing does)?
4. Does minimal density (V-04) preserve all three new criteria — specifically, do the
   compact per-site reminder lines (`READ: … PRESERVE: … CONVICTION TYPE: …`) signal
   C-20 FULL, or does terseness lower them to PARTIAL?
5. Does inertia-forward framing (V-05) produce measurably different C-09 scoring
   relative to V-03 — or does the conviction typing already constrain the narrative arc
   strongly enough that framing emphasis is orthogonal to the score?
