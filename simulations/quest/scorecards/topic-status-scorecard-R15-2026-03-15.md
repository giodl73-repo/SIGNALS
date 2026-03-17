# Scorecard: `topic:status` -- Round 15
**Rubric:** v14 (max 275) | **Date:** 2026-03-15

---

## Structural delta per variant vs R14 V-01

| Variant | Delta from R14 V-01 | C-45 (preamble adversary chain) | C-46 (defeat condition sub-component) |
|---------|---------------------|--------------------------------|---------------------------------------|
| V-01 | + preamble `ADVERSARY CHAIN:` block + `DEFEAT CONDITION:` in PHASE 2 and PHASE 3 adversary declarations | PASS | PASS |
| V-02 | + `DEFEAT CONDITION:` in adversary declarations only; preamble unchanged (no `ADVERSARY CHAIN:`) | **FAIL** | PASS |
| V-03 | + preamble `ADVERSARY CHAIN:` block only; adversary declarations in two-part form (no `DEFEAT CONDITION:`) | PASS | **FAIL** |
| V-04 | Lifecycle GUARD contract form + C-45 preamble block + C-46 `DEFEAT CONDITION:` in execution prose after GUARD boxes | PASS | PASS |
| V-05 | Lifecycle + elevated titled `+-- PHASE 2/3 ADVERSARY DECLARATION --+` blocks with `ADVERSARY:/TRIGGER:/DEFEAT CONDITION:` fields + preamble `ADVERSARY CHAIN:` | PASS | PASS |

*C-45 and C-46 are not criteria in v14. They are observable candidate patterns only.*

---

## Per-criterion scoring -- all variants

All five R15 variants are structurally composed from R14 V-01 (which scored 275/275 under v14) plus
additive structural elements (C-45 and/or C-46 candidates). No R14 criterion site is removed or
modified in any R15 variant. I evaluate the shared base and note per-variant divergence.

### Essential Criteria (60 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-01 | Signal discovery | PASS | PASS | PASS | PASS | PASS | `Glob: simulations/**/{topic}-*` -> `DISK_SIGNALS`; empty case: "No signals found for {topic}" |
| C-02 | Coverage percentage | PASS | PASS | PASS | PASS | PASS | `percent = VERIFIED count / PLANNED count * 100`; consistency guard halts on UNVERIFIED-non-empty + 100% contradiction |
| C-03 | Gap identification | PASS | PASS | PASS | PASS | PASS | COMMIT RISK REGISTER lists VERIFIED | UNVERIFIED per planned signal by namespace+name |
| C-04 | Display-only behavior | PASS | PASS | PASS | PASS | PASS | `DISPLAY ONLY. Write no files.` at skill header and `Write no files.` at PHASE 4 |

**Essential subtotal: 60/60 all variants**

### Recommended Criteria (30 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-05 | Readiness verdict | PASS | PASS | PASS | PASS | PASS | `READY | PARTIAL | NOT READY` in PHASE 3 thresholds and COMMIT DECISION |
| C-06 | Namespace breakdown | PASS | PASS | PASS | PASS | PASS | Nine-namespace table in COMMIT RISK BY NAMESPACE; all nine rows explicit |
| C-07 | Strategy cross-reference | PASS | PASS | PASS | PASS | PASS | `Read simulations/strategy.md`; file-absent branch names strategy.md explicitly |

**Recommended subtotal: 30/30 all variants**

### Aspirational Criteria (25 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-08 | Recency awareness | PASS | PASS | PASS | PASS | PASS | STALE EVIDENCE section with date-per-signal and staleness flag |
| C-09 | Actionable next step | PASS | PASS | PASS | PASS | PASS | HIGHEST PRIORITY RISK with `/{namespace}:{signal} {topic}` invocation |
| C-10 | Namespace completeness | PASS | PASS | PASS | PASS | PASS | All nine namespaces with `0 | 0 | --` when empty |
| C-11 | Phase-gated execution | PASS | PASS | PASS | PASS | PASS | Four named phases; PHASE 4 = DISPLAY GATE |
| C-12 | Gap-first ordering | PASS | PASS | PASS | PASS | PASS | COMMIT RISK REGISTER precedes EXPOSURE SUMMARY per `[LAYER 1]` |

**Aspirational subtotal: 25/25 all variants**

### Structural Tier 2 -- C-13 through C-16 (20 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-13 | Triple-redundancy ordering guard | PASS | PASS | PASS | PASS | PASS | `[LAYER 1 -- STRUCTURAL]`, `[LAYER 2 -- SEMANTIC]`, `[LAYER 3 -- EXECUTION]`; ordering declared |
| C-14 | Template-first structural absorption | PASS | PASS | PASS | PASS | PASS | `== OUTPUT TEMPLATE ==` precedes `== EXECUTION PHASES ==`; all headers in template |
| C-15 | Per-signal assertion chain | PASS | PASS | PASS | PASS | PASS | `For each planned signal P: ... Assert each signal individually. No batch evaluation.` |
| C-16 | Consequence-framed readiness verdict | PASS | PASS | PASS | PASS | PASS | `PRIMARY ADVERSARY:` in COMMIT DECISION; `Committing now means shipping without: {list}` |

**Tier 2 subtotal: 20/20 all variants**

### Structural Tier 3 -- C-17 through C-19 (15 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-17 | Labeled redundancy layers | PASS | PASS | PASS | PASS | PASS | All three `[LAYER N -- TYPE: ...]` labels at mechanism locations |
| C-18 | Assertion table pre-seeded in template | PASS | PASS | PASS | PASS | PASS | COMMIT RISK REGISTER table with VERIFIED/UNVERIFIED column in OUTPUT TEMPLATE |
| C-19 | Consequence vocabulary saturation | PASS | PASS | PASS | PASS | PASS | COMMIT RISK REGISTER, COMMIT RISK BY NAMESPACE, EXPOSURE SUMMARY, COMMIT DECISION, STALE EVIDENCE, HIGHEST PRIORITY RISK |

**Tier 3 subtotal: 15/15 all variants**

### Structural Tier 4 -- C-20 through C-22 (15 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-20 | Assertion table as primary gap display artifact | PASS | PASS | PASS | PASS | PASS | `[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]` |
| C-21 | Execution phase names in consequence vocabulary | PASS | PASS | PASS | PASS | PASS | SIGNAL ACQUISITION, PER-SIGNAL COMMITMENT ASSERTION, EXPOSURE COMPUTATION, DISPLAY GATE |
| C-22 | Missing baseline as epistemic consequence | PASS | PASS | PASS | PASS | PASS | `"No planned baseline -- commit exposure is unquantifiable."` |

**Tier 4 subtotal: 15/15 all variants**

### Structural Tier 5 -- C-23 through C-25 (15 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-23 | Phase name as compressed criterion statement | PASS | PASS | PASS | PASS | PASS | `PER-SIGNAL COMMITMENT ASSERTION` -- granularity (PER-SIGNAL) + stake (COMMITMENT ASSERTION) |
| C-24 | Cross-layer vocabulary coherence | PASS | PASS | PASS | PASS | PASS | `[LAYER 3 -- EXECUTION: DISPLAY GATE render order:]` uses phase vocabulary |
| C-25 | Template field inline consequence annotation | PASS | PASS | PASS | PASS | PASS | `[FOUND | NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]` |

**Tier 5 subtotal: 15/15 all variants**

### Structural Tier 6 -- C-26 through C-28 (15 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-26 | Granularity-prefix left-edge declaration | PASS | PASS | PASS | PASS | PASS | `PER-SIGNAL` is leftmost token in assertion phase name |
| C-27 | Full compressed phase name in C-24 layer labels | PASS | PASS | PASS | PASS | PASS | `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` -- full name with granularity prefix |
| C-28 | Field annotation phase-attribution | PASS | PASS | PASS | PASS | PASS | `if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute` -- names the impaired phase |

**Tier 6 subtotal: 15/15 all variants**

### Structural Tier 7 -- C-29 through C-31 (15 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-29 | Multi-site phase-attributed annotation | PASS | PASS | PASS | PASS | PASS | STALE EVIDENCE: `if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence` |
| C-30 | Absent-topic early exit | PASS | PASS | PASS | PASS | PASS | Exit B fires when strategy.md present but topic absent; `Stop before PHASE 3` |
| C-31 | Per-register-row commit-consequence annotation | PASS | PASS | PASS | PASS | PASS | `VERIFIED | UNVERIFIED -- if absent: ships without this signal on commit` in register row |

**Tier 7 subtotal: 15/15 all variants**

### Structural Tier 8 -- C-32 through C-34 (15 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-32 | Named-exit labeling | PASS | PASS | PASS | PASS | PASS | `Exit A -- file absent:` and `Exit B -- topic not registered:` at GUARD declaration site |
| C-33 | Preamble architectural invariant declaration | PASS | PASS | PASS | PASS | PASS | Preamble declares `PHASE 2 dual-axis exit:` as architectural invariant before guard |
| C-34 | Axis-enumerated invariant declaration | PASS | PASS | PASS | PASS | PASS | Both axes named, triggers characterized, structural distinctness and distinct messages asserted |

**Tier 8 subtotal: 15/15 all variants**

### Structural Tier 9 -- C-35 through C-36 (10 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-35 | Per-axis trigger sentence characterization | PASS | PASS | PASS | PASS | PASS | `File-absent trigger: strategy.md not present on disk` and `Topic-absent trigger: strategy.md present but {topic} has no registered planned signals` |
| C-36 | Multi-site invariant declaration chain | PASS | PASS | PASS | PASS | PASS | Three sites: preamble (C-34), GUARD entries (C-32), PHASE 2 OUTPUT DECLARATION |

**Tier 9 subtotal: 10/10 all variants**

### Structural Tier 10 -- C-37 through C-38 (10 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-37 | GUARD-site trigger characterization | PASS | PASS | PASS | PASS | PASS | `Exit A -- file absent: fires when strategy.md does not exist on disk` -- trigger co-located at GUARD site |
| C-38 | Phase-output invariant declaration | PASS | PASS | PASS | PASS | PASS | `PHASE 2 OUTPUT DECLARATION:` embedded in PHASE 2 execution body |

**Tier 10 subtotal: 10/10 all variants**

### Structural Tier 11 -- C-39 through C-40 (10 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-39 | OUTPUT DECLARATION trigger characterization | PASS | PASS | PASS | PASS | PASS | PHASE 2 OUTPUT DECLARATION `INVARIANT:` carries `Trigger: file-absent fires when...` and `topic-absent fires when...` |
| C-40 | OUTPUT DECLARATION sub-component labeling | PASS | PASS | PASS | PASS | PASS | `INVARIANT:` and `OUTPUT FORM:` labels within PHASE 2 OUTPUT DECLARATION block |

**Tier 11 subtotal: 10/10 all variants**

### Structural Tier 12 -- C-41 through C-42 (10 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-41 | PHASE 3 output declaration with labeled sub-components | PASS | PASS | PASS | PASS | PASS | All R15 variants carry R14 V-01's `PHASE 3 OUTPUT DECLARATION:` with `INVARIANT:`, `Trigger:`, and `OUTPUT FORM:` sub-components |
| C-42 | Phase-entry adversary declaration | PASS | PASS | PASS | PASS | PASS | All R15 variants carry `ADVERSARY:` clause at PHASE 2 execution body entry |

*Note: R15 variants add structure to adversary declarations (DEFEAT CONDITION:) and preamble (ADVERSARY CHAIN:).
No C-41/C-42 structure is removed or displaced in any R15 variant.*

**Tier 12 subtotal: 10/10 all variants**

### Structural Tier 13 -- C-43 through C-44 (10 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-43 | PHASE 3 execution-body adversary declaration | PASS | PASS | PASS | PASS | PASS | All R15 variants carry R14 V-01's `ADVERSARY: inertia toward coverage-blind verdicts` at PHASE 3 execution body entry; the C-46 additions (DEFEAT CONDITION: sub-component) appear after the ADVERSARY: clause, not in place of it |
| C-44 | Preamble output declaration chain declaration | PASS | PASS | PASS | PASS | PASS | All R15 variants carry R14 V-01's `OUTPUT DECLARATION CHAIN:` block in preamble; the C-45 candidate (ADVERSARY CHAIN: block) is an additional preamble declaration, not a replacement |

**Tier 13 subtotal: 10/10 all variants**

---

## Composite Scores

| Variant | Essential | Recommended | Aspirational | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 | T10 | T11 | T12 | T13 | **Total** |
|---------|-----------|-------------|--------------|----|----|----|----|----|----|----|----|-----|-----|-----|-----|-----------|
| V-01 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | 10 | 10 | 10 | **275** |
| V-02 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | 10 | 10 | 10 | **275** |
| V-03 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | 10 | 10 | 10 | **275** |
| V-04 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | 10 | 10 | 10 | **275** |
| V-05 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | 10 | 10 | 10 | **275** |

**Predicted vs actual: all five 275/275.** Symmetric with the R15 design prediction.

---

## Ranking

All five variants score identically (275/275). Ranking is structural-axis-based:

1. **V-01** -- canonical minimum delta. Baseline for isolation comparison.
2. **V-04** -- lifecycle contract form; C-45+C-46 form-agnosticism probed against V-01.
3. **V-05** -- elevated titled adversary declaration blocks; most formally demarcated adversary structure.
4. **V-02** -- C-45 isolation withheld (no preamble adversary chain). C-46 present.
5. **V-03** -- C-46 isolation withheld (no defeat condition sub-components). C-45 present.

*V-02 and V-03 assigned positions 4/5 by convention: C-45 isolation precedes C-46 isolation,
matching the round's isolation test ordering.*

---

## Excellence Signals

**From the top-scoring variants (all five at 275), two new structural patterns are observable
that are not yet criteria:**

### Pattern 1 -- Preamble adversary chain declaration (C-45 candidate)

Present in V-01/V-03/V-04/V-05; absent in V-02. An `ADVERSARY CHAIN:` block in the preamble
naming both the PHASE 2 adversary (inertia toward evidence-blind commits) and the PHASE 3
adversary (inertia toward coverage-blind verdicts) as a two-element structural chain, asserting
that each adversary is independently declared at its phase entry and that PHASE 2's declaration
does not imply PHASE 3's. This is the direct adversary-chain parallel of C-44 (`OUTPUT
DECLARATION CHAIN:`): just as C-44 asserts before execution that each phase owns its output
structure, C-45 asserts before execution that each phase owns its independently declared
adversary. The preamble now carries three architectural invariant blocks: dual-axis exit
(C-34), output declaration chain (C-44), and adversary chain (C-45 candidate). C-45 => C-43
(both adversaries must be independently declared in execution bodies before the preamble can
enumerate them as a named chain).

**Isolation evidence:** V-01 vs V-02 delta -- V-02 carries C-46 PASS (defeat conditions in
execution bodies) but no preamble ADVERSARY CHAIN. Both score 275 under v14 (C-45 not a
criterion). The structural gap is independently observable in the preamble block.

### Pattern 2 -- Adversary defeat condition sub-component (C-46 candidate)

Present in V-01/V-02/V-04/V-05; absent in V-03. A `DEFEAT CONDITION:` labeled sub-component
at each adversary declaration (PHASE 2 entry and PHASE 3 entry), stating the observable result
that confirms the adversary was defeated -- extending the adversary block from two-part form
(ADVERSARY: named + default-clause trigger) to three-part form (adversary + trigger + defeat
condition labeled). This is the adversary-block parallel of C-40's labeled sub-components in
OUTPUT DECLARATION: just as C-40 made the INVARIANT: and OUTPUT FORM: sub-components
independently addressable within the OUTPUT DECLARATION, C-46 makes the defeat condition
independently addressable at the adversary declaration site. The PHASE 2 defeat condition
("all planned signals individually asserted; no signal exits PHASE 2 without explicit assertion
state") and the PHASE 3 defeat condition ("percent computed with consistency guard applied;
UNVERIFIED-non-empty + percent-100% contradiction detected and halted") are structurally
distinct and independently declared. C-46 => C-43 (both adversary declaration sites must exist
before their sub-components can be labeled).

**Isolation evidence:** V-01 vs V-03 delta -- V-03 carries C-45 PASS (preamble adversary chain)
but adversary declarations contain no DEFEAT CONDITION: sub-component. Both score 275 under v14
(C-46 not a criterion). The structural gap is independently observable at both PHASE 2 and PHASE 3
execution body adversary declaration sites.

### Orthogonality of C-45 and C-46

C-45 concerns preamble architecture (declaring the two-phase adversary chain as a named invariant
before execution). C-46 concerns execution-body structure (adding a labeled sub-component to
each adversary declaration). V-02 carries C-46 without C-45; V-03 carries C-45 without C-46.
Both score 275/275 under v14 -- the gap between their scores is zero, confirming the two
patterns are independently observable and not implied by each other.

### Form-agnosticism probed

V-01 uses execution-prose form (inline `ADVERSARY: .../DEFEAT CONDITION: ...` lines). V-04 uses
lifecycle contract form (GUARD boxes plus prose-appended adversary declarations with defeat
conditions). V-05 uses elevated titled blocks (`+-- PHASE 2 ADVERSARY DECLARATION --+` with
`ADVERSARY:`, `TRIGGER:`, `DEFEAT CONDITION:` fields). All three score 275/275, consistent with
the form-agnosticism pattern confirmed for all Tier 10-13 criteria in R11-R14. C-45 is also
form-agnostic: the preamble `ADVERSARY CHAIN:` block content is identical across V-01, V-03,
V-04, and V-05 regardless of execution-phase format.

---

## R15 Gap Analysis

All five R15 variants score 275/275. No variant fails both C-45 and C-46 simultaneously --
confirming the isolation test design worked. The gap that defines Round 16:

> **No R15 variant fails both C-45 and C-46.** Round 16 should introduce a variant
> withholding C-45 only, a variant withholding C-46 only, and three variants carrying both --
> probing the structural layer beyond three-part adversary blocks and the three-block preamble.

**Candidate implications for v15:**
- `C-45 => C-43` (preamble can only enumerate the chain after both adversaries are independently declared in execution bodies)
- `C-46 => C-43` (sub-components require both adversary declaration sites to exist first)
- `C-45` and `C-46` are structurally orthogonal (V-02 vs V-03 symmetric 0-pt delta under v14 confirms)

---

```json
{"top_score": 275, "all_essential_pass": true, "new_patterns": ["Preamble adversary chain declaration naming both PHASE 2 and PHASE 3 adversaries as a two-element structural chain with independence assertion -- adversary-chain parallel of C-44 (OUTPUT DECLARATION CHAIN)", "Adversary defeat condition sub-component at each phase-entry adversary declaration site extending adversary block from two-part to three-part form -- adversary-block parallel of C-40 (OUTPUT DECLARATION labeled sub-components)"]}
```
