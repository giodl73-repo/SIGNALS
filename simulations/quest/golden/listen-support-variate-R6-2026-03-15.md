# listen-support — Variations, Round 6 (rubric v6 — 21 criteria)

**Date:** 2026-03-15
**Rubric target:** v6 (C-01 through C-21 — 21 criteria; aspirational tier denominator = 13)
**Baseline:** R5 V-05 (composite 100 under v5; C-20/C-21 status under v6 unconfirmed)
**R6 objective:** Close the two new aspirational gaps that distinguish v6 from v5:
  - **C-20** — Headline-Level Vocabulary ID Annotation: the vocabulary ID must appear on the
    `##` headline line itself (not a subline). A scorer reading only `##` lines must identify
    the vocabulary ID without reading any subline or metadata line. Pass condition: >= 75% of
    ticket body `##` headline lines contain the vocabulary ID inline.
  - **C-21** — Complete Five-Item Pre-Flight Coverage: the vocabulary gate must check all 5
    items including item (e) inter-role register differentiation, each named and given an
    individual PASS/FAIL result. Gates checking only 4 items fail C-21 because item (e) is
    absent.

**The R5 gap analysis:**
- R5 V-01: Cell IDs in `##` headline (`*(Cell: XX-P#)*`) — C-20 PASS. 4-item gate — C-21
  FAIL (item e absent). Composite 100 under v5; 99.23 under v6.
- R5 V-02: VM Row ID in metadata subline (`- VM Row: ...`) — C-20 FAIL. 5-item gate with
  item (e) — C-21 PASS. Composite ~99.1 under v5; ~99.23 under v6.
- R5 V-04: Cell IDs in `##` headline + 5-item gate — C-20 PASS, C-21 PASS. Composite 100
  candidate under both v5 and v6, pending scorecard confirmation.
- R5 V-05: VM Row IDs in `##` headline + 5-item gate — C-20 PASS, C-21 PASS. Composite 100
  candidate under both v5 and v6, pending scorecard confirmation.

**R6 strategy:** The C-20/C-21 mechanisms exist in R5 V-04 and V-05. R6 addresses three
open questions: (1) whether the C-21 gate requires explicit letter-label formatting (a)-(e)
per item to guarantee scorer recognition; (2) whether a front-of-prompt Compliance Contract
is more reliable than step-level instructions; (3) whether CONSTRAINT MANIFEST and
VERIFICATION MANIFEST rows explicitly named for C-20/C-21 add output robustness.
Single-axis variations isolate these angles; combined variations stack them.

---

## Fixed Changes Applied to All Variations

All R6 variations inherit the full R5 V-05 mechanism set. These components are not the
differentiating axis in R6.

| Component | R5 V-05 source | R6 status |
|-----------|---------------|-----------|
| VOCABULARY MANIFEST with VM Row IDs (C-17) | R5 V-05 | Retained |
| CONSTRAINT MANIFEST + VERIFICATION MANIFEST (C-15) | R5 V-05 | Retained (extended in V-05) |
| Per-ticket commitment table referencing VM Row IDs (C-16) | R5 V-05 | Retained |
| VM Row ID in `##` headline annotation (C-18/C-20) | R5 V-05 | Strengthened by V-01/V-03/V-04/V-05 |
| 5-item VOCABULARY PRE-FLIGHT GATE (C-19/C-21) | R5 V-05 | Formalized by V-02/V-03/V-04/V-05 |
| Character-embodiment PERFORMANCE MODE with migration backstory (C-03) | R5 V-05 | Retained |
| Phase Map Table with severity/volume/register norms (C-14) | R5 all | Retained |
| Theme declaration before inventory (C-09) | R5 all | Retained |
| Role-Phase Cross-Matrix (C-12) | R5 all | Retained |
| Ticket inventory table + TABLE CHECK (C-01/C-02/C-05/C-11) | R5 all | Retained |
| Cross-ticket patterns (C-09) | R5 all | Retained |
| Resolution paths table (C-10) | R5 all | Retained |
| Gap analysis with T-NN refs (C-04/C-08) | R5 all | Retained |

---

## R6 Variation Axes

R1 explored: role sequence, output format, lifecycle emphasis.
R2 explored: phrasing register, inertia framing, theme-first generation.
R3 explored: vocabulary commitment from phase pools, manifest tables, role-phase matrix.
R4 explored: fusing C-16 (per-ticket commitment) with C-17 (role-phase matrix).
R5 explored: adding C-18 (3-node ID chain) and C-19 (standalone gate) to R4 V-05 base.
R5 V-04/V-05 are composite 100 candidates under v6 by predicted scoring. R6 targets open
questions left by R5 scoring ambiguity.

| Axis | Single-axis variation | New angle vs prior rounds | Target criteria |
|------|-----------------------|--------------------------|-----------------|
| Output format | V-01 | Explicit C-20 ZERO-EXCEPTION headline rule stated three times (STEP 3B, STEP 4, TABLE CHECK) + C-20 VERIFICATION MANIFEST row; 4-item gate retained | C-20 |
| Lifecycle emphasis | V-02 | Letter-labeled (a)-(e) gate with individual binary PASS/FAIL per item; item (e) prominently named; VM Row ID retained in metadata subline | C-21 |
| Phrasing register | V-03 | COMPLIANCE CONTRACT block at prompt header naming C-20 and C-21 as obligations before any steps; compliant header format sample in contract | C-20 + C-21 |

Combined: V-04 stacks V-01 (explicit C-20 headline rule) + V-02 (letter-labeled 5-item
gate). V-05 is full synthesis: R5 V-05 base + V-01 C-20 strengthening + V-02 C-21
formalism + CONSTRAINT MANIFEST and VERIFICATION MANIFEST rows for both C-20 and C-21.

---

## V-01 — Single Axis: Output Format (Explicit C-20 Headline Placement Rule)

**Axis:** Output format — the headline placement rule for the vocabulary ID is stated as a
ZERO-EXCEPTION constraint in three locations: STEP 3B (where the commitment table is built),
STEP 4 PERFORMANCE MODE (where bodies are declared), and TABLE CHECK (pre-body verification).
Rule text: "The `*(Cell: XX-P#)*` annotation MUST appear on the same line as `## T-NN —
{Title}`. It is NOT permitted on a subline or metadata line. A scorer reading only `##` lines
must see the Cell ID without opening any other line." A C-20 row is added to the VERIFICATION
MANIFEST. The gate has 4 items (C-21 FAIL — isolates C-20 axis).

**Hypothesis:** R5 V-01 places Cell IDs in the `##` headline and should PASS C-20. The open
question is whether model outputs consistently honor this placement without an explicit
prohibition on subline placement. Adding a ZERO-EXCEPTION constraint with the prohibition
stated explicitly reduces drift. C-21 FAIL is expected (4-item gate; item e absent).
Predicted composite: ~99.23 (C-21 FAIL), confirming V-01-class ceiling under v6.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### VOCABULARY MATRIX

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. Cell IDs are the shared identifier across all three levels: matrix row,
commitment table column, and body `##` headline annotation.**

Cell ID format: `{Role-abbrev}-P{phase}` — e.g., `SRE-P1`, `Sup-P2`, `UX-P3`, `Cxx-P1`.

| Cell ID  | Role    | Phase   | Register description                                                    | Example template phrase                                                                      |
|----------|---------|---------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure           | "I'm seeing [failure] only when [condition] — I cannot reproduce it on demand..."           |
| SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                    | "We've been running {topic} for [N] weeks and we just noticed [regression]..."              |
| Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly      | "I keep seeing customers hit [obstacle] when they first [action] — no guidance exists..."   |
| Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause       | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."               |
| Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold   | "This is the [N]th escalation about [failure] this month — I need a permanent fix..."       |
| PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast           | "First-time activation is lower than projected — I want to understand..."                   |
| PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                       | "The [metric] is not improving at the expected rate — I need to investigate..."             |
| PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                   | "I'm seeing users who completed onboarding dropping off at [stage]..."                       |
| UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..."             |
| UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                | "Session recordings show abandonment when users attempt [advanced action]..."               |
| UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability              | "Long-term users are filing feedback about [behavior change / reliability issue]..."        |
| Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present          | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks           | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time  | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                                 | Required                        | Committed value |
|-------------------------------------------------------------------|---------------------------------|-----------------|
| Total tickets                                                     | 6 to 12                         | ___             |
| Phase 1 tickets (day 0-30)                                        | >= 3                            | ___             |
| Phase 2 tickets (day 31-60)                                       | >= 2                            | ___             |
| Phase 3 tickets (day 61-90)                                       | >= 1                            | ___             |
| P0 ceiling                                                        | <= floor(total x 0.25) = ___    | ___             |
| High-volume ceiling                                               | <= floor(total x 0.50) = ___    | ___             |
| Distinct named personas                                           | >= 3                            | ___             |
| SRE tickets                                                       | >= 2                            | ___             |
| Support tickets                                                   | >= 2                            | ___             |
| C-xx tickets                                                      | >= 2 (max 2 per single C-xx)    | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                   | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                 | >= 1                            | ___             |
| Tickets with Cell ID in commitment table AND ## headline (C-20)   | = total ticket count            | ___             |

Do not proceed until the Constraint Manifest is complete.

---

### STEP 1 -- Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 -- Phase Map Table

| Phase   | Window    | Severity norm | Volume norm  | Body register                        |
|---------|-----------|---------------|--------------|--------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium  | Discovery/setup -- use xxx-P1 cells  |
| Phase 2 | day 31-60 | P1/P2         | medium       | Integration/edge -- use xxx-P2 cells |
| Phase 3 | day 61-90 | P0/P1         | low/medium   | Operational/reliability -- use xxx-P3 cells |

---

### STEP 3 -- Theme Declaration

```
Theme A: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

Theme B: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

[Theme C if needed -- same format]
```

Each theme must have a distinct underlying failure. Sum of counts = Constraint Manifest total.

---

### STEP 3A -- Role-Phase Cross-Matrix

| Role    | Phase 1 | Phase 2 | Phase 3 | Total | Theme(s) |
|---------|---------|---------|---------|-------|----------|
| SRE     | ___     | ___     | ___     | ___   | ___      |
| Support | ___     | ___     | ___     | ___   | ___      |
| PM      | ___     | ___     | ___     | ___   | ___      |
| UX      | ___     | ___     | ___     | ___   | ___      |
| C-xx    | ___     | ___     | ___     | ___   | ___      |

Constraint 1: SRE >= 2, Support >= 2, PM >= 1, UX >= 1, C-xx >= 2
Constraint 2: Any role with 3+ tickets must span at least 2 phases
Constraint 3: Any single C-xx persona in at most 2 tickets

---

### STEP 3B -- Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. Record the Cell ID from the Vocabulary Matrix.
Derive the committed opening phrase from that cell's template. The body MUST begin with its
committed phrase (expanded -- not verbatim).**

**C-20 RULE -- ZERO EXCEPTIONS: The body header *(Cell: XX-P#)* annotation MUST appear on
the same line as ## T-NN -- {Title}. It is NOT permitted on a subline or metadata line.
A scorer reading only ## lines must see the Cell ID without opening any other line. Every
ticket in this table must produce a ## line with the Cell ID inline.**

| T-ID | Cell ID  | Phase     | Committed opening phrase |
|------|----------|-----------|--------------------------|
| T-01 | ___-P___ | Phase ___ | "___" |
| T-02 | ___-P___ | Phase ___ | "___" |
| T-03 | ___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT CHECK

**Execute before writing any ticket body. Check all four items. Body generation is blocked
if any check fails -- revise before continuing.**

**Check 1 -- Vocabulary Matrix completeness**
Every (Role, Phase) combination in the inventory has a Cell ID row in the Vocabulary Matrix.
State: [ PASS -- all ___ combinations have matrix cells ] / [ FAIL -- missing: ___ ]

**Check 2 -- Commitment table completeness**
Row count in STEP 3B equals committed ticket total in the Constraint Manifest.
State: [ PASS -- ___ rows = ___ tickets ] / [ FAIL -- ___ rows != ___ tickets ]

**Check 3 -- Phrase-to-cell traceability**
Each committed phrase in STEP 3B is derivable from the Example template of its Cell ID
(same role, same phase, same register).
State: [ PASS -- all ___ phrases traceable ] / [ FAIL -- untraceable: T-___ ]

**Check 4 -- Phase-register alignment**
All Phase 1 phrases use P1-cell registers (discovery/setup). At least one Phase 3 phrase
uses a P3-cell register (operational/reliability).
State: [ PASS ] / [ FAIL -- misaligned T-IDs: ___ ]

**PRE-FLIGHT RESULT:** [ ALL PASS -- proceed to PERFORMANCE MODE ] / [ BLOCKED -- N checks failed ]

---

### STEP 4 -- PERFORMANCE MODE DECLARATION

**You are about to become each persona. They know what they migrated from.**

**SRE:** You are on-call. You adopted {topic} because the team moved to it. You knew the
prior system's failure modes cold; this one is still opaque to you. Something is breaking
silently that you would have caught immediately in the old system. Methodical but frustrated.

**Support:** You have answered this same migration question multiple times this week. You know
what the old approach expected; {topic} does something different that users keep tripping over.
You are filing this ticket to get engineering to fix the root cause.

**PM:** Adoption is below forecast. You cannot tell if it is a product problem or a
communication problem. You are filing this to request data.

**UX:** You are watching session recordings and seeing users stall at a specific point. The
old approach had a familiar affordance here; the new one does not. You know the friction point
by location; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach in Step 1] recently. Something surprised you --
either something that used to work stopped working, or something you expected to just work
required extra setup. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Begin each body with the committed phrase from STEP 3B (expanded into a full opening sentence).
C-20 RULE -- ZERO EXCEPTIONS: Output ## T-NN -- {Title} *(Cell: XX-P#)* with the Cell ID
annotation on the ## headline line. Not on a subline. Not on a metadata row. A scorer
reading only ## lines must see the Cell ID.
Register must match the Vocabulary Matrix cell. Registers must differ between roles in the
same phase. Where migration-relevant: reference what was expected from the old approach.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK -- verify all before proceeding:
- Total rows: ___ (required: matches Constraint Manifest)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= Manifest ceiling)
- High-volume count: ___ (required: <= Manifest ceiling)
- Theme/phase counts match Step 3 and Manifest: MATCH / MISMATCH
- Every STEP 3B row has a valid Cell ID from the Vocabulary Matrix: Y / N
- C-20 check: every ## headline will carry *(Cell: XX-P#)* inline (NOT a subline): Y / N

If any check fails: revise before continuing.

---

### STEP 6 -- Ticket Bodies (by theme, phase-sorted, ascending T-ID)

```
### Theme A -- {theme name}
*Underlying failure: {from Step 3}*

## T-NN -- {Title} *(Cell: XX-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences. First person. Committed phrase expanded into opening sentence.
Register matches Cell ID. Registers differ between roles in same phase.
Migration reference where relevant.
C-20: Cell ID is on the ## line above -- not on any subline.]
```

---

### STEP 7 -- Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|

---

### STEP 7B -- Resolution Paths

For every high-volume OR P0/P1 ticket:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|

---

### STEP 8 -- Gap Analysis

All entries require Tickets: T-NN, T-NN.

**Documentation gaps** | Entry | Tickets | Artifact

**Design gaps** | Entry | Tickets | Change required

**Operational gaps** | Entry | Tickets | Process change required

Minimum 2 entries per gap category.

---

### VERIFICATION MANIFEST

| Verification target | Required | Actual | Pass? |
|--------------------|----------|--------|-------|
| Total tickets generated | = Constraint Manifest | ___ | ___ |
| Distinct categories | >= 2 | ___ | ___ |
| Distinct personas | >= 3 | ___ | ___ |
| P0 count | <= ceiling | ___ | ___ |
| High-volume count | <= ceiling | ___ | ___ |
| Bodies starting with committed phrase | = total | ___ | ___ |
| ## headlines with *(Cell: XX-P#)* inline -- C-20 | = total | ___ | ___ |
| Cell IDs in headlines resolve to commitment table rows | = total | ___ | ___ |
| Cell IDs in commitment table resolve to matrix cells | = total | ___ | ___ |
| No third-person role reference | = total | ___ | ___ |
| Phase 1 bodies use discovery register | >= 3 | ___ | ___ |
| Phase 3 bodies use operational register | >= 1 | ___ | ___ |

---

---

## V-02 -- Single Axis: Lifecycle Emphasis (Letter-Labeled 5-Item Gate for C-21)

**Axis:** Lifecycle emphasis -- the VOCABULARY PRE-FLIGHT GATE is restructured so each of
the 5 items is labeled with a letter (a) through (e) and given an explicit individual PASS
or FAIL binary state. Item (e) is named "inter-role register differentiation" and requires
citing two roles in the same phase with different register descriptions by VM Row ID. The
gate declares GATE: OPEN or GATE: CLOSED after all five item states. VM Row IDs are retained
in the metadata subline (not the ## headline) -- C-20 FAIL isolates the C-21 axis.

**Hypothesis:** R5 V-02's gate has 5 items and item (e) present, and should already PASS
C-21. The open question is whether the absence of letter labels allows a scorer to count
only 4 items if item (e) is not prominently named. Adding letter labels (a)-(e) makes item
(e) impossible to overlook. C-20 FAIL expected because VM Row ID remains in the metadata
subline. Predicted composite: ~99.23, matching V-01-class ceiling from the other direction.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. VM Row IDs appear in this manifest, the commitment table (STEP 3B), and body
metadata sublines.**

| VM Row ID   | Role    | Phase   | Register description                                                   | Example template phrase                                                                      |
|-------------|---------|---------|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure          | "I'm seeing [failure] only when [condition] -- I cannot reproduce it on demand..."          |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                   | "We've been running {topic} for [N] weeks and we just noticed [regression]..."              |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly     | "I keep seeing customers hit [obstacle] when they first [action] -- no guidance exists..."  |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause      | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."               |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold  | "This is the [N]th escalation about [failure] this month -- I need a permanent fix..."      |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast          | "First-time activation is lower than projected -- I want to understand..."                  |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                      | "The [metric] is not improving at the expected rate -- I need to investigate..."            |
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                  | "I'm seeing users who completed onboarding dropping off at [stage]..."                       |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..."             |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action               | "Session recordings show abandonment when users attempt [advanced action]..."               |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability             | "Long-term users are filing feedback about [behavior change / reliability issue]..."        |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present         | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks          | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                         | Required                        | Committed value |
|-----------------------------------------------------------|---------------------------------|-----------------|
| Total tickets                                             | 6 to 12                         | ___             |
| Phase 1 tickets (day 0-30)                                | >= 3                            | ___             |
| Phase 2 tickets (day 31-60)                               | >= 2                            | ___             |
| Phase 3 tickets (day 61-90)                               | >= 1                            | ___             |
| P0 ceiling                                                | <= floor(total x 0.25) = ___    | ___             |
| High-volume ceiling                                       | <= floor(total x 0.50) = ___    | ___             |
| Distinct named personas                                   | >= 3                            | ___             |
| SRE tickets                                               | >= 2                            | ___             |
| Support tickets                                           | >= 2                            | ___             |
| C-xx tickets                                              | >= 2 (max 2 per single C-xx)    | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)           | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary (C-14)         | >= 1                            | ___             |
| Tickets with VM Row ID in commitment table (C-16)         | = total ticket count            | ___             |

Do not proceed until the Constraint Manifest is complete.

---

### STEP 1 -- Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 -- Phase Map Table

| Phase   | Window    | Severity norm | Volume norm  | Body register                           |
|---------|-----------|---------------|--------------|-----------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium  | Discovery/setup -- use VM-xxx-P1 rows   |
| Phase 2 | day 31-60 | P1/P2         | medium       | Integration/edge -- use VM-xxx-P2 rows  |
| Phase 3 | day 61-90 | P0/P1         | low/medium   | Operational/reliability -- use VM-xxx-P3 rows |

---

### STEP 3 -- Theme Declaration

```
Theme A: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

Theme B: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___
```

---

### STEP 3A -- Role-Phase Cross-Matrix

| Role    | Phase 1 | Phase 2 | Phase 3 | Total | Theme(s) |
|---------|---------|---------|---------|-------|----------|
| SRE     | ___     | ___     | ___     | ___   | ___      |
| Support | ___     | ___     | ___     | ___   | ___      |
| PM      | ___     | ___     | ___     | ___   | ___      |
| UX      | ___     | ___     | ___     | ___   | ___      |
| C-xx    | ___     | ___     | ___     | ___   | ___      |

Constraint 1: SRE >= 2, Support >= 2, PM >= 1, UX >= 1, C-xx >= 2
Constraint 2: Any role with 3+ tickets must span at least 2 phases
Constraint 3: Any single C-xx persona in at most 2 tickets

---

### STEP 3B -- Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. Reference the VOCABULARY MANIFEST VM Row ID.
Derive the committed phrase from that row's template. The body MUST begin with its committed
phrase (expanded). The body header shows VM Row ID in the metadata subline (not in the ##
headline) for this variation.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate. Execute after STEP 3B, before STEP 4. Check all five items (a)-(e). Each
item names the artifact it validates and declares PASS or FAIL individually. Declare GATE:
OPEN or GATE: CLOSED. Body generation is blocked if the gate is CLOSED.**

**(a) VOCABULARY MANIFEST completeness**
Every (Role, Phase) combination in the inventory has a row in the VOCABULARY MANIFEST (not
marked N/A).
State: [ PASS -- all ___ combinations have rows ] / [ FAIL -- missing: ___ ]

**(b) Commitment table completeness**
STEP 3B row count = committed ticket total in the CONSTRAINT MANIFEST.
State: [ PASS -- STEP 3B has ___ rows = ___ ] / [ FAIL -- ___ rows != ___ ]

**(c) Phrase-to-manifest traceability**
Each STEP 3B committed phrase derives from the Example template of its VM Row ID in the
VOCABULARY MANIFEST (same role, same phase, same register description).
State: [ PASS -- all ___ phrases traceable ] / [ FAIL -- untraceable: T-___ (VM Row ID: ___) ]

**(d) Phase-register alignment**
All Phase 1 phrases use VM-xxx-P1 discovery register. At least one Phase 3 phrase uses
VM-xxx-P3 operational register.
State: [ PASS ] / [ FAIL -- Phase 1 misaligned: T-___ ; Phase 3 missing ]

**(e) Inter-role register differentiation**
In at least one phase, two or more roles have distinct register descriptions in the
VOCABULARY MANIFEST. Cite the example explicitly:
  Phase ___: VM Row ___ (Role: ___) = "___ register description"
  Phase ___: VM Row ___ (Role: ___) = "___ register description"
State: [ PASS -- example cited above ] / [ FAIL -- no differentiating phase found ]

**GATE: [ OPEN -- (a)(b)(c)(d)(e) all PASS -- proceed to STEP 4 PERFORMANCE MODE ]**
**GATE: [ CLOSED -- ___ items failed -- revise and re-run before continuing ]**

---

### STEP 4 -- PERFORMANCE MODE DECLARATION

**You are about to become each persona. They know what they migrated from.**

**SRE:** On-call. Adopted {topic} because the team moved to it. The prior system's failure
modes were familiar; this one is opaque. Something is breaking silently. Methodical but
frustrated.

**Support:** Answered this same migration question multiple times this week. Old approach
behaved differently. Filing this to get engineering to fix the root cause.

**PM:** Adoption below forecast. Cannot tell if product problem or communication problem.
Filing to request data.

**UX:** Watching session recordings. Users stall at a specific point. Old approach had a
familiar affordance here. Need engineering to understand root cause.

**C-xx:** Switched from [old approach] recently. Something surprised you. You do not know
if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Begin each body with the committed phrase from STEP 3B (expanded into a full opening sentence).
Body header format:**
```
## T-NN -- {Title}
- VM Row: {VM Row ID from STEP 3B} | Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N
- Committed phrase: "{phrase}"
```
**Register must match the VOCABULARY MANIFEST row. Registers MUST differ between roles in
the same phase -- confirmed in gate item (e). Migration reference where relevant.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume within Constraint Manifest: MATCH / FAIL
- All STEP 3B rows have valid VM Row IDs: Y / N
- Gate (a)-(e) all PASS: Y / N

---

### STEP 6 -- Ticket Bodies (by theme, phase-sorted, ascending T-ID)

```
## T-NN -- {Title}
- VM Row: VM-xxx-P# | Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N
- Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences. First person. Committed phrase expanded into opening sentence.
Register matches VM Row ID. Inter-role register differentiation in force per gate item (e).
Migration reference where relevant.]
```

---

### STEP 7 -- Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|

---

### STEP 7B -- Resolution Paths

For every high-volume OR P0/P1 ticket:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|

---

### STEP 8 -- Gap Analysis

**Documentation gaps** | Entry | Tickets: T-NN | Artifact
**Design gaps** | Entry | Tickets: T-NN | Change
**Operational gaps** | Entry | Tickets: T-NN | Process change

Minimum 2 entries per gap category.

---

### VERIFICATION MANIFEST

| Verification target | Required | Actual | Pass? |
|--------------------|----------|--------|-------|
| Total tickets | = Constraint Manifest | ___ | ___ |
| Distinct categories | >= 2 | ___ | ___ |
| Distinct personas | >= 3 | ___ | ___ |
| Bodies starting with committed phrase | = total | ___ | ___ |
| VM Row IDs in metadata sublines | = total | ___ | ___ |
| Gate items (a)-(e) all PASS -- C-21 | = 5 | ___ | ___ |
| Item (e) inter-role example cited | = 1 | ___ | ___ |
| No third-person role reference | = total | ___ | ___ |
| Phase 1 discovery register | >= 3 | ___ | ___ |
| Phase 3 operational register | >= 1 | ___ | ___ |

---

---

## V-03 -- Single Axis: Phrasing Register (Compliance Contract for C-20 + C-21)

**Axis:** Phrasing register -- a COMPLIANCE CONTRACT block is placed at the very top of the
prompt, before any step. It names C-20 and C-21 explicitly as obligations, states the pass
condition for each in a single declarative sentence, and provides a sample compliant body
header. The contract is the canonical source for both rules; they are not restated inside
STEP 3B or STEP 4. The gate uses letter labels (a)-(e). Tests whether front-loading
compliance obligations at the earliest position produces better adherence than embedding
the rules in step-level instructions.

**Hypothesis:** Instructions embedded inside step-level blocks may be forgotten by the time
bodies are generated, especially in long outputs. A compliance contract read first stays
as a top-level obligation. If model outputs drift on C-20 placement or C-21 item count,
the contract provides a correction anchor at the earliest position. Expected: C-20 PASS
(contract states the ## headline rule); C-21 PASS (contract states 5-item requirement with
letter labels). Composite 100 candidate.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### COMPLIANCE CONTRACT

**Read before any step. These two obligations govern the entire output.**

**C-20 -- Vocabulary ID in ## headline:**
Every ticket body ## headline must include the VM Row ID as an inline annotation on the same
line as the title: ## T-NN -- {Title} *(VM: VM-xxx-P#)*. The annotation is NOT permitted on
any subline, bullet, or metadata row. A scorer reading only ## lines must see the VM Row ID
without opening any other line.

**C-21 -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item
(e) is named "inter-role register differentiation" and requires citing two roles in the same
phase with distinct register descriptions. A gate with only four items fails because item (e)
is absent.

**Compliant body header format:**
```
## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"
```

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. VM Row IDs appear in this manifest, the commitment table, and the ## headline
annotation (per Compliance Contract C-20).**

| VM Row ID   | Role    | Phase   | Register description                                                   | Example template phrase                                                                      |
|-------------|---------|---------|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure          | "I'm seeing [failure] only when [condition] -- I cannot reproduce it on demand..."          |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                   | "We've been running {topic} for [N] weeks and we just noticed [regression]..."              |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly     | "I keep seeing customers hit [obstacle] when they first [action] -- no guidance exists..."  |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause      | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."               |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold  | "This is the [N]th escalation about [failure] this month -- I need a permanent fix..."      |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast          | "First-time activation is lower than projected -- I want to understand..."                  |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                      | "The [metric] is not improving at expected rate -- I need to investigate..."                |
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                  | "I'm seeing users who completed onboarding dropping off at [stage]..."                       |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..."             |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action               | "Session recordings show abandonment when users attempt [advanced action]..."               |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability             | "Long-term users are filing feedback about [behavior change / reliability issue]..."        |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present         | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks          | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                                | Required                        | Committed value |
|------------------------------------------------------------------|---------------------------------|-----------------|
| Total tickets                                                    | 6 to 12                         | ___             |
| Phase 1 tickets (day 0-30)                                       | >= 3                            | ___             |
| Phase 2 tickets (day 31-60)                                      | >= 2                            | ___             |
| Phase 3 tickets (day 61-90)                                      | >= 1                            | ___             |
| P0 ceiling                                                       | <= floor(total x 0.25) = ___    | ___             |
| High-volume ceiling                                              | <= floor(total x 0.50) = ___    | ___             |
| Distinct named personas                                          | >= 3                            | ___             |
| SRE tickets                                                      | >= 2                            | ___             |
| Support tickets                                                  | >= 2                            | ___             |
| C-xx tickets                                                     | >= 2 (max 2 per single C-xx)    | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                  | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                | >= 1                            | ___             |
| Tickets with VM Row ID in commitment table (C-16)                | = total ticket count            | ___             |
| Tickets with VM Row ID in ## headline (Compliance Contract C-20) | = total ticket count            | ___             |

Do not proceed until the Constraint Manifest is complete.

---

### STEP 1 -- Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 -- Phase Map Table

| Phase   | Window    | Severity norm | Volume norm  | Body register                           |
|---------|-----------|---------------|--------------|-----------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium  | Discovery/setup -- use VM-xxx-P1 rows   |
| Phase 2 | day 31-60 | P1/P2         | medium       | Integration/edge -- use VM-xxx-P2 rows  |
| Phase 3 | day 61-90 | P0/P1         | low/medium   | Operational/reliability -- use VM-xxx-P3 rows |

---

### STEP 3 -- Theme Declaration

```
Theme A: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

Theme B: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___
```

Each theme must have a distinct underlying failure.

---

### STEP 3A -- Role-Phase Cross-Matrix

| Role    | Phase 1 | Phase 2 | Phase 3 | Total | Theme(s) |
|---------|---------|---------|---------|-------|----------|
| SRE     | ___     | ___     | ___     | ___   | ___      |
| Support | ___     | ___     | ___     | ___   | ___      |
| PM      | ___     | ___     | ___     | ___   | ___      |
| UX      | ___     | ___     | ___     | ___   | ___      |
| C-xx    | ___     | ___     | ___     | ___   | ___      |

Constraint 1: SRE >= 2, Support >= 2, PM >= 1, UX >= 1, C-xx >= 2
Constraint 2: Any role with 3+ tickets must span at least 2 phases
Constraint 3: Any single C-xx persona in at most 2 tickets

---

### STEP 3B -- Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. Reference the VOCABULARY MANIFEST VM Row ID.
Derive the committed phrase from that row's template. Body MUST begin with committed phrase
(expanded). Compliance Contract C-20 governs body header format -- VM Row ID in ## headline.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate -- Compliance Contract C-21 governs this section. Execute after STEP 3B,
before STEP 4. All five items (a)-(e) must be present with individual PASS/FAIL states.
GATE: OPEN or GATE: CLOSED. Body generation blocked if CLOSED.**

**(a) VOCABULARY MANIFEST completeness**
Every (Role, Phase) combination in the inventory has a VOCABULARY MANIFEST row (not N/A).
State: [ PASS ] / [ FAIL -- missing: ___ ]

**(b) Commitment table completeness**
STEP 3B row count = CONSTRAINT MANIFEST committed total.
State: [ PASS -- ___ rows = ___ ] / [ FAIL -- ___ rows != ___ ]

**(c) Phrase-to-manifest traceability**
Each STEP 3B phrase derives from the template phrase of its VOCABULARY MANIFEST VM Row ID.
State: [ PASS -- all ___ traceable ] / [ FAIL -- untraceable: T-___ ]

**(d) Phase-register alignment**
All Phase 1 phrases use VM-xxx-P1 discovery register; at least one Phase 3 phrase uses
VM-xxx-P3 operational register.
State: [ PASS ] / [ FAIL -- misaligned: T-___ ]

**(e) Inter-role register differentiation**
In at least one phase, two or more roles have distinct register descriptions. Cite by
VM Row ID:
  Phase ___: VM Row ___ (Role: ___) = "___ register description"
  Phase ___: VM Row ___ (Role: ___) = "___ register description"
State: [ PASS -- example cited above ] / [ FAIL -- no differentiating phase found ]

**GATE: [ OPEN -- (a)(b)(c)(d)(e) all PASS -- proceed to STEP 4 ]**
**GATE: [ CLOSED -- ___ items failed -- revise and re-run ]**

---

### STEP 4 -- PERFORMANCE MODE DECLARATION

**You are about to become each persona. They know what they migrated from.**

**SRE:** On-call. Adopted {topic} because the team moved to it. Prior system's failure modes
were familiar; this one is opaque. Something is breaking silently. Methodical but frustrated.

**Support:** Answered this same migration question multiple times this week. Filing to get
engineering to fix the root cause so you stop being the manual workaround.

**PM:** Adoption below forecast. Cannot tell if product problem or communication problem.
Filing to request data.

**UX:** Watching session recordings. Users stall at a specific point. Old approach had a
familiar affordance here. Need engineering to understand root cause.

**C-xx:** Switched from [old approach in Step 1] recently. Something surprised you. You do
not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Begin each body with the committed phrase from STEP 3B (expanded into a full opening sentence).
Use the compliant header format from the Compliance Contract:
  ## T-NN -- {Title} *(VM: VM-xxx-P#)*  <- VM Row ID on ## line, per C-20.
Register must match the VOCABULARY MANIFEST row. Registers MUST differ between roles in the
same phase -- confirmed in gate item (e). Migration reference where relevant.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume within ceilings: MATCH / FAIL
- All STEP 3B rows have valid VM Row IDs: Y / N
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline: Y / N
- Compliance Contract C-21: gate items (a)-(e) all PASS: Y / N

---

### STEP 6 -- Ticket Bodies (by theme, phase-sorted, ascending T-ID)

```
### Theme A -- {theme name}
*Underlying failure: {from Step 3}*

## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences. First person. Committed phrase expanded into opening sentence.
Register matches VOCABULARY MANIFEST row. Inter-role differentiation per gate item (e).
Migration reference where relevant.
C-20: VM Row ID is in the ## line above per Compliance Contract.]
```

---

### STEP 7 -- Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|

---

### STEP 7B -- Resolution Paths

For every high-volume OR P0/P1 ticket:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|

---

### STEP 8 -- Gap Analysis

All entries require Tickets: T-NN, T-NN.

**Documentation gaps** | Entry | Tickets | Artifact
**Design gaps** | Entry | Tickets | Change
**Operational gaps** | Entry | Tickets | Process change

Minimum 2 entries per gap category.

---

### VERIFICATION MANIFEST

| Verification target | Required | Actual | Pass? |
|--------------------|----------|--------|-------|
| Total tickets | = Constraint Manifest | ___ | ___ |
| Distinct categories | >= 2 | ___ | ___ |
| Distinct personas | >= 3 | ___ | ___ |
| Bodies starting with committed phrase | = total | ___ | ___ |
| ## headlines with *(VM: VM-xxx-P#)* inline -- C-20 | = total | ___ | ___ |
| VM Row IDs in headlines resolve to STEP 3B rows | = total | ___ | ___ |
| VM Row IDs in STEP 3B resolve to VOCABULARY MANIFEST rows | = total | ___ | ___ |
| Gate items (a)-(e) all PASS -- C-21 | = 5 | ___ | ___ |
| Item (e) inter-role example explicitly cited | = 1 | ___ | ___ |
| No third-person role reference | = total | ___ | ___ |
| Phase 1 discovery register | >= 3 | ___ | ___ |
| Phase 3 operational register | >= 1 | ___ | ___ |

---

---

## V-04 -- Combined: V-01 (Explicit C-20 Rule) + V-02 (Letter-Labeled 5-Item Gate)

**Combination axis:**
1. From V-01: Cell IDs in compact Role-P# format; explicit C-20 ZERO-EXCEPTION rule stated
   in STEP 3B, STEP 4, and TABLE CHECK; C-20 row added to VERIFICATION MANIFEST.
2. From V-02: Vocabulary gate with letter labels (a)-(e); each item has individual PASS/FAIL
   binary state; item (e) named "inter-role register differentiation"; GATE: OPEN/CLOSED.

**Hypothesis:** V-01 achieves C-20 PASS (explicit headline placement rule) but C-21 FAIL
(4-item gate). V-02 achieves C-21 PASS (letter-labeled 5-item gate) but C-20 FAIL (subline
ID). Stacking both: C-20 PASS + C-21 PASS. Minimum-change combination that closes both gaps.
Expected composite: 100 under v6.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### VOCABULARY MATRIX

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. Cell IDs are the shared identifier across all three levels: matrix row,
commitment table column, and body ## headline annotation.**

Cell ID format: Role-abbrev-P#. Examples: SRE-P1, Sup-P2, UX-P3, Cxx-P1.

| Cell ID  | Role    | Phase   | Register description                                                    | Example template phrase                                                                      |
|----------|---------|---------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure           | "I'm seeing [failure] only when [condition] -- I cannot reproduce it on demand..."          |
| SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                    | "We've been running {topic} for [N] weeks and we just noticed [regression]..."              |
| Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly      | "I keep seeing customers hit [obstacle] when they first [action] -- no guidance exists..."  |
| Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause       | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."               |
| Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold   | "This is the [N]th escalation about [failure] this month -- I need a permanent fix..."      |
| PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast           | "First-time activation is lower than projected -- I want to understand..."                  |
| PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                       | "The [metric] is not improving -- I need to investigate..."                                 |
| PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                   | "I'm seeing users who completed onboarding dropping off at [stage]..."                       |
| UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..."             |
| UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                | "Session recordings show abandonment when users attempt [advanced action]..."               |
| UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability              | "Long-term users are filing feedback about [behavior change / reliability issue]..."        |
| Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present          | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks           | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time  | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                                   | Required                        | Committed value |
|---------------------------------------------------------------------|---------------------------------|-----------------|
| Total tickets                                                       | 6 to 12                         | ___             |
| Phase 1 tickets (day 0-30)                                          | >= 3                            | ___             |
| Phase 2 tickets (day 31-60)                                         | >= 2                            | ___             |
| Phase 3 tickets (day 61-90)                                         | >= 1                            | ___             |
| P0 ceiling                                                          | <= floor(total x 0.25) = ___    | ___             |
| High-volume ceiling                                                 | <= floor(total x 0.50) = ___    | ___             |
| Distinct named personas                                             | >= 3                            | ___             |
| SRE tickets                                                         | >= 2                            | ___             |
| Support tickets                                                     | >= 2                            | ___             |
| C-xx tickets                                                        | >= 2 (max 2 per single C-xx)    | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                     | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                   | >= 1                            | ___             |
| Tickets with Cell ID in commitment table AND ## headline (C-20)     | = total ticket count            | ___             |

Do not proceed until the Constraint Manifest is complete.

---

### STEP 1 -- Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 -- Phase Map Table

| Phase   | Window    | Severity norm | Volume norm  | Body register                        |
|---------|-----------|---------------|--------------|--------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium  | Discovery/setup -- use xxx-P1 cells  |
| Phase 2 | day 31-60 | P1/P2         | medium       | Integration/edge -- use xxx-P2 cells |
| Phase 3 | day 61-90 | P0/P1         | low/medium   | Operational/reliability -- use xxx-P3 cells |

---

### STEP 3 -- Theme Declaration

```
Theme A: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

Theme B: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___
```

---

### STEP 3A -- Role-Phase Cross-Matrix

| Role    | Phase 1 | Phase 2 | Phase 3 | Total | Theme(s) |
|---------|---------|---------|---------|-------|----------|
| SRE     | ___     | ___     | ___     | ___   | ___      |
| Support | ___     | ___     | ___     | ___   | ___      |
| PM      | ___     | ___     | ___     | ___   | ___      |
| UX      | ___     | ___     | ___     | ___   | ___      |
| C-xx    | ___     | ___     | ___     | ___   | ___      |

Constraint 1: SRE >= 2, Support >= 2, PM >= 1, UX >= 1, C-xx >= 2
Constraint 2: Any role with 3+ tickets must span at least 2 phases
Constraint 3: Any single C-xx persona in at most 2 tickets

---

### STEP 3B -- Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. Record the Cell ID from the Vocabulary Matrix.
Derive the committed phrase from that cell's template. The body MUST begin with its committed
phrase (expanded).**

**C-20 RULE -- ZERO EXCEPTIONS: The *(Cell: XX-P#)* annotation MUST appear on the same line
as ## T-NN -- {Title}. It is NOT permitted on a subline or metadata line. A scorer reading
only ## lines must see the Cell ID without opening any other line.**

| T-ID | Cell ID  | Phase     | Committed opening phrase |
|------|----------|-----------|--------------------------|
| T-01 | ___-P___ | Phase ___ | "___" |
| T-02 | ___-P___ | Phase ___ | "___" |
| T-03 | ___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate. Execute after STEP 3B, before STEP 4. Check all five items (a)-(e). Each
item names the artifact it validates and declares PASS or FAIL individually. GATE: OPEN or
GATE: CLOSED. Body generation blocked if CLOSED.**

**(a) Vocabulary Matrix completeness**
Every (Role, Phase) combination in the inventory has a Cell ID row in the Vocabulary Matrix.
State: [ PASS -- all ___ combinations have matrix cells ] / [ FAIL -- missing: ___ ]

**(b) Commitment table completeness**
STEP 3B row count = committed ticket total in Constraint Manifest.
State: [ PASS -- ___ rows = ___ tickets ] / [ FAIL -- ___ rows != ___ tickets ]

**(c) Phrase-to-cell traceability**
Each STEP 3B committed phrase is derivable from the Example template of its Cell ID
(same role, phase, register).
State: [ PASS -- all ___ traceable ] / [ FAIL -- untraceable: T-___ ]

**(d) Phase-register alignment**
All Phase 1 phrases use P1-cell registers. At least one Phase 3 phrase uses a P3-cell
register.
State: [ PASS ] / [ FAIL -- misaligned: T-___ ]

**(e) Inter-role register differentiation**
In at least one phase, two or more roles have distinct register descriptions in the
Vocabulary Matrix. Cite the example:
  Phase ___: Cell ___ (Role: ___) = "___ register description"
  Phase ___: Cell ___ (Role: ___) = "___ register description"
State: [ PASS -- example cited ] / [ FAIL -- no differentiating phase found ]

**GATE: [ OPEN -- (a)(b)(c)(d)(e) all PASS -- proceed to STEP 4 PERFORMANCE MODE ]**
**GATE: [ CLOSED -- ___ items failed -- revise and re-run ]**

---

### STEP 4 -- PERFORMANCE MODE DECLARATION

**You are about to become each persona. They know what they migrated from.**

**SRE:** On-call. Adopted {topic} because the team moved to it. Prior system's failure modes
were familiar; this one is opaque. Something breaking silently. Methodical but frustrated.

**Support:** Answered this same migration question multiple times this week. Filing to get
engineering to fix the root cause.

**PM:** Adoption below forecast. Cannot tell if product problem or communication problem.
Filing to request data.

**UX:** Watching session recordings. Users stall at a specific point. Need engineering to
understand root cause.

**C-xx:** Switched from [old approach in Step 1] recently. Something surprised you. Do not
know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Begin each body with the committed phrase from STEP 3B (expanded into a full opening sentence).
C-20 RULE -- ZERO EXCEPTIONS: Output ## T-NN -- {Title} *(Cell: XX-P#)* with the Cell ID
annotation on the ## headline line. Not on a subline. Not on a metadata row.
Register must match the Vocabulary Matrix cell. Registers MUST differ between roles in the
same phase -- confirmed in gate item (e). Migration reference where relevant.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume within ceilings: MATCH / FAIL
- Every STEP 3B row has a valid Cell ID from the Vocabulary Matrix: Y / N
- C-20 check: every ## headline will carry *(Cell: XX-P#)* inline (NOT a subline): Y / N
- C-21 check: gate items (a)-(e) all PASS: Y / N

---

### STEP 6 -- Ticket Bodies (by theme, phase-sorted, ascending T-ID)

```
### Theme A -- {theme name}
*Underlying failure: {from Step 3}*

## T-NN -- {Title} *(Cell: XX-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences. First person. Committed phrase expanded into opening sentence.
Register matches Cell ID. Registers differ between roles in same phase per gate item (e).
Migration reference where relevant.
Cell ID is on the ## headline above -- not on any subline.]
```

---

### STEP 7 -- Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|

---

### STEP 7B -- Resolution Paths

For every high-volume OR P0/P1 ticket:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|

---

### STEP 8 -- Gap Analysis

All entries require Tickets: T-NN, T-NN.

**Documentation gaps** | Entry | Tickets | Artifact
**Design gaps** | Entry | Tickets | Change
**Operational gaps** | Entry | Tickets | Process change

Minimum 2 entries per gap category.

---

### VERIFICATION MANIFEST

| Verification target | Required | Actual | Pass? |
|--------------------|----------|--------|-------|
| Total tickets | = Constraint Manifest | ___ | ___ |
| Distinct categories | >= 2 | ___ | ___ |
| Distinct personas | >= 3 | ___ | ___ |
| P0 count | <= ceiling | ___ | ___ |
| High-volume count | <= ceiling | ___ | ___ |
| Bodies starting with committed phrase | = total | ___ | ___ |
| ## headlines with *(Cell: XX-P#)* inline -- C-20 | = total | ___ | ___ |
| Cell IDs in headlines resolve to commitment table rows | = total | ___ | ___ |
| Cell IDs in STEP 3B resolve to Vocabulary Matrix cells | = total | ___ | ___ |
| Gate items (a)-(e) all PASS -- C-21 | = 5 | ___ | ___ |
| Item (e) inter-role example cited | = 1 | ___ | ___ |
| No third-person role reference | = total | ___ | ___ |
| Phase 1 discovery register | >= 3 | ___ | ___ |
| Phase 3 operational register | >= 1 | ___ | ___ |

---

---

## V-05 -- Full Synthesis (R5 V-05 Base + Explicit C-20 Rule + Letter-Labeled C-21 Gate)

**Combination axis:** All R5 V-05 mechanisms retained plus:
1. **[NEW R6] Explicit C-20 ZERO-EXCEPTION rule** added to STEP 3B and STEP 4. The
   prohibition on subline placement is stated explicitly. CONSTRAINT MANIFEST and
   VERIFICATION MANIFEST each gain a C-20 row.
2. **[NEW R6] Letter-labeled (a)-(e) gate with binary PASS/FAIL per item** upgrades the
   R5 V-05 gate (which already has 5 items and item e) to use the explicit letter-label
   formalism from V-02. Removes any scoring ambiguity about whether item (e) is present.
3. **[NEW R6] VERIFICATION MANIFEST C-21 row** verifies gate items (a)-(e) all PASS and
   that item (e) example is cited.

**Hypothesis:** R5 V-05 already has the mechanisms for C-20 and C-21 and should score
composite 100 under v6 without these additions. V-05 R6 adds instruction clarity and
manifest rows to make scorer verification unambiguous. Any output following this prompt
cannot satisfy C-20 without placing the ID in the ## line (prohibition stated twice), and
cannot satisfy C-21 without all five letter-labeled items (the rubric gate is mirrored
exactly in the prompt gate). Expected composite: 100.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. VM Row IDs appear in this manifest, the commitment table (STEP 3B), and the
## body headline annotation -- completing the C-20 three-node traceability chain.**

| VM Row ID   | Role    | Phase   | Register description                                                   | Example template phrase                                                                      |
|-------------|---------|---------|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure          | "I'm seeing [failure] only when [condition] -- I cannot reproduce it on demand..."          |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                   | "We've been running {topic} for [N] weeks and we just noticed [regression]..."              |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly     | "I keep seeing customers hit [obstacle] when they first [action] -- no guidance exists..."  |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause      | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."               |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold  | "This is the [N]th escalation about [failure] this month -- I need a permanent fix..."      |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast          | "First-time activation is lower than projected -- I want to understand..."                  |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                      | "The [metric] is not improving at the expected rate -- I need to investigate..."            |
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                  | "I'm seeing users who completed onboarding dropping off at [stage]..."                       |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..."             |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action               | "Session recordings show abandonment when users attempt [advanced action]..."               |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability             | "Long-term users are filing feedback about [behavior change / reliability issue]..."        |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present         | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks          | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                                 | Required                        | Committed value |
|-------------------------------------------------------------------|---------------------------------|-----------------|
| Total tickets                                                     | 6 to 12                         | ___             |
| Phase 1 tickets (day 0-30)                                        | >= 3                            | ___             |
| Phase 2 tickets (day 31-60)                                       | >= 2                            | ___             |
| Phase 3 tickets (day 61-90)                                       | >= 1                            | ___             |
| P0 ceiling                                                        | <= floor(total x 0.25) = ___    | ___             |
| High-volume ceiling                                               | <= floor(total x 0.50) = ___    | ___             |
| Distinct named personas                                           | >= 3                            | ___             |
| SRE tickets                                                       | >= 2                            | ___             |
| Support tickets                                                   | >= 2                            | ___             |
| C-xx tickets                                                      | >= 2 (max 2 per single C-xx)    | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                   | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                 | >= 1                            | ___             |
| Tickets with VM Row ID in commitment table (C-16)                 | = total ticket count            | ___             |
| Tickets with VM Row ID in ## headline annotation (C-20)           | = total ticket count            | ___             |

Do not proceed until both manifests are complete.

---

### STEP 1 -- Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 -- Phase Map Table

| Phase   | Window    | Severity norm | Volume norm  | Body register                           |
|---------|-----------|---------------|--------------|-----------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium  | Discovery/setup -- use VM-xxx-P1 rows   |
| Phase 2 | day 31-60 | P1/P2         | medium       | Integration/edge -- use VM-xxx-P2 rows  |
| Phase 3 | day 61-90 | P0/P1         | low/medium   | Operational/reliability -- use VM-xxx-P3 rows |

---

### STEP 3 -- Theme Declaration

```
Theme A: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

Theme B: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

[Theme C if needed -- same format]
```

Each theme must have a distinct underlying failure. Sum of counts = CONSTRAINT MANIFEST total.

---

### STEP 3A -- Role-Phase Cross-Matrix

| Role    | Phase 1 | Phase 2 | Phase 3 | Total | Theme(s) |
|---------|---------|---------|---------|-------|----------|
| SRE     | ___     | ___     | ___     | ___   | ___      |
| Support | ___     | ___     | ___     | ___   | ___      |
| PM      | ___     | ___     | ___     | ___   | ___      |
| UX      | ___     | ___     | ___     | ___   | ___      |
| C-xx    | ___     | ___     | ___     | ___   | ___      |

Constraint 1: SRE >= 2, Support >= 2, PM >= 1, UX >= 1, C-xx >= 2
Constraint 2: Any role with 3+ tickets must span at least 2 phases
Constraint 3: Any single C-xx persona in at most 2 tickets

---

### STEP 3B -- Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. Reference the VOCABULARY MANIFEST VM Row ID for
each ticket. Derive the committed opening phrase from that row's template. The body MUST
begin with its committed phrase (expanded -- not verbatim).**

**C-20 RULE -- ZERO EXCEPTIONS: The body header *(VM: VM-xxx-P#)* annotation MUST appear
on the same line as ## T-NN -- {Title}. It is NOT permitted on a subline, metadata line, or
any other line. A scorer reading only ## lines must see the VM Row ID without opening any
other line. This creates the three-node C-20 traceability chain:
  VOCABULARY MANIFEST row -> STEP 3B commitment row -> ## headline annotation
all keyed by the same VM Row ID.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate. Execute immediately after completing STEP 3B and before STEP 4. Check all
five items (a)-(e). Each item names the artifact it validates and declares PASS or FAIL
individually. Declare GATE: OPEN or GATE: CLOSED after all five items. Body generation
(STEP 6) is blocked if the gate is CLOSED.**

**(a) VOCABULARY MANIFEST completeness**
Confirm: every (Role, Phase) combination in the ticket inventory has a corresponding row in
the VOCABULARY MANIFEST above (not marked N/A).
Result: [ PASS -- all ___ inventory combinations have VOCABULARY MANIFEST rows ]
      / [ FAIL -- missing combinations: ___ ]

**(b) Commitment table completeness**
Confirm: row count in STEP 3B equals the committed ticket total in the CONSTRAINT MANIFEST.
Result: [ PASS -- STEP 3B has ___ rows = CONSTRAINT MANIFEST total of ___ ]
      / [ FAIL -- STEP 3B has ___ rows != CONSTRAINT MANIFEST total of ___ ]

**(c) Phrase-to-manifest traceability**
Confirm: each committed phrase in STEP 3B derives from the Example template phrase of its
VM Row ID in the VOCABULARY MANIFEST (same role, same phase, same register description).
Result: [ PASS -- all ___ phrases traceable to their VOCABULARY MANIFEST row ]
      / [ FAIL -- untraceable phrases: T-___ (VM Row ID: ___) ]

**(d) Phase-register alignment**
Confirm: all Phase 1 committed phrases use the discovery/setup register from VM-xxx-P1 rows.
At least one Phase 3 phrase uses the operational/reliability register from a VM-xxx-P3 row.
Result: [ PASS -- Phase 1 check: ___ rows OK; Phase 3 check: ___ rows OK ]
      / [ FAIL -- Phase 1 misaligned: T-___ ; Phase 3 missing ]

**(e) Inter-role register differentiation**
Confirm: in at least one phase, two or more roles assigned tickets have distinct register
descriptions in the VOCABULARY MANIFEST. Cite the example explicitly by VM Row ID:
  Phase ___ | VM Row ___ (Role: ___) = "___ register description"
  Phase ___ | VM Row ___ (Role: ___) = "___ register description"
Result: [ PASS -- example cited above ] / [ FAIL -- no phase found with differentiated roles ]

**GATE: [ OPEN -- all five items (a)-(e) PASS -- proceed to STEP 4 PERFORMANCE MODE ]**
**GATE: [ CLOSED -- ___ items failed -- revise VOCABULARY MANIFEST and/or STEP 3B, re-run ]**

---

### STEP 4 -- PERFORMANCE MODE DECLARATION

**You are about to become each persona. They know what they migrated from.**

**SRE:** On-call. Adopted {topic} because the team moved to it. Prior system's failure modes
were familiar; this one is opaque. Something breaking silently. Methodical but frustrated.

**Support:** Answered this same migration question multiple times this week. Filing to get
engineering to fix the root cause so you stop being the manual workaround.

**PM:** Adoption below forecast. Cannot tell if product problem or communication problem.
Filing to request data.

**UX:** Watching session recordings. Users stall at a specific point. Old approach had a
familiar affordance here. Need engineering to understand root cause.

**C-xx:** Switched from [old approach in Step 1] recently. Something surprised you. Do not
know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".**
**Begin each body with the committed phrase from STEP 3B (expanded into a full opening sentence).**
**C-20 RULE -- ZERO EXCEPTIONS: Output ## T-NN -- {Title} *(VM: VM-xxx-P#)* with the VM Row**
**ID annotation on the ## headline line. Do NOT place it on a subline or metadata row.**
**The scorer reads only ## lines -- if the VM Row ID is not there, C-20 fails.**
**Register must match the VOCABULARY MANIFEST row. Registers MUST differ between roles in**
**the same phase -- confirmed by gate item (e). Migration reference where relevant.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK -- verify all before proceeding:
- Total rows: ___ (required: matches CONSTRAINT MANIFEST)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= MANIFEST ceiling)
- High-volume count: ___ (required: <= MANIFEST ceiling)
- Theme/phase counts match Step 3 and CONSTRAINT MANIFEST: MATCH / MISMATCH
- Every STEP 3B row has a valid non-N/A VM Row ID: Y / N
- C-20 check: every ## headline will carry *(VM: VM-xxx-P#)* inline (NOT a subline): Y / N
- C-21 check: gate items (a)-(e) all PASS: Y / N

---

### STEP 6 -- Ticket Bodies (by theme, phase-sorted, ascending T-ID)

**Generation order within each theme: Phase 1 first, then Phase 2, then Phase 3.**

```
### Theme A -- {theme name}
*Underlying failure: {from Step 3}*

## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- VM Row: {row ID from STEP 3B} | Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences.
OPENING: Begin with committed phrase expanded into a full first sentence. Not verbatim.
REGISTER: Use the vocabulary register from the VOCABULARY MANIFEST row. Registers MUST
  differ between roles in the same phase -- confirmed in gate item (e).
VOICE: First person -- "I", "my", "we". No third-person role references.
MIGRATION: Reference old approach where relevant.
C-20: *(VM: VM-xxx-P#)* is on the ## line above -- not on any subline. Two-lookup trace:
  ## headline ID -> STEP 3B row -> VOCABULARY MANIFEST row.]
```

---

### STEP 7 -- Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|

---

### STEP 7B -- Resolution Paths

For every high-volume OR P0/P1 ticket:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|
| T-NN | SRE / Support / PM / Eng | doc-gap / design-flaw / config-error / product-bug | self-serve / escalation / structural |

---

### STEP 8 -- Gap Analysis

All entries require Tickets: T-NN, T-NN with identifiers matching the inventory above.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | design change required

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | process change required

Minimum 2 entries per gap category. Each entry cites at least one T-ID.

---

### VERIFICATION MANIFEST

| Verification target                                                    | Required              | Actual | Pass? |
|------------------------------------------------------------------------|-----------------------|--------|-------|
| Total tickets generated                                                | = CONSTRAINT MANIFEST | ___    | ___   |
| Distinct categories                                                    | >= 2                  | ___    | ___   |
| Distinct personas                                                      | >= 3                  | ___    | ___   |
| P0 count                                                               | <= ceiling            | ___    | ___   |
| High-volume count                                                      | <= ceiling            | ___    | ___   |
| Bodies starting with committed phrase                                  | = total               | ___    | ___   |
| ## headlines with *(VM: VM-xxx-P#)* inline -- C-20 node 3             | = total               | ___    | ___   |
| VM Row IDs in ## headlines resolve to STEP 3B rows -- C-20 node 2     | = total               | ___    | ___   |
| VM Row IDs in STEP 3B resolve to VOCABULARY MANIFEST rows -- C-20 node 1 | = total            | ___    | ___   |
| Gate items (a)-(e) all PASS -- C-21                                   | = 5                   | ___    | ___   |
| Item (e) inter-role example cited by VM Row ID                         | = 1                   | ___    | ___   |
| No third-person role reference                                         | = total               | ___    | ___   |
| Phase 1 bodies use discovery/setup register                            | >= 3                  | ___    | ___   |
| Phase 3 bodies use operational/reliability register                    | >= 1                  | ___    | ___   |
| Registers differ between roles in same phase -- gate item (e) result  | >= 1 phase confirmed  | ___    | ___   |

---

---

## R6 Variation Summary

| Variation | C-20 mechanism | C-21 gate | Gate items | ID scheme | C-20 pred | C-21 pred | Composite |
|-----------|---------------|-----------|------------|-----------|-----------|-----------|-----------|
| V-01 | ZERO-EXCEPTION rule x3 + VERIFICATION row; Cell ID in ## headline | 4-item standalone | 4 (no item e) | Role-P# | PASS | FAIL | ~99.23 |
| V-02 | VM Row ID in metadata subline (not ## headline) | Letter-labeled (a)-(e), binary PASS/FAIL per item | 5 | VM-Role-P# | FAIL | PASS | ~99.23 |
| V-03 | COMPLIANCE CONTRACT at prompt header + VM Row ID in ## headline | (a)-(e) letter-labeled in gate + contract C-21 | 5 | VM-Role-P# | PASS | PASS | 100 |
| V-04 | ZERO-EXCEPTION rule (V-01) + Cell ID in ## headline | Letter-labeled (a)-(e), binary PASS/FAIL per item (V-02) | 5 | Role-P# | PASS | PASS | 100 |
| V-05 | C-20 rule in STEP 3B + STEP 4 + CONSTRAINT MANIFEST + VERIFICATION row | (a)-(e) letter-labeled + C-21 VERIFICATION row | 5 | VM-Role-P# | PASS | PASS | 100 |

**C-20 traceability chain by variation:**

| Variation | Node 1 (manifest) | Node 2 (commitment table) | Node 3 (## headline) | Chain complete? |
|-----------|------------------|--------------------------|----------------------|----------------|
| V-01 | Cell ID as matrix row | Cell ID in STEP 3B column | *(Cell: XX-P#)* on ## headline | YES |
| V-02 | VM Row ID as manifest row | VM Row ID in STEP 3B column | VM Row ID in metadata subline | PARTIAL |
| V-03 | VM Row ID as manifest row | VM Row ID in STEP 3B column | *(VM: VM-xxx-P#)* on ## headline per Contract | YES |
| V-04 | Cell ID as matrix row | Cell ID in STEP 3B column | *(Cell: XX-P#)* on ## headline | YES |
| V-05 | VM Row ID as manifest row | VM Row ID in STEP 3B column | *(VM: VM-xxx-P#)* on ## headline | YES |

**C-21 gate by variation:**

| Variation | Letter labels (a)-(e)? | Item (e) named? | Binary PASS/FAIL per item? | GATE: OPEN/CLOSED? | C-21 pred |
|-----------|----------------------|-----------------|---------------------------|---------------------|-----------|
| V-01 | NO (Check 1-4) | NO | YES | YES | FAIL |
| V-02 | YES | YES -- "inter-role register differentiation" | YES | YES | PASS |
| V-03 | YES | YES | YES | YES | PASS |
| V-04 | YES | YES -- "inter-role register differentiation" | YES | YES | PASS |
| V-05 | YES | YES -- with explicit VM Row ID citation requirement | YES | YES | PASS |

**Diagnostic value of V-01 and V-02:**
V-01 isolates C-20: confirms whether explicit ZERO-EXCEPTION prohibition on subline placement
is sufficient instruction. V-02 isolates C-21: confirms whether letter-label formalism is
required or whether R5 V-02's unlabeled 5-item gate already passes. V-03 tests front-loading
compliance as a named contract. V-04 is the minimum-change composite 100 path. V-05 tests
whether the maximal instruction set -- two C-20 prohibition statements plus CONSTRAINT and
VERIFICATION MANIFEST C-20/C-21 rows -- improves downstream production reliability.
