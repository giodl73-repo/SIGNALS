# crew-roles — Quest Score R20

## Rubric: v14 | Formula: aspirational_pass / 35 * 10 | 0.286 pts per PASS

---

## V-01 — Axis-L: Explicit Phase Mapping Table

**Axis hypothesis**: C-42(a) declared table eliminates inference requirement for phase placement.

### Essential / Recommended Gates

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | PASS | All 5 fields specified in FRAME FILL structure |
| C-02 | PASS | Inertia-advocate required, orientation = status-quo advocate |
| C-03 | PASS | `.roles/{domain}/` stated |
| C-04 | PASS | NON-GENERIC REQUIREMENT enforces domain-specific content |
| C-05 | PASS | CANDIDATE ROSTER minimum 5 (exceeds 3) |
| C-06 | PASS | lens.verify LENS AUDIT items are YES/NO testable checks |
| C-07 | PASS | collaborates_with (2-3 named roles); LENS AUDIT item 5 enforces inertia-advocate name |
| C-08 | PASS | PERSPECTIVE AUDIT requires >= 3 distinct perspectives |

### Aspirational Criteria (35)

| ID | Rating | Evidence |
|----|--------|----------|
| C-09 | PASS | INPUT INVENTORY table present; Row-ID, Source, Excerpt; >= 5 rows; EXIT GATE before STEP 2 |
| C-10 | PASS | "sole citation source for STEP 2 frame fill values — no field may cite the convergence summary or inertia baseline" |
| C-11 | PASS | EXIT GATE: "INPUT INVENTORY >= 5 rows" stated as exit condition |
| C-12 | PASS | S1/S2/S3 in `S{N}: "{exact phrase}"` format required |
| C-13 | PASS | G1/G2/G3 in `G{N}: "{exact phrase}"` format required |
| C-14 | PASS | CANDIDATE ROSTER table with S/G label column; inertia-advocate "defends S1 (and S2, S3)" |
| C-15 | PASS | FRAME FILL: all five fields; `Phase 1 source: {row-id} = "{verbatim phrase}"` citations required |
| C-16 | PASS | PLANNING TABLE: Role, Scope, Perspective, Planned-Vocab-Term, Gap/Strength |
| C-17 | PASS | SCOPE AUDIT: "< 2: fail, expand or reassign. >= 2: pass" — threshold + consequence present |
| C-18 | PASS | PERSPECTIVE AUDIT: "< 3: fail, add or reassign. >= 3: pass" — threshold + consequence present |
| C-19 | PASS | "WRITE INERTIA-ADVOCATE (first)" — labeled write instruction |
| C-20 | PASS | "Emit: INERTIA-ADVOCATE WRITTEN: {path}" stated |
| C-21 | PASS | LENS AUDIT block with all 6 check items per non-inertia role |
| C-22 | PASS | Item 1: "verify[1] domain-specific: YES/NO + evidence" |
| C-23 | PASS | Item 2: "verify[2] domain-specific: YES/NO + evidence" |
| C-24 | PASS | Item 3: "simplify[1] concrete cut: YES/NO + evidence" |
| C-25 | PASS | Item 4: "Planned-Vocab-Term verbatim: YES/NO + location" |
| C-26 | PASS | CHECK 1 per file with PASS/FAIL [missing field] emission |
| C-27 | PASS | CHECK 2: inertia-advocate orientation check |
| C-28 | PASS | CHECK 3A: scope spread >= 2 |
| C-29 | PASS | CHECK 3B: ROLE-REPLACE fires on mismatch |
| C-30 | PASS | CHECK 4A: all planning table roles written |
| C-31 | PASS | CHECK 4B: Planned-Vocab-Terms verbatim; ROLE-REPLACE fires |
| C-32 | PASS | CHECK 5A: written fields match frame fill per role |
| C-33 | PASS | CHECK 5B: citations verifiable against INPUT INVENTORY; per-violation emission |
| C-34 | PASS | CHECK 6: no generic placeholders |
| C-35 | PASS | CHECK 7: all files at `.roles/{domain}/` |
| C-36 | PASS | CHECK 8: perspective spread >= 3 |
| C-37 | PASS | INERTIA ANCHOR CHECK re-reads lens.verify; "Emit: INERTIA ANCHOR CHECK: PASS/FAIL"; FAIL triggers revision |
| C-38 | PASS | EARLY INERTIA ANCHOR CHECK: explicit PASS/FAIL label + "Remaining roles are blocked until EARLY INERTIA ANCHOR CHECK PASS" |
| C-39 | PASS | FRAME FILL PRE-ANCHOR CHECK in STEP 2 — maps to canonical Phase 4 via C-42(a) declared table; explicit label emitted; FAIL halts frame fill |
| C-40 | PASS | NON-GENERIC REQUIREMENT in STEP 1 — maps to canonical Phase 2 via C-42(a); operational def + negative-example list + NON-GENERIC CHECK PASS emission + EXIT GATE inclusion + back-ref "STEP 1 NON-GENERIC CHECK" |
| C-41 | PASS | LENS AUDIT item 6: "references INERTIA BASELINE term (S or G label + phrase): YES/NO + which term" per role; CROSS-ROLE SPREAD CHECK in STEP 4 with PASS/FAIL [N of M] emission |
| C-42 | PASS | C-42(a): explicit PHASE STRUCTURE MAPPING table at header; STEP 1=Phase 1+2, STEP 2=Phase 3+4, STEP 3=Phase 4+6, STEP 4=Phase 7; Phase 7 back-ref uses "STEP 1 NON-GENERIC CHECK" |
| C-43 | PASS | EARLY INERTIA ANCHOR CHECK: PASS→"proceed to remaining roles"; FAIL→"revise file and re-check before proceeding. Remaining roles are blocked until EARLY INERTIA ANCHOR CHECK PASS" |

**Aspirational score: 35/35 × 10 = 10.0**

---

## V-02 — Axis-M: Full Self-Routing Gates

**Axis hypothesis**: Extending dual-branch routing to every blocking gate makes the full prompt executor-complete.

### Essential / Recommended Gates: All PASS (same as V-01)

### Aspirational Criteria (35) — differences from V-01 noted

| ID | Rating | Evidence |
|----|--------|----------|
| C-09–C-16 | PASS | Identical content to V-01 baseline |
| C-17 | PASS | SCOPE AUDIT now self-routing: "SCOPE AUDIT: PASS — distinct Scope values >= 2. Proceed to PERSPECTIVE AUDIT. / FAIL — fewer than 2 distinct scopes; expand role set or reassign before re-running. Do not proceed while SCOPE AUDIT is FAIL." Exceeds criterion threshold |
| C-18 | PASS | PERSPECTIVE AUDIT now self-routing: PASS→"Proceed to write files"; FAIL→remediate + re-run. Exceeds criterion threshold |
| C-19–C-36 | PASS | Identical to V-01 |
| C-37 | PASS | INERTIA ANCHOR CHECK self-routing: PASS→"proceed to CROSS-ROLE SPREAD CHECK"; FAIL→"revise inertia-advocate and re-run CHECK 1, 5A, 5B before proceeding. Do not run CROSS-ROLE SPREAD CHECK while INERTIA ANCHOR CHECK is FAIL." |
| C-38 | PASS | EARLY INERTIA ANCHOR CHECK: PASS/FAIL label + blocking statement present |
| C-39 | PASS | FRAME FILL PRE-ANCHOR CHECK in STEP 2: positional inference unambiguous (C-42(b)); self-routing PASS→"proceed to fill remaining roles"; FAIL→remediate |
| C-40 | PASS | NON-GENERIC REQUIREMENT in STEP 1 alongside INERTIA BASELINE (C-42(b)); back-ref "STEP 1 NON-GENERIC CHECK" |
| C-41 | PASS | LENS AUDIT item 6 present per role; CROSS-ROLE SPREAD CHECK self-routing: PASS→"all verification complete. Proceed to close"; FAIL→remediate + re-run LENS AUDIT + re-run check |
| C-42 | PASS | C-42(b): positional inference unambiguous — FRAME FILL PRE-ANCHOR CHECK immediately after inertia-advocate FRAME FILL block before remaining-roles loop; NON-GENERIC REQUIREMENT in STEP 1 alongside baseline construction; back-ref names actual step |
| C-43 | PASS | EARLY INERTIA ANCHOR CHECK: PASS→"proceed to remaining roles"; FAIL→"revise inertia-advocate role file and re-run this check before proceeding. Remaining roles are blocked until EARLY INERTIA ANCHOR CHECK PASS." |

All 4 step EXIT GATEs are self-routing (STEP N EXIT: PASS→proceed; FAIL→remediate + do not start next step). This pattern is beyond any existing criterion requirement but contributes no negative scoring.

**Aspirational score: 35/35 × 10 = 10.0**

---

## V-03 — Axis-N: Baseline Propagation Map

**Axis hypothesis**: BASELINE PROPAGATION MAP pre-assigns S/G terms to roles at STEP 1, converting CROSS-ROLE SPREAD CHECK from scan to conformance.

### Essential / Recommended Gates: All PASS

### Aspirational Criteria (35) — differences from V-01 noted

| ID | Rating | Evidence |
|----|--------|----------|
| C-09 | PASS | INPUT INVENTORY present; exit gate now includes BASELINE PROPAGATION MAP condition (beyond criterion requirement) |
| C-10–C-15 | PASS | Identical to baseline |
| C-16–C-18 | PASS | SCOPE/PERSPECTIVE AUDIT: same single-branch format as baseline |
| C-19–C-36 | PASS | Identical to baseline |
| C-37 | PASS | INERTIA ANCHOR CHECK: "Emit: INERTIA ANCHOR CHECK: PASS/FAIL"; FAIL triggers revision |
| C-38 | PASS | EARLY INERTIA ANCHOR CHECK with explicit label and blocking |
| C-39 | PASS | FRAME FILL PRE-ANCHOR CHECK in STEP 2 (C-42(b) positional inference unambiguous) |
| C-40 | PASS | NON-GENERIC REQUIREMENT in STEP 1 (C-42(b)); back-ref "STEP 1 NON-GENERIC CHECK" |
| C-41 | PASS | LENS AUDIT item 6: "references INERTIA BASELINE term per PROPAGATION MAP assignment ({label}: {phrase}): YES/NO + which term" — conformance-based formulation. CROSS-ROLE SPREAD CHECK: "verify the assigned term from the BASELINE PROPAGATION MAP appears verbatim" — every non-inertia role checked against its contract, not just "at least one." Exceeds minimum C-41 requirement. |
| C-42 | PASS | C-42(b): positional inference unambiguous (same as baseline R19 V-02) |
| C-43 | PASS | EARLY INERTIA ANCHOR CHECK: PASS→"proceed to remaining roles"; FAIL→"revise file and re-check before proceeding. Remaining roles are blocked until EARLY INERTIA ANCHOR CHECK PASS." |

STEP 1 EXIT GATE in V-03 requires BASELINE PROPAGATION MAP complete (every G-term assigned). This strengthens C-41 enforcement at gate time but does not change any criterion score.

WRITE REMAINING ROLES in STEP 3 adds instruction: "b. Include the BASELINE PROPAGATION MAP assigned term verbatim in lens.verify." This pre-commits the LENS AUDIT item 6 check to a declared assignment rather than a scan.

**Aspirational score: 35/35 × 10 = 10.0**

---

## V-04 — Axis-L + Axis-M

**Axis hypothesis**: Declared phase structure (no inference required) + self-routing gates (no prose consultation required) produce a fully self-documenting audit chain.

### Essential / Recommended Gates: All PASS

### Aspirational Criteria (35)

| ID | Rating | Evidence |
|----|--------|----------|
| C-09–C-16 | PASS | Baseline content present |
| C-17 | PASS | SCOPE AUDIT self-routing (Axis-M): PASS→"distinct Scope values >= 2. Proceed to PERSPECTIVE AUDIT"; FAIL→"expand or reassign and re-run. Do not proceed while SCOPE AUDIT is FAIL." |
| C-18 | PASS | PERSPECTIVE AUDIT self-routing (Axis-M): PASS→"Proceed to write files"; FAIL→remediate + re-run |
| C-19–C-36 | PASS | All checks present |
| C-37 | PASS | INERTIA ANCHOR CHECK self-routing (Axis-M): PASS→"proceed to CROSS-ROLE SPREAD CHECK"; FAIL→"revise inertia-advocate and re-run CHECK 1, 5A, 5B. Do not run CROSS-ROLE SPREAD CHECK while INERTIA ANCHOR CHECK is FAIL." |
| C-38 | PASS | EARLY INERTIA ANCHOR CHECK with label and blocking |
| C-39 | PASS | FRAME FILL PRE-ANCHOR CHECK: C-42(a) resolves phase placement; self-routing PASS/FAIL branches present (Axis-M) |
| C-40 | PASS | NON-GENERIC REQUIREMENT: C-42(a) resolves phase placement; all content elements + back-ref "STEP 1 NON-GENERIC CHECK" |
| C-41 | PASS | LENS AUDIT item 6 per role; CROSS-ROLE SPREAD CHECK self-routing (Axis-M): PASS→"registry complete"; FAIL→"revise at least one non-inertia-advocate role…re-run that role's LENS AUDIT, and re-run CROSS-ROLE SPREAD CHECK" |
| C-42 | PASS | C-42(a): explicit PHASE STRUCTURE MAPPING table (same as V-01) |
| C-43 | PASS | EARLY INERTIA ANCHOR CHECK: PASS→"proceed to remaining roles"; FAIL→"revise inertia-advocate role file and re-run this check before proceeding. Remaining roles are blocked until EARLY INERTIA ANCHOR CHECK PASS." |

All 4 step EXIT GATEs: self-routing PASS/FAIL with explicit continuation and remediation routing.

**Aspirational score: 35/35 × 10 = 10.0**

---

## V-05 — Axis-L + Axis-M + Axis-N (Full Integration)

**Axis hypothesis**: Declared phase structure + self-routing gates + propagation contract produce maximum structural defensibility.

### Essential / Recommended Gates: All PASS

### Aspirational Criteria (35)

| ID | Rating | Evidence |
|----|--------|----------|
| C-09 | PASS | EXIT GATE PASS branch: "INPUT INVENTORY >= 5 rows AND INERTIA BASELINE complete AND NON-GENERIC CHECK PASS AND CONVERGENCE SUMMARY written AND BASELINE PROPAGATION MAP complete (every G-term assigned)." Threshold stated in PASS condition. |
| C-10–C-15 | PASS | All baseline content present |
| C-16 | PASS | PLANNING TABLE with all required columns |
| C-17 | PASS | SCOPE AUDIT self-routing (Axis-M) |
| C-18 | PASS | PERSPECTIVE AUDIT self-routing (Axis-M) |
| C-19–C-36 | PASS | All verification checks present |
| C-37 | PASS | INERTIA ANCHOR CHECK self-routing (Axis-M): PASS→"proceed to CROSS-ROLE SPREAD CHECK"; FAIL→remediate + do not run CROSS-ROLE SPREAD CHECK |
| C-38 | PASS | EARLY INERTIA ANCHOR CHECK with label and blocking |
| C-39 | PASS | FRAME FILL PRE-ANCHOR CHECK: C-42(a) resolves phase placement; self-routing branches present |
| C-40 | PASS | NON-GENERIC REQUIREMENT: C-42(a) resolves phase placement; all elements + back-ref "STEP 1 NON-GENERIC CHECK" |
| C-41 | PASS | LENS AUDIT item 6: "references INERTIA BASELINE term per PROPAGATION MAP assignment ({label}: {phrase}): YES/NO + which term" — conformance formulation. CROSS-ROLE SPREAD CHECK self-routing + conformance-based: PASS→"[N of M non-inertia roles satisfy propagation assignment, list all] — registry complete"; FAIL→"list failing roles — revise each failing role…re-run that role's LENS AUDIT, and re-run CROSS-ROLE SPREAD CHECK." Strongest C-41 implementation across all variations. |
| C-42 | PASS | C-42(a): explicit PHASE STRUCTURE MAPPING table at header |
| C-43 | PASS | EARLY INERTIA ANCHOR CHECK: PASS→"proceed to remaining roles"; FAIL→"revise inertia-advocate role file and re-run this check before proceeding. Remaining roles are blocked until EARLY INERTIA ANCHOR CHECK PASS." |

All 4 step EXIT GATEs self-routing. STEP 1 EXIT GATE includes BASELINE PROPAGATION MAP condition. STEP 2 EXIT GATE includes PROPAGATION MAP role names resolved condition.

**Aspirational score: 35/35 × 10 = 10.0**

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Score |
|-----------|-----------|-------------|--------------|-------|
| V-01 (Axis-L) | 5/5 PASS | 3/3 PASS | 35/35 | **10.0** |
| V-02 (Axis-M) | 5/5 PASS | 3/3 PASS | 35/35 | **10.0** |
| V-03 (Axis-N) | 5/5 PASS | 3/3 PASS | 35/35 | **10.0** |
| V-04 (Axis-L+M) | 5/5 PASS | 3/3 PASS | 35/35 | **10.0** |
| V-05 (Axis-L+M+N) | 5/5 PASS | 3/3 PASS | 35/35 | **10.0** |

---

## Ranking

All five variations tie at **10.0**. The rubric ceiling is reached by all. Secondary ranking by structural robustness (beyond minimum criterion requirements):

**Tier 1**: V-04, V-05 — Both eliminate C-42 inference ambiguity (C-42(a)) AND make all gates self-routing. V-04 is preferred for brevity; V-05 adds the propagation contract at density cost.

**Tier 2**: V-01, V-02, V-03 — Single-axis improvements each address one residual risk cleanly.

Within Tier 2: V-02 (Axis-M) offers the broadest execution-time protection by extending self-routing to every blocking gate; V-01 (Axis-L) offers the strongest C-42 auditability; V-03 (Axis-N) offers the strongest C-41 coverage.

**Recommended adoption**: V-04 — captures both R20 axis improvements without the density risk introduced by the Propagation Map. V-05 is the correct choice if C-41 failure mode (post-hoc cascade revision from baseline term omission) is empirically observed in execution.

---

## Excellence Signals

Two new patterns emerge from R20, neither captured by existing criteria, both candidates for v15:

**Pattern 1 — System-wide EXIT GATE self-routing** (V-02, V-04, V-05 / Axis-M):
Every blocking gate in the prompt (STEP 1–4 EXIT GATEs, SCOPE AUDIT, PERSPECTIVE AUDIT, INERTIA ANCHOR CHECK, CROSS-ROLE SPREAD CHECK) now emits an explicit PASS branch naming the continuation action and a FAIL branch naming the remediation action. An executor can resolve any gate result to its next action without reading surrounding prose. C-43 covers this pattern only for EARLY INERTIA ANCHOR CHECK. A criterion extending this requirement system-wide (candidate C-44) would close the execution ambiguity at every structural boundary, not just one.

**Pattern 2 — BASELINE PROPAGATION MAP as upfront assignment contract** (V-03, V-05 / Axis-N):
The PROPAGATION MAP constructed at the end of STEP 1 pre-commits each non-inertia role to a specific S/G baseline term before the CANDIDATE ROSTER is finalized. LENS AUDIT item 6 and CROSS-ROLE SPREAD CHECK shift from open-ended scan ("does any role reference a baseline term?") to conformance verification ("does each role carry its assigned term?"). The PASS emission in V-05 lists all satisfying roles; the FAIL emission lists all failing roles. This converts a binary gate into a role-level accountability report. A criterion requiring this contract pattern (candidate C-45) would prevent the C-41 failure mode — writing all roles before discovering none carry a baseline term — at the structural level rather than the detection level.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["System-wide EXIT GATE self-routing: every blocking gate emits PASS→continuation and FAIL→remediation branches, making the full prompt executor-complete without prose consultation (candidate C-44; currently C-43 covers EARLY INERTIA ANCHOR CHECK only)", "BASELINE PROPAGATION MAP as upfront assignment contract: pre-commits each non-inertia role to a named S/G baseline term at STEP 1, converting CROSS-ROLE SPREAD CHECK from post-hoc scan to per-role conformance verification with full-roster PASS/FAIL reporting (candidate C-45)"]}
```
