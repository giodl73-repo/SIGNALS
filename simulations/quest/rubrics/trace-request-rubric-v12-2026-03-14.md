Reading the v11 rubric carefully to extract the three C-34 surface signals, then promoting them to C-34, C-35, C-36 and drafting the complete v12 rubric.

---

# trace-request Rubric — v12 (2026-03-15)

**Scale:** 235 (Essential 60 + Recommended 30 + Aspirational 145)
**Golden threshold:** all 4 essential PASS AND composite >= 80%

---

## Three new criteria from R12 excellence signals

| New criterion | R12 excellence signal | What is testable |
|---|---|---|
| **C-34** Structured VT-N schema input | ES-1 (V-03): The Step 8 Header VT# token list is declared in `VT-N: "exact string"` quoted format (one line per token) with a `TOKEN-COUNT: N` self-validation field, making the reference set machine-parseable via `^VT-[0-9]+: ".*"$` without prose reading | Is the VT# token list declared in `VT-N: "..."` quoted format, one per line? Is a `TOKEN-COUNT: N` field present? Does TOKEN-COUNT match the count of VT-N lines? Can the full reference set be extracted via `^VT-[0-9]+: ".*"$` without reading surrounding prose? |
| **C-35** Row-level verdict token | ES-2 (V-04): Step 8c table carries a `Row-Verdict: PASS/HALT` column per row and a `CHECK RESULT: PASS/FAIL -- N rows, M HALT rows` summary line after the table, externalizing checker output as machine tokens — no reading of Match? values or Step 8b prose required to identify halt events | Is a `Row-Verdict` column present in Step 8c with `PASS` or `HALT` per row? Is a `CHECK RESULT:` summary line present after the table? Can halt events be identified by scanning `Row-Verdict` for `HALT` without reading Match? values or Step 8b prose? |
| **C-36** Full checker contract | ES-3 (V-05): Both checker input (Step 8 Header VT-N schema, parseable via `^VT-[0-9]+: ".*"$` + TOKEN-COUNT) and checker output (Row-Verdict per row + CHECK RESULT summary) are machine-parseable structural tokens within the prompt, such that the complete checker contract — parse input, compare, emit output — requires no prose reading at any step | Are both C-34 (structured input schema) and C-35 (externalized output tokens) simultaneously present? Can the complete checker contract be expressed as: (1) parse `^VT-[0-9]+: ".*"$` from header, (2) scan `Row-Verdict` for `HALT`, (3) read `CHECK RESULT`? Is no prose reading required at any step? Does TOKEN-COUNT self-validate schema completeness without positional parsing? |

**Scale:** 220 → **235** (aspirational tier: 26 → 29 criteria, 130 → 145 pts). Golden threshold stays at >= 80%.

---

## Key design decisions

**C-34 vs C-32:** C-32 tests that a VT# token list is co-located at the Step 8 header boundary making Match? computation self-contained — no structural dependency on Steps 0, 3, or 11. C-34 tests that this list is declared in a machine-parseable `VT-N: "..."` quoted schema format with `TOKEN-COUNT` self-validation, such that the reference set can be fully extracted by regex without reading surrounding prose. VT# list present as prose re-affirmation = C-32 PASS + C-34 FAIL.

**C-35 vs C-31:** C-31 tests that the contradiction halt is a named typed event with machine-greppable `CONTRADICTION SIGNAL: Seq# N` label and required `Scope String Correction` Rem# output. C-35 tests that the halt is additionally externalized as a per-row machine token (`Row-Verdict = HALT`) with a `CHECK RESULT` summary — named halt event present but halt not surfaced as per-row token = C-31 PASS + C-35 FAIL.

**C-36 vs C-33:** C-33 tests that all three pre-conditions (reference set, named halt type, Rem# format) are simultaneously present making the automated-check predicate specifiable. C-36 tests that the full checker contract is machine-expressed — both input schema (VT-N quoted format) and output tokens (Row-Verdict + CHECK RESULT) are structural tokens within the prompt, such that no prose reading is required at any step. Pre-conditions present and predicate specifiable (C-33 PASS) but checker I/O not fully machine-parseable without prose reading = C-33 PASS + C-36 FAIL.

**New dependency edges:**
- C-34 depends on C-32 (VT# token list must be co-located at header boundary as a structural requirement before machine-parseable schema encoding can be tested; C-32 establishes the anchor, C-34 tightens the encoding)
- C-35 depends on C-29 (Step 8c coherence table must exist as structural foundation before a Row-Verdict column extension is meaningful) and C-31 (named halt type must exist for `Row-Verdict = HALT` to function as a typed halt event token rather than an arbitrary label)
- C-36 depends on C-34 AND C-35 (both structured input schema and externalized output tokens must be simultaneously present for the full checker contract to be specifiable from structural tokens alone)

**Signal not promoted — C-37 design surface:** Live automated checker: a runnable tool or schema validator that consumes the Step 8 Header VT-N schema lines, the Step 8c Row-Verdict tokens, and the CHECK RESULT summary and produces binary pass/fail without human judgment. Requires C-36 to produce consistent multi-round evidence that the full checker contract (input schema + output tokens) is stable across variation axes before a tool implementation contract can be reliably frozen.

---

## Three new criteria from R11 excellence signals (carried from v11)

| New criterion | R11 excellence signal | What is testable |
|---|---|---|
| **C-31** Named contradiction halt type | ES-1 (V-03): The contradiction between Step 8b prose and Step 8c Match? is introduced as a **named typed structural event** with a machine-greppable label (`CONTRADICTION SIGNAL: Seq# N`) and requires a typed Rem# output (`Scope String Correction`) before the trace may advance | Is the contradiction event named with a typed label? Is the label machine-greppable (fixed token, no prose variation)? Is a Rem# output required? Is the Rem# type specified as `Scope String Correction`? |
| **C-32** Self-contained Match? computation | ES-2 (V-04): Step 8 header carries a re-affirmation of the VT# token list at the step boundary, making Match? computation self-contained — a checker needs only the Step 8 header and the Step 8c table, with zero dependency on Steps 0, 3, or 11 | Is a VT# token list present at the Step 8 header boundary? Can Match? be fully computed from only the Step 8 header + Step 8c table? Is there no structural dependency on Steps 0, 3, or 11 for Match? computation? |
| **C-33** Automated-check predicate completeness | ES-3 (V-05 only): All three automated-check pre-conditions are simultaneously present — (a) reference set co-located at Step 8 header, (b) named halt type with greppable label, (c) Rem# format requirement — such that the automated-check predicate is fully specifiable without semantic reading of prose or cross-section navigation | Are all three pre-conditions simultaneously present? Can an automated checker operate using only Step 8 header + Step 8c table + halt label pattern? Is the predicate fully specifiable from structural tokens alone? |

---

## Three new criteria from R10 excellence signals (carried from v11)

| Criterion | R10 excellence signal | What is testable |
|---|---|---|
| **C-28** Coherence-spine progression gate | ES-1 (V-03): Step 8b contains a REQUIRED prose confirmation per Gap?=Y boundary, explicitly verifying all three link arms (Step 8a → Step 11 → Step 7/9) before Step 9 may proceed | Is a per-boundary confirmation present at Step 8b? Does it name all three link arms? Is it marked REQUIRED? Does it structurally block advancement to Step 9? |
| **C-29** Scope-string coherence table | ES-2 (V-04): Step 8c contains a required table with columns Step3-Auth / Step8a-Invoked / Step11-Params / Match? for each Gap?=Y boundary, positioned before Step 9 | Is a Step 8c table present? Does it carry all four required columns? Is Match? binary (Y/N) per row? Is it required before Step 9? Are VT# scope strings present in column values? |
| **C-30** Dual-surface contradiction signal | ES-3 (V-05 only): Both Step 8b prose confirmation AND Step 8c Match? table are required; a mismatch (prose says coherent, Match? = N) is detectable from structure alone without semantic reading of prose; VT# scope strings appear consistently across both surfaces | Are both C-28 and C-29 surfaces present and both REQUIRED? Is there a structural rule making prose / Match? divergence self-evidencing? Do VT# scope strings propagate consistently from Step 8b prose to Step 8c column values? |

---

## Full aspirational tier — C-21 through C-36

| # | Criterion | Points | Depends on |
|---|---|---|---|
| C-21 | (prior) | 5 | — |
| C-22 | (prior) | 5 | — |
| C-23 | (prior) | 5 | — |
| C-24 | (prior) | 5 | — |
| C-25 | Scope enumeration table with Gap? column | 5 | — |
| C-26 | Scope-gap Rem# three-way cross-link | 5 | C-25, C-23 |
| C-27 | Vocabulary conformance gate (VT# + D=0 gate) | 5 | C-02 |
| C-28 | Coherence-spine progression gate | 5 | C-26, C-25 |
| C-29 | Scope-string coherence table (Step 8c) | 5 | C-26, C-27 |
| C-30 | Dual-surface contradiction signal | 5 | C-28, C-29 |
| C-31 | Named contradiction halt type | 5 | C-30, C-29 |
| C-32 | Self-contained Match? computation | 5 | C-29, C-27 |
| C-33 | Automated-check predicate completeness | 5 | C-31, C-32 |
| **C-34** | **Structured VT-N schema input** | **5** | C-32 |
| **C-35** | **Row-level verdict token** | **5** | C-29, C-31 |
| **C-36** | **Full checker contract** | **5** | C-34, C-35 |

**Aspirational total:** 29 criteria × 5 pts = **145 pts**

---

## Score bands (unchanged)

---

## Summary

**Scale:** 235 pts (v12 rubric, C-01 through C-36)

### R12 retroactive scores under v12

| Rank | Variation | v11 Score | C-34 | C-35 | C-36 | v12 Score |
|---|---|---|---|---|---|---|
| 1 | V-05 (V-03 + V-04 combined) | 220/220 | PASS | PASS | PASS | 235/235 |
| 2 | V-03 (structured schema header) | 220/220 | PASS | FAIL | FAIL | 225/235 |
| 2 | V-04 (row-level verdict token) | 220/220 | FAIL | PASS | FAIL | 225/235 |
| 4 | V-01 (C-31 advisory) | 210/220 | FAIL | FAIL | FAIL | 210/235 |
| 4 | V-02 (C-32 advisory) | 210/220 | FAIL | FAIL | FAIL | 210/235 |

**Isolation confirmed:** V-03 delta = +C-34 only (C-35 absent — no Row-Verdict column, header schema alone does not satisfy output token requirement). V-04 delta = +C-35 only (C-34 absent — header re-affirmation is prose, not `VT-N: "..."` quoted format; C-32 PASS insufficient for C-34). C-36 conjunction dependency on both C-34 AND C-35 confirmed: neither V-03 nor V-04 alone earns C-36. V-01 C-34/C-35 FAIL cascades from C-31 FAIL (Row-Verdict = HALT requires named typed halt event; typed halt absent removes the semantic anchor). V-02 C-34 FAIL cascades from C-32 FAIL (header not REQUIRED; structured schema format presupposes header boundary is a required structural anchor).

---

### Four new patterns (C-37 design surface)

1. **Structured schema input** (V-03): `VT-N: "..."` quoted lines make the reference set machine-parseable via `^VT-[0-9]+: ".*"$`; `TOKEN-COUNT` self-validates completeness without positional parsing.

2. **Row-level verdict token** (V-04): `Row-Verdict: PASS/HALT` column + `CHECK RESULT:` summary externalize the checker output schema — no reading of Match? values or Step 8b prose needed to identify halt events.

3. **Full checker contract** (V-05): Both input schema (header parse via `^VT-[0-9]+: ".*"$`) and output tokens (`Row-Verdict` + `CHECK RESULT`) are machine-parseable within the prompt structure. No prose reading at any step. V-05 is the strongest C-37 pre-condition expression.

4. **C-34 / C-35 as independent axes** (isolation evidence): Structured schema input and row-level verdict token are orthogonal improvements — each earns exactly one criterion without the other, and only their conjunction earns C-36. This independence means either axis can regress without affecting the other, and rubric scoring cleanly attributes each delta.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Structured VT-N: \"exact string\" quoted schema in Step 8 Header makes token reference set machine-parseable via ^VT-[0-9]+: \".*\"$ -- TOKEN-COUNT: N self-validates completeness; no positional counting or prose reading required", "Row-Verdict: PASS/HALT column externalizes contradiction detection as per-row machine token; CHECK RESULT: PASS/FAIL -- N rows, M HALT rows provides single-line binary output; checker identifies halt events by scanning Row-Verdict for HALT without reading Match? values or Step 8b prose", "V-05 full checker contract: parse VT-N schema lines (input), scan Row-Verdict for HALT (comparison), emit CHECK RESULT (output) -- both checker input schema and output tokens machine-parseable within prompt structure; no prose reading at any step; TOKEN-COUNT self-validates schema block completeness", "C-34 and C-35 are orthogonal axes -- V-03 earns C-34 without C-35, V-04 earns C-35 without C-34, V-05 earns both and thereby earns C-36; independence confirmed by clean +5 deltas with no cross-criterion bleed"]}
```
