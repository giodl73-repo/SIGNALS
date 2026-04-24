Looking at the Round 2 scorecard for new excellence patterns not already captured in C-01–C-12:

**V-02 (91 pts)** shows two distinct signals beyond existing criteria: (1) gates are ordered with verdict propagation — Gate 1 null hypothesis verdict gates all downstream work, not just "lifecycle coverage"; (2) the disposition code is derived from gate algebra, not asserted editorially — "gate pass/fail count → READY/CONDITIONAL/BLOCKED, not editorial."

**V-03 and V-04** both show a temporal bracket pattern — an adversarial/challenger reviewer speaks before domain testimony AND after, preventing domain findings from displacing the null hypothesis frame. Neither C-07 nor C-12 captures this; both check presence of null hypothesis framing, not structural bracketing.

That yields three new criteria: **C-13** (gate sequencing with verdict propagation), **C-14** (disposition derivation by stated algebra), **C-15** (adversarial wrap / bracket architecture).

Scoring rebalance: aspirational expands from 4×5 pts to 7×4 pts = 28 pts; essential adjusts to 72 pts; total stays at 100; golden threshold (80) unchanged.

---

```markdown
# org-review Rubric — v3

> Version history: v1 (baseline) → v2 (C-11 disposition code, C-12 null
> hypothesis anchor per role) → v3 (C-13 gate sequencing, C-14 disposition
> algebra, C-15 adversarial bracket).

---

## Scoring Summary

| Block        | Criteria   | Points          | Total |
|--------------|------------|-----------------|-------|
| Essential    | C-01–C-08  | ~9 pts each     | 72    |
| Aspirational | C-09–C-15  | 4 pts each      | 28    |
| **Total**    |            |                 | **100** |

**Golden threshold: 80 / 100**
Aspirational criteria can never rescue a failing essential block; a variation
that scores 0 on C-01 cannot reach 80 regardless of aspirational points.

---

## Essential Criteria (C-01–C-08) — 72 pts

### C-01 — Role Coverage (~9 pts)
All three review archetypes are present: **domain expert** (technical
authority on the artifact class), **lifecycle stakeholder** (PM / program
owner who will commit), and **inertia-advocate** (challenger whose default
position is "don't build"). The role set is explicit — reviewers are named
or labeled, not implicit.

*Fails if:* any archetype is absent, or reviewer roles are unlabeled.

---

### C-02 — Artifact Scope (~9 pts)
The review explicitly enumerates the artifact surface under review: spec,
design, feasibility, competitive context, technical constraints, and any
prior decisions that would be invalidated. Nothing material falls outside
the stated scope.

*Fails if:* scope is undefined, or artifacts are discovered mid-review
without scope amendment.

---

### C-03 — Per-Reviewer Findings with Severity (~9 pts)
Each reviewer produces a distinct findings block that includes at least one
finding with an explicit severity label (HIGH / MEDIUM / LOW). Findings are
not pooled into a shared list; each reviewer owns their findings.

*Fails if:* findings are aggregated across reviewers, or severity labels are
absent from any finding.

---

### C-04 — Severity Semantically Anchored (~9 pts)
Severity labels carry commit-gate semantics:
- **HIGH** = this finding blocks commitment to build
- **MEDIUM** = this finding conditions commitment (requires remediation before
  proceeding)
- **LOW** = this finding is advisory; commitment may proceed

Strongest implementations define these semantics explicitly in the review
preamble. A severity label that appears without this mapping is unanchored
and scores PARTIAL.

*Fails if:* severity labels are present but carry no defined commit-gate
meaning, or are used purely qualitatively (e.g., "important" vs "minor").

---

### C-05 — Lifecycle Coverage (~9 pts)
The review is structured to cover the full decision lifecycle: pre-build
(context / null hypothesis check), build decision (domain artifact review),
and post-build readiness (synthesis / disposition). All three stages must
be named or implied by structure. A snapshot review that covers only one
stage scores PARTIAL.

*Fails if:* the review addresses only the current artifact state with no
acknowledgment of what came before or what must follow.

---

### C-06 — Action Items (~9 pts)
The review produces a concrete action list: items that must be resolved
before commitment (BLOCKED items), items that must be resolved as conditions
(CONDITIONAL items), and optional items (advisory). Each action item is
traceable to a finding.

*Fails if:* the review produces a verdict without actionable resolution
paths, or action items are not traceable to findings.

---

### C-07 — Null Hypothesis Framing (~9 pts)
The review explicitly frames the build question as a null hypothesis:
"the default is not to build; evidence must defeat inertia." The null
hypothesis is stated before domain evidence is weighed, not introduced
retrospectively to justify a predetermined conclusion.

*Fails if:* the review frames the question as "reasons to build vs. concerns"
rather than "evidence defeating the assumption that we should not build."

---

### C-08 — Summary Exists (~9 pts)
The review closes with an explicit synthesis that integrates all reviewer
findings into a single narrative. The summary must reference the null
hypothesis verdict and the disposition. A collection of reviewer blocks
without synthesis does not satisfy C-08.

*Fails if:* no integrating summary is present, or the summary is a
mechanical restatement of individual scores without synthesis.

---

## Aspirational Criteria (C-09–C-15) — 4 pts each

Aspirational criteria reward structural excellence beyond the essential
baseline. PARTIAL credit (2 pts) is awarded when the intent is present but
the mechanism is incomplete.

---

### C-09 — Conflict Detection (4 pts)
The review surfaces explicit disagreements between reviewers on the same
finding or dimension. Conflicts are named, not smoothed. Strongest
implementations quantify divergence (e.g., numeric gap between reviewer
scores on a shared dimension). A review in which all reviewers agree scores
PARTIAL on C-09 unless consensus is explicitly noted as a signal.

---

### C-10 — Reviewer Independence (4 pts)
Reviewer perspectives are structurally separated so that one reviewer's
findings cannot anchor another's before both have committed to a position.
Acceptable mechanisms: parallel-blind protocol (reviewers submit without
seeing others' work), phase-separated assignment (each reviewer owns a
distinct gate), or bracket architecture (challenger reviewer is isolated
from domain testimony in time). Sequential reviews with shared visibility
score PARTIAL unless an explicit independence mechanism is named.

---

### C-11 — Disposition Code Output (4 pts)
The review emits an explicit machine-readable code as its final output:
**READY**, **CONDITIONAL**, or **BLOCKED**. The code is not buried in
narrative; it appears as a labeled output. This transforms the review from
an opinion into a commit gate. Distinct from C-08 (which only requires a
summary): C-11 requires the code to be emitted as a distinct field.

---

### C-12 — Null Hypothesis Anchor per Role (4 pts)
Each reviewer's findings include an explicit act/don't-act stance from their
own frame — not just domain observations. The PM anchors on decision
sufficiency; the architect anchors on technical justification; the
inertia-advocate anchors on workaround viability. A domain finding that does
not resolve to a build stance from that reviewer's frame scores PARTIAL.
Distinct from C-07 (which requires the null hypothesis to be framed for the
review as a whole): C-12 requires every role to individually close the loop.

---

### C-13 — Gate Sequencing with Verdict Propagation (4 pts)
**New in v3. Signal: V-02 (91 pts).**

The review is structured as ordered gates in which each gate's verdict is
visible to — and explicitly referenced by — downstream gates. The null
hypothesis check occupies **Gate 1**; a Gate 1 verdict of "null holds"
renders all downstream gates advisory only (domain findings cannot override
an undefeated null). A review with lifecycle stages that are independent
and non-referencing scores PARTIAL.

Distinct from C-05 (lifecycle coverage): C-05 requires stages to exist;
C-13 requires verdict propagation between them — upstream verdicts
structurally constrain downstream conclusions.

*Strongest implementation (V-02):* Four explicit gates; each gate's
pass/fail/conditional output is the input state for the next gate.

---

### C-14 — Disposition Derivation by Stated Algebra (4 pts)
**New in v3. Signal: V-02 (91 pts).**

The READY / CONDITIONAL / BLOCKED code is derived from gate or verdict
counts by a rule that is stated explicitly within the review structure
itself — not asserted editorially. The derivation rule must be auditable
without reference to reviewer judgment (e.g., "any gate FAIL → BLOCKED;
any gate CONDITIONAL → CONDITIONAL; all gates PASS → READY"). The code is
a function of the review's own outputs, not the reviewers' interpretation
of them.

Distinct from C-11 (disposition code exists): C-11 requires the code to be
emitted; C-14 requires the code to be derived by a stated algorithm.
A review that emits CONDITIONAL without a stated derivation rule scores
PASS on C-11 but FAIL on C-14.

*Strongest implementation (V-02):* Gate pass/fail count drives disposition
automatically; no editorial override is possible.

---

### C-15 — Adversarial Bracket (Wrap Architecture) (4 pts)
**New in v3. Signals: V-03 (83 pts), V-04 (86 pts).**

An inertia-advocate or challenger reviewer occupies two structural positions:
(1) an **opening stance** before domain testimony — establishing the null
hypothesis baseline that domain evidence must defeat; and (2) a **closing
verdict** after all domain findings — rendering a final judgment on whether
the null hypothesis has been defeated.

This bracket prevents domain testimony from displacing the null hypothesis
frame through accumulation. Without a closing bracket, a strong domain
consensus can implicitly override an undefeated null. A review with a
challenger who appears only at the end (challenger-last only) scores
PARTIAL; a review with a challenger only at the start scores PARTIAL.
Full credit requires both positions.

Distinct from C-07 (null hypothesis framing exists) and C-12 (per-role null
anchoring): C-15 requires *temporal structural separation* — the challenger
must speak before domain reviewers commit their findings and again after all
domain findings are complete.

*Strongest implementation (V-04):* Inertia bracket Round 1 (before domain
review) + Round 2 (after domain review); domain reviewers write inside the
bracket and cannot see the closing inertia verdict while writing.

---

## Version Notes

### v3 changes (this version)
- **C-13 added** (gate sequencing with verdict propagation): V-02 showed
  that lifecycle stages that propagate verdicts outperform stages that are
  merely labeled — the null hypothesis gate structurally gates all
  downstream work.
- **C-14 added** (disposition derivation by stated algebra): V-02 showed
  that a disposition code derived by an auditable rule is categorically
  stronger than one asserted editorially; C-11 alone does not capture this.
- **C-15 added** (adversarial bracket): V-03 and V-04 both showed challenger
  reviewers producing higher null hypothesis coverage when they bracket
  domain testimony — appearing before and after, not only at the end.
- **Scoring rebalanced**: Aspirational block expands from 4×5 pts to 7×4 pts
  (28 pts total); essential block adjusts to 72 pts. Total: 100.
  Golden threshold (80) unchanged.

### v2 changes
- C-11 added (disposition code READY/CONDITIONAL/BLOCKED)
- C-12 added (null hypothesis anchor per role)
- C-04 tightened (semantic anchoring guidance strengthened)
- Aspirational rebalanced from 2×10 pts to 4×5 pts

### v1 baseline
- C-01–C-08 essential criteria
- C-09 conflict detection, C-10 reviewer independence (aspirational)
```
