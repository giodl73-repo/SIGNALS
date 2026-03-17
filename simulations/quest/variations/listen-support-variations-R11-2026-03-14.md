Written to `simulations/quest/rubrics/listen-support-rubric-v11-variate-R11-2026-03-15.md`.

---

# listen-support Round 11 -- Skill Body Prompt Variations

**Rubric target**: v11 (225 pts)
**Base**: R10 V-05 (C-01 through C-35 at ceiling)

---

## Variation axes

3 single-axis, then 2 combined:

| # | Axis | Who satisfies |
|---|------|---------------|
| 1 | **Step 4 verbatim anchor** -- `INFERENCE RULE (confirmed)` requires quoting the exact first sentence from 2C paraphrase in brackets, not a free restatement | V-01, V-04, V-05 |
| 2 | **Exception SIGN-OFF BLOCK 5th field** -- `Paraphrase clause:` cites the specific paraphrase clause governing the assignment; no-exception path also states governing clause | V-02, V-05 |
| 3 | **Step 4B paraphrase echo** -- new block before constraint 5 echoes the confirmed/verbatim text, making it live generation context at the distribution scan | V-03, V-04, V-05 |
| 4 | V-01 + V-03 combined | V-04 |
| 5 | Full synthesis: verbatim anchor + 5th field + Step 4B echo + Part C **text-match confirmation** (2C vs Step 4 vs Step 4B, side-by-side with MATCH/DIVERGENCE ruling) | V-05 |

---

## Potential new criteria extracted

| ID | Name | Tightens | Who satisfies |
|----|------|----------|---------------|
| C-36 | Step 4 Verbatim Anchor from 2C | C-34 | V-01, V-04, V-05 |
| C-37 | Exception Block Grounds-to-Paraphrase Clause Citation | C-33 | V-02, V-05 |
| C-38 | Step 4B Paraphrase Echo Before Constraint 5 | C-32 (applied to audit scan) | V-03, V-04, V-05 |
| C-39 | Part C Paraphrase Chain Text-Match | C-35 | V-05 only |

**Signal logic:**

- **C-36** tightens C-34: "restate from 2C" allows fresh-but-consistent paraphrase generation; verbatim quotation requires actual retrieval. V-01's `Verbatim anchor from 2C: "[copy word for word]"` is structurally distinct from C-34's "restate" label.
- **C-37** tightens C-33: four-field block verifies exception status without connecting to the paraphrase commitment; the 5th `Paraphrase clause:` field forces the model to name the specific clause it is applying or overriding.
- **C-38** tightens C-32: C-32 placed the gate decision-adjacent to severity assignment; C-38 applies the same logic to the Step 4B constraint 5 compliance scan -- paraphrase must be live text, not upstream label.
- **C-39** tightens C-35: C-35 confirms audit results are consistent with paraphrase direction; C-39 confirms the Step 4 anchor and Step 4B echo contain the same text as the 2C paraphrase first sentence, closing the divergence path that C-34's label-based cross-reference leaves open.
