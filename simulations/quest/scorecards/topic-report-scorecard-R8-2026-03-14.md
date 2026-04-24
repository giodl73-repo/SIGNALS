Now I have all the information needed to score. Let me evaluate each variation systematically.

---

## `topic-report` — Round 8 Scorecard (Rubric v8)

**Rubric**: C-01–C-27 | Formula: `(ess/5 * 60) + (rec/3 * 30) + (asp/19 * 10)` | Golden: ess=5 AND composite ≥ 80

---

### Criterion Map — Shared Base Analysis

All five variations share the R7 V-05 neutral base. The base already satisfies C-01 through C-27 in full. The three variation axes (A/B/C) add mechanisms not captured by any C-01–C-27 pass condition. Before evaluating per-variation, I confirm the base criterion state:

| Criterion | Basis for PASS |
|-----------|---------------|
| C-01 | PHASE 4 writes and echoes `simulations/{topic}/status-{date}.md` |
| C-02 | SLOT 1 markdown table with Total/Complete/Open columns from PHASE 1 CHECKPOINT |
| C-03 | SLOT 2 lists every open signal with namespace, skill-type, owner field |
| C-04 | SLOT 3 readiness sentence calibrated to BLOCKERS (ready/not ready) |
| C-05 | SLOT 4 concrete next step naming the specific skill from BLOCKERS |
| C-06 | Branch B ASCII card template with 4 sections, `+--` borders, ≤40 lines |
| C-07 | PHASE 1 DISCOVER via Glob + TOPICS.md cross-reference = topic-status parity |
| C-08 | SLOT 2 entries use `{namespace}/{skill-type}` format explicitly |
| C-09 | Readiness sentence template names `{names from LOCKED BLOCKERS list}` -- specific, not generic |
| C-10 | `[RULE G-8 VERIFICATION]` names backtick, less-than, greater-than by character |
| C-11 | Step 2b emits explicit BLOCKERS block as first-class pre-computation artifact |
| C-12 | Branch B template uses only `+ - |` borders; no backtick/angle-bracket in template text |
| C-13 | G-7a COMPLETENESS and G-7b EXCLUSIVITY are separately named invariants in Step 2c |
| C-14 | `[RULE BRANCH-SEAL]` at dispatch + `[RULE BRANCH-SEAL-B]` at Branch B entry = two seal points |
| C-15 | Step 2d: "The BLOCKERS list is now frozen and final. No additions, removals, or revisions are permitted in any subsequent phase." -- standalone LOCK directive |
| C-16 | G-7a COMPLETENESS SCAN + G-7b EXCLUSIVITY SCAN execute before writing readiness sentence |
| C-17 | `[RULE G-7a/G-7b]` at SLOT 3, `[RULE G-9 INERTIA]` at SLOT 4, two branch-seal markers at dispatch/entry |
| C-18 | SLOT 3: LAYER 1 DECLARE `[RULE]` + LAYER 2 ANCHOR (LOCKED BLOCKERS ref) + LAYER 3 VERIFY (scan) all converge at write point |
| C-19 | G-7a/G-7b in register → `[RULE G-7a/G-7b]` annotations → "G-7a COMPLETENESS SCAN"/"G-7b EXCLUSIVITY SCAN" headers |
| C-20 | `[RULE G-7a]`, `[RULE G-7b]`, `[RULE G-9 INERTIA]` all carry correct/violation example pairs |
| C-21 | `[RULE G-9 INERTIA]`: "State the concrete action, then the stall cost" -- inertia clause in write instruction |
| C-22 | `=== THREE-LAYER WRITE POINT ===` with LAYER 1/2/3 enumeration + Recovery line at SLOT 3 |
| C-23 | Violation text at SLOT 4 contains criterion ID: `(no stall cost -- C-21 violation)` at minimum |
| C-24 | `G-9 INERTIA` in contract register → `[RULE G-9 INERTIA]` at annotation -- two-level chain for single-position invariant |
| C-25 | `=== THREE-LAYER WRITE POINT (BRANCH B) ===` with LAYER 1/2/3 self-contained within Branch B |
| C-26 | `[RULE G-9 INERTIA]` carries register-linked label (C-24) AND violation appends criterion ID `(C-21 violation)` (C-23) -- dual chain at same annotation position |
| C-27 | C-22 main-branch header + C-25 Branch B header both present -- dual-branch closure |

**Base state**: 5/5 essential, 3/3 recommended, 19/19 aspirational.

---

### Per-Variation Scoring

#### V-01 — Axis A: dual-identifier violation

**Delta from neutral base**: SLOT 4 violation text changed from `(no stall cost -- C-21 violation)` to `(no stall cost -- G-9 INERTIA / C-21 violation)`.

| Range | Pass count | Change vs base |
|-------|-----------|----------------|
| C-01–C-05 (essential) | 5/5 | none |
| C-06–C-08 (recommended) | 3/3 | none |
| C-09–C-27 (aspirational) | 19/19 | C-23 still passes (criterion ID present); C-26 still passes (register label `G-9 INERTIA` at annotation + criterion ID in violation). No criteria change. |

**Scores**: essential=5, recommended=3, aspirational=19
**Composite**: (5/5×60) + (3/3×30) + (19/19×10) = 60 + 30 + 10 = **100.0**
**Candidate satisfied**: C-28 YES (both G-9 INERTIA register label and C-21 criterion ID in violation text simultaneously)

---

#### V-02 — Axis B: recovery directive in Branch B header

**Delta from neutral base**: Branch B `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header gains explicit recovery instruction: "re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A."

| Range | Pass count | Change vs base |
|-------|-----------|----------------|
| C-01–C-05 (essential) | 5/5 | none |
| C-06–C-08 (recommended) | 3/3 | none |
| C-09–C-27 (aspirational) | 19/19 | C-25 already passes (LAYER 1/2/3 in Branch B); recovery directive is above C-25's pass threshold. SLOT 4 violation retains `(no stall cost -- C-21 violation)` -- C-23 passes, C-26 passes. No criteria change. |

**Scores**: essential=5, recommended=3, aspirational=19
**Composite**: **100.0**
**Candidate satisfied**: C-29 YES (explicit named recovery directive in Branch B header naming both the action and the prohibition against cross-branch reference)

---

#### V-03 — Axis C: slot-indexed contract register

**Delta from neutral base**: Register entries gain `[SLOT n]`/`[BRANCH B]`/`[PHASE 4]` annotations, e.g., `G-9 INERTIA [SLOT 4]`, `G-7a COMPLETENESS [SLOT 3]`, `G-1 [PHASE 4]`.

| Range | Pass count | Change vs base |
|-------|-----------|----------------|
| C-01–C-05 (essential) | 5/5 | none |
| C-06–C-08 (recommended) | 3/3 | none |
| C-09–C-27 (aspirational) | 19/19 | C-19: register → annotation → scan chain intact (slot annotations are additive, don't break label propagation). C-24: `G-9 INERTIA` label still present in register and annotation -- passes. C-23: violation still has `(no stall cost -- C-21 violation)`. No criteria change. |

**Scores**: essential=5, recommended=3, aspirational=19
**Composite**: **100.0**
**Candidate satisfied**: C-30 YES (each register entry names its governed output slot, creating forward-navigation path from register to template position; directionally orthogonal to C-19/C-24 backward chaining)

---

#### V-04 — Axes A+B: dual-identifier violation + Branch B recovery directive

**Delta from neutral base**: Both Axis A (violation text `G-9 INERTIA / C-21`) and Axis B (Branch B recovery directive) applied. No slot indexing.

| Range | Pass count | Change vs base |
|-------|-----------|----------------|
| C-01–C-05 (essential) | 5/5 | none |
| C-06–C-08 (recommended) | 3/3 | none |
| C-09–C-27 (aspirational) | 19/19 | All prior criteria pass unchanged. Axis A + Axis B are text-level additions at governed positions. C-23, C-24, C-26 all pass (register label at annotation + criterion ID in violation). C-25, C-27 pass (Branch B header is self-contained + recovery directive is additive). |

**Scores**: essential=5, recommended=3, aspirational=19
**Composite**: **100.0**
**Candidates satisfied**: C-28 YES, C-29 YES, C-30 NO

---

#### V-05 — Axes A+B+C: ceiling

**Delta from neutral base**: All three axes applied -- dual-identifier violation, Branch B recovery directive, slot-indexed register.

| Range | Pass count | Change vs base |
|-------|-----------|----------------|
| C-01–C-05 (essential) | 5/5 | none |
| C-06–C-08 (recommended) | 3/3 | none |
| C-09–C-27 (aspirational) | 19/19 | All three axes are text-level additions. C-19: `G-7a COMPLETENESS [SLOT 3]` -- slot tag is additive; register label is still `G-7a COMPLETENESS`, annotation and scan header labels unchanged. PASS. C-24: `G-9 INERTIA [SLOT 4]` in register, `[RULE G-9 INERTIA]` at annotation -- chain intact. C-26: register-linked label at annotation (C-24) + dual-ID in violation (C-23) co-present. PASS. C-27: both THREE-LAYER headers present. PASS. |

**Scores**: essential=5, recommended=3, aspirational=19
**Composite**: **100.0**
**Candidates satisfied**: C-28 YES, C-29 YES, C-30 YES

---

### Composite Score Table

| Variation | C-28 | C-29 | C-30 | Ess | Rec | Asp | Score | Golden |
|-----------|------|------|------|-----|-----|-----|-------|--------|
| V-01 | YES | NO | NO | 5/5 | 3/3 | 19/19 | **100.0** | YES |
| V-02 | NO | YES | NO | 5/5 | 3/3 | 19/19 | **100.0** | YES |
| V-03 | NO | NO | YES | 5/5 | 3/3 | 19/19 | **100.0** | YES |
| V-04 | YES | YES | NO | 5/5 | 3/3 | 19/19 | **100.0** | YES |
| V-05 | YES | YES | YES | 5/5 | 3/3 | 19/19 | **100.0** | YES |

**All five score identically under v8.** The three candidate criteria (C-28, C-29, C-30) are discriminators only under a potential v9 rubric.

---

### Ranking Under v8

**All tied at 100.0.** Tie-break by candidate criterion count (predictive ordering for v9):

1. **V-05** — 3 candidates (C-28, C-29, C-30) — ceiling
2. **V-04** — 2 candidates (C-28, C-29)
3. **V-01/V-02/V-03** — 1 candidate each — three-way tie

Under predicted v9 formula (aspirational_pass/22 × 10):

| Variation | asp/22 | v9 score |
|-----------|--------|---------|
| V-05 | 22/22 | **100.0** |
| V-04 | 21/22 | **95.5** |
| V-01/V-02/V-03 | 20/22 | **90.9** |

---

### Excellence Signals from V-05

V-05 is the unique ceiling design. Three mechanisms not captured by any C-01–C-27 criterion:

**1. Dual-identifier violation (C-28 candidate)**
The violation text at SLOT 4 carries both the contract register label (`G-9 INERTIA`) and the rubric criterion ID (`C-21`) simultaneously: `(no stall cost -- G-9 INERTIA / C-21 violation)`. A model encountering the violation can trace to the register obligation (G-9 INERTIA) or the rubric criterion (C-21) from a single textual entry point without any additional scan. C-23 alone provides the rubric path; C-24 alone provides the register path at the annotation label but not within the violation text. V-05 co-locates both paths inside the violation text.

**2. Named recovery directive in Branch B header (C-29 candidate)**
The Branch B THREE-LAYER header gains: "re-read this BRANCH B header to reconstruct the required layer sequence without referencing BRANCH A." C-25 requires structural self-containment (LAYER 1/2/3 enumerated); this directive adds active prescription. The directive names both the recovery action (re-read this header) and the boundary condition (without referencing BRANCH A). The structural guarantee (layers enumerated) becomes an executable recovery procedure (explicit instruction at attention-degradation).

**3. Slot-indexed contract register (C-30 candidate)**
Each register entry names its governed output slot: `G-9 INERTIA [SLOT 4]`, `G-7a COMPLETENESS [SLOT 3]`, `G-1 [PHASE 4]`. C-19 and C-24 establish backward chaining: annotation traces to register. Slot-indexing establishes the forward complement: register entry navigates directly to the governed slot without a template scan. The two directions are structurally independent -- backward and forward navigation are orthogonal reliability properties that can be present or absent independently.

**Structural pattern**: All three additions are **text-level edits within existing structural positions**. Axis A adds identifiers to violation text (no new sections). Axis B adds one sentence to an existing header (no new branches). Axis C adds slot annotations to existing register entries (no new phases). V-05 is the minimal design that closes all three candidate gaps.

---

### v9 Rubric Candidates Confirmed

| ID | Mechanism | Isolating variation | Independent of |
|----|-----------|---------------------|----------------|
| C-28 | Dual-identifier violation text (register label + rubric ID) | V-01 | C-23, C-24, C-26 |
| C-29 | Named recovery directive in Branch B header | V-02 | C-25, C-27 |
| C-30 | Slot-indexed contract register (forward-navigation) | V-03 | C-19, C-24 |

Each is independently verified by a single-axis variation. V-04 confirms C-28 + C-29 are additive (orthogonal failure modes). V-05 confirms all three are simultaneously satisfiable without structural conflict.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["dual-identifier violation text carries both contract register label (G-9 INERTIA) and rubric criterion ID (C-21) simultaneously, enabling two independent recovery paths from a single violation entry point without annotation scan", "named recovery directive in Branch B THREE-LAYER header converts structural self-containment (C-25) into active prescription by naming the recovery action and prohibiting cross-branch reference explicitly", "slot-indexed contract register entries name their governed output slot ([SLOT n]/[BRANCH B]/[PHASE 4]), establishing forward-navigation from register to template position as directional complement to C-19/C-24 backward chaining"]}
```
