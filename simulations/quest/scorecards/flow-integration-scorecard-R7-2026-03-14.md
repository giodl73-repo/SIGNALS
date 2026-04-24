# flow-integration — Round 7 Scoring

## Rubric Summary (167-pt ceiling)

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 to C-04 | 60 |
| Recommended | C-05, C-06 | 30 |
| Aspirational | C-08–C-21 | 67 |
| **v7 new** | C-22, C-23 | 10 |
| **Total** | | **167** |

---

## V-01 — Role Sequence + Vocabulary Unification

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Call inventory | PASS | Role sequence structure enumerates calls with types; unknown/assumed entries present |
| C-02 Auth documentation | PASS | Each call block includes explicit auth entry |
| C-03 Request/response format | PASS | Method + key fields in separate labeled positions per call |
| C-04 Error propagation | PASS | Explicit error-disposition statement per call |
| C-05 Rate limit exposure | PASS | Rate limit entry per external system in call block |
| C-06 Retry/idempotency | PASS | Retry strategy stated; non-idempotent calls flagged |
| C-08–C-17 Structural depth | PASS | Role sequence with expert persona before Stage 1; in-block rate limit; secondary positioning |
| C-18 Secondary positioning | PASS | Fan-out registry declared as populated FROM call block |
| C-19 Four-obligation persona | PASS | All four: forgotten-call, assumed-to-work, unknown-system, delegation-chain |
| C-20 Unconditional coda | PASS | Coda fires unconditionally with explicit no-structures default path |
| C-21 Flag alignment | PASS | Flag markers trace back to obligation categories in inventory entry |
| **C-22 Vocabulary unification** | **PASS** | `VOCABULARY RULE` block immediately after obligation list; explicit "the persona term and the flag name are the same token" — structural enforcement, not implicit |
| **C-23 Unnumbered coda** | **PASS** | Heading `**CROSS-STAGE CODA** *(no stage number — appended after Stage 3)*` — appended after last numbered element, displaces nothing |

**Score: 167 / 167**

---

## V-02 — Table Format + Obligation Table Schema

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Call inventory | PASS | Table format makes call enumeration visually complete |
| C-02 Auth documentation | PASS | Auth column in inventory table |
| C-03 Request/response format | PASS | Method + fields in separate labeled table columns |
| C-04 Error propagation | PASS | Error disposition column per row |
| C-05 Rate limit exposure | PASS | Rate limit column in call table |
| C-06 Retry/idempotency | PASS | Retry/idempotency column present |
| C-08–C-17 Structural depth | PASS | 4-row obligation table makes C-19 row-count auditable; missing row = structurally absent obligation |
| C-18 Secondary positioning | PASS | Secondary positioning declared in table header context |
| C-19 Four-obligation persona | PASS | 4-row table — row count is the completeness check |
| C-20 Unconditional coda | PASS | Unnamed table block appended; no-structures default path in block preamble |
| C-21 Flag alignment | PASS | Flag tokens in inventory columns trace to obligation row terms |
| **C-22 Vocabulary unification** | **PASS** | Column header cells in inventory = Obligation Term cells in persona table; mismatch is visible as header/cell discrepancy — mechanically enforced, strongest C-22 implementation |
| **C-23 Unnumbered coda** | **PASS** | `**CROSS-STAGE AGGREGATION STRUCTURES** *(no section number — appended after Section 3)*` — unnumbered suffix after last section |

**Score: 167 / 167**

**Notable:** Table-column identity is the most structurally auditable C-22 mechanism — a reviewer cannot fail to notice a header/cell token mismatch. Addresses Q2 open question: 4-row obligation table does provide structural completeness guarantee.

---

## V-03 — Declarative Register

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Call inventory | PASS | Declarative inventory enumeration |
| C-02 Auth documentation | PASS | Auth stated per call in declarative prose |
| C-03 Request/response format | PASS | Method + fields in labeled sections |
| C-04 Error propagation | PASS | Disposition statement in declarative form per call |
| C-05 Rate limit exposure | PASS | Rate limit declared per system |
| C-06 Retry/idempotency | PASS | Retry strategy in declarative form |
| C-08–C-17 Structural depth | PASS | Expert persona declaration; in-block rate limit; secondary positioning in declarative prose |
| C-18 Secondary positioning | PASS | Declarative "fan-out registry is populated FROM call block" |
| C-19 Four-obligation persona | PASS | Four obligations stated in declarative list |
| C-20 Unconditional coda | PASS | "This coda fires unconditionally..." — explicit declarative default path |
| C-21 Flag alignment | PASS | Declarative correspondence between flag labels and obligations |
| **C-22 Vocabulary unification** | **PASS** | "Each flag label is the same token as its obligation term" + "A flag label that semantically corresponds to but does not match an obligation term introduces a vocabulary mismatch... the reviewer cannot follow the persona-to-inventory chain without an external mapping" — declarative but explicit |
| **C-23 Unnumbered coda** | **PASS** | Declarative coda appended after Stage 3; no number assigned |

**Score: 167 / 167**

**Note:** Declarative register satisfies C-22 but the enforcement is weaker than V-02's structural column-header mechanism — a model could produce "semantically corresponding" flag labels in output even when instructed otherwise. Score prediction is 167 under strict criterion reading but this variation carries higher execution risk.

---

## V-04 — Phase Architecture + Coda Positioning Test *(R7 probe)*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Call inventory | PASS | Phase architecture includes call inventory in Phase 1/2 |
| C-02 Auth documentation | PASS | Auth per call in Phase 1 |
| C-03 Request/response format | PASS | Method + fields per call block |
| C-04 Error propagation | PASS | Error disposition per call |
| C-05 Rate limit exposure | PASS | Rate limit exposure in Phase 1 |
| C-06 Retry/idempotency | PASS | Retry analysis in Phase 2 |
| C-08–C-17 Structural depth | PASS | Expert persona in Phase 1; in-block rate limit; secondary positioning |
| C-18 Secondary positioning | PASS | Secondary positioning declared in Phase 1 |
| C-19 Four-obligation persona | PASS | Four obligations in Phase 1 persona block |
| C-20 Unconditional coda | PASS | Coda fires unconditionally; default path present |
| C-21 Flag alignment | PASS | Flag markers in Phase 2 inventory trace to Phase 1 obligation terms |
| **C-22 Vocabulary unification** | **PASS** | `VOCABULARY RULE` in Phase 1 persona block; token-identity requirement stated |
| **C-23 Unnumbered coda** | **FAIL** | Coda heading: `*(no phase number — appended after Phase 2, before Phase 3)*` — **not appended after the last numbered element.** C-23 requires the coda to be a terminal suffix after the final numbered element of the outer frame. Placement between Phase 2 and Phase 3 displaces the coda from the terminal position; the outer frame continues after it. This violates the "appended after the last numbered element" constraint implicit in C-23's composition-primitive definition. |

**Score: 162 / 167** (−5 on C-23)

**Probe Result:** V-04 **reveals a real constraint in C-23.** The coda-before-last-element placement does not satisfy the criterion. C-23's "appended after the last numbered element" is not merely a stylistic suggestion — it is the mechanism by which the coda "displaces nothing." A mid-sequence unnumbered element displaces the relative position of all subsequent numbered elements if those elements must be referenced by number from external structures. C-20/C-23 carry an implicit terminal-position constraint that should be made explicit in a future rubric version.

---

## V-05 — Non-Standard Terminology + Obligation Table *(combined)*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Call inventory | PASS | Call inventory present with non-standard obligation terms applied throughout |
| C-02 Auth documentation | PASS | Auth per call |
| C-03 Request/response format | PASS | Method + fields per call |
| C-04 Error propagation | PASS | Error disposition per call |
| C-05 Rate limit exposure | PASS | Rate limit per system |
| C-06 Retry/idempotency | PASS | Retry analysis present |
| C-08–C-17 Structural depth | PASS | 4-row obligation table; in-block rate limit; secondary positioning |
| C-18 Secondary positioning | PASS | Secondary positioning in table context |
| C-19 Four-obligation persona | PASS | 4-row table: `shadow-call`, `taken-for-granted`, `fog-system`, `relay-chain` — row count is structural completeness |
| C-20 Unconditional coda | PASS | Coda fires unconditionally |
| C-21 Flag alignment | PASS | `[shadow-call]`, `[taken-for-granted]`, `[fog-system]`, `[relay-chain]` flags in inventory trace to table rows |
| **C-22 Vocabulary unification** | **PASS** | Obligation Term column → inventory column headers are identical tokens. Explicit rule: "YOU MUST NOT use `[forgotten-call]` when the obligation term is 'shadow-call'." Non-standard-to-non-standard matching is the C-22 contract — canonical substitution explicitly forbidden |
| **C-23 Unnumbered coda** | **PASS** | Unnumbered coda appended after Stage 3; terminal position |

**Score: 167 / 167**

**Notable:** The explicit prohibition of canonical substitution in V-05 is the strongest C-22 signal — it makes the non-standard-to-non-standard contract unambiguous and prevents a model from "helpfully" normalizing to canonical terms.

---

## Ranking

| Rank | Variation | Score | C-22 | C-23 |
|------|-----------|-------|------|------|
| 1 (tied) | V-02 Table Format | **167/167** | Table-column identity (structural) | Unnamed block after Section 3 |
| 1 (tied) | V-05 Non-Standard Terminology | **167/167** | Non-std→non-std + canonical-substitution prohibition | Unnumbered coda after Stage 3 |
| 1 (tied) | V-01 Role Sequence | **167/167** | Explicit VOCABULARY RULE block | Coda after Stage 3 |
| 1 (tied) | V-03 Declarative Register | **167/167** | Declarative token-identity statement | Declarative coda after Stage 3 |
| 5 | V-04 Phase Architecture (probe) | **162/167** | PASS | FAIL — coda not at terminal position |

---

## Excellence Signals

**From V-02 (top structural pattern):**
- **Table-column identity** is the highest-confidence C-22 mechanism. When the obligation term in the persona table and the flag column header in the inventory table are the same cell token, a mismatch is visible as a structural discrepancy — it does not require a reviewer to trace prose. This is structurally enforced C-22, not declaratively enforced.

**From V-05 (top semantic pattern):**
- **Canonical-substitution prohibition** is the correct C-22 complement for non-standard terms. The rule must explicitly forbid normalizing a non-standard persona term to a canonical flag name. Without this prohibition, a model can satisfy C-21 (semantic correspondence) while violating C-22 (token identity).
- **Non-standard term ecosystem round-trip** — when non-standard terms flow consistently from obligation table → flag column headers → inventory entries, the persona-to-inventory chain is traceable without an external mapping. C-22 is satisfied for any consistent term set, canonical or not.

**From V-04 (probe finding):**
- **C-23 terminal-position constraint** is real and implicit. The unnumbered coda only satisfies C-23 when it is the terminal element of the outer frame. A coda inserted between numbered elements is not an additive composition primitive — it becomes a displacement mechanism for subsequent elements. Future rubric revision should make this constraint explicit.

---

```json
{"top_score": 167, "all_essential_pass": true, "new_patterns": ["table-column identity enforces C-22 structurally — obligation term in persona table row = inventory column header, mismatch is visible as structural discrepancy not prose ambiguity", "canonical-substitution prohibition is required C-22 complement for non-standard terms — explicit rule must forbid normalizing non-standard persona terms to canonical flag names", "C-23 carries implicit terminal-position constraint — unnumbered coda must be appended after the last numbered element; mid-sequence coda placement does not satisfy the composition-primitive definition even when unnumbered"]}
```
