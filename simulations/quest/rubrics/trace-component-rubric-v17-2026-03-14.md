v17 written to `simulations/quest/rubrics/trace-component-rubric-v17-2026-03-15.md`.

---

**Three criteria promoted from R16:**

| # | Name | Source | What it adds over v16 |
|---|------|--------|-----------------------|
| **C-52** | Compound Register Header Format | C-49 V-01 PASS — `**NULL REGISTER** -- Epistemic status of null cases` as compound header | C-49 requires a named section label; C-52 requires the compound form (bold label + em-dash + descriptor) so identity and function are co-declared in a single parseable line |
| **C-53** | Horizontal-Rule Boundary Separators Between Named Registers | C-49 V-01 PASS — "with horizontal rule separators" | C-49 requires named labels as distinct document elements; C-53 requires `---` separators at register boundaries, making each boundary a document-level structural event independent of the label change |
| **C-54** | Epistemic-Function Descriptor on Named Register Headers | C-49 V-01 PASS — "Epistemic status of null cases", "Properties of departure claims" | C-52 requires a descriptor field; C-54 requires that field's content to characterize what cognitive/epistemic work the register performs, not its topic, contents, or structural position |

**Ceiling: 176 → 182 pts** (3 new × 2 pts). **54 criteria.**

**R16 triple structure:**
- C-52 and C-54 stack on C-49: C-52 adds the compound form, C-54 constrains the descriptor's content quality
- C-53 is independent: horizontal-rule boundaries exist regardless of header format
- C-54 requires C-52 as a precondition; C-52 and C-53 are independent of each other
