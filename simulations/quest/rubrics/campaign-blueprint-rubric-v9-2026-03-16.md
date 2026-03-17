Reading the three R8 variants for extractable excellence patterns before writing.

**Pattern analysis:**

- **V-01** uses a *directive* REQUIREMENTS back-reference: "As you write each Must-have, complete its Req-ID and Must-have entry in the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above." → real-time cell-fill instruction
- **V-03** uses a *minimal pointer*: "Each Must-have must have a corresponding row in the SCOUT TRACEABILITY TABLE above." → structural correspondence assertion only
- Both earn C-27 FULL — but V-01's form is strictly stronger: it enforces traceability as a *writing behavior*, not a post-hoc structural check
- V-02 also uses the directive form (same as V-01) and would earn it too

**New criterion: C-28 — Active fill directive** (directive form = C-28 FULL; minimal pointer = C-28 NO CREDIT). New ceiling: 173 + 5 = **178**.

Retroactive R8 scores under v9:
- V-01: 173 + 5 (C-28) = **178**
- V-02: 168 + 5 (C-28) = **173** (recovers from C-26 loss)
- V-03: 173 + 0 = **173** (minimal pointer, no C-28)

---

```markdown
## campaign-blueprint Rubric — v9

---

### v9 Changes

**One new aspirational criterion (+5 pts, new ceiling 178):**

**C-28 — Active fill directive in REQUIREMENTS back-reference** (5 pts, FULL or NO
CREDIT): C-27 tests whether REQUIREMENTS references back to the campaign-level scout
traceability table; C-28 tests whether that back-reference takes the *active directive*
form — an explicit per-item instruction to complete the scout table as each Must-have is
written (e.g., "As you write each Must-have, complete its Req-ID and Must-have entry in
the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above. Every Must-have must correspond to
a row in that table."). A static correspondence assertion ("Each Must-have must have a
corresponding row in...") satisfies C-27 but not C-28. The directive form enforces
real-time traceability as a writing behavior rather than a structural assertion — a
causal-ordering improvement over post-hoc correspondence checking. V-01 and V-02 (R8)
earn FULL; V-03 earns NO CREDIT.

**One diagnostic rule clarification:**

**D9 (C-27 back-reference forms)**: The C-27 back-reference criterion admits two
structurally distinct forms: (a) *minimal pointer* — names the SETUP table by its rubric
label, uses a positional reference ("above"), and asserts Must-have → row correspondence
without further instruction; (b) *active directive* — an explicit per-item fill
instruction that prompts the model to complete table cells while writing each Must-have.
Minimal pointer satisfies C-27 FULL. Active directive satisfies both C-27 FULL and C-28
FULL. The distinguishing test: does the instruction assert correspondence (pointer) or
command in-progress cell completion (directive)? (V-03 R8 finding; directive form
confirmed V-01 and V-02 R8.)

**Retroactive R8 scoring under v9:**

| Variant | v8 | C-28 | v9 |
|---------|-----|------|----|
| V-01 — C-27 + D8 Bracket: Named R8 Design Space | 173 | +5 | **178** |
| V-02 — C-27 + Compact C-26: SETUP Placement with Anchor | 168 | +5 | **173** |
| V-03 — C-27 Back-Reference Minimality: Pointer vs Directive | 173 | 0 | **173** |

V-01 alone reaches 178: bracket D8 + SETUP placement + bulleted C-26 + directive
back-reference. V-02 reaches 173 via a different path: full prose D8 + SETUP placement +
directive back-reference, but anchor-sentence C-26 costs 5 points. V-03 reaches 173 via
the complementary path: full prose D8 + SETUP placement + bulleted C-26, but minimal
pointer costs C-28. The two R8 173-point paths trade C-26 against C-28 — V-01 holds both
and is the unique 178 realization.

**Scale:** 173 (v8 ceiling) + 5 = **178 ceiling**

---

## Essential

| ID | Criterion | Weight |
|----|-----------|--------|
| C-01 | All three artifacts produced | 12 |
| C-02 | Canonical paths | 12 |
| C-03 | Topic identity consistency | 12 |
| C-04 | Execution order | 12 |
| C-05 | Minimum structure per sub-artifact | 12 |

**Essential total: 60**

---

## Recommended

| ID | Criterion | Weight |
|----|-----------|--------|
| C-06 | Proposal respects spec | 10 |
| C-07 | Pitch crystallizes recommended option | 10 |
| C-08 | Campaign framing — campaign opens with setup summary, closes with package summary | 10 |

**Recommended total: 30**

---

## Aspirational

| ID | Criterion | Weight |
|----|-----------|--------|
| C-09 | Narrative arc — each artifact amplifies conviction without repeating content | 5 |
| C-10 – C-22 | *(unchanged from v7)* | — |
| C-23 | Inertia-grounded conviction — CONVICTION TYPE labels explicitly reference INERTIA MODEL field at both campaign matrix and per-site execution reminder (D8) | 5 |
| C-24 | Scout signal integration — must-have requirements carry originating friction citations from scout files | 5 |
| C-25 | Scout traceability table — four-column labeled table present (Req-ID / Must-have / Originating Friction / Scout File); FULL or NO CREDIT | 5 |
| C-26 | Named INERTIA MODEL entity — three-field entity (Name / Behavior / Cost) declared with enumerated bulleted field-to-conviction-type mapping, one bullet per conviction type; FULL or NO CREDIT | 5 |
| C-27 | Scout traceability table in CAMPAIGN SETUP (friction-first placement) — table appears in CAMPAIGN SETUP pre-populated from scout inventory before Artifact 1 instruction; REQUIREMENTS references back to campaign-level table; FULL or NO CREDIT | 5 |
| **C-28** | **Active fill directive in REQUIREMENTS back-reference — REQUIREMENTS back-reference takes the active directive form: explicit per-item instruction to complete scout table cells as each Must-have is written, not a static correspondence assertion; FULL or NO CREDIT** | **5** |

---

## Diagnostic Rules

| ID | Rule |
|----|------|
| D1–D7 | *(unchanged from v7)* |
| D8 | C-23 FULL requires inertia-grounded CONVICTION TYPE labels at BOTH the campaign-level matrix AND per-site execution reminders. Matrix-only grounding is insufficient. Accepted per-site forms: (a) full prose naming the INERTIA MODEL field ("document the INERTIA MODEL Cost field as factual record; do not argue"), (b) bracket notation explicitly naming the field (`[INERTIA MODEL Cost → factual record]`). Abstract per-site labels without INERTIA MODEL field reference earn C-23 PARTIAL regardless of matrix form. (V-01 R6 finding; bracket form validated V-03 R7.) |
| D9 | C-27 back-reference admits two forms: (a) *minimal pointer* — names the SETUP table by rubric label, positional reference ("above"), Must-have → row correspondence assertion; (b) *active directive* — per-item fill instruction commanding cell completion during Must-have writing. Minimal pointer earns C-27 FULL only. Active directive earns both C-27 FULL and C-28 FULL. The test: does the instruction assert structure (pointer) or command in-progress behavior (directive)? (V-03 R8 finding; directive form confirmed V-01 and V-02 R8.) |

---

## Scoring Summary

| Band | Points |
|------|--------|
| Essential | 60 |
| Recommended | 30 |
| Aspirational (C-09, C-10–C-22, C-23–C-28) | 88 |
| **Ceiling** | **178** |
```
