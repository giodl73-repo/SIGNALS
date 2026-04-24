# trace-request Rubric — v15 (2026-03-15)

**Scale:** 250 (Essential 60 + Recommended 30 + Aspirational 160)
**Golden threshold:** all 4 essential PASS AND composite >= 80% (200/250)

---

## One new criterion from R16 excellence signal

| New criterion | R16 excellence signal | What is testable |
|---|---|---|
| **C-39** Pre-execution halt boundary declaration | ES-1 (V-03, Tier A): A `TRACE CONTRACT` block declared before any trace step executes carries `HALT-EXPECTED-BOUNDARY: "BC-5 -- PreOperation elevated FLS bypass"` and `HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-5 AND Step 8c Match? = N for BC-5 row"` as machine-greppable tokens, pre-committing the specific boundary predicted to trigger the dual-surface halt and the predicate that will fire it; after the trace executes, a `TRACE CONTRACT validation:` token confirms whether the predicted boundary matched the actual `Row-Verdict = HALT` row in Step 8c — the pre-declaration and confirmation are both checkable by machine without semantic prose reading | Is a TRACE CONTRACT block present in the prompt before any trace step begins? Does it carry a `HALT-EXPECTED-BOUNDARY:` token naming the specific predicted halt boundary (boundary ID and descriptive label)? Does it carry a `HALT-EXPECTED-CONDITION:` token naming the dual-surface predicate for that boundary (Step 8b prose state AND Step 8c Match? = N for the named boundary row)? After the trace executes, is a `TRACE CONTRACT validation:` token present? Does the validation token confirm whether HALT-EXPECTED-BOUNDARY matches the `Row-Verdict = HALT` row in Step 8c? Is the match checkable by comparing `HALT-EXPECTED-BOUNDARY` boundary ID against the `Row-Verdict = HALT` row without reading prose? |

**Scale:** 245 → **250** (aspirational tier: 31 → 32 criteria, 155 → 160 pts). Golden threshold stays at >= 80%.

---

## Key design decisions

**C-39 vs C-38:** C-38 tests that the HALT-RULE in the CHECKER ALGORITHM block encodes the dual-surface architecture as its trigger predicate — the halt condition references Step 8b prose coherence state AND Step 8c Match? = N simultaneously, and this predicate is readable from the HALT-RULE token itself. C-39 tests that a pre-execution TRACE CONTRACT additionally pre-commits the specific boundary predicted to trigger that halt, pairing a machine-greppable `HALT-EXPECTED-BOUNDARY` token (naming the specific BC-N boundary before evidence is gathered) with a post-execution `TRACE CONTRACT validation` confirmation token (confirming whether the predicted boundary matched the actual HALT row). HALT-RULE encodes the generic dual-surface predicate (C-38 PASS) but no boundary is pre-declared before execution = C-38 PASS + C-39 FAIL. Pre-execution HALT-EXPECTED-BOUNDARY + post-execution validation both present = C-38 PASS + C-39 PASS.

**New dependency edge:**
- C-39 depends on C-38 AND C-35 (C-38 establishes the dual-surface HALT-RULE encoding — the generic predicate that the pre-declared condition names and the validation contract references; C-35 provides the Row-Verdict machine token in Step 8c — the post-execution match check compares HALT-EXPECTED-BOUNDARY against the specific Row-Verdict = HALT row by boundary ID without prose reading; both must be present before requiring the pre-declaration and confirmation contract to be machine-checkable)

**Signal not promoted in v15 — C-40 design surfaces:**

1. **DECLARE CONTRADICTION machine-greppable token in Step 8b (Tier B, V-02/V-05):** `DECLARE CONTRADICTION:` present as a named structural token within the Step 8b prose at the HALT boundary row, labeling the contradiction event at the exact moment it fires in the prose surface — before the Match? table is consulted. Creates a third detectable surface (prose-token surface) supplementing the dual-surface architecture of C-30. Explicitly requires V-02/V-05 to produce consistent multi-round evidence before a criterion can be frozen: the token must appear stably across variation axes (single-axis formal register, combined formal+storage-first+equal phases) before the testable surface can be reliably specified.

2. **Pre-trace CHECKER ALGORITHM commitment (Tier C, V-04):** CHECKER ALGORITHM block (with dual-surface HALT-RULE) emitted as the first structural block before Step 1, pre-committing the algorithm declaration before any boundary evidence is gathered. Requires evidence across multiple rounds that pre-trace placement produces different HALT-RULE phrase quality or context-window-compression survival than mid-trace placement before a criterion is justifiable.

---

## One new criterion from R15 excellence signal (carried from v14)

| New criterion | R15 excellence signal | What is testable |
|---|---|---|
| **C-38** HALT-RULE dual-surface architecture encoding | ES-1 (V-01): The HALT-RULE in the CHECKER ALGORITHM block explicitly encodes the C-30 dual-surface contradiction architecture as its halt trigger — declaring that halt fires when Step 8b prose asserts coherence AND Step 8c Match? = N simultaneously — rather than syntactically naming only the output token condition (e.g., `HALT-RULE: Row-Verdict = HALT iff Match? = N`); the halt predicate is expressed as a causal dual-surface rule such that the logical basis for halt (the simultaneous presence of a prose-coherent claim and a table-level mismatch) is readable from the HALT-RULE token itself without reference to any other section | Is the HALT-RULE present as a named machine-greppable token in the CHECKER ALGORITHM block (C-37 PASS required)? Does the HALT-RULE explicitly reference Step 8b prose state (a coherence claim or equivalent)? Does the HALT-RULE explicitly reference Step 8c Match? = N? Does the HALT-RULE declare that halt fires when both conditions hold simultaneously? Is the dual-surface condition expressed as the logical basis for halt rather than as a pointer to an output token (Row-Verdict = HALT)? Is the halt predicate interpretable from the HALT-RULE label alone without reading VT-N lines or Step 8c data? |

**Scale change from v14:** 245 → 250 (aspirational tier: 31 → 32 criteria, 155 → 160 pts).

---

## Key design decisions (R15, carried from v14)

**C-38 vs C-37:** C-37 tests that the CHECKER ALGORITHM block is present in the Step 8 Header and that MATCH-RULE, HALT-RULE, and OUTPUT-RULE are declared as named machine-greppable tokens — the algorithm is structurally present and parseable by fixed-token grep. C-38 tests that the HALT-RULE token additionally encodes the dual-surface contradiction architecture as its trigger predicate: Step 8b prose coherence claim AND Step 8c Match? = N simultaneously. HALT-RULE present as a syntactic pointer to the output token (e.g., `HALT-RULE: Row-Verdict = HALT iff Match? = N`) = C-37 PASS + C-38 FAIL. HALT-RULE present and encoding the dual-surface event as the logical basis for halt = C-37 PASS + C-38 PASS.

**Dependency edge:**
- C-38 depends on C-37 AND C-30 (C-37 establishes the CHECKER ALGORITHM block as a structural token in the Step 8 Header; C-30 establishes the dual-surface contradiction architecture — Step 8b prose surface AND Step 8c Match? table surface — being referenced by the HALT-RULE; both must be present before requiring the halt predicate to encode the dual-surface logic as a machine-greppable token phrase)

**Signal promoted in v15:** The C-39 design surface identified in v14 (live automated checker) was superseded by the R16 Tier A excellence signal (pre-execution halt boundary declaration). The live automated checker concept shifts to C-40 design surface.

---

## One new criterion from R13 excellence signal (carried from v13)

| New criterion | R13 excellence signal | What is testable |
|---|---|---|
| **C-37** Checker algorithm declaration | ES-1 (V-03): The Step 8 Header carries a CHECKER ALGORITHM block immediately after TOKEN-COUNT, declaring MATCH-RULE, HALT-RULE, and OUTPUT-RULE as formal machine-greppable pseudocode tokens — the comparison predicate is machine-readable as a structural property of the header without semantic prose parsing; the algorithm declaration is independent of schema tokens and does not require reading VT-N lines to interpret the logic | Is a CHECKER ALGORITHM block present in the Step 8 Header? Does it appear immediately after TOKEN-COUNT (within the same Step 8 header section)? Does it declare MATCH-RULE, HALT-RULE, and OUTPUT-RULE as named machine-greppable tokens? Is the algorithm declaration structurally independent of VT-N schema tokens (no positional or semantic dependency on VT-N lines to interpret predicate logic)? Is algorithm logic parseable via fixed-token grep without semantic prose reading? |

---

## Key design decisions (R13, carried from v13)

**C-37 vs C-36:** C-36 tests that both checker input (VT-N quoted schema) and checker output (Row-Verdict + CHECK RESULT) are machine-parseable structural tokens within the prompt, such that the complete checker contract — parse input, compare, emit output — requires no prose reading at any step. C-37 tests that the checker algorithm itself — the comparison predicate (MATCH-RULE), the halt condition (HALT-RULE), and the output emission rule (OUTPUT-RULE) — is additionally declared as machine-greppable tokens in the Step 8 Header, such that the logic governing how the contract is executed is also readable from structure alone without semantic prose parsing. Full checker contract present (C-36 PASS) but algorithm declared as prose description rather than named machine-greppable tokens = C-36 PASS + C-37 FAIL.

**Dependency edge:**
- C-37 depends on C-36 (both machine-parseable input schema and externalized output tokens must be simultaneously established as the full checker contract before requiring the algorithm declaration that operates on them to also be a structural token — C-36 establishes the I/O contract, C-37 tightens the algorithm encoding)

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

## Full aspirational tier — C-21 through C-39

| # | Criterion | Points | Depends on |
|---|---|---|---|
| C-21 | Step 8a scope-string format | 5 | C-08 |
| C-22 | Step 8a completeness gate | 5 | C-21 |
| C-23 | VT# token vocabulary declared | 5 | C-08 |
| C-24 | Step 11 param-set co-location | 5 | C-08 |
| C-25 | Step 8 header boundary marker | 5 | C-23 |
| C-26 | Gap?=Y boundary count match | 5 | C-22, C-25 |
| C-27 | Step 8b required-field marker | 5 | C-26 |
| C-28 | Coherence-spine progression gate | 5 | C-27 |
| C-29 | Scope-string coherence table | 5 | C-26 |
| C-30 | Dual-surface contradiction signal | 5 | C-28, C-29 |
| C-31 | Named contradiction halt type | 5 | C-29 |
| C-32 | Self-contained Match? computation | 5 | C-23, C-25 |
| C-33 | Automated-check predicate completeness | 5 | C-31, C-32 |
| C-34 | Structured VT-N schema input | 5 | C-32 |
| C-35 | Row-level verdict token | 5 | C-29, C-31 |
| C-36 | Full checker contract | 5 | C-34, C-35 |
| C-37 | Checker algorithm declaration | 5 | C-36 |
| C-38 | HALT-RULE dual-surface architecture encoding | 5 | C-37, C-30 |
| C-39 | Pre-execution halt boundary declaration | 5 | C-38, C-35 |

**Aspirational subtotal (C-21–C-39):** 19 criteria shown above × 5 = 95 pts of the 160 pt aspirational tier. Criteria C-08 through C-20 (13 criteria × 5 = 65 pts) are stable and inherited from v12 without modification.

---

## Tier summary

| Tier | Criteria | Points |
|---|---|---|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-39 | 160 |
| **Total** | **39 criteria** | **250** |

**Golden threshold:** all 4 essential PASS AND composite >= 200/250 (80%).

---

## Dependency chain — checker contract stack (C-28 → C-39)

```
C-28 (coherence gate)  C-29 (coherence table)
       \                    /         \
        C-30 (dual-surface) C-31 (halt type)
          \                    \
           \                C-35 (row verdict)    C-32 (self-contained)
            \                    \                    \
             \                C-36 (full contract) <- C-34 (VT-N schema)
              \                    \
               \                C-37 (algorithm declaration)
                \                    \
                 +------ C-38 (HALT-RULE dual-surface encoding) ------+
                                      \             \
                                       \          C-35 (row verdict) [reused]
                                        \             \
                                         +--- C-39 (pre-execution halt boundary declaration) ---+
```

C-39 closes the current chain: the dual-surface architecture established at C-30, encoded in the HALT-RULE at C-38, is now required to be pre-committed as a named boundary prediction before the trace executes — the HALT-EXPECTED-BOUNDARY token names the specific BC-N boundary predicted to trigger the halt, paired with a post-execution TRACE CONTRACT validation token confirming the prediction against the actual Row-Verdict = HALT row in Step 8c. The checker contract (C-36), the algorithm declaration (C-38), and the row-level verdict token (C-35) are all prerequisites: the pre-declaration names the boundary; the post-execution confirmation verifies it by matching HALT-EXPECTED-BOUNDARY against the Row-Verdict = HALT row by boundary ID.
