---
skill: quest-variate
skill_target: prove-topic
round: R12
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [per_claim_synthesis_table, named_hypothesis_claims, inline_weakens_annotation]
  combined: [V-04 (named_claims + inline_weakens), V-05 (all_three + gate + full_paths)]
r11_anchor: >
  R11 V-05 scored 100 against rubric v14 using a conviction ladder to propagate THIN
  flags to verdict confidence (C-09 full pass), plus a PRE-STAGE COMMITMENT BLOCK,
  HANDOFF-exclusive synthesis, and four-ceiling ordering. These mechanisms are powerful
  but structurally dense (inherited from R10's counter_claim_chain + evidence_provenance_tracking).
  All R12 variations carry the v14 must-haves: scout blocking before Stage 1, per-stage
  artifact writes with full paths, scout_source in hypothesis frontmatter, THIN flagging
  at point of discovery, and explicit "ready for /topic-story" readiness statement.
r12_thesis: >
  R11 V-05's conviction ladder achieved C-09 by making THIN flags structurally degrade
  a verdict tier. R12 tests whether simpler mechanisms can achieve the same result.
  Three single-axis probes: (V-01) a required THIN EVIDENCE IMPACT TABLE at synthesis
  with per-claim columns forces C-09 compliance without a ladder; (V-02) a CLAIM INDEX
  committed at Stage 1 gives THIN flags a precise claim target, making the synthesis
  table's "claim weakened" column unambiguous; (V-03) inline "weakens: [claim]" annotation
  at discovery eliminates any mapping step at synthesis. If any of these simpler mechanisms
  scores 100, it proves the conviction ladder was over-engineering for v14.
---

# prove-topic — Variate Round 12 (Rubric v14)

**Skill**: prove-topic
**Rubric**: v14
**Round**: R12
**Date**: 2026-03-16

---

## Variation Map

| Var  | Axis                            | Primary targets | Hypothesis                                                               |
|------|---------------------------------|-----------------|-------------------------------------------------------------------------|
| V-01 | per_claim_synthesis_table       | C-09            | A required table at synthesis with Source Stage + Claim + Confidence satisfies C-09 without any conviction ladder machinery |
| V-02 | named_hypothesis_claims         | C-09            | A CLAIM INDEX at Stage 1 gives THIN flags precise named targets; per-claim synthesis table cannot be vague about "claim weakened" |
| V-03 | inline_weakens_annotation       | C-08, C-09      | Requiring "weakens: [claim]" in every THIN flag at discovery makes synthesis aggregation trivial and C-09 mechanically enforced |
| V-04 | named_claims + inline_weakens   | C-08, C-09      | Combining a CLAIM INDEX (V-02) with inline weakens annotation (V-03) creates the tightest possible traceability chain with no retrospective mapping |
| V-05 | all_three + gate + full_paths   | all 10 criteria | Named claims + inline annotation + per-claim synthesis table + structural gate + full paths achieves 100 with less complexity than R11 V-05 |

**Artifact paths** (all variations):

| Stage | Signal              | Full path                                                                      |
|-------|---------------------|--------------------------------------------------------------------------------|
| 1     | prove-hypothesis    | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`        |
| 2     | prove-websearch     | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`          |
| 3     | prove-intelligence  | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`    |
| 4     | prove-analysis      | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`            |
| 5     | prove-synthesize    | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`        |

---

## V-01 — per_claim_synthesis_table

**Axis**: per_claim_synthesis_table
**Hypothesis**: A single required table at Stage 5 synthesis — with columns Source Stage,
Gap, Specific Claim Weakened, and Adjusted Confidence — is the minimum instruction
needed to satisfy C-09 full pass without a conviction ladder, HANDOFF chain, or ceiling
rules. The table columns force the executor to name the source stage and the specific
weakened claim. The instruction that the "Specific Claim Weakened" column must quote
the exact hypothesis claim (not a category) makes the reference precise enough for C-09.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five evidence stages in strict
forward sequence. One artifact written per stage. Final output: evidence brief
ready for /topic-story.

Stages: hypothesis -> websearch -> intelligence -> analysis -> synthesize

---

## SETUP -- Scout Check

Before any stage begins:

1. Glob `simulations/scout/{topic}-scout-*.md`.
2. If no file found:
   Emit: BLOCKED. No scout artifact for `{topic}`. Run a scout skill first.
   Halt. Do not proceed to Stage 1.
3. Set scout_source = full path of found file (most recent if multiple).
4. Read the file.
5. Emit: SCOUT CONFIRMED. scout_source = [full path]

Stage 1 cannot begin until SCOUT CONFIRMED is emitted with scout_source named.

---

## STAGE 1 -- HYPOTHESIS

Precondition: SCOUT CONFIRMED emitted with scout_source named.
If not emitted: BLOCKED at Stage 1. Halt.

Load scout_source. Frame the central testable claim for {topic}, grounded in the
scout findings. Reference scout_source explicitly in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [full path from SETUP]

---

## STAGE 2 -- WEBSEARCH

Precondition: Stage 1 artifact written.

Gather external evidence for the hypothesis. For each source, assess strength of
evidence. When evidence is thin or absent, flag at point of discovery:
  THIN: [area] -- [gap found]
Do not defer THIN flags to synthesis.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 -- INTELLIGENCE

Precondition: Stage 2 artifact written.

Search internal sources -- existing signal artifacts, related topic runs -- for
evidence relevant to the hypothesis. Flag thin evidence inline:
  THIN: [area] -- [gap found]

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 -- ANALYSIS

Precondition: Stage 3 artifact written.

Aggregate all THIN flags from Stages 2 and 3. Map each flag to the hypothesis
claim it weakens. Assess overall evidence strength.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 -- SYNTHESIZE

Precondition: Stage 4 artifact written.

State the verdict: supported / partially supported / not supported.

THIN EVIDENCE IMPACT TABLE (required -- include even if no THIN flags were found):

| Source Stage | Gap | Specific Claim Weakened | Adjusted Confidence |
|-------------|-----|-------------------------|---------------------|
| S2 or S3    | ... | [exact claim text from hypothesis, not a category] | Low / Med / High |

Rules:
- One row per THIN flag collected across Stages 2 and 3.
- "Specific Claim Weakened" must quote or paraphrase the exact hypothesis
  claim being undermined. Do not write a category like "scalability" --
  write the actual claim, e.g., "{topic} reduces deployment time by 50%".
- "Source Stage" must match where the THIN flag was emitted (S2 or S3).
- If no THIN flags: one row -- "none | none | no thin findings | full confidence".

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-02 -- named_hypothesis_claims

**Axis**: named_hypothesis_claims
**Hypothesis**: If the hypothesis artifact requires 3-5 numbered sub-claims in a CLAIM
INDEX (CLAIM-1, CLAIM-2, CLAIM-3), and each THIN flag must reference a specific claim
ID from that index, then the synthesis table's "Claim Weakened" column cannot be vague
-- the claim name is a committed identifier. This makes C-09 compliance structurally
guaranteed rather than instruction-dependent. The CLAIM INDEX also gives evidence
gathering stages a concrete checklist to work against, improving C-08.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages in forward sequence.
One artifact per stage. Final output: evidence brief ready for /topic-story.

---

## ARTIFACT PATHS (declared once; each WRITE instruction echoes the matching path)

| Stage | Signal             | Full path                                                                      |
|-------|--------------------|--------------------------------------------------------------------------------|
| 1     | prove-hypothesis   | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md          |
| 2     | prove-websearch    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md            |
| 3     | prove-intelligence | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md      |
| 4     | prove-analysis     | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md              |
| 5     | prove-synthesize   | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md          |

---

## SETUP -- Scout Check

1. Glob `simulations/scout/{topic}-scout-*.md`.
2. If absent: halt. Emit "BLOCKED -- no scout artifact for {topic}. Run scout first."
3. Set scout_source = path of found file (most recent if multiple). Read it.
4. Emit: SCOUT CONFIRMED. scout_source = [path]

Stage 1 is blocked until SCOUT CONFIRMED is emitted.

---

## STAGE 1 -- HYPOTHESIS

GATE: SCOUT CONFIRMED emitted? If not: BLOCKED at Stage 1. Halt.

Read scout_source. Frame the hypothesis for {topic} grounded in the scout findings.

The artifact body must include a CLAIM INDEX -- 3 to 5 numbered sub-claims:
  CLAIM-1: [one-sentence falsifiable claim]
  CLAIM-2: [one-sentence falsifiable claim]
  CLAIM-3: [one-sentence falsifiable claim]
  (add CLAIM-4 and CLAIM-5 if needed)

Each claim is one sentence. Each must be testable by evidence. These CLAIM-IDs will
be referenced in THIN flags at Stages 2 and 3 and in the synthesis table at Stage 5.

Reference scout_source in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [path from SETUP]

---

## STAGE 2 -- WEBSEARCH

Precondition: Stage 1 artifact written and CLAIM INDEX defined.

Gather external evidence for each claim in the CLAIM INDEX. For each source, assess
strength of evidence. When evidence is thin, conflicting, or absent for a specific
claim, flag immediately at point of discovery using the claim ID:
  THIN: [area] -- [gap] -- weakens: CLAIM-N

Do not defer THIN flags to synthesis.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 -- INTELLIGENCE

Precondition: Stage 2 artifact written.

Search internal sources -- existing signal artifacts, related topics -- for evidence
relevant to each claim. Apply the same THIN flag format:
  THIN: [area] -- [gap] -- weakens: CLAIM-N

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 -- ANALYSIS

Precondition: Stage 3 artifact written.

Aggregate all THIN flags from Stages 2 and 3:

| Flag    | Source Stage | Area | Gap | Claim Weakened |
|---------|-------------|------|-----|----------------|
| THIN-01 | S2          | ...  | ... | CLAIM-N        |

If no THIN flags: one row -- "no THIN flags found across Stages 2-3".

For each claim in the CLAIM INDEX, assess its evidence status:
  SUPPORTED / WEAKENED (has THIN flags) / UNSUPPORTED (no positive evidence found)

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 -- SYNTHESIZE

Precondition: Stage 4 artifact written.

State the overall verdict: supported / partially supported / not supported.

PER-CLAIM CONFIDENCE TABLE (one row per claim in the CLAIM INDEX):

| Claim ID | Claim (one sentence) | Source Stage of THIN Flags | Adjusted Confidence |
|----------|----------------------|---------------------------|---------------------|
| CLAIM-1  | ...                  | S2 / S3 / none            | Low / Med / High    |
| CLAIM-2  | ...                  | ...                       | ...                 |
| CLAIM-3  | ...                  | ...                       | ...                 |

Rules:
- Source Stage column must match the THIN flag origin from Stage 4's aggregation table.
- Any claim with one or more THIN flags: confidence = Low or Med (not High) unless
  Stage 4 analysis explicitly justifies the higher rating with a specific evidence item.
- If a claim has no THIN flags: confidence = High.

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-03 -- inline_weakens_annotation

**Axis**: inline_weakens_annotation
**Hypothesis**: Requiring every THIN flag to carry a "weakens: [claim]" annotation at
the moment of discovery -- "THIN: [area] -- [gap] -- weakens: [exact claim text]" --
eliminates any retrospective mapping step at synthesis. The synthesis simply collects
all THIN lines with their "weakens:" fields and adds a confidence column. The claim
reference is embedded in the original flag, so the synthesis table cannot substitute
a category for a specific claim. This is structurally simpler than a CLAIM INDEX
(V-02) because it requires no pre-committed claim IDs.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five evidence stages in strict
forward sequence. One artifact written per stage. Final output: evidence brief
ready for /topic-story.

Stages: hypothesis -> websearch -> intelligence -> analysis -> synthesize

---

## SETUP -- Scout Check

1. Glob `simulations/scout/{topic}-scout-*.md`.
2. If no file found: emit BLOCKED. No scout artifact for `{topic}`. Run scout first. Halt.
3. Set scout_source = full path of found file (most recent if multiple). Read it.
4. Emit: SCOUT CONFIRMED. scout_source = [full path]

Stage 1 cannot begin until SCOUT CONFIRMED is emitted with scout_source named.

---

## STAGE 1 -- HYPOTHESIS

GATE CHECK: SCOUT CONFIRMED received with scout_source named?
If not: BLOCKED at Stage 1. Halt.

Load scout_source. Frame the central testable hypothesis for {topic}, grounded in
the scout findings. Reference scout_source explicitly in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [full path from SETUP]

---

## STAGE 2 -- WEBSEARCH

Precondition: Stage 1 artifact written.

Gather external evidence for the hypothesis. Assess each source. When evidence is
thin, conflicting, or absent for any hypothesis claim, flag at point of discovery
using this exact format:
  THIN: [area] -- [gap] -- weakens: "[exact claim from the Stage 1 hypothesis]"

The "weakens:" field must name the specific hypothesis claim being undermined.
Do not write a category. Do not defer this flag to synthesis.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

---

## STAGE 3 -- INTELLIGENCE

Precondition: Stage 2 artifact written.

Search internal sources -- existing signal artifacts, related topic runs -- for
evidence relevant to the hypothesis. Apply the same THIN annotation format:
  THIN: [area] -- [gap] -- weakens: "[exact claim from Stage 1 hypothesis]"

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

---

## STAGE 4 -- ANALYSIS

Precondition: Stage 3 artifact written.

Collect all THIN flags emitted during Stages 2 and 3. For each flag, the "weakens:"
field already names the specific claim. Assess the overall evidence case for the
hypothesis given these gaps.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

---

## STAGE 5 -- SYNTHESIZE

Precondition: Stage 4 artifact written.

State the verdict: supported / partially supported / not supported.

CLAIM CONFIDENCE TABLE (required -- one row per THIN flag from Stages 2 and 3):

| Source Stage | Gap | Hypothesis Claim Weakened | Adjusted Confidence |
|-------------|-----|---------------------------|---------------------|
| S2 / S3     | ... | [copy from "weakens:" field in the original THIN flag] | Low / Med / High |

Rules:
- "Hypothesis Claim Weakened" must be copied from the "weakens:" field verbatim or
  as a direct paraphrase. It must identify the specific claim, not a category.
- "Source Stage" must match where the THIN flag was emitted.
- If no THIN flags were emitted: one row -- "none | none | no thin findings | full confidence".

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-04 -- named_claims + inline_weakens (combined)

**Axis**: named_hypothesis_claims + inline_weakens_annotation
**Hypothesis**: Combining a CLAIM INDEX (V-02) with inline "weakens: CLAIM-N" annotation
(V-03) creates the tightest possible traceability chain: claim IDs are committed at Stage 1,
THIN flags reference them by ID at discovery, the synthesis per-claim table closes the loop
by claim ID with source stage. The claim ID makes the reference unambiguous (no paraphrase
drift), and the inline annotation eliminates any retrospective mapping. Together they achieve
C-08 and C-09 full pass with the minimum possible instruction surface.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages in forward sequence.
One artifact per stage. Final output: evidence brief ready for /topic-story.

---

## ARTIFACT PATHS

| Stage | Signal             | Full path                                                                      |
|-------|--------------------|--------------------------------------------------------------------------------|
| 1     | prove-hypothesis   | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md          |
| 2     | prove-websearch    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md            |
| 3     | prove-intelligence | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md      |
| 4     | prove-analysis     | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md              |
| 5     | prove-synthesize   | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md          |

Each WRITE instruction must echo the exact path from this table.

---

## SETUP -- Scout Gate

1. Glob `simulations/scout/{topic}-scout-*.md`.
2. If absent: BLOCKED. Emit "No scout artifact for {topic}. Run scout first." Halt.
3. Set scout_source = full path of found file. Read it.
4. Emit: SCOUT GATE CLEARED. scout_source = [path]

Stage 1 entry is blocked until SCOUT GATE CLEARED fires.

---

## STAGE 1 -- HYPOTHESIS

GATE: SCOUT GATE CLEARED received? If not: BLOCKED. Halt.

Read scout_source. Frame the hypothesis for {topic} grounded in scout findings.

The artifact body must include a CLAIM INDEX:
  CLAIM-1: [one-sentence falsifiable sub-claim]
  CLAIM-2: [one-sentence falsifiable sub-claim]
  CLAIM-3: [one-sentence falsifiable sub-claim]
  (add CLAIM-4, CLAIM-5 if needed; 3-5 claims total)

Reference scout_source in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [path from SETUP -- copied verbatim, not inferred]

Emit: STAGE-1 CLEARED.

---

## STAGE 2 -- WEBSEARCH

Precondition: STAGE-1 CLEARED emitted.

Gather external evidence for each claim in the CLAIM INDEX. When evidence is thin,
conflicting, or absent for a claim, flag immediately at point of discovery:
  THIN: [area] -- [gap] -- weakens: CLAIM-N

Use the exact CLAIM-N ID from the Stage 1 CLAIM INDEX. Do not defer.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: STAGE-2 CLEARED.

---

## STAGE 3 -- INTELLIGENCE

Precondition: STAGE-2 CLEARED emitted.

Search internal sources for evidence relevant to each claim. Same THIN format:
  THIN: [area] -- [gap] -- weakens: CLAIM-N

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: STAGE-3 CLEARED.

---

## STAGE 4 -- ANALYSIS

Precondition: STAGE-3 CLEARED emitted.

Aggregate all THIN flags from Stages 2 and 3:

| Flag    | Source Stage | Area | Gap | Claim Weakened |
|---------|-------------|------|-----|----------------|
| THIN-01 | S2          | ...  | ... | CLAIM-N        |

If no THIN flags: one row -- "no THIN flags found".

Assess each claim's evidence status: SUPPORTED / WEAKENED / UNSUPPORTED.

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: STAGE-4 CLEARED.

---

## STAGE 5 -- SYNTHESIZE

Precondition: STAGE-4 CLEARED emitted.

State the overall verdict: supported / partially supported / not supported.

PER-CLAIM CONFIDENCE TABLE (one row per claim in the CLAIM INDEX):

| Claim ID | Claim (one sentence) | Source Stage of THIN Flags | Adjusted Confidence |
|----------|----------------------|---------------------------|---------------------|
| CLAIM-1  | ...                  | S2 / S3 / none            | Low / Med / High    |

Rules:
- Source Stage must match the THIN flag origin in Stage 4's aggregation table.
- Claims with one or more THIN flags: confidence = Low unless Stage 4 analysis
  provides specific positive evidence that justifies Med.
- Claims with no THIN flags: confidence = High.

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## V-05 -- Full Integration (all three axes + structural gate + full paths)

**Axis**: per_claim_synthesis_table + named_hypothesis_claims + inline_weakens_annotation
**Structural baseline**: gate + scout blocking + full paths + per-stage gate emits

**Hypothesis**: Combining named claims (V-02), inline weakens annotation (V-03), and
a required per-claim confidence table (V-01) with a structural scout gate and full
artifact path declarations achieves 100 on v14 with a substantially simpler prompt
than R11 V-05. No conviction ladder, no HANDOFF-exclusive synthesis, no four-ceiling
ordering, no falsification gate. The minimum needed for all 10 criteria: (1) scout
blocking gate before Stage 1; (2) per-stage gate emits chaining each stage to the
next; (3) CLAIM INDEX at Stage 1; (4) THIN flags with inline "weakens: CLAIM-N";
(5) per-claim synthesis table sourced from Stage 4 aggregation.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for {topic}. Five stages in strict forward
sequence. One artifact written per stage. Final output: evidence brief ready for
/topic-story.

Stages: hypothesis -> websearch -> intelligence -> analysis -> synthesize

---

## ARTIFACT PATH TABLE (declared at campaign open; each WRITE echoes the exact path)

| Stage | Signal             | Full path                                                                      |
|-------|--------------------|--------------------------------------------------------------------------------|
| 1     | prove-hypothesis   | simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md          |
| 2     | prove-websearch    | simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md            |
| 3     | prove-intelligence | simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md      |
| 4     | prove-analysis     | simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md              |
| 5     | prove-synthesize   | simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md          |

---

## SETUP -- Scout Gate

1. Glob `simulations/scout/{topic}-scout-*.md`.
2. If no file found:
   Emit: BLOCKED. No scout artifact for `{topic}`. Run a scout skill first. Halt.
3. Set scout_source = full path of found file (most recent if multiple). Read it.
4. Emit:
   SCOUT GATE CLEARED.
   scout_source: [full path]

Stage 1 is structurally blocked until SCOUT GATE CLEARED is emitted with
scout_source named.

---

## STAGE 1 -- HYPOTHESIS

GATE CHECK:
  [ ] SCOUT GATE CLEARED emitted.
  [ ] scout_source named.
  If either missing: BLOCKED at Stage 1. Halt.

Load scout_source. Frame the hypothesis for {topic} grounded in the scout findings.

The artifact body must include:

1. MAIN CLAIM: one falsifiable sentence about {topic}.
2. CLAIM INDEX:
   CLAIM-1: [sub-claim -- one sentence, testable by evidence]
   CLAIM-2: [sub-claim -- one sentence, testable by evidence]
   CLAIM-3: [sub-claim -- one sentence, testable by evidence]
   (3-5 claims total)
   THIN flags at Stages 2 and 3 must reference these IDs.

Reference scout_source explicitly in the artifact body.

WRITE: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md

Required frontmatter:
  scout_source: [full path from SETUP -- copied verbatim, not inferred]

Emit: STAGE-1 CLEARED.

---

## STAGE 2 -- WEBSEARCH

GATE CHECK: STAGE-1 CLEARED emitted? If not: BLOCKED. Halt.

Gather external evidence for each claim in the CLAIM INDEX. For each source, assess
strength of evidence. When evidence is thin, conflicting, or absent for any claim,
flag immediately at point of discovery using the CLAIM-N ID:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

Do not defer. Emit the THIN flag where the gap is found.

WRITE: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md

Emit: STAGE-2 CLEARED.

---

## STAGE 3 -- INTELLIGENCE

GATE CHECK: STAGE-2 CLEARED emitted? If not: BLOCKED. Halt.

Search internal sources -- existing signal artifacts, related topics, prior runs --
for evidence relevant to each claim. Apply the same THIN annotation:

  THIN: [area] -- [gap] -- weakens: CLAIM-N

WRITE: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md

Emit: STAGE-3 CLEARED.

---

## STAGE 4 -- ANALYSIS

GATE CHECK: STAGE-3 CLEARED emitted? If not: BLOCKED. Halt.

Aggregate all THIN flags from Stages 2 and 3 into a CLAIM IMPACT TABLE:

| Flag    | Source Stage | Area | Gap | Claim Weakened |
|---------|-------------|------|-----|----------------|
| THIN-01 | S2          | ...  | ... | CLAIM-N        |

If no THIN flags: one row -- "no THIN flags found across Stages 2-3".

For each claim in the CLAIM INDEX, state evidence status:
  SUPPORTED / WEAKENED (has one or more THIN flags) / UNSUPPORTED

WRITE: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md

Emit: STAGE-4 CLEARED.

---

## STAGE 5 -- SYNTHESIZE

GATE CHECK: STAGE-4 CLEARED emitted? If not: BLOCKED. Halt.

State the overall verdict: supported / partially supported / not supported.

PER-CLAIM CONFIDENCE TABLE (required -- one row per claim in the CLAIM INDEX):

| Claim ID | Claim (one sentence) | Source Stage of THIN Flags | Gap | Adjusted Confidence |
|----------|----------------------|---------------------------|-----|---------------------|
| CLAIM-1  | ...                  | S2 / S3 / none            | ... | Low / Med / High    |
| CLAIM-2  | ...                  | ...                       | ... | ...                 |
| CLAIM-3  | ...                  | ...                       | ... | ...                 |

Rules:
- Source Stage must match the origin in Stage 4's CLAIM IMPACT TABLE.
- Gap must restate the Stage 4 gap text for that claim -- not a new assessment.
- Claims with one or more THIN flags: confidence = Low (or Med if Stage 4 analysis
  provides specific positive evidence justifying the upgrade).
- Claims with no THIN flags: confidence = High.

State overall verdict and confidence in one sentence.

Close with: Evidence brief for {topic} is ready for /topic-story.

WRITE: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
```

---

## Scoring Prediction

Axis comparison against rubric v14:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 all five in sequence | PASS | PASS | PASS | PASS | PASS |
| C-02 scout named before hypothesis | PASS | PASS | PASS | PASS | PASS |
| C-03 one write per stage | PASS | PASS | PASS | PASS | PASS |
| C-04 synthesis names topic-story | PASS | PASS | PASS | PASS | PASS |
| C-05 full paths on every write | PASS | PASS | PASS | PASS | PASS |
| C-06 forward-only with scout gate | PASS | PASS | PASS | PASS | PASS |
| C-07 scout anchor in hypothesis artifact | PASS | PASS | PASS | PASS | PASS |
| C-08 evidence gaps flagged at discovery | PASS | PASS | PASS | PASS | PASS |
| C-09 thin-evidence propagates to synthesis | ~PASS | PASS | PASS | PASS | PASS |
| C-10 hypothesis structurally blocked | PASS | PASS | PASS | PASS | PASS |

**V-01 C-09 note**: Without a CLAIM INDEX, the "Specific Claim Weakened" column depends
on the executor quoting the exact hypothesis claim rather than a category. The instruction
"must name the exact hypothesis claim, not a category" is a prose enforcement, not a
structural one. This may be sufficient for a full C-09 PASS, or may yield PARTIAL if
the executor substitutes a category. Expected: ~95-100.

**V-02 through V-05**: CLAIM INDEX + THIN flags with CLAIM-N IDs makes the synthesis
table structurally unambiguous. C-09 full PASS expected for all four.

**R12 thesis validation**: If V-02 through V-05 all score 100, the conviction ladder
from R11 V-05 was over-engineering for rubric v14. The minimum needed for C-09 is a
committed claim index plus inline claim annotation at THIN discovery.
