Here is the complete updated rubric:

---

**Two new criteria extracted from R7 excellence signals:**

**C-24 — Four-obligation table schema (5 pts)**
The C-19 obligation declaration is formatted as a structured table with exactly one row per obligation category. Row count = completeness check. A missing row is a structurally absent obligation — detectable without rereading prose. A four-category prose list passes C-19 but not C-24. Obligation table must appear before the inventory gate. This resolves Open Question 2 from v7.

**C-25 — Schema-aligned C-22 enforcement (5 pts)**
The C-21 inventory's flag marker column headers are the same tokens as the C-24 obligation table row terms. Token identity is mechanically verifiable by table schema comparison — a header/row-term mismatch is visible without reading prose. Declarative C-22 (`VOCABULARY RULE` block, prose instruction) passes C-22 but not C-25. Requires C-24 as a structural prerequisite. Resolves the execution risk flagged in R7 V-03: a model can produce semantically corresponding labels even when a declarative rule instructs otherwise; schema alignment removes that failure mode.

**Ceiling: 167 → 177 (+10).** Aspirational total: 87 pts (C-08–C-25).

**Open questions carried to R8:**
1. Coda positioning constraint (V-04 probe inconclusive in R7 — carry forward)
2. C-24/C-25 execution risk under mixed-format outer frames (table obligation block + prose call blocks)
impossible at the section level. C-14 extends the per-call completion gate
from 3-of-5 concerns to all-five-concern scope. C-15 extends the inventory-first
guarantee from initial enumeration to runtime completeness.

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

## Aspirational Criteria (87 pts total)

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
| C-22 | **C-19/C-21 vocabulary unification** | format | aspirational | The flag marker names used in C-21 are the same tokens as the obligation terms declared in C-19 — canonical-to-canonical or non-standard-to-matching-non-standard; a C-21 flag name that semantically corresponds to but does not match the C-19 persona term (e.g., canonical `[forgotten-call]` paired with non-standard persona term "ghost calls") does not pass; vocabulary identity within the variation is the contract, not cross-variation standardization. |
| C-23 | **Unnumbered coda as universal cross-stage adapter** | format | aspirational | The C-20 cross-stage stage is implemented as an unnumbered coda appended after the last numbered element of the outer frame; the coda carries no position number and does not displace or renumber any existing element; this pattern must be applied when the outer frame is numbered (phases, stages, numbered sections); a numbered cross-stage element that displaces an existing position or forces renumbering does not pass. |
| C-24 | **Four-obligation table schema** | format | aspirational | The C-19 obligation declaration is formatted as a structured table with exactly one row per obligation category; presence or absence of each obligation is structurally auditable as a present or absent row; a prose list of four obligations passes C-19 but not C-24; the obligation table must appear before the inventory gate; C-24 is a structural prerequisite for C-25. |
| C-25 | **Schema-aligned C-22 enforcement** | format | aspirational | The C-21 inventory's flag marker column headers are the same tokens as the corresponding row terms in the C-24 obligation table; token identity is mechanically verifiable by table schema comparison — a header/row-term mismatch is visible without reading prose or code blocks; declarative C-22 (text instruction or `VOCABULARY RULE` block) passes C-22 but not C-25; requires C-24; this is the strongest C-22 enforcement mechanism. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-25 | 87 |
| **Total** | | **177** |

### Point Allocation

| Criterion | Points | Tier |
|-----------|--------|------|
| C-01–C-04 | 15 each | Essential (60) |
| C-05–C-07 | 10 each | Recommended (30) |
| C-08–C-09 | 5 each | Aspirational |
| C-10–C-14 | 4 each | Aspirational |
| C-15 | 3 | Aspirational |
| C-16–C-17 | 7 each | Aspirational |
| C-18–C-23 | 5 each | Aspirational |
| C-24–C-25 | 5 each | Aspirational (new v8) |
| **Total** | **177** | |

New ceiling: 177 = R7 ceiling 167 + C-24 (5) + C-25 (5)

---

**What changed in v8:**

- **C-24** captures the *four-obligation table schema* pattern from R7 V-02: when the
  C-19 obligation declaration is formatted as a four-row table, the row count itself
  becomes the completeness check. A missing obligation is a missing row — structurally
  absent and detectable without rereading prose. Four categories in a prose list satisfies
  C-19 (the count is correct) but not C-24 (the count is not structurally enforced). The
  obligation table must appear before the inventory gate so that its row terms can serve
  as the canonical token source for C-25. This resolves Open Question 2 from v7: the
  4-row table does provide a structural completeness guarantee that prose cannot.

- **C-25** captures the *schema-aligned C-22 enforcement* pattern from R7 V-02: the
  C-21 inventory's flag marker column headers are defined using the same tokens as the
  C-24 obligation table row terms. Token identity is now mechanically verifiable — a
  reviewer comparing column headers to obligation table row terms cannot miss a mismatch.
  This resolves the execution risk flagged in the R7 V-03 note: declarative C-22 (a text
  instruction or `VOCABULARY RULE` block stating "the persona term and the flag name are
  the same token") passes C-22 under strict criterion reading but a model can still
  produce semantically corresponding flag labels in output even when instructed otherwise;
  schema-aligned enforcement removes that risk because the token source is a table row
  the model must reference structurally, not a prose rule it must follow. Requires C-24
  as a structural prerequisite.

- **Ceiling**: 167 → 177 (+10).

---

**Open questions for R8:**

1. **Coda positioning constraint** — C-20 requires an unconditional cross-stage stage
   but specifies no position relative to the gap inventory (Stage 3 / Phase 3). V-04 in
   R7 was designed as a probe for this question (Phase Architecture + Coda Positioning
   Test) but its C-23 verdict was not conclusive in the R7 scorecard. R8 should produce
   a definitive verdict on whether coda-before-gaps creates assessment problems and
   whether a positioning constraint (coda must follow the gap inventory) belongs as a
   condition in C-20, C-23, or a new C-26.

2. **C-24/C-25 execution risk under non-table outer frames** — C-24 rewards table
   format for the obligation declaration, but some outer frames (declarative register,
   role sequence) may not use table structure elsewhere, making a table obligation
   block an isolated format island. R8 should test whether mixed-format traces (table
   obligation block + prose call blocks) achieve C-24/C-25 without structural
   inconsistency, and whether a format-consistency constraint belongs in C-24 or C-25.
