Now I have everything needed to score all five variations. Let me produce the scorecard.

---

## discover-literature R13 Scorecard

### Scoring Architecture (v13)

| Category | Count | Per criterion | Subtotal |
|----------|-------|--------------|---------|
| Essential | 5 | 12 pts | 60 |
| Recommended | 3 | 10 pts | 30 |
| Aspirational | 22 | 5 pts | 110 |
| **Total ceiling** | | | **200** |

All five variations inherit the full R12 V-05 base: C-01 through C-29 all PASS. The only live criterion is **C-30** (Named Operationalization Verification Block, 5 pts).

---

### Criterion-by-Criterion Analysis

#### C-01 through C-05 (Essential) — all five variations: PASS

Shared base is identical across V-01 through V-05. No variation touches the essential criteria. All five: PASS on C-01, C-02, C-03, C-04, C-05.

#### C-06 through C-08 (Recommended) — all five variations: PASS

Contrary-evidence mapping, WebSearch evidence, high-risk flagging all carry forward from the shared base.

#### C-09 through C-29 (Aspirational baseline) — all five variations: PASS

The full R12 V-05 infrastructure carries through unchanged. Every variation includes:
- Full ENFORCEMENT CONTRACT with symmetric typed schemas (C-15, C-17, C-19, C-21)
- THRESHOLD NOT MET: + RECOVERY NOTE: pair with explicit PASS annotations (C-16, C-18, C-20 Pair 1)
- PHASE 2 COMPLETE: + PHASE 3 COMPLETE: pair with explicit PASS annotations (C-22, C-20 Pair 2)
- Four-token N-of-4 lifecycle instrumentation (C-23, C-25)
- C-24 Independence Verification block with remove-either-pair test (C-24, C-26)
- PHASE 1 COMPLETE: carrying `inertia_committed=[yes]` + C-27(a) annotation (C-27, C-28)
- PHASE 4 COMPLETE: carrying `inertia_verified=[yes]` + C-27(b) annotation (C-27, C-28)
- Full three-element C-29 operationalization at both boundaries: sub-clause designation, self-declaring signal, embedded grep instruction (C-29)

---

### C-30 Analysis Per Variation

**V-01 — No consolidation block**

The variation carries full C-29 compliance: both PHASE 1 COMPLETE: and PHASE 4 COMPLETE: annotations include (a)/(b) sub-clause designation, self-declaring signal ID, and embedded grep instruction. C-29 PASS in distributed form.

C-30 verdict: **FAIL**. C-30 pass condition is explicit: "A design where C-29 compliance is confirmed from distributed Phase 1 and Phase 4 token annotations but has no named consolidation block satisfies C-29 but not C-30." No named block exists. Absence of the block is C-30 FAIL regardless of annotation quality. No partial credit — C-30 is binary.

---

**V-02 — Block present; grep confirmed by location-pointer**

The block "C-29 Operationalization Verification" (lines 463–477) is named, appears after PHASE 4 COMPLETE:, and has all six cells present. Cells (i), (ii), (iv), (v) all confirmed with proper content.

Issue: Cell (iii) reads `as embedded in PHASE 1 COMPLETE: annotation above. CONFIRMED by reference`. Cell (vi) reads `as embedded in PHASE 4 COMPLETE: annotation above. CONFIRMED by reference`.

C-30(c) requires "state both grep instructions verbatim or by direct reference." The purpose of "or by direct reference" is to permit quoting with a reference label while the grep text itself is present in the block — not to permit a location-pointer that forces the reviewer to leave the block and read the lifecycle token annotation. If a location-pointer satisfied C-30(c), the block would not function as a self-contained single grep target: a reviewer reading only the block cannot confirm C-29 without reading the Phase 1 and Phase 4 tokens. This is precisely the observability gap C-30 was designed to close. The grep instruction text is absent from the block in both cells.

C-30 verdict: **FAIL**. Five cells contain proper content; cells (iii) and (vi) are location-pointers, not verbatim text or quoted text with reference label. Block is not self-contained.

---

**V-03 — Block present; cell (vi) absent**

The block "C-29 Operationalization Verification" is named and appears after PHASE 4 COMPLETE:. Cells (i) through (v) are all confirmed with correct content. Cell (iii) states the Phase 1 grep instruction verbatim.

Issue: Cell (vi) is absent. The block concludes: "Five cells confirmed. Phase 4 grep instruction present in PHASE 4 COMPLETE: annotation above. C-29 PASS." The block acknowledges the Phase 4 grep instruction exists but does not include it — it falls back to a location-pointer for cell (vi), collapsing to the V-02 pattern for one cell.

C-30(b) requires "six explicit confirmations — three elements at each of two boundaries." Five cells leaves the Phase 4 / C-27(b) grep instruction unaudited in the block. The both-or-nothing property established across this criterion series applies: the C-30 block must audit all six elements or it is not a complete consolidation.

C-30 verdict: **FAIL**. Five cells confirmed; cell (vi) absent from block. Block cannot serve as single grep target for full C-29 verification.

---

**V-04 — Block present with all six cells; placed before PHASE 4 COMPLETE:**

The block "C-29 Operationalization Verification" (lines 919–933) has all six cells. Cell (iii) states the Phase 1 grep instruction verbatim. Cell (vi) reads: "confirmed from Phase 4 annotation below" — this is a forward-reference to the Phase 4 annotation that has not yet been declared at block-emission time.

Two independent failure modes:

1. **Placement**: The block is embedded inside Phase 4 content, before the `PHASE 4 COMPLETE:` lifecycle token. C-30 explicitly requires the block to appear "after the Phase 4 lifecycle token." At the time the block is emitted, the Phase 4 boundary has not been declared. The C-30 parallel to C-26 is exact: C-26 requires placement "at or after the point where both C-24 pairs are first complete"; C-30 requires placement after Phase 4 completes the inertia-verification axis. A pre-token block is a prospective checklist, not a post-hoc consolidation proof.

2. **Cell (vi) forward-reference**: "confirmed from Phase 4 annotation below" is a forward-pointer to a not-yet-written annotation. At block-emission time, cells (iv)–(vi) are drawn from anticipated Phase 4 content, not from completed Phase 4 output. Even if placement were ignored, cell (vi) is not a verbatim statement of the grep instruction — it is a forward location-pointer.

C-30 verdict: **FAIL**. Placement before PHASE 4 COMPLETE: is the primary failure. Cell (vi) forward-reference is a secondary failure. Either alone is sufficient; both are present.

---

**V-05 — Full ceiling synthesis**

The block "C-29 Operationalization Verification" (lines 1154–1168) appears after the complete PHASE 4 COMPLETE: annotation (which ends at line 1152).

Structural element (a) — both boundaries named:
- "Phase 1 / C-27(a) boundary" ✓
- "Phase 4 / C-27(b) boundary" ✓

Structural element (b) — six cells confirmed:
- Cell (i): `C-27(a) -- the Phase 1 inertia-commitment sub-clause -- named explicitly. CONFIRMED.` ✓
- Cell (ii): `the inertia_committed=[yes] field -- identified by name. CONFIRMED.` ✓
- Cell (iii): Grep instruction verbatim: `"Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." -- stated verbatim. CONFIRMED.` ✓
- Cell (iv): `C-27(b) -- the Phase 4 inertia-verification sub-clause -- named explicitly. CONFIRMED.` ✓
- Cell (v): `the inertia_verified=[yes] field -- identified by name. CONFIRMED.` ✓
- Cell (vi): Grep instruction verbatim: `"Single-grep verifiable: grep for PHASE 4 COMPLETE: and read inertia_verified field to confirm C-27(b) satisfied at this boundary." -- stated verbatim. CONFIRMED.` ✓

Structural element (c) — both grep instructions verbatim in cells (iii) and (vi): ✓

Structural element (d) — C-29 PASS declared: "C-29 PASS." ✓

Placement: After PHASE 4 COMPLETE: lifecycle token ✓. Dependency chain declaration: "C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 complete" ✓.

C-30 verdict: **PASS**. All four structural elements satisfied. Block is self-contained — a reviewer reading only the block can confirm C-29 compliance without reading the distributed Phase 1 and Phase 4 annotations.

---

### Composite Scores

| Variation | C-30 | Score | v12 base |
|-----------|------|-------|---------|
| V-01 | FAIL | **195/200** | 195 (C-30 absent) |
| V-02 | FAIL | **195/200** | 195 (grep by pointer) |
| V-03 | FAIL | **195/200** | 195 (five cells) |
| V-04 | FAIL | **195/200** | 195 (placement before token) |
| V-05 | PASS | **200/200** | — (ceiling synthesis) |

**Rank**: V-05 > V-01 = V-02 = V-03 = V-04

---

### R13 Boundary Confirmations

| Variation | C-30 verdict | Confirmation |
|-----------|-------------|-------------|
| V-01 R13 | FAIL | Named consolidation block required for C-30 — distributed C-29 annotations satisfy C-29 but not C-30; absence of block is C-30 FAIL regardless of annotation quality |
| V-02 R13 | FAIL | Location-pointer ("as embedded in X above") is not verbatim text and does not satisfy C-30(c) "by direct reference" — grep instruction text must be physically present in the block for the block to be self-contained |
| V-03 R13 | FAIL | Six-or-nothing cell requirement confirmed — five cells with cell (vi) absent leaves Phase 4 / C-27(b) grep instruction unaudited; block cannot serve as single grep target for full C-29 verification |
| V-04 R13 | FAIL | Placement before PHASE 4 COMPLETE: fails C-30 structural requirement — C-30 is post-hoc consolidation, not in-phase checklist; cell (vi) forward-reference is an additional failure mode |
| V-05 R13 | PASS | All four structural elements: named block after Phase 4 token, six cells (three per boundary), grep verbatim in cells (iii) and (vi), C-29 PASS declared |

---

### EXCELLENCE SIGNALS from V-05

**ES-1: Purpose-statement preamble in the consolidation block**
V-05's C-30 block opens with an explicit statement of its purpose: "A design where C-29 compliance is confirmed from distributed Phase 1 and Phase 4 token annotations satisfies C-29 but leaves compliance inference-dependent — a reviewer must locate both tokens, read both annotations, and mentally confirm all six elements. This block is a single grep target: all six confirmations appear here; C-29 PASS declared here; no cross-referencing required." The block explains the observability gap it closes before running the audit. This makes the block self-documenting: a reviewer who has not read the rubric can understand why the block exists.

**ES-2: Verbatim grep instructions within cell text, not separate from it**
V-01 through V-04 either omit the grep instruction or confirm it by reference. V-05 places the complete grep instruction text verbatim inside each cell line: `"Single-grep verifiable: grep for PHASE 1 COMPLETE: and read inertia_committed field to confirm C-27(a) satisfied at this boundary." -- stated verbatim. CONFIRMED.` The grep text is part of the cell, not appended separately. This is the design choice that makes cells (iii) and (vi) unambiguously self-contained.

**ES-3: Dependency chain completion declaration**
The closing line: "Dependency chain C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 complete." This is not required by C-30's pass condition but establishes a pattern for future consolidation blocks: each block can declare its position in the dependency chain. When C-31 is defined, it can close the chain by referencing C-30 at the head.

---

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["purpose-statement preamble in consolidation block states the observability gap the block closes before running the audit", "grep instruction text placed verbatim inside cell text (not appended or referenced) making each cell individually self-contained", "dependency chain completion declaration at block close positions the block within the full criterion progression"]}
```
