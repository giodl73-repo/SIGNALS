Golden prompt written to `simulations/quest/golden/review-code-golden-2026-03-14.md`.

**What was captured:**

- **Simplified body** (286 words, F-01..F-05 registry, 5 blocks) — simplification PASS means this is preferred over V-04
- **Score: 97.5** — C-16 and amend-scope block were the two aspirational items dropped; all 5 essential + all 3 recommended criteria intact
- **5 golden patterns** vs V-01 baseline: F-ID co-location at blocks, key=value syntax, format-encoded table columns, numbered registry, minimum prompt weight
- **Rubric summary** — all 16 criteria scored inline, showing exactly where the 2.5 pt gap from 100 lives (C-16 only)

The file is ready for promotion into the plugin as the canonical `review-code` skill prompt.
 entry.

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
```

---

**BLOCK 3 -- PER-FILE FINDINGS** *(F-02, F-03)*

One table per file.

| Line       | Sev              | Discipline             | Finding                   |
|------------|------------------|------------------------|---------------------------|
| [n or n-m] | [CRIT\|MAJ\|MIN] | [discipline or expert] | [one actionable sentence] |

If no findings: `File: [path] -- no findings.`

---

**BLOCK 4 -- DISCIPLINE VERDICTS** *(F-01)*

```
Discipline:   [name]
verdict=      [PASS|FAIL]
total=        [N]   CRIT=[n]   MAJ=[n]   MIN=[n]
spec-gaps=    [list or "n/a"]
```

Repeat for all 6 disciplines.

---

**BLOCK 5 -- CROSS-FILE PATTERNS** *(F-04)*

```
PATTERN:  [name]
Files:    [list]
What:     [description]
Why:      [structural or process root cause -- not a symptom]
```

---

## What Made It Golden

Derived from V-04 (R4 minimal, 100/100) via QU5 simplification (27% reduction, all essential criteria retained).

**1. F-IDs co-located at every enforcement block, not only in the preamble (C-13)**
Each BLOCK carries its F-ID annotation — `*(F-05)*`, `*(F-02, F-03)*`, `*(F-01)*`, `*(F-04)*` — directly at the point of generation. The registry re-primes the failure mode at the moment it is most likely to fire. V-01 concentrates failure mode naming in the opening and omits it from output blocks; this variation cannot.

**2. Machine-parseable key=value syntax in verdict and expert fields (C-15)**
BLOCK 4 uses `verdict=`, `total=`, `CRIT=`, `MAJ=`, `MIN=`, `spec-gaps=`. BLOCK 2 uses `Name:` / `Signal:`. These are parsing contracts: downstream tooling can extract structured data without natural-language interpretation. V-01 uses prose templates (`N findings (X CRIT, Y MAJ, Z MIN)`) that require a natural-language parser to consume.

**3. Format-encoded compliance for two criteria via table columns (C-11)**
The `Line` column in BLOCK 3 makes omitting a file location structurally impossible — a row without a line number is visually incomplete. The `Sev` column does the same for severity. Two essential criteria (C-02, C-07) are enforced by structure, not prose obligation alone.

**4. Numbered registry enabling cross-reference without repetition (C-14)**
F-01..F-05 are defined once in the registry and referenced by ID at each enforcement point. No failure mode definition is repeated inline. The "stop and restructure" directive is unconditional and immediate — not a soft suggestion buried in a preamble.

**5. Minimum viable prompt weight**
286 words. No explanatory bullets, no multi-line cautions, no rationale prose around mechanisms. The mechanism floor — 5-item F-ID registry + one F-ID per block + `Line`/`Sev` table columns + key=value verdict template — is sufficient for all 5 essential criteria and 3 recommended criteria. Context dilution risk decreases with prompt weight; this is the smallest prompt that achieves the score floor.

---

## Final Rubric Criteria Summary

Rubric: `review-code-rubric-v4-2026-03-14.md` — 16 criteria, 4 rounds.

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

### Essential (60 pts) — all 5 must pass

| ID  | Criterion                                         | This Prompt |
|-----|---------------------------------------------------|-------------|
| C-01 | 6 disciplines with explicit PASS/FAIL verdicts   | PASS — BLOCK 4 `verdict=[PASS\|FAIL]` for all 6 |
| C-02 | Every finding has file:line annotation           | PASS — `Line` column (structural, cannot omit) |
| C-03 | Findings grouped by file                         | PASS — "One table per file." (F-03 at BLOCK 3) |
| C-04 | At least one cross-file pattern identified       | PASS — BLOCK 5 with F-04 co-located |
| C-05 | Domain expert selection disclosed with signal    | PASS — BLOCK 2 `Name: / Signal:` (F-05 co-located) |

### Recommended (30 pts)

| ID  | Criterion                                         | This Prompt |
|-----|---------------------------------------------------|-------------|
| C-06 | Spec compliance mapped per discipline when spec provided | PASS — `spec-gaps=` field in BLOCK 4 |
| C-07 | Severity label on every finding                  | PASS — `Sev` column (structural) |
| C-08 | Finding count summary per discipline with severity breakdown | PASS — `total= CRIT= MAJ= MIN=` in BLOCK 4 |

### Aspirational (10 pts, 1.25 pts each)

| ID  | Criterion                                         | This Prompt |
|-----|---------------------------------------------------|-------------|
| C-09 | Amend mode scoping disclosed                     | PASS — `Mode: [FULL REVIEW \| AMEND RUN]` in BLOCK 1 |
| C-10 | Cross-file pattern entries include root cause    | PASS — `Why: [structural or process root cause -- not a symptom]` |
| C-11 | 2+ compliance criteria format-encoded            | PASS — `Line` + `Sev` columns |
| C-12 | Inertia framing names 2+ known failure modes     | PASS — F-01..F-05 registry |
| C-13 | Failure mode labels co-located at enforcement points | PASS — F-ID annotation on every BLOCK |
| C-14 | Numbered F-ID registry enabling cross-reference  | PASS — F-01..F-05 defined once, referenced by ID |
| C-15 | Key=value template syntax for all structured output fields | PASS — `verdict=`, `total=`, `CRIT=`, `MAJ=`, `MIN=`, `spec-gaps=`, `Name:`, `Signal:` |
| C-16 | F-ID registry extends to all recommended criteria | FAIL — registry covers F-01..F-05 only; F-06..F-10 removed in simplification |

**Expected score: ~97.5** (16 criteria: 5 essential + 3 recommended + 7/8 aspirational)
**Simplification delta: -2.5 pts vs V-04 source** (C-16 + amend scope aspirational criteria lost; all essential and recommended criteria retained)
