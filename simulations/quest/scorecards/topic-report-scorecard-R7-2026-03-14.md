## Round 7 Scorecard -- `topic-report`

**All 5 predictions confirmed.**

### Summary Rankings

| Rank | Variation | Aspirational | Score | Golden? |
|------|-----------|--------------|-------|---------|
| 1 | V-05 Ceiling | 17/17 | **100.0** | YES |
| 2 | V-04 Minimal golden | 16/17 | **99.4** | YES |
| 3 | V-01 C-23 only | 15/17 | **98.8** | YES |
| 3 | V-02 C-24 only | 15/17 | **98.8** | YES |
| 3 | V-03 C-25 only | 15/17 | **98.8** | YES |

### Per-Criterion Analysis

**Neutral base (14/17):** All C-01–C-22 pass. C-23, C-24, C-25 are the live discriminators.

**V-01 (C-23 YES):** `[RULE NEXT-CONCRETE C-21]` violation appends `(no stall cost -- C-21 violation)` — criterion ID embedded, failure mode criterion-recoverable. No G-9 register entry (C-24 FAIL). No Branch B header (C-25 FAIL).

**V-02 (C-24 YES):** G-9 INERTIA at register, propagated exactly to `[RULE G-9 INERTIA]` annotation — two-level chain for single-position invariant. Violation says `(-- G-9 violation)` naming the register label, not the rubric criterion ID, so C-23 FAIL. No Branch B header (C-25 FAIL).

**V-03 (C-25 YES):** `=== THREE-LAYER WRITE POINT (BRANCH B) ===` inside Branch B with independent LAYER 1/2/3. Model in Branch B reconstructs enforcement sequence locally — no cross-branch lookup. No criterion tag (C-23 FAIL). No G-9 register (C-24 FAIL).

**V-04 (C-23 + C-24):** Both annotation-level additions — criterion ID in violation text and G-9 register entry with label propagation — co-present at SLOT 4 without structural conflict. Two independent recovery chains: rubric recovery (C-21) and register recovery (G-9). No Branch B header (C-25 FAIL).

**V-05 (C-23 + C-24 + C-25):** All three pass. Dual-chain at SLOT 4 (G-9 + C-21), self-contained Branch B header. First 17/17 design.

### Excellence Signals

1. **Dual-chain at SLOT 4**: C-23 + C-24 co-present at same annotation position — G-9 recovers the register obligation, C-21 recovers the rubric criterion. Two independent recovery paths without structural conflict.
2. **Two-level chain is the correct treatment for single-position invariants**: G-9 INERTIA terminates at register + annotation (no scan) because there is no bidirectional constraint — structurally distinct from G-7a/G-7b three-level chains.
3. **C-25 closes the --format teams gap**: C-22 + C-25 together make both execution paths self-contained. No cross-branch lookup required at any point.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-23 embeds rubric criterion ID in violation text -- model traces from bad output to specific invariant without scanning the register", "C-24 establishes two-level chain (register to annotation) as the correct structural treatment for single-position invariants without pre-computation or scan steps -- G-9 INERTIA is the canonical instance", "C-25 Branch B independent THREE-LAYER header closes the cross-branch attention gap for --format teams execution -- together with C-22 both paths are self-contained"]}
```
ering the violation cannot recover the rubric invariant (C-21) from the tag alone |
| C-24 | Register-linked single-position invariant | PASS | G-9 INERTIA assigned as named contract register entry. Label propagated exactly to inline `[RULE G-9 INERTIA]` annotation at SLOT 4 -- two-level chain (register to annotation) established for a single-position invariant without a scan step |
| C-25 | Branch B independent THREE-LAYER header | FAIL | No Branch B THREE-LAYER WRITE POINT header. Branch B NEXT STEP section present but no independent enforcement layer enumeration |

**Aspirational**: 15/17 | **Score**: 60 + 30 + (15/17 * 10) = **98.8** | **Golden**: YES

**Mechanism isolated**: G-9 INERTIA at the register mirrors the G-7a/G-7b pattern for single-position invariants. The chain terminates at two levels (register, annotation) because there is no scan step for a single-position constraint -- correct structural treatment. The violation names the register label but not the rubric ID, so C-23 is absent.

---

#### V-03 -- C-25 only (Branch B independent header, no criterion tag, no G-9 register)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01--C-08 | All essential + recommended | PASS | Full foundation from neutral base |
| C-09--C-22 | All aspirational base | PASS | 14 criteria from neutral base unchanged |
| C-23 | Criterion-tagged violation | FAIL | Violation text names the output defect only -- "(no stall cost)" -- without naming the rubric criterion ID. Contrast-demonstrative but not criterion-traceable |
| C-24 | Register-linked single-position invariant | FAIL | No G-9 INERTIA register entry. NEXT STEP annotation not register-linked; locally correct label only |
| C-25 | Branch B independent THREE-LAYER header | PASS | Branch B contains `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header enumerating LAYER 1 DECLARE / LAYER 2 ANCHOR / LAYER 3 VERIFY independently of the Branch A header. A model executing Branch B reconstructs the enforcement sequence from this header alone -- no cross-branch reference required |

**Aspirational**: 15/17 | **Score**: 60 + 30 + (15/17 * 10) = **98.8** | **Golden**: YES

**Mechanism isolated**: Branch B header is a structural addition -- it duplicates the LAYER 1/2/3 enumeration locally so the Branch B execution path is self-contained. This addresses a different failure mode from C-22 (attention loss on the `--format teams` path) vs. the annotation-level mechanisms of C-23 and C-24.

**Discriminator note**: V-01, V-02, V-03 score identically at 15/17 = 98.8. All three new criteria are symmetric at design time -- none is structurally harder to satisfy than the others in isolation. Live-run variance will reveal which criterion addresses the most frequent actual failure mode.

---

#### V-04 -- C-23 + C-24 combined, R7 minimal golden candidate (C-25 NO)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01--C-08 | All essential + recommended | PASS | Full foundation from neutral base |
| C-09--C-22 | All aspirational base | PASS | 14 criteria from neutral base unchanged |
| C-23 | Criterion-tagged violation | PASS | Violation at SLOT 4 reads "(no stall cost -- C-21 violation)" -- criterion ID C-21 embedded, making the failure mode traceable to the rubric invariant at the exact governed position |
| C-24 | Register-linked single-position invariant | PASS | G-9 INERTIA at the contract register. `[RULE G-9 INERTIA]` annotation at SLOT 4 uses the exact register label -- two-level chain established. Register entry and annotation label are the same token |
| C-25 | Branch B independent THREE-LAYER header | FAIL | Branch B does not carry its own `=== THREE-LAYER WRITE POINT (BRANCH B) ===` header. C-22 header in Branch A present; Branch B model must cross-branch to recover the enforcement layer sequence |

**Aspirational**: 16/17 | **Score**: 60 + 30 + (16/17 * 10) = **99.4** | **Golden**: YES

**Design quality**: C-23 and C-24 are annotation-level additions -- each is a one-token change at SLOT 4 without new phases or structural additions. C-23 appends the rubric ID to the existing violation text; C-24 assigns G-9 INERTIA to the register and propagates the label to the annotation. Both sit within the existing SLOT 4 [RULE] construct. C-25 (Branch B header) is a structural addition requiring a new header block inside Branch B -- omitting it makes V-04 the minimum overhead path to 16/17.

**Interaction note**: C-23 and C-24 co-present at SLOT 4 without interference. The annotation `[RULE G-9 INERTIA]` carries the register label; the violation text `(no stall cost -- C-21 violation)` carries the rubric criterion ID. Two independent recovery chains at the same position: register recovery (G-9) and rubric recovery (C-21).

---

#### V-05 -- Ceiling: all three new criteria (C-23 YES, C-24 YES, C-25 YES)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01--C-08 | All essential + recommended | PASS | Full foundation from neutral base |
| C-09--C-22 | All aspirational base | PASS | 14 criteria from neutral base unchanged |
| C-23 | Criterion-tagged violation | PASS | Violation reads "(no stall cost -- C-21 violation)" -- C-21 embedded in violation text at SLOT 4 |
| C-24 | Register-linked single-position invariant | PASS | G-9 INERTIA at register, propagated to `[RULE G-9 INERTIA]` at SLOT 4 -- two-level chain for single-position invariant |
| C-25 | Branch B independent THREE-LAYER header | PASS | `=== THREE-LAYER WRITE POINT (BRANCH B) ===` within Branch B, LAYER 1/2/3 enumerated independently. Recovery note: "re-read this Branch B header to reconstruct the required layer sequence without referencing Branch A." Self-contained enforcement sequence for `--format teams` path |

**Aspirational**: 17/17 | **Score**: 60 + 30 + (17/17 * 10) = **100.0** | **Golden**: YES

**Design note -- C-23 + C-24 interaction**: The SLOT 4 annotation carries both G-9 (register label, C-24) and C-21 (rubric criterion ID, C-23) simultaneously. They serve different recovery paths: G-9 lets a model trace from annotation back to the contract register; C-21 lets a model trace from the violation back to the rubric invariant definition. Dual-chain at one position without structural conflict.

**Design note -- C-25 closure**: The Branch B THREE-LAYER header (C-25) + main-branch THREE-LAYER header (C-22) together close the attention-recovery gap for both execution paths. A model processing either branch reconstructs the enforcement sequence from a local header -- no cross-branch lookup required at any point.

---

### Prediction vs Actual

| Variation | Predicted | Actual | Match? |
|-----------|-----------|--------|--------|
| V-01 | 15/17 = 98.8 | 15/17 = 98.8 | YES |
| V-02 | 15/17 = 98.8 | 15/17 = 98.8 | YES |
| V-03 | 15/17 = 98.8 | 15/17 = 98.8 | YES |
| V-04 | 16/17 = 99.4 | 16/17 = 99.4 | YES |
| V-05 | 17/17 = 100 | 17/17 = 100 | YES |

All 5 predictions confirmed. C-23, C-24, and C-25 are symmetric at design time: each adds exactly one criterion to the base and none is structurally harder to satisfy alone. V-01, V-02, V-03 are equally tied at 15/17 -- only a live-run study would reveal which criterion has the highest compliance variance.

---

### Excellence Signals

**From V-05 (ceiling):**

1. **Dual-chain at SLOT 4 (C-23 + C-24 combined)**: `[RULE G-9 INERTIA]` annotation + violation `(no stall cost -- C-21 violation)` establish two independent recovery chains at the same position. G-9 recovers the register-level obligation; C-21 recovers the rubric-level criterion. A model at SLOT 4 has both chains available simultaneously without any cross-spec lookup.

2. **Correct structural class for single-position invariants (C-24)**: G-9 INERTIA terminates at two levels (register, annotation) because NEXT STEP has no pre-computation block or scan step. This is structurally distinct from G-7a/G-7b which chain three levels (register, annotation, scan header). C-24 vs C-19 is not a difference in depth -- it is a difference in invariant class. Single-position invariants require two-level chains; bidirectional list invariants require three-level chains.

3. **Branch B local recovery point closes the --format teams gap (C-25)**: With C-22 (main branch) + C-25 (Branch B) both present, no execution path requires a cross-branch lookup for enforcement layer sequence. The two headers are independent -- either path is self-contained. This is the structural completion of the attention-recovery pattern begun in R5 with C-22.

**From V-04 (minimal golden):**

4. **C-23 + C-24 at zero structural overhead**: Both are annotation-level additions to an existing SLOT 4 [RULE] construct. The entire 16/17 path adds one token to the violation text (criterion ID) and one register entry (G-9 INERTIA) + one label propagation. No new phases, no new branches, no new headers. Confirms that annotation-level chaining is the minimal mechanism for single-position invariant reliability.

---

### Round 7 Findings

1. **C-23, C-24, C-25 are symmetric at design time**: All three single-criterion variations score 15/17 = 98.8. No criterion is harder to implement alone than the others. Live-run variance data will reveal which is the harder compliance target in practice.

2. **V-04 is the R7 minimal golden**: C-23 + C-24 at annotation level with no structural additions. 16/17 = 99.4. Recommended production design for a team that wants maximum reliability gain at minimum spec overhead.

3. **V-05 closes all three dimensions simultaneously**: First design to achieve 17/17. The three new criteria address orthogonal failure modes -- criterion traceability (C-23), single-position invariant chaining (C-24), and cross-branch attention loss (C-25) -- and can be present in any combination.

4. **C-23 and C-24 are annotation peers, C-25 is structural**: C-23 and C-24 both modify the [RULE] annotation at SLOT 4 (one adds a rubric ID, one adds a register label). C-25 adds an entirely new header block inside Branch B. This asymmetry means C-25 is the only R7 criterion that requires structural editing vs. text-level editing.

5. **G-9 INERTIA establishes the single-position invariant pattern**: G-7a/G-7b chains three levels for list invariants. G-9 chains two levels for single-position invariants. Both patterns are now present in the spec. Any future single-position invariant (new SLOT, new output constraint) should follow the G-9 pattern: register entry + annotation label only, no scan step.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-23 embeds rubric criterion ID in violation text -- model traces from bad output to specific invariant without scanning the register", "C-24 establishes two-level chain (register to annotation) as the correct structural treatment for single-position invariants without pre-computation or scan steps -- G-9 INERTIA is the canonical instance", "C-25 Branch B independent THREE-LAYER header closes the cross-branch attention gap for --format teams execution -- together with C-22 both paths are self-contained"]}
```
