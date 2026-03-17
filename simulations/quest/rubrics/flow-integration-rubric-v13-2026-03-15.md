# flow-integration Rubric — v13

---

**Two new criteria from R12:**

**C-35 — C-24 extended obligation set scalability (5 pts)**
Settles Q2 (extension). V-02 established the pass boundary for extended obligation sets:
a five-row obligation table with five distinct categories (three non-standard substitutes,
one canonical-kept, one new-without-canonical-equivalent) satisfies C-24. The structural
requirement in C-24 is "one row per obligation category" — the four-row canonical default
is not a hard count; it is the minimum for the canonical four-obligation baseline. When the
obligation set is extended beyond four categories, C-24 requires a corresponding additional
row for each new category. V-02 demonstrated: five categories, five rows, one per category
→ C-24 PASS. Requires C-24.

**C-36 — Motivational framing block (5 pts)**
Settles V-03 (Structural Neutrality Probe). A WHY THIS TRACE DISCIPLINE EXISTS
motivational framing block prepended before the expert persona declaration is a
structurally additive pattern: no schema changes to existing stages, obligation tables,
flag columns, gate instructions, or per-call sections are required for it to be present.
Traces that include all structural elements through C-35 without a preceding motivational
framing block pass C-16 but not C-36. The motivational block names the purpose and stakes
of the integration trace discipline before the expert persona takes the floor; its presence
anchors the trace rationale above the persona boundary. Requires C-16.

**Ceiling: 222 → 232 (+10). Aspirational total: 142 pts (C-08–C-36).**

**Open question verdicts from R12:**
1. **Q1 resolved — C-33 subject form (definitive).** The exact subject phrase "the flag
   column headers" is not required to satisfy C-33. The "e.g." qualifier in the C-33
   definition confirms the stated phrase is illustrative, not lexically mandatory. Any
   valid multi-subject plural ARE construction asserting collective identity across all
   flag column headers satisfies C-33; the definite article ("the") and positional
   qualifier ("in the Stage 1 inventory table") are incidental to the structural form.
   V-01 established: "Flag column headers ARE the Obligation Term column values above"
   — without "the" and without the positional qualifier — satisfies C-33. The structural
   requirement is plural collective subject + uppercase ARE + single identity assertion
   covering all headers.
2. **Q2 resolved — C-34 substituted-subset enumeration scope (definitive).** "Each
   substituted canonical token" in C-34 applies only to tokens where a canonical
   obligation term was replaced by a non-standard substitute. Canonical obligation terms
   retained in the obligation table (e.g., delegation-chain kept as-is) and new obligation
   categories with no canonical equivalent (e.g., cold-start, which replaces nothing) are
   outside C-34's scope. V-02 established: a YOU MUST NOT block naming exactly the three
   substituted canonical tokens (forgotten-call, assumed-to-work, unknown-system) from a
   five-row table where the fourth row kept delegation-chain and the fifth row added
   cold-start — satisfies C-34. Per-substitution scope is the natural reading: prohibition
   covers only terms where a canonical token was actively displaced.

**Open questions carried to R13:**
1. **C-36 motivational framing content specificity** — Does C-36 require the framing
   block to name specific failure modes, obligation scope, or integration risks tied to
   C-19's obligation categories, or does any prose block that names the purpose of the
   trace discipline — regardless of specificity — satisfy C-36? The V-03 probe used a
   WHY THIS TRACE DISCIPLINE EXISTS block with no schema changes; whether minimal
   content (purpose statement only) is sufficient or whether obligation-aware framing
   is required has not been tested.
2. **C-35 + C-36 extended-set framing alignment** — When an extended obligation set
   (N > 4, C-35 in play) is paired with a motivational framing block (C-36), does C-36
   require the framing block to acknowledge the extended obligation categories beyond the
   canonical four, or is obligation-count-agnostic framing sufficient?

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

## Aspirational Criteria (142 pts total)

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
| C-36 | **Motivational framing block** | format | aspirational | A WHY THIS TRACE DISCIPLINE EXISTS motivational framing block appears before the expert persona declaration and names the purpose and stakes of the integration trace discipline; the block is structurally additive — no schema changes to existing stages, obligation tables, gate instructions, flag column definitions, or per-call sections are required for it to be present; V-03 (R12) confirmed structural neutrality — all criteria from C-01 through C-34 score identically with and without the framing block; traces that include all structural elements through C-35 without a preceding motivational framing block pass C-16 but not C-36; requires C-16. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-36 | 142 |
| **Total** | | **232** |

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
| **Total** | **232** | |

New ceiling: 232 = R12 ceiling 222 + C-35 (5) + C-36 (5)

---

**What changed in v13:**

- **C-33 pass condition updated** — Q1 from R12 resolved definitively: the exact subject
  phrase "the flag column headers" is not required to satisfy C-33. The "e.g." qualifier
  in C-33's definition is structural, not ornamental — it confirms the stated phrase is
  illustrative. Any valid multi-subject plural ARE construction asserting collective
  identity across all flag column headers satisfies C-33; the definite article and
  positional qualifier ("in the Stage 1 inventory table") are incidental to the
  structural form. V-01 (R12) established the pass boundary: "Flag column headers ARE
  the Obligation Term column values above" — alternate plural ARE subject without the
  canonical definite article — satisfies C-33. The pass condition text now reads: "any
  valid multi-subject plural ARE construction satisfies C-33; the structural requirement
  is plural collective subject + uppercase ARE + single assertion covering all headers."

- **C-34 pass condition updated** — Q2 from R12 resolved definitively: "each substituted
  canonical token" in C-34 applies only to tokens where a canonical obligation term was
  actively replaced by a non-standard substitute. Canonical terms retained without
  substitution and new terms with no canonical equivalent are outside C-34's scope.
  V-02 (R12) established the per-substitution scope pass boundary: a five-row obligation
  table with three non-standard substitutes, one canonical-kept term, and one new-without-
  canonical-equivalent term requires only three tokens enumerated in the YOU MUST NOT
  block — the three substituted ones. The pass condition text now reads: "substituted-
  subset scope — canonical-kept terms and new-without-canonical-equivalent terms are
  outside C-34's scope."

- **C-24 pass condition updated** — Extended in light of V-02 (R12): "row count equals
  obligation category count — four categories require four rows, N categories require N
  rows." The four-row canonical default is not a ceiling; C-24 is a one-per-category
  structural rule that scales. This update is a clarification; C-35 codifies the
  scalability pattern as a distinct criterion.

- **C-21 pass condition updated** — Extended in light of V-02 (R12): "flag count must
  match obligation category count." When C-35 is in play (N > 4 obligations), C-21
  requires N flag columns, not four. The update makes C-21 obligation-count-aware.

- **C-35** captures the *C-24 extended obligation set scalability* pattern from R12 V-02:
  the five-row obligation table (three non-standard, one canonical-kept, one new) passes
  C-24 because the structural rule is one-per-category, not exactly-four. V-02 probed
  Q2 from R12 (whether C-34 enumeration scope is substituted-subset or full-table). The
  resolution confirmed the per-substitution reading, and in doing so demonstrated that
  C-24 scales cleanly to extended obligation sets. The pass boundary (five-row table →
  C-24 PASS) is established by V-02. C-35 codifies: the obligation table schema is
  N-row-scalable; the canonical four-row baseline is the minimum, not the maximum.

- **C-36** captures the *motivational framing block* pattern from R12 V-03 (Structural
  Neutrality Probe): a WHY THIS TRACE DISCIPLINE EXISTS block prepended before the expert
  persona is structurally additive — no existing criteria scores change in its presence.
  V-03 probed whether the motivational framing block disrupts or displaces any structural
  requirement from C-01 through C-34. The structural neutrality ruling confirmed: the
  block composes cleanly with all existing criteria; its presence or absence is orthogonal
  to all prior criteria; it is a distinct excellence pattern that requires C-16 as its
  structural prerequisite. C-36 codifies: the motivational framing block is a first-class
  aspirational pattern; traces without it pass C-16 but not C-36.

- **Ceiling**: 222 → 232 (+10).

---

**Open questions for R13:**

1. **C-36 motivational framing content specificity** — Does C-36 require the framing
   block to name specific failure modes, obligation scope, or integration risks tied to
   the C-19 obligation categories, or does any prose block that names the purpose of the
   trace discipline — regardless of content specificity — satisfy C-36? The V-03 probe
   confirmed structural neutrality but did not probe framing content; whether a minimal
   purpose statement (one sentence naming the trace goal) is sufficient or whether
   obligation-aware framing (referencing forgotten calls, assumed-to-work entries, etc.)
   is required has not been tested. If minimal framing satisfies C-36, the criterion is
   about presence and position only; if content-specific framing is required, C-36
   specifies a semantic constraint, not merely a structural one.

2. **C-35 + C-36 extended-set framing alignment** — When an extended obligation set
   (N > 4, C-35 in play) is paired with a motivational framing block (C-36), does C-36
   require the framing block to acknowledge the extended obligation categories beyond
   the canonical four, or is obligation-count-agnostic framing sufficient to satisfy C-36
   regardless of obligation set size?
