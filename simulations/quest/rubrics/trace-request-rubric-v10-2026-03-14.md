Reading the scorecard, I can identify three promotable excellence signals:

- **ES-1 (V-03):** Step 8b prose-confirmation progression gate per Gap?=Y boundary
- **ES-2 (V-04):** Step 8c scope-string coherence table with independently auditable Match? column
- **ES-3 (V-05):** Dual-surface contradiction detection — mismatch between prose and table is format-detectable without semantic reading

These become **C-28**, **C-29**, **C-30**. Scale bumps 190 → 205.

---

# trace-request Rubric — v10 (2026-03-15)

**Scale:** 205 (Essential 60 + Recommended 30 + Aspirational 115)
**Golden threshold:** all 4 essential PASS AND composite >= 80

---

## Three new criteria from R10 excellence signals

| New criterion | R10 excellence signal | What is testable |
|---|---|---|
| **C-28** Coherence-spine progression gate | ES-1 (V-03): Step 8b contains a REQUIRED prose confirmation per Gap?=Y boundary, explicitly verifying all three link arms (Step 8a → Step 11 → Step 7/9) before Step 9 may proceed | Is a per-boundary confirmation present at Step 8b? Does it name all three link arms? Is it marked REQUIRED? Does it structurally block advancement to Step 9? |
| **C-29** Scope-string coherence table | ES-2 (V-04): Step 8c contains a required table with columns Step3-Auth / Step8a-Invoked / Step11-Params / Match? for each Gap?=Y boundary, positioned before Step 9 | Is a Step 8c table present? Does it carry all four required columns? Is Match? binary (Y/N) per row? Is it required before Step 9? Are VT# scope strings present in column values? |
| **C-30** Dual-surface contradiction signal | ES-3 (V-05 only): Both Step 8b prose confirmation AND Step 8c Match? table are required; a mismatch (prose says coherent, Match? = N) is detectable from structure alone without semantic reading of prose; VT# scope strings appear consistently across both surfaces | Are both C-28 and C-29 surfaces present and both REQUIRED? Is there a structural rule making prose / Match? divergence self-evidencing? Do VT# scope strings propagate consistently from Step 8b prose to Step 8c column values? |

**Scale:** 190 → **205** (aspirational tier: 20 → 23 criteria, 100 → 115 pts). Golden threshold stays at >= 80.

---

## Key design decisions

**C-28 vs C-26:** C-26 tests that every Gap?=Y row is wired to a Rem# and the three-way cross-link exists as a static structural property. C-28 tests that a progression gate at Step 8b actively confirms all three link arms before the trace may advance to Step 9. Cross-link present but no gate confirmation = C-26 PASS + C-28 FAIL.

**C-29 vs C-26:** C-26 tests that the three-way cross-link is traceable across Step 8a / Step 11 / Step 7–9. C-29 tests that the link is decomposed into four independently auditable cells per boundary, enabling machine-verifiable review without narrative reading. Traceable prose cross-link without a backing table = C-26 PASS + C-29 FAIL.

**C-30 vs C-28 + C-29:** C-28 and C-29 each independently enforce their surface. C-30 tests that the two surfaces are jointly required and that structural divergence between them — prose asserts coherent, table shows Match? = N — is itself a detectable signal. Both surfaces present but no rule enforcing consistency = C-28 PASS + C-29 PASS + C-30 FAIL.

**New dependency edges:**
- C-28 depends on C-26 (three-way cross-link structure exists to confirm) and C-25 (scope enumeration table with Gap? column exists); both required
- C-29 depends on C-26 (scope strings available) and C-27 (VT# identifiers present for column values); both required
- C-30 depends on C-28 AND C-29 (both surfaces must be required for contradiction to be format-detectable)

**Signal not promoted — C-31 design surface:** Automated consistency enforcement: a machine-readable schema or linting rule that computes Match? from the Step 8b prose token set and Step 8c cell values, producing a binary pass/fail without human judgment. Requires C-30 to produce consistent multi-round evidence of dual-surface divergence cases before the automated-check predicate can be reliably specified.

---

## Full aspirational tier — C-21 through C-30

| # | Criterion | Points | Depends on |
|---|---|---|---|
| C-21 | (prior) | 5 | — |
| C-22 | (prior) | 5 | — |
| C-23 | (prior) | 5 | — |
| C-24 | (prior) | 5 | — |
| C-25 | Scope enumeration table with Gap? column | 5 | — |
| C-26 | Scope-gap Rem# three-way cross-link | 5 | C-25, C-23 |
| C-27 | Vocabulary conformance gate (VT# + D=0 gate) | 5 | C-02 |
| **C-28** | **Coherence-spine progression gate** | **5** | C-26, C-25 |
| **C-29** | **Scope-string coherence table (Step 8c)** | **5** | C-26, C-27 |
| **C-30** | **Dual-surface contradiction signal** | **5** | C-28, C-29 |

**Aspirational total:** 23 criteria × 5 pts = **115 pts**

---

## Score bands (updated)

| Band | Range | Interpretation |
|---|---|---|
| Gold | >= 80% AND all-essential PASS | Ship signal |
| Silver | 65–79% AND all-essential PASS | Conditional — address gaps |
| Bronze | 50–64% OR one essential FAIL | Rework before advancing |
| Fail | < 50% OR two+ essential FAILs | Restart |
