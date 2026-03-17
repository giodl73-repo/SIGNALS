## review-code — Round 2 Scoring

**All scores (v2 rubric, 12 criteria):**

| Rank | Variation | Composite | C-11 | C-12 |
|------|-----------|-----------|------|------|
| 1 | V-02 (Failure Mode Registry) | **100** | PASS | PASS |
| 1 | V-04 (Template + Failure Mode Labels) | **100** | PASS | PASS |
| 1 | V-05 (Full Spectrum) | **100** | PASS | PASS |
| 4 | V-01 (Template Saturation) | **97.5** | PASS | FAIL |
| 4 | V-03 (Amend-First Branching) | **97.5** | PASS | FAIL |

All 5 variations: all essential pass, golden threshold met.

**Key finding — C-11 is now a floor:** Every R2 variation inherits a findings table with `Line` and `Sev` columns, which is sufficient to pass C-11. The criterion no longer differentiates. **C-12 is the new discriminant** — the only thing separating 97.5 from 100 is whether the prompt explicitly names failure modes.

**Prediction vs actual:** Predicted range 85–100, actual range 97.5–100. Predictions treated C-11 as "med" for V-02/V-03, not anticipating that inherited table structure would satisfy the criterion. V-02 in particular surprised — a pure inertia framing variation (registry + F-ID labels) scores 100 without template saturation as its axis.

**New patterns:**
1. C-11 is a floor in R2 — any prompt with a findings table clears it; C-12 is the ceiling criterion
2. Per-section F-ID labels create local accountability — the failure mode reminder fires at the exact point of regression, stronger than preamble-only priming
3. Full failure mode registry (10 items) achieves C-12 without restructuring format — inertia framing alone reaches 100

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-11 is now a floor — any variation with a findings table (Line + Sev columns) passes; C-12 is the sole discriminant between 97.5 and 100 in R2", "per-section failure mode labels (local accountability) outperform preamble-only naming — the model is reminded at the exact point of regression, not just at the start", "full failure mode registry (10 items + F-IDs) achieves C-12 without template saturation — inertia framing alone reaches 100 when the registry is complete"]}
```
 (PASS/FAIL field) + C-08 (total/CRIT/MAJ/MIN fields) — four criteria format-encoded |
| C-12 | **FAIL** | No failure modes named; V-01 relies entirely on structural enforcement; "a row without either field is structurally invalid" describes invalidity but does not name a failure mode pattern in the rubric's sense |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 3/4 → 7.5
**Composite: 97.5**

---

### V-02 — Inertia Framing: Full Failure Mode Registry

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Step 4 verdict template `[PASS\|FAIL] N findings (X CRIT, Y MAJ, Z MIN)` per discipline; "omitting explicit PASS/FAIL per discipline produces F-01" — F-01 named and section-labeled |
| C-02 | PASS | Step 3 table `Line` column; "a row without a `Line` value produces F-02" — F-ID label at exact point of regression |
| C-03 | PASS | Step 3 — per-file tables; "organizing by discipline instead of by file produces F-03" — named failure mode at point of enforcement |
| C-04 | PASS | Step 5 — Cross-File Patterns; "emitting per-file findings with no synthesis pass produces F-04" |
| C-05 | PASS | Step 2 — EXPERT DISCLOSURE block; "applying domain expertise without this disclosure produces F-05" |
| C-06 | PASS | Step 4 — "if a spec was provided, append `Spec checked: [sections]. Gaps: [list or 'none']`... omitting spec references when a spec exists produces F-10" |
| C-07 | PASS | Step 3 `Sev` column; "a row without a `Sev` value produces F-06" |
| C-08 | PASS | Step 4 verdict template `N findings (X CRIT, Y MAJ, Z MIN)`; "omitting finding counts produces F-07" |
| C-09 | PASS | Step 6 — AMEND SCOPE block with Changed files, Disciplines re-run (trigger reasons), Disciplines skipped (safety justifications); "omitting this block on an amend run produces F-08" — all three C-09 elements present |
| C-10 | PASS | Step 5 pattern block `Why:` field; "omitting the `Why:` field produces F-09" |
| C-11 | PASS | Step 3 table encodes C-02 (Line col) + C-07 (Sev col); Step 4 verdict template encodes C-01 (`[PASS\|FAIL]`) + C-08 (`N findings...`) as named fields |
| C-12 | PASS | 10-item FAILURE MODE REGISTRY opens the prompt with F-01 through F-10 named and defined; "if you find yourself about to produce output matching any of the above failure modes, stop and restructure"; per-section F-ID labels throughout |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 4/4 → 10
**Composite: 100**

---

### V-03 — Lifecycle Emphasis: Amend-First Branching

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Step 4 verdict template `[PASS\|FAIL] -- N findings (X CRIT, Y MAJ, Z MIN)` per discipline |
| C-02 | PASS | Step 3 table `Line` column; "`Line` must be an exact number or range. No function names without a line number." |
| C-03 | PASS | Step 3 — per-file tables with `path/to/file.ext` header; one table per file |
| C-04 | PASS | Step 5 — Cross-File Patterns with PATTERN block including Name/Files/What/Why |
| C-05 | PASS | Step 2 — EXPERT DISCLOSURE block; "expert selection without disclosure is the primary failure mode for this step" |
| C-06 | PASS | Step 4 — "if a spec was provided, append `Spec gaps: [list or 'none']` to each discipline line" |
| C-07 | PASS | Step 3 `Sev` column; "`Sev` must be `CRIT`, `MAJ`, or `MIN`" |
| C-08 | PASS | Step 4 verdict template `N findings (X CRIT, Y MAJ, Z MIN)` per discipline |
| C-09 | PASS | Amend scope block emitted FIRST — "before expert disclosure, before any finding" — with Changed files, Disciplines re-run (trigger), Disciplines skipped (safety); "amend scope is disclosed before findings, not after"; all three C-09 elements, structurally ordered |
| C-10 | PASS | Step 5 `Why:` field; "a `Why:` field stating a symptom instead of a cause is structurally incomplete" |
| C-11 | PASS | Step 3 table encodes C-02 (Line col) + C-07 (Sev col); Step 4 template encodes C-01 (`[PASS\|FAIL]`) + C-08 (`N findings...`) |
| C-12 | **FAIL** | One failure mode named: "expert selection without disclosure is the primary failure mode for this step." No second failure mode explicitly named. "`Line` must be an exact number or range" is a prohibition, not a named failure mode pattern. Rubric requires at least two. |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 3/4 → 7.5
**Composite: 97.5**

---

### V-04 — Output Format + Inertia Framing: Template Blocks + Failure Mode Labels

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Block 4 template `[PASS\|FAIL] total=[N]...` per discipline; opening names "Verdicts absent" as first failure mode; section labeled "*(Prevents: verdicts absent)*"; "emitting no PASS/FAIL per discipline is the 'verdicts absent' failure mode" |
| C-02 | PASS | Block 3 table `Line` column; "a row missing either is structurally invalid"; section labeled "*(Prevents: annotations incomplete)*" |
| C-03 | PASS | Block 3 — per-file tables with `**File: [path]**` header; one block per file |
| C-04 | PASS | Block 5 — CROSS-FILE PATTERNS required block; "emitting per-file findings with no synthesis block is the 'synthesis absent' failure mode"; section labeled "*(Prevents: synthesis absent)*" |
| C-05 | PASS | Block 2 — EXPERT DISCLOSURE with Name + Signal fields; "emitting domain-specific advice without filling in this block is the 'expert selection silent' failure mode"; section labeled "*(Prevents: expert selection silent)*" |
| C-06 | PASS | Block 4 verdict row includes `spec-gaps=[list or "n/a"]`; "The `spec-gaps` field is omitted only if no spec was provided" |
| C-07 | PASS | Block 3 `Sev` column with CRIT/MAJ/MIN; structurally co-required with Line |
| C-08 | PASS | Block 4 verdict template `total=[N] CRIT=[n] MAJ=[n] MIN=[n]`; named fields per discipline |
| C-09 | PASS | Block 6 — Amend Scope fill-in block with Changed files, Disciplines re-run (trigger reasons), Disciplines skipped (safety justifications); all three C-09 elements present |
| C-10 | PASS | Block 5 pattern template `Why:` field; "a `Why:` entry stating a symptom instead of a cause is structurally incomplete" |
| C-11 | PASS | Block 3 table encodes C-02 + C-07; Block 4 template encodes C-01 + C-08; structural encoding and section-level failure mode labels present — dual enforcement |
| C-12 | PASS | Opening paragraph names 4 failure modes: "Verdicts absent," "Annotations incomplete," "Synthesis absent," "Expert selection silent"; per-section "(Prevents: ...)" labels throughout; framing names the failure mode before each output block fires |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 4/4 → 10
**Composite: 100**

---

### V-05 — All Axes: Full Spectrum

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Step 4 verdict template `[PASS\|FAIL] total=[N] CRIT=[n] MAJ=[n] MIN=[n]`; "named fields make omission visible (failure mode 1)" |
| C-02 | PASS | Step 3 `Line` column; "function names without line context produce failure mode 2"; structural column makes omission visible |
| C-03 | PASS | Step 3 — per-file tables; architecture discipline runs first within each file (architecture-first sequencing reinforces per-file structure) |
| C-04 | PASS | Step 5 — "Cross-File Patterns (required phase — not an appendix)"; "this is the other thing a flat review omits (failure mode 3)"; mandatory `Why:` field |
| C-05 | PASS | Step 2 — EXPERT DISCLOSURE block; "emitting domain-specific findings without filling in this block is failure mode 4 (silent expert selection)" |
| C-06 | PASS | Step 4 verdict template includes `spec-gaps=[list or "n/a"]` field |
| C-07 | PASS | Step 3 `Sev` column; "the column makes omission structurally visible" |
| C-08 | PASS | Step 4 verdict template `total=[N] CRIT=[n] MAJ=[n] MIN=[n]` |
| C-09 | PASS | Amend-first branching: "emit this block first — before expert disclosure, before any finding"; AMEND SCOPE block with all three required elements; "amend scope disclosed before findings prevents failure mode 5" |
| C-10 | PASS | Step 5 `Why:` field; "a `Why:` entry stating a symptom instead of a cause is structurally incomplete"; "give the author one root to fix, not a list of symptoms to chase across files" |
| C-11 | PASS | Step 3 table encodes C-02 (Line col) + C-07 (Sev col); Step 4 template encodes C-01 (PASS/FAIL) + C-08 (total/CRIT/MAJ/MIN) |
| C-12 | PASS | Opening paragraph names 5 failure modes: "No explicit discipline verdicts," "Findings without line numbers," "No cross-file synthesis," "Silent expert selection," "Amend scope invisible"; per-section failure mode references throughout; "the format enforces compliance structurally — not through instruction alone" |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 4/4 → 10
**Composite: 100**

---

### Rankings

| Rank | Variation | Composite | All Essential | C-11 | C-12 |
|------|-----------|-----------|---------------|------|------|
| 1 | V-02 (Failure Mode Registry) | **100** | YES | PASS | PASS |
| 1 | V-04 (Template Blocks + Failure Mode Labels) | **100** | YES | PASS | PASS |
| 1 | V-05 (Full Spectrum) | **100** | YES | PASS | PASS |
| 4 | V-01 (Template Saturation) | **97.5** | YES | PASS | FAIL |
| 4 | V-03 (Amend-First Branching) | **97.5** | YES | PASS | FAIL |

---

### Key Finding: C-11 Is Now a Floor, C-12 Is the Ceiling

All five R2 variations pass C-11. Any variation carrying a findings table (Line + Sev columns) clears the "at least two criteria format-encoded" bar — and all R2 variations have such a table. The new discriminant is C-12: the two variations that fail (V-01 and V-03) do not name failure modes; the three that pass do.

Prediction vs actual spread: predicted 85–100, actual 97.5–100. Predictions underestimated how robustly inherited table structure satisfies C-11. The predictions expected C-11=med for V-02 and V-03 because they are not "template saturation" variations — but the table they carry from R1 is sufficient.

---

### Excellence Signals

**Signal 1 — Per-section F-ID labels create local accountability (V-02)**
Labeling each output section with the failure mode it prevents ("a row without a `Line` value produces F-02") reminds the model of the specific failure mode at the exact point of regression — not just in a preamble it may deprioritize under output pressure. This is stronger than registry-only priming because the reminder is local.

**Signal 2 — Dual enforcement provides independent defense (V-04, V-05)**
Structural templates prevent omission at the format level; failure mode naming resists behavioral regression. Either mechanism can catch what the other misses. V-01 has structure without priming (C-12 gap); V-03 has single failure mode without scope (C-12 gap); V-04/V-05 eliminate both gaps simultaneously. Independence matters: output pressure may degrade one mechanism while the other holds.

**Signal 3 — Amend-first ordering converts C-09 from conditional to structurally required (V-03, V-05)**
Emitting the amend scope block FIRST — "before expert disclosure, before any finding" — makes scope disclosure a planned output that gates all subsequent work. The ordering change is mechanical: the model cannot produce findings before declaring scope.

**Signal 4 — Full failure mode registry (10 items) achieves C-12 without template saturation (V-02)**
V-02 reaches 100 on inertia framing alone, without V-01's template saturation. The 10-item registry with per-section F-ID labels is sufficient for C-12 — and the inherited table structure is sufficient for C-11. This confirms that C-12 can be targeted directly without restructuring the entire prompt format.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-11 is now a floor — any variation with a findings table (Line + Sev columns) passes; C-12 is the sole discriminant between 97.5 and 100 in R2", "per-section failure mode labels (local accountability) outperform preamble-only naming — the model is reminded at the exact point of regression, not just at the start", "full failure mode registry (10 items + F-IDs) achieves C-12 without template saturation — inertia framing alone reaches 100 when the registry is complete"]}
```
