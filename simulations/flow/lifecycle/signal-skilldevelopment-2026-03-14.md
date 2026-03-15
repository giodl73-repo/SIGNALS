---
skill: flow-lifecycle
topic: signal
item: skilldevelopment
date: 2026-03-14
skill_version: 0.1.0
input: SHIPPING.md + signal.skills.yaml + tools/quest-run-one.sh
---

# /flow:lifecycle -- Signal Skill Development Lifecycle

**Process being simulated**: The end-to-end lifecycle for taking one atomic skill
from "spec written" to "shipped in a SKILL.md file that a user can run."

**Entry state**: Skill spec exists in signal.skills.yaml with description, no golden prompt.
**Exit state**: SKILL.md file in output/flat/.claude/skills/{skill}/ that produces useful
output when a developer runs it in their repo.

---

## Phase 1: Setup

**Process decomposition** (from SHIPPING.md and observed session work):

```
1. spec-written         skill in signal.skills.yaml with description
2. trace-done           trace-skill run produces hand-compiled expected output
3. findings-applied     spec updated with SF-NN findings
4. rubric-created       quest-rubric produces C-01..N scoring criteria
5. variations-r1        quest-variate produces V-01..V-05 prompt variations
6. scored-r1            quest-score ranks variations, finds excellence signals
7. [loop if needed]     rubric evolves, variations re-generated
8. golden               quest-golden writes the converged prompt body
9. yaml-updated         signal.skills.yaml updated with golden: path
10. program-updated     binding-flat.program.yaml updated with golden body
11. generated           craft generate produces SKILL.md from program.yaml
12. verified            SKILL.md produces useful output when invoked
13. shipped             SKILL.md copied to user's .claude/skills/
```

**Roles**: Signal Developer (skill author), craft CLI (generator), Claude (executor)

---

## Phase 2: Execute

### Step 1 → Step 2: spec-written to trace-done

**Walk**: A skill spec exists. Someone needs to run trace-skill on it.

**Trigger**: Spec is written. Who decides it's ready to trace?
No explicit gate exists. The spec can be in any state -- partially written, missing
lifecycle phases, missing artifact path -- and trace-skill will run on it.

**Decision point**: trace-skill should fail fast if the spec is incomplete. Currently
it produces a USEFUL/NOT USEFUL verdict but doesn't enforce a minimum spec quality
before running. A spec missing the lifecycle section produces a weaker trace.

**Exception flow**: Spec has been updated since the last trace (finding applied).
No mechanism detects spec staleness vs. trace artifact. A trace artifact from before
SF-13 was applied to scout-positioning is now stale -- the trace no longer reflects
the current spec. Nothing flags this.

**Finding FL-01 (MAJOR)**: No staleness detection between spec updates and trace artifacts.
When a spec is updated (SF-NN applied), existing trace artifacts become stale but there
is no mechanism to flag them as needing re-trace. Downstream quest artifacts (rubrics,
scorecards) built on stale traces may not reflect the corrected spec.

### Step 2 → Step 4: trace-done to rubric-created

**Walk**: Trace artifact exists. quest-rubric reads it and generates criteria.

**Happy path**: Rubric is generated, criteria are derived from the trace's USEFUL/NOT USEFUL
analysis and the SF-NN findings embedded in the trace.

**Gap**: The rubric is created from the trace artifact, but the trace artifact may not
cover all the skill's scenarios. scout-competitors has ONE trace (the all-hands scenario).
The rubric derived from it reflects only that scenario. A skill with 3 test scenarios
needs a rubric that covers all 3, not just the first.

**Finding FL-02 (MAJOR)**: Single-scenario rubrics. Each skill has one trace artifact
(one test scenario) but may need 3-5 scenarios for full coverage. The rubric built from
one scenario may produce a "GOLDEN" prompt that only works for that scenario.
Resolution: require at minimum 2 trace scenarios per skill before calling it golden.
A fast path: the wave-1 trace IS scenario 1; the wave-2 re-trace IS scenario 2.
We already have this for scout-competitors -- use it.

### Step 4 → Step 8: rubric to golden (the quest loop)

**Walk**: quest-run-one.sh runs rubric → variate → score → (evolve) → variate → score → golden.

**Observed behavior** (from scout-feasibility running now):
- Round 1: generates 5 variations, scores them, finds excellence signals
- If signals found: rubric evolves, round 2 runs
- Convergence in 2-4 rounds typical

**Bottleneck identified**: The relay runs scripts sequentially per skill. Running 52
skills sequentially = 52 * ~15min = ~13 hours. The relay supports concurrent jobs but
quest-run-one.sh has no job-to-job interference (P-01 compliant), so all 52 can run
in parallel. Need quest-run-all.sh.

**Finding FL-03 (MAJOR)**: No parallel dispatch script. quest-run-all.sh does not exist.
52 skills running sequentially would take ~13 hours. Parallel would take ~30 minutes
(limited by relay throughput and rate limits).

### Step 8 → Step 11: golden to generated SKILL.md

**Walk**: golden prompt is in signal.skills.yaml. binding-flat.program.yaml needs updating.
Then craft generate runs.

**Gap 1**: There is no script that reads signal.skills.yaml and writes binding-flat.program.yaml.
This step is manual -- someone reads the golden: field, copies the description, updates the yaml.
For 52 skills this is ~2 hours of manual work.

**Finding FL-04 (MAJOR)**: No automation from signal.skills.yaml → binding-flat.program.yaml.
A Python script that reads golden files and writes binding-flat.program.yaml would be ~50 lines.

**Gap 2**: craft generate has CF-01 (double frontmatter) and CF-02 (--hydrate missing).
Even with golden prompts in program.yaml, the generated SKILL.md has the frontmatter bug.

**Finding FL-05**: CF-01 and CF-02 are on the critical path to shipping. CF-01 produces
broken SKILL.md files. CF-02 means golden prompts in program.yaml descriptions must be
hand-copied or scripted (no auto-hydration). Both need craftworks fixes before v0.1 ships.

### Step 11 → Step 13: generated to shipped

**Walk**: SKILL.md file exists in output/flat/. User copies it to .claude/skills/.

**Gap**: No install script. The user has to:
1. Find the right SKILL.md for the skill they want
2. Create .claude/skills/{name}/ directory in their repo
3. Copy the file

For a developer installing all 52 skills, this is 52 manual steps.

**Finding FL-06 (MAJOR)**: No install script. `signal install` or `cp -r output/flat/.claude/skills/* ./.claude/skills/` should be a single command in a README. Without it, zero-barrier fails at installation.

---

## Phase 3: Findings

### Bottlenecks

| Step | Bottleneck | Impact | Fix |
|------|-----------|--------|-----|
| spec → trace | No staleness detection | Stale traces → weak golden prompts | Version traces with spec hash |
| trace → rubric | Single-scenario rubrics | Overfitted golden prompts | Require 2+ scenarios per skill |
| quest loop | No parallel dispatch | 13hr sequential vs 30min parallel | quest-run-all.sh |
| golden → program.yaml | Manual update step | 2hr manual work for 52 skills | gen-binding-flat.py |
| generate → ship | No install script | Zero-barrier promise broken | signal-install.sh |

### Missing steps (not in current process)

**Step 11.5: verify** -- run the generated SKILL.md and validate it produces useful output.
Currently there is no verification step between "craft generate completes" and "ship."
A trace-skill run on the generated SKILL.md output would close this gap.

**Step 0: spec quality gate** -- before trace-skill runs, check that the spec has
required sections (lifecycle phases, artifact path, stock roles, example). This prevents
wasted trace runs on incomplete specs.

### Flow summary

```
[spec-written] → [GATE: spec quality] → [trace-done] → [DETECT: staleness] →
[findings-applied] → [rubric-created] → [quest-loop (parallel)] → [golden] →
[AUTO: gen-binding-flat.py] → [craft generate] → [VERIFY: trace output] →
[signal-install.sh] → [shipped]
```

---

## Phase 4: Amend

Three adjustments to the current process:

1. **Add spec quality gate** (before trace): a short checklist (lifecycle phases present?
   artifact path defined? stock roles listed? example in spec?) that fails fast before
   a trace run is wasted on an incomplete spec.

2. **Require 2 trace scenarios per skill** (before quest): wave-1 trace (baseline scenario)
   and wave-2 re-trace (post-findings scenario) already exist for scout-competitors. Make
   this the standard. The wave-2 trace confirms spec fixes and provides a second ground truth
   for the rubric.

3. **Build the 3 missing automation scripts** (FL-03, FL-04, FL-06):
   - `tools/quest-run-all.sh` — parallel dispatch for all non-golden skills
   - `tools/gen-binding-flat.py` — reads signal.skills.yaml → writes binding-flat.program.yaml
   - `tools/signal-install.sh` — copies all SKILL.md files to .claude/skills/ in target repo
