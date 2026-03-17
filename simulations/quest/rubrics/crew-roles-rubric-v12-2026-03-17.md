Reading the scorecard carefully before extracting patterns.

The scorecard shows two new axes, each a distinct structural mechanism:

- **V-01 / Axis-D**: S1/S2/S3 + G1/G2/G3 labels on INERTIA BASELINE entries; label+phrase required verbatim at every forward-reference; "Generic phrases do not constitute valid anchor terms" (blocks C-36 from being satisfied by accidental matches — Risk-1)
- **V-02 / Axis-E**: EARLY INERTIA ANCHOR CHECK fires as a blocking gate in Phase 6.1 immediately after writing the inertia-advocate role; Phase 7 check retained as confirmation (prevents late detection cascade revision — Risk-2)

Those are C-37 and C-38. Formula moves to `/30 * 10` (0.333 pts each).

---

```markdown
# crew-roles rubric — v12

## Changes from v11

Two new aspirational criteria extracted from R17 variations V-01 (Axis-D) and V-02
(Axis-E). Both address structural risks in the C-36 INERTIA BASELINE / INERTIA ANCHOR
CHECK mechanism introduced in v11.

**C-37 — INERTIA BASELINE labeled terms + label-prefixed verbatim propagation** (from
V-01 / Axis-D):
C-36 requires that INERTIA BASELINE records strengths and gaps and that at least one
verbatim strength term propagates to `lens.verify`. The risk (Risk-1: accidental verbatim
matching) is that a strength recorded as a generic phrase (e.g., "easy to use") can
accidentally satisfy the verbatim-match requirement without any intentional anchor
discipline. V-01 closes this by requiring INERTIA BASELINE to label each strength as
S1, S2, S3 … and each gap as G1, G2, G3 …, and by requiring that every forward-reference
to a strength or gap term include the label prefix verbatim (e.g., "S1: familiar
shortcut-key model" rather than "familiar shortcut-key model"). Generic unlabeled phrases
do not constitute valid anchor terms. The EXIT GATE for Phase 2 must verify that INERTIA
BASELINE contains at least S1 and G1 with both label and non-generic phrase. INERTIA
ANCHOR CHECK in Phase 7 must verify label-prefixed verbatim match (label + phrase, not
phrase alone).

**C-38 — EARLY INERTIA ANCHOR CHECK in Phase 6.1 as blocking gate** (from V-02 /
Axis-E):
C-36 places INERTIA ANCHOR CHECK in Phase 7. The risk (Risk-2: late detection requiring
cascade revision) is that a failed anchor check discovered in Phase 7 forces rewriting
roles already committed in Phase 6. V-02 closes this by adding an EARLY INERTIA ANCHOR
CHECK as a blocking gate immediately after STEP 6.1 writes the inertia-advocate role and
before STEP 6.2 begins writing remaining roles. If the inertia-advocate's `lens.verify`
does not contain at least one label-prefixed verbatim S-term from INERTIA BASELINE, Phase
6 halts and the inertia-advocate role must be revised before continuing. The Phase 7
INERTIA ANCHOR CHECK is retained as final confirmation across all written roles. Advancing
past Phase 6.1 without EARLY INERTIA ANCHOR CHECK PASS is a blocking error.

**Formula updated**: `aspirational_pass / 30 * 10` (was `/28`). Each full pass = 0.333 pts.

---

## Criteria (full table)

### Essential (5)
C-01 All 5 fields | C-02 Inertia-advocate present | C-03 Correct output path |
C-04 Domain specificity | C-05 Minimum 3 roles

### Recommended (3)
C-06 Lens actionability | C-07 Collaborates_with resolves | C-08 Perspective diversity

### Aspirational (30)

| ID | Criterion | Introduced |
|----|-----------|------------|
| C-09 | Scope gradient | v1 |
| C-10 | Inertia domain-grounded | v1 |
| C-11 | Vocabulary-forced-field | v2 / R1 |
| C-12 | INPUT INVENTORY phase | v3 / R2 |
| C-13 | Slot-level source citation | v3 / R2 |
| C-14 | Planning table before authoring | v3 / R2 |
| C-15 | CHECK 1 input completeness | v4 / R3 |
| C-16 | CHECK 2 inertia-advocate present | v4 / R3 |
| C-17 | CHECK 3A scope re-validation | v4 / R3 |
| C-18 | CHECK 3B vocab binding re-validation | v4 / R3 |
| C-19 | CHECK 4A scope post-write | v4 / R3 |
| C-20 | CHECK 4B vocab binding post-write | v4 / R3 |
| C-21 | CHECK 5 frame-slot match | v4 / R3 |
| C-22 | CHECK 6 output-path verification | v4 / R3 |
| C-23 | CHECK 7 file-count match | v5 / R5 |
| C-24 | Re-evaluation after role replacement | v6 / R7 |
| C-25 | Source citation in FRAME FILL output | v6 / R7 |
| C-26 | FRAME FILL gate blocks Phase 6 | v7 / R9 |
| C-27 | Forensic source-phrase tracing | v7 / R9 |
| C-28 | SCOPE AUDIT gate | v8 / R11 |
| C-29 | Gap-Addressed column in planning table | v8 / R11 |
| C-30 | Inertia-first gate | v9 / R13 |
| C-31 | Vocab binding column | v9 / R13 |
| C-32 | Inline LENS AUDIT | v9 / R13 |
| C-33 | PERSPECTIVE AUDIT + CHECK 8 re-validation | v10 / R15 |
| C-34 | Per-slot Phase 1 source + CHECK 5A/5B split | v10 / R15 |
| C-35 | ROLE-REPLACE sub-procedure (4 fields + CONFIRMED gate) | v10 / R15 |
| C-36 | INERTIA BASELINE artifact + INERTIA ANCHOR CHECK | v11 / R16 |
| C-37 | INERTIA BASELINE labeled terms + label-prefixed verbatim propagation | v12 / R17 |
| C-38 | EARLY INERTIA ANCHOR CHECK in Phase 6.1 as blocking gate | v12 / R17 |
```

---

Two criteria added. The progression is clean: C-36 (v11) established the INERTIA BASELINE mechanism; C-37 (v12) closes Risk-1 by requiring S/G labels that prevent accidental matching; C-38 (v12) closes Risk-2 by moving the first anchor check to Phase 6.1 before cascade revision becomes necessary.
