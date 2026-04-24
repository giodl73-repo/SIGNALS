## Round 12 Scorecard: topic-roadmap

### Scoring Formula
`score = aspirational_raw / 40 * 10`
(20 aspirational criteria C-09--C-28, 2 pts each)

---

## V-01 — Lexical Identity (C-27 only)

**Stack**: R10 V-04 base + column renamed to "Consequence if unchanged" + exit criterion updated to match. No preamble (C-28 deliberately absent).

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 | essential | PASS | Phase 2 inventory before Phase 6 proposals |
| C-02 | essential | PASS | Phase 4 delta before Phase 6 |
| C-03 | essential | PASS | Phase 6a/6b have ADD/REMOVE/REPRIORITIZE schema with Before/After/Evidence |
| C-04 | essential | PASS | Phase 7 PENDING CONFIRMATION block + "STOP HERE" instruction; strategy.md named as unmodified |
| C-05 | essential | PASS | Phase 2 requires all 9 namespaces with explicit null rows; Phase 6 same |
| C-06 | recommended | PASS | "If all verdicts are HOLDS: emit NULL_DELTA... Stop. Phase 6 does NOT open." |
| C-07 | recommended | PASS | Verdict Vocabulary block defines HIGH/MEDIUM/LOW with countable artifact thresholds |
| C-08 | recommended | PASS | "Consequence if unchanged" column in Phase 5 defeat assessment + Phase 6 proposals |

| Aspirational | Score | Evidence |
|-------------|-------|----------|
| C-09 | 2 | Phase 1 has full read-barrier with ENTRY CONDITION + hard isolation constraint |
| C-10 | 2 | Named SIGNAL READ-LOCK guard with bias labeled (confirmation bias, vocabulary contamination) |
| C-11 | 2 | INERTIA-GATE at Phase 5 entry + independently restated at Phase 6 entry |
| C-12 | 2 | "Consequence if unchanged" column in defeat assessment; preamble blocking absent here but exit criterion enforces |
| C-13 | 2 | Standalone Verdict Vocabulary block defines DEFEATED/HOLDS with forward paths |
| C-14 | 2 | Explicit date rule "NEW = artifact date > STRATEGY DATE" with named STRATEGY DATE field |
| C-15 | 2 | HIGH/MEDIUM/LOW with specific countable evidential criteria (2+/1/inference) |
| C-16 | 2 | All 7 null types present: 4 delta categories + ADDITIONS/REMOVALS/REPRIORITIZATIONS |
| C-17 | 1 | Per-phase bias annotations present at all guards; proposal tables lack "Bias blocked by guard" column |
| C-18 | 2 | WITHDRAW defined with row-level syntax; distinguished from NO and REVISED with explicit behavior |
| C-19 | 2 | Entry/exit conditions on all gated phases referencing phase numbers |
| C-20 | 2 | Every named guard carries inline bias label (PHASE-1-READ-BARRIER, SIGNAL READ-LOCK, INERTIA-GATE ×2, CONFIRMATION GATE, WRITE GUARD ×2) |
| C-21 | 2 | Site 1 at Phase 5 entry + Site 2 at Phase 6 entry with independent restatement of HOLDS exclusion |
| C-22 | 2 | RESTART ISOLATION clause explicitly prohibits re-reading files after interruption |
| C-23 | 2 | Standalone Verdict Vocabulary block with SECTION SCOPE declaring it contains "verdict definitions ONLY" |
| C-24 | 2 | Phase 1/Verdict Vocabulary/Phase 5/Phase 6 each have SECTION SCOPE explicitly excluding other mechanisms' content |
| C-25 | 2 | Phase 5 forward-references Verdict Vocabulary; explicit anti-duplication clause present |
| C-26 | 2 | Exit criterion: "exit blocked if any DEFEATED row has an empty 'Consequence if unchanged' field" |
| C-27 | 2 | Column header "Consequence if unchanged" = exit criterion field name "Consequence if unchanged" — lexically identical |
| C-28 | 1 | Exit criterion site present and self-contained; preamble site deliberately absent — single enforcement site only |

**Aspirational total: 38/40**
**Score: 9.50**

---

## V-02 — Dual-Site Blocking (C-28 only)

**Stack**: R10 V-04 base + CONSEQUENCE GATE preamble (Site 1) + exit criterion (Site 2). Column header deliberately kept as "Consequence if HOLDS" to isolate C-28.

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 | essential | PASS | Phase order preserved |
| C-02 | essential | PASS | Phase 4 before Phase 6 |
| C-03 | essential | PASS | Action-typed proposals with schema |
| C-04 | essential | PASS | Phase 7 STOP + PENDING CONFIRMATION |
| C-05 | essential | PASS | 9 namespaces with null rows |
| C-06 | recommended | PASS | NULL_DELTA present |
| C-07 | recommended | PASS | Confidence tiers in Verdict Vocabulary |
| C-08 | recommended | PARTIAL | Column present in defeat assessment as "Consequence if HOLDS" (different name); "Consequence if unchanged" in proposals |

(2/3 recommended pass — threshold met)

| Aspirational | Score | Evidence |
|-------------|-------|----------|
| C-09 | 2 | Phase 1 read-barrier with isolation constraint |
| C-10 | 2 | SIGNAL READ-LOCK named and bias-labeled |
| C-11 | 2 | Dual-site INERTIA-GATE |
| C-12 | 2 | Column "Consequence if HOLDS" present in defeat assessment; preamble CONSEQUENCE GATE enforces blocking concept |
| C-13 | 2 | Standalone Verdict Vocabulary block |
| C-14 | 2 | Explicit date rule + named STRATEGY DATE |
| C-15 | 2 | HIGH/MEDIUM/LOW with countable criteria |
| C-16 | 2 | All 7 null types present |
| C-17 | 1 | Phase-level annotations present; no "Bias blocked by guard" column in proposal tables |
| C-18 | 2 | WITHDRAW with row-level syntax and distinctions |
| C-19 | 2 | Entry/exit conditions on all gated phases |
| C-20 | 2 | All structural guards carry inline bias labels |
| C-21 | 2 | INERTIA-GATE dual-site with independent restatement |
| C-22 | 2 | RESTART ISOLATION clause present |
| C-23 | 2 | Standalone Verdict Vocabulary block with SECTION SCOPE |
| C-24 | 2 | All SECTION SCOPE declarations exclude other mechanisms' content |
| C-25 | 2 | Phase 5 forward-references Verdict Vocabulary with anti-duplication clause |
| C-26 | 2 | Exit criterion names "Consequence if unchanged" as advancement condition |
| C-27 | 1 | Column = "Consequence if HOLDS"; blocking sites and exit criterion = "Consequence if unchanged" — intent matches but lexical identity fails |
| C-28 | 2 | Preamble [Site 1]: "This rule is stated at this preamble site independently. It does not delegate to the Phase 5 exit criterion." Exit criterion [Site 2]: "stated at this exit criterion site independently. It does not delegate to the preamble above." Both self-contained |

**Aspirational total: 38/40**
**Score: 9.50**

---

## V-03 — C-27 + C-28 Combined, Minimal Base

**Stack**: Essential only. No C-21 (dual-site INERTIA-GATE), C-22 (restart isolation), C-23 (standalone verdict block), C-24 (spatial separation), C-25 (anti-duplication). C-27 + C-28 both target full pass.

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 | essential | PASS | Phase order preserved |
| C-02 | essential | PASS | Phase 4 before Phase 6 |
| C-03 | essential | PASS | Action-typed proposal schema |
| C-04 | essential | PASS | PENDING CONFIRMATION + STOP HERE |
| C-05 | essential | PASS | 9 namespaces with null rows |
| C-06 | recommended | PASS | NULL_DELTA conditional present |
| C-07 | recommended | FAIL | No confidence tier definitions — "Confidence" column present in Phase 6 but HIGH/MEDIUM/LOW with evidential criteria absent |
| C-08 | recommended | PASS | "Consequence if unchanged" column in both Phase 5 and Phase 6 |

(2/3 recommended pass — threshold met)

| Aspirational | Score | Evidence |
|-------------|-------|----------|
| C-09 | 2 | Phase 1 read-barrier with "DO NOT read" instruction and entry condition |
| C-10 | 2 | "SIGNAL READ-LOCK" named with bias annotation |
| C-11 | 2 | Phase 5 and Phase 6 both carry INERTIA-GATE labels |
| C-12 | 2 | "Consequence if unchanged" column in Phase 5 with CONSEQUENCE GATE preamble blocking |
| C-13 | 1 | HOLDS/DEFEATED paths implied by gate statement but no standalone semantic definitions; consequences stated only as phase routing |
| C-14 | 2 | Explicit date rule with named STRATEGY DATE field |
| C-15 | 0 | No HIGH/MEDIUM/LOW confidence tiers with evidential criteria |
| C-16 | 2 | All 4 delta category nulls + 3 proposal type nulls present |
| C-17 | 1 | Some per-phase bias annotations present; Phase 7 confirmation gate unlabeled; no "Bias blocked by guard" column in proposals |
| C-18 | 2 | WITHDRAW defined with syntax and distinction from NO/REVISED |
| C-19 | 2 | Entry/exit conditions present on all gated phases |
| C-20 | 1 | Phase 6 INERTIA-GATE has no bias label; Phase 7 confirmation gate has no formal guard or bias annotation; Phase 8 write guard absent |
| C-21 | 2 | Phase 5 INERTIA-GATE + Phase 6 "[INERTIA-GATE: HOLDS dimensions have no row and no path to this phase]" — independent restatement present |
| C-22 | 0 | No restart isolation clause; Phase 1 barrier covers first-run only |
| C-23 | 0 | No standalone Verdict Vocabulary block; verdict semantics distributed through phase framing |
| C-24 | 0 | C-22 (restart clause) and C-23 (verdict block) absent; three-mechanism spatial separation cannot be evaluated |
| C-25 | 0 | No standalone verdict block exists to reference or defer to |
| C-26 | 2 | Exit criterion: "exit blocked if any DEFEATED row has an empty 'Consequence if unchanged' field -- this blocking rule is stated at this exit criterion site independently" |
| C-27 | 2 | Column header "Consequence if unchanged" = exit criterion field name "Consequence if unchanged" |
| C-28 | 2 | Preamble CONSEQUENCE GATE [Site 1 of 2] self-contained + exit criterion [Site 2 of 2] self-contained; neither delegates to the other |

**Aspirational total: 29/40**
**Score: 7.25**

---

## V-04 — Full Stack + C-27 + C-28 (C-21 through C-28)

**Stack**: R10 V-04 (C-21–C-25) + C-27 (column renamed, exit criterion matches) + C-28 (formal CONSEQUENCE GATE preamble as Site 1; exit criterion as Site 2). Phase 5 SECTION SCOPE updated to declare "consequence blocking enforcement" within its scope.

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01–C-05 | essential | PASS (all) | Same as V-01 |
| C-06–C-08 | recommended | PASS (all) | Same as V-01 |

| Aspirational | Score | Evidence |
|-------------|-------|----------|
| C-09 | 2 | Full Phase 1 read-barrier with SECTION SCOPE, isolation constraint, entry condition |
| C-10 | 2 | SIGNAL READ-LOCK with formal guard label and bias |
| C-11 | 2 | Dual-site INERTIA-GATE |
| C-12 | 2 | "Consequence if unchanged" column in Phase 5 + CONSEQUENCE GATE preamble blocks advancement |
| C-13 | 2 | Standalone Verdict Vocabulary block with full DEFEATED/HOLDS definitions |
| C-14 | 2 | Explicit date rule + named STRATEGY DATE |
| C-15 | 2 | HIGH/MEDIUM/LOW with countable evidential criteria |
| C-16 | 2 | All 7 null types |
| C-17 | 1 | All guard-level annotations present; proposal tables lack "Bias blocked by guard" column |
| C-18 | 2 | WITHDRAW with row-level syntax and distinctions |
| C-19 | 2 | Entry/exit conditions on all gated phases |
| C-20 | 2 | Every named guard carries inline bias label including CONSEQUENCE GATE (new) |
| C-21 | 2 | INERTIA-GATE dual-site with independent restatement at Phase 6 |
| C-22 | 2 | RESTART ISOLATION clause prohibiting file re-read after interruption |
| C-23 | 2 | Standalone Verdict Vocabulary block with SECTION SCOPE |
| C-24 | 2 | SECTION SCOPE for Phase 5 explicitly includes "consequence blocking enforcement" as part of its scope — CONSEQUENCE GATE preamble inside Phase 5 does not contaminate Phase 1 or Verdict Vocabulary sections |
| C-25 | 2 | Phase 5 forward-references Verdict Vocabulary with anti-duplication clause |
| C-26 | 2 | Exit criterion names "Consequence if unchanged" as advancement condition |
| C-27 | 2 | Schema commitment + Phase 5 column + exit criterion all use "Consequence if unchanged" — lexically identical at all sites |
| C-28 | 2 | `[>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<]` formal guard before table + exit criterion [Site 2], each self-contained with explicit non-delegation statement |

**Aspirational total: 39/40**
**Score: 9.75**

---

## V-05 — Full Stack + C-27 + C-28 + Schema Pre-Commitment (Triple-Site)

**Stack**: V-04 base + CONTRACT annotation in Output Schema block pre-committing the column name "Consequence if unchanged" before any file is read. SECTION SCOPE annotations updated across Phase 1, Verdict Vocabulary, and Phase 5 to explicitly exclude schema contract content.

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01–C-05 | essential | PASS (all) | Same as V-04 |
| C-06–C-08 | recommended | PASS (all) | Same as V-04 |

| Aspirational | Score | Evidence |
|-------------|-------|----------|
| C-09 | 2 | Phase 1 SECTION SCOPE updated: "does not contain schema contract annotations" — read-barrier section remains clean |
| C-10 | 2 | SIGNAL READ-LOCK formal guard |
| C-11 | 2 | Dual-site INERTIA-GATE |
| C-12 | 2 | Column + preamble enforcement |
| C-13 | 2 | Standalone Verdict Vocabulary block; SECTION SCOPE now also explicitly excludes "schema contract annotations" |
| C-14 | 2 | Explicit date rule |
| C-15 | 2 | HIGH/MEDIUM/LOW tiers |
| C-16 | 2 | All 7 null types |
| C-17 | 1 | Proposal table missing "Bias blocked by guard" column |
| C-18 | 2 | WITHDRAW with full syntax |
| C-19 | 2 | Entry/exit conditions on all gated phases |
| C-20 | 2 | All structural guards bias-labeled |
| C-21 | 2 | INERTIA-GATE dual-site |
| C-22 | 2 | RESTART ISOLATION clause |
| C-23 | 2 | Standalone Verdict Vocabulary block |
| C-24 | 2 | Phase 5 SECTION SCOPE explicitly states "It does not contain schema contract annotations (those are in the Output Schema block)" — CONTRACT annotation is spatially contained within the Schema block scope and does not bleed into any mechanism section |
| C-25 | 2 | Anti-duplication clause in Phase 5 |
| C-26 | 2 | Exit criterion names field by exact canonical name |
| C-27 | 2 | Triple-site chain: Schema CONTRACT pre-commits "Consequence if unchanged" → Phase 5 column uses "Consequence if unchanged" → exit criterion names "Consequence if unchanged"; all three lexically identical and verifiable against the schema block alone |
| C-28 | 2 | Dual-site blocking: preamble [Site 1] + exit criterion [Site 2], each self-contained |

**Aspirational total: 39/40**
**Score: 9.75**

---

## Composite Ranking

| Rank | Variation | Aspir. | Score | C-27 | C-28 | Delta from R11 top |
|------|-----------|--------|-------|------|------|-------------------|
| 1 | V-04 | 39/40 | 9.75 | FULL | FULL | +0.25 |
| 1 | V-05 | 39/40 | 9.75 | FULL | FULL | +0.25 |
| 3 | V-01 | 38/40 | 9.50 | FULL | PARTIAL | — |
| 3 | V-02 | 38/40 | 9.50 | PARTIAL | FULL | — |
| 5 | V-03 | 29/40 | 7.25 | FULL | FULL | — |

---

## Excellence Signals (V-04 / V-05)

**What made V-04/V-05 the top variations:**

1. **Formal CONSEQUENCE GATE guard label** — C-28's preamble is formalized as `[>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<]` with bias label ("consequence-omission bias") and mechanism statement, matching the structural formalism of all other guards. This is what allows C-20 to remain at full pass despite the new preamble addition.

2. **SECTION SCOPE updated to include consequence blocking enforcement** — Phase 5's SECTION SCOPE declares "gate-exclusion text and consequence blocking enforcement ONLY," making the preamble's presence inside Phase 5 non-contaminating for C-24. The spatial separation test passes because the preamble is categorized correctly within Phase 5's declared scope.

3. **V-05 specific: Schema CONTRACT creates triple-site lexical identity** — The `[>> CONTRACT: <<]` annotation in the Output Schema block pre-commits the exact column name before any file is read. A scorer can identify a C-27 failure at the schema boundary without reading Phase 5 at all. This does not improve the score (C-27 and C-24 are already at 2 in V-04) but establishes a more robust verification surface.

**Persistent gap (all variations):** C-17 — proposal tables (Phase 6a and 6b) lack a "Bias blocked by guard" column. Adding this column to the proposal table schema would push any full-stack variation from 39/40 to 40/40.

---

```json
{"top_score": 9.75, "all_essential_pass": true, "new_patterns": ["CONSEQUENCE GATE formalized as named guard with [>> GUARD: CONSEQUENCE GATE [Site 1 of 2 -- table entry] <<] label and bias annotation, matching the structural formalism of all other guards and enabling C-20 full pass despite adding a new preamble site inside Phase 5", "Schema CONTRACT annotation pre-commits exact column name before any file is read, creating a triple-site lexical identity chain (Schema CONTRACT -> Phase 5 column -> exit criterion) where C-27 violations are detectable at the schema boundary without reading Phase 5"]}
```
