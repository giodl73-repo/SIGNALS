# /signal:review -- Signal Plugin Customer Evaluation
**Topic**: plugin
**Date**: 2026-03-14
**Target**: Signal plugin -- 9 namespaces, 47 skills, skills-in-repo, topic narrative model
**Personas**: C-01 through C-12
**Skill invocation model**: /signal:{namespace} installed as .claude/skills/ per repo

---

## Setup

### Audience Tier Assignments

| Persona | Role / Industry | Tier | Weight |
|---------|----------------|------|--------|
| C-02 James Okafor | Developer / SaaS | Primary | 3x |
| C-03 Priya Sharma | Architect / Finance | Primary | 3x |
| C-09 Lisa Johansson | SRE / Telecom | Primary | 3x |
| C-10 Marcus Rivera | Data Scientist / Education | Primary | 3x |
| C-04 David Kim | PM / Healthcare | Secondary | 2x |
| C-05 Elena Vasquez | Compliance / Insurance | Secondary | 2x |
| C-08 Ahmad Al-Rashid | Partner / Energy | Secondary | 2x |
| C-11 Tomoko Watanabe | Team Lead / Manufacturing | Secondary | 2x |
| C-01 Maria Chen | Maker / Retail | Non-target | 1x |
| C-06 Robert Tanaka | Auditor / Government | Non-target | 1x |
| C-07 Catherine Moore | Executive / Consulting | Non-target | 1x |
| C-12 Frank Hoffmann | Regulator / Legal | Non-target | 1x |

---

## Execute

### C-01: Maria Chen (Maker / Retail, Low Tech)

**First reaction**: "Skills in a repo? I don't know what a repo is. This looks like something
my developers use, not me. I see words like 'namespace' and 'manifest' and I'm already lost.
Is there a simpler version?"

**Scores**: Usefulness: 1/5 | Clarity: 1/5 | Would-adopt: 1/5

**Findings**:
- F-01: Entire mental model assumes repo access and CLI fluency -- no entry point for non-technical users (BLOCKING)
- F-02: "Namespace" and "manifest" are undefined jargon in any user-facing description (MAJOR)
- F-03: No GUI, no web interface, no wizard -- CLI-only is a hard wall for makers (MAJOR)

**NPS**: 2/10
**Dealbreaker**: Requires a terminal. She has never opened one.

---

### C-02: James Okafor (Developer / SaaS, High Tech)

**First reaction**: "Skills in `.claude/skills/` -- I know exactly what this is. Copy the SKILL.md,
run `/signal:scout`, get an artifact. That's it. That's the whole install. I'm in."

**Scores**: Usefulness: 5/5 | Clarity: 4/5 | Would-adopt: 5/5

**Findings**:
- F-04: No SKILL.md schema documented yet -- I'd want to know what variables are available inside a skill prompt before I customize one (MINOR)
- F-05: 47 skills is a lot to discover -- I want a `/signal:help` or a README that shows me the fastest path to first value by role (MINOR)

**NPS**: 9/10
**Dealbreaker**: None. This is exactly how he wants to work.

---

### C-03: Priya Sharma (Architect / Finance, High Tech)

**First reaction**: "The topic narrative model is the part that interests me. I've always had
a problem where simulation artifacts scatter across the repo and nobody synthesizes them.
/signal:topic is the answer to that. My question is: what guarantees that /signal:topic status
finds everything? If someone puts an artifact in the wrong directory it disappears from the
topic view."

**Scores**: Usefulness: 5/5 | Clarity: 4/5 | Would-adopt: 4/5

**Findings**:
- F-06: Topic discovery relies on file naming convention -- one mis-named file breaks the topic view (MAJOR)
- F-07: No formal schema for SKILL.md content -- determinism and reproducibility across runs is unclear (MAJOR)
- F-08: 9 namespaces is the right number. The /flow: vs /trace: split is architecturally correct -- domain process vs. system platform is a real distinction (DELIGHT)

**NPS**: 8/10
**Dealbreaker**: If topic discovery is fragile (naming-convention-dependent), she won't trust the story output.

---

### C-04: David Kim (PM / Healthcare, Medium Tech)

**First reaction**: "This is what I've been missing. I run scouts and feasibility checks all
the time but they never connect to anything. The topic strategy model -- planning which signals
I need before committing to a feature -- that's exactly the structure I need. My concern is
whether I can do this without my engineers."

**Scores**: Usefulness: 4/5 | Clarity: 3/5 | Would-adopt: 4/5

**Findings**:
- F-09: /signal:scout and /signal:draft are PM-facing but still require CLI install -- needs a one-command install path (MAJOR)
- F-10: Topic strategy.md format is undocumented -- I don't know what a good signal plan looks like until I see an example (MINOR)
- F-11: The stage lifecycle (scout -> draft -> review -> ...) is visible in program but not surfaced for PMs who just want the topic view (MINOR)

**NPS**: 7/10
**Dealbreaker**: If install requires engineer involvement, PM adoption drops significantly.

---

### C-05: Elena Vasquez (Compliance / Insurance, Medium Tech)

**First reaction**: "I see /signal:review has a compliance persona in the user walkthrough.
That's good. But what I actually need is an audit trail -- if I run /signal:review on a spec
and it produces a finding, I need to know: who ran it, when, what version of the spec, what
version of the skill. The artifact filename gives me the date but not the rest."

**Scores**: Usefulness: 3/5 | Clarity: 3/5 | Would-adopt: 3/5

**Findings**:
- F-12: Artifact files have no provenance metadata -- no record of who ran the skill, which skill version, on which input hash (MAJOR)
- F-13: No finding lifecycle outside the skill run -- F-01 findings don't persist to a tracking system; once the Amend phase closes, there's no audit log (MAJOR)
- F-14: Compliance persona in /signal:review is a good inclusion -- signals that governance is considered (DELIGHT)

**NPS**: 5/10
**Dealbreaker**: Without provenance metadata, artifacts cannot be used as evidence in compliance reviews.

---

### C-06: Robert Tanaka (Auditor / Government, Low-Medium Tech)

**First reaction**: "I'm not the target user and I know it. But I'll tell you what worries me
from the outside: this produces a lot of Markdown files that look like analysis. Who owns them?
Are they versioned? Can they be amended after the fact without detection? From an audit
perspective, append-only is the right instinct but I'd want to see it enforced, not just
recommended."

**Scores**: Usefulness: 2/5 | Clarity: 2/5 | Would-adopt: 1/5

**Findings**:
- F-15: Append-only is a principle (P-02) but not enforced -- nothing prevents someone from editing a signal artifact after the fact (MAJOR)
- F-16: No ownership model -- who is responsible for a signal artifact? (MINOR)

**NPS**: 3/10
**Dealbreaker**: Not the target. But append-only enforcement matters for any team in a regulated industry.

---

### C-07: Catherine Moore (Executive / Consulting, Low Tech)

**First reaction**: "I don't understand what this is from the description. 'Signal gathering
for feature design' -- that could mean anything. If someone showed me a topic story output
and said 'this is what your team knows about this feature before they committed to building it,'
I would immediately understand the value. Lead with the output, not the mechanism."

**Scores**: Usefulness: 3/5 | Clarity: 2/5 | Would-adopt: 2/5

**Findings**:
- F-17: Value proposition is mechanism-first (9 namespaces, 47 skills) not outcome-first (confident feature decisions, no wasted builds) (MAJOR)
- F-18: No executive-facing artifact -- the topic story is the closest thing but it's aimed at the team, not the sponsor (MINOR)

**NPS**: 4/10
**Dealbreaker**: Cannot sponsor something she cannot explain in one sentence.

---

### C-08: Ahmad Al-Rashid (Partner / Energy, Medium Tech)

**First reaction**: "I'd install this for my delivery teams tomorrow. We run feature validation
constantly and the findings scatter. The topic model solves the scatter problem. My question
is: can I add custom personas for the energy sector? My customers are not C-01 through C-12 --
they're plant operators and SCADA engineers."

**Scores**: Usefulness: 4/5 | Clarity: 4/5 | Would-adopt: 4/5

**Findings**:
- F-19: Custom persona path exists (.craft/roles/signal/) but is not documented in any getting-started flow (MINOR)
- F-20: signal.manifest.json upgrade model is exactly right -- partners need to pin versions and control when they take updates (DELIGHT)

**NPS**: 8/10
**Dealbreaker**: None if custom persona path is clear.

---

### C-09: Lisa Johansson (SRE / Telecom, High Tech)

**First reaction**: "The /signal:trace namespace is written for me. Request tracing, state
validation, deployment tracing -- these are the three things I do before every release and
currently do by hand in Confluence. If this produces a structured artifact I can link from
a post-mortem, I'll adopt it immediately. The skills-in-repo model is correct -- I don't
want a plugin that updates itself without my knowledge."

**Scores**: Usefulness: 5/5 | Clarity: 5/5 | Would-adopt: 5/5

**Findings**:
- F-21: No CI/CD integration path documented -- I want to run /signal:trace as a pre-deploy gate, not just interactively (MAJOR)
- F-22: Skills-in-repo with version control is exactly right for SRE use -- pin, review changes before upgrade, roll back (DELIGHT)

**NPS**: 9/10
**Dealbreaker**: None. This is the right tool for the right job.

---

### C-10: Marcus Rivera (Data Scientist / Education, High Tech)

**First reaction**: "The /signal:prove namespace maps directly to how I think. Hypothesis,
experiments, synthesize, publish -- that's the scientific method as a skill set. I would
use this for every research question I bring to a product team. My concern: the artifacts
are Markdown. I want structured output I can pipe into a notebook or a dashboard."

**Scores**: Usefulness: 5/5 | Clarity: 4/5 | Would-adopt: 4/5

**Findings**:
- F-23: Markdown-only output -- no JSON sidecar, no structured schema, no notebook integration (MAJOR)
- F-24: /signal:prove maps the scientific method correctly -- hypothesis-first with falsification criteria is the right discipline (DELIGHT)
- F-25: prove:analysis skill description is vague -- no connection to actual telemetry or datasets (MINOR)

**NPS**: 7/10
**Dealbreaker**: Markdown-only output limits integration with data pipelines.

---

### C-11: Tomoko Watanabe (Team Lead / Manufacturing, Medium Tech)

**First reaction**: "The /signal:topic status command is what I would use every Monday morning.
Show me what signals exist, what's open, are we ready to commit. My problem is I can't run
a CLI command -- I need this in a dashboard or a Teams message. But the underlying model is
right: topic as the organizing unit, signals accumulating toward a design decision."

**Scores**: Usefulness: 4/5 | Clarity: 4/5 | Would-adopt: 3/5

**Findings**:
- F-26: /signal:topic status is CLI-only -- team leads need a shareable report format (MAJOR)
- F-27: No team assignment model -- signals are produced by individuals but the topic plan shows no signal ownership (MINOR)
- F-28: Topic as organizing unit resonates immediately -- "what do we know about this part before we commit to production?" (DELIGHT)

**NPS**: 6/10
**Dealbreaker**: If status output cannot be shared in Teams or a standup doc, adoption stalls at individual use.

---

### C-12: Frank Hoffmann (Regulator / Legal, Low Tech)

**First reaction**: "I am not the intended user. But I note that the plugin produces artifacts
with dates, topics, and item identifiers. If those artifacts are immutable after creation --
which your principles claim but do not enforce -- they could serve as contemporaneous records
in a regulatory context. That is a positioning opportunity you are not exploiting."

**Scores**: Usefulness: 2/5 | Clarity: 2/5 | Would-adopt: 1/5

**Findings**:
- F-29: Immutability is claimed (P-02) but unenforced -- regulatory argument requires tamper-evidence (MINOR, non-target)
- F-30: Timestamped artifacts as design decision evidence is a positioning opportunity for regulated industries (OBSERVATION)

**NPS**: 3/10
**Dealbreaker**: Not the target. No action required.

---

## Findings Synthesis

### Weighted Aggregate Scores

| Dimension | Primary avg (3x) | Secondary avg (2x) | Non-target avg (1x) | Weighted avg |
|-----------|-----------------|-------------------|--------------------|-|
| Usefulness | 5.00 | 3.75 | 2.00 | 4.12 |
| Clarity | 4.25 | 3.50 | 1.75 | 3.71 |
| Would-adopt | 4.50 | 3.50 | 1.25 | 3.83 |
| **Overall** | **4.58** | **3.58** | **1.67** | **3.89** |

### Adoption Blockers

None. All four primary personas scored would-adopt >= 4. The plugin is strongly validated
for its target audience (high-tech developers, architects, SREs, data scientists).

### Positioning Leaks

- C-07 Catherine: Does not understand value from current description. Executives who fund
  these teams will not sponsor what they cannot explain. Risk is indirect but real.
- C-01 Maria: "Zero barrier to entry" language implies non-technical users are in scope.
  They are not. The phrase needs scoping.

### Delight Signals

Skills-in-repo install model, /flow: vs /trace: architectural split, /signal:prove mapping
the scientific method, signal.manifest.json version pinning, and the topic-as-organizing-unit
model all generated explicit delight from primary and secondary personas. The core design is
sound.

### Cross-Persona Themes

| Theme | Personas | Severity |
|-------|----------|----------|
| No provenance metadata in artifacts | C-05, C-06, C-12 | MAJOR |
| Markdown-only output, no structured schema | C-02, C-09, C-10 | MAJOR |
| No shareable / non-CLI status output | C-04, C-07, C-11 | MAJOR |
| Value prop is mechanism-first not outcome-first | C-01, C-04, C-07 | MAJOR |
| Topic discovery fragile (naming-dependent) | C-03, C-09 | MAJOR |
| "Zero barrier" overclaims for non-technical users | C-01, C-07 | MINOR |

---

## Amendment Recommendations

### A-01: Frontmatter in every artifact (addresses F-12, F-06, F-15)

Every skill writes a standard frontmatter block at the top of the artifact:

  ---
  skill: signal:review
  topic: frogs
  item: users
  date: 2026-03-14
  skill_version: 0.1.0
  input: design/specs/SPEC-FROGS-01.md
  ---

Gives provenance, enables discovery, makes append-only verifiable via git blame.
No user action required -- written by the skill automatically.

### A-02: Optional JSON sidecar (addresses F-23, F-04)

Each skill supports a --json flag producing {topic}-{item}-{date}.json alongside the
Markdown artifact. Schema documented in the skill. Enables notebook integration and
CI/CD consumption.

### A-03: /signal:topic report command (addresses F-26, F-11)

Add /signal:topic report that writes simulations/{topic}/status-{date}.md as a
shareable summary. Add --format teams for a compact ASCII card suitable for paste
into a Teams message or standup doc.

### A-04: Reframe value proposition as outcome-first (addresses F-17)

Change the one-liner to: "Know what you know before you commit. Signal helps teams
gather evidence for feature decisions and synthesizes it into a story."
Drop the namespace and skill counts from the headline -- they are implementation detail.

### A-05: Scope "zero barrier" to developers (addresses F-01, F-09)

Rewrite to: "Zero barrier for developers -- copy one SKILL.md file and run." Remove
any implication that non-technical users are the primary audience.

### A-06: Document the custom persona path at first run (addresses F-19)

Any skill that uses personas should surface on first run: "To add personas for your
domain, create .craft/roles/signal/{name}/ROLE.md. Template at
.claude/skills/signal-roles-template/."