Written to `simulations/quest/rubrics/program-plan-rubric-v5-2026-03-16.md`.

---

## Three new criteria added from R4 excellence signals

**C-19 — Cross-Tier Error Coverage**
Error artifacts (BAD YAML, criterion tags, or correction table) cover errors from BOTH essential criteria (C-01/C-04) AND at least one recommended criterion (C-05/C-07). Essential-only error coverage leaves wrong shapes for recommended criteria invisible at authoring time. R4 source: V-01's BAD block tagged `# WRONG C-05` and `# WRONG C-06` alongside essential-tier tags; V-03's correction table included 2 C-06 pairs. Pass: at least one error artifact has an entry targeting C-05, C-06, or C-07. No partial.

**C-20 — Per-Zone Dependency Constraint Reminder**
Every dependency-bearing arc zone carries an inline prerequisite statement at the skill-list authoring position: `"review:* requires draft:spec artifact from prior stage"`. C-05 states the ordering rule once; C-20 embeds it per-zone so dependency violations feel wrong locally. R4 source: V-02 placed `review:* requires draft:spec` inline at the Design zone skill section. Pass: all dependency-bearing zones; partial: >= half.

**C-21 — Correction Table Scaffold Integration**
YAML template fields carry `# check correction table` (or equivalent) inline at every field type covered by the table — skill lists, gate strings, stage names. C-18 requires the table to exist; C-21 requires the template to route to it at each decision point, ensuring active consultation during generation rather than a one-time read before generation. R4 source: V-03 embedded `# check correction table` at skill, gate, and stage-name placeholders throughout the template. Pass: bridges present at all field types the table covers; partial: some but not all.

**Scoring change:** Aspirational tier 11 → 14 criteria, 55 → 70 pts. Total max is now **160**. Golden threshold (>= 80) unchanged.
