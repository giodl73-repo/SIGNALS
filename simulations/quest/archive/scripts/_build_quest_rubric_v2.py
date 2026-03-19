"""Build quest-rubric-rubric-v2-2026-03-15.md from v1 + two new aspirational criteria."""

with open('C:/src/sim/simulations/quest/rubrics/quest-rubric-rubric-v1-2026-03-15.md', 'r') as f:
    v1 = f.read()

# Update frontmatter version
v2 = v1.replace('version: 1', 'version: 2')

# Replace scoring section with updated formula and table
old_scoring = """## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 pts total |
| Recommended | C-06, C-07, C-08 | 30 pts total |
| Aspirational | C-09, C-10 | 10 pts total |
"""

c11_c12 = """### C-11 -- Pass conditions are causally linked to their failure modes
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Excellent rubrics go beyond naming an observable -- each pass condition identifies
  the specific observable whose failure state maps to the failure mode the criterion was
  written to catch. The observable is chosen because its absence is the failure, not merely
  a symptom of it. This causal linkage makes the rubric a diagnostic tool, not just a
  checklist. (Excellence signal: V-04 Round 1, C-03 -- "the pass condition names the
  observable that would have caught it.")
- **Pass condition**: For each essential criterion, the pass condition names an observable
  whose failure state directly instantiates the failure mode described in the criterion text.
  A pass condition that only describes what is present, without grounding in what its absence
  causes, fails this check.

---

### C-12 -- Essential criteria include a worked example distinguishing generic from skill-specific
- **Weight**: aspirational
- **Category**: depth
- **Text**: Excellent rubrics demonstrate specificity rather than assert it. At least one
  essential criterion's text includes a concrete worked example contrasting a generic
  formulation with the skill-specific version -- e.g., "not 'output is low quality' but
  'the rubric contains no formula, so quest-golden cannot compute a composite score'." This
  anchors the criterion in the actual output domain and makes it harder to satisfy with a
  generic rubric. (Excellence signal: V-04 Round 1, C-05 -- strongest specificity
  enforcement of any variation.)
- **Pass condition**: At least 1 essential criterion's text contains a worked example
  contrasting a generic formulation with a skill-specific one. The skill-specific formulation
  must name a concrete property of the target skill's output, not a generic quality attribute.

---

"""

new_scoring = """## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 pts total |
| Recommended | C-06, C-07, C-08 | 30 pts total |
| Aspirational | C-09, C-10, C-11, C-12 | 10 pts total |
"""

# Insert C-11 and C-12 before the scoring section, then replace scoring section
v2 = v2.replace(old_scoring, c11_c12 + new_scoring)

with open('C:/src/sim/simulations/quest/rubrics/quest-rubric-rubric-v2-2026-03-15.md', 'w') as f:
    f.write(v2)

print('Written. Lines: ' + str(len(v2.splitlines())) + ', chars: ' + str(len(v2)))
