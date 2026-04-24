Writing V-01 through V-03 first, then V-04–V-05 in the next message.

---

# listen-support -- Variations, Round 11 (rubric v11 -- 35 criteria)

**Date:** 2026-03-16
**Rubric target:** v11 (C-01 through C-35 -- 35 criteria; aspirational denominator = 27)
**Baseline:** R10 V-05 (composite 100 under v10 -- passes all 25 aspirational criteria)
**R11 objective:** Probe the three new C-33/C-34/C-35 enforcement timing sites. R10 V-05 already
satisfies C-34 (COMPLIANCE CONTRACT CF via C-20 definition) and C-35 (VERIFICATION MANIFEST
header CF via C-31). C-33 (CONSTRAINT MANIFEST load CF) is absent from R10 V-05 -- the structural
target row "Tickets with VM Row ID in ## headline" carries no consequence-form declaration at the
moment of commitment. All five R11 variations add structure only -- predicted composite: 225/225.

**R11 questions:**
1. Does adding a CF preamble block before the CONSTRAINT MANIFEST table satisfy C-33 at the
   manifest load site, and does RESTATING POSITIONS need a new entry for this site? (V-01)
2. Does replacing the single VM Row ID row with three phase-specific CF rows in the CONSTRAINT
   MANIFEST satisfy C-33 via phase-indexed enforcement? Does per-phase binding create a v12
   candidate for phase-level CF granularity? (V-02)
3. Does adding C-VM as a third named obligation in the COMPLIANCE CONTRACT -- explicitly naming
   the three timing points (CONSTRAINT MANIFEST, COMPLIANCE CONTRACT, VERIFICATION MANIFEST) --
   satisfy C-34 in a structurally stronger form than the implicit C-20 CF? (V-03)
4. Does stacking V-01 preamble + V-02 phase rows in the CONSTRAINT MANIFEST create redundant-
   enforcement at the load site, closing the C-33 gap with belt-and-suspenders coverage? (V-04)
5. Does full synthesis -- V-01 preamble + V-02 phase rows + V-03 C-VM + VERIFICATION MANIFEST
   per-row CF column -- produce a prompt where every timing point carries CF both at header level
   and at individual row level? (V-05)

**Candidate new criteria for v12:**
- C-36 (candidate): Phase-indexed VM Row ID CF in CONSTRAINT MANIFEST -- each phase row carries
  its own CF declaration, binding enforcement to the phase-level count, not just the total.
- C-37 (candidate): VERIFICATION MANIFEST per-row CF column -- VM Row ID check rows carry an
  explicit "Consequence if FAIL" column, distinct from the header-level CF already present (C-35).
- C-38 (candidate, integration): RESTATING POSITIONS names CONSTRAINT MANIFEST as a
  consequence-form site. Requires C-33 PASS + new entry in RESTATING POSITIONS registry.

**Scoring under v10 (all five R11 variations):**

| Variation | v10 score | Path |
|-----------|----------|------|
| V-01 | 100.00 | R10 V-05 + CONSTRAINT MANIFEST CF preamble block |
| V-02 | 100.00 | R10 V-05 + CONSTRAINT MANIFEST phase-specific CF rows |
| V-03 | 100.00 | R10 V-05 + COMPLIANCE CONTRACT C-VM third obligation |
| V-04 | 100.00 | R10 V-05 + preamble + phase rows (C-33 belt-and-suspenders) |
| V-05 | 100.00 | Full synthesis: V-04 + V-03 + VERIFICATION MANIFEST per-row CF column |

**R11 variation axes:**

| Axis | Variation | New angle vs R10 | Candidate criterion |
|------|-----------|-----------------|---------------------|
| Output format | V-01 | CF preamble block before CONSTRAINT MANIFEST table | C-33 |
| Lifecycle emphasis | V-02 | Phase-specific CF rows in CONSTRAINT MANIFEST | C-33 + C-36 |
| Phrasing register | V-03 | C-VM third obligation in COMPLIANCE CONTRACT naming 3 timing points | C-34 (stronger) |
| Combined: output format + lifecycle | V-04 | Preamble + phase rows; both C-33 forms stacked | C-33 + C-36 + C-38 |
| Full synthesis | V-05 | V-04 + V-03 + VERIFICATION MANIFEST per-row CF column | C-33 + C-34 + C-35 + C-36 + C-37 + C-38 |

---

## Fixed Components Applied to All R11 Variations

All R11 variations inherit the full R10 V-05 mechanism set.

| Component | R10 V-05 source | R11 status |
|-----------|----------------|-----------|
| COMPLIANCE CONTRACT C-20 CF clause | R10 V-05 | Retained (all); extended in V-03+V-05 |
| COMPLIANCE CONTRACT C-21 five-item mandate | R10 V-05 | Retained (all) |
| COMPLIANCE CONTRACT compliant + failing sample | R10 V-05 | Retained (all) |
| RESTATING POSITIONS: 7-entry registry with CF | R10 V-05 | Retained (all); V-01+V-04+V-05 add CONSTRAINT MANIFEST entry |
| VOCABULARY MANIFEST header CF | R10 V-05 | Retained (all) |
| CONSTRAINT MANIFEST structural target table | R10 V-05 | Retained in V-03; upgraded in V-01+V-02+V-04+V-05 |
| STEP 5 TABLE CHECK CF | R10 V-05 | Retained (all) |
| STEP 6 body template CF | R10 V-05 | Retained (all) |
| VERIFICATION MANIFEST header CF | R10 V-05 | Retained in V-01+V-02+V-03+V-04; extended in V-05 |
| VERIFICATION MANIFEST five C-21 per-item rows | R10 V-05 | Retained (all) |

---

## V-01 -- Single Axis: Output Format (CONSTRAINT MANIFEST CF Preamble Block)

**Axis:** Output format -- the CONSTRAINT MANIFEST section gains a CF preamble block placed
before the structural target table. R10 V-05's CONSTRAINT MANIFEST opens directly with the table;
the VM Row ID row ("Tickets with VM Row ID in ## headline (Compliance Contract C-20)") carries no
CF language -- it is a count target only. V-01 adds a preamble block that explicitly states the
consequence-form for the VM Row ID structural target at the moment of commitment. RESTATING
POSITIONS gains an eighth entry for the CONSTRAINT MANIFEST site.

**Hypothesis:** Preamble CF at CONSTRAINT MANIFEST load creates the earliest enforcement timing
point in the prompt -- before any step executes. Unlike STEP 3B (which carries CF at commitment
table fill time) or STEP 5 (which carries CF at inventory check time), the CONSTRAINT MANIFEST
preamble fires the CF declaration at constraint declaration time. RESTATING POSITIONS registry
gap (C-38 candidate): V-01 adds the new entry to close that gap. Predicted composite under v11:
225/225.

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

**Failing body header (C-20 violation -- any subline placement fails C-20 regardless of other
compliance):**
```
## T-NN -- {Title}
- VM Row: VM-xxx-P#  {VIOLATION: subline placement -- fails C-20 regardless of other compliance}
- Category: ... | Persona: ...
```
Any ticket whose VM Row ID appears on any line other than the `##` headline line fails C-20.

**RESTATING POSITIONS**

The sections listed below carry obligations derived from this contract. If any section's
wording conflicts with this contract, this contract governs.

- **VOCABULARY MANIFEST**: governed by C-20 (header carries consequence-form -- an output with
  any vocabulary ID on a subline fails C-20 regardless of other compliance; the ## headline is
  the only valid placement site).
- **CONSTRAINT MANIFEST**: governed by C-20 (preamble carries consequence-form at load time --
  an output that commits VM Row IDs to ## headlines but produces any VM Row ID on a subline
  fails C-20 regardless of other compliance; commitment is binding from this point forward).
- **STEP 3B -- Per-Ticket Vocabulary Commitment Table**: governed by C-20 (VM Row ID must
  appear in ## headline; subline placement is NOT permitted -- an output with any vocabulary
  ID on a subline fails C-20 regardless of other compliance).
- **VOCABULARY PRE-FLIGHT GATE**: governed by C-21 (exactly five items (a)-(e) with individual
  PASS/FAIL states; item (e) named "inter-role register differentiation").
- **STEP 4 -- PERFORMANCE MODE DECLARATION**: governed by C-20 (VM Row ID must appear in ##
  headline inline; subline placement is NOT permitted -- an output with any vocabulary ID on
  a subline fails C-20 regardless of other compliance).
- **STEP 5 -- Ticket Inventory TABLE CHECK**: governed by C-20 (C-20 check line carries
  consequence-form -- an output with any vocabulary ID on a subline fails C-20 regardless of
  other compliance).
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
annotation -- per Compliance Contract C-20 -- subline placement is NOT permitted: an output
with any vocabulary ID on a subline fails C-20 regardless of other compliance. The ##
headline is the only valid placement site.**

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
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                  | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability                | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present            | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks             | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time    | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

**VM Row ID consequence-form is active at this manifest load site. The VM Row ID ## headline
structural target (last row below) carries criterion-level enforcement from the moment this
manifest is read: an output that commits to VM Row ID in ## headlines but produces any VM Row
ID on a subline fails C-20 regardless of all other compliance. Commit a value in the VM Row ID
row only when you intend to enforce it through STEP 6. This is the C-33 enforcement timing
point -- consequence-form at constraint load.**

| Structural target                                                                                            | Required                     | Committed value |
|--------------------------------------------------------------------------------------------------------------|------------------------------|-----------------|
| Total tickets                                                                                                | 6 to 12                      | ___             |
| Phase 1 tickets (day 0-30)                                                                                   | >= 3                         | ___             |
| Phase 2 tickets (day 31-60)                                                                                  | >= 2                         | ___             |
| Phase 3 tickets (day 61-90)                                                                                  | >= 1                         | ___             |
| P0 ceiling                                                                                                   | <= floor(total x 0.25) = ___ | ___             |
| High-volume ceiling                                                                                          | <= floor(total x 0.50) = ___ | ___             |
| Distinct named personas                                                                                      | >= 3                         | ___             |
| SRE tickets                                                                                                  | >= 2                         | ___             |
| Support tickets                                                                                              | >= 2                         | ___             |
| C-xx tickets                                                                                                 | >= 2 (max 2 per single C-xx) | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                                                              | >= 3                         | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                                                            | >= 1                         | ___             |
| Tickets with VM Row ID in commitment table (C-16)                                                            | = total ticket count         | ___             |
| Tickets with VM Row ID in ## headline -- FAIL = C-20 violation regardless of other compliance (C-20/C-33)   | = total ticket count         | ___             |

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
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline -- an output
  with any vocabulary ID on a subline fails C-20 regardless of other compliance: Y / N
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
evidence rows (five individual rows for gate items (a)-(e)). An output with any vocabulary ID
on a subline fails C-20 regardless of other compliance -- verify via the C-20 count row below.**

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

## V-02 -- Single Axis: Lifecycle Emphasis (CONSTRAINT MANIFEST Phase-Specific CF Rows)

**Axis:** Lifecycle emphasis -- the CONSTRAINT MANIFEST's single VM Row ID structural target row
is replaced by three phase-specific VM Row ID enforcement rows, one per phase window. Each row
independently carries consequence-form tied to that phase's ticket count. In R10 V-05, a single
aggregate row ("Tickets with VM Row ID in ## headline = total ticket count") commits the total
without phase-level CF binding. V-02 replaces this with Phase 1, Phase 2, and Phase 3 rows that
each carry "FAIL = C-20 violation regardless of other compliance", binding CF to the phase-level
count at the moment of commitment. No preamble block is added (that is V-01's axis).

**Hypothesis:** Phase-specific CF rows in the CONSTRAINT MANIFEST bind enforcement to the adoption
curve. A scorer can verify C-20 compliance at phase granularity rather than only at aggregate
total. The phase-indexed binding may expose a v12 candidate (C-36): CONSTRAINT MANIFEST VM Row ID
CF at per-phase resolution. The single-vs-three-row distinction also tests whether rubric C-33
requires only aggregate CF or recognizes phase-level CF as a structurally stronger form.

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

**Failing body header (C-20 violation -- any subline placement fails C-20 regardless of other
compliance):**
```
## T-NN -- {Title}
- VM Row: VM-xxx-P#  {VIOLATION: subline placement -- fails C-20 regardless of other compliance}
- Category: ... | Persona: ...
```
Any ticket whose VM Row ID appears on any line other than the `##` headline line fails C-20.

**RESTATING POSITIONS**

The sections listed below carry obligations derived from this contract. If any section's
wording conflicts with this contract, this contract governs.

- **VOCABULARY MANIFEST**: governed by C-20 (header carries consequence-form -- an output with
  any vocabulary ID on a subline fails C-20 regardless of other compliance; the ## headline is
  the only valid placement site).
- **STEP 3B -- Per-Ticket Vocabulary Commitment Table**: governed by C-20 (VM Row ID must
  appear in ## headline; subline placement is NOT permitted -- an output with any vocabulary
  ID on a subline fails C-20 regardless of other compliance).
- **VOCABULARY PRE-FLIGHT GATE**: governed by C-21 (exactly five items (a)-(e) with individual
  PASS/FAIL states; item (e) named "inter-role register differentiation").
- **STEP 4 -- PERFORMANCE MODE DECLARATION**: governed by C-20 (VM Row ID must appear in ##
  headline inline; subline placement is NOT permitted -- an output with any vocabulary ID on
  a subline fails C-20 regardless of other compliance).
- **STEP 5 -- Ticket Inventory TABLE CHECK**: governed by C-20 (C-20 check line carries
  consequence-form -- an output with any vocabulary ID on a subline fails C-20 regardless of
  other compliance).
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
annotation -- per Compliance Contract C-20 -- subline placement is NOT permitted: an output
with any vocabulary ID on a subline fails C-20 regardless of other compliance. The ##
headline is the only valid placement site.**

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
| VM-UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                  | "Session recordings show abandonment when users attempt [advanced action]..."                |
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability                | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present            | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks             | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time    | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                                                                                         | Required                     | Committed value |
|---------------------------------------------------------------------------------------------------------------------------|------------------------------|-----------------|
| Total tickets                                                                                                             | 6 to 12                      | ___             |
| Phase 1 tickets (day 0-30)                                                                                                | >= 3                         | ___             |
| Phase 2 tickets (day 31-60)                                                                                               | >= 2                         | ___             |
| Phase 3 tickets (day 61-90)                                                                                               | >= 1                         | ___             |
| P0 ceiling                                                                                                                | <= floor(total x 0.25) = ___ | ___             |
| High-volume ceiling                                                                                                       | <= floor(total x 0.50) = ___ | ___             |
| Distinct named personas                                                                                                   | >= 3                         | ___             |
| SRE tickets                                                                                                               | >= 2                         | ___             |
| Support tickets                                                                                                           | >= 2                         | ___             |
| C-xx tickets                                                                                                              | >= 2 (max 2 per single C-xx) | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                                                                           | >= 3                         | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                                                                         | >= 1                         | ___             |
| Tickets with VM Row ID in commitment table (C-16)                                                                         | = total ticket count         | ___             |
| Phase 1 VM Row IDs in ## headlines (day 0-30) -- FAIL = C-20 violation regardless of other compliance (C-20/C-33)        | = Phase 1 committed count    | ___             |
| Phase 2 VM Row IDs in ## headlines (day 31-60) -- FAIL = C-20 violation regardless of other compliance (C-20/C-33)       | = Phase 2 committed count    | ___             |
| Phase 3 VM Row IDs in ## headlines (day 61-90) -- FAIL = C-20 violation regardless of other compliance (C-20/C-33)       | = Phase 3 committed count    | ___             |

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
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline -- an output
  with any vocabulary ID on a subline fails C-20 regardless of other compliance: Y / N
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
evidence rows (five individual rows for gate items (a)-(e)). An output with any vocabulary ID
on a subline fails C-20 regardless of other compliance -- verify via the C-20 count row below.**

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

## V-03 -- Single Axis: Phrasing Register (COMPLIANCE CONTRACT C-VM Third Obligation)

**Axis:** Phrasing register -- the COMPLIANCE CONTRACT gains a third named obligation, C-VM,
that explicitly names the three enforcement timing points (CONSTRAINT MANIFEST load, COMPLIANCE
CONTRACT, VERIFICATION MANIFEST) and declares that VM Row ID consequence-form must appear at
each timing point. In R10 V-05, the three timing points are structurally present but never
named as a set within the contract itself -- the contract governs C-20 placement and C-21 gate
items but does not declare the three-timing-point coverage requirement as a standalone obligation.
V-03 makes the timing-point coverage explicit: C-VM states the rule that governs C-33/C-34/C-35.
No changes to CONSTRAINT MANIFEST or VERIFICATION MANIFEST rows (those are V-01 and V-02 axes).

**Hypothesis:** Naming C-VM as a third contract obligation makes three-timing-point CF coverage
a governable criterion at the contract site, not a derived consequence of C-20. A scorer reading
only the COMPLIANCE CONTRACT sees the explicit three-timing-point requirement without consulting
RESTATING POSITIONS. This may produce a v12 candidate: contract-level timing-point declaration
as a distinct structural pattern from RESTATING POSITIONS registry coverage (C-38 variant where
the contract itself is the registry rather than RESTATING POSITIONS).

---

```
You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### COMPLIANCE CONTRACT

**Read before any step. These three obligations govern the entire output.**

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

**C-VM -- Three-timing-point consequence-form coverage:**
VM Row ID consequence-form must appear at exactly three enforcement timing points in this output:
(1) CONSTRAINT MANIFEST load site -- the VM Row ID structural target carries CF at the moment
    of commitment, before any step executes.
(2) COMPLIANCE CONTRACT site -- this contract's C-20 definition carries CF (satisfied by C-20
    above: "fails C-20 regardless of other compliance").
(3) VERIFICATION MANIFEST spine site -- the manifest header carries CF (per C-31: "an output
    with any vocabulary ID on a subline fails C-20 regardless of other compliance").
Any timing point without CF is a structural gap at that enforcement site. An output is not
fully protected unless all three timing points independently carry the criterion-level failure
declaration.

**Compliant body header sample:**
```
## T-NN -- {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"
```

**Failing body header (C-20 violation -- any subline placement fails C-20 regardless of other
compliance):**
```
## T-NN -- {Title}
- VM Row: VM-xxx-P#  {VIOLATION: subline placement -- fails C-20 regardless of other compliance}
- Category: ... | Persona: ...
```
Any ticket whose VM Row ID appears on any line other than the `##` headline line fails C-20.

**RESTATING POSITIONS**

The sections listed below carry obligations derived from this contract. If any section's
wording conflicts with this contract, this contract governs.

- **VOCABULARY MANIFEST**: governed by C-20 (header carries consequence-form -- an output with
  any vocabulary ID on a subline fails C-20 regardless of other compliance; the ## headline is
  the only valid placement site).
- **STEP 3B -- Per-Ticket Vocabulary Commitment Table**: governed by C-20 (VM Row ID must
  appear in ## headline; subline placement is NOT permitted -- an output with any vocabulary
  ID on a subline fails C-20 regardless of other compliance).
- **VOCABULARY PRE-FLIGHT GATE**: governed by C-21 (exactly five items (a)-(e) with individual
  PASS/FAIL states; item (e) named "inter-role register differentiation").
- **STEP 4 -- PERFORMANCE MODE DECLARATION**: governed by C-20 (VM Row ID must appear in ##
  headline inline; subline placement is NOT permitted -- an output with any vocabulary ID on
  a subline fails C-20 regardless of other compliance).
- **STEP 5 -- Ticket Inventory TABLE CHECK**: governed by C-20 (C-20 check line carries
  consequence-form -- an output with any vocabulary ID on a subline fails C-20 regardless of
  other compliance).
- **STEP 6 -- Ticket Bodies**: governed by C-20 (VM Row ID must appear in ## headline; subline
  placement is NOT permitted -- an output with any vocabulary ID on a subline fails C-20
  regardless of other compliance).
- **VERIFICATION MANIFEST**: governed by C-20 count row (## headlines with inline ID = total)
  and C-21 per-item evidence rows (five individual rows for gate items (a)-(e) with individual
  Required/Actual/Pass? cells) and C-VM timing-point (3) (VERIFICATION MANIFEST spine carries
  CF per C-31).

Precedence: If any restating position conflicts with this contract, this contract governs.

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused
combinations. VM Row IDs appear in this manifest, the commitment table, and the ## headline
annotation -- per Compliance Contract C-20 -- subline placement is NOT permitted: an output
with any vocabulary ID on a subline fails C-20 regardless of other compliance. The ##
headline is the only valid placement site.**

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
| VM-UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability               | "Long-term users are filing feedback about [behavior change / reliability issue]..."         |
| VM-Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present           | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| VM-Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks            | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| VM-Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time   | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

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
- Compliance Contract C-20: every ## headline will carry *(VM: VM-xxx-P#)* inline -- an output
  with any vocabulary ID on a subline fails C-20 regardless of other compliance: Y / N
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

**Per Compliance Contract above (C-VM timing-point 3) -- this manifest carries C-20 count row
and C-21 per-item evidence rows (five individual rows for gate items (a)-(e)). An output with
any vocabulary ID on a subline fails C-20 regardless of other compliance -- verify via the C-20
count row below.**

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

V-01 through V-03 complete. Continuing with V-04 and V-05 next.
