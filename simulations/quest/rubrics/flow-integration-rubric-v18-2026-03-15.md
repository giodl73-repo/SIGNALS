# flow-integration Rubric — v18

---

**Two new criteria from R17:**

**C-45 — C-43 failure-class conditional sub-type: SHOULD failure mechanism (5 pts)**
Closes Q1 (R17) SHOULD sub-type. RFC 2119 SHOULD introduces *conditional-recommendation*
epistemic weakening: "recommended but not required" converts the unconditional consequence
boundary to a conditional recommendation — the consequence statement becomes "it is
recommended that this become a blocker" rather than "it becomes a blocker". The failure
mechanism is conditionality. SHOULD independently fails C-37 (no unconditional consequence
boundary named — a recommendation is not a constraint), C-39 (unconditional form requirement
violated by conditional modal), C-40 (register-neutrality broken — conditional modal weakening
is not a surface-register property but a semantic-content property), and C-43 (SHOULD named
as failure-class modal). The SHOULD mechanism is distinct from the MAY mechanism (C-46): SHOULD
fails via conditionality (not required but recommended); MAY fails via discretionality (optional
— no recommendation at all). Both produce identical cascade failure across C-37/C-39/C-40/C-43
but via semantically distinct weakening pathways. V-01 (R17) established the SHOULD failure
boundary empirically: "Undocumented integration calls SHOULD become ship-blockers at integration
review and cannot be cleared without a completed trace" → conditional-recommendation form →
C-37 FAIL (SHOULD = conditional recommendation, not unconditional constraint), C-39 FAIL
(cascade + independently broken), C-40 FAIL (conditional modal weakening), C-43 FAIL (named
failure-class modal); all WHY-block stakes-anchor criteria collapse from the single modal
substitution. Requires C-43.

**C-46 — C-43 failure-class discretionary sub-type: MAY failure mechanism and compound
conditionality (5 pts)**
Closes Q1 (R17) MAY sub-type. RFC 2119 MAY introduces *discretionary-possibility* epistemic
weakening: "optional" converts the consequence boundary to a discretionary possibility — the
consequence statement becomes "it is permitted for this to be a blocker" rather than "it is a
blocker". The failure mechanism is optionality, which is semantically distinct from SHOULD's
conditionality: SHOULD says "you ought to, but you may not"; MAY says "you may, but you need
not". Both fail C-40/C-43 but via different epistemic-weakening pathways. When MAY is
compounded with a conditional clause ("if not documented"), the anchor exhibits *compound
conditionality*: (1) the MAY modal introduces discretionary weakening; (2) the conditional
clause further subordinates the already-weakened consequence to a documentary condition; two
independent disqualifying mechanisms are present simultaneously. Crucially, each mechanism
alone suffices for disqualification — compound form does not require both mechanisms to apply,
but confirms that neither can rescue the other: the conditional clause does not strengthen a
weakened modal, and the modal weakness is not mitigated by an attached conditional. The
structural finding is mechanism independence: compound conditionality exposes two failure
surfaces but collapses to the same cascade outcome as any single C-43 failure-class modal.
V-02 (R17) established the MAY failure boundary and the compound conditionality pattern:
"authentication, rate limits, retry behavior, and error propagation gaps MAY become ship-blockers
at integration review if not documented" → MAY modal (mechanism 1: discretionary-possibility)
+ "if not documented" clause (mechanism 2: conditional subordination); both mechanisms
independently named in failure analysis; identical cascade outcome to V-01 (SHOULD) despite
distinct mechanism pair. Requires C-43 and C-45.

**Ceiling: 272 → 282 (+10). Aspirational total: 192 pts (C-08–C-46).**

**Updates to existing criteria:**
No existing criteria updated this round.

**Closed questions:**
- Q1 (R14): **PERMISSIVE** — consequence-form + delivery-phase marker satisfies C-37.
- Q1 (R15): **PERMISSIVE** — stakes anchor alone satisfies C-37; concern enumeration not required.
- Q1 (R16): **NAMED** — RFC-modal MUST/SHALL confirmed as unconditional obligation class; passes C-40 at stronger-than-indicative obligation force.
- Q1 (R17): **CLOSED (NEGATIVE)** — SHOULD (conditional-recommendation mechanism, V-01) and MAY (discretionary-possibility mechanism, V-02) both empirically confirmed to fail C-40 and C-43; two distinct sub-types of the C-43 failure class named; cascade failure across C-37/C-39/C-40/C-43 identical for both sub-types.

**Open questions for R18:**
- Q1 (R18): Does a MAY-only anchor (without conditional clause) confirm modal-only MAY failure independent of compound conditionality? V-02 (R17) used compound form (MAY + "if not documented"); a minimal MAY probe isolating modal-only failure would complete the single-mechanism boundary for the discretionary sub-type.
- Q2 (R18): Does V-03 (three-sentence inertia dominant) score C-44 at ceiling? Carried from R17 Q2 — V-03 table was not completed.

---

**New in v4:** C-16, C-17 codify the two structural patterns identified in Round 3.
C-16 rewards expert persona declaration before Stage 1 — the zero-cost enrichment
mechanism that sharpens call discovery and auth depth without touching any structural
guarantee. C-17 rewards in-block rate limit completeness — the architecture that
resolves the C-11/C-14 registry trade-off by keeping full rate limit data inside the
call block rather than in an external registry, making both criteria simultaneously
achievable at full score.

**New in v5:** C-18, C-19 codify the two structural patterns identified in Round 4.
C-18 rewards explicit secondary positioning of any cross-stage aggregation structure —
the instruction that a fan-out registry is populated FROM the call block and is not the
authoritative source, which makes coexistence with C-17 permanently safe rather than
convention-dependent. C-19 rewards expert persona four-obligation scope — the full
declaration covering forgotten calls, assumed-to-work entries, unknown-system
placeholders, and delegation chain risk, which reaches call categories that a minimal
two-obligation persona structurally cannot discover.

**New in v6:** C-20, C-21 codify the two structural patterns identified in Round 5.
C-20 rewards an unconditional cross-stage stage with an explicit no-structures default
path — the architecture that satisfies C-18 regardless of model output shape, making
secondary positioning a structural guarantee rather than a conditional one that only
fires when a cross-stage structure happens to appear. C-21 rewards inventory flag
alignment to persona obligation categories — the format instruction that makes the
C-19 persona's discoveries structurally traceable as flag markers in the inventory
entry itself, rather than only declared in a preamble; without this alignment, a model
can declare all four obligations and still produce an inventory that does not record
which obligation each entry answers to.

**New in v7:** C-22, C-23 codify the two structural patterns identified in Round 6.
C-22 rewards C-19/C-21 vocabulary unification — the constraint that flag marker names
in C-21 mirror the exact obligation terms used in the C-19 persona declaration (whether
canonical or non-standard), making the persona-to-inventory semantic trace structurally
enforced rather than dependent on a reviewer's implicit mapping; C-21 passes on
semantic correspondence alone, but C-22 requires vocabulary identity — the persona
term and the flag name are the same token. C-23 rewards the unnumbered coda pattern
as a universal Stage 4 adapter — the architectural rule that any numbered outer frame
(phases, stages, flat sections) achieves C-20 by appending an unnumbered coda suffix
after the last numbered element, with the coda carrying no position number and
therefore composing with any existing numbering scheme without renumbering or
displacement; this generalizes Stage 4 from a specific numbered position to an
additive composition primitive that works identically across all outer frame styles.

**New in v8:** C-24, C-25 codify the two structural patterns identified in Round 7.
C-24 rewards the four-obligation table schema — the format upgrade that converts the
C-19 obligation declaration from a prose list into a structured table where presence
or absence of each obligation is mechanically auditable as a present or absent row;
a prose list of four obligations passes C-19 but not C-24 because a model can omit
an obligation in output and the omission is visible only to a reader who recounts the
items; with a four-row table the missing row is structurally absent and detectable
without annotation. C-25 rewards schema-aligned C-22 enforcement — the pattern where
the C-21 inventory's flag marker column headers are the same tokens as the corresponding
row terms in the C-24 obligation table, making token identity mechanically verifiable
by table schema comparison rather than by reading prose or scanning code blocks; this
is the strongest C-22 enforcement mechanism, resolving the execution risk noted for the
declarative V-03 pattern (a model can produce semantically corresponding labels even
when instructed otherwise), and requires C-24 as a structural prerequisite because
there must be an obligation table whose row terms serve as the canonical token source.

**New in v9:** C-26, C-27, C-28 codify the three structural patterns identified in Round 8.
C-26 rewards schema-only C-25 enforcement — the pattern where an explicit schema
instruction (the flag column headers ARE the Obligation Term values from the C-24 table)
makes token identity structurally enforced without a `VOCABULARY RULE` block; the
structural mechanism subsumes the declarative one; a rubric that requires a `VOCABULARY
RULE` block to pass C-25 is over-specifying because schema comparison alone is the
verification mechanism and does not depend on a prose rule the model must remember to
follow. C-27 rewards dual-surface canonical-substitution prohibition — the pattern
where non-standard terms require both enforcement surfaces: schema alignment (C-25)
detects substitution at the table surface because a column header that does not match
its obligation row term is visible by comparison; an explicit YOU MUST NOT prohibition
block names the specific canonical forbidden tokens and blocks substitution at the prose
and annotation surface; the two surfaces are complementary because schema catches
structural failure and prohibition blocks the semantic workaround; a generic vocabulary
instruction that does not name the specific forbidden canonical tokens does not achieve
C-27. C-28 rewards the explicit terminal-position formula for the C-23 unnumbered coda —
the pattern confirmed definitive in Round 8 (Q1 resolved) where coda terminal placement
requires both a header annotation naming the last numbered element and a prose sentence
prohibiting between-elements placement; C-23 allows an unnumbered coda anywhere in the
frame; C-28 closes the mid-sequence gap confirmed in R7 V-04 (unnumbered coda placed
between Phase 2 and Phase 3 — a structural failure, not a stylistic one); the formula
is outer-frame-agnostic and applies identically across phase, stage, and section frames
by substituting the frame unit name and last element identifier.

**New in v10:** C-29, C-30 codify the two structural patterns identified in Round 9.
C-29 settles the C-26 instruction minimum question open since R8: schema-only C-25
enforcement is not achieved by any unambiguous schema-aligned instruction — it requires
the explicit ARE directive asserting that column headers ARE the Obligation Term values;
a cross-reference table describes the mapping but does not assert identity; the ARE form
is the minimum because it converts correspondence into a structural identity constraint
the model must satisfy structurally. C-30 settles the C-27 prohibition scope question
open since R8: the dual-surface prohibition is not achieved by distributing one YOU MUST
NOT per non-standard term across table rows — all substituted canonical tokens must be
named together in a single comprehensive block; the single-block architecture creates
one scannable prohibition surface; per-term inline distribution fragments the surface
and does not achieve equivalent dual-surface coverage.

**New in v11:** C-31, C-32 codify the two structural patterns identified in Round 10.
C-31 settles the C-30 block composition question open since R9: the single YOU MUST NOT
block required by C-27/C-30 must enumerate each substituted canonical token explicitly
by name inside the block itself; a table-reference shorthand that places the block in
a single location but delegates token enumeration to the obligation table ("any of the
canonical Obligation Term values listed in the table above") does not achieve C-27
because the prohibition surface is not self-contained — a reviewer must cross-reference
the table to determine which specific tokens are prohibited, fragmenting the verification
surface; V-01 established the failure boundary (single block, table-reference shorthand
→ C-27/C-30 FAIL) and R8 V-05 confirms the pass boundary (single block, explicit named
tokens → C-27 PASS). C-32 settles the C-29 capitalisation and sentence form question
open since R9: the ARE directive must use the uppercase ARE keyword in an assertive
declarative sentence; lowercase "are" in a non-assertive construction does not satisfy
C-29 because it describes correspondence rather than asserting identity; the uppercase
assertive ARE form is the minimum for schema-only C-25 enforcement; V-01 (R10)
established the pass boundary (uppercase ARE assertive → PASS) and the failure boundary
(lowercase are descriptive → FAIL).

**New in v12:** C-33, C-34 codify the two structural patterns identified in Round 11.
C-33 settles the C-32 subject-form question open since R10: the C-32 ARE directive must
use the multi-subject collective plural form asserting identity for all flag column
headers together; any valid multi-subject plural ARE construction satisfies C-33 —
exact subject phrasing is not required; the structural requirement is plural collective
subject + uppercase ARE + single assertion covering all headers; the per-item IS form
("Each flag column header IS one of the Obligation Term values") is uppercase assertive
but does not satisfy C-29 or C-32 because ARE is the named keyword; V-01 (R11)
established the failure boundary (IS per-item form → FAIL); V-01 (R12) established
subject-form flexibility (alternate plural ARE subject → PASS). C-34 settles the C-31
enumeration-scope question open since R11: the inline enumeration must name every
*substituted* canonical token — canonical terms retained without substitution and new
categories with no canonical equivalent are outside C-34's scope; partial enumeration
of the substituted subset does not satisfy C-31; the prohibition surface must be
self-contained for the substituted subset; V-02 (R11) established the failure boundary
(3-of-4 substituted tokens → FAIL); V-02 (R12) established the per-substitution scope
(substituted-only enumeration on a five-row table → PASS).

**New in v13:** C-35, C-36 codify the two structural patterns identified in Round 12.
C-35 settles the C-24 extended obligation set scalability question open since R11: the
C-24 obligation table schema scales to any N >= 4 obligation categories; "one row per
obligation category" is the structural rule — the four-row canonical default is not a
hard count but the minimum for the four-obligation baseline; a table with five or more
rows satisfies C-24 when it has exactly one row per obligation category and the
structural auditability property is preserved (each category's presence or absence is
detectable as a present or absent row without reading prose); a table with fewer rows
than obligation categories does not pass regardless of total row count; V-02 (R12)
established the pass boundary (five-row extended obligation set → C-24 PASS); requires
C-24. C-36 settles the motivational framing question raised by V-03: a WHY THIS TRACE
DISCIPLINE EXISTS block prepended before the expert persona declaration is a structurally
additive pattern that does not require schema changes to any existing stage, gate,
obligation table, or flag column; its presence anchors the trace rationale at the top
of the document above the persona boundary; V-03 confirmed structural neutrality — all
criteria from C-01 through C-34 scored identically with and without the framing block;
V-01 (R13) confirmed the minimal content standard — a purpose statement naming what the
trace verifies and when documentation gaps become consequential satisfies C-36.

**New in v14:** C-37, C-38 codify the two structural patterns identified in Round 13.
C-37 settles the stakes anchor question from V-01 (R13): the C-36 framing block must
include a temporal or delivery-phase anchor naming the consequence boundary; a purpose-
statement-only framing block that describes what the trace does without a consequence
boundary passes C-36 but not C-37; the temporal form "before the feature ships" was the
first confirmed realization; V-01 (R13) established the pass boundary (temporal form +
declarative unconditional framing → PASS) and the failure boundary (conditional modal
"can become ship-blockers" → FAIL). C-38 settles the C-36 obligation-count-agnostic
scope question: when C-35 is in play (N > 4 obligation categories), the C-36 framing
block satisfies C-36 without enumerating the extended obligation categories; canonical-
term framing covering the four-concern baseline satisfies C-36 regardless of obligation
set extension; V-02 (R13) established the pass boundary (five-row extended obligation
set + canonical four-concern framing → C-36 PASS).

**New in v15:** C-39 codifies the consequence-form delivery-phase equivalence identified
in Round 14. C-39 settles the C-37 form-surface question from V-01 (R14): consequence-
form with an explicit delivery-phase marker ("become ship-blockers at integration review")
satisfies C-37 equivalently to interval-before temporal form ("before the feature ships");
both forms convert the framing from description to constraint; the declarative,
unconditional framing requirement is non-negotiable for both forms — conditional modal
form weakens the consequence statement to a possibility and does not name a constraint
boundary; V-01 (R14) established the pass boundary: consequence-form + explicit delivery-
phase marker + declarative unconditional framing → C-37 PASS; C-39 codifies this
form-surface equivalence as a distinct criterion because C-37's pass condition names
"temporal or delivery-phase anchor" without specifying a realized form, and C-39 closes
that ambiguity by confirming the consequence-form + delivery-phase-marker surface as a
concrete delivery-phase anchor realization. The Q1 (R14) resolution (consequence-form
satisfies C-37) also closes the WHY block form question that had remained open since R13.
The Q1 (R15) resolution confirms PERMISSIVE: concern enumeration is not required for
C-37 — stakes anchor alone satisfies on both temporal and consequence-form surfaces.
cleared without a completed trace" — no temporal interval marker ("before the feature
ships") present, but an explicit delivery-phase marker ("at integration review") and a
declarative, unconditional consequence statement ("become ship-blockers"). Adjudication:
the phrase "at integration review" is an explicit delivery-phase anchor naming the phase
at which the gap becomes a blocker; "become ship-blockers" is declarative and
unconditional — no conditional modal weakening; the framing converts from description
to constraint equivalently to the temporal form. Q1 resolved PERMISSIVE: consequence-
form with delivery-phase marker + declarative unconditional framing satisfies C-37.
C-39 codifies this equivalence as a distinct criterion because it closes the form-surface
ambiguity in C-37 — C-37's pass condition names "temporal or delivery-phase anchor" and
C-39 confirms the consequence-form + delivery-phase-marker surface as a concrete
realization of the delivery-phase anchor class, with the unconditional declarative
requirement as the non-negotiable form condition.

**New in v16:** C-40, C-41, C-42 codify the three structural patterns identified in Round 15.
C-40 settles the C-39 register question from V-03: consequence-form delivery-phase anchor
satisfies C-39 in any surface register — formal declarative, conversational, or imperative —
provided unconditional constraint meaning is preserved; register is a stylistic property of
the sentence surface and does not affect the structural C-39 pass conditions (consequence-form
+ delivery-phase marker + unconditional constraint meaning); V-03 established the pass
boundary (conversational/imperative register → C-39 PASS). C-41 settles the inertia-framing
question from V-04: obligation-scope discovery-failure framing context in the WHY block does
not disqualify C-37 or C-39 when a consequence-form delivery-phase anchor is present; inertia
framing is a background narrative property, not a structural property that overrides or
substitutes for the stakes anchor; V-04 established the pass boundary (inertia-framing context
+ consequence-form anchor → C-37/C-39 PASS) and the failure surface (inertia framing alone,
no stakes anchor → C-37 FAIL remains). C-42 codifies the highest-information WHY block form
identified in V-05 (247/247 ceiling): consequence-form delivery-phase anchor + explicit concern
enumeration; the combination satisfies C-37, C-39, and C-42 simultaneously — the stakes anchor
supplies the delivery-phase constraint boundary and the concern enumeration supplies explicit
scope of which gaps become consequential; Q1 (R15) confirmed concern enumeration is not
required for C-37, making C-42 the next excellence tier above stakes-only form.

**New in v17:** C-43, C-44 codify the two structural patterns identified in Round 16.
C-43 settles the RFC-modal register question from V-02: RFC 2119 MUST and SHALL are a
specific named unconditional obligation class within C-40's register-neutrality scope;
the key finding is that MUST/SHALL are stronger-obligation than indicative form (RFC
2119: MUST = "absolute requirement", SHALL = "absolute obligation"), not merely
equivalent; zero epistemic weakening is introduced; C-43 also closes the RFC-modal
failure boundary: weakening RFC modals — SHOULD ("recommended but not required"), MAY
("optional"), NEED NOT ("not required") — do NOT satisfy C-40 because they convert
unconditional constraint meaning into conditional or discretionary meaning; V-02 (R16)
established the pass boundary (MUST/SHALL with consequence-form delivery-phase anchor
→ 232/232, C-40 PASS, explicit verdict). C-44 establishes the inertia-saturation form:
a WHY block with three inertia sentences (inertia-dominant, 3:1 ratio) followed by a
single anchor-close sentence still passes C-41 — inertia framing quantity does not
affect C-37/C-39 evaluation at any sentence count; when the anchor-close sentence also
contains concern enumeration, the block simultaneously satisfies C-37, C-39, C-41, and
C-42 — the inertia-dominant variant of the highest-information form, providing maximum
justificatory framing before the constraint anchor; V-03 (R16) probed this form.

**New in v18:** C-45, C-46 codify the two structural patterns identified in Round 17.
C-45 closes Q1 (R17) SHOULD sub-type: SHOULD introduces conditional-recommendation
epistemic weakening ("recommended but not required") — distinct from MAY's discretionary-
possibility mechanism — and empirically fails C-37, C-39, C-40, and C-43 via a single
conditional-modal substitution; the entire stakes-anchor criterion chain collapses from
this one modal choice; V-01 (R17) established the empirical failure boundary. C-46 closes
Q1 (R17) MAY sub-type and introduces the compound-conditionality finding: MAY introduces
discretionary-possibility weakening ("optional" — not even recommended), a semantically
distinct failure mechanism from SHOULD's conditionality; when MAY is compounded with a
conditional clause ("if not documented"), two independent disqualifying mechanisms are
present simultaneously — each alone suffices for disqualification, and neither can rescue
the other in compound construction; V-02 (R17) established the MAY failure boundary and
confirmed the compound conditionality pattern. The R17 C-43 failure-class taxonomy is
now complete: MUST/SHALL → unconditional obligation class (C-43 pass); SHOULD →
conditional-recommendation sub-type (C-45); MAY → discretionary-possibility sub-type
(C-46); compound conditionality pattern (C-46) closes the multi-mechanism failure surface.

---

## Essential Criteria (60 pts total)

| ID | Criterion | Category | Tier | Pass Condition |
|----|-----------|----------|------|----------------|
| C-01 | **Call inventory** | correctness | essential | At minimum two calls documented; call types explicit; "unknown system" and "assumed to work" entries present when applicable. |
| C-02 | **Authentication documentation** | correctness | essential | Every call in C-01 has an explicit auth entry; "unknown" acceptable only if flagged as a gap. |
| C-03 | **Request and response format** | correctness | essential | Method + key fields documented per call in separate labeled positions; single merged cell does not pass. |
| C-04 | **Error propagation path** | correctness | essential | Each call has an explicit error-disposition statement; "a call that never fails" still requires a disposition. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Tier | Pass Condition |
|----|-----------|----------|------|----------------|
| C-05 | **Rate limit exposure** | depth | recommended | At least one rate-limit entry per external system; no-limit systems called out as exposure. |
| C-06 | **Retry and idempotency analysis** | depth | recommended | Retry strategy stated for each transiently-failing call; non-idempotent calls without mitigation listed as findings. |
| C-07 | **Gap inventory** | format | recommended | At least one structured finding section with call-ID references and gap-type labels. |

---

## Aspirational Criteria (192 pts total)

| ID | Criterion | Category | Tier | Pass Condition |
|----|-----------|----------|------|----------------|
| C-08 | **Severity ranking** | depth | aspirational | Every finding carries a severity label with a one-line rationale; MEDIUM and LOW findings not exempt. |
| C-09 | **Remediation sketch** | behavior | aspirational | At least one actionable fix per HIGH finding; specific to call context, not generic advice. |
| C-10 | **Inventory-first gate** | format | aspirational | Inventory section appears first and is complete before any per-call analysis; analysis before inventory does not pass. |
| C-11 | **Single-concern phase isolation** | format | aspirational | Each section labeled with exactly one concern; reviewer can locate all content for any concern without scanning elsewhere. |
| C-12 | **Gate-enforced per-call completion** | format | aspirational | At least one section uses an explicit all-calls-covered completion condition; implicit or voluntary does not pass. |
| C-13 | **Per-call section-level concern exclusion** | format | aspirational | Every concern section in at least one call block carries a single-concern declaration and named exclusion of all other concerns within the section itself. |
| C-14 | **Five-concern per-call completion checklist** | format | aspirational | Five-item checklist in every call block; explicitly gates the next call block; three-or-fewer-concern checklist does not pass. |
| C-15 | **Late-call inventory discipline** | format | aspirational | Explicit instruction requiring newly discovered calls be entered into the inventory before their block is opened. |
| C-16 | **Expert persona declaration** | format | aspirational | Named expert persona appears before the inventory gate naming the domain and at least two discovery obligations; generic preamble without domain-specific obligations does not pass. |
| C-17 | **In-block rate limit completeness** | format | aspirational | Every call block contains a rate limit section with limit value, burst risk, and throttle response as separate labeled fields; registry-pointer-only section does not pass. |
| C-18 | **Cross-stage structure explicit secondary positioning** | format | aspirational | Every cross-stage aggregation structure carries an explicit source-of-truth demotion naming all three properties — populated-from, not-authoritative, not-required-for-assessment; structure present without this statement does not pass; traces with no cross-stage structures pass by default. |
| C-19 | **Expert persona four-obligation scope** | format | aspirational | Persona names all four discovery obligation categories — forgotten calls, assumed-to-work entries, unknown-system placeholders, delegation chain risk — before the inventory gate; two or three categories passes C-16 but not C-19. |
| C-20 | **Unconditional cross-stage stage with no-structures default** | format | aspirational | A dedicated stage for cross-stage aggregation structure handling fires unconditionally and contains an explicit "no structures produced" default instruction; C-18 is thereby satisfied regardless of whether the model produces any aggregation structure; traces where cross-stage handling is conditional on a structure having appeared do not pass. |
| C-21 | **Inventory flag alignment to persona obligation categories** | format | aspirational | Inventory entry format includes named flag fields corresponding to all C-19 obligation categories; flags make persona discoveries structurally traceable in the inventory; inventory entries that correctly declare all C-19 obligations in preamble but carry no per-entry flag fields do not pass; flag count must match obligation category count (four flags for four categories, five flags for five categories, etc.). |
| C-22 | **C-19/C-21 vocabulary unification** | format | aspirational | The flag marker names used in C-21 are the same tokens as the obligation terms declared in C-19 — canonical-to-canonical or non-standard-to-matching-non-standard; a C-21 flag name that semantically corresponds to but does not match the C-19 persona term does not pass; vocabulary identity within the variation is the contract, not cross-variation standardization. |
| C-23 | **Unnumbered coda as universal cross-stage adapter** | format | aspirational | The C-20 cross-stage stage is implemented as an unnumbered coda appended after the last numbered element of the outer frame; the coda carries no position number and does not displace or renumber any existing element; this pattern must be applied when the outer frame is numbered (phases, stages, numbered sections); a numbered cross-stage element that displaces an existing position or forces renumbering does not pass. |
| C-24 | **Obligation table schema** | format | aspirational | The C-19 obligation declaration is formatted as a structured table with exactly one row per obligation category; presence or absence of each obligation is structurally auditable as a present or absent row; a prose list of obligations passes C-19 but not C-24; the obligation table must appear before the inventory gate; row count equals obligation category count — four categories require four rows, N categories require N rows; C-24 is a structural prerequisite for C-25. |
| C-25 | **Schema-aligned C-22 enforcement** | format | aspirational | The C-21 inventory's flag marker column headers are the same tokens as the corresponding row terms in the C-24 obligation table; token identity is mechanically verifiable by table schema comparison — a header/row-term mismatch is visible without reading prose or code blocks; declarative C-22 (text instruction or `VOCABULARY RULE` block) passes C-22 but not C-25; requires C-24; this is the strongest C-22 enforcement mechanism. |
| C-26 | **Schema-only C-25 enforcement** | format | aspirational | The C-25 schema alignment is achieved by explicit schema instruction alone without a `VOCABULARY RULE` block; the instruction specifies that inventory flag column headers ARE the Obligation Term values from the C-24 table — token identity is structurally enforced at the format level, not at the prose level; a rubric that mandates a `VOCABULARY RULE` block to pass C-25 over-specifies the enforcement mechanism; schema identity instruction alone is sufficient and is the cleaner implementation; requires C-24 and C-25. |
| C-27 | **Dual-surface canonical-substitution prohibition** | format | aspirational | When non-standard obligation terms replace canonical ones, C-22/C-25 coverage requires both surfaces: (1) schema alignment (C-25) detects term substitution at the table surface — column header vs. row term mismatch visible by comparison without reading prose; (2) an explicit YOU MUST NOT prohibition block names the specific canonical tokens that are forbidden in this trace, blocking semantic substitution at the prose and annotation surface; a generic vocabulary instruction that does not name specific forbidden canonical tokens does not satisfy C-27; requires C-24 and C-25. |
| C-28 | **Explicit terminal-position formula** | format | aspirational | The C-23 coda header includes the canonical formula: `*(no [frame-unit] number — appended after [last-element], the last numbered [frame-unit])*`; a supporting prose sentence confirms: "It does not appear between any two numbered [frame-units]; it does not displace or renumber any existing element"; both surfaces required — header annotation anchors structural position, prose sentence closes the between-elements gap; C-23 requires only an unnumbered coda; C-28 requires the full two-surface formula; formula is outer-frame-agnostic; requires C-23. |
| C-29 | **C-26 explicit ARE directive requirement** | format | aspirational | The C-26 schema-only enforcement instruction must use an explicit ARE directive of the form "the flag column headers ARE the Obligation Term column values above — use those exact tokens as column headers"; a cross-reference mapping table that describes obligation-term-to-column-header correspondence without the explicit ARE keyword does not satisfy C-26 and therefore does not satisfy C-29; the ARE form asserts identity — the cross-reference form describes correspondence; identity assertion is the minimum for schema-only enforcement; requires C-26. |
| C-30 | **C-27 single-block comprehensive prohibition** | format | aspirational | The C-27 dual-surface prohibition requires all substituted canonical tokens to be named together in a single YOU MUST NOT block; per-term inline prohibition distributed across obligation table rows — one prohibition column or cell per substituted canonical token — does not create a unified prohibition surface and does not satisfy C-27 or C-30; the single-block architecture makes the complete prohibition scannable without traversing multiple rows; requires C-27. |
| C-31 | **C-30 explicit inline token enumeration** | format | aspirational | The single YOU MUST NOT block required by C-27/C-30 must enumerate each substituted canonical token explicitly by name inside the block itself; a table-reference shorthand that places the block in a single location but delegates token enumeration to the obligation table — e.g., "YOU MUST NOT use any of the canonical Obligation Term values listed in the table above" — does not satisfy C-27 because the prohibition surface is not self-contained; a reviewer must cross-reference the obligation table to determine which specific tokens are prohibited, fragmenting the verification surface; inline enumeration produces a single scannable prohibition unit; requires C-27 and C-30. |
| C-32 | **C-29 uppercase ARE assertive form** | format | aspirational | The C-29 ARE directive must use the uppercase ARE keyword in an assertive declarative sentence; lowercase "are" in a non-assertive construction — e.g., "the flag column headers are the Obligation Term column values above" — describes correspondence without asserting identity and does not satisfy C-29; the uppercase ARE form is the minimum because it marks the schema alignment as a format-level identity constraint, not a prose observation; the assertive sentence form makes the constraint structurally enforceable — a model that violates it produces a detectable mismatch; requires C-29. |
| C-33 | **C-32 multi-subject collective ARE form** | format | aspirational | The C-32 ARE directive must use the multi-subject collective form asserting identity for all flag column headers together in a single statement; any valid multi-subject plural ARE construction satisfies C-33 — the exact subject phrase is not required; the structural requirement is: plural collective subject + uppercase ARE + single assertion covering all headers; e.g., "Flag column headers ARE the Obligation Term column values above" (without definite article) satisfies C-33 equally to "the flag column headers ARE..."; a per-item IS form that asserts identity one header at a time — e.g., "Each flag column header IS one of the Obligation Term values" — is uppercase and assertive but does not satisfy C-29 or C-32 because ARE is a named keyword in C-29, not a proxy for the class of uppercase assertive identity verbs including IS; V-01 (R11) established the failure boundary (IS per-item form → FAIL); V-01 (R12) established the subject-form flexibility (alternate plural ARE subject → PASS); requires C-32. |
| C-34 | **C-31 complete inline enumeration (substituted-subset scope)** | format | aspirational | The C-31 inline enumeration must name every substituted canonical token in the YOU MUST NOT block — "each substituted canonical token" means every token where a canonical obligation term was actively replaced by a non-standard substitute; canonical obligation terms retained in the table without substitution and new obligation categories with no canonical equivalent are outside C-34's scope; partial enumeration of the substituted subset (naming n−1 of n substituted tokens) does not satisfy C-31; the prohibition surface must be self-contained for the substituted subset — a model can use any unenumerated substituted term freely; V-02 (R11) established the failure boundary (3-of-4 substituted tokens → FAIL); V-02 (R12) established the per-substitution scope (substituted-only enumeration on a five-row table → PASS); requires C-31. |
| C-35 | **C-24 extended obligation set scalability** | format | aspirational | The C-24 obligation table schema scales to any N >= 4 obligation categories; "one row per obligation category" is the structural rule — the four-row canonical default is not a hard count but the minimum for the four-obligation baseline; a table with five or more rows satisfies C-24 when it has exactly one row per obligation category and the structural auditability property is preserved (each category's presence or absence is detectable as a present or absent row without reading prose); a table with fewer rows than obligation categories does not pass regardless of total row count; V-02 (R12) established the pass boundary (five-row extended obligation set → C-24 PASS); requires C-24. |
| C-36 | **Motivational framing block** | format | aspirational | A WHY THIS TRACE DISCIPLINE EXISTS motivational framing block appears before the expert persona declaration and names the purpose of the integration trace discipline; any prose block that names what the trace is for satisfies C-36 — obligation-aware framing is not required; presence + position + purpose statement is the minimum; the block is structurally additive — no schema changes to existing stages, obligation tables, gate instructions, flag column definitions, or per-call sections are required for it to be present; V-03 (R12) confirmed structural neutrality — all criteria from C-01 through C-34 score identically with and without the framing block; V-01 (R13) confirmed the minimal content standard — a purpose statement naming what the trace verifies and when documentation gaps become consequential satisfies C-36; traces that include all structural elements through C-35 without a preceding motivational framing block pass C-16 but not C-36; requires C-16. |
| C-37 | **Temporal stakes anchor in motivational framing** | format | aspirational | The C-36 motivational framing block includes an explicit temporal or delivery-phase anchor naming the consequence boundary of undocumented integration calls; the stakes anchor converts the framing from a description of trace purpose to a delivery-phase constraint — a statement of when or at what phase the documentation gap becomes a ship-blocker; a purpose-statement-only WHY block that names what the trace does without specifying a consequence boundary passes C-36 but not C-37; concern enumeration alongside the stakes anchor is not required — a stakes anchor alone satisfies C-37 (Q1, R15 resolved PERMISSIVE: V-01 consequence-form without concern enumeration → PASS; V-02 temporal form without concern enumeration → PASS); two realized forms satisfy C-37: (1) interval-before temporal form — "before the feature ships" (V-01, R13); (2) consequence-form with explicit delivery-phase marker — "become ship-blockers at integration review" using declarative, unconditional framing (V-01, R14); conditional modal form ("can become ship-blockers") does not name a constraint and does not satisfy C-37; any temporal or delivery-phase consequence boundary in declarative unconditional form satisfies C-37; requires C-36. |
| C-38 | **C-36 obligation-count-agnostic content scope** | format | aspirational | When C-35 is in play (N > 4 obligation categories), the C-36 motivational framing block satisfies C-36 without enumerating the extended obligation categories; the framing block is evaluated at trace-discipline scope (purpose + stakes), not at obligation-category enumeration scope; canonical-term framing covering the four-concern verification baseline satisfies C-36 regardless of obligation set extension; V-02 (R13) established the pass boundary (five-row extended obligation set + canonical four-concern framing, no cold-start mention → C-36 PASS); this resolves Q2 from R12/R13; the framing block and the obligation table operate at independent structural layers — the framing block describes the trace discipline, the obligation table describes the discovery scope; a framing block that enumerates obligation categories passes C-38 equally to one that does not; requires C-35 and C-36. |
| C-39 | **C-37 consequence-form delivery-phase equivalence** | format | aspirational | The C-37 stakes anchor is satisfied by consequence-form with an explicit delivery-phase marker equivalently to interval-before temporal form; temporal form ("before the feature ships") names the interval before which documentation must be complete; consequence-form ("become ship-blockers at integration review") names the delivery phase at which undocumented calls become blockers; the two forms are structurally equivalent C-37 realizations — both convert the framing from description to constraint, one by naming the interval-before, the other by naming the point-at; the declarative, unconditional framing requirement is non-negotiable for both forms — conditional modal form ("can become ship-blockers") weakens the consequence statement to a possibility and does not name a constraint boundary; V-01 (R14) established the pass boundary: consequence-form + explicit delivery-phase marker ("at integration review") + declarative unconditional framing ("become ship-blockers") → C-37 PASS; C-39 codifies this form-surface equivalence as a distinct criterion because C-37's pass condition names "temporal or delivery-phase anchor" without specifying a realized form, and C-39 closes that ambiguity by confirming the consequence-form + delivery-phase-marker surface as a concrete delivery-phase anchor realization; requires C-37. |
| C-40 | **C-39 register-neutrality** | format | aspirational | The C-39 consequence-form delivery-phase anchor satisfies C-37/C-39 in any surface register — formal declarative, conversational, or imperative — provided the unconditional constraint meaning is preserved; register is a stylistic property of the sentence surface and does not affect the structural C-39 pass conditions (consequence-form + explicit delivery-phase marker + declarative unconditional constraint meaning); a conversational/imperative formulation — e.g., "Make sure undocumented calls become ship-blockers at integration review" — carries unconditional constraint semantics equivalently to formal declarative register when no modal weakening is present; register variation that introduces conditional modal weakening — e.g., "try to ensure calls can become ship-blockers" — does not satisfy C-39 regardless of register; V-03 (R15) established the pass boundary (conversational/imperative register with consequence-form anchor → C-39 PASS); requires C-39. |
| C-41 | **C-39 inertia-context framing neutrality** | format | aspirational | An inertia/obligation-scope discovery-failure framing context in the WHY block — one that frames the trace rationale around prior trace failures to discover calls rather than around prospective discovery — does not disqualify C-37 or C-39 when a consequence-form delivery-phase anchor is present; inertia framing is a background narrative property of the WHY block, not a structural property that overrides or substitutes for the stakes anchor; the two are independent: inertia framing alone without a stakes anchor fails C-37 (no consequence boundary named); inertia framing plus a consequence-form delivery-phase anchor satisfies C-37/C-39 as normal; V-04 (R15) established the pass boundary (inertia-context framing + consequence-form anchor → C-37 PASS and C-39 PASS); V-04 also confirmed that inertia framing does not substitute for concern enumeration — the absence of concern enumeration in an inertia-framed WHY block does not penalize C-37 (Q1 already confirmed permissive); requires C-39. |
| C-42 | **Highest-information WHY block: consequence-form + concern enumeration** | format | aspirational | The highest-information form of the C-36 motivational framing block combines both structural features: (1) a consequence-form delivery-phase anchor satisfying C-37 and C-39; and (2) explicit concern enumeration naming the specific verification concerns the trace addresses; a WHY block with only a stakes anchor passes C-37/C-39 (Q1, R15 confirmed permissive) but not C-42; a WHY block with only concern enumeration and no stakes anchor passes C-36 but not C-37 or C-42; the C-42 form requires both features present simultaneously — the stakes anchor supplies the delivery-phase constraint boundary and the concern enumeration supplies the explicit scope of which gaps become consequential at that boundary; the combination is the highest-information form because it tells the model both why the deadline is binding and what specific gaps become consequential, making the framing block maximally constraining at the format level; V-05 (R15, 247/247 ceiling) confirmed this as the strongest WHY block realization, simultaneously satisfying C-37, C-39, and C-42; concern enumeration in a C-42 block must name the specific verification concerns the trace addresses — a generic "various concerns" reference does not pass; requires C-37 and C-39. |
| C-43 | **RFC-modal MUST/SHALL unconditional obligation class** | format | aspirational | RFC 2119 MUST and SHALL constitute a specific named unconditional obligation register class within C-40's register-neutrality scope; the defining property is that MUST/SHALL are *stronger-obligation* than indicative form — RFC 2119 defines MUST as "absolute requirement" and SHALL as "absolute obligation" — not merely equivalent; zero epistemic weakening is introduced; a consequence-form delivery-phase anchor using MUST or SHALL satisfies C-40 with stronger obligation force than the indicative baseline; the RFC-modal failure boundary is also closed by this criterion: RFC-weakening modals — SHOULD ("recommended but not required"), MAY ("optional"), NEED NOT ("not required") — do NOT satisfy C-40 because they convert unconditional constraint meaning into conditional or discretionary meaning, introducing epistemic weakening; the MUST/SHALL pass boundary and the SHOULD/MAY failure boundary are structurally complementary — the distinction is unconditional-obligation modals vs. conditional-or-discretionary modals; V-02 (R16) established the pass boundary: MUST/SHALL with consequence-form delivery-phase anchor → 232/232, explicit C-40 verdict PASS, "RFC-modal MUST/SHALL register is register-neutral. No degradation."; requires C-40. |
| C-44 | **C-41 inertia-dominant saturation: three-sentence inertia prefix with C-42 anchor close** | format | aspirational | A WHY block with three inertia sentences — covering independent scope-failure root causes such as implicit SDK call undercounting, delegation chain documentation failure, and obligation-scope never explicitly defined — followed by a single anchor-close sentence constitutes an inertia-dominant block (3:1 inertia-to-anchor ratio by sentence count); C-41 holds at this saturation level — inertia framing quantity does not affect C-37/C-39 evaluation at any sentence count; only the presence or absence of the consequence anchor determines the outcome; when the anchor-close sentence also contains concern enumeration (supplying both a stakes anchor and explicit concern names), the block simultaneously satisfies C-37, C-39, C-41, and C-42 — the inertia-dominant variant of the highest-information form; the three-sentence inertia prefix adds discovery-context saturation: multiple independent scope-failure root causes establish why the obligation boundary must be made explicit, providing maximum justificatory framing before the constraint anchor; the structural property confirmed by this criterion is inertia-sentence-count neutrality — C-41 is not bounded by inertia sentence count; V-03 (R16) probed this form with three inertia sentences + one scope + anchor + enumeration closing sentence; requires C-41 and C-42. |
| C-45 | **C-43 failure-class conditional sub-type: SHOULD failure mechanism** | format | aspirational | RFC 2119 SHOULD introduces *conditional-recommendation* epistemic weakening: "recommended but not required" converts the unconditional consequence boundary to a conditional recommendation — the consequence statement becomes "it is recommended that this become a blocker" rather than "it becomes a blocker"; the failure mechanism is conditionality; SHOULD independently fails C-37 (conditional recommendation is not an unconditional constraint boundary — a recommendation can be declined without violating a rule), C-39 (unconditional form requirement violated by conditional modal), C-40 (register-neutrality applies only when unconditional constraint meaning is preserved; conditional modal weakening is a semantic-content property, not a surface-register property), and C-43 (SHOULD is named as failure-class modal); the cascade from a single SHOULD substitution is complete and deterministic — the entire stakes-anchor criterion chain collapses; the SHOULD mechanism is semantically distinct from the MAY mechanism (C-46): SHOULD weakens via conditionality ("not required but recommended" — some obligation force remains); MAY weakens via discretionality ("optional" — no obligation force at all); both produce identical cascade outcomes across C-37/C-39/C-40/C-43 but via different epistemic paths; C-43 named the failure class; C-45 names the conditional-recommendation sub-type and closes Q1 (R17) SHOULD pathway; V-01 (R17) established the empirical failure boundary: "Undocumented integration calls SHOULD become ship-blockers at integration review and cannot be cleared without a completed trace" → conditional-recommendation form → C-37 FAIL, C-39 FAIL, C-40 FAIL, C-43 FAIL; requires C-43. |
| C-46 | **C-43 failure-class discretionary sub-type: MAY failure mechanism and compound conditionality** | format | aspirational | RFC 2119 MAY introduces *discretionary-possibility* epistemic weakening: "optional" converts the consequence boundary to a discretionary possibility — the consequence statement becomes "it is permitted for this to become a blocker" rather than "it becomes a blocker"; the failure mechanism is optionality, semantically distinct from SHOULD's conditionality: SHOULD says "you ought to, but you may not" (some residual obligation); MAY says "you may, but you need not" (no obligation whatsoever); both fail C-40/C-43 via different weakening pathways but produce identical cascade outcomes; when MAY is compounded with a conditional clause ("if not documented"), the anchor exhibits *compound conditionality* — two independent disqualifying mechanisms are present simultaneously: (1) MAY modal introduces discretionary weakening; (2) conditional clause further subordinates the already-weakened consequence to a documentary condition; crucially, each mechanism alone suffices for disqualification — compound form does not require both to apply; neither mechanism can rescue the other in compound construction: the conditional clause does not strengthen a discretionary modal ("if not documented, it is still merely optional"), and the MAY modal is not rescued by a condition that specifies when the discretion applies ("it becomes optional only when not documented" is still optional); the structural finding is mechanism independence — compound conditionality exposes two failure surfaces but collapses to the same cascade outcome as any single C-43 failure-class modal; this is the first confirmed two-mechanism failure pattern in the WHY block criterion chain; V-02 (R17) established the MAY failure boundary and the compound conditionality pattern: "authentication, rate limits, retry behavior, and error propagation gaps MAY become ship-blockers at integration review if not documented" → MAY modal (mechanism 1: discretionary-possibility) + "if not documented" conditional clause (mechanism 2: documentary subordination); both mechanisms independently named; cascade outcome identical to V-01 SHOULD despite distinct mechanism pair; closes Q1 (R17) MAY sub-type; requires C-43 and C-45. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-46 | 192 |
| **Total** | | **282** |

### Point Allocation

| Criterion | Points | Tier |
|-----------|--------|------|
| C-01–C-04 | 15 each | Essential (60) |
| C-05–C-07 | 10 each | Recommended (30) |
| C-08–C-09 | 5 each | Aspirational |
| C-10–C-14 | 4 each | Aspirational |
| C-15 | 3 | Aspirational |
| C-16–C-17 | 7 each | Aspirational |
| C-18–C-28 | 5 each | Aspirational |
| C-29–C-30 | 5 each | Aspirational (new v10) |
| C-31–C-32 | 5 each | Aspirational (new v11) |
| C-33–C-34 | 5 each | Aspirational (new v12) |
| C-35–C-36 | 5 each | Aspirational (new v13) |
| C-37–C-38 | 5 each | Aspirational (new v14) |
| C-39 | 5 | Aspirational (new v15) |
| C-40–C-42 | 5 each | Aspirational (new v16) |
| C-43–C-44 | 5 each | Aspirational (new v17) |
| C-45–C-46 | 5 each | Aspirational (new v18) |
| **Total** | **282** | |

New ceiling: 282 = R17 ceiling 272 + C-45 (5) + C-46 (5)

---

**What changed in v18:**

- **C-45** captures the *SHOULD conditional-recommendation failure mechanism* from R17 V-01.
  V-01 probed RFC 2119 SHOULD in a consequence-form delivery-phase WHY block — the first
  empirical confirmation of the C-43 failure-class conditional sub-type. The key finding is
  the mechanism: SHOULD introduces conditionality ("recommended but not required"), which
  converts the unconditional constraint boundary to a conditional recommendation. This is
  semantically distinct from MAY's discretionality and from C-37's original conditional-modal
  failure boundary (which applied to non-RFC modals). C-43 named SHOULD as a failure-class
  modal and predicted C-40 FAIL on logical grounds; V-01 (R17) confirms it empirically with
  full cascade scoring. C-45 closes Q1 (R17) SHOULD sub-type and names the conditional-
  recommendation pathway as a distinct sub-type within the C-43 failure class.

- **C-46** captures the *MAY discretionary-possibility failure mechanism and compound
  conditionality* from R17 V-02. V-02 probed RFC 2119 MAY compounded with a conditional
  clause ("if not documented") — the empirical confirmation of the C-43 failure-class
  discretionary sub-type and the first observation of a two-mechanism failure pattern. The
  MAY mechanism (optionality) is semantically distinct from SHOULD's conditionality: SHOULD
  retains some residual obligation force ("recommended"); MAY has none ("optional"). The
  compound conditionality finding is new: two independent disqualifying mechanisms present
  simultaneously, each alone sufficient, neither rescuable by the other. This closes Q1 (R17)
  MAY sub-type and completes the C-43 failure-class taxonomy: MUST/SHALL (unconditional
  obligation class, C-43 pass) / SHOULD (conditional-recommendation sub-type, C-45 failure) /
  MAY (discretionary-possibility sub-type + compound conditionality, C-46 failure).

- **Ceiling**: 272 → 282 (+10).
