**R12 complete. Scorecard written.**

---

## Summary

**Scale:** 220 pts (v11 rubric, C-01 through C-33)

| Rank | Variation | Score | C-31 | C-32 | C-33 |
|---|---|---|---|---|---|
| 1 | V-05 (schema + row verdict) | 220/220 | PASS | PASS | PASS |
| 1 | V-04 (row verdict) | 220/220 | PASS | PASS | PASS |
| 1 | V-03 (schema header) | 220/220 | PASS | PASS | PASS |
| 4 | V-01 (C-31 advisory) | 210/220 | FAIL | PASS | FAIL |
| 4 | V-02 (C-32 advisory) | 210/220 | PASS | FAIL | FAIL |

**Isolation confirmed:** V-01 delta = -C-31 -C-33 (C-32 survives). V-02 delta = -C-32 -C-33 (C-31 survives). C-33's conjunction dependency on both validated.

---

**Three new patterns (C-34 design surface):**

1. **Structured schema input** (V-03): `VT-N: "..."` quoted lines make the reference set machine-parseable via `^VT-[0-9]+: ".*"$`; `TOKEN-COUNT` self-validates completeness.

2. **Row-level verdict token** (V-04): `Row-Verdict: PASS/HALT` column + `CHECK RESULT:` summary externalize the checker output schema — no reading of Match? values or Step 8b prose needed.

3. **Full checker contract** (V-05): Both input schema (header parse) and output tokens (Row-Verdict + CHECK RESULT) are machine-parseable within the prompt structure. No prose reading at any step. V-05 is the strongest C-34 pre-condition expression.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Structured VT-N: \"exact string\" quoted format in Step 8 Header makes token reference set machine-parseable without prose reading -- pattern ^VT-[0-9]+: \".*\"$ extracts expected scope strings; TOKEN-COUNT makes schema block self-validating without positional parsing", "Row-Verdict column (PASS/HALT) externalizes contradiction-detection as per-row machine token -- checker scans for HALT without reading Match? values or Step 8b prose; CHECK RESULT summary provides single-line binary output for entire table check", "V-05 full checker contract: parse VT-N schema lines (input), scan Row-Verdict for HALT (comparison), emit CHECK RESULT (output) -- both checker input and output formats machine-parseable within prompt structure; no prose reading at any step"]}
```
and:** Gold

---

### V-02 -- Regression: C-32 Advisory

| Criterion | Result | Evidence |
|---|---|---|
| C-28 | **PASS** | Step 8b REQUIRED progression gate intact; all three link arms named (Step 8a -> Step 11 -> Step 7/9); structurally blocks advancement to Step 9 |
| C-29 | **PASS** | Step 8c table REQUIRED before Step 9; four columns present; Match? binary Y/N; VT# scope strings appear in column values from Step 0 commitment (header advisory but strings still propagate from Step 0 through trace steps) |
| C-30 | **PASS** | Both surfaces REQUIRED; CONTRADICTION HALT block preserved with CONTRADICTION SIGNAL: Seq# N label; prose/table divergence is format-detectable via co-presence of "Coherence confirmed" in Step 8b AND Match? = N; no dependency on header for this criterion |
| C-31 | **PASS** | CONTRADICTION SIGNAL: Seq# N label preserved as named typed halt event; machine-greppable fixed token present; Scope String Correction Rem# type requirement in Step 11 preserved; halt fires when prose asserts coherent AND Match? = N |
| C-32 | **FAIL** | Step 8 Header softened to advisory; REQUIRED label removed; binding commitment statement removed; Match? computation anchor on header removed (Y if byte-identical -- no longer requires matching Step 8 Header VT# token); VT# token list not co-located at Step 8 boundary as structural REQUIRED reference; reviewer cannot verify Match? from header + table alone without returning to Steps 0, 3, or 11 |
| C-33 | **FAIL** | Pre-condition (a) -- reference set co-located at Step 8 header -- absent (C-32 FAIL); C-33 dependency on C-31 AND C-32 not satisfied; two of three pre-conditions present but reference set pre-condition missing |
| Essential C-01--C-04 | **ALL PASS** | Regression axis touches only aspirational tier |

**Composite:** 205 + 5 + 0 + 0 = **210 / 220 = 95.5%**
**All-essential PASS:** Yes | **Band:** Gold

---

### V-03 -- Output Format: Structured Token Schema

| Criterion | Result | Evidence |
|---|---|---|
| C-28 | **PASS** | Step 8b REQUIRED coherence progression gate preserved; names all three link arms; per-boundary confirmation form requires VT# string from Step 8 Header schema |
| C-29 | **PASS** | Step 8c REQUIRED table; four columns present; Match? extended: Y if byte-identical AND each cell value appears verbatim as quoted value in Step 8 Header schema; DISQUALIFIER added for cells not in schema; VT# scope strings in column values; mandatory before Step 9 |
| C-30 | **PASS** | Both surfaces REQUIRED; CONTRADICTION HALT block fires; VT# scope strings propagate from header schema (quoted values) through Step 8b confirmation through Step 8c cells; schema enforces consistency across both surfaces |
| C-31 | **PASS** | CONTRADICTION SIGNAL: Seq# N label preserved with header schema token cited; machine-greppable label intact; Scope String Correction Rem# type requires "correct quoted value from Step 8 Header schema: [string]"; typed halt event fully present with schema-referenced correction record |
| C-32 | **PASS** | Step 8 Header REQUIRED; VT# tokens declared in VT-N: "exact string" quoted format (one per line) + TOKEN-COUNT: N; Match? rule explicitly references header schema; DISQUALIFIER: missing quoted VT-N lines fails C-32; self-contained computation stronger than prose re-affirmation -- checker parses ^VT-[0-9]+: ".*"$ lines, no prose reading required, no dependency on Steps 0, 3, or 11 |
| C-33 | **PASS** | All three pre-conditions simultaneously present: (a) reference set co-located at Step 8 header in machine-parseable VT-N: "..." schema format; (b) named halt type with CONTRADICTION SIGNAL machine-greppable label; (c) Scope String Correction Rem# format requirement; automated-check predicate fully specifiable: parse ^VT-[0-9]+: ".*"$ lines from header, compare each Step 8c cell against extracted set, emit per-row pass/fail -- no prose reading at any step |
| Essential C-01--C-04 | **ALL PASS** | |

**Composite:** 205 + 5 + 5 + 5 = **220 / 220 = 100%**
**All-essential PASS:** Yes | **Band:** Gold

**C-34 surface signal:** Step 8 Header VT-N: "..." schema format provides a defined machine-parseable input interface for a live checker -- TOKEN-COUNT: N makes the schema block self-validating (parser confirms completeness without positional counting).

---

### V-04 -- Output Format: Row-Level Verdict Token

| Criterion | Result | Evidence |
|---|---|---|
| C-28 | **PASS** | Step 8b REQUIRED progression gate preserved from R11 V-05; names all three link arms; blocks Step 9 |
| C-29 | **PASS** | Step 8c REQUIRED table; four columns present plus Row-Verdict column; Match? binary Y/N; VT# scope strings in column values; mandatory before Step 9 |
| C-30 | **PASS** | Both surfaces REQUIRED; CONTRADICTION SIGNAL fires on first Row-Verdict = HALT; prose/table divergence format-detectable; VT# scope strings propagate consistently |
| C-31 | **PASS** | CONTRADICTION SIGNAL fires on Row-Verdict = HALT; named typed label CONTRADICTION SIGNAL: Seq# N present; Scope String Correction Rem# type preserved; Row-Verdict = HALT is itself a machine token that identifies the halt event boundary without reading Match? column |
| C-32 | **PASS** | Step 8 Header scope-token re-affirmation preserved exactly as in R11 V-05; REQUIRED, VT# token list co-located, Match? self-contained; Row-Verdict column further reduces checker dependency: scan Row-Verdict for HALT without reading Match? values or Step 8b prose |
| C-33 | **PASS** | All three pre-conditions simultaneously present; Row-Verdict column + CHECK RESULT summary externalize the automated-check output schema within the prompt; checker contract: (1) parse Step 8 Header VT# list (input), (2) scan Row-Verdict for HALT (comparison), (3) read CHECK RESULT (output) -- no prose reading at any step; predicate specifiable from structural tokens alone |
| Essential C-01--C-04 | **ALL PASS** | |

**Composite:** 205 + 5 + 5 + 5 = **220 / 220 = 100%**
**All-essential PASS:** Yes | **Band:** Gold

**C-34 surface signal:** Row-Verdict (PASS/HALT) column externalizes contradiction-detection as per-row machine token; CHECK RESULT summary CHECK RESULT: PASS/FAIL -- N rows, M HALT rows provides single-line binary output -- checker output schema is specified without semantic reading.

---

### V-05 -- Two-Axis Combination: V-03 + V-04

| Criterion | Result | Evidence |
|---|---|---|
| C-28 | **PASS** | REQUIRED progression gate; all three link arms named; per-boundary confirmation requires VT# string from Step 8 Header schema |
| C-29 | **PASS** | REQUIRED table; Match? references Step 8 Header schema (V-03) AND Row-Verdict column present (V-04); four required columns plus Row-Verdict; mandatory before Step 9 |
| C-30 | **PASS** | Both surfaces REQUIRED; CONTRADICTION SIGNAL fires on first Row-Verdict = HALT; VT# scope strings propagate from quoted schema through Step 8b confirmation through Step 8c cells; strongest dual-surface enforcement |
| C-31 | **PASS** | CONTRADICTION SIGNAL fires on Row-Verdict = HALT; named label present; Step 8 Header schema token cited in CONTRADICTION SIGNAL block; Scope String Correction Rem# type with "correct quoted value from Step 8 Header schema" requirement; named halt type fully present with schema-referenced correction record |
| C-32 | **PASS** | Step 8 Header REQUIRED with VT-N: "..." quoted schema format + TOKEN-COUNT (V-03); Match? computation references schema; both header schema (input) and Row-Verdict (output) make computation self-contained -- strongest structural expression of self-containment across all five variations |
| C-33 | **PASS** | All three pre-conditions simultaneously present; V-05 provides the strongest form: checker input schema (parse ^VT-[0-9]+: ".*"$ from header), checker comparison (scan Row-Verdict for HALT), checker output (emit CHECK RESULT: PASS/FAIL); no prose reading at any step; predicate specifiable from structural tokens alone; TOKEN-COUNT self-validates schema completeness |
| Essential C-01--C-04 | **ALL PASS** | |

**Composite:** 205 + 5 + 5 + 5 = **220 / 220 = 100%**
**All-essential PASS:** Yes | **Band:** Gold

**C-34 surface signal (strongest):** Full checker contract fully specified within prompt structure: input schema (VT-N: "..." lines, TOKEN-COUNT), comparison operation (Row-Verdict scan for HALT), output token (CHECK RESULT). Both input and output formats machine-parseable. A tool implementing this contract requires no semantic reading at any step.

---

## Variation Ranking

| Rank | Variation | Score | % | All-Essential | Band | C-31 | C-32 | C-33 |
|---|---|---|---|---|---|---|---|---|
| 1 | **V-05** (V-03+V-04) | 220/220 | 100% | PASS | Gold | PASS | PASS | PASS |
| 1 | **V-04** (row verdict) | 220/220 | 100% | PASS | Gold | PASS | PASS | PASS |
| 1 | **V-03** (schema header) | 220/220 | 100% | PASS | Gold | PASS | PASS | PASS |
| 4 | **V-01** (C-31 advisory) | 210/220 | 95.5% | PASS | Gold | FAIL | PASS | FAIL |
| 4 | **V-02** (C-32 advisory) | 210/220 | 95.5% | PASS | Gold | PASS | FAIL | FAIL |

**Isolation check confirmed:**
- V-01 vs V-03: delta = 10 pts from C-31 FAIL + C-33 FAIL -- C-31 and C-33 independently load-bearing; C-32 surviving V-01 regression confirms C-31 and C-32 are separable axes
- V-02 vs V-03: delta = 10 pts from C-32 FAIL + C-33 FAIL -- C-32 and C-33 independently load-bearing; C-31 surviving V-02 regression confirms C-31 and C-32 are separable axes
- C-33 dependency on both C-31 AND C-32 structurally validated: neither V-01 nor V-02 can achieve C-33 PASS with one pre-condition missing

---

## Excellence Signals (V-05, top-scoring)

**ES-1 (V-03):** Structured VT-N: "exact string" quoted format in Step 8 Header makes the token reference set **machine-parseable without prose reading** -- a checker extracts expected scope strings by pattern ^VT-[0-9]+: ".*"$; TOKEN-COUNT makes the schema block **self-validating** (parser confirms completeness without positional counting). Match? rule explicitly references the schema, tightening the C-33 automated predicate.

**ES-2 (V-04):** Row-Verdict column (PASS/HALT) **externalizes contradiction-detection as a per-row machine token** -- a checker scans for HALT without reading Match? column values or Step 8b prose. CHECK RESULT summary CHECK RESULT: PASS/FAIL -- N rows, M HALT rows provides a single-line binary output for the entire table. The checker output schema is now specified within the prompt structure.

**ES-3 (V-05 combination):** Full automated checker contract **explicitly specified within prompt structure**: (1) parse VT-N: "..." lines from Step 8 Header (input schema), (2) scan Row-Verdict column for HALT (comparison step), (3) emit CHECK RESULT (output). Both checker input format and checker output format are machine-parseable. No prose reading required at any step. Strongest structural expression of C-33 across all rounds.

---

## C-34 Design Surface (R12 yield)

| Property | Source | Structural form |
|---|---|---|
| Parseable input schema | V-03 | VT-N: "..." lines + TOKEN-COUNT: N in Step 8 Header |
| Self-validating schema completeness | V-03 | TOKEN-COUNT enables parser to verify no lines missed |
| Parseable output verdict (per-row) | V-04 | Row-Verdict: PASS/HALT column in Step 8c table |
| Parseable output verdict (table-level) | V-04 | CHECK RESULT: PASS/FAIL -- N rows, M HALT rows line |
| Full checker contract | V-05 | Input schema + per-row token + table-level token all co-present |

V-05 fully satisfies the C-34 pre-condition: a runnable checker needs only (1) parse header lines matching ^VT-[0-9]+: ".*"$, (2) scan Row-Verdict column for HALT, (3) emit CHECK RESULT: PASS/FAIL. No semantic reading required at any step. TOKEN-COUNT self-validates input schema completeness.

**C-34 candidate:** Live automated checker -- a runnable tool or schema validator that consumes the Step 8 Header VT-N: "..." schema block, scans the Step 8c Row-Verdict column, and emits CHECK RESULT: PASS/FAIL without human judgment. V-03, V-04, V-05 provide consistent multi-round evidence across two separable properties (input format, output token) that the predicate specification is stable.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Structured VT-N: \"exact string\" quoted format in Step 8 Header makes token reference set machine-parseable without prose reading -- pattern ^VT-[0-9]+: \".*\"$ extracts expected scope strings; TOKEN-COUNT makes schema block self-validating without positional parsing", "Row-Verdict column (PASS/HALT) externalizes contradiction-detection as per-row machine token -- checker scans for HALT without reading Match? values or Step 8b prose; CHECK RESULT summary provides single-line binary output for entire table check", "V-05 full checker contract: parse VT-N schema lines (input), scan Row-Verdict for HALT (comparison), emit CHECK RESULT (output) -- both checker input and output formats machine-parseable within prompt structure; no prose reading at any step"]}
```
