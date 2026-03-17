Reading the scorecard, I can identify three promotable excellence signals:

- **ES-1 (V-03):** Named typed contradiction halt event with machine-greppable label and required `Scope String Correction` Rem# output
- **ES-2 (V-04):** Step 8 header VT# re-affirmation makes Match? computation self-contained — no cross-section dependency on Steps 0, 3, or 11
- **ES-3 (V-05):** All three automated-check pre-conditions co-present (reference set + halt type + Rem# format) → automated-check predicate is now specifiable

These become **C-31**, **C-32**, **C-33**. Scale bumps 205 → 220.

---

# trace-request Rubric — v11 (2026-03-15)

**Scale:** 220 (Essential 60 + Recommended 30 + Aspirational 130)
**Golden threshold:** all 4 essential PASS AND composite >= 80%

---

## Three new criteria from R11 excellence signals

| New criterion | R11 excellence signal | What is testable |
|---|---|---|
| **C-31** Named contradiction halt type | ES-1 (V-03): The contradiction between Step 8b prose and Step 8c Match? is introduced as a **named typed structural event** with a machine-greppable label (`CONTRADICTION SIGNAL: Seq# N`) and requires a typed Rem# output (`Scope String Correction`) before the trace may advance | Is the contradiction event named with a typed label? Is the label machine-greppable (fixed token, no prose variation)? Is a Rem# output required? Is the Rem# type specified as `Scope String Correction`? |
| **C-32** Self-contained Match? computation | ES-2 (V-04): Step 8 header carries a re-affirmation of the VT# token list at the step boundary, making Match? computation self-contained — a checker needs only the Step 8 header and the Step 8c table, with zero dependency on Steps 0, 3, or 11 | Is a VT# token list present at the Step 8 header boundary? Can Match? be fully computed from only the Step 8 header + Step 8c table? Is there no structural dependency on Steps 0, 3, or 11 for Match? computation? |
| **C-33** Automated-check predicate completeness | ES-3 (V-05 only): All three automated-check pre-conditions are simultaneously present — (a) reference set co-located at Step 8 header, (b) named halt type with greppable label, (c) Rem# format requirement — such that the automated-check predicate is fully specifiable without semantic reading of prose or cross-section navigation | Are all three pre-conditions simultaneously present? Can an automated checker operate using only Step 8 header + Step 8c table + halt label pattern? Is the predicate fully specifiable from structural tokens alone? |

**Scale:** 205 → **220** (aspirational tier: 23 → 26 criteria, 115 → 130 pts). Golden threshold stays at >= 80%.

---

## Key design decisions

**C-31 vs C-30:** C-30 tests that structural divergence between the prose and table surfaces is format-detectable without semantic reading. C-31 tests that the contradiction event is named and typed, carrying a fixed machine-greppable label and a required Rem# format output. Detectable divergence present but no typed halt event = C-30 PASS + C-31 FAIL.

**C-32 vs C-29:** C-29 tests that the Step 8c coherence table is present with four required columns and is mandatory before Step 9. C-32 tests that a VT# token list is co-located at the Step 8 header boundary, making Match? computation self-contained — no cross-section navigation to Steps 0, 3, or 11 required. Table present with all required columns but no header re-affirmation = C-29 PASS + C-32 FAIL.

**C-33 vs C-31 + C-32:** C-31 and C-32 each independently enforce their pre-condition. C-33 tests that all three pre-conditions (reference set, named halt type, Rem# format) are simultaneously present, making the automated-check predicate fully specifiable. Any two present but not all three = one of C-31 / C-32 PASS + C-33 FAIL.

**New dependency edges:**
- C-31 depends on C-30 (dual-surface contradiction must be format-detectable before halt typing can be tested) and C-29 (Match? column must be present for a typed halt event to fire)
- C-32 depends on C-29 (coherence table required before self-contained computation is meaningful) and C-27 (VT# identifiers must exist to populate header re-affirmation)
- C-33 depends on C-31 AND C-32 (both pre-conditions required before the automated predicate is specifiable)

**Signal not promoted — C-34 design surface:** Live automated checker: a runnable tool or schema validator that consumes the Step 8 header VT# list, the Step 8c table cells, and the halt label token and produces a binary pass/fail without human judgment. Requires C-33 to produce consistent multi-round evidence that the predicate specification is stable across variation axes before a tool contract can be reliably frozen.

---

## Three new criteria from R10 excellence signals (carried from v10)

| Criterion | R10 excellence signal | What is testable |
|---|---|---|
| **C-28** Coherence-spine progression gate | ES-1 (V-03): Step 8b contains a REQUIRED prose confirmation per Gap?=Y boundary, explicitly verifying all three link arms (Step 8a → Step 11 → Step 7/9) before Step 9 may proceed | Is a per-boundary confirmation present at Step 8b? Does it name all three link arms? Is it marked REQUIRED? Does it structurally block advancement to Step 9? |
| **C-29** Scope-string coherence table | ES-2 (V-04): Step 8c contains a required table with columns Step3-Auth / Step8a-Invoked / Step11-Params / Match? for each Gap?=Y boundary, positioned before Step 9 | Is a Step 8c table present? Does it carry all four required columns? Is Match? binary (Y/N) per row? Is it required before Step 9? Are VT# scope strings present in column values? |
| **C-30** Dual-surface contradiction signal | ES-3 (V-05 only): Both Step 8b prose confirmation AND Step 8c Match? table are required; a mismatch (prose says coherent, Match? = N) is detectable from structure alone without semantic reading of prose; VT# scope strings appear consistently across both surfaces | Are both C-28 and C-29 surfaces present and both REQUIRED? Is there a structural rule making prose / Match? divergence self-evidencing? Do VT# scope strings propagate consistently from Step 8b prose to Step 8c column values? |

---

## Full aspirational tier — C-21 through C-33

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
| **C-31** | **Named contradiction halt type** | **5** | C-30, C-29 |
| **C-32** | **Self-contained Match? computation** | **5** | C-29, C-27 |
| **C-33** | **Automated-check predicate completeness** | **5** | C-31, C-32 |

**Aspirational total:** 26 criteria × 5 pts = **130 pts**

---

## Score bands (unchanged)

| Band | Range | Interpretation |
|---|---|---|
| Gold | >= 80% AND all-essential PASS | Ship signal |
| Silver | 65–79% AND all-essential PASS | Conditional — address gaps |
| Bronze | 50–64% OR one essential FAIL | Rework before advancing |
| Fail | < 50% OR two+ essential FAILs | Restart |
