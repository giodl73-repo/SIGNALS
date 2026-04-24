Written to `simulations/quest/golden/flow-resilience-variate-R1-2026-03-15.md`.

---

## Round 1 Variations — flow-resilience

**5 variations across 3 single-axis + 2 combination axes:**

---

### V-01 — Role Sequence: DS Expert First
**Axis**: Role sequence
**Hypothesis**: Leading with the distributed systems expert anchors scenarios in technically correct failure terminology before commerce context is applied. Prevents C-04 failure (impossible consistency guarantees) because the DS expert constrains what is physically possible before the commerce expert names the scenarios.

Structure: DS expert catalogs failure modes by class → Commerce expert maps each to a named commerce flow → Gap identification in three typed sections → Conflict resolution adequacy pass.

---

### V-02 — Output Format: Scenario Table
**Axis**: Output format
**Hypothesis**: A table with mandatory named columns (Scenario / Class / State / Capability / Data-at-Risk / Recovery) makes it structurally impossible to omit a field (C-02). A blank cell is more salient than a missing prose section. Class column makes degradation coverage (C-01) inspectable without reading the full artifact.

Structure: Phase 1 scenario discovery (names only, no analysis) → Phase 2 six-column table, every cell mandatory → Phase 3 three labeled gap sections (OEG-NN / DCV-NN / MRF-NN) → Phase 4 conflict resolution per Class C row.

---

### V-03 — Lifecycle Emphasis: Pre-Classification Gate
**Axis**: Lifecycle emphasis
**Hypothesis**: An explicit Gate 0 coverage contract — fill in scenario slots for all three classes before writing any analysis — prevents late coverage collapse. The roster creates a visible contract a reviewer can check without reading the full artifact.

Structure: Gate 0 roster (declare all scenario names, minimum 2 per class) → Gate 1 four-field analysis per scenario → Gate 2 three typed gap sections → Gate 3 conflict resolution review.

---

### V-04 — DS Expert First + Scenario Table
**Axes**: Role sequence + Output format
**Hypothesis**: The DS expert generates a confidence-annotated catalog (high/medium/low + "commerce grounding needed"); the table is the format for the commerce-grounded four-field analysis. Together they address the two most commonly co-occurring failure modes: technically incorrect scenarios that look complete, and complete scenarios with missing analysis fields.

Structure: Role 1 (DS expert) produces failure mode catalog with confidence ratings → Role 2 (Commerce expert) grounds each high/medium-confidence scenario in a named commerce operation → Seven-column table (adds Commerce Flow column) → Gap identification → Conflict resolution.

---

### V-05 — Scenario Table + Pre-Classification Gate + Conversational Register
**Axes**: Output format + Lifecycle emphasis + Phrasing register
**Hypothesis**: Conversational phrasing ("What could a shopper still do?" vs. "enumerate user capabilities") lowers the abstraction barrier for C-05 commerce grounding. The table structures that conversational output into rigid schema. The pre-classification roster prevents conversational drift from causing coverage collapse.

Structure: Roster with explicit "why can't you fill this?" accountability → Table with conversational column headers and inline examples of useful vs. useless cell content → Three gap sections with "explicit nil finding" norm → Split-brain dialog ("which one wins — and is that the right choice?") per Class C row.

---

**Signal candidates to watch across rounds:**
1. **Column-enforced four-field** (V-02, V-04, V-05) — does table format reliably prevent missing-field failures, or do models still produce trivial cell content?
2. **Pre-scan class roster** (V-03, V-05) — does upfront commitment to class coverage prevent late omission, or does the model just fill slots with low-quality scenario names?
3. **Conversational recovery elicitation** (V-05) — does "who does what, in order" phrasing produce better actor-labeled recovery paths than the formal imperative phrasing in V-01/V-02/V-03?
