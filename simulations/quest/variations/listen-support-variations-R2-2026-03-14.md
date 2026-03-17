Written to `simulations/quest/variations/listen-support-variations-R2-2026-03-14.md`.

---

## Round 2 Variations -- listen-support

| V | Axis | Hypothesis |
|---|------|------------|
| **V-01** | STATUS QUO isolation (V-04 R1 base + STATUS QUO, no phases) | Isolates whether STATUS QUO alone -- without phase overhead -- drives C-07/C-08 improvement and passes C-11 via instruction-only citation requirement |
| **V-02** | C-11 traceability enforcement (named `STATUS QUO connection:` field per card) | A named required field eliminates the floating-preamble C-11 failure mode; traceability is structural, not discretionary |
| **V-03** | C-12 consequence specificity (three-part consequence: affected segment + day-90 scenario + adoption cost) | Three-part structure makes generic "this will cause confusion" structurally impossible; each part requires naming specifics of the named pattern |
| **V-04** | V-02 R1 recovery (role sequence + STATUS QUO + CROSS-TICKET PATTERN + three-part consequence) | V-02 R1 was 87 with one structural miss (C-09); three targeted additions recover to 100+ while retaining the SRE escalation pass that uniquely strengthens C-06 |
| **V-05** | Full synthesis R2 (V-05 R1 + named connection field + three-part consequence + traceability coverage check) | All 12 criteria enforced structurally; ceiling 110/110 |

**Key design choices:**
- V-01 and V-02 are isolating experiments that answer whether STATUS QUO or the named connection field is the load-bearing C-11 mechanism
- V-03 is the isolated C-12 experiment against V-05 R1 as baseline
- V-04 tests the role-sequence path to 100+ -- a structurally different route from V-04/V-05 R1
- V-05 combines all winning mechanisms; the traceability coverage check is a post-generation verification gate that catches C-11 failures before the output is finalized
eliably -- a named connection field (V-02) or instruction-only STATUS QUO grounding (V-01)? (V-01 vs. V-02 comparison answers this.)
- Does a three-part consequence structure (V-03) produce measurably more specific C-12 output than V-05 R1's single line? (V-03 vs. V-05 R1 baseline answers this.)
- Can the role-sequence path (V-04) close the gap to 100+ once C-09 and C-12 structural misses are corrected? (V-04 answers this.)

**R1 baseline scores for context:**
V-05=100, V-04=97, V-02=87, V-03=86, V-01=84 (out of 100 on v1 rubric, 10-pt aspirational ceiling).
On v2 rubric (110-pt ceiling): R1 V-05 likely scores ~100-103 -- C-11 may partially pass
(STATUS QUO present in instructions but no per-card enforcement), C-12 may partially pass
(consequence line present but no specificity structure required).

---

## V-01: STATUS QUO Isolation (V-04 R1 Base + STATUS QUO, No Phases)

**Axis:** Inertia framing -- V-04 R1 per-ticket card structure with a STATUS QUO section
inserted before ticket generation. No phase windows.
**Hypothesis:** STATUS QUO alone (without phase overhead) produces the C-07/C-08 improvement
V-05 R1 demonstrated. V-04 R1 scored 97 on C-07/C-08 without STATUS QUO; V-05 R1 scored 100
with STATUS QUO + phases. This variation isolates the STATUS QUO contribution from the phase
contribution. C-11 is addressed by requiring PM volume rationale and ticket body to explicitly
reference STATUS QUO -- a floating preamble is structurally excluded by the per-card citation
requirement. C-12 is lightly addressed via "Not closing this means:" with a specificity hint;
not the full three-part structure tested in V-03.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. The STATUS QUO section must be completed before any
ticket card is generated. Each ticket is a structured card with role-labeled sections.
All section headers and card fields are required. Do not reorder or remove any section.
Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration};
severity in {P0, P1, P2, P3}; volume in {high, medium, low}.
Stock roles for persona field: Support, SRE, PM, UX, C-01 through C-12.

---

## SETUP
Topic: [Feature or product being analyzed.]
Signal: [Artifact being used as input.]
Prediction window: 90 days post-launch.

## STATUS QUO: CURRENT SUPPORT LANDSCAPE
[Complete this section before generating any ticket cards. Grounds volume ratings and body
authenticity in every card below. If the status quo varies significantly by persona type,
note the dominant pattern and flag the exception.]

Current workaround: [What users do today when they hit a problem with this feature or something
similar. One sentence per distinct workaround behavior.]
Support channel today: [Where users go first -- Slack, docs, GitHub Issues, Stack Overflow,
internal wiki, or no channel. Be specific.]
Workaround friction: [high | medium | low]
Doc gap today: [What documentation, guide, or example users currently cannot find. One sentence.
State "unknown" if genuinely unclear.]
Volume anchor: [One sentence connecting STATUS QUO friction to expected first-30-day volume.
Example: "High workaround friction + no existing doc = high volume for how-to and config tickets
in the first 30 days, decreasing to medium as workarounds are documented."]

---

## TICKET CARDS
[Predict at least 5 tickets covering the full 90-day window. Cover at least 3 distinct category
values across all cards. Each card has three role-labeled sections: Support triage, PM rating,
and ticket body. All three sections are required in every card.
The PM volume rationale must reference the STATUS QUO friction level above. The ticket body must
reference what the persona tried based on the STATUS QUO scenario -- do not write a body that
ignores the current-state context.]

### Ticket T-01

**Support: Triage**
Title: [One sentence. Specific enough to route to the right team.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role: Support, SRE, PM, UX, or C-01 through C-12]

**PM: Rating**
Volume: [high | medium | low]
Volume rationale: [One sentence: reference the STATUS QUO friction level and workaround behavior.
How large is the affected population? How frequently does this arise given that current-state friction?]
Severity: [P0 | P1 | P2 | P3]
Severity rationale: [One sentence: is the feature broken or inaccessible (P0/P1), or is a
workaround available and the impact is lower (P2/P3)?]

**Ticket Body**
[Write in first person, in the persona's voice from the Support triage section above.
Reference what the persona tried based on the STATUS QUO scenario -- what workaround they
attempted, what channel they checked, what failed. Use vocabulary, concerns, and framing
specific to this persona's role. SRE: operational/infra language. PM: roadmap/metrics/impact
framing. C-XX: domain and business pain. Minimum 3 sentences. Do not write a generic body
that fits any persona equally well and ignores the STATUS QUO context.]
> [Body text here.]

---

### Ticket T-02

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low]
Volume rationale: [One sentence. Reference STATUS QUO friction if this ticket shares the same
root cause. Explain shift from T-01 volume if different.]
Severity: [P0 | P1 | P2 | P3]
Severity rationale: [One sentence.]

**Ticket Body**
> [First-person body in persona's voice. Reference STATUS QUO scenario context where applicable.
> Role-specific language required.]

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

[Add T-06, T-07, ... for additional tickets. Same three-section structure required in every card.
STATUS QUO reference in PM volume rationale required for any ticket driven by the same root cause.]

## COVERAGE CHECKS

Category coverage: [List distinct category values from all cards. Must be >= 3. If fewer, add cards.]
Volume coverage: [List distinct volume values from all cards.]
Absent volume level (if any): [Which level is absent -- one sentence reason. If all cards share
one volume value, revise at least two cards before proceeding.]
STATUS QUO traceability check: [Name at least two ticket IDs whose PM volume rationale or body
explicitly references the STATUS QUO scenario. Example: "T-01 body references the GitHub Issues
workaround described in STATUS QUO; T-02 volume rationale cites high workaround friction." If
fewer than two tickets reference STATUS QUO, revise before proceeding.]

## GAP ANALYSIS

### Doc Gaps
[Reference the STATUS QUO doc gap identified above. Tie each gap to specific ticket IDs.]
- [Gap 1: what is missing and which ticket(s) it prevents.]
[Add rows as needed.]

### Design Gaps
[At least one specific design gap. Name the missing UX affordance, error state, or behavioral
contract. Reference ticket ID(s) it drives.]
- [Gap 1: what is missing and which ticket(s) it drives.]
[Add rows as needed.]

### Operational Gaps
[At least one specific operational gap. Name the missing runbook, alert, dashboard, or deployment
check. Reference ticket ID(s) it drives.]
- [Gap 1: what is missing and which ticket(s) it drives.]
[Add rows as needed.]

### Priority Close Order
[Rank all gaps by severity and volume of tickets prevented. Tie each ranked gap to ticket IDs
with severity and volume from PM rating fields. Show reasoning.]
1. [Highest-priority gap] -- prevents: [ticket IDs with severity and volume.]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Identify at least one systemic pattern across multiple ticket cards. Name it and cite specific
ticket IDs. Trace the root cause to the STATUS QUO scenario described above.]
Pattern: [Name] -- tickets: [IDs] -- root cause: [One sentence tracing to the STATUS QUO
workaround, channel gap, or doc gap identified above.]
Not closing this means: [What the support queue looks like if this pattern is still unaddressed
at day 90. Name the specific user segment that remains stuck and the specific scenario they face.
Do not write a generic statement -- name the segment, the scenario, and the cost.]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count, status_quo_friction.
```

---

## V-02: C-11 Traceability Enforcement (Explicit Connection Field Per Card)

**Axis:** C-11 traceability enforcement -- V-05 R1 base structure (STATUS QUO + phases +
role-labeled cards) with a named "STATUS QUO connection:" field added to every ticket card,
placed between PM: Rating and Ticket Body.
**Hypothesis:** V-05 R1 may partially pass C-11 because STATUS QUO is present and PM/body
instructions reference it. But the C-11 pass condition requires at least two tickets to be
explicitly traceable to the STATUS QUO scenario -- a floating preamble that never appears in
ticket content does not pass. Making STATUS QUO connection a named required field in every card
eliminates the discretionary gap: the model must name the specific STATUS QUO element (workaround,
channel, doc gap, or friction level) each ticket traces to. C-12 retains V-05 R1's "Not closing
this means:" mechanism unchanged -- this variation isolates C-11 enforcement.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. STATUS QUO section runs first. The 90-day window is
divided into three phases. Each ticket is a structured card with role-labeled sections including
a mandatory STATUS QUO connection field. All section headers and card fields are required.
Do not reorder or remove any section.
Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration};
severity in {P0, P1, P2, P3}; volume in {high, medium, low}.
Stock roles for persona field: Support, SRE, PM, UX, C-01 through C-12.

---

## SETUP
Topic: [Feature or product being analyzed.]
Signal: [Artifact being used as input.]

## STATUS QUO: CURRENT SUPPORT LANDSCAPE
[Complete before generating any tickets. Grounds volume ratings and body authenticity below.]

Current workaround: [What users do today when they hit this problem. One sentence per distinct
workaround behavior.]
Support channel today: [Where users go first. Be specific.]
Workaround friction: [high | medium | low]
Doc gap today: [What documentation users currently cannot find. One sentence. "unknown" if unclear.]
Volume anchor: [One sentence connecting STATUS QUO friction to Phase 1 volume predictions.]

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

**STATUS QUO connection:** [Name the specific STATUS QUO element this ticket traces to. Choose one
of: the current workaround, the support channel gap, the workaround friction level, or the missing
doc. Be specific -- do not write "the STATUS QUO." Example: "Users currently file a GitHub Issue
with no template; this ticket replaces that unstructured path." Do not leave blank or write "N/A".]

**Ticket Body**
> [First-person body in persona's voice. Reference what they tried based on the STATUS QUO
> connection field above -- what workaround they attempted, what channel they checked, what failed.
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

**STATUS QUO connection:** [Name the specific STATUS QUO element this ticket traces to. If
different from T-01, name the different element. If same root cause, note that explicitly.]

**Ticket Body**
> [First-person body in persona's voice. Reference STATUS QUO connection in body framing.
> Role-specific language required.]

---

[Add T-03 and beyond for Phase 1 if needed. Same card structure. STATUS QUO connection required.]

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

**STATUS QUO connection:** [Name the STATUS QUO element this Phase 2 ticket traces to. If this
ticket does not trace to a STATUS QUO element (it emerges from Phase 2 edge-case behavior), write:
"Emerges from Phase 2 behavior, not STATUS QUO baseline -- [one sentence: what drives it instead]."]

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

**STATUS QUO connection:** [STATUS QUO element or Phase 2 emergence note.]

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

**STATUS QUO connection:** [STATUS QUO element or Phase 3 emergence note. Phase 3 tickets often
reflect gaps not visible in STATUS QUO -- state explicitly if that is the case.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add more Phase 3 tickets as needed.]

## COVERAGE CHECKS

Category coverage: [List distinct category values across all phases. Must be >= 3. If fewer, add tickets.]
Volume coverage: Phase 1 = [value] | Phase 2 = [value] | Phase 3 = [value]
Distinct volume levels: [Count. Must be >= 2. If all phases share one level, explain why.]
Phase distribution: Phase 1: [N] | Phase 2: [N] | Phase 3: [N] | Total: [N]
STATUS QUO traceability check: [List the ticket IDs whose STATUS QUO connection field names a
specific STATUS QUO element (not an emergence note). Must be at least 2. If fewer than 2, revise
before proceeding. Example: "T-01 -- traces to GitHub Issues channel gap; T-02 -- traces to
missing setup doc."]

## GAP ANALYSIS

### Doc Gaps
[Reference STATUS QUO doc gap. Tie each gap to ticket IDs and phase.]
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
[Rank by severity and volume of tickets prevented. Tie each ranked gap to STATUS QUO root cause
where applicable.]
1. [Highest-priority gap] -- prevents: [ticket IDs, phase, severity, volume.] -- STATUS QUO root: [one sentence.]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Identify at least one systemic pattern spanning two or more phases, traceable to STATUS QUO.
Name the pattern. Cite ticket IDs with phase labels. Connect to the STATUS QUO root cause.]
Pattern: [Name] -- tickets: [T-01 (P1), T-03 (P2), ...] -- root cause: [One sentence tracing to
the STATUS QUO workaround, channel gap, or doc gap identified above.]
Not closing this means: [What the support queue looks like at day 90 if this pattern is unaddressed.
Reference STATUS QUO behavior and name the specific user segment that remains stuck.]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, status_quo_friction,
             status_quo_traced_ticket_count.
```

---

## V-03: C-12 Consequence Specificity Enforcement (Three-Part Consequence Structure)

**Axis:** Consequence framing specificity -- V-05 R1 base structure (STATUS QUO + phases +
role-labeled cards) with the "Not closing this means:" line replaced by a mandatory three-part
consequence structure in the CROSS-TICKET PATTERN section.
**Hypothesis:** V-05 R1's single "Not closing this means:" line produces a consequence statement
but the C-12 pass condition requires the consequence to be specific to the named pattern --
generic "this will cause user confusion" fails. A three-part structure (affected segment + day-90
scenario + adoption cost) forces C-12 specificity by making generic statements structurally
impossible: each part addresses a different dimension that requires naming the pattern's specific
users, scenario, and cost. C-11 retains V-05 R1's STATUS QUO mechanisms unchanged -- this
variation isolates C-12 enforcement.

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

Current workaround: [What users do today when they hit this problem. One sentence per distinct
workaround behavior.]
Support channel today: [Where users go first. Be specific.]
Workaround friction: [high | medium | low]
Doc gap today: [What documentation users currently cannot find. One sentence. "unknown" if unclear.]
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

[Add T-03 and beyond for Phase 1 if needed.]

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
[Identify at least one systemic pattern spanning two or more phases, traceable to STATUS QUO.
Name the pattern. Cite ticket IDs with phase labels. Connect to the STATUS QUO root cause.

After identifying the pattern, fill in the three-part consequence structure below.
Every part is required. Do not collapse into a single sentence.
Do not write "this will cause user confusion" or any generic impact statement.
Each part must name something specific to this pattern -- not a statement that would fit
any other pattern equally well.]

Pattern: [Name] -- tickets: [T-01 (P1), T-03 (P2), ...] -- root cause: [One sentence tracing to
the STATUS QUO workaround, channel gap, or doc gap identified above.]

Consequence:
- Affected segment: [Who specifically is still stuck at day 90? Name the role or user cohort from
  the ticket cards above -- not generic "users." Example: "SRE teams who completed Phase 1 setup
  but have not yet migrated legacy config files."]
- Day-90 scenario: [What does the support queue look like if this pattern is unaddressed at day 90?
  One specific scenario tied to this named pattern, not a general trend. Example: "T-03 and T-04
  continue arriving at medium volume because the config migration guide still does not exist, and
  SRE teams are still using the Phase 1 Slack-ask workaround as their primary migration path."]
- Adoption cost: [What does this pattern cost in adoption friction, SLA, or user retention? One
  sentence specific to this pattern. Not "this will cause user confusion." Example: "Each affected
  SRE team spends 4-6 hours on a workaround that a 2-page config migration guide would eliminate,
  blocking Phase 2 adoption for their downstream service consumers."]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, status_quo_friction.
```

---

## V-04: V-02 R1 Recovery (Role Sequence + STATUS QUO + Cross-Ticket + Three-Part Consequence)

**Axis:** Role sequence (V-02 R1 base: Support -> PM -> SRE -> bodies) with three structural
additions: (1) lightweight STATUS QUO section before the Support pass, (2) CROSS-TICKET PATTERN
section at the end (the V-02 R1 structural miss), (3) three-part consequence structure for C-12.
**Hypothesis:** V-02 R1 scored 87/100 entirely due to one structural miss (C-09 -- no CROSS-TICKET
PATTERN section; 0/5). Its role-sequence architecture produced the strongest C-06 result in R1
(SRE escalation pass structurally confirms P0/P1) and strong C-07 (PM rationale column forces
volume differentiation). Adding CROSS-TICKET PATTERN + three-part consequence + lightweight
STATUS QUO to V-02 R1 produces a variation with independent strengths not present in V-04/V-05 R1:
role-sequence severity confirmation (SRE pass), plus C-11 and C-12 structural coverage. This is
the lightest-overhead path to 100+ -- no phase windows, shorter template than V-05.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. A STATUS QUO section runs before ticket generation.
Three role passes run in sequence: Support generates the ticket list, PM adds volume and severity
ratings, SRE validates operational severity. Ticket bodies are written after all ratings are locked.
All section headers are fixed. Do not reorder, rename, or remove any section header.
Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration};
severity in {P0, P1, P2, P3}; volume in {high, medium, low}.
Stock roles for persona field: Support, SRE, PM, UX, C-01 through C-12.

---

## SETUP
Topic: [Feature or product being analyzed.]
Signal: [Artifact being used as input.]
Prediction window: 90 days post-launch.

## STATUS QUO: CURRENT SUPPORT LANDSCAPE
[Complete before generating any tickets. Used by PM volume rationale pass and body-writing pass.]

Current workaround: [What users do today. One sentence per distinct behavior.]
Support channel today: [Where users go first. Be specific.]
Workaround friction: [high | medium | low]
Doc gap today: [What documentation is missing. One sentence. "unknown" if unclear.]

---

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
Volume rationale required -- cite the STATUS QUO friction level and affected user population size.
Severity rationale required -- P0/P1 means feature is broken or inaccessible; P2/P3 means
workaround available or impact is cosmetic. Do not assign all tickets the same volume level.]

| ID   | Volume            | Volume Rationale                                                   | Severity | Severity Rationale                           |
|------|-------------------|--------------------------------------------------------------------|----------|----------------------------------------------|
| T-01 | [high|medium|low] | [STATUS QUO friction level + who hits this and how often?]         | [P0-P3]  | [Broken/inaccessible or workaround exists?]  |
| T-02 | [high|medium|low] | [Rationale; reference STATUS QUO if same root cause]               | [P0-P3]  | [Rationale]                                  |
| T-03 | [high|medium|low] | [Rationale]                                                        | [P0-P3]  | [Rationale]                                  |
| T-04 | [high|medium|low] | [Rationale]                                                        | [P0-P3]  | [Rationale]                                  |
| T-05 | [high|medium|low] | [Rationale]                                                        | [P0-P3]  | [Rationale]                                  |
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
Reference what the persona tried based on the STATUS QUO scenario -- what workaround they
attempted or what channel they checked before filing. Do not write generic bodies.]

### T-01: [Title]
Persona: [From Support list]
> [First-person body in persona's voice. Minimum 3 sentences. Role-specific language required.
> Reference STATUS QUO context: what workaround or channel they tried and why it was insufficient.]

### T-02: [Title]
Persona: [From Support list]
> [First-person body in persona's voice. Role-specific language required. STATUS QUO reference
> where applicable.]

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
[Reference the STATUS QUO doc gap identified above.]
- [Gap 1: specific missing doc or guide, and which ticket(s) it would prevent.]
[Add as needed.]

### Design Gaps
- [Gap 1: specific missing UX affordance, error state, or behavioral contract, and which ticket(s) it drives.]
[Add as needed.]

### Operational Gaps
[The SRE pre-launch needs statement above should inform at least one gap here.]
- [Gap 1: specific missing runbook, alert, or deployment check, and which ticket(s) it drives.]
[Add as needed.]

### Priority Close Order
1. [Highest-priority gap] -- prevents: [ticket IDs, with severity and volume from PM ratings.]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Identify at least one systemic pattern across multiple tickets. Name it and cite ticket IDs.
Trace the root cause to the STATUS QUO scenario where possible.

After identifying the pattern, fill in the three-part consequence structure below.
Every part is required. Do not write generic impact statements -- name the specific segment,
scenario, and cost tied to this pattern.]

Pattern: [Name] -- tickets: [IDs] -- root cause: [One sentence. Trace to STATUS QUO if applicable.]

Consequence:
- Affected segment: [Who specifically is still stuck at day 90? Name the role or user cohort from
  the ticket list -- not generic "users."]
- Day-90 scenario: [What does the support queue look like if this pattern is unaddressed? One
  specific scenario tied to this named pattern. Not a general trend.]
- Adoption cost: [What does this pattern cost in adoption friction, SLA, or user retention? One
  sentence specific to the named pattern. Not "this will cause user confusion."]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count.
```

---

## V-05: Full Synthesis R2 (V-05 R1 + C-11 Named Connection Field + C-12 Three-Part Consequence + Traceability Coverage Check)

**Axes:** Full synthesis -- V-05 R1 base (STATUS QUO + phases + role-labeled cards) upgraded with:
(1) named "STATUS QUO connection:" field in every ticket card (V-02 R2 C-11 mechanism),
(2) three-part consequence structure in the CROSS-TICKET PATTERN section (V-03 R2 C-12 mechanism),
(3) STATUS QUO traceability coverage check that verifies >= 2 traces before output is complete.
**Hypothesis:** V-05 R1 scored 100/100 on the v1 rubric. On the v2 rubric (110-pt ceiling), the
two new aspirational criteria require structural enforcement that V-05 R1 did not provide. C-11
requires at least two tickets explicitly traceable to STATUS QUO content -- V-05 R1 left this
to model discretion via instructions. C-12 requires a specific consequence tied to the named
pattern -- V-05 R1's single line creates room for generic statements. This variation adds
structural enforcement for both: a named connection field eliminates the C-11 floating-preamble
failure mode; the three-part consequence structure eliminates the C-12 generic-statement failure
mode; and a post-generation coverage check verifies C-11 traceability before the output is
finalized. Combined, this variation should produce 110/110 structural ceiling.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. STATUS QUO section runs first. The 90-day window is
divided into three phases. Each ticket is a structured card with role-labeled sections including
a mandatory STATUS QUO connection field. All section headers and card fields are required.
Do not reorder or remove any section.
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

Current workaround: [What users do today when they hit this problem. One sentence per distinct
workaround behavior.]
Support channel today: [Where users go first. Be specific.]
Workaround friction: [high | medium | low]
Doc gap today: [What documentation users currently cannot find. One sentence. "unknown" if unclear.]
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

**STATUS QUO connection:** [Name the specific STATUS QUO element this ticket traces to: the current
workaround, the support channel gap, the workaround friction level, or the missing doc. Be specific --
name the element, not just "the STATUS QUO." Example: "Traces to the GitHub Issues channel gap --
users currently file unstructured reports with no routing; this ticket replaces that path."
Do not leave blank or write "N/A".]

**Ticket Body**
> [First-person body in persona's voice. Reference what the persona tried based on the STATUS QUO
> connection above -- what workaround they attempted, what channel they checked, what failed.
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

**STATUS QUO connection:** [Name the specific STATUS QUO element this ticket traces to. If
different root cause from T-01, name the different element. If same, note that explicitly.]

**Ticket Body**
> [First-person body in persona's voice. Reference STATUS QUO connection in body framing.
> Role-specific language required.]

---

[Add T-03 and beyond for Phase 1 if needed. Same card structure. STATUS QUO connection required in every card.]

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

**STATUS QUO connection:** [Name the STATUS QUO element this Phase 2 ticket traces to. If this
ticket does not trace to a STATUS QUO element, write: "Emerges from Phase 2 behavior, not STATUS
QUO baseline -- [one sentence: what drives it instead]."]

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

**STATUS QUO connection:** [STATUS QUO element or Phase 2 emergence note.]

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

**STATUS QUO connection:** [STATUS QUO element or Phase 3 emergence note. Phase 3 tickets often
reflect gaps not visible in STATUS QUO -- state explicitly if that is the case.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add more Phase 3 tickets as needed.]

## COVERAGE CHECKS

Category coverage: [List distinct category values across all phases. Must be >= 3. If fewer, add tickets.]
Volume coverage: Phase 1 = [value] | Phase 2 = [value] | Phase 3 = [value]
Distinct volume levels: [Count. Must be >= 2. If all phases share one level, explain why.]
Phase distribution: Phase 1: [N] | Phase 2: [N] | Phase 3: [N] | Total: [N]
STATUS QUO traceability check: [List the ticket IDs whose STATUS QUO connection field names a
specific STATUS QUO element (not an emergence note). Must be at least 2. If fewer than 2, revise
those cards before proceeding. Example: "T-01 -- traces to GitHub Issues channel gap; T-02 --
traces to missing setup doc. Count: 2. Passes."]

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
[Identify at least one systemic pattern spanning two or more phases, traceable to STATUS QUO.
Name the pattern. Cite ticket IDs with phase labels. Connect to the STATUS QUO root cause.

After identifying the pattern, fill in the three-part consequence structure below.
Every part is required. Do not collapse into a single line.
Do not write "this will cause user confusion" or any generic impact statement.
Each part must name something specific to this named pattern -- a statement that would fit
any other pattern equally well does not pass.]

Pattern: [Name] -- tickets: [T-01 (P1), T-03 (P2), ...] -- root cause: [One sentence tracing to
the STATUS QUO workaround, channel gap, or doc gap identified above.]

Consequence:
- Affected segment: [Who specifically is still stuck at day 90? Name the role or user cohort from
  the ticket cards above -- not generic "users." Example: "Developers who completed Phase 1 setup
  but have not yet configured multi-tenant routing."]
- Day-90 scenario: [What does the support queue look like if this pattern is unaddressed? One
  specific scenario tied to this named pattern. Example: "T-03 and T-04 continue arriving at medium
  volume because the routing configuration doc still does not exist; developers are still using the
  Phase 1 Slack-ask workaround as their primary path."]
- Adoption cost: [What does this pattern cost in adoption friction, SLA, or user retention? One
  sentence specific to this pattern. Example: "Each affected team spends 2-3 hours on a workaround
  that a single configuration reference page would eliminate, blocking Phase 2 adoption for their
  downstream service consumers."]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, status_quo_friction,
             status_quo_traced_ticket_count.
```

---

## Round 2 Design Notes

### Axis selection rationale

Three of the five variations are single-mechanism additions to high-scoring R1 bases:
V-01 adds STATUS QUO to V-04 R1 without phases (isolates STATUS QUO as a load-bearing mechanism),
V-02 adds a named connection field to V-05 R1 (isolates C-11 enforcement), V-03 adds a three-part
consequence structure to V-05 R1 (isolates C-12 enforcement). V-04 repairs V-02 R1's structural
miss with three targeted additions (STATUS QUO + CROSS-TICKET PATTERN + three-part consequence).
V-05 combines all winning mechanisms.

Phrasing register and general output format were not chosen as variation axes in Round 2 because
the new rubric criteria (C-11, C-12) are insensitive to register and format -- they test specific
structural properties of the STATUS QUO connection and the consequence statement. Productive Round
2 variations are those that test whether the new criteria can be passed structurally or whether
they rely on model discretion.

### C-11 structural comparison

| V    | C-11 mechanism                                                   | Failure path                                         |
|------|------------------------------------------------------------------|------------------------------------------------------|
| V-01 | STATUS QUO + PM rationale instruction + body instruction (citation required by text) | Instruction-only; model may satisfy PM field without body trace |
| V-02 | Named "STATUS QUO connection:" field per card (required, no blank) | Structural; floating preamble excluded by named field |
| V-03 | STATUS QUO + instruction-only (V-05 R1 base, unchanged)          | Same as V-05 R1; not the isolated C-11 test          |
| V-04 | Lightweight STATUS QUO + body instruction references it          | Lighter enforcement than V-02; PM rationale may suffice alone |
| V-05 | Named connection field + traceability coverage check verifies >= 2 traces | Strongest; two independent enforcement layers |

### C-12 structural comparison

| V    | C-12 mechanism                                                   | Failure path                                         |
|------|------------------------------------------------------------------|------------------------------------------------------|
| V-01 | "Not closing this means:" with specificity hint (one sentence)   | Hint does not structurally prevent generic statement |
| V-02 | "Not closing this means:" (V-05 R1 base, unchanged)              | Same as V-05 R1; not the isolated C-12 test          |
| V-03 | Three-part structure: affected segment + day-90 scenario + adoption cost | Generic statements cannot satisfy three named parts |
| V-04 | Three-part structure (same as V-03)                              | Same mechanism; tests whether role-sequence base helps |
| V-05 | Three-part structure + explicit fail condition ("not generic") stated | Strongest; fail condition named; three parts required |

### Cross-variation experiment matrix

| Experiment | V-A | V-B (baseline) | What changes | What we learn |
|------------|-----|----------------|--------------|---------------|
| STATUS QUO load-bearing for C-07/C-08? | V-01 | V-04 R1 | V-01 adds STATUS QUO; V-04 R1 has no STATUS QUO | If V-01 outscores V-04 R1 on C-07/C-08, STATUS QUO is load-bearing |
| C-11: named field vs. instruction-only? | V-02 | V-01 | V-02 has named connection field; V-01 has instruction-only | If V-02 outscores V-01 on C-11, named field is the necessary mechanism |
| C-12: three-part vs. single line? | V-03 | V-05 R1 | V-03 has three-part consequence; V-05 R1 has one line | If V-03 outscores V-05 R1 on C-12, three-part structure is necessary |
| Role-sequence recovery: can V-04 reach 100+? | V-04 | V-02 R1 | V-04 adds STATUS QUO + cross-ticket + consequence | Measures the recovery lift from three targeted additions |

### V-golden candidate

**V-05** is the direct 110/110 ceiling candidate:
- STATUS QUO volume anchor + phase gradient + per-card rationale = three-layer C-07 pressure
- Named STATUS QUO connection field per card = C-11 structural enforcement
- Traceability coverage check verifies >= 2 explicit traces before completion
- Three-part consequence structure = C-12 structural enforcement
- Explicit fail condition for generic consequence statements
- Phase-labeled ticket IDs in both cards and pattern section = C-09 structural citation format
- Priority close order tied to ticket data by ID, phase, severity, and volume = C-10 pass

**V-03** is the most targeted C-12 test: if the three-part consequence structure alone passes
C-12 in V-05 R1 base, V-05 R2's full synthesis is confirmed as the ceiling variation without
any ambiguity about which mechanism is load-bearing for C-12.

**V-02** is the most targeted C-11 test: if the named connection field alone passes C-11 in
V-05 R1 base, the traceability coverage check in V-05 R2 is confirmatory rather than necessary.
