`topic-story-rubric-v11-variations-R11-2026-03-15.md` written.

---

## R11 Variations -- `topic-story` (v11 Rubric)

**Three variation axes explored** (all preserve C-37/C-38/C-39 from R10 V-05):

---

### V-01 -- Single-Axis: Inertia Framing
**Axis**: How prominently the status-quo competitor is featured

**Hypothesis**: The S1 build-decision filter asks "Does this finding change whether to build `{topic}`?" without naming the null hypothesis (the status quo: not building). `**Inertia verdict**:` labels say "moves the prior position" without grounding the prior. S4 explicitly measures against `**Prior position**:` -- but S1, which decides what reaches S4's measurement, uses a disconnected filter. Naming the status quo competitor in S1 ties curation directly to the inertia axis baseline.

**Changes**: S1 filter → "Does this finding move the decision away from the status quo (not building `{topic}`)?" / `**Inertia verdict**:` YES/NO/PARTIAL labels rewritten to reference displacing vs. confirming the status quo.

---

### V-02 -- Single-Axis: Output Format (Inventory Section Column)
**Axis**: Table format -- Section column added to field inventory

**Hypothesis**: The inventory is "auditable from this table alone" for constraints but not for placement -- an auditor still needs section templates to know where `**Pattern claim**:` and `**Verdict consequence**:` live. Adding a Section column (S1/S2/S3/S4 per field) extends the "auditable from this table" principle from constraints to placement, completing the registry.

**Changes**: Inventory table restructured with 5 rows (Falsifiability axis split by section: S1, S2, S3, S4; Inertia-framing axis row stays as S4). Extension protocol step 2 adds "section" to what must be registered.

---

### V-03 -- Single-Axis: Lifecycle Emphasis (Per-Section Entry Conditions)
**Axis**: How explicitly section boundaries are stated as sequencing gates

**Hypothesis**: Layer 1 checklist verifies template compliance but does not enforce writing order -- an author can write S4 before S2. Per-section entry conditions make the sequence structurally explicit: S2 requires S1's `**Inertia verdict**:` fields to be written; S3 requires S2's `**Pattern claim**:` and `**Disproof condition**:` committed; S4 requires S3's `**Verdict consequence**:` written.

**Changes**: Bold **Entry condition** block added at the top of S1 (checklist gate), S2, S3, S4 -- each naming the predecessor fields that must exist before entry is valid.

---

### V-04 -- Compound: V-01 + V-02
Status quo in S1 filter + Section column in inventory. Two structurally distinct locations with no interaction -- both fire without conflict.

---

### V-05 -- Compound: V-01 + V-02 + V-03 + Entry-Condition/Inventory Integration
All three axes plus: each per-section entry condition (V-03) cross-references the **inventory row** (V-02) as its authority for prerequisite fields rather than naming those fields independently. S2's entry condition names "Falsifiability axis, S1 row" as the source; S3 names "Falsifiability axis, S2 row"; S4 names "Falsifiability axis, S3 row." A maintainer adding a new field to an inventory row automatically propagates to the entry condition that references that row. Extension protocol gains step 4: update the entry condition of the following section to cross-reference the new inventory row. Reference hierarchy: inventory row → section template → next section's entry condition.
