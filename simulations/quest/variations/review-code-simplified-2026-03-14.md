---

## QU5 Simplification Report

**Source**: V-04 from R4 (100/100 golden prompt)
**Output**: `simulations/quest/variations/review-code-simplified-2026-03-14.md`

### What was removed (12 items, zero essential criteria lost)

| Cut | Words saved | Reason |
|-----|-------------|--------|
| F-06 through F-10 from registry | ~46 | Each serves only recommended or aspirational criteria; their template fields (Sev column, total/CRIT/MAJ/MIN, spec-gaps, Why: field) remain in the output blocks and continue enforcing those criteria structurally |
| BLOCK 6 -- AMEND SCOPE | ~34 | Aspirational amend-scope criterion only; no C-01..C-05 dependency |
| `Output order: 1 -> 2 -> 3 -> 4 -> 5 -> 6 (if amend).` | ~12 | Fully implied by numbered sequential blocks |
| Orphan F-ID tags (`, F-06`, `, F-06, F-07, F-10`, `, F-09`) | ~6 | Dead references after registry trim |
| `sorted by line` | 3 | No essential criterion requires row ordering |
| `spec-gaps omitted only if no spec provided.` | ~9 | Guidance for recommended C-06 only; the `"n/a"` template value already signals this |

**Total removed: ~110 words**

### Essential criteria: all 5 pass YES

C-01 (verdicts) — BLOCK 4 template with 6 named disciplines + `[PASS|FAIL]`
C-02 (file:line) — BLOCK 3 `Line` column (required field, structural)
C-03 (file grouping) — BLOCK 3: "One table per file."
C-04 (cross-file pattern) — BLOCK 5 PATTERN/Files/What/Why template
C-05 (expert disclosure) — BLOCK 2 `Name: [expert] Signal: [exact code signal]`

### Score impact

The template fields for recommended criteria (Sev column, total/CRIT/MAJ/MIN, spec-gaps) survive intact — only their registry re-priming entries are gone. Loss is confined to two aspirational criteria: C-16 (registry doesn't extend to recommended F-IDs) and the amend-scope block. Expected: **~97.5 vs 100**.

```json
{"simplified_word_count": 286, "original_word_count": 394, "all_essential_still_pass": true}
```
ross-file pattern | BLOCK 5 PATTERN template with Files/What/Why | YES |
| C-05: Expert selection disclosed with signal | BLOCK 2 Name: [expert] Signal: [exact code signal] | YES |

### What is lost vs V-04

- C-16 (aspirational): F-06..F-10 removed from registry -- registry no longer extends to recommended criteria. -1.25 pts
- Amend scope (aspirational): BLOCK 6 removed. -1.25 pts
- Expected score: ~97.5 vs 100. All essential criteria and all recommended template fields intact.

---

## Simplified Prompt

You are running a multi-discipline code review. Produce the blocks below in order.

```
FAILURE MODE REGISTRY
---------------------
F-01  Verdicts absent          -- no explicit PASS/FAIL per discipline
F-02  Line numbers omitted     -- finding references function/class without line number
F-03  File grouping absent     -- findings not grouped per file
F-04  Synthesis missing        -- per-file findings done; no cross-file pattern pass
F-05  Expert selection silent  -- domain advice without naming expert or trigger signal
```

Stop and restructure if output matches any entry.

---

**BLOCK 1 -- FILE INVENTORY**

```
Input type:  [full files | PR diff | diff range]
Mode:        [FULL REVIEW | AMEND RUN]
Files:       [list all files in scope, one per line]
```

---

**BLOCK 2 -- EXPERT DISCLOSURE** *(F-05)*

```
Stock:  Correctness | Security | Performance | Architecture | Style | Testability
Added:
  Name: [expert]   Signal: [exact code signal]
  (or) none -- no framework signals detected
```

---

**BLOCK 3 -- PER-FILE FINDINGS** *(F-02, F-03)*

One table per file. All disciplines in the same table.

**`[path/to/file.ext]`**

| Line | Sev              | Discipline             | Finding               |
|------|------------------|------------------------|-----------------------|
| [n]  | [CRIT\|MAJ\|MIN] | [discipline or expert] | [actionable sentence] |

No findings: `[path] -- no findings.`

---

**BLOCK 4 -- DISCIPLINE VERDICTS** *(F-01)*

```
Correctness:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Security:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Performance:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Architecture: [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Style:        [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
Testability:  [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
[Expert]:     [PASS|FAIL]  total=[N]  CRIT=[n]  MAJ=[n]  MIN=[n]  spec-gaps=[list or "n/a"]
```

PASS = zero CRIT or MAJ.

---

**BLOCK 5 -- CROSS-FILE PATTERNS** *(F-04)*

```
PATTERN: [name]
Files:   [file1] | [file2]
What:    [repeated issue or structural element]
Why:     [structural or process root cause -- not a symptom]
```

No patterns: `Cross-file patterns: none -- [justification].`
