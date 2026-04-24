Looking at the R9 scorecard, I see three distinct deltas that aren't yet captured:

1. **C-07 V-02 PARTIAL** — spread mechanism column exists but the slot label lacks the inline specificity constraint ("not generic word-of-mouth — name the signal or artifact"). Parallels C-27 exactly.
2. **C-13/C-14 V-04 PASS vs. others PARTIAL** — V-04's phase-header questions enforce ID citation by making the ID the *answer to a question* rather than a *field to fill*. Distinct enforcement mechanism.
3. **C-19 V-04 PARTIAL** — "Paradox of strength": the strongest architecture almost never fires a correction, so C-19 (requires visible correction) becomes paradoxically hard to satisfy. Gap: terminal section should prove gate execution regardless of outcome.

These elevate as C-28, C-29, C-30. Max composite 185 → 200.

---

```markdown
# Rubric: listen-adoption — v10

**Max composite:** 200 | **Golden threshold:** 80

---

**What changed from v9:**

Three new aspirational criteria (C-28, C-29, C-30) from R9 excellence signals.

Signal 1 (C-07 V-02 partial — spread mechanism table column lacks inline specificity constraint)
is elevated as C-28. It is a distinct observable output property: the spread mechanism slot
either embeds the constraint "not generic word-of-mouth — name the signal or artifact" in its
column header or field label at generation time, or it delegates enforcement to a separate
instruction or relies on downstream review. C-07 tests whether a named spread mechanism exists
per transition; C-28 tests whether the slot label makes generic entries structurally incompatible
with the slot — same elevation class as C-27 (field label encodes concrete-action constraint).
A spread mechanism column labeled "Spread Mechanism" passes C-07 but fails C-28 regardless of
what the model writes in the cell; a column labeled "Spread Mechanism: [named signal or
artifact — not generic word-of-mouth]" passes C-28 regardless of whether any separate
instruction exists. C-28 fails automatically if C-07 fails.

Signal 2 (C-13/C-14 V-04 PASS vs. others PARTIAL — question-based vs. instruction-based
citation enforcement) is elevated as C-29. It is a distinct observable output property: inertia
ID citations in phase bodies are either enforced by answer-form phase-header questions ("Which
Named Inertia ID is driving the chasm?"), which make ID omission structurally incompatible with
answering the question at all, or they are enforced by fill-form field instructions ("cite I-0X
from SECTION B"), which make omission a compliance failure rather than an incoherent answer.
Both forms produce ID citations; only the former makes omission detectable at generation time
without an audit. C-11 tests whether named inertia IDs exist per archetype; C-13 tests whether
IDs are cited in downstream sections; C-14 tests whether champion rationale is double-anchored;
C-29 tests whether the enforcement mechanism for those citations is answer-form rather than
fill-form. A document that passes C-13 and C-14 via field instructions fails C-29. A document
whose phase headers ask "Which Named Inertia ID is driving the chasm?" and "Named Inertia ID
this champion is positioned to overcome" passes C-29 regardless of whether any separate citation
instruction exists. C-29 fails automatically if C-11 fails.

Signal 3 (C-19 V-04 PARTIAL — paradox of strength: best generation-time compliance yields
lowest probability of a correction block firing) is elevated as C-30. It is a distinct
observable output property: the terminal section either contains a per-gate execution stamp for
every gate evaluated ("EVALUATED — no correction triggered" or equivalent), proving the audit
ran regardless of outcome, or it records gate states only when a correction was triggered,
leaving the no-correction case unverifiable. C-16 tests whether a self-audit section exists;
C-18 tests whether revision is obligated on fail; C-19 tests whether corrected content is
visible in the output; C-20 tests whether gate states are consolidated in a terminal section;
C-30 tests whether the terminal section is self-sufficient as proof of audit execution without
requiring a failure to have occurred. A terminal section that records only failures (passing
gates leave no entry) passes C-20 but fails C-30. A terminal section that records an explicit
execution stamp per gate — including "PASS — no correction triggered" for gates that passed on
first attempt — passes C-30 regardless of whether any CORRECTION BLOCK appears elsewhere in
the document. C-30 fails automatically if C-20 fails.

---

## Criteria

**C-01 — All 16 roles mapped to canonical Rogers archetypes** (12 pts)
An explicit role-to-archetype table with all 16 roles assigned to one of the five canonical
Rogers archetypes (Innovator, Early Adopter, Early Majority, Late Majority, Laggard). No role
omitted. No archetype invented. Pass condition: table is present and complete.

**C-02 — Month-by-month adoption sequence ordered by Rogers archetypes** (12 pts)
A PHASE 1–6 structure spanning at least 6 months with archetypes assigned in Rogers order
(Innovators first, Laggards last). Phase 3 (Chasm) explicitly marked as a non-adoption crossing
event, not an archetype phase. Pass condition: phase sequence and month labeling are present and
correctly ordered.

**C-03 — Chasm section present with crossing diagnosis** (12 pts)
A dedicated chasm section that diagnoses the early-majority crossing challenge: what defends the
incumbent's position among the late majority, what bridge condition must hold, and what early
signal confirms the chasm has been crossed. Pass condition: chasm section present with all three
elements.

**C-04 — Champion network section present with named roles** (12 pts)
A dedicated champion network section naming at least three specific roles (by title or archetype)
who are positioned to advocate for adoption and displace the incumbent. Pass condition: champion
section present with named roles and adoption rationale per role.

**C-05 — Intervention ranking section present** (12 pts)
A dedicated section ranking retention interventions by impact on adoption velocity. Ranking must
reference at least two phases and two named roles. Pass condition: section present with
multi-phase, multi-role ranking.

**C-06 — Churn risk register with named trigger and mitigation per entry** (10 pts)
A structured churn register in which every entry contains (a) a named reversion trigger — the
specific condition that would cause a role to revert to the incumbent — and (b) a mitigation.
Pass condition: register present; no entry lacks a named trigger and at least one mitigation.

**C-07 — Spread mechanism named per phase transition** (10 pts)
An explicit spread mechanism named per phase transition (Innovator→Early Adopter,
Early Adopter→Early Majority, etc.). The mechanism must be feature-specific — a named signal,
artifact, or social proof event — not a generic description such as "word of mouth" or
"organic growth." Pass condition: mechanism present per transition; all mechanisms are
feature-specific.

**C-08 — Tabular or structured month view with scannable phase headers** (10 pts)
Phase headers that include the month range and archetype name, formatted so the adoption
timeline is scannable without reading the body text. Pass condition: headers present for all
phases; month ranges are explicit.

**C-09 — Sensitivity analysis with two named scenarios** (5 pts)
A sensitivity analysis — table or equivalent — with at least two named scenarios (e.g.,
Fast Adoption and Slow Adoption) and at least one named lever that shifts the outcome between
scenarios. Pass condition: two named scenarios and at least one named lever present.

**C-10 — Signal readiness feedback loop with threshold and interpretation** (5 pts)
A readiness table mapping named signals to adoption thresholds and interpretations. Each row
must contain: the signal name, the threshold value or condition, and the interpretation
(what it means for adoption timing). Pass condition: table present; all rows complete.

**C-11 — Named inertia IDs assigned per Rogers archetype** (5 pts)
Named inertia identifiers (I-01 through I-05 or equivalent) assigned one per canonical
archetype, with the inertia described as the structural reason that archetype resists adoption.
Pass condition: five IDs assigned, one per archetype, each with a named inertia description.

**C-12 — No orphan sections** (5 pts)
Every named criterion that generates content has a dedicated structural slot in the document.
No criterion depends on content embedded in another criterion's section. Pass condition: all
C-09 and C-10 slots present as dedicated sections; no criterion is satisfied by content found
only in another criterion's section.

**C-13 — Named inertia IDs cited as downstream backbone** (5 pts)
The named inertia IDs from C-11 are cited by ID (e.g., I-03) in at least four downstream
locations: bridge conditions, intervention rationale, champion rationale, and churn register
entries. Pass condition: all four downstream location types contain at least one ID citation.
Aspirational. H gate corrects misses.

**C-14 — Champion rationale double-anchored to archetype bridge and inertia ID** (5 pts)
Each champion entry contains two separate anchors: (a) the archetype-bridge rationale — why
this role's archetype position makes it an effective adoption champion — and (b) the named
inertia ID (from C-11) that this champion is positioned to overcome, cited by ID. Pass
condition: both anchors present per champion entry. Aspirational. I gate corrects misses.

**C-15 — Churn register mitigations are concrete retention actions** (5 pts)
Every mitigation in the churn register is a concrete retention action — something a team does
to reduce reversion probability — rather than a surveillance or monitoring flag (e.g., "track
usage" or "monitor engagement" fails this criterion). Pass condition: no entry contains only a
surveillance flag as its mitigation. Aspirational. J gate corrects misses.

**C-16 — Self-audit section for C-13, C-14, and C-15 present** (5 pts)
Dedicated gate sections H (C-13 audit), I (C-14 audit), and J (C-15 audit) are present,
named, and explicitly reference the criterion being audited by ID. Pass condition: all three
gate sections present with criterion-ID references.

**C-17 — Dedicated structural slot per aspirational criterion** (5 pts)
Each aspirational criterion (C-13, C-14, C-15) has its own named gate section that is
structurally separate from the content section it audits. Pass condition: H, I, J are separate
named sections; none is embedded inside a content section.

**C-18 — Revision obligation on gate fail** (5 pts)
Each gate section (H, I, J) contains an explicit revision obligation: if the gate fails, a
CORRECTION BLOCK must be produced immediately before proceeding. The obligation must be stated
in imperative form within the gate section itself. Pass condition: revision obligation
explicitly stated in all three gate sections.

**C-19 — Corrected content visible in output as inline CORRECTION BLOCK** (5 pts)
At least one inline CORRECTION BLOCK — containing a BEFORE field and an AFTER field — appears
in the document body above the terminal section. Pass condition: CORRECTION BLOCK with both
fields present and inline (not in the terminal section). Aspirational in architecturally strong
variations where all gates pass on first attempt; see C-30 for the complementary criterion.

**C-20 — Gate states consolidated in a single terminal section** (5 pts)
A single named terminal section (SECTION K or equivalent) consolidates the initial gate result,
revision performed (yes/no), CORRECTION BLOCK location (section reference), and final gate
result for all three gates (H, I, J). Pass condition: all four fields present per gate in a
single terminal section.

**C-21 — Corrected content excluded from terminal section** (5 pts)
The terminal section records gate outcomes only. No CORRECTION BLOCK content — no BEFORE or
AFTER fields — appears in the terminal section. Pass condition: terminal section contains no
BEFORE or AFTER fields.

**C-22 — Terminal section contains a self-verifying invariant** (5 pts)
The terminal section contains an explicit invariant stating the consistency condition that the
terminal section itself must satisfy: for every "Revision Performed: Yes" entry, a CORRECTION
BLOCK with BEFORE and AFTER content must exist earlier in the document at the cited location.
Pass condition: invariant present and states the consistency condition in verifiable form.

**C-23 — Named verification boundary separates content generation from audit** (5 pts)
A "## VERIFICATION MODE" header or equivalent explicitly marks the boundary between content
generation and the audit stage. No audit content appears before the boundary; no content
generation appears after it. Pass condition: named boundary present; audit sections (H, I, J, K)
all appear after it.

**C-24 — Invariant names its own falsification condition** (5 pts)
The terminal section invariant states an explicit failure mode: the specific condition that
would falsify the invariant (e.g., "a Yes row whose CORRECTION BLOCK Location references a
section containing no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field,
falsifies this invariant"). Pass condition: falsification condition present and specific.

**C-25 — Phase headers enforce Rogers sequence architecturally** (5 pts)
The document uses PHASE 1 INNOVATORS through PHASE 6 LAGGARDS as structural section headers,
with PHASE 3 CHASM explicitly marked as a non-adoption crossing event. The Rogers sequence is
structurally enforced by header names, not merely instructed in a preamble. Pass condition:
all six phase headers present with correct Rogers labeling; PHASE 3 marked as non-adoption.

**C-26 — Incumbent-first displacement framing names THE INCUMBENT before archetype
assignment** (5 pts)
Source: V-04's opening structure, which explicitly names the current workflow or tool being
displaced (THE INCUMBENT) before beginning archetype assignment, then runs all phase bodies
through the displacement lens — asking "what does this phase do to THE INCUMBENT's position?"
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

**C-27 — Churn register field label encodes the concrete-action constraint at generation
time** (5 pts)
Source: V-04's PART 3 churn register, which uses the field label "Retention intervention: [one
concrete action that reduces reversion probability]" rather than a generic "Mitigation:" label
augmented by a separate instruction or downstream audit prohibiting surveillance-only entries.
When the positive constraint is embedded in the field label itself — "[one concrete action]" —
the model must write an action because that is what fits the slot; the constraint is enforced at
generation time rather than caught after the fact. C-06 tests that the churn register is present
and that each entry contains a named trigger and at least one mitigation; C-15 tests that the
mitigation is a concrete retention action rather than a surveillance or monitoring flag; C-27
tests whether the field label itself makes a separate instruction or downstream audit unnecessary
— the constraint is verifiable by reading the label alone, before reading any mitigation entry.
A churn register with a "Mitigation" label and a bracketed prohibition in an instruction block
passes C-06 and may pass C-15 depending on what the model wrote, but fails C-27 because the
constraint is not in the label. A churn register whose label reads "Retention intervention:
[one concrete action that reduces reversion probability]" passes C-27 regardless of whether any
separate instruction exists. C-27 fails automatically if C-06 fails.

**C-28 — Spread mechanism slot label encodes the specificity constraint at generation
time** (5 pts)
Source: V-02 PARTIAL on C-07 — the spread mechanism column existed in TABLE 3 but the column
header was a generic "Spread Mechanism" label without the inline constraint, reducing generation-
time pressure for feature-specific entries. The excellence seen in other R9 variations is that
the spread mechanism slot label itself embeds the constraint: "Spread Mechanism: [named signal
or artifact — not generic word-of-mouth]." When the constraint is in the label, a model
writing "word-of-mouth" cannot do so without violating the slot's own type; when the constraint
is in a separate instruction, the model can satisfy the slot structurally while violating the
constraint semantically. C-07 tests whether a named spread mechanism exists per transition;
C-28 tests whether the slot label makes generic entries structurally incompatible at generation
time — same elevation class as C-27. A spread mechanism column labeled "Spread Mechanism" that
produces feature-specific entries passes C-07 but fails C-28; the constraint is not in the
label and cannot be verified by reading the label alone. A spread mechanism column labeled
"Spread Mechanism: [named signal or artifact — not generic word-of-mouth]" passes C-28
regardless of whether any separate instruction exists. C-28 fails automatically if C-07 fails.

**C-29 — Inertia ID citations enforced by answer-form phase-header questions** (5 pts)
Source: V-04 PASS on C-13 and C-14 vs. PARTIAL for all other R9 variations — V-04's phase
headers ask "Which Named Inertia ID is driving the chasm?" and "Named Inertia ID this champion
is positioned to overcome (from SECTION B — cite I-0X)" as mandatory phase-body fields, making
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

**C-30 — Terminal section contains per-gate execution stamps regardless of correction
outcome** (5 pts)
Source: V-04 PARTIAL on C-19 — "Paradox of strength": V-04's phase-header architecture
produces the highest generation-time compliance for C-13 and C-14, meaning gates H and I are
most likely to pass on first attempt, meaning no CORRECTION BLOCK fires, meaning C-19 (requires
at least one visible CORRECTION BLOCK) paradoxically fails in the strongest variation. The gap
is that the terminal section records gate states only when a correction was triggered, leaving
the no-correction case unverifiable: a terminal section with no entries is indistinguishable
from a terminal section whose gates were never evaluated. The excellence criterion is: the
terminal section must contain a per-gate execution stamp for every gate evaluated, including
explicitly recording "PASS — no correction triggered" or equivalent for gates that passed on
first attempt. C-16 tests whether a self-audit section exists; C-18 tests whether revision is
obligated on fail; C-19 tests whether corrected content is visible; C-20 tests whether gate
states are in a terminal section; C-30 tests whether the terminal section is self-sufficient as
proof of audit execution — complete regardless of whether any correction fired. A terminal
section recording only failures has no entry for a passing gate and fails C-30 because the
passing case is unverified. A terminal section recording "H: PASS — no correction triggered |
I: PASS — no correction triggered | J: PASS — no correction triggered" passes C-30 regardless
of whether any CORRECTION BLOCK appears elsewhere. C-30 fails automatically if C-20 fails.

---

**Max composite: 185 → 200. Golden threshold (80) unchanged.**

Dependency chains:
```
C-16 (audit exists) -> C-18 (correction triggered) -> C-19 (content visible)

C-07 (spread mechanism exists) -> C-28 (spread mechanism label encodes constraint)
C-11 (named inertia per archetype) -> C-29 (question-based citation enforcement)
C-20 (terminal section exists) -> C-30 (gate execution proof in terminal section)
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
| **Total** | **200** | |
```
