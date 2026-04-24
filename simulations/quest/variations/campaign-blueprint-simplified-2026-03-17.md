Now I have the complete V-05 prompt (lines 578–729). Let me perform the analysis and simplification.

---

## Simplification Analysis — V-05 (R5 Golden, ~888 words)

### Zero-work phrases identified

| # | Removed phrase/block | Words | Criterion it claimed to serve | Why it's zero-work |
|---|---------------------|-------|-------------------------------|-------------------|
| 1 | Phase 0 intro para 2: "Minimum form: four fields in Element 2. Additional fields permitted, not required. Gate marker and propagation rule are load-bearing -- not optional." | 25 | C-17/C-18 (aspirational) | Meta-explanation of why the structure exists; the structure itself is already present and enforces the behavior |
| 2 | Phase 0 intro para 1 trimmed: "Three elements. All co-located here. Completing Phase 0 satisfies all three simultaneously." | 12 | C-17 (aspirational) | Three sentence fragments restating what Element 1-2-3 labels already communicate structurally |
| 3 | OPTION 0 COST three-dimension template (Time/Effort/Risk/N-A rows + "At least one dimension must be filled") | 47→14 | C-11 (aspirational) | C-03 only needs "a do-nothing option with Cons" — a one-liner achieves that; the 3-dimension template adds scoring richness above essential threshold |
| 4 | "It appears as the specific name, not as an unnamed catch-all." | 12 | C-16 (aspirational) | The preceding sentence already names the verbatim requirement; this sentence restates the negative form of the same rule |
| 5 | DISCIPLINE RULE block in OPEN QUESTIONS (5 lines about product/user + technical/architecture domains) | 45→9 | C-13 (aspirational) | C-02 only requires "at least two specific open questions" — the discipline split is above essential; collapsed to "Name the signal namespace per item." |
| 6 | OPTION 0 COST TEMPLATE block in Proposal ("the Cons cell must use the cost template from Phase 0 Element 2... priced cost-of-inertia. Not qualitative description only.") | 37 | C-11 (aspirational) | The table Cons cell hint `[OPTION 0 COST -- concrete dimension]` already enforces the link; this prose block restates it in paragraph form |
| 7 | "Pull scout-feasibility for effort and risk estimates on non-zero options if found." | 13 | C-07 (recommended) | C-03 says nothing about scout-feasibility; this line adds no weight to any essential criterion |
| 8 | 4-element numbered list in Pitch ("Each version must contain these four elements: 1. Hook... 2. What it does... 3. Why it matters -- explicit DELTA STATEMENT... 4. CTA") | 86→14 | C-14 (aspirational) | The framing-per-audience table that follows already specifies hook + what + delta + CTA per audience; the numbered list is a redundant preamble to the table. Collapsed to one line. |
| 9 | ANTI-POSITIONING extra qualifier: "Each must rule out an adjacent or commonly confused use case by name -- not generic hedging." | 17 | C-10 aspirational extension | The requirement itself ("at least two specific named exclusion statements") is present in the preceding sentence; this sentence amplifies but doesn't add a distinct criterion |
| 10 | Three Campaign Close check blocks (Open questions discipline check / Per-audience delta check / Option 0 cost template check) | 60 | C-11/C-13/C-14 (all aspirational) | These are audit rows for aspirational criteria only; essential checklist (gate tokens + Option 0 propagation) is in the main summary table already |

**Total removed: ~304 words**

---

## Simplified Prompt Body

```
You are running /campaign-blueprint for: {topic}

================================
PHASE 0 -- COMPOUND GATE
================================

Phase 0 is the structural gate. Three elements co-located here.

ELEMENT 1 -- ARTIFACT CONTRACT MATRIX

| Field           | Spec                                                   | Proposal                                               | Pitch                                                  |
|-----------------|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|
| READ            | Topic identity; scout signals (if found)               | Spec decisions; Option 0 cost                          | Proposal recommended option; Option 0 cost             |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md         | simulations/draft/proposals/{topic}-proposal-{date}.md | simulations/draft/pitches/{topic}-pitch-{date}.md      |
| PRESERVE        | (first artifact)                                       | All spec decisions; Option 0 name                      | Recommended option name; Option 0 name                 |
| CARRIES FORWARD | Feature identity; Option 0 name+cost; decisions        | Recommended option; Option 0 cost                      | (final)                                                |

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

[SPEC WRITTEN]
GATE: Artifact 2 does not begin until simulations/draft/specs/{topic}-spec-{date}.md
is confirmed written to disk.

================================
ARTIFACT 2: PROPOSAL
================================

Write to: simulations/draft/proposals/{topic}-proposal-{date}.md
Reads: Spec. Pull scout-feasibility if found in inventory.

Minimum three options. Row 0 uses Phase 0 OPTION 0 NAME verbatim.

| Option | Name                    | Description | Pros | Cons                                  | Risk | Effort |
|--------|-------------------------|-------------|------|---------------------------------------|------|--------|
| 0      | [Phase 0 OPTION 0 NAME] |             |      | [OPTION 0 COST -- concrete dimension] |      |        |
| B      |                         |             |      |                                       |      |        |
| C      |                         |             |      |                                       |      |        |

RECOMMENDATION: Named option. Rationale references at least one M-tier spec requirement
and at least one spec constraint.

[PROPOSAL WRITTEN -- Option {X} recommended]
GATE: Artifact 3 does not begin until simulations/draft/proposals/{topic}-proposal-{date}.md
is confirmed written to disk.

================================
ARTIFACT 3: PITCH
================================

Write to: simulations/draft/pitches/{topic}-pitch-{date}.md
Reads: Proposal recommended option. Pull scout-positioning if found in inventory.

Three audience versions: EXEC / DEV / MAKER.
Each version: hook (Option 0 cost as anchor) / what it does / delta for this audience / CTA.

  EXEC  -- Outcome and approval framing; Option 0 cost in business terms.
           Delta: [what the executive gains / risk eliminated that others do not see]
           CTA: approve/fund/unblock.
  DEV   -- Workflow change; spec design referenced; specific capability unlocked.
           Delta: [what the developer can now do that was previously blocked or manual]
           CTA: join beta/review spec.
  MAKER -- Daily friction resolved; plain language; "is this for me?" framing.
           Delta: [what daily task changes or disappears for this user type]
           CTA: try it/sign up/start now.

OPTION 0 NAME from Phase 0 appears verbatim in at least one version.
ANTI-POSITIONING: "What {topic} is NOT." At least two specific named exclusion statements.

[PITCH WRITTEN]

================================
CAMPAIGN CLOSE
================================

| Artifact | Path                                                   | Gate token                        | Option 0 name tracked         |
|----------|--------------------------------------------------------|-----------------------------------|-------------------------------|
| Phase 0  | --                                                     | [PHASE 0 COMPLETE] printed: Y/N   | assigned in Element 2: Y/N    |
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md         | [SPEC WRITTEN]: Y/N               | --                            |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md | [PROPOSAL WRITTEN]: Y/N           | verbatim row 0: Y/N           |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md      | [PITCH WRITTEN]: Y/N              | verbatim in at least 1: Y/N   |
```

---

## Simplification Report

**Original V-05 word count**: ~888 words  
**Simplified word count**: ~584 words  
**Reduction**: ~304 words removed (~34%)

### What was removed and why

| # | Block | Words saved | Why |
|---|-------|-------------|-----|
| 1 | Phase 0 intro para 2 ("Minimum form: four fields...") | 25 | Explains C-17/C-18 scoring logic — not executable behavior; structure enforces itself |
| 2 | Phase 0 intro para 1 trimmed (fragmented restatement) | 12 | Three sentence fragments restating what Element labels already communicate |
| 3 | OPTION 0 COST three-dimension template | 33 | C-11 aspirational; C-03 only needs a do-nothing option with cost — collapsed to one-liner |
| 4 | "It appears as the specific name, not as an unnamed catch-all." | 12 | Negative restatement of the verbatim rule already in the preceding sentence |
| 5 | DISCIPLINE RULE block in OPEN QUESTIONS | 36 | C-13 aspirational; collapsed to "Name the signal namespace per item" (9 words) |
| 6 | OPTION 0 COST TEMPLATE paragraph in Proposal | 37 | C-11 aspirational; Cons cell template row already links to Phase 0 cost |
| 7 | "Pull scout-feasibility for effort and risk estimates on non-zero options if found." | 13 | C-07 recommended only; no essential criterion requires it |
| 8 | 4-element numbered list in Pitch | 72 | C-14 aspirational preamble; per-audience framing table that follows already specifies all four elements — collapsed to one-liner |
| 9 | ANTI-POSITIONING extra qualifier sentence | 17 | Amplifies C-10 (aspirational); the requirement itself ("two specific named exclusion statements") remains |
| 10 | Three Campaign Close check blocks | 60 | C-11/C-13/C-14 audit rows, all aspirational — essential close table unchanged |

### Essential criteria verification

| Criterion | Mechanism in simplified version | Still passes? |
|-----------|--------------------------------|---------------|
| C-01 — All three artifacts at correct paths | Contract matrix WRITE row + "Write to:" per artifact | YES |
| C-02 — Spec has five required sections | Required sections list unchanged | YES |
| C-03 — Proposal has three options + do-nothing + RECOMMENDATION | Row 0 verbatim + table + RECOMMENDATION line unchanged | YES |
| C-04 — Pitch has three distinct audience versions | EXEC/DEV/MAKER framing table unchanged | YES |
| C-05 — Sequence integrity | "Reads:" lines + GATE statements + contract matrix preserved | YES |

**All essential criteria still pass: YES**

```json
{"simplified_word_count": 584, "original_word_count": 888, "all_essential_still_pass": true}
```
