---
skill: trace-skill
rubric_version: v3
round: R3
date: 2026-03-17
top_score: 100
all_essential_pass: true
new_patterns: []
convergence: approaching (V-05 = 100, no new patterns)
---

# Quest:Score -- trace-skill Round 3 (Rubric v3)

**Skill**: `trace-skill` | **Rubric**: v3 (C-01 through C-14) | **Date**: 2026-03-17
**Entry state**: C-01 through C-08 reliably PASS (baseline = 90). Aspirationals C-09 through C-14 are the scoring frontier.

---

## Scoring Architecture

| Tier | Criteria | Total pts | Per criterion |
|------|----------|-----------|---------------|
| Essential | C-01 to C-05 | 60 | 12 |
| Recommended | C-06 to C-08 | 30 | 10 |
| Aspirational | C-09 to C-14 | 10 | 1.67 |

PASS = full credit (1.67). PARTIAL = half credit (0.83). FAIL or N/A = 0.

---

## Per-Variation Evaluation

### V-01 -- Lifecycle emphasis (targets C-10, C-11)

**Axis**: Two-sentence carry-forward confirmations at every phase boundary
("Step Xa complete. Produced: [named output]." / "Step Xb prerequisite satisfied. Step Xb is valid to begin.")
plus an explicit consolidated Gate-Clearance Summary block between Step 3c and Step 3d.

**Essential C-01 through C-08**: All PASS. V-01 adds enforcement overhead but does not alter structural phase requirements.

**Aspirational:**

| C | Result | Evidence |
|---|--------|----------|
| C-09 | PARTIAL | Ledger template unchanged. Better phase tracking marginally increases odds of specific observations, but V-01 adds no constraint prohibiting "as expected" cells. |
| C-10 | PASS | Two-sentence carry-forward ("Produced: [named output]" + "Step Xb prerequisite satisfied") forces the model to name the output before writing the confirmation. Directly satisfies the Schema 5 prerequisite + transition sentence confirming satisfaction requirement. |
| C-11 | PASS | Explicit consolidated Gate-Clearance Summary block placed between Step 3c and Step 3d ("G-1 PASS, G-2 PASS, G-3 PASS -- Step 3d is valid to begin"). Phase 4 entry already carries gate status in the base template. Both required locations covered. |
| C-12 | FAIL | V-01 adds no remediation loop structure. Base skill has "If FAIL: structural defect" language but no mandatory (1) remediation action, (2) re-check, (3) updated result record -- and no exemption notice requirement. |
| C-13 | PARTIAL | The carry-forward confirmation at end of prior step ("Step Xa complete. Produced: [named output]") improves traceability but is positioned at step close, not step open. C-13 requires each sub-step to open with "Prerequisite: [stated condition]. Check: YES -- [named artifact]." V-01's structure lacks the opening-checkbox format and fails the named-referent-at-opening requirement. |
| C-14 | N/A | C-12 FAIL -- C-14 not evaluable. |

**Aspirational total**: 0.83 + 1.67 + 1.67 + 0 + 0.83 + 0 = **5.00**
**Composite: 95.0** | All essential PASS | Golden: YES (>= 80, all essential pass)

---

### V-02 -- Output format: named-artifact prerequisite checkboxes (targets C-13)

**Axis**: Each Phase 3 sub-step opens with "Prerequisite: [stated condition]. Check: YES -- [named artifact or row]"
(or structurally equivalent). The YES resolution must name a specific artifact; a bare YES is treated as mechanical and fails.

**Essential C-01 through C-08**: All PASS.

**Aspirational:**

| C | Result | Evidence |
|---|--------|----------|
| C-09 | PARTIAL | Ledger template unchanged. Checkbox rigor may encourage specificity in observation cells but V-02 adds no "as expected is invalid" prohibition. |
| C-10 | PASS | The named-artifact checkbox opening each sub-step includes "Prerequisite: [condition]. Check: YES -- [named output from prior step]." This provides both the prerequisite declaration and the confirmation-with-referent that C-10 requires. |
| C-11 | PASS | The Step 3d opening checkbox reads: "Prerequisite: Step 3c all-PASS (G-1=PASS, G-2=PASS, G-3=PASS). Check: YES -- gate results at Step 3c above." This names all three gates and their results at the 3c->3d boundary -- satisfying C-11's consolidated entry-clearance summary requirement. Phase 4 entry gate status from base template covers the Phase 4 boundary. |
| C-12 | FAIL | V-02 adds no remediation loop structure or exemption notice. |
| C-13 | PASS | Directly targeted. "Prerequisite: [stated condition]. Check: YES -- [named artifact]" is the exact C-13 format. The requirement that YES resolution names a specific artifact (not bare YES) is the axis constraint. |
| C-14 | N/A | C-12 FAIL -- not evaluable. |

**Aspirational total**: 0.83 + 1.67 + 1.67 + 0 + 1.67 + 0 = **5.83**
**Composite: 95.8** | All essential PASS | Golden: YES

---

### V-03 -- Phrasing register: HALT/REMEDIATE with structured remediation loop (targets C-12, C-14)

**Axis**: Imperative HALT/REMEDIATE language at gate checks. When any gate FAIL: (1) HALT -- names the structural
defect, (2) REMEDIATE -- records what was added/changed/removed in Step 3b, (3) RE-CHECK -- re-runs the gate,
(4) records updated result. When all gates pass on first evaluation: explicit "C-12 EXEMPTION APPLIES" notice.

**Essential C-01 through C-08**: All PASS.

**Aspirational:**

| C | Result | Evidence |
|---|--------|----------|
| C-09 | PARTIAL | No change to ledger section. |
| C-10 | PARTIAL | HALT/REMEDIATE language improves gate-step clarity but does not add two-sentence carry-forward blocks with named outputs at phase boundaries. V-03 addresses remediation flow, not Schema 5 transition structure. |
| C-11 | PARTIAL | HALT/REMEDIATE structure at Step 3c produces gate results and a re-check summary as a by-product, which partially resembles a consolidated gate-clearance summary. However, the axis does not explicitly mandate a dedicated "G-1 PASS, G-2 PASS, G-3 PASS -- Phase 4 is valid to begin" block before Step 3d. A remediation summary names individual gates but is not the same as a dedicated phase-entry clearance block. |
| C-12 | PASS | Directly targeted. Structured remediation loop with all three required records: (1) remediation action, (2) re-check, (3) updated gate result. Exemption notice ("C-12 EXEMPTION APPLIES") when all gates pass on first evaluation satisfies the C-12 requirement that silence not confirm exemption. |
| C-13 | FAIL | No opening-checkpoint format added. |
| C-14 | PARTIAL | C-12 PASS, but C-11 only PARTIAL. Rubric: "a trace failing either C-11 or C-12 is not evaluated for C-14." C-11 is PARTIAL (a partial summary exists -- not exactly FAIL). C-14 is partially evaluable: the partial gate summary may or may not reflect post-remediation states. Scored PARTIAL. |

**Aspirational total**: 0.83 + 0.83 + 0.83 + 1.67 + 0 + 0.83 = **5.00**
**Composite: 95.0** | All essential PASS | Golden: YES

---

### V-04 -- Combined V-01 + V-02 (targets C-10, C-11, C-13)

**Axis**: Lifecycle emphasis (V-01's two-sentence carry-forward + explicit consolidated gate-clearance summary
between 3c and 3d) PLUS named-artifact prerequisite checkboxes opening each Phase 3 sub-step (V-02's format).

**Essential C-01 through C-08**: All PASS.

**Aspirational:**

| C | Result | Evidence |
|---|--------|----------|
| C-09 | PARTIAL | Neither V-01 nor V-02 prohibits "as expected" in the ledger. |
| C-10 | PASS | Dual enforcement: V-01's closing carry-forward names the step's output; V-02's opening checkpoint names the received artifact. Together they bracket every sub-step transition with named referents on both sides -- stronger structural guarantee than either alone. |
| C-11 | PASS | V-01's explicit structural block positioned between Step 3c and Step 3d (unambiguously before Step 3d begins) provides the consolidated gate-clearance summary. V-04 inherits this cleanly -- cleaner path than V-02's checkpoint-at-3d-opening approach. |
| C-12 | FAIL | Not addressed by either V-01 or V-02. |
| C-13 | PASS | V-02's named-artifact checkbox format. V-04 inherits cleanly. |
| C-14 | N/A | C-12 FAIL -- not evaluable. |

**Aspirational total**: 0.83 + 1.67 + 1.67 + 0 + 1.67 + 0 = **5.83**
**Composite: 95.8** | All essential PASS | Golden: YES

---

### V-05 -- Full aspirational integration (targets C-09 through C-14)

**Axis**: All four mechanisms combined plus additional constraints:
(a) compliance ledger with explicit "as expected is structurally invalid -- Observed behavior must name specific values, labels, or invariant results" prohibition (C-09);
(b) V-01's two-sentence carry-forward blocks (C-10);
(c) V-01's explicit consolidated gate-clearance summary at 3c->3d and Phase 4 boundaries (C-11);
(d) V-03's HALT/REMEDIATE structured remediation loop with C-12 exemption notice (C-12);
(e) V-02's named-artifact prerequisite checkboxes (C-13);
(f) explicit coherence directive: "if a C-12 remediation loop resolved a FAIL to PASS, the C-11 gate-clearance summary must reflect post-remediation states -- the initial FAIL must not appear in the Phase 4 entry summary" (C-14).

**Essential C-01 through C-08**: All PASS.

**Aspirational:**

| C | Result | Evidence |
|---|--------|----------|
| C-09 | PASS | Explicit anti-pattern prohibition ("as expected is structurally invalid") is a structural constraint in the skill body. Forces models to write specific labels, counts, or observed values in each VC row. Not satisfied by template alone -- V-05 adds the prohibition as a rule. |
| C-10 | PASS | V-01 component: two-sentence carry-forward at every phase boundary with named output and prerequisite confirmation. |
| C-11 | PASS | V-01 component: explicit consolidated Gate-Clearance Summary block positioned between Step 3c and Step 3d. Phase 4 gate status from base template. Both boundaries covered. |
| C-12 | PASS | V-03 component: HALT/REMEDIATE loop with three-part remediation record plus C-12 EXEMPTION APPLIES notice on first-pass success. Exemption notice is always present, never silent. |
| C-13 | PASS | V-02 component: opening checkbox per sub-step with "Check: YES -- [named artifact]." Named referent required; bare YES flagged as mechanical and structurally invalid. |
| C-14 | PASS | Both C-11 and C-12 PASS, making C-14 evaluable. Explicit coherence directive in the skill body: "the Phase 4 consolidated summary reads post-remediation gate states -- do not carry forward the initial FAIL result after remediation resolves it." Directive names the exact anti-pattern to avoid. |

**Aspirational total**: 1.67 x 6 = **10.0**
**Composite: 100** | All essential PASS | Golden: YES -- perfect score

---

## Leaderboard

| Rank | Variation | Composite | Essential | Aspirationals passing |
|------|-----------|-----------|-----------|----------------------|
| 1 | **V-05 (all)** | **100.0** | PASS | C-09, C-10, C-11, C-12, C-13, C-14 |
| 2 | **V-04 (C-10+C-11+C-13)** | **95.8** | PASS | C-10, C-11, C-13 (partial C-09) |
| 3 | **V-02 (C-13)** | **95.8** | PASS | C-10, C-11, C-13 (partial C-09) |
| 4 | **V-01 (C-10+C-11)** | **95.0** | PASS | C-10, C-11 (partial C-09, partial C-13) |
| 5 | **V-03 (C-12)** | **95.0** | PASS | C-12 (partial C-09, C-10, C-11, C-14) |

V-04 ranked above V-02 (same composite): dual enforcement of C-10/C-13 via both carry-forward and checkpoint
provides stronger structural confidence. V-01 ranked above V-03: two clean PASSes vs V-03's cascade of PARTIALs.

---

## Failure Patterns

| Pattern | Criteria | Variations affected | Diagnosis |
|---------|----------|---------------------|-----------|
| Compliance ledger generic entries | C-09 | V-01, V-02, V-03, V-04 | None of these variations prohibit "as expected" cells. C-09 is a skill gap: the base ledger template allows mechanical fill. Fix: add structural prohibition in the Verdict section. |
| Missing remediation loop | C-12 | V-01, V-02, V-04 | Single-axis lifecycle and checkbox variations don't address remediation flow. Without an explicit mandate, a trace that passes all three gates has no natural place to write the exemption notice. |
| C-14 not evaluable | C-14 | V-01, V-02, V-04 | C-14 is gated on both C-11 and C-12. Any variation missing C-12 automatically forfeits C-14. The criterion cannot be tested without the remediation loop infrastructure. |

---

## Excellence Signals (from V-05)

**XS-1 -- The "as expected" prohibition converts C-09 from PARTIAL to PASS.**
V-01 through V-04 all PARTIAL on C-09 because they trust the model to fill the ledger with specific values.
V-05's explicit structural constraint ("as expected is structurally invalid -- name specific values, labels, or
invariant results") removes model discretion. This is the single change that separates 95.8 from 100 across
the non-C-12 variations.

**XS-2 -- The C-12 exemption notice unlocks the C-14 coherence check.**
V-03 and V-05 demonstrate that C-12 is only achievable when the skill body explicitly mandates the exemption
path. Without the exemption notice, a trace where all gates pass has nothing to write for C-12, causing the
criterion to be silently skipped. The exemption notice transforms C-12 from a conditional criterion into an
always-present structural element.

**XS-3 -- Dual-bracket enforcement (V-04 pattern) is the most reliable path to C-10 + C-13 simultaneously.**
V-04 places carry-forward confirmation at step close (naming what was produced) and named-artifact checkpoint
at step open (naming what was received). The same artifact appears twice: once when written, once when verified.
This cross-reference chain makes mechanical compliance detectable. Promoted as a skill design principle
(not a new rubric criterion -- C-10 and C-13 already capture this separately).

---

## Summary Grid

|      | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | Score |
|------|------|------|------|------|------|------|-------|
| V-01 | P~   | PASS | PASS | FAIL | P~   | N/A  | 95.0  |
| V-02 | P~   | PASS | PASS | FAIL | PASS | N/A  | 95.8  |
| V-03 | P~   | P~   | P~   | PASS | FAIL | P~   | 95.0  |
| V-04 | P~   | PASS | PASS | FAIL | PASS | N/A  | 95.8  |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | **100** |

P~ = PARTIAL

---

## Convergence Assessment

**Round 3 status**: The rubric (v3) now has a perfect-scoring variation. V-05 = 100, all criteria C-01
through C-14 achievable in a single skill body design. No new excellence patterns emerge that require a C-15.

**Dual convergence check**:
- All essential criteria: PASS across all five variations. (condition 1: MET)
- New excellence patterns: none beyond what C-01 through C-14 already capture. (condition 2: MET)

**Recommendation**: Write V-05 as the candidate golden prompt. Run one additional verification round
(Round 4) across varied invocations (different topics, different gap compositions, different gate outcomes).
If V-05 scores 100 in Round 4 with no new patterns, declare dual convergence and write the golden prompt.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
