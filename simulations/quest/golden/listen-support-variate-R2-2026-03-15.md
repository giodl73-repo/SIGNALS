---
skill: quest-variate
skill_target: listen-support
rubric_version: 2
date: 2026-03-15
round: 2
baseline: listen-support-variate-R1-2026-03-15.md (V-05, composite 75.5)
---

# listen-support — Variations, Round 2

**Baseline:** V-05 from R1 (composite 75.5 — best R1 score)
**R2 objective:** Apply P0/P1 rubric v2 fixes to all variations; explore axes deferred in R1

---

## Fixed Changes Applied to All Variations

All five R2 variations share these three changes. They are not the differentiating axis.

| Fix | Criterion | What the prompt now says |
|-----|-----------|--------------------------|
| P0 | C-03 | PERFORMANCE MODE DECLARATION step added; explicit first-person mandate ("I"/"my"/"we") + explicit third-person prohibition |
| P0 | C-04 | All gap section formats require `Tickets: T-NN, T-NN`; entries without a matching T-NN identifier are invalid |
| P1 | C-06 | Ticket count gate reads `>= 6 and <= 12`; upper bound enforced alongside lower bound in all table checks |

---

## R2 Variation Axes

R1 covered: role sequence (V-01), output format (V-02), lifecycle emphasis (V-03), combined (V-04, V-05).
R2 explores three new axes:

| Axis | Single-axis variation | Hypothesis |
|------|-----------------------|-----------|
| Phrasing register | V-01 | Character-embodiment framing at PERFORMANCE MODE suppresses third-person drift more reliably than prohibition framing, because models treat identity constraints differently than rule-avoidance |
| Inertia framing | V-02 | Naming the status-quo approach users are replacing generates tickets about migration confusion and workflow disruption — failure classes absent from generic prompts |
| Theme-first generation | V-03 | Declaring named themes before tickets forces every ticket to be explicitly derived from a named product risk; C-09 is satisfied by construction rather than retrospective grouping |

Combined: V-04 stacks V-01 + V-02. V-05 stacks all three + resolution path (C-10).

---

## V-01 — Single Axis: Phrasing Register (Character-Embodiment)

**Axis:** PERFORMANCE MODE DECLARATION rewritten as identity-embodiment instead of prohibition list
**Hypothesis:** "You ARE this persona" suppresses third-person drift more than "third-person is prohibited"
because identity framing changes the model's generation mode, not just adds a rule to avoid.
**Baseline:** V-05 R1 structure with P0/P1 fixes. Only STEP 4 PERFORMANCE MODE text changes.

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

### STEP 2 — Phase Map Table

| Phase | Window | Severity norm | Volume norm | Character |
|-------|--------|--------------|------------|-----------|
| Phase 1 | day 0-30 | P2/P3 | high/medium | Setup confusion, activation errors, first-time how-to |
| Phase 2 | day 31-60 | P1/P2 | medium | Edge cases, integration surprises, config depth |
| Phase 3 | day 61-90 | P0/P1 | low/medium | Operational failures, data integrity, regression |

Phase-severity inference rule: assign from the norm column. Override only if the specific
failure is unambiguously more or less severe than the phase norm.

---

### STEP 3 — Role Activation (SRE-First)

```
SRE:     activate first   [minimum: 2 tickets]
Support: activate second  [minimum: 2 tickets]
PM:      activate third   [minimum: 1 ticket]
UX:      activate fourth  [minimum: 1 ticket]
C-xx:    fill remaining   [minimum: 2 tickets, max 2 per single C-xx persona]
```

Role-phase cross-matrix (fill before generating bodies):

| Role    | Phase 1 | Phase 2 | Phase 3 | Total |
|---------|---------|---------|---------|-------|
| SRE     | ___     | ___     | ___     | ___   |
| Support | ___     | ___     | ___     | ___   |
| PM      | ___     | ___     | ___     | ___   |
| UX      | ___     | ___     | ___     | ___   |
| C-xx    | ___     | ___     | ___     | ___   |

Constraint: any role with 3+ tickets must span at least 2 phases.

---

### STEP 4 — PERFORMANCE MODE DECLARATION (character-embodiment)

**You are about to become each persona. Read this before writing any ticket body.**

When you write a ticket attributed to **SRE**: you are the on-call engineer. You have monitoring
dashboards in front of you. You know your old system's failure modes by heart; you do not know
this one's yet. You are frustrated by a silent gap you did not plan for.

When you write a ticket attributed to **Support**: you are the frontline agent. You have answered
this question three times today. You are looking for the underlying pattern. You are tired of not
having a definitive answer. You file this ticket to escalate to the team that can fix it.

When you write a ticket attributed to **PM**: you are watching adoption metrics. The numbers are
below expectation. You do not know whether the problem is in the product or in the communication.
You file this ticket to get data.

When you write a ticket attributed to **UX**: you are watching session recordings. You see exactly
where users stall. You can name the friction point but not the root cause. You file this ticket
to name the pattern you're seeing so engineering can investigate.

When you write a ticket attributed to **C-xx**: you are a customer who is stuck. You do not know
the internal architecture. You just know what you expected and what you got instead. You are not
angry — you are confused. You file this ticket because you need to keep moving.

**In every case: you are that person. Write in first person. Use "I", "my", "we".**
**Never write "the SRE", "the user", "the developer", "the PM". You are not describing them —
you are being them.**

---

### STEP 5 — Vocabulary Pre-Commitment

| T-ID | Title (draft) | Category | Persona | Volume | Severity | Phase |
|------|---------------|----------|---------|--------|----------|-------|
| T-01 | ... | ... | ... | ... | ... | ... |
| ... | | | | | | |

TABLE CHECK — verify before proceeding:
- Total rows: ___ (required: >= 6 and <= 12)
- Distinct categories: ___ (required: >= 2)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= 25% of total, round down)
- High-volume count: ___ (required: <= 50% of total, round down)
- Phase distribution matches Step 1 commitment: MATCH / MISMATCH

If MISMATCH or any check fails: revise the table before continuing.

---

### STEP 6 — Ticket Bodies (phase order, ascending T-ID within each phase)

For each ticket:

```
## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[2-5 sentences. You ARE the persona established in Step 4. Every sentence in first person.]
```

---

### STEP 7 — Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Adoption cost |
|-------------|-----------------|------------|---------------|
| ... | T-NN, T-NN | ... | ... |

---

### STEP 8 — Gap Analysis

All entries must include `Tickets: T-NN, T-NN` with identifiers matching the inventory above.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it (specific doc page or guide)

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it (specific design decision)

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it (runbook, alert, or dashboard)

---

### STEP 9 — Verification Pass

Coverage trace (one sentence each):
- C-01: ... | C-02: ... | C-03: ... | C-04: ... | C-05: ...

Phase confirmation:
```
Phase 1: declared ___ / actual ___   MATCH / MISMATCH
Phase 2: declared ___ / actual ___   MATCH / MISMATCH
Phase 3: declared ___ / actual ___   MATCH / MISMATCH
```

---

## V-02 — Single Axis: Inertia Framing (Status-Quo Competitor)

**Axis:** Add STEP 1B STATUS QUO ANALYSIS naming what users are replacing; frame 90-day window
as a migration period; Phase 1 enriched with habit-carry-over confusion tickets
**Hypothesis:** Naming the prior approach generates migration confusion tickets that generic
prompts miss; Phase 1 becomes richer because "I expected it to work like [old way]" is a
distinct failure class that only appears when the competitor is explicit.
**Baseline:** V-05 R1 + P0/P1 fixes. STEP 1B added; Phase map gains migration context column.

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

Before analyzing failure patterns, name what users are migrating from:

```
Current approach users are replacing: ___
Key habit they carry in from the old approach: ___
Primary migration friction (first wall they hit): ___
Migration window frame:
  Phase 1 = habit disruption — users trying to do it the old way and hitting walls
  Phase 2 = hybrid use — some on {topic}, some still on old approach; integration gaps surface
  Phase 3 = committed or churned — full adopters hit operational limits; late deciders file last tickets
```

Use this context when generating Phase 1 tickets: at least one ticket in Phase 1 must address
migration confusion specifically — not general unfamiliarity, but "I expected it to work like
[old approach] because..."

---

### STEP 2 — Phase Map Table

| Phase | Window | Migration context | Severity norm | Volume norm |
|-------|--------|------------------|--------------|------------|
| Phase 1 | day 0-30 | Habit disruption | P2/P3 | high/medium |
| Phase 2 | day 31-60 | Hybrid / edge cases | P1/P2 | medium |
| Phase 3 | day 61-90 | Committed or churned | P0/P1 | low/medium |

---

### STEP 3 — Role Activation (SRE-First)

```
SRE: >= 2 | Support: >= 2 | PM: >= 1 | UX: >= 1 | C-xx: >= 2 (max 2 per single C-xx)
```

Role-phase cross-matrix:

| Role    | Phase 1 | Phase 2 | Phase 3 | Total |
|---------|---------|---------|---------|-------|
| SRE     | ___     | ___     | ___     | ___   |
| Support | ___     | ___     | ___     | ___   |
| PM      | ___     | ___     | ___     | ___   |
| UX      | ___     | ___     | ___     | ___   |
| C-xx    | ___     | ___     | ___     | ___   |

Constraint: any role with 3+ tickets must span at least 2 phases.

---

### STEP 4 — PERFORMANCE MODE DECLARATION

Write every ticket body in first person. Use "I", "my", "we".
Do not write "the user", "the SRE", "the developer", or any third-person role reference.
If you catch yourself writing "The [role]..." — stop and rewrite as "I..."

Where a ticket is migration-related: the body may reference what the user expected from the old
approach named in Step 1B. This anchors confusion in a real prior habit rather than abstraction.

---

### STEP 5 — Vocabulary Pre-Commitment

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Migration? |
|------|-------|----------|---------|--------|----------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows: ___ (required: >= 6 and <= 12)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= 25% of total)
- High-volume count: ___ (required: <= 50% of total)
- At least 1 migration-related ticket in Phase 1: Y / N
- Phase distribution matches Step 1: MATCH / MISMATCH

---

### STEP 6 — Ticket Bodies (phase order, ascending T-ID)

```
## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[First person, 2-5 sentences. If migration-related: include one reference to what the user
expected based on the old approach named in Step 1B.]
```

---

### STEP 7 — Gap Analysis

All entries require `Tickets: T-NN, T-NN` with identifiers matching the inventory.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it

**Migration friction sub-section** (include if >= 2 tickets are migration-related):
Friction point | ticket count | what would eliminate the friction (migration guide, parity doc, redirect)

---

### STEP 8 — Verification Pass

Coverage trace:
- C-01: ... | C-02: ... | C-03: ... | C-04: ... | C-05: ...

Phase confirmation:
```
Phase 1: declared ___ / actual ___   MATCH / MISMATCH
Phase 2: declared ___ / actual ___   MATCH / MISMATCH
Phase 3: declared ___ / actual ___   MATCH / MISMATCH
```

---

## V-03 — Single Axis: Theme-First Generation

**Axis:** Declare 2-3 named themes with underlying product failures before generating tickets;
tickets are written to fit declared themes; gap analysis maps to themes and T-NNs
**Hypothesis:** Theme-first forces every ticket to derive from a named product risk; C-09 is
satisfied by construction; clusters are coherent because they were declared as design, not
discovered retrospectively.
**Baseline:** V-05 R1 + P0/P1 fixes. Phase-first organization replaced by theme-first.

---

You are generating a first-90-day support ticket forecast for: **{topic}**

Stock roles: Support, SRE, PM, UX, C-01 through C-12 (customer personas).
Ticket categories: how-to | bug | feature-request | config | integration
Volume values: high | medium | low
Severity values: P0 | P1 | P2 | P3

---

### STEP 1 — Budget Declaration

```
Total tickets: ___ (required: >= 6 and <= 12)
Number of themes: 2 or 3
```

---

### STEP 2 — Theme Declaration

Declare 2-3 named themes before generating any ticket. For each:

```
Theme A: {short name, e.g. "Activation friction"}
  Underlying product/doc failure: {what is missing or broken that generates this class}
  Roles most likely to file: {list 1-2 roles}
  Expected ticket count: N
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)

Theme B: {short name}
  Underlying product/doc failure: ...
  Roles most likely to file: ...
  Expected ticket count: N
  Phase distribution: Phase 1 (_) / Phase 2 (_) / Phase 3 (_)

[Theme C if needed — same format]
```

Constraints:
- Each theme must have a distinct underlying product/doc failure (no two themes share the same root)
- Sum of expected ticket counts must equal Step 1 total
- Each theme's phase distribution must sum to that theme's ticket count

---

### STEP 3 — Role Coverage Check

Verify that declared themes collectively satisfy role minimums:

```
SRE across all themes:     ___ (required: >= 2)
Support across all themes: ___ (required: >= 2)
PM or UX:                  ___ (required: >= 1)
C-xx across all themes:    ___ (required: >= 2, max 2 per single C-xx persona)
```

If any minimum is unmet: revise theme ticket counts or add a ticket to an existing theme.

---

### STEP 4 — PERFORMANCE MODE DECLARATION

Write every ticket body in first person. Use "I", "my", "we".
Do not write "the user", "the SRE", "the developer", or any third-person role reference.

Register guidance per theme type (adapt based on themes declared in Step 2):
- Operational/SRE-owned theme: technical vocabulary, monitoring and alerting context
- Onboarding/customer-owned theme: end-user vocabulary, no internal architecture references
- Config/integration theme: setup-step vocabulary, error code references, "I followed the docs but..."

---

### STEP 5 — Vocabulary Pre-Commitment (organized by theme)

**Theme A — {name} tickets:**
| T-ID | Title | Category | Persona | Volume | Severity | Phase |
|------|-------|----------|---------|--------|----------|-------|
| T-01 | ... | ... | ... | ... | ... | ... |

**Theme B — {name} tickets:**
| T-ID | Title | Category | Persona | Volume | Severity | Phase |
|------|-------|----------|---------|--------|----------|-------|
| T-NN | ... | ... | ... | ... | ... | ... |

[Theme C table if declared]

TABLE CHECK (across all themes combined):
- Total rows: ___ (required: >= 6 and <= 12)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= 25% of total)
- High-volume count: ___ (required: <= 50% of total)
- Theme ticket counts match Step 2 declarations: MATCH / MISMATCH

---

### STEP 6 — Ticket Bodies (by theme, ascending T-ID within each theme)

```
### Theme A — {theme name}
*Underlying failure: {one-line from Step 2}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[First person, 2-5 sentences. Voice consistent with the theme's register guidance from Step 4.]
```

---

### STEP 7 — Gap Analysis

Gap entries cite both theme context (optional) and T-NN identifiers (required).

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it

---

### STEP 8 — Verification Pass

Coverage trace:
- C-01: ... | C-02: ... | C-03: ... | C-04: ... | C-05: ...

Theme integrity check:
```
Theme A: declared ___ / actual ___   MATCH / MISMATCH
Theme B: declared ___ / actual ___   MATCH / MISMATCH
[Theme C if declared]
```

---

## V-04 — Combined: Character-Embodiment + Inertia Framing

**Axis combination:** V-01 (character-embodiment PERFORMANCE MODE) + V-02 (STATUS QUO ANALYSIS)
**Hypothesis:** Identity-embodiment and migration context reinforce each other: the persona knows
what they were doing before, which makes their confusion more specific; character-embodiment
makes migration-rooted frustration vivid rather than generic.
**Baseline:** V-05 R1 + P0/P1 fixes + both new axes combined.

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
Primary migration friction: ___
```

This analysis feeds both Phase 1 ticket content and the character backstories in Step 4.

---

### STEP 2 — Phase Map Table

| Phase | Window | Migration context | Severity norm | Volume norm |
|-------|--------|------------------|--------------|------------|
| Phase 1 | day 0-30 | Habit disruption | P2/P3 | high/medium |
| Phase 2 | day 31-60 | Hybrid / edge cases | P1/P2 | medium |
| Phase 3 | day 61-90 | Committed or churned | P0/P1 | low/medium |

---

### STEP 3 — Role Activation (SRE-First)

```
SRE: >= 2 | Support: >= 2 | PM: >= 1 | UX: >= 1 | C-xx: >= 2 (max 2 per single C-xx)
```

Role-phase cross-matrix:

| Role    | Phase 1 | Phase 2 | Phase 3 | Total |
|---------|---------|---------|---------|-------|
| SRE     | ___     | ___     | ___     | ___   |
| Support | ___     | ___     | ___     | ___   |
| PM      | ___     | ___     | ___     | ___   |
| UX      | ___     | ___     | ___     | ___   |
| C-xx    | ___     | ___     | ___     | ___   |

Constraint: any role with 3+ tickets must span at least 2 phases.

---

### STEP 4 — PERFORMANCE MODE DECLARATION (character-embodiment + migration context)

**You are about to inhabit each persona. They all know what they came from.**

**SRE character — migration context:**
You adopted {topic} because your team decided to. You knew the old approach's failure modes by
heart; {topic} is new to you. You are now discovering a gap you did not anticipate. You are
frustrated but methodical. Speak from inside that frustration.

**Support character — migration context:**
You have been fielding the same migration question all week. You know the old approach cold;
{topic} is newer to you too. You are trying to find the common thread so you can escalate it.
You are tired of not having a good answer. Speak from that position.

**PM character — migration context:**
Adoption is slower than projected. You do not know if it is a product problem or a messaging
problem. The old approach had known friction; this one has unknown friction. You need data.

**UX character — migration context:**
Users are stalling where the old approach had a familiar pattern. The new flow does not read as
the replacement it is. You can see it in the recordings. You are filing this to name the problem.

**C-xx character — migration context:**
You switched because someone recommended it or your team moved you over. You did it the old way
for a long time. Something in the new approach surprised you and you do not know if it is a bug
or if you are doing it wrong. You need an answer so you can keep moving.

**Every ticket body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Where the ticket is migration-rooted: reference what you expected based on [old approach in Step 1B].**

---

### STEP 5 — Vocabulary Pre-Commitment

| T-ID | Title | Category | Persona | Volume | Severity | Phase | Migration? |
|------|-------|----------|---------|--------|----------|-------|-----------|
| T-01 | ... | ... | ... | ... | ... | ... | Y/N |

TABLE CHECK:
- Total rows: ___ (required: >= 6 and <= 12)
- Distinct personas: ___ (required: >= 3)
- P0 count: ___ (required: <= 25% of total)
- High-volume count: ___ (required: <= 50% of total)
- At least 1 migration ticket in Phase 1: Y / N
- Phase distribution matches Step 1: MATCH / MISMATCH

---

### STEP 6 — Ticket Bodies (phase order, ascending T-ID)

```
## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[First person, 2-5 sentences. Speak as the character from Step 4 with their migration history.
If migration-flavored: include one reference to what was expected from the old approach.]
```

---

### STEP 7 — Cross-Ticket Patterns

| Pattern name | Affected tickets | Root cause | Migration-rooted? |
|-------------|-----------------|------------|------------------|
| ... | T-NN, T-NN | ... | Y/N |

---

### STEP 8 — Gap Analysis

All entries require `Tickets: T-NN, T-NN`.

**Documentation gaps**
Entry: name the gap | Tickets: T-NN, T-NN | artifact that would close it

**Design gaps**
Entry: name the gap | Tickets: T-NN, T-NN | change that would close it

**Operational gaps**
Entry: name the gap | Tickets: T-NN, T-NN | action that would close it

**Migration friction sub-section** (if >= 2 migration tickets exist):
Friction point | affected tickets | what would eliminate the friction

---

### STEP 9 — Verification Pass

Coverage trace:
- C-01: ... | C-02: ... | C-03: ... | C-04: ... | C-05: ...

Phase confirmation:
```
Phase 1: declared ___ / actual ___   MATCH / MISMATCH
Phase 2: declared ___ / actual ___   MATCH / MISMATCH
Phase 3: declared ___ / actual ___   MATCH / MISMATCH
```

---

## V-05 — Full Synthesis

**Axis combination:** V-05-R1 (phase-first + ROLE-PHASE CROSS-MATRIX) + P0/P1 fixes +
V-01 (character-embodiment) + V-02 (inertia framing) + V-03 (theme-first) + STEP 7B resolution
paths (C-10)
**Hypothesis:** Five axes address five distinct generation-time failure modes without conflict:
(1) phase-first prevents temporal clustering, (2) role-matrix prevents role concentration,
(3) character-embodiment prevents third-person drift, (4) inertia framing generates
migration-specific tickets, (5) theme-first forces coherent clusters. Resolution path
step targets C-10 aspirational. This variation is the golden candidate.

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
| Phase 3 | day 61-90 | Committed or churned | P0/P1 | low/medium | "We've been running this for two months and now something serious broke" |

**Phase-severity inference rule:** Assign from the norm column. Explicit override only if the
specific failure is unambiguously more or less severe than the phase norm.

---

### STEP 2B — Phase Body Template Table

Commit to one sentence template per phase per role before writing bodies.
These are vocabulary anchors — expand into full bodies, not copy-paste.

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
Constraint 2: Any role with 3+ tickets must span at least 2 phases (C-12)
Constraint 3: Any single C-xx persona in at most 2 tickets

---

### STEP 4 — PERFORMANCE MODE DECLARATION (character-embodiment + migration context)

**You are about to become each persona. They know what they migrated from.**

**SRE:** You're on-call. You adopted {topic} because the team moved to it. You knew the prior
system's failure modes cold; this one is still opaque to you. Something is now breaking silently
that you would have caught immediately in the old system. You are methodical but frustrated.

**Support:** You've answered this same migration question multiple times this week. You know what
the old approach expected; {topic} does something different that users keep tripping over. You
are filing this ticket to get the engineering team to fix the root cause so you can stop answering it.

**PM:** Adoption is below forecast. You cannot tell if it is a product problem or a communication
problem. You are filing this to request data that would help you decide which to address first.

**UX:** You are watching session recordings and seeing users stall at a specific point. The old
approach had a familiar affordance here; the new one does not. You know the friction point by
location; you need engineering to understand the root cause.

**C-xx:** You switched from [old approach named in Step 1B] recently. Something surprised you —
either something that used to work stopped working, or something you expected to just work
required extra setup. You do not know if it is a bug or if you are doing it wrong.

**Every body: first person. "I", "my", "we". Never "the SRE", "the user", "the developer".
Where migration-relevant: reference what was expected from the old approach.**

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

```
### Theme A — {theme name}
*Underlying failure: {from Step 3}*

## T-NN — {Title}
- Category: ... | Persona: ... | Volume: ... | Severity: ... | Phase: Phase N (day X-Y)

**Ticket body:**
[First person, 2-5 sentences. Embody the character from Step 4.
Use the phase body anchor from Step 2B as the sentence scaffold.
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
  Phase 1 tickets at P2/P3: ___ of ___   (required: >= 60%)
  At least 1 Phase 3 ticket at P0/P1: Y / N

Broken T-NN refs in gap entries: ___   (required: 0)
Resolution paths complete for all qualifying tickets: Y / N
```

If any check fails: revise before submitting.

---

## Variation Summary

| ID | Primary axis | Secondary axis | New vs R1 V-05 |
|----|-------------|---------------|----------------|
| V-01 | Phrasing register (character-embodiment) | — | PERFORMANCE MODE rewrites prohibition as character inhabitation; personas have backstory and emotional state |
| V-02 | Inertia framing (status-quo competitor) | — | STEP 1B STATUS QUO ANALYSIS added; migration context column in phase map; gap analysis has migration sub-section |
| V-03 | Theme-first generation | — | THEME DECLARATION before ticket generation; tickets organized by theme; vocab table split by theme |
| V-04 | Character-embodiment | Inertia framing | V-01 + V-02 combined; migration history feeds persona backstory for richer first-person voice |
| V-05 | All axes (full synthesis) | + resolution path | V-05-R1 + all R2 axes + STEP 7B resolution paths; candidate for golden |

**Expected R2 composite for V-05:** ~88 (vs R1 V-05 baseline of 75.5)
- C-03: PASS (character-embodiment + first-person mandate, both present)
- C-04: PASS (T-NN format required in all gap sections)
- C-06: PASS (<= 12 upper bound enforced in TABLE CHECK)
- C-09: PASS (themes declared before generation — satisfied by construction)
- C-10: PASS (STEP 7B resolution paths for high-volume/P0/P1 tickets)
- C-11: PASS (dual-pass verification checks zero broken T-NN refs)
- C-12: PASS (role-phase cross-matrix constraint 2)
- C-13: PASS (pass 2 structural property check)
