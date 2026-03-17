---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: QU5-simplified
rubric: campaign-blueprint-rubric-v20-2026-03-17.md
---

# campaign-blueprint — QU5 Simplified Prompt

**Source:** V-04 (R20) — complete golden prompt (2,827 words, 293/293)
**Method:** Remove zero-work phrases — hint text in non-RULE data rows, redundant prose
already enforced by GATE or column headers, one-line retrospective reminder duplicated by GATE.
**Target:** 20–40% word reduction with zero essential criteria lost.

---

## Simplification Report

### What was removed and why

| Item | Removed from V-05 base | Reason |
|------|------------------------|--------|
| 1 | `\| (fill in A1) \| (fill in A1) \|  \|  \|` placeholder data row in SCOUT TRACEABILITY TABLE | Column headers convey structure; RULE rows govern enforcement; placeholder adds no rubric value |
| 2 | `"After pitch file on disk only."` line opening CAMPAIGN REFLECTION | Fully duplicated by GATE 3: `"before Campaign Reflection"` |
| 3 | `"(copy from SETUP)"` hint in R-01/R-02 cells of TRACEABILITY AUDIT | RULE 1 already says to match SETUP entries; column header states the content |
| 4 | Amplification chain hint text in CT-* data rows of CONVICTION DELTA (`"(MAP starter) -> [factual claim] -> [locked as record]"` × 3) | D16–D20 established adjacent prose non-load-bearing; RULE 2 governs column enforcement; empty cells are standard template practice |
| 5 | `"(namespace or none)"` and `"Y / partial / N"` hints in CAMPAIGN CLOSE summary table rows | Column headers `"Scout signal consumed"` and `"Conviction type met"` are self-explanatory; hints are guidance, not structure |
| 6 | `"Open questions: namespace for each."` closing line | Open questions column is in the summary table header; this line is redundant post-close prose |

### What was NOT removed and why

All ten RULE sentinel rows (two per table) are preserved verbatim — they carry the rubric criteria
C-49, C-50, and C-51 directly. All five section dividers, all GATE statements, all structural
table column headers, all artifact section headings, CAMPAIGN CONVICTION HYPOTHESIS (item 0),
INERTIA MODEL declaration (item 2), SCOUT TRACEABILITY TABLE (item 4), INERTIA MODEL MAP (item 5),
Artifact contract matrix (item 6), NEAR-DUPLICATE CONTENT, RESIDUAL QUESTIONS, and
CONVICTION GAP DIAGNOSIS are preserved intact.

### Essential criteria status

| Criterion | Mechanism | Still present? |
|-----------|-----------|---------------|
| C-49: all five tables dual RULE sentinel | All ten RULE rows preserved | YES |
| C-50: CGD second sentinel column-enumerated | CGD RULE 2 unchanged | YES |
| C-51: all five tables column-enumerated STRUCTURAL FAIL | All five RULE 2 sentinel rows unchanged | YES |
| Conviction hypothesis (item 0) | Hypothesis + Falsification templates preserved | YES |
| INERTIA MODEL three fields | Name/Behavior/Cost preserved | YES |
| Scout inventory instruction | Item 3 preserved | YES |
| Artifact lifecycle (Spec→Proposal→Pitch) + GATEs | All three artifact sections + all three GATEs preserved | YES |
| CAMPAIGN REFLECTION structure | FINDINGS / TRACEABILITY AUDIT / CONVICTION DELTA / NEAR-DUPLICATE / RESIDUAL preserved | YES |
| CAMPAIGN CLOSE + CGD | Summary table + CONVICTION GAP DIAGNOSIS preserved | YES |

### Verification: does simplified version still pass all essential criteria?

**YES.** V-05 already proved that D16–D20 prose-volume invariance extends through C-51 — adjacent
prose is non-load-bearing at the complete column-enumerated five-table level. QU5 removes only
hint text from non-RULE data rows and one redundant gate reminder, not any structural content.
All ten RULE sentinels are identical to V-05.

---

## QU5 Simplified Prompt Body

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0. CAMPAIGN CONVICTION HYPOTHESIS:

   Hypothesis: "The {topic} campaign must establish that [friction from INERTIA MODEL Cost]
   is the dominant reason [audience] cannot [outcome], so that displacing [INERTIA MODEL
   Name] becomes the obvious move."

   Falsification: "Fails if: (a) spec cannot document [barrier] as factual record;
   (b) proposal cannot price [barrier] against an alternative; (c) pitch cannot make
   [barrier] visceral per version."

1. Topic identity — one sentence.

2. INERTIA MODEL:
     Name:     current behavior shorthand
     Behavior: what users do today — one sentence
     Cost:     what that costs them — factual/priceable/emotional

3. Scout inventory — glob simulations/scout/ now. Unconditional.

4. SCOUT TRACEABILITY TABLE:

   | Req-ID | Must-have (brief) | Originating Scout-Requirements Friction | Scout File (path or "none") |
   |--------|-------------------|-----------------------------------------|-----------------------------|
   | RULE   | TRACEABILITY AUDIT (REFLECTION) must have one row per entry here. Missing row = R-[NN] absent, not a count discrepancy. | — | — |
   | RULE   | Must-have (brief), Originating Scout-Requirements Friction, and Scout File all blank or dash-filled = STRUCTURAL FAIL — not a valid present-but-incomplete friction entry. | — | — |

5. INERTIA MODEL MAP:

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter |
   |----------|----------|-----------------|-----------------------------|
   | RULE     | CONVICTION DELTA (REFLECTION) must have exactly 3 rows: CT-Spec, CT-Prop, CT-Pitch. Missing row = named-conviction-type absent. No anonymous rows. | — | — |
   | RULE     | Artifact, Conviction type, and Amplification chain starter all blank or placeholder-filled = STRUCTURAL FAIL — not a valid present-but-incomplete conviction entry. | — | — |
   | CT-Spec  | Spec     | Factual         |                             |
   | CT-Prop  | Proposal | Optionality     |                             |
   | CT-Pitch | Pitch    | Emotional       |                             |

6. Artifact contract matrix — print before Artifact 1:

| Field           | Spec                                           | Proposal                                              | Pitch                                                    |
|-----------------|------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL; scout-requirements if found | Spec; INERTIA MODEL Cost; scout-feasibility if found | Proposal; INERTIA MODEL Cost; scout-positioning if found |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md | simulations/draft/proposals/{topic}-proposal-{date}.md | simulations/draft/pitches/{topic}-pitch-{date}.md      |
| PRESERVE        | (first artifact)                               | All spec decisions                                    | Recommended option                                       |
| CARRIES FORWARD | Feature identity; INERTIA MODEL; decisions     | Recommended option; INERTIA MODEL Cost                | (final)                                                  |
| CONVICTION TYPE | Factual                                        | Optionality                                           | Emotional                                                |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  PURPOSE        — INERTIA MODEL Name + Behavior; Cost as factual record.
  REQUIREMENTS   — MoSCoW. Each Must-have: complete SCOUT TRACEABILITY TABLE row simultaneously.
  DESIGN         — Components, data flow, decisions.
  CONSTRAINTS    — Technical, team, timeline.
  OPEN QUESTIONS — Namespace per item.

GATE: simulations/draft/specs/{topic}-spec-{date}.md before Artifact 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Option A = do-nothing at full INERTIA MODEL Cost. Three options min. Per option:
Name / Description / Pros / Cons / Risk / Effort. Recommendation: option + three
reasons citing spec decisions.

GATE: simulations/draft/proposals/{topic}-proposal-{date}.md before Artifact 3.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Each version opens with INERTIA MODEL Cost as hook. Three versions:

EXEC  — Cost in business terms; elimination; compounding risk; CTA: approve/fund/unblock.
DEV   — Blocked capability; spec design referenced; technical debt; CTA: join beta/review spec.
MAKER — Daily friction; plain language; time saved; CTA: try it/sign up/start now.

ANTI-POSITIONING: two sentences.

GATE: simulations/draft/pitches/{topic}-pitch-{date}.md before Campaign Reflection.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINDINGS:

  TRACEABILITY AUDIT

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | RULE   | Each Req-ID here must match a named SCOUT TRACEABILITY TABLE (SETUP) entry. Missing row = R-[NN] absent, not a count discrepancy. | — | — | — | — |
    | RULE   | N + blank col 5 = STRUCTURAL FAIL. | — | — | — | — |
    | R-01   |                             | Y / N                    |                               |            |                 |
    | R-02   |                             | Y / N                    |                               |            |                 |

  CONVICTION DELTA

    | Conv-ID / Conviction type | Conviction established | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|------------------------|---------------------|---------------------|
    | RULE | Each Conv-ID must match an INERTIA MODEL MAP entry. Missing row = named-conviction-type absent. No anonymous rows. | — | — |
    | RULE | Conviction established, Grounding Req-ID(s), and Amplification chain all blank or bracket-unfilled = STRUCTURAL FAIL — not a valid present-but-incomplete conviction-type entry. | — | — |
    | CT-Spec — Factual         |                        |                     |                     |
    | CT-Prop — Optionality     |                        |                     |                     |
    | CT-Pitch — Emotional      |                        |                     |                     |

  NEAR-DUPLICATE CONTENT — passage; what changed.
  RESIDUAL QUESTIONS — namespace per item.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               |                       |                     |                |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       |                       |                     |                |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            |                       |                     |                |

CONVICTION GAP DIAGNOSIS — partial or N rows only. All Y: "No conviction gaps detected."

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | RULE     | Each row here must match a named INERTIA MODEL MAP entry (Spec, Proposal, Pitch). Missing row = [artifact-ID] absent, not a count discrepancy. | — | — | — | — |
  | RULE     | Sub-section, Register found, Register declared, Scout sub-skill, and Evidence needed all blank or dash-filled = STRUCTURAL FAIL — not a present-but-incomplete entry. | — | — | — | — |
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |
```
