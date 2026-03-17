# listen-support — Variations, Round 5 (rubric v5 — 19 criteria)

**Date:** 2026-03-15
**Rubric target:** v5 (C-01 through C-19 — 19 criteria; aspirational tier denominator = 11)
**Baseline:** R4 V-05 (composite 100 under v4; scores 98.18 under v5 — C-18/C-19 not closed)
**R5 objective:** Close the two new aspirational gaps that R4 V-05-class outputs cannot
satisfy under v5:
  - **C-18** — Vocabulary Planning Artifact Linkage: a shared ID scheme must link all three
    levels — vocabulary matrix cell, commitment table row, AND body header annotation — so any
    body is traceable to its matrix cell in two ID lookups without reading body text.
  - **C-19** — Multi-Criteria Vocabulary Pre-Flight Gate: a standalone block before body
    generation that explicitly validates >= 3 of 5 vocabulary constraints by naming the
    artifacts it checks; body generation must follow the block in output order.

**The R4 gap analysis:**
- R4 V-01: Cell IDs in matrix and commitment table — C-18 PARTIAL (body headers do not
  cite Cell ID; tracing requires reading body text for the opening phrase). C-19 FAIL
  (pre-flight checks embedded inside STEP 2B, not a standalone vocabulary gate).
- R4 V-02/V-04/V-05: VM Row IDs link manifest to commitment table — C-18 PARTIAL (VM Row ID
  appears in body metadata line but the rubric requires >= 75% of headers to cite the ID as
  a headline annotation; scorers must still read the metadata line). C-19 FAIL (pre-flight
  checks in STEP 3B are constraints on the commitment table, not a standalone section naming
  vocabulary artifacts and blocking body generation by section order).
- R4 V-03: Distributed per-role tables without shared IDs — C-18 FAIL (tracing requires
  reading 5 blocks and matching phrase text).

**R5 strategy:** All five variations inherit the full R4 V-05 mechanism set. Single-axis
variations isolate three distinct approaches to adding C-18 and C-19; combined variations
stack them. The composite 100 candidate (V-05) adds VM Row IDs as headline body header
annotations AND inserts a standalone 5-item blocking vocabulary gate between the commitment
table and PERFORMANCE MODE.

---

## Fixed Changes Applied to All Variations

All five R5 variations inherit the full R4 V-05 foundation. These components are not the
differentiating axis.

| Component | R4 V-05 source | R5 status |
|-----------|---------------|-----------|
| VOCABULARY MANIFEST with VM Row IDs (C-17) | R4 V-05 | Retained |
| CONSTRAINT MANIFEST + VERIFICATION MANIFEST (C-15) | R4 V-05 | Retained |
| Per-ticket commitment table referencing VM Row IDs (C-16) | R4 V-05 | Extended (C-18 adds body header citation) |
| Character-embodiment PERFORMANCE MODE with migration backstory (C-03) | R4 V-05 | Retained |
| Phase Map Table with severity/volume/register norms (C-14) | R4 all | Retained |
| Theme declaration before inventory (C-09) | R4 all | Retained |
| Role-Phase Cross-Matrix (C-12) | R4 all | Retained |
| Ticket inventory table + TABLE CHECK (C-01/C-02/C-05/C-11) | R4 all | Retained |
| Ticket bodies by theme, phase-sorted, ascending T-ID | R4 all | Extended (C-18 adds ID annotation in header) |
| Cross-ticket patterns (C-09) | R4 all | Retained |
| Resolution paths table (C-10) | R4 all | Retained |
| Gap analysis with T-NN refs (C-04/C-08) | R4 all | Retained |
| Verification manifest post-generation (C-15) | R4 V-05 | Retained |

---

## R5 Variation Axes

R1 explored: role sequence, output format, lifecycle emphasis.
R2 explored: phrasing register, inertia framing, theme-first generation.
R3 explored: lifecycle emphasis (vocabulary commitment from phase pools), output format
(manifest tables), role sequence (role-phase vocabulary matrix).
R4 explored: three approaches to fusing C-16 (per-ticket commitment table) with C-17
(role-phase vocabulary matrix), which R3 developed independently.
R5 targets the orthogonal gap: adding C-18 (3-node ID chain) and C-19 (standalone vocabulary
gate) to the R4 V-05 base.

| Axis | Single-axis variation | New angle vs prior rounds | Target criteria |
|------|-----------------------|--------------------------|-----------------|
| Output format | V-01 | Compact Cell IDs (`Role-P#` format) in matrix, commitment table, AND body headline annotation `*(Cell: XX-P#)*` | C-18 |
| Lifecycle emphasis | V-02 | Standalone VOCABULARY PRE-FLIGHT GATE section (5 items, named artifacts, blocking declaration) placed between commitment table and PERFORMANCE MODE | C-19 |
| Phrasing register | V-03 | Named semantic register IDs (`REG-ROLE-TYPE`) encode meaning in the ID itself; inter-role differentiation enforced by register name; 3-item minimum gate | C-18 + C-19 (lighter) |

Combined: V-04 stacks V-01 (compact Cell IDs) + V-02 (5-item blocking gate). V-05 stacks
all R4 V-05 mechanisms + VM Row ID body header annotation (C-18 complete 3-node chain) +
5-item standalone blocking gate (C-19) + body instruction encoding the traceability rule.

---

## V-01 — Single Axis: Output Format (Compact Cell ID 3-Node Chain for C-18)

**Axis:** Output format — the vocabulary matrix uses compact Cell IDs in the format
`{Role-abbrev}-P{phase-number}` (e.g., `SRE-P1`, `Sup-P3`, `Cxx-P2`). These IDs appear in
ALL THREE levels: (1) as row identifiers in the vocabulary matrix header, (2) as the "Cell ID"
column in the commitment table, and (3) as a headline annotation in every ticket body header
`*(Cell: XX-P#)*`. A scorer can trace any body to its matrix row in two ID lookups without
reading body text. The C-19 gate checks 4 items as a standalone block placed between the
commitment table and PERFORMANCE MODE.

**Hypothesis:** R4 V-01 established Cell IDs in the matrix and commitment table — two of the
three required nodes. Body headers in R4 V-01 do not cite the Cell ID, forcing a scorer to
read body text to confirm the match. Adding `*(Cell: XX-P#)*` as a headline annotation
completes the 3-node chain: scorer reads the header annotation, looks up the commitment table
row by Cell ID, reads the matrix cell by Cell ID — two lookups, zero body text. The 4-item
standalone gate satisfies C-19 at minimum passing threshold. This is the lightest-weight path
to C-18 + C-19 PASS from the R4 V-01 base.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### VOCABULARY MATRIX

**Complete before generating any ticket. Customize for {topic} — replace bracketed
placeholders with feature-specific language. Mark N/A for unused combinations.
Cell IDs are the shared identifier across ALL three levels: matrix row, commitment table
column, and body header annotation. Every ticket body is traceable to its matrix cell by
Cell ID in two lookups.**

Cell ID format: `{Role-abbrev}-P{phase}` — e.g., `SRE-P1`, `Sup-P2`, `UX-P3`, `Cxx-P1`.

| Cell ID  | Role    | Phase   | Register description                                                    | Example template phrase                                                                      |
|----------|---------|---------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure           | "I'm seeing [failure] only when [condition] — I cannot reproduce it on demand..."           |
| SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                    | "We've been running {topic} in production for [N] weeks and we just noticed [regression]..." |
| Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly      | "I keep seeing customers hit [obstacle] when they first [action] — no guidance exists..."   |
| Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause       | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."               |
| Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold   | "This is the [N]th escalation about [failure] this month — I need a permanent fix..."       |
| PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast           | "First-time activation for {topic} is lower than projected — I want to understand..."       |
| PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                       | "The [metric] I projected is not improving — I need to investigate whether [hypothesis]..." |
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

| Structural target                                             | Required                        | Committed value |
|---------------------------------------------------------------|---------------------------------|-----------------|
| Total tickets                                                 | 6 to 12                         | ___             |
| Phase 1 tickets (day 0-30)                                    | >= 3                            | ___             |
| Phase 2 tickets (day 31-60)                                   | >= 2                            | ___             |
| Phase 3 tickets (day 61-90)                                   | >= 1                            | ___             |
| P0 ceiling                                                    | <= floor(total × 0.25) = ___    | ___             |
| High-volume ceiling                                           | <= floor(total × 0.50) = ___    | ___             |
| Distinct named personas                                       | >= 3                            | ___             |
| SRE tickets                                                   | >= 2                            | ___             |
| Support tickets                                               | >= 2                            | ___             |
| C-xx tickets                                                  | >= 2 (max 2 per single C-xx)    | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)               | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary (C-14)             | >= 1                            | ___             |
| Tickets with Cell ID in commitment table AND body header (C-18) | = total ticket count          | ___             |

Do not proceed until the Constraint Manifest is complete.

---

### STEP 1 — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 — Phase Map Table

| Phase   | Window    | Severity norm | Volume norm    | Body register                          |
|---------|-----------|---------------|----------------|----------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium    | Discovery/setup — use xxx-P1 cells     |
| Phase 2 | day 31-60 | P1/P2         | medium         | Integration/edge — use xxx-P2 cells    |
| Phase 3 | day 61-90 | P0/P1         | low/medium     | Operational/reliability — use xxx-P3 cells |

Phase-severity inference rule: assign from the norm column. Override only if the specific
failure is unambiguously more or less severe than the phase norm.

---

### STEP 3 — Theme Declaration

```
Theme A: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

Theme B: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

[Theme C if needed — same format]
```

Each theme must have a distinct underlying failure. Sum of counts = Constraint Manifest total.

---

### STEP 3A — Role-Phase Cross-Matrix

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

### STEP 3B — Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. For each ticket: record the Cell ID from the
Vocabulary Matrix, derive the committed opening phrase from that cell's template, and record
it here. The body MUST begin with its committed phrase (expanded — not verbatim). The body
header MUST include `*(Cell: XX-P#)*` as a headline annotation citing the Cell ID. This
creates the three-node traceability chain: Vocabulary Matrix cell header → commitment table
Cell ID column → body header annotation, all keyed by the same Cell ID.**

| T-ID | Cell ID  | Phase     | Committed opening phrase |
|------|----------|-----------|--------------------------|
| T-01 | ___-P___ | Phase ___ | "___" |
| T-02 | ___-P___ | Phase ___ | "___" |
| T-03 | ___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT CHECK

**Execute before writing any ticket body. Check all four items against named artifacts.
State PASS or FAIL for each. Body generation is blocked if any check fails — revise the
Vocabulary Matrix or commitment table before continuing.**

**Check 1 — Vocabulary Matrix completeness**
For every (Role, Phase) combination in the ticket inventory, a Cell ID row exists in the
Vocabulary Matrix (not marked N/A).
State: [ PASS — all ___ inventory combinations have matrix cells ] / [ FAIL — missing: ___ ]

**Check 2 — Commitment table completeness**
Row count in STEP 3B equals committed ticket total in the Constraint Manifest.
State: [ PASS — ___ rows = ___ tickets ] / [ FAIL — ___ rows ≠ ___ tickets ]

**Check 3 — Phrase-to-cell traceability**
Each committed phrase in STEP 3B is derivable from the Example template phrase of its Cell ID
in the Vocabulary Matrix (same role, same phase, same register).
State: [ PASS — all ___ phrases traceable ] / [ FAIL — untraceable: T-___ ]

**Check 4 — Phase-register alignment**
All Phase 1 committed phrases use P1-cell registers (discovery/setup). At least one Phase 3
phrase uses a P3-cell register (operational/reliability).
State: [ PASS ] / [ FAIL — misaligned T-IDs: ___ ]

**PRE-FLIGHT RESULT:** [ ALL PASS — proceed to PERFORMANCE MODE ] / [ BLOCKED — N checks failed ]

---

### STEP 4 — PERFORMANCE MODE DECLARATION (character-embodiment + migration context)

**You are about to become each persona. They know what they migrated from.**

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior
system's failure modes cold; this one is still opaque to you. Something is now breaking
silently that you would have caught immediately in the old system. You are methodical but
frustrated.

**Support:** You've answered this same migration question multiple times this week. You know
what the old approach expected; {topic} does something different that users keep tripping over.
You are filing this ticket to get engineering to fix the root cause so you can stop answering it.

**PM:** Adoption is below forecast. You cannot tell if it is a product problem or a
communication problem. You are filing this to request data.

**UX:** You are watching session recordings and seeing users stall at a specific point. The
old approach had a familiar affordance here; the new one does not. You know the friction point
by location; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach in Step 1] recently. Something surprised you —
either something that used to work stopped working, or something you expected to just work
required extra setup. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Begin each body with the committed phrase from STEP 3B (expanded into a full opening sentence).
Body header MUST include `*(Cell: XX-P#)*` as a headline annotation citing the Cell ID.
Register must match the Vocabulary Matrix cell. Registers must differ between roles in the
same phase. Where migration-relevant: reference what was expected from the old approach.**

---

### STEP 5 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK — verify all before proceeding:
- Total rows: ___ (required: matches Constraint Manifest)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= Manifest ceiling)
- High-volume count: ___ (required: <= Manifest ceiling)
- Theme counts match Step 3 declarations: MATCH / MISMATCH
- Phase distribution matches Constraint Manifest: MATCH / MISMATCH
- All Phase 1 tickets have committed discovery phrase in STEP 3B: Y / N
- At least 1 Phase 3 ticket has committed operational phrase in STEP 3B: Y / N
- Every STEP 3B row has a valid Cell ID from the Vocabulary Matrix: Y / N
- Every ticket body will have `*(Cell: XX-P#)*` headline annotation: Y / N

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

**Generation order within each theme: Phase 1 tickets first, then Phase 2, then Phase 3.**

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title} *(Cell: XX-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences.
OPENING: Begin with the committed phrase from STEP 3B — expand it into a full first sentence.
  Do not copy verbatim.
REGISTER: Use the vocabulary register from the Cell ID. SRE bodies use technical/operational
  vocabulary. C-xx bodies reflect confusion or migration surprise. Support bodies reflect
  recurring-question frustration. Registers must differ between roles in the same phase.
VOICE: First person throughout — "I", "my", "we". No third-person role references.
MIGRATION: Where relevant, reference what was expected from the old approach (Step 1).]
```

---

### STEP 7 — Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|
| ... | T-NN, T-NN | ... | Y/N | ... |

---

### STEP 7B — Resolution Paths

For every ticket that is high-volume OR P0/P1:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|
| T-NN | SRE / Support / PM / Eng | doc-gap / design-flaw / config-error / product-bug | self-serve / escalation / structural |

---

### STEP 8 — Gap Analysis

All entries require `Tickets: T-NN, T-NN` with identifiers matching the inventory above.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | design change required

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | process change required

Minimum 2 entries per gap category. Each entry cites at least one T-ID.

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
| Bodies with `*(Cell: XX-P#)*` headline annotation (C-18) | = total | ___ | ___ |
| Cell IDs in headers resolve to commitment table rows | = total | ___ | ___ |
| Cell IDs in commitment table resolve to matrix cells | = total | ___ | ___ |
| No body uses third-person role reference | = total | ___ | ___ |
| Phase 1 bodies use discovery register | >= 3 | ___ | ___ |
| Phase 3 bodies use operational register | >= 1 | ___ | ___ |

If any row fails: identify the ticket, correct, and re-verify.

---

---

## V-02 — Single Axis: Lifecycle Emphasis (Standalone 5-Item Blocking Vocabulary Gate for C-19)

**Axis:** Lifecycle emphasis — a standalone section named `VOCABULARY PRE-FLIGHT GATE` is
placed between the commitment table (STEP 3B) and PERFORMANCE MODE (STEP 4). It checks all
five C-19 items, names each artifact by its section name ("VOCABULARY MANIFEST", "commitment
table", "STEP 3B"), and declares `GATE: OPEN` or `GATE: CLOSED`. Body generation is
explicitly blocked if the gate is CLOSED. VM Row IDs from R4 V-05 are retained for the
manifest and commitment table. Body headers show `VM Row: VM-xxx-P#` in the metadata line
(C-18 partially satisfied — two nodes of the chain are present; C-18 PARTIAL expected).

**Hypothesis:** R4 V-05's pre-flight checks are embedded inside STEP 3B — they read as
constraints on the commitment table step, not as a standalone vocabulary gate. C-19 requires
a block that: (a) is standalone (not embedded in another step), (b) names the vocabulary
artifacts being validated by section name, (c) checks >= 3 of the 5 items explicitly,
and (d) appears before body generation in output order. This variation isolates that
property. The gate is the differentiating element; the rest of the prompt inherits R4 V-05
verbatim. Expected result: C-19 PASS, C-18 PARTIAL (VM Row ID in metadata line satisfies
two of three chain nodes — commitment table cites VM Row ID, body metadata cites VM Row ID,
but body headline does not). Composite ~99.1 under v5. V-04/V-05 complete C-18 by adding the
headline annotation.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic} — replace bracketed
placeholders with feature-specific language. Mark N/A for unused combinations. This is the
vocabulary contract: every ticket body must be traceable to its assigned VOCABULARY MANIFEST
row via VM Row ID.**

| VM Row ID   | Role    | Phase   | Register description                                                   | Example template phrase                                                                      |
|-------------|---------|---------|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure          | "I'm seeing [failure] only when [condition] — I cannot reproduce it on demand..."           |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                   | "We've been running {topic} in production for [N] weeks and we just noticed [regression]..." |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly     | "I keep seeing customers hit [obstacle] when they first [action] — no guidance exists..."   |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause      | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."               |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold  | "This is the [N]th escalation about [failure] this month — I need a permanent fix..."       |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast          | "First-time activation for {topic} is lower than projected — I want to understand..."       |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                      | "The [metric] I projected is not improving — I need to investigate whether [hypothesis]..." |
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
| P0 ceiling                                                | <= floor(total × 0.25) = ___    | ___             |
| High-volume ceiling                                       | <= floor(total × 0.50) = ___    | ___             |
| Distinct named personas                                   | >= 3                            | ___             |
| SRE tickets                                               | >= 2                            | ___             |
| Support tickets                                           | >= 2                            | ___             |
| C-xx tickets                                              | >= 2 (max 2 per single C-xx)    | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)           | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary (C-14)         | >= 1                            | ___             |
| Tickets with VM Row ID in commitment table (C-16)         | = total ticket count            | ___             |

Do not proceed until the Constraint Manifest is complete.

---

### STEP 1 — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 — Phase Map Table

| Phase   | Window    | Severity norm | Volume norm    | Body register                             |
|---------|-----------|---------------|----------------|-------------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium    | Discovery/setup — use VM-xxx-P1 register  |
| Phase 2 | day 31-60 | P1/P2         | medium         | Integration/edge — use VM-xxx-P2 register |
| Phase 3 | day 61-90 | P0/P1         | low/medium     | Operational/reliability — use VM-xxx-P3 register |

---

### STEP 3 — Theme Declaration

```
Theme A: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

Theme B: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

[Theme C if needed — same format]
```

---

### STEP 3A — Role-Phase Cross-Matrix

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

### STEP 3B — Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. Reference the VOCABULARY MANIFEST Row ID, derive
the committed opening phrase from that row's template, and record it here. The body MUST
begin with its committed phrase (expanded). The body metadata line MUST cite the VM Row ID.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate. Execute immediately after completing STEP 3B and before STEP 4. Each item
names the artifact it validates. Declare GATE: OPEN or GATE: CLOSED. Body generation
(STEP 6) is blocked if the gate is CLOSED — revise the VOCABULARY MANIFEST or STEP 3B
and re-run this gate before continuing.**

**Item 1 — VOCABULARY MANIFEST completeness**
Confirm: every (Role, Phase) combination that appears in the ticket inventory has a
corresponding row in the VOCABULARY MANIFEST (not marked N/A).
Result: [ PASS — all ___ inventory combinations have VOCABULARY MANIFEST rows ]
      / [ FAIL — missing: ___ ]

**Item 2 — Commitment table completeness**
Confirm: row count in STEP 3B equals committed ticket total in the CONSTRAINT MANIFEST.
Result: [ PASS — STEP 3B has ___ rows = CONSTRAINT MANIFEST total of ___ ]
      / [ FAIL — STEP 3B has ___ rows ≠ CONSTRAINT MANIFEST total of ___ ]

**Item 3 — Phrase-to-manifest traceability**
Confirm: each committed phrase in STEP 3B derives from the Example template phrase of its
VM Row ID in the VOCABULARY MANIFEST (same role, same phase, same register).
Result: [ PASS — all ___ phrases traceable to VOCABULARY MANIFEST rows ]
      / [ FAIL — untraceable phrases: T-___ (VM Row ID: ___) ]

**Item 4 — Phase-register alignment**
Confirm: all Phase 1 committed phrases in STEP 3B use the discovery/setup register from
VM-xxx-P1 rows. At least one Phase 3 phrase uses the operational/reliability register from
a VM-xxx-P3 row.
Result: [ PASS ] / [ FAIL — misaligned: ___ ]

**Item 5 — Inter-role register differentiation**
Confirm: in at least one phase, two or more roles have distinct register descriptions in
the VOCABULARY MANIFEST.
Cite example: Phase ___ | VM Row ___ (___ role) = "___ register" vs VM Row ___ (___ role) = "___ register"
Result: [ PASS — example cited ] / [ FAIL ]

**GATE: [ OPEN — all 5 items PASS — proceed to STEP 4 ]**
**GATE: [ CLOSED — ___ items failed — revise VOCABULARY MANIFEST and/or STEP 3B, then re-run ]**

---

### STEP 4 — PERFORMANCE MODE DECLARATION (character-embodiment + migration context)

**You are about to become each persona. They know what they migrated from.**

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior
system's failure modes cold; this one is still opaque to you. Something is now breaking
silently that you would have caught immediately in the old system. You are methodical but
frustrated.

**Support:** You've answered this same migration question multiple times this week. You know
what the old approach expected; {topic} does something different that users keep tripping over.
You are filing this ticket to get engineering to fix the root cause so you can stop answering it.

**PM:** Adoption is below forecast. You cannot tell if it is a product problem or a
communication problem. You are filing this to request data.

**UX:** You are watching session recordings and seeing users stall at a specific point. The
old approach had a familiar affordance here; the new one does not. You know the friction point
by location; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach in Step 1] recently. Something surprised you —
either something that used to work stopped working, or something you expected to just work
required extra setup. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Begin each body with the committed phrase from STEP 3B (expanded into a full opening sentence).
The metadata line below each body header MUST include `VM Row: {VM Row ID}` from STEP 3B.
Register must match the VOCABULARY MANIFEST row. Where migration-relevant: reference what was
expected from the old approach.**

---

### STEP 5 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK — verify all before proceeding:
- Total rows: ___ (required: matches Constraint Manifest)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count, high-volume count within ceilings: Y / N
- Every STEP 3B row has a valid non-N/A VM Row ID: Y / N
- Every ticket body metadata line will include VM Row ID citation: Y / N

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted, ascending T-ID)

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- VM Row: {VM Row ID from STEP 3B} | Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences. Begin with committed phrase expanded. First person. Register matches VM Row.
Migration reference where relevant.]
```

---

### STEP 7 — Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|

---

### STEP 7B — Resolution Paths

For every high-volume OR P0/P1 ticket:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|

---

### STEP 8 — Gap Analysis

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | design change required

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | process change required

Minimum 2 entries per gap category.

---

### VERIFICATION MANIFEST

| Verification target | Required | Actual | Pass? |
|--------------------|----------|--------|-------|
| Total tickets generated | = Constraint Manifest | ___ | ___ |
| Distinct categories | >= 2 | ___ | ___ |
| Distinct personas | >= 3 | ___ | ___ |
| Bodies starting with committed phrase | = total | ___ | ___ |
| Bodies with VM Row ID in metadata line | = total | ___ | ___ |
| No body uses third-person role reference | = total | ___ | ___ |
| Phase 1 discovery register | >= 3 | ___ | ___ |
| Phase 3 operational register | >= 1 | ___ | ___ |

---

---

## V-03 — Single Axis: Phrasing Register (Semantic REG-ID Scheme for C-18 + Lightweight C-19)

**Axis:** Phrasing register — instead of positional Cell IDs (`SRE-P1`) or manifest row IDs
(`VM-SRE-P1`), the vocabulary matrix uses named semantic register IDs in the format
`REG-{ROLE}-{TYPE}` where TYPE encodes the register meaning (e.g., `REG-SRE-SETUP`,
`REG-CUST-CONFUSE`, `REG-SUP-ESCALATE`). REG-IDs appear in ALL three levels: vocabulary
matrix rows, commitment table, and body headline annotations `*(Reg: REG-xxx-TYPE)*`. The
C-19 gate checks 3 items (minimum passing threshold).

**Hypothesis:** Positional IDs (`SRE-P1`) require a scorer to look up the matrix to
understand what register is implied. Named register IDs (`REG-SRE-SETUP`) communicate the
register without lookup — register drift in a body is immediately visible by reading the
headline ID without opening the matrix. This variation tests whether semantic naming produces
more register-consistent body generation than positional IDs, at the cost of slightly longer
header annotations. The 3-item gate satisfies C-19 at minimum compliance; the REG-ID scheme
satisfies C-18's 3-node chain. Combined variations (V-04, V-05) upgrade to 5-item gates.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### REGISTER VOCABULARY MATRIX

**Complete before generating any ticket. Assign a REG-ID to each role-phase combination.
Format: `REG-{ROLE}-{TYPE}` where ROLE is a short role abbreviation and TYPE is a semantic
label for the register (SETUP, CONFUSE, ESCALATE, METRIC, SESSION, SUSTAIN, etc.). REG-IDs
appear in this matrix, the commitment table, AND the body headline annotation. A scorer can
trace any body to its matrix row in two REG-ID lookups without reading body text.**

| REG-ID              | Role    | Phase   | Register type | Register description                                                    | Example template phrase                                                                      |
|---------------------|---------|---------|---------------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| REG-SRE-SETUP       | SRE     | Phase 1 | SETUP         | Technical confusion after deployment: monitoring/alerting gap           | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| REG-SRE-EDGE        | SRE     | Phase 2 | EDGE          | Intermittent condition-specific operational failure                     | "I'm seeing [failure] only when [condition] — I cannot reproduce it on demand..."           |
| REG-SRE-REGRESS     | SRE     | Phase 3 | REGRESS       | Silent reliability regression surfacing after sustained production run  | "We've been running {topic} for [N] weeks and we just noticed [regression]..."              |
| REG-SUP-REPEAT      | Support | Phase 1 | REPEAT        | Same migration obstacle filing repeatedly; no existing guidance         | "I keep seeing customers hit [obstacle] when they first [action]..."                         |
| REG-SUP-PATTERN     | Support | Phase 2 | PATTERN       | Recurring questions pointing to a systemic root cause                   | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."               |
| REG-SUP-ESCALATE    | Support | Phase 3 | ESCALATE      | Chronic failure reaching leadership escalation threshold                | "This is the [N]th escalation about [failure] this month..."                                 |
| REG-PM-METRIC       | PM      | Phase 1 | METRIC        | First-time activation below forecast; cause unknown                     | "First-time activation is lower than projected — I want to understand what is blocking..."   |
| REG-PM-FUNNEL       | PM      | Phase 2 | FUNNEL        | Mid-adoption metric stalled; product vs comms hypothesis                | "The [metric] is not improving at the expected rate — I need to investigate..."              |
| REG-PM-ATTRITION    | PM      | Phase 3 | ATTRITION     | Post-onboarding drop-off surfacing in late cohort                       | "I'm seeing users who completed onboarding dropping off at [stage]..."                       |
| REG-UX-SESSION      | UX      | Phase 1 | SESSION       | Users stalling at identifiable UI location in session recordings        | "I'm watching session recordings and users consistently stall at [location]..."             |
| REG-UX-ABANDON      | UX      | Phase 2 | ABANDON       | Drop-off on advanced feature interaction                                | "Session recordings show abandonment when users attempt [advanced action]..."               |
| REG-UX-LONGTERM     | UX      | Phase 3 | LONGTERM      | Long-term user feedback about changed behavior or reliability           | "Long-term users are filing feedback about [behavior change / reliability issue]..."        |
| REG-CUST-CONFUSE    | C-xx    | Phase 1 | CONFUSE       | Migration surprise: old-approach expectation not met                    | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| REG-CUST-ADVANCED   | C-xx    | Phase 2 | ADVANCED      | Advanced scenario failure after basics are working                      | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| REG-CUST-SUSTAIN    | C-xx    | Phase 3 | SUSTAIN       | Reliability or data concern surfacing after sustained use               | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

| Structural target                                              | Required                        | Committed value |
|----------------------------------------------------------------|---------------------------------|-----------------|
| Total tickets                                                  | 6 to 12                         | ___             |
| Phase 1 tickets (day 0-30)                                     | >= 3                            | ___             |
| Phase 2 tickets (day 31-60)                                    | >= 2                            | ___             |
| Phase 3 tickets (day 61-90)                                    | >= 1                            | ___             |
| P0 ceiling                                                     | <= floor(total × 0.25) = ___    | ___             |
| High-volume ceiling                                            | <= floor(total × 0.50) = ___    | ___             |
| Distinct named personas                                        | >= 3                            | ___             |
| SRE tickets                                                    | >= 2                            | ___             |
| Support tickets                                                | >= 2                            | ___             |
| C-xx tickets                                                   | >= 2 (max 2 per single C-xx)    | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary (C-14)              | >= 1                            | ___             |
| Tickets with REG-ID in commitment table AND body header (C-18) | = total ticket count            | ___             |

---

### STEP 1 — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 — Phase Map Table

| Phase   | Window    | Severity norm | Volume norm    | Register type range                              |
|---------|-----------|---------------|----------------|--------------------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium    | SETUP / REPEAT / METRIC / SESSION / CONFUSE       |
| Phase 2 | day 31-60 | P1/P2         | medium         | EDGE / PATTERN / FUNNEL / ABANDON / ADVANCED      |
| Phase 3 | day 61-90 | P0/P1         | low/medium     | REGRESS / ESCALATE / ATTRITION / LONGTERM / SUSTAIN |

---

### STEP 3 — Theme Declaration

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

### STEP 3A — Role-Phase Cross-Matrix

| Role    | Phase 1 | Phase 2 | Phase 3 | Total | Theme(s) |
|---------|---------|---------|---------|-------|----------|
| SRE     | ___     | ___     | ___     | ___   | ___      |
| Support | ___     | ___     | ___     | ___   | ___      |
| PM      | ___     | ___     | ___     | ___   | ___      |
| UX      | ___     | ___     | ___     | ___   | ___      |
| C-xx    | ___     | ___     | ___     | ___   | ___      |

---

### STEP 3B — Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. Record the REG-ID from the Register Vocabulary
Matrix. Derive the committed phrase from that REG-ID's template. The body MUST begin with its
committed phrase (expanded). The body header MUST include `*(Reg: REG-xxx-TYPE)*` as a
headline annotation citing the REG-ID — completing the 3-node chain: Register Vocabulary
Matrix REG-ID row → commitment table REG-ID column → body header annotation.**

| T-ID | REG-ID          | Phase     | Committed opening phrase |
|------|-----------------|-----------|--------------------------|
| T-01 | REG-___-___     | Phase ___ | "___" |
| T-02 | REG-___-___     | Phase ___ | "___" |
| T-03 | REG-___-___     | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT CHECK

**Execute before writing any ticket body. Check all three items.**

**Check 1 — Register Vocabulary Matrix completeness**
Confirm: every (Role, Phase) combination in the ticket inventory has a REG-ID row in the
Register Vocabulary Matrix.
State: [ PASS ] / [ FAIL — missing: ___ ]

**Check 2 — Commitment table completeness**
Confirm: STEP 3B row count = committed ticket total in Constraint Manifest.
State: [ PASS — ___ rows = ___ tickets ] / [ FAIL ]

**Check 3 — Inter-role register differentiation**
Confirm: in at least one phase, two roles have REG-IDs with distinct TYPE labels.
Cite example: Phase ___, REG-___-___ (TYPE: ___) vs REG-___-___ (TYPE: ___)
State: [ PASS — example cited ] / [ FAIL ]

**PRE-FLIGHT RESULT:** [ ALL PASS — proceed ] / [ BLOCKED — revise before continuing ]

---

### STEP 4 — PERFORMANCE MODE DECLARATION

**You are about to become each persona. They know what they migrated from.**

**SRE (REG-SRE-SETUP / EDGE / REGRESS):** You're on-call. {topic} replaced a system you
knew cold. Something is breaking silently. You need engineering to see what you're seeing
before the on-call alert fires. You are methodical but frustrated.

**Support (REG-SUP-REPEAT / PATTERN / ESCALATE):** You've seen this question every day this
week. You know what the old approach expected. You are filing this to get engineering to fix
the root so you stop being the manual workaround.

**PM (REG-PM-METRIC / FUNNEL / ATTRITION):** Your activation forecast is wrong. You cannot
tell if it is a product problem or a communication problem. You are filing for data.

**UX (REG-UX-SESSION / ABANDON / LONGTERM):** You are watching session recordings. Users
stall at a specific location. The old approach had a familiar affordance. You need
engineering to understand the root cause you can see but they cannot.

**C-xx (REG-CUST-CONFUSE / ADVANCED / SUSTAIN):** You switched from [old approach] recently.
Something surprised you. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Begin each body with the committed phrase from STEP 3B (expanded).
Body header MUST include `*(Reg: REG-xxx-TYPE)*` as a headline annotation citing the REG-ID.
Register type must match the REG-ID. Where migration-relevant: reference the old approach.**

---

### STEP 5 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows: ___ (matches Constraint Manifest)
- Distinct categories: ___ (>= 2), personas: ___ (>= 3)
- P0, high-volume within ceilings: Y / N
- All STEP 3B rows have valid REG-IDs: Y / N
- All bodies will have `*(Reg: REG-xxx-TYPE)*` headline annotation: Y / N

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted, ascending T-ID)

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title} *(Reg: REG-xxx-TYPE)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences. Begin with committed phrase expanded. First person only.
Register type matches REG-ID. Migration reference where relevant.]
```

---

### STEP 7 — Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|

---

### STEP 7B — Resolution Paths

For every high-volume OR P0/P1 ticket:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|

---

### STEP 8 — Gap Analysis

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | design change required

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | process change required

---

### VERIFICATION MANIFEST

| Verification target | Required | Actual | Pass? |
|--------------------|----------|--------|-------|
| Total tickets | = Constraint Manifest | ___ | ___ |
| Distinct categories | >= 2 | ___ | ___ |
| Distinct personas | >= 3 | ___ | ___ |
| Bodies starting with committed phrase | = total | ___ | ___ |
| Bodies with `*(Reg: REG-xxx-TYPE)*` headline annotation (C-18) | = total | ___ | ___ |
| REG-IDs in headers resolve to matrix rows | = total | ___ | ___ |
| No third-person role reference in any body | = total | ___ | ___ |

---

---

## V-04 — Combined: V-01 Compact Cell IDs + V-02 Standalone 5-Item Blocking Gate

**Combination axis:** V-01's compact Cell ID 3-node chain + V-02's standalone 5-item blocking
VOCABULARY PRE-FLIGHT GATE. The Cell ID scheme (`Role-P#`) from V-01 satisfies C-18 at all
three levels (matrix row header, commitment table Cell ID column, body headline annotation
`*(Cell: XX-P#)*`). The gate from V-02 satisfies C-19: standalone, names artifacts, 5 items,
blocking declaration. The rest inherits R4 V-05 verbatim (VOCABULARY MANIFEST with VM Row
IDs replaced by compact Cell IDs throughout; all other mechanisms preserved).

**Hypothesis:** V-01 satisfies C-18; V-02 satisfies C-19. V-04 tests whether the two
mechanisms are compositionally independent — each can be added without disrupting the other.
The compact Cell ID scheme is simpler than VM Row IDs and requires less space in headers.
If C-18 is satisfied by the compact Cell ID 3-node chain, V-04 achieves composite 100 under
v5 with lower structural overhead than V-05. The 5-item blocking gate makes C-19 pass
unambiguous. Expected result: composite 100.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium / low
Severity values: P0 | P1 | P2 | P3

---

### VOCABULARY MATRIX

**Complete before generating any ticket. Customize for {topic}. Cell IDs are the shared
identifier at all three levels: matrix row header, commitment table column, and body headline
annotation. Traceability: scorer reads body headline Cell ID, looks up STEP 3B row by Cell ID,
looks up matrix row by Cell ID — two lookups, zero body text.**

Cell ID format: `{Role-abbrev}-P{phase}` — e.g., `SRE-P1`, `Sup-P3`.

| Cell ID  | Role    | Phase   | Register description                                                    | Example template phrase                                                                      |
|----------|---------|---------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure           | "I'm seeing [failure] only when [condition] — I cannot reproduce it on demand..."           |
| SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                    | "We've been running {topic} for [N] weeks and we just noticed [regression]..."              |
| Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly      | "I keep seeing customers hit [obstacle] when they first [action]..."                         |
| Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause       | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."               |
| Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold   | "This is the [N]th escalation about [failure] this month — I need a permanent fix..."       |
| PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast           | "First-time activation is lower than projected — I want to understand what is blocking..."   |
| PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                       | "The [metric] is not improving at the expected rate — I need to investigate..."              |
| PM-P3    | PM      | Phase 3 | Late-stage attrition signal: post-onboarding drop-off                   | "I'm seeing users who completed onboarding dropping off at [stage]..."                       |
| UX-P1    | UX      | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..."             |
| UX-P2    | UX      | Phase 2 | Advanced feature abandonment: drop-off on complex action                | "Session recordings show abandonment when users attempt [advanced action]..."               |
| UX-P3    | UX      | Phase 3 | Long-term frustration with changed behavior or reliability              | "Long-term users are filing feedback about [behavior change / reliability issue]..."        |
| Cxx-P1   | C-xx    | Phase 1 | Migration surprise: expected old-approach behavior not present          | "I just switched from [old approach] and expected [X] but instead got [Y]..."               |
| Cxx-P2   | C-xx    | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks           | "I got the basics working but now [advanced scenario] fails with [error]..."                 |
| Cxx-P3   | C-xx    | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time  | "I've been using {topic} for [N] months and I'm noticing [concern]..."                      |

---

### CONSTRAINT MANIFEST

| Structural target                                             | Required                        | Committed value |
|---------------------------------------------------------------|---------------------------------|-----------------|
| Total tickets                                                 | 6 to 12                         | ___             |
| Phase 1 tickets (day 0-30)                                    | >= 3                            | ___             |
| Phase 2 tickets (day 31-60)                                   | >= 2                            | ___             |
| Phase 3 tickets (day 61-90)                                   | >= 1                            | ___             |
| P0 ceiling                                                    | <= floor(total × 0.25) = ___    | ___             |
| High-volume ceiling                                           | <= floor(total × 0.50) = ___    | ___             |
| Distinct named personas                                       | >= 3                            | ___             |
| SRE tickets                                                   | >= 2                            | ___             |
| Support tickets                                               | >= 2                            | ___             |
| C-xx tickets                                                  | >= 2 (max 2 per single C-xx)    | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)               | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary (C-14)             | >= 1                            | ___             |
| Tickets with Cell ID in commitment table AND body header (C-18) | = total ticket count          | ___             |

---

### STEP 1 — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 — Phase Map Table

| Phase   | Window    | Severity norm | Volume norm    | Body register                        |
|---------|-----------|---------------|----------------|--------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium    | Discovery/setup — use xxx-P1 cells   |
| Phase 2 | day 31-60 | P1/P2         | medium         | Integration/edge — use xxx-P2 cells  |
| Phase 3 | day 61-90 | P0/P1         | low/medium     | Operational/reliability — use xxx-P3 cells |

---

### STEP 3 — Theme Declaration

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

### STEP 3A — Role-Phase Cross-Matrix

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

### STEP 3B — Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. Record the Cell ID from the Vocabulary Matrix.
Derive the committed phrase from that cell's template. Body MUST begin with its committed
phrase (expanded). Body header MUST include `*(Cell: XX-P#)*` as a headline annotation.**

| T-ID | Cell ID  | Phase     | Committed opening phrase |
|------|----------|-----------|--------------------------|
| T-01 | ___-P___ | Phase ___ | "___" |
| T-02 | ___-P___ | Phase ___ | "___" |
| T-03 | ___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate. Execute immediately after STEP 3B, before STEP 4. Names artifacts by
section name. Declare GATE: OPEN or GATE: CLOSED. Body generation is blocked if CLOSED —
revise Vocabulary Matrix or STEP 3B and re-run this gate.**

**Item 1 — Vocabulary Matrix completeness**
Confirm: every (Role, Phase) in the ticket inventory has a Cell ID row in the VOCABULARY
MATRIX (not marked N/A).
Result: [ PASS — all ___ inventory combinations have VOCABULARY MATRIX cells ]
      / [ FAIL — missing: ___ ]

**Item 2 — Commitment table completeness**
Confirm: STEP 3B row count equals committed total in CONSTRAINT MANIFEST.
Result: [ PASS — STEP 3B has ___ rows = CONSTRAINT MANIFEST total ___ ]
      / [ FAIL — STEP 3B ___ ≠ CONSTRAINT MANIFEST ___ ]

**Item 3 — Phrase-to-cell traceability**
Confirm: each committed phrase in STEP 3B derives from the Example template phrase of its
Cell ID in the VOCABULARY MATRIX (same role, same phase, same register).
Result: [ PASS — all ___ phrases traceable to VOCABULARY MATRIX cells ]
      / [ FAIL — untraceable: T-___ (Cell ID: ___) ]

**Item 4 — Phase-register alignment**
Confirm: all Phase 1 committed phrases use P1-cell registers. At least one Phase 3 phrase
uses a P3-cell register (operational/reliability).
Result: [ PASS ] / [ FAIL — misaligned: ___ ]

**Item 5 — Inter-role register differentiation**
Confirm: in at least one phase, two or more roles have distinct register descriptions in
the VOCABULARY MATRIX.
Cite example: Phase ___, Cell ___ (___ role) = "___ register" vs Cell ___ (___ role) = "___ register"
Result: [ PASS — example cited ] / [ FAIL ]

**GATE: [ OPEN — all 5 items PASS — proceed to STEP 4 ]**
**GATE: [ CLOSED — ___ items failed — revise and re-run before continuing ]**

---

### STEP 4 — PERFORMANCE MODE DECLARATION

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior
system's failure modes cold; this one is still opaque to you. Something is breaking silently.
You are methodical but frustrated.

**Support:** You've answered this same migration question multiple times this week. You are
filing this to get engineering to fix the root cause so you can stop answering it.

**PM:** Adoption is below forecast. You are filing to request data.

**UX:** You are watching session recordings and seeing users stall at a specific point. You
know the friction point by location; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach in Step 1] recently. Something surprised you. You
do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Begin each body with the committed phrase from STEP 3B (expanded).
Body header MUST include `*(Cell: XX-P#)*` as a headline annotation.
Register matches the Vocabulary Matrix cell. Registers differ between roles in the same phase.
Where migration-relevant: reference what was expected from the old approach.**

---

### STEP 5 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows, categories, personas, P0/high-volume ceilings: all within Constraint Manifest
- All STEP 3B rows have valid Cell IDs from Vocabulary Matrix: Y / N
- All ticket bodies will have `*(Cell: XX-P#)*` headline annotation: Y / N

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted, ascending T-ID)

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title} *(Cell: XX-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences. Begin with committed phrase expanded. First person.
Register matches Cell ID. Migration reference where relevant.]
```

---

### STEP 7 — Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|

---

### STEP 7B — Resolution Paths

For every high-volume OR P0/P1 ticket:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|

---

### STEP 8 — Gap Analysis

**Documentation gaps** | Entry | Tickets: T-NN | Artifact

**Design gaps** | Entry | Tickets: T-NN | Change required

**Operational gaps** | Entry | Tickets: T-NN | Process change required

Minimum 2 entries per gap category.

---

### VERIFICATION MANIFEST

| Verification target | Required | Actual | Pass? |
|--------------------|----------|--------|-------|
| Total tickets | = Constraint Manifest | ___ | ___ |
| Distinct categories | >= 2 | ___ | ___ |
| Distinct personas | >= 3 | ___ | ___ |
| Bodies starting with committed phrase | = total | ___ | ___ |
| Bodies with `*(Cell: XX-P#)*` headline (C-18 node 3) | = total | ___ | ___ |
| Cell IDs in headers resolve to STEP 3B rows (C-18 node 2) | = total | ___ | ___ |
| Cell IDs in STEP 3B resolve to matrix rows (C-18 node 1) | = total | ___ | ___ |
| No third-person role reference | = total | ___ | ___ |
| Phase 1 discovery register | >= 3 | ___ | ___ |
| Phase 3 operational register | >= 1 | ___ | ___ |

---

---

## V-05 — Full Combination (All R4 V-05 Mechanisms + C-18 VM Body Header + C-19 5-Item Gate)

**Combination axis:** All R4 V-05 mechanisms retained verbatim plus two targeted additions:
1. **VOCABULARY MANIFEST** with VM Row IDs (R4 V-05 C-17) — retained
2. **CONSTRAINT MANIFEST + VERIFICATION MANIFEST** (R4 V-05 C-15) — retained
3. **Per-ticket commitment table** referencing VM Row IDs (R4 V-05 C-16) — retained
4. **Character-embodiment PERFORMANCE MODE** with migration backstory (R4 V-05 C-03) — retained
5. **Dual body instruction**: VM Row anchor + register rule (R4 V-05) — extended
6. **[NEW R5] Body header headline annotation `*(VM: VM-xxx-P#)*`** — completes C-18 3-node
   chain: VOCABULARY MANIFEST row → STEP 3B commitment row → body headline, all keyed by VM Row ID
7. **[NEW R5] Standalone VOCABULARY PRE-FLIGHT GATE section** — 5-item blocking gate placed
   after STEP 3B, before STEP 4; names VOCABULARY MANIFEST and commitment table by section
   name; declares GATE: OPEN / CLOSED; satisfies C-19

**Hypothesis:** R4 V-05 achieves 98.18 under v5: C-18 PARTIAL (VM Row IDs link manifest to
commitment table — two of three chain nodes — but body headers show VM Row ID in the metadata
subline, not as a headline annotation; rubric C-18 pass requires >= 75% of body headers to
cite a vocabulary identifier; a metadata subline may not qualify as "body header citation").
C-19 FAIL (pre-flight checks in STEP 3B are embedded in the commitment table step — they are
constraints on that step, not a standalone block naming vocabulary artifacts). V-05 R5 adds:
(1) `*(VM: VM-xxx-P#)*` as a mandatory headline annotation in every body header, making the
VM Row ID visible at headline scan without reading metadata or body text — scorer lookup: body
headline → STEP 3B Cell by VM Row ID → VOCABULARY MANIFEST row by VM Row ID, two lookups;
(2) a standalone VOCABULARY PRE-FLIGHT GATE section between STEP 3B and STEP 4, checking all
5 items, naming artifacts by section name, and declaring GATE: OPEN before STEP 4 runs. These
two additions satisfy C-18 and C-19 with minimum change to the R4 V-05 structure. Expected
result: composite 100 under v5.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic} — replace bracketed
placeholders with feature-specific language. Mark N/A for unused combinations. This is the
vocabulary contract: every ticket body must be traceable to its assigned VOCABULARY MANIFEST
row. VM Row IDs appear in this section, the commitment table (STEP 3B), AND the body headline
annotation — completing the 3-node C-18 traceability chain.**

| VM Row ID   | Role    | Phase   | Register description                                                   | Example template phrase                                                                      |
|-------------|---------|---------|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| VM-SRE-P1   | SRE     | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap post-deploy | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| VM-SRE-P2   | SRE     | Phase 2 | Edge-case operational: intermittent condition-specific failure          | "I'm seeing [failure] only when [condition] — I cannot reproduce it on demand..."           |
| VM-SRE-P3   | SRE     | Phase 3 | Reliability regression in production                                   | "We've been running {topic} in production for [N] weeks and we just noticed [regression]..." |
| VM-Sup-P1   | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly     | "I keep seeing customers hit [obstacle] when they first [action] — no guidance exists..."   |
| VM-Sup-P2   | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause      | "We're getting repeat questions about [X] and the pattern seems to be [Y]..."               |
| VM-Sup-P3   | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility threshold  | "This is the [N]th escalation about [failure] this month — I need a permanent fix..."       |
| VM-PM-P1    | PM      | Phase 1 | Adoption metric concern: first-time activation below forecast          | "First-time activation for {topic} is lower than projected — I want to understand..."       |
| VM-PM-P2    | PM      | Phase 2 | Funnel investigation: mid-adoption metric stalled                      | "The [metric] I projected is not improving — I need to investigate whether [hypothesis]..." |
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

| Structural target                                                   | Required                        | Committed value |
|---------------------------------------------------------------------|---------------------------------|-----------------|
| Total tickets                                                       | 6 to 12                         | ___             |
| Phase 1 tickets (day 0-30)                                          | >= 3                            | ___             |
| Phase 2 tickets (day 31-60)                                         | >= 2                            | ___             |
| Phase 3 tickets (day 61-90)                                         | >= 1                            | ___             |
| P0 ceiling                                                          | <= floor(total × 0.25) = ___    | ___             |
| High-volume ceiling                                                 | <= floor(total × 0.50) = ___    | ___             |
| Distinct named personas                                             | >= 3                            | ___             |
| SRE tickets                                                         | >= 2                            | ___             |
| Support tickets                                                     | >= 2                            | ___             |
| C-xx tickets                                                        | >= 2 (max 2 per single C-xx)    | ___             |
| Phase 1 bodies with discovery vocabulary (C-14)                     | >= 3                            | ___             |
| Phase 3 bodies with operational vocabulary (C-14)                   | >= 1                            | ___             |
| Tickets with VM Row ID in commitment table (C-16)                   | = total ticket count            | ___             |
| Tickets with VM Row ID in body headline annotation (C-18 node 3)   | = total ticket count            | ___             |

Do not proceed until both manifests are complete.

---

### STEP 1 — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 — Phase Map Table

| Phase   | Window    | Severity norm | Volume norm    | Body register                             |
|---------|-----------|---------------|----------------|-------------------------------------------|
| Phase 1 | day 0-30  | P2/P3         | high/medium    | Discovery/setup — use VM-xxx-P1 register  |
| Phase 2 | day 31-60 | P1/P2         | medium         | Integration/edge — use VM-xxx-P2 register |
| Phase 3 | day 61-90 | P0/P1         | low/medium     | Operational/reliability — use VM-xxx-P3 register |

---

### STEP 3 — Theme Declaration

```
Theme A: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

Theme B: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

[Theme C if needed — same format]
```

Each theme must have a distinct underlying failure. Sum of counts = CONSTRAINT MANIFEST total.

---

### STEP 3A — Role-Phase Cross-Matrix

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

### STEP 3B — Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. Reference the VOCABULARY MANIFEST Row ID for each
ticket. Derive the committed opening phrase from that row's template. The body MUST begin with
its committed phrase (expanded — not verbatim). The body header MUST include `*(VM: VM-xxx-P#)*`
as a headline annotation, completing the C-18 3-node chain:
  VOCABULARY MANIFEST row (VM Row ID) → STEP 3B commitment row (VM Row ID) → body headline (VM Row ID)
A scorer traces any body to its VOCABULARY MANIFEST row in two ID lookups, no body text required.**

| T-ID | VM Row ID   | Phase     | Committed opening phrase |
|------|-------------|-----------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ...  | | | |

---

### VOCABULARY PRE-FLIGHT GATE

**Standalone gate. Execute immediately after completing STEP 3B and before STEP 4. Each item
names the artifact it validates by section name. Declare GATE: OPEN or GATE: CLOSED. Body
generation (STEP 6) is blocked if the gate is CLOSED — revise the VOCABULARY MANIFEST or
STEP 3B and re-run this gate. The gate output must appear in the document before STEP 4.**

**Item 1 — VOCABULARY MANIFEST completeness**
Confirm: every (Role, Phase) combination in the ticket inventory has a corresponding row in
the VOCABULARY MANIFEST above (not marked N/A).
Result: [ PASS — all ___ inventory combinations have VOCABULARY MANIFEST rows ]
      / [ FAIL — missing combinations: ___ ]

**Item 2 — Commitment table completeness**
Confirm: row count in STEP 3B equals the committed ticket total in the CONSTRAINT MANIFEST.
Result: [ PASS — STEP 3B has ___ rows = CONSTRAINT MANIFEST total of ___ ]
      / [ FAIL — STEP 3B has ___ rows ≠ CONSTRAINT MANIFEST total of ___ ]

**Item 3 — Phrase-to-manifest traceability**
Confirm: each committed phrase in STEP 3B derives from the Example template phrase of its
VM Row ID in the VOCABULARY MANIFEST (same role, same phase, same register description).
Result: [ PASS — all ___ phrases traceable to their VOCABULARY MANIFEST row ]
      / [ FAIL — untraceable phrases: T-___ (VM Row ID: ___) ]

**Item 4 — Phase-register alignment**
Confirm: all Phase 1 committed phrases in STEP 3B use the discovery/setup register from
VM-xxx-P1 rows. At least one Phase 3 phrase uses the operational/reliability register from
a VM-xxx-P3 row.
Result: [ PASS — Phase 1 check: ___ rows OK; Phase 3 check: ___ rows OK ]
      / [ FAIL — Phase 1 misaligned: T-___ ; Phase 3 missing ]

**Item 5 — Inter-role register differentiation**
Confirm: in at least one phase, two or more roles have distinct register descriptions in
the VOCABULARY MANIFEST (bodies for those roles should sound different in that phase).
Cite the example explicitly:
  Phase ___ | VM Row ___ (___ role) = "___ register description"
  Phase ___ | VM Row ___ (___ role) = "___ register description"
Result: [ PASS — example cited above ] / [ FAIL — no phase found with differentiated roles ]

**GATE: [ OPEN — all 5 items PASS — proceed to STEP 4 PERFORMANCE MODE ]**
**GATE: [ CLOSED — ___ items failed — revise VOCABULARY MANIFEST and/or STEP 3B, then re-run this gate ]**

---

### STEP 4 — PERFORMANCE MODE DECLARATION (character-embodiment + migration context)

**You are about to become each persona. They know what they migrated from.**

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior
system's failure modes cold; this one is still opaque to you. Something is now breaking
silently that you would have caught immediately in the old system. You are methodical but
frustrated.

**Support:** You've answered this same migration question multiple times this week. You know
what the old approach expected; {topic} does something different that users keep tripping over.
You are filing this ticket to get engineering to fix the root cause so you can stop answering it.

**PM:** Adoption is below forecast. You cannot tell if it is a product problem or a
communication problem. You are filing this to request data.

**UX:** You are watching session recordings and seeing users stall at a specific point. The
old approach had a familiar affordance here; the new one does not. You know the friction point
by location; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach in Step 1] recently. Something surprised you —
either something that used to work stopped working, or something you expected to just work
required extra setup. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".**
**Begin each body with the committed phrase from STEP 3B (expanded into a full opening sentence).**
**Body header MUST include `*(VM: VM-xxx-P#)*` as a headline annotation citing the VOCABULARY**
**MANIFEST row ID — this is C-18 node 3. The scorer reads the headline, looks up STEP 3B by**
**VM Row ID, then looks up the VOCABULARY MANIFEST row by VM Row ID — two lookups, no body text.**
**Register must match the VOCABULARY MANIFEST row. Registers MUST differ between roles in the**
**same phase — confirmed by Item 5 of the VOCABULARY PRE-FLIGHT GATE above.**
**Where migration-relevant: reference what was expected from the old approach (Step 1).**

---

### STEP 5 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK — verify all before proceeding:
- Total rows: ___ (required: matches CONSTRAINT MANIFEST)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= MANIFEST ceiling)
- High-volume count: ___ (required: <= MANIFEST ceiling)
- Theme counts match Step 3 declarations: MATCH / MISMATCH
- Phase distribution matches CONSTRAINT MANIFEST: MATCH / MISMATCH
- All Phase 1 tickets have committed discovery phrase in STEP 3B: Y / N
- At least 1 Phase 3 ticket has committed operational phrase in STEP 3B: Y / N
- Every STEP 3B row has a valid non-N/A VM Row ID from VOCABULARY MANIFEST: Y / N
- Every ticket body will have `*(VM: VM-xxx-P#)*` headline annotation: Y / N

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

**Generation order within each theme: Phase 1 tickets first, then Phase 2, then Phase 3.**

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title} *(VM: VM-xxx-P#)*
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- VM Row: {row ID from STEP 3B} | Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences.
OPENING: Begin with the committed phrase from STEP 3B — expand into a full first sentence.
  Do not copy verbatim.
REGISTER: Use the vocabulary register from the VOCABULARY MANIFEST row. SRE bodies use
  technical/operational vocabulary. C-xx bodies reflect confusion or migration surprise.
  Support bodies reflect recurring-question frustration. Registers MUST differ between
  roles in the same phase — confirmed in VOCABULARY PRE-FLIGHT GATE Item 5.
VOICE: First person throughout — "I", "my", "we". No third-person role references.
MIGRATION: Where relevant, reference what was expected from the old approach (Step 1).
TRACEABILITY: The `*(VM: VM-xxx-P#)*` headline annotation is the C-18 node 3. A scorer
  reads the headline, looks up STEP 3B by VM Row ID (node 2), then looks up the
  VOCABULARY MANIFEST by VM Row ID (node 1) — two lookups, no body text required.
  Do not let the body deviate from its VOCABULARY MANIFEST row register.]
```

---

### STEP 7 — Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|
| ... | T-NN, T-NN | ... | Y/N | ... |

---

### STEP 7B — Resolution Paths

For every ticket that is high-volume OR P0/P1:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|
| T-NN | SRE / Support / PM / Eng | doc-gap / design-flaw / config-error / product-bug | self-serve (doc fix) / escalation (eng fix) / structural (design change) |

---

### STEP 8 — Gap Analysis

All entries require `Tickets: T-NN, T-NN` with identifiers matching the inventory above.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it (specific page or guide name)

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | design change required

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | process change required

Minimum 2 entries per gap category. Each entry cites at least one T-ID.

---

### VERIFICATION MANIFEST

**Post-generation audit. Complete after all bodies are written.**

| Verification target                                                     | Required              | Actual | Pass? |
|-------------------------------------------------------------------------|-----------------------|--------|-------|
| Total tickets generated                                                 | = CONSTRAINT MANIFEST | ___    | ___   |
| Distinct categories                                                     | >= 2                  | ___    | ___   |
| Distinct personas                                                       | >= 3                  | ___    | ___   |
| P0 count                                                                | <= ceiling            | ___    | ___   |
| High-volume count                                                       | <= ceiling            | ___    | ___   |
| Bodies starting with committed phrase                                   | = total               | ___    | ___   |
| Bodies with `*(VM: VM-xxx-P#)*` headline annotation (C-18 node 3)      | = total               | ___    | ___   |
| VM Row IDs in headlines resolve to STEP 3B rows (C-18 node 2)          | = total               | ___    | ___   |
| VM Row IDs in STEP 3B resolve to VOCABULARY MANIFEST rows (C-18 node 1) | = total              | ___    | ___   |
| No body uses third-person role reference                                | = total               | ___    | ___   |
| Phase 1 bodies use discovery/setup register                             | >= 3                  | ___    | ___   |
| Phase 3 bodies use operational/reliability register                     | >= 1                  | ___    | ___   |
| Registers differ between roles in same phase (C-17 + C-18 enforcement) | >= 1 phase confirmed  | ___    | ___   |

If any row fails: identify the ticket, correct, and re-verify.

---

---

## R5 Variation Summary

| Variation | C-18 mechanism | C-19 gate | Gate items | ID scheme | Predicted composite |
|-----------|---------------|-----------|------------|-----------|---------------------|
| V-01 | Compact Cell IDs in matrix, STEP 3B, and body headline `*(Cell: XX-P#)*` | Standalone block | 4 items | `Role-P#` | ~100 |
| V-02 | VM Row IDs in manifest, STEP 3B, body metadata line (2/3 nodes; headline absent) | Standalone blocking gate | 5 items, artifact-named | `VM-Role-P#` | ~99.1 |
| V-03 | Semantic REG-IDs in matrix, STEP 3B, and body headline `*(Reg: REG-Role-TYPE)*` | Standalone block | 3 items (minimum) | `REG-Role-TYPE` | ~100 |
| V-04 | Compact Cell IDs at all 3 levels; matrix, STEP 3B, body headline `*(Cell: XX-P#)*` | Standalone blocking gate | 5 items, artifact-named | `Role-P#` | 100 |
| V-05 | VM Row IDs at all 3 levels; VOCABULARY MANIFEST, STEP 3B, body headline `*(VM: VM-xxx-P#)*` | Standalone blocking gate | 5 items, artifact-named, blocking declaration | `VM-Role-P#` | 100 |

**C-18 traceability chain by variation:**

| Variation | Node 1 (matrix) | Node 2 (commitment table) | Node 3 (body header) | Chain complete? |
|-----------|----------------|--------------------------|----------------------|----------------|
| V-01 | Cell ID as row header | Cell ID column in STEP 3B | `*(Cell: XX-P#)*` headline | YES |
| V-02 | VM Row ID as manifest row | VM Row ID column in STEP 3B | VM Row ID in metadata subline | PARTIAL |
| V-03 | REG-ID as matrix row | REG-ID column in STEP 3B | `*(Reg: REG-xxx-TYPE)*` headline | YES |
| V-04 | Cell ID as row header | Cell ID column in STEP 3B | `*(Cell: XX-P#)*` headline | YES |
| V-05 | VM Row ID as manifest row | VM Row ID column in STEP 3B | `*(VM: VM-xxx-P#)*` headline | YES |

**C-19 gate by variation:**

| Variation | Gate is standalone section? | Names artifacts by section name? | Items >= 3? | Declares blocking? | C-19 prediction |
|-----------|---------------------------|----------------------------------|-------------|---------------------|-----------------|
| V-01 | YES | Partial (names "Vocabulary Matrix") | 4 | YES | PASS |
| V-02 | YES | YES (names "VOCABULARY MANIFEST", "CONSTRAINT MANIFEST", "STEP 3B") | 5 | YES | PASS |
| V-03 | YES | Partial (names "Register Vocabulary Matrix") | 3 | YES | PASS |
| V-04 | YES | YES (names "VOCABULARY MATRIX", "CONSTRAINT MANIFEST", "STEP 3B") | 5 | YES | PASS |
| V-05 | YES | YES (names "VOCABULARY MANIFEST", "CONSTRAINT MANIFEST", "STEP 3B") | 5 | YES, explicit | PASS |

**Observation for scorecard:**
V-02's C-18 is PARTIAL because the VM Row ID appears in the body metadata subline
(`VM Row: VM-xxx-P1`), not as a headline annotation. The rubric requires >= 75% of body
headers to cite the vocabulary identifier — whether a metadata subline counts as a "body
header citation" is the open question. V-04 and V-05 close this ambiguity by placing the ID
in the headline itself (`*(Cell: XX-P#)*` or `*(VM: VM-xxx-P#)*`). An R5 scorecard that
confirms V-01/V-03/V-04/V-05 all score C-18 PASS and V-02 PARTIAL would provide the
disambiguation evidence for R6: the exact format required in the headline annotation vs
metadata subline.
