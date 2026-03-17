`flow-integration-rubric-v7-2026-03-14.md` written. Here's what changed:

---

**C-22 — C-19/C-21 vocabulary unification (5 pts)**
> Flag marker names must be the same tokens as the obligation terms in the C-19 persona — canonical-to-canonical or non-standard-to-matching-non-standard. Semantic correspondence (C-21's bar) is not enough; vocabulary identity is required. A canonical `[forgotten-call]` flag paired with a non-standard "ghost calls" persona term does not pass C-22 — the reviewer cannot follow the chain without an external mapping.

**C-23 — Unnumbered coda as universal cross-stage adapter (5 pts)**
> The C-20 stage must be implemented as an unnumbered suffix appended after the last numbered element of the outer frame. The coda carries no position number and displaces nothing. This generalizes Stage 4 from a specific numbered slot to a composition primitive that works with any outer frame (phases, stages, flat numbered sections) without renumbering any existing element.

**Ceiling: 157 → 167.** Aspirational section header updated to `C-08–C-23` (77 pts). Two open questions carried forward for R7: coda positioning constraint, and obligation table schema as a potential future criterion.
leed concerns across sections.

**New in v3:** C-13, C-14, C-15 codify the structural patterns that broke the
110-point ceiling in Round 2 (V-05 Per-Call Gate Blocks). C-13 makes C-11 violations
structurally impossible at the section level. C-14 extends the per-call completion gate
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

## Aspirational Criteria (77 pts total)

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

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-23 | 77 |
| **Total** | | **167** |

### Point Allocation

| Criterion | Points | Tier |
|-----------|--------|------|
| C-01–C-04 | 15 each | Essential (60) |
| C-05–C-07 | 10 each | Recommended (30) |
| C-08–C-09 | 5 each | Aspirational |
| C-10–C-14 | 4 each | Aspirational |
| C-15 | 3 | Aspirational |
| C-16–C-17 | 7 each | Aspirational |
| C-18–C-21 | 5 each | Aspirational |
| C-22–C-23 | 5 each | Aspirational (new v7) |
| **Total** | **167** | |

New ceiling: 167 = R6 ceiling 157 + C-22 (5) + C-23 (5)

---

**What changed in v7:**

- **C-22** captures the *vocabulary unification* pattern from R6 V-05: when non-standard
  obligation terms are used in C-19 (e.g., "ghost calls"), the C-21 flag markers must
  use the same tokens (e.g., `[ghost-call]`), not canonical equivalents. C-21 passes on
  semantic correspondence alone; C-22 requires vocabulary identity — the persona term
  and the flag name are the same string. Mixing canonical flag names with non-standard
  persona terms breaks the persona-to-inventory trace; a reviewer can no longer follow
  the chain from obligation declaration to inventory flag without an external mapping.

- **C-23** captures the *unnumbered coda* pattern from R6 V-04: the C-20 cross-stage
  stage is an unnumbered suffix appended after the last numbered element of the outer
  frame. It carries no position number and cannot conflict with existing numbering. The
  pattern generalizes Stage 4 from a specific numbered slot to a universal additive
  composition primitive: wherever the numbered frame ends, the unnumbered coda follows.
  Applies to any outer frame (phases, stages, flat numbered sections) without requiring
  renumbering of any existing element.

- **Ceiling**: 157 → 167 (+10).

---

**Open questions for R7:**

1. **Coda positioning constraint** — C-20 requires an unconditional cross-stage stage
   but specifies no position relative to the gap inventory (Stage 3 / Phase 3). A trace
   placing the coda before the gap inventory satisfies C-20 and C-23 literally while
   creating an ordering anomaly. R7 should test whether coda-before-gaps produces
   assessment problems, and whether a positioning constraint (coda must follow the gap
   inventory) belongs as a condition in C-20 or C-23.

2. **Obligation table schema for C-19** — V-02's C-18 resolution reveals a general
   principle: table schemas enforce N-property completeness mechanically; prose lists do
   not. The same structural argument applies to C-19: four obligation categories as four
   named table rows is mechanically stronger than four categories in a prose declaration.
   A future criterion could reward "obligation table format" where presence/absence of
   each obligation is visually explicit as a present/absent row rather than inferable
   from a prose count.
