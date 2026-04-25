---
skill: trace-skill
topic: plugin
item: scout-competitors-w2
date: 2026-03-14
skill_version: 0.1.0
input: simulations/draft/specs/signal-scout-2026-03-14.md (post-SF-01/02/03)
wave: 2
prior_trace: plugin-scout-competitors-2026-03-14.md
---

# /trace-skill -- scout-competitors (Wave 2)

**Changes applied since wave 1**:
- SF-01: Artifact naming fixed to `{topic}-competitors-{date}.md`
- SF-02: "None / status quo" added as required competitor row in setup
- SF-03: WebSearch confirmed as tool, explicit note to verify claims not just reason

**Re-trace purpose**: Confirm the fixes hold under the same scenario. Check for new findings.

---

## Setup Phase (re-trace)

**Same invocation**: `/scout-competitors "Signal plugin for Claude Code"`
**Same repo context**: sim

**Setup with SF-02 applied**:

Reading spec (updated): "Always include 'none / status quo' as a competitor row --
the most common competitor is teams doing nothing at all."

The skill now explicitly includes inertia. Setup proceeds identically -- auto-detect
from repo context, no user prompt needed. The "none" row is added before execute starts.

**Setup verdict**: PASS. No change needed from wave 1. SF-02 fix is clean.

---

## Execute Phase (re-trace)

Same 4 roles. Now with "none / status quo" as an explicit row.

### PM lens

Adding "none" row to the matrix changes the scoring context. When "none" scores 0/10
on feature parity but HIGH on threat level (because inertia is the default state),
the PM lens correctly reframes the competitive story: Signal is not competing against
Cursor -- it is competing against "we don't do this."

Matrix (updated with "none" row):

| Competitor | Feature Parity | Positioning Gap | Technical Moat | Distribution | Threat |
|------------|---------------|-----------------|----------------|--------------|--------|
| None (inertia) | 0/10 | Direct | Habit + no switching cost | Everywhere | HIGH |
| Custom ad-hoc scripts | 5/10 | Direct | None | Copy-paste | MEDIUM |
| Cursor AI | 2/10 | Complementary | Editor lock-in | VS Code fork | LOW |
| GitHub Copilot | 2/10 | Complementary | GitHub lock-in | GitHub native | LOW |
| Panel (craftworks) | 6/10 | Complementary (ally) | Same ecosystem | craftworks | NONE |

### Strategy lens

With "none" explicit, the positioning clarity sharpens:
- Signal is a **behavior change** product, not a feature comparison product
- The core message is not "Signal vs. Cursor" -- it is "investigation vs. no investigation"
- This changes the pitch from feature matrix to ROI/risk argument:
  "Teams that skip pre-build investigation spend 3x longer fixing post-ship bugs
  (cite evidence from techniques corpus)"

### Architect lens (unchanged from W1)

Technical moat analysis unchanged. The techniques corpus, topic model, and binding-agnostic
design remain the three moat dimensions.

### GTM lens

With "none" explicit: the GTM challenge is adoption of a new behavior, not displacement
of an existing tool. This means the rollout strategy at the all-hands should NOT be
"try Signal instead of X." It should be "try Signal where you currently have nothing."

---

## Findings Phase (updated)

### Competitive Matrix (wave 2)

"None / inertia" is now row 1 and the highest-threat competitor. The matrix tells a
cleaner story: Signal competes primarily against the absence of process, secondarily
against fragmented ad-hoc approaches, and barely against any named tool.

### Whitespace (unchanged)

No structured pre-build investigation tool exists in the Claude Code ecosystem.
Signal owns this space entirely.

### Table stakes (updated)

T-01 through T-04 unchanged. Adding:
- T-05: The pitch must address inertia directly -- "why bother" before "why Signal"

### Findings delta from W1

**New finding -- NF-01 (MAJOR)**: The "none" row changes the GTM framing fundamentally.
The all-hands pitch should open with "how many of you do structured pre-build
investigation today?" not "have you heard of simulation?" The behavior gap is the
hook, not the tool comparison.

**SF-01 resolved**: Artifact naming now correct. The skill writes to
`simulations/scout/competitors/{topic}-competitors-{date}.md`. CLOSED.

**SF-02 resolved**: "None / status quo" row is explicit in the spec and appears in
the matrix. CLOSED.

**SF-03 resolved**: WebSearch confirmed in tools. The skill spec now explicitly says
"use web search to verify competitor feature claims." CLOSED.

---

## Amend Phase (updated)

Same 3 amend options as W1, with one addition:

4. **Change the framing from competitive analysis to behavior change analysis** --
   if the audience is the all-hands PM persona, the brief should be structured as
   "cost of NOT investigating" rather than "Signal vs. competitors." This reframes
   the artifact from a competitive matrix to a risk quantification brief. Could be
   a flag: `--mode risk` vs `--mode competitive`.

---

## Verdict (wave 2)

**Result**: IMPROVED -- the SF-02 fix (inertia as competitor) is the highest-value
change. It transforms a standard competitive analysis into a behavior change argument.

**Loop pattern assessment**:

The wave 1 → spec fix → wave 2 loop worked exactly as intended:
- Wave 1 found 3 findings (SF-01, SF-02, SF-03)
- Spec was updated in < 5 minutes
- Wave 2 confirmed all 3 closed, found 1 new finding (NF-01)
- NF-01 is additive (a flag suggestion), not a blocking spec problem

**New finding for spec**:
- NF-01 (MINOR): Add `--mode risk` flag option to scout-competitors that reframes
  the output from competitive matrix to "cost of not acting" risk brief. Useful for
  all-hands/exec audience who respond to risk framing over feature comparison.

**Loop readiness**: The trace-skill → find → fix → retrace loop is working. The
pattern is:
  W1 = baseline trace, find structural problems (naming, missing rows, tool gaps)
  W2 = confirm fixes, find framing/UX improvements
  W3+ = only if W2 surfaces blocking findings

W2 has no blocking findings. Scout-competitors spec is READY for the other 7 traces.
