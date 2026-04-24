# org-review Rubric — v2
**Updated**: 2026-03-15 (from Round 1 scorecard)
**Changes from v1**: C-04 pass condition tightened with semantic anchoring insight from V-04.
Two new aspirational criteria added (C-11, C-12) from Round 1 excellence signals.
Aspirational tier rebalanced: 4 criteria × 5 pts each = 20 pts (total unchanged at 100).

The toughest criterion to pass is C-03 — most LLM runs produce reviewers that echo each
other. That is the real discriminator between a genuine org-review and a shallow pass.

---

## Essential Criteria (weight: 50 pts total)

### C-01 — Role Selection
**Category**: correctness
**Weight**: essential

Reviewers must be drawn from the role registry at `.roles/signal/`, not invented
on the fly. An invented role has no lens file — its verify questions, simplify principles,
and expertise domain are undefined, making its findings unreproducible and unverifiable.

**Pass condition**: Every reviewer named in the output has a corresponding file in
`.roles/signal/`. The output must enumerate the registry before selecting roles —
either explicitly or by reference. No role may appear that lacks a registry file.

---

### C-02 — Review Matrix Structure
**Category**: correctness
**Weight**: essential

Every reviewer entry must contain all four fields: **role**, **findings**, **severity**,
**recommendation**. The review matrix is the contract of this skill — missing any field
makes the output structurally incomplete and unsuitable for decision-making.

**Pass condition**: Every reviewer entry has all four fields present and non-empty.
A table, list, or structured section form all satisfy this — structure is flexible,
field completeness is not.

---

### C-03 — Perspective Fidelity
**Category**: correctness
**Weight**: essential

Each role must review from its own orientation: verify questions, simplify lens, and
expertise domain drawn from its role file. A PM finding must not read like an architect
finding. Homogeneous findings signal the reviewer personas were not actually applied.

**Pass condition**: Findings from at least two distinct roles are substantively different
in framing and concern. The PM's findings address decision/inertia/commitment concerns;
the architect's findings address technical feasibility/boundary/complexity concerns;
the inertia-advocate's findings stress-test the null hypothesis. Roles must not echo
each other's framing verbatim.

---

### C-04 — Severity Classification
**Category**: correctness
**Weight**: essential

Severity must be meaningful — not every finding can be HIGH and not every finding can
be LOW. The classification scheme must be consistent (same vocabulary across all
reviewers) and non-uniform across findings so the output actually guides prioritization.

**Pass condition**: At least two distinct severity levels appear across the review.
Severity labels use consistent vocabulary (e.g., HIGH/MEDIUM/LOW or critical/major/minor).
Not all findings share the same severity level. Strongest implementations anchor severity
to commitment impact: HIGH = blocks commitment, MEDIUM = conditions commitment,
LOW = advisory (does not block).

---

### C-05 — Depth Flag Behavior
**Category**: behavior
**Weight**: essential

`--depth deep` runs all roles in the registry. Standard depth filters to roles relevant
to the artifact type. These two modes must produce observably different reviewer sets
when applied to the same artifact — otherwise the flag is cosmetic.

**Pass condition**: When both modes are described or demonstrated on the same artifact,
deep produces more reviewer entries than standard. If only one mode is run, the output
explicitly states which mode was used and the reviewer count is consistent with that mode
(standard: subset; deep: all available roles).

---

## Recommended Criteria (weight: 30 pts total)

### C-06 — Verify Questions Present
**Category**: depth
**Weight**: recommended

The skill description calls out verify questions as an explicit output dimension.
Each reviewer should ask at least one clarifying or verification question from their
lens — this surfaces assumptions the artifact makes that may not hold.

**Pass condition**: At least 50% of reviewers include at least one verify question
in their section. Questions should be grounded in the reviewer's verify lens
(e.g., PM asks about commitment threshold; architect asks about contract-to-implementation
match; inertia-advocate asks what the team does today instead).

---

### C-07 — Simplify Lens Applied
**Category**: depth
**Weight**: recommended

The skill description lists simplify as a distinct reviewer lens alongside verify and
expertise. Each reviewer should surface at least one simplification principle or
reduction observation — what could be removed, collapsed, or clarified.

**Pass condition**: At least one simplify-framed statement per reviewer. The statement
should align with that role's simplify principles (e.g., PM: "if the signal doesn't
change what we build, it wasn't worth gathering"; architect: "if you can't hand-compile
the spec, you can't implement it").

---

### C-08 — Aggregated Cross-Role Summary
**Category**: coverage
**Weight**: recommended

Individual reviewer entries are useful; a synthesized view is essential for decision-making.
The output should conclude with a summary that identifies where reviewers agree, where they
diverge, which artifact areas are most at risk, and what the overall signal is.

**Pass condition**: An aggregated summary section is present. It references findings from
at least two different roles. It identifies at least one area of reviewer agreement or
divergence. It does not simply repeat individual findings.

---

## Aspirational Criteria (weight: 20 pts total — 5 pts each)

### C-09 — Cross-Role Conflict Detection
**Category**: depth
**Weight**: aspirational

When two roles give contradictory recommendations on the same artifact element — e.g.,
PM says "commit now" and inertia-advocate says "the workaround is sufficient" — the output
should flag the conflict explicitly rather than silently presenting both views.

**Pass condition**: When a genuine cross-role contradiction exists, the output names it
as a conflict, identifies which roles are in tension, and states what decision the reader
must make to resolve it. If no contradiction exists in the artifact, this criterion is
N/A (does not penalize).

---

### C-10 — Area Coverage for Deep Runs
**Category**: coverage
**Weight**: aspirational

The five Signal org areas (evidence, discovery, quality, adoption, platform) each have
distinct concerns. A full `--depth deep` run on a multi-namespace artifact should draw
at least one reviewer from each area so no org function is invisible.

**Pass condition**: For `--depth deep` on an artifact touching 3+ namespaces,
at least one reviewer from each of the five org areas (evidence, discovery, quality,
adoption, platform) is included in the review matrix. Pass is N/A for single-namespace
artifacts or standard depth runs.

---

### C-11 — Disposition Code Output
**Category**: actionability
**Weight**: aspirational
**Added**: v2, from Round 1 excellence signals (V-02, V-04)

The aggregated summary should emit a single machine-readable disposition code —
READY, CONDITIONAL, or BLOCKED — that transforms the review from an opinion document
into an actionable commit-gate signal. Without a disposition code, the reader must
infer a commit decision from prose; with one, the signal is unambiguous.

**Definitions**:
- **READY** — evidence supports commitment; no blocking findings present
- **CONDITIONAL** — commitment is viable contingent on named condition(s) being met
- **BLOCKED** — at least one genuine blocker exists that must be resolved before commitment

**Pass condition**: The output includes exactly one of READY / CONDITIONAL / BLOCKED as
a named disposition code, accompanied by a one-sentence rationale that names the
highest-severity finding driving that disposition. The code must appear in the
aggregated summary, not buried in a reviewer entry.

---

### C-12 — Null Hypothesis Anchoring per Role
**Category**: correctness
**Weight**: aspirational
**Added**: v2, from Round 1 excellence signals (V-03)

Each reviewer's findings should include an explicit position on whether the artifact
justifies action over the status quo, framed from that role's lens. This is distinct
from C-03 (perspective fidelity), which checks that roles use different frames — C-12
checks that every role's frame is anchored to the build/don't-build question, not just
to domain concerns. A PM finding that never addresses commitment sufficiency, or an
architect finding that never addresses whether the technical approach is warranted, has
drifted from the artifact's core question.

**Pass condition**: At least two reviewer sections include an explicit act/don't-act
or build/don't-build stance, each expressed from that role's perspective. The stances
must differ — one role's null-hypothesis position must not simply echo another's phrasing.
PM frame: "is the decision evidence sufficient to commit?"; architect frame: "does the
technical approach justify the complexity over the status quo?"; inertia-advocate frame:
"does the current workaround still hold?".

---

## Scoring Reference

| Tier | Criteria | Pts per criterion | Max pts |
|------|----------|------------------|---------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 10 (pass) / 5 (partial) / 0 (fail) | 50 |
| Recommended | C-06, C-07, C-08 | 10 (pass) / 5 (partial) / 0 (fail) | 30 |
| Aspirational | C-09, C-10, C-11, C-12 | 5 (pass) / 2 (partial) / 0 (fail) | 20 |
| **Total** | | | **100** |

**Golden threshold**: All 5 essential pass + composite >= 80.

Example: 5/5 essential + 2/3 recommended + 1/4 aspirational
= (5 * 10) + (2 * 10) + (5 * 1) = 50 + 20 + 5 = **75** — below threshold.

Example: 5/5 essential + 3/3 recommended + 0/4 aspirational
= 50 + 30 + 0 = **80** — passes at threshold.
