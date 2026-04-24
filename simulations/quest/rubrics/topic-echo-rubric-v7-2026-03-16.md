Written to `simulations/quest/rubrics/topic-echo-rubric-v7-2026-03-16.md`.

---

Here is the complete updated rubric:

---

# topic:echo Rubric — v7

**Max composite:** 170

---

## Three new criteria from Round 6

**C-22 — Chain-flag progression gate**
(behavior, gate: C-19)

C-19 requires the Chain Integrity Audit to emit CHAIN-COMPLETE or CHAIN-FLAG tokens per entry. C-22 requires the CHAIN-FLAG token to function as a hard gate: any CHAIN-FLAG blocks further production until the flag is resolved. Without a blocking condition, a reviewer can acknowledge CHAIN-FLAG tokens and proceed to completion anyway — the audit is visible but advisory. With a gate, chain integrity failure is a production stop, not an observation. First appeared in Round 6 V-01's PHASE 3B specification ("CHAIN-FLAG blocks progression"); all five Round 6 variations retain it.

**C-23 — Distillation phase blocking condition with named gate**
(behavior, gate: C-20)

C-20 requires a RULES-ANCHORED traceability check confirming tier alignment. C-23 requires that check to name an explicit blocking condition: production cannot proceed to the next phase until all rules show ALIGNED. Without it, the traceability check is advisory — a reviewer can note misalignment and the artifact can still be completed. With a named gate, the distillation layer enforces the same production-stop semantics as C-16 and C-18's per-entry attestation gates. First appeared in Round 6 V-02's PHASE 4B specification ("Do not proceed to Phase 5 until all rules show ALIGNED"); V-03, V-04, V-05 retain it.

**C-24 — Enforcement mechanism section at artifact head position**
(behavior, gate: C-21)

C-21 requires the enforcement mechanism declaration to be in an independently navigable section. C-24 requires that section to be placed at **position 1** of the artifact — before PBI, before Handle Ledger, before any entries. C-21 ensures a reviewer can find the mechanism classification via section headings; C-24 ensures a reviewer who opens the artifact encounters it before any content. Without head positioning the reviewer must navigate to the section; with it, orientation precedes content, making the enforcement frame the first interpretive lens rather than a findable annotation. V-03 and V-05 achieve this; V-01, V-02, and V-04 place the declaration within the PBI section.

---

## Score model

| Tier | Points | Criteria | Per-criterion |
|------|--------|----------|---------------|
| Essential | 60 | 5 | 12 |
| Recommended | 30 | 3 | 10 |
| Aspirational | **80** | **16** | 5 |
| **Max composite** | **170** | | |

**Golden threshold:** All C-01–C-05 pass AND composite >= 80. Unchanged.

---

## What the Round 6 variations score under v7

| Variation | C-22 | C-23 | C-24 | Asp (v7) | Composite | vs v6 |
|-----------|------|------|------|----------|-----------|-------|
| V-01 | **PASS** (CHAIN-FLAG blocks progression) | FAIL (no Rules of Thumb) | FAIL (declaration in PBI section) | 12/16 = 60 | 150 | +5 |
| V-02 | **PASS** (retained from V-01) | **PASS** ("Do not proceed to Phase 5 until all rules show ALIGNED") | FAIL (declaration in PBI section) | 13/16 = 65 | 160 | +10 |
| V-03 | **PASS** (retained) | **PASS** (retained from V-02) | **PASS** (ENFORCEMENT MECHANISM section, position 1) | 16/16 = 80 | **170** | +15 |
| V-04 | **PASS** (same specification as V-01) | **PASS** (same specification as V-02) | FAIL (declaration in PBI section) | 13/16 = 65 | 160 | +10 |
| V-05 | **PASS** (retained) | **PASS** (retained) | **PASS** (ENFORCEMENT MECHANISM section, position 1) | 16/16 = 80 | **170** | +15 |

V-03 and V-05 both reach 170/170 — new gold ceiling for Round 7.

---

**Three key changes from v6:**
- Max composite: 155 → 170 (3 new aspirational criteria, 5 pts each)
- Aspirational criteria: 13 → 16
- New relationships: C-19/C-22 (blocking gate extends chain audit), C-20/C-23 (named gate extends distillation check), C-21/C-24 (head position extends navigability)

---

**Notes on Round 6 pattern:**

The three new criteria follow the same structural pattern as C-19/C-20/C-21 before them: each takes an existing criterion and asks what the *enforcement* version looks like.

- C-19 made the chain audit visible → C-22 makes CHAIN-FLAG a gate (not just a token)
- C-20 made the distillation traceable → C-23 makes RULES-ANCHORED a gate (not just a check)
- C-21 made the mechanism navigable → C-24 makes the section primary (not just findable)

The progression across versions: visibility → navigability → primacy. Each layer converts an advisory signal into an enforcement mechanism.
"We expected X to be negligible; it turned out to dominate" (surprise). |
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

## Aspirational Criteria (weight: 80 points total, 5 pts each)

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
| C-19 | **Post-production chain integrity audit with visible tokens** | behavior | After the artifact is written, a discrete Chain Integrity Audit re-verifies all four chain elements [PBI-Ref, Handle, Source, Verified quotation] for internal consistency. Each entry receives a visible CHAIN-COMPLETE token (or CHAIN-FLAG with description) produced by this audit step. The audit is distinct from the production-time attestation layer (C-16/C-18): C-16/C-18 attest that checks were performed; C-19 confirms those attestations are correct by re-running verification independently. An artifact with C-19 is auditable from output alone -- a reviewer reads CHAIN-COMPLETE and knows the chain was externally validated, not just self-reported. Applicable only when C-18 is satisfied. |
| C-20 | **Impact-anchored distillation layer with traceability verification** | behavior | The artifact includes a Rules of Thumb section encoding the highest-impact surprises in <=20-word quotable form. Each rule carries a tier annotation ([HIGH] or [MEDIUM]) matching its surprise entry; LOW-tier surprises are excluded. After all rules are written, a named traceability check (e.g., RULES-ANCHORED) confirms tier alignment between each rule and its parent surprise entry. Pass requires both: (1) the distillation layer with tier annotations, and (2) the named traceability check confirming alignment. Without the traceability check the distillation is a summary; with it the distillation is an auditable extract of the hierarchy, citable by future teams without re-reading full entries. Applicable only when C-09 is satisfied. |
| C-21 | **Enforcement mechanism declaration in independently navigable section** | behavior | The C-17 enforcement mechanism classification is placed in a discrete headed section or titled table that a reviewer can locate without reading the full artifact. Inline declaration embedded in a PBI preamble, narrative paragraph, or step description does not satisfy C-21 even if it satisfies C-17. Test: can a reviewer jump directly to the enforcement mechanism claim using section headings or table titles alone? If yes, C-21 passes. Applicable only when C-17 is satisfied. |
| C-22 | **Chain-flag progression gate** | behavior | The CHAIN-FLAG token produced by the Chain Integrity Audit (C-19) functions as a hard production gate: any CHAIN-FLAG on any entry blocks further artifact completion until the flag is resolved. Pass requires an explicit blocking condition in the PHASE 3B specification -- a statement that CHAIN-FLAG halts progression, not merely that it is emitted and visible. Without a blocking condition CHAIN-FLAG is advisory; with it chain integrity failure is a production stop that cannot be bypassed by continued writing. Applicable only when C-19 is satisfied. |
| C-23 | **Distillation phase blocking condition with named gate** | behavior | The RULES-ANCHORED traceability check (C-20) names an explicit blocking condition: production cannot proceed to the next phase until all rules show ALIGNED. Pass requires the blocking condition to be stated by name in the phase specification -- not implied by the check's existence. Without a named gate, misaligned tier annotations are observable but non-blocking; a reviewer can note them and the artifact can still be completed. With a named gate, the distillation layer enforces the same production-stop semantics as C-16 and C-18's per-entry attestation gates. Applicable only when C-20 is satisfied. |
| C-24 | **Enforcement mechanism section at artifact head position** | behavior | The C-21 independently navigable section containing the enforcement mechanism declaration is placed at position 1 of the artifact -- before PBI, before Handle Ledger, before any entries. C-21 ensures the section is findable via heading navigation; C-24 ensures a reader who opens the artifact encounters enforcement mechanism classification before any content. Without head positioning a reviewer must navigate to the section; with it, the enforcement frame is the first interpretive lens, not a findable annotation. Pass requires the ENFORCEMENT MECHANISM section (or equivalent titled section) to appear before all other major sections. Applicable only when C-21 is satisfied. |

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
- Aspirational: 80 points total (16 criteria, 5 points each)
- Max composite: 170

### Example score calculation

- Essential: 4/5 pass -> 4/5 * 60 = 48
- Recommended: 2/3 pass -> 2/3 * 30 = 20
- Aspirational: 1/16 pass -> 1/16 * 80 = 5
- **Composite = 73** -- fails golden (essential incomplete), failing overall

### Golden path (baseline)

- Essential: 5/5 -> 60
- Recommended: 2/3 -> 20
- Aspirational: 0/16 -> 0
- **Composite = 80** -- golden (all essential + composite >= 80)

### Golden path (full)

- Essential: 5/5 -> 60
- Recommended: 3/3 -> 30
- Aspirational: 16/16 -> 80
- **Composite = 170** -- maximum

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

**C-18 / C-19**: C-18 is the evidence layer (attestations contain quotations). C-19 is the
audit layer (attestations were re-verified for correctness after production). An artifact can
satisfy C-18 (quotations present and substantive) while failing C-19 (no post-production
verification that the quotations accurately represent the source content). C-19 closes the
final gap in the chain: C-16 confirms checks happened, C-18 shows what was found, C-19
confirms what was found was correctly quoted. The three layers together make the chain
self-auditing without reviewer re-derivation.

**C-19 / C-22**: C-19 requires the Chain Integrity Audit to emit CHAIN-FLAG tokens. C-22
requires those tokens to gate production -- CHAIN-FLAG must halt further completion until
resolved. An artifact can satisfy C-19 (tokens are visible) while failing C-22 (no blocking
condition stated; reviewer can proceed past flags). C-22 converts the audit from a transparency
mechanism into an enforcement mechanism: the audit does not merely report chain state, it
controls whether production continues.

**C-09 / C-20**: C-09 requires a defensible impact hierarchy. C-20 requires the highest-impact
findings from that hierarchy to be distilled into a citable form and verified against the
hierarchy. C-20 cannot be satisfied without C-09 because the tier annotations and traceability
check are meaningless without a proven hierarchy to check against. C-09 produces the hierarchy;
C-20 extracts and verifies a distillation of it.

**C-20 / C-23**: C-20 requires the RULES-ANCHORED check to confirm tier alignment. C-23 requires
that check to name a blocking condition that halts production until alignment is confirmed. An
artifact can satisfy C-20 (check performed, alignment stated) while failing C-23 (no blocking
condition; artifact can be completed with misaligned rules). C-23 makes the distillation layer
structurally equivalent to the entry-level attestation gates (C-16, C-18): the phase cannot
close until the check passes.

**C-17 / C-21**: C-17 is the classification layer (tier, property, implication). C-21 is the
navigability layer (classification is discoverable without full-read). An artifact can satisfy
C-17 at highest level (tier + property + reviewer implication) while failing C-21 (classification
embedded inline). C-21 rewards design for reviewers: the enforcement mechanism claim is
independently auditable without re-parsing the prose. Inline C-17 pass: minimum bar, no C-21.
Dedicated section C-17 + C-21 pass: highest level.

**C-21 / C-24**: C-21 requires the enforcement mechanism section to be independently navigable
(reachable via section headings without full-artifact reading). C-24 requires that section to
be at position 1 -- before PBI, before any entries. An artifact can satisfy C-21 (section
exists and is headed) while failing C-24 (section appears mid-artifact after PBI or entries).
C-24 makes orientation structural rather than navigational: the reader does not choose to find
the enforcement frame -- it is the first thing encountered. The distinction matters for trust
calibration: a reviewer who encounters enforcement mechanism classification before reading any
entries brings a different prior to the content than one who finds it mid-read or after.

---

## Historical criterion notes

**v6 -- three new criteria from Round 5:**

C-19 (behavior, gate: C-18): Post-production Chain Integrity Audit with CHAIN-COMPLETE/CHAIN-FLAG
tokens per entry. Distinct from C-16/C-18 attestation layer: C-19 re-verifies correctness of
attestations after production rather than attesting at production time.

C-20 (behavior, gate: C-09): Rules of Thumb distillation with tier annotations ([HIGH]/[MEDIUM])
and RULES-ANCHORED traceability check. Distillation is auditable extract of hierarchy, not summary.

C-21 (behavior, gate: C-17): Enforcement mechanism declaration in a discrete headed section
independently navigable without full-artifact reading.

**v5 -- two new criteria from Round 4:**

C-17 (correctness, gate: C-15): Artifact classifies its declared enforcement mechanism on the
strength hierarchy (structural > temporal) and states the distinguishing property. C-15 is the
declaration (which mechanism); C-17 is the calibration layer (how strong, and why).

C-18 (behavior, gate: C-16): Each surprise entry's production-time attestation quotes the
actual text of the PBI entry and source finding -- not just their identifiers. C-16 is the
attestation (checks were performed); C-18 is the evidence layer (here is what was checked).

**v4 -- two new criteria from Round 3:**

C-15 (correctness, gate: C-11): Artifact declares how its PBI was isolated from signal
knowledge. Temporal provenance (phase gate freeze) < structural provenance (role-scope
exclusion). Without a mechanism declaration a reviewer must re-derive pre-commitment quality
from content analysis alone.

C-16 (behavior, gate: C-14): Each surprise entry includes a production-time attestation
confirming all three audit pointers were verified before writing. Shifts audit burden from
reviewer obligation (C-14) to producer evidence (C-16).
