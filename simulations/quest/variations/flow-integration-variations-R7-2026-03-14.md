Written to `simulations/quest/rubrics/flow-integration-rubric-v7-R7-2026-03-14.md`.

---

## R7 Variations — flow-integration (167 pt ceiling)

**Axes selected:** role sequence (V-01), output format (V-02), phrasing register (V-03) — then combined: lifecycle + coda ordering (V-04), terminology + obligation table (V-05).

---

### V-01 — Role Sequence + Vocabulary Unification
**Axis:** Role sequence
**Hypothesis:** Explicit vocabulary rule placed between persona declaration and inventory format instruction enforces C-22 at zero cost. Dropping "4" from "Stage 4" → unnumbered coda satisfies C-23 without renumbering anything.

**C-22 mechanism:** `VOCABULARY RULE` block immediately after obligation list: "A flag whose name semantically corresponds to but does not match an obligation term does not satisfy this rule. The persona term and the flag name are the same token."

**C-23 mechanism:** Heading reads `**CROSS-STAGE CODA** *(no stage number — appended after Stage 3)*`

---

### V-02 — Table Format + Obligation Table Schema
**Axis:** Output format (tables)
**Hypothesis:** 4-row obligation table makes C-19 completeness visually auditable — a missing row is a structurally absent obligation. Column headers in inventory table enforce C-22 mechanically: header cell = obligation term cell. Tests R7 open question 2.

**C-22 mechanism:** Column headers `[forgotten-call]` ... in inventory table = Obligation Term cells in persona table. Mismatch is visible as a header/cell discrepancy.

**C-23 mechanism:** Heading `**CROSS-STAGE AGGREGATION STRUCTURES** *(no section number — appended after Section 3)*`

---

### V-03 — Declarative Register
**Axis:** Phrasing register (declarative)
**Hypothesis:** "Each flag label is the same token as its obligation term" in declarative prose satisfies C-22 without switching register. Coda description in declarative form ("This coda fires unconditionally...") composes cleanly.

**C-22 mechanism:** Declarative correspondence statement: "A flag label that semantically corresponds to but does not match an obligation term introduces a vocabulary mismatch... the reviewer cannot follow the persona-to-inventory chain without an external mapping."

**C-23 mechanism:** `**CROSS-STAGE CODA** *(no stage number — appended after Stage 3)*`

---

### V-04 — Phase Architecture + Coda Positioning Test *(R7 probe)*
**Axes (combined):** Lifecycle emphasis + coda ordering
**Hypothesis (probe):** C-20 and C-23 specify no position relative to the gap inventory. Moving the unnumbered coda to **after Phase 2, before Phase 3** satisfies both criteria literally. If no scoring penalty, coda-before-gaps is valid and no positioning constraint is needed. If penalty appears, C-20/C-23 have an implicit constraint gap.

**C-22 mechanism:** `VOCABULARY RULE` in Phase 1 persona block.

**C-23 mechanism:** `**CROSS-STAGE CODA** *(no phase number — appended after Phase 2, before Phase 3)*` — tests whether C-23 requires coda-after-gaps specifically.

---

### V-05 — Non-Standard Terminology + Obligation Table *(combined)*
**Axes (combined):** Terminology variation + obligation table schema
**Hypothesis:** Non-standard terms (`shadow-call`, `taken-for-granted`, `fog-system`, `relay-chain`) in a 4-row table provide both Q2 structural completeness (row count) and C-22 vocabulary identity (flag token = table row term) in one structure. Non-standard-to-non-standard matching is the C-22 contract.

**C-22 mechanism:** Obligation Term column in persona table → flag tokens in inventory. `VOCABULARY RULE` explicitly forbids canonical substitution: "YOU MUST NOT use `[forgotten-call]` when the obligation term is 'shadow-call'."

**C-23 mechanism:** `**CROSS-STAGE CODA** *(no stage number — appended after Stage 3)*`

---

### Variation Summary

| ID | Axis | C-22 | C-23 | Probe |
|----|------|------|------|-------|
| V-01 | Role sequence | Explicit rule block after obligations | Coda after Stage 3 | — |
| V-02 | Table format | Column header = obligation term (table-enforced) | Unnamed table block after Section 3 | Q2: obligation table |
| V-03 | Declarative register | Declarative correspondence statement | Declarative coda after Stage 3 | — |
| V-04 | Phase + coda ordering | Vocabulary rule in Phase 1 | Coda **after Phase 2, before Phase 3** | Q1: coda-before-gaps |
| V-05 | Terminology + table | Non-standard term = flag token (table row → header) | Unnamed coda after Stage 3 | Q2: obligation table (non-standard) |

**Scoring predictions:** V-01/V-02/V-03/V-05 → 167/167. V-04 → 167 if no coda positioning constraint in C-20/C-23; reveals constraint gap if scored lower.
