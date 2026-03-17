`listen-adoption-rubric-v11-2026-03-14.md` is written. Here's what changed:

---

**Three new elevation candidates from R10 — C-31, C-32, C-33. Max 200 → 215.**

**C-31 — Spread mechanism table uses named transition-pair row labels as structural slots** (5 pts)
From: C-07 V-02/V-03 PARTIAL. V-02/V-03 used phase-body questions covering one transition contextually; V-01/V-04/V-05 used TABLE 3 with four named rows (Innovator → EA, EA → EM, EM → LM, LM → Laggard). Distinct from C-07 (existence check) and C-28 (label constraint): C-31 tests whether named row keys enforce per-transition coverage structurally rather than via instruction compliance. Phase-body question fails C-31 regardless of contextual coverage. Four named rows pass C-31. Fails automatically if C-07 fails.

**C-32 — Correction mechanism presence anchor in document body** (5 pts)
From: C-19 V-02/V-04/V-05 PARTIAL (paradox of strength persists beyond C-30). C-30 proves the audit ran via SECTION K stamps; it does not prove the correction mechanism was armed in the body. C-32 requires either a triggered CORRECTION BLOCK (BEFORE + AFTER) or a "CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered" declaration in the document body before SECTION K. Perfect compliance + SECTION K stamps + no body anchor = FAIL. Mechanism-armed declaration = PASS without a failure occurring. Fails automatically if C-18 fails.

**C-33 — Answer-form enforcement co-present with correction mechanism anchor** (5 pts)
From: No R10 variation simultaneously passes C-13/C-14/C-19/C-29. Answer-form (C-29) suppresses C-19; fill-form allows C-19 but fails C-29. C-32 breaks the paradox for answer-form designs. C-33 is the composition criterion: C-29 and C-32 must be co-present — the only architecture that achieves PASS on all four simultaneously. Fails automatically if either C-29 or C-32 fails.
(C-19 V-02/V-04/V-05 PARTIAL — paradox of strength persists beyond C-30; C-30
proves the audit ran via per-gate execution stamps in the terminal section, but does not
prove the correction mechanism was armed and available in the document body) is elevated as
C-32. It is a distinct observable output property: the document either contains a
correction-mechanism presence anchor — an inline CORRECTION BLOCK triggered by a gate
failure (containing BEFORE and AFTER fields, satisfying C-19 directly) or an explicit
"CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered" declaration placed in the
document body before SECTION K — or it relies on terminal-section gate state entries alone
to prove mechanism availability. C-19 tests whether corrected content is visible as a
triggered CORRECTION BLOCK; C-20 tests whether gate states are consolidated in a terminal
section; C-30 tests whether the terminal section records per-gate execution stamps; C-32
tests whether the correction mechanism itself is proven present in the document body,
independent of whether any gate failed. A document with perfect compliance, SECTION K
per-gate stamps satisfying C-30, and no correction mechanism anchor of any form in the body
fails C-32 because the mechanism's availability is unproven in the body. A document with at
minimum one inline CORRECTION BLOCK passes C-32 because the mechanism was proven to fire; a
document with a "CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered" declaration
before SECTION K passes C-32 because the mechanism is proven present even without firing.
C-32 fails automatically if C-18 fails.

Signal 3 (no single R10 variation simultaneously passes C-13, C-14, C-19, and C-29 —
answer-form enforcement satisfies C-29/C-13/C-14 while suppressing C-19 by producing high
gate-pass rates that prevent CORRECTION BLOCK from firing; fill-form satisfies C-19 while
failing C-29/C-13/C-14 because enforcement is instructional rather than architectural; C-32
resolves the C-19 paradox for answer-form designs; the composition of C-29 and C-32
co-present in the same document is the only architecture that achieves all four
simultaneously) is elevated as C-33. It is a distinct observable output property: the
document either uses answer-form questions as the citation-enforcement mechanism (satisfying
C-29) and contains a correction-mechanism presence anchor (satisfying C-32) — the only
structural combination that achieves PASS on C-13, C-14, C-29, and C-32 simultaneously —
or it trades off one mechanism against the other. C-33 does not introduce new structural
requirements beyond C-29 and C-32; it tests whether those two mechanisms are co-present in
the same document, closing the trade-off gap that prevents any single-mechanism architecture
from satisfying the full criterion set. A document that passes C-29 and fails C-32 fails
C-33; a document that passes C-32 and fails C-29 fails C-33; a document that passes both
C-29 and C-32 passes C-33 regardless of whether any other criterion fails. C-33 fails
automatically if either C-29 or C-32 fails.

---

## Criteria

**C-01 â€” All 16 roles mapped to canonical Rogers archetypes** (12 pts)
An explicit role-to-archetype table with all 16 roles assigned to one of the five canonical
Rogers archetypes (Innovator, Early Adopter, Early Majority, Late Majority, Laggard). No role
omitted. No archetype invented. Pass condition: table is present and complete.

**C-02 â€” Month-by-month adoption sequence ordered by Rogers archetypes** (12 pts)
A PHASE 1â€“6 structure spanning at least 6 months with archetypes assigned in Rogers order
(Innovators first, Laggards last). Phase 3 (Chasm) explicitly marked as a non-adoption crossing
event, not an archetype phase. Pass condition: phase sequence and month labeling are present and
correctly ordered.

**C-03 â€” Chasm section present with crossing diagnosis** (12 pts)
A dedicated chasm section that diagnoses the early-majority crossing challenge: what defends the
incumbent's position among the late majority, what bridge condition must hold, and what early
signal confirms the chasm has been crossed. Pass condition: chasm section present with all three
elements.

**C-04 â€” Champion network section present with named roles** (12 pts)
A dedicated champion network section naming at least three specific roles (by title or archetype)
who are positioned to advocate for adoption and displace the incumbent. Pass condition: champion
section present with named roles and adoption rationale per role.

**C-05 â€” Intervention ranking section present** (12 pts)
A dedicated section ranking retention interventions by impact on adoption velocity. Ranking must
reference at least two phases and two named roles. Pass condition: section present with
multi-phase, multi-role ranking.

**C-06 â€” Churn risk register with named trigger and mitigation per entry** (10 pts)
A structured churn register in which every entry contains (a) a named reversion trigger â€” the
specific condition that would cause a role to revert to the incumbent â€” and (b) a mitigation.
Pass condition: register present; no entry lacks a named trigger and at least one mitigation.

**C-07 â€” Spread mechanism named per phase transition** (10 pts)
An explicit spread mechanism named per phase transition (Innovatorâ†’Early Adopter,
Early Adopterâ†’Early Majority, etc.). The mechanism must be feature-specific â€” a named signal,
artifact, or social proof event â€” not a generic description such as "word of mouth" or
"organic growth." Pass condition: mechanism present per transition; all mechanisms are
feature-specific.

**C-08 â€” Tabular or structured month view with scannable phase headers** (10 pts)
Phase headers that include the month range and archetype name, formatted so the adoption
timeline is scannable without reading the body text. Pass condition: headers present for all
phases; month ranges are explicit.

**C-09 â€” Sensitivity analysis with two named scenarios** (5 pts)
A sensitivity analysis â€” table or equivalent â€” with at least two named scenarios (e.g.,
Fast Adoption and Slow Adoption) and at least one named lever that shifts the outcome between
scenarios. Pass condition: two named scenarios and at least one named lever present.

**C-10 â€” Signal readiness feedback loop with threshold and interpretation** (5 pts)
A readiness table mapping named signals to adoption thresholds and interpretations. Each row
must contain: the signal name, the threshold value or condition, and the interpretation
(what it means for adoption timing). Pass condition: table present; all rows complete.

**C-11 â€” Named inertia IDs assigned per Rogers archetype** (5 pts)
Named inertia identifiers (I-01 through I-05 or equivalent) assigned one per canonical
archetype, with the inertia described as the structural reason that archetype resists adoption.
Pass condition: five IDs assigned, one per archetype, each with a named inertia description.

**C-12 â€” No orphan sections** (5 pts)
Every named criterion that generates content has a dedicated structural slot in the document.
No criterion depends on content embedded in another criterion's section. Pass condition: all
C-09 and C-10 slots present as dedicated sections; no criterion is satisfied by content found
only in another criterion's section.

**C-13 â€” Named inertia IDs cited as downstream backbone** (5 pts)
The named inertia IDs from C-11 are cited by ID (e.g., I-03) in at least four downstream
locations: bridge conditions, intervention rationale, champion rationale, and churn register
entries. Pass condition: all four downstream location types contain at least one ID citation.
Aspirational. H gate corrects misses.

**C-14 â€” Champion rationale double-anchored to archetype bridge and inertia ID** (5 pts)
Each champion entry contains two separate anchors: (a) the archetype-bridge rationale â€” why
this role's archetype position makes it an effective adoption champion â€” and (b) the named
inertia ID (from C-11) that this champion is positioned to overcome, cited by ID. Pass
condition: both anchors present per champion entry. Aspirational. I gate corrects misses.

**C-15 â€” Churn register mitigations are concrete retention actions** (5 pts)
Every mitigation in the churn register is a concrete retention action â€” something a team does
to reduce reversion probability â€” rather than a surveillance or monitoring flag (e.g., "track
usage" or "monitor engagement" fails this criterion). Pass condition: no entry contains only a
surveillance flag as its mitigation. Aspirational. J gate corrects misses.

**C-16 â€” Self-audit section for C-13, C-14, and C-15 present** (5 pts)
Dedicated gate sections H (C-13 audit), I (C-14 audit), and J (C-15 audit) are present,
named, and explicitly reference the criterion being audited by ID. Pass condition: all three
gate sections present with criterion-ID references.

**C-17 â€” Dedicated structural slot per aspirational criterion** (5 pts)
Each aspirational criterion (C-13, C-14, C-15) has its own named gate section that is
structurally separate from the content section it audits. Pass condition: H, I, J are separate
named sections; none is embedded inside a content section.

**C-18 â€” Revision obligation on gate fail** (5 pts)
Each gate section (H, I, J) contains an explicit revision obligation: if the gate fails, a
CORRECTION BLOCK must be produced immediately before proceeding. The obligation must be stated
in imperative form within the gate section itself. Pass condition: revision obligation
explicitly stated in all three gate sections.

**C-19 â€” Corrected content visible in output as inline CORRECTION BLOCK** (5 pts)
At least one inline CORRECTION BLOCK â€” containing a BEFORE field and an AFTER field â€” appears
in the document body above the terminal section. Pass condition: CORRECTION BLOCK with both
fields present and inline (not in the terminal section). Aspirational in architecturally strong
variations where all gates pass on first attempt; see C-30 for the complementary criterion and
C-32 for the mechanism-presence criterion.

**C-20 â€” Gate states consolidated in a single terminal section** (5 pts)
A single named terminal section (SECTION K or equivalent) consolidates the initial gate result,
revision performed (yes/no), CORRECTION BLOCK location (section reference), and final gate
result for all three gates (H, I, J). Pass condition: all four fields present per gate in a
single terminal section.

**C-21 â€” Corrected content excluded from terminal section** (5 pts)
The terminal section records gate outcomes only. No CORRECTION BLOCK content â€” no BEFORE or
AFTER fields â€” appears in the terminal section. Pass condition: terminal section contains no
BEFORE or AFTER fields.

**C-22 â€” Terminal section contains a self-verifying invariant** (5 pts)
The terminal section contains an explicit invariant stating the consistency condition that the
terminal section itself must satisfy: for every "Revision Performed: Yes" entry, a CORRECTION
BLOCK with BEFORE and AFTER content must exist earlier in the document at the cited location.
Pass condition: invariant present and states the consistency condition in verifiable form.

**C-23 â€” Named verification boundary separates content generation from audit** (5 pts)
A "## VERIFICATION MODE" header or equivalent explicitly marks the boundary between content
generation and the audit stage. No audit content appears before the boundary; no content
generation appears after it. Pass condition: named boundary present; audit sections (H, I, J, K)
all appear after it.

**C-24 â€” Invariant names its own falsification condition** (5 pts)
The terminal section invariant states an explicit failure mode: the specific condition that
would falsify the invariant (e.g., "a Yes row whose CORRECTION BLOCK Location references a
section containing no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field,
falsifies this invariant"). Pass condition: falsification condition present and specific.

**C-25 â€” Phase headers enforce Rogers sequence architecturally** (5 pts)
The document uses PHASE 1 INNOVATORS through PHASE 6 LAGGARDS as structural section headers,
with PHASE 3 CHASM explicitly marked as a non-adoption crossing event. The Rogers sequence is
structurally enforced by header names, not merely instructed in a preamble. Pass condition:
all six phase headers present with correct Rogers labeling; PHASE 3 marked as non-adoption.

**C-26 â€” Incumbent-first displacement framing names THE INCUMBENT before archetype
assignment** (5 pts)
Source: V-04's opening structure, which explicitly names the current workflow or tool being
displaced (THE INCUMBENT) before beginning archetype assignment, then runs all phase bodies
through the displacement lens â€” asking "what does this phase do to THE INCUMBENT's position?"
rather than "what does this phase predict for {{topic}}?" This framing surfaces role-specific
inertia and reversion risk without requiring named ID cross-references, because every phase
already inherits the displacement lens: chasm diagnosis names what defends THE INCUMBENT's
position among the late-majority, champion rationale explains which roles are willing to displace
it, churn triggers identify what would cause reversion to it, and retention interventions name
what would prevent that reversion. C-01 tests whether all roles are mapped to the five canonical
Rogers archetypes; C-26 tests whether the simulation is structured as a displacement story from
its first named element, with THE INCUMBENT explicitly identified as the thing being displaced.
A correctly ordered adoption timeline without displacement framing passes C-02; a correctly
populated role-to-archetype table without displacement framing passes C-01; neither passes C-26.
C-26 fails automatically if C-01 fails.

**C-27 â€” Churn register field label encodes the concrete-action constraint at generation
time** (5 pts)
Source: V-04's PART 3 churn register, which uses the field label "Retention intervention: [one
concrete action that reduces reversion probability]" rather than a generic "Mitigation:" label
augmented by a separate instruction or downstream audit prohibiting surveillance-only entries.
When the positive constraint is embedded in the field label itself â€” "[one concrete action]" â€”
the model must write an action because that is what fits the slot; the constraint is enforced at
generation time rather than caught after the fact. C-06 tests that the churn register is present
and that each entry contains a named trigger and at least one mitigation; C-15 tests that the
mitigation is a concrete retention action rather than a surveillance or monitoring flag; C-27
tests whether the field label itself makes a separate instruction or downstream audit unnecessary
â€” the constraint is verifiable by reading the label alone, before reading any mitigation entry.
A churn register with a "Mitigation" label and a bracketed prohibition in an instruction block
passes C-06 and may pass C-15 depending on what the model wrote, but fails C-27 because the
constraint is not in the label. A churn register whose label reads "Retention intervention:
[one concrete action that reduces reversion probability]" passes C-27 regardless of whether any
separate instruction exists. C-27 fails automatically if C-06 fails.

**C-28 â€” Spread mechanism slot label encodes the specificity constraint at generation
time** (5 pts)
Source: V-02 PARTIAL on C-07 â€” the spread mechanism column existed in TABLE 3 but the column
header was a generic "Spread Mechanism" label without the inline constraint, reducing generation-
time pressure for feature-specific entries. The excellence seen in other R9 variations is that
the spread mechanism slot label itself embeds the constraint: "Spread Mechanism: [named signal
or artifact â€” not generic word-of-mouth]." When the constraint is in the label, a model
writing "word-of-mouth" cannot do so without violating the slot's own type; when the constraint
is in a separate instruction, the model can satisfy the slot structurally while violating the
constraint semantically. C-07 tests whether a named spread mechanism exists per transition;
C-28 tests whether the slot label makes generic entries structurally incompatible at generation
time â€” same elevation class as C-27. A spread mechanism column labeled "Spread Mechanism" that
produces feature-specific entries passes C-07 but fails C-28; the constraint is not in the
label and cannot be verified by reading the label alone. A spread mechanism column labeled
"Spread Mechanism: [named signal or artifact â€” not generic word-of-mouth]" passes C-28
regardless of whether any separate instruction exists. C-28 fails automatically if C-07 fails.

**C-29 â€” Inertia ID citations enforced by answer-form phase-header questions** (5 pts)
Source: V-04 PASS on C-13 and C-14 vs. PARTIAL for all other R9 variations â€” V-04's phase
headers ask "Which Named Inertia ID is driving the chasm?" and "Named Inertia ID this champion
is positioned to overcome (from SECTION B â€” cite I-0X)" as mandatory phase-body fields, making
ID citation the answer to a question rather than the value of a fill-form field. Instructions
require the citation as a field value and permit omission at the cost of a compliance miss;
questions require the citation as the coherent answer and make omission syntactically
incomplete. C-11 tests whether named inertia IDs exist per archetype; C-13 tests whether IDs
are cited in downstream locations; C-14 tests whether champion rationale is double-anchored;
C-29 tests whether the enforcement mechanism for those citations is answer-form (phase-header
question whose answer must be an inertia ID) rather than fill-form (field instruction requiring
an inertia ID citation). A document that passes C-13 and C-14 via fill-form field instructions
fails C-29 because the enforcement is instructional rather than architectural. A document whose
phase headers ask "Which Named Inertia ID is driving the chasm?" passes C-29 regardless of
whether any separate citation instruction exists. C-29 fails automatically if C-11 fails.

**C-30 â€” Terminal section contains per-gate execution stamps regardless of correction
outcome** (5 pts)
Source: V-04 PARTIAL on C-19 â€” "Paradox of strength": V-04's phase-header architecture
produces the highest generation-time compliance for C-13 and C-14, meaning gates H and I are
most likely to pass on first attempt, meaning no CORRECTION BLOCK fires, meaning C-19 (requires
at least one visible CORRECTION BLOCK) paradoxically fails in the strongest variation. The gap
is that the terminal section records gate states only when a correction was triggered, leaving
the no-correction case unverifiable: a terminal section with no entries is indistinguishable
from a terminal section whose gates were never evaluated. The excellence criterion is: the
terminal section must contain a per-gate execution stamp for every gate evaluated, including
explicitly recording "PASS â€” no correction triggered" or equivalent for gates that passed on
first attempt. C-16 tests whether a self-audit section exists; C-18 tests whether revision is
obligated on fail; C-19 tests whether corrected content is visible; C-20 tests whether gate
states are in a terminal section; C-30 tests whether the terminal section is self-sufficient as
proof of audit execution â€” complete regardless of whether any correction fired. A terminal
section recording only failures has no entry for a passing gate and fails C-30 because the
passing case is unverified. A terminal section recording "H: PASS â€” no correction triggered |
I: PASS â€” no correction triggered | J: PASS â€” no correction triggered" passes C-30 regardless
of whether any CORRECTION BLOCK appears elsewhere. C-30 fails automatically if C-20 fails.

**C-31 — Spread mechanism table uses named transition-pair row labels as structural
slots** (5 pts)
Source: V-02/V-03 PARTIAL on C-07 — both variations addressed spread mechanism through
phase-body questions rather than TABLE 3, producing contextual coverage of one transition
while leaving the other three without dedicated structural slots. V-01, V-04, and V-05
passed C-07 via TABLE 3 with explicit named rows for each transition pair
(Innovator → Early Adopter, Early Adopter → Early Majority, Early Majority → Late
Majority, Late Majority → Laggard), making per-transition omission structurally
incompatible with completing the table. C-07 tests whether a named spread mechanism exists
per transition; C-28 tests whether the slot label embeds the specificity constraint inline;
C-31 tests whether the table structure itself enforces per-transition coverage via named
transition-pair row keys — whether coverage is enforced by structural slot count (four named
rows requiring four entries) rather than by instruction compliance (a question that
contextually encourages multi-transition coverage without requiring it syntactically). A
spread mechanism embedded in a phase-body question fails C-31 regardless of how many
transitions it addresses contextually, because the remaining transitions have no structural
slot and no generation-time pressure. A table with four rows labeled with the four canonical
transition pairs passes C-31 regardless of whether any separate per-transition instruction
exists, because completing the table requires a spread mechanism entry for each named row.
C-31 fails automatically if C-07 fails.

**C-32 — Correction mechanism presence anchor in document body proves mechanism
availability** (5 pts)
Source: V-02/V-04/V-05 PARTIAL on C-19 — the paradox of strength persists beyond C-30:
C-30 proves the audit ran via per-gate execution stamps in SECTION K, but does not prove
the correction mechanism was armed and available in the document body. A document that
achieves perfect gate compliance has no triggered CORRECTION BLOCK, making the mechanism's
existence in the document body unverifiable from any terminal-section entry alone. The
excellence criterion is: the document must contain a correction-mechanism presence anchor —
either an inline CORRECTION BLOCK triggered by a gate failure (containing BEFORE and AFTER
fields, satisfying C-19 directly) or an explicit "CORRECTION BLOCK MECHANISM ARMED — no
gate failure triggered" declaration placed in the document body before SECTION K, proving
the mechanism was present and available regardless of gate outcomes. C-19 tests whether
corrected content is visible as a triggered CORRECTION BLOCK; C-20 tests whether gate
states are consolidated in a terminal section; C-30 tests whether the terminal section
records per-gate execution stamps; C-32 tests whether the correction mechanism itself is
proven present in the document body, independent of whether any gate failed. A document
with perfect compliance, SECTION K per-gate stamps satisfying C-30, and no correction
mechanism anchor of any form in the body fails C-32 because the mechanism's availability
is unproven in the body. A document with at minimum one inline CORRECTION BLOCK passes
C-32 because the mechanism was proven to fire; a document with a "CORRECTION BLOCK
MECHANISM ARMED — no gate failure triggered" declaration before SECTION K passes C-32
because the mechanism is proven present even without firing. C-32 fails automatically if
C-18 fails.

**C-33 — Answer-form citation enforcement co-present with correction mechanism
anchor** (5 pts)
Source: No single R10 variation simultaneously passes C-13, C-14, C-19, and C-29 —
answer-form enforcement (V-02, V-04, V-05) satisfies C-29/C-13/C-14 while suppressing
C-19 by producing high gate-pass rates that prevent CORRECTION BLOCK from firing; fill-form
enforcement (V-01, V-03) satisfies C-19 by producing medium gate-pass rates that allow
correction blocks to fire, while failing C-29/C-13/C-14 because enforcement is
instructional rather than architectural. C-32 resolves the C-19 paradox for answer-form
designs by replacing proof-by-execution (C-19) with proof-by-declaration-or-execution
(C-32): an answer-form design that also contains a "CORRECTION BLOCK MECHANISM ARMED"
declaration satisfies C-32 without requiring any gate to fail. C-33 tests whether the
answer-form citation mechanism (C-29) and the correction mechanism anchor (C-32) are
co-present in the same document — the only structural combination that achieves PASS on
C-13, C-14, C-29, and C-32 simultaneously, breaking the trade-off that prevented any
single R10 variation from holding all four. C-33 does not introduce new structural
requirements beyond C-29 and C-32; it is the composition criterion whose satisfaction
requires both mechanisms together rather than either alone. A document that passes C-29
and fails C-32 fails C-33; a document that passes C-32 and fails C-29 fails C-33; a
document that passes both C-29 and C-32 passes C-33 regardless of whether any other
criterion fails. C-33 fails automatically if either C-29 or C-32 fails.

---

**Max composite: 200 → 215. Golden threshold (80) unchanged.**

Dependency chains:
```
C-16 (audit exists) -> C-18 (correction triggered) -> C-19 (content visible)

C-07 (spread mechanism exists) -> C-28 (spread mechanism label encodes constraint)
                               -> C-31 (table uses named transition-pair row keys)
C-11 (named inertia per archetype) -> C-29 (question-based citation enforcement)
C-20 (terminal section exists) -> C-30 (gate execution proof in terminal section)
C-18 (revision obligation) -> C-32 (mechanism anchor in body)
C-29 (answer-form enforcement) + C-32 (mechanism anchor) -> C-33 (co-present)
```

---

## Scoring Reference

| Criterion | Weight | Category |
|---|---|---|
| C-01 All 16 roles mapped | 12 | Foundational |
| C-02 Month-by-month Rogers sequence | 12 | Foundational |
| C-03 Chasm section with diagnosis | 12 | Foundational |
| C-04 Champion network named | 12 | Foundational |
| C-05 Intervention ranking present | 12 | Foundational |
| C-06 Churn register with trigger + mitigation | 10 | Structural |
| C-07 Spread mechanism per transition | 10 | Structural |
| C-08 Tabular month view | 10 | Structural |
| C-09 Sensitivity analysis 2 scenarios | 5 | Aspirational |
| C-10 Signal readiness feedback loop | 5 | Aspirational |
| C-11 Named inertia IDs per archetype | 5 | Aspirational |
| C-12 No orphan sections | 5 | Aspirational |
| C-13 Named inertia as downstream backbone | 5 | Aspirational |
| C-14 Champion rationale double-anchored | 5 | Aspirational |
| C-15 Concrete retention actions | 5 | Aspirational |
| C-16 Self-audit for C-13/C-14/C-15 | 5 | Aspirational |
| C-17 Dedicated slot per aspirational criterion | 5 | Aspirational |
| C-18 Revision obligation on fail | 5 | Aspirational |
| C-19 Corrected content visible inline | 5 | Aspirational |
| C-20 Gate states in single terminal section | 5 | Aspirational |
| C-21 Corrected content not in terminal section | 5 | Aspirational |
| C-22 Terminal section self-verifying invariant | 5 | Aspirational |
| C-23 Named verification boundary | 5 | Aspirational |
| C-24 Invariant names falsification condition | 5 | Aspirational |
| C-25 Phase headers enforce Rogers sequence | 5 | Aspirational |
| C-26 Incumbent-first displacement framing | 5 | Aspirational |
| C-27 Field label encodes concrete-action constraint | 5 | Aspirational |
| C-28 Spread mechanism label encodes specificity constraint | 5 | Aspirational |
| C-29 Question-based inertia citation enforcement | 5 | Aspirational |
| C-30 Per-gate execution stamps in terminal section | 5 | Aspirational |
| C-31 Spread mechanism table uses named transition-pair rows | 5 | Aspirational |
| C-32 Correction mechanism presence anchor in document body | 5 | Aspirational |
| C-33 Answer-form enforcement co-present with mechanism anchor | 5 | Aspirational |
| **Total** | **215** | |