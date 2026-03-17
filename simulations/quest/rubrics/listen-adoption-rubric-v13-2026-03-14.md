`listen-adoption-rubric-v13-2026-03-14.md` written. Here's what was extracted and why:

---

**Three new criteria from R12 excellence signals. Max 230 → 245.**

**C-37 — TABLE 1 includes an Incumbent Dependency column co-present with archetype assignment** (5 pts)
V-01/V-05 were the only R12 variations to merge C-01 and C-26 at TABLE 1 generation time. V-02/V-03/V-04 satisfied C-26 via standalone SECTION B — the incumbent is named before TABLE 1 but is not structurally active during it. An Incumbent Dependency column makes displacement framing the fill contract for that column at the exact generation step as archetype assignment. C-37 tests whether the two-criteria merge is encoded in TABLE 1 itself, not whether the incumbent is named alongside it. Dependency: C-26.

**C-38 — TABLE 3 row labels use SLOT-KEY: prefix to re-assert typed contract at row level** (5 pts)
C-36 places the typed-slot-key contract in the header, visible once at table-entry time. The SLOT-KEY: prefix (V-02/V-04/V-05) re-asserts the contract at each row label individually — the model re-encounters it at each generation point rather than once at the header. Row-label analogue of C-27 and C-28: the contract is independently present at every fill step. Dependency: C-36.

**C-39 — PHASE 3 CHASM decomposed into named structural subsections per required element** (5 pts)
V-01/V-02 satisfy C-03 by bold-item enumeration in an undivided PHASE 3; a missing element is a missing list item. V-03/V-04/V-05 decompose PHASE 3 into CHASM-A/CHASM-B/CHASM-C, making each of the three required elements a structural slot — per-element omission leaves a named structural gap. Same enforcement class as C-17 (dedicated structural slot per aspirational criterion), applied to the three chasm elements. Dependency: C-03.

**Dependency chain additions:**
```
C-03 -> C-39
C-26 -> C-37
C-36 -> C-38
```

The spread mechanism chain now reads `C-07 -> C-28 -> C-31 -> C-36 -> C-38` (five deep). Projected scores for R13 V-05 carrying all three new axes: 240/245 (C-19 paradox persists).
ll three elements present but without structural gaps
that signal omission. When PHASE 3 is undivided, a missing element is a missing list item;
when PHASE 3 is divided into CHASM-A/B/C, a missing element is a missing named subsection
heading — structurally incompatible with completing the section. Same elevation class as
C-17 (dedicated structural slot per aspirational criterion): C-39 applies the
structural-slot enforcement pattern to the three required chasm elements. Dependency: C-03.

**Dependency chain additions:**
```
C-03  -> C-39
C-26  -> C-37
C-36  -> C-38
```

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
An explicit spread mechanism named per phase transition (Innovator -> Early Adopter,
Early Adopter -> Early Majority, etc.). The mechanism must be feature-specific — a named signal,
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
variations where all gates pass on first attempt; see C-30 for the complementary criterion and
C-32 for the mechanism-presence criterion.

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

**C-31 — Spread mechanism table uses named transition-pair row labels as structural
slots** (5 pts)
Source: V-02/V-03 PARTIAL on C-07 — both variations addressed spread mechanism through
phase-body questions rather than TABLE 3, producing contextual coverage of one transition
while leaving the other three without dedicated structural slots. V-01, V-04, and V-05
passed C-07 via TABLE 3 with explicit named rows for each transition pair
(Innovator -> Early Adopter, Early Adopter -> Early Majority, Early Majority -> Late
Majority, Late Majority -> Laggard), making per-transition omission structurally
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

**C-34 — Correction mechanism anchor double-anchored at gate level and verification
boundary** (5 pts)
Source: V-05 R11 — the distinction between a single-location C-32 anchor and a dual-location
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
simultaneously — that neither level alone is load-bearing because both are present. A document
with only a pre-verification declaration but no per-gate footers passes C-32 and fails C-34;
a document with per-gate footers in H/I/J but no pre-verification declaration passes C-32 and
fails C-34; a document with a dedicated MECHANISM ANCHOR section but no per-gate footers passes
C-32 and fails C-34; a document with both per-gate footers in each gate section and a
pre-verification declaration passes C-34 regardless of whether any separate mechanism anchor
section exists. C-34 fails automatically if C-32 fails.

**C-35 — STRUCTURAL CONTRACT explicitly names answer-form and mechanism anchor as mandatory
co-present requirements** (5 pts)
Source: V-04/V-05 R11 — the distinction between implicit co-presence and architecturally
mandated co-presence. V-01/V-02/V-03 satisfied C-33 through implicit co-presence: baseline
C-29 carried and C-32 introduced separately; both mechanisms present in the document and their
structural conjunction satisfies the rubric, but no part of the document asserts that both are
required together. V-04/V-05 introduced a STRUCTURAL CONTRACT — an explicit block that names
both the answer-form questions (C-29) and the MECHANISM STATE line (C-32) as mandatory
co-present requirements — making C-33 architecturally required rather than emergent: no
trade-off between the two mechanisms is possible without violating the STRUCTURAL CONTRACT
itself. C-33 tests whether C-29 and C-32 are co-present; C-35 tests whether their co-presence
is explicitly declared as mandatory at the structural contract level, closing the gap between
"both happen to be here" and "both are required to be here." A document that passes C-29 and
C-32 in separate, unconnected structural regions passes C-33 and fails C-35 because the
co-presence is observable but undeclared. A document with a STRUCTURAL CONTRACT naming both
mechanisms as mandatory co-present requirements passes C-35 regardless of where in the document
the STRUCTURAL CONTRACT appears, provided it is prior to the content generation sections it
governs. C-35 fails automatically if C-33 fails.

**C-36 — TABLE 3 row labels typed as structural slot keys in the table header** (5 pts)
Source: V-05 R11 enhancement of C-31. C-31 tests whether the four named transition-pair rows
exist as structural slots, enforcing per-transition coverage by slot count — four rows named
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

**C-37 — TABLE 1 includes an Incumbent Dependency column co-present with archetype
assignment** (5 pts)
Source: V-01/V-05 R12 — the structural difference between standalone SECTION B (V-02/V-03/V-04)
and TABLE 1 integration. C-26 tests whether the simulation opens with incumbent-first
displacement framing; both SECTION B placement and TABLE 1 column integration satisfy C-26.
The distinction is generation-time co-presence: SECTION B names the incumbent before TABLE 1
begins, making the displacement lens available in context but not structurally active during
archetype assignment. An Incumbent Dependency column in TABLE 1 places the displacement lens
as a fill contract for every row in the table, forcing the model to name each role's specific
incumbent dependency at the same generation step as its archetype assignment — merging C-01
and C-26 into a single structural slot. A simulation with SECTION B and TABLE 1 archetype rows
achieves C-01 and C-26 in separate structural regions; a simulation whose TABLE 1 contains an
Incumbent Dependency column achieves C-01 and C-26 as co-present generation-time contracts at
the table level. C-37 tests whether the merging of archetype assignment and displacement framing
is encoded structurally in TABLE 1, not whether the incumbent is named somewhere before or
alongside TABLE 1. A TABLE 1 with a generic "Notes" or "Displacement" column that is not
contract-typed as incumbent dependency fails C-37; a TABLE 1 with an Incumbent Dependency
column labeled to encode each role's specific dependency on the incumbent workflow or tool
passes C-37. C-37 fails automatically if C-26 fails.

**C-38 — TABLE 3 row labels use SLOT-KEY: prefix to re-assert typed contract at row
level** (5 pts)
Source: V-02/V-04/V-05 R12 — the extension of C-36 to row-level contract re-assertion. C-36
tests whether the TABLE 3 table header declares the rows as typed structural slot keys, making
the contract visible once at table-entry time. The SLOT-KEY: prefix applies the contract to
each individual row label: "SLOT-KEY: Innovator -> Early Adopter," "SLOT-KEY: Early Adopter ->
Early Majority," etc. When the header is the only typed-slot-key declaration, the model
encounters the contract once and must hold it across all subsequent row fills from memory; when
each row label carries SLOT-KEY:, the model re-encounters the typed-slot-key contract at the
generation moment for that row independently, making the contract continuously present at each
fill step rather than once at table entry. Same elevation class as C-27 (concrete-action
constraint encoded in field label) and C-28 (specificity constraint encoded in slot label):
C-38 is the row-label analogue — the constraint that makes each TABLE 3 row self-describing as
a typed structural slot at generation time. C-36 tests whether the header declares the row type
contract; C-38 tests whether each row re-asserts that contract in its own label, independent of
the header. A table whose header declares typed slot keys but whose row labels are plain
transition-pair names passes C-36 and fails C-38 because the contract is not re-asserted at
the row level. A table whose every row label is prefixed with SLOT-KEY: passes C-38 regardless
of the header form, provided C-36 passes. C-38 fails automatically if C-36 fails.

**C-39 — PHASE 3 CHASM decomposed into named structural subsections per required
element** (5 pts)
Source: V-03/V-04/V-05 R12 — the structural difference between bold-item enumeration and
subsection decomposition for the three required C-03 chasm elements. C-03 tests whether all
three elements are present (incumbent defense, bridge condition, crossing signal); bold-item
enumeration (V-01/V-02) satisfies C-03 with all three items in an undivided PHASE 3 section,
but a missing item is a missing list item — the surrounding section structure is complete
regardless. Named subsection decomposition (CHASM-A: Incumbent Defense, CHASM-B: Bridge
Condition, CHASM-C: Crossing Signal) makes each element a structural slot: the model cannot
complete PHASE 3 without encountering each subsection header, and a missing element leaves a
named structural gap with an empty or absent subsection — the same enforcement pattern as C-17
(dedicated structural slot per aspirational criterion) applied to the three required chasm
elements. When PHASE 3 is undivided, per-element omission is invisible at the section level;
when PHASE 3 is divided into CHASM-A/B/C, per-element omission is structurally conspicuous.
C-03 tests that all three elements are present; C-39 tests whether each element has its own
named structural subsection, making per-element coverage a structural requirement rather than
an enumeration compliance check. A PHASE 3 with three bold-labeled items in a single prose
block passes C-03 and fails C-39; a PHASE 3 divided into CHASM-A, CHASM-B, and CHASM-C named
subsections passes C-39 regardless of whether any separate per-element instruction exists.
C-39 fails automatically if C-03 fails.

---

**Max composite: 230 -> 245. Golden threshold (80%) unchanged.**

Dependency chains:
```
C-16 (audit exists) -> C-18 (revision obligation) -> C-19 (content visible)

C-07 (spread mechanism exists) -> C-28 (slot label encodes constraint)
                               -> C-31 (table uses named transition-pair row keys)
                                       -> C-36 (header types rows as slot keys)
                                               -> C-38 (row labels use SLOT-KEY: prefix)
C-03 (chasm section present) -> C-39 (CHASM-A/B/C subsections)
C-11 (named inertia per archetype) -> C-29 (question-based citation enforcement)
C-20 (terminal section exists) -> C-30 (gate execution proof in terminal section)
C-18 (revision obligation) -> C-32 (mechanism anchor in body)
                                    -> C-34 (double-anchored at gate + boundary)
C-29 (answer-form) + C-32 (mechanism anchor) -> C-33 (co-present)
                                                      -> C-35 (STRUCTURAL CONTRACT)
C-01 (all roles mapped) -> C-26 (incumbent-first framing)
                                -> C-37 (TABLE 1 incumbent dependency column)
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
| C-34 Correction mechanism anchor double-anchored at gate + boundary | 5 | Aspirational |
| C-35 STRUCTURAL CONTRACT mandates answer-form + mechanism anchor co-presence | 5 | Aspirational |
| C-36 TABLE 3 header types rows as structural slot keys | 5 | Aspirational |
| C-37 TABLE 1 Incumbent Dependency column co-present with archetype assignment | 5 | Aspirational |
| C-38 TABLE 3 row labels use SLOT-KEY: prefix at row level | 5 | Aspirational |
| C-39 PHASE 3 decomposed into CHASM-A/B/C structural subsections | 5 | Aspirational |
| **Total** | **245** | |
