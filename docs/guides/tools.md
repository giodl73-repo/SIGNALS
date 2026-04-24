# tools — Mock Coverage and Workflow Scaffolding

## The short version

The tools namespace generates synthetic signal artifacts for testing, onboarding, and
coverage validation. Three skills: mock all namespaces in one pass, mock a single namespace,
and review mock coverage to decide what needs to be replaced with real investigation.

---

## When to use this namespace

Use tools when you want to explore Signal's output format without committing to a full
investigation, when you are onboarding a new team to Signal's artifact structures, or
when you want to scaffold coverage for a topic before running the real skills.

- You are new to Signal and want to see what the artifact structures look like before running
  real investigations.
- You want to test tooling or automation that consumes Signal artifacts without doing real
  research.
- You are scaffolding a new topic and want placeholder coverage before the real investigation
  starts.
- You want to see which namespaces need real investigation versus which can be mock-accepted.

Tools are not evidence. Artifacts produced by tools are annotated as MOCK and are not
equivalent to artifacts produced by real investigation skills. tools-accept is the formal
decision step that records which mock artifacts are acceptable and which need to be replaced.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `tools-coverage` | Generate synthetic signal artifacts for all namespaces in a single pass. Each mock follows the structural requirements of its golden rubric. Automatic pre-flagging: EVIDENCE-HEAVY namespaces get REAL-REQUIRED. Coverage summary table. Supports --tier 1/2/3 and --compliance flags. | When you want complete structural coverage immediately. First step in mock-first workflow. |
| `tools-preview` | Generate a mock artifact for a single namespace. Same annotation and category rules as tools-coverage. --skill to target a specific skill. Supports --tier 1/2/3. | When you want to preview the artifact format for a specific namespace before running the real skill. |
| `tools-accept` | Step 2 of mock-first workflow: review mock coverage picture and produce MOCK-ACCEPTED or REAL-REQUIRED decisions per namespace. Writes updated Status fields back into the source mock artifact -- the only permitted in-place edit in Signal. Reason codes: STRUCTURAL-COVERAGE-SUFFICIENT or DOMAIN-KNOWLEDGE-CONSISTENT. Produces next-steps list. | After tools-coverage. Formalizes which namespaces need real investigation. |

---

## The mock-first workflow

Mock-first is a scaffolding pattern, not a replacement for real investigation. It is most
useful for teams onboarding to Signal and for topics where you want to understand coverage
requirements before committing to full investigation.

**Step 1: Generate mock coverage.**

```
/tools-coverage payment-reminders
```

Produces synthetic artifacts for all namespaces. Each artifact is annotated:
- `MOCK-ACCEPTED`: structural coverage is sufficient for this namespace given the topic.
- `REAL-REQUIRED`: this namespace requires genuine investigation -- mock output cannot
  substitute. Evidence-heavy namespaces (discover-hypothesis, discover-websearch,
  discover-synthesize, validate-feedback, validate-adoption) are always pre-flagged
  REAL-REQUIRED. Compliance namespaces at any tier are always pre-flagged REAL-REQUIRED.

**Step 2: Review the coverage picture.**

```
/tools-accept payment-reminders
```

Reads the mock artifacts and the coverage picture. For each namespace: records the decision
(MOCK-ACCEPTED or REAL-REQUIRED), the reason code, and the next-steps recommendation.
Writes the Status field back into the source mock artifact.

Output: a next-steps list showing exactly which real investigation skills need to run.
The acceptance artifact becomes the investigation brief: here is what the mocks told us,
here is what still needs to be done.

**Step 3: Run the real skills on REAL-REQUIRED namespaces.**

The acceptance output tells you which skills to run next. Work through the REAL-REQUIRED
namespaces with the real investigation skills.

---

## What it produces

All tools artifacts write to `simulations/mock/`:

```
simulations/mock/
  payment-reminders-mock-2026-03-16.md
  payment-reminders-discover-mock-2026-03-16.md
  payment-reminders-accept-2026-03-16.md
```

Example frontmatter for a mock artifact:

```yaml
---
skill: tools-coverage
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
mock: true
---
```

The `mock: true` field distinguishes tools output from real investigation output. Any
downstream skill that reads Signal artifacts will detect this field and treat the content
accordingly.

---

## Common patterns

**tools-coverage is a format explorer, not a research tool.** The mock artifacts show you
what a real artifact looks like structurally. They do not contain real evidence, real
findings, or real scoring. Use them to understand the format before you invest in the
real investigation.

**tools-accept is the only skill that edits source artifacts.** Every other Signal skill
appends or creates. tools-accept writes back to the source mock artifact to update Status
fields. This is by design: the acceptance decision is part of the mock artifact's lifecycle,
not a separate artifact.

**REAL-REQUIRED is not a failure.** A namespace flagged REAL-REQUIRED means it is important
enough that mock output cannot substitute. This is a useful finding: it tells you where to
invest investigation effort. Evidence-heavy namespaces (hypothesis, websearch, synthesis,
feedback, adoption) are always REAL-REQUIRED by definition.

---

## What's next

- **[discover](discover.md)** -- after tools-accept, run the REAL-REQUIRED evidence skills.
- **[validate](validate.md)** -- feedback and adoption are always REAL-REQUIRED; run them
  after mocks identify the namespace priority.
- **[govern](govern.md)** -- govern-status tracks the transition from mock to real coverage.
