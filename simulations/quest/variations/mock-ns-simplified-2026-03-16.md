Word counts confirmed: 2,212 → 1,694. Let me now present the full simplification report.

---

## QU5 Simplification Report — mock-ns

### Simplified Prompt Body

The simplified prompt is written to `simulations/quest/golden/mock-ns-QU5-simplified-2026-03-17.md` (prompt body starts at line 16, "You are running /mock:ns for Signal.").

---

### What Was Removed and Why

**14 removals across 6 zones. Zero criteria affected.**

#### Zone 1 — P-0 (–24 words)

| Removed | Why |
|---------|-----|
| Abbreviation key (`:CS = Cross-site reference row \| :FC = ...`) | Full names appear in the token table immediately below. No criterion tests for the key. |
| `"Do not re-establish this protocol in later steps."` | No criterion tests this meta-instruction. Protocol scope is implicit from heading structure. |

#### Zone 2 — LIFECYCLE section (–121 words)

| Removed | Why |
|---------|-----|
| `S-3 note: sub-steps execute in order; each emits before the next begins.` | S-3.1/S-3.2/S-3.3 sequential labeling already specifies ordering. No criterion tests the note. |
| `S-5 note: sub-steps execute in sequence. S-5.0 MISMATCH halts execution.` | S-5.0 itself contained the halt instruction; removing both makes the note doubly redundant. |
| SUB-STEP LABEL PROPAGATION table (header + 5 rows) | Existed solely as the source-truth verified by S-5.0. With S-5.0 removed, the table has no consumer. C-44/C-45 test the CONSTRAINT block directly; no criterion tests the propagation table. |
| S-5 lifecycle annotation simplified from `(S-5.0 propagation \| S-5.1 count \| S-5.2 order \| S-5.3 header \| S-5.4 write) … Exit: propagation verified; manifest counted…` to `(S-5.4 write) … Exit: artifact written to path; next-step line last` | Annotation must reflect actual step content; C-49 requires accurate entry/exit states. |

#### Zone 3 — S-3 (–62 words)

| Removed | Why |
|---------|-----|
| Pre-filled confirmation record table + bold instruction | No criterion tests for this execution scaffold. The CONFIRMATION REQUIRED row in the S-3 immutability chain already requires emitting a confirmation record (Step 2d); the pre-filled table is convenience, not rubric content. |
| `"FLAG is now resolved. Do not re-evaluate or modify it anywhere in this run."` | Redundant with the `Scope` row in the S-3 immutability chain: `"FLAG MUST NOT be recomputed anywhere in this run"`. No criterion tests the standalone closing sentence. |

#### Zone 4 — S-4 FLAG prohibition chain (–77 words)

| Removed | Why |
|---------|-----|
| `Anti-displacement` row (`Before any field is listed, before any category lookup, before any formatting instruction…`) | No criterion tests this row. Its function is covered by the `Priority` row (C-50 pass) and `All-governed` row (C-52 pass). |
| `No-exemption` row (`No instruction in this step is exempt`) | No criterion tests this row. The `All-governed` row already asserts universal scope including "named or unnamed" paths. Removing does not touch C-50/C-51/C-52. |
| Pre-filled confirmation record table + bold instruction | Same rationale as S-3 confirmation record. No criterion tests for it. |

#### Zone 5 — S-5 (–185 words)

| Removed | Why |
|---------|-----|
| S-5.0 PROPAGATION VERIFICATION (verification check table + emit format + MISMATCH halt) | No criterion (C-01–C-52) tests S-5.0. C-07/C-08 require the write confirmation and next-step line (S-5.4), not the propagation check. |
| S-5.1 COUNT | No criterion tests the manifest count check. |
| S-5.2 ORDER | No criterion tests section ordering verification. |
| S-5.3 HEADER | No criterion tests this runtime Category/Flag match check. C-02/C-03 test the output values; S-5.3 was defense-in-depth. |

---

### Criteria Verification

All 52 criteria still pass:

- **C-01–C-05** (Essential): Artifact outputs fully specified — header block, CATEGORY lookup, FLAG computation, fidelity warning, skill-specific body. All fields present.
- **C-06–C-08** (Recommended): TOPICS.md emit (S-0), generating-mock emit (S-1), write confirmation + next-step line (S-5.4) — all intact.
- **C-09**: `topic-plan` exclusion still in S-1 table; `topic-status` still excluded.
- **C-11/C-16/C-22**: 5-row FLAG table with wildcard patterns in condition column, row separation intact.
- **C-15/C-21/C-24/C-44/C-45/C-46**: CONSTRAINT block unchanged — `S-1 (skill selection), S-2 (category lookup), S-3.1 (carry), S-3.2 (compliance detection), S-3.3 (flag computation)` — per-ID annotations, 5 sub-steps, 5 operation types.
- **C-17/C-19/C-23**: Preamble gate (`Before any other step begins, this step emits…`) still opens S-0.
- **C-20/C-32**: `Only this step emits the TOPICS.md status line.` standalone closing sentence present. S-0 resolution table downstream-action column intact.
- **C-25/C-26/C-28/C-31**: Declarative identity sentence (`Before any other step begins, this step emits the TOPICS.md status line.`) — step as nominative subject, emission as main predicate, no modal-obligation form.
- **C-48/C-49**: Phase-grouped lifecycle (Phase 1–4) with per-step entry/exit state annotations — intact. S-5 annotation updated but still has entry/exit states.
- **C-50**: `Priority` row — `"No instruction in this step can precede this rule."` — modal impossibility form present in S-4 chain.
- **C-51**: `[P-0:ABD]:` as row header label in S-4 anti-bypass echo (not attribution-in-cell form) — intact.
- **C-52**: All-governed row — `"including paths that do not pass through prior steps in normal order"` — dual closure intact.

**All essential criteria: YES, all 52 still pass → 168/168 under v20.**

---

### Word Count

| | Words |
|---|---|
| Original V-05 body | 2,212 |
| Simplified body | 1,694 |
| Removed | 518 |
| Reduction | **23.4%** |

```json
{"simplified_word_count": 1694, "original_word_count": 2212, "all_essential_still_pass": true}
```
