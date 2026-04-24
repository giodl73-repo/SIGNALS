Written to `simulations/quest/rubrics/campaign-validate-rubric-v3-2026-03-16.md`.

---

Here's the complete updated rubric:

---

# campaign-validate Rubric — v3

> Updated after R2 scoring (V-01: 107, V-02: 112, V-03: 113, V-04: 113). Three new aspirational
> criteria added from R2 excellence patterns: phase-gate-categorical-separation (C-14),
> rogers-curve-as-completeness-skeleton (C-15), inertia-baseline-as-adoption-anchor (C-16).

---

## Quick Reference

**5 essential** (all must pass for golden):
- **C-01** — All 5 sub-skills represented. Common failure: listen-adoption silently skipped.
- **C-02** — Findings ranked by *adoption impact*, not severity.
- **C-03** — Explicit go/no-go verdict. "It depends" without a condition fails.
- **C-04** — Top 3 blockers attributed to source sub-skill (trivially passes on go verdicts).
- **C-05** — Artifact written to `simulations/{topic}/validate-{date}.md`.

**3 recommended** (needed to reach composite >= 80):
- **C-06** — Cross-signal synthesis. Concatenation fails.
- **C-07** — Per-sub-skill labeled sections.
- **C-08** — Severity tiers (P1/P2/P3), not flat list.

**8 aspirational** (5 pts each):
- **C-09** — Adoption impact quantified: `(segment, ~N%)` format.
- **C-10** — Remediation paths per blocker.
- **C-11** *(v2)* — Table skeleton per sub-skill as completeness gate.
- **C-12** *(v2)* — Adoption Impact as dedicated column, separate from Severity.
- **C-13** *(v2)* — `Artifact written: ...` confirmation string.
- **C-14** *(v3)* — Categorical separation declared for listen-feedback vs listen-adoption.
- **C-15** *(v3)* — All five Rogers segments named with % anchors.
- **C-16** *(v3)* — Status-quo workaround cited per blocker.

**Max: 130. Golden: all essential pass + composite >= 80.**

---

## What changed in v3

| ID | Pattern | What it encodes |
|----|---------|-----------------|
| C-14 | `phase-gate-categorical-separation` | Declares "listen-feedback = pre-ship reaction; listen-adoption = post-ship trajectory — categorically different" as a structural marker at the section boundary, not buried in prose. Strongest C-01 enforcement pattern observed. |
| C-15 | `rogers-curve-as-completeness-skeleton` | All five Rogers segments (innovators ~2.5%, early adopters ~13.5%, early majority ~34%, late majority ~34%, laggards ~16%) as named required entries. Missing segment = absent required row. Also structurally forces C-09: one row per segment requires one % estimate per segment. |
| C-16 | `inertia-baseline-as-adoption-anchor` | Each top blocker names the specific workaround users employ today and the switching cost. "Users do X today; feature requires giving up X because Y." Workaround's user population IS the adoption risk segment — forces C-09 segment identification without a separate enforcement point. |

**Scoring model** updated: aspirational expands from 25 pts (5 criteria) to 40 pts (8 criteria), max composite moves from 115 to 130. Golden threshold unchanged at 80. V-03 top-pattern example added to pass/fail table showing ~125.
, each attributed to the sub-skill that surfaced it. If verdict is go, this criterion passes trivially. |
| C-05 | Artifact written to disk | behavior | Output is written to `simulations/{topic}/validate-{date}.md` following the signal artifact naming convention. File must exist after skill run. |

---

## Recommended Criteria (weight: 30 points total)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Cross-signal synthesis | depth | Brief identifies at least one pattern or tension appearing across 2+ sub-skills (e.g., a usability finding from review-users confirmed by a support-ticket prediction from listen-feedback). Not just a concatenation of sub-skill outputs. |
| C-07 | Per-sub-skill labeled sections | format | Each sub-skill's findings appear under a clearly labeled heading. Reader can navigate directly to review-design findings, listen-adoption findings, etc. without reading the whole document. |
| C-08 | Finding severity differentiation | depth | Findings use consistent severity tiers (P1/P2/P3, blocking/major/minor, or equivalent). High-severity findings visually distinct from low-severity. Not a flat undifferentiated list. |

---

## Aspirational Criteria (weight: 5 points each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Adoption impact quantified per finding | depth | Each ranked finding includes an estimated adoption impact magnitude with segment and %. Format: "(segment, ~N%)" — e.g., "blocks chasm crossing (early majority, ~34%)", "impedes innovators only (~2.5%)". Generic labels ("high impact", "most users") without segment identity and % fail. |
| C-10 | Remediation paths for top blockers | depth | Each top blocker includes a concrete remediation suggestion pointing to a design decision the team can make. Not just "fix this" — specifies what change would resolve the blocker and which sub-skill result supports it. |
| C-11 | Table-format per sub-skill as completeness gate | format | Each sub-skill's findings are presented in a structured table (not prose), so that a missing sub-skill appears as an empty table rather than invisible absent text. The table skeleton is present even if the sub-skill found nothing — making omission detectable, not silent. |
| C-12 | Adoption Impact as dedicated column separate from Severity | format | Severity and Adoption Impact appear as distinct columns or fields in the findings output. A finding can be P3 severity and high adoption impact; the two axes are never merged. This structural separation prevents rank-by-severity errors at the layout level. |
| C-13 | Explicit artifact confirmation string | behavior | After writing the artifact, the skill emits a confirmation line: "Artifact written: simulations/{topic}/validate-{date}.md". The confirmation string is machine-detectable, closing the C-05 verification loop with a positive signal rather than relying on absence of error. |
| C-14 | Categorical separation declared for listen-feedback vs listen-adoption | completeness | Output explicitly declares the categorical distinction between listen-feedback and listen-adoption — not just labels them separately, but names what each covers: listen-feedback as pre-ship customer reaction to the design; listen-adoption as post-ship adoption trajectory by segment. The declaration appears as a structural marker (heading note, gate annotation, or explicit statement) before or at the top of the relevant sections. A merged or unlabeled combined section fails unconditionally. |
| C-15 | All five Rogers segments enumerated by name with % anchors | depth | The adoption analysis (listen-adoption findings) enumerates all five Rogers diffusion segments as named distinct entries: innovators (~2.5%), early adopters (~13.5%), early majority (~34%), late majority (~34%), laggards (~16%). A segment absent from the output is detectable as a missing required entry, not invisible as absent prose. Approximate percentage ranges must be cited — a segment named without a % anchor fails. |
| C-16 | Status-quo workaround cited per blocker | depth | Each top blocker includes a reference to the specific workaround users employ today in the absence of this feature — what keeps them at rest. The citation names the behavior and the switching cost: "Users today do X; this feature asks them to give up X because Y." Generic "users have workarounds" without naming the workaround and cost fails. Inertia is zero without a named status-quo anchor. |

---

## Criterion Notes

**C-01 — all 5 must appear**: A common failure mode is skipping listen-adoption because the
model conflates it with listen-feedback. Pass requires both listen sub-skills visibly present
with distinct content.

**C-02 — adoption impact is the sort key**: Findings ranked by severity alone (P1 first) is
NOT sufficient. The ranking must reflect adoption impact — a P2 finding that blocks the chasm
crossing outranks a P1 cosmetic issue.

**C-04 — trivial pass on go**: If the brief reaches a go verdict, C-04 passes automatically.
The criterion only activates on no-go or "go with conditions" outcomes.

**C-06 — synthesis vs concatenation**: The brief fails C-06 if it simply lists Section 1 =
review-design output, Section 2 = review-users output, etc. Synthesis means drawing a
connection across sections: "X surfaced in review-users is confirmed by Y in listen-feedback."

**C-10 — remediation as structured column (EX-2)**: The strongest implementations embed
remediation inside the blocker table as a dedicated column, not as separate prose. When
remediation is a column, every row demands a cell — the structure forces completeness.
Prose remediation sections pass C-10 but risk being skipped; columnar remediation is the
preferred pattern (see V-02 vs V-01 in R1 scoring).

**C-11 — table skeleton forces completeness (EX-1)**: The criterion is met when the table
structure is pre-defined with sub-skill labels as row or section headers, so a skipped
sub-skill produces a visibly empty table rather than no table at all. V-02 demonstrated this:
"table-per-sub-skill structure makes omission visually obvious as a blank table."

**C-12 — orthogonal axes (EX-3)**: The column separation communicates the distinction at the
layout level, before any cell is read. A finding ranked P3 severity / high adoption impact is
correctly ranked higher than a P1 cosmetic — but only if the reader can see both dimensions.
Merged fields (e.g., "P2 — high adoption impact" in one cell) pass C-08 but fail C-12.

**C-13 — confirmation as detection signal (EX-4)**: The confirmation string is not just
informational — it is a detectable artifact. Automated scoring and pipeline validation can
grep for "Artifact written:" to confirm the write step executed without inspecting the
filesystem. This closes the loop on C-05 with a positive signal.

**C-14 — categorical separation prevents listen merge (R2 pattern: phase-gate-categorical-separation)**:
The strongest C-01 implementations do not merely label the two sections differently — they
declare the categorical distinction before each section so the content-generator understands
the sections serve different analytical purposes. V-03 achieved this with phase gates:
"listen-feedback is about pre-ship customer reaction to the design, not the adoption
trajectory. Do not merge this section with Phase 5." and "listen-adoption is categorically
different from listen-feedback. Each row must contain distinct content from Phase 4." This
gate makes the separation structural, not advisory. A note buried in prose fails; a gate
annotation at the section boundary passes.

**C-15 — Rogers skeleton forces adoption completeness (R2 pattern: rogers-curve-as-completeness-skeleton)**:
Naming all five Rogers segments as required entries achieves C-11 for the adoption sub-skill
specifically: a segment missing from the output is an absent required row, not invisible
absent text. It also structurally forces C-09 compliance — one entry per segment requires one
adoption impact estimate per segment, preventing generic "most users" quantification. V-03's
Phase 5 demonstrated this: all five segment rows were pre-declared with named % anchors,
making any missing segment detectable as an absent row.

**C-16 — inertia anchor forces segment identification (R2 pattern: inertia-baseline-as-adoption-anchor)**:
Naming the status-quo workaround per blocker does more than explain why the blocker matters —
it structurally identifies the user population at risk. The workaround's current users ARE the
adoption risk segment. A blocker without a named workaround is a blocker without a named
segment, which makes C-09 quantification impossible at that finding. V-02's inertia framing
demonstrated this: "inertia comparison (why it keeps users in their workaround)" as a required
field forced segment identification automatically, without a separate C-09 enforcement point.

---

## Scoring Model

| Tier | Criteria | Points | Max |
|------|----------|--------|-----|
| Essential | C-01 through C-05 | 12 pts each | 60 |
| Recommended | C-06 through C-08 | 10 pts each | 30 |
| Aspirational | C-09 through C-16 | 5 pts each | 40 |
| **Total** | | | **130** |

Golden: all 5 essential pass + composite >= 80.
Composite > 100 is achievable when all recommended + majority of aspirational criteria pass.

---

## Example Pass/Fail Patterns

| Pattern | Essential | Recommended | Composite | Golden? |
|---------|-----------|-------------|-----------|---------|
| All 5 sub-skills, go verdict, ranked findings, synthesis | 5/5 | 3/3 | 100 | YES |
| Missing listen-adoption, rest good | 4/5 | 3/3 | 78 | NO — C-01 fails |
| All 5 present, findings NOT ranked by adoption impact | 4/5 | 2/3 | 72 | NO — C-02 fails |
| All 5, ranked, verdict present, blockers listed, no synthesis | 5/5 | 1/3 | 70 | NO — composite < 80 |
| All 5, ranked, verdict, blockers, synthesis, severity tiers | 5/5 | 3/3 | 100 | YES |
| V-02 pattern: tables + columns + confirmation + remediation col | 5/5 | 3/3 + C-09/C-10/C-12/C-13 | 112 | YES |
| V-03 pattern: phase gates + Rogers rows + inertia anchors | 5/5 | 3/3 + C-09/C-10/C-11(partial)/C-12/C-13/C-14/C-15(partial)/C-16 | ~125 | YES |
| Full v3 pattern: all aspirational | 5/5 | 3/3 | 130 | YES |
