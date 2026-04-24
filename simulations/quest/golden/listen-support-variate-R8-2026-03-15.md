# listen-support -- Variations, Round 8 (rubric v8 -- 27 criteria)

**Date:** 2026-03-15
**Rubric target:** v8 (C-01 through C-27 -- 27 criteria; aspirational denominator = 19)
**Baseline:** R7 V-02 / V-03 / V-04 (composite 98.95 under v8 -- three distinct 17/19 paths)
**R8 objective:** Achieve composite 100 under v8 by combining C-25 + C-26 + C-27 in a single
variation. No R7 variation holds all three simultaneously. R8 isolates each new criterion as a
single-axis variation (confirming which structural elements are load-bearing), then combines
them to find the composite-100 path.

**The three new v8 criteria and their R7 sources:**

- **C-25 -- Per-Item C-21 Gate Evidence Rows in VM**: Five individually named VERIFICATION
  MANIFEST rows (one per gate item (a)-(e)) with Required/Actual/Pass? cells each, replacing
  the single aggregate summary row. R7 V-02-class introduces this pattern.

- **C-26 -- Contract Enforcement Site Registry with Precedence Declaration**: COMPLIANCE
  CONTRACT contains a RESTATING POSITIONS section naming all governed downstream sites (STEP 3B,
  STEP 4, VERIFICATION MANIFEST), a precedence declaration ("this contract governs in case of
  conflict"), and back-references at each named site. R7 V-03-class introduces this pattern.

- **C-27 -- Consequence-Form Criterion-Citing Prohibition Statement**: At least one prohibition
  statement names the specific criterion violated ("fails C-20"), declares the failure
  deterministic, and includes a "regardless of other compliance" qualifier. R7 V-04-class
  introduces this pattern. R7 V-01 uses a consequence-adjacent form but omits the criterion
  citation -- it fails C-27.

**R7 gap analysis (what is and is not settled):**

- R7 V-02-class: composite 98.95 (passes C-09-C-22 + C-23 + C-24 + C-25; fails C-26 and C-27).
  Five individual per-item rows in VM replace the summary row. Contract retains full R6 V-03
  sample + prohibition; no RESTATING POSITIONS section; permission-form prohibition only.
- R7 V-03-class: composite 98.95 (passes C-09-C-24 + C-26; fails C-25 and C-27). CONTRACT adds
  RESTATING POSITIONS section + precedence + back-references. VM retains single C-21 summary row;
  permission-form prohibition only.
- R7 V-04-class: composite 98.95 (passes C-09-C-24 + C-25 + C-27; fails C-22 and C-26).
  Consequence-form prohibition + individual per-item rows. But V-04 removes the sample header
  from the contract -- C-22 fails (sample required), dragging C-26 with it (C-26 requires C-22).

**R8 questions:**
1. Can C-25 (per-item rows) be grafted onto R6 V-03 base without disturbing C-22 or C-23? (V-01)
2. Can C-26 (enforcement registry) be grafted onto R6 V-03 base without disturbing C-25? (V-02)
3. Can C-27 (consequence-form prohibition) be grafted onto R6 V-03 without disturbing C-22? (V-03)
4. Do C-25 + C-26 compose cleanly? (V-04)
5. Do all three compose simultaneously -- the composite-100 path? (V-05)

---

## Fixed Components Applied to All R8 Variations

All R8 variations inherit the full R6 V-03 mechanism set. These are not the differentiating axes.

| Component | R6 V-03 source | R8 status |
|-----------|---------------|-----------|
| COMPLIANCE CONTRACT with sample header + prohibition + 5-item mandate -- C-22 | R6 V-03 | Retained (extended in V-02/V-04/V-05) |
| VM Row ID in ## headline *(VM: VM-xxx-P#)* -- C-20 | R6 V-03 | Retained |
| 5-item gate (a)-(e) with GATE: OPEN/CLOSED -- C-21 | R6 V-03 | Retained |
| CONSTRAINT MANIFEST C-20 count row | R6 V-03 | Retained |
| STEP 3B obligation header citing contract (C-23 site 1) | R6 V-03 | Retained (extended V-02/V-04/V-05) |
| STEP 4 obligation header citing contract (C-23 site 2) | R6 V-03 | Retained (extended V-02/V-04/V-05) |
| VERIFICATION MANIFEST C-20 count row | R6 V-03 | Retained |
| VERIFICATION MANIFEST C-21 summary row | R6 V-03 | Retained in V-02/V-03; replaced by 5 rows in V-01/V-04/V-05 |
| Character-embodiment PERFORMANCE MODE with migration backstory | R6 V-03 | Retained |
| Phase Map Table -- C-14 | All R6 | Retained |
| Theme declaration before inventory -- C-09 | All R6 | Retained |
| Role-Phase Cross-Matrix -- C-12 | All R6 | Retained |
| Ticket inventory table + TABLE CHECK | All R6 | Retained |
| Cross-ticket patterns -- C-09 | All R6 | Retained |
| Resolution paths table -- C-10 | All R6 | Retained |
| Gap analysis with T-NN refs -- C-04/C-08 | All R6 | Retained |

---

## R8 Variation Axes

R1: role sequence, output format, lifecycle emphasis.
R2: phrasing register, inertia framing, theme-first generation.
R3: vocabulary commitment from phase pools, manifest tables, role-phase matrix.
R4: fusing C-16 (per-ticket commitment) with C-17 (role-phase matrix).
R5: C-18 (3-node ID chain) and C-19 (standalone gate) added to R4 V-05 base.
R6: C-20 (headline placement), C-21 (letter-labeled 5-item gate), C-22 (COMPLIANCE CONTRACT).
    R6 V-03 is composite 100 under v7.
R7: isolating load-bearing elements of each of the three v7 new criteria. Each of
    V-02/V-03/V-04 passes exactly one or two of the three new v8 criteria.
R8: combining C-25 + C-26 + C-27 simultaneously. Single-axis first, then combined.

| Axis | Variation | New angle vs prior rounds | Target criteria |
|------|-----------|--------------------------|-----------------|
| Lifecycle emphasis | V-01 | Five per-item C-21 rows in VM on R6 V-03 base (no contract changes) | C-25 |
| Output format | V-02 | RESTATING POSITIONS registry in contract on R6 V-03 base (no VM row changes) | C-26 |
| Phrasing register | V-03 | Consequence-form prohibition on R6 V-03 base (no registry, no per-item rows) | C-27 |

Combined: V-04 stacks V-01 (per-item rows) + V-02 (enforcement registry). V-05 is full
synthesis: R6 V-03 base + V-01 per-item rows + V-02 enforcement registry + V-03 consequence-form
prohibition -- the composite-100 candidate.

---

## V-01 -- Single Axis: Lifecycle Emphasis (Per-Item C-21 Gate Rows in VM)

**Axis:** Lifecycle emphasis -- the VERIFICATION MANIFEST C-21 summary row is replaced with five
individual rows, one per gate item (a)-(e), each named explicitly with its own
Required/Actual/Pass? cells. The COMPLIANCE CONTRACT is unchanged from R6 V-03 (sample header
+ permission-form prohibition + 5-item mandate). No RESTATING POSITIONS section added. No
consequence-form language introduced.

**Hypothesis:** Adding five individual C-21 gate-item rows to the VM is a fully additive change.
No existing mechanism is removed or modified. Predicted composite: 98.95 (passes C-09-C-24 +
C-25; fails C-26 and C-27). V-01 establishes the C-25 baseline independently before combining.

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

**Compliant body header sample:**
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
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                    | "I'm seeing users who completed onboarding dropping off at [stage]..."                        |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location  | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                  | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability                | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present            | "I just switched from [old approach] and expected [X] but instead got [Y]..."                |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks             | "I got the basics working but now [advanced scenario] fails with [error]..."                  |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time    | "I've been using {topic} for [N] months and I'm noticing [concern]..."                       |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                                | Required                     | Committed value |
|------------------------------------------------------------------|------------------------------|-----------------|
| Total tickets                                                    | 6 to 12                      | ___             |
| Phase 1 tickets (day 0-30)                                       | >= 3                         | ___             |
| Phase 2 tickets (day 31-60)                                      | >= 2                         | ___             |
| Phase 3 tickets (day 61-90)                                      | >= 1                         | ___             |
| P0 ceiling                                                       | <= floor(total x 0.25) = ___ | ___             |
| High-volume ceiling                                              | <= floor(total x 0.50) = ___ | ___             |
| Distinct named personas                                          | >= 3                         | ___             |
| SRE tickets                                                      | >= 2                         | ___             |
| Support tickets                                                  | >= 2                         | ___             |
| C-xx tickets                                                     | >= 2 (max 2 per single C-xx) | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                  | >= 3                         | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                | >= 1                         | ___             |
| Tickets with VM Row ID in commitment table (C-16)                | = total ticket count         | ___             |
| Tickets with VM Row ID in ## headline (Compliance Contract C-20) | = total ticket count         | ___             |

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
(expanded). Compliance Contract C-20 governs body header format -- VM Row ID in ## headline.
Subline placement is NOT permitted.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___"                    |
| T-02 | VM-___-P___ | Phase ___ | "___"                    |
| T-03 | VM-___-P___ | Phase ___ | "___"                    |
| ...  |             |           |                          |

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
subline placement is NOT permitted:
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

| Verification target                                              | Required              | Actual | Pass? |
|------------------------------------------------------------------|-----------------------|--------|-------|
| Total tickets                                                    | = Constraint Manifest | ___    | ___   |
| Distinct categories                                              | >= 2                  | ___    | ___   |
| Distinct personas                                                | >= 3                  | ___    | ___   |
| Bodies starting with committed phrase                            | = total               | ___    | ___   |
| ## headlines with *(VM: VM-xxx-P#)* inline -- C-20              | = total               | ___    | ___   |
| VM Row IDs in headlines resolve to STEP 3B rows                  | = total               | ___    | ___   |
| VM Row IDs in STEP 3B resolve to VOCABULARY MANIFEST rows        | = total               | ___    | ___   |
| (a) VOCABULARY MANIFEST completeness -- C-21                     | all combos have rows  | ___    | ___   |
| (b) Commitment table completeness -- C-21                        | rows = ticket count   | ___    | ___   |
| (c) Phrase-to-cell traceability -- C-21                          | all phrases traceable | ___    | ___   |
| (d) Phase-register alignment -- C-21                             | P1=discovery, P3=ops  | ___    | ___   |
| (e) Inter-role register differentiation -- C-21                  | >= 2 roles differ     | ___    | ___   |
| No third-person role reference                                   | = total               | ___    | ___   |
| Phase 1 discovery register                                       | >= 3                  | ___    | ___   |
| Phase 3 operational register                                     | >= 1                  | ___    | ___   |
```

---

---

## V-02 -- Single Axis: Output Format (Contract Enforcement Site Registry)

**Axis:** Output format -- the COMPLIANCE CONTRACT gains a RESTATING POSITIONS sub-section
naming every downstream section that carries contract-derived obligations (STEP 3B, VOCABULARY
PRE-FLIGHT GATE, STEP 4, VERIFICATION MANIFEST), a precedence declaration ("this contract
governs in case of conflict"), and back-references at each named section. The VERIFICATION
MANIFEST retains the single C-21 summary row. Prohibition statement remains permission-form.

**Hypothesis:** Adding the enforcement site registry and precedence declaration is a pure
additive change to the contract block and each named section. Cannot degrade C-22 (contract
block remains with sample + prohibition + mandate), C-23 (multi-site anchoring unchanged), or
C-25 (VM row structure unchanged -- single summary row). Predicted composite: 98.95 (passes
C-09-C-24 + C-26; fails C-25 and C-27). V-02 establishes the C-26 baseline independently.

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
  appear in ## headline; subline placement is NOT permitted).
- **VOCABULARY PRE-FLIGHT GATE**: governed by C-21 (exactly five items (a)-(e) with individual
  PASS/FAIL states; item (e) named "inter-role register differentiation").
- **STEP 4 -- PERFORMANCE MODE DECLARATION**: governed by C-20 (VM Row ID must appear in ##
  headline inline; subline placement is NOT permitted).
- **VERIFICATION MANIFEST**: governed by C-20 count row (## headlines with inline ID = total)
  and C-21 evidence row (gate items (a)-(e) all PASS).

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
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                    | "I'm seeing users who completed onboarding dropping off at [stage]..."                        |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location  | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                  | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability                | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present            | "I just switched from [old approach] and expected [X] but instead got [Y]..."                |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks             | "I got the basics working but now [advanced scenario] fails with [error]..."                  |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time    | "I've been using {topic} for [N] months and I'm noticing [concern]..."                       |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                                | Required                     | Committed value |
|------------------------------------------------------------------|------------------------------|-----------------|
| Total tickets                                                    | 6 to 12                      | ___             |
| Phase 1 tickets (day 0-30)                                       | >= 3                         | ___             |
| Phase 2 tickets (day 31-60)                                      | >= 2                         | ___             |
| Phase 3 tickets (day 61-90)                                      | >= 1                         | ___             |
| P0 ceiling                                                       | <= floor(total x 0.25) = ___ | ___             |
| High-volume ceiling                                              | <= floor(total x 0.50) = ___ | ___             |
| Distinct named personas                                          | >= 3                         | ___             |
| SRE tickets                                                      | >= 2                         | ___             |
| Support tickets                                                  | >= 2                         | ___             |
| C-xx tickets                                                     | >= 2 (max 2 per single C-xx) | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                  | >= 3                         | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                | >= 1                         | ___             |
| Tickets with VM Row ID in commitment table (C-16)                | = total ticket count         | ___             |
| Tickets with VM Row ID in ## headline (Compliance Contract C-20) | = total ticket count         | ___             |

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
(expanded). Per Compliance Contract above -- VM Row ID in ## headline; subline placement
is NOT permitted.**

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
Per Compliance Contract above -- VM Row ID inline on ## headline; subline placement NOT
permitted:
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
Per Compliance Contract above -- VM Row ID is on the ## line, not on any subline.]
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

**Per Compliance Contract above -- this manifest carries C-20 count row and C-21 evidence row.**

| Verification target                                              | Required              | Actual | Pass? |
|------------------------------------------------------------------|-----------------------|--------|-------|
| Total tickets                                                    | = Constraint Manifest | ___    | ___   |
| Distinct categories                                              | >= 2                  | ___    | ___   |
| Distinct personas                                                | >= 3                  | ___    | ___   |
| Bodies starting with committed phrase                            | = total               | ___    | ___   |
| ## headlines with *(VM: VM-xxx-P#)* inline -- C-20              | = total               | ___    | ___   |
| VM Row IDs in headlines resolve to STEP 3B rows                  | = total               | ___    | ___   |
| VM Row IDs in STEP 3B resolve to VOCABULARY MANIFEST rows        | = total               | ___    | ___   |
| Gate items (a)-(e) all PASS -- C-21                              | = 5                   | ___    | ___   |
| Item (e) inter-role example explicitly cited                     | = 1                   | ___    | ___   |
| No third-person role reference                                   | = total               | ___    | ___   |
| Phase 1 discovery register                                       | >= 3                  | ___    | ___   |
| Phase 3 operational register                                     | >= 1                  | ___    | ___   |
```

---

---

## V-03 -- Single Axis: Phrasing Register (Consequence-Form Criterion-Citing Prohibition)

**Axis:** Phrasing register -- the prohibition statement in the COMPLIANCE CONTRACT C-20 clause
is upgraded from permission-form to consequence-form: "an output with any vocabulary ID on a
subline fails C-20 regardless of other compliance." This form names the specific criterion
(C-20), declares the failure deterministic, and includes the "regardless of other compliance"
qualifier. No RESTATING POSITIONS section added. VERIFICATION MANIFEST retains single C-21
summary row.

**Hypothesis:** C-27 requires exactly this form: criterion citation ("fails C-20") +
deterministic declaration + "regardless" qualifier. R6 V-03 uses permission-form only ("NOT
permitted") -- fails C-27. R7 V-01 uses consequence-adjacent form ("any ticket body...fails")
but omits criterion citation and "regardless" qualifier -- fails C-27. V-03 consequence-form is
the minimal sufficient addition. Cannot degrade C-22 (contract structure unchanged -- sample
still present), C-23 (multi-site prohibition sites unchanged), or C-24 (VM row structure
unchanged). Predicted composite: 98.95 (passes C-09-C-24 + C-27; fails C-25 and C-26). V-03
establishes the C-27 baseline independently.

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
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                    | "I'm seeing users who completed onboarding dropping off at [stage]..."                        |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location  | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                  | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability                | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present            | "I just switched from [old approach] and expected [X] but instead got [Y]..."                |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks             | "I got the basics working but now [advanced scenario] fails with [error]..."                  |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time    | "I've been using {topic} for [N] months and I'm noticing [concern]..."                       |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                                | Required                     | Committed value |
|------------------------------------------------------------------|------------------------------|-----------------|
| Total tickets                                                    | 6 to 12                      | ___             |
| Phase 1 tickets (day 0-30)                                       | >= 3                         | ___             |
| Phase 2 tickets (day 31-60)                                      | >= 2                         | ___             |
| Phase 3 tickets (day 61-90)                                      | >= 1                         | ___             |
| P0 ceiling                                                       | <= floor(total x 0.25) = ___ | ___             |
| High-volume ceiling                                              | <= floor(total x 0.50) = ___ | ___             |
| Distinct named personas                                          | >= 3                         | ___             |
| SRE tickets                                                      | >= 2                         | ___             |
| Support tickets                                                  | >= 2                         | ___             |
| C-xx tickets                                                     | >= 2 (max 2 per single C-xx) | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                  | >= 3                         | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                | >= 1                         | ___             |
| Tickets with VM Row ID in commitment table (C-16)                | = total ticket count         | ___             |
| Tickets with VM Row ID in ## headline (Compliance Contract C-20) | = total ticket count         | ___             |

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
(expanded). Compliance Contract C-20 governs body header format -- VM Row ID in ## headline.
Subline placement is NOT permitted -- an output with any vocabulary ID on a subline fails C-20
regardless of other compliance.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___"                    |
| T-02 | VM-___-P___ | Phase ___ | "___"                    |
| T-03 | VM-___-P___ | Phase ___ | "___"                    |
| ...  |             |           |                          |

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
Use the body header format per Compliance Contract C-20 -- VM Row ID inline on the ## headline;
subline placement is NOT permitted -- an output with any vocabulary ID on a subline fails C-20
regardless of other compliance:
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
C-20: VM Row ID is on the ## line above -- not on any subline. Any vocabulary ID on a
subline fails C-20 regardless of other compliance.]
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

| Verification target                                              | Required              | Actual | Pass? |
|------------------------------------------------------------------|-----------------------|--------|-------|
| Total tickets                                                    | = Constraint Manifest | ___    | ___   |
| Distinct categories                                              | >= 2                  | ___    | ___   |
| Distinct personas                                                | >= 3                  | ___    | ___   |
| Bodies starting with committed phrase                            | = total               | ___    | ___   |
| ## headlines with *(VM: VM-xxx-P#)* inline -- C-20              | = total               | ___    | ___   |
| VM Row IDs in headlines resolve to STEP 3B rows                  | = total               | ___    | ___   |
| VM Row IDs in STEP 3B resolve to VOCABULARY MANIFEST rows        | = total               | ___    | ___   |
| Gate items (a)-(e) all PASS -- C-21                              | = 5                   | ___    | ___   |
| Item (e) inter-role example explicitly cited                     | = 1                   | ___    | ___   |
| No third-person role reference                                   | = total               | ___    | ___   |
| Phase 1 discovery register                                       | >= 3                  | ___    | ___   |
| Phase 3 operational register                                     | >= 1                  | ___    | ___   |
```

---

---

## V-04 -- Combined: Lifecycle Emphasis + Output Format (C-25 + C-26)

**Axes:** Lifecycle emphasis (C-25: per-item VM rows) combined with output format (C-26:
enforcement site registry). V-04 stacks V-01 and V-02 simultaneously: the COMPLIANCE CONTRACT
gains the RESTATING POSITIONS section (from V-02), and the VERIFICATION MANIFEST gains five
individual C-21 gate-item rows (from V-01). No consequence-form prohibition added (C-27 absent).

**Hypothesis:** C-25 and C-26 are structurally orthogonal. The RESTATING POSITIONS section names
VERIFICATION MANIFEST as a governed site -- the exact site where the five C-25 per-item rows
appear. The back-reference at VERIFICATION MANIFEST ("Per Compliance Contract above") now governs
a richer structure: five rows rather than one. Neither mechanism cancels the other. This is the
first R8 variation to simultaneously pass two of the three new criteria. Predicted composite:
99.47 (passes C-09-C-24 + C-25 + C-26; fails C-27).

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
  appear in ## headline; subline placement is NOT permitted).
- **VOCABULARY PRE-FLIGHT GATE**: governed by C-21 (exactly five items (a)-(e) with individual
  PASS/FAIL states; item (e) named "inter-role register differentiation").
- **STEP 4 -- PERFORMANCE MODE DECLARATION**: governed by C-20 (VM Row ID must appear in ##
  headline inline; subline placement is NOT permitted).
- **VERIFICATION MANIFEST**: governed by C-20 count row (## headlines with inline ID = total)
  and C-21 per-item evidence rows (five individual rows for gate items (a)-(e)).

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
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                    | "I'm seeing users who completed onboarding dropping off at [stage]..."                        |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location  | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                  | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability                | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present            | "I just switched from [old approach] and expected [X] but instead got [Y]..."                |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks             | "I got the basics working but now [advanced scenario] fails with [error]..."                  |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time    | "I've been using {topic} for [N] months and I'm noticing [concern]..."                       |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                                | Required                     | Committed value |
|------------------------------------------------------------------|------------------------------|-----------------|
| Total tickets                                                    | 6 to 12                      | ___             |
| Phase 1 tickets (day 0-30)                                       | >= 3                         | ___             |
| Phase 2 tickets (day 31-60)                                      | >= 2                         | ___             |
| Phase 3 tickets (day 61-90)                                      | >= 1                         | ___             |
| P0 ceiling                                                       | <= floor(total x 0.25) = ___ | ___             |
| High-volume ceiling                                              | <= floor(total x 0.50) = ___ | ___             |
| Distinct named personas                                          | >= 3                         | ___             |
| SRE tickets                                                      | >= 2                         | ___             |
| Support tickets                                                  | >= 2                         | ___             |
| C-xx tickets                                                     | >= 2 (max 2 per single C-xx) | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                  | >= 3                         | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                | >= 1                         | ___             |
| Tickets with VM Row ID in commitment table (C-16)                | = total ticket count         | ___             |
| Tickets with VM Row ID in ## headline (Compliance Contract C-20) | = total ticket count         | ___             |

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
(expanded). Per Compliance Contract above -- VM Row ID in ## headline; subline placement
is NOT permitted.**

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
Per Compliance Contract above -- VM Row ID inline on ## headline; subline placement NOT
permitted:
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
Per Compliance Contract above -- VM Row ID is on the ## line, not on any subline.]
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
evidence rows (five individual rows for gate items (a)-(e)).**

| Verification target                                              | Required              | Actual | Pass? |
|------------------------------------------------------------------|-----------------------|--------|-------|
| Total tickets                                                    | = Constraint Manifest | ___    | ___   |
| Distinct categories                                              | >= 2                  | ___    | ___   |
| Distinct personas                                                | >= 3                  | ___    | ___   |
| Bodies starting with committed phrase                            | = total               | ___    | ___   |
| ## headlines with *(VM: VM-xxx-P#)* inline -- C-20              | = total               | ___    | ___   |
| VM Row IDs in headlines resolve to STEP 3B rows                  | = total               | ___    | ___   |
| VM Row IDs in STEP 3B resolve to VOCABULARY MANIFEST rows        | = total               | ___    | ___   |
| (a) VOCABULARY MANIFEST completeness -- C-21                     | all combos have rows  | ___    | ___   |
| (b) Commitment table completeness -- C-21                        | rows = ticket count   | ___    | ___   |
| (c) Phrase-to-cell traceability -- C-21                          | all phrases traceable | ___    | ___   |
| (d) Phase-register alignment -- C-21                             | P1=discovery, P3=ops  | ___    | ___   |
| (e) Inter-role register differentiation -- C-21                  | >= 2 roles differ     | ___    | ___   |
| No third-person role reference                                   | = total               | ___    | ___   |
| Phase 1 discovery register                                       | >= 3                  | ___    | ___   |
| Phase 3 operational register                                     | >= 1                  | ___    | ___   |
```

---

---

## V-05 -- Full Synthesis: All Three Axes (C-25 + C-26 + C-27)

**Axes:** Lifecycle emphasis (C-25) + output format (C-26) + phrasing register (C-27).
V-05 is the composite-100 candidate under v8.

**Structural composition:**
- From V-01/V-04: VERIFICATION MANIFEST has five individual C-21 gate-item rows (C-25).
- From V-02/V-04: COMPLIANCE CONTRACT has RESTATING POSITIONS section naming STEP 3B, VOCABULARY
  PRE-FLIGHT GATE, STEP 4, VERIFICATION MANIFEST + precedence declaration + back-references
  at each named site (C-26).
- From V-03: COMPLIANCE CONTRACT C-20 clause uses consequence-form prohibition -- "an output
  with any vocabulary ID on a subline fails C-20 regardless of other compliance" -- which
  propagates to STEP 3B and STEP 4 through their back-references to the contract (C-27).

**Why V-05 succeeds where all R7 variations failed:**
- R7 V-04-class had C-25 + C-27 but removed the sample header -- failing C-22 and therefore
  C-26. V-05 retains the sample header -- C-22 PASS is preserved.
- R7 V-03-class had C-26 but no consequence-form prohibition and no per-item rows. V-05 adds
  both without removing the registry.
- R7 V-02-class had C-25 but no registry and no consequence-form prohibition. V-05 adds both
  without removing the per-item rows.

**Hypothesis:** The three mechanisms are structurally orthogonal:
- C-27 changes only the prohibition form (not the contract structure -- sample and mandate still
  present). C-22 PASS is maintained. C-27 propagates through back-references at STEP 3B and
  STEP 4, reinforcing C-23 multi-site anchoring.
- C-26 adds a RESTATING POSITIONS block and back-references. The VERIFICATION MANIFEST
  back-reference now correctly describes five per-item C-25 rows rather than a summary row.
- C-25 replaces one VM row with five. This richer structure is correctly anticipated by the
  C-26 RESTATING POSITIONS entry for VERIFICATION MANIFEST.
Predicted composite: 100.0 (all C-09 through C-27 PASS).

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
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                    | "I'm seeing users who completed onboarding dropping off at [stage]..."                        |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location  | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                  | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability                | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present            | "I just switched from [old approach] and expected [X] but instead got [Y]..."                |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks             | "I got the basics working but now [advanced scenario] fails with [error]..."                  |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time    | "I've been using {topic} for [N] months and I'm noticing [concern]..."                       |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                                | Required                     | Committed value |
|------------------------------------------------------------------|------------------------------|-----------------|
| Total tickets                                                    | 6 to 12                      | ___             |
| Phase 1 tickets (day 0-30)                                       | >= 3                         | ___             |
| Phase 2 tickets (day 31-60)                                      | >= 2                         | ___             |
| Phase 3 tickets (day 61-90)                                      | >= 1                         | ___             |
| P0 ceiling                                                       | <= floor(total x 0.25) = ___ | ___             |
| High-volume ceiling                                              | <= floor(total x 0.50) = ___ | ___             |
| Distinct named personas                                          | >= 3                         | ___             |
| SRE tickets                                                      | >= 2                         | ___             |
| Support tickets                                                  | >= 2                         | ___             |
| C-xx tickets                                                     | >= 2 (max 2 per single C-xx) | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                  | >= 3                         | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                | >= 1                         | ___             |
| Tickets with VM Row ID in commitment table (C-16)                | = total ticket count         | ___             |
| Tickets with VM Row ID in ## headline (Compliance Contract C-20) | = total ticket count         | ___             |

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
(expanded). Per Compliance Contract above -- VM Row ID in ## headline; subline placement is
NOT permitted -- an output with any vocabulary ID on a subline fails C-20 regardless of other
compliance.**

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
Per Compliance Contract above -- VM Row ID inline on ## headline; subline placement is NOT
permitted -- an output with any vocabulary ID on a subline fails C-20 regardless of other
compliance:
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
Per Compliance Contract above -- VM Row ID is on the ## line, not on any subline.
Any vocabulary ID on a subline fails C-20 regardless of other compliance.]
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
evidence rows (five individual rows for gate items (a)-(e) with individual Required/Actual/Pass?
cells).**

| Verification target                                              | Required              | Actual | Pass? |
|------------------------------------------------------------------|-----------------------|--------|-------|
| Total tickets                                                    | = Constraint Manifest | ___    | ___   |
| Distinct categories                                              | >= 2                  | ___    | ___   |
| Distinct personas                                                | >= 3                  | ___    | ___   |
| Bodies starting with committed phrase                            | = total               | ___    | ___   |
| ## headlines with *(VM: VM-xxx-P#)* inline -- C-20              | = total               | ___    | ___   |
| VM Row IDs in headlines resolve to STEP 3B rows                  | = total               | ___    | ___   |
| VM Row IDs in STEP 3B resolve to VOCABULARY MANIFEST rows        | = total               | ___    | ___   |
| (a) VOCABULARY MANIFEST completeness -- C-21                     | all combos have rows  | ___    | ___   |
| (b) Commitment table completeness -- C-21                        | rows = ticket count   | ___    | ___   |
| (c) Phrase-to-cell traceability -- C-21                          | all phrases traceable | ___    | ___   |
| (d) Phase-register alignment -- C-21                             | P1=discovery, P3=ops  | ___    | ___   |
| (e) Inter-role register differentiation -- C-21                  | >= 2 roles differ     | ___    | ___   |
| No third-person role reference                                   | = total               | ___    | ___   |
| Phase 1 discovery register                                       | >= 3                  | ___    | ___   |
| Phase 3 operational register                                     | >= 1                  | ___    | ___   |
```

---

---

## Scoring Predictions (v8 rubric)

| Variation | Axes | New criteria targeted | Predicted composite | Notes |
|-----------|------|-----------------------|---------------------|-------|
| V-01 | Lifecycle emphasis | C-25 only | 98.95 (17/19) | Per-item VM rows on R6 V-03 base; fails C-26 + C-27 |
| V-02 | Output format | C-26 only | 98.95 (17/19) | Enforcement registry on R6 V-03 base; fails C-25 + C-27 |
| V-03 | Phrasing register | C-27 only | 98.95 (17/19) | Consequence-form prohibition on R6 V-03 base; fails C-25 + C-26 |
| V-04 | Lifecycle + output | C-25 + C-26 | 99.47 (18/19) | First variation to pass two of three new criteria; fails C-27 only |
| V-05 | All three | C-25 + C-26 + C-27 | 100.0 (19/19) | Composite-100 candidate -- three mechanisms compose cleanly |

**V-05 scoring breakdown:**
```
Essential:       5/5  -> 60.0
Recommended:     3/3  -> 30.0
Aspirational:   19/19 -> 10.0
Composite:      100.0
```

**Critical structural properties of V-05 distinguishing it from all R7 variations:**

1. **Contract sample retained** (C-22 PASS): The COMPLIANCE CONTRACT contains the compliant
   body header sample. This is the element R7 V-04-class removed -- causing C-22 to fail and
   making C-26 impossible. V-05 never removes the sample.

2. **RESTATING POSITIONS section** (C-26 PASS): Naming exactly four governed sites with
   precedence declaration + back-references at each. The VERIFICATION MANIFEST entry correctly
   describes five per-item C-25 rows rather than a summary row -- the C-26 description is
   forward-compatible with C-25.

3. **Consequence-form prohibition** (C-27 PASS): The exact form "fails C-20 regardless of other
   compliance" appears in the contract C-20 clause. This form propagates to STEP 3B and STEP 4
   through their "Per Compliance Contract above" back-references, giving C-27 compliance at
   multiple sites (reinforcing C-23 simultaneously).

4. **Five per-item VM rows** (C-25 PASS): The VERIFICATION MANIFEST has five individual rows
   for gate items (a)-(e), each with Required/Actual/Pass? cells independently. The C-26
   RESTATING POSITIONS entry for VERIFICATION MANIFEST explicitly anticipates this structure.
