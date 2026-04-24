Written to `simulations/quest/rubrics/corps-pr-rubric-v3-2026-03-16.md`.

---

Here is the complete updated rubric:

---

# Corps-PR Review Rubric — v3

**Skill**: corps-pr
**Version**: v3 (updated from v2 after Round 2 scoring — added C-13, C-14 from Round 2 excellence signals)
**Date**: 2026-03-16

---

## Design Intent

The core tension this rubric guards against is **silent selection + generic output**: corps-pr's entire value is that reviewer routing is traceable to the diff and that each reviewer sounds like their role. A run that selects reviewers without showing why, or produces findings that any generic reviewer could write, fails two essential criteria independently — making it impossible to pass golden without fixing both.

**v2 additions**: Round 1 scoring identified two patterns in V-01 that pushed it from 92.5 to 100 vs V-02. Both are added as aspirational criteria: (C-11) Inertia-first sequencing that turns the Advocate's output into a reference object other roles argue against, and (C-12) explicit anti-pattern prohibition in divergence explanations that forces architectural mechanism naming rather than perspective labeling.

**v3 additions**: Round 2 scoring showed C-12 scoring PARTIAL across all five variations — no variation had a comprehensive, enumerated ban list. V-01 had a positive instruction only; V-02 named one prohibited phrase; V-04 named one prohibited phrase with a "do not" framing; none were exhaustive. The first new criterion (C-13) closes this gap: the prohibition must enumerate >=3 banned phrases as a self-auditable checklist, not a general principle. The second new criterion (C-14) makes C-11's reference-object sequencing bidirectional: technical role sections must explicitly anchor at least one finding against the Inertia Advocate's verdict by name, completing the structural loop that C-11 opens.

---

## Essential Criteria (60 pts total)

*(C-01 through C-05 unchanged)*

---

## Recommended Criteria (30 pts total)

*(C-06 through C-08 unchanged)*

---

## Aspirational Criteria (10 pts total)

*(C-09 through C-12 unchanged)*

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| **C-13** | **Perspective-label prohibition is enumerated, not principled** | aspirational | depth | The skill's consensus template contains an explicit, enumerated ban list of >=3 prohibited perspective-label phrases — not a general instruction to "avoid perspective labels." The ban list must be checkable: a reviewer can scan the output against each listed phrase and make a binary pass/fail determination per phrase. A prohibition expressed only as a positive instruction ("name the mechanism") or a single example ("'they prioritize differently' fails") is insufficient — the ban list must enumerate multiple distinct surface forms of the anti-pattern. A run with no divergent findings passes by default. |
| **C-14** | **Each technical role section explicitly anchors at least one finding against the Inertia Advocate's verdict** | aspirational | depth | When the Inertia Advocate is a selected reviewer, each subsequent technical role section must contain at least one finding that names the Inertia Advocate's assessment as the counterpoint — e.g., "IA found the current error-handling sufficient; compiler-lead rates P1 because the new codegen path bypasses the existing guard." The anchor may appear in any finding within the section; it does not need to be F-01. A technical role section with zero IA references fails. A run that does not include the Inertia Advocate as a selected reviewer passes by default. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

*aspirational denominator increased from 4 to 6 in v3; each criterion is worth ~1.67 pts; a perfect run still scores 100.*

---

## What changed from v2

**C-13 closes the C-12 gap.** C-12 was PARTIAL in all five Round 2 variations because each variation expressed the prohibition differently — one positive instruction, one example phrase, one "do not" with a single case. None were mechanically auditable. C-13 makes the ban list a first-class artifact: >=3 enumerated phrases, each independently checkable. A model writing "they see this through different lenses" alongside a mechanism name passes C-12 (mechanism is named) but fails C-13 (banned phrase present).

**C-14 completes C-11's structural intent.** C-11 puts the Inertia Advocate first so technical reviewers have a baseline to argue against. But C-11 only enforces sequencing — it does not require technical roles to actually *use* the baseline. C-14 enforces the other end: each technical section must name the IA's verdict and explain why the role disagrees. Without C-14, C-11 produces a reference object that sits unused; with C-14, the reference object is load-bearing.
ls. |
| C-07 | Per-role finding counts are summarized with severity breakdown | recommended | format | Each role findings section ends with a summary line stating: total findings for that role and the count by severity (e.g., "3 findings: 1 P1, 2 P3"). The summary must appear as a distinct element -- not require the reader to count manually. A run with no per-role summaries fails. A run where summaries appear only in the consensus section and not per-role fails. |
| C-08 | AMEND mode scope is disclosed when run with added reviewer or changed scope | recommended | behavior | When run with an AMEND directive (e.g., "add security-architect", "change scope to compiler only"), output contains a scope disclosure block naming: (a) what was amended, (b) which roles were added or removed, (c) which prior findings are superseded. A run in default mode passes by default. An AMEND run with no scope disclosure fails. |

---

## Aspirational Criteria (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Consensus analysis includes root cause synthesis for role-divergent findings | aspirational | depth | When two or more roles disagree on a finding, the consensus section contains a root cause synthesis stating WHY the roles diverge -- not just that they do. The synthesis must name the structural reason (e.g., "compiler-lead rates P1 because the change affects codegen path; tpm rates P3 because no user-facing behavior changes"). A consensus section that only lists the highest-severity verdict without explaining divergence fails. |
| C-10 | Go/no-go conditions are actionable: each condition names the role responsible for sign-off | aspirational | correctness | When the recommendation is GO WITH CONDITIONS, each condition names: (a) what must be resolved, (b) which role must confirm resolution before merge. A GO WITH CONDITIONS recommendation that lists conditions without named owner roles fails. A GO or NO-GO recommendation passes by default. |
| C-11 | Inertia Advocate is sequenced first among all selected reviewers | aspirational | depth | The Inertia Advocate's findings section appears before all technical role findings sections. This sequencing establishes a status-quo baseline that technical reviewers can explicitly argue against, generating structural divergence rather than pile-on agreement. The Inertia Advocate's findings become a reference object that other roles respond to -- their P1s and P2s are anchored against "Inertia Advocate found this sufficient." A run that places the Inertia Advocate last or in any non-first position fails. A run that does not include the Inertia Advocate as a selected reviewer passes by default. |
| C-12 | Consensus divergence explanations name the architectural mechanism, not a perspective label | aspirational | depth | When the consensus section explains why two roles diverge on a finding, the explanation must name the structural or architectural reason -- not use a perspective-label phrase such as "they have different perspectives," "they prioritize differently," or "their roles lead them to different conclusions." A valid explanation names the mechanism: what property of the code, system, or change causes each role to rate it as they do. A divergence explanation that consists solely of a perspective label with no mechanism fails. A run with no divergent findings passes by default. |
| **C-13** | **Perspective-label prohibition is enumerated, not principled** | aspirational | depth | The skill's consensus template contains an explicit, enumerated ban list of >=3 prohibited perspective-label phrases -- not a general instruction to "avoid perspective labels." The ban list must be checkable: a reviewer can scan the output against each listed phrase and make a binary pass/fail determination per phrase. A prohibition expressed only as a positive instruction ("name the mechanism") or a single example ("'they prioritize differently' fails") is insufficient -- the ban list must enumerate multiple distinct surface forms of the anti-pattern. A run with no divergent findings passes by default. |
| **C-14** | **Each technical role section explicitly anchors at least one finding against the Inertia Advocate's verdict** | aspirational | depth | When the Inertia Advocate is a selected reviewer, each subsequent technical role section must contain at least one finding that names the Inertia Advocate's assessment as the counterpoint -- e.g., "IA found the current error-handling sufficient; compiler-lead rates P1 because the new codegen path bypasses the existing guard." The anchor may appear in any finding within the section; it does not need to be F-01. A technical role section with zero IA references fails. A run that does not include the Inertia Advocate as a selected reviewer passes by default. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

*aspirational denominator increased from 4 to 6 in v3; each criterion is worth ~1.67 pts; a perfect run still scores 100.*

---

## Common Failure Modes

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| -- | C-01 | Reviewer list names three roles with no file mapping; reader cannot determine why security-architect was selected over compiler-lead for the auth module change |
| -- | C-02 | tpm section lists four observations as prose bullets with no P1/P2/P3 label on any of them |
| -- | C-03 | Output ends after the last per-role section; no cross-role synthesis; reader must infer agreement and disagreement from the individual sections |
| -- | C-04 | Recommendation section reads "the team should weigh the P1 findings before merging"; no explicit GO/NO-GO decision |
| -- | C-05 | Security-architect section raises "inconsistent naming conventions" and "missing inline comments" -- findings any reviewer could write; no threat surface, auth, or data handling signal present |
| -- | C-06 | Diff includes changes to `infra/deploy.yaml`; no org.yaml role owns infrastructure; output contains no coverage gap notice |
| -- | C-07 | Each role section ends abruptly after the last finding; reader must count manually to know how many P1s the security role raised |
| -- | C-08 | AMEND adds a compliance reviewer; output shows the new reviewer's findings but never discloses what changed from the prior run or which earlier findings are now superseded |
| -- | C-09 | Compiler-lead rates a type-system change P1; tpm rates it P3; consensus block picks P1 as the winner but does not explain why the two roles diverged |
| -- | C-10 | Recommendation is GO WITH CONDITIONS with three conditions listed; no condition names which role must confirm resolution; the merge gate is ambiguous |
| -- | C-11 | Inertia Advocate is listed as a selected reviewer but their section appears after security-architect and compiler-lead; their status-quo finding cannot function as a baseline because technical objections are already on record |
| -- | C-12 | Consensus notes "compiler-lead and tpm see this differently due to their respective roles"; no mechanism is named; the explanation is indistinguishable from a generic disagreement label and gives the reader nothing actionable |
| -- | C-13 | Consensus template instructs "name the structural reason, not a perspective label" -- one positive instruction, no enumerated ban list; a model can satisfy the positive instruction while still writing "they have different lenses on this problem" alongside a mechanism name; the anti-pattern is not blocked |
| -- | C-14 | Inertia Advocate is selected and sequenced first; compiler-lead section raises three P1s -- none reference the IA's verdict; the reference-object relationship is one-directional and the structural divergence C-11 intended to generate never materializes in the technical sections |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-16 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-16 | Added C-11 (Inertia-first sequencing) and C-12 (mechanism-level divergence explanation) from V-01 Round 1 excellence signals; aspirational denominator updated from 2 to 4 in scoring formula |
| v3 | 2026-03-16 | Added C-13 (enumerated perspective-label ban list) and C-14 (explicit IA counterpoint anchoring in technical sections) from Round 2 excellence signals; C-12 was PARTIAL in all five Round 2 variations -- C-13 closes the gap between positive instruction and self-auditable prohibition; C-14 completes C-11's reference-object sequencing by requiring bidirectional anchoring; aspirational denominator updated from 4 to 6 in scoring formula |
