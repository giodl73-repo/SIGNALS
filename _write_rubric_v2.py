"""Write topic-roadmap-rubric-v2-2026-03-17.md"""
import re

v1_path = "C:/src/sim/simulations/quest/rubrics/topic-roadmap-rubric-v1-2026-03-17.md"
v2_path = "C:/src/sim/simulations/quest/rubrics/topic-roadmap-rubric-v2-2026-03-17.md"

with open(v1_path) as f:
    src = f.read()

# --- patch frontmatter version ---
src = src.replace("version: 1", "version: 2", 1)

# --- patch scoring formula (aspirational denominator 2 -> 5) ---
src = src.replace(
    "          + (aspirational_pass / 2 * 10)",
    "          + (aspirational_pass / 5 * 10)"
)

# --- patch scoring example (aspirational_pass/2 -> /5) ---
# The examples section references the old denominator implicitly; update
# the example that references "aspirational_pass / 2":
# (no explicit formula repeated in examples, so nothing to change there)

# --- append three new aspirational criteria before the summary table ---
new_criteria = """
---

### C-11 -- Gate-sequenced architecture separates analysis from behavior
- **Weight:** aspirational
- **Category:** behavior
- **Source:** R1 excellence signal -- V-05 Simplified Gates + Embedded Inertia
- **Text:** The skill uses named structural gates that separate analytical
  steps (inventory complete, delta complete, proposals typed) from behavioral
  steps (confirmation, write). C-04 and C-05 violations become architectural:
  skipping Gate 3 produces a malformed gate sequence, not just an omitted
  instruction. Confirmation cannot be implied when it is a named gate with
  a required output artifact.
- **Pass condition:** At least four named gates are present and labeled (e.g.,
  Gate 1: inventory complete, Gate 2: delta complete, Gate 3: confirmation,
  Gate 4: write). Each gate produces a named output artifact or termination
  state. A skill where confirmation and write appear as trailing instructions
  rather than named structural gates fails.

---

### C-12 -- Per-gate inertia enforcement (not single front-load)
- **Weight:** aspirational
- **Category:** correctness
- **Source:** R1 excellence signal -- V-05 Simplified Gates + Embedded Inertia
- **Text:** The inertia prior fires at each analysis gate independently --
  inventory gate, delta gate, and proposal gate each carry their own
  advances-only-if-evidence-beats-NO-CHANGE check. A single front-loaded
  competitor block can be implicitly bypassed in downstream steps; per-gate
  checks cannot. Three enforcement points versus one.
- **Pass condition:** At least three distinct inertia check points are
  present and labeled: one at the inventory/classification level, one at
  the delta-to-proposal transition, and one at proposal selection. Each
  must be phrased as a gate advancement condition, not a general instruction.
  A single front-loaded inertia block with no per-gate restatement fails.

---

### C-13 -- Gate-termination nulls as structural artifacts
- **Weight:** aspirational
- **Category:** format
- **Source:** R1 excellence signal -- V-05 Simplified Gates + Embedded Inertia
- **Text:** Null declarations are produced as gate-termination artifacts
  when a gate does not advance, not as explicit output conventions the model
  must remember to follow. The null is the gate output when no candidates
  pass; it cannot be omitted without skipping the gate itself. This makes
  C-07 compliance a structural consequence rather than an instructed behavior.
- **Pass condition:** Each null declaration is phrased as a gate termination
  outcome, e.g., ADDITIONS gate: inertia holds -- no candidates beat NO
  CHANGE. A null phrased as a general note without tying it to a named gate
  termination fails. A null that would be present even without gates (a
  convention, not a gate artifact) fails.

"""

# Insert before ## Criterion Summary
src = src.replace(
    "## Criterion Summary",
    new_criteria.lstrip() + "## Criterion Summary"
)

# --- patch the criterion summary table: add three new rows before the closing line ---
old_summary_tail = "| C-10 | Conflict audit across NEW artifacts       | aspirational  | coverage    |"
new_summary_tail = (
    "| C-10 | Conflict audit across NEW artifacts       | aspirational  | coverage    |\n"
    "| C-11 | Gate-sequenced architecture (R1 signal)   | aspirational  | behavior    |\n"
    "| C-12 | Per-gate inertia enforcement (R1 signal)  | aspirational  | correctness |\n"
    "| C-13 | Gate-termination nulls (R1 signal)        | aspirational  | format      |"
)
src = src.replace(old_summary_tail, new_summary_tail)

# --- patch scoring examples ---
# Update the "passes golden" example to use new denominator math
old_ex = (
    "**Passes golden (all essential + composite >= 80):**\n"
    "- C-01 thru C-05 all pass (60 pts)\n"
    "- C-06 + C-07 pass, C-08 fails (20 pts)\n"
    "- C-09 passes, C-10 fails (5 pts)\n"
    "- Composite = 60 + 20 + 5 = 85 -- GOLDEN"
)
new_ex = (
    "**Passes golden (all essential + composite >= 80):**\n"
    "- C-01 thru C-05 all pass (60 pts)\n"
    "- C-06 + C-07 pass, C-08 fails (20 pts)\n"
    "- C-09 passes, C-10 thru C-13 fail (2 pts)\n"
    "- Composite = 60 + 20 + 2 = 82 -- GOLDEN"
)
src = src.replace(old_ex, new_ex)

# Add R1 winner mapping at end
src = src.rstrip() + "\n\n**R1 winner V-05 mapped to v2:**\n"
src += "- C-01 thru C-05 pass (60 pts)\n"
src += "- C-06 + C-07 pass, C-08 partial (22-25 pts)\n"
src += "- C-09 partial, C-10/C-11/C-12/C-13 pass (8-9 pts)\n"
src += "- Composite ~= 90+ -- GOLDEN\n"

with open(v2_path, "w") as f:
    f.write(src)

print("written:", v2_path)
print("length:", len(src))
