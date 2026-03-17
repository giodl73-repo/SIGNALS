Here is the complete updated rubric:

---

**Three new criteria extracted from R8 excellence signals:**

**C-26 — Schema-only C-25 enforcement (5 pts)**
The C-25 schema alignment is achieved by explicit schema instruction alone — no `VOCABULARY RULE` block required. The rubric instruction specifies that the flag column headers ARE the Obligation Term values from the C-24 table; token identity is structurally enforced at the format level, not the prose level. A rubric that mandates a `VOCABULARY RULE` block over-specifies C-25. Confirmed by V-02 (177/177 without any `VOCABULARY RULE` block). Requires C-24 and C-25.

**C-27 — Dual-surface canonical-substitution prohibition (5 pts)**
When non-standard obligation terms replace the canonical four, full C-22/C-25 coverage requires both surfaces: (1) schema alignment (C-25) detects substitution at the table surface — column header vs. row term mismatch visible by comparison; (2) an explicit YOU MUST NOT prohibition block names the specific canonical tokens that are forbidden in this trace, blocking semantic substitution at the prose and annotation surface. A generic vocabulary rule without specific token names does not satisfy C-27. Confirmed by V-05 (177/177). Requires C-24 and C-25.

**C-28 — Explicit terminal-position formula (5 pts)**
The C-23 coda header includes the canonical formula: `*(no [frame-unit] number — appended after [last-element], the last numbered [frame-unit])*`. A supporting prose sentence confirms: "It does not appear between any two numbered [frame-units]; it does not displace or renumber any existing element." Both surfaces required. C-23 requires only an unnumbered coda; C-28 closes the mid-sequence gap confirmed by R7 V-04 (structural failure, not stylistic). Formula is outer-frame-agnostic. Requires C-23.

**Ceiling: 177 → 192 (+15).** Aspirational total: 102 pts (C-08–C-28).

**Open question verdicts from R8:**
- Q1 resolved: terminal position confirmed mandatory for C-23; C-28 codifies the definitive formula.
- Q2 resolved: column headers required for C-25; pipe-delimited inline flag tokens provide no schema comparison surface.

**Open questions carried to R9:**
1. C-26 instruction minimum — explicit ARE formulation required, or any schema-aligned instruction sufficient?
2. C-27 prohibition scope — single block covering all substitutions, or per-term prohibition satisfies?

The full rubric is written to `simulations/quest/rubrics/flow-integration-rubric-v9-2026-03-14.md`. It carries forward the complete criterion table (C-01–C-28), updated scoring summary (192 total), point allocation table, "What changed in v9" section, and "New in v9" narrative alongside the full v4–v8 history.
oda placed between Phase 2 and Phase 3) demonstrated that unnumbered alone does not prevent mid-sequence placement; C-28 closes this gap. The formula is outer-frame-agnostic — substituting the frame unit name (phase / stage / section) and the last element identifier produces the correct formula for any outer frame style. Requires C-23. Confirmed by V-04 (explicit dual-surface formula, 177/177); R7 V-04 failure was structural, not stylistic (Q1 resolved).

**Ceiling: 177 → 192 (+15).** Aspirational total: 102 pts (C-08–C-28).

**Open question verdicts from R8:**
1. **Q1 resolved — C-23 terminal-position constraint (definitive).** The explicit dual-surface language — coda header annotation naming the last numbered element + prose sentence prohibiting between-elements placement — achieves a clean C-23 PASS. The R7 V-04 failure was structural: the coda appeared between Phase 2 and Phase 3, not after the last numbered phase. Terminal position is confirmed mandatory for C-23. C-28 codifies the full definitive formula.
2. **Q2 resolved — C-25 column header requirement (definitive).** Inline flag tokens in pipe-delimited inventory entries satisfy C-22 (a `VOCABULARY RULE` block covers token identity) but not C-25. The C-25 mechanism is header/row-term schema comparison, which requires actual Markdown table column header cells. No column header cells = no schema comparison surface = C-25 FAIL regardless of whether flag tokens are present in pipe-delimited entries.

**Open questions carried to R9:**
1. **C-26 instruction minimum** — Does schema-only C-25 enforcement require an explicit directive of the form "the flag column headers ARE the Obligation Term column values above — use those exact tokens as column headers," or does any unambiguous schema-aligned instruction satisfy C-26? V-02 used the direct explicit form; minimum viable instruction for C-26 is undefined.
2. **C-27 prohibition scope** — Must all substituted canonical tokens be named in a single YOU MUST NOT block, or does one prohibition per non-standard substitution satisfy C-27? V-05 used a single comprehensive prohibition block covering all non-standard terms; per-term minimum is untested.

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
a prose list counting four obligations passes C-19 but not C-24 because a model can
omit an obligation in output and the omission is visible only to a reader who recounts
the items; with a four-row table the missing row is structurally absent and detectable
without annotation. C-25 rewards schema-aligned C-22 enforcement — the pattern where
the C-21 inventory's flag marker column headers are defined using the same tokens as
the C-24 obligation table row terms, making token identity mechanically verifiable by
table schema comparison rather than by reading prose or scanning code blocks; this is
the strongest C-22 enforcement mechanism, resolving the execution risk noted for the
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
naming the specific canonical forbidden tokens blocks substitution at the prose and
annotation surface; the two surfaces are complementary because schema catches structural
failure and prohibition blocks the semantic workaround; a generic vocabulary instruction
that does not name the specific forbidden tokens does not achieve C-27. C-28 rewards the
explicit terminal-position formula for the C-23 unnumbered coda — the pattern confirmed
definitive in Round 8 (Q1 resolved) where coda terminal placement requires both a header
annotation naming the last numbered element and a prose sentence prohibiting between-
elements placement; C-23 allows an unnumbered coda anywhere in the frame; C-28 closes
the mid-sequence gap confirmed in R7 V-04 (unnumbered coda placed between Phase 2 and
Phase 3 — a structural failure, not a stylistic one); the formula is outer-frame-agnostic
and applies identically across phase, stage, and section frames by substituting the frame
unit name and last element identifier.

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

## Aspirational Criteria (102 pts total)

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
| C-21 | **Inventory flag alignment to persona obligation categories** | format | aspirational | Inventory entry format includes named flag fields corresponding to all four C-19 obligation categories (forgotten-call, assumed-to-work, unknown-system, delegation-chain); flags make persona discoveries structurally traceable in the inventory; inventory entries that correctly declare all four C-19 obligations in preamble but carry no per-entry flag fields do not pass. |
| C-22 | **C-19/C-21 vocabulary unification** | format | aspirational | The flag marker names used in C-21 are the same tokens as the obligation terms declared in C-19 — canonical-to-canonical or non-standard-to-matching-non-standard; a C-21 flag name that semantically corresponds to but does not match the C-19 persona term does not pass; vocabulary identity within the variation is the contract, not cross-variation standardization. |
| C-23 | **Unnumbered coda as universal cross-stage adapter** | format | aspirational | The C-20 cross-stage stage is implemented as an unnumbered coda appended after the last numbered element of the outer frame; the coda carries no position number and does not displace or renumber any existing element; this pattern must be applied when the outer frame is numbered (phases, stages, numbered sections); a numbered cross-stage element that displaces an existing position or forces renumbering does not pass. |
| C-24 | **Four-obligation table schema** | format | aspirational | The C-19 obligation declaration is formatted as a structured table with exactly one row per obligation category; presence or absence of each obligation is structurally auditable as a present or absent row; a prose list of four obligations passes C-19 but not C-24; the obligation table must appear before the inventory gate; C-24 is a structural prerequisite for C-25. |
| C-25 | **Schema-aligned C-22 enforcement** | format | aspirational | The C-21 inventory's flag marker column headers are the same tokens as the corresponding row terms in the C-24 obligation table; token identity is mechanically verifiable by table schema comparison — a header/row-term mismatch is visible without reading prose or code blocks; declarative C-22 (text instruction or `VOCABULARY RULE` block) passes C-22 but not C-25; requires C-24; this is the strongest C-22 enforcement mechanism. |
| C-26 | **Schema-only C-25 enforcement** | format | aspirational | The C-25 schema alignment is achieved by explicit schema instruction alone without a `VOCABULARY RULE` block; the instruction specifies that inventory flag column headers ARE the Obligation Term values from the C-24 table — token identity is structurally enforced at the format level, not at the prose level; a rubric that mandates a `VOCABULARY RULE` block to pass C-25 over-specifies the enforcement mechanism; schema identity instruction alone is sufficient and is the cleaner implementation; requires C-24 and C-25. |
| C-27 | **Dual-surface canonical-substitution prohibition** | format | aspirational | When non-standard obligation terms replace the canonical four, C-22/C-25 coverage requires both surfaces: (1) schema alignment (C-25) detects term substitution at the table surface — column header vs. row term mismatch visible by comparison without reading prose; (2) an explicit YOU MUST NOT prohibition block names the specific canonical tokens that are forbidden in this trace, blocking semantic substitution at the prose and annotation surface; a generic vocabulary instruction that does not name specific forbidden canonical tokens does not satisfy C-27; requires C-24 and C-25. |
| C-28 | **Explicit terminal-position formula** | format | aspirational | The C-23 coda header includes the canonical formula: `*(no [frame-unit] number — appended after [last-element], the last numbered [frame-unit])*`; a supporting prose sentence confirms: "It does not appear between any two numbered [frame-units]; it does not displace or renumber any existing element"; both surfaces required — header annotation anchors structural position, prose sentence closes the between-elements gap; C-23 requires only an unnumbered coda; C-28 requires the full two-surface formula; formula is outer-frame-agnostic; requires C-23. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-28 | 102 |
| **Total** | | **192** |

### Point Allocation

| Criterion | Points | Tier |
|-----------|--------|------|
| C-01–C-04 | 15 each | Essential (60) |
| C-05–C-07 | 10 each | Recommended (30) |
| C-08–C-09 | 5 each | Aspirational |
| C-10–C-14 | 4 each | Aspirational |
| C-15 | 3 | Aspirational |
| C-16–C-17 | 7 each | Aspirational |
| C-18–C-25 | 5 each | Aspirational |
| C-26–C-28 | 5 each | Aspirational (new v9) |
| **Total** | **192** | |

New ceiling: 192 = R8 ceiling 177 + C-26 (5) + C-27 (5) + C-28 (5)

---

**What changed in v9:**

- **C-26** captures the *schema-only C-25 enforcement* pattern from R8 V-02: dropping
  the `VOCABULARY RULE` block entirely and relying solely on an explicit schema instruction
  achieves full C-25 score. The instruction form that achieves this is "the flag column
  headers in the inventory table are the Obligation Term column values above — use those
  exact tokens as column headers," which makes token identity a format-level constraint the
  model must satisfy structurally rather than a prose rule it must remember to follow.
  V-02 confirms schema-only achieves 177/177 without any `VOCABULARY RULE` block. A
  rubric that mandates a `VOCABULARY RULE` block is over-specifying C-25.

- **C-27** captures the *dual-surface canonical-substitution prohibition* pattern from R8
  V-05: when non-standard obligation terms are used, schema alignment alone (C-25) detects
  structural substitution at the table surface, but a model can still produce semantically
  corresponding labels in prose and annotations without triggering a schema mismatch. An
  explicit YOU MUST NOT prohibition naming the specific canonical tokens that are forbidden
  in this trace closes that gap. The two surfaces are complementary: schema catches
  structural failure; prohibition blocks the semantic workaround. "YOU MUST NOT" naming
  the specific forbidden canonical tokens is required — a generic instruction is not
  sufficient because it does not create a verifiable prohibition at the token level.

- **C-28** captures the *explicit terminal-position formula* pattern confirmed definitive
  in R8 V-04 (Q1 resolved): the R7 V-04 failure was structural — the unnumbered coda
  appeared between Phase 2 and Phase 3, not after the last numbered phase. C-23 requires
  only that the coda be unnumbered; it does not require terminal position. C-28 closes
  this gap with a two-surface formula: the header annotation names the last numbered
  element (`appended after [last-element], the last numbered [frame-unit]`), and the prose
  sentence prohibits between-elements placement (`does not appear between any two numbered
  [frame-units]`). Both surfaces are required. The formula is outer-frame-agnostic.

- **Ceiling**: 177 → 192 (+15).

---

**Open questions for R9:**

1. **C-26 instruction minimum** — Does schema-only C-25 enforcement require an explicit
   directive of the form "the flag column headers ARE the Obligation Term column values
   above — use those exact tokens as column headers," or does any unambiguous schema-
   aligned instruction satisfy C-26? V-02 used the direct explicit ARE form. R9 should
   probe whether a cross-reference table mapping obligation terms to column header names,
   or a conditional instruction, achieves C-26 without the explicit ARE formulation.

2. **C-27 prohibition scope** — Must all substituted canonical tokens be named in a
   single YOU MUST NOT block, or does one prohibition per non-standard substitution
   satisfy C-27? V-05 used a single comprehensive block covering all non-standard terms
   simultaneously. R9 should test whether per-term prohibition (one YOU MUST NOT sentence
   per substituted token, distributed across the obligation table rows) achieves equivalent
   dual-surface coverage.
