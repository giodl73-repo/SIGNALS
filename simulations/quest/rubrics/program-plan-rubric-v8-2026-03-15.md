Written to `simulations/quest/rubrics/program-plan-rubric-v8-2026-03-16.md`.

---

## Three new criteria from R7 excellence signals

**C-28 — Structural Gate Target Field Co-Location**
When C-24 structural gate-contrast fields exist, the actual authoring-target `gate:` field appears as a named sibling YAML key alongside `gate_fail:` / `gate_pass:` at each zone — separating pedagogical fields from the production output slot at the schema level. Without it, a model cannot tell from structure alone which field to fill. C-24 requires the contrast fields; C-28 requires the production target to co-locate as a third key, converting a two-field contrast pair into an unambiguous three-field teaching unit. R7 source: V-02 and V-03 both used `gate_fail:/gate_pass:/gate:` as actual YAML sibling keys at all 5 non-echo zones — first variates to make the output slot structurally explicit alongside the contrast pair.

**C-29 — Correction Table Recommended-Tier Pairs**
The correction table (C-18) includes at least one wrong-to-correct pair for each of C-05, C-06, and C-07 individually. C-22 requires error artifacts collectively to cover all three recommended criteria; C-29 requires the correction table specifically to carry that coverage, so the pre-generation lookup tool covers quality failures as well as structural ones. R7 source: V-02's 13-row correction table included rows for C-05 (dep order), C-06 (namespace-label-to-intent-label stage names), and C-07 (executor-framing-to-plan-identity).

**C-30 — Dep-Reminder and Correction-Bridge Independence**
At dependency-bearing zone `skills:` lines, a dep constraint reminder (`# requires: <artifact>`) and a correction-table navigational bridge (`# check correction table`) are each present independently — neither substitutes for the other. The two serve orthogonal purposes: the reminder enforces prerequisite ordering; the bridge enables skill-name and gate-value lookup. C-21 and C-23 are both prerequisites. R7 source: V-02's Design zone skills line carried only `# check correction table: skill names` with no dep reminder, earning C-20/C-23 PARTIAL; V-03 carried both annotations independently at all 4 dep zones.

**Scoring change:** Aspirational 20 → 23 criteria, 100 → 115 pts. Total max: **205 pts.** Golden threshold (>= 80) unchanged.
