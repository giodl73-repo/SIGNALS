# listen-adoption rubric v20

Three new criteria extracted from R19 excellence signals:

- **C-55 (Pattern 1 / Axis A carry-forward)**: Protected behavior propagates from the DOWNSTREAM CITATION CONTRACT source declaration (C-54) into the CORRECTION BLOCK label when Gate H fires (C-52 label extension) -- making each correction a self-describing displacement-commitment fault record without SECTION A cross-reference.
- **C-56 (Pattern 1+3 / Axis B carry-forward)**: Protected behavior propagates from source (C-54) into the SECTION K CITATION CONTRACT COMPLETION RECORD, completing the three-tier displacement accountability chain: commit (C-54) -- correct (C-55) -- certify (C-56).
- **C-57 (Pattern 2 / Axis C)**: Arc discontinuities detected by C-53's DISPLACEMENT ARC INTEGRITY CHECK trigger an ARC CORRECTION BLOCK with mandatory BEFORE/AFTER structure -- the same mandatory-repair protocol as citation failures -- closing the loop between arc-discontinuity detection and arc-discontinuity correction.

---

**Max: 320 --> 335. Golden threshold (80%): 268 pts. Paradox ceiling: 330/335** (C-19 structural FAIL persists).

New dependency chain additions:
```
C-52 + C-54 -> C-55
C-51 + C-54 -> C-56
C-53 -> C-57
```

---

## Criteria

**C-01 -- All 16 roles mapped to canonical Rogers archetypes** (12 pts)
An explicit role-to-archetype table with all 16 roles assigned to one of the five canonical
Rogers archetypes (Innovator, Early Adopter, Early Majority, Late Majority, Laggard). No role
omitted. No archetype invented. Pass condition: table is present and complete.

**C-02 -- Month-by-month adoption sequence ordered by Rogers archetypes** (12 pts)
A PHASE 1-6 structure spanning at least 6 months with archetypes assigned in Rogers order
(Innovators first, Laggards last). Phase 3 (Chasm) explicitly marked as a non-adoption crossing
event, not an archetype phase. Pass condition: phase sequence and month labeling are present and
correctly ordered.

**C-03 -- Chasm section present with crossing diagnosis** (12 pts)
A dedicated chasm section that diagnoses the early-majority crossing challenge: what defends the
incumbent's position among the late majority, what bridge condition must hold, and what early
signal confirms the chasm has been crossed. Pass condition: chasm section present with all three
elements.

**C-04 -- Champion network section present with named roles** (12 pts)
A dedicated champion network section naming at least three specific roles (by title or archetype)
who are positioned to advocate for adoption and displace the incumbent. Pass condition: champion
section present with named roles and adoption rationale per role.

**C-05 -- Intervention ranking section present** (12 pts)
A dedicated section ranking retention interventions by impact on adoption velocity. Ranking must
reference at least two phases and two named roles. Pass condition: section present with
multi-phase, multi-role ranking.

**C-06 -- Churn risk register with named trigger and mitigation per entry** (10 pts)
A structured churn register in which every entry contains (a) a named reversion trigger -- the
specific condition that would cause a role to revert to the incumbent -- and (b) a mitigation.
Pass condition: register present; no entry lacks a named trigger and at least one mitigation.

**C-07 -- Spread mechanism named per phase transition** (10 pts)
An explicit spread mechanism named per phase transition (Innovator -> Early Adopter,
Early Adopter -> Early Majority, etc.). The mechanism must be feature-specific -- a named signal,
artifact, or social proof event -- not a generic description such as "word of mouth" or
"organic growth." Pass condition: mechanism present per transition; all mechanisms are
feature-specific.

**C-08 -- Tabular or structured month view with scannable phase headers** (10 pts)
Phase headers that include the month range and archetype name, formatted so the adoption
timeline is scannable without reading the body text. Pass condition: headers present for all
phases; month ranges are explicit.

**C-09 -- Sensitivity analysis with two named scenarios** (5 pts)
A sensitivity analysis -- table or equivalent -- with at least two named scenarios (e.g.,
Fast Adoption and Slow Adoption) and at least one named lever that shifts the outcome between
scenarios. Pass condition: two named scenarios and at least one named lever present.

**C-10 -- Signal readiness feedback loop with threshold and interpretation** (5 pts)
A readiness table mapping named signals to adoption thresholds and interpretations. Each row
must contain: the signal name, the threshold value or condition, and the interpretation
(what it means for adoption timing). Pass condition: table present; all rows complete.

**C-11 -- Named inertia IDs assigned per Rogers archetype** (5 pts)
Named inertia identifiers (I-01 through I-05 or equivalent) assigned one per canonical
archetype, with the inertia described as the structural reason that archetype resists adoption.
Pass condition: five IDs assigned, one per archetype, each with a named inertia description.

**C-12 -- No orphan sections** (5 pts)
Every named criterion that generates content has a dedicated structural slot in the document.
No criterion depends on content embedded in another criterion's section. Pass condition: all
C-09 and C-10 slots present as dedicated sections; no criterion is satisfied by content found
only in another criterion's section.

**C-13 -- Named inertia IDs cited as downstream backbone** (5 pts)
The named inertia IDs from C-11 are cited by ID (e.g., I-03) in at least four downstream
locations: bridge conditions, intervention rationale, champion rationale, and churn register
entries. Pass condition: all four downstream location types contain at least one ID citation.
Aspirational. H gate corrects misses. C-44 is the structural enabler for full PASS on
intervention rationale.

**C-14 -- Champion rationale double-anchored to archetype bridge and inertia ID** (5 pts)
Each champion entry contains two separate anchors: (a) the archetype-bridge rationale -- why
this role's archetype position makes it an effective adoption champion -- and (b) the named
inertia ID (from C-11) that this champion is positioned to overcome, cited by ID. Pass
condition: both anchors present per champion entry. Aspirational. I gate corrects misses.

**C-15 -- Churn register mitigations are concrete retention actions** (5 pts)
Every mitigation in the churn register is a concrete retention action -- something a team does
to reduce reversion probability -- rather than a surveillance or monitoring flag (e.g., "track
usage" or "monitor engagement" fails this criterion). Pass condition: no entry contains only a
surveillance flag as its mitigation. Aspirational. J gate corrects misses.

**C-16 -- Self-audit section for C-13, C-14, and C-15 present** (5 pts)
Dedicated gate sections H (C-13 audit), I (C-14 audit), and J (C-15 audit) are present,
named, and explicitly reference the criterion being audited by ID. Pass condition: all three
gate sections present with criterion-ID references.

**C-17 -- Dedicated structural slot per aspirational criterion** (5 pts)
Each aspirational criterion (C-13, C-14, C-15) has its own named gate section that is
structurally separate from the content section it audits. Pass condition: H, I, J are separate
named sections; none is embedded inside a content section.

**C-18 -- Revision obligation on gate fail** (5 pts)
Each gate section (H, I, J) contains an explicit revision obligation: if the gate fails, a
CORRECTION BLOCK must be produced immediately before proceeding. The obligation must be stated
in imperative form within the gate section itself. Pass condition: revision obligation
explicitly stated in all three gate sections.

**C-19 -- Corrected content visible in output as inline CORRECTION BLOCK** (5 pts)
At least one inline CORRECTION BLOCK -- containing a BEFORE field and an AFTER field -- appears
in the document body above the terminal section. Pass condition: CORRECTION BLOCK with both
fields present and inline (not in the terminal section). Aspirational in architecturally strong
variations where all gates pass on first attempt; see C-30 for the complementary criterion and
C-32 for the mechanism-presence criterion.

**C-20 -- Gate states consolidated in a single terminal section** (5 pts)
A single named terminal section (SECTION K or equivalent) consolidates the initial gate result,
revision performed (yes/no), CORRECTION BLOCK location (section reference), and final gate
result for all three gates (H, I, J). Pass condition: all four fields present per gate in a
single terminal section.

**C-21 -- Corrected content excluded from terminal section** (5 pts)
The terminal section records gate outcomes only. No CORRECTION BLOCK content -- no BEFORE or
AFTER fields -- appears in the terminal section. Pass condition: terminal section contains no
BEFORE or AFTER fields.

**C-22 -- Terminal section contains a self-verifying invariant** (5 pts)
The terminal section contains an explicit invariant stating the consistency condition that the
terminal section itself must satisfy: for every "Revision Performed: Yes" entry, a CORRECTION
BLOCK with BEFORE and AFTER content must exist earlier in the document at the cited location.
Pass condition: invariant present and states the consistency condition in verifiable form.

**C-23 -- Named verification boundary separates content generation from audit** (5 pts)
A "## VERIFICATION MODE" header or equivalent explicitly marks the boundary between content
generation and the audit stage. No audit content appears before the boundary; no content
generation appears after it. Pass condition: named boundary present; audit sections (H, I, J, K)
all appear after it.

**C-24 -- Invariant names its own falsification condition** (5 pts)
The terminal section invariant states an explicit failure mode: the specific condition that
would falsify the invariant (e.g., "a Yes row whose CORRECTION BLOCK Location references a
section containing no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field,
falsifies this invariant"). Pass condition: falsification condition present and specific; must
name both the missing-CORRECTION-BLOCK case and the CORRECTION-BLOCK-without-BEFORE-field case.

**C-25 -- Phase headers enforce Rogers sequence architecturally** (5 pts)
The document uses PHASE 1 INNOVATORS through PHASE 6 LAGGARDS as structural section headers,
with PHASE 3 CHASM explicitly marked as a non-adoption crossing event. The Rogers sequence is
structurally enforced by header names, not merely instructed in a preamble. Pass condition:
all six phase headers present with correct Rogers labeling; PHASE 3 marked as non-adoption.

**C-26 -- Incumbent-first displacement framing names THE INCUMBENT before archetype
assignment** (5 pts)
Source: V-04's opening structure, which explicitly names the current workflow or tool being
displaced (THE INCUMBENT) before beginning archetype assignment, then runs all phase bodies
through the displacement lens -- asking "what does this phase do to THE INCUMBENT's position?"
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

**C-27 -- Churn register field label encodes the concrete-action constraint at generation
time** (5 pts)
Source: V-04's PART 3 churn register, which uses the field label "Retention intervention: [one
concrete action that reduces reversion probability]" rather than a generic "Mitigation:" label
augmented by a separate instruction or downstream audit prohibiting surveillance-only entries.
When the positive constraint is embedded in the field label itself -- "[one concrete action]" --
the model must write an action because that is what fits the slot; the constraint is enforced at
generation time rather than caught after the fact. C-06 tests that the churn register is present
and that each entry contains a named trigger and at least one mitigation; C-15 tests that the
mitigation is a concrete retention action rather than a surveillance or monitoring flag; C-27
tests whether the field label itself makes a separate instruction or downstream audit unnecessary
-- the constraint is verifiable by reading the label alone, before reading any mitigation entry.
A churn register with a "Mitigation" label and a bracketed prohibition in an instruction block
passes C-06 and may pass C-15 depending on what the model wrote, but fails C-27 because the
constraint is not in the label. A churn register whose label reads "Retention intervention:
[one concrete action that reduces reversion probability]" passes C-27 regardless of whether any
separate instruction exists. C-27 fails automatically if C-06 fails.

**C-28 -- Spread mechanism slot label encodes the specificity constraint at generation
time** (5 pts)
Source: V-02 PARTIAL on C-07 -- the spread mechanism column existed in TABLE 3 but the column
header was a generic "Spread Mechanism" label without the inline constraint, reducing generation-
time pressure for feature-specific entries. The excellence seen in other R9 variations is that
the spread mechanism slot label itself embeds the constraint: "Spread Mechanism: [named signal
or artifact -- not generic word-of-mouth]." When the constraint is in the label, a model
writing "word-of-mouth" cannot do so without violating the slot's own type; when the constraint
is in a separate instruction, the model can satisfy the slot structurally while violating the
constraint semantically. C-07 tests whether a named spread mechanism exists per transition;
C-28 tests whether the slot label makes generic entries structurally incompatible at generation
time -- same elevation class as C-27. A spread mechanism column labeled "Spread Mechanism" that
produces feature-specific entries passes C-07 but fails C-28; the constraint is not in the
label and cannot be verified by reading the label alone. A spread mechanism column labeled
"Spread Mechanism: [named signal or artifact -- not generic word-of-mouth]" passes C-28
regardless of whether any separate instruction exists. C-28 fails automatically if C-07 fails.

**C-29 -- Inertia ID citations enforced by answer-form phase-header questions** (5 pts)
Source: V-04 PASS on C-13 and C-14 vs. PARTIAL for all other R9 variations -- V-04's phase
headers ask "Which Named Inertia ID is driving the chasm?" and "Named Inertia ID this champion
is positioned to overcome (from SECTION B -- cite I-0X)" as mandatory phase-body fields, making
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

**C-30 -- Terminal section contains per-gate execution stamps regardless of correction
outcome** (5 pts)
Source: V-04 PARTIAL on C-19 -- "Paradox of strength": V-04's phase-header architecture
produces the highest generation-time compliance for C-13 and C-14, meaning gates H and I are
most likely to pass on first attempt, meaning no CORRECTION BLOCK fires, meaning C-19 (requires
at least one visible CORRECTION BLOCK) paradoxically fails in the strongest variation. The gap
is that the terminal section records gate states only when a correction was triggered, leaving
the no-correction case unverifiable: a terminal section with no entries is indistinguishable
from a terminal section whose gates were never evaluated. The excellence criterion is: the
terminal section must contain a per-gate execution stamp for every gate evaluated, including
explicitly recording "PASS -- no correction triggered" or equivalent for gates that passed on
first attempt. C-16 tests whether a self-audit section exists; C-18 tests whether revision is
obligated on fail; C-19 tests whether corrected content is visible; C-20 tests whether gate
states are in a terminal section; C-30 tests whether the terminal section is self-sufficient as
proof of audit execution -- complete regardless of whether any correction fired. A terminal
section recording only failures has no entry for a passing gate and fails C-30 because the
passing case is unverified. A terminal section recording "H: PASS -- no correction triggered |
I: PASS -- no correction triggered | J: PASS -- no correction triggered" passes C-30 regardless
of whether any CORRECTION BLOCK appears elsewhere. C-30 fails automatically if C-20 fails.

**C-31 -- Spread mechanism table uses named transition-pair row labels as structural
slots** (5 pts)
Source: V-02/V-03 PARTIAL on C-07 -- both variations addressed spread mechanism through
phase-body questions rather than TABLE 3, producing contextual coverage of one transition
while leaving the other three without dedicated structural slots. V-01, V-04, and V-05
passed C-07 via TABLE 3 with explicit named rows for each transition pair
(Innovator -> Early Adopter, Early Adopter -> Early Majority, Early Majority -> Late
Majority, Late Majority -> Laggard), making per-transition omission structurally
incompatible with completing the table. C-07 tests whether a named spread mechanism exists
per transition; C-28 tests whether the slot label embeds the specificity constraint inline;
C-31 tests whether the table structure itself enforces per-transition coverage via named
transition-pair row keys -- whether coverage is enforced by structural slot count (four named
rows requiring four entries) rather than by instruction compliance (a question that
contextually encourages multi-transition coverage without requiring it syntactically). A
spread mechanism embedded in a phase-body question fails C-31 regardless of how many
transitions it addresses contextually, because the remaining transitions have no structural
slot and no generation-time pressure. A table with four rows labeled with the four canonical
transition pairs passes C-31 regardless of whether any separate per-transition instruction
exists, because completing the table requires a spread mechanism entry for each named row.
C-31 fails automatically if C-07 fails.

**C-32 -- Correction mechanism presence anchor in document body proves mechanism
availability** (5 pts)
Source: V-02/V-04/V-05 PARTIAL on C-19 -- the paradox of strength persists beyond C-30:
C-30 proves the audit ran via per-gate execution stamps in SECTION K, but does not prove
the correction mechanism was armed and available in the document body. A document that
achieves perfect gate compliance has no triggered CORRECTION BLOCK, making the mechanism's
existence in the document body unverifiable from any terminal-section entry alone. The
excellence criterion is: the document must contain a correction-mechanism presence anchor --
either an inline CORRECTION BLOCK triggered by a gate failure (containing BEFORE and AFTER
fields, satisfying C-19 directly) or an explicit "CORRECTION BLOCK MECHANISM ARMED -- no
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
MECHANISM ARMED -- no gate failure triggered" declaration before SECTION K passes C-32
because the mechanism is proven present even without firing. C-32 fails automatically if
C-18 fails.

**C-33 -- Answer-form citation enforcement co-present with correction mechanism
anchor** (5 pts)
Source: No single R10 variation simultaneously passes C-13, C-14, C-19, and C-29 --
answer-form enforcement (V-02, V-04, V-05) satisfies C-29/C-13/C-14 while suppressing
C-19 by producing high gate-pass rates that prevent CORRECTION BLOCK from firing; fill-form
enforcement (V-01, V-03) satisfies C-19 by producing medium gate-pass rates that allow
correction blocks to fire, while failing C-29/C-13/C-14 because enforcement is
instructional rather than architectural. C-32 resolves the C-19 paradox for answer-form
designs by replacing proof-by-execution (C-19) with proof-by-declaration-or-execution
(C-32): an answer-form design that also contains a "CORRECTION BLOCK MECHANISM ARMED"
declaration satisfies C-32 without requiring any gate to fail. C-33 tests whether the
answer-form citation mechanism (C-29) and the correction mechanism anchor (C-32) are
co-present in the same document -- the only structural combination that achieves PASS on
C-13, C-14, C-29, and C-32 simultaneously, breaking the trade-off that prevented any
single R10 variation from holding all four. C-33 does not introduce new structural
requirements beyond C-29 and C-32; it is the composition criterion whose satisfaction
requires both mechanisms together rather than either alone. A document that passes C-29
and fails C-32 fails C-33; a document that passes C-32 and fails C-29 fails C-33; a
document that passes both C-29 and C-32 passes C-33 regardless of whether any other
criterion fails. C-33 fails automatically if either C-29 or C-32 fails.

**C-34 -- Correction mechanism anchor double-anchored at gate level and verification
boundary** (5 pts)
Source: V-05 R11 -- the distinction between a single-location C-32 anchor and a dual-location
anchor. V-01/V-04 satisfied C-32 via a pre-verification MECHANISM STATE line (single anchor at
the verification boundary only); V-02 satisfied C-32 via per-gate footers in SECTIONS H/I/J
(anchor at the gate level only); V-03 satisfied C-32 via a dedicated MECHANISM ANCHOR section
between SECTION J and SECTION K (single anchor in its own named section). V-05 achieves both
simultaneously: per-gate footers inside each of SECTIONS H, I, J AND a pre-verification
declaration before VERIFICATION MODE. A single-location anchor proves mechanism availability
at one structural point; a double-anchored implementation proves availability independently at
both the per-gate level (immediately visible within each gate's section) and the verification
boundary level (immediately visible at the content/audit transition), making the mechanism
evaluable by two independent routes without requiring the evaluator to cross-reference between
structural regions. C-32 tests whether any correction mechanism anchor exists in the document
body before SECTION K; C-34 tests whether the anchor is proven at both structural levels
simultaneously -- that neither level alone is load-bearing because both are present. A document
with only a pre-verification declaration but no per-gate footers passes C-32 and fails C-34;
a document with per-gate footers in H/I/J but no pre-verification declaration passes C-32 and
fails C-34; a document with a dedicated MECHANISM ANCHOR section but no per-gate footers passes
C-32 and fails C-34; a document with both per-gate footers in each gate section and a
pre-verification declaration passes C-34 regardless of whether any separate mechanism anchor
section exists. C-34 fails automatically if C-32 fails.

**C-35 -- STRUCTURAL CONTRACT explicitly names answer-form and mechanism anchor as mandatory
co-present requirements** (5 pts)
Source: V-04/V-05 R11 -- the distinction between implicit co-presence and architecturally
mandated co-presence. V-01/V-02/V-03 satisfied C-33 through implicit co-presence: baseline
C-29 carried and C-32 introduced separately; both mechanisms present in the document and their
structural conjunction satisfies the rubric, but no part of the document asserts that both are
required together. V-04/V-05 introduced a STRUCTURAL CONTRACT -- an explicit block that names
both the answer-form questions (C-29) and the MECHANISM STATE line (C-32) as mandatory
co-present requirements -- making C-33 architecturally required rather than emergent: no
trade-off between the two mechanisms is possible without violating the STRUCTURAL CONTRACT
itself. C-33 tests whether C-29 and C-32 are co-present; C-35 tests whether their co-presence
is explicitly declared as mandatory at the structural contract level, closing the gap between
"both happen to be here" and "both are required to be here." A document that passes C-29 and
C-32 in separate, unconnected structural regions passes C-33 and fails C-35 because the
co-presence is observable but undeclared. A document with a STRUCTURAL CONTRACT naming both
mechanisms as mandatory co-present requirements passes C-35 regardless of where in the document
the STRUCTURAL CONTRACT appears, provided it is prior to the content generation sections it
governs. C-35 fails automatically if C-33 fails.

**C-36 -- TABLE 3 row labels typed as structural slot keys in the table header** (5 pts)
Source: V-05 R11 enhancement of C-31. C-31 tests whether the four named transition-pair rows
exist as structural slots, enforcing per-transition coverage by slot count -- four rows named
with canonical transition pairs require four mechanism entries. V-05's TABLE 3 header goes
further: it explicitly names the four rows as typed structural slot keys, signaling a slot-type
contract to the downstream model rather than just a row-count requirement. Same elevation class
as C-27 (churn register field label encodes the concrete-action constraint) and C-28 (spread
mechanism slot label encodes the specificity constraint): C-36 is the table-header analogue,
encoding the row-as-typed-slot-key contract at the header level so per-transition enforcement
shifts from count-based (four named rows) to type-based (four typed slot keys whose type
contract constrains what can fill each row). When the header declares the rows as typed slot
keys, a model completing the table cannot satisfy the header's own type contract without
providing a mechanism entry that fits the slot type for each named transition pair; when the
header is a generic label such as "Spread Mechanism" or "TABLE 3," row count enforces coverage
but slot type does not constrain entry quality at generation time. C-31 tests whether named
transition-pair rows exist; C-28 tests whether the column label embeds the specificity
constraint; C-36 tests whether the table header itself encodes the row-as-typed-slot-key
contract, making the table self-describing as a typed slot structure independent of any column
label or separate instruction. A table with four named rows and a column label satisfying C-28
but a generic table header passes C-31 and C-28 and fails C-36; a table whose header explicitly
names the four rows as typed structural slot keys passes C-36 regardless of whether any separate
per-transition instruction or column label exists. C-36 fails automatically if C-31 fails.

**C-37 -- TABLE 1 includes an Incumbent Dependency column co-present with archetype
assignment** (5 pts)
Source: V-01/V-05 R12 -- the structural difference between standalone SECTION B (V-02/V-03/V-04)
and TABLE 1 integration. C-26 tests whether the simulation opens with incumbent-first
displacement framing; both SECTION B placement and TABLE 1 column integration satisfy C-26.
The distinction is generation-time co-presence: SECTION B names the incumbent before TABLE 1
begins, making the displacement lens available in context but not structurally active during
archetype assignment. An Incumbent Dependency column in TABLE 1 places the displacement lens
as a fill contract for every row in the table, forcing the model to name each role's specific
incumbent dependency at the same generation step as its archetype assignment -- merging C-01
and C-26 into a single structural slot. A simulation with SECTION B and TABLE 1 archetype rows
achieves C-01 and C-26 in separate structural regions; a simulation whose TABLE 1 contains an
Incumbent Dependency column achieves C-01 and C-26 as co-present generation-time contracts at
the table level. C-37 tests whether the merging of archetype assignment and displacement framing
is encoded structurally in TABLE 1, not whether the incumbent is named somewhere before or
alongside TABLE 1. A TABLE 1 with a generic "Notes" or "Displacement" column that is not
contract-typed as incumbent dependency fails C-37; a TABLE 1 with an Incumbent Dependency
column labeled to encode each role's specific dependency on the incumbent workflow or tool
passes C-37. C-37 fails automatically if C-26 fails.

**C-38 -- TABLE 3 row labels use SLOT-KEY: prefix to re-assert typed contract at row
level** (5 pts)
Source: V-02/V-04/V-05 R12 -- the extension of C-36 to row-level contract re-assertion. C-36
tests whether the TABLE 3 table header declares the rows as typed structural slot keys, making
the contract visible once at table-entry time. The SLOT-KEY: prefix applies the contract to
each individual row label: "SLOT-KEY: Innovator -> Early Adopter," "SLOT-KEY: Early Adopter ->
Early Majority," etc. When the header is the only typed-slot-key declaration, the model
encounters the contract once and must hold it across all subsequent row fills from memory; when
each row label carries SLOT-KEY:, the model re-encounters the typed-slot-key contract at the
generation moment for that row independently, making the contract continuously present at each
fill step rather than once at table entry. Same elevation class as C-27 (concrete-action
constraint encoded in field label) and C-28 (specificity constraint encoded in slot label):
C-38 is the row-label analogue -- the constraint that makes each TABLE 3 row self-describing as
a typed structural slot at generation time. C-36 tests whether the header declares the row type
contract; C-38 tests whether each row re-asserts that contract in its own label, independent of
the header. A table whose header declares typed slot keys but whose row labels are plain
transition-pair names passes C-36 and fails C-38 because the contract is not re-asserted at
the row level. A table whose every row label is prefixed with SLOT-KEY: passes C-38 regardless
of the header form, provided C-36 passes. C-38 fails automatically if C-36 fails.

**C-39 -- PHASE 3 CHASM decomposed into named structural subsections per required
element** (5 pts)
Source: V-03/V-04/V-05 R12 -- the structural difference between bold-item enumeration and
subsection decomposition for the three required C-03 chasm elements. C-03 tests whether all
three elements are present (incumbent defense, bridge condition, crossing signal); bold-item
enumeration (V-01/V-02) satisfies C-03 with all three items in an undivided PHASE 3 section,
but a missing item is a missing list item -- the surrounding section structure is complete
regardless. Named subsection decomposition (CHASM-A: Incumbent Defense, CHASM-B: Bridge
Condition, CHASM-C: Crossing Signal) makes each element a structural slot: the model cannot
complete PHASE 3 without encountering each subsection header, and a missing element leaves a
named structural gap with an empty or absent subsection -- the same enforcement pattern as C-17
(dedicated structural slot per aspirational criterion) applied to the three required chasm
elements. When PHASE 3 is undivided, per-element omission is invisible at the section level;
when PHASE 3 is divided into CHASM-A/B/C, per-element omission is structurally conspicuous.
C-03 tests that all three elements are present; C-39 tests whether each element has its own
named structural subsection, making per-element coverage a structural requirement rather than
an enumeration compliance check. A PHASE 3 with three bold-labeled items in a single prose
block passes C-03 and fails C-39; a PHASE 3 divided into CHASM-A, CHASM-B, and CHASM-C named
subsections passes C-39 regardless of whether any separate per-element instruction exists.
C-39 fails automatically if C-03 fails.

**C-40 -- PART 2 expansion decomposes into CHASM-A EXPANSION / CHASM-B EXPANSION /
CHASM-C EXPANSION structural subsections with PHASE 3 back-references** (5 pts)
Source: V-01 R13 -- the extension of the C-39 structural-slot enforcement pattern into the
expansion depth. C-39 tests whether PHASE 3 itself is divided into CHASM-A/CHASM-B/CHASM-C
named structural subsections, making per-element omission structurally conspicuous at the phase
level. V-01's PART 2 applies the same pattern one level deeper: the expansion section
decomposes into CHASM-A EXPANSION, CHASM-B EXPANSION, and CHASM-C EXPANSION with explicit
back-references to their PHASE 3 counterparts ("Expanding CHASM-A from PHASE 3 --"), carrying
each structural slot's identity forward into expansion depth. When PART 2 is an undivided
expansion block, a missing chasm element in the expansion is a missing list item -- invisible
at the section level even if PHASE 3's CHASM-A/B/C slots are structurally intact. When PART 2
decomposes into CHASM-A EXPANSION / CHASM-B EXPANSION / CHASM-C EXPANSION, a missing element
in the expansion is a missing named structural subsection -- same enforcement class as C-39,
applied one generation layer deeper. The back-reference ("Expanding CHASM-A from PHASE 3 --")
makes the structural identity of each slot explicit, ensuring the expansion cannot be completed
without naming the counterpart slot it expands. C-39 tests whether PHASE 3 has per-element
structural subsections; C-40 tests whether the expansion section mirrors those subsections with
back-references, enforcing per-element coverage in the expansion by structural slot count rather
than enumeration compliance. A PART 2 with undivided expansion prose fails C-40 regardless of
C-39 status; a PART 2 decomposed into CHASM-A EXPANSION / CHASM-B EXPANSION / CHASM-C
EXPANSION with PHASE 3 back-references passes C-40. C-40 fails automatically if C-39 fails.

**C-41 -- TABLE 1 Inertia ID column makes three contracts co-present per row: archetype
assignment, Incumbent Dependency, and Inertia ID citation** (5 pts)
Source: V-02 R13 -- the extension of TABLE 1 from two co-present contracts (C-01 + C-37) to
three by adding an Inertia ID column. C-37 tests whether TABLE 1 merges archetype assignment
(C-01) and displacement framing (C-26) into a single structural slot via the Incumbent
Dependency column -- two contracts co-present per row at generation time. V-02 adds a 4th
TABLE 1 column: "Inertia ID: [cite I-0X from SECTION A -- named inertia explaining this
archetype's resistance]," making the named inertia citation (C-11) a per-row fill contract
in TABLE 1 itself. The model must name each role's specific inertia ID at the same generation
step as its archetype assignment and incumbent dependency assignment. When the Inertia ID is
only in SECTION A (satisfying C-11), the citation is resolved once per archetype at the
section level and is not structurally active during TABLE 1 generation; when the Inertia ID
column is in TABLE 1, the citation contract is re-asserted per role at the row level --
generation-time co-presence at each TABLE 1 row, not just at the section level. Same
elevation class as C-37 (displaces incumbent dependency into TABLE 1 per-row contract)
applied to C-11: C-41 tests whether the inertia citation contract is structurally co-present
with archetype assignment at TABLE 1 generation time, not whether C-11 is satisfied
independently. A TABLE 1 with Incumbent Dependency column but no Inertia ID column passes
C-37 and fails C-41; a TABLE 1 with both Incumbent Dependency and Inertia ID columns
passes C-41 regardless of whether SECTION A or any separate section independently satisfies
C-11. Three contracts co-present per row: C-01 (archetype), C-37 (incumbent dependency),
C-41 (inertia ID). C-41 fails automatically if C-37 fails or C-11 fails.

**C-42 -- PART 2 CHASM expansion subsections carry named inertia ID citations per
slot** (5 pts)
Source: V-01 R14. Axis A. Extends C-40's structural-slot enforcement with the inertia-carry
dimension. C-40 tests whether PART 2 decomposes into CHASM-A EXPANSION / CHASM-B EXPANSION /
CHASM-C EXPANSION with PHASE 3 back-references, making per-element omission structurally
conspicuous. C-42 tests whether each expansion subsection also cites the named inertia ID
(I-0X from SECTION A) that drives resistance at that specific chasm element -- the inertia
preventing the bridge condition from forming (CHASM-A), the inertia the bridge must overcome
(CHASM-B), the inertia whose weakening the crossing signal confirms (CHASM-C). The inertia
citation in PART 2 is not a free-standing field but an in-situ re-assertion at expansion slot
generation time, independent of SECTION A's prior inertia ID assignment and independent of
TABLE 1's per-row Inertia ID column (C-41). When PART 2 expansion subsections carry no inertia
citation, the inertia carry stops at the PHASE 3 level even though each CHASM-A/B/C slot was
structurally intact; when each PART 2 subsection cites I-0X for its slot, the inertia backbone
propagates into expansion depth, making inertia reasoning structurally active at three
consecutive generation levels: SECTION A (C-11), TABLE 1 (C-41), and PART 2 expansion (C-42).
Same generation-time enforcement class as C-41 applied one layer deeper. C-42 fails
automatically if C-40 fails or C-11 fails.

**C-43 -- TABLE 1 row labels use SLOT-KEY: prefix to re-assert three-contract type at row
level** (5 pts)
Source: V-02 R14. Axis B. TABLE 1 analogue of C-38 (TABLE 3 SLOT-KEY: prefix). C-41 makes
three contracts co-present per TABLE 1 row at generation time: archetype assignment (C-01),
Incumbent Dependency (C-37), Inertia ID citation (C-41). The table header carries the
three-contract type contract at table-entry time, but the model must hold it from the header
across all subsequent row fills from memory. The SLOT-KEY: prefix on each TABLE 1 row label
re-asserts the three-contract type at the row generation moment independently of the header:
the model re-encounters the full contract fresh at each row rather than relying on the header
remaining active. Same elevation class as C-38 (TABLE 3 row-level SLOT-KEY: re-assertion)
applied to TABLE 1: C-43 tests whether the three-contract co-presence enforced by C-41 is
re-asserted at the row level by label, not only declared at the header level. A TABLE 1 with
three columns but plain role-name row labels passes C-41 and fails C-43 because the
three-contract type contract is not re-asserted at each row. A TABLE 1 whose row labels carry
SLOT-KEY: prefix (e.g., "SLOT-KEY: [Role] -- [Archetype] -- [Incumbent Dependency] --
[Inertia ID]") passes C-43. C-43 fails automatically if C-41 fails.

**C-44 -- PART 5 intervention rows include "Targets inertia: [cite I-0X]" field per
entry** (5 pts)
Source: V-03 R14. Axis C. Structural enabler for C-13 full-pass. C-13 requires inertia ID
citations in at least four downstream locations including intervention rationale; V-01/V-02
were PARTIAL on C-13 because PART 5 lacked a per-row inertia citation field, leaving
intervention rationale unanchored to a specific inertia ID at generation time. V-03 introduces
a "Targets inertia: [cite I-0X from SECTION A -- named inertia this intervention is designed
to overcome]" field per PART 5 row, making the inertia citation a per-row generation-time
contract in the intervention section itself, not in a separate section or preamble. Completing
the PART 5 table requires a named inertia ID for each intervention row; the constraint is
embedded in the field label at the row level, making omission structurally incompatible with
filling the slot. Same elevation class as C-27 (churn register field label encodes
concrete-action constraint), C-28 (spread mechanism slot label encodes specificity constraint):
C-44 is the PART 5 analogue -- the per-row field label that makes inertia citation structurally
required at intervention row generation time rather than satisfied once at section level.
C-05 tests whether an intervention ranking section is present; C-13 tests whether inertia IDs
are cited in intervention rationale (among four required locations); C-44 tests whether that
citation is enforced at generation time by a per-row labeled field in PART 5 itself. A PART 5
table with intervention rows but no "Targets inertia:" field passes C-05 and may pass C-13 if
other downstream locations provide sufficient citations, but fails C-44 because the per-row
field constraint is absent. A PART 5 table whose rows include "Targets inertia: [cite I-0X]"
passes C-44 regardless of whether any separate inertia citation instruction exists. C-44 fails
automatically if C-11 fails or C-05 fails.

**C-45 -- Phase-close footer carries per-phase displacement ledger fields** (5 pts)
Source: V-01 R15. Axis A. Phase-Close Displacement Ledger. Each adoption phase close
(PHASE 1-6) contains mandatory footer fields encoding the displacement arc at that phase
boundary: `Incumbent position after this phase: [explicit displacement status]` and `Inertia
ID this phase overcame: [I-0X from SECTION A -- or N/A if pre-chasm phase where inertia is
latent rather than overcome]`. PHASE 3 (Chasm) uses the variant form `Inertia ID defending
THE INCUMBENT at this boundary: [I-0X]` rather than the overcome form, reflecting the
non-adoption crossing-attempt framing: PHASE 3 does not overcome an inertia, it identifies
which inertia is defending the incumbent's position at the crossing boundary. When phase-close
footers are absent, the displacement arc is a narrative claim in the phase bodies but not a
per-phase structural account; when each phase closes with these fields, the model must
explicitly account for incumbent displacement status and inertia lifecycle at every phase
boundary, making the displacement arc traceable across the full adoption sequence as a ledger
rather than an assertion. Same enforcement class as C-44 (per-row labeled field makes inertia
citation structurally required at generation time), applied at phase-close level: completing
a phase without closing the displacement ledger leaves a structurally visible gap. C-25 tests
whether phase headers enforce Rogers sequence; C-26 tests whether incumbent-first framing
is present; C-45 tests whether the displacement arc and inertia lifecycle are accounted for at
each phase close via mandatory footer fields, not merely framed at document opening. A
document with C-26 incumbent-first framing and C-25 phase headers but no phase-close footer
fields passes C-25 and C-26 and fails C-45 because displacement accounting ends at the frame
level and is not carried forward per phase. A document whose every phase close carries
`Incumbent position after this phase:` + `Inertia ID this phase overcame:` footer fields
(and whose PHASE 3 close uses the variant form) passes C-45. C-45 fails automatically if
C-11 fails or C-26 fails.

**C-46 -- PART 3 churn register row labels use SLOT-KEY: prefix to re-assert trigger-mitigation
contract at row level** (5 pts)
Source: V-02 R15. Axis B. PART 3 analogue of C-43 (TABLE 1 SLOT-KEY: prefix) and C-38 (TABLE
3 SLOT-KEY: prefix). C-27 tests whether the churn register field label encodes the
concrete-action constraint at generation time ("Retention intervention: [one concrete action
that reduces reversion probability]"); the field label is present at the column or register
header level. C-46 tests whether each PART 3 churn row label carries a SLOT-KEY: prefix --
"SLOT-KEY: [Role] -- churn entry" -- re-asserting the trigger-mitigation type contract at
the row generation moment independently of the header: the model re-encounters the typed slot
contract fresh at each churn row fill rather than holding the column-header contract from
memory. Gate J audit language explicitly references "SLOT-KEY: churn entries" when C-46 is
active, making the row-level enforcement visible in the gate audit itself rather than only in
the content body. Same elevation class as C-38 and C-43: C-46 is the PART 3 row-label
analogue -- the third application of the SLOT-KEY: re-assertion pattern to a structural table
(TABLE 3 -> C-38, TABLE 1 -> C-43, PART 3 -> C-46). A churn register with field labels
satisfying C-27 but plain role-name row labels fails C-46 because the typed contract is
declared at the column level only and is not re-asserted at each row. A churn register whose
every row is prefixed "SLOT-KEY: [Role] -- churn entry" passes C-46 regardless of whether any
separate per-row instruction exists. C-46 fails automatically if C-06 fails or C-27 fails.

**C-47 -- PART 4 champion network rows use SLOT-KEY: prefix to re-assert double-anchor type
contract at row level** (5 pts)
Source: V-02 R16. Axis B. PART 4 analogue of C-43 (TABLE 1 SLOT-KEY: prefix), C-38 (TABLE 3
SLOT-KEY: prefix), and C-46 (PART 3 SLOT-KEY: prefix) -- the fourth application of the
row-level SLOT-KEY: re-assertion pattern. C-14 tests whether each champion entry carries both
the archetype-bridge anchor and the inertia ID anchor (double-anchored champion rationale);
the double-anchor type contract is declared at the PART 4 section level. C-47 tests whether
each PART 4 champion row label carries a SLOT-KEY: prefix -- "SLOT-KEY: [Role] -- champion
entry" -- re-asserting the double-anchor type contract at the row generation moment
independently of the section header: the model re-encounters the full archetype-bridge + inertia
ID contract fresh at each champion row fill rather than holding the section-header contract
from memory. Gate I audit language explicitly references "SLOT-KEY: champion entries" when
C-47 is active, making the row-level enforcement visible in the gate audit. PART 4 header
declares the typed row-key contract at section-entry time; C-47 tests whether that contract
is re-asserted at the individual row level by label, independent of the header -- the same
generation-time pressure distinction as C-38 (TABLE 3 header vs. row) and C-43 (TABLE 1 header
vs. row). A PART 4 with double-anchored champion entries satisfying C-14 but plain role-name
row labels fails C-47 because the double-anchor type contract is not re-asserted at each row.
A PART 4 whose champion row labels carry SLOT-KEY: prefix passes C-47. Gate I references
"SLOT-KEY: champion entries" explicitly in the audit language, making omission auditable at the
gate level. C-47 fails automatically if C-04 fails or C-14 fails.

**C-48 -- PART 2 expansion subsections carry displacement state field per slot** (5 pts)
Source: V-01 R16. Axis A. Extends C-45's phase-close displacement ledger into expansion slot
depth. C-45 places a displacement ledger footer at each of the six phase closes, making the
displacement arc traceable across phase boundaries; C-42 places an inertia ID citation in each
PART 2 CHASM-A/B/C EXPANSION subsection, making inertia carry traceable at expansion depth.
C-48 fills the remaining gap: each PART 2 expansion subsection (CHASM-A EXPANSION, CHASM-B
EXPANSION, CHASM-C EXPANSION) carries a mandatory `Incumbent position at this chasm element:
[explicit displacement status at this element]` field. When C-45 footers are present but C-48
fields are absent, the displacement arc is accounted for at phase-boundary granularity only --
the chasm's internal structure (three expansion slots) has no per-slot displacement accounting.
When C-48 fields are present, the displacement state is explicitly recorded at chasm-element
depth, making the incumbent's position traceable at three structural levels: document open
(C-26), phase close (C-45), and chasm expansion slot (C-48). Same enforcement class as C-42
(inertia carry into expansion slot) applied to the displacement state dimension: completing
a PART 2 expansion subsection without the displacement state field leaves a structurally visible
gap. C-45 tests whether phase-close footers carry displacement ledger fields; C-42 tests whether
expansion slots carry inertia citations; C-48 tests whether expansion slots also carry
displacement state, making expansion slots three-field structural slots (Named Inertia in effect
via C-42, Incumbent position at this chasm element via C-48, prose body). C-48 fails
automatically if C-40 fails or C-45 fails.

**C-49 -- SECTION A carries DOWNSTREAM CITATION CONTRACT mapping each inertia ID to required
downstream citation sinks** (5 pts)
Source: V-03 R16. Axis C. After SECTION A's inertia table, a DOWNSTREAM CITATION CONTRACT
block explicitly maps each named inertia ID (I-01 through I-05) to the downstream structural
locations where that ID is contractually required to appear: phase-close displacement ledger
(C-45), PART 2 expansion inertia citation (C-42), PART 3 churn rows (C-46), PART 4 champion
rows (C-47), PART 5 intervention rows (C-44). Gate H audits against the declared contract rows
(each I-0X row listing its required citation positions) rather than performing a free-form scan
for ID presence -- making the audit condition a named contract violation ("contract row I-03
requires citation in PART 2 CHASM-A EXPANSION; no such citation found") rather than a coverage
judgement. Without a DOWNSTREAM CITATION CONTRACT, Gate H must infer required citation
positions from C-13's general requirement (four downstream location types) -- a coverage check
that cannot distinguish which inertia ID was expected where. With the contract declared at
SECTION A generation time, the model sees the required citation sinks immediately after
generating each I-0X entry, making the downstream citation commitment visible at the source
rather than only discoverable at gate audit. The DOWNSTREAM CITATION CONTRACT also makes C-49
dependent on the completeness of the downstream structural apparatus: a contract row for I-03
citing CHASM-A EXPANSION as a required sink requires C-42 (expansion inertia carry) to be
active before the contract is verifiable -- contract rows whose sinks are not structurally
present are unverifiable commitments. C-11 tests whether named inertia IDs are assigned per
archetype; C-13 tests whether IDs appear in downstream locations; C-49 tests whether the
source-to-sink mapping is declared as a named contract in SECTION A itself, making gate audit
a contract-compliance check rather than a coverage scan. A SECTION A with inertia IDs
satisfying C-11 but no DOWNSTREAM CITATION CONTRACT fails C-49; a SECTION A whose
DOWNSTREAM CITATION CONTRACT maps each I-0X to named downstream citation positions passes
C-49. Gate H references the contract rows explicitly in its audit language. C-49 fails
automatically if C-11 fails or C-13 fails.

**C-50 -- DOWNSTREAM CITATION CONTRACT rows carry Gate H Status field per I-0X** (5 pts)
Source: V-03 R17. Axis C. Each I-0X row in the SECTION A DOWNSTREAM CITATION CONTRACT (C-49)
carries a `Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation]` fill
field that is left unfilled at document generation time and completed by Gate H during audit.
C-49 turns Gate H's audit condition into a named contract violation rather than a coverage
judgement; C-50 turns each contract row into the audit record for that I-0X by co-locating the
compliance status with the commitment declaration. Without C-50, the contract (SECTION A) and
the audit record (Gate H section or SECTION K) occupy separate structural regions, requiring
an evaluator to cross-reference contract rows against a separate audit section to determine
per-I-0X compliance. With C-50, each contract row is self-reporting: the declaration of the
required sinks and the verdict on their satisfaction appear in the same slot, making compliance
verifiable by reading SECTION A alone. Same elevation class as C-34 (double-anchoring the
correction mechanism across structural levels): C-50 co-locates the audit target and the audit
result within the contract slot rather than distributing them across structural regions. A
SECTION A with DOWNSTREAM CITATION CONTRACT satisfying C-49 but no Gate H Status fields per
contract row passes C-49 and fails C-50 because the compliance record is external to the
contract. A SECTION A whose contract rows include `Gate H Status:` fill fields that Gate H
completes during audit passes C-50. Gate H's audit protocol explicitly populates these fields
rather than writing a separate coverage summary, making the contract a live audit ledger rather
than a static declaration. C-50 fails automatically if C-49 fails.

**C-51 -- SECTION K mirrors DOWNSTREAM CITATION CONTRACT compliance as terminal contract
record** (5 pts)
Source: V-02 R17. Axis B. SECTION K's terminal audit section includes a per-I-0X compliance
mirror of the DOWNSTREAM CITATION CONTRACT (C-49), recording for each inertia ID whether its
contractually required citation sinks were satisfied and at which structural locations. C-20
requires SECTION K to consolidate gate outcomes; C-30 requires SECTION K to carry per-gate
execution stamps; C-51 extends SECTION K's completeness obligation to cover per-I-0X contract
compliance -- making SECTION K the canonical terminal record for both gate execution (C-20/C-30)
and citation contract satisfaction. Without C-51, SECTION K closes the audit with gate outcome
rows but leaves citation contract compliance distributed across Gate H's section and C-50's
contract row status fields; with C-51, the contract lifecycle is complete at three structural
levels: source declaration at SECTION A generation time (C-49), per-row audit co-location during
Gate H execution (C-50), and terminal compliance record at SECTION K (C-51). A downstream
verifier reading only SECTION K can determine both whether all gates executed and whether all
I-0X citation contracts were satisfied, without navigating to SECTION A or Gate H. Same
elevation class as C-30 (terminal section as proof of audit execution) applied to contract
compliance: C-51 tests whether SECTION K is sufficient as a contract compliance proof
independent of the contract declaration location. The SECTION K mirror records compliance
results (PASS / FAIL per I-0X per required sink and the structural location where the citation
was found or expected) -- it does not duplicate the contract declaration itself. A SECTION K
with per-gate execution stamps satisfying C-30 but no per-I-0X citation compliance rows fails
C-51; a SECTION K that includes a citation contract compliance table with one row per I-0X
passes C-51. C-51 fails automatically if C-49 fails or C-20 fails.

**C-52 -- Per-I-0X CORRECTION BLOCK label identifies the specific failed contract row** (5 pts)
Source: V-01 R18. Axis A. When Gate H marks a DOWNSTREAM CITATION CONTRACT row FAIL via the
C-50 Gate H Status field, the CORRECTION BLOCK produced for that failure carries a label
identifying the specific I-0X contract row that triggered it (e.g., `CORRECTION BLOCK -- I-03
CITATION CONTRACT VIOLATION`). Correction granularity matches citation granularity: one failed
I-0X contract row produces one CORRECTION BLOCK labeled for that I-0X. Without C-52, a Gate H
correction block for a citation failure is structurally a generic CORRECTION BLOCK -- its
connection to the failed I-0X contract row requires cross-referencing the Gate H Status field
in SECTION A. With C-52, the CORRECTION BLOCK is self-identifying: the I-0X identity is in
the label, and no SECTION A cross-reference is needed to understand which contract failure
triggered the correction. The per-I-0X label also makes C-52 auditable by structural inspection:
a reviewer counting labeled CORRECTION BLOCKs can verify that every SECTION A contract row
carrying a FAIL status produced its own corresponding CORRECTION BLOCK, without reading the
BEFORE/AFTER content. C-19 tests whether a CORRECTION BLOCK with BEFORE and AFTER fields
appears inline; C-52 tests whether a Gate H citation failure triggers a CORRECTION BLOCK that
carries the failing I-0X in its label, matching correction identity to contract row identity.
A CORRECTION BLOCK without a per-I-0X label in the block header satisfies C-19 but fails
C-52; a CORRECTION BLOCK labeled `CORRECTION BLOCK -- I-03 CITATION CONTRACT VIOLATION`
satisfies both C-52 and C-19. C-52 fails automatically if C-50 fails.

**C-53 -- SECTION K carries DISPLACEMENT ARC INTEGRITY CHECK proving phase-open/phase-close
chain consistency** (5 pts)
Source: V-02 R18. Axis B. SECTION K includes a DISPLACEMENT ARC INTEGRITY CHECK block that
verifies the displacement arc's internal consistency across phase boundaries: the `Incumbent
position after this phase` field from each phase-close footer (C-45) must chain coherently --
the incumbent's displacement state at phase N close must be compatible with its position framing
at phase N+1 open, and the terminal phase-6 close must reflect a displacement outcome consistent
with the document's opening incumbent declaration (C-26). Without C-53, SECTION K proves gate
execution (C-30) and citation contract satisfaction (C-51), but displacement arc continuity
across the six-phase sequence is not terminally auditable -- verifying it requires re-reading
all six phase-close footer fields and tracing the chain manually. With C-53, SECTION K's
DISPLACEMENT ARC INTEGRITY CHECK summarizes the phase-open/phase-close chain and asserts chain
consistency or names the specific phase boundary where continuity breaks (e.g., "PHASE 3 close
claims inertia I-03 defending incumbent; PHASE 4 open does not acknowledge I-03's prior
presence -- arc discontinuity at PHASE 3/4 boundary"). Closes the structural gap left by C-45
(per-phase displacement accounting) and R17's Axis A: C-53 makes the displacement narrative's
internal coherence a terminal audit outcome recorded in SECTION K, not only a phase-body reading
task. C-45 tests whether each phase close carries displacement ledger fields; C-51 tests whether
SECTION K carries citation contract compliance; C-53 tests whether SECTION K also verifies
the chain those C-45 fields form across all six phases, making SECTION K self-sufficient as
proof of gate execution (C-30), citation compliance (C-51), and displacement arc continuity
(C-53) simultaneously. A SECTION K that passes C-30 and C-51 but contains no DISPLACEMENT
ARC INTEGRITY CHECK fails C-53; a SECTION K containing a DISPLACEMENT ARC INTEGRITY CHECK
that asserts or denies phase-open/phase-close chain consistency passes C-53. C-53 fails
automatically if C-45 fails or C-20 fails.

**C-54 -- DOWNSTREAM CITATION CONTRACT rows carry Protected behavior column per I-0X** (5 pts)
Source: V-03 R18. Axis C. Each I-0X row in the SECTION A DOWNSTREAM CITATION CONTRACT carries
a `Protected behavior: [the specific displacement-committed behavior this inertia ID must not
revert -- the concrete thing the team is committing to maintain once this inertia is overcome]`
field, declared at contract generation time before any phase body is written. C-49 declares
which citation sinks are required; C-54 declares what displacement stake is at risk if those
citations are absent -- making each I-0X contract row a three-field structural slot: required
citation sinks (C-49), Gate H Status (C-50), and Protected behavior (C-54). The Protected
behavior column commits displacement stakes at source: the model must name what would be lost
if I-0X's inertia persists, before writing any phase body that depends on that inertia being
overcome. V-04/V-05 carry Protected behavior into correction labels: when Gate H fires a
CORRECTION BLOCK for a failed I-0X contract row (C-52), the CORRECTION BLOCK label includes
the Protected behavior, making each repair a targeted displacement-commitment correction
("CORRECTION BLOCK -- I-03 CITATION CONTRACT VIOLATION -- Protected behavior: [named
behavior] at risk") rather than a structural compliance fix. The Protected behavior field also
enriches the C-51 SECTION K citation mirror: each I-0X compliance row in SECTION K can
reference the Protected behavior, making SECTION K sufficient to answer not only whether
citations are present but whether the displacement commitments they represent are secured.
C-49 tests whether the DOWNSTREAM CITATION CONTRACT maps I-0X to citation sinks; C-54 tests
whether each contract row also declares the Protected behavior stake, making the contract a
displacement-commitment record rather than a citation coverage map. A DOWNSTREAM CITATION
CONTRACT satisfying C-49 and C-50 but carrying no Protected behavior field per row passes C-49
and C-50 and fails C-54 because the displacement stakes are not committed at source. A
DOWNSTREAM CITATION CONTRACT whose rows include `Protected behavior:` fields passes C-54
regardless of whether any separate displacement-stakes instruction exists. C-54 fails
automatically if C-49 fails.

**C-55 -- CORRECTION BLOCK label carries Protected behavior when Gate H fires on I-0X
failure** (5 pts)
Source: V-01/V-04/V-05 R19. Axis A carry-forward. C-52 requires that a Gate H CORRECTION
BLOCK label identifies the specific I-0X contract row that triggered it; C-55 requires that
the same label also carries the Protected behavior declared in C-54's contract row for that
I-0X. When both C-52 and C-55 are active, the full label form is `CORRECTION BLOCK -- I-0X
CITATION CONTRACT VIOLATION -- Protected behavior: [named behavior]`, making each correction
self-describing as a displacement-commitment repair: the label names the contract row (C-52)
and the displacement stake at risk (C-55) in the same label, without requiring SECTION A
cross-reference. Without C-55, the correction label identifies what failed structurally
(I-0X contract row) but not what is at risk in displacement terms (the commitment that
failure leaves unfulfilled). With C-55, a reviewer reading the label alone can determine
both the citation failure identity and its displacement consequence -- the correction is
structurally self-sufficient as a displacement-commitment fault record. C-52 tests whether
the label names the I-0X; C-55 tests whether the label also carries the Protected behavior,
completing the label as a displacement-commitment fault record rather than a contract
compliance ID. A CORRECTION BLOCK labeled `CORRECTION BLOCK -- I-03 CITATION CONTRACT
VIOLATION` satisfies C-52 and fails C-55 because the displacement stake is not in the label.
A label of the form `CORRECTION BLOCK -- I-03 CITATION CONTRACT VIOLATION -- Protected
behavior: [EM workflow]` satisfies both C-52 and C-55. The Protected behavior value is
copied verbatim from the SECTION A contract row's C-54 field -- no restatement or
paraphrase; the label is self-consistent with its source declaration at contract generation
time. C-55 fails automatically if C-52 fails or C-54 fails.

**C-56 -- SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior per I-0X
compliance row** (5 pts)
Source: V-02/V-04/V-05 R19. Axis B carry-forward. C-51 requires SECTION K to mirror
per-I-0X contract compliance (PASS/FAIL per required citation sink and structural location);
C-56 requires each I-0X compliance row in the SECTION K CITATION CONTRACT COMPLETION RECORD
to also carry the Protected behavior declared at C-54 for that I-0X. When C-51 and C-56 are
both active, SECTION K's CITATION CONTRACT COMPLETION RECORD becomes a displacement-commitment
certificate: each I-0X row records whether citations were satisfied (C-51 compliance field) and
what displacement commitment is confirmed or left open by that satisfaction status (C-56
Protected behavior field). Without C-56, SECTION K answers "were the required citations
present?" but not "what displacement stake was secured or left at risk?" With C-56, SECTION K
is sufficient to answer both questions in the same row, without navigating to SECTION A's
contract declaration. This completes the three-tier displacement accountability chain: Protected
behavior is committed at source (C-54), named in each correction label when Gate H fires (C-55),
and certified in the terminal record regardless of gate outcome (C-56 -- present whether the
I-0X row records PASS or FAIL). C-51 tests whether SECTION K carries per-I-0X compliance rows;
C-56 tests whether those rows also carry the Protected behavior, making SECTION K a
displacement-commitment certificate rather than a coverage compliance record alone. A SECTION K
CITATION CONTRACT COMPLETION RECORD satisfying C-51 but carrying no Protected behavior fields
per I-0X row passes C-51 and fails C-56. A SECTION K whose per-I-0X compliance rows include
`Protected behavior: [named behavior]` passes C-56 regardless of whether any separate
terminal-section instruction exists. Protected behavior value matches the SECTION A source
declaration verbatim. C-56 fails automatically if C-51 fails or C-54 fails.

**C-57 -- SECTION K arc discontinuity triggers ARC CORRECTION BLOCK with mandatory
BEFORE/AFTER structure** (5 pts)
Source: V-03/V-05 R19. Axis C. C-53's DISPLACEMENT ARC INTEGRITY CHECK detects
phase-open/phase-close chain discontinuity and names the boundary where continuity breaks
(MISMATCH verdict); the baseline stops at detection. C-57 closes the repair loop: a MISMATCH
verdict in C-53 triggers an ARC CORRECTION BLOCK inserted in the document body before the
pre-verification declaration (the same structural insertion point as Gate H/I/J citation
correction blocks), carrying mandatory BEFORE and AFTER fields that show the discontinuous
phase-close displacement value and the corrected displacement state. SECTION K arc integrity
verdict gains three enumerated states when C-57 is active: PASS (chain is internally
consistent, no correction required), FAIL (discontinuity detected, no correctable repair is
possible -- records the boundary and displacement values that conflict), and CORRECTED
(discontinuity detected, ARC CORRECTION BLOCK fired before the pre-verification boundary,
BEFORE field names the breaking phase-close value, AFTER field names the corrected
displacement state, and correction location is cited in SECTION K). Without C-57, a MISMATCH
in C-53's check leaves a displacement arc inconsistency as a named audit finding with no
structural repair obligation -- the discontinuity is detected terminally but not corrected in
the body. With C-57, arc discontinuities and citation failures enter the same mandatory-repair
lifecycle: both trigger correction blocks with BEFORE/AFTER structure before the verification
boundary, both record their repair state in SECTION K, and both are terminally verifiable by
reading SECTION K alone. This closes the structural asymmetry between citation failures (Gate
H detects and forces repair, C-52 labels the correction) and arc discontinuities (C-53 detects
but baseline imposes no repair obligation). C-53 tests whether SECTION K performs the arc
integrity check and states PASS or MISMATCH; C-57 tests whether a MISMATCH triggers a mandatory
ARC CORRECTION BLOCK with BEFORE/AFTER fields in the document body, and whether SECTION K
records the CORRECTED state with a correction-location citation. A SECTION K with
DISPLACEMENT ARC INTEGRITY CHECK recording MISMATCH but no ARC CORRECTION BLOCK in the
document body passes C-53 and fails C-57 because the detection-to-repair loop is not closed.
A SECTION K recording CORRECTED with a corresponding ARC CORRECTION BLOCK containing BEFORE
and AFTER fields at the correct structural location passes C-57. C-57 fails automatically if
C-53 fails.

---

**Max composite: 320 --> 335. Golden threshold (80%): 268 pts.**

Dependency chains:
```
C-16 (audit exists) -> C-18 (revision obligation) -> C-19 (content visible)

C-07 (spread mechanism exists) -> C-28 (slot label encodes constraint)
                               -> C-31 (table uses named transition-pair row keys)
                                       -> C-36 (header types rows as slot keys)
                                               -> C-38 (row labels use SLOT-KEY: prefix)
C-03 (chasm section present) -> C-39 (CHASM-A/B/C subsections)
                                      -> C-40 (PART 2 expansion mirrors CHASM-A/B/C)
                                              -> C-42 (expansion subsections carry I-0X citations)
                                              -> C-48 (expansion subsections carry displacement state)
C-11 (named inertia per archetype) -> C-29 (question-based citation enforcement)
C-20 (terminal section exists) -> C-30 (gate execution proof in terminal section)
C-18 (revision obligation) -> C-32 (mechanism anchor in body)
                                    -> C-34 (double-anchored at gate + boundary)
C-29 (answer-form) + C-32 (mechanism anchor) -> C-33 (co-present)
                                                      -> C-35 (STRUCTURAL CONTRACT)
C-01 (all roles mapped) -> C-26 (incumbent-first framing)
                                -> C-37 (TABLE 1 incumbent dependency column)
                                        -> C-41 (TABLE 1 inertia ID column; also requires C-11)
                                                -> C-43 (TABLE 1 row labels use SLOT-KEY: prefix)
C-11 + C-05 -> C-44 (PART 5 "Targets inertia:" per-row field)
C-11 + C-26 -> C-45 (phase-close displacement ledger footer fields)
                     -> C-48 (PART 2 expansion displacement state; also requires C-40)
C-06 + C-27 -> C-46 (PART 3 row labels use SLOT-KEY: prefix)
C-04 + C-14 -> C-47 (PART 4 champion row labels use SLOT-KEY: prefix)
C-11 + C-13 -> C-49 (SECTION A DOWNSTREAM CITATION CONTRACT)
                     -> C-50 (contract rows carry Gate H Status field)
                             -> C-52 (per-I-0X CORRECTION BLOCK label on contract failure)
                                     -> C-55 (CORRECTION BLOCK label carries Protected behavior; also requires C-54)
C-49 + C-20 -> C-51 (SECTION K mirrors citation contract compliance)
                     -> C-56 (SECTION K compliance rows carry Protected behavior; also requires C-54)
C-45 + C-20 -> C-53 (SECTION K DISPLACEMENT ARC INTEGRITY CHECK)
                     -> C-57 (MISMATCH triggers ARC CORRECTION BLOCK with BEFORE/AFTER)
C-49 -> C-54 (DOWNSTREAM CITATION CONTRACT rows carry Protected behavior column)
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
| C-24 Invariant names falsification condition (both cases) | 5 | Aspirational |
| C-25 Phase headers enforce Rogers sequence | 5 | Aspirational |
| C-26 Incumbent-first displacement framing | 5 | Aspirational |
| C-27 Field label encodes concrete-action constraint | 5 | Aspirational |
| C-28 Spread mechanism label encodes specificity constraint | 5 | Aspirational |
| C-29 Question-based inertia citation enforcement | 5 | Aspirational |
| C-30 Per-gate execution stamps in terminal section | 5 | Aspirational |
| C-31 Spread mechanism table uses named transition-pair rows | 5 | Aspirational |
| C-32 Correction mechanism presence anchor in document body | 5 | Aspirational |
| C-33 Answer-form enforcement co-present with mechanism anchor | 5 | Aspirational |
| C-34 Correction mechanism anchor double-anchored at gate + boundary | 5 | Aspirational |
| C-35 STRUCTURAL CONTRACT mandates answer-form + mechanism anchor co-presence | 5 | Aspirational |
| C-36 TABLE 3 header types rows as structural slot keys | 5 | Aspirational |
| C-37 TABLE 1 Incumbent Dependency column co-present with archetype assignment | 5 | Aspirational |
| C-38 TABLE 3 row labels use SLOT-KEY: prefix at row level | 5 | Aspirational |
| C-39 PHASE 3 decomposed into CHASM-A/B/C structural subsections | 5 | Aspirational |
| C-40 PART 2 expansion mirrors CHASM-A/B/C with PHASE 3 back-references | 5 | Aspirational |
| C-41 TABLE 1 Inertia ID column -- three contracts co-present per row | 5 | Aspirational |
| C-42 PART 2 expansion subsections carry named inertia ID citations per slot | 5 | Aspirational |
| C-43 TABLE 1 row labels use SLOT-KEY: prefix -- three-contract type re-asserted per row | 5 | Aspirational |
| C-44 PART 5 "Targets inertia:" field per intervention row | 5 | Aspirational |
| C-45 Phase-close footer carries per-phase displacement ledger fields | 5 | Aspirational |
| C-46 PART 3 churn register row labels use SLOT-KEY: prefix at row level | 5 | Aspirational |
| C-47 PART 4 champion rows use SLOT-KEY: prefix -- double-anchor type re-asserted per row | 5 | Aspirational |
| C-48 PART 2 expansion subsections carry displacement state field per slot | 5 | Aspirational |
| C-49 SECTION A DOWNSTREAM CITATION CONTRACT maps each I-0X to required citation sinks | 5 | Aspirational |
| C-50 DOWNSTREAM CITATION CONTRACT rows carry Gate H Status field per I-0X | 5 | Aspirational |
| C-51 SECTION K mirrors DOWNSTREAM CITATION CONTRACT compliance as terminal contract record | 5 | Aspirational |
| C-52 Per-I-0X CORRECTION BLOCK label identifies the specific failed contract row | 5 | Aspirational |
| C-53 SECTION K DISPLACEMENT ARC INTEGRITY CHECK proves phase-open/phase-close chain consistency | 5 | Aspirational |
| C-54 DOWNSTREAM CITATION CONTRACT rows carry Protected behavior column per I-0X | 5 | Aspirational |
| C-55 CORRECTION BLOCK label carries Protected behavior when Gate H fires on I-0X failure | 5 | Aspirational |
| C-56 SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior per I-0X compliance row | 5 | Aspirational |
| C-57 SECTION K arc discontinuity triggers ARC CORRECTION BLOCK with mandatory BEFORE/AFTER structure | 5 | Aspirational |
