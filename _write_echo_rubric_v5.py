path = 'C:/src/sim/simulations/quest/rubrics/topic-echo-rubric-v5-2026-03-16.md'

rubric = """\
# topic:echo Rubric -- v5

**Skill:** `topic:echo`
**Version:** 5
**Date:** 2026-03-16
**Max composite:** 140

---

## Changelog

**v5 -- two new criteria extracted from Round 4 scoring differentials:**

**C-17 -- Enforcement mechanism strength classification with calibration rationale**
(correctness, applicability gate: C-15)

The Round 4 scorecard revealed that C-15 splits on whether the mechanism declaration includes
a strength tier and rationale. V-01/V-04 scored PASS on C-15 with a freeze label that named
the mechanism type but did not classify it on the strength hierarchy or explain why it earned
that tier. V-03/V-05 scored above the C-15 bar: each provided a dedicated Pre-Commitment
Provenance section that named the mechanism type, placed it in the strength hierarchy
(structural > temporal), and stated the property that determines tier membership. V-05 added
the further precision "enforced by role sequencing, not by instruction." C-17 captures this
second tier: the artifact must not only declare which mechanism was used (C-15) but must
classify it on the strength hierarchy and explain why. Without the tier and rationale, a
reviewer who does not already know the hierarchy must reason from first principles to calibrate
their trust in C-13; with both, calibration is immediate.

**C-18 -- Per-entry attestation with evidentiary quotation**
(behavior, applicability gate: C-16)

The Round 4 scorecard revealed that C-16 splits on whether the verification attestation quotes
the actual texts being verified. V-02/V-04 scored PASS on C-16 with a Verified field that
named each check individually. V-05 scored above the C-16 bar: the Verified field additionally
quoted the attested text inline ("(2) PBI-Ref PB-NN confirmed; entry reads: ...; (3) Source
{artifact} confirmed; finding reads: ..."). C-18 captures this third tier: the per-entry
attestation must quote the actual PBI entry text and source finding text, not just name their
identifiers. Without quotation, a reviewer must navigate to the PBI section and signal artifact
to confirm the cited identifiers point to the right content; with quotation, the attestation
is self-contained and confirmable from the entry alone.

**Score model update:** Aspirational 40 pts (8 criteria) -> 50 pts (10 criteria, 5 pts each).
Max composite: 130 -> 140. Golden threshold unchanged (all essential pass AND composite >= 80).
Example calculations and golden path examples updated to reflect 10 aspirational criteria.

**New relationship entries:**
- C-15 / C-17: C-17 extends C-15 by requiring the declared mechanism to also be classified on
  the strength hierarchy with a rationale. C-15 is the declaration (which mechanism); C-17 is
  the calibration layer (how strong, and why).
- C-16 / C-18: C-18 extends C-16 by requiring the per-entry attestation to quote the actual
  texts being verified, not just name their identifiers. C-16 is the attestation (checks were
  performed); C-18 is the evidence layer (here is what was checked).

---

**v4 -- two new criteria extracted from Round 3 scoring differentials:**

C-15 (correctness, gate: C-11): Artifact declares how its PBI was isolated from signal
knowledge. Temporal provenance (phase gate freeze) < structural provenance (role-scope
exclusion). Without a mechanism declaration a reviewer must re-derive pre-commitment quality
from content analysis alone.

C-16 (behavior, gate: C-14): Each surprise entry includes a production-time attestation
confirming all three audit pointers were verified before writing. Shifts audit burden from
reviewer obligation (C-14) to producer evidence (C-16).

---

## Essential Criteria (weight: 60 points total, 12 pts each)

All five must pass. If any essential criterion fails, the output is not useful.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Named surprises present** | correctness | At least one surprise is named as a discrete item. A surprise is not a finding -- it must be framed as something unexpected: the output must make clear what was anticipated and why the actual result departed from it. A list of findings without surprise framing fails entirely. NOT: "We found that X matters" (finding). PASS: "We expected X to be negligible; it turned out to dominate" (surprise). |
| C-02 | **Signal tracing per surprise** | correctness | Every named surprise is traced to a specific source signal or artifact by name. Generic attribution is insufficient. Each surprise must name the artifact that produced it. A surprise without a traceable source cannot be audited by the next team and fails. |
| C-03 | **Design impact assessed per surprise** | depth | Every named surprise carries an explicit assessment of its impact on design direction. Impact may be confirming, redirecting, or destabilizing. An impact statement that does not identify which design decision is affected fails. "This changes things" without naming what changes is insufficient. |
| C-04 | **Synthesis not summary** | behavior | The artifact contains only surprises and their analysis. Expected findings are either absent or explicitly marked as context-only. An artifact that enumerates findings and labels some "interesting" fails -- the surprise/expected partition must be explicit and structural. |
| C-05 | **Surprise specificity** | correctness | Each surprise is specific to this investigation's signal set, not a generic observation that could appear in any investigation. "APIs are harder to design than expected" fails -- it applies universally. "The scout:competitors signal revealed that all three competitors treat X as a solved problem, contrary to our assumption that the space was unsolved" passes -- it is falsifiable against this investigation's artifacts. |

---

## Recommended Criteria (weight: 30 points total, 10 pts each)

Output is better with these. Golden typically requires at least 2 of 3.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Expectation counterfactual** | depth | Each surprise explicitly names what was expected versus what was found. The counterfactual structure is stated, not implied. A reader new to the topic can reconstruct the prior assumption from the surprise entry alone, without consulting the underlying signal artifacts. Surprises that omit the expected-state half are incomplete. |
| C-07 | **Institutional framing** | behavior | The artifact is explicitly addressed to a future team. At least one element signals forward-facing intent: surprises framed as things the next team would not predict, a closing note naming what to investigate first, or an opening institutional purpose declaration. An artifact that reads as a personal retrospective without forward framing fails. |
| C-08 | **Cross-signal pattern identification** | coverage | If two or more surprises share an underlying cause or implication, that relationship is named with a statement of what they have in common and what that implies for design. If all surprises are genuinely independent, the output explicitly states this. Omitting pattern analysis when multiple surprises exist is a fail. |

---

## Aspirational Criteria (weight: 50 points total, 5 pts each)

Raise the bar once essential and recommended criteria are stable.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Surprise hierarchy by design impact** | depth | Surprises are ranked by design impact with an explicit rationale that is argued, not asserted. A ranked list without argument is insufficient -- the hierarchy must be defensible to a reader who disagrees with it. |
| C-10 | **Riskiest surprise flagged** | behavior | The single surprise most likely to invalidate a core assumption is explicitly flagged. The flag names the assumption at risk, the signal that revealed it, and what would need to be true for the assumption to hold despite the surprise. |
| C-11 | **Pre-committed prior belief inventory** | correctness | The artifact contains a Prior Belief Inventory produced before signal reading -- a discrete, labeled section predating surprise entries. Each surprise entry references a specific PB entry by identifier. Minimum bar: (a) discrete PBI section exists, (b) entries are addressable by identifier, (c) each surprise cites a specific PBI entry by that identifier. |
| C-12 | **Named surprise handles** | behavior | Each surprise carries a short named handle (2-5 words) specific enough to be cited by future signal artifacts without re-reading the echo. Test: could a teammate say "remember the [handle] surprise?" and be unambiguously understood? "API complexity surprise" fails. "competitor-treated-X-as-solved" passes. |
| C-13 | **Dual phase-locked pre-commitment integrity** | correctness | The PBI and Handle Ledger are demonstrably independent -- PBI entries use belief language; Handle Ledger titles use finding language specific to what signals revealed. Independence fails if a PBI entry names a handle label by its final form, or a Handle Ledger title echoes PBI entry language verbatim. Applicable only when both C-11 and C-12 are satisfied. |
| C-14 | **Single-entry audit trail completeness** | behavior | Each surprise entry contains all three pointers enabling provenance verification without consulting other sections: (1) Handle Ledger title, (2) PBI identifier, (3) source signal artifact. All three checks possible from the entry alone. Applicable only when both C-11 and C-12 are satisfied. |
| C-15 | **Pre-commitment enforcement mechanism declaration** | correctness | The artifact declares how its PBI was isolated from signal knowledge. A timestamped freeze declaration provides temporal provenance. A role-scope declaration provides structural provenance. Without a mechanism declaration a reviewer must infer pre-commitment quality from content analysis alone -- making C-13 independence unverifiable without re-deriving it from scratch. Note: temporal < structural because a phase gate sequences but does not block cross-phase reasoning. Applicable only when C-11 is satisfied. |
| C-16 | **Production-time per-entry verification attestation** | behavior | Each surprise entry includes an explicit statement confirming all three audit pointers were verified at production time: (1) handle confirmed in Handle Ledger, (2) PBI-Ref confirmed at cited identifier, (3) source artifact confirmed in signal set. An attestation naming each check explicitly is a pass; a generic "verified" without naming what was verified fails. Applicable only when C-14 is satisfied. |
| C-17 | **Enforcement mechanism strength classification with calibration rationale** | correctness | The artifact classifies its declared enforcement mechanism on the strength hierarchy (structural > temporal) and states the property that earns that classification. Pass bar requires two elements: (a) tier label stated ("structural provenance" or "temporal provenance"), and (b) the distinguishing property explained -- structural provenance is enforced by role-scope exclusion (the PBI-writing role cannot access signal artifacts regardless of instruction); temporal provenance is enforced by phase sequencing (phases are ordered but cross-phase reasoning is not blocked). Declaring "structural provenance" without explaining why it is structural rather than temporal fails C-17. Stating tier, distinguishing property, and reviewer implication ("independence is enforced, not instructed; C-13 content analysis is confirmatory rather than probative") passes at the highest level. Applicable only when C-15 is satisfied. |
| C-18 | **Per-entry attestation with evidentiary quotation** | behavior | Each surprise entry's production-time attestation quotes the actual text of the PBI entry and source finding being attested -- not just their identifiers. Pass condition: the Verified field quotes substantive text for both -- the actual belief statement and the relevant finding sentence -- sufficient to confirm that cited identifiers point to the right content. A fragment too short to confirm correct citation fails; a quoted sentence that uniquely identifies the prior belief and the finding passes. Converts the attestation from a declaration of action (checks were performed) into a disclosure of evidence (here is what was checked). Applicable only when C-16 is satisfied. |

---

## Scoring Reference

| Result | Condition |
|--------|-----------|
| Golden | All C-01 through C-05 pass AND composite >= 80 |
| Passing | All essential pass, composite < 80 |
| Failing | Any essential criterion fails |

### Score weights

- Essential: 60 points total (5 criteria, 12 points each)
- Recommended: 30 points total (3 criteria, 10 points each)
- Aspirational: 50 points total (10 criteria, 5 points each)
- Max composite: 140

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 1/10 pass -> 1/10 * 50 = 5
- **Composite = 73** -- fails golden (essential incomplete), failing overall

### Golden path (baseline)

- Essential: 5/5 -> 60
- Recommended: 2/3 -> 20
- Aspirational: 0/10 -> 0
- **Composite = 80** -- golden (all essential + composite >= 80)

### Golden path (full)

- Essential: 5/5 -> 60
- Recommended: 3/3 -> 30
- Aspirational: 10/10 -> 50
- **Composite = 140** -- maximum

---

## Criterion Relationships

**C-01 / C-04**: C-01 requires at least one named surprise with departure framing. C-04 requires
the artifact to contain only surprises -- no unsegregated summary content. Both must pass together:
an artifact can have named surprises (C-01) while burying them in a summary (C-04 fail).

**C-02 / C-05**: C-02 requires tracing to a named source artifact. C-05 requires specificity to
this investigation. An artifact can cite a specific source (C-02 pass) but describe a generic
observation not derived from that source content (C-05 fail).

**C-06 / C-07 tension**: C-06 is oriented backward (reconstructing the prior state). C-07 is
oriented forward (addressing the next team). An artifact that does both anchors the surprise in
history and projects it into the future.

**C-09 / C-10**: C-09 requires ranking all surprises. C-10 requires flagging the most dangerous
one. C-09 can be satisfied without C-10, and C-10 without C-09.

**C-06 / C-11**: C-06 requires the expected-X-found-Y structure per entry. C-11 requires the
expected state to have been committed before signal reading via a discrete PBI. C-06 can be
satisfied post-hoc; C-11 cannot. C-11 automatically satisfies C-06 but not the reverse. C-11
is the structural enforcement of what C-06 asks for rhetorically.

**C-01 / C-12**: C-01 requires named surprises with departure framing. C-12 requires each
surprise to also carry a reusable handle citable by future artifacts. C-05 and C-12 reinforce
each other: a specific surprise is easier to name concisely.

**C-11 + C-12 / C-13**: C-13 is inapplicable if either C-11 or C-12 is absent. Given both,
C-13 tests whether the two pre-commitments are genuinely independent or co-constructed. PBI
entries must use belief language; Handle Ledger titles must use finding language that PBI
entries could not have anticipated.

**C-13 + C-14**: C-13 tests independence between sections (macro level). C-14 tests integration
within entries (micro level). Satisfying both establishes the pre-commitments are independent
at macro and composable at micro.

**C-11 / C-15**: C-11 is the structural minimum (PBI section exists, is addressable). C-15 is
the provenance layer (the isolation mechanism is declared and legible). An artifact can satisfy
C-11 while failing C-15 (no declaration of phase gate vs role boundary). With C-15 satisfied
the enforcement mechanism is stated; without it the reviewer must infer quality from content
analysis alone.

**C-13 / C-15**: C-13 tests independence via content evidence (language analysis). C-15 tests
independence via mechanism evidence (provenance declaration). Both target genuine pre-commitment
through different lenses. The strongest artifacts satisfy both: mechanism was sound (C-15) and
content confirms it (C-13).

**C-14 / C-16**: C-14 is the structural requirement (three pointers present). C-16 is the
evidence layer (pointers were checked at production time, not just present). Satisfying both
shifts audit burden from reviewer to producer and makes the audit chain both genuine and legible.

**C-15 / C-17**: C-15 is the identification layer (which mechanism). C-17 is the calibration
layer (how strong, and why). An artifact can satisfy C-15 (mechanism named) while failing C-17
(no tier, no distinguishing property). C-17 exists because a mechanism name alone requires a
reviewer to independently know the hierarchy to calibrate; a mechanism name plus tier plus
rationale makes calibration self-contained. Practical test: can a reviewer unfamiliar with the
hierarchy immediately know how much weight to place on the independence claim? C-15 alone: no.
C-15 + C-17: yes.

**C-16 / C-18**: C-16 is the attestation layer (checks were performed; here are their
identifiers). C-18 is the evidence layer (here is what was found at those identifiers). An
artifact can satisfy C-16 (Verified field names all three checks with identifiers) while failing
C-18 (no quotation of actual attested text). Without quotation a reviewer must navigate to PBI
and signal artifact to confirm identifiers point to the right content. With quotation, both
confirmations are possible from the entry alone. C-18 completes the self-containment goal:
the full evidentiary chain -- pointers, attestation, and actual texts -- is visible at the
surprise entry without navigation.
"""

with open(path, 'w') as f:
    f.write(rubric)
print('written', len(rubric), 'bytes to', path)
