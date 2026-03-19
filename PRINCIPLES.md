# Sim Plugin — Design Principles

These principles guide every decision about the sim plugin: skill design, artifact layout,
naming conventions, agent behavior, and namespace architecture. When a decision is unclear,
check here first.

---

## P-01: Concurrent by Default

The plugin is used in shared repositories where multiple people run simulations in parallel.
Every design decision must be safe under concurrent use.

**What this means:**
- Artifacts are independent dated files. Two runs of the same skill on the same topic produce
  two files, not a conflict. File naming encodes enough uniqueness (topic-signal-date) that
  concurrent runs never collide.
- No shared mutable state. No file that two agents or two users write to simultaneously.
  TOPICS.md is a registry that humans update intentionally, not a file skills append to.
- No skill depends on another skill's output file at execution time. Cross-namespace flows
  are documented (review findings feed back to draft), but skills do not read each other's
  artifacts as execution inputs. A prove:synthesize run reads the repo and the spec -- not
  the output of a concurrent review:design run.
- Investigations are self-contained. Each prove:* run starts from its own hypothesis, not
  from a file another agent wrote. If synthesis is needed across runs, a human or a later
  session performs it intentionally.

**Multiple contributors at the same stage:**
Multiple people (or agents) can contribute to the same topic at the same stage simultaneously.
Two developers running /trace:state on the `frogs` topic produce:
  `frogs-authflow-2026-03-14.md`
  `frogs-cachepath-2026-03-14.md`
Different signals, different files, no conflict. The signal name is the contributor's differentiator.
When a later synthesis is needed, a human or a /prove:synthesize run reads all `frogs-*`
files and produces a single synthesis. The synthesis is never automatic -- it is intentional.

**Anti-patterns to avoid:**
- "Agent B synthesizes Agent A's output" (ordering dependency, breaks concurrency)
- "All agents append to the same findings file" (write collision)
- "The synthesis step runs after all other agents complete" (sequencing assumption)
- "One signal per topic per stage" (forces serial contribution)

---

## P-02: Artifacts Are Append-Only

Skills produce new files. They never update or overwrite existing artifacts.

**What this means:**
- Every skill run produces `{topic}-{signal}-{date}.md`. The signal name describes the angle
  this artifact covers (e.g., `frogs-authflow`, `frogs-competitors`). If you run the same
  skill twice on the same day on different angles, vary the signal name. The date is not a
  version number -- it is a timestamp.
- The amend phase of a skill's lifecycle produces a new artifact or an amendment section
  appended to the original, not an in-place edit of a prior run's output.
- Findings, DCRs, and synthesis documents are final when written. They are superseded by
  new artifacts, not edited. The history of what we believed and when is preserved.

---

## P-03: Skills Are Self-Contained

Each skill drives its own E2E workflow from first prompt to final artifact. No skill
requires another skill to have run first.

**What this means:**
- Stock roles ship with every skill. Zero setup required.
- Each skill reads the repo and the spec directly -- it does not depend on a prior skill's
  output file. A user can run /trace:state without having run /scout:feasibility first.
- Cross-namespace flows described in specs (e.g., "listen:feedback findings loop back to
  draft:spec") are recommendations for the human, not hard execution dependencies.
- The program orchestrator (/program:plan) sequences skills into a staged plan, but each
  skill in that plan remains self-contained and can be run standalone.

---

## P-04: Namespace = Audience

The namespace prefix tells the user whether this skill is for them, without reading
documentation.

**What this means:**
- /scout: and /draft: are PM-facing. Lightweight default. Speed to output.
- /trace: and /flow: are developer-facing. Full default. Rigor expected.
- /review: is team-facing. Full default. Multi-perspective synthesis.
- /prove: is researcher/PM-facing. Full default. Hypothesis-first discipline.
- /listen: is team-facing, post-ship orientation. Lightweight default.
- /program: is lead-facing. Full default. Orchestration.

A developer who sees /scout: knows it is not their primary tool. A PM who sees /trace:
knows it is not theirs. Namespace routing is zero-effort.

---

## P-05: Zero Barrier to First Run

The first run of any skill must produce a useful result with no prior setup.

**What this means:**
- Stock roles are embedded in each skill and activate by default.
- No configuration file required. simulate.yaml is created on first run if the user wants
  to customize, but it is never required.
- The first artifact a user sees should be useful, not a setup wizard asking 10 questions.
- If a skill would produce significantly better results with custom roles, it says so after
  producing its first result -- not before.

---

## P-06: Every Program Ends with an Echo

After all stages of a program complete, the echo synthesizes unexpected findings.

**What this means:**
- The echo is not a review. It is a reflection. It asks one question: "What did we learn
  that we did not expect?"
- The echo is always the final stage in program.yaml. It is auto-generated from prior stage
  findings -- no skill to run, just synthesis.
- Programs that skip the echo ship faster but learn slower.
- The echo artifact ({topic}-echo-{date}.md) becomes institutional memory for the next
  team that walks this path.

---

## P-07: Naming Is a Contract

Artifact naming (`{topic}-{signal}-{date}.md`) is a contract, not a convention.

**What this means:**
- Topic prefix ties all artifacts for an initiative across all directories. Glob `sim-*`
  finds everything. Renaming a topic breaks discoverability.
- Signal name describes what this artifact is about (the angle it covers), not the skill
  that produced it. `sim-q01-crossrole-2026-03-14.md` not `sim-prove-synthesize-2026-03-14.md`.
- Signal name signals intent. Same signal = same contribution = edit the existing file (you
  are adding to what someone else started on this angle). Different signal = different angle =
  new file. This is the collaboration rule: `frogs-authflow` and `frogs-cachepath` are two
  signals on the frogs topic; a third person investigating auth flow edits `frogs-authflow`,
  not creates `frogs-authflow-v2`.
- Users never need to say the word "signal." They name the angle and the system tracks it.
- Date is when it was created, ISO 8601. It is a timestamp for ordering, not a version.
- Skill outputs land in the directory matching their namespace and skill:
  `signals/{namespace}/{skill}/{topic}-{signal}-{date}.md`.
  No exceptions.

---

## P-08: Techniques Have Heritage

Every skill traces back to a proven technique with evidence. New skills are not invented
without evidence.

**What this means:**
- Each skill in the catalog maps to one or more techniques in `techniques/01-09/`.
- User testing results (Q01, Q02) are the evidence base for namespace architecture decisions.
- New skills proposed without technique heritage are flagged and require a prove: investigation
  before they are added to the catalog.
- The evidence corpus in `techniques/` is read-only historical record. New evidence goes into
  `signals/prove/` using the prove: lifecycle.

---

## P-09: Every Artifact Has Provenance

Skills write a standard frontmatter block at the top of every artifact. No user action required.

```
---
skill: signal:review
topic: frogs
item: users
date: 2026-03-14
skill_version: 0.1.0
input: design/specs/SPEC-FROGS-01.md
---
```

**What this means:**
- Provenance is automatic -- the skill writes it, not the user
- Enables discovery by any tool (grep frontmatter, parse YAML)
- Makes append-only verifiable -- git blame on the frontmatter block shows if it was edited
- Enables compliance use -- who ran it, when, on what input, at what skill version

Skills also support `--json` to produce a structured sidecar `{topic}-{item}-{date}.json`
alongside the Markdown artifact. The JSON schema is documented in the skill. Enables notebook
integration, dashboard queries, and CI/CD consumption without parsing Markdown.

---

## P-10: Skills Are Binding-Agnostic

The methodology of a skill is defined once. How it is invoked is a binding decision.

**What this means:**
- Skill bodies are authored in `signal.program.yaml` as the single source of truth
- Binding variants (flat standalone, grouped namespace, plugin, Cursor, Cline/Roo)
  are generated from the same skill content with different packaging configuration
- Skill instructions never reference their invocation form -- they do not say
  "/prove-hypothesis" or "/prove hypothesis". They describe what to do, not how
  to call it.
- The atomic skill identity is `{namespace}-{skill}` (e.g., `prove-hypothesis`).
  Bindings wrap this identity in the invocation shape the target platform requires.
- See `signal.bindings.md` for the full binding specification and release strategy.

---

## Summary

| Principle | One Line |
|-----------|----------|
| P-01 Concurrent by Default | Multiple people, same repo, no collisions |
| P-02 Append-Only Artifacts | New files, never overwrites |
| P-03 Self-Contained Skills | No execution dependencies between skills |
| P-04 Namespace = Audience | Routing is zero-effort |
| P-05 Zero Barrier | First run produces results with no setup |
| P-06 Echo | Every program ends with a reflection |
| P-07 Naming Is a Contract | topic-signal-date, no exceptions |
| P-08 Heritage | Every skill traces to proven technique |
| P-09 Provenance | Every artifact has frontmatter; --json for structured output |
| P-10 Binding-Agnostic | Skills defined once; invocation shape is a binding decision |

---

## P-11: The Customer Test Is the Rubric

The quality of a skill is not determined by its golden score. It is determined by whether
a real person — unfamiliar with Signal, running it for the first time, trying to answer
a genuine question — can complete their task without confusion.

The rubric found by the quest loop is what the skill *should* do.
The customer test found by simulation is whether it *actually* does it.

Run the customer test before you ship. Run it again after every significant change.
24 personas across 3 rounds found 16 bugs that 168 golden prompts did not. The quest
loop builds the ship. The customer test confirms it floats.

**What this means:**
- Every skill with a golden prompt also needs a simulated customer run
- Bugs found by customer test are higher priority than rubric gaps
- "All essential criteria pass" is necessary but not sufficient
- The test topic should be real: a feature a real team would actually consider
- Negative test results (customer scores 1/5) are as valuable as positive ones --
  they tell you exactly what to fix

**The flair:** *The primary competitor in quality assurance is also inertia: the
assumption that because the rubric passes, the user will too.*

---

## Summary

| Principle | One Line |
|-----------|----------|
| P-01 Concurrent by Default | Multiple people, same repo, no collisions |
| P-02 Append-Only Artifacts | New files, never overwrites |
| P-03 Self-Contained Skills | No execution dependencies between skills |
| P-04 Namespace = Audience | Routing is zero-effort |
| P-05 Zero Barrier | First run produces results with no setup |
| P-06 Echo | Every program ends with a reflection |
| P-07 Naming Is a Contract | topic-signal-date, no exceptions |
| P-08 Heritage | Every skill traces to proven technique |
| P-09 Provenance | Every artifact has frontmatter; --json for structured output |
| P-10 Binding-Agnostic | Skills defined once; invocation shape is a binding decision |
| P-11 Customer Test Is the Rubric | The quest loop builds the ship. The customer test confirms it floats. |
