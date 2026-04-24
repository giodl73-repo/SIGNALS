Written to `simulations/quest/variations/listen-support-variations-R1-2026-03-14.md`.

---

## Round 1 Variations -- Summary

| V | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Output format (per-ticket cards) | Pre-printed fields make C-01/C-02/C-03 structurally unavoidable; body as a named section eliminates table-cell truncation path |
| **V-02** | Role sequence (Support lists, PM rates, SRE validates) | Separating listing from rating prevents "all-high" volume stamps; PM rationale column is the lightest C-07 fix; SRE pass surfaces P0/P1 escalations structurally |
| **V-03** | Lifecycle emphasis (3 phase windows) | Phase-gated generation varies volume and category without per-ticket rationale; Phase 1=high/how-to-bug, Phase 2=medium/config-integration, Phase 3=low/feature-request |
| **V-04** | Axes 1+2 (cards + role-labeled fields per card) | Cards kill the body-omission path; PM rationale co-located in every card is hardest to skip; strongest C-01..C-08 without phase overhead |
| **V-05** | Full synthesis (STATUS QUO + phases + role-labeled cards) | STATUS QUO anchors C-07 volume predictions and creates the C-09 root-cause trace; phase windows force C-05 spread; role-labeled cards lock C-03/C-06/C-07 |

**Key structural insight:** The C-07 failure mode (all tickets stamped "high") has three independent remedies tested here -- explicit rationale field (V-02), phase gradient (V-03), and co-located rationale in card (V-04). V-05 layers all three. Round 2 should isolate which is load-bearing.

**Predicted ceiling:** V-05. **Strongest non-combination:** V-04.
y-omission path that consolidated tables allow (body gets truncated in table cells)
- PM volume rationale fields (V-02/V-04/V-05) are the primary C-07 mechanism -- forcing a rationale prevents blanket "high" stamps
- Phase windows (V-03/V-05) are the structural C-07 path without requiring explicit rationale fields; volume follows phase pattern
- STATUS QUO (V-05) is the C-09 enabler -- cross-ticket patterns trace to STATUS QUO workarounds without requiring model-discretion insight

**Predicted ceiling:** V-05 -- maximum structural coverage for all 10 criteria.
**Strongest non-combination competitor:** V-04 -- card format + role-labeled fields without phase overhead.
**Minimum viable for C-07:** V-02 -- PM rationale column is the lightest intervention that differentiates volume.

---

## V-01: Output Format (Per-Ticket Cards)

**Axis:** Output format -- each ticket is a structured card with all 5 required fields as named
labels, body as an explicitly named field with persona-voice instruction, not a table column
**Hypothesis:** Pre-printed per-ticket cards structurally prevent C-01 field omissions -- each
field is a named label the model must fill. The body as a named section (not a truncated table
cell) forces the model to write a full persona-authentic response. Consolidated tables allow the
model to abbreviate the body or drop it entirely. The C-02 vocabulary reminder is embedded in
every field label as a constrained value set, preventing out-of-vocabulary entries.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. All ticket cards are pre-printed. Fill every field in every card.
Do not skip, collapse, merge, or reorder any card or field.
Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration};
severity in {P0, P1, P2, P3}; volume in {high, medium, low}.
Stock roles for persona field: Support, SRE, PM, UX, C-01 through C-12.

---

## SETUP
Topic: [Feature or product being analyzed.]
Signal: [Artifact being used as input.]
Prediction window: 90 days post-launch.

## TICKET CARDS
[Predict at least 5 tickets. Cover at least 3 distinct category values across all cards.
Fill every field in every card. Do not omit any field or leave a field blank.]

### Ticket T-01
Title: [One sentence. Specific enough to route to the right team.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [One of: Support, SRE, PM, UX, C-01, C-02, C-03, C-04, C-05, C-06,
          C-07, C-08, C-09, C-10, C-11, C-12]
Volume: [high | medium | low]
Severity: [P0 | P1 | P2 | P3]
Body:
> [Sample ticket text written in first person, in the persona's voice. Use vocabulary, concerns,
> and framing specific to this persona. SRE: operational/infra language. PM: roadmap/metrics/impact
> language. C-XX: that persona's domain and pain. Minimum 3 sentences. Do not write a generic body
> that would fit any persona equally well.]

### Ticket T-02
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role -- see list above.]
Volume: [high | medium | low]
Severity: [P0 | P1 | P2 | P3]
Body:
> [First-person ticket in persona's voice. Role-specific vocabulary required.]

### Ticket T-03
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role -- see list above.]
Volume: [high | medium | low]
Severity: [P0 | P1 | P2 | P3]
Body:
> [First-person ticket in persona's voice. Role-specific vocabulary required.]

### Ticket T-04
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role -- see list above.]
Volume: [high | medium | low]
Severity: [P0 | P1 | P2 | P3]
Body:
> [First-person ticket in persona's voice. Role-specific vocabulary required.]

### Ticket T-05
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role -- see list above.]
Volume: [high | medium | low]
Severity: [P0 | P1 | P2 | P3]
Body:
> [First-person ticket in persona's voice. Role-specific vocabulary required.]

[Add T-06, T-07, ... as needed. Same format -- all fields required in every card.]

## CATEGORY COVERAGE CHECK
Categories used: [List distinct category values from all cards above.]
Count: [N distinct categories. Must be >= 3. If fewer, add cards until >= 3 are covered.]

## VOLUME CHECK
Volume ratings used: [List distinct volume values from all cards above.]
Absent level (if any): [high | medium | low] -- Reason: [One sentence why this level is not represented.]
[If all cards share the same volume value, revise at least two cards before proceeding.]

## GAP ANALYSIS

### Doc Gaps
[At least one specific documentation gap. Name the missing doc, guide, or reference,
and which ticket ID(s) it would prevent.]
- [Gap: what is missing and which ticket(s) it would prevent.]
[Add rows as needed.]

### Design Gaps
[At least one specific design gap. Name the missing UX affordance, error state, or
behavioral contract, and which ticket ID(s) it drives.]
- [Gap: what is missing and which ticket(s) it drives.]
[Add rows as needed.]

### Operational Gaps
[At least one specific operational gap. Name the missing runbook, alert, dashboard,
or deployment check, and which ticket ID(s) it drives.]
- [Gap: what is missing and which ticket(s) it drives.]
[Add rows as needed.]

### Priority Close Order
[Rank all gaps by severity and volume of tickets they would prevent. One sentence per ranked gap.]
1. [Highest-priority gap] -- prevents: [ticket IDs with severity and volume.]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Identify at least one systemic pattern across multiple ticket cards. Name it explicitly and
cite specific ticket IDs or titles. Example: "T-01, T-03, and T-04 all trace to missing error
guidance for the config namespace -- one doc addition covers three distinct ticket categories."]
Pattern: [Name] -- tickets: [IDs] -- root cause: [One sentence.]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count.
```

---

## V-02: Role Sequence (Support-Triage-First, PM Rates, SRE Validates)

**Axis:** Role sequence -- Support generates ticket list first (title, category, persona only),
PM adds volume and severity with explicit rationale in a second pass, SRE reviews operational
severity in a third pass; ticket bodies come after all ratings are locked
**Hypothesis:** Separating the listing pass (Support) from the rating pass (PM) prevents the model
from locking in "high" volume while listing tickets. The PM volume-rationale column forces the
model to consider the affected user population and ask frequency before committing to a rating --
the leading failure mode for C-07. The SRE third pass identifies which tickets describe service
outages or data-loss scenarios and escalates severity, giving C-06 a structural mechanism beyond
model discretion. Ticket bodies come last, after personas are locked, so the model is not
distracted by voice when deciding category and severity.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. Three role passes run in sequence.
All section headers are fixed. Do not reorder, rename, or remove any section header or template fragment.
Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration};
severity in {P0, P1, P2, P3}; volume in {high, medium, low}.
Stock roles for persona field: Support, SRE, PM, UX, C-01 through C-12.

---

## SETUP
Topic: [Feature or product being analyzed.]
Signal: [Artifact being used as input.]
Prediction window: 90 days post-launch.

## SUPPORT: TICKET TRIAGE LIST
[Support role generates the ticket list. Focus on what will actually arrive in the queue.
For each ticket: title, category, and persona only. Do not add volume or severity here.
Predict at least 5 tickets. Cover at least 3 distinct category values.]

| ID   | Title     | Category                                            | Persona      |
|------|-----------|-----------------------------------------------------|--------------|
| T-01 | [Title]   | [how-to|bug|feature-request|config|integration]    | [stock role] |
| T-02 | [Title]   | [how-to|bug|feature-request|config|integration]    | [stock role] |
| T-03 | [Title]   | [how-to|bug|feature-request|config|integration]    | [stock role] |
| T-04 | [Title]   | [how-to|bug|feature-request|config|integration]    | [stock role] |
| T-05 | [Title]   | [how-to|bug|feature-request|config|integration]    | [stock role] |
[Add rows as needed. Minimum 5. At least 3 distinct category values required.]

## PM: VOLUME AND SEVERITY RATINGS
[PM role adds volume and severity to each ticket from the Support list above.
Volume rationale required -- cite affected user population size and ask frequency.
Severity rationale required -- P0/P1 means feature is broken or inaccessible; P2/P3 means
workaround available or impact is cosmetic. Do not assign all tickets the same volume level.]

| ID   | Volume            | Volume Rationale                               | Severity | Severity Rationale                       |
|------|-------------------|------------------------------------------------|----------|------------------------------------------|
| T-01 | [high|medium|low] | [Who hits this and how often?]                 | [P0-P3]  | [Why this severity level?]               |
| T-02 | [high|medium|low] | [Rationale]                                    | [P0-P3]  | [Rationale]                              |
| T-03 | [high|medium|low] | [Rationale]                                    | [P0-P3]  | [Rationale]                              |
| T-04 | [high|medium|low] | [Rationale]                                    | [P0-P3]  | [Rationale]                              |
| T-05 | [high|medium|low] | [Rationale]                                    | [P0-P3]  | [Rationale]                              |
[Mirror all ticket IDs from the Support list. Do not omit any row.]

Volume coverage: [List distinct volume values used. If only one value appears, revise before proceeding.]

## SRE: OPERATIONAL SEVERITY REVIEW
[SRE role reviews for operational-class issues: service outage, data loss, degraded API behavior,
failed deployment. Flag any such ticket and confirm or escalate its PM-assigned severity.
If no escalation, state why the PM rating is correct for each candidate ticket.]

Flagged tickets: [List T-IDs with service-class impact, or "None" if none apply.]
Severity escalations: [For each flagged ticket: PM severity -> SRE severity, one-sentence rationale.]
Pre-launch SRE needs: [One sentence: what runbook, alert, or rollback procedure the SRE team needs
before launch to handle the operationally-flagged tickets above.]

## TICKET BODIES
[Write a sample ticket body for each ticket in the Support list.
First person, in the persona's voice. Role-specific vocabulary, concerns, and framing required.
Do not write generic bodies -- a body that fits any persona equally well fails this step.]

### T-01: [Title]
Persona: [From Support list]
> [First-person body in persona's voice. Minimum 3 sentences. Role-specific language required.]

### T-02: [Title]
Persona: [From Support list]
> [First-person body in persona's voice. Role-specific language required.]

### T-03: [Title]
Persona: [From Support list]
> [First-person body in persona's voice. Role-specific language required.]

### T-04: [Title]
Persona: [From Support list]
> [First-person body in persona's voice. Role-specific language required.]

### T-05: [Title]
Persona: [From Support list]
> [First-person body in persona's voice. Role-specific language required.]

[Add bodies for any additional tickets. Same format.]

## GAP ANALYSIS

### Doc Gaps
- [Gap 1: specific missing doc or guide, and which ticket(s) it would prevent.]
[Add as needed.]

### Design Gaps
- [Gap 1: specific missing UX affordance, error state, or behavioral contract, and which ticket(s) it drives.]
[Add as needed.]

### Operational Gaps
- [Gap 1: specific missing runbook, alert, or deployment check, and which ticket(s) it drives.]
[The SRE pre-launch needs statement above should inform at least one gap here.]
[Add as needed.]

### Priority Close Order
1. [Highest-priority gap] -- prevents: [ticket IDs, with severity and volume from PM ratings.]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count.
```

---

## V-03: Lifecycle Emphasis (90-Day Window Split into Three Phases)

**Axis:** Lifecycle emphasis -- the 90-day prediction window is divided into three explicit phases,
each with its own ticket table and dominant-volume declaration; overall coverage checks run after
all phases complete
**Hypothesis:** Phase-gated ticket generation naturally varies volume and category without requiring
explicit rationale fields. Phase 1 (launch chaos) produces how-to and bug tickets at high volume.
Phase 2 (learning curve) produces config and integration tickets at medium volume as the population
stabilizes. Phase 3 (advanced use) produces feature-request tickets at low volume from a smaller
expert cohort. Volume differentiation (C-07) and category spread (C-05) become structural outputs
of the phase architecture rather than relying on model discretion. Cross-ticket patterns (C-09)
emerge naturally when tickets across phases share a root cause -- the phase labels make this visible.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. The 90-day prediction window is divided into three phases.
Generate ticket predictions for each phase. All section headers are fixed. Do not reorder or remove sections.
Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration};
severity in {P0, P1, P2, P3}; volume in {high, medium, low}.
Stock roles for persona field: Support, SRE, PM, UX, C-01 through C-12.

---

## SETUP
Topic: [Feature or product being analyzed.]
Signal: [Artifact being used as input.]

## PHASE 1: LAUNCH WEEK (Days 1-14)
[First adopters and internal users. Setup friction, missing prerequisites, unclear error messages.
Expect how-to and bug tickets at high volume as users hit the first wall.
Generate at least 2 tickets for this phase.]

| ID   | Title   | Category                                            | Persona      | Volume            | Severity |
|------|---------|-----------------------------------------------------|--------------|-------------------|----------|
| T-01 | [Title] | [how-to|bug|feature-request|config|integration]    | [stock role] | [high|medium|low] | [P0-P3]  |
| T-02 | [Title] | [how-to|bug|feature-request|config|integration]    | [stock role] | [high|medium|low] | [P0-P3]  |
[Add Phase 1 rows as needed. Use categories that fit early-adoption patterns.]

Phase 1 dominant volume: [high | medium | low]
Rationale: [One sentence: why this volume level fits the launch-week user population and behavior.]

## PHASE 2: LEARNING CURVE (Days 15-60)
[Core user population has onboarded. Configuration variations, integration failures, and edge cases emerge.
Volume decreases from Phase 1 as the most common issues are resolved or documented.
Expect config and integration tickets at medium volume.
Generate at least 2 tickets for this phase.]

| ID   | Title   | Category                                            | Persona      | Volume            | Severity |
|------|---------|-----------------------------------------------------|--------------|-------------------|----------|
| T-03 | [Title] | [how-to|bug|feature-request|config|integration]    | [stock role] | [high|medium|low] | [P0-P3]  |
| T-04 | [Title] | [how-to|bug|feature-request|config|integration]    | [stock role] | [high|medium|low] | [P0-P3]  |
[Add Phase 2 rows as needed. Use categories that fit post-onboarding patterns.]

Phase 2 dominant volume: [high | medium | low]
Rationale: [One sentence: why this volume level differs from Phase 1.]

## PHASE 3: ADVANCED USE (Days 61-90)
[Power users, edge workflows, feature gaps at scale. Small expert population generates low-volume
feature-request and advanced-config tickets.
Generate at least 1 ticket for this phase.]

| ID   | Title   | Category                                            | Persona      | Volume            | Severity |
|------|---------|-----------------------------------------------------|--------------|-------------------|----------|
| T-05 | [Title] | [how-to|bug|feature-request|config|integration]    | [stock role] | [high|medium|low] | [P0-P3]  |
[Add Phase 3 rows as needed. Use categories that fit advanced-use patterns.]

Phase 3 dominant volume: [high | medium | low]
Rationale: [One sentence: why this volume level fits the advanced-use population.]

## TICKET BODIES
[For each ticket above, write a sample body in the persona's voice.
First person. Role-specific vocabulary and framing required. Do not write generic bodies.]

### T-01: [Title] (Phase 1)
Persona: [From Phase 1 table]
> [First-person body in persona's voice. Minimum 3 sentences. Role-specific language required.]

### T-02: [Title] (Phase 1)
Persona: [From Phase 1 table]
> [First-person body in persona's voice. Role-specific language required.]

### T-03: [Title] (Phase 2)
Persona: [From Phase 2 table]
> [First-person body in persona's voice. Role-specific language required.]

### T-04: [Title] (Phase 2)
Persona: [From Phase 2 table]
> [First-person body in persona's voice. Role-specific language required.]

### T-05: [Title] (Phase 3)
Persona: [From Phase 3 table]
> [First-person body in persona's voice. Role-specific language required.]

[Add bodies for all additional tickets. Same format.]

## COVERAGE CHECKS

Volume coverage: Phase 1 = [value] | Phase 2 = [value] | Phase 3 = [value]
Distinct volume levels: [Count. Must be >= 2. If all three phases share the same level, explain why.]

Category coverage: [List distinct category values across all phases.]
Distinct categories: [Count. Must be >= 3. If fewer, add tickets before proceeding.]

## GAP ANALYSIS

### Doc Gaps
[Reference which phase each gap fires in. Phase 1 gaps typically rank higher in priority close order.]
- [Gap 1: missing doc or guide, which ticket(s) it prevents, which phase.]
[Add as needed.]

### Design Gaps
- [Gap 1: missing UX affordance or behavioral contract, which ticket(s) it drives, which phase.]
[Add as needed.]

### Operational Gaps
- [Gap 1: missing runbook or operational readiness item, which ticket(s) it drives, which phase.]
[Add as needed.]

### Priority Close Order
[Rank by severity and volume of prevented tickets. Phase 1 gaps typically rank first -- explain if not.]
1. [Highest-priority gap] -- prevents: [ticket IDs, phase, severity, volume.]
2. [Second-priority gap] -- prevents: [ticket IDs, phase.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Identify at least one systemic pattern that spans two or more phases. Name it and cite ticket IDs with phase labels.]
Pattern: [Name] -- tickets: [T-01 (P1), T-03 (P2), ...] -- root cause: [What makes this pattern persist
across the 90-day window? One sentence.]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count.
```

---

## V-04: Axes 1+2 (Per-Ticket Cards + Role-Labeled Fields Within Each Card)

**Axes:** Output format (per-ticket cards, V-01 axis) + role sequence (role-labeled fields inside
each card, V-02 axis)
**Hypothesis:** Per-ticket cards eliminate the body-omission path from table formats. Role-labeled
fields inside each card -- Support triage, PM rating, ticket body -- enforce the separation of
concerns without requiring a separate pass. The PM volume rationale field is a named required
element in every card, preventing the model from stamping "high" without justification (C-07).
The ticket body is clearly marked as persona-voiced and co-located with the persona label (C-08).
Combined, these two axes give the strongest structural coverage of C-01 through C-08 without
the overhead of phase windows or a STATUS QUO section.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. Each ticket is a structured card with role-labeled sections.
All card fields are required. Do not skip, merge, or reorder any section or field.
Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration};
severity in {P0, P1, P2, P3}; volume in {high, medium, low}.
Stock roles for persona field: Support, SRE, PM, UX, C-01 through C-12.

---

## SETUP
Topic: [Feature or product being analyzed.]
Signal: [Artifact being used as input.]
Prediction window: 90 days post-launch.

## TICKET CARDS
[Predict at least 5 tickets. Cover at least 3 distinct category values across all cards.
Each card has three role-labeled sections: Support triage, PM rating, and ticket body.
All three sections are required in every card.]

### Ticket T-01

**Support: Triage**
Title: [One sentence. Specific enough to route to the right team.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role: Support, SRE, PM, UX, or C-01 through C-12]

**PM: Rating**
Volume: [high | medium | low]
Volume rationale: [One sentence: how large is the affected user population? How frequently does
this situation arise in the first 90 days?]
Severity: [P0 | P1 | P2 | P3]
Severity rationale: [One sentence: is the feature broken or inaccessible (P0/P1), or is a
workaround available and impact is lower (P2/P3)?]

**Ticket Body**
[Write in first person, in the persona's voice named in the Support triage section above.
Use vocabulary, concerns, and framing specific to this persona. SRE: operational/infra language.
PM: roadmap/metrics/user-impact language. C-XX: that persona's domain and business pain.
Minimum 3 sentences. Do not write a body that fits any persona equally well.]
> [Body text here.]

---

### Ticket T-02

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low]
Volume rationale: [One sentence.]
Severity: [P0 | P1 | P2 | P3]
Severity rationale: [One sentence.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

### Ticket T-03

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low]
Volume rationale: [One sentence.]
Severity: [P0 | P1 | P2 | P3]
Severity rationale: [One sentence.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

### Ticket T-04

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low]
Volume rationale: [One sentence.]
Severity: [P0 | P1 | P2 | P3]
Severity rationale: [One sentence.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

### Ticket T-05

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low]
Volume rationale: [One sentence.]
Severity: [P0 | P1 | P2 | P3]
Severity rationale: [One sentence.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add T-06, T-07, ... for additional tickets. Same three-section structure required in every card.]

## COVERAGE CHECKS

Category coverage: [List distinct category values from all cards. Must be >= 3.]
Volume coverage: [List distinct volume values from all cards.]
Absent volume level (if any): [Reason -- one sentence. If all cards share the same volume, revise at least two.]

## GAP ANALYSIS

### Doc Gaps
[At least one gap. Name the missing doc, guide, or reference. Reference ticket ID(s) it prevents.]
- [Gap: what is missing and which ticket(s) it prevents.]
[Add as needed.]

### Design Gaps
[At least one gap. Name the missing UX affordance, error state, or behavioral contract. Reference ticket ID(s).]
- [Gap: what is missing and which ticket(s) it drives.]
[Add as needed.]

### Operational Gaps
[At least one gap. Name the missing runbook, alert, dashboard, or deployment check. Reference ticket ID(s).]
- [Gap: what is missing and which ticket(s) it drives.]
[Add as needed.]

### Priority Close Order
[Rank all gaps by severity and volume from the PM rating fields in the ticket cards above. Show reasoning.]
1. [Highest-priority gap] -- prevents: [ticket IDs with severity and volume from PM: Rating fields.]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Identify at least one systemic pattern across multiple ticket cards. Name it and cite ticket IDs.]
Pattern: [Name] -- tickets: [IDs] -- root cause: [One sentence.]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count.
```

---

## V-05: Full Synthesis (STATUS QUO + Phase Windows + Role-Labeled Cards)

**Axes:** Inertia framing (STATUS QUO section first) + lifecycle emphasis (three phase windows,
V-03 axis) + role-labeled per-ticket cards (V-04 axis)
**Hypothesis:** Maximum structural coverage of all 10 criteria. STATUS QUO grounds volume ratings
before the first ticket is generated: high workaround friction -> high Phase 1 volume (C-07 path).
STATUS QUO also surfaces the C-09 cross-ticket pattern: root causes trace to current workarounds
being inadequate, and the pattern is named at the end. Phase windows force category spread and
natural volume graduation across phases (C-05, C-07). Role-labeled cards within each phase make
C-03, C-06, and C-07 structurally unavoidable -- PM volume rationale and persona tag are
pre-printed fields. Gap analysis priority close order is tied to ticket data by ID, severity, and
volume (C-10). The "Not closing this means:" line forces a consequence statement at the end.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. STATUS QUO section runs first. The 90-day window is
divided into three phases. Each ticket is a structured card with role-labeled sections.
All section headers and card fields are required. Do not reorder or remove any section.
Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration};
severity in {P0, P1, P2, P3}; volume in {high, medium, low}.
Stock roles for persona field: Support, SRE, PM, UX, C-01 through C-12.

---

## SETUP
Topic: [Feature or product being analyzed.]
Signal: [Artifact being used as input.]

## STATUS QUO: CURRENT SUPPORT LANDSCAPE
[Complete before generating any tickets. Grounds volume ratings and body authenticity below.
If the status quo varies by persona type, note the dominant pattern and flag exceptions.]

Current workaround: [What do users do today when they hit a problem with this feature or something
similar? One sentence per distinct workaround behavior.]
Support channel today: [Where do users go first -- Slack, docs, GitHub Issues, Stack Overflow,
internal wiki, or no channel? Be specific.]
Workaround friction: [high | medium | low]
Doc gap today: [What doc, guide, or example users currently cannot find. One sentence. State "unknown" if unclear.]
Volume anchor: [One sentence connecting STATUS QUO friction to Phase 1 volume predictions.
Example: "High workaround friction + no existing doc = high volume for how-to and config tickets
in Phase 1, decreasing to medium as workarounds are documented."]

## PHASE 1: LAUNCH WEEK (Days 1-14)

[First adopters hit setup and prerequisite walls. Volume shaped by STATUS QUO workaround friction.
High friction -> expect high-volume how-to and bug tickets. Generate at least 2 tickets.]

### T-01 (Phase 1)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence: reference STATUS QUO friction and affected population.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence: broken/inaccessible (P0/P1) or workaround available (P2/P3)?]

**Ticket Body**
> [First-person body in persona's voice. Reference what they tried, what failed, what they need.
> Role-specific vocabulary required. SRE: ops/infra language. C-XX: domain and business context.
> PM: impact/metrics framing. Minimum 3 sentences. Not a generic body.]

---

### T-02 (Phase 1)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence rationale; reference STATUS QUO if applicable.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add T-03 and beyond for Phase 1 if needed. Same card structure.]

## PHASE 2: LEARNING CURVE (Days 15-60)

[Core population has onboarded. Config variations, integration failures, edge cases emerge.
Volume decreases from Phase 1. Generate at least 2 tickets.]

### T-03 (Phase 2)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence; explain shift from Phase 1 if volume differs.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

### T-04 (Phase 2)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence rationale.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add more Phase 2 tickets as needed.]

## PHASE 3: ADVANCED USE (Days 61-90)

[Power users, edge workflows, feature gap discovery. Small expert population; volume is lower.
Generate at least 1 ticket.]

### T-05 (Phase 3)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence; explain why lower than Phase 1.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add more Phase 3 tickets as needed.]

## COVERAGE CHECKS

Category coverage: [List distinct category values across all phases. Must be >= 3. If fewer, add tickets.]
Volume coverage: Phase 1 = [value] | Phase 2 = [value] | Phase 3 = [value]
Distinct volume levels: [Count. Must be >= 2. If all phases share one level, explain why.]
Phase distribution: Phase 1: [N] | Phase 2: [N] | Phase 3: [N] | Total: [N]

## GAP ANALYSIS

### Doc Gaps
[Reference STATUS QUO doc gap. Tie each gap to ticket IDs and phase. Phase 1 gaps typically rank highest.]
- [Gap 1: missing doc, which ticket(s) it drives, which phase(s) it fires in.]
[Add as needed.]

### Design Gaps
- [Gap 1: missing UX affordance or behavioral contract, which ticket(s), which phase.]
[Add as needed.]

### Operational Gaps
[Reference STATUS QUO support channel if the channel itself is the gap.]
- [Gap 1: missing operational element, which ticket(s), which phase.]
[Add as needed.]

### Priority Close Order
[Rank by severity and volume of tickets prevented. Phase 1 gaps typically rank first -- explain if not.
Tie each ranked gap to STATUS QUO root cause where applicable.]
1. [Highest-priority gap] -- prevents: [ticket IDs, phase, severity, volume.] -- STATUS QUO root: [one sentence.]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Identify at least one systemic pattern spanning two or more phases, traceable to STATUS QUO behavior.
Name the pattern. Cite ticket IDs with phase labels. Connect to the STATUS QUO root cause.]
Pattern: [Name] -- tickets: [T-01 (P1), T-03 (P2), ...] -- root cause: [One sentence tracing to the
STATUS QUO workaround, channel gap, or doc gap identified above.]
Not closing this means: [What the support queue looks like at day 90 if this pattern is unaddressed.
One sentence. Reference STATUS QUO behavior if applicable.]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, status_quo_friction.
```

---

## Round 1 Design Notes

### Axis selection rationale

Three single-axis variations chosen: output format (V-01), role sequence (V-02), lifecycle emphasis
(V-03). Output format tests whether per-ticket cards eliminate the body-omission and volume-blanket
failure modes that consolidated tables enable. Role sequence tests whether separating listing from
rating produces better volume differentiation without requiring structural phase overhead. Lifecycle
emphasis tests whether phase-gated generation produces C-05 and C-07 coverage structurally, without
requiring explicit rationale fields per ticket.

Phrasing register was not chosen as a single axis because no rubric criterion is sensitive to
formal vs. conversational language -- all criteria test field completeness, vocabulary compliance,
persona accuracy, and structural coverage. Inertia framing was reserved for V-05 because STATUS QUO
adds the most overhead; testing it in isolation would use a variation slot better occupied by a
more targeted intervention.

### C-07 structural comparison

| V  | C-07 mechanism                                          | Failure path                                         |
|----|--------------------------------------------------------|------------------------------------------------------|
| V-01 | No explicit rationale; volume is a card field       | Model stamps all cards "high"                        |
| V-02 | PM volume rationale column required per ticket      | Rationale without differentiation still fails        |
| V-03 | Phase dominant-volume declaration + rationale       | Phase pattern enforces gradient without per-ticket work |
| V-04 | PM volume rationale inside every card               | Hardest to ignore; co-located with the decision      |
| V-05 | STATUS QUO volume anchor + phase gradient + card rationale | Maximum structural pressure; three layers       |

### C-03 structural comparison

| V  | C-03 mechanism                                           | Omission path                                  |
|----|----------------------------------------------------------|------------------------------------------------|
| V-01 | Named body field in card; persona label above          | No vocabulary instruction per field            |
| V-02 | Body section after personas locked; per-persona instructions | Model may still write generic bodies      |
| V-03 | Body section per ticket; persona from phase table      | Same as V-02                                   |
| V-04 | Body section labeled; persona in same card; explicit instruction | Persona and instruction are co-located  |
| V-05 | Same as V-04 + STATUS QUO context grounds realistic body | Maximum grounding                             |

### C-09 structural comparison

C-09 passes when at least one named cross-ticket pattern with explicit ticket references appears.
V-01 and V-02 can produce C-09 through model discretion but have no structural scaffold.
V-03 creates the phase-span condition structurally: phase labels make cross-phase patterns
visible. V-05 adds the STATUS QUO root-cause trace, which is the strongest C-09 mechanism --
patterns that trace to current workarounds are more specific and harder to avoid than generic
"these tickets share a root cause" statements.

### V-golden candidate

**V-05** is the direct synthesis target:
- STATUS QUO anchors volume predictions (C-07 path) and cross-ticket patterns (C-09 path)
- Phase windows force category spread and natural volume graduation (C-05, C-07)
- Role-labeled cards make C-03/C-06/C-07 structurally unavoidable
- Priority close order tied to ticket data by ID and phase (C-10 path)
- "Not closing this means:" line forces a consequence statement at the CROSS-TICKET PATTERN section

**V-04** is the strongest structural competitor for C-01..C-08 without phase or STATUS QUO overhead.
Key open question for Round 2: does the STATUS QUO section in V-05 produce measurably better C-07
coverage (volume differentiation across cards within a phase), or does the PM rationale field in V-04
achieve the same differentiation without the STATUS QUO section? Phase windows vs. per-card
rationale is the critical experiment to resolve.
