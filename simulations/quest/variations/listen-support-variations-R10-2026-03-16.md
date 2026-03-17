A complete R10 file already exists for today — it probes overlapping but distinct territory (V-03 uses a dual-case sample in the CONTRACT, which I hadn't chosen). Rather than duplicate, I'll output my generated variations which cover three clean single axes not present in the prior run. Here they are:

---

# listen-support -- Variations, Round 10 (rubric v10 -- 32 criteria)

**Date:** 2026-03-16
**Rubric target:** v10 (C-01 through C-32; max 210 pts)
**Baseline:** R9 V-05 (composite 100 under v10)
**R10 objective:** Probe sites that reference VM Row IDs but do not yet carry consequence-form:
(1) CONSTRAINT MANIFEST C-20 row, (2) VOCABULARY MANIFEST header (ID origin), (3) STEP 5
TABLE CHECK C-20 line. All five inherit full R9 V-05 and score 100/100 under v10.

**Candidate new criteria for v11:**
- C-33: Planning-table source-enforcement -- CONSTRAINT MANIFEST C-20 row carries the consequence clause, making the constraint table self-enforcing at the planning phase.
- C-34: Origin-site source-enforcement -- VOCABULARY MANIFEST header carries consequence-form at the VM Row ID creation site.
- C-35: Mid-sequence gate consequence-form -- STEP 5 TABLE CHECK C-20 line carries the consequence clause, creating a fourth timing site between planning and generation.

**Predicted scores under v10:**

| Variation | v10 score | Path |
|-----------|-----------|------|
| V-01 | 100.00 | R9 V-05 + CONSTRAINT MANIFEST C-20 row consequence-form (unregistered) |
| V-02 | 100.00 | R9 V-05 + VOCABULARY MANIFEST header consequence-form (origin site) |
| V-03 | 100.00 | R9 V-05 + STEP 5 TABLE CHECK C-20 line consequence-form |
| V-04 | 100.00 | V-01 + V-02 + both sites added to RESTATING POSITIONS |
| V-05 | 100.00 | Full synthesis: all three axes + RESTATING POSITIONS updated |

**R10 variation axes:**

| Axis | Variation | New angle vs R9 | Candidate criterion |
|------|-----------|-----------------|---------------------|
| Output format | V-01 | CF at CONSTRAINT MANIFEST C-20 row (unregistered planning-phase site) | C-33 |
| Lifecycle emphasis | V-02 | CF at VOCABULARY MANIFEST header (ID-origin site) | C-34 |
| Phrasing register | V-03 | CF at STEP 5 TABLE CHECK C-20 line (mid-sequence gate) | C-35 |
| Combined: output format + lifecycle | V-04 | V-01 + V-02 + RESTATING POSITIONS gains two entries | C-33 + C-34 |
| Full synthesis | V-05 | All three axes; every VM Row ID touch-point carries CF | C-33 + C-34 + C-35 |

---

## V-01 -- Single Axis: Output Format (CONSTRAINT MANIFEST C-20 Row Gains Consequence-Form)

**Axis:** Output format -- the CONSTRAINT MANIFEST C-20 row label gains the consequence clause inline. In R9 V-05, the row reads `Tickets with VM Row ID in ## headline (Compliance Contract C-20) | = total ticket count`. V-01 upgrades the label to carry the full consequence clause: `(C-20: subline placement is NOT permitted -- an output with any vocabulary ID on a subline fails C-20 regardless of other compliance)`. This makes the planning-commitment table itself self-enforcing.

**Hypothesis:** The CONSTRAINT MANIFEST is the first structured commitment a model makes about ticket count. Adding CF here creates an enforcement site at pre-generation planning, independent of STEP 3B. RESTATING POSITIONS unchanged from R9 V-05 -- CONSTRAINT MANIFEST is unregistered. Candidate C-33 introduced.

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
line as the title: ## T-NN -- {Title} *(VM: VM-xxx-P#)*. Placing the vocabulary ID on any
subline, bullet, or metadata row is NOT permitted -- an output with any vocabulary ID on a
subline fails C-20 regardless of other compliance. A scorer reading only ## lines must see the
VM Row ID without opening any other line.

**C-21 -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item (e)
is named "inter-role register differentiation" and requires citing two roles in the same phase
with distinct register descriptions. A gate with only four items fails because item (e) is
absent.

**Compliant body header sample:**
```
## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"
```

**RESTATING POSITIONS**

The sections listed below carry obligations derived from this contract. If any section's
wording conflicts with this contract, this contract governs.

- **STEP 3B -- Per-Ticket Vocabulary Commitment Table**: governed by C-20 (VM Row ID must
  appear in ## headline; subline placement is NOT permitted -- an output with any vocabulary
  ID on a subline fails C-20 regardless of other compliance).
- **VOCABULARY PRE-FLIGHT GATE**: governed by C-21 (exactly five items (a)-(e) with individual
  PASS/FAIL states; item (e) named "inter-role register differentiation").
- **STEP 4 -- PERFORMANCE MODE DECLARATION**: governed by C-20 (VM Row ID must appear in ##
  headline inline; subline placement is NOT permitted -- an output with any vocabulary ID on
  a subline fails C-20 regardless of other compliance).
- **STEP 6 -- Ticket Bodies**: governed by C-20 (VM Row ID must appear in ## headline; subline
  placement is NOT permitted -- an output with any vocabulary ID on a subline fails C-20
  regardless of other compliance).
- **VERIFICATION MANIFEST**: governed by C-20 count row (## headlines with inline ID = total)
  and C-21 per-item evidence rows (five individual rows for gate items (a)-(e) with individual
  Required/Actual/Pass? cells).

Precedence: If any restating position conflicts with this contract, this contract governs.

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. VM Row IDs appear in this manifest, the commitment table, and the ## headline
annotation (per Compliance Contract C-20).**

| VM Row ID   | Role    | Phase   | Register description                                                    | Example template phrase                                                                      |
|-------------|---------|---------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy  | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..."  |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure            | "I'm seeing [failure] only when [condition] -- I cannot reproduce it on demand..."           |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                     | "We've been running {topic} for [N] weeks and we just noticed [regression]..."               |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly       | "I keep seeing customers hit [obstacle] when they first [action] -- no guidance exists..."   |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause        | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."                |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold    | "This is the [N]th escalation about [failure] this month -- I need a permanent fix..."       |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast            | "First-time activation is lower than projected -- I want to understand..."                   |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                        | "The [metric] is not improving at the expected rate -- I need to investigate..."             |
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                    | "I'm seeing users who completed onboarding dropping off at [stage]..."                       |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location  | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                 | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability                | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present            | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks             | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time    | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                                                                                               | Required                     | Committed value |
|---------------------------------------------------------------------------------------------------------------------------------|------------------------------|-----------------|
| Total tickets                                                                                                                   | 6 to 12                      | ___             |
| Phase 1 tickets (day 0-30)                                                                                                      | >= 3                         | ___             |
| Phase 2 tickets (day 31-60)                                                                                                     | >= 2                         | ___             |
| Phase 3 tickets (day 61-90)                                                                                                     | >= 1                         | ___             |
| P0 ceiling                                                                                                                      | <= floor(total x 0.25) = ___ | ___             |
| High-volume ceiling                                                                                                             | <= floor(total x 0.50) = ___ | ___             |
| Distinct named personas                                                                                                         | >= 3                         | ___             |
| SRE tickets                                                                                                                     | >= 2                         | ___             |
| Support tickets                                                                                                                 | >= 2                         | ___             |
| C-xx tickets                                                                                                                    | >= 2 (max 2 per single C-xx) | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                                                                                 | >= 3                         | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                                                                               | >= 1                         | ___             |
| Tickets with VM Row ID in commitment table (C-16)                                                                               | = total ticket count         | ___             |
| Tickets with VM Row ID in ## headline (C-20: subline placement is NOT permitted -- an output with any vocabulary ID on a subline fails C-20 regardless of other compliance) | = total ticket count | ___ |

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

| Phase   | Window    | Severity norm | Volume norm  | Body register                                  |
|---------|-----------|---------------|--------------|------------------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium  | Discovery/setup -- use VM-xxx-P1 rows          |
| Phase 2 | day 31-60 | P1/P2         | medium       | Integration/edge -- use VM-xxx-P2 rows         |
| Phase 3 | day 61-90 | P0/P1         | low/medium   | Operational/reliability -- use VM-xxx-P3 rows  |

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
(expanded). Compliance Contract C-20 governs body header format -- VM Row ID in ## headline;
subline placement is NOT permitted -- an output with any vocabulary ID on a subline fails
C-20 regardless of other compliance.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___"                    |
| T-02 | VM-___-P___ | Phase ___ | "___"                    |
| T-03 | VM-___-P___ | Phase ___ | "___"                    |
| ...  |             |           |                          |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate -- Per Compliance Contract above, C-21 governs this section. Execute after
STEP 3B, before STEP 4. All five items (a)-(e) must be present with individual PASS/FAIL states.
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
Use the body header format per Compliance Contract C-20 -- VM Row ID inline on ## headline;
subline placement is NOT permitted -- an output with any vocabulary ID on a subline fails
C-20 regardless of other compliance:
  ## T-NN -- {Title} *(VM: VM-xxx-P#)*
Register must match the VOCABULARY MANIFEST row. Registers MUST differ between roles in the
same phase -- confirmed in gate item (e). Migration reference where relevant.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|------------|
| T-01 | ...   | ...      | ...     | ...    | ...      | ...   | ...   | Y/N        |

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume within Constraint Manifest ceilings: MATCH / FAIL
- All STEP 3B rows have valid VM Row IDs from VOCABULARY MANIFEST: Y / N
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline: Y / N
- Compliance Contract C-21: gate items (a)-(e) all PASS: Y / N

If any check fails: revise before continuing.

---

### STEP 6 -- Ticket Bodies (by theme, phase-sorted, ascending T-ID)

**Per Compliance Contract above (STEP 6 governed by C-20): VM Row ID must appear in ##
headline; subline placement is NOT permitted -- an output with any vocabulary ID on a subline
fails C-20 regardless of other compliance.**

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
C-20: VM Row ID is on the ## line above -- not on any subline -- an output with any
vocabulary ID on a subline fails C-20 regardless of other compliance.]
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

**Per Compliance Contract above -- this manifest carries C-20 count row and C-21 per-item
evidence rows. An output with any vocabulary ID on a subline fails C-20 regardless of other
compliance -- verify via the C-20 count row below.**

| Verification target | Required | Actual | Pass? |
|---|---|---|---|
| Total tickets | = Constraint Manifest | ___ | ___ |
| Distinct categories | >= 2 | ___ | ___ |
| Distinct personas | >= 3 | ___ | ___ |
| Bodies starting with committed phrase | = total | ___ | ___ |
| ## headlines with *(VM: VM-xxx-P#)* inline -- C-20 | = total | ___ | ___ |
| VM Row IDs in headlines resolve to STEP 3B rows | = total | ___ | ___ |
| VM Row IDs in STEP 3B resolve to VOCABULARY MANIFEST rows | = total | ___ | ___ |
| (a) VOCABULARY MANIFEST completeness -- C-21 | all combos have rows | ___ | ___ |
| (b) Commitment table completeness -- C-21 | rows = ticket count | ___ | ___ |
| (c) Phrase-to-cell traceability -- C-21 | all phrases traceable | ___ | ___ |
| (d) Phase-register alignment -- C-21 | P1=discovery, P3=ops | ___ | ___ |
| (e) Inter-role register differentiation -- C-21 | >= 2 roles differ | ___ | ___ |
| No third-person role reference | = total | ___ | ___ |
| Phase 1 discovery register | >= 3 | ___ | ___ |
| Phase 3 operational register | >= 1 | ___ | ___ |
```

---

---

## V-02 -- Single Axis: Lifecycle Emphasis (VOCABULARY MANIFEST Header Gains Consequence-Form)

**Axis:** Lifecycle emphasis -- VOCABULARY MANIFEST header gains consequence-form at the VM Row ID origin site. In R9 V-05, the header ends: "VM Row IDs appear in this manifest, the commitment table, and the ## headline annotation (per Compliance Contract C-20)." V-02 appends: "An output placing any VM Row ID on a subline instead of the ## headline fails C-20 regardless of other compliance -- this table is the source registry; every ID from this table must appear on a ## headline, never a subline."

**Hypothesis:** Consequence-form at the ID creation site (VOCABULARY MANIFEST) fires the rule at the moment the model assigns VM Row IDs to roles and phases -- before any ticket planning begins. RESTATING POSITIONS unchanged from R9 V-05. Candidate C-34 introduced.

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
line as the title: ## T-NN -- {Title} *(VM: VM-xxx-P#)*. Placing the vocabulary ID on any
subline, bullet, or metadata row is NOT permitted -- an output with any vocabulary ID on a
subline fails C-20 regardless of other compliance. A scorer reading only ## lines must see the
VM Row ID without opening any other line.

**C-21 -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item (e)
is named "inter-role register differentiation" and requires citing two roles in the same phase
with distinct register descriptions. A gate with only four items fails because item (e) is
absent.

**Compliant body header sample:**
```
## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"
```

**RESTATING POSITIONS**

The sections listed below carry obligations derived from this contract. If any section's
wording conflicts with this contract, this contract governs.

- **STEP 3B -- Per-Ticket Vocabulary Commitment Table**: governed by C-20 (VM Row ID must
  appear in ## headline; subline placement is NOT permitted -- an output with any vocabulary
  ID on a subline fails C-20 regardless of other compliance).
- **VOCABULARY PRE-FLIGHT GATE**: governed by C-21 (exactly five items (a)-(e) with individual
  PASS/FAIL states; item (e) named "inter-role register differentiation").
- **STEP 4 -- PERFORMANCE MODE DECLARATION**: governed by C-20 (VM Row ID must appear in ##
  headline inline; subline placement is NOT permitted -- an output with any vocabulary ID on
  a subline fails C-20 regardless of other compliance).
- **STEP 6 -- Ticket Bodies**: governed by C-20 (VM Row ID must appear in ## headline; subline
  placement is NOT permitted -- an output with any vocabulary ID on a subline fails C-20
  regardless of other compliance).
- **VERIFICATION MANIFEST**: governed by C-20 count row (## headlines with inline ID = total)
  and C-21 per-item evidence rows (five individual rows for gate items (a)-(e) with individual
  Required/Actual/Pass? cells).

Precedence: If any restating position conflicts with this contract, this contract governs.

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. VM Row IDs appear in this manifest, the commitment table, and the ## headline
annotation (per Compliance Contract C-20). An output placing any VM Row ID on a subline
instead of the ## headline fails C-20 regardless of other compliance -- this table is the
source registry; every ID from this table must appear on a ## headline, never a subline.**

| VM Row ID   | Role    | Phase   | Register description                                                    | Example template phrase                                                                      |
|-------------|---------|---------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy  | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..."  |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure            | "I'm seeing [failure] only when [condition] -- I cannot reproduce it on demand..."           |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                     | "We've been running {topic} for [N] weeks and we just noticed [regression]..."               |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly       | "I keep seeing customers hit [obstacle] when they first [action] -- no guidance exists..."   |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause        | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."                |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold    | "This is the [N]th escalation about [failure] this month -- I need a permanent fix..."       |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast            | "First-time activation is lower than projected -- I want to understand..."                   |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                        | "The [metric] is not improving at the expected rate -- I need to investigate..."             |
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                    | "I'm seeing users who completed onboarding dropping off at [stage]..."                       |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location  | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                 | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability                | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present            | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks             | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time    | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target | Required | Committed value |
|---|---|---|
| Total tickets | 6 to 12 | ___ |
| Phase 1 tickets (day 0-30) | >= 3 | ___ |
| Phase 2 tickets (day 31-60) | >= 2 | ___ |
| Phase 3 tickets (day 61-90) | >= 1 | ___ |
| P0 ceiling | <= floor(total x 0.25) = ___ | ___ |
| High-volume ceiling | <= floor(total x 0.50) = ___ | ___ |
| Distinct named personas | >= 3 | ___ |
| SRE tickets | >= 2 | ___ |
| Support tickets | >= 2 | ___ |
| C-xx tickets | >= 2 (max 2 per single C-xx) | ___ |
| Phase 1 bodies with discovery vocabulary (C-14) | >= 3 | ___ |
| Phase 3 bodies with operational vocabulary (C-14) | >= 1 | ___ |
| Tickets with VM Row ID in commitment table (C-16) | = total ticket count | ___ |
| Tickets with VM Row ID in ## headline (Compliance Contract C-20) | = total ticket count | ___ |

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

| Phase | Window | Severity norm | Volume norm | Body register |
|---|---|---|---|---|
| Phase 1 | day 0-30 | P2/P3 | high/medium | Discovery/setup -- use VM-xxx-P1 rows |
| Phase 2 | day 31-60 | P1/P2 | medium | Integration/edge -- use VM-xxx-P2 rows |
| Phase 3 | day 61-90 | P0/P1 | low/medium | Operational/reliability -- use VM-xxx-P3 rows |

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

| Role | Phase 1 | Phase 2 | Phase 3 | Total | Theme(s) |
|---|---|---|---|---|---|
| SRE | ___ | ___ | ___ | ___ | ___ |
| Support | ___ | ___ | ___ | ___ | ___ |
| PM | ___ | ___ | ___ | ___ | ___ |
| UX | ___ | ___ | ___ | ___ | ___ |
| C-xx | ___ | ___ | ___ | ___ | ___ |

Constraint 1: SRE >= 2, Support >= 2, PM >= 1, UX >= 1, C-xx >= 2
Constraint 2: Any role with 3+ tickets must span at least 2 phases
Constraint 3: Any single C-xx persona in at most 2 tickets

---

### STEP 3B -- Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. Reference the VOCABULARY MANIFEST VM Row ID.
Derive the committed phrase from that row's template. Body MUST begin with committed phrase
(expanded). Compliance Contract C-20 governs body header format -- VM Row ID in ## headline;
subline placement is NOT permitted -- an output with any vocabulary ID on a subline fails
C-20 regardless of other compliance.**

| T-ID | VM Row ID | Phase | Committed opening phrase |
|---|---|---|---|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate -- Per Compliance Contract above, C-21 governs this section. Execute after
STEP 3B, before STEP 4. All five items (a)-(e) must be present with individual PASS/FAIL states.
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
Use the body header format per Compliance Contract C-20 -- VM Row ID inline on ## headline;
subline placement is NOT permitted -- an output with any vocabulary ID on a subline fails
C-20 regardless of other compliance:
  ## T-NN -- {Title} *(VM: VM-xxx-P#)*
Register must match the VOCABULARY MANIFEST row. Registers MUST differ between roles in the
same phase -- confirmed in gate item (e). Migration reference where relevant.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|---|---|---|---|---|---|---|---|---|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume within Constraint Manifest ceilings: MATCH / FAIL
- All STEP 3B rows have valid VM Row IDs from VOCABULARY MANIFEST: Y / N
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline: Y / N
- Compliance Contract C-21: gate items (a)-(e) all PASS: Y / N

If any check fails: revise before continuing.

---

### STEP 6 -- Ticket Bodies (by theme, phase-sorted, ascending T-ID)

**Per Compliance Contract above (STEP 6 governed by C-20): VM Row ID must appear in ##
headline; subline placement is NOT permitted -- an output with any vocabulary ID on a subline
fails C-20 regardless of other compliance.**

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
C-20: VM Row ID is on the ## line above -- not on any subline -- an output with any
vocabulary ID on a subline fails C-20 regardless of other compliance.]
```

---

### STEP 7 -- Cross-Ticket Patterns / STEP 7B -- Resolution Paths / STEP 8 -- Gap Analysis

[Same structure as V-01 -- unchanged from R9 V-05]

---

### VERIFICATION MANIFEST

**Per Compliance Contract above -- this manifest carries C-20 count row and C-21 per-item
evidence rows. An output with any vocabulary ID on a subline fails C-20 regardless of other
compliance -- verify via the C-20 count row below.**

[Same 15-row table as V-01 -- unchanged from R9 V-05]
```

---

---

## V-03 -- Single Axis: Phrasing Register (STEP 5 TABLE CHECK C-20 Line Gains Consequence-Form)

**Axis:** Phrasing register -- the STEP 5 TABLE CHECK C-20 line is upgraded from assertion-form (`Y / N`) to consequence-form. In R9 V-05: `"Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline: Y / N"`. V-03: `"Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline -- subline placement is NOT permitted; an output with any vocabulary ID on a subline fails C-20 regardless of other compliance: Y / N"`. STEP 5 sits between planning and body generation -- a model that passes STEP 3B and the PRE-FLIGHT GATE is intercepted here a second time before writing a single body.

**Hypothesis:** A fourth timing site (COMPLIANCE CONTRACT load → STEP 3B planning → STEP 5 pre-body gate → STEP 6 generation → VERIFICATION MANIFEST post-check). RESTATING POSITIONS unchanged. Candidate C-35 introduced.

---

```
You are generating a first-90-day support ticket forecast for: **{topic}**

[COMPLIANCE CONTRACT, VOCABULARY MANIFEST, CONSTRAINT MANIFEST -- same as V-01]

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|---|---|---|---|---|---|---|---|---|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume within Constraint Manifest ceilings: MATCH / FAIL
- All STEP 3B rows have valid VM Row IDs from VOCABULARY MANIFEST: Y / N
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline -- subline
  placement is NOT permitted; an output with any vocabulary ID on a subline fails C-20
  regardless of other compliance: Y / N
- Compliance Contract C-21: gate items (a)-(e) all PASS: Y / N

If any check fails: revise before continuing.

[STEP 6 through VERIFICATION MANIFEST -- same as V-01]
```

*Note: V-03 is identical to V-01 in all sections except the STEP 5 TABLE CHECK C-20 line. All other sections inherit R9 V-05 unchanged.*

---

---

## V-04 -- Combined: Output Format + Lifecycle Emphasis (V-01 + V-02 + Both Sites in RESTATING POSITIONS)

**Axes:** V-01 (CONSTRAINT MANIFEST C-20 row CF) + V-02 (VOCABULARY MANIFEST header CF). Closes both registry gaps: RESTATING POSITIONS gains two new entries. RESTATING POSITIONS now names seven governed sites: VOCABULARY MANIFEST, CONSTRAINT MANIFEST C-20 row, STEP 3B, VOCABULARY PRE-FLIGHT GATE, STEP 4, STEP 6, VERIFICATION MANIFEST. STEP 5 TABLE CHECK retains assertion-form.

**Hypothesis:** Registry coherence test for two new planning-phase sites simultaneously. Candidate C-33 + C-34 both introduced; C-37 (registry coverage of both new sites) signal introduced.

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
[same as V-01]

**C-21 -- All five gate items present:**
[same as V-01]

**Compliant body header sample:**
[same as V-01]

**RESTATING POSITIONS**

The sections listed below carry obligations derived from this contract. If any section's
wording conflicts with this contract, this contract governs.

- **VOCABULARY MANIFEST**: governed by C-20 (every VM Row ID in this table must ultimately
  appear on a ## headline; subline placement is NOT permitted -- an output with any vocabulary
  ID on a subline fails C-20 regardless of other compliance).
- **CONSTRAINT MANIFEST -- C-20 row**: governed by C-20 (the row constraint requires VM Row ID
  in ## headline; subline placement is NOT permitted -- an output with any vocabulary ID on a
  subline fails C-20 regardless of other compliance).
- **STEP 3B -- Per-Ticket Vocabulary Commitment Table**: governed by C-20 (VM Row ID must
  appear in ## headline; subline placement is NOT permitted -- an output with any vocabulary
  ID on a subline fails C-20 regardless of other compliance).
- **VOCABULARY PRE-FLIGHT GATE**: governed by C-21 (exactly five items (a)-(e) with individual
  PASS/FAIL states; item (e) named "inter-role register differentiation").
- **STEP 4 -- PERFORMANCE MODE DECLARATION**: governed by C-20 (VM Row ID must appear in ##
  headline inline; subline placement is NOT permitted -- an output with any vocabulary ID on
  a subline fails C-20 regardless of other compliance).
- **STEP 6 -- Ticket Bodies**: governed by C-20 (VM Row ID must appear in ## headline; subline
  placement is NOT permitted -- an output with any vocabulary ID on a subline fails C-20
  regardless of other compliance).
- **VERIFICATION MANIFEST**: governed by C-20 count row (## headlines with inline ID = total)
  and C-21 per-item evidence rows (five individual rows for gate items (a)-(e) with individual
  Required/Actual/Pass? cells).

Precedence: If any restating position conflicts with this contract, this contract governs.

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. VM Row IDs appear in this manifest, the commitment table, and the ## headline
annotation (per Compliance Contract C-20). An output placing any VM Row ID on a subline
instead of the ## headline fails C-20 regardless of other compliance -- this table is the
source registry; every ID from this table must appear on a ## headline, never a subline.**

[15-row table same as V-01]

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

[Same as V-01 -- C-20 row label carries consequence clause]

---

[STEP 1 through STEP 8 and VERIFICATION MANIFEST -- same as V-01]
```

---

---

## V-05 -- Full Synthesis: All Three Axes + RESTATING POSITIONS Updated

**Axes:** V-01 + V-02 + V-03. RESTATING POSITIONS: seven governed sites (same as V-04). The maximum-coverage form. Consequence-form fires at every VM Row ID touch-point across the full lifecycle: ID creation (VOCABULARY MANIFEST header) → planning constraint (CONSTRAINT MANIFEST row) → per-ticket commitment (STEP 3B) → mid-sequence gate (STEP 5 TABLE CHECK) → body generation (STEP 6 header + body template) → post-generation verification (VERIFICATION MANIFEST header).

**Hypothesis:** Full synthesis. Candidate C-33 + C-34 + C-35 all introduced together plus registry coherence C-37. Six distinct CF sites -- one more than R9 V-05 (five sites).

---

```
You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### COMPLIANCE CONTRACT

[C-20 clause, C-21 clause, compliant sample -- same as V-01]

**RESTATING POSITIONS**

[Seven-entry version from V-04 -- VOCABULARY MANIFEST + CONSTRAINT MANIFEST C-20 row +
STEP 3B + VOCABULARY PRE-FLIGHT GATE + STEP 4 + STEP 6 + VERIFICATION MANIFEST]

---

### VOCABULARY MANIFEST

[Header with consequence-form from V-02]
[15-row table same as V-01]

---

### CONSTRAINT MANIFEST

[C-20 row with consequence clause from V-01]

---

### STEP 1 through STEP 3B -- same as V-01

---

### STEP 5 -- Ticket Inventory Table

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume within Constraint Manifest ceilings: MATCH / FAIL
- All STEP 3B rows have valid VM Row IDs from VOCABULARY MANIFEST: Y / N
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline -- subline
  placement is NOT permitted; an output with any vocabulary ID on a subline fails C-20
  regardless of other compliance: Y / N
- Compliance Contract C-21: gate items (a)-(e) all PASS: Y / N

---

### STEP 6 -- Ticket Bodies

**Per Compliance Contract above (STEP 6 governed by C-20): VM Row ID must appear in ##
headline; subline placement is NOT permitted -- an output with any vocabulary ID on a subline
fails C-20 regardless of other compliance.**

[Body template with C-20 reminder -- same as V-01]

---

[STEP 7, STEP 7B, STEP 8 -- same as V-01]

---

### VERIFICATION MANIFEST

**Per Compliance Contract above -- this manifest carries C-20 count row and C-21 per-item
evidence rows. An output with any vocabulary ID on a subline fails C-20 regardless of other
compliance -- verify via the C-20 count row below.**

[15-row table same as V-01]
```

---

**Note on existing R10 file:** `listen-support-variate-R10-2026-03-16.md` already exists from a prior session and probes different territory (V-03 there introduces a dual-case failing-form counterexample in the CONTRACT sample -- candidate C-36). These two R10 variation sets are complementary, not duplicate. The existing file's V-03 is the stronger novel probe; the C-35 mid-sequence gate axis above overlaps with that file's V-01. If only one R10 set is scored, prefer the existing file's set for C-36 novelty. If both are scored, the overlapping V-01/V-03 axes between the two files will confirm C-34/C-35 jointly.
