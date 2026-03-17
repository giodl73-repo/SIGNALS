---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 19
rubric: campaign-blueprint-rubric-v19-2026-03-17.md
---

# campaign-blueprint — Prompt Variations R19

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04 through V-05).

## R19 Context

R18 variants under v19 retroactive scoring:

| Variant | v18 | C-48 | C-49 | v19 |
|---------|-----|------|------|-----|
| V-01 — Four-Sentinel Control | 263 | 0 | 0 | **263** |
| V-02 — Minimum Five-Sentinel Form | 273 | 0 | 0 | **273** |
| V-03 — Conversational Register | 273 | 0 | 0 | **273** |
| V-04 — Maximum-Density Five-Sentinel | 273 | 0 | 0 | **273** |
| V-05 — Prose-Compressed Five-Sentinel | 273 | 0 | 0 | **273** |

No R18 variant earns C-48 or C-49. All V-02 through V-05 variants carry the CONVICTION
GAP DIAGNOSIS as a 6-column structural table in CAMPAIGN CLOSE with a single in-table
RULE sentinel row declaring the identifier-to-MAP-entry binding and named-artifact absence
(C-46 FULL). The table satisfies the first sentinel requirement — structural linkage
self-enforcement at the presence level — without the second sentinel requirement:
enforcement at the completeness level (an artifact row with all substantive cells blank
or dash-filled is a STRUCTURAL FAIL, not a present-but-incomplete entry).

The dual-sentinel upgrade chain for CONVICTION GAP DIAGNOSIS:
  C-35 FULL: 6-column table, pre-declared artifact rows, register-split columns —
             ontological at cell level
  C-46 FULL: C-35 FULL + first in-table RULE sentinel: identifier-to-MAP-entry binding
             + named-artifact-absence rule — self-enforcing at structural linkage level
  C-48 FULL: C-46 FULL + second in-table RULE sentinel: N+blank STRUCTURAL FAIL rule —
             self-enforcing at both presence and completeness levels simultaneously

The full five-table dual-sentinel upgrade chain for C-49:
  C-47 FULL: all five structural tables carry at least one in-table RULE sentinel
  C-48 FULL: CONVICTION GAP DIAGNOSIS carries dual in-table RULE sentinels
  C-49 FULL: all five structural tables carry dual in-table RULE sentinels simultaneously
             (MAP dual + CONVICTION DELTA dual + SCOUT TRACEABILITY TABLE dual +
             TRACEABILITY AUDIT dual [C-45, confirmed R17] + CONVICTION GAP DIAGNOSIS dual)

The only path to 278 runs through C-48:

  Base 273 (v18 ceiling, V-02 through V-05 R18)
  + C-48: second in-table RULE sentinel inside CONVICTION GAP DIAGNOSIS (N+blank STRUCTURAL FAIL) → +5
  = **278**

The only path to 283 requires C-49 in addition:

  Base 278 (C-48 ceiling)
  + C-49: all five structural tables dual-sentinel simultaneously                        → +5
  = **283**

C-49 is a strict superset of C-48. It passes only if C-48 FULL, and additionally
requires MAP, CONVICTION DELTA, and SCOUT TRACEABILITY TABLE each carry a second
in-table RULE sentinel row (N+blank STRUCTURAL FAIL enforcement), matching the dual
architecture TRACEABILITY AUDIT already carries (C-45, R17) and CONVICTION GAP DIAGNOSIS
carries under C-48.

**R19 design questions:**

1. **Five-sentinel single-CGD control (V-01):** R18 V-02 reproduced exactly — all five
   tables with single RULE sentinels. CONVICTION GAP DIAGNOSIS carries the first RULE
   sentinel (C-46 FULL) but no second. Does V-01 score 273 and earn C-48 NO CREDIT?
   Expected: 273.

2. **Minimum CGD dual-sentinel (V-02):** R18 V-02 form + second RULE sentinel row
   inside CONVICTION GAP DIAGNOSIS, minimum text: an artifact row with all substantive
   analysis cells blank or dash-filled = STRUCTURAL FAIL. MAP, CONVICTION DELTA, and
   SCOUT TRACEABILITY TABLE remain single-sentinel. Does V-02 earn C-48 FULL and
   C-49 NO CREDIT? Expected: 278.

3. **Conversational CGD dual-sentinel (V-03):** V-02 structural tables unchanged; the
   second CONVICTION GAP DIAGNOSIS RULE sentinel phrased in conversational register.
   Tests whether register affects C-48 verdict (D18 extended to second-sentinel axis).
   Expected: 278.

4. **Complete five-table dual-sentinel, maximum density (V-04):** All five structural
   tables carry dual RULE sentinels. MAP, CONVICTION DELTA, and SCOUT TRACEABILITY TABLE
   each gain a second RULE sentinel declaring the N+blank STRUCTURAL FAIL rule.
   CONVICTION GAP DIAGNOSIS gains a second RULE sentinel (C-48). Maximum prose density
   throughout. Does V-04 earn C-48 FULL and C-49 FULL? Expected: 283.

5. **Complete five-table dual-sentinel, compressed (V-05):** All five structural tables
   dual-sentinel; surrounding prose stripped to minimum viable form. Tests whether
   adjacent prose volume is load-bearing at the 283-ceiling level. Expected: 283.

**Predicted scoring pattern:**

| Variant | Axis | C-46 | C-47 | C-48 | C-49 | v19 |
|---------|------|------|------|------|------|-----|
| V-01 — Five-Sentinel Control | Lifecycle (dual-sentinel isolation) | FULL | FULL | NO | NO | **273** |
| V-02 — Minimum CGD Dual-Sentinel | Output format (minimum second RULE text) | FULL | FULL | FULL | NO | **278** |
| V-03 — Conversational CGD Dual-Sentinel | Phrasing register | FULL | FULL | FULL | NO | **278** |
| V-04 — Complete Five-Table Dual-Sentinel | Lifecycle emphasis (maximum density) | FULL | FULL | FULL | FULL | **283** |
| V-05 — Compressed Five-Table Dual-Sentinel | Lifecycle compression (minimum prose) | FULL | FULL | FULL | FULL | **283** |

V-01 is the diagnostic control: confirms five single-sentinel tables do not earn C-48 or C-49.
V-02 and V-03 target 278 by adding the second CGD sentinel only.
V-04 and V-05 target 283 by adding dual sentinels to all five tables simultaneously.

---

## V-01 — Five-Sentinel Control

**Axis:** Lifecycle emphasis — single-axis isolation. R18 V-02 reproduced exactly. All
five structural tables carry a single in-table RULE sentinel row (C-42 MAP, C-43 CONVICTION
DELTA, C-44 SCOUT TRACEABILITY TABLE, C-45 dual TRACEABILITY AUDIT, C-46 CONVICTION GAP
DIAGNOSIS). The CONVICTION GAP DIAGNOSIS carries its first RULE sentinel (C-46 FULL) but
no second RULE sentinel row declaring the N+blank STRUCTURAL FAIL rule.

**Hypothesis:** C-48 requires a second non-data RULE sentinel row inside the CONVICTION
GAP DIAGNOSIS, positioned before artifact data rows, whose text embeds the N+blank
STRUCTURAL FAIL rule: an artifact row with all substantive analysis cells blank or
populated exclusively with structural placeholders = STRUCTURAL FAIL, not a
present-but-incomplete entry. V-01 does not supply this second row. C-46 FULL; C-48
NO CREDIT; C-49 NO CREDIT (strict superset of C-48). Score: 273.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent. Fill all SETUP tables
before Artifact 1. No SETUP field may be deferred to REFLECTION.

0. CAMPAIGN CONVICTION HYPOTHESIS — two required items, completed before item 1:

   Hypothesis: "The {topic} campaign must establish that [specific friction from INERTIA
   MODEL Cost] is the dominant reason [audience] cannot [achieve desired outcome], so that
   displacing [INERTIA MODEL Name] becomes the obvious move."

   Falsification conditions: "This campaign fails if: (a) spec cannot document [barrier]
   as measured cost with factual record; (b) proposal cannot price [barrier] against an
   alternative; (c) pitch cannot make [barrier] visceral per version."

1. Topic identity — one sentence.

2. INERTIA MODEL:
     Name:     current behavior shorthand
     Behavior: what users do today — one sentence
     Cost:     what that costs them — one sentence, covering factual/priceable/emotional

   Conviction map: Factual->spec documents Cost; Optionality->proposal prices Cost;
   Emotional->pitch makes Cost visceral per audience.

3. Scout inventory — glob simulations/scout/ now. Unconditional.

4. SCOUT TRACEABILITY TABLE — source of truth for TRACEABILITY AUDIT row identifiers.
   Each Req-ID here becomes a named row in REFLECTION.

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | RULE         | TRACEABILITY AUDIT (REFLECTION) must have one row per entry here. Missing row = R-[NN] absent, not a count discrepancy. | — | — |
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (one row per friction; if none: one row, Friction from INERTIA MODEL Cost, file = "none")

5. INERTIA MODEL MAP — source of truth for CONVICTION DELTA row identifiers.

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter                                    |
   |----------|----------|-----------------|----------------------------------------------------------------|
   | RULE     | The CONVICTION DELTA in REFLECTION must contain exactly 3 rows (CT-Spec, CT-Prop, CT-Pitch). A missing row is a named-conviction-type absence. Do not introduce anonymous version rows. | — | — |
   | CT-Spec  | Spec     | Factual         | (fill in: opening factual move for spec's conviction chain)    |
   | CT-Prop  | Proposal | Optionality     | (fill in: opening optionality move for proposal's chain)       |
   | CT-Pitch | Pitch    | Emotional       | (fill in: opening emotional move for pitch's conviction chain) |

6. Artifact contract matrix:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening                                   | Recommended option — crystallize, do not reconsider                                |
| CARRIES FORWARD | Feature identity; INERTIA MODEL; design decisions                | Recommended option + rationale; INERTIA MODEL Cost                          | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — INERTIA MODEL Cost as factual record                   | Optionality — Cost priced against each alternative                          | Emotional — Cost visceral per audience                                             |

Print the matrix. Do not begin Artifact 1 until printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL; scout-requirements if found.
                    PRESERVE: (first artifact). CONVICTION TYPE: Factual.

  PURPOSE        — INERTIA MODEL Name + Behavior; Cost as factual record.
  REQUIREMENTS   — Bulleted, MoSCoW (M/S/C/W). Each Must-have: complete Req-ID + SETUP
                   SCOUT TRACEABILITY TABLE row simultaneously. Every Must-have = one row.
  DESIGN         — Components, data flow, decisions.
  CONSTRAINTS    — Technical, team, timeline, dependencies.
  OPEN QUESTIONS — Unknowns; namespace per item.

GATE: Write simulations/draft/specs/{topic}-spec-{date}.md before Artifact 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec; INERTIA MODEL Cost; scout-feasibility if found.
                    PRESERVE: all spec decisions. CONVICTION TYPE: Optionality.

Option A = do-nothing at full INERTIA MODEL Cost. State Cost before alternatives.
Three options min. Per option: Name / Description / Pros / Cons / Risk / Effort.
Recommendation: option + three reasons citing spec decisions.

GATE: Write simulations/draft/proposals/{topic}-proposal-{date}.md before Artifact 3.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal; INERTIA MODEL Cost; scout-positioning if found.
                    PRESERVE: recommended option. CONVICTION TYPE: Emotional.

Each version opens with INERTIA MODEL Cost as hook. Three versions in full:

EXEC — Cost in business terms; Cost elimination; compounding risk; CTA: approve/fund/unblock.
DEV  — Blocked capability; spec design referenced; technical debt; CTA: join beta/review spec.
MAKER — Daily friction; plain language only; time saved; CTA: try it/sign up/start now.
ANTI-POSITIONING: what this feature is NOT, two sentences.

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md before Campaign Reflection.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After pitch file exists on disk only. Retrospective — completed artifacts only.

FINDINGS:

  TRACEABILITY AUDIT
    One row per SETUP SCOUT TRACEABILITY TABLE row. Copy Req-ID and Friction from SETUP
    now; complete remaining columns after Artifact 1. Row count must match SETUP.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | RULE   | Each Req-ID here must match a named entry in the SCOUT TRACEABILITY TABLE (SETUP). Missing row = R-[NN] absent, not a count discrepancy. | — | — | — | — |
    | RULE   | N in col 3 + blank col 5 = STRUCTURAL FAIL — not an acceptable omission. | — | — | — | — |
    | R-01   | (copy from SETUP row 1)     | Y / N                    |                               |            |                 |
    | R-02   | (copy from SETUP row 2)     | Y / N                    |                               |            |                 |
    (match SETUP row count exactly — do not reduce)

    Must-have found: Y = distinct Must-have in Artifact 1 REQUIREMENTS covers friction.
    Must-have text: verbatim from Artifact 1. Blank if N.
    Gap: if N, state absent requirement. N + blank = STRUCTURAL FAIL per RULE row.
    Scout namespace: specific sub-skill for N rows. Blank if Y.

  CONVICTION DELTA
    Three rows only — CT-Spec, CT-Prop, CT-Pitch from INERTIA MODEL MAP. No anonymous
    version rows. Each row's Amplification chain anchors to the MAP starter for that
    Conv-ID. Replace all bracketed tokens. An unfilled bracket fails the row.

    | Conv-ID / Conviction type | Conviction established (one-sentence claim) | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|---------------------------------------------|---------------------|-----------------------------------------------------|
    | RULE | Each Conv-ID must match an INERTIA MODEL MAP entry. Missing row = named-conviction-type absent. Do not add rows. | — | — |
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec starter]) -> [Req-ID's factual claim from Must-have] -> [how spec locked claim as record] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop starter]) -> [Option A = INERTIA MODEL Cost] -> [how recommendation prices against baseline] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch starter]) -> [Req-ID's claim made visceral] -> [audience register that carried it] |

    No grounding: "GAP — [Req-ID] nearest; does not ground CT-[X] because [reason]."

  NEAR-DUPLICATE CONTENT — passage copied; what changed to make it conviction-bearing.
  RESIDUAL QUESTIONS — scout signal needed; namespace per item.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS — complete partial or N rows. Blank row when partial or N = fail.
All Y: "No conviction gaps detected."

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | RULE     | Each artifact row here must match a named INERTIA MODEL MAP entry. Missing row = [artifact-ID] absent, not a count discrepancy. | — | — | — | — |
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Register found / Register declared: one word each, distinct columns.
  Scout sub-skill: specific identifier (e.g., scout-requirements), not namespace alone.
  Evidence needed: one sentence.

Open questions: namespace for each.
```

---

## V-02 — Minimum CGD Dual-Sentinel

**Axis:** Output format — minimum-text implementation of the second in-table RULE sentinel
row inside CONVICTION GAP DIAGNOSIS. The second RULE sentinel is positioned inside the
CONVICTION GAP DIAGNOSIS table boundary, after the first RULE sentinel and before the
Spec/Proposal/Pitch data rows. Its text declares the N+blank STRUCTURAL FAIL rule at
minimum viable density. MAP, CONVICTION DELTA, and SCOUT TRACEABILITY TABLE retain their
single-sentinel R18 forms. The TRACEABILITY AUDIT retains its dual-sentinel R17 form.

**Hypothesis:** C-48 requires a second non-data RULE sentinel row inside the CONVICTION
GAP DIAGNOSIS table whose cell text embeds the N+blank STRUCTURAL FAIL rule: an artifact
row with all substantive analysis cells blank or dash-filled = STRUCTURAL FAIL, not a
present-but-incomplete entry. V-02 supplies this at minimum text density — the rubric
evaluates structural placement (in-table, after first RULE sentinel, before data rows)
and rule content presence, not directive verbosity. C-48 FULL. C-49 requires all five
tables dual-sentinel; V-02 provides dual sentinels only in TRACEABILITY AUDIT (C-45) and
CONVICTION GAP DIAGNOSIS (C-48) — MAP, CONVICTION DELTA, and SCOUT TRACEABILITY TABLE
remain single-sentinel. C-49 NO CREDIT. Score: 278.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent. Fill all SETUP tables
before Artifact 1. No SETUP field may be deferred to REFLECTION.

0. CAMPAIGN CONVICTION HYPOTHESIS — two required items, completed before item 1:

   Hypothesis: "The {topic} campaign must establish that [specific friction from INERTIA
   MODEL Cost] is the dominant reason [audience] cannot [achieve desired outcome], so that
   displacing [INERTIA MODEL Name] becomes the obvious move."

   Falsification conditions: "This campaign fails if: (a) spec cannot document [barrier]
   as measured cost with factual record; (b) proposal cannot price [barrier] against an
   alternative; (c) pitch cannot make [barrier] visceral per version."

1. Topic identity — one sentence.

2. INERTIA MODEL:
     Name:     current behavior shorthand
     Behavior: what users do today — one sentence
     Cost:     what that costs them — one sentence, covering factual/priceable/emotional

   Conviction map: Factual->spec documents Cost; Optionality->proposal prices Cost;
   Emotional->pitch makes Cost visceral per audience.

3. Scout inventory — glob simulations/scout/ now. Unconditional.

4. SCOUT TRACEABILITY TABLE — source of truth for TRACEABILITY AUDIT row identifiers.
   Each Req-ID here becomes a named row in REFLECTION.

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | RULE         | TRACEABILITY AUDIT (REFLECTION) must have one row per entry here. Missing row = R-[NN] absent, not a count discrepancy. | — | — |
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (one row per friction; if none: one row, Friction from INERTIA MODEL Cost, file = "none")

5. INERTIA MODEL MAP — source of truth for CONVICTION DELTA row identifiers.

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter                                    |
   |----------|----------|-----------------|----------------------------------------------------------------|
   | RULE     | The CONVICTION DELTA in REFLECTION must contain exactly 3 rows (CT-Spec, CT-Prop, CT-Pitch). A missing row is a named-conviction-type absence. Do not introduce anonymous version rows. | — | — |
   | CT-Spec  | Spec     | Factual         | (fill in: opening factual move for spec's conviction chain)    |
   | CT-Prop  | Proposal | Optionality     | (fill in: opening optionality move for proposal's chain)       |
   | CT-Pitch | Pitch    | Emotional       | (fill in: opening emotional move for pitch's conviction chain) |

6. Artifact contract matrix:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening                                   | Recommended option — crystallize, do not reconsider                                |
| CARRIES FORWARD | Feature identity; INERTIA MODEL; design decisions                | Recommended option + rationale; INERTIA MODEL Cost                          | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — INERTIA MODEL Cost as factual record                   | Optionality — Cost priced against each alternative                          | Emotional — Cost visceral per audience                                             |

Print the matrix. Do not begin Artifact 1 until printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL; scout-requirements if found.
                    PRESERVE: (first artifact). CONVICTION TYPE: Factual.

  PURPOSE        — INERTIA MODEL Name + Behavior; Cost as factual record.
  REQUIREMENTS   — Bulleted, MoSCoW (M/S/C/W). Each Must-have: complete Req-ID + SETUP
                   SCOUT TRACEABILITY TABLE row simultaneously. Every Must-have = one row.
  DESIGN         — Components, data flow, decisions.
  CONSTRAINTS    — Technical, team, timeline, dependencies.
  OPEN QUESTIONS — Unknowns; namespace per item.

GATE: Write simulations/draft/specs/{topic}-spec-{date}.md before Artifact 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec; INERTIA MODEL Cost; scout-feasibility if found.
                    PRESERVE: all spec decisions. CONVICTION TYPE: Optionality.

Option A = do-nothing at full INERTIA MODEL Cost. State Cost before alternatives.
Three options min. Per option: Name / Description / Pros / Cons / Risk / Effort.
Recommendation: option + three reasons citing spec decisions.

GATE: Write simulations/draft/proposals/{topic}-proposal-{date}.md before Artifact 3.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal; INERTIA MODEL Cost; scout-positioning if found.
                    PRESERVE: recommended option. CONVICTION TYPE: Emotional.

Each version opens with INERTIA MODEL Cost as hook. Three versions in full:

EXEC — Cost in business terms; Cost elimination; compounding risk; CTA: approve/fund/unblock.
DEV  — Blocked capability; spec design referenced; technical debt; CTA: join beta/review spec.
MAKER — Daily friction; plain language only; time saved; CTA: try it/sign up/start now.
ANTI-POSITIONING: what this feature is NOT, two sentences.

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md before Campaign Reflection.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After pitch file exists on disk only. Retrospective — completed artifacts only.

FINDINGS:

  TRACEABILITY AUDIT
    One row per SETUP SCOUT TRACEABILITY TABLE row. Copy Req-ID and Friction from SETUP
    now; complete remaining columns after Artifact 1. Row count must match SETUP.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | RULE   | Each Req-ID here must match a named entry in the SCOUT TRACEABILITY TABLE (SETUP). Missing row = R-[NN] absent, not a count discrepancy. | — | — | — | — |
    | RULE   | N in col 3 + blank col 5 = STRUCTURAL FAIL — not an acceptable omission. | — | — | — | — |
    | R-01   | (copy from SETUP row 1)     | Y / N                    |                               |            |                 |
    | R-02   | (copy from SETUP row 2)     | Y / N                    |                               |            |                 |
    (match SETUP row count exactly — do not reduce)

    Must-have found: Y = distinct Must-have in Artifact 1 REQUIREMENTS covers friction.
    Must-have text: verbatim from Artifact 1. Blank if N.
    Gap: if N, state absent requirement. N + blank = STRUCTURAL FAIL per RULE row.
    Scout namespace: specific sub-skill for N rows. Blank if Y.

  CONVICTION DELTA
    Three rows only — CT-Spec, CT-Prop, CT-Pitch from INERTIA MODEL MAP. No anonymous
    version rows. Each row's Amplification chain anchors to the MAP starter for that
    Conv-ID. Replace all bracketed tokens. An unfilled bracket fails the row.

    | Conv-ID / Conviction type | Conviction established (one-sentence claim) | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|---------------------------------------------|---------------------|-----------------------------------------------------|
    | RULE | Each Conv-ID must match an INERTIA MODEL MAP entry. Missing row = named-conviction-type absent. Do not add rows. | — | — |
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec starter]) -> [Req-ID's factual claim from Must-have] -> [how spec locked claim as record] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop starter]) -> [Option A = INERTIA MODEL Cost] -> [how recommendation prices against baseline] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch starter]) -> [Req-ID's claim made visceral] -> [audience register that carried it] |

    No grounding: "GAP — [Req-ID] nearest; does not ground CT-[X] because [reason]."

  NEAR-DUPLICATE CONTENT — passage copied; what changed to make it conviction-bearing.
  RESIDUAL QUESTIONS — scout signal needed; namespace per item.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS — complete partial or N rows. Blank row when partial or N = fail.
All Y: "No conviction gaps detected."

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | RULE     | Each artifact row here must match a named INERTIA MODEL MAP entry. Missing row = [artifact-ID] absent, not a count discrepancy. | — | — | — | — |
  | RULE     | An artifact row with all substantive analysis cells (Sub-section, Register found, Register declared, Scout sub-skill, Evidence needed) blank or populated exclusively with structural placeholders (dashes) = STRUCTURAL FAIL — not a present-but-incomplete entry. | — | — | — | — |
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Register found / Register declared: one word each, distinct columns.
  Scout sub-skill: specific identifier (e.g., scout-requirements), not namespace alone.
  Evidence needed: one sentence.

Open questions: namespace for each.
```

---

## V-03 — Conversational CGD Dual-Sentinel

**Axis:** Phrasing register — V-02 structural tables unchanged in column count, row
declaration, and placement of both CONVICTION GAP DIAGNOSIS RULE sentinel rows. The
second CONVICTION GAP DIAGNOSIS RULE sentinel is phrased conversationally inside the
table boundary — second-person, direct address, plain-language description of the
failure mode. All surrounding instructional prose uses the same conversational register
as R18 V-03. The structural property evaluated by C-48 is the presence of a second
non-data RULE sentinel row inside the table whose cell text embeds the N+blank
STRUCTURAL FAIL rule — not the register used to phrase it.

**Hypothesis:** D18 (extended D17 invariance) confirmed that register does not affect
the C-46 verdict on the first CONVICTION GAP DIAGNOSIS sentinel. V-03 tests whether the
same register invariance holds for C-48: a conversational second RULE sentinel inside
the CONVICTION GAP DIAGNOSIS table boundary — phrased as plain-language enforcement
rather than formal structural declaration — earns C-48 FULL identical to V-02. C-48
FULL. C-49 NO CREDIT (MAP, CONVICTION DELTA, SCOUT TRACEABILITY TABLE single-sentinel).
Score: 278.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your job in SETUP is to name the enemy before writing a single word of the campaign.
Fill everything here before Artifact 1. Nothing defers to REFLECTION.

0. Write the CAMPAIGN CONVICTION HYPOTHESIS first. Two parts, in full, before anything else:

   Hypothesis: "The {topic} campaign must establish that [specific friction from INERTIA
   MODEL Cost] is the dominant reason [audience] cannot [achieve desired outcome], so that
   displacing [INERTIA MODEL Name] becomes the obvious move."

   Falsification conditions: "This campaign fails if: (a) spec cannot document [barrier]
   as a measured cost with factual record; (b) proposal cannot price [barrier] against an
   alternative; (c) pitch cannot make [barrier] visceral for at least one version."

   Do not move to item 1 until both parts are written in full.

1. Write one sentence: feature name, audience, problem solved.

2. Declare the INERTIA MODEL:
     Name:     what is the current behavior called? One short phrase.
     Behavior: what do users do today without this feature? One sentence.
     Cost:     what does that cost them? Cover factual, priceable, and emotional.

   The conviction types use the INERTIA MODEL like this:
   - Spec    -> documents Cost as factual record (Factual conviction)
   - Proposal -> prices Cost against alternatives (Optionality conviction)
   - Pitch   -> makes Cost visceral per audience (Emotional conviction)

3. Run glob simulations/scout/ for this topic right now. List every file. Do this
   unconditionally — skip nothing even if no signals exist.

4. Fill the SCOUT TRACEABILITY TABLE. One row per friction from scout-requirements.
   Originating Friction and Scout File go in now. Req-ID and Must-have go in during
   Artifact 1 as you write each Must-have.

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | RULE         | You must have one row in the TRACEABILITY AUDIT (REFLECTION) for every row here. If a row is missing there, that's R-[NN] absent — say it by name, not as a count discrepancy. | — | — |
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (If no scout-requirements file found: one row, Friction from INERTIA MODEL Cost, Scout File = "none")

5. Fill the INERTIA MODEL MAP now, before Artifact 1. Every cell. The row names you
   put in this map are the only row names the CONVICTION DELTA in REFLECTION can use.
   No new conviction-type identifiers may appear in REFLECTION that aren't here.

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter                                    |
   |----------|----------|-----------------|----------------------------------------------------------------|
   | RULE     | You need exactly 3 rows in CONVICTION DELTA (REFLECTION): CT-Spec, CT-Prop, CT-Pitch. A missing row is CT-[X] absent — a named failure, not a count problem. No anonymous rows. | — | — |
   | CT-Spec  | Spec     | Factual         | (write the opening factual move for spec's conviction chain)   |
   | CT-Prop  | Proposal | Optionality     | (write the opening optionality move for proposal's chain)      |
   | CT-Pitch | Pitch    | Emotional       | (write the opening emotional move for pitch's conviction chain) |

6. Print the artifact contract matrix now. Do not start Artifact 1 until it is printed.

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact — no prior decisions)                            | Every spec decision — don't re-open anything the spec settled               | The recommended option from the proposal — crystallize it, do not question it      |
| CARRIES FORWARD | Feature identity; INERTIA MODEL; design decisions                | Recommended option + rationale; INERTIA MODEL Cost                          | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — INERTIA MODEL Cost as factual record                   | Optionality — Cost priced against each alternative                          | Emotional — Cost visceral per audience                                             |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: topic identity; INERTIA MODEL; scout-requirements if found.
Your conviction type is Factual. Document what the INERTIA MODEL costs users before
you prescribe what replaces it.

Write all of these sections:

  PURPOSE        — Name the INERTIA MODEL, describe its Behavior, document the Cost as
                   factual record. Show the reader the problem before the solution.
  REQUIREMENTS   — Bulleted, MoSCoW-tagged. For each Must-have: immediately fill in its
                   Req-ID and entry in the SCOUT TRACEABILITY TABLE above. Every
                   Must-have gets a SETUP table row. No orphan Must-haves.
  DESIGN         — Components, data flow, key decisions. Specific enough to build from.
  CONSTRAINTS    — Technical, team, timeline, dependency limits.
  OPEN QUESTIONS — What you don't know. Name a namespace for each.

Write to disk: simulations/draft/specs/{topic}-spec-{date}.md
Do not start Artifact 2 until that file exists.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: spec file; INERTIA MODEL Cost; scout-feasibility if found.
PRESERVE: every spec decision — do not re-open anything the spec settled.
Your conviction type is Optionality. Option A is do-nothing at full INERTIA MODEL
Cost — state that cost explicitly and concretely before any other option.

Three options minimum. Option A = do-nothing; its cost = the INERTIA MODEL Cost.
Every other option is measured against Option A, not against zero.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: one option, three reasons, each citing a spec decision.

Write to disk: simulations/draft/proposals/{topic}-proposal-{date}.md
Do not start Artifact 3 until that file exists.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: proposal file; INERTIA MODEL Cost; scout-positioning if found.
PRESERVE: the recommended option from the proposal — crystallize it, do not reconsider.
Your conviction type is Emotional. Open every version with the INERTIA MODEL Cost as
the hook. Your audience has the facts (spec) and the options (proposal). Make the Cost felt.

Write all three versions:

EXEC — urgency through compounding Cost:
  Hook: Cost in business terms. What it does: Cost elimination as outcome.
  Why: compounding risk of sustained Behavior. CTA: approve / fund / unblock.

DEV — urgency through blocked capability:
  Hook: what INERTIA MODEL Behavior blocks engineers from building.
  What it does: reference the spec's technical design explicitly.
  Why: technical debt of sustained Behavior. CTA: join beta / review spec / contribute.

MAKER — plain language only, no spec terms, no proposal jargon:
  Hook: the daily friction of INERTIA MODEL Behavior for this person.
  What it does: what changes in their daily work.
  Why: time saved, steps removed. CTA: try it / sign up / start now.

ANTI-POSITIONING: two sentences — what this feature is NOT.

Write to disk: simulations/draft/pitches/{topic}-pitch-{date}.md
Do not start Campaign Reflection until that file exists.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Start here only after the pitch file is on disk. This is retrospective — you are
assessing completed artifacts, not writing new ones.

FINDINGS:

  TRACEABILITY AUDIT
    Take every row from the SCOUT TRACEABILITY TABLE in SETUP. Copy its Req-ID and
    Friction into a named row here — one row per SETUP row, no more, no less.
    Pre-fill Req-ID and Friction before Artifact 1; fill the rest after all artifacts.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | RULE   | Every Req-ID here must match a named row from the SCOUT TRACEABILITY TABLE (SETUP). If R-02 is missing here, say "R-02 absent" — not "one row short." | — | — | — | — |
    | RULE   | If col 3 is N and col 5 is blank, that row is broken. Fix it — blank is not an acceptable omission. | — | — | — | — |
    | R-01   | (paste from SETUP row 1)    | Y / N                    |                               |            |                 |
    | R-02   | (paste from SETUP row 2)    | Y / N                    |                               |            |                 |
    (match SETUP row count exactly)

    Must-have found: Y = a distinct Must-have in Artifact 1 REQUIREMENTS covers this friction directly. N = nothing covers it.
    Must-have text: verbatim Must-have text from Artifact 1. Leave blank only if N.
    Gap: if N, write what requirement is absent. Blank + N = broken row.
    Scout namespace: sub-skill name for N rows (e.g., scout-requirements). Blank if Y.

  CONVICTION DELTA
    Use exactly the three rows from the INERTIA MODEL MAP. Do not use Exec/Dev/Maker —
    those are pitch audience labels, not conviction-type identifiers. Each row answers:
    did this artifact establish its declared conviction type?

    Three rows required (CT-Spec, CT-Prop, CT-Pitch). If a row is missing, that conviction
    type is untracked. An unfilled bracket in the Amplification chain fails the row.

    | Conv-ID / Conviction type | Conviction established (one-sentence claim) | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|---------------------------------------------|---------------------|-----------------------------------------------------|
    | RULE | Each Conv-ID must match an INERTIA MODEL MAP entry. Missing row = CT-[X] absent — a named failure, not a count problem. | — | — |
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec starter]) -> [Req-ID's factual claim] -> [how the spec locked that claim as record] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop starter]) -> [Option A = INERTIA MODEL Cost stated] -> [how the recommendation prices against that baseline] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch starter]) -> [Req-ID's claim made visceral] -> [which audience register carried it furthest] |

    No grounding? Write: "GAP — [Req-ID] nearest; does not ground CT-[X] because [reason]."

  NEAR-DUPLICATE CONTENT — passage copied; what you changed to make it conviction-bearing.
  RESIDUAL QUESTIONS — what scout signal would resolve what no artifact answered; namespace.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Fill the summary table. Y = dominant register matches declared conviction type.
Partial = mixed. N = primary register fails declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  For each partial or N row: fill that artifact's row in the diagnosis table.
  All three Y? Write "No conviction gaps detected." after the table.

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | RULE     | Every row here must be one of the three artifacts from the INERTIA MODEL MAP (Spec, Proposal, Pitch). If Proposal is missing, say "Proposal absent" — don't just count rows. | — | — | — | — |
  | RULE     | If you name an artifact in col 1 but leave Sub-section, Register found, Register declared, Scout sub-skill, and Evidence needed all blank or dashed, that row is broken — treat it as a STRUCTURAL FAIL, not a partial answer you can leave incomplete. | — | — | — | — |
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Sub-section: specific sub-section name — not just the artifact (e.g., "Spec PURPOSE —
  Cost described as opinion, not factual record").
  Register found: one word. Register declared: one word. Separate columns — do not merge.
  Scout sub-skill: exact sub-skill name, not namespace (e.g., scout-requirements).
  Evidence needed: one sentence.

List open questions with recommended namespace for each.
```

---

## V-04 — Complete Five-Table Dual-Sentinel, Maximum Density

**Axis:** Lifecycle emphasis — all five structural tables carry dual in-table RULE
sentinel rows at maximum enforcement density. TRACEABILITY AUDIT retains its R17 dual
form (C-45). CONVICTION GAP DIAGNOSIS gains a second RULE sentinel (C-48). INERTIA MODEL
MAP (SETUP, item 5), CONVICTION DELTA (REFLECTION), and SCOUT TRACEABILITY TABLE (SETUP,
item 4) each gain a second RULE sentinel row declaring the N+blank STRUCTURAL FAIL rule
for that table's data type. All five second sentinels are positioned inside their
respective table boundaries, after the first RULE sentinel and before the data rows.
Surrounding prose at maximum directive density throughout.

**Hypothesis:** C-49 requires the five-table dual-sentinel architecture simultaneously:
MAP dual + CONVICTION DELTA dual + SCOUT TRACEABILITY TABLE dual + TRACEABILITY AUDIT
dual (C-45) + CONVICTION GAP DIAGNOSIS dual (C-48). V-04 supplies all five. The three
previously single-sentinel tables each gain a second in-table RULE sentinel declaring
their respective N+blank STRUCTURAL FAIL rules: a SCOUT TRACEABILITY TABLE row with all
substantive cells blank or dash-filled = STRUCTURAL FAIL; an INERTIA MODEL MAP row with
all analysis cells blank or placeholder-filled = STRUCTURAL FAIL; a CONVICTION DELTA row
with all analytical cells blank or bracket-unfilled = STRUCTURAL FAIL. C-48 FULL; C-49
FULL. Score: 283. If V-04 and V-05 both score 283, density invariance (D16 through D18)
extends to C-49 — confirming that directive density in adjacent prose is non-load-bearing
at the dual-sentinel level across all five tables.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent — the status quo each
artifact must displace. Fill all SETUP tables completely before Artifact 1. No SETUP
field or table may be deferred, partially completed, or left for REFLECTION to supply.

0. CAMPAIGN CONVICTION HYPOTHESIS — two required items, completed in full before item 1:

   Hypothesis: "The {topic} campaign must establish that [specific friction from INERTIA
   MODEL Cost] is the dominant reason [audience] cannot [achieve desired outcome], so that
   displacing [INERTIA MODEL Name] becomes the obvious move."

   Falsification conditions: "This campaign fails if: (a) spec cannot document [barrier
   named above] as a measured cost with factual record; (b) proposal cannot price
   [barrier] against at least one do-something alternative; (c) pitch cannot make
   [barrier] visceral for at least one audience version. Any unmet condition means the
   CAMPAIGN CONVICTION HYPOTHESIS is unproven and the campaign is incomplete."

   Complete item 0 in full before proceeding to item 1. The hypothesis names what the
   campaign bets against; the falsification conditions name how to know if the bet is lost.

1. Topic identity — one sentence: feature name, audience, problem solved.

2. INERTIA MODEL — three-field declaration:
     Name:     one short phrase identifying the current behavior in shorthand
     Behavior: what users do today without this feature — one sentence
     Cost:     what that behavior costs them — one sentence covering factual,
               priceable, and emotional dimensions

   The three conviction types map onto INERTIA MODEL fields directly:
   - Factual conviction (spec):         documents the Cost field as factual record
   - Optionality conviction (proposal): prices the Cost field against each alternative
   - Emotional conviction (pitch):      makes the Cost field visceral per audience

3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Unconditional. Do not gate on signal presence.

4. SCOUT TRACEABILITY TABLE — source of truth for TRACEABILITY AUDIT row identifiers.
   Each Req-ID pre-declared here becomes a named row in CAMPAIGN REFLECTION. Fill
   Originating Friction and Scout File now from scout-requirements findings; complete
   Req-ID and Must-have during Artifact 1 REQUIREMENTS writing.

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | RULE         | The TRACEABILITY AUDIT in CAMPAIGN REFLECTION must contain exactly one row per entry in this table. A missing REFLECTION row is a named-identifier absence — R-02 absent means that friction is unaudited — not a count discrepancy discoverable only by comparing totals. The TRACEABILITY AUDIT row count must equal this table's Req-ID data row count at all times. | — | — |
   | RULE         | A SCOUT TRACEABILITY TABLE data row with all substantive cells (Must-have brief, Originating Scout-Requirements Friction, Scout File) blank or populated exclusively with structural placeholders = STRUCTURAL FAIL — not a valid present-but-incomplete friction entry. | — | — |
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (one row per identified friction; if no scout-requirements file found, one row with Friction
   derived from INERTIA MODEL Cost and Scout File = "none")

5. INERTIA MODEL MAP — source of truth for CONVICTION DELTA row identifiers. Each Conv-ID
   pre-declared here becomes a named row in CAMPAIGN REFLECTION. Fill all four columns
   now, before Artifact 1. The map is the conviction-type source of truth; do not
   introduce conviction-type identifiers in REFLECTION that are not pre-declared here.

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter                                    |
   |----------|----------|-----------------|----------------------------------------------------------------|
   | RULE     | The CONVICTION DELTA in REFLECTION must contain exactly 3 rows (CT-Spec, CT-Prop, CT-Pitch). A missing row is a named-conviction-type absence: CT-Spec absent means the Spec's Factual conviction type is untracked — visible at a glance by named-entry absence, not discoverable only by count comparison. Do not introduce anonymous version rows (Exec, Dev, Maker). | — | — |
   | RULE     | An INERTIA MODEL MAP data row with all substantive analysis cells (Artifact, Conviction type, Amplification chain starter) blank or populated exclusively with structural placeholders = STRUCTURAL FAIL — not a valid present-but-incomplete conviction entry. | — | — |
   | CT-Spec  | Spec     | Factual         | (fill in: what factual claim anchors the spec's Cost record)   |
   | CT-Prop  | Proposal | Optionality     | (fill in: what cost framing anchors the proposal's options)    |
   | CT-Pitch | Pitch    | Emotional       | (fill in: what emotional anchor makes Cost visceral in pitch)  |

6. Artifact contract matrix — print in full before Artifact 1:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening                                   | Recommended option — crystallize, do not reconsider                                |
| CARRIES FORWARD | Feature identity; INERTIA MODEL; design decisions                | Recommended option + rationale; INERTIA MODEL Cost                          | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — INERTIA MODEL Cost as factual record                   | Optionality — Cost priced against each alternative                          | Emotional — Cost visceral per audience                                             |

Do not begin Artifact 1 until the matrix is printed in full.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL (all fields); scout-requirements
if found. PRESERVE: (first artifact — no prior decisions to carry). CONVICTION TYPE: Factual.
Document the Cost as factual record before prescribing what replaces it.

  PURPOSE        — INERTIA MODEL Name + Behavior; Cost as factual record with observable
                   evidence. The reader must see the cost before the solution.
  REQUIREMENTS   — Bulleted, MoSCoW (M/S/C/W). Each Must-have: complete Req-ID + SETUP
                   SCOUT TRACEABILITY TABLE row simultaneously and unconditionally.
                   Every Must-have = exactly one SETUP table row. No orphan Must-haves.
  DESIGN         — Components, data flow, key design decisions with rationale.
  CONSTRAINTS    — Technical, team, timeline, external dependencies. Specific.
  OPEN QUESTIONS — Unknowns with named namespace per item. Do not leave nameless.

GATE: Write simulations/draft/specs/{topic}-spec-{date}.md. Do not begin Artifact 2
until that file exists on disk and is complete.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; INERTIA MODEL Cost; scout-feasibility if found.
PRESERVE: all spec design decisions — do not re-open anything the spec settled.
CONVICTION TYPE: Optionality. Option A is do-nothing at the full, stated INERTIA MODEL
Cost — declare that cost explicitly and concretely before presenting any alternative.

Three options minimum. Option A = do-nothing; its explicit cost = the INERTIA MODEL Cost.
Every subsequent option is measured against Option A's cost, not against zero.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: one option + three reasons, each reason citing a spec decision by name.

GATE: Write simulations/draft/proposals/{topic}-proposal-{date}.md. Do not begin
Artifact 3 until that file exists on disk and is complete.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; INERTIA MODEL Cost; scout-positioning if found.
PRESERVE: recommended option from proposal — crystallize it, do not reconsider.
CONVICTION TYPE: Emotional. Every version opens with the INERTIA MODEL Cost as the hook.
The audience already has facts (spec) and options (proposal). Make the Cost visceral.

Three versions, each in full:

EXEC — urgency through business Cost compounding:
  Hook: INERTIA MODEL Cost in business terms. Outcome: Cost elimination.
  Why now: compounding risk if Behavior continues. CTA: approve / fund / unblock.

DEV — urgency through blocked engineering capability:
  Hook: what INERTIA MODEL Behavior prevents engineers from building today.
  Outcome: reference the spec's design explicitly by section and feature.
  Why now: technical debt of sustained Behavior. CTA: join beta / review spec / contribute.

MAKER — plain language, zero spec terms, zero proposal jargon:
  Hook: daily friction of INERTIA MODEL Behavior for this person specifically.
  Outcome: what changes in their daily work, concretely.
  Why now: time saved, steps removed. CTA: try it / sign up / start now.

ANTI-POSITIONING: what this feature is NOT — two sentences, specific and committal.

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md. Do not begin Campaign
Reflection until that file exists on disk and is complete.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Begin only after the pitch file exists on disk. Retrospective mode — assess completed
artifacts only. Do not revise any artifact during REFLECTION.

FINDINGS:

  TRACEABILITY AUDIT
    One row per SETUP SCOUT TRACEABILITY TABLE entry. Copy Req-ID and Friction from SETUP
    now — pre-populate both columns before Artifact 1. Complete remaining columns after
    all three artifacts are written. Row count must equal SETUP exactly — do not reduce.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | RULE   | Each Req-ID here must match a named entry in the SCOUT TRACEABILITY TABLE (SETUP). A missing REFLECTION row is a named-identifier absence — R-02 absent means that friction is unaudited — not a count discrepancy discoverable only by comparing totals. Do not reduce row count below SETUP. | — | — | — | — |
    | RULE   | N in col 3 + blank col 5 = STRUCTURAL FAIL for that row — not an acceptable omission. Every N row requires a Gap entry naming the absent requirement. | — | — | — | — |
    | R-01   | (copy from SETUP row 1)     | Y / N                    |                               |            |                 |
    | R-02   | (copy from SETUP row 2)     | Y / N                    |                               |            |                 |
    (match SETUP row count exactly — do not reduce under any condition)

    Must-have found: Y = a distinct Must-have in Artifact 1 REQUIREMENTS covers the friction directly.
    Must-have text: verbatim phrase from Artifact 1 REQUIREMENTS. Blank only if N — not if partial.
    Gap: if N, state the absent requirement precisely. N + blank Gap = STRUCTURAL FAIL.
    Scout namespace: specific sub-skill identifier for N rows (e.g., scout-requirements). Blank if Y.

  CONVICTION DELTA
    Exactly three rows — CT-Spec, CT-Prop, CT-Pitch from the INERTIA MODEL MAP. No
    anonymous version rows (Exec, Dev, Maker are audience labels, not conviction types).
    Each row's Amplification chain must anchor to the MAP starter for that Conv-ID.
    Replace all bracketed tokens. An unfilled bracket anywhere in the chain fails the row.

    | Conv-ID / Conviction type | Conviction established (one-sentence claim) | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|---------------------------------------------|---------------------|-----------------------------------------------------|
    | RULE | Each Conv-ID must match a named entry in the INERTIA MODEL MAP. A missing row is a named-conviction-type absence: CT-Spec absent means the Spec's Factual conviction is untracked — not discoverable by count alone. Do not add rows not declared in the MAP. | — | — |
    | RULE | A CONVICTION DELTA data row with all analytical cells (Conviction established, Grounding Req-IDs, Amplification chain) blank or containing only unfilled bracket tokens = STRUCTURAL FAIL — not a valid present-but-incomplete conviction-type entry. | — | — |
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec starter]) -> [Req-ID's factual claim from Must-have] -> [how spec locked claim as record] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop starter]) -> [Option A = INERTIA MODEL Cost fully stated] -> [how recommendation prices against that baseline] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch starter]) -> [Req-ID's claim made visceral] -> [audience register that carried it furthest] |

    No grounding: "GAP — [Req-ID] nearest; does not ground CT-[X] because [specific reason]."

  NEAR-DUPLICATE CONTENT — passage copied verbatim from prior artifact; what changed to make it conviction-bearing.
  RESIDUAL QUESTIONS — scout signal needed to answer what no artifact resolved; namespace per item.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Fill the summary table completely. Y = dominant register matches declared conviction type
for that artifact. Partial = meaningful mixed-register content. N = primary register
demonstrably fails declared conviction type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS — complete one row per partial or N artifact. A blank row for
any partial or N artifact is a structural failure — the diagnosis table must be as
complete as the CLOSE table's verdict requires. All three Y: "No conviction gaps detected."

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | RULE     | The CONVICTION GAP DIAGNOSIS must contain exactly one row per artifact declared in the INERTIA MODEL MAP (Spec, Proposal, Pitch). A missing row is a named-artifact absence — "Proposal absent" means the Proposal artifact's conviction gap status is undiagnosed — not a count discrepancy discoverable only by comparing totals. Artifact identifiers in col 1 must match INERTIA MODEL MAP entries. Do not introduce anonymous rows. | — | — | — | — |
  | RULE     | A CONVICTION GAP DIAGNOSIS data row with all substantive analysis cells (Sub-section, Register found, Register declared, Scout sub-skill, Evidence needed) blank or populated exclusively with structural placeholders (dashes) = STRUCTURAL FAIL — not a present-but-incomplete entry. Naming the artifact in col 1 while leaving all analysis cells empty does not constitute a valid partial diagnosis. | — | — | — | — |
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Sub-section: specific sub-section name and failure mode — not artifact name alone.
  Register found: one word. Register declared: one word. Distinct columns — never merged.
  Scout sub-skill: exact sub-skill identifier, not namespace alone (e.g., scout-requirements).
  Evidence needed: one sentence — what would change the verdict from N/partial to Y.

Open questions: namespace for each.
```

---

## V-05 — Complete Five-Table Dual-Sentinel, Compressed

**Axis:** Lifecycle compression — all five structural tables carry dual in-table RULE
sentinel rows; all surrounding instructional prose stripped to minimum viable form.
Phase headers retained; instructional paragraphs before and after each table reduced
to one line or removed. All ten RULE sentinel rows (two per table) are present and
positioned correctly inside their respective table boundaries. Tests whether adjacent
prose volume is load-bearing at the 283-ceiling level.

**Hypothesis:** V-05 is the prose-compression parallel of R18 V-05, extended to the
full dual-sentinel architecture across all five tables. All five second RULE sentinels
are present. Surrounding instructional prose is stripped — no explanatory paragraphs,
no enforcement rationale outside the RULE rows, no expanded column definitions. The
structural properties evaluated by C-48 and C-49 are in-table placement and rule content
presence; neither criterion depends on surrounding prose volume. C-48 FULL; C-49 FULL.
Score: 283. If V-05 scores identically to V-04, the D16/D17/D18 invariance stack extends
to include adjacent prose at the dual-sentinel level — adjacent prose volume is confirmed
non-load-bearing for the complete five-table dual-sentinel architecture.

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

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | RULE         | TRACEABILITY AUDIT (REFLECTION) must have one row per entry here. Missing row = R-[NN] absent, not a count discrepancy. | — | — |
   | RULE         | A data row with all substantive cells blank or dash-filled = STRUCTURAL FAIL — not a valid present-but-incomplete friction entry. | — | — |
   | (fill in A1) | (fill in A1)         |                                              |                             |

5. INERTIA MODEL MAP:

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter  |
   |----------|----------|-----------------|------------------------------|
   | RULE     | CONVICTION DELTA (REFLECTION) must have exactly 3 rows: CT-Spec, CT-Prop, CT-Pitch. Missing row = named-conviction-type absent. No anonymous rows. | — | — |
   | RULE     | A data row with all analysis cells blank or placeholder-filled = STRUCTURAL FAIL — not a valid present-but-incomplete conviction entry. | — | — |
   | CT-Spec  | Spec     | Factual         |                              |
   | CT-Prop  | Proposal | Optionality     |                              |
   | CT-Pitch | Pitch    | Emotional       |                              |

6. Artifact contract matrix — print before Artifact 1:

| Field           | Spec                                           | Proposal                                              | Pitch                                                  |
|-----------------|------------------------------------------------|-------------------------------------------------------|--------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL; scout-requirements if found | Spec; INERTIA MODEL Cost; scout-feasibility if found | Proposal; INERTIA MODEL Cost; scout-positioning if found |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md | simulations/draft/proposals/{topic}-proposal-{date}.md | simulations/draft/pitches/{topic}-pitch-{date}.md    |
| PRESERVE        | (first artifact)                               | All spec decisions                                    | Recommended option                                     |
| CARRIES FORWARD | Feature identity; INERTIA MODEL; decisions     | Recommended option; INERTIA MODEL Cost                | (final)                                                |
| CONVICTION TYPE | Factual                                        | Optionality                                           | Emotional                                              |

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

EXEC — Cost in business terms; elimination; compounding risk; CTA: approve/fund/unblock.
DEV  — Blocked capability; spec design referenced; technical debt; CTA: join beta/review spec.
MAKER — Daily friction; plain language; time saved; CTA: try it/sign up/start now.
ANTI-POSITIONING: two sentences.

GATE: simulations/draft/pitches/{topic}-pitch-{date}.md before Campaign Reflection.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After pitch file on disk only.

FINDINGS:

  TRACEABILITY AUDIT

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | RULE   | Each Req-ID here must match a named SCOUT TRACEABILITY TABLE (SETUP) entry. Missing row = R-[NN] absent, not a count discrepancy. | — | — | — | — |
    | RULE   | N + blank col 5 = STRUCTURAL FAIL. | — | — | — | — |
    | R-01   | (copy from SETUP)           | Y / N                    |                               |            |                 |
    | R-02   | (copy from SETUP)           | Y / N                    |                               |            |                 |

  CONVICTION DELTA

    | Conv-ID / Conviction type | Conviction established | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|------------------------|---------------------|---------------------|
    | RULE | Each Conv-ID must match an INERTIA MODEL MAP entry. Missing row = named-conviction-type absent. No anonymous rows. | — | — |
    | RULE | A row with all analytical cells blank or bracket-unfilled = STRUCTURAL FAIL — not a valid present-but-incomplete conviction-type entry. | — | — |
    | CT-Spec — Factual         |                        |                     | (MAP starter) -> [factual claim] -> [locked as record] |
    | CT-Prop — Optionality     |                        |                     | (MAP starter) -> [Option A = Cost] -> [prices against baseline] |
    | CT-Pitch — Emotional      |                        |                     | (MAP starter) -> [claim visceral] -> [audience register] |

  NEAR-DUPLICATE CONTENT — passage; what changed.
  RESIDUAL QUESTIONS — namespace per item.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     |                |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     |                |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     |                |

CONVICTION GAP DIAGNOSIS — partial or N rows only. All Y: "No conviction gaps detected."

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | RULE     | Each row here must match a named INERTIA MODEL MAP entry (Spec, Proposal, Pitch). Missing row = [artifact-ID] absent, not a count discrepancy. | — | — | — | — |
  | RULE     | A data row with all substantive analysis cells blank or dash-filled = STRUCTURAL FAIL — not a present-but-incomplete entry. | — | — | — | — |
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

Open questions: namespace for each.
```
