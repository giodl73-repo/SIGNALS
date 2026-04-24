# listen-support — Variations, Round 4 (rubric v4 — 17 criteria)

**Date:** 2026-03-15
**Rubric target:** v4 (C-01 through C-17 — 17 criteria; aspirational tier denominator = 9)
**Baseline:** R3 V-05 (composite 100 under v3; scores 97.8 under v4 — C-16/C-17 not yet closed)
**R4 objective:** Close the two new aspirational gaps that R3 V-05 cannot satisfy under v4:
  - **C-16** — Per-ticket vocabulary pre-commitment: a visible commitment table (T-ID + committed opening phrase) before body writing; each body begins with its committed phrase.
  - **C-17** — Role-phase vocabulary matrix: a 2D role × phase matrix (min 4 cells, 2+ roles × 2+ phases); each cell has distinct register; ticket bodies traceable to their assigned cell.

**The R3 gap analysis:**
- R3 V-01: per-ticket commitment table from *phase-only* pools → C-16 PASS, C-17 FAIL (no role differentiation within phases)
- R3 V-03: role-phase vocabulary matrix declared → C-17 PASS, C-16 FAIL (no per-ticket commitment table)
- R3 V-04/V-05: V-01 + V-02 mechanisms but without role-phase matrix → C-16 PASS, C-17 FAIL

**R4 strategy:** All five variations must combine both mechanisms. Single-axis variations isolate
three approaches to the integration; combined variations stack them.

---

## Fixed Changes Applied to All Variations

All five R4 variations inherit the full R3 V-05 foundation. These components are not the
differentiating axis.

| Component | R3 source | R4 status |
|-----------|----------|-----------|
| Phase distribution target declaration | R3 all | Retained |
| Status quo / migration analysis | R3 all | Retained |
| Phase map with severity norms, volume norms | R3 all | Retained |
| Theme declaration (C-09) | R3 all | Retained |
| Role-phase count matrix / planning | R3 all | Retained |
| Character-embodiment PERFORMANCE MODE (C-03) | R3 V-04/V-05 | Retained |
| Ticket inventory table + TABLE CHECK (C-01/C-02/C-05/C-11) | R3 all | Extended (adds C-16/C-17 checks) |
| Ticket bodies by theme/phase | R3 all | Extended (adds matrix-cell header line) |
| Cross-ticket patterns (C-09) | R3 all | Retained |
| Resolution paths table (C-10) | R3 all | Retained |
| Gap analysis with T-NN refs (C-04/C-08) | R3 all | Retained |
| Dual-pass verification (C-11/C-15) | R3 V-02/V-05 | Extended (adds C-16/C-17 lines) |
| Constraint manifest + verification manifest (C-15) | R3 V-02/V-04/V-05 | Retained in V-02/V-04/V-05 |

---

## R4 Variation Axes

R1 explored: role sequence, output format, lifecycle emphasis.
R2 explored: phrasing register, inertia framing, theme-first generation.
R3 explored: lifecycle emphasis (vocabulary pre-commitment from phase pools), output format
(manifest tables), role sequence (role-phase vocabulary matrix).
R4 targets the orthogonal intersection: combine the phase-pool commitment table (C-16) with
the role-phase vocabulary matrix (C-17) — two mechanisms that R3 developed independently.

| Axis | Single-axis variation | New angle vs prior rounds | Target criteria |
|------|-----------------------|--------------------------|-----------------|
| Lifecycle emphasis | V-01 | Matrix-derived per-ticket commitment: commitment table rows reference a specific role × phase cell | C-16 + C-17 |
| Output format | V-02 | Vocabulary manifest as a named top-level section; commitment table references manifest row IDs | C-17 + C-16 + C-15 |
| Role sequence | V-03 | Per-role vocabulary declaration blocks with inline commitment sub-tables before each role's bodies | C-17 + C-16 |

Combined: V-04 stacks V-01 + V-02. V-05 stacks all R3 and R4 mechanisms (composite 100
candidate under v4).

---

## V-01 — Single Axis: Lifecycle Emphasis (Matrix-Derived Per-Ticket Commitment)

**Axis:** Lifecycle emphasis — STEP 2 introduces a role-phase vocabulary matrix that defines
vocabulary register for each role × phase combination. STEP 2B derives the per-ticket
commitment table from that matrix: each row records T-ID, role, phase, matrix cell ID, and
committed opening phrase. The body must begin with its committed phrase, making bodies
traceable to their matrix cell by inspection.

**Hypothesis:** R3 V-01 committed per ticket from phase-only pools (all Phase 1 tickets drew
from the same pool regardless of role), satisfying C-16 but not C-17. R3 V-03 declared a
role-phase matrix but had no per-ticket commitment table, satisfying C-17 but not C-16. V-01
R4 fuses the mechanisms: the matrix defines the vocabulary space (C-17 structure); the
commitment table draws from matrix cells with explicit cell references (C-16 + C-17 body
traceability). C-16 and C-17 are satisfied simultaneously by construction: the scorer can
trace any body opening phrase to its matrix cell without inspecting metadata.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### STEP 1 — Phase Distribution Target

Declare before generating any ticket:

```
Phase 1 (day 0-30):   ___ tickets   [target: >= 3]
Phase 2 (day 31-60):  ___ tickets   [target: >= 2]
Phase 3 (day 61-90):  ___ tickets   [target: >= 1]
Total:                ___ tickets   [required: >= 6 and <= 12]
P0 ceiling:           ___ = floor(total × 0.25)
High-volume ceiling:  ___ = floor(total × 0.50)
```

---

### STEP 1B — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 — Role-Phase Vocabulary Matrix

**Customize each cell for {topic} before generating any ticket. Replace bracketed placeholders
with feature-specific language. Enter "N/A" for combinations where that role produces no
tickets in that phase.**

Each cell provides two things: a vocabulary register description and an example template
phrase. Every ticket body must begin with a phrase drawn from its assigned cell. Expand
the template — do not copy verbatim.

Cell ID convention: {role-abbreviation}/P{phase-number} — e.g., SRE/P1, Support/P2, C-xx/P3.

| Role    | Phase 1 (discovery/setup) | Phase 2 (integration/edge) | Phase 3 (operational/reliability) |
|---------|--------------------------|---------------------------|-----------------------------------|
| SRE | Register: setup-oriented technical confusion — SRE deployed the feature but monitoring/alerting is broken. Template: "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." | Register: edge-case operational failure — intermittent, condition-specific. Template: "I'm seeing [failure] only when [condition] — I cannot reproduce it consistently..." | Register: reliability regression in production. Template: "We've been running {topic} in production for [N] weeks and we just noticed [silent failure / regression]..." |
| Support | Register: recurring-question frustration — same migration obstacle arriving repeatedly. Template: "I keep seeing customers hit [obstacle] when they first [action] — I cannot find guidance on..." | Register: pattern identification — repeat questions pointing to a root cause. Template: "We're getting repeat questions about [X] and the pattern seems to be [Y]..." | Register: escalation urgency — chronic failure at leadership visibility threshold. Template: "This is the [N]th escalation about [failure] this month — I need a permanent fix..." |
| PM | Register: adoption metric concern — first-time activation below forecast. Template: "First-time activation for {topic} is lower than projected — I want to understand what is blocking..." | Register: funnel investigation — mid-adoption metric stalled. Template: "The [metric] I projected is not improving at the rate expected — I need to investigate..." | Register: late-stage attrition signal — post-onboarding drop-off. Template: "I'm seeing users who completed onboarding dropping off at [stage]..." |
| UX | Register: session-observation friction — users stalling at identifiable UI location. Template: "I'm watching session recordings and users consistently stall at [location]..." | Register: advanced feature abandonment — identifiable drop-off on complex action. Template: "Session recordings show abandonment when users attempt [advanced action]..." | Register: long-term frustration — changed behavior or reliability concern. Template: "Long-term users are filing feedback about [behavior change / reliability issue]..." |
| C-xx | Register: migration surprise — expected old-approach behavior not present. Template: "I just switched from [old approach from Step 1B] and expected [X] but instead got [Y]..." | Register: advanced usage failure — basics work, advanced scenario breaks. Template: "I got the basics working but now [advanced scenario] fails with [error]..." | Register: sustained-usage concern — reliability or data issue surfacing over time. Template: "I've been using {topic} for [N] months and I'm noticing [concern] that wasn't there initially..." |

**Rule: every ticket body must begin with a phrase drawn from its role × phase cell.
Expand the template into a full opening sentence — do not copy verbatim.**

---

### STEP 2B — Per-Ticket Vocabulary Commitment Table

**Fill this table before generating any ticket body. For each ticket: select the opening
phrase from its role × phase matrix cell, record the cell ID, and write the committed phrase.
The body MUST begin with its committed phrase (expanded into a full sentence — not verbatim).**

| T-ID | Role | Phase | Cell ID | Committed opening phrase |
|------|------|-------|---------|--------------------------|
| T-01 | ___ | Phase ___ | ___/P___ | "___" |
| T-02 | ___ | Phase ___ | ___/P___ | "___" |
| T-03 | ___ | Phase ___ | ___/P___ | "___" |
| ... | | | | |

Pre-flight check:
- All Phase 1 rows reference Phase-1 cells (P1 in Cell ID): Y / N
- All Phase 1 committed phrases use discovery/setup register: Y / N
- At least one Phase 3 row uses operational/reliability register (P3 cell): Y / N
- All cell IDs reference valid non-N/A cells in STEP 2 matrix: Y / N

If any check is N: revise commitment table before continuing.

---

### STEP 3 — Theme Declaration

Declare 2-3 named themes before generating any ticket:

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

Each theme must have a distinct underlying failure. Sum of counts = Step 1 total.

---

### STEP 3A — Role-Phase Cross-Matrix

Fill before generating any ticket body.

| Role    | Phase 1 | Phase 2 | Phase 3 | Total | Theme(s) |
|---------|---------|---------|---------|-------|----------|
| SRE     | ___     | ___     | ___     | ___   | ___      |
| Support | ___     | ___     | ___     | ___   | ___      |
| PM      | ___     | ___     | ___     | ___   | ___      |
| UX      | ___     | ___     | ___     | ___   | ___      |
| C-xx    | ___     | ___     | ___     | ___   | ___      |

Constraint 1: SRE >= 2, Support >= 2, PM >= 1, UX >= 1, C-xx >= 2
Constraint 2: Any role with 3+ tickets must span at least 2 phases (C-12)
Constraint 3: Any single C-xx persona in at most 2 tickets

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

**C-xx:** You switched from [old approach in Step 1B] recently. Something surprised you —
either something that used to work stopped working, or something you expected to just work
required extra setup. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Begin each body with the phrase committed in STEP 2B (expanded into a full opening sentence).
Where migration-relevant: reference what was expected from the old approach.**

---

### STEP 5 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK — verify all before proceeding:
- Total rows: ___ (required: >= 6 and <= 12)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= Step 1 ceiling)
- High-volume count: ___ (required: <= Step 1 ceiling)
- Theme counts match Step 3 declarations: MATCH / MISMATCH
- Phase distribution matches Step 1: MATCH / MISMATCH
- All Phase 1 tickets have committed discovery phrase in STEP 2B: Y / N
- At least 1 Phase 3 ticket has committed operational phrase in STEP 2B: Y / N
- Every STEP 2B row has a valid cell ID referencing STEP 2 matrix: Y / N

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Matrix cell: {cell ID from STEP 2B} | Committed phrase: "{phrase from STEP 2B}"

**Ticket body:**
[2-5 sentences. Begin with the committed phrase from STEP 2B (expanded).
Embody the persona from Step 4. Register must match the matrix cell declared above.
Where migration-relevant: reference what was expected from the old approach in Step 1B.]
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

All three fields required per qualifying ticket.

---

### STEP 8 — Gap Analysis

All entries require `Tickets: T-NN, T-NN` with identifiers matching the inventory above.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it (specific page or guide name)

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it (specific design decision)

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it (runbook, alert, or dashboard)

**Migration friction sub-section** (include if >= 2 migration tickets):
Friction point | affected tickets | what would eliminate it

---

### STEP 9 — Dual-Pass Verification

**Pass 1 — Coverage trace (one sentence each):**
- C-01 (inventory complete): ...
- C-02 (persona attribution): ...
- C-03 (first-person voice): ...
- C-04 (T-NN in gap entries): ...
- C-05 (distribution non-trivial): ...

**Pass 2 — Structural property verification:**

```
Phase distribution:
  Phase 1: declared ___ / actual ___   MATCH / MISMATCH
  Phase 2: declared ___ / actual ___   MATCH / MISMATCH
  Phase 3: declared ___ / actual ___   MATCH / MISMATCH

Theme distribution:
  Theme A: declared ___ / actual ___   MATCH / MISMATCH
  Theme B: declared ___ / actual ___   MATCH / MISMATCH

Role-phase compound coverage (C-12):
  Roles with 3+ tickets: [list] — each spans 2+ phases: Y / N

Phase-severity calibration (C-13):
  Phase 1 tickets at P2/P3: ___ of ___   (required: >= 60%)   PASS / FAIL
  At least 1 Phase 3 ticket at P0/P1: Y / N   PASS / FAIL

Phase-anchored vocabulary (C-14):
  Phase 1 bodies beginning with discovery/onboarding phrase: ___ of ___   (required: >= 3)   PASS / FAIL
  Phase 3 bodies beginning with operational/reliability phrase: ___ of ___   (required: >= 1)   PASS / FAIL

Per-ticket vocabulary commitment (C-16):
  Commitment table rows present: ___ (required: = total ticket count)   PASS / FAIL
  Bodies beginning with committed phrase: ___ of ___   (required: all)   PASS / FAIL

Role-phase vocabulary matrix (C-17):
  Matrix cells populated (non-N/A): ___ (required: >= 4)   PASS / FAIL
  Distinct roles in matrix: ___ (required: >= 2)   PASS / FAIL
  Distinct phases in matrix: ___ (required: >= 2)   PASS / FAIL
  Each cell has distinct register (not a copy of adjacent cell): Y / N   PASS / FAIL
  At least one Phase 1 pair shows role differentiation: Y / N   PASS / FAIL
  Ticket bodies traceable to matrix cells via cell ID header lines: Y / N   PASS / FAIL

Broken T-NN refs in gap entries: ___   (required: 0)
Resolution paths complete for all qualifying tickets: Y / N
```

If any check fails: revise before submitting.

---

## V-02 — Single Axis: Output Format (Vocabulary Manifest + Constraint Manifest + Verification Manifest)

**Axis:** Output format — the role-phase vocabulary matrix is elevated to a named VOCABULARY
MANIFEST at the very top of the output, a structural peer to the CONSTRAINT MANIFEST. The
VOCABULARY MANIFEST has rows for each role × phase combination with register and example
phrase columns. The per-ticket commitment table (STEP 3) references vocabulary manifest rows
by row ID. The VERIFICATION MANIFEST at the bottom adds vocabulary and commitment verification
rows alongside structural constraint rows.

**Hypothesis:** R3 V-02 introduced the CONSTRAINT MANIFEST / VERIFICATION MANIFEST pair,
making C-15 satisfiable by form — the manifest structure cannot be absent if the prompt
requires it as the first visible section. V-02 R4 extends this architecture with a third
manifest: the VOCABULARY MANIFEST makes C-17 satisfiable by form (the matrix cannot be
omitted when it is a named top-level section the prompt requires first); the per-ticket
commitment table referencing manifest row IDs makes C-16 satisfiable by structure (each
ticket must have a manifest row reference before body generation). All three criteria
(C-15, C-16, C-17) become form-level guarantees. A scorer can check all three by reading
three named sections: VOCABULARY MANIFEST, per-ticket commitment table, VERIFICATION MANIFEST.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize register descriptions and template phrases
for {topic}. Mark N/A for role-phase combinations that will not appear in the ticket inventory.
This is your vocabulary contract — every ticket body must be traceable to its manifest row.**

| Row ID | Role | Phase | Register description | Example template phrase |
|--------|------|-------|----------------------|-------------------------|
| VM-SRE-P1 | SRE | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap after deployment | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| VM-SRE-P2 | SRE | Phase 2 | Edge-case operational: intermittent condition-specific failure | "I'm seeing [failure] only when [condition] — I cannot reproduce it on demand..." |
| VM-SRE-P3 | SRE | Phase 3 | Reliability regression in production | "We've been running {topic} in production for [N] weeks and we just noticed [regression]..." |
| VM-Sup-P1 | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly | "I keep seeing customers hit [obstacle] when they first [action]..." |
| VM-Sup-P2 | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause | "We're getting repeat questions about [X] and the pattern seems to be [Y]..." |
| VM-Sup-P3 | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility | "This is the [N]th escalation about [failure] this month — I need a permanent fix..." |
| VM-PM-P1 | PM | Phase 1 | Adoption metric concern: first-time activation below forecast | "First-time activation for {topic} is lower than projected — I want to understand what is blocking..." |
| VM-PM-P2 | PM | Phase 2 | Funnel investigation: metric stalled mid-adoption | "The [metric] I projected is not improving — I need to investigate whether [hypothesis]..." |
| VM-PM-P3 | PM | Phase 3 | Late-stage attrition signal: post-onboarding drop-off | "I'm seeing users who completed onboarding dropping off at [stage]..." |
| VM-UX-P1 | UX | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..." |
| VM-UX-P2 | UX | Phase 2 | Advanced feature abandonment: drop-off on complex action | "Session recordings show abandonment when users attempt [advanced action]..." |
| VM-UX-P3 | UX | Phase 3 | Long-term frustration with changed behavior or reliability | "Long-term users are filing feedback about [behavior change / reliability issue]..." |
| VM-Cxx-P1 | C-xx | Phase 1 | Migration surprise: expected old-approach behavior not present | "I just switched from [old approach] and expected [X] but instead got [Y]..." |
| VM-Cxx-P2 | C-xx | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks | "I got the basics working but now [scenario] fails with [error]..." |
| VM-Cxx-P3 | C-xx | Phase 3 | Sustained-usage concern: reliability or data issue over time | "I've been using {topic} for [N] months and I'm noticing [concern]..." |

Do not proceed to CONSTRAINT MANIFEST until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

**Complete before generating any ticket. Pre-generation structural commitment.**

| Structural target | Required | Committed value |
|------------------|----------|----------------|
| Total tickets | 6 to 12 | ___ |
| Phase 1 tickets (day 0-30) | >= 3 | ___ |
| Phase 2 tickets (day 31-60) | >= 2 | ___ |
| Phase 3 tickets (day 61-90) | >= 1 | ___ |
| P0 ceiling | <= floor(total × 0.25) = ___ | ___ |
| High-volume ceiling | <= floor(total × 0.50) = ___ | ___ |
| Distinct named personas | >= 3 | ___ |
| SRE tickets | >= 2 | ___ |
| Support tickets | >= 2 | ___ |
| C-xx tickets | >= 2 (max 2 per single C-xx) | ___ |
| Phase 1 bodies with discovery vocabulary (C-14) | >= 3 | ___ |
| Phase 3 bodies with operational vocabulary (C-14) | >= 1 | ___ |
| Tickets with VM row reference in commitment table (C-16) | = total ticket count | ___ |

Do not proceed to STEP 1 until both manifests are complete.

---

### STEP 1 — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 — Phase Map Table

| Phase | Window | Severity norm | Volume norm | Body register |
|-------|--------|--------------|------------|--------------|
| Phase 1 | day 0-30 | P2/P3 | high/medium | Discovery/setup — see VM-xxx-P1 rows |
| Phase 2 | day 31-60 | P1/P2 | medium | Integration/edge — see VM-xxx-P2 rows |
| Phase 3 | day 61-90 | P0/P1 | low/medium | Operational/reliability — see VM-xxx-P3 rows |

---

### STEP 2B — Theme Declaration

Declare 2-3 named themes:

```
Theme A: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

Theme B: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

[Theme C if needed]
```

Sum of counts = CONSTRAINT MANIFEST total.

---

### STEP 3 — Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. Reference the Vocabulary Manifest row ID for each
ticket. The body must begin with a phrase consistent with that row's register and template —
expanded, not verbatim.**

| T-ID | VM Row ID | Phase | Committed opening phrase |
|------|-----------|-------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| ... | | | |

Verification:
- All VM Row IDs reference non-N/A rows in VOCABULARY MANIFEST: Y / N
- Phase in each row matches the phase embedded in its VM Row ID: Y / N

If either fails: revise before generating tickets.

---

### STEP 4 — Role-Phase Cross-Matrix

| Role    | Phase 1 | Phase 2 | Phase 3 | Total |
|---------|---------|---------|---------|-------|
| SRE     | ___     | ___     | ___     | ___   |
| Support | ___     | ___     | ___     | ___   |
| PM      | ___     | ___     | ___     | ___   |
| UX      | ___     | ___     | ___     | ___   |
| C-xx    | ___     | ___     | ___     | ___   |

Constraint: Any role with 3+ tickets must span at least 2 phases.

---

### STEP 5 — PERFORMANCE MODE DECLARATION

**You are about to become each persona. They know what they migrated from.**

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior
system's failure modes cold; this one is still opaque to you. Something is now breaking
silently. You are methodical but frustrated.

**Support:** You've answered this same migration question multiple times. You know what the
old approach expected; {topic} does something different. You are filing this to get engineering
to fix the root cause.

**PM:** Adoption is below forecast. You cannot tell if it is a product or communication
problem. You are filing this to request data.

**UX:** You are watching session recordings. Users stall at a specific point. The old approach
had a familiar affordance here. You know the friction point; you need engineering to understand
the root cause.

**C-xx:** You switched from [old approach in Step 1] recently. Something surprised you. You
do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Begin each body with the committed phrase from STEP 3. Register must match the VM row.**

---

### STEP 6 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows: ___ (required: matches CONSTRAINT MANIFEST)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= MANIFEST ceiling)
- High-volume count: ___ (required: <= MANIFEST ceiling)
- Phase distribution: Phase 1 ___ / Phase 2 ___ / Phase 3 ___ (required: matches MANIFEST)
- Every ticket has a row in STEP 3 commitment table: Y / N

---

### STEP 7 — Ticket Bodies (by theme, phase-sorted within each theme)

```
### Theme A — {theme name}
*Underlying failure: {from Step 2B}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- VM Row: {row ID from STEP 3} | Committed phrase: "{phrase from STEP 3}"

**Ticket body:**
[2-5 sentences. Begin with the committed phrase (expanded).
Register must match the Vocabulary Manifest row for this ticket.
First person: "I", "my", "we". Where migration-relevant: reference the old approach.]
```

---

### STEP 8 — Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|
| ... | T-NN, T-NN | ... | Y/N | ... |

---

### STEP 8B — Resolution Paths

For every ticket that is high-volume OR P0/P1:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|
| T-NN | SRE / Support / PM / Eng | doc-gap / design-flaw / config-error / product-bug | self-serve / escalation / structural |

---

### STEP 9 — Gap Analysis

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it

**Migration friction sub-section** (include if >= 2 migration tickets):
Friction point | affected tickets | what would eliminate it

---

### VERIFICATION MANIFEST

**Complete after gap analysis. Compares CONSTRAINT MANIFEST commitments to actual output.**

| Structural target | Required | Actual | Status |
|------------------|----------|--------|--------|
| Total tickets | 6–12 | ___ | PASS / FAIL |
| Phase 1 tickets | >= 3 | ___ | PASS / FAIL |
| Phase 2 tickets | >= 2 | ___ | PASS / FAIL |
| Phase 3 tickets | >= 1 | ___ | PASS / FAIL |
| P0 tickets | <= ___ (floor(___ × 0.25)) | ___ | PASS / FAIL |
| High-volume tickets | <= ___ (floor(___ × 0.50)) | ___ | PASS / FAIL |
| Distinct named personas | >= 3 | ___ | PASS / FAIL |
| SRE tickets | >= 2 | ___ | PASS / FAIL |
| Support tickets | >= 2 | ___ | PASS / FAIL |
| C-xx tickets | >= 2 | ___ | PASS / FAIL |
| Roles with 3+ tickets spanning 2+ phases (C-12) | all: Y | Y / N | PASS / FAIL |
| Phase 1 tickets at P2/P3 (C-13) | >= 60% (>= ___ of ___) | ___ of ___ | PASS / FAIL |
| Phase 3 tickets at P0/P1 (C-13) | >= 1 | ___ | PASS / FAIL |
| Phase 1 bodies with discovery vocabulary (C-14) | >= 3 | ___ | PASS / FAIL |
| Phase 3 bodies with operational vocabulary (C-14) | >= 1 | ___ | PASS / FAIL |
| Commitment table rows = total ticket count (C-16) | = ___ | ___ | PASS / FAIL |
| Bodies beginning with committed phrase (C-16) | all (___ of ___) | ___ | PASS / FAIL |
| VM non-N/A rows populated (C-17) | >= 4 | ___ | PASS / FAIL |
| VM distinct roles (C-17) | >= 2 | ___ | PASS / FAIL |
| VM distinct phases (C-17) | >= 2 | ___ | PASS / FAIL |
| Phase 1 cells show role differentiation (C-17) | >= 1 pair | Y / N | PASS / FAIL |
| Ticket bodies traceable to VM rows (C-17) | all | Y / N | PASS / FAIL |
| Pre-ticket structural commitment present (C-15) | CONSTRAINT MANIFEST: Y | Y / N | PASS / FAIL |
| Post-ticket numeric verification (C-15) | VERIFICATION MANIFEST: Y | Y / N | PASS / FAIL |
| Broken T-NN refs in gap entries (C-11) | 0 | ___ | PASS / FAIL |
| Resolution paths complete (C-10) | all qualifying | Y / N | PASS / FAIL |

If any row shows FAIL: revise before submitting.

---

## V-03 — Single Axis: Role Sequence (Per-Role Vocabulary Declaration Blocks)

**Axis:** Role sequence — tickets generated in strict role blocks (SRE → Support → PM → UX →
C-xx). Before generating each role's ticket bodies, a ROLE VOCABULARY DECLARATION sub-section
specifies: (a) phases this role appears in, (b) register and example phrase per phase, (c) a
per-role commitment sub-table listing all tickets in this role block with committed phrases.

**Hypothesis:** R3 V-03 used role-sequence generation with a global role-phase matrix declared
before all tickets. The distance between matrix declaration and body writing could span 80+
lines for late roles. V-03 R4 collapses this distance: vocabulary declaration → commitment →
body generation occur in a single tightly-coupled role block. When writing C-xx/Phase-3
bodies, the C-xx/Phase-3 register is visible three lines above, not 80 lines above. C-17 is
satisfied by the per-role vocabulary declaration structure (distinct register per phase, role
block physically present before bodies); C-16 is satisfied by per-role commitment sub-tables
(all commitments for a role are declared immediately before that role's bodies are written).
A model cannot skip vocabulary pre-commitment for a role without the role block structure
visibly breaking.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### STEP 1 — Structural Targets

Declare before generating any ticket:

```
Total tickets:          ___ (required: >= 6 and <= 12)
Phase 1 target (0-30):  ___ (required: >= 3)
Phase 2 target (31-60): ___ (required: >= 2)
Phase 3 target (61-90): ___ (required: >= 1)
P0 ceiling:             ___ = floor(total × 0.25)
High-volume ceiling:    ___ = floor(total × 0.50)
Distinct named personas: >= 3
Role minimums: SRE >= 2, Support >= 2, PM >= 1, UX >= 1, C-xx >= 2
```

---

### STEP 1B — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction: ___
```

---

### STEP 2 — Phase Map

| Phase | Window | Severity norm | Volume norm | Vocabulary character |
|-------|--------|--------------|------------|---------------------|
| Phase 1 | day 0-30 | P2/P3 | high/medium | Discovery and onboarding — first contact, setup confusion, doc gaps |
| Phase 2 | day 31-60 | P1/P2 | medium | Integration and edge cases — basics work, advanced scenarios surprise |
| Phase 3 | day 61-90 | P0/P1 | low/medium | Operational and reliability — sustained use, regressions, SLO impact |

---

### STEP 3 — Theme Declaration

Declare 2-3 named themes:

```
Theme A: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

Theme B: {short name}
  Underlying product/doc failure: ___
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)
  Expected ticket count: ___

[Theme C if needed]
```

Sum of counts = Step 1 total. Each theme has a distinct underlying failure.

---

### STEP 4 — Role-Phase Count Matrix

| Role    | Phase 1 | Phase 2 | Phase 3 | Total |
|---------|---------|---------|---------|-------|
| SRE     | ___     | ___     | ___     | ___   |
| Support | ___     | ___     | ___     | ___   |
| PM      | ___     | ___     | ___     | ___   |
| UX      | ___     | ___     | ___     | ___   |
| C-xx    | ___     | ___     | ___     | ___   |

Constraint: Any role with 3+ tickets must span at least 2 phases (C-12).

---

### STEP 5 — Ticket Inventory Table

List all tickets before generating any body.

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK — verify before entering role blocks:
- Total rows: ___ (required: >= 6 and <= 12, matches Step 1)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= Step 1 ceiling)
- High-volume count: ___ (required: <= Step 1 ceiling)
- Phase distribution matches Step 1: MATCH / MISMATCH

If any check fails: revise before entering role blocks.

---

### ROLE BLOCKS

**Generate in this order: SRE → Support → PM → UX → C-xx. Before writing any body within
a role block, complete the VOCABULARY DECLARATION and COMMITMENT TABLE for that role.**

---

#### ROLE BLOCK: SRE

**SRE Vocabulary Declaration**

You are on-call. You adopted {topic} because the team moved to it. You knew the prior
system's failure modes cold; this one is still opaque. Something is breaking silently that
you would have caught in the old system. You are methodical but frustrated.

| Phase | Register for SRE | Example opening phrase |
|-------|-----------------|------------------------|
| Phase 1 | Setup/monitoring confusion: SRE deployed but observability broke | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| Phase 2 | Edge-case operational: intermittent, condition-specific failure | "I'm seeing [failure] only when [condition] — I cannot reproduce it consistently..." |
| Phase 3 | Reliability regression in production | "We've been running {topic} in production for [N] weeks and we just noticed [regression]..." |

**SRE Commitment Table** (fill before writing any SRE body)

| T-ID | Phase | Committed opening phrase |
|------|-------|--------------------------|
| T-__ | Phase ___ | "___" |
| ... | | |

**SRE Ticket Bodies**

```
## T-NN — {Title}
- Category: ... | Persona: SRE | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Register: {Phase row from SRE Vocabulary Declaration} | Committed: "{phrase}"

**Ticket body:**
[Begin with the committed phrase — expanded into a full opening sentence.
Use SRE register from the Phase row above. First person: "I", "my", "we".]
```

---

#### ROLE BLOCK: Support

**Support Vocabulary Declaration**

You've answered this same migration question multiple times this week. You know what the old
approach expected; {topic} does something different that users keep tripping over. You are
filing this ticket to get engineering to fix the root cause so you can stop answering it.

| Phase | Register for Support | Example opening phrase |
|-------|---------------------|------------------------|
| Phase 1 | Recurring-question frustration: same migration obstacle arriving repeatedly | "I keep seeing customers hit [obstacle] when they first [action] — I cannot find guidance on..." |
| Phase 2 | Pattern identification: repeat questions with identifiable root cause | "We're getting repeat questions about [X] and the pattern seems to be [Y]..." |
| Phase 3 | Escalation urgency: chronic failure at leadership visibility | "This is the [N]th escalation about [failure] this month — I need a permanent fix..." |

**Support Commitment Table** (fill before writing any Support body)

| T-ID | Phase | Committed opening phrase |
|------|-------|--------------------------|
| T-__ | Phase ___ | "___" |
| ... | | |

**Support Ticket Bodies**

```
## T-NN — {Title}
- Category: ... | Persona: Support | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Register: {Phase row from Support Vocabulary Declaration} | Committed: "{phrase}"

**Ticket body:**
[Begin with the committed phrase. Use Support register. First person.]
```

---

#### ROLE BLOCK: PM

**PM Vocabulary Declaration**

Adoption is below forecast. You cannot tell if it is a product problem or a communication
problem. You are filing this to request data.

| Phase | Register for PM | Example opening phrase |
|-------|----------------|------------------------|
| Phase 1 | Adoption metric concern: first-time activation below forecast | "First-time activation for {topic} is lower than projected — I want to understand what is blocking..." |
| Phase 2 | Funnel investigation: mid-adoption metric not improving | "The [metric] I projected is not improving at the rate expected — I need to investigate..." |
| Phase 3 | Late-stage attrition signal: post-onboarding drop-off | "I'm seeing users who completed onboarding dropping off at [stage]..." |

**PM Commitment Table** (fill before writing any PM body)

| T-ID | Phase | Committed opening phrase |
|------|-------|--------------------------|
| T-__ | Phase ___ | "___" |
| ... | | |

**PM Ticket Bodies**

```
## T-NN — {Title}
- Category: ... | Persona: PM | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Register: {Phase row from PM Vocabulary Declaration} | Committed: "{phrase}"

**Ticket body:**
[Begin with the committed phrase. Use PM register. First person.]
```

---

#### ROLE BLOCK: UX

**UX Vocabulary Declaration**

You are watching session recordings and seeing users stall at a specific point. The old
approach had a familiar affordance here; the new one does not. You know the friction point
by location; you need engineering to understand the root cause.

| Phase | Register for UX | Example opening phrase |
|-------|----------------|------------------------|
| Phase 1 | Session-observation friction: users stalling at an identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..." |
| Phase 2 | Advanced feature abandonment: identifiable drop-off on complex actions | "Session recordings show consistent abandonment when users attempt [advanced action]..." |
| Phase 3 | Long-term frustration with changed behavior | "Long-term users are filing feedback about [behavior change / reliability issue]..." |

**UX Commitment Table** (fill before writing any UX body)

| T-ID | Phase | Committed opening phrase |
|------|-------|--------------------------|
| T-__ | Phase ___ | "___" |
| ... | | |

**UX Ticket Bodies**

```
## T-NN — {Title}
- Category: ... | Persona: UX | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Register: {Phase row from UX Vocabulary Declaration} | Committed: "{phrase}"

**Ticket body:**
[Begin with the committed phrase. Use UX register. First person.]
```

---

#### ROLE BLOCK: C-xx

**C-xx Vocabulary Declaration**

You switched from [old approach in Step 1B] recently. Something surprised you — either
something that used to work stopped working, or something you expected to just work required
extra setup. You do not know if it is a bug or if you are doing it wrong.

| Phase | Register for C-xx | Example opening phrase |
|-------|------------------|------------------------|
| Phase 1 | Migration surprise: expected old-approach behavior not present | "I just switched from [old approach] and expected [X] but instead got [Y]..." |
| Phase 2 | Advanced usage failure: basics work, advanced scenario breaks | "I got the basics working but now [scenario] fails with [error or unexpected result]..." |
| Phase 3 | Sustained-usage concern: reliability or data issue over time | "I've been using {topic} for [N] months and I'm noticing [concern] that wasn't there initially..." |

**C-xx Commitment Table** (fill before writing any C-xx body)

| T-ID | Persona (C-NN) | Phase | Committed opening phrase |
|------|---------------|-------|--------------------------|
| T-__ | C-__ | Phase ___ | "___" |
| ... | | | |

Note: any single C-xx persona appears in at most 2 tickets.

**C-xx Ticket Bodies**

```
## T-NN — {Title}
- Category: ... | Persona: C-NN | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- Register: {Phase row from C-xx Vocabulary Declaration} | Committed: "{phrase}"

**Ticket body:**
[Begin with the committed phrase. Use C-xx register. First person.]
```

---

### STEP 6 — Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|
| ... | T-NN, T-NN | ... | Y/N | ... |

---

### STEP 6B — Resolution Paths

For every ticket that is high-volume OR P0/P1:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|
| T-NN | SRE / Support / PM / Eng | doc-gap / design-flaw / config-error / product-bug | self-serve / escalation / structural |

---

### STEP 7 — Gap Analysis

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it

**Migration friction sub-section** (include if >= 2 migration tickets):
Friction point | affected tickets | what would eliminate it

---

### STEP 8 — Verification

```
Phase distribution:
  Phase 1: target ___ / actual ___   MATCH / MISMATCH
  Phase 2: target ___ / actual ___   MATCH / MISMATCH
  Phase 3: target ___ / actual ___   MATCH / MISMATCH

Phase-severity calibration (C-13):
  Phase 1 tickets at P2/P3: ___ of ___   (required: >= 60%)   PASS / FAIL
  At least 1 Phase 3 ticket at P0/P1: Y / N   PASS / FAIL

Phase-anchored vocabulary (C-14):
  Phase 1 bodies beginning with discovery phrase: ___ of ___   (required: >= 3)   PASS / FAIL
  Phase 3 bodies beginning with operational phrase: ___ of ___   (required: >= 1)   PASS / FAIL

Per-role vocabulary declarations (C-17 contribution):
  Role blocks with vocabulary declaration present: ___ of 5 active roles   PASS / FAIL
  Each declaration has >= 2 distinct phase rows: Y / N   PASS / FAIL
  Phase 1 register differs between at least two roles (cross-check SRE vs C-xx): Y / N   PASS / FAIL

Per-role commitment sub-tables (C-16 contribution):
  Commitment sub-tables present in all active role blocks: Y / N   PASS / FAIL
  Bodies begin with committed phrase from sub-table (spot-check 3): Y / N   PASS / FAIL

Role-phase compound coverage (C-12):
  Roles with 3+ tickets: [list] — each spans 2+ phases: Y / N

Broken T-NN refs in gap entries: ___   (required: 0)
Resolution paths complete for all qualifying tickets: Y / N
```

---

## V-04 — Combination: V-01 + V-02 (Matrix-Derived Commitment Table + Full Manifest Architecture)

**Combination axis:** V-01 R4 (role-phase vocabulary matrix with matrix-derived commitment
table, cell ID traceability) stacked with V-02 R4 (vocabulary manifest as a named top-level
section, constraint manifest, verification manifest).

**Hypothesis:** V-01 satisfies C-16 + C-17 through the matrix-derived commitment table
mechanism: the matrix defines register (C-17), the commitment table draws from matrix cells
with explicit cell IDs (C-16), and each body opens with its committed phrase (C-16 verifiable,
C-17 traceable). V-02 elevates the vocabulary matrix to a named manifest, making C-17
satisfiable by structural form. V-04 combines both: the VOCABULARY MANIFEST is simultaneously
a named top-level manifest (V-02 structure) and the source vocabulary space for per-ticket
commitment phrases (V-01 mechanism). Commitment table rows reference manifest row IDs
(auditable by row lookup). The VERIFICATION MANIFEST adds C-16 and C-17 verification rows.
A scorer can check C-15, C-16, and C-17 by reading three named sections alone.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic}. Mark N/A for unused combinations.
This manifest is the vocabulary contract for the entire output.**

| Row ID | Role | Phase | Register description | Example template phrase |
|--------|------|-------|----------------------|-------------------------|
| VM-SRE-P1 | SRE | Phase 1 | Setup-oriented technical confusion: deployed but monitoring/alerting broke | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| VM-SRE-P2 | SRE | Phase 2 | Edge-case operational: intermittent condition-specific failure | "I'm seeing [failure] only when [condition] — I cannot reproduce it on demand..." |
| VM-SRE-P3 | SRE | Phase 3 | Reliability regression in production | "We've been running {topic} in production for [N] weeks and we just noticed [regression]..." |
| VM-Sup-P1 | Support | Phase 1 | Recurring-question frustration: same migration obstacle repeatedly | "I keep seeing customers hit [obstacle] when they first [action]..." |
| VM-Sup-P2 | Support | Phase 2 | Pattern identification: repeat questions pointing to root cause | "We're getting repeat questions about [X] and the pattern seems to be [Y]..." |
| VM-Sup-P3 | Support | Phase 3 | Escalation urgency: chronic failure at leadership threshold | "This is the [N]th escalation about [failure] this month..." |
| VM-PM-P1 | PM | Phase 1 | Adoption metric concern: activation below forecast | "First-time activation is lower than projected — I want to understand what is blocking..." |
| VM-PM-P2 | PM | Phase 2 | Funnel investigation: metric stalled mid-adoption | "The [metric] I projected is not improving — I need to investigate..." |
| VM-PM-P3 | PM | Phase 3 | Late-stage attrition: post-onboarding drop-off | "I'm seeing users who completed onboarding dropping off at [stage]..." |
| VM-UX-P1 | UX | Phase 1 | Session-observation friction: users stalling at identifiable location | "I'm watching session recordings and users consistently stall at [location]..." |
| VM-UX-P2 | UX | Phase 2 | Advanced feature abandonment: drop-off on complex action | "Session recordings show abandonment when users attempt [advanced action]..." |
| VM-UX-P3 | UX | Phase 3 | Long-term frustration: changed behavior or reliability | "Long-term users are filing feedback about [behavior change / reliability issue]..." |
| VM-Cxx-P1 | C-xx | Phase 1 | Migration surprise: expected old-approach behavior not present | "I just switched from [old approach] and expected [X] but instead got [Y]..." |
| VM-Cxx-P2 | C-xx | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks | "I got the basics working but now [scenario] fails with [error]..." |
| VM-Cxx-P3 | C-xx | Phase 3 | Sustained-usage concern: reliability or data issue over time | "I've been using {topic} for [N] months and I'm noticing [concern]..." |

Do not proceed until all rows are customized or marked N/A.

---

### CONSTRAINT MANIFEST

| Structural target | Required | Committed value |
|------------------|----------|----------------|
| Total tickets | 6 to 12 | ___ |
| Phase 1 tickets (day 0-30) | >= 3 | ___ |
| Phase 2 tickets (day 31-60) | >= 2 | ___ |
| Phase 3 tickets (day 61-90) | >= 1 | ___ |
| P0 ceiling | <= floor(total × 0.25) = ___ | ___ |
| High-volume ceiling | <= floor(total × 0.50) = ___ | ___ |
| Distinct named personas | >= 3 | ___ |
| SRE tickets | >= 2 | ___ |
| Support tickets | >= 2 | ___ |
| C-xx tickets | >= 2 (max 2 per C-xx) | ___ |
| Phase 1 bodies with discovery vocabulary (C-14) | >= 3 | ___ |
| Phase 3 bodies with operational vocabulary (C-14) | >= 1 | ___ |
| Tickets with VM row reference (C-16) | = total ticket count | ___ |

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

| Phase | Window | Severity norm | Volume norm | Body register |
|-------|--------|--------------|------------|--------------|
| Phase 1 | day 0-30 | P2/P3 | high/medium | Discovery/setup — VM-xxx-P1 rows |
| Phase 2 | day 31-60 | P1/P2 | medium | Integration/edge — VM-xxx-P2 rows |
| Phase 3 | day 61-90 | P0/P1 | low/medium | Operational/reliability — VM-xxx-P3 rows |

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

[Theme C if needed]
```

---

### STEP 4 — Role-Phase Cross-Matrix

| Role    | Phase 1 | Phase 2 | Phase 3 | Total | Theme(s) |
|---------|---------|---------|---------|-------|----------|
| SRE     | ___     | ___     | ___     | ___   | ___      |
| Support | ___     | ___     | ___     | ___   | ___      |
| PM      | ___     | ___     | ___     | ___   | ___      |
| UX      | ___     | ___     | ___     | ___   | ___      |
| C-xx    | ___     | ___     | ___     | ___   | ___      |

Constraint: Any role with 3+ tickets must span at least 2 phases.

---

### STEP 5 — Per-Ticket Vocabulary Commitment Table

**Fill before writing any body. Reference the VOCABULARY MANIFEST row ID for each ticket.
Expand the template phrase into a committed opening sentence — not verbatim.**

| T-ID | VM Row ID | Phase | Committed opening phrase |
|------|-----------|-------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| ... | | | |

Verification:
- All VM Row IDs reference non-N/A rows: Y / N
- Phase in row matches phase in VM Row ID: Y / N

---

### STEP 6 — PERFORMANCE MODE DECLARATION

**SRE:** On-call. Adopted {topic} under team mandate. Prior system's failure modes were
familiar; this one is opaque. Something is breaking silently. Methodical but frustrated.

**Support:** Has answered this migration question multiple times. Knows what old approach
expected. Filing to get a root cause fix.

**PM:** Adoption below forecast. Cannot distinguish product from communication problem.
Filing to request data.

**UX:** Watching session recordings. Users stall at a specific point. Knows friction location;
needs root cause.

**C-xx:** Switched from old approach recently. Surprised by the delta. Does not know if
bug or user error.

**Every body: first person. "I", "my", "we". Never third-person role references. Begin each
body with the committed phrase from STEP 5. Register must match the VM row.**

---

### STEP 7 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows: ___ / Personas: ___ / P0 count: ___ / High-vol count: ___
- Phase 1 ___ / Phase 2 ___ / Phase 3 ___
- CONSTRAINT MANIFEST targets: MATCH / MISMATCH
- Every ticket has STEP 5 commitment row: Y / N

---

### STEP 8 — Ticket Bodies (by theme, phase-sorted within each theme)

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- VM Row: {row ID from STEP 5} | Committed phrase: "{phrase from STEP 5}"

**Ticket body:**
[2-5 sentences. Begin with the committed phrase (expanded).
Register must match the VM row. First person: "I", "my", "we".
Where migration-relevant: reference what was expected from the old approach.]
```

---

### STEP 9 — Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? | Adoption cost |
|-------------|-----------------|------------|------------------|---------------|
| ... | T-NN, T-NN | ... | Y/N | ... |

---

### STEP 9B — Resolution Paths

For every ticket that is high-volume OR P0/P1:

| T-ID | Triage owner | Root cause category | Resolution type |
|------|-------------|---------------------|-----------------|
| T-NN | SRE / Support / PM / Eng | doc-gap / design-flaw / config-error / product-bug | self-serve / escalation / structural |

---

### STEP 10 — Gap Analysis

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it

**Migration friction sub-section** (include if >= 2 migration tickets):
Friction point | affected tickets | what would eliminate it

---

### VERIFICATION MANIFEST

| Structural target | Required | Actual | Status |
|------------------|----------|--------|--------|
| Total tickets | 6–12 | ___ | PASS / FAIL |
| Phase 1 tickets | >= 3 | ___ | PASS / FAIL |
| Phase 2 tickets | >= 2 | ___ | PASS / FAIL |
| Phase 3 tickets | >= 1 | ___ | PASS / FAIL |
| P0 tickets | <= ___ | ___ | PASS / FAIL |
| High-volume tickets | <= ___ | ___ | PASS / FAIL |
| Distinct named personas | >= 3 | ___ | PASS / FAIL |
| SRE tickets | >= 2 | ___ | PASS / FAIL |
| Support tickets | >= 2 | ___ | PASS / FAIL |
| C-xx tickets | >= 2 | ___ | PASS / FAIL |
| Roles with 3+ tickets spanning 2+ phases (C-12) | all: Y | Y / N | PASS / FAIL |
| Phase 1 tickets at P2/P3 (C-13) | >= 60% (___ of ___) | ___ of ___ | PASS / FAIL |
| Phase 3 tickets at P0/P1 (C-13) | >= 1 | ___ | PASS / FAIL |
| Phase 1 bodies with discovery vocabulary (C-14) | >= 3 | ___ | PASS / FAIL |
| Phase 3 bodies with operational vocabulary (C-14) | >= 1 | ___ | PASS / FAIL |
| Commitment table rows = total tickets (C-16) | = ___ | ___ | PASS / FAIL |
| Bodies beginning with committed phrase (C-16) | all | ___ of ___ | PASS / FAIL |
| VM non-N/A rows populated (C-17) | >= 4 | ___ | PASS / FAIL |
| VM distinct roles (C-17) | >= 2 | ___ | PASS / FAIL |
| VM distinct phases (C-17) | >= 2 | ___ | PASS / FAIL |
| Phase 1 cells show role differentiation (C-17) | >= 1 pair | Y / N | PASS / FAIL |
| Bodies traceable to VM rows (C-17) | all | Y / N | PASS / FAIL |
| CONSTRAINT MANIFEST present (C-15) | Y | Y / N | PASS / FAIL |
| VERIFICATION MANIFEST with numeric rows (C-15) | Y | Y / N | PASS / FAIL |
| Broken T-NN refs in gap entries (C-11) | 0 | ___ | PASS / FAIL |
| Resolution paths complete (C-10) | all qualifying | Y / N | PASS / FAIL |

If any row shows FAIL: revise before submitting.

---

## V-05 — Full Combination (All R3 + R4 Mechanisms — Composite 100 Candidate Under v4)

**Combination axis:** All mechanisms from R3 and R4 combined in a single prompt:
1. VOCABULARY MANIFEST (V-02/V-04 R4): role-phase matrix as named top-level manifest (C-17 by form)
2. CONSTRAINT MANIFEST + VERIFICATION MANIFEST (R3 V-02): pre-ticket declaration + post-ticket audit (C-15)
3. Per-ticket vocabulary commitment table referencing VM row IDs (V-01/V-04 R4): T-ID + phrase + VM row reference (C-16)
4. Character-embodiment PERFORMANCE MODE with migration backstory (R3 V-04/V-05): C-03
5. Dual mechanism in body instruction (R3 V-05): VM-row anchor (vocabulary) + role-phase character template (structure)

**Hypothesis:** Under v4, R3 V-05-class outputs score 97.8 — all 15 R3 criteria but not C-16
or C-17. V-05 R4 adds the VOCABULARY MANIFEST and matrix-derived commitment table to the
full R3 V-05 base. The resulting output satisfies all 17 criteria: C-01 through C-15 by R3
inheritance, C-16 by commitment table with body-opening enforcement, C-17 by vocabulary
manifest with distinct cells and header-line body traceability. A scorer checking C-16 reads
the commitment table then verifies body openings. A scorer checking C-17 reads the vocabulary
manifest, verifies >= 4 distinct cells, and spot-checks body openings against row registers.
Both checks are O(1) by section lookup.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### VOCABULARY MANIFEST

**Complete before generating any ticket. Customize for {topic} — replace bracketed placeholders
with feature-specific language. Mark N/A for unused combinations. This is the vocabulary
contract: every ticket body must be traceable to its assigned manifest row.**

| Row ID | Role | Phase | Register description | Example template phrase |
|--------|------|-------|----------------------|-------------------------|
| VM-SRE-P1 | SRE | Phase 1 | Setup-oriented technical confusion: monitoring/alerting gap after deployment | "I set up {topic} and now my [monitoring / alert / pipeline] is not [expected behavior]..." |
| VM-SRE-P2 | SRE | Phase 2 | Edge-case operational: intermittent condition-specific failure | "I'm seeing [failure] only when [condition] — I cannot reproduce it on demand..." |
| VM-SRE-P3 | SRE | Phase 3 | Reliability regression in production | "We've been running {topic} in production for [N] weeks and we just noticed [regression]..." |
| VM-Sup-P1 | Support | Phase 1 | Recurring-question frustration: same migration obstacle arriving repeatedly | "I keep seeing customers hit [obstacle] when they first [action] — I cannot find guidance on..." |
| VM-Sup-P2 | Support | Phase 2 | Pattern identification: repeat questions pointing to a root cause | "We're getting repeat questions about [X] and the pattern seems to be [Y]..." |
| VM-Sup-P3 | Support | Phase 3 | Escalation urgency: chronic failure at leadership visibility | "This is the [N]th escalation about [failure] this month — I need a permanent fix..." |
| VM-PM-P1 | PM | Phase 1 | Adoption metric concern: first-time activation below forecast | "First-time activation for {topic} is lower than projected — I want to understand what is blocking..." |
| VM-PM-P2 | PM | Phase 2 | Funnel investigation: mid-adoption metric stalled | "The [metric] I projected is not improving — I need to investigate whether [hypothesis]..." |
| VM-PM-P3 | PM | Phase 3 | Late-stage attrition signal: post-onboarding drop-off | "I'm seeing users who completed onboarding dropping off at [stage]..." |
| VM-UX-P1 | UX | Phase 1 | Session-observation friction: users stalling at identifiable UI location | "I'm watching session recordings and users consistently stall at [location]..." |
| VM-UX-P2 | UX | Phase 2 | Advanced feature abandonment: drop-off on complex action | "Session recordings show abandonment when users attempt [advanced action]..." |
| VM-UX-P3 | UX | Phase 3 | Long-term frustration with changed behavior or reliability | "Long-term users are filing feedback about [behavior change / reliability issue]..." |
| VM-Cxx-P1 | C-xx | Phase 1 | Migration surprise: expected old-approach behavior not present | "I just switched from [old approach] and expected [X] but instead got [Y]..." |
| VM-Cxx-P2 | C-xx | Phase 2 | Advanced usage failure: basics work, advanced scenario breaks | "I got the basics working but now [advanced scenario] fails with [error]..." |
| VM-Cxx-P3 | C-xx | Phase 3 | Sustained-usage concern: reliability or data issue surfacing over time | "I've been using {topic} for [N] months and I'm noticing [concern] that wasn't there initially..." |

Do not proceed until all rows are customized (or explicitly marked N/A).

---

### CONSTRAINT MANIFEST

**Complete before generating any ticket. Pre-generation structural commitment.**

| Structural target | Required | Committed value |
|------------------|----------|----------------|
| Total tickets | 6 to 12 | ___ |
| Phase 1 tickets (day 0-30) | >= 3 | ___ |
| Phase 2 tickets (day 31-60) | >= 2 | ___ |
| Phase 3 tickets (day 61-90) | >= 1 | ___ |
| P0 ceiling | <= floor(total × 0.25) = ___ | ___ |
| High-volume ceiling | <= floor(total × 0.50) = ___ | ___ |
| Distinct named personas | >= 3 | ___ |
| SRE tickets | >= 2 | ___ |
| Support tickets | >= 2 | ___ |
| C-xx tickets | >= 2 (max 2 per single C-xx) | ___ |
| Phase 1 bodies with discovery vocabulary (C-14) | >= 3 | ___ |
| Phase 3 bodies with operational vocabulary (C-14) | >= 1 | ___ |
| Tickets with VM row reference in commitment table (C-16) | = total ticket count | ___ |

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

| Phase | Window | Severity norm | Volume norm | Body register |
|-------|--------|--------------|------------|--------------|
| Phase 1 | day 0-30 | P2/P3 | high/medium | Discovery/setup — use VM-xxx-P1 register |
| Phase 2 | day 31-60 | P1/P2 | medium | Integration/edge — use VM-xxx-P2 register |
| Phase 3 | day 61-90 | P0/P1 | low/medium | Operational/reliability — use VM-xxx-P3 register |

Phase-severity inference rule: assign from the norm column. Override only if the specific
failure is unambiguously more or less severe than the phase norm.

---

### STEP 3 — Theme Declaration

Declare 2-3 named themes before generating any ticket:

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

Fill before generating any ticket body.

| Role    | Phase 1 | Phase 2 | Phase 3 | Total | Theme(s) |
|---------|---------|---------|---------|-------|----------|
| SRE     | ___     | ___     | ___     | ___   | ___      |
| Support | ___     | ___     | ___     | ___   | ___      |
| PM      | ___     | ___     | ___     | ___   | ___      |
| UX      | ___     | ___     | ___     | ___   | ___      |
| C-xx    | ___     | ___     | ___     | ___   | ___      |

Constraint 1: SRE >= 2, Support >= 2, PM >= 1, UX >= 1, C-xx >= 2
Constraint 2: Any role with 3+ tickets must span at least 2 phases (C-12)
Constraint 3: Any single C-xx persona in at most 2 tickets

---

### STEP 3B — Per-Ticket Vocabulary Commitment Table

**Fill before generating any ticket body. For each ticket: reference the VOCABULARY MANIFEST
row ID, derive the committed opening phrase from that row's template, and record it here.
The body MUST begin with its committed phrase (expanded into a full sentence — not verbatim).**

| T-ID | VM Row ID | Phase | Committed opening phrase |
|------|-----------|-------|--------------------------|
| T-01 | VM-___-P___ | Phase ___ | "___" |
| T-02 | VM-___-P___ | Phase ___ | "___" |
| T-03 | VM-___-P___ | Phase ___ | "___" |
| ... | | | |

Pre-flight check:
- All Phase 1 rows reference VM-xxx-P1 rows: Y / N
- All Phase 1 committed phrases use discovery/setup register: Y / N
- At least one Phase 3 row references a VM-xxx-P3 row: Y / N
- At least one Phase 3 phrase uses operational/reliability register: Y / N
- All VM Row IDs reference non-N/A VOCABULARY MANIFEST rows: Y / N

If any check is N: revise commitment table before continuing.

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
Register must match the VOCABULARY MANIFEST row. Where migration-relevant: reference what was
expected from the old approach.**

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
- Every STEP 3B row has a valid non-N/A VM Row ID: Y / N

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

**Generation order within each theme: Phase 1 tickets first, then Phase 2, then Phase 3.**

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)
- VM Row: {row ID from STEP 3B} | Committed phrase: "{phrase from STEP 3B}"

**Ticket body:**
[2-5 sentences.
OPENING: Begin with the committed phrase from STEP 3B — expand it into a full first sentence.
Do not copy verbatim.
REGISTER: Use the vocabulary register described in the VM Row. SRE bodies use
  technical/operational vocabulary. C-xx bodies reflect confusion or migration surprise.
  Support bodies reflect recurring-question frustration. Registers must differ between roles
  in the same phase.
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
| T-NN | SRE / Support / PM / Eng | doc-gap / design-flaw / config-error / product-bug | self-serve (doc fix) / escalation (eng fix) / structural (design change) |

All three fields required per qualifying ticket.

---

### STEP 8 — Gap Analysis

All entries require `Tickets: T-NN, T-NN` with identifiers matching the inventory above.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it (specific page or guide name)

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it (specific design decision)

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it (runbook, alert, or dashboard)

**Migration friction sub-section** (include if >= 2 migration tickets):
Friction point | affected tickets | what would eliminate it

---

### VERIFICATION MANIFEST

**Complete after gap analysis. A row showing FAIL requires revision before submission.**

| Structural target | Required | Actual | Status |
|------------------|----------|--------|--------|
| Total tickets | 6–12 | ___ | PASS / FAIL |
| Phase 1 tickets | >= 3 | ___ | PASS / FAIL |
| Phase 2 tickets | >= 2 | ___ | PASS / FAIL |
| Phase 3 tickets | >= 1 | ___ | PASS / FAIL |
| P0 tickets | <= ___ (floor(___ × 0.25)) | ___ | PASS / FAIL |
| High-volume tickets | <= ___ (floor(___ × 0.50)) | ___ | PASS / FAIL |
| Distinct named personas | >= 3 | ___ | PASS / FAIL |
| SRE tickets | >= 2 | ___ | PASS / FAIL |
| Support tickets | >= 2 | ___ | PASS / FAIL |
| C-xx tickets | >= 2 | ___ | PASS / FAIL |
| Roles with 3+ tickets spanning 2+ phases (C-12) | all: Y | Y / N | PASS / FAIL |
| Phase 1 tickets at P2/P3 (C-13) | >= 60% (>= ___ of ___) | ___ of ___ | PASS / FAIL |
| Phase 3 tickets at P0/P1 (C-13) | >= 1 | ___ | PASS / FAIL |
| Phase 1 bodies with discovery vocabulary (C-14) | >= 3 | ___ | PASS / FAIL |
| Phase 3 bodies with operational vocabulary (C-14) | >= 1 | ___ | PASS / FAIL |
| Commitment table rows = total ticket count (C-16) | = ___ | ___ | PASS / FAIL |
| Bodies beginning with committed phrase (C-16) | all (___ of ___) | ___ | PASS / FAIL |
| VM non-N/A rows populated (C-17) | >= 4 | ___ | PASS / FAIL |
| VM distinct roles (C-17) | >= 2 | ___ | PASS / FAIL |
| VM distinct phases (C-17) | >= 2 | ___ | PASS / FAIL |
| Phase 1 cells show role differentiation (C-17) | >= 1 pair differs | Y / N | PASS / FAIL |
| Ticket bodies traceable to VM rows via header lines (C-17) | all | Y / N | PASS / FAIL |
| CONSTRAINT MANIFEST present with 2+ structural targets (C-15) | Y | Y / N | PASS / FAIL |
| VERIFICATION MANIFEST with numeric actual vs required (C-15) | Y | Y / N | PASS / FAIL |
| Broken T-NN refs in gap entries (C-11) | 0 | ___ | PASS / FAIL |
| Resolution paths complete for qualifying tickets (C-10) | all qualifying | Y / N | PASS / FAIL |

---

## Mechanism Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-15 (constraint declaration) | PASS via STEP 1 declaration | PASS via CONSTRAINT MANIFEST | PASS via STEP 1 declaration | PASS via CONSTRAINT MANIFEST | PASS via CONSTRAINT MANIFEST |
| C-16 (per-ticket commitment table) | PASS via STEP 2B matrix-derived table | PASS via STEP 3 VM-referenced table | PASS via per-role commitment sub-tables | PASS via STEP 5 VM-referenced table | PASS via STEP 3B VM-referenced table |
| C-17 (role-phase vocabulary matrix) | PASS via STEP 2 matrix (2D, cell IDs) | PASS via VOCABULARY MANIFEST (named section) | PASS via per-role vocabulary declaration blocks | PASS via VOCABULARY MANIFEST | PASS via VOCABULARY MANIFEST |
| C-14 (phase-anchored body voice) | PASS via commitment pool enforcement | PASS via phase map register column | PASS via role vocabulary phase rows | PASS via VM register + commitment | PASS via VM register + PERFORMANCE MODE |
| C-16/C-17 integration | Cell ID column in commitment table | VM Row ID in commitment table | Per-role structure collapses vocabulary-to-body distance | VM Row ID + manifest form | VM Row ID + manifest form + PERFORMANCE MODE |
| C-16/C-17 scorer path | Read STEP 2 matrix + STEP 2B table | Read VOCABULARY MANIFEST + STEP 3 | Read role block vocab decl + sub-table | Read VOCABULARY MANIFEST + STEP 5 | Read VOCABULARY MANIFEST + STEP 3B |

**R4 composite 100 candidate:** V-05 — VOCABULARY MANIFEST (C-17 by form), CONSTRAINT
MANIFEST + VERIFICATION MANIFEST (C-15), per-ticket commitment table with VM row references
(C-16), character-embodiment PERFORMANCE MODE (C-03), dual-mechanism body instruction
(C-14 + C-16 + C-17). All 17 criteria satisfied by architectural structure, not by
instruction-following alone.
