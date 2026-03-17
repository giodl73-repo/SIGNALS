Written to `simulations/quest/rubrics/trace-component-rubric-v13-variate-R13-2026-03-15.md`.

---

## trace-component — Round 13 Variations

**Variation axes:** Role sequence (V-01), Lifecycle emphasis (V-02), Phrasing register (V-03), combined (V-04, V-05)

---

### V-01 · Role Sequence — Abstract-Requirements Blank-Slot Authorship *(C-42 target)*

**Hypothesis:** R12 V-02's Requirements A–D gave the model labeled, prescriptive content areas that could be paraphrased. V-01 replaces them with abstract functional questions ("What does a Direction cell mean when it carries no departure code?") that describe the *information need* without supplying copyable rule language. Blank slot + strong anti-copy. C-41 not targeted. Expected: ~154–156/158.

**Key mechanism:** Schema slot is blank with `Do not reproduce any language from this prompt — not even in paraphrase.` Requirements are questions, not prescriptions.

**Placeholder form (C-40):**
`*[From your TRAVERSAL-SCHEMA: reproduce the question-3 close-line verbatim — this is the last line of this manifest.]*`
Content source named (TRAVERSAL-SCHEMA question-3) + position named (last line) + single instruction.

---

### V-02 · Lifecycle Emphasis — Schema Causal Explanation Requirement *(C-41 target)*

**Hypothesis:** Requirement C is split into two steps: (a) answer three causal questions in sequence, then (b) declare the close-line text. The questions force the model to articulate the full enforcement chain — "what does a model contradict if it inserts content between the close-line and the table header?" — before committing to the close-line text. Standard labeled requirements, no anti-copy (clean C-41 isolation). Expected: ~152–156/158.

**Key mechanism:** Requirement C three-question sequence before declaration: why closing position, what is contradicted, why visible at point-of-production.

**Placeholder form:** `*[Apply your TRAVERSAL-SCHEMA Requirement C close-line here — verbatim, as this manifest's last line. You explained why it must be last.]*` — the reminder phrase "You explained why it must be last" references the causal commitment.

---

### V-03 · Phrasing Register — Procedural Dual-Constraint Placeholder *(C-40 target)*

**Hypothesis:** R12's dual-constraint placeholders used compact abbreviation. V-03 tests whether procedurally-enumerated form — both constraints numbered within the placeholder with explicit statement they cannot be satisfied independently — produces stronger C-40 compliance. No schema architect role (C-39 not targeted; close-line declared in TRACE CHARTER). Isolation test: if V-03 scores well on C-40, the dual-constraint phrasing is the mechanism, not the schema-authorship scaffolding. Expected: ~146–150/158.

**Key mechanism:** `*[Two requirements, one instruction: (1) content — reproduce TRACE CHARTER close-line exactly; (2) position — absolute last line of this manifest, TABLE-N follows directly. Neither constraint is satisfied without the other.]*`

---

### V-04 · Combined: Role Sequence + Lifecycle Emphasis *(C-42 + C-41 + C-40)*

**Hypothesis:** V-01's abstract requirements (C-42) + V-02's causal explanation requirement (C-41) in a single schema architect role. Area 3 is a two-part task: first answer the mechanism questions, then declare the close-line. Blank slot + anti-copy enforces authorship; causal questions enforce reasoning commitment; dual-constraint placeholders reference the authored schema. All three criteria via one causal chain. Expected: ~154–158/158.

---

### V-05 · Combined: All Three Axes + Null-Hypothesis Inertia *(C-40 + C-41 + C-42 + C-36)*

**Hypothesis:** V-04 plus structural unification. Area 2 asks why inertia is the null hypothesis for traversal hops. Area 3 asks why the post-manifest position is null by default — and how this is *structurally parallel* to Area 2. Both Direction cells and post-manifest positions share the same epistemic structure: active claims require assertion, the null requires none. A model that authors this unified principle cannot violate either mechanism without contradicting the unified framework it produced. Procedural dual-constraint placeholders (V-03 register). Maximum R13 coverage. Expected: ~156–158/158.

---

**C-40/C-41/C-42 targeting matrix:**

| | C-40 | C-41 | C-42 |
|---|---|---|---|
| V-01 | dual-constraint placeholder | — | primary (abstract reqs + blank + anti-copy) |
| V-02 | dual-constraint placeholder | primary (3-question causal chain) | — |
| V-03 | primary (procedural enumerated) | — | — |
| V-04 | dual-constraint placeholder | causal 3-question | abstract reqs + blank + anti-copy |
| V-05 | procedural dual-constraint | causal + structural parallel to C-36 | abstract reqs + blank + anti-copy |
