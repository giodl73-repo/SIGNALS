---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 17
rubric: campaign-blueprint-rubric-v17-2026-03-17.md
---

# campaign-blueprint — Prompt Variations R17

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04 through V-05).

## R17 Context

R16 variants under v17 retroactive scoring:

| Variant | v16 | C-44 | C-45 | v17 |
|---------|-----|------|------|-----|
| V-01 — Pitch-First Role Sequence | 243 | 0 | 0 | **243** |
| V-02 — Conversational Register | 243 | 0 | 0 | **243** |

Neither R16 variant earns C-44 or C-45. Both deliver the traceability match directive
as prose outside the SCOUT TRACEABILITY TABLE boundary. V-01 uses formal prose; V-02
uses conversational prose ("One thing to remember...") — both earn C-38 FULL and C-44
NO CREDIT. Role-sequence and register invariance (D17) confirm no non-structural axis
can supply the missing in-table sentinel.

The R16 pattern completes the invariance survey for the current structural level:
- Register invariance (D16): formal vs. conversational — confirmed non-ceiling-breaking
- Directive density invariance (D16): terse vs. exhaustive prose — confirmed
- Role-sequence invariance (D17): generation order permutations — confirmed

The only path to 263 runs through two in-table RULE sentinels on the traceability axis:

  Base 253 (v16 ceiling, V-04 R15)
  + C-44: in-table RULE sentinel inside SCOUT TRACEABILITY TABLE (SETUP)    → +5
  + C-45: in-table RULE sentinel inside TRACEABILITY AUDIT (REFLECTION)     → +5
  = **263**

Both sentinels must be present simultaneously (C-45 is a strict superset of C-44).
The existing V-04 R15 TRACEABILITY AUDIT carries a RULE row for N+blank structural
failure, but NOT a Req-ID-binding RULE row declaring named-identifier absence as the
failure mode for a missing REFLECTION row. That is the gap this round closes.

D17 four-sentinel chain test applied to the target pattern:
1. C-34 FULL: 4-column CONVICTION DELTA with in-cell Amplification chain template
2. C-35 FULL: 6-column CONVICTION GAP DIAGNOSIS with register-split columns
3. C-38 FULL: named Req-ID rows in TRACEABILITY AUDIT with SETUP match directive
4. C-40 FULL: 4-column INERTIA MODEL MAP with CONVICTION DELTA rows pre-named from MAP
5. C-42 FULL: in-table RULE sentinel inside INERTIA MODEL MAP (SETUP)
6. C-43 FULL: in-table RULE sentinel inside CONVICTION DELTA (REFLECTION)
7. C-44 FULL: in-table RULE sentinel inside SCOUT TRACEABILITY TABLE (SETUP)
   — sentinel precedes Req-ID data rows; text declares TRACEABILITY AUDIT must contain
   one row per SETUP entry; missing row = R-[NN] absent, not a count discrepancy
8. C-45 FULL: in-table RULE sentinel inside TRACEABILITY AUDIT (REFLECTION)
   — sentinel declares each Req-ID must match a named SCOUT TRACEABILITY TABLE entry;
   missing row = named-identifier absence

**R17 design questions:**

1. **SCOUT TRACEABILITY TABLE sentinel only (V-01):** Does adding the RULE sentinel to
   the SCOUT TRACEABILITY TABLE in SETUP while leaving the TRACEABILITY AUDIT unchanged
   (keeping only the N+blank=FAIL RULE row, not adding a Req-ID-binding row) earn C-44
   FULL and C-45 NO CREDIT? Expected: 258 (step 7 passes, step 8 fails — TRACEABILITY
   AUDIT carries N+blank sentinel but not a Req-ID-to-SETUP-entry binding sentinel).

2. **Minimum-form four-sentinel chain (V-02):** Add the SCOUT TRACEABILITY TABLE RULE
   sentinel (minimum text) and a second RULE row in TRACEABILITY AUDIT (minimum text,
   Req-ID-to-SETUP binding). Does minimum form earn C-44 FULL and C-45 FULL? Expected: 263.

3. **Conversational register (V-03):** V-02 structural tables unchanged; all instructional
   prose converted to second-person imperative. Tests D17 register invariance: does a
   conversational-register SCOUT TRACEABILITY TABLE RULE sentinel earn C-44 FULL? Expected: 263.

4. **Maximum-density four-sentinel chain (V-04):** All four RULE sentinels at maximum
   enforcement density. Both traceability RULE rows (SETUP and REFLECTION) carry
   exhaustive structural declarations. Both conviction-type RULE rows (SETUP and
   REFLECTION) unchanged from V-04 R15. Expected: 263.

5. **Minimum-density full compression (V-05):** All four structural sentinels present;
   all surrounding prose stripped to minimum viable instructions. Tests whether adjacent
   prose is load-bearing at the 263-ceiling level. Expected: 263.

**Predicted scoring pattern:**

| Variant | Axis | C-42 | C-43 | C-44 | C-45 | v17 |
|---------|------|------|------|------|------|-----|
| V-01 — SCOUT TABLE Sentinel Only | Lifecycle (SETUP-axis isolation) | FULL | FULL | FULL | NO | **258** |
| V-02 — Minimum Four-Sentinel Form | Output format (minimum sentinel text) | FULL | FULL | FULL | FULL | **263** |
| V-03 — Conversational Register | Phrasing register | FULL | FULL | FULL | FULL | **263** |
| V-04 — Maximum-Density Four-Sentinel | Lifecycle emphasis (maximum density) | FULL | FULL | FULL | FULL | **263** |
| V-05 — Minimum-Density Compression | Lifecycle compression (minimum prose) | FULL | FULL | FULL | FULL | **263** |

V-01 is the diagnostic control: it isolates C-44 from C-45 by supplying the SETUP
sentinel without the REFLECTION counterpart. V-02 through V-05 each target 263 via
different implementation forms of the two new sentinels.

---

## V-01 — SCOUT TRACEABILITY TABLE Sentinel Only

**Axis:** Lifecycle emphasis — single-axis isolation of the SETUP traceability sentinel.
The SCOUT TRACEABILITY TABLE in SETUP gains an in-table RULE sentinel row preceding the
Req-ID data rows. The TRACEABILITY AUDIT in REFLECTION retains the V-04 R15 form: named
Req-ID rows (R-01, R-02) with the existing N+blank=STRUCTURAL FAIL RULE row. No new
Req-ID-binding RULE row is added to the TRACEABILITY AUDIT.

**Hypothesis:** C-44 requires an in-table RULE sentinel inside the SCOUT TRACEABILITY TABLE
in SETUP. The D17 step-7 test: locate the SCOUT TRACEABILITY TABLE and scan for a non-data
RULE sentinel row preceding the Req-ID data rows. V-01 supplies this. D17 step-8 test:
locate the TRACEABILITY AUDIT in REFLECTION and scan for a non-data RULE row whose text
declares each Req-ID must match a named SETUP entry and that a missing row is a
named-identifier absence. V-01 does not supply this — the existing RULE row declares
N+blank=STRUCTURAL FAIL (a cell-level rule) rather than a Req-ID-to-SETUP-entry binding
rule (an entry-level rule). C-44 FULL; C-45 NO CREDIT. Score: 258.

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

   Conviction map: Factual→spec documents Cost; Optionality→proposal prices Cost;
   Emotional→pitch makes Cost visceral per audience.

3. Scout inventory — glob simulations/scout/ now. Unconditional.

4. SCOUT TRACEABILITY TABLE — source of truth for TRACEABILITY AUDIT row identifiers.
   Each Req-ID pre-declared here becomes a named row in REFLECTION.

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | RULE         | The TRACEABILITY AUDIT in REFLECTION must contain exactly one row per entry in this table. A missing row is a named-identifier absence (R-[NN] absent), not a count discrepancy. | — | — |
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (one row per friction; if none found: one row, Friction from INERTIA MODEL Cost, file = "none")

5. INERTIA MODEL MAP — source of truth for CONVICTION DELTA row identifiers. Each Conv-ID
   pre-declared here becomes a named row in REFLECTION. A missing CONVICTION DELTA row is a
   CT-[X] absence — CT-Spec absent means Factual conviction type is untracked.

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
    | RULE   | N in col 3 + blank col 5 = STRUCTURAL FAIL — not an acceptable omission  | — | — | — | — |
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
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec starter]) → [Req-ID's factual claim from Must-have] → [how spec locked claim as record] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop starter]) → [Option A = INERTIA MODEL Cost] → [how recommendation prices against baseline] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch starter]) → [Req-ID's claim made visceral] → [audience register that carried it] |

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
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Register found / Register declared: one word each, distinct columns.
  Scout sub-skill: specific identifier (e.g., scout-requirements), not namespace alone.
  Evidence needed: one sentence.

Open questions: namespace for each.
```

---

## V-02 — Minimum-Form Four-Sentinel Chain

**Axis:** Output format — minimum-text implementation of all four in-table RULE sentinel
rows. The SCOUT TRACEABILITY TABLE (SETUP) gains a RULE sentinel row at minimum viable
text. The TRACEABILITY AUDIT (REFLECTION) gains a second RULE sentinel row (in addition
to the existing N+blank=FAIL row) at minimum viable text, specifically binding each Req-ID
to a SCOUT TRACEABILITY TABLE entry. The conviction-type sentinels (INERTIA MODEL MAP and
CONVICTION DELTA) are unchanged from V-04 R15.

**Hypothesis:** C-44 requires a non-data RULE row inside the SCOUT TRACEABILITY TABLE whose
text embeds the structural enforcement rule: TRACEABILITY AUDIT must contain one row per
SETUP entry; missing row = R-[NN] absent. C-45 requires that TRACEABILITY AUDIT also carries
its own in-table RULE row binding each Req-ID to a SETUP entry and declaring named-identifier
absence. The minimum form tests whether terse sentinel text is structurally sufficient — the
rubric evaluates the structural property (in-table placement), not directive density. Both
sentinels are inside their respective tables, preceding the data rows. C-44 FULL; C-45 FULL.
Score: 263.

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

   Conviction map: Factual→spec documents Cost; Optionality→proposal prices Cost;
   Emotional→pitch makes Cost visceral per audience.

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
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec starter]) → [Req-ID's factual claim from Must-have] → [how spec locked claim as record] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop starter]) → [Option A = INERTIA MODEL Cost] → [how recommendation prices against baseline] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch starter]) → [Req-ID's claim made visceral] → [audience register that carried it] |

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
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Register found / Register declared: one word each, distinct columns.
  Scout sub-skill: specific identifier (e.g., scout-requirements), not namespace alone.
  Evidence needed: one sentence.

Open questions: namespace for each.
```

---

## V-03 — Conversational Register

**Axis:** Phrasing register — V-02 structural tables unchanged in column count, row
declaration, and all four RULE sentinel rows. All instructional prose converted to
second-person imperative throughout. Table instructions become direct commands. Phase
headers become directives. Column definitions become inline guards. RULE sentinel text
inside each table is phrased conversationally but remains inside the table boundary.

**Hypothesis:** D17 establishes register invariance for in-table sentinels: a
conversational-register in-table RULE sentinel earns C-44 FULL; a formal-register
prose directive outside the table earns C-44 NO CREDIT. V-03 tests the affirmative
case: the SCOUT TRACEABILITY TABLE carries a conversational RULE sentinel ("If you don't
have a TRACEABILITY AUDIT row for every entry here, that's R-[NN] absent — call it by
name") and the TRACEABILITY AUDIT carries a conversational RULE sentinel binding each
Req-ID to a SETUP entry. The structural property is in-table placement; register does
not affect verdict. C-44 FULL; C-45 FULL. Score: 263.

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
   - Spec   → documents Cost as factual record (Factual conviction)
   - Proposal → prices Cost against alternatives (Optionality conviction)
   - Pitch  → makes Cost visceral per audience (Emotional conviction)

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
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec starter]) → [Req-ID's factual claim] → [how the spec locked that claim as record] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop starter]) → [Option A = INERTIA MODEL Cost stated] → [how the recommendation prices against that baseline] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch starter]) → [Req-ID's claim made visceral] → [which audience register carried it furthest] |

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
  A blank row when CLOSE shows partial or N is a broken diagnosis. Fix it.
  All three Y? Write "No conviction gaps detected." after the table.

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
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

## V-04 — Maximum-Density Four-Sentinel Chain

**Axis:** Lifecycle emphasis — all four structural sentinels at maximum enforcement
density simultaneously. The SCOUT TRACEABILITY TABLE carries an exhaustive RULE sentinel
row with the full structural declaration. The TRACEABILITY AUDIT carries both a Req-ID-
binding RULE sentinel (exhaustive form) and the existing N+blank=FAIL RULE sentinel
(retained at full density). Both conviction-type sentinels (INERTIA MODEL MAP and
CONVICTION DELTA) carried at V-04 R15 density, unchanged. Maximum prose density
surrounding each table is preserved — no compression.

**Hypothesis:** Maximum-density sentinel text is the strictest achievable form of
structural enforcement embedding. The test is whether exhaustive directive text in
the RULE rows supplies any scoring advantage beyond minimum form (V-02), or whether
structural placement is the only property evaluated. Predicted score: 263. If V-04
scores identically to V-02, the density invariance established in D16 extends to the
traceability sentinel axis — confirming that directive density is non-load-bearing at
the 263-ceiling level.

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
   | CT-Spec  | Spec     | Factual         | (fill in: what factual claim anchors the spec's Cost record)   |
   | CT-Prop  | Proposal | Optionality     | (fill in: what cost framing anchors the proposal's options)    |
   | CT-Pitch | Pitch    | Emotional       | (fill in: what visceral register anchors the pitch's hook)     |

6. Artifact contract matrix — declares what each artifact inherits, produces, protects, and carries:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening, no new design work               | Recommended option from proposal — crystallize, do not reconsider                  |
| CARRIES FORWARD | Feature identity; INERTIA MODEL (all fields); design decisions   | Recommended option name and rationale; INERTIA MODEL Cost                   | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — documents INERTIA MODEL Cost as factual record         | Optionality — prices INERTIA MODEL Cost against each alternative            | Emotional — makes INERTIA MODEL Cost visceral per audience                         |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL (Name, Behavior, Cost); scout-requirements if found.
                    PRESERVE: (first artifact — no prior decisions to protect).
                    CONVICTION TYPE: Factual [INERTIA MODEL Cost → factual record]

Document what the INERTIA MODEL costs users before prescribing what replaces it.

Sections (all required):

  PURPOSE        — State the INERTIA MODEL Name and Behavior, then document the Cost as
                   factual record. "The INERTIA MODEL creates [Cost] for [audience]
                   because [Behavior persists]."
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   As you write each Must-have, complete its Req-ID and Must-have entry in
                   the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above. Every Must-have
                   must correspond to a row in that table.
  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; INERTIA MODEL Cost; scout-feasibility if found.
                    PRESERVE: all spec design decisions — do not re-open anything the spec resolved.
                    CONVICTION TYPE: Optionality [INERTIA MODEL Cost → priced against each alternative]

Option A is do-nothing — the INERTIA MODEL maintained at full Cost. State that Cost
explicitly and concretely before presenting alternatives. Every other option is measured
against the INERTIA MODEL Cost, not against zero.

Three options minimum. Option A: do-nothing — state the INERTIA MODEL Cost as the option cost.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; INERTIA MODEL Cost; scout-positioning if found.
                    PRESERVE: recommended option from proposal — crystallize it, do not reconsider.
                    CONVICTION TYPE: Emotional [INERTIA MODEL Cost → visceral per audience]

Each version opens with the INERTIA MODEL Cost as its hook. The audience already has the
facts (spec) and the options (proposal). What they need is to feel why the INERTIA MODEL
Cost exceeds the cost of acting now — and why that urgency is specific to them.

Three versions in full:

EXEC (decision-makers) — urgency through compounding INERTIA MODEL Cost:
  Hook: the INERTIA MODEL Cost in business terms — what keeps accumulating without this.
  What it does: the outcome the recommended option delivers, framed as Cost elimination.
  Why it matters: the compounding risk of sustained INERTIA MODEL Behavior.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through blocked capability:
  Hook: what the INERTIA MODEL Behavior prevents engineers from doing or building.
  What it does: references the technical design from the spec explicitly.
  Why it matters: the technical debt or opportunity cost of sustained INERTIA MODEL Behavior.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through daily INERTIA MODEL Cost:
  Hook: the specific daily friction of the INERTIA MODEL Behavior for this audience.
  What it does: no spec terminology, no proposal jargon — only what changes in daily work.
  Why it matters: time saved and steps removed from the INERTIA MODEL Behavior.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production
begins, not during pitch production. What follows is retrospective assessment of completed
artifacts. The question in each sub-field: did the artifact make the INERTIA MODEL Cost
visceral at its declared conviction level?

FINDINGS:

  TRACEABILITY AUDIT
    One row per SETUP SCOUT TRACEABILITY TABLE row. Copy Req-ID and Friction from SETUP
    now; complete remaining columns after Artifact 1. Row count must match SETUP exactly.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | RULE   | Each Req-ID in this table must match a named entry in the SCOUT TRACEABILITY TABLE (SETUP). A missing row is a named-identifier absence — R-02 absent means that friction is unaudited — not a count discrepancy discoverable only by comparing totals. The row count in this table must equal the SETUP SCOUT TRACEABILITY TABLE's Req-ID data row count. | — | — | — | — |
    | RULE   | N in col 3 + blank col 5 = STRUCTURAL FAIL — not an acceptable omission. State the absent requirement explicitly in col 5 for every N row. | — | — | — | — |
    | R-01   | (copy from SETUP row 1)     | Y / N                    |                               |            |                 |
    | R-02   | (copy from SETUP row 2)     | Y / N                    |                               |            |                 |
    (add rows to match SETUP table exactly — do not reduce row count)

    Must-have found in spec?: Y if a distinct bulleted Must-have in Artifact 1 REQUIREMENTS
    directly addresses this friction; N otherwise.
    Must-have text (exact phrase): verbatim text from Artifact 1. Blank if N.
    Gap: if N, state absent requirement explicitly. N row + blank Gap = STRUCTURAL FAIL
    per second RULE row.
    Scout namespace: specific scout sub-skill for N rows. Blank if Y.

  CONVICTION DELTA
    Three rows only — CT-Spec, CT-Prop, CT-Pitch from INERTIA MODEL MAP. No anonymous
    version rows. Each row's Amplification chain anchors to the MAP starter for that
    Conv-ID. Replace all bracketed tokens. An unfilled bracket fails the row.

    | Conv-ID / Conviction type | Conviction established (one-sentence claim) | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|---------------------------------------------|---------------------|-----------------------------------------------------|
    | RULE | Each Conv-ID must match a named INERTIA MODEL MAP entry. A missing row is a named-conviction-type absence: CT-Pitch absent means Emotional conviction type is untracked, visible at a glance without count comparison. Do not add rows beyond MAP entries. | — | — |
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec starter]) → [Req-ID's factual claim from Must-have] → [how spec locked claim as factual record] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop starter]) → [Option A = INERTIA MODEL Cost stated explicitly] → [how recommended option prices against that baseline] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch starter]) → [Req-ID's factual claim made visceral] → [audience-specific emotional register applied] |

    Conviction established: the single claim this artifact establishes that the prior
    artifact could not — one sentence maximum.
    Grounding Req-ID(s): canonical Must-have identifier(s) from Artifact 1 REQUIREMENTS.
    Required per row. If no Must-have grounds a row: "GAP — [Req-ID] is closest anchor
    but does not ground CT-[X] conviction because [reason]."

  NEAR-DUPLICATE CONTENT
    Name any passage nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For "Conviction type met": Y if dominant register matches declared conviction type
(Factual for spec, Optionality for proposal, Emotional for pitch); partial if mixed;
N if primary register fails declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  For each row marked partial or N above: complete that artifact's pre-declared row in the
  diagnosis table. A row left blank when CLOSE shows partial or N is a structural
  incompleteness in this diagnosis. If all three CLOSE rows are Y, write
  "No conviction gaps detected." after the table.

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Sub-section where gap originates: specific named sub-section — not the artifact alone
  (e.g., "Spec REQUIREMENTS — Must-haves framed as prescriptions rather than documented facts").
  Register found: one word only — Factual, Optionality, or Emotional.
  Register declared: one word only. Structurally distinct columns — do not merge.
  Scout sub-skill: specific sub-skill identifier, not namespace alone (e.g.,
  scout-requirements, scout-feasibility, scout-positioning — not "scout").
  Evidence needed: one sentence describing the specific signal that closes this gap.

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-05 — Minimum-Density Full Compression

**Axis:** Lifecycle compression — all four RULE sentinel rows present at minimum viable
text density; all surrounding instructional prose stripped to the shortest form that
still identifies each table's role and cell-fill requirements. The structural tables
carry the full requirement burden; prose carries only what tables cannot express.

**Hypothesis:** C-42, C-43, C-44, and C-45 are structural placement properties — the
rubric tests whether a non-data RULE sentinel row appears inside each table, preceding
the data rows, with text declaring the binding constraint. Sentinel text density and
surrounding prose volume are confirmed non-load-bearing at the 253 ceiling level (D16
density invariance, V-05 R15). V-05 extends this test to the 263 ceiling: if the
traceability axis sentinels (C-44 SCOUT TRACEABILITY TABLE, C-45 TRACEABILITY AUDIT)
are structurally present at minimum text density, and all other structural properties
are preserved, the score should match V-02 and V-04. Predicted score: 263.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0. CAMPAIGN CONVICTION HYPOTHESIS:
   Hypothesis: "The {topic} campaign must establish that [friction from INERTIA MODEL Cost]
   is the dominant reason [audience] cannot [desired outcome], so displacing [INERTIA MODEL
   Name] becomes the obvious move."
   Falsification: (a) spec cannot document barrier as measured cost; (b) proposal cannot
   price barrier against alternative; (c) pitch cannot make barrier visceral per version.
   Complete before item 1.

1. Topic identity — feature name, audience, problem solved. One sentence.

2. INERTIA MODEL:
     Name:     current behavior shorthand
     Behavior: what users do today — one sentence
     Cost:     what that costs — one sentence (factual, priceable, emotional)
   Conviction map: Factual→spec; Optionality→proposal; Emotional→pitch.

3. Scout inventory — glob simulations/scout/ for this topic. Unconditional.

4. SCOUT TRACEABILITY TABLE — fill Friction + Scout File from scout-requirements;
   fill Req-ID + Must-have during Artifact 1:

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | RULE         | TRACEABILITY AUDIT must have one row per entry here. Missing row = R-[NN] absent. | — | — |
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (one row per friction; if none: one row, Friction from INERTIA MODEL Cost, file = "none")

5. INERTIA MODEL MAP — fill all cells before Artifact 1. CONVICTION DELTA row count must
   match this table. CT-[X] absent in REFLECTION = named-conviction-type absent.

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter     |
   |----------|----------|-----------------|---------------------------------|
   | RULE     | CONVICTION DELTA must have 3 rows: CT-Spec, CT-Prop, CT-Pitch. Missing = CT-[X] absent. No anonymous rows. | — | — |
   | CT-Spec  | Spec     | Factual         | (fill in)                       |
   | CT-Prop  | Proposal | Optionality     | (fill in)                       |
   | CT-Pitch | Pitch    | Emotional       | (fill in)                       |

6. Artifact contract matrix:

| Field           | Spec                                                     | Proposal                                                    | Pitch                                                              |
|-----------------|----------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL; scout-requirements        | Spec; INERTIA MODEL Cost; scout-feasibility                 | Proposal; INERTIA MODEL Cost; scout-positioning                    |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md           | simulations/draft/proposals/{topic}-proposal-{date}.md      | simulations/draft/pitches/{topic}-pitch-{date}.md                  |
| PRESERVE        | (first)                                                  | All spec decisions                                          | Recommended option                                                 |
| CARRIES FORWARD | Feature identity; INERTIA MODEL; decisions               | Recommended option + rationale; Cost                        | (final)                                                            |
| CONVICTION TYPE | Factual — Cost as factual record                         | Optionality — Cost priced against alternatives              | Emotional — Cost visceral per audience                             |

Print matrix. Do not begin Artifact 1 until printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: topic identity; INERTIA MODEL; scout-requirements. CONVICTION TYPE: Factual.

  PURPOSE — INERTIA MODEL Name/Behavior; Cost as factual record.
  REQUIREMENTS — MoSCoW (M/S/C/W). Each Must-have: complete Req-ID + SETUP row now.
  DESIGN — Components, data flow, decisions.
  CONSTRAINTS — Technical, team, timeline, dependencies.
  OPEN QUESTIONS — Unknowns; namespace per item.

GATE: Write simulations/draft/specs/{topic}-spec-{date}.md before Artifact 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: spec; INERTIA MODEL Cost; scout-feasibility. CONVICTION TYPE: Optionality.
Option A = do-nothing at full INERTIA MODEL Cost. State Cost before alternatives.
Three options min. Per option: Name / Description / Pros / Cons / Risk / Effort.
Recommendation: option + three reasons citing spec decisions.

GATE: Write simulations/draft/proposals/{topic}-proposal-{date}.md before Artifact 3.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: proposal; INERTIA MODEL Cost; scout-positioning. CONVICTION TYPE: Emotional.
Each version opens with INERTIA MODEL Cost as hook. Three versions:

EXEC — Cost in business terms; Cost elimination; compounding risk; CTA: approve/fund/unblock.
DEV  — Blocked capability; spec design referenced; technical debt; CTA: join beta/review spec.
MAKER — Daily friction; plain language; time saved; CTA: try it/sign up/start now.
ANTI-POSITIONING: two sentences — what this feature is NOT.

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md before Campaign Reflection.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After pitch file on disk. Retrospective only.

FINDINGS:

  TRACEABILITY AUDIT — one row per SETUP SCOUT TRACEABILITY TABLE row.
  Pre-fill Req-ID + Friction from SETUP before Artifact 1; complete rest after.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | RULE   | Each Req-ID must match a named SCOUT TRACEABILITY TABLE entry (SETUP). Missing = R-[NN] absent. | — | — | — | — |
    | RULE   | N + blank Gap = STRUCTURAL FAIL. | — | — | — | — |
    | R-01   | (copy from SETUP row 1)     | Y / N                    |                               |            |                 |
    | R-02   | (copy from SETUP row 2)     | Y / N                    |                               |            |                 |
    (match SETUP row count — do not reduce)

    Must-have found: Y = distinct Must-have covers friction; N = absent.
    Must-have text: verbatim. Blank if N.
    Gap: if N, state absent requirement. Blank + N = fail.
    Scout namespace: sub-skill for N rows. Blank if Y.

  CONVICTION DELTA — 3 rows from INERTIA MODEL MAP. No anonymous rows.

    | Conv-ID / Conviction type | Conviction established (one-sentence claim) | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|---------------------------------------------|---------------------|-----------------------------------------------------|
    | RULE | Each Conv-ID must match MAP entry. Missing = CT-[X] absent. No extra rows. | — | — |
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec]) → [Req-ID's factual claim] → [how spec locked it] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop]) → [Option A = INERTIA MODEL Cost] → [how recommendation prices it] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch]) → [claim made visceral] → [audience register] |

    No grounding: "GAP — [Req-ID] nearest; does not ground CT-[X] because [reason]."

  NEAR-DUPLICATE CONTENT — passage; what changed.
  RESIDUAL QUESTIONS — signal needed; namespace.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS — complete partial or N rows. Blank = fail. All Y: "No gaps."

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Register found / Register declared: one word each, distinct columns.
  Scout sub-skill: specific identifier, not namespace.
  Evidence needed: one sentence.

Open questions: namespace for each.
```
