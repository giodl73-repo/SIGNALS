Written to `simulations/quest/rubrics/corps-pr-rubric-v2-2026-03-16.md`.

---

Here is the complete updated rubric:

---

# Corps-PR Review Rubric — v2

**Skill**: corps-pr
**Version**: v2 (updated from v1 after Round 1 scoring — added C-11, C-12 from V-01 excellence signals)
**Date**: 2026-03-16

---

## Design Intent

The core tension this rubric guards against is **silent selection + generic output**: corps-pr's entire value is that reviewer routing is traceable to the diff and that each reviewer sounds like their role. A run that selects reviewers without showing why, or produces findings that any generic reviewer could write, fails two essential criteria independently — making it impossible to pass golden without fixing both.

**v2 additions**: Round 1 scoring identified two patterns in V-01 that pushed it from 92.5 to 100 vs V-02. Both are added as aspirational criteria: (C-11) Inertia-first sequencing that turns the Advocate's output into a reference object other roles argue against, and (C-12) explicit anti-pattern prohibition in divergence explanations that forces architectural mechanism naming rather than perspective labeling.

---

## Essential Criteria (60 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | Reviewer selection is disclosed with a files-changed-to-role mapping | essential | transparency | Output contains a reviewer selection section that maps each changed file (or file group) to the org.yaml role selected to review it, with an explicit reason for each selection. A reviewer list with no file mapping is not acceptable. A role that appears in the output but whose selection cannot be traced to a specific file or files-changed signal is a hard fail. |
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
| C-09 | Consensus analysis includes root cause synthesis for role-divergent findings | aspirational | depth | When two or more roles disagree on a finding, the consensus section contains a root cause synthesis stating WHY the roles diverge — not just that they do. The synthesis must name the structural reason (e.g., "compiler-lead rates P1 because the change affects codegen path; tpm rates P3 because no user-facing behavior changes"). A consensus section that only lists the highest-severity verdict without explaining divergence fails. |
| C-10 | Go/no-go conditions are actionable: each condition names the role responsible for sign-off | aspirational | correctness | When the recommendation is GO WITH CONDITIONS, each condition names: (a) what must be resolved, (b) which role must confirm resolution before merge. A GO WITH CONDITIONS recommendation that lists conditions without named owner roles fails. A GO or NO-GO recommendation passes by default. |
| **C-11** | **Inertia Advocate is sequenced first among all selected reviewers** | aspirational | depth | The Inertia Advocate's findings section appears before all technical role findings sections. This sequencing establishes a status-quo baseline that technical reviewers can explicitly argue against, generating structural divergence rather than pile-on agreement. The Inertia Advocate's findings become a reference object that other roles respond to — their P1s and P2s are anchored against "Inertia Advocate found this sufficient." A run that places the Inertia Advocate last or in any non-first position fails. A run that does not include the Inertia Advocate as a selected reviewer passes by default. |
| **C-12** | **Consensus divergence explanations name the architectural mechanism, not a perspective label** | aspirational | depth | When the consensus section explains why two roles diverge on a finding, the explanation must name the structural or architectural reason — not use a perspective-label phrase such as "they have different perspectives," "they prioritize differently," or "their roles lead them to different conclusions." A valid explanation names the mechanism: what property of the code, system, or change causes each role to rate it as they do. A divergence explanation that consists solely of a perspective label with no mechanism fails. A run with no divergent findings passes by default. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

*aspirational denominator increased from 2 to 4 in v2; each criterion is worth 2.5 pts; a perfect run still scores 100.*

---

## Common Failure Modes

*(C-01 through C-10 unchanged; two new entries:)*

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| -- | C-11 | Inertia Advocate is a selected reviewer but their section appears after security-architect and compiler-lead; their status-quo finding cannot function as a baseline because technical objections are already on record |
| -- | C-12 | Consensus notes "compiler-lead and tpm see this differently due to their respective roles"; no mechanism is named; the explanation is indistinguishable from a generic disagreement label and gives the reader nothing actionable |

---

**What changed from v1**: The two gaps that V-02 exposed — C-08 partial (AMEND unhandled) and C-10 partial (sign-off owner not enforced by schema) — were already in v1. The two new criteria capture the V-01 patterns that V-02 lacked by design: sequencing the Inertia Advocate first so technical roles argue against a baseline, and forcing mechanism-level divergence explanations rather than perspective labels. These are aspirational because a run can pass golden (all 5 essential, composite >= 80) without them — but they are what separates a 92.5 from a 100.
y skipped with no coverage gap notice |
| -- | C-07 | Each role section ends abruptly after the last finding; reader must count manually to know how many P1s the security role raised |
| -- | C-08 | AMEND adds a compliance reviewer; output shows the new reviewer's findings but never discloses what changed from the prior run or which earlier findings are now superseded |
| -- | C-09 | Compiler-lead rates a type-system change P1; tpm rates it P3; consensus block picks P1 as the winner but does not explain why the two roles diverged |
| -- | C-10 | Recommendation is GO WITH CONDITIONS with three conditions listed; no condition names which role must confirm resolution; the merge gate is ambiguous |
| -- | C-11 | Inertia Advocate is listed as a selected reviewer but their section appears after security-architect and compiler-lead; their status-quo finding cannot function as a baseline because technical objections are already on record |
| -- | C-12 | Consensus notes "compiler-lead and tpm see this differently due to their respective roles"; no mechanism is named; the explanation is indistinguishable from a generic disagreement label and gives the reader nothing actionable |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-16 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-16 | Added C-11 (Inertia-first sequencing) and C-12 (mechanism-level divergence explanation) from V-01 Round 1 excellence signals; aspirational denominator updated from 2 to 4 in scoring formula |
