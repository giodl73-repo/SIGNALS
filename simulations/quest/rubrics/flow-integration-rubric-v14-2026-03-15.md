# flow-integration Rubric — v14

---

**Two new criteria from R13:**

**C-37 — Temporal stakes anchor in motivational framing (5 pts)**
Settles the stakes-anchor pattern established by V-01. The C-36 motivational framing
block includes an explicit temporal or delivery-phase anchor naming the consequence
boundary of undocumented integration calls ("before the feature ships"). V-01's WHY
block — "verify that each call's authentication, rate limits, retry behavior, and error
propagation are fully documented before the feature ships" — converts the framing from
a description of trace purpose to a delivery-phase constraint. The adjudication named
"before the feature ships" as the consequence anchor: a purpose-statement-only WHY
block that describes what the trace does without naming a consequence boundary passes
C-36 but not C-37. Requires C-36.

**C-38 — C-36 obligation-count-agnostic content scope (5 pts)**
Settles Q2 from R12/R13. When an extended obligation set is in play (C-35, N > 4),
the C-36 motivational framing block does not need to enumerate the extended obligation
categories to satisfy C-36. The framing block is evaluated at trace-discipline scope
(purpose + stakes), not at obligation-category enumeration scope. V-02 established the
pass boundary: a five-row extended obligation set (cold-start added, three canonical
terms substituted) paired with canonical four-concern framing in the WHY block — with
no cold-start mention — satisfies C-36. Canonical framing satisfies C-36 regardless
of obligation set extension. Requires C-35 and C-36.

**Ceiling: 232 → 242 (+10). Aspirational total: 152 pts (C-08–C-38).**

**Q1 and Q2 resolutions from R13 update existing criteria:**
- **C-36** — pass condition clarified: any prose block that names the purpose of the
  trace discipline satisfies C-36; obligation-aware framing is not required; presence +
  position + purpose statement is the minimum; V-01 adjudication established: "any prose
  that names what the trace is for satisfies C-36"

**Open questions for R14:**
1. **C-37 temporal-vs-consequence form** — Does C-37 require a delivery-phase temporal
   anchor ("before the feature ships"), or does a consequence-form anchor without an
   explicit temporal marker ("undocumented calls become ship-blockers") satisfy C-37
   equivalently? V-01 used the temporal form; the consequence-only form has not been tested.
2. **C-37 stakes-only vs. concern-enumerated stakes** — Does C-37 require concern
   enumeration alongside the stakes anchor, or does a stakes-anchored purpose statement
   without naming specific verification concerns satisfy C-37? V-01 combined concern
   enumeration with the stakes anchor; whether the stakes anchor alone achieves C-37
   has not been tested.

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
open since R9: the C-29 ARE directive requires the uppercase ARE keyword in an assertive
declarative sentence; lowercase "are" in a non-assertive construction describes
correspondence without asserting identity and does not satisfy C-29; the uppercase ARE
form is the minimum because capitalisation marks the assertion as a format-level
constraint, not a prose observation; V-02 established the failure boundary (lowercase
"are" → C-29 FAIL) and all confirmed PASS variations used uppercase ARE in assertive
sentences.

**New in v12:** C-33, C-34 codify the two structural patterns identified in Round 11.
C-33 settles the C-32 assertive form variant question open since R10: the C-32 ARE
directive requires the multi-subject collective form — "the flag column headers ARE the
Obligation Term column values above" — asserting identity for all headers in a single
statement; a per-item IS form ("Each flag column header IS one of the Obligation Term
values") is uppercase and assertive but does not satisfy C-29 or C-32 because ARE is
the named keyword in C-29, not a proxy class for assertive identity verbs; the collective
ARE form makes all headers subject to one identity constraint; the per-item IS form
distributes assertions and does not create an equivalent structural constraint; V-01
established the failure boundary (IS form → C-29/C-32 FAIL). C-34 settles the C-31
enumeration completeness question open since R10: the YOU MUST NOT block must enumerate
every substituted canonical token — partial enumeration naming n−1 of n tokens does not
satisfy C-31; "each substituted canonical token" in C-31 means all; a prohibition surface
missing any token is not self-contained — a model can use the unenumerated token freely;
full enumeration is the minimum for complete dual-surface coverage; V-02 established the
failure boundary (3-of-4 tokens → C-27/C-31 FAIL).

**New in v13:** C-35, C-36 codify the two structural patterns identified in Round 12.
C-35 settles the C-24 extended obligation set scalability question open since R11: the
C-24 obligation table schema is not hard-limited to four rows; "one row per obligation
category" is the structural rule; a five-row table with five obligation categories
satisfies C-24 because the structural auditability property — each category has exactly
one row whose presence or absence is detectable without reading prose — is preserved
regardless of row count; V-02 established the pass boundary (five-row extended set →
C-24 PASS); the canonical four-row baseline is the minimum for the four-obligation
default, not a universal ceiling. C-36 settles the motivational framing question raised
by V-03: a WHY THIS TRACE DISCIPLINE EXISTS block prepended before the expert persona
declaration is a structurally additive pattern that does not require schema changes to
any existing stage, gate, obligation table, or flag column; its presence anchors the
trace rationale at the top of the document above the persona boundary; V-03 confirmed
structural neutrality — all criteria from C-01 through C-34 scored identically with and
without the framing block; C-36 codifies the framing block as a distinct excellence
pattern that requires C-16 as its structural prerequisite.

**New in v14:** C-37, C-38 codify the two structural patterns identified in Round 13.
C-37 settles the C-36 content-form question open since R12 (Q1): the minimal pass
condition for C-36 is presence + position + purpose statement; any prose naming what
the trace is for satisfies C-36; but the V-01 WHY block demonstrated a stronger form —
purpose + concern-enumeration + temporal stakes anchor ("before the feature ships") —
that converts the framing from a description into a delivery-phase constraint; "before
the feature ships" is the consequence anchor named in the V-01 adjudication; a C-36
block without a temporal or delivery-phase stakes anchor passes C-36 but not C-37;
C-37 captures the stakes-anchored form as the next excellence tier above bare C-36.
C-38 settles the C-35 + C-36 framing alignment question open since R12 (Q2): when an
extended obligation set is in play (C-35, N > 4), the C-36 motivational framing block
satisfies C-36 without enumerating the extended obligation categories; V-02 established
the pass boundary (five-row extended set + canonical four-concern framing, no cold-start
mention → C-36 PASS); the framing block is evaluated at trace-discipline scope (purpose
+ stakes), not at obligation-category enumeration scope; canonical framing satisfies
C-36 regardless of obligation set extension; C-38 codifies this count-agnostic content
scope as a distinct pattern because it confirms the framing block and the obligation
table operate at independent structural layers.

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

## Aspirational Criteria (152 pts total)

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
| C-35 | **C-24 extended obligation set scalability** | format | aspirational | The C-24 obligation table schema scales to any N ≥ 4 obligation categories; "one row per obligation category" is the structural rule — the four-row canonical default is not a hard count but the minimum for the four-obligation baseline; a table with five or more rows satisfies C-24 when it has exactly one row per obligation category and the structural auditability property is preserved (each category's presence or absence is detectable as a present or absent row without reading prose); a table with fewer rows than obligation categories does not pass regardless of total row count; V-02 (R12) established the pass boundary (five-row extended obligation set → C-24 PASS); requires C-24. |
| C-36 | **Motivational framing block** | format | aspirational | A WHY THIS TRACE DISCIPLINE EXISTS motivational framing block appears before the expert persona declaration and names the purpose of the integration trace discipline; any prose block that names what the trace is for satisfies C-36 — obligation-aware framing is not required; presence + position + purpose statement is the minimum; the block is structurally additive — no schema changes to existing stages, obligation tables, gate instructions, flag column definitions, or per-call sections are required for it to be present; V-03 (R12) confirmed structural neutrality — all criteria from C-01 through C-34 score identically with and without the framing block; V-01 (R13) confirmed the minimal content standard — a purpose statement naming what the trace verifies and when documentation gaps become consequential satisfies C-36; traces that include all structural elements through C-35 without a preceding motivational framing block pass C-16 but not C-36; requires C-16. |
| C-37 | **Temporal stakes anchor in motivational framing** | format | aspirational | The C-36 motivational framing block includes an explicit temporal or delivery-phase anchor naming the consequence boundary of undocumented integration calls; the stakes anchor converts the framing from a description of trace purpose to a delivery-phase constraint — a statement of when the documentation gap becomes a ship-blocker; a purpose-statement-only WHY block that names what the trace does without specifying a consequence boundary passes C-36 but not C-37; V-01 (R13) established the pass boundary: purpose + concern-enumeration + "before the feature ships" — the temporal anchor "before the feature ships" is the consequence-boundary marker; the stakes anchor need not name specific failure modes; any temporal or delivery-phase consequence boundary satisfies C-37; requires C-36. |
| C-38 | **C-36 obligation-count-agnostic content scope** | format | aspirational | When C-35 is in play (N > 4 obligation categories), the C-36 motivational framing block satisfies C-36 without enumerating the extended obligation categories; the framing block is evaluated at trace-discipline scope (purpose + stakes), not at obligation-category enumeration scope; canonical-term framing covering the four-concern verification baseline satisfies C-36 regardless of obligation set extension; V-02 (R13) established the pass boundary (five-row extended obligation set + canonical four-concern framing, no cold-start mention → C-36 PASS); this resolves Q2 from R12/R13; the framing block and the obligation table operate at independent structural layers — the framing block describes the trace discipline, the obligation table describes the discovery scope; a framing block that enumerates obligation categories passes C-38 equally to one that does not; requires C-35 and C-36. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-38 | 152 |
| **Total** | | **242** |

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
| **Total** | **242** | |

New ceiling: 242 = R13 ceiling 232 + C-37 (5) + C-38 (5)

---

**What changed in v14:**

- **C-36 pass condition updated** — Q1 from R13 resolved definitively: the minimum
  content standard for C-36 is presence + position + purpose statement; any prose block
  that names the purpose of the trace discipline (what it is for) satisfies C-36;
  obligation-aware framing that references specific C-19 obligation categories is not
  required; V-01 (R13) established the pass boundary with a purpose statement naming
  verification scope and temporal stakes — the adjudication confirmed "any prose that
  names what the trace is for satisfies C-36." The pass condition text is updated to
  read: "any prose block that names the purpose of the integration trace discipline
  satisfies C-36; obligation-aware framing is not required; presence + position +
  purpose statement is the minimum."

- **C-37** captures the *temporal stakes anchor* pattern from R13 V-01. The V-01 WHY
  block — "verify that each call's authentication, rate limits, retry behavior, and
  error propagation are fully documented before the feature ships" — was adjudicated as
  demonstrating purpose + concern-enumeration + temporal stakes anchor. The adjudication
  specifically named "before the feature ships" as the consequence anchor that converts
  the framing from description to constraint. A C-36 block with a purpose statement
  but no temporal or delivery-phase stakes anchor passes C-36 but not C-37. V-01
  established the pass boundary (temporal stakes anchor present → C-37 PASS). The
  open question for R14 is whether the delivery-phase form ("before the feature ships")
  is required or whether a consequence-form anchor without an explicit temporal marker
  achieves C-37 equivalently.

- **C-38** captures the *obligation-count-agnostic content scope* pattern from R13 V-02,
  resolving Q2 from R12/R13. V-02 used a five-row extended obligation set (three
  non-standard substitutes, one canonical-kept, one new-without-canonical-equivalent)
  paired with a WHY block written in canonical four-concern language with no mention of
  the extended cold-start category. C-36 PASS for V-02 establishes: the framing block
  and the obligation table operate at independent structural layers; the framing block
  is evaluated at trace-discipline scope; canonical framing satisfies C-36 regardless
  of obligation set size. C-38 codifies this as a distinct criterion because it confirms
  that C-36 does not cascade into a requirement to update the motivational framing when
  C-35 is triggered — the two criteria are orthogonally composable.

- **Ceiling**: 232 → 242 (+10).

---

**Open questions for R14:**

1. **C-37 temporal-vs-consequence form** — Does C-37 require a delivery-phase temporal
   anchor ("before the feature ships"), or does a consequence-form anchor without an
   explicit temporal marker ("undocumented calls become ship-blockers at integration
   review") satisfy C-37 equivalently? V-01 used the temporal form; the consequence-only
   form has not been tested. If temporal form is required, C-37 specifies a surface-level
   pattern; if consequence form also satisfies, C-37 is about stakes presence regardless
   of form.

2. **C-37 stakes-only vs. concern-enumerated stakes** — Does C-37 require concern
   enumeration alongside the stakes anchor, or does a stakes-anchored purpose statement
   without naming specific verification concerns satisfy C-37? V-01 combined concern
   enumeration ("authentication, rate limits, retry behavior, and error propagation")
   with the stakes anchor ("before the feature ships"); whether the stakes anchor alone —
   without enumerating the specific concerns the trace verifies — achieves C-37 has not
   been tested. If concern enumeration is required, a subsequent criterion could codify
   the concern-enumerated form as a further excellence tier.
