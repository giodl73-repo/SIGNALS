## Round 12 Scoring — `topic:status` vs Rubric v11

**Rubric:** v11 (max 245) | **Variants:** 5 | **Date:** 2026-03-15

---

### Structural Baseline

All five R12 variants are built on top of R11 245-scoring structure. The R12 axis is exclusively the interior of the `PHASE 2 OUTPUT DECLARATION` block — every criterion from C-01 through C-36 is inherited intact. C-37 and C-38 pass for all variants (the R12 design explicitly preserves these). I confirm each below in the tier-by-tier walkthrough, then focus variation analysis on the distinguishing features.

---

### Criterion Evaluation

#### Essential Tier (C-01–C-04) — all variants

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-01 | PASS | PASS | PASS | PASS | PASS | `Glob: simulations/**/{topic}-*` in PHASE 1; result assigned to `DISK_SIGNALS`; empty-set stop present |
| C-02 | PASS | PASS | PASS | PASS | PASS | `percent = VERIFIED count / PLANNED count * 100`; consistency guard on 100%+UNVERIFIED contradiction |
| C-03 | PASS | PASS | PASS | PASS | PASS | COMMIT RISK REGISTER lists per-planned-signal assertions; gap rows explicitly named by namespace+signal |
| C-04 | PASS | PASS | PASS | PASS | PASS | `Write no files.` preamble instruction; PHASE 4 `Write no files.` execution close; no file emission |

**Essential: 60/60 all variants.**

---

#### Recommended Tier (C-05–C-07) — all variants

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|------|------|------|------|------|----------|
| C-05 | PASS | PASS | PASS | PASS | PASS | COMMIT DECISION: `Readiness: READY \| PARTIAL \| NOT READY`; consequence-framed verdict present |
| C-06 | PASS | PASS | PASS | PASS | PASS | COMMIT RISK BY NAMESPACE table with all 9 rows; zero-rows display `0 \| 0 \| --` |
| C-07 | PASS | PASS | PASS | PASS | PASS | `strategy.md: [FOUND \| NOT FOUND -- if absent: ...]` template field; Exit A explicitly names the file |

**Recommended: 30/30 all variants.**

---

#### Aspirational Tier (C-08–C-12) — all variants

| ID | V-01–V-05 | Evidence |
|----|-----------|----------|
| C-08 | PASS | STALE EVIDENCE section with per-signal date and days-old annotation |
| C-09 | PASS | HIGHEST PRIORITY RISK section with concrete `/{namespace}:{signal} {topic}` skill invocation |
| C-10 | PASS | All 9 namespace rows in COMMIT RISK BY NAMESPACE; zero-value rows retained |
| C-11 | PASS | Named phases: SIGNAL ACQUISITION / PER-SIGNAL COMMITMENT ASSERTION / EXPOSURE COMPUTATION / DISPLAY GATE; DISPLAY GATE gates display on pre-display invariant check |
| C-12 | PASS | COMMIT RISK REGISTER precedes EXPOSURE SUMMARY in output template; ordering fixed in template |

**Aspirational: 25/25 all variants.**

---

#### Structural Tiers 2–9 (C-13–C-36) — all variants

These tiers are structurally identical across all five variants (same preamble, same output template, same layer labels, same execution phases). Spot-checking key criteria:

| ID | Pass evidence |
|----|---------------|
| C-13 | Three-layer sequence declared: preamble vocabulary coherence block [structural] → execution GUARD/assertion [semantic] → DISPLAY GATE [execution]; ordering stated as invariant |
| C-14 | `== OUTPUT TEMPLATE ==` block precedes `== EXECUTION PHASES ==`; column headers defined in template, not emitted ad-hoc |
| C-15 | `For each planned signal P: If P matches... VERIFIED Else UNVERIFIED`; `Assert each signal individually. No batch evaluation.` |
| C-16 | COMMIT DECISION: `Committing now means shipping without: {list}` — consequence-framed verdict naming specific missing items |
| C-17 | `[LAYER 1 -- STRUCTURAL: ...]`, `[LAYER 2 -- SEMANTIC: ...]`, `[LAYER 3 -- EXECUTION: ...]` labels at mechanism locations |
| C-18 | COMMIT RISK REGISTER table with VERIFIED/UNVERIFIED column headers in OUTPUT TEMPLATE section |
| C-19 | Section headers: COMMIT RISK REGISTER / COMMIT RISK BY NAMESPACE / EXPOSURE SUMMARY / COMMIT DECISION / STALE EVIDENCE / HIGHEST PRIORITY RISK — all consequence-domain |
| C-20 | `[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]` contains both required strings |
| C-21 | Phase names: SIGNAL ACQUISITION / PER-SIGNAL COMMITMENT ASSERTION / EXPOSURE COMPUTATION / DISPLAY GATE — all consequence vocabulary |
| C-22 | Exit A: `"No planned baseline -- commit exposure is unquantifiable."` — epistemic-consequence statement |
| C-23 | `PER-SIGNAL COMMITMENT ASSERTION` — granularity prefix + decision-stake noun phrase in phase name |
| C-24 | `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` uses full phase vocabulary |
| C-25 | `strategy.md: [FOUND \| NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]` — inline `if absent:` consequence in field format string |
| C-26 | `PER-SIGNAL` is leftmost token in assertion phase name |
| C-27 | Layer 2 label carries full `PER-SIGNAL COMMITMENT ASSERTION` form including granularity prefix |
| C-28 | Field annotation names `PER-SIGNAL COMMITMENT ASSERTION` as impaired phase (not generic `commit exposure`) |
| C-29 | STALE EVIDENCE annotation: `if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence` — phase-attributed with degraded-not-blocked verb |
| C-30 | PHASE 2 has distinct file-absent (Exit A) and topic-absent (Exit B) stops; Exit B explicitly stops before PHASE 3 |
| C-31 | Register row: `VERIFIED \| UNVERIFIED -- if absent: ships without this signal on commit` — per-row commit-consequence annotation |
| C-32 | `Exit A -- file absent:` and `Exit B -- topic not registered:` — distinct named identifiers at branch declaration site |
| C-33 | Preamble `-- Vocabulary coherence invariant --` block precedes guard; names PHASE 2 dual-axis exit property |
| C-34 | Preamble: `file-absent and topic-absent are structurally distinct stop conditions with distinct messages` — both axes named, triggers characterized, distinctness asserted |
| C-35 | Preamble trigger sentences: `File-absent trigger: strategy.md not present on disk`; `Topic-absent trigger: strategy.md present but {topic} has no registered planned signals` — dedicated per-axis sentences |
| C-36 | Invariant declared at: (1) preamble [C-34], (2) Exit A/Exit B at GUARD [C-32], (3) PHASE 2 OUTPUT DECLARATION [C-38 site] — three-site chain |

**Tiers 2–9: 120/120 all variants.**

---

#### Structural Tier 10 (C-37–C-38)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-37 | PASS | PASS | PASS | PASS | PASS |
| C-38 | PASS | PASS | PASS | PASS | PASS |

**C-37 evidence (all variants):**
- V-01/V-02/V-03 (execution-prose form): `Exit A -- file absent: fires when strategy.md does not exist on disk` / `Exit B -- topic not registered: fires when strategy.md present but {topic} has no registered planned signals` — each named exit carries inline trigger clause at the exit declaration site.
- V-04/V-05 (lifecycle contract form): GUARD block carries `Exit A -- file absent: fires when strategy.md does not exist on disk` and `Exit B -- topic not registered: fires when strategy.md present but {topic} has no registered planned signals` in the contract field — trigger characterization co-located with named exit at GUARD site.

**C-38 evidence (all variants):**
- V-01/V-02/V-03: `PHASE 2 OUTPUT DECLARATION:` block explicitly present within PHASE 2 execution body (not a COMMIT DECISION post-execution section, not a lifecycle phase definition header).
- V-04: `PHASE 2 OUTPUT DECLARATION:` appended within PHASE 2 execution section body, after the contract box but still within the PHASE 2 block.
- V-05: `+-- PHASE 2 OUTPUT DECLARATION -- dual-axis gate invariant ---------------+` elevated box structurally resident within the PHASE 2 execution section.

**Tier 10: 10/10 all variants.**

---

### Composite Scores

| Variant | Ess (60) | Rec (30) | Asp (25) | T2 (20) | T3 (15) | T4 (15) | T5 (15) | T6 (15) | T7 (15) | T8 (15) | T9 (10) | T10 (10) | Total |
|---------|----------|----------|----------|---------|---------|---------|---------|---------|---------|---------|---------|----------|-------|
| V-01 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | **245** |
| V-02 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | **245** |
| V-03 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | **245** |
| V-04 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | **245** |
| V-05 | 60 | 30 | 25 | 20 | 15 | 15 | 15 | 15 | 15 | 15 | 10 | 10 | **245** |

**All five variants: 245/245 under v11.** All essential criteria pass. C-39 and C-40 are not yet criteria — they are observable structural gaps, not scoreable properties under v11.

---

### Excellence Signals

**Ranking under v11:** All five variants tied at 245/245. Rank is indeterminate under current rubric. The excellence signals are the *observable structural differences* that score identically but represent genuinely distinct structural properties.

**Excellence Signal 1 — Per-axis trigger sentences within the OUTPUT DECLARATION (C-39 candidate)**

Observable gap: V-02 vs V-01.

V-01's `PHASE 2 OUTPUT DECLARATION` INVARIANT sub-component:
```
INVARIANT: Dual-axis gate -- file-absent and topic-absent exits are
  structurally distinct stop conditions with distinct messages.
  Trigger: file-absent fires when strategy.md does not exist on disk;
  topic-absent fires when strategy.md present but {topic} has no registered
  planned signals.
```

V-02's INVARIANT sub-component:
```
INVARIANT: Dual-axis gate -- file-absent and topic-absent exits are
  structurally distinct stop conditions with distinct messages.
```

The `Trigger:` sentence is present in V-01, absent in V-02. Both pass C-35 (preamble trigger sentences) and C-37 (GUARD-site trigger sentences). The OUTPUT DECLARATION is a structurally distinct third site where trigger characterization can be independently declared. V-02 confirms this is not implied by C-35 + C-37 co-presence: having trigger sentences at two sites does not propagate them to the third site automatically.

**Excellence Signal 2 — Labeled sub-components within the OUTPUT DECLARATION (C-40 candidate)**

Observable gap: V-03 vs V-01.

V-01's OUTPUT DECLARATION uses `INVARIANT:` and `OUTPUT FORM:` as named sub-component labels, making each declaration independently addressable. V-03's OUTPUT DECLARATION carries equivalent content but as undifferentiated prose with lowercase inline labels (`Dual-axis gate invariant:`, `Output form:`):
```
PHASE 2 OUTPUT DECLARATION:
    Dual-axis gate invariant: file-absent and topic-absent exits are structurally
    distinct stop conditions with distinct messages.
    ...
    Output form: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.
```

V-03 and V-01 score identically under v11. The structural gap: labeled sub-components (`INVARIANT:` / `OUTPUT FORM:`) vs. undifferentiated prose with lowercase prefixes. Labeled form makes each OUTPUT DECLARATION sub-component independently addressable and verifiable without parsing the surrounding prose. Extends the labeled-sub-structure pattern from C-17 (layer enforcement labels) into the OUTPUT DECLARATION interior.

**Orthogonality confirmed:** V-02 (C-40 PASS, C-39 FAIL) and V-03 (C-39 PASS, C-40 FAIL) both score 245/245 under v11. Neither implies the other. The structural gap is independently observable in each isolation test.

**Form-agnosticism:** V-04 (execution-prose with appended declaration) and V-05 (elevated titled box) both carry C-39 + C-40 structure and score identically to V-01. Consistent with R11's confirmation that C-37 and C-38 are form-agnostic.

---

### No Additional Excellence Signals

V-05's elevated titled box form adds a boxed demarcation to the OUTPUT DECLARATION sub-components:
```
+-- PHASE 2 OUTPUT DECLARATION -- dual-axis gate invariant ---------------+
| INVARIANT: ...                                                           |
| OUTPUT FORM: ...                                                         |
+--------------------------------------------------------------------------+
```

This is a presentation variant of C-40 (labeled sub-components), not a new structural property. Box demarcation makes independent verifiability visually stronger but carries no structural information beyond what inline `INVARIANT:` / `OUTPUT FORM:` labels already provide. Not a new excellence signal.

---

```json
{"top_score": 245, "all_essential_pass": true, "new_patterns": ["Per-axis trigger sentences within the PHASE 2 OUTPUT DECLARATION extending the trigger-characterization chain to a third structural site (preamble C-35, GUARD C-37, OUTPUT DECLARATION) -- present in V-01/V-03/V-04/V-05, withheld in V-02", "Labeled sub-components (INVARIANT: and OUTPUT FORM:) within the OUTPUT DECLARATION making each declaration independently addressable by name -- labeled form present in V-01/V-02/V-04/V-05, withheld as undifferentiated prose in V-03"]}
```
