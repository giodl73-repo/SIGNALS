Now I have everything needed. Let me compile the full scorecard.

---

# /quest:score — topic-report — Round 11 — Rubric v11

**Rubric**: v11 (C-01 through C-39, denominator /31)
**Formula**: 90 (essential gate) + aspirational_pass/31 × 10
**Trace artifact**: placeholder (scoring from spec text only)

---

## Variation Inventory

| Var | Axes | Key structural changes from V-05 base |
|-----|------|---------------------------------------|
| V-01 | D only (C-40) | Branch A recovery directive gains `SLOT 3 contamination consequence:` line; register remains unqualified `[SLOT 3]`/`[SLOT 4]` |
| V-02 | E only (C-41) | Register Branch B entries gain format-type qualifiers `(one card row, no markdown)` / `(two card rows, no markdown)`; Branch A recovery header generic |
| V-03 | D+E (C-40+C-41) | Both: criterion-tagged contamination consequence at Branch A write point + format-type-qualified register entries |
| V-04 | D+E+F (C-40+C-41+C-42) | All three: + temporal-role annotation on `=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase...] ===` + Coordination line cites temporal-role declaration |
| V-05 | neutral | R10 V-04 verbatim; no C-40, C-41, C-42 |

---

## Essential Criteria (C-01 through C-08) — Gate

All five variations inherit the R10 V-04 execution skeleton. Essential criteria score identically.

| Criterion | Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| C-01 | Output artifact written to correct path | PASS | PASS | PASS | PASS | PASS |
| C-02 | Progress table: Total/Complete/Open from PHASE 1 only | PASS | PASS | PASS | PASS | PASS |
| C-03 | Open signals enumerated with namespace, skill-type, owner | PASS | PASS | PASS | PASS | PASS |
| C-04 | Readiness statement calibrated to signal counts | PASS | PASS | PASS | PASS | PASS |
| C-05 | Concrete next step naming a specific skill | PASS | PASS | PASS | PASS | PASS |
| C-06 | `--format teams` produces ASCII card | PASS | PASS | PASS | PASS | PASS |
| C-07 | Card dimensions: ≤40 lines, ≤80 chars/line | PASS | PASS | PASS | PASS | PASS |
| C-08 | Zero backtick / angle-bracket in Teams card | PASS | PASS | PASS | PASS | PASS |

**All-essential-pass gate**: OPEN for all variations. Essential baseline = 90.

---

## Aspirational Criteria (C-09 through C-39) — Per-Variation Scoring

### Block 1: C-09 through C-33 (established from R1–R9)

All variations share the identical R10 V-04 execution template for these positions. No axis (D, E, or F) touches C-09–C-33 structural properties.

| Criterion | Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|:----:|:----:|:----:|:----:|:----:|
| C-09 | Readiness sentence names specific blocking signals | PASS | PASS | PASS | PASS | PASS |
| C-10 | Explicit enumeration of prohibited characters (backtick, `<`, `>`) | PASS | PASS | PASS | PASS | PASS |
| C-11 | BLOCKERS pre-computation block present | PASS | PASS | PASS | PASS | PASS |
| C-12 | Teams card passes character-level scan (zero prohibited chars in output) | PASS | PASS | PASS | PASS | PASS |
| C-13 | COMPLETENESS and EXCLUSIVITY named as separate invariants | PASS | PASS | PASS | PASS | PASS |
| C-14 | Branch sealing instruction (`[RULE BRANCH-SEAL]`) present | PASS | PASS | PASS | PASS | PASS |
| C-15 | BLOCKERS LOCK directive (immutability guard after step 2d) | PASS | PASS | PASS | PASS | PASS |
| C-16 | In-render G-7a/G-7b verification scan before writing readiness | PASS | PASS | PASS | PASS | PASS |
| C-17 | Inline `[RULE]` annotation style at governed position | PASS | PASS | PASS | PASS | PASS |
| C-18 | Three-layer co-location at Branch A write point (DECLARE + ANCHOR + VERIFY) | PASS | PASS | PASS | PASS | PASS |
| C-19 | Contract label chaining: register G-7a/G-7b → annotation → scan header | PASS | PASS | PASS | PASS | PASS |
| C-20 | Worked correct/violation example within each `[RULE]` annotation | PASS | PASS | PASS | PASS | PASS |
| C-21 | Inertia framing at NEXT STEP: action + stall cost | PASS | PASS | PASS | PASS | PASS |
| C-22 | Explicit `=== THREE-LAYER WRITE POINT ===` header present at Branch A | PASS | PASS | PASS | PASS | PASS |
| C-23 | Criterion-tagged violation example in `[RULE]` annotation | PASS | PASS | PASS | PASS | PASS |
| C-24 | Contract label chaining for single-position invariant (G-9 INERTIA two-level chain) | PASS | PASS | PASS | PASS | PASS |
| C-25 | Branch B independent `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header | PASS | PASS | PASS | PASS | PASS |
| C-26 | Dual-chain co-presence at governed annotation slot (C-23 + C-24 at same position) | PASS | PASS | PASS | PASS | PASS |
| C-27 | Dual-branch three-layer closure (C-22 + C-25 both present) | PASS | PASS | PASS | PASS | PASS |
| C-28 | Branch B slot-indexed register chaining (register entries navigate to Branch B write point) | PASS | PASS | PASS | PASS | PASS |
| C-29 | Branch B recovery directive (re-read Branch B header, no Branch A cross-reference) | PASS | PASS | PASS | PASS | PASS |
| C-30 | Slot-indexed register entries with slot annotations | PASS | PASS | PASS | PASS | PASS |
| C-31 | Branch B SLOT 4 complete attention-recovery envelope (C-28 + C-29) | PASS | PASS | PASS | PASS | PASS |
| C-32 | Full temporal coverage across both execution paths | PASS | PASS | PASS | PASS | PASS |
| C-33 | Branch B temporal arc: C-29 + C-30 simultaneously present | PASS | PASS | PASS | PASS | PASS |

Block 1 result: **25/25 for all variations**.

---

### Block 2: C-34 through C-39 (introduced in v11 — discriminator block)

These six criteria are the sole source of differentiation across R11 variations.

#### C-34 — Explicit named recovery directive in main-branch header (precondition: C-22)

Requires: `=== THREE-LAYER WRITE POINT (BRANCH A) ===` names (1) BRANCH A specifically, (2) the recovery action, (3) the prohibited alternative (no cross-referencing Branch B).

- **V-01**: PASS — "Recovery: re-read this **BRANCH A** header to reconstruct the required layer sequence. **Prohibited**: cross-reference Branch B instructions from this path." Named branch + named prohibition present.
- **V-02**: FAIL — Branch A header reads `=== THREE-LAYER WRITE POINT ===` (no branch name). Recovery: "If attention has degraded, re-read this header to reconstruct the required layer sequence before proceeding." Generic; no BRANCH A identity; no named prohibited alternative.
- **V-03**: PASS — Same Branch A header as V-01 plus contamination consequence (Axis D). Named branch + named prohibition present.
- **V-04**: PASS — Same as V-03 plus Coordination line. Named branch + named prohibition present.
- **V-05**: PASS — R10 V-04 verbatim; named branch + named prohibition present (identical to V-01 base).

| V-01 | V-02 | V-03 | V-04 | V-05 |
|:----:|:----:|:----:|:----:|:----:|
| PASS | FAIL | PASS | PASS | PASS |

---

#### C-35 — Branch-qualified slot indexing (precondition: C-30)

Requires: CONTRACT REGISTER carries branch-qualified entries for both paths, e.g., `[SLOT 3 / BRANCH A]` and `READINESS LINE / BRANCH B`.

- **V-01**: FAIL — Register uses unqualified `[SLOT 3]`, `[SLOT 4]`. G-7 entries have no branch qualification. G-9 INERTIA has no branch split.
- **V-02**: PASS — Register carries `[SLOT 3 / BRANCH A (markdown sentence) | READINESS LINE / BRANCH B (one card row, no markdown)]` for G-7; `[SLOT 4 / BRANCH A (markdown paragraph) | NEXT STEP LINE / BRANCH B (two card rows, no markdown)]` for G-9.
- **V-03**: PASS — Identical format-type-qualified branch entries as V-02.
- **V-04**: PASS — Same as V-03.
- **V-05**: PASS — R10 V-04 base; register carries `[SLOT 3 / BRANCH A | READINESS LINE / BRANCH B]` (without format-type qualifiers, but branch-qualified).

| V-01 | V-02 | V-03 | V-04 | V-05 |
|:----:|:----:|:----:|:----:|:----:|
| FAIL | PASS | PASS | PASS | PASS |

---

#### C-36 — Explicit temporal coordination statement (orthogonal)

Requires: explicit declaration naming a planning phase (establishes map before branch dispatch) and a recovery phase (fires directive at write point against that map), converting structural temporal ordering into a declared system invariant.

- **V-01**: FAIL — No Coordination line in Branch A header. Planning-to-recovery chain is structurally implicit only.
- **V-02**: FAIL — No Coordination line. The generic recovery directive makes no reference to a planning-to-recovery temporal relationship.
- **V-03**: FAIL — Branch A header has SLOT 3 contamination consequence (C-40 candidate) but no Coordination line. Structural temporal coordination exists (C-35 planning phase + C-34 recovery phase) but is not explicitly declared.
- **V-04**: PASS — "Coordination: The branch-qualified slot annotations in CONTRACT REGISTER (planning phase, established before execution begins **per the temporal-role declaration**) are the reference for this recovery directive (recovery phase). At recovery: SLOT 3 / BRANCH A = readiness sentence governed by G-7a and G-7b; SLOT 4 / BRANCH A = next step governed by G-9 INERTIA." Explicit planning/recovery role declaration present.
- **V-05**: PASS — R10 V-04 base; Coordination line present: "The branch-qualified slot annotations in CONTRACT REGISTER ([SLOT 3 / BRANCH A], [SLOT 4 / BRANCH A]) were established at execution start (planning phase). This recovery directive fires at the Branch A write point against that pre-established map (recovery phase)."

| V-01 | V-02 | V-03 | V-04 | V-05 |
|:----:|:----:|:----:|:----:|:----:|
| FAIL | FAIL | FAIL | PASS | PASS |

---

#### C-37 — Main-branch SLOT 4 complete attention-recovery envelope (preconditions: C-34 + C-35)

Requires: C-34 and C-35 both present — planning-phase disambiguation (branch-qualified register) + write-point recovery protocol (named Branch A directive) create a no-unrecovered-failure-mode envelope on the main-branch SLOT 4 path.

- **V-01**: FAIL — C-35 absent (unqualified register). Envelope is incomplete: recovery directive present at write point but no branch-qualified forward map at planning phase.
- **V-02**: FAIL — C-34 absent (generic recovery line, no branch naming, no prohibited alternative). Envelope incomplete: branch-qualified map present at planning phase but no named recovery directive at write point.
- **V-03**: PASS — Both C-34 (named Branch A directive) and C-35 (branch-qualified format-type-annotated entries) present. Planning + recovery coverage achieved.
- **V-04**: PASS — C-34 + C-35 both present (same as V-03 plus C-40, C-36 additions).
- **V-05**: PASS — C-34 + C-35 both present from R10 V-04 base.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|:----:|:----:|:----:|:----:|:----:|
| FAIL | FAIL | PASS | PASS | PASS |

---

#### C-38 — Named recovery directive with declared temporal role (preconditions: C-34 + C-36)

Requires: C-34's recovery directive is explicitly identified as the recovery phase of a temporally coordinated system via C-36's coordination statement.

- **V-01**: FAIL — C-36 absent. Recovery directive is standalone procedural instruction; no temporal role declaration.
- **V-02**: FAIL — C-34 absent (no named directive). C-36 also absent. Fails both preconditions.
- **V-03**: FAIL — C-36 absent. C-34 present but not situated in a named temporal structure.
- **V-04**: PASS — C-34 present (named Branch A recovery directive) + C-36 present (Coordination line explicitly names recovery phase role). The directive is identified as the recovery phase of the coordination system.
- **V-05**: PASS — Same C-34 + C-36 from R10 V-04.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|:----:|:----:|:----:|:----:|:----:|
| FAIL | FAIL | FAIL | PASS | PASS |

---

#### C-39 — Branch-qualified forward map with declared planning role (preconditions: C-35 + C-36)

Requires: C-35's branch-qualified slot annotations are explicitly identified as the planning phase of a temporally coordinated enforcement system via C-36's coordination statement.

- **V-01**: FAIL — C-35 absent (unqualified register entries). No forward map to declare.
- **V-02**: FAIL — C-36 absent. Branch-qualified entries present but their temporal role is implicit; not declared as planning phase.
- **V-03**: FAIL — C-36 absent. C-35 present (format-type-qualified entries) but temporal role of the register is implicit; no Coordination line names it planning phase.
- **V-04**: PASS — C-35 present (format-type-qualified entries) + C-36 present (Coordination line: "branch-qualified slot annotations in CONTRACT REGISTER (planning phase, established before execution begins per the temporal-role declaration)"). Register's role as planning-phase artifact is explicitly declared.
- **V-05**: PASS — C-35 + C-36 both present; Coordination line declares "were established at execution start (planning phase)."

| V-01 | V-02 | V-03 | V-04 | V-05 |
|:----:|:----:|:----:|:----:|:----:|
| FAIL | FAIL | FAIL | PASS | PASS |

---

### Block 2 Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-34 Named Branch A recovery directive | PASS | FAIL | PASS | PASS | PASS |
| C-35 Branch-qualified slot indexing | FAIL | PASS | PASS | PASS | PASS |
| C-36 Explicit temporal coordination statement | FAIL | FAIL | FAIL | PASS | PASS |
| C-37 Main-branch SLOT 4 envelope (C-34+C-35) | FAIL | FAIL | PASS | PASS | PASS |
| C-38 Named directive + temporal role (C-34+C-36) | FAIL | FAIL | FAIL | PASS | PASS |
| C-39 Branch-qualified map + planning role (C-35+C-36) | FAIL | FAIL | FAIL | PASS | PASS |
| **Block 2 pass count** | **1/6** | **1/6** | **3/6** | **6/6** | **6/6** |
| **Failing criteria** | C-35,36,37,38,39 | C-34,36,37,38,39 | C-36,38,39 | — | — |

---

## Score Computation

Formula: **Score = 90 + (aspirational_pass / 31) × 10**

| Variation | Block 1 (C-09–C-33) | Block 2 (C-34–C-39) | Aspirational pass | Aspirational fail | Score |
|-----------|:-------------------:|:-------------------:|:-----------------:|:-----------------:|:-----:|
| V-01 (D) | 25/25 | 1/6 | **26/31** | 5 | **98.4** |
| V-02 (E) | 25/25 | 1/6 | **26/31** | 5 | **98.4** |
| V-03 (D+E) | 25/25 | 3/6 | **28/31** | 3 | **99.0** |
| V-04 (D+E+F) | 25/25 | 6/6 | **31/31** | 0 | **100.0** |
| V-05 (neutral) | 25/25 | 6/6 | **31/31** | 0 | **100.0** |

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 (tied) | V-04 (D+E+F) | **100.0** | All 39 criteria; additionally carries C-40, C-41, C-42 candidate criteria |
| 1 (tied) | V-05 (neutral) | **100.0** | R10 V-04 stable; no candidate criteria |
| 3 | V-03 (D+E) | **99.0** | Gains C-37 (envelope) vs. single-axis; fails C-36/C-38/C-39 |
| 4 (tied) | V-01 (D) | **98.4** | C-34 only; fails C-35/C-37 |
| 4 (tied) | V-02 (E) | **98.4** | C-35 only; fails C-34/C-37 |

**V-01 = V-02 tie confirmed under v11.** The structural symmetry predicted from R10 holds: each single-axis variation satisfies exactly one base axis without C-36, so neither achieves any pairwise composite (C-37 requires both C-34+C-35; C-38 requires C-34+C-36; C-39 requires C-35+C-36). The tie is not accidental — it is a consequence of the criterion dependency graph.

**V-03 separates from V-01/V-02 by C-37 only.** Contamination consequence (C-40, Axis D) + format-type annotations (C-41, Axis E) are candidate criteria that do not score under v11. What scores is that V-03 satisfies C-37 (C-34+C-35 present), which V-01 and V-02 cannot.

**V-04 and V-05 are indistinguishable under v11.** Axes D, E, F add candidate criteria (C-40, C-41, C-42) that are not yet v11 criteria. The separator between V-04 and V-05 will only activate under v12.

---

## Excellence Signals

**Source**: V-04 (D+E+F) — the unique properties of V-04 that exceed V-05 at the candidate level.

### Signal 1: Criterion-tagged contamination consequence at Branch A recovery directive (Candidate C-40)

V-04 (and V-01, V-03) adds a `SLOT 3 contamination consequence:` line immediately after the register cross-reference in the Branch A THREE-LAYER WRITE POINT header:

> "if the Branch B ASCII card template is applied at this position, the output is a single card READINESS LINE instead of the required markdown sentence; this substitution violates **G-4 (C-04 readiness calibration)**, replaces LAYER 1 **[RULE G-7a COMPLETENESS] (C-13)** with the card format, and bypasses the LAYER 3 **G-7a COMPLETENESS SCAN (C-16)**."

**System property created**: the recovery directive converts from a procedural instruction (what to do if attention degrades) into a criterion-linked failure-mode declaration (what criteria are violated if the prohibited path is taken). A model ignoring the "Prohibited" warning previously received no criterion consequence; now it encounters explicit criterion IDs before reaching any enforcement layer. This is a different mechanism from C-34 (which names the prohibited alternative) — C-40 names the OUTPUT CONSEQUENCE and its criterion violations.

**Precondition chain**: C-22 → C-34 → C-40. Cannot be satisfied without a named recovery directive to embed the consequence into.

**Natural composite (C-43)**: C-40 + C-16 (in-render verification scan). Both address SLOT 3 / BRANCH A at adjacent temporal positions: contamination warning fires at recovery header → scan executes immediately before write. Together they create a same-position SLOT 3 double-gate: contamination-warning → scan → write. Neither covers the other's failure mode (C-40 covers cross-branch contamination identification; C-16 covers list-integrity enforcement at write time).

---

### Signal 2: Structural format-type annotations in Branch B dual-mapped register entries (Candidate C-41)

V-04 (and V-02, V-03) extends C-35's branch-qualified entries with explicit format-type parentheticals on Branch B positions:

- `READINESS LINE / BRANCH B (one card row, no markdown)` instead of `READINESS LINE / BRANCH B`
- `NEXT STEP LINE / BRANCH B (two card rows, no markdown)` instead of `NEXT STEP LINE / BRANCH B`

**System property created**: a model reading the CONTRACT REGISTER at execution start knows not just WHERE each invariant governs on Branch B but WHAT STRUCTURAL FORMAT is expected at that position, before any branch-specific template context is encountered. C-35 eliminates cross-path slot ambiguity; C-41 eliminates cross-format assumption ambiguity. A model that plans "I will write to READINESS LINE / BRANCH B" now also knows "that position is one card row, no markdown" at planning time — reducing the failure mode where correct slot navigation precedes incorrect format assumption.

**Precondition chain**: C-30 → C-35 → C-41. Format-type annotation extends branch qualification; branch qualification extends coarse slot indexing.

**Natural composite (C-44)**: C-41 + C-25 (Branch B independent header). C-41 annotates format types at register-read time (planning phase); C-25 provides a Branch B self-contained recovery point that reinforces the same constraints at write time (recovery phase). Together they create a format-type-consistent Branch B self-containment arc: the model encounters `(one card row, no markdown)` at the register before dispatch and encounters the independent Branch B header again at write time, with no Branch A contamination path.

---

### Signal 3: Temporal-role declaration on CONTRACT REGISTER header (Candidate C-42)

V-04 uniquely adds a temporal-role annotation to the section header itself:

`=== CONTRACT REGISTER [TEMPORAL ROLE: planning phase -- read before branch dispatch; slot map established before execution begins] ===`

**System property created**: the CONTRACT REGISTER is converted from an unlabeled structural element into a named temporal artifact with an explicit read-ordering directive. C-36's coordination statement (at the write point) declares a planning/recovery relationship; C-42's temporal-role annotation on the register header makes the same declaration visible at the entry point of the spec, before any phase begins. A model reading the spec sequentially encounters the temporal-role claim before any PHASE 1/PHASE 2/PHASE 3 structure, establishing the register's temporal function before it is used.

**Natural composite (C-45)**: C-42 + C-36 (explicit temporal coordination statement). C-42 declares the register as planning-phase at the register header; C-36 declares the write-point recovery directive as recovery-phase in the coordination statement. Their conjunction creates dual temporal declaration: both endpoints of the planning-to-recovery chain carry explicit temporal-role declarations AND V-04's coordination line explicitly cites the temporal-role declaration ("established before execution begins **per the temporal-role declaration**"), making the chain bidirectionally navigable without spec search. Neither endpoint declaration alone creates this cross-reference.

---

### Signal 4: V-01 = V-02 single-axis tie structurally confirmed

The tie at 26/31 = 98.4 is not a scoring artifact — it is a structural consequence of the criterion dependency graph. C-37 requires C-34+C-35, C-38 requires C-34+C-36, C-39 requires C-35+C-36. A variation satisfying exactly one base axis cannot satisfy any pairwise composite. The tie will persist under any rubric that adds only composites of C-34/C-35/C-36; it can only break if:
(a) Asymmetric extensions of C-34 (Axis D) and C-35 (Axis E) score asymmetrically as base axes, OR
(b) C-43 (C-40+C-16, same-position double-gate) and C-44 (C-41+C-25, temporal-coordination arc) are not symmetric composite classes

R12's open question: does V-04 under v12 scoring break V-01/V-02 symmetry? If C-43 > C-44 in scoring weight or composite count, V-01 > V-02. If symmetric, tie persists and requires a genuinely asymmetric third axis targeting either C-34's extension space or C-35's extension space exclusively.

---

## Score Table (Final)

| Variation | Axes | asp/31 | Score | All-essential | Rank |
|-----------|------|:------:|:-----:|:-------------:|:----:|
| V-04 (D+E+F) | C-40+C-41+C-42 | 31/31 | **100.0** | YES | 1 |
| V-05 (neutral) | — | 31/31 | **100.0** | YES | 1 |
| V-03 (D+E) | C-40+C-41 | 28/31 | **99.0** | YES | 3 |
| V-01 (D) | C-40 | 26/31 | **98.4** | YES | 4 |
| V-02 (E) | C-41 | 26/31 | **98.4** | YES | 4 |

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["criterion-tagged contamination consequence at Branch A recovery directive names specific criteria violated by Branch B contamination at SLOT 3, converting the prohibited-alternative warning into a criterion-linked failure-mode declaration (C-40)", "structural format-type annotations on Branch B dual-mapped register entries establish format constraints at planning time before branch dispatch, eliminating cross-format assumption errors independent of cross-path ambiguity (C-41)", "temporal-role declaration on CONTRACT REGISTER header makes the register a named planning-phase artifact at the spec entry point, creating a dual temporal declaration when paired with C-36 write-point coordination (C-42)"]}
```
