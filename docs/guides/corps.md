# corp — Virtual Org Governance and ROB

## The short version

The corp namespace runs your virtual organization against features, PRs, and business reviews.
Four skills: scan a repo to draft an org, build the org from a confirmed config, run Review
of Business stages, and review a PR through the full org. Corp brings Signal from feature
signals to org-level readiness.

---

## When to use this namespace

Use corp when decisions require org-level review: when a feature affects multiple teams,
when a PR has cross-cutting security or compliance implications, or when you want to rehearse
a committee meeting before it happens.

- You are about to build a new product area and want to set up an org configuration.
- A feature needs ROB review before the next planning cycle.
- You want every relevant role in your org to review a PR before it merges.
- Your monthly product review is tomorrow and you want to rehearse it today.

The corp namespace requires an `org.yaml` configuration -- the contract between your real org
structure and Signal's virtual org model. corp-scan generates a draft from your repo.
corp-build writes the role files. After that, corp-rob and corp-pr use your actual org roles
for every review.

---

## The virtual company model

Corp's virtual company lives in two places:

```
org.yaml                    the org configuration contract
.roles/{area}/        role definition files (one per role per team)
```

`org.yaml` declares your org structure: divisions, tribes, pillars, teams, and the exec office.
It does not describe what each person does -- that is what `.roles/` is for. The roles
in `.roles/` are markdown files with each role's orientation, lens, expertise, scope,
and collaboration pattern.

When corp-rob or corp-pr runs, it reads `org.yaml` to select relevant participants, then
loads each participant's role file from `.roles/` to instantiate their perspective.
The virtual company is as good as the role definitions behind it.

Every team always includes an Inertia Advocate role -- the voice of the status quo. The
Inertia Advocate's job is to argue that the current workaround is sufficient. This is not
sabotage; it is the strongest quality check a team has.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `corp-scan` | Walks the repo and produces a draft org.yaml. Pivot modes: directory, concept, service, domain. Does NOT write .roles/ -- outputs draft for human review first. | First-time setup. When onboarding a new codebase to corp. |
| `corp-build` | Reads confirmed org.yaml and generates org-chart.md and all .roles/ files. Supports arbitrary group nesting. Inertia-advocate always included per team. | After confirming org.yaml. Regenerate when org structure changes. |
| `corp-rob` | Runs Review of Business stages. Stages: leadership, teams, pm, tpm, arch-board, exec-office. --stage all for full ROB. --scope {group} for one division. Reads org.yaml + .roles/. | Before planning cycles, feature commits, or major releases. |
| `corp-pr` | Routes a PR through the full org. Selects reviewers based on files changed. Each role reviews from their perspective. Per-role findings P1/P2/P3, consensus analysis, go/no-go recommendation. | Before merging high-impact PRs. Replaces "assign 3 reviewers and hope." |
| `corp-chart` | Generates org structure for a product or domain from existing .roles/. Produces org-chart.md with ASCII box diagram, headcount by area, committee charters, operating rhythm. | When you need a visual org representation. After corp-build. |
| `corp-committee` | Simulates a committee meeting before the real one: ROB, shiproom, or arch-board. Each participant reviews from their role. Produces mock meeting minutes. | Before real committee meetings. Rehearsal artifact. |

---

## Example workflow: setting up a new org

Your team is starting a new product area and wants corp configured.

**Step 1: Scan the repo.**

```
/corp-scan my-product-area
```

Walks the repo. Produces a draft org.yaml with detected teams, suggested group structure,
standard roles. Returns the draft for your review -- does NOT write any role files yet.

**Step 2: Confirm and build.**

You review the draft, adjust team names, add a Security Architect role, confirm. Then:

```
/corp-build my-product-area
```

Generates org-chart.md and `.roles/` directory tree with a role file for every
role in the confirmed org.yaml. Inertia Advocate is included in every team automatically.

**Step 3: Run a ROB before the next planning cycle.**

```
/corp-rob payment-reminders --stage all
```

Runs six stages in sequence: leadership (exec briefing), teams (all team self-reviews),
pm (PM cross-alignment), tpm (risk register + go/no-go), arch-board (architecture decision
review), exec-office (S-office missions cascade). Each stage produces its artifact.
The tpm stage produces a risk register and a go/no-go recommendation before the real meeting.

**Step 4: Rehearse the committee meeting.**

```
/corp-committee payment-reminders --type shiproom
```

Simulates the shiproom meeting. Each participant reads the feature signals and reviews from
their role. Produces mock minutes: decisions reached, action items, dissenting opinions.
Compare against the real meeting outcomes to calibrate your role definitions.

---

## What it produces

Corp artifacts write to `simulations/corp/` and `design/corp/`:

```
simulations/corp/
  payment-reminders-scan-2026-03-16.md
  payment-reminders-rob-leadership-2026-03-16.md
  payment-reminders-rob-all-2026-03-16.md
  payment-reminders-pr-review-2026-03-16.md
  payment-reminders-committee-2026-03-16.md
design/corp/
  org-chart.md
.roles/
  {area}/{role}.md
```

---

## Common patterns

**corp-rob before the real meeting, then compare.** The Simulation Rehearsal achievement
requires running corp-rob before a real committee meeting and recording the comparison.
The gap between what the simulation predicted and what actually happened is a calibration
signal for your role definitions. The first few comparisons are always revealing.

**corp-pr selects reviewers by files changed.** You do not specify who reviews -- corp-pr
reads the diff and selects roles from org.yaml based on what changed. Security changes get
security and compliance roles. Compiler changes get architecture roles. This is what
"everyone relevant reviewed it" looks like at the org level.

**The Inertia Advocate is always present.** Every team in corp includes an Inertia Advocate.
When corp-rob runs, the Inertia Advocate argues for the status quo at every stage. If the
feature cannot survive the Inertia Advocate's objections, it is not ready for the real ROB.

---

## What's next

- **[crew](crew.md)** -- crew is the lightweight version of corp. No org.yaml required, stock roles activate by default.
- **[topic](topic.md)** -- topic-story is the input to corp-rob. Synthesize signals before running the ROB.
- **[ACHIEVEMENTS](../ACHIEVEMENTS.md)** -- Full Corp, PR Reviewed, and Simulation Rehearsal are corp achievements.
