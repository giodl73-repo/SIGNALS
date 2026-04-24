# listen-support — Variations, Round 7 (rubric v7 — 25 criteria)

**Date:** 2026-03-16
**Rubric target:** v7 (C-01 through C-25 — 25 criteria; aspirational tier = 17)
**Baseline:** R6 V-05 (Compliance Contract + VM Row IDs in ## headline + 5-item gate; composite 175 candidate)
**R7 objective:** Close the three new aspirational gaps that distinguish v7 from v6:
  - **C-23** — Belt-and-suspenders criterion satisfaction: each rubric criterion has BOTH a
    generation-time instruction (belt) AND a verification-time check (suspenders), both
    labeled with the C-ID. A criterion enforced only at generation or only at verification
    is not belt-and-suspenders.
  - **C-24** — Materialized-view traceability instruction: an explicit instruction to produce
    a materialized view projection showing how each vocabulary ID flows from VOCABULARY MANIFEST
    → STEP 3B commitment table → ticket body ## headline. Includes an orphan-gap check.
  - **C-25** — Criterion-ID-named final verification spine: the final verification block is
    a table with one row per active rubric criterion (C-01 through C-25), each row naming
    the C-ID, criterion name, required condition, actual value, and PASS/PARTIAL/FAIL.

**R6 base:** All R6 V-05 mechanisms retained in all R7 variations:
  Compliance Contract (C-20 + C-21 obligations), VOCABULARY MANIFEST (VM Row IDs), CONSTRAINT
  MANIFEST, VOCABULARY PRE-FLIGHT GATE items (a)-(e), VM Row ID in ## headline annotation,
  letter-labeled 5-item gate, VERIFICATION MANIFEST.

---

## R7 Variation Axes

R1 explored: role sequence, output format, lifecycle emphasis.
R2 explored: phrasing register, inertia framing, theme-first generation.
R3 explored: vocabulary commitment from phase pools, manifest tables, role-phase matrix.
R4 explored: fusing C-16 (per-ticket commitment) with C-17 (role-phase matrix).
R5 explored: C-18 (3-node ID chain) and C-19 (standalone gate) added to R4 V-05 base.
R6 explored: C-20 (headline placement rule) and C-21 (letter-labeled 5-item gate).
R7 explores: C-23 (belt-and-suspenders labels), C-24 (materialized-view instruction),
             C-25 (criterion-ID-named spine).

| Axis | Single-axis variation | New angle vs prior rounds | Target criteria |
|------|-----------------------|--------------------------|-----------------|
| Lifecycle emphasis | V-01 | Criterion-ID-named spine as final STEP 10 block replacing VERIFICATION MANIFEST | C-25 |
| Output format | V-02 | VOCABULARY MATERIALIZATION section after STEP 3B with orphan-gap check | C-24 |
| Phrasing register | V-03 | Belt-and-suspenders labels [C-NN: BELT] at generation steps, [C-NN: SUSPENDERS] at verification checks | C-23 |

Combined: V-04 stacks V-01 (criterion spine) + V-03 (belt-and-suspenders labels).
V-05 is full synthesis: R6 V-05 base + V-01 spine + V-02 materialization + V-03 belt-and-suspenders.

---

## Fixed Changes Applied to All Variations

All R7 variations inherit the full R6 V-05 mechanism set.

| Component | R6 V-05 source | R7 status |
|-----------|----------------|-----------|
| COMPLIANCE CONTRACT (C-20 + C-21) | R6 V-05 | Retained |
| VOCABULARY MANIFEST with VM Row IDs | R6 V-05 | Retained |
| CONSTRAINT MANIFEST | R6 V-05 | Retained |
| VM Row ID in ## headline (C-20) | R6 V-05 | Retained |
| VOCABULARY PRE-FLIGHT GATE (a)-(e) (C-21) | R6 V-05 | Retained |
| VERIFICATION MANIFEST | R6 V-05 | Retained or replaced per variation |

---

## V-01 — Single Axis: Lifecycle Emphasis (Criterion-ID-Named Verification Spine)

**Axis:** Lifecycle emphasis — the output lifecycle ends with a named STEP 10 CRITERION
VERIFICATION SPINE block rather than the VERIFICATION MANIFEST. The spine is a structured
table with one row per active rubric criterion (C-01 through C-25), each row containing the
C-ID, criterion name, required condition, actual value, and PASS/PARTIAL/FAIL. A scorer
reading only the spine can determine the status of every criterion without scanning earlier
sections. The VERIFICATION MANIFEST is replaced; the spine covers all manifest targets and
expands them with criterion-level granularity.

**Hypothesis:** The VERIFICATION MANIFEST in R6 V-05 lists structural properties but does
not name rubric criterion IDs. A scorer must map manifest rows to criteria manually. Adding
an explicit CRITERION VERIFICATION SPINE where each row names the C-ID eliminates this
mapping work and makes the output self-scoring. Predicted C-25 PASS. C-23 and C-24 gaps
remain (no belt-and-suspenders labels, no materialization section). Predicted composite gain:
+5 pts (C-25 PASS) over R6 V-05 baseline.

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
line as the title: `## T-NN -- {Title} *(VM: VM-xxx-P#)*`. The annotation is NOT permitted
on any subline, bullet, or metadata row. A scorer reading only ## lines must see the VM Row
ID without opening any other line.

**C-21 -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item
(e) is named "inter-role register differentiation" and requires citing two roles in the same
phase with distinct register descriptions by VM Row ID. A gate with only four items fails
because item (e) is absent.

**Compliant body header format:**
```
## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"
```

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. VM Row IDs appear in this manifest, the commitment table (STEP 3B), and the
## headline annotation (per Compliance Contract C-20).**

| VM Row ID   | Role    | Phase   | Register description                                                    | Example template phrase                                                                       |
|-------------|---------|---------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..."  |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure           | "I'm seeing [failure] only when [condition] -- I cannot reproduce it on demand..."           |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                    | "We've been running {topic} for [N] weeks and we just noticed [regression]..."               |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly      | "I keep seeing customers hit [obstacle] when they first [action] -- no guidance exists..."   |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause       | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."                |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold   | "This is the [N]th escalation about [failure] this month -- I need a permanent fix..."       |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast           | "First-time activation is lower than projected -- I want to understand..."                   |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                       | "The [metric] is not improving at the expected rate -- I need to investigate..."             |
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                   | "I'm seeing users who completed onboarding dropping off at [stage]..."                        |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability              | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present          | "I just switched from [old approach] and expected [X] but instead got [Y]..."                |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks           | "I got the basics working but now [advanced scenario] fails with [error]..."                  |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time  | "I've been using {topic} for [N] months and I'm noticing [concern]..."                       |

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
  `## T-NN -- {Title} *(VM: VM-xxx-P#)*`  <- VM Row ID on ## line, per C-20.
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

Do not proceed if any check fails.

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

All entries require Tickets: T-NN, T-NN reference.

**Documentation gaps** | Entry | Tickets | Artifact
**Design gaps** | Entry | Tickets | Change required
**Operational gaps** | Entry | Tickets | Process change required

Minimum 2 entries per gap category.

---

### STEP 9 -- Gap Coverage Trace

| Gap entry | Tickets | Gap category | Orphan? |
|-----------|---------|-------------|---------|

After completing:
1. Confirm: "Every gap entry maps to at least one Ticket ID -- no orphan gaps."
2. Confirm: "Every ticket in the inventory appears in at least one gap row."
State: "ORPHAN-FREE" or "ORPHANS FOUND: [list gap entries with no ticket]"

---

### STEP 10 -- CRITERION VERIFICATION SPINE

**Complete one row per active rubric criterion. A scorer reading only this table must be
able to determine PASS/PARTIAL/FAIL for every criterion without consulting earlier sections.
Evidence column: cite the step, table name, or ticket ID that satisfies the criterion.**

| C-ID | Criterion name | Required condition | Actual value | PASS/PARTIAL/FAIL |
|------|---------------|-------------------|--------------|-------------------|
| C-01 | Title field on each card | Title: field with descriptive value on every card | ___ | ___ |
| C-02 | Controlled vocabulary declared and enforced | Vocabulary manifest present; all card values match declared options | ___ | ___ |
| C-03 | First-person voice throughout | All bodies pass first-person check; constraint stated in prompt | ___ | ___ |
| C-04 | Gap analysis with three named sections | Doc/Design/Operational gaps, each with >= 1 named artifact | ___ | ___ |
| C-05 | Minimum ticket count with structural gate | TABLE CHECK block with halt instruction; total >= 7 | ___ | ___ |
| C-06 | [Recommended criterion name] | [Required condition] | ___ | ___ |
| C-07 | [Recommended criterion name] | [Required condition] | ___ | ___ |
| C-08 | [Recommended criterion name] | [Required condition] | ___ | ___ |
| C-09 | [Aspirational criterion name] | [Required condition] | ___ | ___ |
| C-10 | [Aspirational criterion name] | [Required condition] | ___ | ___ |
| C-11 | Phase as named card field | Phase: field present on every card | ___ | ___ |
| C-12 | Fallback-grounded severity | Phase 1 = P2/P3; Phase 3 = P0/P1; no Phase 1 P0/P1 non-outage | ___ | ___ |
| C-13 | Mid-output verification block | Audit block appears between ticket generation and gap analysis | ___ | ___ |
| C-14 | Phase-differentiated body register | Phase 1 bodies use discovery vocabulary; Phase 3 use operational | ___ | ___ |
| C-15 | Temporal adoption window in severity reasoning | Severity tied explicitly to adoption phase window | ___ | ___ |
| C-16 | Prior-tool coverage in verification | Inertia competitor name appears in verification manifest check | ___ | ___ |
| C-17 | Phase-as-severity-key declaration | Phase severity norms stated as inference rule before ticket table | ___ | ___ |
| C-18 | Gate minimum correct at >= 7 | TABLE CHECK minimum sums to >= 7 (not < 7) | ___ | ___ |
| C-19 | TABLE CHECK halt instruction names next step | Halt explicitly blocks progression to named step | ___ | ___ |
| C-20 | VM Row ID in ## headline (Compliance Contract) | All ## ticket headlines carry *(VM: VM-xxx-P#)* inline | ___ | ___ |
| C-21 | Five-item gate all present with item (e) | Gate items (a)-(e) all present; (e) = inter-role differentiation | ___ | ___ |
| C-22 | [Aspirational criterion name] | [Required condition] | ___ | ___ |
| C-23 | Belt-and-suspenders criterion satisfaction | Each key criterion labeled [C-NN: BELT] at generation and [C-NN: SUSPENDERS] at verification | ___ | ___ |
| C-24 | Materialized-view traceability | VOCABULARY MATERIALIZATION table present with orphan-gap check | ___ | ___ |
| C-25 | Criterion-ID-named final verification spine | This table present; one row per criterion; C-IDs in column 1 | ___ | ___ |

**SPINE RESULT:** [ ALL ESSENTIAL PASS ] / [ ESSENTIAL FAILURES: C-___ ]
**COMPOSITE ESTIMATE:** ___/175

---

---

## V-02 — Single Axis: Output Format (Materialized-View Traceability)

**Axis:** Output format -- a VOCABULARY MATERIALIZATION section is inserted immediately after
STEP 3B (the commitment table) and before the VOCABULARY PRE-FLIGHT GATE. The section
produces a two-part output: (1) a materialized-view table mapping each VM Row ID from the
VOCABULARY MANIFEST to its appearance in STEP 3B and the planned ## headline location, and
(2) an orphan-gap check confirming no VM Row ID planned in STEP 3B is absent from ticket
bodies, and no ticket body uses a VM Row ID absent from the manifest. The VERIFICATION
MANIFEST is retained unchanged. C-25 spine is not added (isolates C-24 axis).

**Hypothesis:** R6 V-05 has no explicit materialized-view projection. A scorer checking C-24
must mentally trace VM Row IDs from manifest → STEP 3B → body ## lines. Adding an explicit
VOCABULARY MATERIALIZATION section with an orphan-gap check makes the traceability path
machine-readable and eliminates orphan drift. Predicted C-24 PASS. C-23 and C-25 remain
open. Predicted composite gain: +5 pts over R6 V-05 baseline.

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
line as the title: `## T-NN -- {Title} *(VM: VM-xxx-P#)*`. The annotation is NOT permitted
on any subline, bullet, or metadata row. A scorer reading only ## lines must see the VM Row
ID without opening any other line.

**C-21 -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item
(e) is named "inter-role register differentiation" and requires citing two roles in the same
phase with distinct register descriptions by VM Row ID. A gate with only four items fails
because item (e) is absent.

**Compliant body header format:**
```
## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"
```

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. VM Row IDs appear in this manifest, the commitment table (STEP 3B), and the
## headline annotation (per Compliance Contract C-20). The VOCABULARY MATERIALIZATION section
(after STEP 3B) will map each row ID through all three locations.**

| VM Row ID   | Role    | Phase   | Register description                                                    | Example template phrase                                                                       |
|-------------|---------|---------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..."  |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure           | "I'm seeing [failure] only when [condition] -- I cannot reproduce it on demand..."           |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                    | "We've been running {topic} for [N] weeks and we just noticed [regression]..."               |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly      | "I keep seeing customers hit [obstacle] when they first [action] -- no guidance exists..."   |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause       | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."                |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold   | "This is the [N]th escalation about [failure] this month -- I need a permanent fix..."       |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast           | "First-time activation is lower than projected -- I want to understand..."                   |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                       | "The [metric] is not improving at the expected rate -- I need to investigate..."             |
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                   | "I'm seeing users who completed onboarding dropping off at [stage]..."                        |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability              | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present          | "I just switched from [old approach] and expected [X] but instead got [Y]..."                |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks           | "I got the basics working but now [advanced scenario] fails with [error]..."                  |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time  | "I've been using {topic} for [N] months and I'm noticing [concern]..."                       |

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

### VOCABULARY MATERIALIZATION

**Complete after STEP 3B. This section materializes the full traceability path for every
VM Row ID used in the forecast. Produce two outputs: (1) the materialization table showing
each VM Row ID's path from manifest to output, and (2) the orphan-gap check.**

**Part 1 -- Materialization Table**

| VM Row ID used | In VOCABULARY MANIFEST | In STEP 3B (T-IDs) | Planned ## headline location |
|---------------|----------------------|-------------------|------------------------------|
| VM-___-P___ | YES / N/A | T-___, T-___ | ## T-___ *(VM: VM-___-P___)*, ... |

One row per VM Row ID that appears in STEP 3B. Leave rows unused in STEP 3B out of this
table. All rows must resolve: no VM Row ID in STEP 3B may be absent from this table.

**Part 2 -- Orphan-Gap Check**

Orphan type A (manifest rows with no commitment): List VM Row IDs in VOCABULARY MANIFEST
  that do not appear in STEP 3B and are not marked N/A.
  Result: [ ORPHAN-FREE ] / [ ORPHANS: VM-___-P___ (no STEP 3B entry) ]

Orphan type B (commitment rows with no body): After STEP 6 is complete, re-confirm each
  T-ID in STEP 3B appears in a generated body.
  Result (fill after STEP 6): [ ORPHAN-FREE ] / [ ORPHANS: T-___ (no body generated) ]

State: "MATERIALIZATION COMPLETE -- all [N] VM Row IDs in STEP 3B traced to planned body locations."

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate -- Compliance Contract C-21 governs this section. Execute after
VOCABULARY MATERIALIZATION, before STEP 4. All five items (a)-(e) must be present with
individual PASS/FAIL states. GATE: OPEN or GATE: CLOSED. Body generation blocked if CLOSED.**

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
  `## T-NN -- {Title} *(VM: VM-xxx-P#)*`  <- VM Row ID on ## line, per C-20.
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

Do not proceed if any check fails.

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
C-20: VM Row ID is in the ## line above per Compliance Contract.
VOCABULARY MATERIALIZATION orphan type B: confirm this T-ID resolves from STEP 3B.]
```

After generating all bodies, complete VOCABULARY MATERIALIZATION Part 2 (Orphan type B check).

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

All entries require Tickets: T-NN, T-NN reference.

**Documentation gaps** | Entry | Tickets | Artifact
**Design gaps** | Entry | Tickets | Change required
**Operational gaps** | Entry | Tickets | Process change required

Minimum 2 entries per gap category.

---

### STEP 9 -- Gap Coverage Trace

| Gap entry | Tickets | Gap category | Orphan? |
|-----------|---------|-------------|---------|

After completing:
1. Confirm: "Every gap entry maps to at least one Ticket ID -- no orphan gaps."
2. Confirm: "Every ticket appears in at least one gap row."
State: "ORPHAN-FREE" or "ORPHANS FOUND: [list]"

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
| VOCABULARY MATERIALIZATION table present | = 1 | ___ | ___ |
| Orphan type A check completed and ORPHAN-FREE | YES/NO | ___ | ___ |
| Orphan type B check completed and ORPHAN-FREE | YES/NO | ___ | ___ |

---

---

## V-03 — Single Axis: Phrasing Register (Belt-and-Suspenders Labels)

**Axis:** Phrasing register -- every key rubric criterion receives a dual-label treatment.
At the generation-time instruction step, the instruction is annotated `[C-NN: BELT]`. At the
corresponding verification check, the same criterion is annotated `[C-NN: SUSPENDERS]`. The
labels appear inline adjacent to the instruction and check text. A scorer can grep for
`[C-01: BELT]` to find the generation instruction and `[C-01: SUSPENDERS]` to find the
verification check, for every criterion from C-01 through C-21. The VERIFICATION MANIFEST
is retained unchanged. C-24 materialization and C-25 spine are not added (isolates C-23 axis).

**Hypothesis:** R6 V-05 contains generation instructions and verification checks for most
criteria but does not name the C-ID at both locations. A scorer must infer which instruction
covers which criterion. Adding explicit belt-and-suspenders labels at both locations makes
the redundant enforcement visible and named. Predicted C-23 PASS. C-24 and C-25 remain open.
Predicted composite gain: +5 pts over R6 V-05 baseline.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### COMPLIANCE CONTRACT

**Read before any step. These two obligations govern the entire output.**

**[C-20: BELT] -- Vocabulary ID in ## headline:**
Every ticket body ## headline must include the VM Row ID as an inline annotation on the same
line as the title: `## T-NN -- {Title} *(VM: VM-xxx-P#)*`. The annotation is NOT permitted
on any subline, bullet, or metadata row. A scorer reading only ## lines must see the VM Row
ID without opening any other line.

**[C-21: BELT] -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item
(e) is named "inter-role register differentiation" and requires citing two roles in the same
phase with distinct register descriptions by VM Row ID. A gate with only four items fails
because item (e) is absent.

**[C-03: BELT] -- First-person voice:**
Every ticket body is written in first person. No role titles in body text: never write
"the SRE", "the PM", "the user", "the developer", or any role-preceding-verb form.

**[C-01: BELT] -- Title field:**
Every card must include `Title:` as a discrete named field with a descriptive subject line
value. Embedding the title in the ## heading only does not satisfy this criterion.

**Compliant body header format:**
```
## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Title: {descriptive subject line}
- Committed phrase: "{phrase from STEP 3B}"
```

---

### VOCABULARY MANIFEST

**[C-02: BELT] -- Controlled vocabulary source. Complete before generating any ticket.
Customize for {topic}. Mark N/A for unused combinations. VM Row IDs appear in this manifest,
the commitment table (STEP 3B), and the ## headline annotation (per C-20 Compliance Contract).
All Category/Volume/Severity values in ticket cards MUST match the declared controlled
vocabulary. Free-form variants are not accepted.**

| VM Row ID   | Role    | Phase   | Register description                                                    | Example template phrase                                                                       |
|-------------|---------|---------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..."  |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure           | "I'm seeing [failure] only when [condition] -- I cannot reproduce it on demand..."           |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                    | "We've been running {topic} for [N] weeks and we just noticed [regression]..."               |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly      | "I keep seeing customers hit [obstacle] when they first [action] -- no guidance exists..."   |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause       | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."                |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold   | "This is the [N]th escalation about [failure] this month -- I need a permanent fix..."       |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast           | "First-time activation is lower than projected -- I want to understand..."                   |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                       | "The [metric] is not improving at the expected rate -- I need to investigate..."             |
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                   | "I'm seeing users who completed onboarding dropping off at [stage]..."                        |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability              | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present          | "I just switched from [old approach] and expected [X] but instead got [Y]..."                |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks           | "I got the basics working but now [advanced scenario] fails with [error]..."                  |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time  | "I've been using {topic} for [N] months and I'm noticing [concern]..."                       |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

**[C-05: BELT] -- Structural minimums declared here. The TABLE CHECK in STEP 5 enforces
these committed values with a halt instruction. Gate minimum must sum to >= 7 [C-18: BELT].**

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
| Phase 1 bodies with discovery vocabulary [C-14: BELT]            | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary [C-14: BELT]          | >= 1                            | ___             |
| Tickets with VM Row ID in commitment table [C-16: BELT]          | = total ticket count            | ___             |
| Tickets with VM Row ID in ## headline [C-20: BELT confirmed]     | = total ticket count            | ___             |

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

**[C-12: BELT] -- Phase-severity inference rule. Severity must be grounded in adoption phase.
Phase 1 (learning, fallback available): P2/P3. Phase 3 (committed, no fallback): P0/P1.**

| Phase   | Window    | Severity norm | Volume norm  | Body register                           |
|---------|-----------|---------------|--------------|-----------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium  | Discovery/setup -- use VM-xxx-P1 rows   |
| Phase 2 | day 31-60 | P1/P2         | medium       | Integration/edge -- use VM-xxx-P2 rows  |
| Phase 3 | day 61-90 | P0/P1         | low/medium   | Operational/reliability -- use VM-xxx-P3 rows |

**[C-14: BELT] -- Phase-differentiated register. Phase 1 bodies use discovery vocabulary
(learning, migration surprise, setup confusion). Phase 3 bodies use operational vocabulary
(production reliability, no fallback, parity gap).**

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

**[C-16: BELT] -- VM Row ID required in every row. Fill before generating any ticket body.
Reference the VOCABULARY MANIFEST VM Row ID. Derive the committed phrase from that row's
template. Body MUST begin with committed phrase (expanded).
[C-20: BELT confirmed] -- Compliance Contract C-20 governs body header: VM Row ID in ## line.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate -- [C-21: BELT confirmed] -- Compliance Contract C-21 governs this section.
Execute after STEP 3B, before STEP 4. All five items (a)-(e) must be present with individual
PASS/FAIL states. GATE: OPEN or GATE: CLOSED. Body generation blocked if CLOSED.**

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

**[C-03: BELT confirmed] -- Every body: first person. "I", "my", "we". Never "the SRE",
"the user", "the developer". Begin each body with the committed phrase from STEP 3B
(expanded into a full opening sentence).
[C-01: BELT confirmed] -- Every card body must include `Title:` as a discrete named field.
[C-20: BELT triple-confirmed] -- Use the compliant header format:
  `## T-NN -- {Title} *(VM: VM-xxx-P#)*`  <- VM Row ID on ## line, not subline.
[C-14: BELT confirmed] -- Register must match the VOCABULARY MANIFEST row.
[C-21: BELT confirmed] -- Registers MUST differ between roles in same phase per gate item (e).
Migration reference where relevant.**

---

### STEP 5 -- Ticket Inventory Table

**[C-05: BELT confirmed] -- TABLE CHECK enforces structural minimums. Halt instruction below.**

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK -- verify all before proceeding to STEP 6: [C-05: BELT triple, C-18: BELT, C-19: BELT]
- Total rows: ___ (required: matches Constraint Manifest; minimum 7 for gate sum) [C-18: BELT confirmed]
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= Manifest ceiling)
- High-volume count: ___ (required: <= Manifest ceiling)
- All STEP 3B rows have valid VM Row IDs [C-16: BELT confirmed]: Y / N
- Compliance Contract C-20 [C-20: BELT confirmed]: every ## headline will carry *(VM: VM-xxx-P#)*: Y / N
- Compliance Contract C-21 [C-21: BELT confirmed]: gate items (a)-(e) all PASS: Y / N

**Do not proceed to STEP 6 until all TABLE CHECK items are satisfied. [C-19: BELT]**

---

### STEP 6 -- Ticket Bodies (by theme, phase-sorted, ascending T-ID)

```
### Theme A -- {theme name}
*Underlying failure: {from Step 3}*

## T-NN -- {Title} *(VM: VM-xxx-P#)*    <- [C-20: BELT in output]
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Title: {descriptive subject line}    <- [C-01: BELT in output]
- Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences. First person [C-03: BELT in output]. Committed phrase expanded.
Register matches VOCABULARY MANIFEST row [C-14: BELT in output].
Inter-role differentiation per gate item (e) [C-21: BELT in output].
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

**[C-04: BELT] -- Three named sections required. Each section must reference >= 1 named artifact.**

All entries require Tickets: T-NN, T-NN reference.

**Documentation gaps** | Entry | Tickets | Artifact
**Design gaps** | Entry | Tickets | Change required
**Operational gaps** | Entry | Tickets | Process change required

Minimum 2 entries per gap category.

---

### STEP 9 -- Gap Coverage Trace

| Gap entry | Tickets | Gap category | Orphan? |
|-----------|---------|-------------|---------|

After completing:
1. Confirm: "Every gap entry maps to at least one Ticket ID -- no orphan gaps."
2. Confirm: "Every ticket appears in at least one gap row."
State: "ORPHAN-FREE" or "ORPHANS FOUND: [list]"

---

### VERIFICATION MANIFEST

**[C-NN: SUSPENDERS] labels appear on each row below. Each row is the verification-time
counterpart to the [C-NN: BELT] instruction in the generation step.**

| Verification target | C-ID | Required | Actual | Pass? |
|--------------------|------|----------|--------|-------|
| Title field on every card [C-01: SUSPENDERS] | C-01 | Title: field present, descriptive | ___ | ___ |
| Vocabulary values match declared options [C-02: SUSPENDERS] | C-02 | All Category/Volume/Severity values match manifest | ___ | ___ |
| No third-person role reference [C-03: SUSPENDERS] | C-03 | Zero role-title-preceding-verb instances | ___ | ___ |
| Three named gap sections with artifacts [C-04: SUSPENDERS] | C-04 | Doc/Design/Operational present, each >= 1 artifact | ___ | ___ |
| TABLE CHECK with halt instruction [C-05: SUSPENDERS] | C-05 | TABLE CHECK block present; halt instruction names STEP 6 | ___ | ___ |
| Phase 1 discovery register [C-14: SUSPENDERS] | C-14 | >= 3 Phase 1 bodies use VM-xxx-P1 register | ___ | ___ |
| Phase 3 operational register [C-14: SUSPENDERS] | C-14 | >= 1 Phase 3 body uses VM-xxx-P3 register | ___ | ___ |
| VM Row IDs in STEP 3B [C-16: SUSPENDERS] | C-16 | = total ticket count rows with VM Row ID | ___ | ___ |
| Gate minimum >= 7 [C-18: SUSPENDERS] | C-18 | TABLE CHECK minimum sum >= 7 | ___ | ___ |
| Halt instruction names next step [C-19: SUSPENDERS] | C-19 | "Do not proceed to STEP 6" explicit | ___ | ___ |
| ## headlines with VM Row ID [C-20: SUSPENDERS] | C-20 | = total ticket count; inline on ## line | ___ | ___ |
| Gate items (a)-(e) all PASS [C-21: SUSPENDERS] | C-21 | 5 items present; item (e) = inter-role differentiation | ___ | ___ |
| Belt-and-suspenders labels present [C-23: SUSPENDERS] | C-23 | [C-NN: BELT] labels at generation; [C-NN: SUSPENDERS] at verification | ___ | ___ |

---

---

## V-04 — Combined: V-01 (Criterion Spine) + V-03 (Belt-and-Suspenders Labels)

**Combination axes:**
1. From V-01: STEP 10 CRITERION VERIFICATION SPINE replacing VERIFICATION MANIFEST -- one
   row per C-ID (C-01 through C-25) with required condition, actual value, PASS/PARTIAL/FAIL.
2. From V-03: [C-NN: BELT] labels at generation steps, [C-NN: SUSPENDERS] labels in the
   spine table (the spine serves as the consolidated suspenders layer for all criteria).

**Hypothesis:** V-01 achieves C-25 PASS (spine present) but C-23 FAIL (no belt labels at
generation steps). V-03 achieves C-23 PASS (belt labels present, verification manifest has
suspenders labels) but C-25 FAIL (no criterion-ID-named spine). V-04 stacks both: belt
labels at generation steps + spine as the consolidated suspenders. Both C-23 and C-25 should
PASS. C-24 remains open (no materialization section). Predicted composite gain: +10 pts
over R6 V-05 baseline.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### COMPLIANCE CONTRACT

**Read before any step. These two obligations govern the entire output.**

**[C-20: BELT] -- Vocabulary ID in ## headline:**
Every ticket body ## headline must include the VM Row ID as an inline annotation on the same
line as the title: `## T-NN -- {Title} *(VM: VM-xxx-P#)*`. The annotation is NOT permitted
on any subline, bullet, or metadata row. A scorer reading only ## lines must see the VM Row
ID without opening any other line.

**[C-21: BELT] -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item
(e) is named "inter-role register differentiation" and requires citing two roles in the same
phase with distinct register descriptions by VM Row ID. A gate with only four items fails
because item (e) is absent.

**[C-01: BELT] -- Title field on each card:**
Every card must include `Title:` as a discrete named field with a descriptive subject line.

**[C-03: BELT] -- First-person voice:**
Every ticket body is first person. No role titles in body text.

**Compliant body header format:**
```
## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Title: {descriptive subject line}
- Committed phrase: "{phrase from STEP 3B}"
```

---

### VOCABULARY MANIFEST

**[C-02: BELT] -- Controlled vocabulary source. Complete before generating any ticket.
Customize for {topic}. Mark N/A for unused combinations. VM Row IDs appear in this manifest,
the commitment table (STEP 3B), and the ## headline annotation (per C-20 Compliance Contract).
All card values MUST match the declared options.**

| VM Row ID   | Role    | Phase   | Register description                                                    | Example template phrase                                                                       |
|-------------|---------|---------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..."  |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure           | "I'm seeing [failure] only when [condition] -- I cannot reproduce it on demand..."           |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                    | "We've been running {topic} for [N] weeks and we just noticed [regression]..."               |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly      | "I keep seeing customers hit [obstacle] when they first [action] -- no guidance exists..."   |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause       | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."                |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold   | "This is the [N]th escalation about [failure] this month -- I need a permanent fix..."       |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast           | "First-time activation is lower than projected -- I want to understand..."                   |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                       | "The [metric] is not improving at the expected rate -- I need to investigate..."             |
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                   | "I'm seeing users who completed onboarding dropping off at [stage]..."                        |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability              | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present          | "I just switched from [old approach] and expected [X] but instead got [Y]..."                |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks           | "I got the basics working but now [advanced scenario] fails with [error]..."                  |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time  | "I've been using {topic} for [N] months and I'm noticing [concern]..."                       |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

**[C-05: BELT] -- Structural minimums. [C-18: BELT] Gate minimum >= 7. TABLE CHECK in STEP 5
enforces these values with a halt instruction [C-19: BELT] that blocks STEP 6.**

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
| Phase 1 bodies with discovery vocabulary [C-14: BELT]            | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary [C-14: BELT]          | >= 1                            | ___             |
| Tickets with VM Row ID in commitment table [C-16: BELT]          | = total ticket count            | ___             |
| Tickets with VM Row ID in ## headline [C-20: BELT]               | = total ticket count            | ___             |

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

**[C-12: BELT] -- Phase-severity inference. [C-14: BELT] -- Phase-differentiated register.**

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

**[C-16: BELT] -- VM Row ID required in every row. [C-20: BELT] -- VM Row ID goes on ##
headline. Fill before generating any ticket body.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate -- [C-21: BELT] -- Five items (a)-(e) required. GATE: OPEN/CLOSED.**

**(a) VOCABULARY MANIFEST completeness**
State: [ PASS ] / [ FAIL -- missing: ___ ]

**(b) Commitment table completeness**
State: [ PASS -- ___ rows = ___ ] / [ FAIL -- ___ rows != ___ ]

**(c) Phrase-to-manifest traceability**
State: [ PASS -- all ___ traceable ] / [ FAIL -- untraceable: T-___ ]

**(d) Phase-register alignment**
State: [ PASS ] / [ FAIL -- misaligned: T-___ ]

**(e) Inter-role register differentiation**
  Phase ___: VM Row ___ (Role: ___) = "___ register description"
  Phase ___: VM Row ___ (Role: ___) = "___ register description"
State: [ PASS -- example cited above ] / [ FAIL -- no differentiating phase found ]

**GATE: [ OPEN -- (a)(b)(c)(d)(e) all PASS -- proceed to STEP 4 ]**
**GATE: [ CLOSED -- ___ items failed -- revise and re-run ]**

---

### STEP 4 -- PERFORMANCE MODE DECLARATION

**You are about to become each persona. They know what they migrated from.**

**SRE:** On-call. Adopted {topic} because the team moved to it. Methodical but frustrated.
**Support:** Filed to get engineering to fix the root cause.
**PM:** Adoption below forecast. Filing to request data.
**UX:** Watching session recordings. Users stall at a specific point.
**C-xx:** Switched from [old approach in Step 1] recently. Something surprised you.

**[C-03: BELT confirmed] -- First person. "I", "my", "we". No role titles in body.
[C-01: BELT confirmed] -- Include Title: as discrete named field on every card.
[C-20: BELT confirmed] -- `## T-NN -- {Title} *(VM: VM-xxx-P#)*` -- VM Row ID on ## line.
[C-14: BELT confirmed] -- Register must match VOCABULARY MANIFEST row.
[C-21: BELT confirmed] -- Registers MUST differ between roles in same phase.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

**TABLE CHECK [C-05: BELT, C-18: BELT, C-19: BELT] -- Do not proceed to STEP 6 until all pass:**
- Total rows: ___ (required: Constraint Manifest total; gate sum >= 7)
- Distinct categories >= 2, personas >= 3: Y / N
- P0 and high-volume counts within Manifest ceilings: Y / N
- All STEP 3B rows have valid VM Row IDs [C-16: BELT]: Y / N
- C-20 confirmed: every ## headline will carry VM Row ID inline: Y / N
- C-21 confirmed: gate items (a)-(e) all PASS: Y / N

---

### STEP 6 -- Ticket Bodies (by theme, phase-sorted, ascending T-ID)

```
### Theme A -- {theme name}
*Underlying failure: {from Step 3}*

## T-NN -- {Title} *(VM: VM-xxx-P#)*    [C-20: BELT in output]
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Title: {descriptive subject line}    [C-01: BELT in output]
- Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[First person [C-03: BELT]. Committed phrase expanded. Register matches VM row [C-14: BELT].
Inter-role differentiation per (e) [C-21: BELT]. Migration reference where relevant.]
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

**[C-04: BELT] -- Three named sections required. >= 1 named artifact each.**

All entries require Tickets: T-NN, T-NN reference.

**Documentation gaps** | Entry | Tickets | Artifact
**Design gaps** | Entry | Tickets | Change required
**Operational gaps** | Entry | Tickets | Process change required

Minimum 2 entries per gap category.

---

### STEP 9 -- Gap Coverage Trace

| Gap entry | Tickets | Gap category | Orphan? |
|-----------|---------|-------------|---------|

State: "ORPHAN-FREE" or "ORPHANS FOUND: [list]"

---

### STEP 10 -- CRITERION VERIFICATION SPINE

**The CRITERION VERIFICATION SPINE is the consolidated suspenders layer for all criteria
labeled [C-NN: BELT] in the generation steps above. One row per active rubric criterion.
A scorer reading only this table determines PASS/PARTIAL/FAIL for every criterion.**

| C-ID | Criterion name | [C-NN: BELT] location | Required condition | Actual | PASS/PARTIAL/FAIL |
|------|---------------|----------------------|-------------------|--------|-------------------|
| C-01 | Title field on each card [C-01: SUSPENDERS] | Compliance Contract + STEP 4 | Title: field present, descriptive, on every card | ___ | ___ |
| C-02 | Controlled vocabulary [C-02: SUSPENDERS] | VOCABULARY MANIFEST header | All card values match declared options | ___ | ___ |
| C-03 | First-person voice [C-03: SUSPENDERS] | Compliance Contract + STEP 4 | Zero role-title-preceding-verb; constraint stated | ___ | ___ |
| C-04 | Gap analysis three named sections [C-04: SUSPENDERS] | STEP 8 header | Doc/Design/Operational present; >= 1 artifact each | ___ | ___ |
| C-05 | Structural gate with halt [C-05: SUSPENDERS] | CONSTRAINT MANIFEST + TABLE CHECK | TABLE CHECK present; halt names STEP 6 | ___ | ___ |
| C-06 | [Recommended] [C-06: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-07 | [Recommended] [C-07: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-08 | [Recommended] [C-08: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-09 | [Aspirational] [C-09: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-10 | [Aspirational] [C-10: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-11 | Phase as named card field [C-11: SUSPENDERS] | STEP 6 template | Phase: field present on every card | ___ | ___ |
| C-12 | Fallback-grounded severity [C-12: SUSPENDERS] | STEP 2 Phase Map + STEP 4 | Phase 1 = P2/P3; Phase 3 = P0/P1 | ___ | ___ |
| C-13 | Mid-output verification [C-13: SUSPENDERS] | TABLE CHECK position | Audit block between generation and gap analysis | ___ | ___ |
| C-14 | Phase-differentiated register [C-14: SUSPENDERS] | CONSTRAINT MANIFEST + STEP 2 + STEP 4 | Phase 1 discovery >= 3; Phase 3 operational >= 1 | ___ | ___ |
| C-15 | Temporal adoption window in severity [C-15: SUSPENDERS] | STEP 2 Phase Map | Severity tied to adoption window, not impact only | ___ | ___ |
| C-16 | VM Row ID in commitment table [C-16: SUSPENDERS] | STEP 3B header | All STEP 3B rows have VM Row ID | ___ | ___ |
| C-17 | Phase-as-severity-key declaration [C-17: SUSPENDERS] | STEP 2 Phase Map | Phase severity norms stated as rule before table | ___ | ___ |
| C-18 | Gate minimum >= 7 [C-18: SUSPENDERS] | TABLE CHECK | Minimum sum >= 7 confirmed | ___ | ___ |
| C-19 | TABLE CHECK halt names next step [C-19: SUSPENDERS] | TABLE CHECK footer | "Do not proceed to STEP 6" explicit | ___ | ___ |
| C-20 | VM Row ID in ## headline [C-20: SUSPENDERS] | Compliance Contract + STEP 4 + TABLE CHECK | All ## headlines carry *(VM: VM-xxx-P#)* inline | ___ | ___ |
| C-21 | Five-item gate with item (e) [C-21: SUSPENDERS] | Compliance Contract + GATE section | Items (a)-(e) all PASS; (e) cited by VM Row ID | ___ | ___ |
| C-22 | [Aspirational] [C-22: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-23 | Belt-and-suspenders labels [C-23: SUSPENDERS] | Throughout prompt | [C-NN: BELT] present at generation; this spine = suspenders layer | ___ | ___ |
| C-24 | Materialized-view traceability [C-24: SUSPENDERS] | Not in this variation | VOCABULARY MATERIALIZATION section absent | ABSENT | FAIL |
| C-25 | Criterion-ID-named spine [C-25: SUSPENDERS] | This STEP 10 | Spine present; one row per criterion; C-IDs in col 1 | PRESENT | PASS |

**SPINE RESULT:** [ ALL ESSENTIAL PASS ] / [ ESSENTIAL FAILURES: C-___ ]
**COMPOSITE ESTIMATE:** ___/175

---

---

## V-05 — Full Synthesis: C-23 + C-24 + C-25 (Belt-and-Suspenders + Materialization + Spine)

**Full synthesis axis:** All three R7 mechanisms stacked on the R6 V-05 base.
1. From V-03: [C-NN: BELT] labels at all generation steps.
2. From V-02: VOCABULARY MATERIALIZATION section after STEP 3B with orphan-gap check.
3. From V-01: STEP 10 CRITERION VERIFICATION SPINE (the consolidated suspenders layer).
The spine serves as the suspenders for all belt labels; no separate VERIFICATION MANIFEST
is needed. The materialization section is referenced in the spine (C-24 SUSPENDERS row).

**Hypothesis:** V-04 is predicted at +10 pts (C-23 + C-25 PASS). V-05 adds C-24 (materialization)
for an additional +5 pts. Predicted composite: R6 V-05 baseline + 15 pts = 175/175 candidate.
No prior round has stacked all three R7 mechanisms. V-05 is the first composite 175 candidate
under v7, conditional on all C-01 through C-22 criteria also passing.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### COMPLIANCE CONTRACT

**Read before any step. All four obligations govern the entire output.**

**[C-20: BELT] -- Vocabulary ID in ## headline:**
Every ticket body ## headline must include the VM Row ID as an inline annotation on the same
line as the title: `## T-NN -- {Title} *(VM: VM-xxx-P#)*`. The annotation is NOT permitted
on any subline, bullet, or metadata row. A scorer reading only ## lines must see the VM Row
ID without opening any other line.

**[C-21: BELT] -- All five gate items present:**
The VOCABULARY PRE-FLIGHT GATE must check exactly five items labeled (a) through (e). Item
(e) is named "inter-role register differentiation" and requires citing two roles in the same
phase with distinct register descriptions by VM Row ID.

**[C-01: BELT] -- Title field on each card:**
Every card must include `Title:` as a discrete named field with a descriptive subject line.

**[C-03: BELT] -- First-person voice throughout:**
Every ticket body is first person. No role titles in body text. Constraint stated in prompt.

**[C-23: BELT] -- Belt-and-suspenders labeling:**
Every key criterion has a [C-NN: BELT] label at its generation instruction (in this prompt)
and a [C-NN: SUSPENDERS] label at its verification check (in the STEP 10 spine). The spine
is the consolidated suspenders layer.

**[C-24: BELT] -- Materialized-view traceability:**
After STEP 3B, produce the VOCABULARY MATERIALIZATION section mapping every VM Row ID
through VOCABULARY MANIFEST → STEP 3B → ticket body ## headline, with orphan-gap check.

**[C-25: BELT] -- Criterion-ID-named spine:**
STEP 10 is the CRITERION VERIFICATION SPINE: one row per criterion C-01 through C-25,
naming C-ID, criterion name, belt location, required condition, actual value, PASS/PARTIAL/FAIL.

**Compliant body header format:**
```
## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Title: {descriptive subject line}
- Committed phrase: "{phrase from STEP 3B}"
```

---

### VOCABULARY MANIFEST

**[C-02: BELT] -- Controlled vocabulary source. Complete before generating any ticket.
Customize for {topic}. Mark N/A for unused combinations. VM Row IDs appear in this manifest,
the commitment table (STEP 3B), and the ## headline annotation (per C-20 Compliance Contract).
All card Category/Volume/Severity values MUST match declared options. No free-form variants.**

| VM Row ID   | Role    | Phase   | Register description                                                    | Example template phrase                                                                       |
|-------------|---------|---------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..."  |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure           | "I'm seeing [failure] only when [condition] -- I cannot reproduce it on demand..."           |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                    | "We've been running {topic} for [N] weeks and we just noticed [regression]..."               |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly      | "I keep seeing customers hit [obstacle] when they first [action] -- no guidance exists..."   |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause       | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."                |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold   | "This is the [N]th escalation about [failure] this month -- I need a permanent fix..."       |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast           | "First-time activation is lower than projected -- I want to understand..."                   |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                       | "The [metric] is not improving at the expected rate -- I need to investigate..."             |
| VM-PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                   | "I'm seeing users who completed onboarding dropping off at [stage]..."                        |
| VM-UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..."              |
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability              | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present          | "I just switched from [old approach] and expected [X] but instead got [Y]..."                |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks           | "I got the basics working but now [advanced scenario] fails with [error]..."                  |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time  | "I've been using {topic} for [N] months and I'm noticing [concern]..."                       |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

**[C-05: BELT] -- Structural minimums declared here.
[C-18: BELT] -- Gate minimum must sum to >= 7 (P3+P2+P1 phase distribution total).
[C-19: BELT] -- TABLE CHECK in STEP 5 will block STEP 6 with a named halt instruction.**

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
| Phase 1 bodies with discovery vocabulary [C-14: BELT]            | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary [C-14: BELT]          | >= 1                            | ___             |
| Tickets with VM Row ID in commitment table [C-16: BELT]          | = total ticket count            | ___             |
| Tickets with VM Row ID in ## headline [C-20: BELT]               | = total ticket count            | ___             |

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

**[C-12: BELT] -- Phase-severity inference: severity grounded in adoption phase (fallback
availability). [C-14: BELT] -- Phase-differentiated register governs body vocabulary.
[C-17: BELT] -- Phase severity norms stated here as the governing inference rule.**

Inference rule: Phase 1 (learning, fallback available) = P2/P3. Phase 3 (committed, no
fallback) = P0/P1. Phase 1 P0/P1 non-outage is a violation. Phase 3 P3 blocking is a
violation. This rule applies to every severity assignment in the ticket table.

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

**[C-16: BELT] -- VM Row ID required in every row. Derive committed phrase from VM manifest
row template. Body MUST begin with committed phrase (expanded).
[C-20: BELT] -- VM Row ID goes on ## headline per Compliance Contract.
[C-24: BELT] -- VOCABULARY MATERIALIZATION section follows this table.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY MATERIALIZATION

**[C-24: BELT confirmed] -- Produce the materialization table immediately. Show the full
traceability path for every VM Row ID committed in STEP 3B.**

**Part 1 -- Materialization Table**

| VM Row ID used | In VOCABULARY MANIFEST | In STEP 3B (T-IDs) | Planned ## headline location |
|---------------|----------------------|-------------------|------------------------------|
| VM-___-P___ | YES | T-___, T-___ | ## T-___ *(VM: VM-___-P___)*, ... |

One row per VM Row ID appearing in STEP 3B. All rows must resolve.

**Part 2 -- Orphan-Gap Check**

Orphan type A (manifest rows with no commitment):
  Result: [ ORPHAN-FREE ] / [ ORPHANS: VM-___-P___ (no STEP 3B entry) ]

Orphan type B (commitment rows with no body -- fill after STEP 6):
  Result: [ ORPHAN-FREE ] / [ ORPHANS: T-___ (no body generated) ]

State: "MATERIALIZATION COMPLETE -- all [N] VM Row IDs in STEP 3B traced to planned body locations."

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate -- [C-21: BELT confirmed] -- Five items (a)-(e) required. GATE: OPEN/CLOSED.
Body generation blocked if CLOSED.**

**(a) VOCABULARY MANIFEST completeness**
State: [ PASS ] / [ FAIL -- missing: ___ ]

**(b) Commitment table completeness**
State: [ PASS -- ___ rows = ___ ] / [ FAIL -- ___ rows != ___ ]

**(c) Phrase-to-manifest traceability**
State: [ PASS -- all ___ traceable ] / [ FAIL -- untraceable: T-___ ]

**(d) Phase-register alignment**
State: [ PASS ] / [ FAIL -- misaligned: T-___ ]

**(e) Inter-role register differentiation**
  Phase ___: VM Row ___ (Role: ___) = "___ register description"
  Phase ___: VM Row ___ (Role: ___) = "___ register description"
State: [ PASS -- example cited above ] / [ FAIL -- no differentiating phase found ]

**GATE: [ OPEN -- (a)(b)(c)(d)(e) all PASS -- proceed to STEP 4 ]**
**GATE: [ CLOSED -- ___ items failed -- revise and re-run ]**

---

### STEP 4 -- PERFORMANCE MODE DECLARATION

**You are about to become each persona. They know what they migrated from.**

**SRE:** On-call. Adopted {topic} because the team moved to it. Methodical but frustrated.
**Support:** Answered this same question too many times. Filing for a root-cause fix.
**PM:** Adoption below forecast. Filing to request data.
**UX:** Watching session recordings. Users stall at a specific point.
**C-xx:** Switched from [old approach in Step 1] recently. Something surprised you.

**[C-03: BELT confirmed] -- First person. "I", "my", "we". No role titles in body text.
[C-01: BELT confirmed] -- Include Title: as discrete named field on every card.
[C-20: BELT confirmed] -- `## T-NN -- {Title} *(VM: VM-xxx-P#)*` -- VM Row ID on ## line.
[C-14: BELT confirmed] -- Register must match VOCABULARY MANIFEST row.
[C-21: BELT confirmed] -- Registers MUST differ between roles in same phase per gate item (e).
Migration reference where relevant. After STEP 6, complete VOCABULARY MATERIALIZATION Part 2.**

---

### STEP 5 -- Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

**TABLE CHECK [C-05: BELT, C-18: BELT, C-19: BELT] -- Do not proceed to STEP 6 until all pass:**
- Total rows: ___ (required: Constraint Manifest total; gate minimum sum >= 7) [C-18]
- Distinct categories >= 2, personas >= 3: Y / N
- P0 and high-volume counts within Manifest ceilings: Y / N
- All STEP 3B rows have valid VM Row IDs [C-16: BELT]: Y / N
- C-20 confirmed: every ## headline will carry VM Row ID inline: Y / N
- C-21 confirmed: gate items (a)-(e) all PASS: Y / N
- VOCABULARY MATERIALIZATION Part 1 table complete [C-24: BELT]: Y / N

---

### STEP 6 -- Ticket Bodies (by theme, phase-sorted, ascending T-ID)

```
### Theme A -- {theme name}
*Underlying failure: {from Step 3}*

## T-NN -- {Title} *(VM: VM-xxx-P#)*    [C-20: BELT in output]
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Title: {descriptive subject line}    [C-01: BELT in output]
- Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[First person [C-03: BELT]. Committed phrase expanded. Register matches VM row [C-14: BELT].
Phase severity per inference rule [C-12: BELT]. Inter-role differentiation per (e) [C-21: BELT].
Migration reference where relevant.]
```

After all bodies generated: complete VOCABULARY MATERIALIZATION Part 2 (orphan type B check).

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

**[C-04: BELT] -- Three named sections required, >= 1 named artifact each.**

All entries require Tickets: T-NN, T-NN reference.

**Documentation gaps** | Entry | Tickets | Artifact
**Design gaps** | Entry | Tickets | Change required
**Operational gaps** | Entry | Tickets | Process change required

Minimum 2 entries per gap category.

---

### STEP 9 -- Gap Coverage Trace

| Gap entry | Tickets | Gap category | Orphan? |
|-----------|---------|-------------|---------|

After completing:
1. Confirm: "Every gap entry maps to at least one Ticket ID -- no orphan gaps."
2. Confirm: "Every ticket appears in at least one gap row."
State: "ORPHAN-FREE" or "ORPHANS FOUND: [list]"

---

### STEP 10 -- CRITERION VERIFICATION SPINE

**[C-25: BELT confirmed] -- Consolidated suspenders for all [C-NN: BELT] labels in this
prompt. One row per active rubric criterion. Scorer reads only this table to determine
PASS/PARTIAL/FAIL for every criterion.**

| C-ID | Criterion name | [C-NN: BELT] location | Required condition | Actual | PASS/PARTIAL/FAIL |
|------|---------------|----------------------|-------------------|--------|-------------------|
| C-01 | Title field on each card [C-01: SUSPENDERS] | Compliance Contract | Title: field, descriptive, on every card | ___ | ___ |
| C-02 | Controlled vocabulary declared and enforced [C-02: SUSPENDERS] | VOCABULARY MANIFEST header | All card values match declared options | ___ | ___ |
| C-03 | First-person voice throughout [C-03: SUSPENDERS] | Compliance Contract + STEP 4 | Zero role-title-preceding-verb; constraint stated | ___ | ___ |
| C-04 | Gap analysis three named sections [C-04: SUSPENDERS] | STEP 8 header | Doc/Design/Operational; >= 1 artifact each | ___ | ___ |
| C-05 | Structural gate with halt [C-05: SUSPENDERS] | CONSTRAINT MANIFEST + TABLE CHECK | TABLE CHECK present; halt names STEP 6 | ___ | ___ |
| C-06 | [Recommended] [C-06: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-07 | [Recommended] [C-07: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-08 | [Recommended] [C-08: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-09 | [Aspirational] [C-09: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-10 | [Aspirational] [C-10: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-11 | Phase as named card field [C-11: SUSPENDERS] | STEP 6 template | Phase: field on every card | ___ | ___ |
| C-12 | Fallback-grounded severity [C-12: SUSPENDERS] | STEP 2 inference rule | Phase 1 = P2/P3; Phase 3 = P0/P1; violations corrected | ___ | ___ |
| C-13 | Mid-output verification block [C-13: SUSPENDERS] | TABLE CHECK position | Audit block between generation and gap analysis | ___ | ___ |
| C-14 | Phase-differentiated register [C-14: SUSPENDERS] | CONSTRAINT MANIFEST + STEP 2 + STEP 4 | Phase 1 discovery >= 3; Phase 3 operational >= 1 | ___ | ___ |
| C-15 | Temporal adoption window in severity [C-15: SUSPENDERS] | STEP 2 Phase Map | Severity tied explicitly to adoption window | ___ | ___ |
| C-16 | VM Row ID in commitment table [C-16: SUSPENDERS] | STEP 3B header | All STEP 3B rows have VM Row ID | ___ | ___ |
| C-17 | Phase-as-severity-key declaration [C-17: SUSPENDERS] | STEP 2 inference rule statement | Phase norms stated as explicit rule before ticket table | ___ | ___ |
| C-18 | Gate minimum >= 7 [C-18: SUSPENDERS] | CONSTRAINT MANIFEST + TABLE CHECK | Gate minimum sum >= 7 confirmed | ___ | ___ |
| C-19 | TABLE CHECK halt names next step [C-19: SUSPENDERS] | TABLE CHECK footer | "Do not proceed to STEP 6" explicit | ___ | ___ |
| C-20 | VM Row ID in ## headline [C-20: SUSPENDERS] | Compliance Contract + STEP 4 + TABLE CHECK | All ## headlines carry *(VM: VM-xxx-P#)* inline | ___ | ___ |
| C-21 | Five-item gate all present with item (e) [C-21: SUSPENDERS] | Compliance Contract + GATE section | Items (a)-(e) all PASS; (e) cited by VM Row ID | ___ | ___ |
| C-22 | [Aspirational] [C-22: SUSPENDERS] | ___ | ___ | ___ | ___ |
| C-23 | Belt-and-suspenders labels [C-23: SUSPENDERS] | Compliance Contract + throughout prompt | [C-NN: BELT] at generation; [C-NN: SUSPENDERS] in this spine | ___ | ___ |
| C-24 | Materialized-view traceability [C-24: SUSPENDERS] | VOCABULARY MATERIALIZATION + TABLE CHECK | Materialization table present; orphan-gap check completed | ___ | ___ |
| C-25 | Criterion-ID-named spine [C-25: SUSPENDERS] | This STEP 10 | Spine present; one row per C-01 through C-25; C-IDs in col 1 | PRESENT | PASS |

**SPINE RESULT:** [ ALL ESSENTIAL PASS ] / [ ESSENTIAL FAILURES: C-___ ]
**COMPOSITE ESTIMATE:** ___/175
