---
skill: review-customers
topic: signal-plugin-docs
audience: BIC Microsoft customers
date: 2026-03-16
status: COMPLETE
input: QUICKSTART.md, ACHIEVEMENTS.md, guides/scout.md, guides/corps.md
rubric: review-customers-rubric-v5
---

# Signal Docs — BIC Customer Review
## Customer Advisory Panel: 12 Microsoft / BIC Personas

Work through this as a customer advisory panel. Each person has read the Signal QUICKSTART, scanned
ACHIEVEMENTS.md, and reviewed the scout and corp guides. They bring their real work context into
the room. Take each person through the docs one at a time.

---

## EACH PERSON

---

[C-01] Priya Sharma (Senior PM, Power Platform / Dynamics 365) | Tier: PRIMARY

- Usefulness [1-5]: 5
- Clarity [1-5]: 4
- Would-Adopt [1-5]: 4

Rationale: Priya's core job is justifying features to stakeholders before committing budget and
engineering time. The QUICKSTART's inertia rule — "Why would teams do nothing?" as the first
question — maps directly onto the pre-requisite she currently handles manually via BIC telemetry
plus ad hoc stakeholder conversations. Signal's `/scout-competitors` produces the inertia case in
10 minutes; her current equivalent takes a multi-day synthesis of NPS data, feature usage dashboards,
and stakeholder interviews. The specific mechanism that drives her high would-adopt: the
`--for exec` parameter and `--mode risk` combination on scout skills produces output framed as
cost-of-not-acting, which is exactly the frame her stakeholders require — not a feature description,
but a risk case. The one friction point: the docs assume a code repo is the primary workspace, and
Priya's evidence artifacts today live in SharePoint and ADO tickets, not a `simulations/` directory.
The file-system artifact model is a workflow delta she will need to absorb.

Flags: [DELIGHT: Usefulness — inertia-first framing maps precisely onto the PM stakeholder
justification workflow]

---

[C-02] Marcus Johnson (Principal Engineer, Dynamics 365 Commerce) | Tier: PRIMARY

- Usefulness [1-5]: 3
- Clarity [1-5]: 4
- Would-Adopt [1-5]: 2

Rationale: Marcus cares about not shipping regressions and is skeptical of process overhead that
does not directly reduce defect rate or review burden. The `trace` namespace — specifically
`/trace-contract` and `/trace-state` — addresses his exact risk: does the implementation match
the spec? The QUICKSTART's "Common starting points" table maps "Implementation done, want to verify
it matches spec" to `/trace-contract`, which is a direct answer to his workflow. However, the
would-adopt score is suppressed by a specific doc gap: the `trace` namespace skills are listed but
not demonstrated with a runtime code example anywhere in QUICKSTART or the scout/corp guides
available. The mechanism: Marcus cannot evaluate whether `trace-contract` produces findings with
enough technical specificity to replace his current manual diff-against-spec pass, because the
docs only describe the skill in behavioral terms ("finds what testing misses") without showing a
sample artifact with actual P1 findings. For a skeptical engineer evaluating a new tool, promised
behavior without inspectable output is not a credible signal.

Flags: [BLOCKER — Primary, Would-Adopt = 2]

---

[C-03] Elena Volkov (Compliance Officer, regulated financial services customer) | Tier: SECONDARY

- Usefulness [1-5]: 4
- Clarity [1-5]: 3
- Would-Adopt [1-5]: 3

Rationale: Elena needs audit trails and documented decision rationale. Signal's append-only dated
artifact model (`{topic}-{signal}-{date}.md`, never overwritten) is structurally aligned with audit
trail requirements — every decision has a timestamped evidence artifact, and the full `simulations/`
directory becomes a machine-readable decision log. The `/scout-compliance` skill and the fact that
the corp namespace produces structured committee minutes via `/corp-committee` are directly useful.
The clarity gap: the docs never name "audit trail" or "compliance documentation" as outputs, and
the frontmatter format is described in terms of skill routing, not evidentiary record-keeping. The
specific mechanism blocking higher would-adopt is that Elena needs to understand whether Signal
artifacts are admissible evidence in a regulated review — and the docs make no statement about
artifact integrity, immutability guarantees, or chain-of-custody. "Append-only" is mentioned in
PRINCIPLES.md (referenced but not read), not in QUICKSTART. She cannot find the answer to her
primary question without navigating beyond the docs she was given.

---

[C-04] Kevin O'Brien (ISV Partner, Power Platform, 3-person team) | Tier: PRIMARY

- Usefulness [1-5]: 4
- Clarity [1-5]: 5
- Would-Adopt [1-5]: 4

Rationale: Kevin ships fast and has no tolerance for heavyweight process. The QUICKSTART's "Zero
setup" section — "The first run of any skill produces a useful result with no prior configuration.
No config file required." — directly addresses his cost model. The "Common starting points" table
with single-line entry points for each situation (feature idea → `/scout-competitors`; shipped,
adoption flat → `/listen-adoption`) is the most persuasive section of the docs for this persona
because it shows that Signal can be entered at any point in the workflow, not just as an
upfront investment. The specific clarity mechanism that earns a 5: the docs consistently use a
concrete example (payment-reminders) throughout QUICKSTART and the scout guide, which means Kevin
reads a feature investigation rather than a feature description. He learns Signal by watching it
work on a real case, not by reading an abstract framework. One mild would-adopt friction: the
artifact directory model (`simulations/scout/competitors/`) implies a repo structure he may not
have if he is building in a Power Apps environment rather than a code repo.

Flags: [DELIGHT: Clarity — concrete worked example sustained across docs teaches Signal by
demonstration, not description]

---

[C-05] Aisha Patel (TPM, QBRs and shiprooms, Dynamics features) | Tier: PRIMARY

- Usefulness [1-5]: 5
- Clarity [1-5]: 3
- Would-Adopt [1-5]: 4

Rationale: Aisha lives in structured evidence for go/no-go decisions. The corp namespace —
specifically `/corp-rob --stage all` and `/corp-committee` — is the highest-value feature in the
entire docs for her workflow. The QUICKSTART's `/topic-status` output showing coverage percentage
and readiness for target outcome (design commit, ship, post-ship) is exactly the dashboard artifact
she assembles manually before each shiproom. The Inertia Advocate role in every team is a
formalization of the "who is going to argue against this?" question she asks in every review. The
clarity gap: the QUICKSTART introduces corp in one paragraph late in the doc, with `/corp-pr` and
`/corp-rob` mentioned briefly. The corps guide gives depth, but the connection between the
topic-status coverage view and the ROB stages — that a topic at 7/9 namespace coverage translates
to a specific ROB stage recommendation — is never made explicit. The mechanism: Aisha needs to
know what signal density maps to "ready for shiproom," and the docs describe coverage thresholds
(Pre-Commitment Ready = 7 namespaces) without connecting them to the governance calendar she runs.

Flags: [DELIGHT: Usefulness — topic-status coverage dashboard directly replaces manual pre-shiproom
evidence assembly]

---

[C-06] David Chen (Enterprise Architect, Fortune 500 manufacturing, Dynamics 365) | Tier: SECONDARY

- Usefulness [1-5]: 4
- Clarity [1-5]: 3
- Would-Adopt [1-5]: 2

Rationale: David gate-keeps every Dynamics customization for technical debt risk. The `trace`
namespace (contract, state, permissions, deployment, migration) and the corp Arch Board stage in
`/corp-rob` map directly onto his review function. The QUICKSTART's description of `/trace-contract`
— "Does the implementation match the spec?" — is the exact question he asks in every architecture
review gate. The clarity score is suppressed because the docs use Signal's own vocabulary
(namespace, skill, topic, signal artifact) without establishing a bridge to the vocabulary David
uses in his architecture practice (ADR, impact assessment, change control). The specific would-adopt
blocker: the `/corp-scan` prerequisite for org configuration requires repo access and produces a
draft `org.yaml` from directory structure. David's org is not structured as a code directory — it
is structured as a Dynamics 365 solution topology, and the docs give no signal on whether corp-scan
can work against that model. The mechanism: corp-scan's "directory, concept, service, domain" pivot
modes are listed but not elaborated; David cannot tell if "domain" mode covers a Dynamics solution
domain or is scoped to software package domains.

---

[C-07] Sarah Martinez (UX Researcher, adoption patterns, Dynamics features) | Tier: SECONDARY

- Usefulness [1-5]: 5
- Clarity [1-5]: 4
- Would-Adopt [1-5]: 4

Rationale: Sarah studies why features fail adoption and knows that switching costs dominate. She
will recognize the inertia rule immediately — it is the research finding she quotes in every
feature post-mortem. The `listen` namespace (`/listen-adoption`, `/listen-support`, `/listen-feedback`)
and the ACHIEVEMENTS.md "Deep Listen" milestone are the highest-value elements for her. The
specific mechanism driving the usefulness 5: `listen-adoption` is described as "simulate adoption
before ship" and explicitly frames the problem as predicting the support tickets and adoption curve
before rollout begins — which is the pre-ship research instrumentation she argues for in every
feature cycle and rarely gets funded for. The QUICKSTART's "The primary competitor is always
inertia" directly echoes her research findings. Clarity is 4 rather than 5 because the docs do
not specify what research methodology or evidence type underpins the listen skills — she will want
to know whether `/listen-adoption` produces a persona-based adoption model, a market diffusion
curve, or something else before trusting its outputs.

Flags: [DELIGHT: Usefulness — listen namespace formalization of adoption simulation matches her
research practice pre-ship]

---

[C-08] Raj Patel (Head of Sales Engineering, Microsoft SI partner) | Tier: SECONDARY

- Usefulness [1-5]: 3
- Clarity [1-5]: 4
- Would-Adopt [1-5]: 2

Rationale: Raj demos Dynamics daily and hears "we do it this way in our current system" constantly.
The inertia framing resonates personally — he fights inertia in every sales cycle — but Signal is a
pre-build tool, not a sales tool, and Raj's workflow is post-build. He can see the value of
`/scout-positioning` for competitive messaging and `/scout-competitors` for inertia articulation in
demos, but those use cases require adapting Signal from its intended developer-facing evidence
function into a sales enablement function the docs do not address. The would-adopt blocker: Signal's
artifact model is designed for contributors writing to a `simulations/` directory in a shared repo.
Raj works across customer environments and does not have a persistent repo workspace to accumulate
evidence. The mechanism: Signal's append-only file system artifact contract (`{topic}-{signal}-{date}.md`
in `simulations/`) assumes a single codebase home for signal accumulation. Raj's investigations are
ephemeral per-customer, with no persistent artifact store — the signal accumulation model breaks
in his workflow.

---

[C-09] Lena Fischer (VP Engineering, mid-size European Dynamics customer) | Tier: PRIMARY

- Usefulness [1-5]: 4
- Clarity [1-5]: 3
- Would-Adopt [1-5]: 3

Rationale: Lena has 10 engineers, a constrained budget, strict GDPR requirements, and needs ROI
justification for every feature. The ACHIEVEMENTS system in Signal is the most persuasive element
for her: "Full Pre-Commit Chain" and "Pre-Commitment Ready" provide documented evidence that a
team investigated before committing, which is the investment-justification artifact she needs for
every non-trivial feature. The `/scout-compliance` skill and the compliance officer persona in
the corp virtual org also address her GDPR gate directly. However, the clarity gap is significant:
the docs are written for an audience with a shared codebase. Lena's team customizes Dynamics 365
using Power Apps, Power Automate, and D365 customizations — low-code/no-code surfaces that do not
produce a `simulations/` directory naturally. The specific mechanism suppressing would-adopt: the
docs describe Signal as operating against a repo with files the skills can read ("Scans your repo
for stack signals"), and Lena has no repo with stack signals for a Power Apps customization. She
cannot tell whether Signal works for her environment or only for code-first development teams.

---

[C-10] Tom Nguyen (Developer Advocate, Power Platform, citizen developers) | Tier: SECONDARY

- Usefulness [1-5]: 3
- Clarity [1-5]: 2
- Would-Adopt [1-5]: 2

Rationale: Tom teaches Power Platform to citizen developers — business users who build apps with
no engineering background. Signal's vocabulary is a hard barrier for this persona. The docs use
terms — namespace, frontmatter, skill version, artifact, trace-contract, flow-lifecycle — that
assume a developer mental model. The clarity score of 2 is not a writing quality judgment; the
writing is clear within its target audience. The mechanism is the target audience assumption itself:
the QUICKSTART's "Common starting points" table starts from developer situations (feature idea,
spec written, implementation done) that map to engineering workflows, not citizen developer ones.
Tom's audience builds a Canvas App to solve a business problem; they do not "write a spec" or
"trace a contract." The would-adopt blocker: Signal's entry points and vocabulary are uniformly
scoped to software engineering workflows, and there is no "citizen developer" or "business builder"
framing anywhere in the docs. The `/topic-new` command returns artifacts to a `simulations/`
markdown directory — a surface that does not exist in a citizen developer's Power Apps environment.
Tom cannot recommend Signal to his audience because the docs do not address them, and he cannot
easily adapt it without building the bridge himself.

---

[C-11] Fatima Al-Rashid (Director of Product Management, public sector, Microsoft customer) | Tier: PRIMARY

- Usefulness [1-5]: 5
- Clarity [1-5]: 4
- Would-Adopt [1-5]: 4

Rationale: Fatima operates under procurement rules where every feature decision needs documented
evidence and formal approvals. Signal's artifact model is structurally aligned with procurement
documentation requirements: every skill produces a dated, frontmattered evidence artifact with
a named skill, topic, and version. The corps guide's `/corp-rob --stage all` producing artifacts
for leadership, PM, TPM, Arch Board, and Exec Office stages maps directly onto the approval chain
she navigates. The ACHIEVEMENTS system — particularly "Full Pre-Commit Chain" — produces
documented evidence of a compliant investigation process that she can attach to a procurement
approval request. The specific mechanism driving the usefulness 5: Signal's append-only artifact
model means every decision in the investigation is timestamped and non-destructive, which satisfies
the evidentiary requirements of public sector procurement audit. The clarity friction: the docs do
not mention procurement or approval workflows as a target use case, so Fatima has to do the
translation herself — the connection is inferrable but not named.

Flags: [DELIGHT: Usefulness — append-only timestamped artifact model satisfies public sector
audit trail requirements without additional tooling]

---

[C-12] Chris Park (Startup founder, Dynamics 365 / Power Platform, Series A, 5-person team) | Tier: PRIMARY

- Usefulness [1-5]: 4
- Clarity [1-5]: 5
- Would-Adopt [1-5]: 4

Rationale: Chris will adopt Signal if and only if it saves time. The QUICKSTART's five-step
minimal workflow and "Zero setup" section are the two most important sections for him. The
specific mechanism driving the clarity 5: Signal's docs are structured around "start where the
pain is" — you do not have to run all nine namespaces; you run the one that answers the question
blocking you right now. The QUICKSTART's entry point table gives Chris a single command for each
situation (adoption flat → `/listen-adoption`; assumption to test → `/prove-hypothesis`), which
maps onto how a startup operates: respond to the current blocker, not a methodology. The 4 on
would-adopt (not a 5) comes from one friction: the ACHIEVEMENTS system, while clearly optional,
implies a practice that grows over time (coverage milestones, chain achievements, team
achievements). A founder at Series A is not building a practice — they are solving the problem
in front of them. The docs do not clearly distinguish "one-off use to answer a specific question"
from "ongoing practice building." Chris needs Signal presented as a tool, not a methodology, and
the ACHIEVEMENTS framing slightly muddies that line.

Flags: [DELIGHT: Clarity — "start where the pain is" entry-point structure removes onboarding
friction for fast-moving teams]

---

## SCORING TABLE

All 12 personas scored in prose above. Summary:

| ID   | Name              | Role                     | Tier       | Useful | Clarity | W-Adopt | Flags         |
|------|-------------------|--------------------------|------------|--------|---------|---------|---------------|
| C-01 | Priya Sharma      | Senior PM                | Primary    | 5      | 4       | 4       | DELIGHT:Use   |
| C-02 | Marcus Johnson    | Principal Engineer       | Primary    | 3      | 4       | 2       | BLOCKER       |
| C-03 | Elena Volkov      | Compliance Officer       | Secondary  | 4      | 3       | 3       |               |
| C-04 | Kevin O'Brien     | ISV Partner              | Primary    | 4      | 5       | 4       | DELIGHT:Clar  |
| C-05 | Aisha Patel       | TPM / QBR Lead           | Primary    | 5      | 3       | 4       | DELIGHT:Use   |
| C-06 | David Chen        | Enterprise Architect     | Secondary  | 4      | 3       | 2       |               |
| C-07 | Sarah Martinez    | UX Researcher            | Secondary  | 5      | 4       | 4       | DELIGHT:Use   |
| C-08 | Raj Patel         | Sales Engineering Head   | Secondary  | 3      | 4       | 2       |               |
| C-09 | Lena Fischer      | VP Engineering           | Primary    | 4      | 3       | 3       |               |
| C-10 | Tom Nguyen        | Developer Advocate       | Non-target | 3      | 2       | 2       |               |
| C-11 | Fatima Al-Rashid  | Dir. Product Management  | Primary    | 5      | 4       | 4       | DELIGHT:Use   |
| C-12 | Chris Park        | Startup Founder          | Primary    | 4      | 5       | 4       | DELIGHT:Clar  |

---

## IS ADOPTION BLOCKED?

Two primary personas scored Would-Adopt < 3: Marcus Johnson (C-02, Would-Adopt = 2).

**C-02 Marcus Johnson — Blocker Chain**

First, the stakes: Marcus reviews 50+ PRs per sprint and bears personal accountability for
regressions that slip through. His adoption gate for any new tool is a simple cost-benefit: does
this reduce the probability of shipping a regression more than the process overhead costs? He is
not opposed to tooling — he is opposed to tooling that produces overhead without a demonstrated
reduction in defect rate.

Then, the feature-level gap: the Signal docs describe what skills do ("trace-contract finds the
gap between spec and implementation") but do not show what a trace-contract artifact looks like
for a real implementation. Marcus cannot evaluate whether the findings would be specific enough
to act on, or whether they would be the kind of generic structural observations that he already
produces faster by reading the diff himself.

Then, the sub-feature mechanism: the QUICKSTART's "Common starting points" table maps his
situation ("Implementation done, want to verify it matches spec") to `/trace-contract`, but the
trace namespace has no example artifact in any of the docs reviewed. The artifact format section
shows only frontmatter YAML — `skill: scout-competitors, topic: payment-reminders, date:
2026-03-16` — not a sample trace-contract output with findings at P1/P2/P3 severity. The amendment
target is the absence of a trace-contract sample output in the docs: Marcus cannot make a
would-adopt decision without seeing what a finding looks like at the level of specificity he
requires. Adding one representative trace-contract artifact — with two P1 findings, mechanism
named, spec section cited — would move his Would-Adopt from 2 to 3-4.

**C-09 Lena Fischer — Would-Adopt = 3 (not a hard blocker, but flagged)**

Lena's 3 reflects genuine uncertainty rather than resistance. The blocker mechanism — docs assume
a code repo, Lena's environment is low-code Power Apps — suppresses adoption confidence without
being a hard no. If the docs addressed low-code/no-code environments explicitly, her would-adopt
would move to 4.

---

## IS THE POSITIONING LEAKING?

Three positioning leaks identified.

**Leak 1 — C-03 Elena Volkov (Compliance Officer, Secondary → reads as a compliance tool)**

Elena's usefulness score of 4 is driven by Signal's append-only artifact model and the
`/scout-compliance` skill. She is reading Signal as an audit trail and compliance documentation
system, not as a pre-build evidence tool for feature development teams. The framing element
causing this: the dated artifact contract (`{topic}-{signal}-{date}.md`, never overwritten) is
described in PRINCIPLES.md as an append-only design principle — but the QUICKSTART does not
frame it as a design principle. It presents it as a practical convenience ("Two people running
the same skill on the same topic produce two files — different signals, no collision"). A compliance
officer reads the same property as evidentiary immutability, which is a different and stronger
value claim. Signal could clarify that compliance audit-trail use is a secondary benefit, not a
primary design goal, to prevent this leak becoming a support burden when Elena expects
compliance certification.

**Leak 2 — C-07 Sarah Martinez (UX Researcher, Secondary → reads as a research instrumentation tool)**

Sarah's usefulness 5 and Would-Adopt 4 are driven by her mapping Signal's listen namespace onto
her UX research practice. She is reading `/listen-adoption` as a pre-ship user research substitute,
not as a signal evidence artifact in a developer workflow. The specific framing element: "simulate
adoption before ship" and "you have simulated your users before they arrived" (ACHIEVEMENTS.md)
are research-methodology descriptions, not developer-tool descriptions. Signal is framing the
listen namespace in research vocabulary, which naturally attracts researchers. If Signal is not
positioned as a UX research tool, the docs should distinguish between "evidence artifact for
developer decision-making" and "user research simulation" more clearly.

**Leak 3 — C-08 Raj Patel (Sales Engineer, Secondary → reads as a competitive intelligence tool)**

Raj's usefulness 3 is lower than his initial read of the tool would suggest. His first reaction
to "inertia is always the primary competitor" is that this is a competitive intelligence framing
he can use in sales conversations. The scout namespace description — "5-8 named competitors with
threat scoring" — reads as competitive intelligence output, not pre-build feature evidence.
The positioning element causing this: Signal uses competitive analysis vocabulary (threat scoring,
market positioning, TAM/SAM/SOM) in a developer-tool context, which attracts sales and BD
personas who read the same vocabulary as sales intelligence. Signal is not a sales tool; the
framing should clarify that competitive analysis here serves the inertia case for build decisions,
not sales enablement.

---

## WHO IS DELIGHTED?

**Usefulness 5 — Priya Sharma (C-01), Aisha Patel (C-05), Sarah Martinez (C-07), Fatima Al-Rashid (C-11)**

Common sub-feature property: Signal's named-output, structured-artifact model produces
decision-ready evidence artifacts with a single command, replacing multi-hour manual synthesis
work. For all four personas, the specific delight mechanism is not "Signal produces evidence" —
it is that Signal produces evidence in a format directly usable in their downstream workflow
(stakeholder justification decks for Priya, shiproom dashboards for Aisha, pre-ship research
artifacts for Sarah, procurement approval packages for Fatima). The amplification opportunity:
onboarding messaging should lead with "your first `/scout-competitors` run produces a stakeholder-ready
inertia case in 10 minutes" — making the output-to-workflow connection explicit rather than
inferrable.

**Clarity 5 — Kevin O'Brien (C-04), Chris Park (C-12)**

Common sub-feature property: the concrete worked example (payment-reminders) sustained across
QUICKSTART and scout guide, combined with the "start where the pain is" entry-point table. Both
personas are fast-moving, low-tolerance for abstraction, and both were convinced by documentation
that demonstrated Signal working rather than described it. The amplification opportunity: lead
the docs with the entry-point table (currently mid-QUICKSTART) — make the first thing a new
reader sees the answer to "where do I start given my situation right now?"

---

## WHAT DO THE NUMBERS SAY IN AGGREGATE?

**Tier assignments and weights:**
- Primary (6 personas, 3x weight): C-01, C-02, C-04, C-05, C-09, C-11, C-12
  Note: C-12 brings the Primary count to 7 — all seven BIC-adjacent decision-makers and builders.
  Revised: Primary = C-01, C-02, C-04, C-05, C-09, C-11, C-12 (7 personas, 3x weight)
- Secondary (4 personas, 2x weight): C-03, C-06, C-07, C-08
- Non-target (1 persona, 1x weight): C-10

**Weighted score computation:**

Primary scores (weight 3):
| Persona | Useful | Clarity | W-Adopt |
|---------|--------|---------|---------|
| C-01    | 5      | 4       | 4       |
| C-02    | 3      | 4       | 2       |
| C-04    | 4      | 5       | 4       |
| C-05    | 5      | 3       | 4       |
| C-09    | 4      | 3       | 3       |
| C-11    | 5      | 4       | 4       |
| C-12    | 4      | 5       | 4       |
| Avg     | 4.29   | 4.00    | 3.57    |
| x3 =    | 12.86  | 12.00   | 10.71   |

Secondary scores (weight 2):
| Persona | Useful | Clarity | W-Adopt |
|---------|--------|---------|---------|
| C-03    | 4      | 3       | 3       |
| C-06    | 4      | 3       | 2       |
| C-07    | 5      | 4       | 4       |
| C-08    | 3      | 4       | 2       |
| Avg     | 4.00   | 3.50    | 2.75    |
| x2 =    | 8.00   | 7.00    | 5.50    |

Non-target scores (weight 1):
| Persona | Useful | Clarity | W-Adopt |
|---------|--------|---------|---------|
| C-10    | 3      | 2       | 2       |
| x1 =    | 3.00   | 2.00    | 2.00    |

Total weight units: (7 x 3) + (4 x 2) + (1 x 1) = 21 + 8 + 1 = 30

Weighted dimension averages:
- Usefulness:   (12.86 + 8.00 + 3.00) / 10 = 23.86 / 10 — rescaled: (21 x 4.29 + 8 x 4.00 + 1 x 3.00) / 30 = (90.09 + 32.00 + 3.00) / 30 = 125.09 / 30 = **4.17**
- Clarity:      (21 x 4.00 + 8 x 3.50 + 1 x 2.00) / 30 = (84.00 + 28.00 + 2.00) / 30 = 114.00 / 30 = **3.80**
- Would-Adopt:  (21 x 3.57 + 8 x 2.75 + 1 x 2.00) / 30 = (74.97 + 22.00 + 2.00) / 30 = 98.97 / 30 = **3.30**

**Overall composite** (average of three weighted dimensions): (4.17 + 3.80 + 3.30) / 3 = **3.76 / 5**

**NPS approximation (Would-Adopt mapped to NPS scale):**
Promoters (W-Adopt 4-5): C-01, C-04, C-05, C-07, C-11, C-12 = 6 personas
Passive (W-Adopt 3): C-03, C-09 = 2 personas
Detractors (W-Adopt 1-2): C-02, C-06, C-08, C-10 = 4 personas

Raw NPS: (6 - 4) / 12 = +17 (unweighted)
Weighted NPS (primary 3x): Promoters weighted = C-01(3) + C-04(3) + C-05(3) + C-07(2) + C-11(3) + C-12(3) = 17; Detractors weighted = C-02(3) + C-06(2) + C-08(2) + C-10(1) = 8; Total weight = 30; Weighted NPS = (17 - 8) / 30 x 100 = **+30**

**Cross-persona pattern at sub-feature resolution:**

The primary pattern is not "clarity is lower than usefulness" (a distribution observation). The
pattern with sub-feature cause: the five personas who score Clarity 3 or lower (C-05, C-06, C-09,
C-10, C-03) share a common cause — Signal's docs describe skills in terms of what they do
conceptually ("trace-contract finds the gap between spec and implementation") but do not show
a sample artifact output with findings at the specificity level the persona requires to make an
adoption decision. The QUICKSTART's artifact section shows only YAML frontmatter as a concrete
example; the body of an artifact is never shown. Personas who need to evaluate output quality
before adopting — the engineer (C-02), the architect (C-06), the compliance officer (C-03), the
VP of engineering (C-09), the developer advocate (C-10) — are all suppressed by the same
sub-feature gap: the absence of a representative artifact body in the docs. The amendment target
is the artifact example section in QUICKSTART: expand it from frontmatter-only to include
2-3 lines of actual skill output (one finding, one severity rating, one recommendation) so that
evaluators can assess output quality before running the first skill.

---

## WHAT SHOULD CHANGE?

**Amendment 1 — Add a representative artifact body to the QUICKSTART artifact section (addresses C-02 blocker, lifts C-06, C-03, C-09)**

Current state: the QUICKSTART artifact section shows only YAML frontmatter as the concrete example
of what a skill produces. The body of a skill output is never shown.

The blocker chain for C-02 (Marcus Johnson) named the sub-feature mechanism: the absence of a
sample trace-contract artifact with P1/P2/P3 findings means a skeptical engineer cannot evaluate
whether Signal's trace output is specific enough to replace his manual diff-against-spec pass.

Amendment target: the artifact example block in QUICKSTART (currently lines 137-144, showing
only the frontmatter). Expand it to include 4-6 lines of representative artifact body for one
skill — for example, a scout-competitors fragment showing the inertia case with threat rating,
or a trace-contract fragment showing one P1 finding with spec section cited and mechanism named.

Projected score movement: fixing the artifact-body gap for C-02 likely lifts primary Would-Adopt
by ~1.5 points (2 → 3-4), moving the weighted Would-Adopt composite from 3.30 to approximately
3.40. The same fix also addresses C-06 (enterprise architect, would-adopt 2) and C-09 (VP eng,
would-adopt 3), moving the secondary would-adopt average from 2.75 toward 3.25.

**Amendment 2 — Add a one-paragraph "works without a code repo" callout in the Zero Setup section (addresses C-09 and C-04 friction, unlocks low-code audience)**

Current state: the Zero Setup section says "No config file required" but makes no statement about
whether Signal requires a code repository. Several skills are described as scanning "your repo"
for stack signals (scout-feasibility: "Scans your repo for stack signals"), which implies
code-repo dependency.

The mechanism suppressing Lena Fischer (C-09) and creating ambiguity for Kevin O'Brien (C-04):
the docs never state whether Signal works for teams building on Power Platform, Power Apps, or
Dynamics customizations without a traditional code repository. The ambiguity is a would-adopt
suppressor for the Power Platform audience — which is a large segment of the BIC customer base.

Amendment target: the Zero Setup section. Add a callout: "No repo required for most skills. Skills
that scan for stack signals (scout-feasibility, trace-contract) work best with a codebase, but
every other skill in every other namespace runs standalone against any topic description you provide."

Projected score movement: fixing this gap for C-09 (Lena Fischer) likely lifts Would-Adopt from
3 to 4, moving the weighted composite from 3.30 to approximately 3.34.

**Amendment 3 — Clarify ACHIEVEMENTS as optional practice, not required methodology (addresses C-12 friction, reduces methodology-overhead perception)**

Current state: ACHIEVEMENTS.md presents a milestone and gamification system with coverage thresholds,
chain requirements, and team achievements. The doc is excellent for teams building a practice but
creates an implicit methodology overhead signal for fast-moving founders and small ISV teams who
read "Full Coverage — Cover all 9 namespaces on a single topic" and worry they are expected to
run 47 skills before committing.

The sub-feature framing element causing the friction for C-12 (Chris Park): ACHIEVEMENTS.md leads
with "Achievements are not grinding" and immediately describes milestones across five categories,
including team achievements requiring multiple contributors. A Series A founder reads this as a
practice ramp, not an optional menu.

Amendment target: the ACHIEVEMENTS.md introduction. Add one sentence after "The unearned
achievements are the curriculum": "You can use Signal for a single skill on a single topic and
stop. The achievements describe what more looks like — not what is required." This disambiguation
costs nothing and removes the methodology-overhead read that suppresses would-adopt for fast-movers.

Projected score movement: fixing this framing for C-12 likely lifts Would-Adopt from 4 to 5
(removing the one friction point he named). This moves the primary would-adopt average from 3.57
to approximately 3.71, and the weighted composite from 3.30 to approximately 3.39.

---

## SUMMARY

**Weighted aggregate NPS (primary audience): +30**
**Overall composite (1-5): 3.76**
**Primary audience composite: 3.76**

**Adoption blockers ranked by frequency:**
1. Absence of sample artifact body in docs — affects C-02 (hard blocker), C-06, C-09, C-03 (4 personas, 1 primary)
2. Low-code / no-code environment ambiguity — affects C-09, C-04, C-10 (3 personas)
3. Methodology-overhead perception from ACHIEVEMENTS — affects C-12, C-04 (2 primary personas)

**Top 3 positioning leaks:**
1. C-03 Elena Volkov — reads Signal as an audit trail / compliance documentation system (driven by append-only artifact framing)
2. C-07 Sarah Martinez — reads Signal as a UX research instrumentation tool (driven by research vocabulary in listen namespace)
3. C-08 Raj Patel — reads Signal as a competitive intelligence tool for sales (driven by threat-scoring vocabulary in scout namespace)

**Delight signals (personas with score 5):**
- Usefulness 5: C-01, C-05, C-07, C-11 — driven by structured artifact model producing decision-ready outputs for their specific downstream workflows
- Clarity 5: C-04, C-12 — driven by concrete worked example and "start where the pain is" entry-point structure

**The three amendments in priority order:**
1. Add representative artifact body to QUICKSTART (highest would-adopt lift, removes primary blocker)
2. Add "works without a code repo" callout in Zero Setup (unlocks Power Platform audience)
3. Clarify ACHIEVEMENTS as optional menu, not required methodology (removes methodology-overhead perception for fast-movers)
