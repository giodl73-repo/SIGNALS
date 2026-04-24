---
skill: scout-competitors
topic: plugin
item: competitors
date: 2026-03-15
skill_version: golden-2026-03-14
input: auto-detected from CLAUDE.md, plugin-plan.md
rounds: 2
---

# Competitive Brief: Signal — Developer Evidence Gathering Before Feature Commitment

> Strategy first. Matrix is supporting evidence.

---

## 1. The Primary Competitor: Inertia

**Threat: HIGH**

The team does nothing. They open a Jira ticket, write three lines of acceptance criteria, and start coding. This is not ignorance — it is the rational default. Investigation feels like delay. The backlog is already behind. The PM has already promised Q2. Asking "have we gathered evidence?" is asking the team to pause while the sprint clock runs.

What makes inertia sticky:

- **No shared vocabulary for pre-build evidence.** Teams don't have a word for "the things we should know before we commit." Without a word, there's no checklist, no definition of done, no moment where someone can say "we haven't done this yet."
- **Retrospective cost is invisible upfront.** The cost of committing to the wrong feature architecture appears six months later as a rewrite, not on the day the Jira ticket was created.
- **The artifact doesn't exist until it's produced.** There's no empty slot in the PR that says "evidence missing here." The absence of investigation leaves no footprint.
- **Tooling default is "build."** Copilot, Cursor, Claude Code — every AI tool in the developer environment accelerates toward implementation. Nothing in the environment pulls toward investigation first.

What would make a team choose to keep doing nothing: they shipped three features without it and they were fine. The fourth feature — the one that required a rewrite — may have been fine anyway. The counterfactual is invisible.

**Signal's answer to inertia:** Zero-barrier entry (copy one SKILL.md file, no config required), developer-native vocabulary (namespaces map to roles already on the team), and artifacts that land in the repo so absence of evidence is visible in the same place where code lives.

---

## 2. The Whitespace

**No tool currently occupies: structured, artifact-producing, multi-dimension evidence gathering for developers before feature commitment.**

The space around Signal is occupied by tools that do adjacent, not competing, work:

- **PM tools** (Productboard, Dovetail, Aha!) gather *customer* signals before *roadmap* decisions. Signal gathers *technical and architectural* signals before *build* decisions. Different evidence type, different audience, different moment in the chain.
- **ADR tools** (adr-tools, Log4Brains) *capture* a decision already made. Signal *investigates before* a decision is made. ADRs are the output of a process Signal enables.
- **AI coding workspaces** (Copilot Workspace, Cursor) *assume the decision to build is made* and accelerate from spec to code. Signal operates upstream of that assumption.
- **Pre-mortem practice** exists as a facilitation technique and whitepaper category. No product operationalizes it as an artifact-producing developer workflow. The entire adversarial pre-feature investigation category is unoccupied as software.

The whitespace Signal owns: **pre-decision, developer-facing, multi-namespace evidence gathering that produces named artifacts living in the repo alongside the code they informed.**

---

## 3. The Table Stakes

Any entrant into this space must have to be taken seriously:

| Must-Have | Why |
|-----------|-----|
| **Developer-native entry point** | If it requires a PM, a Notion doc, or a browser tab, developers won't use it. Must live in the coding environment. |
| **Artifact output that lands in the repo** | Evidence that lives in Confluence or Notion is invisible to the developer's workflow. If it is not in git, it does not count. |
| **Role/persona model** | Single-perspective analysis produces single-perspective blind spots. Any credible evidence tool must simulate multiple reviewers, critics, or domain experts. |
| **Topic continuity** | Evidence from different angles (technical, market, user) must be linkable to a single decision. A naming convention or registry that ties artifacts across namespaces is required. |
| **AI-native execution** | Manual research workflows will not compete. Value comes from AI running the investigation at speed, not templates for humans to fill in. |

Signal has all five. Most adjacent tools have one or two.

---

## 4. The Competitive Matrix

| Competitor | Feature Overlap | Positioning | Technical Moat | Distribution | Threat |
|-----------|-----------------|-------------|----------------|--------------|--------|
| **Inertia / status quo** | n/a | Primary -- does nothing | Zero switching cost | Pre-installed on every team | HIGH |
| **GitHub Copilot Workspace** | MEDIUM (draft, trace) | Adjacent -- assumes build decision made; accelerates spec-to-code | GitHub + Microsoft distribution, IDE integration | Every GitHub user | HIGH (future) |
| **Linear Product Intelligence** | LOW-MEDIUM (program namespace) | Adjacent -- manages in-flight work, triage, planning | Deep issue-tracker integration, developer habit | 25k+ paying teams | MEDIUM (future) |
| **Productboard / Dovetail** | LOW (listen namespace) | Complementary -- PM-side customer signals | Research repository + integrations | Enterprise PM teams | LOW |
| **adr-tools / Log4Brains** | LOW (draft:proposal) | Complementary -- post-decision ADR capture | Git-native, open source | Developer community | LOW |
| **claude-code-workflows / Superpowers** | MEDIUM (program, review namespaces) | Adjacent -- lifecycle structure for Claude Code | Claude Code ecosystem, skill framework | Claude Code users | LOW-MEDIUM |
| **Aha! / Jeda.ai** | LOW (scout namespace) | Adjacent -- PM roadmap prioritization | Existing PM toolchain integrations | PM/product teams | LOW |
| **LaunchDarkly** | NONE | Complementary -- post-build release decisions | Feature flag infra, experimentation platform | Engineering orgs | NONE |
| **MITRE Premortem / Explorer Labs** | LOW (scout:feasibility, prove) | Adjacent -- facilitation technique | None (whitepapers + canvases) | Consultants, innovation teams | LOW |

**Source verification:**
- Copilot Workspace brainstorm-to-spec pipeline: https://githubnext.com/projects/copilot-workspace
- Linear deep-links to AI coding tools from issues (2026-02-26 changelog): https://linear.app/changelog/2026-02-26-deeplink-to-ai-coding-tools
- adr-tools canonical open-source ADR: https://github.com/npryce/adr-tools
- Claude Code plugin ecosystem scan: https://www.turbodocx.com/blog/best-claude-code-skills-plugins-mcp-servers
- Productboard AI discovery: https://www.productboard.com/blog/how-to-do-product-discovery-with-ai/

---

## 5. --mode risk: The Cost of Building the Wrong Thing

*For exec audiences who respond to risk quantification over feature comparison.*

The question is not "which tool has the best feature set." The question is: **what does a team lose by not investigating before they commit?**

**Direct costs:**

- A feature built to the wrong architectural pattern costs 3-6x in rework versus discovering the pattern mismatch before the first commit. (McConnell, *Code Complete*; NIST software defect discovery cost curves)
- A feature shipped with an unvalidated assumption about user behavior fails adoption. The cost is not the build -- it is the opportunity cost of sprint capacity that could have been directed elsewhere.
- A feature that violates a compliance boundary discovered post-build requires legal review, delayed release, and potential redesign. Pre-build compliance investigation via `/scout:compliance` costs hours; post-build discovery costs weeks.

**The quantification story:**

A team that ships five features per quarter without Signal invests 100% of build capacity. A team that invests 10% of capacity in Signal-style pre-build evidence gathering before each feature expects to avoid one full-feature rework per year. At median engineering cost of $200K/engineer/year and 2-engineer features: one avoided rework = $80K. Signal's cost = one SKILL.md file and one session per feature.

**The exec reframe:** This is not a tooling decision. It is a risk management decision. The question is whether the team prices in investigation cost before the feature or rework cost after.

---

## 6. Amendments

**Amend 1: Narrow to Claude Code ecosystem only**
- User changes: scope competitive scan to Claude Code plugins and AI coding tools only
- Output changes: matrix shrinks to 5 rows; Copilot Workspace becomes the clear #1 named threat; whitespace analysis focuses on "what no Claude Code plugin does" rather than what no tool category does

**Amend 2: Add enterprise procurement lens**
- User changes: specify that target customers are enterprise engineering teams with procurement processes
- Output changes: distribution column becomes critical (Copilot Workspace wins via existing GitHub enterprise contracts; Signal needs an enterprise install story); table stakes expands with "SOC 2 / security review" as a blocker; inertia section adds "approved vendor list" as a stickiness factor

**Amend 3: Focus on the PM-to-dev handoff gap**
- User changes: scope the brief to the gap between PM discovery tools (Productboard, Dovetail) and developer implementation tools (Copilot Workspace, Cursor)
- Output changes: brief reframes Signal as "the missing middle layer" between PM evidence gathering and developer execution; whitespace becomes "technical due diligence layer between product decision and implementation sprint"; Dovetail moves from low-threat to close architectural relative
