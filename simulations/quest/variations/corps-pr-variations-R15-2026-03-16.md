Written to `simulations/quest/golden/corps-pr-variate-R15-2026-03-17.md`.

---

## Variate R15 — corps-pr

**Baseline**: R14 V-04 scores 33/36 against v13 — passes C-42 (two-branch conditional syntax already present), fails C-43 (note lacks "do not use" directive) and C-44 (C-41 declares C-40 at table-column level but "or" path still offered in format rules).

**Three single-axis variations:**

| Var | Axis | C-43 | C-44 | Score |
|-----|------|------|------|-------|
| V-01 | Output format — add "do not use" directive + name both C-38/C-40 to existing note; "or" path still described in format rules | PASS | FAIL | 34/36 |
| V-02 | Lifecycle emphasis — remove "or" path from format rules entirely; no prohibition text | FAIL | PASS | 34/36 |
| V-03 | Phrasing register — move prohibition to `CLOSED PATHS` block in pipeline declaration; format rules unchanged (still have "or" path) | PASS | FAIL | 34/36 |

**Two combinations:**

| Var | Axes | Mechanism | Score |
|-----|------|-----------|-------|
| V-04 | V-01 + V-02 | Prohibition inline in format rules + "or" path eliminated — C-43 names the closed path with "do not use"; C-44 satisfied because the path is gone | 36/36 |
| V-05 | V-02 + V-03 | `CLOSED PATHS` + `Declaration-template consistency` sections added to pipeline declaration + path eliminated from format rules — C-43 and C-44 both auditable from the pipeline block alone | 36/36 |

**Key difference between V-04 and V-05**: V-04 puts the prohibition inline in format rules (reader must read format rules to audit C-43). V-05 elevates the prohibition to the structural declaration (reader can audit both C-43 and C-44 from the pipeline block without reading format rules).
