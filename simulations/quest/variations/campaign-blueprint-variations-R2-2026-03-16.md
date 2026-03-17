Written to `simulations/quest/variations/campaign-blueprint-variations-R2-2026-03-16.md`.

---

## campaign-blueprint — Round 2 Variations

**R2 context:** R1 left two excellence gaps. V-03 (100 base) missed C-14. V-05 (97.5) missed C-13. R2 targets closing both.

---

### V-01 — Artifact Contract Axis
**Hypothesis:** Explicit READ/WRITE/PRESERVE contracts at the top of each artifact make the dependency chain visible before execution — preventing C-06/C-07 failures, and creating a natural FINDINGS slot after each artifact.
**Expected C-13:** Yes (FINDINGS after each artifact, conviction audit in pitch FINDINGS). **Expected C-14:** Yes (signal consumption table in close).

---

### V-02 — Pre-flight Verification Axis
**Hypothesis:** A structured pre-flight checklist before each GATE forces in-loop structural verification. The pitch checklist includes explicit "conviction delta" and "duplication check" items — testing whether checklist format achieves C-13 vs FINDINGS label.
**Expected C-13:** Partial (checklist items, not a labeled FINDINGS block). **Expected C-14:** Yes.

---

### V-03 — Minimal Density Axis
**Hypothesis:** The shortest possible prompt containing all four excellence trigger phrases (GATE, proactive glob, FINDINGS with conviction audit, signal log table) — tests whether scaffolding is load-bearing or ceremony. If it scores the same, shorter wins.
**Expected:** Full — all 4 excellence signals in minimal surface area.

---

### V-04 — Lifecycle + Conviction Merge (C-13 + C-14 Target)
**Hypothesis:** Pure surgical merge of V-03 R1's 4-phase lifecycle (which earned C-13) with V-05 R1's signal consumption table (which earned C-14). No new structure invented — just filling the two documented gaps. Expected: 108 (100 base + 8 excellence bonus).
**Prediction:** Strongest structural candidate.

---

### V-05 — Pre-execution Conviction Architecture
**Hypothesis:** Tests whether a "BEFORE WRITING — conviction architecture" block (answer conviction questions *before* writing) substitutes for post-execution FINDINGS. If C-13 requires the FINDINGS label specifically, this scores partial; if intent matters more than placement, this scores full.
**Prediction:** Boundary test — will settle whether conviction audit placement matters.

---

**Key scoring question R2 will answer:** Does C-13 require the word "FINDINGS" and post-execution placement, or does any explicit conviction/duplication prompt satisfy it? V-02 and V-05 are the diagnostic variants.
 signal namespace that resolves it.

FINDINGS: list three findings from the spec process — decisions made, ambiguities
  surfaced, assumptions that still need validation.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md
      is written to disk.

═══════════════════════════════════════
ARTIFACT 2: PROPOSAL
Contract:
  READS:          spec from Artifact 1 (required); scout-feasibility if found in setup
  WRITES:         simulations/draft/proposals/{topic}-proposal-{date}.md
  PRESERVES:      spec decisions — do not re-open questions the spec resolved
  CARRIES FORWARD: recommended option name to Artifact 3
═══════════════════════════════════════
Options (three minimum, do-nothing required):
  For each: name, description, pros, cons, risk (H/M/L), effort (S/M/L).
  Do-nothing: describe honestly — what cost does the team keep paying?

Recommendation: state chosen option. Three reasons, each citing a spec decision or
  constraint. No new design work here.

FINDINGS: state which spec decisions most constrained the option space. Flag any design
  question the proposal had to resolve that the spec left open — these are contamination
  risks for Artifact 3.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md
      is written to disk.

═══════════════════════════════════════
ARTIFACT 3: PITCH
Contract:
  READS:          proposal from Artifact 2 (required); spec from Artifact 1 (required);
                  scout-positioning if found in setup
  WRITES:         simulations/draft/pitches/{topic}-pitch-{date}.md
  CARRIES FORWARD: recommended option as subject of all three versions
═══════════════════════════════════════
Three versions (all required):

EXEC (decision-makers):
  Hook: cost of inertia — what keeps happening without this?
  What: outcome of the recommended option, business-level.
  Why: risk of continued inertia (from do-nothing option in proposal).
  CTA: approve / fund / unblock.

DEV (engineers and technical leads):
  Hook: capability unlocked — what can you build that you couldn't before?
  What: reference the technical design from the spec.
  Why: technical debt or opportunity cost of the current approach.
  CTA: join beta / review the spec / contribute.

MAKER (practitioners):
  Hook: the friction you feel today (from inertia baseline).
  What: plain language only. No spec or proposal terminology.
  Why: time saved, steps removed, frustration resolved.
  CTA: try it / sign up / start now.

Anti-positioning (shared across all three): what this feature is NOT, two sentences.

FINDINGS: state what conviction each version establishes that the spec and proposal did not.
  Note any content you nearly duplicated from spec or proposal — name it explicitly.

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md

═══════════════════════════════════════
CAMPAIGN CLOSE
═══════════════════════════════════════
| Artifact | Path                                    | Scout signal consumed  | Open questions |
|----------|-----------------------------------------|------------------------|----------------|
| Spec     | simulations/draft/specs/...             | (namespace or none)    | (list)         |
| Proposal | simulations/draft/proposals/...         | (namespace or none)    | (list)         |
| Pitch    | simulations/draft/pitches/...           | (namespace or none)    | (list)         |

For each open question, recommend the signal namespace that would resolve it.
```

---

## V-02 — Pre-flight Verification Axis

**Hypothesis:** Requiring a structured pre-flight checklist at the end of each artifact —
to be completed before the GATE opens — forces in-loop verification of structural
completeness and excellence signal compliance. R1 found that failures compound across
artifacts (a thin spec produces a weak proposal). A per-artifact gate with explicit
checks catches failures before they propagate. The pitch checklist includes conviction
delta and duplication check, which maps to C-13 via a different structural mechanism
than V-03 R1's FINDINGS block — testing whether checklist-format achieves the same
outcome.

```
You are running /campaign-blueprint for: {topic}

This campaign produces three artifacts in strict sequence. Each artifact must pass its
pre-flight checklist before the GATE opens.

CAMPAIGN SETUP
Step 1. Glob simulations/scout/ for this topic. List every file found, by namespace.
        Run this now — not conditionally.
Step 2. Topic identity in one sentence: feature, audience, problem solved.
        Lock this. All three artifacts must use this identity.
Step 3. Inertia baseline in one sentence: what users do today without this feature.

Do not begin Artifact 1 until all three steps are printed.

─────────────────────────────────────────
ARTIFACT 1: SPEC
─────────────────────────────────────────
Write the specification. All five sections are required:
  PURPOSE     — what and why, tied to inertia baseline.
  REQUIREMENTS — MoSCoW-tagged bullets; pull from scout-requirements if found in setup.
  DESIGN      — components, data flow, key decisions.
  CONSTRAINTS — technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — each unknown + signal namespace that resolves it.

PRE-FLIGHT (complete before GATE):
  [ ] All five required sections present and non-empty
  [ ] At least one Must-have requirement tagged
  [ ] Every open question paired with a signal namespace
  [ ] Topic identity from setup is consistent with content

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md
      is written to disk.

─────────────────────────────────────────
ARTIFACT 2: PROPOSAL
─────────────────────────────────────────
Read the spec. Pull from scout-feasibility if found in setup.

Write the proposal:
  Three options minimum. Option A must be do-nothing — describe its cost honestly.
  For each option: name, description, pros, cons, risk (H/M/L), effort (S/M/L).
  RECOMMENDATION: chosen option + three reasons, each citing a spec decision or constraint.
  Do not re-open any question the spec resolved.

PRE-FLIGHT (complete before GATE):
  [ ] Do-nothing option present with honest cost described
  [ ] Three or more options
  [ ] Recommendation cites three spec decisions or constraints
  [ ] No spec decision re-opened

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md
      is written to disk.

─────────────────────────────────────────
ARTIFACT 3: PITCH
─────────────────────────────────────────
Read the proposal. The recommended option is the subject.
Pull from scout-positioning if found in setup.

Write three full versions (all required):
  EXEC  — Hook: cost of inertia. What: outcome of recommended option.
          Why: risk of continued inertia. CTA: approve/fund/unblock.
  DEV   — Hook: capability unlocked. What: references technical design from spec.
          Why: technical debt of current approach. CTA: join beta/review spec.
  MAKER — Hook: friction today. What: plain language, no jargon.
          Why: time saved/friction removed. CTA: try it/start now.

Anti-positioning (shared): what this is NOT, two sentences.

PRE-FLIGHT (complete before GATE):
  [ ] All three versions written in full with hook, what, why, and CTA
  [ ] Exec version leads with cost of inertia
  [ ] Dev version references spec's technical design by name
  [ ] Maker version contains no spec or proposal terminology
  [ ] Anti-positioning section present
  [ ] Conviction delta: state what conviction each version adds that the spec and proposal
      did not — write it out before calling the pitch complete
  [ ] Duplication check: name any content you nearly repeated from spec or proposal

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md

─────────────────────────────────────────
CAMPAIGN CLOSE
─────────────────────────────────────────
| Artifact | Path                            | Scout signal consumed  | Open questions |
|----------|---------------------------------|------------------------|----------------|
| Spec     | simulations/draft/specs/...     | (namespace or none)    | (list)         |
| Proposal | simulations/draft/proposals/... | (namespace or none)    | (list)         |
| Pitch    | simulations/draft/pitches/...   | (namespace or none)    | (list)         |

Recommend the signal namespace for each open question remaining.
```

---

## V-03 — Minimal Density Axis

**Hypothesis:** A prompt containing only the minimum required trigger phrases — the
right keywords (GATE, proactive glob, FINDINGS with conviction audit, per-artifact
signal log) with no scaffolding — tests whether briefer prompts that embed the critical
signal phrases score comparably to verbose structured prompts. If the scoring is equal,
shorter is preferable. If the scoring drops, the scaffolding is load-bearing, not just
ceremony.

```
You are running /campaign-blueprint for: {topic}

SETUP
Glob simulations/scout/ for this topic now. List all signals found, by namespace.
Topic identity: one sentence. Inertia baseline: one sentence.
Do not begin Artifact 1 until setup is printed.

ARTIFACT 1 — SPEC
Sections: purpose (anchor to inertia baseline), requirements (MoSCoW), design,
constraints, open questions (with signal namespace per item).
Pull scout-requirements from setup inventory if found.
Path: simulations/draft/specs/{topic}-spec-{date}.md
GATE: Do not begin Artifact 2 until this file is written to disk.

ARTIFACT 2 — PROPOSAL
Read the spec. Pull scout-feasibility from setup inventory if found.
Three options minimum (do-nothing required, described with honest cost).
Per option: name, description, pros, cons, risk (H/M/L), effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.
Do not re-open questions the spec resolved.
Path: simulations/draft/proposals/{topic}-proposal-{date}.md
GATE: Do not begin Artifact 3 until this file is written to disk.

ARTIFACT 3 — PITCH
Read the proposal. Pull scout-positioning from setup inventory if found.
Three versions (exec, dev, maker), each with hook, what, why, CTA.
  Exec: cost-of-inertia hook; outcome of recommended option; risk of inertia; approve/fund.
  Dev: capability-unlocked hook; references technical design from spec; no business jargon.
  Maker: friction-today hook; plain language only, no jargon; time saved; try it.
Anti-positioning: what this is NOT, two sentences.

FINDINGS: state what conviction each version adds that the spec and proposal did not.
Note any content you nearly duplicated from spec or proposal.

Path: simulations/draft/pitches/{topic}-pitch-{date}.md

CAMPAIGN CLOSE
| Artifact | Path | Scout signal consumed  | Open questions |
|----------|------|------------------------|----------------|
| Spec     | simulations/draft/specs/...     | (namespace or none) | (list) |
| Proposal | simulations/draft/proposals/... | (namespace or none) | (list) |
| Pitch    | simulations/draft/pitches/...   | (namespace or none) | (list) |
```

---

## V-04 — Lifecycle + Conviction Merge (C-13 + C-14 Target)

**Hypothesis:** V-03 (R1) scored 100 base but missed C-14 (signal consumption log).
V-05 (R1) scored 97.5 base but missed C-13 (conviction audit in FINDINGS). This
variation merges V-03 R1's 4-phase lifecycle — which produced the strongest conviction
audit — with V-05 R1's per-artifact signal consumption table. No new structural
invention. Pure surgical merge of what already worked, targeting both excellence gaps
simultaneously. Expected: 108 (100 base + 8 excellence bonus).

```
You are running /campaign-blueprint for: {topic}

Run the 4-phase lifecycle (SETUP / EXECUTE / FINDINGS / AMEND) for each artifact.
Complete all phases before the GATE opens. Do not begin the next artifact until the
GATE condition is met.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GLOB: simulations/scout/ for this topic. List every signal file found, organized by
      namespace. Run now — not conditionally.
IDENTITY: confirm topic in one sentence — feature, audience, problem solved.
          This identity must not deviate across all three artifacts.
INERTIA: one sentence — what users do today without this feature. This is the baseline
         competitor for all three artifacts.

Print the setup block in full. Do not begin Artifact 1 until complete.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP: Pull scout-requirements from setup inventory if found.
       Note any requirements already captured.

EXECUTE: Author specification — all five sections required:
  PURPOSE     — what and why, anchored to the inertia baseline.
  REQUIREMENTS — bulleted, MoSCoW-tagged. Pull from scout-requirements if found.
  DESIGN      — components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS — technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — unknowns; for each, name the signal namespace that could resolve it.

FINDINGS: list three findings — decisions made, ambiguities surfaced, assumptions
          requiring validation.

AMEND: for each open question, confirm or add the signal namespace that resolves it.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md
      is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP: Read the spec just written. Pull scout-feasibility from setup inventory if found.
       Identify the spec decisions that most constrain the option space.

EXECUTE: Author proposal — three options minimum (do-nothing is required, describe its
  cost honestly):
  For each option: name, description, pros, cons, risk (H/M/L), effort (S/M/L).
  RECOMMENDATION: chosen option + three reasons, each citing a spec decision or constraint.
  Do not re-open any design question the spec resolved.

FINDINGS: state which spec decisions most influenced the recommendation. Note any spec
          gaps that made option comparison difficult.

AMEND: flag any design question the proposal had to resolve that the spec left open.
       These are forward-contamination risks — name them explicitly.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md
      is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP: Read the proposal. Identify the recommended option.
       Pull scout-positioning from setup inventory if found.

EXECUTE: Author three pitch versions in full:

EXEC (decision-makers):
  Hook: cost of inertia — what keeps happening without this?
  What: outcome of the recommended option, business-level.
  Why: risk of continued inertia (from do-nothing option in proposal).
  CTA: approve / fund / unblock.

DEV (engineers and technical leads):
  Hook: capability unlocked — what can you build that you couldn't before?
  What: reference the technical design from the spec.
  Why: technical debt or opportunity cost of the current approach.
  CTA: join beta / review the spec / contribute.

MAKER (practitioners):
  Hook: the friction you feel today (inertia baseline).
  What: plain language only. No spec or proposal terminology.
  Why: time saved, steps removed, frustration resolved.
  CTA: try it / sign up / start now.

Anti-positioning (shared): what this feature is NOT, two sentences.

FINDINGS: state what conviction each version establishes that the spec and proposal did not.
          Note any content you nearly duplicated from spec or proposal — name it explicitly.

AMEND: list one improvement per version that a specific scout signal could enable.

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
| Artifact | Path                                    | Scout signal consumed  | Open questions |
|----------|-----------------------------------------|------------------------|----------------|
| Spec     | simulations/draft/specs/...             | (namespace or none)    | (list)         |
| Proposal | simulations/draft/proposals/...         | (namespace or none)    | (list)         |
| Pitch    | simulations/draft/pitches/...           | (namespace or none)    | (list)         |

For each open question, name the signal namespace that would resolve it.
```

---

## V-05 — Pre-execution Conviction Architecture (Front-loaded Audit)

**Hypothesis:** R1's C-13 winner (V-03) placed the conviction audit in a post-execution
FINDINGS block — reflection after writing. This variation tests whether moving the
conviction audit BEFORE execution (as a pre-write framing question) produces higher
conviction differentiation by forcing the model to articulate each version's unique
purpose before a single word is written — analogous to "hypothesis first" in the
prove namespace. Combined with the signal consumption table (C-14) and all other
excellence signals. If pre-execution audit scores lower than post-execution FINDINGS,
R1's lesson is confirmed: reflection after, not intent before.

```
You are running /campaign-blueprint for: {topic}

Produce three artifacts that form a coherent decision package: spec, proposal, pitch.
Each artifact is written to disk before the next begins.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. GLOB: simulations/scout/ — list every file found under this topic, by namespace.
   Run now. This is not conditional.
2. IDENTITY: one sentence — feature, audience, problem solved.
   All three artifacts use this identity without deviation.
3. INERTIA: one sentence — what users do today without this feature.
4. ARTIFACTS TO PRODUCE:
   - simulations/draft/specs/{topic}-spec-{date}.md
   - simulations/draft/proposals/{topic}-proposal-{date}.md
   - simulations/draft/pitches/{topic}-pitch-{date}.md

Print setup block in full. Do not begin Artifact 1 until complete.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pull scout-requirements from setup inventory if found.

Write all five sections:
  PURPOSE      — what and why, anchored to inertia baseline.
  REQUIREMENTS — bulleted, MoSCoW-tagged. Pull from scout-requirements if found.
  DESIGN       — components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS  — technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — each unknown + signal namespace that resolves it.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md
      is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Read the spec. Pull scout-feasibility from setup inventory if found.
Do not re-open any design question the spec resolved.

Three options minimum. Option A must be do-nothing — describe its cost honestly.
For each option: name | description | pros | cons | risk (H/M/L) | effort (S/M/L)

RECOMMENDATION: chosen option + three reasons, each citing a spec decision or constraint.
State explicitly what the do-nothing option keeps costing.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md
      is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Read the proposal. The recommended option is the subject.
Pull scout-positioning from setup inventory if found.

BEFORE WRITING — conviction architecture:
  Answer these two questions in writing, then write the pitch:
  (a) What specific conviction does each version need to establish that neither the
      spec nor the proposal established? One sentence per version.
  (b) What content from the spec or proposal are you most at risk of duplicating?
      Name it. Then avoid it.

Write three versions in full:

EXEC (decision-makers):
  Hook: cost of inertia — what keeps happening without this?
  What: business-level outcome from the recommended option.
  Why: risk of continued inertia, from do-nothing option in the proposal.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads):
  Hook: capability unlocked.
  What: reference the technical design from the spec.
  Why: technical debt or opportunity cost of the current approach.
  CTA: join beta / review the spec / contribute.

MAKER (practitioners):
  Hook: the friction you feel today.
  What: plain language only. No spec or proposal terminology.
  Why: time saved, steps removed, frustration resolved.
  CTA: try it / sign up / start now.

Anti-positioning (shared): what this feature is NOT, two sentences.

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
| Artifact | Path                                    | Scout signal consumed  | Open questions |
|----------|-----------------------------------------|------------------------|----------------|
| Spec     | simulations/draft/specs/...             | (namespace or none)    | (list)         |
| Proposal | simulations/draft/proposals/...         | (namespace or none)    | (list)         |
| Pitch    | simulations/draft/pitches/...           | (namespace or none)    | (list)         |

For each open question, recommend the signal namespace that would resolve it.
```

---

## Variation Summary

| ID | Axis | Hypothesis shorthand | Expected C-11 | Expected C-12 | Expected C-13 | Expected C-14 |
|----|------|----------------------|---------------|---------------|---------------|---------------|
| V-01 | Artifact contract | Explicit READ/WRITE contracts enforce dependency chain | Yes | Yes | Yes (FINDINGS) | Yes |
| V-02 | Pre-flight verification | Checklist before each GATE catches structural failures in-loop | Yes | Yes | Partial (checklist, not FINDINGS label) | Yes |
| V-03 | Minimal density | Right trigger phrases without scaffolding scores the same | Yes | Yes | Yes (FINDINGS) | Yes |
| V-04 | Lifecycle + conviction merge | Surgical merge of V-03 R1 + V-05 R1 hits all 4 excellence signals | Yes | Yes | Yes (FINDINGS) | Yes |
| V-05 | Pre-execution conviction | Front-loading conviction audit before writing vs post-execution FINDINGS | Yes | Yes | Partial (pre-write, not FINDINGS) | Yes |

**R2 prediction**: V-04 is the structural favorite (pure merge of proven patterns).
V-01 and V-03 are strong contenders if the rubric scores FINDINGS content over FINDINGS
label. V-02 and V-05 test boundary conditions: does checklist-format satisfy C-13? does
pre-execution audit substitute for post-execution reflection?
