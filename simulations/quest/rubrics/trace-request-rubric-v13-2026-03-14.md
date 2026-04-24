Reading the v12 rubric and R13 scorecard to identify the one new excellence signal (V-03 CHECKER ALGORITHM block → C-37), then drafting the complete v13 rubric.

---

# trace-request Rubric — v13 (2026-03-15)

**Scale:** 240 (Essential 60 + Recommended 30 + Aspirational 150)
**Golden threshold:** all 4 essential PASS AND composite >= 80%

---

## One new criterion from R13 excellence signal

| New criterion | R13 excellence signal | What is testable |
|---|---|---|
| **C-37** Checker algorithm declaration | ES-1 (V-03): The Step 8 Header carries a CHECKER ALGORITHM block immediately after TOKEN-COUNT, declaring MATCH-RULE, HALT-RULE, and OUTPUT-RULE as formal machine-greppable pseudocode tokens — the comparison predicate is machine-readable as a structural property of the header without semantic prose parsing; the algorithm declaration is independent of schema tokens and does not require reading VT-N lines to interpret the logic | Is a CHECKER ALGORITHM block present in the Step 8 Header? Does it appear immediately after TOKEN-COUNT (within the same Step 8 header section)? Does it declare MATCH-RULE, HALT-RULE, and OUTPUT-RULE as named machine-greppable tokens? Is the algorithm declaration structurally independent of VT-N schema tokens (no positional or semantic dependency on VT-N lines to interpret predicate logic)? Is algorithm logic parseable via fixed-token grep without semantic prose reading? |

**Scale:** 235 → **240** (aspirational tier: 29 → 30 criteria, 145 → 150 pts). Golden threshold stays at >= 80%.

---

## Key design decisions

**C-37 vs C-36:** C-36 tests that both checker input (VT-N quoted schema) and checker output (Row-Verdict + CHECK RESULT) are machine-parseable structural tokens within the prompt, such that the complete checker contract — parse input, compare, emit output — requires no prose reading at any step. C-37 tests that the checker algorithm itself — the comparison predicate (MATCH-RULE), the halt condition (HALT-RULE), and the output emission rule (OUTPUT-RULE) — is additionally declared as machine-greppable tokens in the Step 8 Header, such that the logic governing how the contract is executed is also readable from structure alone without semantic prose parsing. Full checker contract present (C-36 PASS) but algorithm declared as prose description rather than named machine-greppable tokens = C-36 PASS + C-37 FAIL.

**New dependency edge:**
- C-37 depends on C-36 (both machine-parseable input schema and externalized output tokens must be simultaneously established as the full checker contract before requiring the algorithm declaration that operates on them to also be a structural token — C-36 establishes the I/O contract, C-37 tightens the algorithm encoding)

**Signal not promoted — C-38 design surface:** Live automated checker: a runnable tool or schema validator that (1) parses the Step 8 Header VT-N schema via `^VT-[0-9]+: ".*"$` and CHECKER ALGORITHM block MATCH-RULE/HALT-RULE/OUTPUT-RULE tokens, (2) executes the declared algorithm against Step 8c data, (3) emits Row-Verdict per row and CHECK RESULT summary — producing binary pass/fail without human judgment at any step. Requires C-37 to produce consistent multi-round evidence that the algorithm declaration is stable across variation axes before a tool implementation contract can be reliably frozen.

---

## Three new criteria from R12 excellence signals (carried from v12)

| New criterion | R12 excellence signal | What is testable |
|---|---|---|
| **C-34** Structured VT-N schema input | ES-1 (V-03): The Step 8 Header VT# token list is declared in `VT-N: "exact string"` quoted format (one line per token) with a `TOKEN-COUNT: N` self-validation field, making the reference set machine-parseable via `^VT-[0-9]+: ".*"$` without prose reading | Is the VT# token list declared in `VT-N: "..."` quoted format, one per line? Is a `TOKEN-COUNT: N` field present? Does TOKEN-COUNT match the count of VT-N lines? Can the full reference set be extracted via `^VT-[0-9]+: ".*"$` without reading surrounding prose? |
| **C-35** Row-level verdict token | ES-2 (V-04): Step 8c table carries a `Row-Verdict: PASS/HALT` column per row and a `CHECK RESULT: PASS/FAIL -- N rows, M HALT rows` summary line after the table, externalizing checker output as machine tokens — no reading of Match? values or Step 8b prose required to identify halt events | Is a `Row-Verdict` column present in Step 8c with `PASS` or `HALT` per row? Is a `CHECK RESULT:` summary line present after the table? Can halt events be identified by scanning `Row-Verdict` for `HALT` without reading Match? values or Step 8b prose? |
| **C-36** Full checker contract | ES-3 (V-05 only): Both checker input (Step 8 Header VT-N schema, parseable via `^VT-[0-9]+: ".*"$` + TOKEN-COUNT) and checker output (Row-Verdict per row + CHECK RESULT summary) are machine-parseable structural tokens within the prompt, such that the complete checker contract — parse input, compare, emit output — requires no prose reading at any step | Are both C-34 (structured input schema) and C-35 (externalized output tokens) simultaneously present? Can the complete checker contract be expressed as: (1) parse `^VT-[0-9]+: ".*"$` from header, (2) scan `Row-Verdict` for `HALT`, (3) read `CHECK RESULT`? Is no prose reading required at any step? Does TOKEN-COUNT self-validate schema completeness without positional parsing? |

---

## Key design decisions (R12, carried from v12)

**C-34 vs C-32:** C-32 tests that a VT# token list is co-located at the Step 8 header boundary making Match? computation self-contained — no structural dependency on Steps 0, 3, or 11. C-34 tests that this list is declared in a machine-parseable `VT-N: "..."` quoted schema format with `TOKEN-COUNT` self-validation, such that the reference set can be fully extracted by regex without reading surrounding prose. VT# list present as prose re-affirmation = C-32 PASS + C-34 FAIL.

**C-35 vs C-31:** C-31 tests that the contradiction halt is a named typed event with machine-greppable `CONTRADICTION SIGNAL: Seq# N` label and required `Scope String Correction` Rem# output. C-35 tests that the halt is additionally externalized as a per-row machine token (`Row-Verdict = HALT`) with a `CHECK RESULT` summary — named halt event present but halt not surfaced as per-row token = C-31 PASS + C-35 FAIL.

**C-36 vs C-33:** C-33 tests that all three pre-conditions (reference set, named halt type, Rem# format) are simultaneously present making the automated-check predicate specifiable. C-36 tests that the full checker contract is machine-expressed — both input schema (VT-N quoted format) and output tokens (Row-Verdict + CHECK RESULT) are structural tokens within the prompt, such that no prose reading is required at any step. Pre-conditions present and predicate specifiable (C-33 PASS) but checker I/O not fully machine-parseable without prose reading = C-33 PASS + C-36 FAIL.

**R12 dependency edges:**
- C-34 depends on C-32
- C-35 depends on C-29 and C-31
- C-36 depends on C-34 AND C-35

---

## Three new criteria from R11 excellence signals (carried from v12)

| New criterion | R11 excellence signal | What is testable |
|---|---|---|
| **C-31** Named contradiction halt type | ES-1 (V-03): The contradiction between Step 8b prose and Step 8c Match? is introduced as a **named typed structural event** with a machine-greppable label (`CONTRADICTION SIGNAL: Seq# N`) and requires a typed Rem# output (`Scope String Correction`) before the trace may advance | Is the contradiction event named with a typed label? Is the label machine-greppable (fixed token, no prose variation)? Is a Rem# output required? Is the Rem# type specified as `Scope String Correction`? |
| **C-32** Self-contained Match? computation | ES-2 (V-04): Step 8 header carries a re-affirmation of the VT# token list at the step boundary, making Match? computation self-contained — a checker needs only the Step 8 header and the Step 8c table, with zero dependency on Steps 0, 3, or 11 | Is a VT# token list present at the Step 8 header boundary? Can Match? be fully computed from only the Step 8 header + Step 8c table? Is there no structural dependency on Steps 0, 3, or 11 for Match? computation? |
| **C-33** Automated-check predicate completeness | ES-3 (V-05 only): All three automated-check pre-conditions are simultaneously present — (a) reference set co-located at Step 8 header, (b) named halt type with greppable label, (c) Rem# format requirement — such that the automated-check predicate is fully specifiable without semantic reading of prose or cross-section navigation | Are all three pre-conditions simultaneously present? Can an automated checker operate using only Step 8 header + Step 8c table + halt label pattern? Is the predicate fully specifiable from structural tokens alone? |

---

## Three new criteria from R10 excellence signals (carried from v12)

| Criterion | R10 excellence signal | What is testable |
|---|---|---|
| **C-28** Coherence-spine progression gate | ES-1 (V-03): Step 8b contains a REQUIRED prose confirmation per Gap?=Y boundary, explicitly verifying all three link arms (Step 8a → Step 11 → Step 7/9) before Step 9 may proceed | Is a per-boundary confirmation present at Step 8b? Does it name all three link arms? Is it marked REQUIRED? Does it structurally block advancement to Step 9? |
| **C-29** Scope-string coherence table | ES-2 (V-04): Step 8c contains a required table with columns Step3-Auth / Step8a-Invoked / Step11-Params / Match? for each Gap?=Y boundary, positioned before Step 9 | Is a Step 8c table present? Does it carry all four required columns? Is Match? binary (Y/N) per row? Is it required before Step 9? Are VT# scope strings present in column values? |
| **C-30** Dual-surface contradiction signal | ES-3 (V-05 only): Both Step 8b prose confirmation AND Step 8c Match? table are required; a mismatch (prose says coherent, Match? = N) is detectable from structure alone without semantic reading of prose; VT# scope strings appear consistently across both surfaces | Are both C-28 and C-29 surfaces present and both REQUIRED? Is there a structural rule making prose / Match? divergence self-evidencing? Do VT# scope strings propagate consistently from Step 8b prose to Step 8c column values? |

---

## Full aspirational tier — C-21 through C-37

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
| C-34 | Structured VT-N schema input | 5 | C-32 |
| C-35 | Row-level verdict token | 5 | C-29, C-31 |
| C-36 | Full checker contract | 5 | C-34, C-35 |
| **C-37** | **Checker algorithm declaration** | **5** | **C-36** |
