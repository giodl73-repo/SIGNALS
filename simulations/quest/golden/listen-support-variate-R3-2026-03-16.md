---
skill: quest-variate
skill_target: listen-support
rubric_version: 3
date: 2026-03-16
round: 3
baseline: listen-support-variate-R2-2026-03-15.md (V-05, expected composite ~88)
---

# listen-support — Variations, Round 3

**Baseline:** V-05 from R2 (full synthesis — phase-first + role-matrix + character-embodiment + inertia framing + theme-first + resolution paths)
**R3 objective:** Target the three new rubric criteria (C-14, C-15, C-16) while preserving all R2 gains

---

## R3 Regression Analysis (from R2 scorecard)

| Criterion | R2 finding | Structural gap |
|-----------|-----------|---------------|
| C-14 (Phase+Title coexistence) | R2 V-05 uses `## T-NN — {Title}` header — Title embedded in heading, not a named field; adding Phase to metadata line crowds the format | Need explicit `Title:` as named field AND `Phase:` as named field on same card — neither satisfies the other |
| C-15 (Temporal severity model) | R2 uses "severity norm" inference language ("P2/P3" as target range with override path) — this is fallback-grounded, not mechanical | Day-window lookup table: day 0-30 → P2/P3 mechanically, day 61-90 → P0/P1 mechanically — no "norm" language, no fallback |
| C-16 (Prior-tool 4th verification check) | R2 STEP 9 has 3 structural checks (phase distribution, severity compliance, role diversity); prior-tool citation counted nowhere | Add 4th check: count of bodies naming prior tool by exact name, with PASS/FAIL gate |

---

## R3 Variation Axes

| Axis | Variation | Hypothesis |
|------|-----------|-----------|
| Output format (card template) | V-01 | Separating `Title:` from the T-NN header as a distinct named field, while keeping `Phase:` as a separate named field, prevents the displacement regression — neither field can be satisfied by the other |
| Lifecycle emphasis (mechanical severity) | V-02 | Replacing "severity norm" language with a day-window lookup table that assigns tiers mechanically makes C-15 pass by construction; the model has no fallback path to use inference |
| Inertia framing (prior-tool citation) | V-03 | Requiring prior tool exact name in Step 1B, tracking it in the vocabulary table, and adding a named count in verification makes C-16 pass by construction |
| V-01 + V-02 combined | V-04 | Card template rigidity and mechanical severity reinforce each other: the Phase field on the card is now the anchor for the severity lookup, not an optional decoration |
| Full synthesis (all R3 axes) | V-05 | All three R3 criteria addressed simultaneously with minimal structural change to R2 V-05; the three fixes are independent and do not conflict |

---

## V-01 — Single Axis: Output Format (Card Template Rigidity)

**Axis:** Card template rewritten so `Title:` is an explicit named field SEPARATE from the `## T-NN` header, and `Phase:` remains as a named field on the metadata line. Both fields enforced in vocabulary table and verification.
**Hypothesis:** The displacement regression occurs because R2 embedded Title in the markdown heading (`## T-NN — {Title}`), which satisfies heading syntax but not the `Title:` named-field requirement. Separating them forces both to be present as explicit named fields without one evicting the other.
**Baseline:** R2 V-05 with one change: STEP 6 card template restructured; C-14 check added to STEP 9.

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

| Phase | Window | Migration context | Severity norm | Volume norm | Body character |
|-------|--------|------------------|--------------|------------|----------------|
| Phase 1 | day 0-30 | Habit disruption | P2/P3 | high/medium | "I tried the old way and hit a wall" |
| Phase 2 | day 31-60 | Hybrid / edge cases | P1/P2 | medium | "I got past setup but now something unexpected" |
| Phase 3 | day 61-90 | Committed or churned | P0/P1 | low/medium | "We've been running this for two months and something serious broke" |

**Phase-severity inference rule:** Assign from the norm column. Explicit override only if the specific failure is unambiguously more or less severe than the phase norm.

---

### STEP 2B — Phase Body Template Table

| Phase | SRE anchor | Support anchor | C-xx anchor |
|-------|-----------|---------------|-------------|
| Phase 1 | "I set up {topic} and now my [monitoring/alert/pipeline] is..." | "I keep seeing [X] when customers try to [Y] and can't find..." | "I just switched from [old approach] and expected [X] but instead got..." |
| Phase 2 | "I'm seeing [failure] that only appears when [edge condition]..." | "We're getting repeat questions about [X] — the pattern seems to be..." | "I got the basic setup working but now [advanced feature] is failing with..." |
| Phase 3 | "We've been running {topic} in prod for [N] weeks and we just saw..." | "This is the third time this month someone has escalated [X]..." | "I've been using {topic} for a couple months and I've noticed [data/reliability concern]..." |

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

Fill before generating any ticket body. This is a constraint declaration.

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

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior system's failure modes cold; this one is still opaque to you. Something is now breaking silently that you would have caught immediately in the old system. You are methodical but frustrated.

**Support:** You've answered this same migration question multiple times this week. You know what the old approach expected; {topic} does something different that users keep tripping over. You are filing this ticket to get the engineering team to fix the root cause so you can stop answering it.

**PM:** Adoption is below forecast. You cannot tell if it is a product problem or a communication problem. You are filing this to request data that would help you decide which to address first.

**UX:** You are watching session recordings and seeing users stall at a specific point. The old approach had a familiar affordance here; the new one does not. You know the friction point by location; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach named in Step 1B] recently. Something surprised you — either something that used to work stopped working, or something you expected to just work required extra setup. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer". Where migration-relevant: reference what was expected from the old approach.**

---

### STEP 5 — Vocabulary Pre-Commitment

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

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

**Card template — BOTH fields required on every card:**

```
## T-NN
- Title: [descriptive subject line]
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[First person, 2-5 sentences. Embody the character from Step 4.
Use the phase body anchor from Step 2B as the sentence scaffold.
Where migration-relevant: reference the old approach from Step 1B.]
```

**Title rule:** `Title:` must be a human-readable subject line summarizing the feedback.
The `## T-NN` heading is the ticket ID — it does NOT satisfy the `Title:` field.
Example: `- Title: Pipeline silently drops events with no alert when {topic} batch size exceeds limit`

**Phase rule:** `Phase:` must appear as a named field on the metadata line with its full window label
(`Phase 1 (day 0-30)`, `Phase 2 (day 31-60)`, or `Phase 3 (day 61-90)`).
A bare phase number or severity abbreviation does not satisfy this field.

**Both fields are required and neither satisfies the other.**

Body organization:

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

[All Theme A ticket cards here]

### Theme B — {theme name}
*Underlying failure: {from Step 3}*

[All Theme B ticket cards here]
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

### STEP 9 — Dual-Pass Verification

**Pass 1 — Coverage trace (one sentence each):**
- C-01 (Title named field): [confirm every card has `Title:` as a separate named field, not just a heading]
- C-02 (vocabulary enforced): ...
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

Role-phase compound coverage:
  Roles with 3+ tickets: [list] — each spans 2+ phases: Y / N

Phase-severity calibration:
  Phase 1 tickets at P2/P3: ___ of ___   (required: >= 60%)
  At least 1 Phase 3 ticket at P0/P1: Y / N

Card template compliance (C-14):
  Cards with Title: as named field: ___ of ___   (required: all)
  Cards with Phase: as named field: ___ of ___   (required: all)
  Both fields present on same card: ___ of ___   (required: all)
  PASS / FAIL

Broken T-NN refs in gap entries: ___   (required: 0)
Resolution paths complete for all qualifying tickets: Y / N
```

If any check fails: revise before submitting.

---

## V-02 — Single Axis: Lifecycle Emphasis (Mechanical Severity Assignment)

**Axis:** STEP 2 phase map replaces "severity norm" inference language with a strict day-window severity lookup table. The model reads the ticket's Phase window, looks up the required tier, and assigns from it — no "override" path, no "norm" language, no fallback inference.
**Hypothesis:** The word "norm" signals that deviation is acceptable, which allows inference to substitute for mechanical compliance. A strict lookup table with tier boundaries has no norm to deviate from — severity is an output of phase position, not an estimate. C-15 is satisfied by construction because there is nothing else to do.
**Baseline:** R2 V-05 with one change: STEP 2 rewritten as day-window lookup; mechanical severity check added to STEP 9.

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

### STEP 2 — Severity Assignment (Day-Window Lookup)

Severity is assigned mechanically from the ticket's Phase window. Look up the window, assign from the tier.

```
Day-window severity table:
  Phase 1 (day 0-30)  → P2 or P3   [setup and habit-disruption failures; not P0, not P1]
  Phase 2 (day 31-60) → P1 or P2   [edge-case and integration failures; not P0, not P3]
  Phase 3 (day 61-90) → P0 or P1   [operational and reliability failures; not P2, not P3]
```

**Assignment procedure:**
1. Determine the ticket's Phase window from Step 1 distribution
2. Look up that window in the table above
3. Assign severity from the allowed tier (P2/P3 for Phase 1; P1/P2 for Phase 2; P0/P1 for Phase 3)
4. Choose the specific value within the tier based on the failure's impact on the user

**No override path exists.** If you believe a Phase 1 ticket warrants P0: reclassify the ticket to Phase 3, or omit it. The window determines the tier.

---

### STEP 2B — Phase Context Table

| Phase | Window | Migration context | Volume norm | Body character |
|-------|--------|------------------|------------|----------------|
| Phase 1 | day 0-30 | Habit disruption | high/medium | "I tried the old way and hit a wall" |
| Phase 2 | day 31-60 | Hybrid / edge cases | medium | "I got past setup but now something unexpected" |
| Phase 3 | day 61-90 | Committed or churned | low/medium | "We've been running this for two months and something serious broke" |

---

### STEP 2C — Phase Body Template Table

| Phase | SRE anchor | Support anchor | C-xx anchor |
|-------|-----------|---------------|-------------|
| Phase 1 | "I set up {topic} and now my [monitoring/alert/pipeline] is..." | "I keep seeing [X] when customers try to [Y] and can't find..." | "I just switched from [old approach] and expected [X] but instead got..." |
| Phase 2 | "I'm seeing [failure] that only appears when [edge condition]..." | "We're getting repeat questions about [X] — the pattern seems to be..." | "I got the basic setup working but now [advanced feature] is failing with..." |
| Phase 3 | "We've been running {topic} in prod for [N] weeks and we just saw..." | "This is the third time this month someone has escalated [X]..." | "I've been using {topic} for a couple months and I've noticed [data/reliability concern]..." |

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

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior system's failure modes cold; this one is still opaque to you. Something is now breaking silently that you would have caught immediately in the old system. You are methodical but frustrated.

**Support:** You've answered this same migration question multiple times this week. You know what the old approach expected; {topic} does something different that users keep tripping over. You are filing this ticket to get the engineering team to fix the root cause so you can stop answering it.

**PM:** Adoption is below forecast. You cannot tell if it is a product problem or a communication problem. You are filing this to request data that would help you decide which to address first.

**UX:** You are watching session recordings and seeing users stall at a specific point. The old approach had a familiar affordance here; the new one does not. You know the friction point by location; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach named in Step 1B] recently. Something surprised you — either something that used to work stopped working, or something you expected to just work required extra setup. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer". Where migration-relevant: reference what was expected from the old approach.**

---

### STEP 5 — Vocabulary Pre-Commitment

Before filling this table: for each ticket, determine its Phase, then look up its severity tier in the STEP 2 day-window table. Assign severity from within the allowed tier before recording it here.

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | [from window lookup] | ... | ... | Y/N |

TABLE CHECK — verify all before proceeding:
- Total rows: ___ (required: >= 6 and <= 12)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= 25% of total, round down)
- High-volume count: ___ (required: <= 50% of total, round down)
- Phase 1 severities all P2/P3: Y / N  [check window lookup compliance now]
- Phase 3 has at least 1 P0/P1: Y / N
- Theme counts match Step 3 declarations: MATCH / MISMATCH
- Phase distribution matches Step 1: MATCH / MISMATCH

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[First person, 2-5 sentences. Embody the character from Step 4.
Use the phase body anchor from Step 2C as the sentence scaffold.
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

---

### STEP 8 — Gap Analysis

All entries require `Tickets: T-NN, T-NN` with identifiers matching the inventory above.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it

**Migration friction sub-section** (include if >= 2 migration tickets):
Friction point | affected tickets | what would eliminate it

---

### STEP 9 — Dual-Pass Verification

**Pass 1 — Coverage trace (one sentence each):**
- C-01 (Title field present): ...
- C-02 (vocabulary enforced): ...
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

Role-phase compound coverage:
  Roles with 3+ tickets: [list] — each spans 2+ phases: Y / N

Mechanical severity compliance (C-15):
  Phase 1 tickets (day 0-30) with severity outside {P2, P3}: ___   (required: 0)
  Phase 2 tickets (day 31-60) with severity outside {P1, P2}: ___   (required: 0)
  Phase 3 tickets (day 61-90) with severity outside {P0, P1}: ___   (required: 0)
  All windows compliant: Y / N   PASS / FAIL

Broken T-NN refs in gap entries: ___   (required: 0)
Resolution paths complete for all qualifying tickets: Y / N
```

If any check fails: revise before submitting.

---

## V-03 — Single Axis: Inertia Framing (Prior-Tool Citation Mandate)

**Axis:** STEP 1B gains a required `Prior tool exact name:` field. The vocabulary table gains a `Prior-tool ref?` column (Y/N). STEP 9 gains a 4th structural check: count of ticket bodies that name the prior tool by its exact recorded name, with PASS (>= 2) / FAIL gate.
**Hypothesis:** R2 framed inertia as migration context — the prior approach is described narratively but never referenced by exact name in verification. Naming the prior tool exactly in STEP 1B creates a citation target; tracking it in the vocabulary table and counting it in STEP 9 makes the model verify its own coverage. The 4th check is C-16 by construction.
**Baseline:** R2 V-05 with three additions: (1) `Prior tool exact name:` in Step 1B, (2) `Prior-tool ref?` column in Step 5 table, (3) prior-tool citation count in Step 9.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### STEP 1 — Phase Distribution Target

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
Prior tool exact name: ___          ← record once; this is the citation target for STEP 9
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
Migration window frame:
  Phase 1 = habit disruption — users trying to do it the old way and hitting walls
  Phase 2 = hybrid use — some on {topic}, some still on old approach; integration gaps surface
  Phase 3 = committed or churned — full adopters hit operational limits
```

At least 2 ticket bodies must name the prior tool by its exact name recorded above.
This is a hard requirement verified in STEP 9.

---

### STEP 2 — Phase Map Table

| Phase | Window | Migration context | Severity norm | Volume norm | Body character |
|-------|--------|------------------|--------------|------------|----------------|
| Phase 1 | day 0-30 | Habit disruption | P2/P3 | high/medium | "I tried the old way and hit a wall" |
| Phase 2 | day 31-60 | Hybrid / edge cases | P1/P2 | medium | "I got past setup but now something unexpected" |
| Phase 3 | day 61-90 | Committed or churned | P0/P1 | low/medium | "We've been running this for two months and something serious broke" |

**Phase-severity inference rule:** Assign from the norm column. Explicit override only if the specific failure is unambiguously more or less severe than the phase norm.

---

### STEP 2B — Phase Body Template Table

| Phase | SRE anchor | Support anchor | C-xx anchor |
|-------|-----------|---------------|-------------|
| Phase 1 | "I set up {topic} and now my [monitoring/alert/pipeline] is..." | "I keep seeing [X] when customers try to [Y] and can't find..." | "I just switched from [prior tool name] and expected [X] but instead got..." |
| Phase 2 | "I'm seeing [failure] that only appears when [edge condition]..." | "We're getting repeat questions about [X] — the pattern seems to be..." | "I got the basic setup working but now [advanced feature] is failing with..." |
| Phase 3 | "We've been running {topic} in prod for [N] weeks and we just saw..." | "This is the third time this month someone has escalated [X]..." | "I've been using {topic} for a couple months — we migrated from [prior tool name] and I've noticed..." |

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

**You are about to become each persona. They know what they migrated from, and they know the prior tool's name.**

**SRE:** You're on-call. You adopted {topic} because the team moved to it from [prior tool name]. You knew [prior tool name]'s failure modes cold; {topic} is still opaque to you. Something is now breaking silently that you would have caught immediately in [prior tool name]. You are methodical but frustrated.

**Support:** You've answered this same migration question multiple times this week. [Prior tool name] expected users to [do X]; {topic} does something different that users keep tripping over. You are filing this ticket to get the engineering team to fix the root cause.

**PM:** Adoption is below forecast. [Prior tool name] had known friction; {topic} has unknown friction. You cannot tell if the problem is in the product or the messaging. You need data.

**UX:** Users are stalling where [prior tool name] had a familiar affordance. The new flow in {topic} does not read as the replacement it is. You can see it in the session recordings. You are filing to name the pattern so engineering can investigate.

**C-xx:** You switched from [prior tool name] to {topic}. Something surprised you — either something [prior tool name] handled for you now requires extra setup, or something you expected to carry over didn't. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer". Where migration-relevant: name the prior tool exactly as recorded in Step 1B.**

---

### STEP 5 — Vocabulary Pre-Commitment

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? | Prior-tool ref? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|----------------|
| T-01 | ... | ... | ... | ... | ... | ... | ... | Y/N | Y/N |

**Prior-tool ref column:** Y = ticket body names the prior tool by its exact name from Step 1B. At least 2 rows must be Y.

TABLE CHECK — verify all before proceeding:
- Total rows: ___ (required: >= 6 and <= 12)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= 25% of total, round down)
- High-volume count: ___ (required: <= 50% of total, round down)
- Prior-tool ref Y count: ___ (required: >= 2)
- Theme counts match Step 3 declarations: MATCH / MISMATCH
- Phase distribution matches Step 1: MATCH / MISMATCH

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[First person, 2-5 sentences. Embody the character from Step 4.
Use the phase body anchor from Step 2B as the sentence scaffold.
Where Prior-tool ref? = Y: name the prior tool by its exact name from Step 1B.]
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

---

### STEP 8 — Gap Analysis

All entries require `Tickets: T-NN, T-NN` with identifiers matching the inventory above.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it

**Migration friction sub-section** (include if >= 2 migration tickets):
Friction point | affected tickets | what would eliminate it

---

### STEP 9 — Dual-Pass Verification

**Pass 1 — Coverage trace (one sentence each):**
- C-01 (Title field present): ...
- C-02 (vocabulary enforced): ...
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

Role-phase compound coverage:
  Roles with 3+ tickets: [list] — each spans 2+ phases: Y / N

Phase-severity calibration:
  Phase 1 tickets at P2/P3: ___ of ___   (required: >= 60%)
  At least 1 Phase 3 ticket at P0/P1: Y / N

Prior-tool citation count (C-16):
  Prior tool exact name from Step 1B: "___"
  Ticket bodies naming that exact string: ___ of ___   (required: >= 2)
  PASS / FAIL

Broken T-NN refs in gap entries: ___   (required: 0)
Resolution paths complete for all qualifying tickets: Y / N
```

If any check fails: revise before submitting.

---

## V-04 — Combined: Card Template Rigidity + Mechanical Severity

**Axis combination:** V-01 (output format — explicit Title + Phase named fields) + V-02 (lifecycle emphasis — mechanical day-window severity lookup)
**Hypothesis:** The card template fix and the mechanical severity fix reinforce each other: the `Phase: Phase N (day X-Y)` named field on the card now explicitly anchors the day window, making the lookup unambiguous; the Phase field is not decorative — it is the input to the severity table. This structural coupling makes both C-14 and C-15 pass together more reliably than either fix alone.
**Baseline:** R2 V-05 + V-01 card template change + V-02 severity model change.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### STEP 1 — Phase Distribution Target

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

### STEP 2 — Severity Assignment (Day-Window Lookup)

Severity is assigned mechanically from the ticket's Phase window.

```
Day-window severity table:
  Phase 1 (day 0-30)  → P2 or P3   [not P0, not P1]
  Phase 2 (day 31-60) → P1 or P2   [not P0, not P3]
  Phase 3 (day 61-90) → P0 or P1   [not P2, not P3]
```

**Assignment procedure:**
1. Determine the ticket's Phase window from Step 1 distribution
2. Look up the required tier in the table above
3. Choose the specific value within the tier (e.g., P2 vs P3) based on the failure's impact
4. Record the Phase window explicitly on the card — the Phase field is the lookup key for the severity tier

No override path exists. If a Phase 1 failure seems like P0: reclassify to Phase 3, or omit it.

---

### STEP 2B — Phase Context Table

| Phase | Window | Migration context | Volume norm | Body character |
|-------|--------|------------------|------------|----------------|
| Phase 1 | day 0-30 | Habit disruption | high/medium | "I tried the old way and hit a wall" |
| Phase 2 | day 31-60 | Hybrid / edge cases | medium | "I got past setup but now something unexpected" |
| Phase 3 | day 61-90 | Committed or churned | low/medium | "We've been running this for two months and something serious broke" |

---

### STEP 2C — Phase Body Template Table

| Phase | SRE anchor | Support anchor | C-xx anchor |
|-------|-----------|---------------|-------------|
| Phase 1 | "I set up {topic} and now my [monitoring/alert/pipeline] is..." | "I keep seeing [X] when customers try to [Y] and can't find..." | "I just switched from [old approach] and expected [X] but instead got..." |
| Phase 2 | "I'm seeing [failure] that only appears when [edge condition]..." | "We're getting repeat questions about [X] — the pattern seems to be..." | "I got the basic setup working but now [advanced feature] is failing with..." |
| Phase 3 | "We've been running {topic} in prod for [N] weeks and we just saw..." | "This is the third time this month someone has escalated [X]..." | "I've been using {topic} for a couple months and I've noticed [data/reliability concern]..." |

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

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior system's failure modes cold; this one is still opaque to you. Something is now breaking silently that you would have caught immediately in the old system. You are methodical but frustrated.

**Support:** You've answered this same migration question multiple times this week. You know what the old approach expected; {topic} does something different that users keep tripping over. You are filing this ticket to get the engineering team to fix the root cause so you can stop answering it.

**PM:** Adoption is below forecast. You cannot tell if it is a product problem or a communication problem. You are filing this to request data that would help you decide which to address first.

**UX:** You are watching session recordings and seeing users stall at a specific point. The old approach had a familiar affordance here; the new one does not. You know the friction point by location; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach named in Step 1B] recently. Something surprised you — either something that used to work stopped working, or something you expected to just work required extra setup. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer". Where migration-relevant: reference what was expected from the old approach.**

---

### STEP 5 — Vocabulary Pre-Commitment

Before recording severity: determine each ticket's Phase, look up the allowed tier in the STEP 2 table, assign from within that tier.

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|
| T-01 | ... | ... | ... | ... | [from window lookup] | Phase N (day X-Y) | ... | Y/N |

TABLE CHECK — verify all before proceeding:
- Total rows: ___ (required: >= 6 and <= 12)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= 25% of total, round down)
- High-volume count: ___ (required: <= 50% of total, round down)
- Phase 1 severities all P2/P3: Y / N
- Phase 3 has at least 1 P0/P1: Y / N
- Theme counts match Step 3 declarations: MATCH / MISMATCH
- Phase distribution matches Step 1: MATCH / MISMATCH

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

**Card template — BOTH Title and Phase are required named fields on every card:**

```
## T-NN
- Title: [descriptive subject line]
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[First person, 2-5 sentences. Embody the character from Step 4.
Use the phase body anchor from Step 2C as the sentence scaffold.
Where migration-relevant: reference the old approach from Step 1B.]
```

**Title rule:** `Title:` must be a human-readable subject line. The `## T-NN` heading is the ticket ID — it does NOT satisfy this field.
**Phase rule:** `Phase:` must appear on the metadata line with full window label. It is the lookup key for severity — if it is missing, the severity cannot be verified.
**Both fields are required. One does not satisfy the other.**

Body organization:

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

[All Theme A ticket cards here]

### Theme B — {theme name}
*Underlying failure: {from Step 3}*

[All Theme B ticket cards here]
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

---

### STEP 8 — Gap Analysis

All entries require `Tickets: T-NN, T-NN`.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it

**Migration friction sub-section** (include if >= 2 migration tickets):
Friction point | affected tickets | what would eliminate it

---

### STEP 9 — Dual-Pass Verification

**Pass 1 — Coverage trace (one sentence each):**
- C-01 (Title named field): [confirm every card has `Title:` as a named field separate from heading]
- C-02 (vocabulary enforced): ...
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

Role-phase compound coverage:
  Roles with 3+ tickets: [list] — each spans 2+ phases: Y / N

Card template compliance (C-14):
  Cards with Title: as named field: ___ of ___   (required: all)
  Cards with Phase: as named field: ___ of ___   (required: all)
  Both fields present on same card: ___ of ___   (required: all)
  PASS / FAIL

Mechanical severity compliance (C-15):
  Phase 1 tickets with severity outside {P2, P3}: ___   (required: 0)
  Phase 2 tickets with severity outside {P1, P2}: ___   (required: 0)
  Phase 3 tickets with severity outside {P0, P1}: ___   (required: 0)
  All windows compliant: Y / N   PASS / FAIL

Broken T-NN refs in gap entries: ___   (required: 0)
Resolution paths complete for all qualifying tickets: Y / N
```

If any check fails: revise before submitting.

---

## V-05 — Full Synthesis (R3 Golden Candidate)

**Axis combination:** R2 V-05 base + V-01 (card template rigidity) + V-02 (mechanical severity) + V-03 (prior-tool citation mandate)
**Hypothesis:** The three R3 fixes address three independent structural gaps without conflict. The card template fix (V-01) and mechanical severity fix (V-02) share the Phase named field — fixing one strengthens the other. The prior-tool citation mandate (V-03) adds a dimension to STEP 1B, the vocabulary table, and STEP 9 without touching the card template or severity model. The three fixes stack cleanly onto R2 V-05 and push C-14/C-15/C-16 to PASS by construction. This is the R3 golden candidate.

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
Prior tool exact name: ___          ← record once; citation target for STEP 9
Key habit they carry in: ___
Primary migration friction (first wall they hit): ___
Migration window frame:
  Phase 1 = habit disruption — users trying to do it the old way and hitting walls
  Phase 2 = hybrid use — some on {topic}, some still on old approach; integration gaps surface
  Phase 3 = committed or churned — full adopters hit operational limits
```

Constraint: at least 2 ticket bodies must name the prior tool by the exact string recorded above.

---

### STEP 2 — Severity Assignment (Day-Window Lookup)

Severity is a mechanical output of the ticket's Phase window — not an estimate or a norm.

```
Day-window severity table:
  Phase 1 (day 0-30)  → P2 or P3   [not P0, not P1]
  Phase 2 (day 31-60) → P1 or P2   [not P0, not P3]
  Phase 3 (day 61-90) → P0 or P1   [not P2, not P3]
```

**Assignment procedure:**
1. Determine the ticket's Phase window from Step 1 distribution
2. Look up the allowed tier above
3. Choose the specific value within the tier based on the failure's impact
4. The Phase field on the card is the lookup key — it is required, not decorative

No override path exists. If a Phase 1 failure seems like P0: reclassify to Phase 3, or omit it.

---

### STEP 2B — Phase Context Table

| Phase | Window | Migration context | Volume norm | Body character |
|-------|--------|------------------|------------|----------------|
| Phase 1 | day 0-30 | Habit disruption | high/medium | "I tried the old way and hit a wall" |
| Phase 2 | day 31-60 | Hybrid / edge cases | medium | "I got past setup but now something unexpected" |
| Phase 3 | day 61-90 | Committed or churned | low/medium | "We've been running this for two months and something serious broke" |

---

### STEP 2C — Phase Body Template Table

Commit to one sentence template per phase per role before writing bodies. These are vocabulary anchors — expand into full bodies, not copy-paste.

| Phase | SRE anchor | Support anchor | C-xx anchor |
|-------|-----------|---------------|-------------|
| Phase 1 | "I set up {topic} and now my [monitoring/alert/pipeline] is..." | "I keep seeing [X] when customers try to [Y] and can't find..." | "I just switched from [prior tool name] and expected [X] but instead got..." |
| Phase 2 | "I'm seeing [failure] that only appears when [edge condition]..." | "We're getting repeat questions about [X] — the pattern seems to be..." | "I got the basic setup working but now [advanced feature] is failing with..." |
| Phase 3 | "We've been running {topic} in prod for [N] weeks and we just saw..." | "This is the third time this month someone has escalated [X]..." | "We migrated from [prior tool name] a couple months ago and I've now noticed [data/reliability concern]..." |

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

Fill before generating any ticket body. This is a constraint declaration.

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

**You are about to become each persona. They know what they migrated from and they know the prior tool's name.**

**SRE:** You're on-call. You adopted {topic} because the team moved to it from [prior tool exact name]. You knew [prior tool exact name]'s failure modes cold; {topic} is still opaque to you. Something is now breaking silently that you would have caught immediately in [prior tool exact name]. You are methodical but frustrated.

**Support:** You've answered this same migration question multiple times this week. [Prior tool exact name] expected users to work a certain way; {topic} does something different that users keep tripping over. You are filing this ticket to get the engineering team to fix the root cause so you can stop answering it.

**PM:** Adoption is below forecast. [Prior tool exact name] had known friction; {topic} has unknown friction. You cannot tell if the problem is in the product or in the communication. You need data to decide which to fix first.

**UX:** Users are stalling where [prior tool exact name] had a familiar affordance. The new flow in {topic} does not read as the replacement it is. You can see it in the session recordings. You are filing to name the pattern so engineering can investigate.

**C-xx:** You switched from [prior tool exact name] to {topic}. Something surprised you — either something [prior tool exact name] handled automatically now requires extra setup, or something you expected to carry over didn't. You do not know if it is a bug or if you are doing it wrong. You need an answer so you can keep moving.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer". Where migration-relevant: name the prior tool exactly as recorded in Step 1B.**

---

### STEP 5 — Vocabulary Pre-Commitment

Before recording severity: determine each ticket's Phase, look up the allowed tier in STEP 2, assign from within that tier.

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Theme | Migration? | Prior-tool ref? |
|------|-------|----------|---------|--------|----------|-------|-------|-----------|----------------|
| T-01 | ... | ... | ... | ... | [from window lookup] | Phase N (day X-Y) | ... | Y/N | Y/N |

**Prior-tool ref column:** Y = ticket body names the prior tool by its exact string from Step 1B.

TABLE CHECK — verify all before proceeding:
- Total rows: ___ (required: >= 6 and <= 12)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= 25% of total, round down)
- High-volume count: ___ (required: <= 50% of total, round down)
- Phase 1 severities all P2/P3: Y / N
- Phase 3 has at least 1 P0/P1: Y / N
- Prior-tool ref Y count: ___ (required: >= 2)
- Theme counts match Step 3 declarations: MATCH / MISMATCH
- Phase distribution matches Step 1: MATCH / MISMATCH

If any check fails: revise before continuing.

---

### STEP 6 — Ticket Bodies (by theme, phase-sorted within each theme, ascending T-ID)

**Card template — Title and Phase are BOTH required named fields on every card:**

```
## T-NN
- Title: [descriptive subject line]
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[First person, 2-5 sentences. Embody the character from Step 4.
Use the phase body anchor from Step 2C as the sentence scaffold.
Where Prior-tool ref? = Y: name the prior tool by its exact string from Step 1B.
Where migration-relevant: reference what was expected from the prior tool.]
```

**Title rule:** `Title:` must be a human-readable subject line. The `## T-NN` heading is the ticket ID — it does NOT satisfy this field.
**Phase rule:** `Phase:` must appear on the metadata line with full window label — it is the lookup key for severity. A bare phase number or severity code does not satisfy this field.
**Both fields are required. One does not satisfy the other.**

Body organization:

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

[All Theme A ticket cards here]

### Theme B — {theme name}
*Underlying failure: {from Step 3}*

[All Theme B ticket cards here]
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

### STEP 9 — Triple-Pass Verification

**Pass 1 — Coverage trace (one sentence each):**
- C-01 (Title named field): [confirm every card has `Title:` as a named field, not just a heading]
- C-02 (vocabulary enforced): ...
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

Role-phase compound coverage:
  Roles with 3+ tickets: [list] — each spans 2+ phases: Y / N
```

**Pass 3 — R3 traceability verification:**

```
Card template compliance (C-14):
  Cards with Title: as named field (not heading): ___ of ___   (required: all)
  Cards with Phase: as named field on metadata line: ___ of ___   (required: all)
  Both fields present on same card: ___ of ___   (required: all)
  PASS / FAIL

Mechanical severity compliance (C-15):
  Phase 1 tickets with severity outside {P2, P3}: ___   (required: 0)
  Phase 2 tickets with severity outside {P1, P2}: ___   (required: 0)
  Phase 3 tickets with severity outside {P0, P1}: ___   (required: 0)
  All windows compliant: Y / N   PASS / FAIL

Prior-tool citation count (C-16):
  Prior tool exact name from Step 1B: "___"
  Ticket bodies containing that exact string: ___ of ___   (required: >= 2)
  PASS / FAIL

Broken T-NN refs in gap entries: ___   (required: 0)
Resolution paths complete for all qualifying tickets: Y / N
```

If any check fails: revise before submitting.

---

## Variation Summary

| ID | Primary axis | Rubric target | Change from R2 V-05 |
|----|-------------|--------------|---------------------|
| V-01 | Output format (card template) | C-14 | `Title:` as named field separate from `## T-NN` heading; `Phase:` kept on metadata line; both required; C-14 check in STEP 9 |
| V-02 | Lifecycle emphasis (mechanical severity) | C-15 | Day-window lookup table replaces "norm" inference; no override path; mechanical compliance check in STEP 9 |
| V-03 | Inertia framing (prior-tool citation) | C-16 | `Prior tool exact name:` in STEP 1B; `Prior-tool ref?` column in STEP 5; citation count check in STEP 9 |
| V-04 | Output format + lifecycle | C-14 + C-15 | V-01 + V-02; Phase field on card serves as lookup key for severity — the two fixes share an anchor |
| V-05 | Full synthesis (R3 golden candidate) | C-14 + C-15 + C-16 | V-01 + V-02 + V-03; Pass 3 in STEP 9 covers all three R3 criteria as a dedicated block |

**Expected R3 composite for V-05:** 130/130 (ceiling on v3 rubric)
- C-01: PASS (Title as named field separate from heading)
- C-14: PASS (both Title and Phase as named fields on same card — Pass 3 check)
- C-15: PASS (day-window lookup, no override path — Pass 3 mechanical check)
- C-16: PASS (prior-tool citation count >= 2 — Pass 3 check)
- All R2 criteria preserved (C-02 through C-13 unchanged in structure)
