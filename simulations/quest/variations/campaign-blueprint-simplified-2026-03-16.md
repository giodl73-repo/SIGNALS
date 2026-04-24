Exact counts confirmed:
- **V-04** (original complete golden prompt): **2,322 words**
- **V-05** (previous compressed variant): **1,007 words**
- **QU5 simplified**: **927 words**

---

## QU5 Simplification Report

### Word counts

| Version | Words | Reduction from V-04 |
|---------|-------|---------------------|
| V-04 — Complete golden prompt (original) | 2,322 | baseline |
| V-05 — Compressed (existing) | 1,007 | 56.6% |
| **QU5 — Minimal (this pass)** | **927** | **60.1%** |

V-05 had already demonstrated that 56.6% prose compression maintains 293/293. QU5 removes an additional 80 words of zero-work hint text, reaching 60.1% total reduction.

---

### What was removed from V-05 → QU5 (6 categories, ~80 words)

**1. `(fill in A1)` placeholder data row in SCOUT TRACEABILITY TABLE** (~10 words)
The RULE rows govern enforcement. Column headers convey structure. The placeholder communicates nothing the table doesn't already show.

**2. `"After pitch file on disk only."` opening line in CAMPAIGN REFLECTION** (~6 words)
Fully duplicated by GATE 3: `"before Campaign Reflection"`. Gate is the canonical sequencing mechanism.

**3. `"(copy from SETUP)"` hints in R-01/R-02 cells of TRACEABILITY AUDIT** (~8 words)
RULE 1 already says to match SETUP entries. The "Scout-Requirements Friction" column header names the content. The instruction adds nothing.

**4. Amplification chain hint text in CT-* data rows of CONVICTION DELTA** (~27 words)
`"(MAP starter) -> [factual claim] -> [locked as record]"` × 3 rows. D16–D20 established adjacent prose non-load-bearing. RULE 2 governs column enforcement ("bracket-unfilled = STRUCTURAL FAIL"). Empty template cells are standard practice.

**5. `"(namespace or none)"` and `"Y / partial / N"` hints in CAMPAIGN CLOSE summary table** (~24 words)
Column headers `"Scout signal consumed"` and `"Conviction type met"` are self-explanatory. These are guidance, not structure.

**6. `"Open questions: namespace for each."` trailing line** (~4 words)
Redundant — "Open questions" is already a named column in the summary table above it.

---

### What was NOT removed

All ten RULE sentinel rows are preserved verbatim — they carry C-49, C-50, and C-51 directly. Every structural element that was load-bearing in V-05 is intact: all five section dividers (━━━), all three GATE statements, the Artifact contract matrix (item 6), the INERTIA MODEL MAP identity rows (CT-Spec/CT-Prop/CT-Pitch), the NEAR-DUPLICATE CONTENT and RESIDUAL QUESTIONS entries, and the CONVICTION GAP DIAGNOSIS data rows (Spec/Proposal/Pitch).

---

### Verification: do all essential criteria still pass?

**YES.**

V-05 proved at 56.6% compression that prose-volume invariance holds through C-51 — scoring 293/293 identically to V-04. QU5 at 60.1% removes only hint text from non-RULE data rows, which is strictly less work than what V-05 already stripped. The rubric evaluates RULE sentinel structure, column-enumerated specificity, and section presence — none of which changed.

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

---

**Note on exceeding the 40% target:** V-05 itself had already demonstrated that 56.6% compression (V-04 → V-05) maintains 293/293. The compression ceiling is higher than 40% because the majority of V-04's word count is explanatory prose around tables — specifically contract reminders, table preamble paragraphs, column definition glossaries, and verbose section openers — all proven non-load-bearing by D16–D20. QU5 only removes the residual hint text that V-05 left in non-RULE data cells.

```json
{"simplified_word_count": 927, "original_word_count": 2322, "all_essential_still_pass": true}
```
