Written to `simulations/quest/variations/discover-literature-variations-R17-2026-03-20.md`.

---

## R17 Variations -- Summary

**Criterion probed: C-34 + C-35**

| V | Axis | C-34 | C-35 | Predicted |
|---|------|------|------|-----------|
| V-01 | C-33 PASS via scattered inline prose -- no labeled sub-section | FAIL | FAIL | 215/225 |
| V-02 | Labeled sub-section with 4 per-element attestations, no chain | PASS | FAIL | 220/225 |
| V-03 | Labeled sub-section + chain truncated at C-32 (C-33 link absent) | PASS | FAIL | 220/225 |
| V-04 | Labeled sub-section + chain with gap (C-30 skipped) | PASS | FAIL | 220/225 |
| V-05 | Full synthesis -- labeled sub-section + complete chain | PASS | PASS | 225/225 |

**Four axes probed:**

1. **Scattered-prose failure (V-01)** -- C-33 elements present in inline prose after C-32 PASS, but no `#### C-33 Compliance Declaration` heading. C-34 requires the declaration to be a labeled sub-section *distinct from surrounding text*; distributed confirmation within the C-32 PASS paragraph fails C-34. Direct analogy to C-31(c)'s surrounding-prose failure and C-24's scattered-annotations failure.

2. **C-34 alone, no C-35 (V-02)** -- Labeled sub-section (`#### C-33 Compliance Declaration`) with (a)(b)(c)(d) per-element confirmations and C-33 PASS. No terminal chain-completion statement anywhere in the sub-section. C-35 requires the statement to be *within* the C-34 sub-section boundary; absence is C-35 FAIL.

3. **C-35 chain truncated at C-32 (V-03)** -- Labeled sub-section PASS. Chain statement present but stops at `C-32 complete`, omitting the `-> C-33 complete` terminal link. C-35 requires the full chain named in order; stopping at C-32 omits C-33 as the current terminal and fails completeness.

4. **C-35 chain with gap (V-04)** -- Labeled sub-section PASS. Chain present: `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-31 -> C-32 -> C-33 complete` -- C-30 skipped. C-35 requires every link named; a gap at any position is C-35 FAIL. Symmetric to C-28's both-or-nothing: no link may be omitted.

5. **Full synthesis (V-05)** -- Labeled sub-section with (a)(b)(c)(d) confirmed, C-33 PASS, and complete chain `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 complete` as the sub-section's terminal statement. C-34 PASS, C-35 PASS = 225/225.

**What changes between variations:** Only the closing of the C-29 Operationalization Verification block -- specifically, whether (a) the C-33 declaration uses a labeled sub-section heading, and (b) a complete terminal chain statement appears within it. All preceding content (enforcement contract, phases, lifecycle tokens, six-cell audit, C-31/C-32 PASS declarations) is identical to R16 V-05 across all five variations.

**Dependency chain: C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-34 -> C-35**
