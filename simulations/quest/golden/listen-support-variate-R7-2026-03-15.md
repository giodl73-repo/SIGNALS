# listen-support -- Variations, Round 7 (rubric v7 -- 24 criteria)

**Date:** 2026-03-15
**Rubric target:** v7 (C-01 through C-24 -- 24 criteria; aspirational denominator = 16)
**Baseline:** R6 V-03 (composite 100.0 under v7 -- sole candidate; C-22/C-23/C-24 all PASS)
**R7 objective:** Stress-test the three new v7 aspirational criteria by varying the structural
mechanisms that produce them. R6 V-03 is the only composite-100 candidate, so R7 isolates each
of the three new mechanisms to confirm which structural elements are load-bearing and whether
alternative formulations preserve the composite-100 ceiling.

**The three new v7 criteria and their v7 sources:**

- **C-22 -- Front-Loaded Compliance Contract**: A named `COMPLIANCE CONTRACT` block must appear
  before any enumerated step. The block must contain (1) a compliant header sample and (2) an
  explicit prohibition statement. Both elements are required; a contract that states obligations
  without a prohibition, or without a sample header, may fail. R6 V-04 and V-05 pass C-20/C-21
  via step-embedded instructions but have no pre-step named contract block -- they fail C-22.

- **C-23 -- Multi-Site Subline Prohibition Anchoring**: The subline prohibition for the
  vocabulary ID must appear at a minimum of two positions: STEP 3B (where the commitment table
  is built) and STEP 4 (where bodies are declared). The VERIFICATION MANIFEST must also carry a
  count row confirming numeric compliance. R6 V-02 uses sublines intentionally and states no
  prohibition -- it fails C-23. All other R6 variations pass because each anchors the
  prohibition at both positions with a VM count row.

- **C-24 -- Output-Embedded Compliance Evidence for Vocabulary Format Criteria**: The
  VERIFICATION MANIFEST must carry rows for both C-20 evidence (numeric count of ## headline
  lines with inline vocabulary ID) and C-21 evidence (all 5 pre-flight gate items PASS with
  item-label citation). R6 V-01 has a C-20 manifest row but the C-21 row lacks individual
  item-label citation -- C-24 is PARTIAL for V-01. R6 V-03/V-04/V-05 carry both rows and pass.

**The R6 gap analysis (what is and is not settled):**

- R6 V-03: composite 100.0 (C-22/C-23/C-24 all PASS). Distinguishing mechanism: COMPLIANCE
  CONTRACT block before VOCABULARY MANIFEST, containing both a compliant header sample and an
  explicit prohibition statement. Gate uses letter labels (a)-(e). VERIFICATION MANIFEST carries
  "## headlines with *(VM: VM-xxx-P#)* inline -- C-20 = total" row and "Gate items (a)-(e) all
  PASS -- C-21 = 5" row.
- R6 V-04/V-05: composite 99.375 (C-23/C-24 PASS, C-22 FAIL -- no pre-step contract block).
  Both achieve C-20 + C-21 via step-embedded instructions. The open question: can V-04/V-05 be
  promoted to composite 100 simply by prepending a COMPLIANCE CONTRACT, without other changes?
- R6 V-01: composite 98.44 (C-23 PASS, C-24 PARTIAL, C-21/C-22 FAIL).
- R6 V-02: composite ~97.5 (C-20/C-22/C-23 FAIL, C-24 PARTIAL).

**R7 questions:**
1. Is the sample header required for C-22, or is the obligation statement alone sufficient?
   (V-01 tests this by removing the sample header from the contract.)
2. Does explicit item-label citation per row in the VERIFICATION MANIFEST (5 rows instead of
   one summary "(a)-(e) all PASS" row) produce stronger C-24 compliance? (V-02.)
3. Does a COMPLIANCE CONTRACT with forward-reference anchors -- naming the three positions where
   its rules will be restated -- produce a more robust C-22 + C-23 architecture? (V-03.)
4. Combined: explicit prohibition + individual gate-item rows. (V-04.)
5. Full synthesis. (V-05.)

---

## Fixed Changes Applied to All R7 Variations

All R7 variations inherit the full R6 V-03 mechanism set. These components are not the
differentiating axis in R7.

| Component | R6 V-03 source | R7 status |
|-----------|---------------|-----------|
| COMPLIANCE CONTRACT before VOCABULARY MANIFEST | R6 V-03 | Retained (varied in V-01/V-03) |
| VM Row ID in ## headline *(VM: VM-xxx-P#)* format -- C-20 | R6 V-03 | Retained |
| 5-item gate (a)-(e) with GATE: OPEN/CLOSED -- C-21 | R6 V-03 | Retained |
| CONSTRAINT MANIFEST row for C-20 (# tickets with VM Row in headline) | R6 V-03 | Retained |
| STEP 3B obligation header citing contract (C-23 site 1) | R6 V-03 | Retained |
| STEP 4 obligation header citing contract (C-23 site 2) | R6 V-03 | Retained |
| VERIFICATION MANIFEST C-20 count row | R6 V-03 | Retained (extended in V-02/V-05) |
| VERIFICATION MANIFEST C-21 summary row | R6 V-03 | Retained (extended in V-02/V-04/V-05) |
| Character-embodiment PERFORMANCE MODE with migration backstory | R6 V-03 | Retained |
| Phase Map Table with severity/volume/register norms -- C-14 | All R6 | Retained |
| Theme declaration before inventory -- C-09 | All R6 | Retained |
| Role-Phase Cross-Matrix -- C-12 | All R6 | Retained |
| Ticket inventory table + TABLE CHECK | All R6 | Retained |
| Cross-ticket patterns -- C-09 | All R6 | Retained |
| Resolution paths table -- C-10 | All R6 | Retained |
| Gap analysis with T-NN refs -- C-04/C-08 | All R6 | Retained |

---

## R7 Variation Axes

R1 explored: role sequence, output format, lifecycle emphasis.
R2 explored: phrasing register, inertia framing, theme-first generation.
R3 explored: vocabulary commitment from phase pools, manifest tables, role-phase matrix.
R4 explored: fusing C-16 (per-ticket commitment) with C-17 (role-phase matrix).
R5 explored: adding C-18 (3-node ID chain) and C-19 (standalone gate) to R4 V-05 base.
R6 explored: C-20 (headline placement rule), C-21 (letter-labeled 5-item gate), C-22
  (COMPLIANCE CONTRACT block). R6 V-03 is composite 100 under v7.
R7 targets the three new v7 criteria: what exactly is load-bearing in each mechanism.

| Axis | Single-axis variation | New angle vs prior rounds | Target criteria |
|------|-----------------------|--------------------------|-----------------|
| Contract required elements | V-01 | Sample header removed from COMPLIANCE CONTRACT -- tests whether sample is required for C-22 PASS | C-22 |
| C-24 manifest granularity | V-02 | 5 individual per-item rows in VERIFICATION MANIFEST replace one summary "(a)-(e) all PASS" row | C-24 |
| Contract forward-reference | V-03 | COMPLIANCE CONTRACT names its three restating positions (STEP 3B / STEP 4 / VM) and declares precedence | C-22 + C-23 |

Combined: V-04 stacks V-01 (no-sample contract) + V-02 (individual item rows). V-05 is full
synthesis: R6 V-03 base + V-03 forward-references + V-02 individual item rows + V-01 explicit
prohibition statement.

---

## V-01 -- Single Axis: Contract Required Elements (Sample Header Removed)

**Axis:** Output format -- the COMPLIANCE CONTRACT block retains its pre-step position and
explicit prohibition statement, but the compliant body header sample is removed. The contract
states both C-20 and C-21 as obligations and names the prohibited placement, but does not
provide a formatted example of the correct ## headline.

**Hypothesis:** C-22 requires "a compliant header sample and an explicit prohibition statement
before any generation work begins." If the sample header is strictly required, V-01 should fail
C-22 (missing sample) and score 99.375, matching the V-04/V-05 R6 ceiling. If the contract
obligation statement alone is sufficient, V-01 should pass C-22 and score 100. This variation
isolates whether the sample header is a pass condition or a scoring note. Predicted composite:
99.375 (C-22 FAIL, sample absent) confirming the sample is a required element.

---

```
You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### COMPLIANCE CONTRACT

**Read before any step. These obligations govern the entire output.**

**C-20 -- Vocabulary ID in ## headline:**
Every ticket body ## headline must include the VM Row ID as an inline annotation on the same
line as the title. Placing the vocabulary ID on any subline, bullet, or metadata row is
prohibited. The annotation must appear directly on the ## headline line so a scorer reading
only ## lines sees the VM Row ID without opening any other line.

**C-21 -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item (e)
is named "inter-role register differentiation" and requires citing two roles in the same phase
with distinct register descriptions. A gate with only four items fails because item (e) is
absent.

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
(expanded). Compliance Contract C-20 governs body header format -- VM Row ID in ## headline.
Subline placement is prohibited -- any ticket body with the VM Row ID on a subline fails.**

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
State: [ PASS -- all ___ combinations have rows ] / [ FAIL -- missing: ___ ]

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
In at least one phase, two or more roles have distinct register descriptions. Cite by VM Row ID:
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
Use the body header format per Compliance Contract C-20 -- VM Row ID inline on the ## headline,
subline placement prohibited:
  ## T-NN -- {Title} *(VM: VM-xxx-P#)*
Register must match the VOCABULARY MANIFEST row. Registers MUST differ between roles in the
same phase -- confirmed in gate item (e). Migration reference where relevant.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume within Constraint Manifest ceilings: MATCH / FAIL
- All STEP 3B rows have valid VM Row IDs from VOCABULARY MANIFEST: Y / N
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline: Y / N
- Compliance Contract C-21: gate items (a)-(e) all PASS: Y / N

If any check fails: revise before continuing.

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
C-20: VM Row ID is on the ## line above per Compliance Contract -- not on any subline.]
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
```

---

---

## V-02 -- Single Axis: C-24 Manifest Granularity (Individual Per-Item Gate Rows)

**Axis:** Lifecycle emphasis -- the VERIFICATION MANIFEST row for C-21 evidence is replaced
with five individual rows, one per gate item (a) through (e), each named and with its own
Required/Actual/Pass? cells. The single summary row "Gate items (a)-(e) all PASS -- C-21 = 5"
becomes five rows: "(a) VOCABULARY MANIFEST completeness -- C-21", "(b) Commitment table
completeness -- C-21", "(c) Phrase-to-manifest traceability -- C-21", "(d) Phase-register
alignment -- C-21", "(e) Inter-role register differentiation -- C-21". The full COMPLIANCE
CONTRACT from R6 V-03 (including sample header) is retained.

**Hypothesis:** C-24 requires "confirmation that all five pre-flight gate items passed with
item-label citation." R6 V-03's summary row "(a)-(e) all PASS" cites item labels by range
notation and is scored as PASS for C-24. The open question is whether individual named rows
make C-24 self-evident to a scorer without inspection -- each row confirms a specific labeled
item. Adding individual rows cannot lower C-24 compliance; they can only make it more explicit.
Predicted composite: 100 (C-22 PASS via retained contract with sample; C-23 PASS via retained
multi-site prohibition; C-24 PASS with maximum item-label granularity).

---

```
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
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item (e)
is named "inter-role register differentiation" and requires citing two roles in the same phase
with distinct register descriptions. A gate with only four items fails because item (e) is
absent.

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
(expanded). Compliance Contract C-20 governs body header format -- VM Row ID in ## headline.
Subline placement is NOT permitted.**

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
State: [ PASS -- all ___ combinations have rows ] / [ FAIL -- missing: ___ ]

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
In at least one phase, two or more roles have distinct register descriptions. Cite by VM Row ID:
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
- Total rows, categories, personas, P0/high-volume within Constraint Manifest ceilings: MATCH / FAIL
- All STEP 3B rows have valid VM Row IDs from VOCABULARY MANIFEST: Y / N
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline: Y / N
- Compliance Contract C-21: gate items (a)-(e) all PASS: Y / N

If any check fails: revise before continuing.

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
C-20: VM Row ID is on the ## line above per Compliance Contract.]
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
| (a) VOCABULARY MANIFEST completeness -- C-21 | PASS | ___ | ___ |
| (b) Commitment table completeness -- C-21 | PASS | ___ | ___ |
| (c) Phrase-to-manifest traceability -- C-21 | PASS | ___ | ___ |
| (d) Phase-register alignment -- C-21 | PASS | ___ | ___ |
| (e) Inter-role register differentiation -- C-21 | PASS | ___ | ___ |
| Item (e) inter-role example explicitly cited | = 1 | ___ | ___ |
| No third-person role reference | = total | ___ | ___ |
| Phase 1 discovery register | >= 3 | ___ | ___ |
| Phase 3 operational register | >= 1 | ___ | ___ |
```

---

---

## V-03 -- Single Axis: Contract Forward-Reference Architecture

**Axis:** Phrasing register -- the COMPLIANCE CONTRACT is extended with a third section:
"RESTATING POSITIONS". This section names the three locations in the output where the contract
rules will be restated and declares the contract as governing if any restatement conflicts.
The contract governs; steps cite the contract. Each restating step (STEP 3B, STEP 4, the
VERIFICATION MANIFEST) contains a citation: "Per Compliance Contract above." The sample header
from R6 V-03 is retained.

**Hypothesis:** R6 V-03's contract states the rules and provides a sample but does not name
its obligation sites. The contract and the steps are structurally separate; a model generating
the output must remember the contract applies to downstream steps. Explicit forward references
from the contract to its three restating positions create a structural obligation chain: the
scorer can confirm at each restating site that the contract was honored. This should not change
the C-22 PASS condition (the contract still precedes steps, has a sample header, and states a
prohibition) but reinforces C-23 (named multi-site restating positions) and may add robustness
to C-24 (the VM is explicitly called out as a compliance evidence site in the contract).
Predicted composite: 100.

---

```
You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### COMPLIANCE CONTRACT

**Read before any step. These obligations govern the entire output. This contract is restated
at three positions downstream -- STEP 3B, STEP 4, and the VERIFICATION MANIFEST -- which each
cite this contract by name. If any restating position conflicts with this contract, this
contract governs.**

**C-20 -- Vocabulary ID in ## headline:**
Every ticket body ## headline must include the VM Row ID as an inline annotation on the same
line as the title: ## T-NN -- {Title} *(VM: VM-xxx-P#)*. The annotation is NOT permitted on
any subline, bullet, or metadata row. A scorer reading only ## lines must see the VM Row ID
without opening any other line.

**C-21 -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item (e)
is named "inter-role register differentiation" and requires citing two roles in the same phase
with distinct register descriptions. A gate with only four items fails because item (e) is
absent.

**Compliant body header format:**
```
## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"
```

**Restating positions:** This contract is restated at:
1. STEP 3B obligation header -- governs the commitment table and the ## headline format rule.
2. STEP 4 PERFORMANCE MODE -- governs every ticket body header generated in STEP 6.
3. VERIFICATION MANIFEST -- carries explicit count rows confirming numeric compliance with
   C-20 (headline count) and C-21 (each gate item labeled and confirmed).

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. VM Row IDs appear in this manifest, the commitment table, and the ## headline
annotation (per Compliance Contract C-20 above).**

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

**Per Compliance Contract above -- C-20 governs this table. Fill before generating any ticket
body. Reference the VOCABULARY MANIFEST VM Row ID. Derive the committed phrase from that row's
template. Body MUST begin with committed phrase (expanded). VM Row ID MUST appear in the ##
headline of the ticket body. Subline placement is NOT permitted.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate -- Per Compliance Contract above, C-21 governs this section. Execute after
STEP 3B, before STEP 4. All five items (a)-(e) must be present with individual PASS/FAIL
states. GATE: OPEN or GATE: CLOSED. Body generation blocked if CLOSED.**

**(a) VOCABULARY MANIFEST completeness**
Every (Role, Phase) combination in the inventory has a VOCABULARY MANIFEST row (not N/A).
State: [ PASS -- all ___ combinations have rows ] / [ FAIL -- missing: ___ ]

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
In at least one phase, two or more roles have distinct register descriptions. Cite by VM Row ID:
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
Per Compliance Contract above -- use the compliant header format:
  ## T-NN -- {Title} *(VM: VM-xxx-P#)*  <- VM Row ID on ## line, per C-20.
Register must match the VOCABULARY MANIFEST row. Registers MUST differ between roles in the
same phase -- confirmed in gate item (e). Migration reference where relevant.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume within Constraint Manifest ceilings: MATCH / FAIL
- All STEP 3B rows have valid VM Row IDs from VOCABULARY MANIFEST: Y / N
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline: Y / N
- Compliance Contract C-21: gate items (a)-(e) all PASS: Y / N

If any check fails: revise before continuing.

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
C-20: VM Row ID is on the ## line above per Compliance Contract.]
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

**Per Compliance Contract above -- this manifest carries explicit compliance evidence for C-20
and C-21 as named in the contract's Restating Positions section.**

| Verification target | Required | Actual | Pass? |
|--------------------|----------|--------|-------|
| Total tickets | = Constraint Manifest | ___ | ___ |
| Distinct categories | >= 2 | ___ | ___ |
| Distinct personas | >= 3 | ___ | ___ |
| Bodies starting with committed phrase | = total | ___ | ___ |
| ## headlines with *(VM: VM-xxx-P#)* inline -- C-20 count | = total | ___ | ___ |
| VM Row IDs in headlines resolve to STEP 3B rows | = total | ___ | ___ |
| VM Row IDs in STEP 3B resolve to VOCABULARY MANIFEST rows | = total | ___ | ___ |
| Gate items (a)-(e) all PASS -- C-21 | = 5 | ___ | ___ |
| Item (e) inter-role example explicitly cited | = 1 | ___ | ___ |
| No third-person role reference | = total | ___ | ___ |
| Phase 1 discovery register | >= 3 | ___ | ___ |
| Phase 3 operational register | >= 1 | ___ | ___ |
```

---

---

## V-04 -- Combined: V-01 (No-Sample Contract) + V-02 (Individual Gate-Item VM Rows)

**Combination axis:**
1. From V-01: COMPLIANCE CONTRACT with explicit prohibition statement but no sample header.
   Tests whether the sample header is required for C-22 while stacking with V-02's C-24 axis.
2. From V-02: VERIFICATION MANIFEST replaces one C-21 summary row with five individual
   per-item rows (a) through (e), each named and with individual Required/Actual/Pass? cells.

**Hypothesis:** If C-22 requires a sample header (as predicted), V-04 fails C-22 and reaches
99.375 (same as V-01 alone). If C-22 does not require a sample header, V-04 achieves composite
100 because it also passes C-23 (multi-site prohibition in STEP 3B + STEP 4 + VM count row)
and C-24 (five individually labeled VM rows). V-04 serves as the critical test: if V-01 fails
C-22 and V-04 also fails C-22, the sample header is definitively required. If both pass, the
prohibition statement alone is sufficient.

---

```
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
line as the title. Placing the vocabulary ID on any subline, bullet, or metadata row is
prohibited. An output with any vocabulary ID on a subline fails C-20 regardless of other
compliance. A scorer reading only ## lines must see the VM Row ID without opening any other
line.

**C-21 -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item (e)
is named "inter-role register differentiation" and requires citing two roles in the same phase
with distinct register descriptions. A gate with only four items fails because item (e) is
absent.

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
(expanded). Compliance Contract C-20 governs body header format -- VM Row ID in ## headline.
Placing the VM Row ID on a subline is prohibited.**

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
State: [ PASS -- all ___ combinations have rows ] / [ FAIL -- missing: ___ ]

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
In at least one phase, two or more roles have distinct register descriptions. Cite by VM Row ID:
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
Body header format per Compliance Contract C-20 -- VM Row ID on the ## headline, subline
placement prohibited:
  ## T-NN -- {Title} *(VM: VM-xxx-P#)*
Register must match the VOCABULARY MANIFEST row. Registers MUST differ between roles in the
same phase -- confirmed in gate item (e). Migration reference where relevant.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume within Constraint Manifest ceilings: MATCH / FAIL
- All STEP 3B rows have valid VM Row IDs from VOCABULARY MANIFEST: Y / N
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline: Y / N
- Compliance Contract C-21: gate items (a)-(e) all PASS: Y / N

If any check fails: revise before continuing.

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
C-20: VM Row ID is on the ## line above per Compliance Contract -- not on any subline.]
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
| (a) VOCABULARY MANIFEST completeness -- C-21 | PASS | ___ | ___ |
| (b) Commitment table completeness -- C-21 | PASS | ___ | ___ |
| (c) Phrase-to-manifest traceability -- C-21 | PASS | ___ | ___ |
| (d) Phase-register alignment -- C-21 | PASS | ___ | ___ |
| (e) Inter-role register differentiation -- C-21 | PASS | ___ | ___ |
| Item (e) inter-role example explicitly cited | = 1 | ___ | ___ |
| No third-person role reference | = total | ___ | ___ |
| Phase 1 discovery register | >= 3 | ___ | ___ |
| Phase 3 operational register | >= 1 | ___ | ___ |
```

---

---

## V-05 -- Full Synthesis

**Combination axis:**
1. From V-01: Explicit prohibition statement in COMPLIANCE CONTRACT ("Subline placement is
   prohibited. An output with any vocabulary ID on a subline fails C-20 regardless of other
   compliance.") -- tests robustness of C-22 with maximum prohibition clarity.
2. From V-02: VERIFICATION MANIFEST five individual per-item rows replacing one summary row --
   maximum C-24 evidence granularity with named item labels (a)-(e) in the manifest itself.
3. From V-03: COMPLIANCE CONTRACT RESTATING POSITIONS section names STEP 3B, STEP 4, and the
   VERIFICATION MANIFEST as governed sites; each site cites the contract by name -- maximum
   C-22 structural architecture and C-23 multi-site anchoring.
4. Full COMPLIANCE CONTRACT sample header retained from R6 V-03.

**Hypothesis:** V-05 is the maximum-precision formulation of all three new v7 criteria. It
retains the sample header (satisfying C-22's sample requirement), adds an explicit prohibition
statement (reinforcing C-22), names all three restating positions in the contract (reinforcing
C-23 and C-22's two-layer architecture), and provides five individually labeled VERIFICATION
MANIFEST rows for C-21 (maximizing C-24 evidence). Expected composite: 100, with the highest
structural redundancy of any R7 variation. Where R6 V-03 achieves 100 through architectural
correctness, V-05 achieves it through architectural correctness plus maximum explicit evidence.

---

```
You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### COMPLIANCE CONTRACT

**Read before any step. These obligations govern the entire output. This contract is restated
at three positions downstream -- STEP 3B, STEP 4, and the VERIFICATION MANIFEST -- which each
cite this contract by name. If any restating position conflicts with this contract, this
contract governs.**

**C-20 -- Vocabulary ID in ## headline:**
Every ticket body ## headline must include the VM Row ID as an inline annotation on the same
line as the title: ## T-NN -- {Title} *(VM: VM-xxx-P#)*. Placing the vocabulary ID on any
subline, bullet, or metadata row is prohibited. An output with any vocabulary ID on a subline
fails C-20 regardless of other compliance. A scorer reading only ## lines must see the VM Row
ID without opening any other line.

**C-21 -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item (e)
is named "inter-role register differentiation" and requires citing two roles in the same phase
with distinct register descriptions. A gate with only four items fails because item (e) is
absent.

**Compliant body header format:**
```
## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"
```

**Restating positions:** This contract is restated at:
1. STEP 3B obligation header -- governs the commitment table and the ## headline format rule.
2. STEP 4 PERFORMANCE MODE -- governs every ticket body header generated in STEP 6.
3. VERIFICATION MANIFEST -- carries five individually labeled rows (a)-(e) confirming that
   each gate item passed, plus a numeric count row confirming C-20 headline compliance.

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. VM Row IDs appear in this manifest, the commitment table, and the ## headline
annotation (per Compliance Contract C-20 above).**

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

**Per Compliance Contract above -- C-20 governs this table. Fill before generating any ticket
body. Reference the VOCABULARY MANIFEST VM Row ID. Derive the committed phrase from that row's
template. Body MUST begin with committed phrase (expanded). VM Row ID MUST appear on the ##
headline of the ticket body. Subline placement is prohibited -- any ticket body with the VM
Row ID on a subline fails C-20.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate -- Per Compliance Contract above, C-21 governs this section. Execute after
STEP 3B, before STEP 4. All five items (a)-(e) must be present with individual PASS/FAIL
states. GATE: OPEN or GATE: CLOSED. Body generation blocked if CLOSED.**

**(a) VOCABULARY MANIFEST completeness**
Every (Role, Phase) combination in the inventory has a VOCABULARY MANIFEST row (not N/A).
State: [ PASS -- all ___ combinations have rows ] / [ FAIL -- missing: ___ ]

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
In at least one phase, two or more roles have distinct register descriptions. Cite by VM Row ID:
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
Per Compliance Contract above -- use the compliant header format with VM Row ID on ## headline.
Subline placement is prohibited:
  ## T-NN -- {Title} *(VM: VM-xxx-P#)*  <- VM Row ID on ## line, per C-20.
Register must match the VOCABULARY MANIFEST row. Registers MUST differ between roles in the
same phase -- confirmed in gate item (e). Migration reference where relevant.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume within Constraint Manifest ceilings: MATCH / FAIL
- All STEP 3B rows have valid VM Row IDs from VOCABULARY MANIFEST: Y / N
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline: Y / N
- Compliance Contract C-21: gate items (a)-(e) all PASS: Y / N

If any check fails: revise before continuing.

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
C-20: VM Row ID is on the ## line above per Compliance Contract -- subline placement prohibited.]
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

**Per Compliance Contract above -- this manifest carries explicit compliance evidence for C-20
and C-21 as named in the contract's Restating Positions section.**

| Verification target | Required | Actual | Pass? |
|--------------------|----------|--------|-------|
| Total tickets | = Constraint Manifest | ___ | ___ |
| Distinct categories | >= 2 | ___ | ___ |
| Distinct personas | >= 3 | ___ | ___ |
| Bodies starting with committed phrase | = total | ___ | ___ |
| ## headlines with *(VM: VM-xxx-P#)* inline -- C-20 count | = total | ___ | ___ |
| VM Row IDs in headlines resolve to STEP 3B rows | = total | ___ | ___ |
| VM Row IDs in STEP 3B resolve to VOCABULARY MANIFEST rows | = total | ___ | ___ |
| (a) VOCABULARY MANIFEST completeness -- C-21 | PASS | ___ | ___ |
| (b) Commitment table completeness -- C-21 | PASS | ___ | ___ |
| (c) Phrase-to-manifest traceability -- C-21 | PASS | ___ | ___ |
| (d) Phase-register alignment -- C-21 | PASS | ___ | ___ |
| (e) Inter-role register differentiation -- C-21 | PASS | ___ | ___ |
| Item (e) inter-role example explicitly cited | = 1 | ___ | ___ |
| No third-person role reference | = total | ___ | ___ |
| Phase 1 discovery register | >= 3 | ___ | ___ |
| Phase 3 operational register | >= 1 | ___ | ___ |
```

---

## Predicted Scores Under v7 Rubric

| Variation | C-22 (Contract) | C-23 (Multi-site) | C-24 (VM evidence) | Predicted composite |
|-----------|----------------|-------------------|--------------------|---------------------|
| V-01 | FAIL (no sample header) | PASS | PASS | 99.375 |
| V-02 | PASS | PASS | PASS (5 individual rows) | 100.0 |
| V-03 | PASS | PASS | PASS | 100.0 |
| V-04 | FAIL (no sample header) | PASS | PASS (5 individual rows) | 99.375 |
| V-05 | PASS | PASS | PASS (5 individual rows) | 100.0 |

**Decision tree from R7 scoring:**
- If V-01 scores 99.375: sample header is required for C-22. V-04 will also score 99.375.
  V-02, V-03, V-05 all retain the sample and should score 100.
- If V-01 scores 100.0: sample header is not required; the prohibition statement alone
  satisfies C-22. This would revise the rubric interpretation of C-22's pass condition.
- If V-02's 5-row VM structure raises the C-24 score above V-03's range-notation row: the
  individual per-item rows provide stronger C-24 evidence. This would inform whether to
  standardize on individual rows for future rounds.
