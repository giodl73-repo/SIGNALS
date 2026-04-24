## Round 13 Scoring -- `topic:status` vs Rubric v12

**Result:** All five variants score **255/255** under v12. All essential criteria pass.

---

### Score Summary

| Variant | Axis | C-41 | C-42 | v12 Score |
|---------|------|------|------|-----------|
| V-01 | Min delta: C-41+C-42 in execution-prose form | PASS | PASS | **255** |
| V-02 | C-41 withheld -- adversary at PHASE 2 entry only | FAIL | PASS | **255** |
| V-03 | C-42 withheld -- PHASE 3 output declaration only | PASS | FAIL | **255** |
| V-04 | Lifecycle GUARD contract + prose-appended declarations | PASS | PASS | **255** |
| V-05 | Lifecycle + elevated titled blocks for both | PASS | PASS | **255** |

---

### Excellence Signals

**C-41 candidate** (V-01 vs V-02 gap): PHASE 3 OUTPUT DECLARATION block with `INVARIANT:` label + `Trigger:` sentence + `OUTPUT FORM:` label — structurally parallel to PHASE 2's OUTPUT DECLARATION (C-38/C-39/C-40), independently necessary as a second-phase mechanism. Present: V-01/V-03/V-04/V-05. Withheld: V-02.

**C-42 candidate** (V-01 vs V-03 gap): `ADVERSARY:` clause at PHASE 2 execution body entry naming inertia as what the phase defeats — extends adversary framing from output-template-only site (COMMIT DECISION, C-16) into execution phase body, creating a two-site adversary chain. C-16 presence does not imply C-42 presence. Present: V-01/V-02/V-04/V-05. Withheld: V-03.

**Orthogonality:** V-02 (C-42 without C-41) and V-03 (C-41 without C-42) score identically under v12, confirming independent necessity. Under a hypothetical v13 (5 pts each): V-01/V-04/V-05 → 265; V-02/V-03 → 260 (symmetric delta).

**Form-agnosticism confirmed:** V-04 (lifecycle contract) and V-05 (elevated titled blocks) score identically to V-01 — consistent with prior C-37/C-38/C-39/C-40 form-agnosticism.

---

```json
{"top_score": 255, "all_essential_pass": true, "new_patterns": ["PHASE 3 OUTPUT DECLARATION block within the PHASE 3 execution body -- carries INVARIANT: label (consistency guard assertion with Trigger: sentence) and OUTPUT FORM: label (percent, readiness verdict); extends the output-declaration-residency pattern from PHASE 2 to PHASE 3 as an independently necessary second-phase mechanism -- present in V-01/V-03/V-04/V-05, withheld in V-02", "ADVERSARY: clause at PHASE 2 execution body entry naming inertia as what the phase defeats -- extends adversary framing from output-template-only site (COMMIT DECISION, C-16) into the execution phase body, creating a two-site adversary chain; presence in execution body is not implied by presence in output template -- present in V-01/V-02/V-04/V-05, withheld in V-03"]}
```
QUISITION / PER-SIGNAL COMMITMENT ASSERTION / EXPOSURE COMPUTATION / DISPLAY GATE; DISPLAY GATE gates display on pre-display invariant check |
| C-12 | PASS | COMMIT RISK REGISTER precedes EXPOSURE SUMMARY in output template; ordering fixed in template |

**Aspirational: 25/25 all variants.**

---

#### Structural Tiers 2--9 (C-13--C-36) -- all variants

All five R13 variants carry identical preamble, output template, and structural annotation. Spot-check confirms criteria C-13 through C-36 pass across all variants:

| ID | Pass evidence |
|----|---------------|
| C-13 | Three-layer sequence: preamble vocabulary coherence block [structural] -> execution GUARD/assertion [semantic] -> DISPLAY GATE [execution]; ordering stated as invariant |
| C-14 | `== OUTPUT TEMPLATE ==` block precedes `== EXECUTION PHASES ==`; column headers defined in template |
| C-15 | `For each planned signal P: If P matches... VERIFIED Else UNVERIFIED`; `Assert each signal individually. No batch evaluation.` |
| C-16 | COMMIT DECISION: `Committing now means shipping without: {list}` -- consequence-framed verdict naming specific missing items |
| C-17 | `[LAYER 1 -- STRUCTURAL: ...]`, `[LAYER 2 -- SEMANTIC: ...]`, `[LAYER 3 -- EXECUTION: ...]` labels at mechanism locations |
| C-18 | COMMIT RISK REGISTER table with VERIFIED/UNVERIFIED column headers in OUTPUT TEMPLATE section |
| C-19 | Section headers: COMMIT RISK REGISTER / COMMIT RISK BY NAMESPACE / EXPOSURE SUMMARY / COMMIT DECISION / STALE EVIDENCE / HIGHEST PRIORITY RISK -- all consequence-domain |
| C-20 | `[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]` contains both required strings |
| C-21 | Phase names: SIGNAL ACQUISITION / PER-SIGNAL COMMITMENT ASSERTION / EXPOSURE COMPUTATION / DISPLAY GATE -- all consequence vocabulary |
| C-22 | Exit A: `"No planned baseline -- commit exposure is unquantifiable."` -- epistemic-consequence statement |
| C-23 | `PER-SIGNAL COMMITMENT ASSERTION` -- granularity prefix + decision-stake noun phrase in phase name |
| C-24 | `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` uses full phase vocabulary |
| C-25 | `strategy.md: [FOUND \| NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]` -- inline `if absent:` consequence |
| C-26 | `PER-SIGNAL` is leftmost token in assertion phase name |
| C-27 | Layer 2 label carries full `PER-SIGNAL COMMITMENT ASSERTION` form including granularity prefix |
| C-28 | Field annotation names `PER-SIGNAL COMMITMENT ASSERTION` as impaired phase |
| C-29 | STALE EVIDENCE annotation: `if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence` |
| C-30 | PHASE 2 has distinct file-absent (Exit A) and topic-absent (Exit B) stops; Exit B explicitly stops before PHASE 3 |
| C-31 | Register row: `VERIFIED \| UNVERIFIED -- if absent: ships without this signal on commit` -- per-row commit-consequence annotation |
| C-32 | `Exit A -- file absent:` and `Exit B -- topic not registered:` -- distinct named identifiers at branch declaration site |
| C-33 | Preamble `-- Vocabulary coherence invariant --` block precedes guard; names PHASE 2 dual-axis exit property |
| C-34 | Preamble: `file-absent and topic-absent are structurally distinct stop conditions with distinct messages` -- both axes named, triggers characterized, distinctness asserted |
| C-35 | Preamble trigger sentences: `File-absent trigger: strategy.md not present on disk`; `Topic-absent trigger: strategy.md present but {topic} has no registered planned signals` |
| C-36 | Invariant declared at three sites: (1) preamble [C-34], (2) Exit A/Exit B at GUARD [C-32], (3) PHASE 2 OUTPUT DECLARATION [C-38 site] |

**Tiers 2--9: 120/120 all variants.**

---

#### Structural Tier 10 (C-37--C-38) -- all variants

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-37 | PASS | PASS | PASS | PASS | PASS |
| C-38 | PASS | PASS | PASS | PASS | PASS |

**C-37 evidence (all variants):**
- V-01/V-02/V-03 (execution-prose form): `Exit A -- file absent: fires when strategy.md does not exist on disk` / `Exit B -- topic not registered: fires when strategy.md present but {topic} has no registered planned signals` -- each named exit carries inline trigger clause at the exit declaration site.
- V-04/V-05 (lifecycle contract form): GUARD block carries both named exits with `fires when...` trigger clauses in the contract field -- trigger characterization co-located with named exit at GUARD site.

**C-38 evidence (all variants):**
- V-01/V-02/V-03: `PHASE 2 OUTPUT DECLARATION:` block explicitly present within PHASE 2 execution body.
- V-04: `PHASE 2 OUTPUT DECLARATION:` appended within PHASE 2 execution section body, after the contract box but still within the PHASE 2 block.
- V-05: `+-- PHASE 2 OUTPUT DECLARATION -- dual-axis gate invariant ---------------+` elevated box structurally resident within the PHASE 2 execution section.

**Tier 10: 10/10 all variants.**

---

#### Structural Tier 11 (C-39--C-40) -- all variants

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-39 | PASS | PASS | PASS | PASS | PASS |
| C-40 | PASS | PASS | PASS | PASS | PASS |

**C-39 evidence (all variants):**
All five variants carry a `Trigger:` sentence within the INVARIANT sub-component of the PHASE 2 OUTPUT DECLARATION. The sentence characterizes both axes: `file-absent fires when strategy.md does not exist on disk; topic-absent fires when strategy.md present but {topic} has no registered planned signals.`
- V-01/V-02/V-03: execution-prose form -- `Trigger:` sentence indented within `INVARIANT:` sub-component.
- V-04: execution-prose appended form -- identical `Trigger:` sentence in PHASE 2 OUTPUT DECLARATION after contract box.
- V-05: elevated titled-box form -- `Trigger:` sentence inside `+-- PHASE 2 OUTPUT DECLARATION --+` box under `INVARIANT:` label.

**C-40 evidence (all variants):**
All five variants use `INVARIANT:` and `OUTPUT FORM:` as distinct labeled sub-components within the PHASE 2 OUTPUT DECLARATION.
- V-01/V-02/V-03: uppercase `INVARIANT:` / `OUTPUT FORM:` labels present at sub-component boundary.
- V-04: same labels present in prose-appended PHASE 2 OUTPUT DECLARATION.
- V-05: same labels present as named fields within the elevated titled box.

**Tier 11: 10/10 all variants.**

---

### Composite Scores

| Variant | Ess (60) | Rec (30) | Asp (25) | T2 (20) | T3 (15) | T4 (15) | T5 (15) | T6 (15) | T7 (15) | T8 (15) | T9 (10) | T10 (10) | T11 (10) | Total |
|---------|----------|----------|----------|---------|---------|---------|---------|---------|---------|---------|---------|----------|----------|-------|
| V-01 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | 10 | **255** |
| V-02 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | 10 | **255** |
| V-03 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | 10 | **255** |
| V-04 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | 10 | **255** |
| V-05 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | 10 | **255** |

**All five variants: 255/255 under v12.** All essential criteria pass. C-41 and C-42 are not yet criteria -- they are observable structural gaps, not scoreable properties under v12.

---

### Excellence Signals

**Ranking under v12:** All five variants tied at 255/255. Rank is indeterminate under the current rubric. The excellence signals are the observable structural differences that score identically but represent genuinely distinct structural properties.

---

**Excellence Signal 1 -- PHASE 3 OUTPUT DECLARATION with labeled sub-components and trigger characterization (C-41 candidate)**

Observable gap: V-01 vs V-02.

V-01's PHASE 3 execution body (after readiness thresholds):
```
PHASE 3 OUTPUT DECLARATION:
  INVARIANT: Consistency guard -- UNVERIFIED-non-empty and percent-100%
    contradiction halts computation before readiness verdict is issued.
    Trigger: guard fires when UNVERIFIED count > 0 and computed percent = 100%.
  OUTPUT FORM: percent (integer 0-100); readiness verdict
    (READY | PARTIAL | NOT READY).
```

V-02's PHASE 3 execution body ends at:
```
Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY
```

No OUTPUT DECLARATION, no INVARIANT: label, no Trigger: sentence, no OUTPUT FORM: label. The PHASE 3 execution body closes with the readiness threshold enumeration.

The `PHASE 3 OUTPUT DECLARATION:` block is structurally parallel to the PHASE 2 OUTPUT DECLARATION introduced by C-38: it is resident within the execution phase body (not in the output template), it carries `INVARIANT:` and `OUTPUT FORM:` labeled sub-components (parallel to C-40), and it carries a `Trigger:` sentence characterizing the guard condition (parallel to C-39). V-02 confirms that the PHASE 2 output declaration pattern does not propagate to PHASE 3 automatically -- C-41 is independently necessary as a second-phase mechanism.

Variants with C-41: V-01, V-03, V-04, V-05. Withheld in: V-02.
V-05 form: elevated `+-- PHASE 3 OUTPUT DECLARATION -- consistency guard invariant --+` titled box.

---

**Excellence Signal 2 -- ADVERSARY: clause at PHASE 2 execution body entry (C-42 candidate)**

Observable gap: V-01 vs V-03.

V-01's PHASE 2 execution body opens with:
```
ADVERSARY: inertia toward evidence-blind commits -- default when this phase
is skipped: each unverified signal ships without explicit assertion.
```

V-03's PHASE 2 execution body opens with:
```
Read simulations/strategy.md.
```

The ADVERSARY: clause is absent in V-03. Adversary framing exists in V-03 only at the COMMIT DECISION section of the output template (C-16 site: `PRIMARY ADVERSARY: commit without evidence`). The gap: COMMIT DECISION names the adversary for output display; PHASE 2's ADVERSARY: clause names what the execution phase itself defeats -- a two-site adversary chain rather than a single-site output-template framing. V-03 confirms that adversary framing in the output template does not imply adversary framing at the execution-phase-body site: C-42 is independently necessary as a second-site mechanism.

V-04 form: prose `ADVERSARY:` line within PHASE 2 execution body, below the contract box header.
V-05 form: elevated `+-- PHASE 2 ADVERSARY DECLARATION --+` titled box with ADVERSARY:, Trigger:, and Outcome-if-undefeated fields.

Variants with C-42: V-01, V-02, V-04, V-05. Withheld in: V-03.

---

**Orthogonality confirmed:**

V-02 has C-42 (ADVERSARY: at PHASE 2 entry) without C-41 (PHASE 3 OUTPUT DECLARATION). V-03 has C-41 without C-42. Both score 255/255 under v12 -- indistinguishable from each other and from V-01. Under a hypothetical v13 rubric extracting both criteria at 5 pts each:
- V-01/V-04/V-05: 265 (PASS both)
- V-02: 260 (FAIL C-41, PASS C-42)
- V-03: 260 (PASS C-41, FAIL C-42)

The symmetric delta confirms neither criterion implies the other.

---

**Form-agnosticism confirmed:**

V-04 (lifecycle GUARD contract boxes + prose-appended output declarations) and V-05 (elevated titled boxes for both new structures) carry both C-41 and C-42 and would score identically to V-01 under v13. Consistent with R11/R12 confirmation that the output-declaration-residency pattern (C-38), trigger-characterization pattern (C-39), and labeled-sub-component pattern (C-40) are form-agnostic across prose, lifecycle-contract, and titled-block presentation styles.

V-05 extension: The `+-- PHASE 2 ADVERSARY DECLARATION --+` block adds a `Trigger:` and `Outcome if undefeated:` field alongside the `ADVERSARY:` declaration -- a richer adversary block structure with trigger characterization mirroring the OUTPUT DECLARATION interior pattern. This is a potential C-43 candidate (adversary block with trigger sentence at execution-phase site), not a new excellence signal extractable from the current variant set alone (V-04's single-line ADVERSARY: prose and V-05's titled block both satisfy C-42 -- the richer interior structure of V-05 is not isolated by any V-04 vs V-05 gap under v12).

---

### No Additional Excellence Signals

V-04's lifecycle contract form (INPUT/GUARD/OUTPUT fields for all four phases) and V-05's elevated titled boxes add presentation structure but no new observable structural gaps beyond C-41 and C-42. All properties present in V-04 and V-05 that are absent in V-01 are either presentation variants of already-extracted criteria or are structural extensions that require an additional isolation test (V-05 adversary block interior vs V-04 single-line adversary) not yet probed in this round.

---

```json
{"top_score": 255, "all_essential_pass": true, "new_patterns": ["PHASE 3 OUTPUT DECLARATION block within the PHASE 3 execution body -- carries INVARIANT: label (consistency guard assertion with Trigger: sentence) and OUTPUT FORM: label (percent, readiness verdict); extends the output-declaration-residency pattern from PHASE 2 to PHASE 3 as an independently necessary second-phase mechanism -- present in V-01/V-03/V-04/V-05, withheld in V-02", "ADVERSARY: clause at PHASE 2 execution body entry naming inertia as what the phase defeats -- extends adversary framing from output-template-only site (COMMIT DECISION, C-16) into the execution phase body, creating a two-site adversary chain; presence in execution body is not implied by presence in output template -- present in V-01/V-02/V-04/V-05, withheld in V-03"]}
```
