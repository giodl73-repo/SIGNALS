Written to `simulations/quest/golden/trace-component-variate-R1-2026-03-15.md`.

---

## trace-component R1 Variations

**5 variations across 3 single-axis + 2 combined:**

---

### V-01 -- Role Sequence
**Axis**: Role sequence (framework-detect → expert-assign → trace)
**Hypothesis**: Naming a framework-specific expert role before the trace anchors vocabulary. A generic "frontend developer" defaults to React even on Vue topics; explicit detection + role activation eliminates the mismatch and forces idiomatic component names (C-02) and state primitives (C-03).

Structure: 3-step preamble (detect → assign → trace), then all 8 output sections in prose. Role is an active constraint on vocabulary throughout, not just a framing sentence.

---

### V-02 -- Output Format
**Axis**: Output format (structured tables)
**Hypothesis**: Each handler and each re-render becomes a table row with typed columns. A missing row is visually obvious; a vague prose phrase cannot hide in a table. Targets C-01 (event chain enumeration) and C-04 (re-render list completeness) most directly.

Structure: Table 1 = event chain, Table 2 = component path, Table 3 = state delta, Table 4 = re-render list; then prose blocks for side effects, issue audit, final UI state.

---

### V-03 -- Lifecycle Emphasis
**Axis**: Lifecycle emphasis (8 named phases with explicit completion criteria)
**Hypothesis**: Phase gates prevent C-01 (event chain) and C-03 (state delta) from bleeding together -- each must be fully populated before the model proceeds. Per-phase completion criteria make partial fulfillment visible during scoring.

Structure: PHASE 1 through PHASE 8, each with a stated completion criterion before content. Phase 5 explicitly produces MISSING-LOADING / MISSING-ERROR notes that become Phase 6 findings.

---

### V-04 -- Combined: Role Sequence + Phrasing Register
**Axis**: Expert identity + conversational walkthrough ("follow the call into...")
**Hypothesis**: Conversational register elicits more specific naming than formal imperative -- the expert explains their reasoning rather than just listing outputs. Surfaces C-06d (accessibility) and C-09 (framework-portable annotations) more naturally, since the expert narrates why things work the way they do.

Structure: Expert self-declaration ("I am a [Framework] Senior Engineer"), then 7 conversational question sections. Adds optional "Framework Notes" section to prompt C-09.

---

### V-05 -- Combined: Output Format + Lifecycle Emphasis + Inertia Framing
**Axis**: Tables + phase gates + naive-DOM baseline column
**Hypothesis**: An inertia column in the re-render table ("Naive Assessment: NEEDED / UNNECESSARY / MEMOIZED-SKIP") makes unnecessary re-renders machine-readable rather than editorial. Any UNNECESSARY row auto-flags for C-06. This is the strongest variation for covering the full rubric but also the most verbose.

Structure: Naive baseline section first, then 8 phases. Tables in Phases 1-4 each have a "Naive Equivalent" or "Naive Assessment" column. Phase 5 produces `MISSING-LOADING` / `MISSING-ERROR` tokens that Phase 6 consumes by reference.

---

**Coverage prediction by variation:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Event chain | strong | very strong | strong | strong | very strong |
| C-02 Component tree | very strong | strong | strong | very strong | strong |
| C-03 State delta | strong | strong | very strong | strong | very strong |
| C-04 Re-render list | strong | very strong | very strong | moderate | very strong |
| C-05 Side effects | moderate | moderate | strong | moderate | strong |
| C-06 Issue flags | moderate | strong | moderate | strong | very strong |
| C-07 Final UI state | moderate | strong | strong | moderate | very strong |
| C-08 Optimization | weak | moderate | moderate | moderate | strong |
| C-09 Framework-portable | moderate | weak | weak | strong | weak |

**Predicted winner for essential coverage (C-01 through C-04)**: V-05 or V-03  
**Predicted winner for full-rubric ceiling**: V-05  
**Predicted winner for C-09 (framework-portable annotations)**: V-04 — the "Framework Notes" section is the only variation that explicitly prompts for it
