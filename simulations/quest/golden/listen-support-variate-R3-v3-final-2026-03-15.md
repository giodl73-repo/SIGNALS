# listen-support — Variations, Round 3 (rubric v3 — 15 criteria)

**Date:** 2026-03-15
**Rubric target:** v3 (C-01 through C-15 — 15 criteria; aspirational tier denominator = 7)
**Baseline:** R2 V-05 (composite 96.0 — passes C-01 through C-13; C-14/C-15 not yet in rubric at time of R2)
**R3 objective:** Close the two aspirational gaps that R2 V-05 cannot yet be scored against:
  - **C-14** — Phase-anchored body voice: 3+ early-phase bodies contain discovery/onboarding vocabulary; 1+ late-phase body contains operational/reliability vocabulary — verified in body text, not in metadata labels.
  - **C-15** — Pre-generation constraint declaration: pre-ticket block naming 2+ structural targets; post-ticket verification block with at least one numeric actual vs. required comparison — both visible in output.

---

## Fixed Changes Applied to All Variations

All five R3 variations inherit the full R2 V-05 foundation. These are not the differentiating axis.

| Component | R2 V-05 source | R3 status |
|-----------|---------------|-----------|
| Phase distribution target (STEP 1) | Declared before tickets | Retained |
| Status quo / migration analysis (STEP 1B) | Named prior approach | Retained |
| Phase map with body character (STEP 2) | Phase → severity norm, volume norm, character one-liner | Retained |
| Phase body anchor templates (STEP 2B) | Role × phase sentence scaffolds | Extended in V-01, V-03 |
| Theme declaration (STEP 3) | 2-3 themes before any ticket | Retained |
| Role-phase cross-matrix (STEP 3A) | Fill before any body; 3 constraints | Retained |
| Character-embodiment PERFORMANCE MODE (STEP 4) | Persona inhabitation + migration backstory | Retained |
| Ticket inventory table + TABLE CHECK (STEP 5) | Row-per-ticket with gate checks | Retained |
| Ticket bodies by theme/phase (STEP 6) | Body format anchored to Step 2B template | Retained |
| Cross-ticket patterns (STEP 7) | Pattern table | Retained |
| Resolution paths (STEP 7B) | High-vol / P0/P1 resolution table (C-10) | Retained |
| Gap analysis with T-NN refs (STEP 8) | Three sections + migration sub-section | Retained |
| Dual-pass verification (STEP 9) | Pass 1 coverage trace + Pass 2 structural checks | Extended in V-02, V-05 |

---

## R3 Variation Axes

R1 explored: role sequence, output format, lifecycle emphasis.
R2 explored: phrasing register, inertia framing, theme-first generation.
R3 re-engages three axes at a new level of specificity, each directly targeting a specific new criterion:

| Axis | Single-axis variation | New angle (vs prior rounds) | Target criterion |
|------|-----------------------|-----------------------------|-----------------|
| Lifecycle emphasis | V-01 | Vocabulary pre-commitment: per-ticket phrase selection from phase-specific pools recorded before body writing | C-14 |
| Output format | V-02 | Manifest table format: CONSTRAINT MANIFEST (pre-ticket) + VERIFICATION MANIFEST (post-ticket) with Required / Actual / Status columns | C-15 |
| Role sequence | V-03 | Role-phase vocabulary matrix: each cell declares exact register for that role × phase combination; generation order is SRE-first | C-14 + C-12 |

Combined: V-04 stacks V-01 + V-02. V-05 stacks full R2 V-05 + V-01 + V-02 (golden candidate, composite 100).

---

## V-01 — Single Axis: Lifecycle Emphasis (Vocabulary Pre-Commitment Per Ticket)

**Axis:** Lifecycle emphasis — STEP 2B expanded from anchor-template-to-expand into a per-ticket vocabulary commitment table. Before writing any body, the model selects a specific opening phrase from a phase-gated vocabulary pool and records it. The body must begin with the committed phrase.

**Hypothesis:** R2 V-05 STEP 2B gave sentence templates as scaffolds. The generation-time failure C-14 is trying to catch is not that bodies are generic — R2 V-05 bodies were non-generic — but that they may use the right severity label without using the right phase register in the body text. A per-ticket vocabulary commitment step makes the phase-contextual language visible before the body is written. The model cannot generate a Phase 1 body without first writing down a discovery/onboarding opener; it cannot complete a Phase 3 ticket without first writing down an operational opener. C-14 is satisfied by construction: the committed phrase is the body evidence.

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
```

---

### STEP 1B — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 — Phase Map Table

| Phase | Window | Severity norm | Volume norm | Support character |
|-------|--------|--------------|------------|------------------|
| Phase 1 | day 0-30 | P2/P3 | high/medium | Setup confusion, first-time activation, docs mismatch |
| Phase 2 | day 31-60 | P1/P2 | medium | Edge cases, integration surprises, unexpected behavior |
| Phase 3 | day 61-90 | P0/P1 | low/medium | Operational failures, SLO impact, reliability regressions |

Phase-severity inference rule: assign from the norm column. Override only if the specific failure is unambiguously more or less severe than the phase norm.

---

### STEP 2B — Vocabulary Pre-Commitment

**Before writing any ticket body: select an opening phrase for each ticket from the vocabulary pools. Record selections in the commitment table. Begin each body with its committed phrase — expand it, do not copy verbatim.**

**Phase 1 vocabulary pool (discovery/onboarding — required for all Phase 1 tickets):**
- "I'm trying to set up {topic} for the first time and..."
- "I can't figure out how to configure..."
- "Just started using {topic} and I don't see any option to..."
- "I followed the getting started guide but..."
- "We're onboarding our team to {topic} and ran into..."
- "This is my first time using this feature and..."
- "I don't understand what the setup step is asking me to do when..."

**Phase 3 vocabulary pool (operational/reliability — required for at least 1 Phase 3 ticket):**
- "We've been running {topic} in production for [N] weeks and we just saw..."
- "Something changed recently — this used to work and now..."
- "Our on-call was paged because..."
- "We're seeing elevated error rates in..."
- "This is causing a production incident where..."
- "Our SLO is at risk because..."
- "I need to consider rolling this back because..."

**Phase 2:** No vocabulary constraint — use language natural to the persona and scenario.

**Vocabulary commitment table (fill before Step 3):**

| T-ID | Phase | Committed opening phrase |
|------|-------|-------------------------|
| T-01 | Phase ___ | "___" |
| T-02 | Phase ___ | "___" |
| T-03 | Phase ___ | "___" |
| ... | | |

Pre-flight check:
- Phase 1 rows all use discovery/onboarding vocabulary: Y / N
- At least one Phase 3 row uses operational/reliability vocabulary: Y / N

If either check is N: revise commitment table before continuing.

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

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior system's failure modes cold; this one is still opaque to you. Something is now breaking silently that you would have caught immediately in the old system. You are methodical but frustrated.

**Support:** You've answered this same migration question multiple times this week. You know what the old approach expected; {topic} does something different that users keep tripping over. You are filing this ticket to get engineering to fix the root cause so you can stop answering it.

**PM:** Adoption is below forecast. You cannot tell if it is a product problem or a communication problem. You are filing this to request data.

**UX:** You are watching session recordings and seeing users stall at a specific point. The old approach had a familiar affordance here; the new one does not. You know the friction point by location; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach in Step 1B] recently. Something surprised you — either something that used to work stopped working, or something you expected to just work required extra setup. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer". Begin each body with the phrase committed in STEP 2B. Where migration-relevant: reference what was expected from the old approach.**

---

### STEP 5 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK — verify all before proceeding:
- Total rows: ___ (required: >= 6 and <= 12)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= 25% of total, round down)
- High-volume count: ___ (required: <= 50% of total, round down)
- Theme counts match Step 3 declarations: MATCH / MISMATCH
- Phase distribution matches Step 1: MATCH / MISMATCH
- All Phase 1 tickets have committed discovery phrase in STEP 2B table: Y / N
- At least 1 Phase 3 ticket has committed operational phrase in STEP 2B table: Y / N

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[2-5 sentences. Begin with the phrase committed in STEP 2B. Embody the persona from Step 4.
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
|------|-------------|--------------------|-----------------:|
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

Broken T-NN refs in gap entries: ___   (required: 0)
Resolution paths complete for all qualifying tickets: Y / N
```

If any check fails: revise before submitting.

---

## V-02 — Single Axis: Output Format (Constraint Manifest + Verification Manifest Tables)

**Axis:** Output format — replace scattered constraint declarations across STEP 1, STEP 3A, and STEP 5 TABLE CHECK with a single CONSTRAINT MANIFEST table at the very top of the output; replace STEP 9 Pass 2 fill-in-the-blank lines with a VERIFICATION MANIFEST table at the bottom that has Required / Actual / Status columns for every structural property.

**Hypothesis:** R2 V-05 declares constraints at four points (STEP 1 target lines, STEP 3A matrix, STEP 5 TABLE CHECK, STEP 9 Pass 2 lines) and verifies them in-line. C-15 requires a single visible pre-ticket block naming 2+ structural targets and a single visible post-ticket block with at least one numeric comparison. The manifest table format satisfies C-15 by form: the CONSTRAINT MANIFEST cannot be mistaken for anything other than a pre-ticket declaration, and the VERIFICATION MANIFEST cannot be produced without completing numeric actual vs. required comparisons for every row. An output generated from this prompt cannot satisfy constraints silently — the two manifest tables are the output's most visible structural landmarks.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### CONSTRAINT MANIFEST

**Complete this table before generating any ticket. This is your pre-generation commitment.**

| Structural target | Required | Your committed value |
|------------------|----------|---------------------|
| Total tickets | 6 to 12 | ___ |
| Phase 1 tickets (day 0-30) | >= 3 | ___ |
| Phase 2 tickets (day 31-60) | >= 2 | ___ |
| Phase 3 tickets (day 61-90) | >= 1 | ___ |
| P0 ticket ceiling | <= floor(total × 0.25) = ___ | ___ |
| High-volume ticket ceiling | <= floor(total × 0.50) = ___ | ___ |
| Distinct named personas | >= 3 | ___ |
| SRE tickets | >= 2 | ___ |
| Support tickets | >= 2 | ___ |
| C-xx tickets | >= 2 (max 2 per single C-xx) | ___ |
| Phase 1 bodies with discovery/onboarding vocabulary | >= 3 | ___ |
| Phase 3 bodies with operational/reliability vocabulary | >= 1 | ___ |

Do not proceed to STEP 1 until this manifest is complete.

---

### STEP 1 — Phase Map Table

| Phase | Window | Severity norm | Volume norm | Body register |
|-------|--------|--------------|------------|--------------|
| Phase 1 | day 0-30 | P2/P3 | high/medium | Discovery: "I'm trying to set up", "I can't find", "just started using", "first time" |
| Phase 2 | day 31-60 | P1/P2 | medium | Integration: "I got past setup but now", "I'm seeing an issue when", "edge case" |
| Phase 3 | day 61-90 | P0/P1 | low/medium | Operational: "we've been running in prod", "our on-call was paged", "this used to work", "SLO" |

---

### STEP 1B — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 — Theme Declaration

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

[Theme C if needed — same format]
```

Sum of counts = CONSTRAINT MANIFEST total. Each theme has a distinct underlying failure.

---

### STEP 3 — Role-Phase Cross-Matrix

| Role    | Phase 1 | Phase 2 | Phase 3 | Total | Theme(s) |
|---------|---------|---------|---------|-------|----------|
| SRE     | ___     | ___     | ___     | ___   | ___      |
| Support | ___     | ___     | ___     | ___   | ___      |
| PM      | ___     | ___     | ___     | ___   | ___      |
| UX      | ___     | ___     | ___     | ___   | ___      |
| C-xx    | ___     | ___     | ___     | ___   | ___      |

Constraint: Any role with 3+ tickets must span at least 2 phases.

---

### STEP 4 — PERFORMANCE MODE DECLARATION (character-embodiment + migration context)

**You are about to become each persona. They know what they migrated from.**

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior system's failure modes cold; this one is still opaque to you. Something is now breaking silently. You are methodical but frustrated.

**Support:** You've answered this same migration question multiple times. You know what the old approach expected; {topic} does something different. You are filing this to get engineering to fix the root cause.

**PM:** Adoption is below forecast. You cannot tell if it is a product or communication problem. You are filing this to request data.

**UX:** You are watching session recordings. Users stall at a specific point. You know the friction point; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach in Step 1B] recently. Something surprised you. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer". Body register must match the phase map in STEP 1. Where migration-relevant: reference what was expected from the old approach.**

---

### STEP 5 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows: ___ (required: matches CONSTRAINT MANIFEST committed value)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= MANIFEST ceiling)
- High-volume count: ___ (required: <= MANIFEST ceiling)
- Phase distribution: Phase 1 ___ / Phase 2 ___ / Phase 3 ___ (required: matches MANIFEST)

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

```
### Theme A — {theme name}
*Underlying failure: {from Step 2}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[2-5 sentences. First person — "I", "my", "we".
Body register must match phase (STEP 1 body register column):
  Phase 1: discovery/onboarding vocabulary required
  Phase 3: operational/reliability vocabulary required
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
|------|-------------|--------------------|-----------------:|
| T-NN | SRE / Support / PM / Eng | doc-gap / design-flaw / config-error / product-bug | self-serve / escalation / structural |

---

### STEP 8 — Gap Analysis

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

**Complete after gap analysis. Each row compares CONSTRAINT MANIFEST commitment to actual output.**

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
| Roles with 3+ tickets spanning 2+ phases | all: Y / N | Y / N | PASS / FAIL |
| Phase 1 tickets at P2/P3 | >= 60% (>= ___ of ___) | ___ of ___ | PASS / FAIL |
| Phase 3 tickets at P0/P1 | >= 1 | ___ | PASS / FAIL |
| Phase 1 bodies with discovery/onboarding vocab | >= 3 | ___ | PASS / FAIL |
| Phase 3 bodies with operational/reliability vocab | >= 1 | ___ | PASS / FAIL |
| Broken T-NN refs in gap entries | 0 | ___ | PASS / FAIL |
| Resolution paths for qualifying tickets | complete: Y / N | Y / N | PASS / FAIL |

If any row shows FAIL: revise before submitting.

---

## V-03 — Single Axis: Role Sequence (Role-Phase Vocabulary Matrix)

**Axis:** Role sequence — tickets generated in strict role order (SRE → Support → PM → UX → C-xx); generation preceded by a role-phase vocabulary matrix where each cell declares the exact vocabulary register for that role at that phase, customized to {topic} before any body is written.

**Hypothesis:** R1 V-01 used role sequence to improve severity distribution. R2 V-01 used character-embodiment to suppress third-person drift. V-03 adds vocabulary targeting: by declaring the register for each role × phase cell in a matrix before generation, the model has a specific opening committed before writing each body. A SRE/Phase-1 body has a committed "discovery-from-SRE-perspective" opener; a SRE/Phase-3 body has a committed "operational-from-SRE-perspective" opener. The matrix is finer-grained than a shared phase pool (V-01) because it accounts for the difference between "I'm trying to set up" (end-user discovery) and "I set up {topic} and my monitoring is broken" (SRE discovery) — both are Phase 1, but different roles surface C-14-qualifying language differently.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### STEP 1 — Constraint Declaration

Fill before generating any ticket:

```
Total tickets:          ___ (required: >= 6 and <= 12)
Phase 1 target (0-30):  ___   (required: >= 3)
Phase 2 target (31-60): ___   (required: >= 2)
Phase 3 target (61-90): ___   (required: >= 1)
P0 ceiling:             ___ = floor(total × 0.25)
High-volume ceiling:    ___ = floor(total × 0.50)
Distinct named personas: >= 3
```

---

### STEP 1B — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction: ___
```

---

### STEP 2 — Role-Phase Vocabulary Matrix

**Customize each cell for {topic} before generating any ticket. Replace bracketed placeholders with feature-specific language. Enter "N/A" if that role produces no tickets in that phase.**

Every ticket body must begin with language from its role-phase cell. Expand the template into a full sentence — do not copy verbatim.

| Role    | Phase 1 (discovery/setup) | Phase 2 (integration/edge) | Phase 3 (operational/reliability) |
|---------|--------------------------|-----------------------------|-----------------------------------|
| SRE | "I set up {topic} and now my [monitoring/alert/pipeline] is not..." | "I'm seeing [failure] only when [edge condition]..." | "We've been running {topic} in production for [N] weeks and we just noticed..." |
| Support | "I keep seeing customers hit [X] when they first try to [Y] and can't find..." | "We're getting repeat questions about [X] — the pattern seems to be..." | "This is the third time this month someone has escalated [X] — I need a root cause..." |
| PM | "First-time activation is lower than expected — I want to understand what's blocking..." | "I need to investigate why [metric] is not improving at the rate we projected..." | "We're seeing a pattern in late-stage adoption where users are dropping off at [X]..." |
| UX | "I'm seeing users stall at [specific location] in the UI — I can't find guidance on why..." | "Session recordings show a consistent drop-off when users attempt [advanced feature]..." | "Long-term users are expressing frustration with [reliability issue / changed behavior]..." |
| C-xx | "I just switched from [old approach] and expected [X] but instead got [Y]..." | "I got the basics working but now [advanced scenario] is failing with [error message]..." | "I've been using {topic} for [N] months and I've noticed [data/reliability concern]..." |

**Role generation order: SRE first, then Support, then PM, then UX, then C-xx.**
Minimum per role: SRE >= 2, Support >= 2, PM >= 1, UX >= 1, C-xx >= 2.

---

### STEP 3 — Role-Phase Cross-Matrix

| Role    | Phase 1 | Phase 2 | Phase 3 | Total |
|---------|---------|---------|---------|-------|
| SRE     | ___     | ___     | ___     | ___   |
| Support | ___     | ___     | ___     | ___   |
| PM      | ___     | ___     | ___     | ___   |
| UX      | ___     | ___     | ___     | ___   |
| C-xx    | ___     | ___     | ___     | ___   |

Constraint: Any role with 3+ tickets must span at least 2 phases.

---

### STEP 4 — PERFORMANCE MODE DECLARATION (character-embodiment)

**Before writing any body, become the persona.**

**SRE:** You're on-call. You knew the old system's failure modes cold. This one is opaque to you. Something is breaking silently. Methodical but frustrated.

**Support:** You've answered this same question multiple times. You know what users expected from the old approach. You are direct and tired of not having a root-cause fix.

**PM:** Adoption is below forecast. You write concisely; you are diagnosing, not complaining.

**UX:** You have session evidence of where users stall. You know the location; you need engineering to know the root cause.

**C-xx:** You switched from the old approach. Something surprised you. You do not know if it is you or the product.

**Every sentence first person. "I", "my", "we". No third-person role references. Begin each body with vocabulary from the STEP 2 matrix cell for this role-phase combination.**

---

### STEP 5 — Ticket Inventory Table

**Generate SRE tickets first, then Support, then PM, then UX, then C-xx.**

| T-ID | Title | Category | Persona | Volume | Severity | Phase |
|------|-------|----------|---------|--------|----------|-------|
| T-01 | ... | ... | SRE | ... | ... | ... |
| ... | | | | | | |

TABLE CHECK:
- Total rows: ___ (required: matches Step 1 total)
- P0 count: ___ (required: <= Step 1 ceiling)
- High-volume count: ___ (required: <= Step 1 ceiling)
- Distinct personas: ___ (required: >= 3)
- Phase distribution: Phase 1 ___ / Phase 2 ___ / Phase 3 ___ (required: matches Step 1 targets)

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (role order: SRE → Support → PM → UX → C-xx; ascending T-ID within each role)

```
### SRE Tickets

## T-NN — {Title}
- Category: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[Begin with vocabulary from STEP 2 matrix cell for SRE at this phase.
2-5 sentences. First person. SRE register: monitoring, operational, reliability language.]

### Support Tickets
[same format — begin with Support vocabulary from STEP 2 matrix for this phase]

### PM Tickets
[same format]

### UX Tickets
[same format]

### Customer Persona Tickets
[same format — begin with C-xx vocabulary from STEP 2 matrix for this phase]
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
|------|-------------|--------------------|-----------------:|
| T-NN | SRE / Support / PM / Eng | doc-gap / design-flaw / config-error / product-bug | self-serve / escalation / structural |

---

### STEP 8 — Gap Analysis

All entries require `Tickets: T-NN, T-NN`.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it

---

### STEP 9 — Dual-Pass Verification

**Pass 1:**
- C-01: ... | C-02: ... | C-03: ... | C-04: ... | C-05: ...

**Pass 2:**
```
Phase distribution: Phase 1 declared ___ / actual ___ | Phase 2 declared ___ / actual ___ | Phase 3 declared ___ / actual ___
P0 count: ceiling ___ / actual ___   PASS / FAIL
High-vol count: ceiling ___ / actual ___   PASS / FAIL
Roles with 3+ tickets spanning 2+ phases: [list]   PASS / FAIL
Phase 1 tickets at P2/P3: ___ of ___ (required: >= 60%)   PASS / FAIL
Phase 3 with P0/P1: ___ (required: >= 1)   PASS / FAIL
Phase 1 bodies with discovery/onboarding vocab: ___ of ___ (required: >= 3)   PASS / FAIL
Phase 3 bodies with operational/reliability vocab: ___ of ___ (required: >= 1)   PASS / FAIL
Broken T-NN refs in gap entries: ___ (required: 0)
Resolution paths for qualifying tickets: Y / N
```

---

## V-04 — Combined: Lifecycle Vocabulary Pre-Commitment + Constraint Manifest Format

**Axis combination:** V-01 (vocabulary pre-commitment: per-ticket phrase selection from phase-gated pools recorded before body writing) + V-02 (manifest table format: CONSTRAINT MANIFEST pre-ticket + VERIFICATION MANIFEST post-ticket with Required/Actual/Status columns)

**Hypothesis:** V-01 and V-02 target C-14 and C-15 through orthogonal mechanisms with no interaction cost. V-01 forces vocabulary selection at the ticket level (C-14 evidence is in the committed phrase, which the body must begin with); V-02 forces constraint declaration and verification into table form (C-15 is satisfied by form — the two manifest tables are structural landmarks that cannot be skipped). Combined, the output has both: every Phase 1 body carries a committed discovery phrase, every Phase 3 body carries a committed operational phrase, and the CONSTRAINT MANIFEST / VERIFICATION MANIFEST pair is unambiguously the pre/post constraint evidence C-15 requires. Neither mechanism requires the other to work, but they compound: the vocabulary commitment table provides additional numeric evidence for the C-14 row in the VERIFICATION MANIFEST.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### CONSTRAINT MANIFEST

**Complete before generating any ticket.**

| Structural target | Required | Your committed value |
|------------------|----------|---------------------|
| Total tickets | 6 to 12 | ___ |
| Phase 1 tickets (day 0-30) | >= 3 | ___ |
| Phase 2 tickets (day 31-60) | >= 2 | ___ |
| Phase 3 tickets (day 61-90) | >= 1 | ___ |
| P0 ticket ceiling | <= floor(total × 0.25) = ___ | ___ |
| High-volume ticket ceiling | <= floor(total × 0.50) = ___ | ___ |
| Distinct named personas | >= 3 | ___ |
| SRE tickets | >= 2 | ___ |
| Support tickets | >= 2 | ___ |
| C-xx tickets | >= 2 (max 2 per single C-xx) | ___ |
| Phase 1 bodies with discovery/onboarding vocabulary | >= 3 | ___ |
| Phase 3 bodies with operational/reliability vocabulary | >= 1 | ___ |

---

### STEP 1 — Phase Map Table

| Phase | Window | Severity norm | Volume norm | Body register |
|-------|--------|--------------|------------|--------------|
| Phase 1 | day 0-30 | P2/P3 | high/medium | Discovery: "I'm trying to set up", "just started using", "first time", "I can't find" |
| Phase 2 | day 31-60 | P1/P2 | medium | Integration: "I got past setup but", "I'm seeing an issue when", "edge case" |
| Phase 3 | day 61-90 | P0/P1 | low/medium | Operational: "we've been running in prod", "our on-call was paged", "this used to work", "SLO" |

---

### STEP 1B — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2B — Vocabulary Pre-Commitment

Before writing any ticket body, select and record an opening phrase for each ticket.

**Phase 1 pool (discovery/onboarding — required for all Phase 1 tickets):**
- "I'm trying to set up {topic} for the first time and..."
- "I can't figure out how to configure..."
- "Just started using {topic} and I don't see any option to..."
- "I followed the getting started guide but..."
- "We're onboarding our team to {topic} and ran into..."
- "This is my first time using this feature and..."

**Phase 3 pool (operational/reliability — required for at least 1 Phase 3 ticket):**
- "We've been running {topic} in production for [N] weeks and we just saw..."
- "Something changed recently — this used to work and now..."
- "Our on-call was paged because..."
- "We're seeing elevated error rates in..."
- "This is causing a production incident where..."
- "Our SLO is at risk because..."

**Vocabulary commitment table:**

| T-ID | Phase | Committed opening phrase |
|------|-------|-------------------------|
| T-01 | Phase ___ | "___" |
| ... | | |

Pre-flight: Phase 1 rows all use discovery vocabulary: Y / N | At least 1 Phase 3 row uses operational vocabulary: Y / N

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

Sum of counts = CONSTRAINT MANIFEST total. Each theme has a distinct underlying failure.

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

### STEP 4 — PERFORMANCE MODE DECLARATION (character-embodiment + migration context)

**You are about to become each persona. They know what they migrated from.**

**SRE:** On-call. Adopted {topic} because the team moved to it. Prior system's failure modes were familiar; this one is opaque. Something is breaking silently. Methodical but frustrated.

**Support:** Same migration question answered multiple times. Old approach was familiar; {topic} behaves differently. Filing to get engineering to fix root cause.

**PM:** Adoption below forecast. Filing to request data to diagnose cause.

**UX:** Session recordings show users stalling. Knows the friction point; needs engineering to know too.

**C-xx:** Switched from old approach. Something surprised them. Does not know if it is a bug or user error.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer". Begin each body with the phrase committed in STEP 2B. Where migration-relevant: reference what was expected from the old approach.**

---

### STEP 5 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows: ___ (required: matches CONSTRAINT MANIFEST)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= MANIFEST ceiling)
- High-volume count: ___ (required: <= MANIFEST ceiling)
- All Phase 1 tickets have committed discovery phrase: Y / N
- At least 1 Phase 3 ticket has committed operational phrase: Y / N

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted, ascending T-ID)

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[2-5 sentences. Begin with committed phrase from STEP 2B. First person only.
Phase 1: discovery vocabulary. Phase 3: operational vocabulary.
Where migration-relevant: reference old approach from Step 1B.]
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
|------|-------------|--------------------|-----------------:|
| T-NN | SRE / Support / PM / Eng | doc-gap / design-flaw / config-error / product-bug | self-serve / escalation / structural |

---

### STEP 8 — Gap Analysis

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it

**Migration friction sub-section** (if >= 2 migration tickets):
Friction point | affected tickets | what would eliminate it

---

### VERIFICATION MANIFEST

**Complete after gap analysis.**

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
| Roles with 3+ tickets spanning 2+ phases | all: Y / N | Y / N | PASS / FAIL |
| Phase 1 tickets at P2/P3 | >= 60% (>= ___ of ___) | ___ of ___ | PASS / FAIL |
| Phase 3 tickets at P0/P1 | >= 1 | ___ | PASS / FAIL |
| Phase 1 bodies with discovery/onboarding vocab | >= 3 | ___ | PASS / FAIL |
| Phase 3 bodies with operational/reliability vocab | >= 1 | ___ | PASS / FAIL |
| Broken T-NN refs in gap entries | 0 | ___ | PASS / FAIL |
| Resolution paths for qualifying tickets | complete: Y / N | Y / N | PASS / FAIL |

If any row shows FAIL: revise before submitting.

---

## V-05 — Full Synthesis: R2 V-05 + Vocabulary Pre-Commitment + Manifest Tables

**Axis combination:** Full R2 V-05 structure (all five R2 axes: phase-first, role-phase matrix, character-embodiment, inertia framing, theme-first + STEP 7B resolution paths) extended with V-01 (per-ticket vocabulary pre-commitment table in STEP 2B) and V-02 (CONSTRAINT MANIFEST pre-ticket + VERIFICATION MANIFEST post-ticket). This is the golden candidate for composite 100.

**Hypothesis:** R2 V-05 scored 96.0 by passing C-01 through C-13. C-14 and C-15 were not scoreable at time of R2. With both now defined:
- C-14 is closed by per-ticket vocabulary pre-commitment: the committed phrase is in the body text, not a metadata label. 3+ Phase 1 committed phrases are from the discovery pool; 1+ Phase 3 committed phrase is from the operational pool. Pass by construction.
- C-15 is closed by manifest table format: CONSTRAINT MANIFEST names 12 structural targets before any ticket; VERIFICATION MANIFEST has 17 rows each with Required / Actual / Status numeric comparisons after all content. Both blocks are unavoidable — they are the first and last visible sections of the output. Pass by form.
- No existing passes are lost: the vocabulary pre-commitment integrates naturally with STEP 2B anchor templates (commitment table feeds body generation); the manifest tables subsume STEP 1 declaration and STEP 9 Pass 2 without removing either.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### CONSTRAINT MANIFEST

**Complete before generating any ticket. This is your pre-generation commitment.**

| Structural target | Required | Your committed value |
|------------------|----------|---------------------|
| Total tickets | 6 to 12 | ___ |
| Phase 1 tickets (day 0-30) | >= 3 | ___ |
| Phase 2 tickets (day 31-60) | >= 2 | ___ |
| Phase 3 tickets (day 61-90) | >= 1 | ___ |
| P0 ticket ceiling | <= floor(total × 0.25) = ___ | ___ |
| High-volume ticket ceiling | <= floor(total × 0.50) = ___ | ___ |
| Distinct named personas | >= 3 | ___ |
| SRE tickets | >= 2 | ___ |
| Support tickets | >= 2 | ___ |
| C-xx tickets | >= 2 (max 2 per single C-xx) | ___ |
| Phase 1 bodies with discovery/onboarding vocabulary | >= 3 | ___ |
| Phase 3 bodies with operational/reliability vocabulary | >= 1 | ___ |

Do not proceed to STEP 1 until this manifest is complete.

---

### STEP 1 — Phase Distribution Target

```
Phase 1 (day 0-30):   ___ tickets   [must match MANIFEST commitment]
Phase 2 (day 31-60):  ___ tickets
Phase 3 (day 61-90):  ___ tickets
Total:                ___ tickets
```

---

### STEP 1B — Status Quo Analysis

```
Current approach users are replacing: ___
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
```

---

### STEP 2 — Phase Map Table

| Phase | Window | Migration context | Severity norm | Volume norm | Body character |
|-------|--------|------------------|--------------|------------|----------------|
| Phase 1 | day 0-30 | Habit disruption | P2/P3 | high/medium | "I tried the old way and hit a wall" |
| Phase 2 | day 31-60 | Hybrid / edge cases | P1/P2 | medium | "I got past setup but now something unexpected" |
| Phase 3 | day 61-90 | Committed or churned | P0/P1 | low/medium | "We've been running this for weeks and now something serious broke" |

**Phase-severity inference rule:** Assign from norm column. Explicit override only if the specific failure is unambiguously more or less severe than the phase norm.

---

### STEP 2B — Phase Vocabulary Pre-Commitment

Two inputs for every ticket: (1) the anchor template from the role-phase table below as sentence scaffold; (2) a committed opening phrase from the phase vocabulary pool, recorded before writing the body. Begin each body with the committed phrase.

**Role-phase anchor templates (scaffold — expand, do not copy verbatim):**

| Phase | SRE anchor | Support anchor | C-xx anchor |
|-------|-----------|---------------|-------------|
| Phase 1 | "I set up {topic} and now my [monitoring/alert/pipeline] is..." | "I keep seeing [X] when customers try to [Y] and can't find..." | "I just switched from [old approach] and expected [X] but instead got..." |
| Phase 2 | "I'm seeing [failure] that only appears when [edge condition]..." | "We're getting repeat questions about [X] — the pattern seems to be..." | "I got the basic setup working but now [advanced feature] is failing with..." |
| Phase 3 | "We've been running {topic} in prod for [N] weeks and we just saw..." | "This is the third time this month someone has escalated [X]..." | "I've been using {topic} for a couple months and I've noticed [data/reliability concern]..." |

**Phase vocabulary pools:**

Phase 1 pool (discovery/onboarding — required for all Phase 1 tickets):
- "I'm trying to set up {topic} for the first time and..."
- "I can't figure out how to configure..."
- "Just started using {topic} and I don't see any option to..."
- "I followed the getting started guide but..."
- "We're onboarding our team to {topic} and ran into..."
- "This is my first time using this feature and..."

Phase 3 pool (operational/reliability — required for at least 1 Phase 3 ticket):
- "We've been running {topic} in production for [N] weeks and we just saw..."
- "Something changed recently — this used to work and now..."
- "Our on-call was paged because..."
- "We're seeing elevated error rates in..."
- "This is causing a production incident where..."
- "Our SLO is at risk because..."

**Vocabulary commitment table (fill before Step 3):**

| T-ID | Phase | Committed opening phrase |
|------|-------|-------------------------|
| T-01 | Phase ___ | "___" |
| T-02 | Phase ___ | "___" |
| T-03 | Phase ___ | "___" |
| ... | | |

Pre-flight check:
- Phase 1 rows all use discovery/onboarding vocabulary: Y / N
- At least one Phase 3 row uses operational/reliability vocabulary: Y / N

If either check is N: revise commitment table before continuing.

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

### STEP 4 — PERFORMANCE MODE DECLARATION (character-embodiment + migration context)

**You are about to become each persona. They know what they migrated from.**

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior system's failure modes cold; this one is still opaque to you. Something is now breaking silently that you would have caught immediately in the old system. You are methodical but frustrated.

**Support:** You've answered this same migration question multiple times this week. You know what the old approach expected; {topic} does something different that users keep tripping over. You are filing this ticket to get engineering to fix the root cause so you can stop answering it.

**PM:** Adoption is below forecast. You cannot tell if it is a product problem or a communication problem. You are filing this to request data that would help you decide which to address first.

**UX:** You are watching session recordings and seeing users stall at a specific point. The old approach had a familiar affordance here; the new one does not. You know the friction point by location; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach in Step 1B] recently. Something surprised you — either something that used to work stopped working, or something you expected to just work required extra setup. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer". Begin each body with the phrase committed in STEP 2B. Use the role-phase anchor from STEP 2B as the sentence scaffold. Where migration-relevant: reference what was expected from the old approach.**

---

### STEP 5 — Ticket Inventory Table

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK — verify all before proceeding:
- Total rows: ___ (required: matches CONSTRAINT MANIFEST committed value)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= MANIFEST ceiling)
- High-volume count: ___ (required: <= MANIFEST ceiling)
- Theme counts match Step 3 declarations: MATCH / MISMATCH
- Phase distribution matches Step 1: MATCH / MISMATCH
- All Phase 1 tickets have committed discovery phrase in STEP 2B table: Y / N
- At least 1 Phase 3 ticket has committed operational phrase in STEP 2B table: Y / N

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[2-5 sentences. Begin with the phrase committed in STEP 2B.
Use the role-phase anchor from STEP 2B as the sentence scaffold.
First person only. Embody the character from Step 4.
Where migration-relevant: reference the old approach from Step 1B.]
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
|------|-------------|--------------------|-----------------:|
| T-NN | SRE / Support / PM / Eng | doc-gap / design-flaw / config-error / product-bug | self-serve (doc fix) / escalation (eng fix) / structural (design change) |

All three fields required per qualifying ticket. If no tickets qualify: state "no high-volume or P0/P1 tickets."

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

**Complete after gap analysis. Every row is a numeric actual vs. required comparison.**

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
| Roles with 3+ tickets spanning 2+ phases | all: Y / N | Y / N | PASS / FAIL |
| Phase 1 tickets at P2/P3 | >= 60% (>= ___ of ___) | ___ of ___ | PASS / FAIL |
| Phase 3 tickets at P0/P1 | >= 1 | ___ | PASS / FAIL |
| Phase 1 bodies with discovery/onboarding vocab | >= 3 | ___ | PASS / FAIL |
| Phase 3 bodies with operational/reliability vocab | >= 1 | ___ | PASS / FAIL |
| Broken T-NN refs in gap entries | 0 | ___ | PASS / FAIL |
| Resolution paths for qualifying tickets | complete: Y / N | Y / N | PASS / FAIL |

If any row shows FAIL: revise before submitting.

---

## Variation Summary

| ID | Primary axis | Secondary axis | Delta vs R2 V-05 | C-14 mechanism | C-15 mechanism |
|----|-------------|---------------|------------------|---------------|----------------|
| V-01 | Lifecycle emphasis | — | STEP 2B: phase vocabulary pools + per-ticket commitment table; body begins with committed phrase | Committed phrase is the body text evidence; can be counted | — (STEP 9 Pass 2 lines retained; C-15 partially implied but not manifest-table form) |
| V-02 | Output format | — | CONSTRAINT MANIFEST table before STEP 1; VERIFICATION MANIFEST table with Required/Actual/Status at end | Phase 1/3 vocab rows in VERIFICATION MANIFEST | Both manifest tables are unambiguous pre/post blocks |
| V-03 | Role sequence | — | Role-phase vocabulary matrix: each cell declares exact register for role × phase; SRE-first generation order | Matrix cells force role-appropriate discovery/operational language per phase | STEP 1 + STEP 9 Pass 2 retained; partial C-15 |
| V-04 | Lifecycle emphasis | Output format | V-01 + V-02: commitment table + manifest tables | Committed phrase + VERIFICATION MANIFEST vocab rows | CONSTRAINT MANIFEST + VERIFICATION MANIFEST |
| V-05 | Full synthesis | All R2 V-05 + V-01 + V-02 | Full R2 V-05 + commitment table in STEP 2B + manifest tables replacing STEP 1 / STEP 9 Pass 2 | Committed phrase is body text evidence; VERIFICATION MANIFEST row counts it | CONSTRAINT MANIFEST (12 targets declared) + VERIFICATION MANIFEST (17 rows, each with numeric comparison) |

**Expected R3 composite for V-05:**
- C-01 through C-09: PASS (inherited from R2 V-05)
- C-10: PASS (STEP 7B resolution paths)
- C-11: PASS (dual-pass verification + manifest tables catch zero broken T-NN refs)
- C-12: PASS (role-phase cross-matrix constraint 2)
- C-13: PASS (VERIFICATION MANIFEST rows 12-13 enforce phase-severity calibration)
- C-14: PASS (committed phrases from discovery/operational pools begin Phase 1/3 bodies — evidence in body text, not metadata)
- C-15: PASS (CONSTRAINT MANIFEST names 12 structural targets; VERIFICATION MANIFEST has 17 rows each with Required/Actual/Status — far exceeds "2+ targets" and "1+ numeric comparison")
- **Expected composite: 100**
