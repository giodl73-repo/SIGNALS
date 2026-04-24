Written to `simulations/quest/golden/campaign-validate-golden-2026-03-16.md`.

Key decisions made:
- Used the **simplified prompt body** (simplification PASS, 25% reduction)
- Dashes in prompt body converted to `--` (ASCII-safe per project rules)
- The five "what made it golden" patterns pulled from structural decisions that drove the high rubric scores: code-first sequencing, skeleton enforcement, impact/severity decoupling, listen categorical split, remediation-as-column

The two open gaps in the rubric (C-18 switching-cost, C-19 row-level blanks) are documented in the criteria summary but not artificially patched — the score of 155 reflects what the prompt actually earns.
tness of contracts, edge-case
handling, schema constraints, performance implications, and hard blockers
to shipment. Label all findings P1 (blocker), P2 (significant), or P3 (minor).
For every P1 finding, name the status-quo workaround users currently rely on.

---

PHASE 2 -- review-design

Analyze the design for: internal consistency, alignment with prior spec signals,
conceptual integrity, and adherence to platform conventions. Rate each finding
by its adoption impact (not its severity).

---

PHASE 3 -- review-users

Analyze the user experience for: task completion clarity, friction points,
cognitive load, and discoverability. For each finding, estimate the user segment
most affected: innovators, early adopters, early majority, late majority,
or laggards. Weight your finding's adoption-impact score accordingly.

---

PHASE 4 -- listen-feedback

Synthesize existing feedback signals (interviews, support tickets, prior research).
Distinguish feedback from adoption posture: feedback is what users said; adoption
posture is what that implies about their switching readiness. Do not collapse these.

---

PHASE 5 -- listen-adoption

Apply the Rogers diffusion model. For each segment, estimate whether the design
would unlock or block adoption. Name the single biggest friction per segment.

---

OUTPUT FORMAT

Write your validation brief in this structure:

## Sub-Skill Results

For each of the five sub-skills, write a labeled section:
### review-code | review-design | review-users | listen-feedback | listen-adoption
Include a table skeleton per sub-skill:
| Finding | Severity | Affected Segment | Adoption Impact |
Even if empty, the table must appear (confirmed-empty if no findings).
Adoption Impact and Severity are separate columns -- do not merge them.

## Ranked Findings

Rank all findings across all five sub-skills by adoption impact (not severity).
Adoption impact = estimated % of user base for whom this finding is a friction
or blocker at or before the early-majority crossing.

Format:
| Rank | Finding | Source Sub-Skill | Severity | Adoption Impact (segment, ~N%) |

## P1 Blockers and Remediation

List all P1 findings. For each:
| Blocker | Source Sub-Skill | Status-Quo Workaround | Remediation Path |

Remediation paths belong in this table as a required column.
Do not move remediation into the verdict section prose.

## Cross-Signal Synthesis

Name at least 3 relationships that are not visible in any single sub-skill alone.
Each row must name a relationship that only emerges when two or more sub-skills
are read together.

| Signal A | Signal B | Emergent Relationship (not visible in either alone) |

## Rogers Readiness

| Segment | ~% | Adoption Status | Primary Blocker |
Name all five segments. Include % anchors.

## Verdict

State one of: GO / NO-GO / CONDITIONAL GO (condition: [specific, actionable]).
"It depends" without a named condition is not a valid verdict.

---

After writing the brief, write the artifact to:
  simulations/{{topic}}/validate-{{date}}.md

Confirm with: `Artifact written: simulations/{{topic}}/validate-{{date}}.md`
```

---

## What Made It Golden

**1. review-code anchors the sequence**
Running `review-code` first establishes a hard technical floor before UX and adoption
signals layer in. Code-level blockers surface early and are never buried inside the
adoption narrative. The remaining sub-skills build on a known-stable foundation rather
than discovering blockers retroactively.

**2. Table skeletons as structural completeness enforcement**
Requiring a `| Finding | Severity | Affected Segment | Adoption Impact |` table per
sub-skill -- even if confirmed-empty -- makes absent content a visible blank rather than
a silent prose omission. The author cannot skip a sub-skill without leaving an obvious
structural gap. This generalizes C-19 to the sub-skill level.

**3. Adoption-impact ranking decoupled from severity**
Ranked Findings sorts by adoption impact (segment, ~N%), not by P1/P2/P3. Adoption
Impact and Severity appear as separate columns in every table -- never merged. This
surfaces findings that block the early-majority crossing even when they are not
severity-P1, which is the actual decision-relevant signal.

**4. Categorical separation of listen-feedback vs listen-adoption**
Phase 4 explicitly defines the boundary: "feedback is what users said; adoption posture
is what that implies about their switching readiness." Collapsing these into one signal
is prohibited inline. This prevents the common failure mode where listen-adoption is
silently satisfied by quoting support tickets.

**5. Remediation as a required column, not verdict prose**
The P1 Blockers table has `Remediation Path` as a required column with an explicit
prohibition: "do not move remediation into the verdict section prose." Every P1 blocker
receives a path by construction -- not only those the author chose to narrate -- satisfying
C-22 and partially C-18.

---

## Rubric v5 -- Criteria Summary

**Max: 160. Golden: all essential pass + composite >= 80.**

### Essential (12 pts each -- all must pass)

| ID | Criterion |
|----|-----------|
| C-01 | All 5 sub-skills represented (review-code, review-design, review-users, listen-feedback, listen-adoption). Silent omission or review-customers substitution fails unconditionally. |
| C-02 | Findings ranked by adoption impact, not severity. |
| C-03 | Explicit GO / NO-GO / CONDITIONAL GO verdict. "It depends" without a named condition fails. |
| C-04 | Top blockers attributed to source sub-skill. |
| C-05 | Artifact written to `simulations/{topic}/validate-{date}.md`. |

### Recommended (10 pts each)

| ID | Criterion |
|----|-----------|
| C-06 | Cross-signal synthesis present. Concatenation fails. |
| C-07 | Per-sub-skill labeled sections. |
| C-08 | Severity tiers P1/P2/P3, not a flat list. |

### Aspirational (5 pts each)

| ID | Criterion |
|----|-----------|
| C-09 | Adoption impact quantified: `(segment, ~N%)` format. |
| C-10 | Remediation paths per blocker. |
| C-11 | Table skeleton per sub-skill as completeness gate. |
| C-12 | Adoption Impact as dedicated column, separate from Severity. |
| C-13 | `Artifact written: ...` confirmation string. |
| C-14 | Categorical separation declared for listen-feedback vs listen-adoption. |
| C-15 | All five Rogers segments named with % anchors. |
| C-16 | Status-quo workaround cited per P1 blocker. |
| C-17 | Schema designed so one decision satisfies a criterion cluster. |
| C-18 | Switching-cost comparison encoded as required columns, not prose. |
| C-19 | Required rows pre-declared so absent content is a visible blank. |
| C-20 | Synthesis encoded as a dedicated table with per-row anti-concatenation rule. |
| C-21 | One table per analytical concern; no two concerns share a table. |
| C-22 | Remediation paths as a required column in blockers table, not verdict-section prose. |
