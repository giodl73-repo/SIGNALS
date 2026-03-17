---

# prove-synthesize — Round 12 Variations (v12 rubric)

**Date**: 2026-03-15 | **Rubric**: v12 (177.5 pts max) | **Targeting**: C-42 + C-43 simultaneously

---

## Axis plan

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single: Phase-ceiling integration | Add C-39/C-42 to R11 V-02's concurrent gate-block base → earns all 5 new criteria at once |
| V-02 | Single: Output format | Labeled section pairs with inline scoring directives per slot |
| V-03 | Single: Phrasing register | Conversational imperative, second-person — tests register-independence of criteria |
| V-04 | Combined: Lifecycle + Phase ceiling | Per-signal phase annotation pass before synthesis; adds Primary/Supporting/Contextual role classification |
| V-05 | Combined: Inertia framing + Phase ceiling | Status-quo competitor as fourth evidence dimension in ceiling calculation |

---

## V-01 — Phase-ceiling integration (primary target)

**Single axis**: Insert C-39/C-42 pre-synthesis step into R11 V-02's confirmed architecture.

**Additions over R11 V-02**:
- Phase table (Explore/Test/Validate → ceilings 25/50/72/none) before any reasoning
- Mandatory declaration: *"State before proceeding: 'Evidence phase coverage: [phases]. Confidence ceiling: [value or none].'"*

The rest is R11 V-02's concurrent + unified gate block + dual exemplars per role architecture, unchanged.

**Expected score**: ~122.5 (R11 V-02's 117.5 + 2.5 for C-39 + 2.5 for C-42)

**Predicted PASS**: C-39 (phase table + ceilings as pre-synthesis constraint), C-42 (mandatory named declaration step, fixed output form, positioned before reasoning begins), C-35/C-40/C-43 (carried from R11 V-02).

---

## V-02 — Output format

**Single axis**: Replace five floating prose headers with labeled section pairs — each section has an inline *pass condition* directive in italics immediately after it.

**Key structural change**: The self-containment check is dissolved into the sections themselves — each section's pass condition is stated at the section, making C-37 verification mechanical (no separate check needed, but the check section still appears for C-41 revision mandate compliance).

---

## V-03 — Phrasing register

**Single axis**: Conversational imperative ("You are the synthesizer… Watch out for:… Now write this line before you do anything else:").

**Architecture**: Identical to V-01 structurally. The gate block becomes *"Check each role before writing"* with "What failure looks like" / "What passing looks like" per-role pairs. The mandatory declaration becomes an explicit first-person contract: `"Now write this statement before you do anything else: > 'Evidence phase coverage: … Confidence ceiling: …'"`.

---

## V-04 — Lifecycle emphasis + Phase ceiling

**Combined axes**: Full per-signal annotation pass (Phase 1) before synthesis (Phase 2).

**Key addition over V-01**: Rather than inferring phase coverage from the signal set, the model is required to annotate each signal with its Phase (Explore/Test/Validate) and Role (Primary/Supporting/Contextual) before producing the coverage summary. The ceiling is then derived from that annotation rather than estimated.

**What this tests**: Whether more explicit lifecycle scaffolding strengthens C-39/C-42 compliance, and whether Primary/Supporting weighting improves SYNTHESIST gate compliance.

---

## V-05 — Inertia framing + Phase ceiling

**Combined axes**: Inertia coverage as a second classification dimension alongside phase, affecting the ceiling formula.

**Key addition over V-01**: The ceiling table has a second axis — inertia coverage (absent/present) — and the mandatory declaration must include inertia state: *"Inertia coverage: [absent/partial/present]."* The gate block's SYNTHESIST failure mode shifts from "signal averaging" to "inertia blindness."

**What this tests**: Whether the adoption-vs-demand distinction maps cleanly onto C-39/C-42 and whether inertia-specific principles emerge as a consistent pattern.

---

**Output saved**: `simulations/quest/rubrics/prove-synthesize-rubric-v12-variate-R12-2026-03-15.md`
