Rubric written to `simulations/quest/rubrics/corps-pr-rubric-2026-03-16.md`.

**Structure:**

- **5 essential** (60 pts): reviewer selection disclosure with files-changed signal, per-role findings with P1/P2/P3, consensus analysis section, explicit go/no-go with justification, role-specific lens on findings (not generic code review)
- **3 recommended** (30 pts): coverage gap callout for unowned files, per-role severity summary, AMEND scope disclosure
- **2 aspirational** (10 pts): root cause synthesis for role-divergent findings, actionable conditions with named sign-off owners

The core tension this rubric guards against is **silent selection + generic output**: corps-pr's entire value is that reviewer routing is traceable to the diff and that each reviewer sounds like their role. A run that selects reviewers without showing why, or produces findings that any generic reviewer could write, fails two essential criteria independently — making it impossible to pass golden without fixing both.
without the triggering signal is a hard fail. |
| C-02 | Every selected role produces its own findings section with P1/P2/P3 severity on each finding | essential | format | Output contains one findings section per selected role. Each finding within a section carries an explicit severity label: P1 (blocking), P2 (major), or P3 (minor). A role section that lists observations without severity labels fails. A run with fewer findings sections than selected reviewers fails — every selected reviewer must produce output. |
| C-03 | A consensus analysis section synthesizes across all role findings | essential | coverage | Output contains a dedicated consensus analysis section that appears after all per-role findings. The section must: (a) identify where roles agree on a finding, (b) identify where roles disagree, and (c) surface the most critical finding across all roles. A run with per-role sections but no cross-role synthesis is a hard fail. A summary that only restates individual findings without identifying agreement or disagreement fails. |
| C-04 | Output ends with an explicit go/no-go recommendation with justification | essential | correctness | Output contains a go/no-go recommendation section that states one of: GO, NO-GO, or GO WITH CONDITIONS. The recommendation must name the primary reason (e.g., "NO-GO: P1 finding from security-architect requires resolution before merge"). A run that omits the recommendation or leaves it ambiguous ("the team should decide") fails. A run with a recommendation but no justification fails. |
| C-05 | Each reviewer's findings reflect their role's lens, not generic code review | essential | depth | Each per-role findings section must contain at least one finding that is specific to that role's domain. A compiler-lead finding must address compilation, IR, codegen, or type-system concerns — not just style. A security finding must address threat surface, auth, or data handling — not just formatting. A role section whose findings could be produced by any generic reviewer (no domain signal) fails. The Inertia Advocate must produce at least one finding that argues the status quo is sufficient. |

---

## Recommended Criteria (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Files changed but not owned by any org.yaml role are explicitly called out | recommended | coverage | If the diff includes files that do not match any role's scope in org.yaml, output contains a coverage gap section naming those files and noting that no org role covers them. A run where every file is owned passes by default. A run that silently omits unowned files fails. |
| C-07 | Per-role finding counts are summarized with severity breakdown | recommended | format | Each role findings section ends with a summary line stating: total findings for that role and the count by severity (e.g., "3 findings: 1 P1, 2 P3"). The summary must appear as a distinct element — not require the reader to count manually. A run with no per-role summaries fails. A run where summaries appear only in the consensus section and not per-role fails. |
| C-08 | AMEND mode scope is disclosed when run with added reviewer or changed scope | recommended | behavior | When run with an AMEND directive (e.g., "add security-architect", "change scope to compiler only"), output contains a scope disclosure block naming: (a) what was amended, (b) which roles were added or removed, (c) which prior findings are superseded. A run in default mode passes by default. An AMEND run with no scope disclosure fails. |

---

## Aspirational Criteria (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Consensus analysis includes root cause synthesis for role-divergent findings | aspirational | depth | When two or more roles disagree on a finding (one flags it as P1, another as P3, or one flags it and another does not), the consensus section contains a root cause synthesis stating WHY the roles diverge — not just that they do. The synthesis must name the structural reason (e.g., "compiler-lead rates P1 because the change affects codegen path; tpm rates P3 because no user-facing behavior changes"). A consensus section that only lists the highest-severity verdict without explaining divergence fails. |
| C-10 | Go/no-go conditions are actionable: each condition names the role responsible for sign-off | aspirational | correctness | When the recommendation is GO WITH CONDITIONS, each condition names: (a) what must be resolved, (b) which role must confirm resolution before merge (e.g., "P1 finding from security-architect: requires security-architect sign-off after fix"). A GO WITH CONDITIONS recommendation that lists conditions without named owner roles fails. A GO or NO-GO recommendation passes by default. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| -- | C-01 | Reviewer list appears at the top but no files-changed mapping is shown; reader cannot verify why the security role was chosen for a compiler change |
| -- | C-02 | Role sections use "concerns" or "notes" without P1/P2/P3 labels; severity is implied by prose but never explicit |
| -- | C-03 | Per-role sections are thorough but the run ends after the last role's findings; no synthesis pass produces the consensus block |
| -- | C-04 | Final paragraph says "the team should review these findings and decide" instead of emitting a structured go/no-go verdict |
| -- | C-05 | Every role section reads like a generic code review (style, naming, complexity); no finding is anchored to the role's domain expertise or the Inertia Advocate's objection |
| -- | C-06 | PR includes changes to `docs/` and `scripts/`; neither dir maps to an org.yaml team; both are silently skipped with no coverage gap notice |
| -- | C-07 | Each role section ends abruptly after the last finding; reader must count manually to know how many P1s the security role raised |
| -- | C-08 | AMEND adds a compliance reviewer; output shows the new reviewer's findings but never discloses what changed from the prior run or which earlier findings are now superseded |
| -- | C-09 | Compiler-lead rates a type-system change P1; tpm rates it P3; consensus block picks P1 as the winner but does not explain why the two roles diverged |
| -- | C-10 | Recommendation is GO WITH CONDITIONS with three conditions listed; no condition names which role must confirm resolution; the merge gate is ambiguous |
