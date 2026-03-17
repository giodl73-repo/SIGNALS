Written to `simulations/quest/golden/program-plan-variate-R12-2026-03-16.md`.

---

# program-plan — R12 Variate Prompt Bodies (V-01 through V-05)

**Rubric**: v12 (2026-03-16) · **255 pts** · golden threshold 235

---

## R12-2026-03-15 Retrospective (Against New Rubric)

All five prior R12 variants scored 240/240 on the old rubric. Under the new 255-pt rubric, all five fail the three new criteria:

| Criterion | Gap in prior R12 |
|-----------|-----------------|
| **C-38** | All use neutral `# BAD PLAN` headers — passes C-36 (no false restriction) but no affirmative claim of coverage scope |
| **C-39** | C-03 violations tagged at gate or name fields, never at the `skills:` entry line itself |
| **C-40** | C-34 + C-29 both present in V-04/V-05 but the conjunction was not a named criterion and was not explicitly required |

---

## New Canonical Language

**C-38** (affirmative header — closes neutral-silence failure mode):
- PASS: `# BAD PLAN -- all 7 criteria (C-01 through C-07) indexed below`
- PASS: `# BAD PLAN -- essential and recommended violations (C-01 through C-07), all field types annotated`
- FAIL: `# BAD PLAN` alone — scope ambiguous

**C-39** (skills-field co-location — completes three-field pattern):
- `gate_fail:` → `# WRONG C-04` at that line (C-26)
- `name:` → `# WRONG C-06` at that line (C-37)
- `skills:` → `# WRONG C-03` at that line **(C-39 — new)**
- PASS: `- gather-requirements  # WRONG C-03: invented skill name, not in Signal catalog`

**C-40** (conjunction — C-34 template-zone + C-29 lookup-zone):
- C-34: every `gate_fail:` field has `# WRONG C-04` + `Why:` co-located at the field
- C-29: correction table contains C-05, C-06, and C-07 wrong-to-correct pairs
- Neither substitutes: different teaching moments (mid-authoring vs pre-authoring)

---

## Variation Axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | C-38 — Affirmative-Header Banner | Header names all 7 by number; compact formal register. Model primed to look for exactly 7 tags before scanning. |
| **V-02** | C-39 — THREE-FIELD CO-LOCATION RULE as named principle | Declaring the three-field pattern explicitly makes C-39 feel like completion of a rule, not an isolated req. |
| **V-03** | C-40 — DUAL TEACHING MOMENT discovery | Tutorial voice frames C-34 (mid-authoring) and C-29 (pre-authoring) as functionally distinct; the conjunction is motivated. |
| **V-04** | C-38 + C-39 — Failure-Taxonomy Anatomy | Inertia-first opens by naming "silent-header gap" and "untethered-skills-tag gap" as failure modes; protocol provides counter-moves. |
| **V-05** | All three — Complete Integration (Full Reference) | Maximal formulation: SKILLS-FIELD ANNOTATION RULE + DUAL TEACHING CHANNELS + affirmative header naming both criterion set and field coverage. |

---

## Design Differentiators per Variation

**V-01**: BAD PLAN header leads with `-- all 7 criteria (C-01 through C-07) indexed below`. The claim is the headline. Register: compact formal/reference, table-first preamble.

**V-02**: `THREE-FIELD CO-LOCATION RULE` declared as a named table before the BAD PLAN, listing all three field types (gate_fail/name/skills). BAD PLAN header: `"essential and recommended violations (C-01 through C-07), three-field co-location complete"`. Register: formal/structured with named rules.

**V-03**: Second-person tutorial throughout. DUAL TEACHING MOMENT subsection named before the correction table. BAD PLAN header: `"all 7 criteria (C-01 through C-07) -- check your work against each tag below"`. Gate_fail compound annotations framed as "your mid-authoring reference." Register: discovery/conversational.

**V-04**: Three named failure modes in opening anatomy — Failure 1 (catalog-first), Failure 2 (silent-header gap), Failure 3 (untethered-skills-tag gap). BAD PLAN header carries `"SILENT-HEADER COUNTER-MOVE"` label; skills entries carry `"(Failure 3 counter-move: tag at field)"` parenthetical. Register: inertia-first + analytical.

**V-05**: Dedicated `SKILLS-FIELD ANNOTATION RULE` section (a table of three field types), dedicated `DUAL TEACHING CHANNELS` section (explains temporal distinction between C-34 and C-29), and the richest BAD PLAN header: `"essential and recommended violations (C-01 through C-07), all field types annotated (gate_fail:/name:/skills:)"`. Step 10 checklist extends through C-40 with full pass conditions inline. Register: comprehensive reference.

---

All five complete prompt bodies are in the file. Each satisfies C-01 through C-40 (255 pts target). The three new criteria are achieved via distinct mechanisms across the five variations, enabling score differentiation to identify which formulation is most robust under v12.
