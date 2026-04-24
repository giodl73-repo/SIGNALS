Now let me write the simplification report.

---

## Simplification Report: quest-variate golden prompt

**Word counts**: original ~2308 words → simplified ~1687 words (~27% reduction)

---

### What was removed and why

**1. NON-SUPPRESSION INVARIANT CONTRACT block (lines 21–43, ~163 words) — CUT entirely**

This preamble declared the non-suppression rule and stated that Step 4's compliance audit must include the invariant statement. But Step 4 already contains:
- `NON-SUPPRESSION INVARIANT ACTIVE:` header before the checkpoints
- `DUAL-CHECKPOINT:` declaration
- `EXECUTION DIRECTIVE:` at each co-location site

The preamble was a prologue to instructions that already self-enforce at execution time. Zero work for C-01 through C-05.

**2. EVALUATION ORDER TABLE SCHEMA (lines 75–98, ~186 words) — CUT entirely**

Defined the evaluation order table's columns a second time after the COLUMN CONTRACT already defined them, and a third time appears in Step 4 item 3's table header and column rules. Pure duplication. The simplified version references "Apply the Column Contract columns" in item 3, which is sufficient.

**3. Co-location annotation explanatory paragraphs in 4a and 4b (~165 words combined) — CUT to EXECUTION DIRECTIVE lines only**

Each co-location annotation contained a multi-sentence paragraph explaining *why* the annotation was co-located (self-referential meta-commentary). The functional instruction was the `EXECUTION DIRECTIVE:` line. The explanatory paragraph served C-33 (aspirational), not C-01 through C-05. Kept: the labeled header + EXECUTION DIRECTIVE line.

**4. `(Executing 4b regardless of 4a result.)` — CUT (7 words)**

Immediately redundant with the EXECUTION DIRECTIVE two lines above it.

**5. Role 6 closing sentence (~14 words) — CUT**

"Findings Synthesizer must not declare item 3 complete until this role emits a PASS summary." Already stated in Role 5's responsibility block. 

**6. Step 4 intro trimmed (~13 words saved)**

"(declared in the preamble above)" and "All boxes must be checked" removed. The Column Contract section carries its own completeness requirement; the instruction to write the completion acknowledgment is sufficient.

**7. Step 4 item 3 pointer trimmed (~25 words saved)**

"Apply the EVALUATION ORDER TABLE SCHEMA defined in the preamble" → "Apply the Column Contract columns." The TABLE SCHEMA being removed makes the pointer unnecessary; the COLUMN CONTRACT reference suffices.

**8. Completion-gate scope notes trimmed (~48 words saved)**

4a COMPLETION-GATE: 50 → 24 words (kept the functional restriction + non-suppression note, cut redundant restatements).  
4b COMPLETION-GATE: 34 → 12 words (single sentence captures the intent).

---

### Essential criteria verification

| Criterion | Pass? | Evidence in simplified prompt |
|-----------|-------|-------------------------------|
| C-01: variations complete/standalone/runnable | YES | "[COMPLETE SKILL BODY...]" in Step 2; Role 2 instruction |
| C-02: exactly N variations labeled V-01 through V-0N | YES | "Generate {N}...", Step 1 list, V-NN template |
| C-03: axis: and hypothesis: fields present | YES | Step 2 template with axis:, hypothesis:, sub-fields |
| C-04: single-axis = one axis change; combo = explicitly declared | YES | Intro "each changes exactly one axis", C-04 Prediction column |
| C-05: canonical axis bank with all six axes | YES | Step 1 list: role-sequence, output-format, lifecycle-emphasis, phrasing-register, inertia-framing, scoring-granularity |

**All five essential criteria: PASS**

---

### Minor remaining redundancy (left in intentionally)

The COLUMN CONTRACT has both an opening sentence ("A table written without completing this Column Contract is structurally incomplete") and a closing sentence ("A table written without this contract complete is structurally incomplete"). These ~22 redundant words were left in because they bracket the block structurally and the cost is negligible.

The Role 4 INDEPENDENCE REQUIREMENT (3 lines, ~36 words) remains as it reinforces behavior that relates to recommended/aspirational criteria without adding length burden.

---

Simplified file written to: `simulations/quest/golden/quest-variate-golden-QU5-simplified-2026-03-15.md`

```json
{"simplified_word_count": 1687, "original_word_count": 2308, "all_essential_still_pass": true}
```
