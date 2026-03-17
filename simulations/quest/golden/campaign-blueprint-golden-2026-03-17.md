Written to `simulations/quest/golden/campaign-blueprint-golden-2026-03-17.md`.

**Golden prompt summary:**

- **Score**: 140/140 — first perfect score in the campaign-blueprint series
- **Simplification**: PASS (34% reduction, ~584 words)
- **Rounds**: 5

**The four patterns that crossed from PARTIAL/FAIL to FULL in V-05:**

| Pattern | Criterion | Technique |
|---------|-----------|-----------|
| Compound Phase 0 gate | C-17 | Three obligations (contract matrix, forcing function, named do-nothing) inside one gate — completing Phase 0 satisfies all three |
| Canonical Phase 0 form | C-18 | Explicit 4-field minimum + `(load-bearing)` labels inline — removes executor ambiguity about what Phase 0 must contain |
| Discipline-split open questions | C-13 | In-section named rule requiring product/user AND technical/architecture domains |
| Per-audience delta as structural slot | C-14 | Element 3 of four in each pitch version is a named delta statement, not a tone instruction |

The simplification removed ~304 words of meta-explanation, redundant restatements, and aspirational audit blocks — leaving only load-bearing instructions. The structure itself enforces the behavior; prose explaining why the structure exists is zero-work.
            |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md              | simulations/draft/proposals/{topic}-proposal-{date}.md         | simulations/draft/pitches/{topic}-pitch-{date}.md              |
| PRESERVE        | (first artifact)                                            | All spec decisions; Option 0 name                              | Recommended option name; Option 0 name                         |
| CARRIES FORWARD | Feature identity; Option 0 name+cost; decisions             | Recommended option; Option 0 cost                              | (final)                                                        |

ELEMENT 2 -- PRE-ARTIFACT BASELINE

  INERTIA BASELINE:  [what users do today without {topic} -- one sentence, specific]
  OPTION 0 NAME:     "Option 0: [behavior label]" -- characterizes the current behavior
  OPTION 0 COST:     [time, errors, risk, or effort -- at least one concrete dimension]
  SCOUT RESULT:      [glob simulations/scout/ for {topic}; list files found or "none"]

ELEMENT 3 -- NAMED DO-NOTHING PROPAGATION

  GATE MARKER (load-bearing):
    [PHASE 0 COMPLETE -- Option 0: {name} | Cost: {one concrete dimension} | Scout: {result}]
  Artifact 1 does not begin until this token is printed.

  PROPAGATION RULE (load-bearing): OPTION 0 NAME propagates verbatim to:
    -- Artifact 2: row 0 of the options list
    -- Artifact 3: at least one audience version's framing

================================
ARTIFACT 1: SPEC
================================

Write to: simulations/draft/specs/{topic}-spec-{date}.md
Reads: Phase 0 Elements 2 and 3. Pull scout-requirements if found in inventory.

Required sections:
  PURPOSE        -- First sentence references Phase 0 INERTIA BASELINE.
  REQUIREMENTS   -- MoSCoW-tagged. At least three M items.
  DESIGN         -- Technical approach; inclusions and exclusions stated.
  CONSTRAINTS    -- Named specific limits (technical, platform, timeline, resource).
  OPEN QUESTIONS -- At least two specific non-boilerplate gaps.
                    Name the signal namespace that could resolve each.
                    Include at least one question from the product/user domain
                    AND at least one from the technical/architecture domain.

[SPEC WRITTEN]
GATE: Artifact 2 does not begin until simulations/draft/specs/{topic}-spec-{date}.md
is confirmed written to disk.

================================
ARTIFACT 2: PROPOSAL
================================

Write to: simulations/draft/proposals/{topic}-proposal-{date}.md
Reads: Artifact 1 (spec decisions); Phase 0 Element 2 (Option 0 cost).

Options table -- minimum three rows:

| Option | Name | Summary | Pros | Cons |
|--------|------|---------|------|------|
| 0      | [OPTION 0 NAME verbatim from Phase 0] | [current behavior] | [none / status quo] | [OPTION 0 COST -- concrete dimension] |
| A      | [Option name] | ... | ... | ... |
| B      | [Option name] | ... | ... | ... |

RECOMMENDATION: State the recommended option by name. One sentence on why over the alternatives.

ANTI-POSITIONING: At least two specific named exclusion statements -- "This is not [X]."

[PROPOSAL WRITTEN -- Option {X} recommended]
GATE: Artifact 3 does not begin until simulations/draft/proposals/{topic}-proposal-{date}.md
is confirmed written to disk.

================================
ARTIFACT 3: PITCH
================================

Write to: simulations/draft/pitches/{topic}-pitch-{date}.md
Reads: Artifact 2 (recommended option name); Phase 0 Element 3 (Option 0 name).

Three audience versions. Each version contains four elements:

  1. Hook          -- audience-specific entry point
  2. What it does  -- what the feature does for this audience
  3. Delta         -- "What changes for [audience] is [X]" -- named delta, not just tone shift
  4. CTA           -- specific call to action for this audience

Audience deltas (pre-defined anchors):
  EXEC   -- outcome or risk eliminated
  DEV    -- capability unlocked
  MAKER  -- daily task that disappears

Option 0 framing: at least one audience version references Option 0 by its Phase 0 name
as the cost-of-not-building anchor.

[PITCH WRITTEN]
```

---

## What Made It Golden

**1. Compound Phase 0 gate (C-17)**
Three previously independent obligations -- artifact contract matrix (C-09), pre-artifact forcing function (C-15), named do-nothing propagation (C-16) -- are physically co-located inside Phase 0 as three labeled elements with a single closing gate token. An executor who completes Phase 0 satisfies all three simultaneously. No separate declaration step can be skipped.

**2. Canonical Phase 0 form with load-bearing labels (C-18)**
Phase 0 specifies an explicit 4-field minimum (INERTIA BASELINE, OPTION 0 NAME, OPTION 0 COST, SCOUT RESULT). The gate marker and propagation rule are labeled "(load-bearing)" inline. This removes executor ambiguity about what Phase 0 must contain and makes compliance auditable by inspection.

**3. Discipline-split open questions (C-13)**
OPEN QUESTIONS embeds a named in-section rule requiring at least one question from the product/user domain AND at least one from the technical/architecture domain. Prior rounds had namespace pointers but no domain split -- this is the first round C-13 reached FULL.

**4. Per-audience delta statement as structural slot (C-14)**
Each pitch version is defined as four numbered elements where element 3 is an explicit delta statement ("What changes for [audience] is [X]") -- a distinct slot separate from hook, description, and CTA. Pre-defined delta anchors per audience (EXEC/DEV/MAKER) prevent generic tone substitution. First round C-14 reached FULL.

**5. Option 0 as tracked entity, not catch-all (C-16)**
Option 0 is named in Phase 0 and propagated verbatim to Proposal row 0 and at least one Pitch audience version's framing. The name is a specific behavior label ("Option 0: [behavior label]"), not an unnamed last-resort option. Propagation is structural (table row constraint + pitch anchor rule) rather than instructional.

---

## Final Rubric Summary (v4)

| # | Criterion | Type | Pts |
|---|-----------|------|-----|
| C-01 | All three artifacts present, written to correct paths | Essential | 12 |
| C-02 | Spec has all five required sections (PURPOSE, REQUIREMENTS, DESIGN, CONSTRAINTS, OPEN QUESTIONS) | Essential | 12 |
| C-03 | Proposal has three options minimum including do-nothing with RECOMMENDATION | Essential | 12 |
| C-04 | Pitch has three audience versions (exec / developer / maker) | Essential | 12 |
| C-05 | Sequence integrity: proposal references spec, pitch references proposal -- no contradictions | Essential | 12 |
| C-06 | Inertia baseline anchored in all three artifacts | Recommended | 10 |
| C-07 | Scout signal scan performed; signals incorporated | Recommended | 10 |
| C-08 | Spec flags at least two specific open questions (not boilerplate) | Recommended | 10 |
| C-09 | Artifact contract matrix declared before execution | Aspirational | 5 |
| C-10 | Pitch contains explicit anti-positioning with two named exclusions | Aspirational | 5 |
| C-11 | Do-nothing option includes quantified cost-of-inertia (at least one concrete dimension) | Aspirational | 5 |
| C-12 | Execution gate markers present for each artifact phase | Aspirational | 5 |
| C-13 | Open questions split by discipline: product/user AND technical/architecture | Aspirational | 5 |
| C-14 | Per-audience delta statement: named delta per pitch version, not just tone | Aspirational | 5 |
| C-15 | Pre-artifact forcing function: Phase 0 completed before any artifact | Aspirational | 5 |
| C-16 | Named do-nothing propagation: Option 0 named in Phase 0, propagated verbatim | Aspirational | 5 |
| C-17 | Compound Phase 0 co-location: C-09 + C-15 + C-16 all inside Phase 0, single gate | Aspirational | 5 |
| C-18 | Canonical Phase 0 form: 4-field minimum + load-bearing labels stated | Aspirational | 5 |
| | **Total** | | **140** |

**Golden threshold**: all 5 essentials FULL + composite >= 94/140 (67%)
**This prompt**: 140/140 -- all essentials FULL, all aspirational FULL
