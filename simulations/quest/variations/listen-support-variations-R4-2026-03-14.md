Written to `simulations/quest/variations/listen-support-variations-R4-2026-03-14.md`.

---

## Round 4 Variations -- listen-support

| V | Axis | Hypothesis |
|---|------|------------|
| **V-01** | C-15 gap bridge column | 3-column trace table -- adds "Gap traced to" so every traced ticket names the gap it drives; gaps with no table row become structurally visible as unsupported |
| **V-02** | C-16 per-field prohibited sentinels | Named "Prohibited:" example immediately below each flat consequence field -- locally checkable failure without cross-field comparison |
| **V-03** | Role-simulation register | Model is cast as each persona filing the ticket (not as analyst predicting); STATUS QUO connection and body shift to first-person performance mode |
| **V-04** | V-01 + V-02 combined (no register change) | Minimal content-gate upgrade from V-05 R3 baseline |
| **V-05** | Full synthesis R4 | V-05 R3 + gap bridge + sentinels + role-simulation register |

**Escalation context:** V-04 and V-05 R3 both score 130/130 on v4. Round 4 is not chasing the ceiling -- it's probing the next structural level: from **format gates** (table/flat, R3) toward **content gates** (cross-reference column, field-local prohibitions, characterization→performance register). These are the likely C-17/C-18 candidates.

**What each experiment answers:**
- V-01 vs. R3 baseline: Does linking the trace table to the gap analysis prevent gap inflation?
- V-02 vs. R3 baseline: Do per-field sentinels outperform section-level prohibition?
- V-03 vs. R3 baseline: Does role-simulation produce more specific STATUS QUO connections and bodies?
- V-04 vs. R3: Do the two content gates together reveal new output-quality failure modes?
- V-05 vs. V-04: Does the register shift add independent value above the structural gates?
tion-level prohibition instruction alone?
- **V-03 vs. V-05 R3 baseline**: Does role-simulation register improve C-03/C-08 body authenticity without introducing vocabulary or compliance risks?
- **V-04 vs. V-05 R3**: Does the minimal combination (gap bridge + sentinels) reveal new failure modes at 130/130?
- **V-05 vs. V-04**: Does adding role-simulation register on top of the content gates improve ticket body quality further?

---

## V-01: C-15 Gap Bridge Column

**Axis:** C-15 table column extension -- V-05 R3 base with the COMPETING SOLUTION TRACE ENUMERATION table extended to three columns: Ticket ID, Competing-solution element, Gap traced to. The third column forces each traced ticket to name the gap (from the Gap Analysis section) that the STATUS QUO element drives. A gap appearing in the Gap Analysis with no corresponding trace table row has no ticket evidence -- the cross-reference makes this visible.

**Hypothesis:** V-05 R3's trace table (two columns: Ticket ID + element) verifies that STATUS QUO tracing exists and is per-ticket, but it does not verify that the gap analysis is grounded in ticket evidence. A gap section can list plausible gaps that no ticket actually predicts -- gap inflation. A third "Gap traced to" column makes the gap analysis auditable from the table: count distinct gap values in column 3, compare to Gap Analysis items. Gaps in the Gap Analysis but absent from column 3 are either evidence-free or the trace table is incomplete. This structural cross-reference should tighten C-10 (prioritized gap closing) and expose gap inflation that the current table cannot catch.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. COMPETING SOLUTION section runs first -- this describes
the active alternative that users return to if the feature disappoints. The 90-day window is
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

## COMPETING SOLUTION: WHAT USERS DO INSTEAD
[Complete before generating any tickets. Describes what users actively do when this feature
is not available or disappoints. This is not a neutral baseline -- it is the named competing
solution that drives volume calibration and consequence framing throughout the template.
If the competing solution varies by persona, note the dominant pattern and flag exceptions.]

Current solution: [What users do today to solve the problem this feature addresses. One sentence
per distinct alternative. Name the tool, command, or process -- not generically "the old way."]
Where it lives: [The specific tool, channel, doc, or command users execute the current solution
through. Be specific: "pgAdmin direct SQL" not "the database."]
Switching friction: [high | medium | low -- how hard is it to switch from the current solution
to this feature? This anchors Phase 1 volume calibration: high friction means committed users
push through and file tickets; low friction means marginal users revert silently.]
Current solution gap: [What the current solution cannot do that this feature enables. One sentence.
This is the feature's only competitive advantage over the status quo.]
Defection anchor: [One sentence naming the persona most likely to revert and the specific
threshold at which they abandon the feature. Example: "C-04 data engineers will revert to
direct SQL if this feature's setup exceeds 30 min -- they know the competing solution and their
switching cost is near zero."]
Volume anchor: [One sentence connecting switching friction and defection anchor to Phase 1
volume prediction. Example: "High switching friction + strong defection risk for C-04 = high
Phase 1 how-to and config ticket volume; if tickets are unanswered, C-04 defection reduces
Phase 2 volume as a lagging indicator, not an improvement signal."]

## PHASE 1: LAUNCH WEEK (Days 1-14)

[First adopters are testing the feature against the competing solution. Volume reflects commitment:
high-volume tickets come from users who are still trying; low-volume tickets in an area with a
strong competing solution may mean silent defection is already occurring. Generate at least 2
tickets. For each, assess: is this a committed-user ticket or a defection-signal ticket?]

### T-01 (Phase 1)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence: how many users will file this vs. revert to
the competing solution? Reference switching friction and defection anchor. Example: "High --
C-04 will file this before switching back to SQL; the automated scheduling advantage keeps them
trying despite the setup friction."]
Severity: [P0 | P1 | P2 | P3] -- [One sentence: broken/inaccessible (P0/P1) or workaround
available (P2/P3)? If the competing solution is the available workaround, state that explicitly.]

**STATUS QUO connection:** [Name the specific competing-solution element this ticket traces to:
the current solution they tried, the switching friction, the current solution gap, or the
defection anchor. Be specific. Example: "Traces to defection anchor -- C-04 tried direct SQL
for 30 min before filing; feature setup friction is at the reversion threshold."
Do not leave blank or write "N/A".]

**Ticket Body**
> [First-person body in persona's voice. Reference what the persona tried in the competing
> solution before filing -- what they did in the old tool, what failed to transfer, why they
> are still trying the new feature. Role-specific vocabulary required. SRE: ops/infra language.
> C-XX: domain and business context. PM: impact/metrics framing. Minimum 3 sentences. Not a
> generic body. A body that ignores the competing solution context does not pass.]

---

### T-02 (Phase 1)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence: reference switching friction and defection risk.
If this ticket has low volume because the competing solution is easy to revert to for this ticket
type, state that explicitly.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale. Note if competing solution is the
available workaround that suppresses severity.]

**STATUS QUO connection:** [Competing-solution element this ticket traces to. Different element
from T-01 if root cause differs; note explicitly if same root.]

**Ticket Body**
> [First-person body in persona's voice. Reference competing-solution context. Role-specific
> language required.]

---

[Add T-03 and beyond for Phase 1 if needed. Same card structure. STATUS QUO connection required in every card.]

## PHASE 2: LEARNING CURVE (Days 15-60)

[Users who passed Phase 1 without reverting are now integrating the feature into workflows.
Competing-solution inertia decreases for committed users. Phase 2 tickets come from users who
have crossed the switching threshold. Volume decreases from Phase 1. Generate at least 2 tickets.]

### T-03 (Phase 2)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence; explain volume shift from Phase 1. If lower,
is it because committed users have cleared the competing-solution threshold?]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Competing-solution element or Phase 2 emergence note. If this Phase
2 ticket has no competing-solution connection (it emerges from post-commitment behavior), write:
"Emerges from Phase 2 committed-user behavior -- [one sentence: what drives it instead]."]

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

**STATUS QUO connection:** [Competing-solution element or Phase 2 emergence note.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add more Phase 2 tickets as needed.]

## PHASE 3: ADVANCED USE (Days 61-90)

[Power users pushing feature limits. Competing solution is largely irrelevant for this cohort.
Volume is lower. Generate at least 1 ticket.]

### T-05 (Phase 3)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence; explain lower volume. Note whether the competing
solution is still a reversion option for this persona or has been permanently replaced.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Competing-solution element or Phase 3 emergence note.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add more Phase 3 tickets as needed.]

## COVERAGE CHECKS

Category coverage: [List distinct category values across all phases. Must be >= 3. If fewer, add tickets.]
Volume coverage: Phase 1 = [value] | Phase 2 = [value] | Phase 3 = [value]
Distinct volume levels: [Count. Must be >= 2. If all phases share one value, explain in terms of
competing-solution switching behavior -- a uniform-volume explanation citing defection dynamics
passes; "all tickets are equally important" does not.]
Phase distribution: Phase 1: [N] | Phase 2: [N] | Phase 3: [N] | Total: [N]

## COMPETING SOLUTION TRACE ENUMERATION
[Complete this table after all ticket cards AND the Gap Analysis section are written. Fill one
row per ticket whose STATUS QUO connection field names a specific competing-solution element
(not an emergence note). Each ticket gets its own row -- do not summarize multiple tickets in
one sentence. Column 3 (Gap traced to) must name the gap from the Gap Analysis section that
this STATUS QUO element drives. A gap that appears in the Gap Analysis but in no row of column 3
has no ticket evidence -- either add a ticket card or remove the gap from the Gap Analysis.
If the table has fewer than 2 rows, revise those ticket cards before proceeding.]

| Ticket ID | Competing-solution element named in connection field | Gap traced to |
|-----------|------------------------------------------------------|---------------|
| [T-XX]    | [The specific competing-solution element, e.g., "C-04 direct SQL reversion threshold (30 min)"] | [Gap name from Gap Analysis, e.g., "Doc gap: no migration runbook"] |
| [T-XX]    | [Specific element -- must name the element from COMPETING SOLUTION, not paraphrase as "status quo"] | [Gap name or "Phase N emergence -- no gap trace"] |
[Add one row per ticket with a specific competing-solution element named. Emergence-note tickets
list their gap trace if one exists, or mark "Phase N emergence -- no gap trace" if none.]

Trace count: [N]. Required: >= 2. Gap coverage check: [List any Gap Analysis gaps not in column 3. If all gaps appear in column 3, write "All gaps evidenced."] Gate: [PASSES | REVISE -- identify which cards or gaps need revision before proceeding.]

## GAP ANALYSIS

### Doc Gaps
[Reference the current solution gap from COMPETING SOLUTION. Doc gaps that go unclosed keep
the competing solution viable for a wider population -- note the reversion path they leave open.]
- [Gap 1: missing doc, which ticket(s) it drives, which phase(s), and which competing-solution
  reversion path it leaves open if unclosed.]
[Add as needed.]

### Design Gaps
- [Gap 1: missing UX affordance or behavioral contract, which ticket(s), which phase. Note if
  the competing solution handles this case better today.]
[Add as needed.]

### Operational Gaps
- [Gap 1: missing operational element, which ticket(s), which phase.]
[Add as needed.]

### Priority Close Order
[Rank by severity, volume, and reversion risk. A gap that leaves the competing solution's primary
advantage intact ranks higher regardless of ticket volume alone.]
1. [Highest-priority gap] -- prevents: [ticket IDs, phase, severity, volume.] -- reversion risk: [one sentence: which persona reverts if this gap stays open?]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Identify at least one systemic pattern spanning two or more phases. Name it, cite ticket IDs
with phase labels, and trace the root cause to the COMPETING SOLUTION section.

Fill in all four consequence fields below. Each field is required and independently checkable.
Do not nest these inside a "Consequence:" parent. Do not collapse into a single sentence or
a bullet list. The consequence of leaving a pattern open in this framing is that the reversion
path stays clear -- name the reversion path explicitly in the consequence fields.
Fail conditions: "this will cause user confusion" (fails all three), "adoption will be impacted"
(fails all three), "users will be frustrated" (fails all three). A statement that could be
copied verbatim to any other pattern does not pass any consequence field.]

Pattern name: [One name for this pattern.]
Pattern tickets: [T-01 (P1), T-03 (P2), ...] with phase labels.
Pattern root cause: [One sentence tracing to the competing-solution element -- switching friction,
defection anchor, or current solution gap -- that this pattern exposes.]

Consequence -- Affected segment: [Who specifically is still at reversion risk at day 90? Name
the exact role or user cohort from the ticket cards and COMPETING SOLUTION defection anchor.
Not generic "users." The named cohort must appear in the ticket IDs above. Example: "C-04 data
engineers who completed Phase 1 setup but have not yet moved their primary scheduling workload
off direct SQL -- estimated 40% of target C-04 installs at this stage."]
Consequence -- Day-90 scenario: [What does the support queue look like and what reversion behavior
is still active at day 90 if this pattern is unaddressed? One specific event tied to this pattern
and these ticket IDs. Reference the competing solution still in use. Example: "T-03 and T-04
continue at medium volume; C-04 teams are running SQL jobs in parallel as a safety net because
the scheduling conflict doc was never shipped -- the competing solution has not been displaced."]
Consequence -- Adoption cost: [What does leaving this pattern open cost the feature's competitive
position? One sentence naming a rate, dependency blocked, or retained competing-solution share.
Specific to this pattern -- not "user confusion." Example: "The direct-SQL workflow retains
C-04's primary scheduling load until the conflict resolution doc ships -- estimated 40% of target
installs are partial, handling only non-critical jobs through the new feature."]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, competing_solution_friction,
             status_quo_traced_ticket_count, gaps_with_ticket_evidence.
```

---

## V-02: C-16 Per-Field Prohibited-Value Sentinels

**Axis:** C-16 consequence field content guard -- V-05 R3 base with a named "Prohibited:" sentinel added immediately below each flat consequence field instruction. Each sentinel names a specific generic value that would fail that field, making the prohibition checkable at the field level without reading across fields or comparing to other patterns.

**Hypothesis:** V-05 R3's flat fields prohibit generic statements at the section level: "A statement that could be copied verbatim to any other pattern does not pass any consequence field." This is a cross-field prohibition -- it requires comparing the output to a hypothetical other pattern, which is not self-verifying at fill time. Per-field sentinels name a concrete generic value adjacent to the field: the model filling "Affected segment: users" would see "Prohibited: 'users' -- fails this field" immediately below its own output. The sentinel is field-local (no comparison required) and the prohibited value is pattern-generic by definition -- a model writing the prohibited value is writing a self-evidently failing response. This should produce more specific content than section-level prohibition alone.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. COMPETING SOLUTION section runs first -- this describes
the active alternative that users return to if the feature disappoints. The 90-day window is
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

## COMPETING SOLUTION: WHAT USERS DO INSTEAD
[Complete before generating any tickets. Describes what users actively do when this feature
is not available or disappoints. This is not a neutral baseline -- it is the named competing
solution that drives volume calibration and consequence framing throughout the template.
If the competing solution varies by persona, note the dominant pattern and flag exceptions.]

Current solution: [What users do today to solve the problem this feature addresses. One sentence
per distinct alternative. Name the tool, command, or process -- not generically "the old way."]
Where it lives: [The specific tool, channel, doc, or command users execute the current solution
through. Be specific: "pgAdmin direct SQL" not "the database."]
Switching friction: [high | medium | low -- how hard is it to switch from the current solution
to this feature? This anchors Phase 1 volume calibration: high friction means committed users
push through and file tickets; low friction means marginal users revert silently.]
Current solution gap: [What the current solution cannot do that this feature enables. One sentence.
This is the feature's only competitive advantage over the status quo.]
Defection anchor: [One sentence naming the persona most likely to revert and the specific
threshold at which they abandon the feature. Example: "C-04 data engineers will revert to
direct SQL if this feature's setup exceeds 30 min -- they know the competing solution and their
switching cost is near zero."]
Volume anchor: [One sentence connecting switching friction and defection anchor to Phase 1
volume prediction. Example: "High switching friction + strong defection risk for C-04 = high
Phase 1 how-to and config ticket volume; if tickets are unanswered, C-04 defection reduces
Phase 2 volume as a lagging indicator, not an improvement signal."]

## PHASE 1: LAUNCH WEEK (Days 1-14)

[First adopters are testing the feature against the competing solution. Volume reflects commitment:
high-volume tickets come from users who are still trying; low-volume tickets in an area with a
strong competing solution may mean silent defection is already occurring. Generate at least 2
tickets. For each, assess: is this a committed-user ticket or a defection-signal ticket?]

### T-01 (Phase 1)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence: how many users will file this vs. revert to
the competing solution? Reference switching friction and defection anchor. Example: "High --
C-04 will file this before switching back to SQL; the automated scheduling advantage keeps them
trying despite the setup friction."]
Severity: [P0 | P1 | P2 | P3] -- [One sentence: broken/inaccessible (P0/P1) or workaround
available (P2/P3)? If the competing solution is the available workaround, state that explicitly.]

**STATUS QUO connection:** [Name the specific competing-solution element this ticket traces to:
the current solution they tried, the switching friction, the current solution gap, or the
defection anchor. Be specific. Example: "Traces to defection anchor -- C-04 tried direct SQL
for 30 min before filing; feature setup friction is at the reversion threshold."
Do not leave blank or write "N/A".]

**Ticket Body**
> [First-person body in persona's voice. Reference what the persona tried in the competing
> solution before filing -- what they did in the old tool, what failed to transfer, why they
> are still trying the new feature. Role-specific vocabulary required. SRE: ops/infra language.
> C-XX: domain and business context. PM: impact/metrics framing. Minimum 3 sentences. Not a
> generic body. A body that ignores the competing solution context does not pass.]

---

### T-02 (Phase 1)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence: reference switching friction and defection risk.
If this ticket has low volume because the competing solution is easy to revert to for this ticket
type, state that explicitly.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale. Note if competing solution is the
available workaround that suppresses severity.]

**STATUS QUO connection:** [Competing-solution element this ticket traces to. Different element
from T-01 if root cause differs; note explicitly if same root.]

**Ticket Body**
> [First-person body in persona's voice. Reference competing-solution context. Role-specific
> language required.]

---

[Add T-03 and beyond for Phase 1 if needed. Same card structure. STATUS QUO connection required in every card.]

## PHASE 2: LEARNING CURVE (Days 15-60)

[Users who passed Phase 1 without reverting are now integrating the feature into workflows.
Competing-solution inertia decreases for committed users. Phase 2 tickets come from users who
have crossed the switching threshold. Volume decreases from Phase 1. Generate at least 2 tickets.]

### T-03 (Phase 2)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence; explain volume shift from Phase 1. If lower,
is it because committed users have cleared the competing-solution threshold?]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Competing-solution element or Phase 2 emergence note. If this Phase
2 ticket has no competing-solution connection, write:
"Emerges from Phase 2 committed-user behavior -- [one sentence: what drives it instead]."]

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

**STATUS QUO connection:** [Competing-solution element or Phase 2 emergence note.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add more Phase 2 tickets as needed.]

## PHASE 3: ADVANCED USE (Days 61-90)

[Power users pushing feature limits. Competing solution is largely irrelevant for this cohort.
Volume is lower. Generate at least 1 ticket.]

### T-05 (Phase 3)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence; explain lower volume. Note whether the competing
solution is still a reversion option for this persona or has been permanently replaced.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Competing-solution element or Phase 3 emergence note.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add more Phase 3 tickets as needed.]

## COVERAGE CHECKS

Category coverage: [List distinct category values across all phases. Must be >= 3. If fewer, add tickets.]
Volume coverage: Phase 1 = [value] | Phase 2 = [value] | Phase 3 = [value]
Distinct volume levels: [Count. Must be >= 2. If all phases share one value, explain in terms of
competing-solution switching behavior -- a uniform-volume explanation citing defection dynamics
passes; "all tickets are equally important" does not.]
Phase distribution: Phase 1: [N] | Phase 2: [N] | Phase 3: [N] | Total: [N]

## COMPETING SOLUTION TRACE ENUMERATION
[Complete this table after all ticket cards are written. Fill one row per ticket whose STATUS
QUO connection field names a specific competing-solution element (not an emergence note). Do not
write a summary statement covering multiple tickets in one sentence -- each ticket gets its own
row. If the table has fewer than 2 rows, revise those ticket cards before proceeding. Each row
must independently satisfy: ticket ID, named competing-solution element, and element type.
A row that reads "general switching friction" without naming the specific element does not count.]

| Ticket ID | Competing-solution element named in connection field | Element type |
|-----------|------------------------------------------------------|--------------|
| [T-XX]    | [The specific competing-solution element, e.g., "C-04 direct SQL reversion threshold (30 min)"] | [current-solution \| switching-friction \| solution-gap \| defection-anchor] |
| [T-XX]    | [Specific element -- must name the element from COMPETING SOLUTION, not paraphrase as "status quo"] | [type] |
[Add one row per ticket with a specific competing-solution element named.]

Trace count: [N]. Required: >= 2. Gate: [PASSES | REVISE -- identify which cards need a specific competing-solution element before proceeding.]

## GAP ANALYSIS

### Doc Gaps
[Reference the current solution gap from COMPETING SOLUTION. Doc gaps that go unclosed keep
the competing solution viable for a wider population -- note the reversion path they leave open.]
- [Gap 1: missing doc, which ticket(s) it drives, which phase(s), and which competing-solution
  reversion path it leaves open if unclosed.]
[Add as needed.]

### Design Gaps
- [Gap 1: missing UX affordance or behavioral contract, which ticket(s), which phase. Note if
  the competing solution handles this case better today.]
[Add as needed.]

### Operational Gaps
- [Gap 1: missing operational element, which ticket(s), which phase.]
[Add as needed.]

### Priority Close Order
[Rank by severity, volume, and reversion risk. A gap that leaves the competing solution's primary
advantage intact ranks higher regardless of ticket volume alone.]
1. [Highest-priority gap] -- prevents: [ticket IDs, phase, severity, volume.] -- reversion risk: [one sentence: which persona reverts if this gap stays open?]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Identify at least one systemic pattern spanning two or more phases. Name it, cite ticket IDs
with phase labels, and trace the root cause to the COMPETING SOLUTION section.

Fill in the four consequence fields below. Each field is required and independently checkable.
Do not nest these inside a "Consequence:" parent. Do not collapse into a single sentence.
Each field carries a "Prohibited:" sentinel below it naming the generic value that fails that
specific field. A value that matches or is equivalent to the Prohibited example fails the field
regardless of other content present in the output.]

Pattern name: [One name for this pattern.]
Pattern tickets: [T-01 (P1), T-03 (P2), ...] with phase labels.
Pattern root cause: [One sentence tracing to the competing-solution element -- switching friction,
defection anchor, or current solution gap -- that this pattern exposes.]

Consequence -- Affected segment: [Who specifically is still at reversion risk at day 90? Name
the exact role or user cohort from the ticket cards and COMPETING SOLUTION defection anchor.
Not generic. The named cohort must appear in the ticket IDs above.]
Prohibited: "users" | "customers" | "affected teams" | any cohort label not drawn from a named
stock role appearing in the ticket cards above. If the value could fit any feature's support
ticket set without modification, it fails this field.

Consequence -- Day-90 scenario: [What does the support queue look like and what reversion behavior
is still active at day 90 if this pattern is unaddressed? One specific event tied to this pattern
and these ticket IDs. Reference the competing solution still in use and name at least two ticket IDs.]
Prohibited: "tickets continue to arrive" without naming a specific competing-solution behavior
still active and without citing the ticket IDs for this pattern. A scenario that does not name
the competing solution still in use at day 90 fails this field.

Consequence -- Adoption cost: [What does leaving this pattern open cost the feature's competitive
position? One sentence naming a rate, dependency blocked, or retained competing-solution share.
Specific to this pattern -- not a general impact statement.]
Prohibited: "this will cause user confusion" | "adoption will be impacted" | "users will be
frustrated" | any statement that does not name the competing solution or provide a specific
rate, duration, or downstream dependency. A consequence that could be copied verbatim to any
other pattern in this output fails this field.

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, competing_solution_friction,
             status_quo_traced_ticket_count.
```

---

## V-03: Phrasing Register -- Role-Simulation (First-Person Filing Mode)

**Axis:** Phrasing register -- V-05 R3 base with ticket-generation instructions shifted from analytical-prediction mode ("Predict what [persona] would file") to role-simulation mode ("You are [persona]. File the ticket you would file after hitting this problem"). The model is cast as each persona for the duration of each card, not as an analyst generating ticket predictions.

**Hypothesis:** All prior variations position the model as an analyst generating ticket predictions about named personas. This mode produces characterization: "C-04 would file a ticket about X, writing in a data engineering voice." Role-simulation positions the model as the persona: "You are C-04. You just hit this problem. File the ticket." The STATUS QUO connection field becomes first-person experience ("I tried the direct SQL approach first -- it took 35 min and failed at step 3"), not third-person description. The ticket body requirement shifts from "role-appropriate vocabulary" to "your actual vocabulary as C-04." This should produce more specific C-08 (persona-authentic bodies) and C-03 (voiced bodies) because the model is not generating a description of what the persona would say -- it is performing the persona. Volume and severity assignments remain analyst-mode (the PM: Rating block does not shift to persona voice) to avoid vocabulary compliance risks.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. COMPETING SOLUTION section runs first and is completed
in analyst mode. The 90-day window is divided into three phases. Each ticket card has two modes:
(1) the PM: Rating block is completed in analyst mode (you are predicting severity and volume);
(2) the Ticket Body and STATUS QUO connection field are completed in persona mode (you ARE the
persona, filing the ticket in your own voice after attempting the competing solution first).
All section headers and card fields are required. Do not reorder or remove any section.
Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration};
severity in {P0, P1, P2, P3}; volume in {high, medium, low}.
Stock roles for persona field: Support, SRE, PM, UX, C-01 through C-12.

---

## SETUP
Topic: [Feature or product being analyzed.]
Signal: [Artifact being used as input.]

## COMPETING SOLUTION: WHAT USERS DO INSTEAD
[Analyst mode. Complete before generating any tickets. Describes what users actively do when this
feature is not available or disappoints. Names the competing solution that drives volume calibration
and consequence framing throughout the template.]

Current solution: [What users do today to solve the problem this feature addresses. One sentence
per distinct alternative. Name the tool, command, or process -- not generically "the old way."]
Where it lives: [The specific tool, channel, doc, or command users execute the current solution
through. Be specific: "pgAdmin direct SQL" not "the database."]
Switching friction: [high | medium | low -- how hard is it to switch from the current solution
to this feature?]
Current solution gap: [What the current solution cannot do that this feature enables. One sentence.]
Defection anchor: [One sentence naming the persona most likely to revert and the specific
threshold at which they abandon the feature.]
Volume anchor: [One sentence connecting switching friction and defection anchor to Phase 1
volume prediction.]

## PHASE 1: LAUNCH WEEK (Days 1-14)

[First adopters are testing the feature against the competing solution. Generate at least 2 tickets.
For each ticket: the PM: Rating block is analyst mode; the STATUS QUO connection and Ticket Body
are persona mode -- you ARE that persona, filing the ticket after attempting the competing solution.]

### T-01 (Phase 1)

**Support: Triage** [Analyst mode]
Title: [One sentence -- what the persona titled their ticket.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role -- who you will become for the STATUS QUO connection and Ticket Body below.]

**PM: Rating** [Analyst mode]
Volume: [high | medium | low] -- [One sentence: how many users will file this vs. revert to
the competing solution? Reference switching friction and defection anchor.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence: broken/inaccessible (P0/P1) or workaround
available (P2/P3)? If the competing solution is the available workaround, state that explicitly.]

**STATUS QUO connection:** [Persona mode -- you ARE the persona named above. Before filing this
ticket, you tried the competing solution first. Name exactly what you tried, how long you spent,
what step failed, and what made you continue trying the new feature instead of reverting.
First-person. Be specific: "I tried [competing solution name] for [X minutes] -- I got as far
as [step], then [what broke]." Do not write "N/A" or a generic reference to the STATUS QUO.]

**Ticket Body** [Persona mode -- you ARE the persona. File the ticket in your own voice.]
> [First person. You are this persona. Write the ticket body as you would write it -- your
> vocabulary, your concerns, your framing. SRE: you are describing infrastructure failure in
> ops terms. C-XX: you are describing the business problem and the workflow you cannot complete.
> PM: you are naming the metric or user impact. Reference what you tried in the competing solution
> (from STATUS QUO connection above) as context for why you are filing now. Minimum 3 sentences.
> Do not write from outside the persona. Do not use "the user" or "they" -- you ARE the user.]

---

### T-02 (Phase 1)

**Support: Triage** [Analyst mode]
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating** [Analyst mode]
Volume: [high | medium | low] -- [One sentence: reference switching friction and defection risk.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale. Note if competing solution is the
available workaround that suppresses severity.]

**STATUS QUO connection:** [Persona mode -- you ARE this persona. What did you try in the
competing solution before filing? First person, specific step, specific element from COMPETING
SOLUTION section. Different competing-solution element from T-01 if root cause differs.]

**Ticket Body** [Persona mode -- you ARE this persona.]
> [First person. Your vocabulary, your role-specific concerns. Reference what you tried in the
> competing solution as context. Role-specific language: your language, not a description of it.]

---

[Add T-03 and beyond for Phase 1 if needed. Same card structure. Each card has analyst-mode
Rating and persona-mode STATUS QUO connection + Ticket Body. The persona changes per card.]

## PHASE 2: LEARNING CURVE (Days 15-60)

[Users who passed Phase 1 without reverting are integrating the feature. Generate at least 2
tickets. Persona mode for STATUS QUO connection and Ticket Body in each card.]

### T-03 (Phase 2)

**Support: Triage** [Analyst mode]
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating** [Analyst mode]
Volume: [high | medium | low] -- [One sentence; explain volume shift from Phase 1.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Persona mode -- you ARE this persona. If this Phase 2 ticket traces
to a competing-solution element, name it in first person: "When I hit this, I checked [competing
solution] first -- [what you found or tried]." If this ticket emerges from post-commitment
behavior with no competing-solution trace, write: "I have already switched -- this is not about
the old tool. [One sentence: what drives this ticket instead]."]

**Ticket Body** [Persona mode -- you ARE this persona.]
> [First person. Role-specific vocabulary. Reference the competing solution context if applicable.]

---

### T-04 (Phase 2)

**Support: Triage** [Analyst mode]
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating** [Analyst mode]
Volume: [high | medium | low] -- [One sentence rationale.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Persona mode -- competing-solution element or post-commitment note.]

**Ticket Body** [Persona mode -- you ARE this persona.]
> [First person. Role-specific vocabulary.]

---

[Add more Phase 2 tickets as needed.]

## PHASE 3: ADVANCED USE (Days 61-90)

[Power users pushing feature limits. Competing solution is largely irrelevant for this cohort.
Generate at least 1 ticket.]

### T-05 (Phase 3)

**Support: Triage** [Analyst mode]
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating** [Analyst mode]
Volume: [high | medium | low] -- [One sentence; explain lower volume.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Persona mode -- competing-solution element or Phase 3 emergence note
in first person.]

**Ticket Body** [Persona mode -- you ARE this persona.]
> [First person. Role-specific vocabulary. Phase 3 bodies reflect advanced expertise -- you are
> not a new user; you have been running the feature for weeks. Your language reflects that.]

---

[Add more Phase 3 tickets as needed.]

## COVERAGE CHECKS
[Return to analyst mode for all checks below.]

Category coverage: [List distinct category values across all phases. Must be >= 3. If fewer, add tickets.]
Volume coverage: Phase 1 = [value] | Phase 2 = [value] | Phase 3 = [value]
Distinct volume levels: [Count. Must be >= 2. If all phases share one value, explain in terms of
competing-solution switching behavior.]
Phase distribution: Phase 1: [N] | Phase 2: [N] | Phase 3: [N] | Total: [N]

## COMPETING SOLUTION TRACE ENUMERATION
[Analyst mode. Complete this table after all ticket cards are written. Fill one row per ticket
whose STATUS QUO connection field names a specific competing-solution element (first-person or
third-person -- the element must be named). Each ticket gets its own row. If the table has fewer
than 2 rows, revise those ticket cards before proceeding.]

| Ticket ID | Competing-solution element named in connection field | Element type |
|-----------|------------------------------------------------------|--------------|
| [T-XX]    | [The specific competing-solution element named in persona-mode STATUS QUO connection] | [current-solution \| switching-friction \| solution-gap \| defection-anchor] |
| [T-XX]    | [Specific element -- name it as stated in the connection field] | [type] |
[Add one row per ticket with a specific competing-solution element named.]

Trace count: [N]. Required: >= 2. Gate: [PASSES | REVISE -- identify which cards need revision before proceeding.]

## GAP ANALYSIS
[Analyst mode.]

### Doc Gaps
[Reference the current solution gap from COMPETING SOLUTION. Note the reversion path each gap
leaves open.]
- [Gap 1: missing doc, which ticket(s) it drives, which phase(s), and which competing-solution
  reversion path it leaves open if unclosed.]
[Add as needed.]

### Design Gaps
- [Gap 1: missing UX affordance or behavioral contract, which ticket(s), which phase. Note if
  the competing solution handles this case better today.]
[Add as needed.]

### Operational Gaps
- [Gap 1: missing operational element, which ticket(s), which phase.]
[Add as needed.]

### Priority Close Order
[Rank by severity, volume, and reversion risk.]
1. [Highest-priority gap] -- prevents: [ticket IDs, phase, severity, volume.] -- reversion risk: [one sentence.]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Analyst mode. Identify at least one systemic pattern spanning two or more phases. Name it,
cite ticket IDs with phase labels, trace the root cause to COMPETING SOLUTION.

Fill in the four consequence fields below. Each field is required and independently checkable.
Do not nest these inside a "Consequence:" parent. Do not collapse into a single sentence.
The reversion path must be named in the consequence fields. A statement that could be copied
verbatim to any other pattern does not pass any consequence field.]

Pattern name: [One name for this pattern.]
Pattern tickets: [T-01 (P1), T-03 (P2), ...] with phase labels.
Pattern root cause: [One sentence tracing to the competing-solution element this pattern exposes.]

Consequence -- Affected segment: [Who specifically is still at reversion risk at day 90? Name
the exact role or cohort from the ticket cards -- not generic "users." Must appear in ticket IDs above.]
Consequence -- Day-90 scenario: [What does the support queue look like and what reversion behavior
is still active at day 90? One specific event tied to this pattern and these ticket IDs. Reference
the competing solution still in use.]
Consequence -- Adoption cost: [What does leaving this pattern open cost the feature's competitive
position? One sentence naming a rate, dependency blocked, or retained competing-solution share.
Specific to this pattern.]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, competing_solution_friction,
             status_quo_traced_ticket_count.
```

---

## V-04: C-15 Gap Bridge + C-16 Per-Field Sentinels (Minimal Combination, V-05 R3 Base)

**Axes:** C-15 table column extension + C-16 per-field prohibited-value sentinels -- V-05 R3 base
with exactly two structural additions: (1) a third "Gap traced to" column in the COMPETING SOLUTION
TRACE ENUMERATION table (from V-01), (2) a "Prohibited:" sentinel line below each flat consequence
field (from V-02). No register change. All other V-05 R3 mechanisms unchanged.

**Hypothesis:** V-05 R3 scores 130/130 on the v4 rubric. V-04 R4 tests whether the two content-gate
additions reveal new structural failure modes beyond what V-05 R3 catches. If V-04 R4 produces
better gap analysis quality (fewer unsupported gaps via gap bridge) and more specific consequence
fields (per-field sentinels prevent known generic values), these improvements represent structural
advances beyond the v4 rubric ceiling -- potential C-17/C-18 candidates.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. COMPETING SOLUTION section runs first -- this describes
the active alternative that users return to if the feature disappoints. The 90-day window is
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

## COMPETING SOLUTION: WHAT USERS DO INSTEAD
[Complete before generating any tickets. Describes what users actively do when this feature
is not available or disappoints. This is not a neutral baseline -- it is the named competing
solution that drives volume calibration and consequence framing throughout the template.
If the competing solution varies by persona, note the dominant pattern and flag exceptions.]

Current solution: [What users do today to solve the problem this feature addresses. One sentence
per distinct alternative. Name the tool, command, or process -- not generically "the old way."]
Where it lives: [The specific tool, channel, doc, or command users execute the current solution
through. Be specific: "pgAdmin direct SQL" not "the database."]
Switching friction: [high | medium | low -- how hard is it to switch from the current solution
to this feature? This anchors Phase 1 volume calibration: high friction means committed users
push through and file tickets; low friction means marginal users revert silently.]
Current solution gap: [What the current solution cannot do that this feature enables. One sentence.
This is the feature's only competitive advantage over the status quo.]
Defection anchor: [One sentence naming the persona most likely to revert and the specific
threshold at which they abandon the feature. Example: "C-04 data engineers will revert to
direct SQL if this feature's setup exceeds 30 min -- they know the competing solution and their
switching cost is near zero."]
Volume anchor: [One sentence connecting switching friction and defection anchor to Phase 1
volume prediction. Example: "High switching friction + strong defection risk for C-04 = high
Phase 1 how-to and config ticket volume; if tickets are unanswered, C-04 defection reduces
Phase 2 volume as a lagging indicator, not an improvement signal."]

## PHASE 1: LAUNCH WEEK (Days 1-14)

[First adopters are testing the feature against the competing solution. Volume reflects commitment:
high-volume tickets come from users who are still trying; low-volume tickets in an area with a
strong competing solution may mean silent defection is already occurring. Generate at least 2
tickets. For each, assess: is this a committed-user ticket or a defection-signal ticket?]

### T-01 (Phase 1)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence: how many users will file this vs. revert to
the competing solution? Reference switching friction and defection anchor. Example: "High --
C-04 will file this before switching back to SQL; the automated scheduling advantage keeps them
trying despite the setup friction."]
Severity: [P0 | P1 | P2 | P3] -- [One sentence: broken/inaccessible (P0/P1) or workaround
available (P2/P3)? If the competing solution is the available workaround, state that explicitly.]

**STATUS QUO connection:** [Name the specific competing-solution element this ticket traces to:
the current solution they tried, the switching friction, the current solution gap, or the
defection anchor. Be specific. Example: "Traces to defection anchor -- C-04 tried direct SQL
for 30 min before filing; feature setup friction is at the reversion threshold."
Do not leave blank or write "N/A".]

**Ticket Body**
> [First-person body in persona's voice. Reference what the persona tried in the competing
> solution before filing -- what they did in the old tool, what failed to transfer, why they
> are still trying the new feature. Role-specific vocabulary required. SRE: ops/infra language.
> C-XX: domain and business context. PM: impact/metrics framing. Minimum 3 sentences. Not a
> generic body. A body that ignores the competing solution context does not pass.]

---

### T-02 (Phase 1)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence: reference switching friction and defection risk.
If this ticket has low volume because the competing solution is easy to revert to for this ticket
type, state that explicitly.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale. Note if competing solution is the
available workaround that suppresses severity.]

**STATUS QUO connection:** [Competing-solution element this ticket traces to. Different element
from T-01 if root cause differs; note explicitly if same root.]

**Ticket Body**
> [First-person body in persona's voice. Reference competing-solution context. Role-specific
> language required.]

---

[Add T-03 and beyond for Phase 1 if needed. Same card structure. STATUS QUO connection required in every card.]

## PHASE 2: LEARNING CURVE (Days 15-60)

[Users who passed Phase 1 without reverting are now integrating the feature into workflows.
Competing-solution inertia decreases for committed users. Phase 2 tickets come from users who
have crossed the switching threshold. Volume decreases from Phase 1. Generate at least 2 tickets.]

### T-03 (Phase 2)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence; explain volume shift from Phase 1. If lower,
is it because committed users have cleared the competing-solution threshold?]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Competing-solution element or Phase 2 emergence note. If this Phase
2 ticket has no competing-solution connection, write:
"Emerges from Phase 2 committed-user behavior -- [one sentence: what drives it instead]."]

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

**STATUS QUO connection:** [Competing-solution element or Phase 2 emergence note.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add more Phase 2 tickets as needed.]

## PHASE 3: ADVANCED USE (Days 61-90)

[Power users pushing feature limits. Competing solution is largely irrelevant for this cohort.
Volume is lower. Generate at least 1 ticket.]

### T-05 (Phase 3)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence; explain lower volume. Note whether the competing
solution is still a reversion option for this persona or has been permanently replaced.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Competing-solution element or Phase 3 emergence note.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add more Phase 3 tickets as needed.]

## COVERAGE CHECKS

Category coverage: [List distinct category values across all phases. Must be >= 3. If fewer, add tickets.]
Volume coverage: Phase 1 = [value] | Phase 2 = [value] | Phase 3 = [value]
Distinct volume levels: [Count. Must be >= 2. If all phases share one value, explain in terms of
competing-solution switching behavior -- a uniform-volume explanation citing defection dynamics
passes; "all tickets are equally important" does not.]
Phase distribution: Phase 1: [N] | Phase 2: [N] | Phase 3: [N] | Total: [N]

## COMPETING SOLUTION TRACE ENUMERATION
[Complete this table after all ticket cards AND the Gap Analysis section are written. Fill one
row per ticket whose STATUS QUO connection field names a specific competing-solution element
(not an emergence note). Each ticket gets its own row -- do not summarize multiple tickets in
one sentence. Column 3 (Gap traced to) must name the gap from the Gap Analysis section that
this STATUS QUO element drives. A gap that appears in the Gap Analysis but in no row of column 3
has no ticket evidence -- either add a ticket card or remove the gap from the Gap Analysis.
A gap bridge row with "Gap traced to: general" does not count; name the specific gap item.
If the table has fewer than 2 rows, revise those ticket cards before proceeding.]

| Ticket ID | Competing-solution element named in connection field | Gap traced to |
|-----------|------------------------------------------------------|---------------|
| [T-XX]    | [The specific competing-solution element, e.g., "C-04 direct SQL reversion threshold (30 min)"] | [Gap name from Gap Analysis section, e.g., "Doc gap: no setup guide for data engineer onboarding"] |
| [T-XX]    | [Specific element -- must name the element from COMPETING SOLUTION] | [Gap name or "Phase N emergence -- no gap trace"] |
[Add one row per ticket with a specific competing-solution element named. Emergence-note tickets
mark their gap trace if one exists, or "Phase N emergence -- no gap trace" if none.]

Trace count: [N]. Required: >= 2.
Gap coverage check: [List any Gap Analysis gaps not in column 3. If all gaps appear in column 3,
write "All gaps evidenced." If any gap has no column-3 row, name it here -- then either add a
ticket card or remove the gap before proceeding.]
Gate: [PASSES | REVISE -- identify which cards or gaps need revision before proceeding.]

## GAP ANALYSIS

### Doc Gaps
[Reference the current solution gap from COMPETING SOLUTION. Doc gaps that go unclosed keep
the competing solution viable for a wider population -- note the reversion path they leave open.]
- [Gap 1: missing doc, which ticket(s) it drives, which phase(s), and which competing-solution
  reversion path it leaves open if unclosed.]
[Add as needed.]

### Design Gaps
- [Gap 1: missing UX affordance or behavioral contract, which ticket(s), which phase. Note if
  the competing solution handles this case better today.]
[Add as needed.]

### Operational Gaps
- [Gap 1: missing operational element, which ticket(s), which phase.]
[Add as needed.]

### Priority Close Order
[Rank by severity, volume, and reversion risk. A gap that leaves the competing solution's primary
advantage intact ranks higher regardless of ticket volume alone.]
1. [Highest-priority gap] -- prevents: [ticket IDs, phase, severity, volume.] -- reversion risk: [one sentence: which persona reverts if this gap stays open?]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Identify at least one systemic pattern spanning two or more phases. Name it, cite ticket IDs
with phase labels, and trace the root cause to the COMPETING SOLUTION section.

Fill in the four consequence fields below. Each field is required and independently checkable.
Do not nest these inside a "Consequence:" parent. Do not collapse into a single sentence.
Each field carries a "Prohibited:" sentinel below it -- a value that matches the prohibited
example fails that field regardless of other content present in the output.]

Pattern name: [One name for this pattern.]
Pattern tickets: [T-01 (P1), T-03 (P2), ...] with phase labels.
Pattern root cause: [One sentence tracing to the competing-solution element -- switching friction,
defection anchor, or current solution gap -- that this pattern exposes.]

Consequence -- Affected segment: [Who specifically is still at reversion risk at day 90? Name
the exact role or user cohort from the ticket cards and COMPETING SOLUTION defection anchor.
Not generic. The named cohort must appear in the ticket IDs above. Example: "C-04 data engineers
who completed Phase 1 setup but have not yet moved their primary scheduling workload off direct
SQL -- estimated 40% of target C-04 installs at this stage."]
Prohibited: "users" | "customers" | "affected teams" | any label not drawn from a named stock
role in the ticket cards above. A cohort not traceable to a specific ticket card fails.

Consequence -- Day-90 scenario: [What does the support queue look like and what reversion behavior
is still active at day 90? One specific event tied to this pattern and these ticket IDs. Reference
the competing solution still in use. Name at least two ticket IDs explicitly.]
Prohibited: "tickets continue to arrive" without naming a specific competing-solution behavior
still active at day 90. A scenario that does not name the competing solution still in use and
does not cite the specific ticket IDs for this pattern fails this field.

Consequence -- Adoption cost: [What does leaving this pattern open cost the feature's competitive
position? One sentence naming a rate, dependency blocked, or retained competing-solution share.
Specific to this pattern.]
Prohibited: "this will cause user confusion" | "adoption will be impacted" | "users will be
frustrated" | any statement that does not name the competing solution or a specific rate,
duration, or blocked dependency. A cost statement that could be pasted verbatim into any other
support ticket analysis fails this field.

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, competing_solution_friction,
             status_quo_traced_ticket_count, gaps_with_ticket_evidence.
```

---

## V-05: Full Synthesis R4

**Axes:** All winning R3 mechanisms + C-15 gap bridge column + C-16 per-field prohibited-value
sentinels + role-simulation register for ticket bodies. V-05 R3 (130/130) upgraded with the three
new mechanisms targeting enhanced gap analysis quality, consequence field specificity, and body
authenticity.

**Hypothesis:** V-05 R3 is the R3 golden at 130/130. The three additions in V-05 R4 do not change
which criteria pass -- all 16 remain structurally satisfied. They target quality above the rubric
ceiling: (1) the gap bridge column makes the gap analysis self-auditing (gap inflation becomes
structurally visible); (2) per-field sentinels make C-16 compliance locally checkable without
cross-field comparison; (3) role-simulation register produces first-person STATUS QUO connection
fields and ticket bodies (performance mode, not characterization mode). If they reveal new failure
modes, they become the basis for C-17/C-18.

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. COMPETING SOLUTION section runs first in analyst mode.
The 90-day window is divided into three phases. Each ticket card has two modes:
(1) PM: Rating block -- analyst mode (predict severity, volume, category);
(2) STATUS QUO connection and Ticket Body -- persona mode (you ARE the persona, filing the ticket
in your own first-person voice after attempting the competing solution first).
All section headers and card fields are required. Do not reorder or remove any section.
Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration};
severity in {P0, P1, P2, P3}; volume in {high, medium, low}.
Stock roles for persona field: Support, SRE, PM, UX, C-01 through C-12.

---

## SETUP
Topic: [Feature or product being analyzed.]
Signal: [Artifact being used as input.]

## COMPETING SOLUTION: WHAT USERS DO INSTEAD
[Analyst mode. Complete before generating any tickets. Names the competing solution that drives
volume calibration, consequence framing, and persona body grounding throughout the template.
If the competing solution varies by persona, note the dominant pattern and flag exceptions.]

Current solution: [What users do today to solve the problem this feature addresses. One sentence
per distinct alternative. Name the tool, command, or process specifically.]
Where it lives: [The specific tool, channel, doc, or command. Be specific: "pgAdmin direct SQL"
not "the database."]
Switching friction: [high | medium | low -- how hard is it to switch? This anchors Phase 1
volume calibration: high friction means committed users push through and file tickets; low
friction means marginal users revert silently.]
Current solution gap: [What the current solution cannot do that this feature enables. One sentence.
This is the feature's only competitive advantage over the status quo.]
Defection anchor: [One sentence naming the persona most likely to revert and the specific
threshold at which they abandon. Example: "C-04 data engineers will revert to direct SQL if
this feature's setup exceeds 30 min -- they know the competing solution and switching cost is
near zero."]
Volume anchor: [One sentence connecting switching friction and defection anchor to Phase 1
volume prediction. Example: "High switching friction + strong defection risk for C-04 = high
Phase 1 how-to and config ticket volume; if tickets are unanswered, C-04 defection reduces
Phase 2 volume as a lagging indicator, not an improvement signal."]

## PHASE 1: LAUNCH WEEK (Days 1-14)

[First adopters testing the feature against the competing solution. Volume reflects commitment:
high-volume tickets come from users who are still trying; low volume with a strong competing
solution means silent defection is occurring. Generate at least 2 tickets. For each: analyst
mode for PM: Rating; persona mode for STATUS QUO connection and Ticket Body.]

### T-01 (Phase 1)

**Support: Triage** [Analyst mode]
Title: [One sentence -- what the persona titled the ticket.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role -- who you will become for the STATUS QUO connection and Ticket Body below.]

**PM: Rating** [Analyst mode]
Volume: [high | medium | low] -- [One sentence: how many users will file this vs. revert to
the competing solution? Reference switching friction and defection anchor. Example: "High --
C-04 will file this before switching back to SQL; the automated scheduling advantage keeps them
trying despite the setup friction."]
Severity: [P0 | P1 | P2 | P3] -- [One sentence: broken/inaccessible (P0/P1) or workaround
available (P2/P3)? If the competing solution is the available workaround, state that explicitly.]

**STATUS QUO connection:** [Persona mode -- you ARE the persona named above. Before filing this
ticket, you tried the competing solution first. State in first person: what you tried, how long,
what step failed, what made you continue with the new feature rather than reverting. Name the
specific competing-solution element from COMPETING SOLUTION section -- the current solution name,
the switching friction level, the solution gap, or the defection anchor behavior.
Example: "I tried [current solution name] first -- spent [X minutes] getting to [step], hit
[specific failure], and decided to file because the [current solution gap] would still not be
solved by going back." Do not write "N/A" or a generic reference to the STATUS QUO.]

**Ticket Body** [Persona mode -- you ARE this persona. File the ticket in your own voice.]
> [First person. You are this persona. Write as you would write. SRE: you are describing
> infrastructure failure in your own operational terms -- runbooks, SLAs, observability.
> C-XX: you are describing the business workflow that is blocked in your domain vocabulary.
> PM: you are naming the metric at risk and the user impact you are reporting.
> Reference what you tried in the competing solution (from STATUS QUO connection above) as
> context for why you are filing now. Minimum 3 sentences. Do not write "the user" or "they."
> You are filing this ticket. Do not describe what the persona would say -- say it.]

---

### T-02 (Phase 1)

**Support: Triage** [Analyst mode]
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating** [Analyst mode]
Volume: [high | medium | low] -- [One sentence: reference switching friction and defection risk.
If this ticket has low volume because the competing solution is easy to revert to for this ticket
type, state that explicitly.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale. Note if competing solution is the
available workaround that suppresses severity.]

**STATUS QUO connection:** [Persona mode -- you ARE this persona. First person, specific competing-
solution element named. Different element from T-01 if root cause differs; note if same root.]

**Ticket Body** [Persona mode -- you ARE this persona.]
> [First person. Your vocabulary, your concerns, your competing-solution context. Role-specific
> language: say it, do not describe it.]

---

[Add T-03 and beyond for Phase 1 if needed. Same card structure. STATUS QUO connection and
Ticket Body in persona mode per card. The persona changes per card.]

## PHASE 2: LEARNING CURVE (Days 15-60)

[Users who crossed the switching threshold in Phase 1. Competing-solution inertia decreases
for committed users. Generate at least 2 tickets. Persona mode for STATUS QUO connection and
Ticket Body in each card.]

### T-03 (Phase 2)

**Support: Triage** [Analyst mode]
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating** [Analyst mode]
Volume: [high | medium | low] -- [One sentence; explain volume shift from Phase 1. If lower,
is it because committed users have cleared the competing-solution threshold?]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Persona mode -- first person. If this Phase 2 ticket traces to a
competing-solution element: "When I hit this, I checked [competing solution] first -- [what you
found or tried, first person]." If this ticket emerges from post-commitment behavior: "I have
already switched fully -- this is not about the old tool. [One sentence: what drives it instead,
first person]."]

**Ticket Body** [Persona mode -- you ARE this persona.]
> [First person. Role-specific vocabulary. Phase 2 bodies reflect a user who has been running
> the feature for 2-4 weeks -- you have context, you have tried things, you are not new.]

---

### T-04 (Phase 2)

**Support: Triage** [Analyst mode]
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating** [Analyst mode]
Volume: [high | medium | low] -- [One sentence rationale.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Persona mode -- competing-solution element or post-commitment note,
first person.]

**Ticket Body** [Persona mode -- you ARE this persona.]
> [First person. Role-specific vocabulary.]

---

[Add more Phase 2 tickets as needed.]

## PHASE 3: ADVANCED USE (Days 61-90)

[Power users pushing feature limits. Competing solution is largely irrelevant for this cohort.
Generate at least 1 ticket.]

### T-05 (Phase 3)

**Support: Triage** [Analyst mode]
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating** [Analyst mode]
Volume: [high | medium | low] -- [One sentence; explain lower volume. Note whether the competing
solution is still a reversion option or has been permanently replaced.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Persona mode -- competing-solution element or Phase 3 emergence note,
first person. Phase 3 personas have been running the feature for weeks and rarely reference the
competing solution; note explicitly if they no longer think about it.]

**Ticket Body** [Persona mode -- you ARE this persona.]
> [First person. Role-specific vocabulary. Phase 3 bodies reflect deep familiarity with the
> feature -- you are not asking basic questions; you are pushing limits, integrating edge cases,
> or requesting capabilities the feature does not yet have.]

---

[Add more Phase 3 tickets as needed.]

## COVERAGE CHECKS
[Return to analyst mode for all checks below.]

Category coverage: [List distinct category values across all phases. Must be >= 3. If fewer, add tickets.]
Volume coverage: Phase 1 = [value] | Phase 2 = [value] | Phase 3 = [value]
Distinct volume levels: [Count. Must be >= 2. If all phases share one value, explain in terms of
competing-solution switching behavior -- a uniform-volume explanation citing defection dynamics
passes; "all tickets are equally important" does not.]
Phase distribution: Phase 1: [N] | Phase 2: [N] | Phase 3: [N] | Total: [N]

## COMPETING SOLUTION TRACE ENUMERATION
[Analyst mode. Complete this table after all ticket cards AND the Gap Analysis section are
written. Fill one row per ticket whose STATUS QUO connection field names a specific competing-
solution element (first-person or analyst-mode -- the element must be specifically named, not
paraphrased as "status quo" or "competing solution baseline"). Each ticket gets its own row.
Column 3 (Gap traced to) must name the gap from the Gap Analysis section that the STATUS QUO
element drives. A gap appearing in the Gap Analysis but in no column-3 row has no ticket evidence
-- add a ticket or remove the gap. A bridge row with "Gap traced to: general" does not count.
If the table has fewer than 2 rows, revise those ticket cards before proceeding.]

| Ticket ID | Competing-solution element named in connection field | Gap traced to |
|-----------|------------------------------------------------------|---------------|
| [T-XX]    | [The specific named element, e.g., "C-04 direct SQL reversion threshold (30 min) -- from persona-mode STATUS QUO connection"] | [Gap name from Gap Analysis, e.g., "Doc gap: no data engineer onboarding guide"] |
| [T-XX]    | [Specific element as stated in the connection field -- must be nameable] | [Gap name or "Phase N emergence -- no gap trace"] |
[Add one row per ticket with a specific competing-solution element named.]

Trace count: [N]. Required: >= 2.
Gap coverage check: [List any Gap Analysis gaps not in column 3. If all gaps appear, write
"All gaps evidenced." If any gap has no column-3 row, name it -- then add a ticket or remove
the gap before proceeding.]
Gate: [PASSES | REVISE -- identify which cards or gaps need revision before proceeding.]

## GAP ANALYSIS
[Analyst mode.]

### Doc Gaps
[Reference the current solution gap from COMPETING SOLUTION. Doc gaps that go unclosed keep
the competing solution viable for a wider population -- note the reversion path they leave open.]
- [Gap 1: missing doc, which ticket(s) it drives, which phase(s), and which competing-solution
  reversion path it leaves open if unclosed.]
[Add as needed.]

### Design Gaps
- [Gap 1: missing UX affordance or behavioral contract, which ticket(s), which phase. Note if
  the competing solution handles this case better today.]
[Add as needed.]

### Operational Gaps
- [Gap 1: missing operational element, which ticket(s), which phase.]
[Add as needed.]

### Priority Close Order
[Rank by severity, volume, and reversion risk. A gap that leaves the competing solution's primary
advantage intact ranks higher regardless of ticket volume alone.]
1. [Highest-priority gap] -- prevents: [ticket IDs, phase, severity, volume.] -- reversion risk: [one sentence: which persona reverts if this gap stays open?]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Analyst mode. Identify at least one systemic pattern spanning two or more phases. Name it,
cite ticket IDs with phase labels, trace the root cause to COMPETING SOLUTION.

Fill in the four consequence fields below. Each field is required and independently checkable.
Do not nest these inside a "Consequence:" parent. Do not collapse into a single sentence.
The reversion path must be named explicitly. Each field carries a "Prohibited:" sentinel -- a
value matching the prohibited example fails that field regardless of other content present.]

Pattern name: [One name for this pattern.]
Pattern tickets: [T-01 (P1), T-03 (P2), ...] with phase labels.
Pattern root cause: [One sentence tracing to the competing-solution element -- switching friction,
defection anchor, or current solution gap -- that this pattern exposes.]

Consequence -- Affected segment: [Who specifically is still at reversion risk at day 90? Name
the exact role or user cohort from the ticket cards and COMPETING SOLUTION defection anchor.
Not generic. The named cohort must appear in the ticket IDs above. Example: "C-04 data engineers
who completed Phase 1 setup but have not yet moved their primary scheduling workload off direct
SQL -- estimated 40% of target C-04 installs at this stage."]
Prohibited: "users" | "customers" | "affected teams" | any cohort label not drawn from a named
stock role appearing in the ticket cards above. A cohort not traceable to a specific ticket
card fails this field.

Consequence -- Day-90 scenario: [What does the support queue look like and what reversion behavior
is still active at day 90 if this pattern is unaddressed? One specific event tied to this pattern
and these ticket IDs. Reference the competing solution still in use. Name at least two ticket IDs
explicitly. Example: "T-03 and T-04 continue at medium volume; C-04 teams are running SQL jobs
in parallel as a safety net because the scheduling conflict doc was never shipped."]
Prohibited: "tickets continue to arrive" without naming a specific competing-solution behavior
still active at day 90. A scenario that does not name the competing solution still in use and
does not cite the specific ticket IDs for this pattern fails this field.

Consequence -- Adoption cost: [What does leaving this pattern open cost the feature's competitive
position? One sentence naming a rate, dependency blocked, or retained competing-solution share.
Specific to this pattern. Example: "The direct-SQL workflow retains C-04's primary scheduling
load until the conflict resolution doc ships -- estimated 40% of target installs are partial,
handling only non-critical jobs through the new feature."]
Prohibited: "this will cause user confusion" | "adoption will be impacted" | "users will be
frustrated" | any statement that does not name the competing solution or a specific rate,
duration, or blocked dependency. A cost that could be pasted verbatim into any other support
ticket analysis fails this field.

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, competing_solution_friction,
             status_quo_traced_ticket_count, gaps_with_ticket_evidence.
```

---

## Round 4 Design Notes

### Axis selection rationale

All five R3 variations scored at or near 130/130 on the v4 rubric. V-04 and V-05 R3 are identical
in rubric performance (both 130/130). Round 4's question is not "how do we reach the ceiling?" --
V-05 R3 already does that. Round 4's question is: "what structural improvements above the ceiling
might reveal C-17/C-18 failure modes?"

The escalation pattern through four rounds:
- Round 1: Existence gates -- STATUS QUO section present; consequence present
- Round 2: Verification gates -- self-check enumeration exists; fields are separate
- Round 3: Format gates -- enumeration is a table; fields are flat (no container)
- Round 4: **Content gates** -- table has a cross-reference column (gap bridge); fields have
  per-field prohibited sentinels; register shifts from characterization to performance

V-01 (gap bridge column) targets the next structural level of C-15: not just "is the table
present and per-ticket?" but "does the table's column 3 close the gap between the trace section
and the gap analysis section?" The failure mode this prevents: a gap analysis with items not
evidenced by any ticket -- gap inflation that was invisible in a two-column table.

V-02 (per-field sentinels) targets the next structural level of C-16: not just "are the fields
flat and independent?" but "does each field carry a locally-checkable prohibition?" The failure
mode this prevents: a generic value that passes a cross-field comparison check but does not
obviously violate the section-level prohibition because other content camouflages the weak field.

V-03 (role-simulation register) is an untested axis. It has not appeared in any prior round.
The hypothesis: characterization mode produces a description of what a persona would say;
performance mode produces what they actually say. The STATUS QUO connection field is the
primary beneficiary -- a model filing as the persona must state what *it* tried before filing,
not what the persona "would have tried." This converts a description of behavior into a first-
person report of behavior, carrying more specific content by construction.

V-04 combines V-01 and V-02 without V-03 (the minimum content-gate upgrade, no register change).
V-05 combines all three on the V-05 R3 base (full synthesis R4).

### Structural comparison table: C-15 mechanism

| V | C-15 mechanism | What it prevents |
|---|----------------|-----------------|
| V-01 R4 | 3-column table (ticket ID, element, gap traced to) | Gap inflation -- gaps without ticket evidence become visible |
| V-02 R4 | 2-column table (V-05 R3 unchanged) | Same as V-05 R3: paragraph collapse impossible, row count self-verifying |
| V-03 R4 | 2-column table (V-05 R3 unchanged) | Same as V-05 R3 |
| V-04 R4 | 3-column table (same as V-01 R4) | Gap inflation visible |
| V-05 R4 | 3-column table with persona-mode element naming | Gap inflation visible; first-person element names may be more specific |

### Structural comparison table: C-16 mechanism

| V | C-16 mechanism | What it prevents |
|---|----------------|-----------------|
| V-01 R4 | Flat fields (V-05 R3 unchanged) | Container-level compliance with component genericity |
| V-02 R4 | Flat fields + per-field prohibited sentinels | Named generic values are locally checkable failures per field |
| V-03 R4 | Flat fields (V-05 R3 unchanged) | Container-level compliance with component genericity |
| V-04 R4 | Flat fields + per-field prohibited sentinels (same as V-02) | Named generic values are locally checkable |
| V-05 R4 | Flat fields + per-field prohibited sentinels + reversion framing | Named generic values + reversion path naming prevents the specific generic values that inertia framing makes available |

### Cross-variation experiment matrix

| Question | Variations that answer it |
|----------|--------------------------|
| Does the gap bridge column improve gap analysis quality? | V-01 vs. V-05 R3 baseline -- if V-01 produces fewer unsupported gaps, the column is load-bearing |
| Do per-field sentinels produce more specific consequence fields than section-level prohibition? | V-02 vs. V-05 R3 baseline -- if V-02's consequence fields name more specific cohorts, events, and costs, sentinels are load-bearing |
| Does role-simulation register improve C-03/C-08 body authenticity? | V-03 vs. V-05 R3 baseline -- if V-03's ticket bodies are more role-specific, the register shift is load-bearing |
| Is the minimal combination sufficient to reveal new failure modes? | V-04 vs. V-05 R3 -- if V-04 produces visibly different gap analysis and consequence quality, the two additions are structural |
| Does role-simulation add value on top of the content gates? | V-05 vs. V-04 -- if V-05 ticket bodies are more authentic, the register shift adds content-level value beyond structural gates |
