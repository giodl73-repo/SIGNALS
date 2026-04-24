Written to `simulations/quest/rubrics/topic-plan-rubric-v4-variations-R4-2026-03-15.md`.

---

# topic-plan Round 4 — V-01 through V-05

**Rubric**: v4 (C-01–C-20, 150 pts)
**Universal gaps targeted**: C-13 (inline evidence in diff, failed all R3), C-16 (two-level traceability, all R3 PARTIAL), C-17 (null conflict declaration, 2 R3 failures), C-19 (Proposal ID in diff, new), C-20 (Delta Finding column in proposals, new)

---

## V-01 — Signals-First
**Axis**: Role sequence — signals read before strategy
**Hypothesis**: Reading signals before strategy primes contrast-based delta detection. The strategy becomes the "what they thought" document encountered *after* evidence is in memory, sharpening the "Strategy assumed X" anchor that C-18 requires and that C-20's Delta Finding column depends on.

**Key structural bets**:
- Step 1 reads and IDs all signals; Step 2 reads strategy — contrast is already loaded when the delta step runs
- Step 6 proposal table: mandatory Proposal ID + Delta Finding columns (C-19, C-20)
- Step 7 diff: Evidence inline `[file.md — finding]` + Proposal column (C-13, C-19)
- Step 5 conflict null: "format-agnostic" mandatory rule — closes the V-01/V-04 R3 gap in C-17

---

## V-02 — Template-Driven
**Axis**: Output format — explicit table templates with named columns
**Hypothesis**: When the template names "Delta Finding" and "Proposal ID" as literal column headers the model must fill, compliance is mechanical fill-in-the-blank. C-19 and C-20 pass without the model needing to reason about navigability.

**Key structural bets**:
- Phases A–I each begin with "fill every cell" + an empty template
- Phase F (proposals): template pre-declares all columns including `Delta Finding` and `Proposal ID`
- Phase G (diff): template pre-declares `Evidence` inline column and `Proposal` cross-reference column
- Phase E (conflict): required null row reproduced exactly — model copies it when no conflicts found

---

## V-03 — Conversational Register
**Axis**: Phrasing register — first-person
**Hypothesis**: "I'll build the proposals table, making sure each row has its Delta Finding column..." — first-person narration commits the model to the structure *before* the table is built, creating a self-monitoring channel. R3 V-05 scored 130/140 with this register; isolated test of whether register alone can hit C-19 and C-20.

**Key structural bets**:
- Steps narrated in first person: "I'll check every namespace — scout, draft, review..."
- Step 6: narrates "Each row will carry a Proposal ID... a Delta Finding column..." then builds the table
- Step 7: narrates "Each diff row will have Evidence inline and a Proposal column..." then builds the table
- C-17: "I'll say so explicitly... I'll write 'No conflicts detected.' rather than leaving this section blank... regardless of whether I'm using a table or inline annotation"

---

## V-04 — Hypothesis-First + Unified Table
**Axis**: Role sequence + Output format — gap hypothesis formed before reading; proposals and diff merged into one table
**Hypothesis**: (1) Pre-reading hypothesis forces the model to approach files as evidence for/against predictions. (2) A unified table merging proposals, before/after, evidence, and Delta Finding into one structure eliminates the C-13/C-19/C-20 navigation problem entirely — there are no separate sections to cross-reference.

**Key structural bets**:
- Step 1: hypothesis table before any file is read
- Step 3: hypothesis revision step after strategy is read (creates a double-update of the causal chain)
- Step 6: single unified table with columns `Proposal ID | Type | Namespace | Before | After | Delta Finding | Evidence | Confidence` — replaces separate proposals and diff sections entirely
- C-13 + C-19 are collapsed: the unified table has Evidence inline AND is self-cross-referencing (no Proposal ID needed because Before/After are already in the same row)

---

## V-05 — Inertia-Foregrounded
**Axis**: Lifecycle emphasis + Inertia framing — strategy commitments reconstructed in full before reading signals; every proposal row names cost of inaction
**Hypothesis**: Making the strategy's unstated assumptions explicit (Step 1 "What it assumed without naming") before signals are read creates the richest possible "Strategy assumed X" anchor. Adding an "If unchanged: [cost]" column to every proposal forces the model to have traced the causal path from assumption → gap → consequence — making C-20's Delta Finding entries naturally substantive rather than mechanical label fills.

**Key structural bets**:
- Step 1: strategy reconstruction table includes "What it assumed without naming — at least one item"
- Step 2: signal inventory includes "Confirms or challenges which assumption?" column
- Step 6: proposals table has an "If unchanged" column alongside Delta Finding and Proposal ID
- C-17: "mandatory null case... regardless of whether your format is tabular or inline" — format-agnostic, closes R3 V-01/V-04 gap
- R3 V-04 (inertia axis) lost C-14 (partial) and C-17 (fail); V-05 fixes both with verbatim anti-inventory warning and format-agnostic null rule

---

## Coverage Matrix Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-13** inline evidence in diff | Evidence col | Template-forced | Narrated | Unified inline | Evidence col |
| **C-14** anti-inventory verbatim | Verbatim | Verbatim | Verbatim | Verbatim | Verbatim |
| **C-16** two-level chain | Delta Finding + Evidence cols | Template-forced | Narrated | Unified table | Delta Finding + If unchanged |
| **C-17** null conflict declaration | Format-agnostic | Null row | Format-agnostic | Null row | Format-agnostic |
| **C-19** Proposal ID in diff | Proposal col | Template-forced | Narrated | Unified (no separate diff) | Proposal col |
| **C-20** Delta Finding in proposals | Mandatory col | Template-forced | Narrated then mandatory | Unified table | Mandatory + inertia forces depth |

All 5 variations target all 5 gap criteria simultaneously. The discrimination will be in execution fidelity — V-02's template-forcing vs V-03's narration-first vs V-04's structural collapse of the navigation problem entirely.
