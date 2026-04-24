# Flow-Trigger Skill — Round 11 Variations (Rubric v7)

Saved to `simulations/quest/rubrics/flow-trigger-rubric-v7-R11-2026-03-15.md`.

---

## Design Rationale

R10 found C-20 by accident — every variation annotated TC-2/TC-3 with IF-* labels because the instructions said "cite IF-* where applicable." R11's job is to make this a **designed requirement**, not an emergent behavior, and to find the next above-baseline signal.

---

## V-01 — Role Sequence: IF-* Forward Mesh Pre-Declaration

**Axis**: Role 0 not only produces IF-* failure mode labels — it also pre-declares which TC-2 and TC-3 entries *will* carry each label. Role 1 has a **fulfillment contract**, not a general annotation instruction. Unfulfilled predictions become explicit ⚠ flags that travel downstream.

**Hypothesis**: Pre-declaring expected TC back-references eliminates annotation gaps because Role 1 must satisfy or flag each expectation. An orphaned IF-* label (declared but uncorroborated) becomes detectable at catalog-construction time — earlier than pathology can catch it.

**Structure**: Scenario boundary → Role 0 (IF-* forward mesh predictions with expected TC-2/TC-3 signatures) → Role 1 (TC-1/TC-2/TC-3 with fulfillment status: "confirmed" or "⚠ not confirmed") → Role 2 (trigger table + registry summary) → Role 3 (budget gate) → Role 4 (pathology with verdict-first + 3-layer remediation + callback to Role 0 fulfilled/unfulfilled predictions)

**New signal**: Role 0 fulfillment contract — unfulfilled IF-* predictions are flagged at Phase 1 with `⚠ Role 0 prediction not confirmed`, making mesh gaps visible before the trigger table is built.

---

## V-02 — Output Format: TC-1 IF-* Annotation Column (Full Mesh Extension)

**Axis**: Fill-in schema templates that extend IF-* back-annotation to **TC-1** (candidate trigger conditions), not just TC-2/TC-3. C-20 requires TC-2/TC-3 entries to carry IF-* labels. V-02 bakes a fourth annotation direction into the schema: when a condition's YES/NO evaluation outcome is the proximate cause of a failure mode, TC-1 entries carry IF-* labels too.

**Hypothesis**: Schema-driven annotation of TC-1 closes the remaining unlinked direction of the reference mesh. Risk provenance becomes traceable forward through conditions → cascade paths → side effects, and backward from any catalog cell to its failure mode.

**Structure**: BLOCK A (IF-* schema) → BLOCK B (TC-1 with IF-* annotation column; TC-2 with IF-* required; TC-3 with IF-* required) → BLOCK C (trigger table) → BLOCK D (registry summary) → BLOCK E (budget gate) → BLOCK F (pathology schema with BLOCK B citations in evidence field)

**New signal**: TC-1 IF-* annotation column — when a trigger condition's evaluation outcome drives a failure mode, the condition entry is annotated at the catalog level, extending C-20's bidirectional mesh to all three TC sections.

---

## V-03 — Lifecycle Emphasis: Orphaned IF-* Detection Gate

**Axis**: A dedicated **mesh completeness check** runs between Phase 1A (threat cataloging) and Phase 1B (trigger table), structured as a verification table with COMPLETE/ORPHANED status per IF-* label. A phase gate blocks table construction until the check is present.

**Hypothesis**: An explicit completeness check produces stronger C-20 compliance than per-entry annotation instructions because it surfaces null cases structurally. A model can annotate TC-2/TC-3 entries correctly while leaving IF-Circular ORPHANED (no TC entry references it) if the scenario has no circular candidates. The check gate forces this null case to be explicit.

**Structure**: Phase 0 (Inertia Analyst) → Phase 1A (threat cataloging with IF-* annotations) → **Mesh Completeness Check** (table: IF-* label | TC-2 count | TC-3 count | COMPLETE/ORPHANED) → Phase 1B (trigger table) → Phase 2 (budget) → Phase 3 (pathology)

**New signal**: Mesh completeness check table — structured verification artifact making ORPHANED failure modes explicit; an absent check is a failure, an ORPHANED status is a valid explicit null result.

---

## V-04 — Combined: Role Sequence + Phrasing Register

**Axes**: Role sequence (IF-* forward mesh prediction) + Phrasing register (investigative narrative: "predict before you observe, return to your predictions in Step 5").

**Hypothesis**: When the Inertia Analyst's mandate is framed as "stake your claims before you look at the data," and Step 5 explicitly returns to those claims to verify which predictions were confirmed vs. unfulfilled, the pre-analysis phase becomes a testable hypothesis — not a labeling chore. The callback in Step 5 produces richer pathology evidence because the model closes a loop it opened.

**Structure**: Step 1 (Inertia Analyst: "imagine the worst — stake your failure mode claims, predict TC-2/TC-3 signatures") → Step 2 (Threat Cataloger: map threat surface + verify Step 1 predictions in TC-2/TC-3) → Step 3 (Registry Analyst) → Step 4 (Budget Analyst) → Step 5 (Pathology Analyst: "Return to your claims from Step 1 — which predictions were confirmed, which were unfulfilled?")

**New signal**: Prediction-callback loop — Step 5 explicitly compares Step 1 predictions against catalog evidence before rendering a verdict; the pathology section becomes a hypothesis verification rather than a pattern detection.

---

## V-05 — Combined: Lifecycle Emphasis + Output Format + Inertia Framing

**Axes**: Lifecycle emphasis (hard ⛔ gates) + Output format (fill-in schema) + Inertia framing (Role 0 exclusion boundary language + "IF-none" as explicit null annotation).

**Hypothesis**: Three orthogonal enforcement mechanisms together: phase gates prevent section skipping, schema templates prevent structural omissions, and the "IF-none" explicit null annotation prevents silent omissions from being misread as compliance. Every TC-2/TC-3 entry must carry an IF-* annotation — either a real failure mode label or the mandatory "IF-none" null.

**Structure**: BLOCK A (Inertia Analyst: IF-* schema; "absolute boundary — no involvement in downstream blocks") → BLOCK B (TC-1 with IF-* column; TC-2/TC-3 with IF-* required including "IF-none" for null cases) → BLOCK C (trigger table) → BLOCK D (registry summary) → BLOCK E (budget gate) → BLOCK F (pathology fill-in schema with 3-layer remediation labeled fields)

**New signal**: "IF-none" explicit null annotation — TC-2/TC-3 entries that don't drive any failure mode carry a mandatory "IF-none" annotation rather than a blank cell. Blank cells become structurally invalid, not just undesirable — a row with no IF-* annotation invalidates the block.

---

## Variation Summary

| Variation | Axes | New Signal Targeted | C-20 Mechanism |
|-----------|------|---------------------|----------------|
| V-01 | Role sequence | IF-* forward mesh pre-declaration; fulfillment flags | Role 0 declares expected TC-2/TC-3 entries; Role 1 confirms or ⚠-flags each |
| V-02 | Output format | TC-1 IF-* annotation column; full three-TC mesh | Schema column on TC-1/TC-2/TC-3 each carry IF-* annotation field |
| V-03 | Lifecycle emphasis | Orphaned IF-* detection gate (mesh completeness check) | Explicit gate table: COMPLETE/ORPHANED status per IF-* label |
| V-04 | Role sequence + phrasing register | Prediction-callback loop (Step 1 predictions → Step 5 return-to-claims) | Step 2 verifies Step 1 predictions; Step 5 closes each claim |
| V-05 | Lifecycle + format + inertia framing | "IF-none" explicit null annotation; Role 0 absolute exclusion boundary | TC-2/TC-3 schema: blank IF-* cells invalid; "IF-none" is required null |
