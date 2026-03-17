Reading the Round 5 scorecard to identify the new structural patterns before writing the rubric.

From the V-01 and V-02 scoring, two patterns emerge that go beyond C-18 and C-19:

1. **V-01 C-18 PASS reasoning**: *"C-18 satisfied unconditionally regardless of model output shape"* — Stage 4 fires whether or not any cross-stage structure was produced, with an explicit default path. This is structurally stronger than C-18's requirement (which only applies when a structure exists). A new criterion can reward the unconditional stage + explicit no-structures default.

2. **V-01 inventory format**: The entry format uses flag markers `[forgotten-call][assumed-to-work][unknown-system][delegation-chain]` that mirror the four C-19 obligation categories exactly — making persona discoveries structurally traceable in the inventory rather than only declared in a preamble. C-19 rewards the declaration; a new criterion rewards the structural linkage between declaration and inventory format.

These become C-20 and C-21.

---

```markdown
# flow-integration Rubric — v6

**Version:** 6 (updated from Round 5 excellence signals)
**Quest:** flow-integration
**Date:** 2026-03-14

---

## Overview

An integration trace maps every call a feature makes to external systems and accounts
for auth, shape, error fate, rate limits, idempotency, and the gaps that threaten
production reliability. This rubric measures whether a trace is complete, analytical,
actionable, and structurally disciplined.

**Tier philosophy:**

- **Essential** (C-01–C-04): documentation completeness — every call accounted for
  with its auth, shape, and error fate; the minimum for any useful integration trace.
- **Recommended** (C-05–C-07): analysis quality — did the trace catch the integration
  failure modes that matter in production?
- **Aspirational** (C-08–C-21): actionability and structural discipline — ranked risk,
  concrete fixes, and organizational guarantees that make the other criteria
  structurally reliable rather than convention-dependent.

**New in v2:** C-10, C-11, C-12 codify the structural patterns that produced perfect
essential coverage in Round 1 (V-04 Gated Phase Lifecycle). These criteria reward
traces that cannot accidentally omit a call or bleed concerns across sections.

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

## Aspirational Criteria (67 pts total)

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

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-21 | 67 |
| **Total** | | **157** |

### Point Allocation

| Criterion | Points | Tier |
|-----------|--------|------|
| C-01–C-04 | 15 each | Essential (60) |
| C-05–C-07 | 10 each | Recommended (30) |
| C-08–C-09 | 5 each | Aspirational |
| C-10–C-14 | 4 each | Aspirational |
| C-15 | 3 | Aspirational |
| C-16–C-17 | 7 each | Aspirational |
| C-18–C-19 | 5 each | Aspirational |
| C-20–C-21 | 5 each | Aspirational (new v6) |
| **Total** | **157** | |

New ceiling: 157 = R5 ceiling 147 + C-20 (5) + C-21 (5)
```

---

**What changed in v6:**

- **C-20** captures the *unconditional stage* pattern from V-01: Stage 4 fires regardless of output shape, with an explicit "No cross-stage structures" default. C-18 requires the three demotion properties *when a structure is present*; C-20 requires the stage to fire even when no structure is present, making C-18 a structural guarantee rather than a conditional one.

- **C-21** captures the *inventory flag alignment* pattern from V-01: the inventory entry format uses `[forgotten-call][assumed-to-work][unknown-system][delegation-chain]` markers that mirror the C-19 obligation categories 1:1. Without this, a model can declare all four obligations correctly and still produce an inventory with no record of which obligation each entry answers to — the persona's work disappears at the inventory boundary.

- **Ceiling**: 147 → 157 (+10).
