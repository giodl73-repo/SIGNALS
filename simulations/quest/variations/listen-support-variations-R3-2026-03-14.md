Written to `simulations/quest/variations/listen-support-variations-R3-2026-03-14.md`.

---

## Round 3 Variations -- listen-support

| V | Axis | Hypothesis |
|---|------|------------|
| **V-01** | C-13 gate format (enumeration table vs. text check) | A mandatory table -- one row per traced ticket -- structurally prevents summary statements from passing C-13; row count is self-evident and no single sentence can cover multiple rows |
| **V-02** | C-14 consequence field structure (flat labeled fields vs. nested bullets) | Flat top-level fields at the same level as "Pattern name:" eliminate the parent-container escape; each field is independently checkable, no single sentence can satisfy all three |
| **V-03** | Inertia framing (STATUS QUO reframed as active competing solution) | Competitor framing sharpens volume calibration (each ticket is a defection signal) and consequence specificity (pattern consequence names the reversion path that stays open) |
| **V-04** | C-13 table + C-14 flat fields combined (V-05 R2 base, no other changes) | Minimal structural upgrade from 110 to 120; tests whether two field-format changes alone are sufficient |
| **V-05** | Full synthesis R3 (V-05 R2 + table + flat fields + inertia framing) | All 14 criteria structurally enforced; ceiling 120/120 |

---

**What each variation isolates:**

- **V-01 vs. V-05 R2 baseline**: Does the table form matter for C-13, or does V-05 R2's text check already pass? If V-01 scores higher on C-13, the table is the load-bearing mechanism.
- **V-02 vs. V-05 R2 baseline**: Are nested bullets structurally sufficient for C-14, or must the fields be flat? If V-02 scores higher on C-14, flat fields are necessary.
- **V-03 vs. V-05 R2 baseline**: Does reversion-risk framing improve C-07/C-12 quality without sacrificing C-01/C-02 compliance?
- **V-04 score alone**: If 120/120, the minimal upgrade path works and V-05 is redundant.
- **V-05 vs. V-04**: Does inertia framing add measurable quality on top of the structural upgrades?
 questions this round answers:**
- Does V-05 R2's text-format traceability check already pass C-13, or does a table form matter? (V-01 vs. V-05 R2 baseline)
- Are V-05 R2's nested bullet consequence fields structurally separate enough for C-14, or must they be flat? (V-02 vs. V-05 R2 baseline)
- Does inertia framing improve consequence specificity (C-12/C-14) or introduce overhead that risks C-01/C-02 compliance? (V-03)

---

## V-01: C-13 Enumeration Table Gate

**Axis:** C-13 gate format -- V-05 R2 base with the STATUS QUO traceability check text replaced
by a mandatory enumeration table in COVERAGE CHECKS. One row per traced ticket; each row
independently requires a ticket ID and a named scenario element. Everything else is V-05 R2
unchanged.
**Hypothesis:** V-05 R2's traceability check is a text field with an example format ("T-01 --
traces to GitHub Issues channel gap; T-02 -- traces to missing setup doc"). This format permits
the model to write a compact paragraph that mentions two ticket IDs without enumerating them as
truly independent entries. A table form structurally prevents the paragraph collapse: the model
must fill a separate row for each ticket, and each row's "STATUS QUO element" column requires a
named element that cannot be shared with another row's cell. The table is also self-checking --
the row count is directly visible, making the "Count: N. Passes." gate trivially verifiable.

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

## STATUS QUO TRACE ENUMERATION
[Complete this table after all ticket cards are written. Fill one row per ticket whose STATUS
QUO connection field names a specific STATUS QUO element (not an emergence note). Do not write
a summary statement covering multiple tickets in one sentence. Each ticket gets its own row.
If the table has fewer than 2 rows, revise those ticket cards before proceeding.]

| Ticket ID | STATUS QUO element named in connection field | Element type |
|-----------|----------------------------------------------|--------------|
| [T-XX]    | [The specific element from STATUS QUO this card references, e.g., "missing setup doc" or "Slack-ask workaround as primary path"] | [workaround \| channel-gap \| doc-gap \| friction-level] |
| [T-XX]    | [Specific element -- must be named, not "STATUS QUO baseline"] | [type] |
[Add one row per ticket with a specific STATUS QUO element named. Emergence-note tickets are not counted.]

Trace count: [N]. Required: >= 2. Gate: [PASSES | REVISE -- identify which cards need a specific element named before proceeding.]

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

## V-02: C-14 Flat Consequence Fields

**Axis:** C-14 consequence field structure -- V-05 R2 base with the nested bullet consequence
block replaced by three flat labeled fields at the same structural level as "Pattern:" and
"Root cause:". One single change in CROSS-TICKET PATTERN. Everything else is V-05 R2 unchanged.
**Hypothesis:** V-05 R2's consequence block uses three bullet points under a parent "Consequence:"
label. The parent label creates a container: a model can still write one dense sentence per bullet
that is generic at the component level while naming the parent correctly. Flat fields remove the
parent container entirely -- each field (Pattern -- Affected segment, Pattern -- Day-90 scenario,
Pattern -- Adoption cost) is independently checkable, and no single sentence can satisfy all three
because they require different named specifics: a role or cohort, a dated queue scenario, and a
quantified or qualified cost. The flat format makes C-14's "each component requiring a
pattern-specific value" structurally unambiguous.

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

Fill in all four consequence fields below. Each field is required independently. Do not collapse
into a single sentence or a nested list under "Consequence:". A statement that could be copied
verbatim to any other pattern does not pass any of the three consequence fields.
Prohibited generic statements: "this will cause user confusion," "adoption will be impacted,"
"users will be frustrated." Name the specific cohort, the specific scenario, the specific cost.]

Pattern name: [One name for this pattern.]
Pattern tickets: [T-01 (P1), T-03 (P2), ...] with phase labels.
Pattern root cause: [One sentence tracing to the STATUS QUO workaround, channel gap, or doc gap.]

Consequence -- Affected segment: [Who specifically is still stuck at day 90? Name the exact role
or user cohort from the ticket cards -- not generic "users." Name the cohort that appears in the
specific ticket IDs above. Example: "SRE teams who reached Phase 2 config setup but have no
migration runbook for the legacy config format."]
Consequence -- Day-90 scenario: [What does the support queue look like if this pattern is
unaddressed at day 90? One specific event tied to this named pattern and these named tickets --
not a general trend. Reference ticket IDs. Example: "T-03 and T-04 still arrive at medium volume
because the config migration guide was never written; SRE teams are still using the Phase 1
Slack-ask workaround as their primary migration path."]
Consequence -- Adoption cost: [What does leaving this pattern open cost in adoption friction,
SLA, or user retention? One sentence naming a rate, duration, or downstream dependency blocked --
specific to this pattern. Example: "Each affected SRE team spends 4-6 hours on a workaround that
a 2-page migration guide would eliminate, blocking Phase 2 sign-off for their downstream service
consumers."]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, status_quo_friction,
             status_quo_traced_ticket_count.
```

---

## V-03: Inertia Framing -- STATUS QUO as Competing Solution

**Axis:** Inertia framing -- V-05 R2 base with STATUS QUO section reframed as the competing
solution users actively choose over the new feature. Volume rationale must reference the reversion
risk (how many users will file vs. silently fall back). Consequence must name the reversion path
that stays open if the pattern is not closed. Card structure is V-05 R2 unchanged.
**Hypothesis:** All prior variations frame STATUS QUO as neutral current state. This framing
produces volume rationale that describes population size and frequency, which is accurate but
produces generic calibration. Framing STATUS QUO as the competing solution produces volume
rationale that describes defection risk -- how likely is a user to file a ticket vs. abandon
the feature and revert to the old way? This reversion framing should produce sharper volume
differentiation (C-07) because the question is now "who is committed enough to file?" rather
than "how many users hit this?" It should also produce more specific consequence statements
(C-12/C-14) because the pattern consequence becomes "users who hit this unresolved pattern
have an easy exit: they revert to [named competing solution]."

```
You are running /listen:support. Fill in this structured template.
Topic and signal are provided as inputs. COMPETING SOLUTION section runs first -- this describes
what users do instead of the feature being analyzed. The 90-day window is divided into three
phases. Each ticket is a structured card with role-labeled sections including a mandatory STATUS
QUO connection field. All section headers and card fields are required.
Do not reorder or remove any section.
Controlled vocabulary is mandatory: category in {how-to, bug, feature-request, config, integration};
severity in {P0, P1, P2, P3}; volume in {high, medium, low}.
Stock roles for persona field: Support, SRE, PM, UX, C-01 through C-12.

---

## SETUP
Topic: [Feature or product being analyzed.]
Signal: [Artifact being used as input.]

## COMPETING SOLUTION: WHAT USERS DO INSTEAD
[Complete before generating any tickets. Describes the solution users return to if the feature
under analysis disappoints. This is not a neutral baseline -- it is the active alternative.
Volume ratings reflect defection risk: a high-volume ticket means users are still trying the
feature; a low-volume ticket in an area with a strong competing solution may mean users have
already abandoned silently. If the competing solution varies significantly by persona, note the
dominant pattern and flag exceptions.]

Current solution: [What users do today to solve the problem this feature addresses. One sentence
per distinct alternative -- name the tool, process, or workaround specifically, not generically.]
Where it lives: [The specific tool, channel, document, or command users use to execute the current
solution. Be specific: "direct SQL queries via pgAdmin" not "the database directly."]
Switching friction: [high | medium | low -- how hard is it to switch from the current solution
to this feature? High = strong inertia toward the competing solution; low = users will switch
easily if the feature works.]
Current solution gap: [What the current solution cannot do that this feature enables. One sentence.
This is the feature's competitive advantage over the status quo -- the reason users might switch.]
Defection anchor: [One sentence naming the persona most likely to revert and the threshold at
which they abandon. Example: "C-04 (data engineers) will revert to direct SQL if API setup
requires > 30 min -- they know the current solution well and switching cost is low." This anchors
which tickets are defection signals vs. committed-user signals.]

## PHASE 1: LAUNCH WEEK (Days 1-14)

[First adopters hit setup and prerequisite walls. Volume shaped by competing-solution inertia:
high friction here means users are testing the feature against a known alternative. Generate at
least 2 tickets. For each, ask: does this ticket come from a user committed enough to push through
friction, or is this their last attempt before reverting?]

### T-01 (Phase 1)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence: how many users will hit this and still file
vs. reverting to the competing solution? Reference the switching friction and defection anchor.
Example: "High -- C-04 personas will file this before switching back to SQL; the feature's
competitive gap (automated scheduling) is strong enough to keep them trying."]
Severity: [P0 | P1 | P2 | P3] -- [One sentence: broken/inaccessible (P0/P1) or workaround
available (P2/P3)? Note: if the competing solution is the workaround, state that explicitly.]

**STATUS QUO connection:** [Name the specific competing-solution element this ticket traces to:
the current solution they tried first, the switching friction level, the current solution gap,
or the defection anchor persona behavior. Be specific. Example: "Traces to the defection anchor
-- C-04 persona tried direct SQL first (30 min), then filed this ticket as their last attempt
before reverting." Do not leave blank or write "N/A".]

**Ticket Body**
> [First-person body in persona's voice. Reference what the persona tried in the competing
> solution before filing -- what they did in the old tool, what failed to transfer, why they
> are still trying the new feature. Role-specific vocabulary required. SRE: ops/infra language.
> C-XX: domain and business context. PM: impact/metrics framing. Minimum 3 sentences. Not a
> generic body. Do not write a body that ignores the competing solution context.]

---

### T-02 (Phase 1)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence: reference competing-solution switching friction
and the filing persona's defection risk. If this ticket has low volume because the competing
solution is easy to revert to, state that explicitly.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale. Note if competing solution is the
available workaround that suppresses severity.]

**STATUS QUO connection:** [Competing-solution element this ticket traces to. Different from T-01
if root cause differs; note explicitly if same root.]

**Ticket Body**
> [First-person body in persona's voice. Reference competing-solution context. Role-specific
> language required.]

---

[Add T-03 and beyond for Phase 1 if needed. Same card structure. STATUS QUO connection required in every card.]

## PHASE 2: LEARNING CURVE (Days 15-60)

[Users who did not revert in Phase 1 are now integrating the feature into workflows. Competing
solution inertia decreases for committed users; Phase 2 tickets come from users who have made
the switch and are now hitting config, integration, and edge-case walls. Volume decreases from
Phase 1. Generate at least 2 tickets.]

### T-03 (Phase 2)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence; explain volume shift from Phase 1. If lower,
is it because users have committed past the competing-solution reversion threshold, or because
fewer users remain active?]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Competing-solution element or Phase 2 emergence note. Phase 2 tickets
often emerge from users who have already switched and can no longer revert easily -- note if that
changes the competing-solution framing.]

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

[Power users pushing feature limits. Competing solution is largely irrelevant for this cohort --
they have committed. Volume is lower. Generate at least 1 ticket.]

### T-05 (Phase 3)

**Support: Triage**
Title: [One sentence.]
Category: [how-to | bug | feature-request | config | integration]
Persona: [Stock role]

**PM: Rating**
Volume: [high | medium | low] -- [One sentence; explain lower volume. Note whether the competing
solution is still relevant to this Phase 3 persona or has been permanently replaced.]
Severity: [P0 | P1 | P2 | P3] -- [One sentence rationale.]

**STATUS QUO connection:** [Competing-solution element or Phase 3 emergence note.]

**Ticket Body**
> [First-person body in persona's voice. Role-specific language required.]

---

[Add more Phase 3 tickets as needed.]

## COVERAGE CHECKS

Category coverage: [List distinct category values across all phases. Must be >= 3. If fewer, add tickets.]
Volume coverage: Phase 1 = [value] | Phase 2 = [value] | Phase 3 = [value]
Distinct volume levels: [Count. Must be >= 2. If all phases share one level, explain why in terms
of competing-solution switching behavior, not volume washing.]
Phase distribution: Phase 1: [N] | Phase 2: [N] | Phase 3: [N] | Total: [N]
STATUS QUO traceability check: [List the ticket IDs whose STATUS QUO connection field names a
specific competing-solution element (not an emergence note). Must be at least 2. If fewer than
2, revise before proceeding. Example: "T-01 -- traces to defection anchor (C-04 SQL reversion
threshold); T-02 -- traces to switching friction (high, competing solution is well-known).
Count: 2. Passes."]

## GAP ANALYSIS

### Doc Gaps
[Reference the current solution gap from COMPETING SOLUTION. Each doc gap that goes unclosed
keeps the competing solution viable for a wider population.]
- [Gap 1: missing doc, which ticket(s) it drives, which phase(s), and which competing-solution
  reversion path it leaves open.]
[Add as needed.]

### Design Gaps
- [Gap 1: missing UX affordance or behavioral contract, which ticket(s), which phase, and
  whether the competing solution handles this case better today.]
[Add as needed.]

### Operational Gaps
[Reference the competing solution's operational simplicity if it creates a design gap.]
- [Gap 1: missing operational element, which ticket(s), which phase.]
[Add as needed.]

### Priority Close Order
[Rank by severity, volume, and reversion risk. A gap that leaves the competing solution's primary
advantage intact ranks higher than a cosmetic gap, regardless of ticket volume alone.]
1. [Highest-priority gap] -- prevents: [ticket IDs, phase, severity, volume.] -- reversion risk: [one sentence: which personas revert if this gap stays open?]
2. [Second-priority gap] -- prevents: [ticket IDs.]
[Continue until all gaps are ranked.]

## CROSS-TICKET PATTERN
[Identify at least one systemic pattern spanning two or more phases. Name it, cite ticket IDs
with phase labels, and trace the root cause to the COMPETING SOLUTION.

Fill in the three-part consequence structure below. Every part is required. Do not collapse into
one sentence. The key framing for this variation: the consequence of leaving a pattern open is
that the reversion path stays clear for the affected segment -- the competing solution remains
their active fallback. Name the reversion path explicitly in the consequence fields.
A generic statement ("this will cause user confusion") does not pass any part.]

Pattern: [Name] -- tickets: [T-01 (P1), T-03 (P2), ...] -- root cause: [One sentence tracing
to the competing solution element that this pattern exposes -- the switching friction, the
defection anchor, or the current solution gap that the feature has not yet closed.]

Consequence:
- Affected segment: [Who specifically is still at risk of reverting at day 90? Name the exact
  role or user cohort from the ticket cards -- not generic "users." Name the defection anchor
  persona if applicable. Example: "C-04 data engineers who completed Phase 1 setup but have
  not yet switched their primary scheduling workflow from direct SQL."]
- Day-90 scenario: [What does the support queue look like and what reversion behavior is still
  active if this pattern is unaddressed at day 90? One specific scenario tied to this named
  pattern. Reference ticket IDs and the competing solution still in use. Example: "T-03 and T-04
  continue arriving at medium volume; C-04 personas are still running SQL jobs in parallel as
  a safety net because the scheduling conflict resolution doc was never written."]
- Adoption cost: [What does this pattern cost in adoption friction, SLA, or competitive position?
  One sentence naming what stays broken or what the competing solution retains. Example: "The
  competing SQL-direct workflow retains C-04's primary workload until the scheduling doc ships --
  estimated 40% of target C-04 installations are partial deployments where the feature handles
  only non-critical jobs."]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, competing_solution_friction,
             status_quo_traced_ticket_count.
```

---

## V-04: C-13 Table + C-14 Flat Fields (V-05 R2 Base, Minimal Upgrade)

**Axes:** C-13 gate format + C-14 consequence field structure -- V-05 R2 base with exactly two
changes: (1) the text-format STATUS QUO traceability check replaced by the enumeration table
from V-01, (2) the nested bullet consequence block replaced by the flat labeled fields from V-02.
No other changes from V-05 R2. Inertia framing, phase structure, STATUS QUO connection field, and
all other mechanisms are unchanged.
**Hypothesis:** V-05 R2 scored 110/110 on the v2 rubric. The v3 rubric adds C-13 and C-14. If
V-05 R2's existing mechanisms already partially satisfy C-13 (text check names ticket IDs) and
C-14 (nested bullets are structurally labeled), the gap to 120 may require only the two targeted
field-format changes in V-01 and V-02. V-04 tests this minimal-overhead hypothesis: no new
framing, no new phases, no new sections -- just replacing a text check with a table and a nested
list with flat fields.

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
name the element, not just "the STATUS QUO." Do not leave blank or write "N/A".]

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

## STATUS QUO TRACE ENUMERATION
[Complete this table after all ticket cards are written. Fill one row per ticket whose STATUS
QUO connection field names a specific STATUS QUO element (not an emergence note). Do not write
a summary statement covering multiple tickets in one sentence. Each ticket gets its own row.
If the table has fewer than 2 rows, revise those ticket cards before proceeding.]

| Ticket ID | STATUS QUO element named in connection field | Element type |
|-----------|----------------------------------------------|--------------|
| [T-XX]    | [The specific element this card references, e.g., "missing setup doc" or "Slack-ask workaround"] | [workaround \| channel-gap \| doc-gap \| friction-level] |
| [T-XX]    | [Specific element -- must be named, not paraphrased as "STATUS QUO baseline"] | [type] |
[Add one row per ticket with a specific STATUS QUO element named. Emergence-note tickets are not counted.]

Trace count: [N]. Required: >= 2. Gate: [PASSES | REVISE -- identify which cards need revision before proceeding.]

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

Fill in all four consequence fields below. Each field is required and independently checkable.
Do not nest these inside a "Consequence:" parent block. Do not collapse into a single sentence.
A statement that would fit any other pattern equally well does not pass any of the three
consequence fields. Named failure patterns: "this will cause user confusion" (fails all three);
"users will be impacted" (fails all three); "adoption will suffer" (fails all three).]

Pattern name: [One name for this pattern.]
Pattern tickets: [T-01 (P1), T-03 (P2), ...] with phase labels.
Pattern root cause: [One sentence tracing to the STATUS QUO workaround, channel gap, or doc gap.]

Consequence -- Affected segment: [Who specifically is still stuck at day 90? Name the exact role
or user cohort from the ticket cards above -- not generic "users." The segment must appear in the
named ticket IDs. Example: "Developers who completed Phase 1 onboarding but have not yet
migrated their multi-tenant routing config from the legacy format."]
Consequence -- Day-90 scenario: [What does the support queue look like if this pattern is
unaddressed at day 90? One specific event tied to this named pattern and these named ticket IDs --
not a general trend. Example: "T-03 and T-04 continue arriving at medium volume because the
config migration guide still does not exist; developers are still using the Phase 1 Slack-ask
workaround as their primary migration path."]
Consequence -- Adoption cost: [What does this pattern cost in adoption friction, SLA, or user
retention? One sentence naming a rate, duration, or downstream dependency blocked. Specific to
this pattern. Example: "Each affected team spends 4-6 hours on a workaround that a 2-page
migration guide would eliminate, blocking Phase 2 sign-off for their downstream service consumers."]

---

Write artifact: simulations/listen/support/{topic}-support-{date}.md
Frontmatter: skill, topic, date, ticket_count, categories_covered, gap_count,
             phase1_count, phase2_count, phase3_count, status_quo_friction,
             status_quo_traced_ticket_count.
```

---

## V-05: Full Synthesis R3

**Axes:** All winning R2 mechanisms + C-13 enumeration table + C-14 flat labeled consequence
fields + inertia competitor framing for STATUS QUO. V-05 R2 (110/110) upgraded with the three
new mechanisms targeting C-13, C-14, and enhanced C-07/C-12 quality.
**Hypothesis:** V-05 R2 is the R2 golden. The v3 rubric adds C-13 and C-14 as aspirational
criteria worth 5 pts each. V-05 R2 likely partially satisfies both under the new rubric: its
text traceability check names ticket IDs (C-13 partial) and its nested bullets are labeled fields
(C-14 partial). The three additions in V-05 R3 remove all ambiguity: the enumeration table makes
C-13 trivially verifiable (row count); the flat consequence fields make C-14 trivially verifiable
(each field independently checkable); and the inertia competitor framing sharpens C-07/C-12
quality by grounding volume and consequence in reversion risk rather than population size.
Combined ceiling: 120/120.

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
passes; a uniform-volume explanation citing "all tickets are equally important" does not.]
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
| [T-XX]    | [The specific competing-solution element, e.g., "C-04 direct SQL reversion threshold (30 min)" or "no structured ticket channel exists for this path today"] | [current-solution \| switching-friction \| solution-gap \| defection-anchor] |
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
             status_quo_traced_ticket_count.
```

---

## Round 3 Design Notes

### Axis selection rationale

V-01 and V-02 are single-mechanism changes to V-05 R2, each targeting one of the two new v3
criteria. This isolates whether the criterion can be passed by a minimal structural change
(field format) without adding new sections or framing. V-03 is the first inertia-framing
experiment -- it has not appeared in any prior round, and the v3 rubric's C-07/C-12 requirements
are well-suited to testing whether reversion-risk language sharpens calibration vs. introducing
vocabulary overhead that risks C-01/C-02. V-04 combines V-01 and V-02 without V-03 -- the
minimum-change ceiling test. V-05 adds V-03 to V-04 for the full synthesis.

Phrasing register and lifecycle emphasis were not chosen as the primary single-axis experiments
because the new v3 criteria (C-13/C-14) are insensitive to register -- they test structural
properties of specific fields. Inertia framing was chosen as the third single-axis test because
it is the one untested axis most likely to improve C-07/C-08/C-12 quality independently of the
structural gate and field format changes.

### C-13 structural comparison

| V | C-13 mechanism | Structural property |
|---|----------------|---------------------|
| V-01 | Enumeration table (one row per ticket, ticket ID + element + type) | Row count is self-evident; single-sentence summaries are impossible |
| V-02 | V-05 R2 text check (unchanged) | Text format; compact paragraph permitted; summary statement possible |
| V-03 | V-05 R2 text check (unchanged, with competitor framing) | Same structural property as V-05 R2; competitor labels may improve element naming |
| V-04 | Enumeration table (same as V-01) | Row count self-evident |
| V-05 | Enumeration table (same as V-01, competitor element types) | Row count self-evident; element types extended for competitor framing |

### C-14 structural comparison

| V | C-14 mechanism | Structural property |
|---|----------------|---------------------|
| V-01 | V-05 R2 nested bullets (unchanged) | Three labeled bullets under "Consequence:" parent |
| V-02 | Flat labeled fields (Consequence -- Affected segment, etc.) | No parent container; each field independently checkable |
| V-03 | V-05 R2 nested bullets (unchanged, with competitor framing) | Same structure as V-05 R2; reversion framing may improve specificity without structural change |
| V-04 | Flat labeled fields (same as V-02) | No parent container |
| V-05 | Flat labeled fields (same as V-02, with reversion framing) | No parent container; reversion framing adds content specificity on top of structural separation |

### Cross-variation experiment matrix

| Question | Variations that answer it |
|----------|--------------------------|
| Does the text traceability check already pass C-13, or must it be a table? | V-01 vs. V-05 R2 (if V-01 scores higher on C-13 than V-05 R2, table form is load-bearing) |
| Are V-05 R2's nested bullets structurally sufficient for C-14? | V-02 vs. V-05 R2 (if V-02 scores higher on C-14, flat fields are load-bearing) |
| Does inertia framing improve C-07/C-12 quality while preserving C-01/C-02? | V-03 vs. V-05 R2 |
| Is the minimal upgrade (table + flat fields) sufficient to reach 120? | V-04 score: if 120, the answer is yes |
| Does inertia framing add value on top of the structural upgrades? | V-05 vs. V-04 |
