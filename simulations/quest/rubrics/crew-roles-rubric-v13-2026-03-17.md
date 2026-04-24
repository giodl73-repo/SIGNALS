Reading the scorecard for new structural mechanisms before writing.

Three new axes appear:

- **V-01 / Axis-G**: FRAME FILL PRE-ANCHOR CHECK in Phase 4 — fires after inertia-advocate FRAME FILL, before Phase 5/6. Converts Phase 6.1 EARLY ANCHOR CHECK from detection → confirmation.
- **V-02 / Axis-H**: NON-GENERIC REQUIREMENT block in Phase 2 with explicit operational definition + negative-example list + NON-GENERIC CHECK in EXIT GATE. Closes definitional ambiguity that allows "easy to use" to pass C-37.
- **V-03 / Axis-F**: 6th LENS AUDIT item per non-inertia role + CROSS-ROLE SPREAD CHECK in Phase 7. Prevents INERTIA BASELINE terms from being siloed in the inertia-advocate role only.

Those are C-39, C-40, C-41. Formula moves to `/33 * 10` (0.303 pts each).

---

```markdown
# crew-roles rubric — v13

## Changes from v12

Three new aspirational criteria extracted from R18 variations V-01 (Axis-G), V-02
(Axis-H), and V-03 (Axis-F). Each addresses a distinct residual risk in the INERTIA
BASELINE / INERTIA ANCHOR CHECK mechanism introduced in v11 and refined in v12.

**C-39 — FRAME FILL PRE-ANCHOR CHECK in Phase 4 as blocking gate** (from V-01 / Axis-G):
C-38 places EARLY INERTIA ANCHOR CHECK after STEP 6.1 writes the inertia-advocate role.
The residual risk (Risk-3: intra-Phase-6 cascade revision) is that anchor failure is
detected only after the full role text is committed in STEP 6.1, requiring rewriting an
already-authored role. Axis-G eliminates this final detection latency by adding a FRAME
FILL PRE-ANCHOR CHECK as a blocking gate in Phase 4, immediately after the
inertia-advocate's FRAME FILL block and before Phase 5 or Phase 6 begins. The check
verifies that the inertia-advocate's `lens.verify` draft contains at least one
label-prefixed verbatim S-term from INERTIA BASELINE (matching the "S{N}: {phrase}"
format required by C-37). If the check fails, Phase 4 halts and the FRAME FILL must be
revised before continuing. With Axis-G in place, the three-checkpoint chain reads:
Phase 4 FRAME FILL PRE-ANCHOR CHECK (detection) → Phase 6.1 EARLY INERTIA ANCHOR CHECK
(confirmation) → Phase 7 INERTIA ANCHOR CHECK (final validation). Advancing past Phase 4
inertia-advocate FRAME FILL without FRAME FILL PRE-ANCHOR CHECK PASS is a blocking error.

**C-40 — NON-GENERIC REQUIREMENT block with operational definition + NON-GENERIC CHECK
in Phase 2 EXIT GATE** (from V-02 / Axis-H):
C-37 requires INERTIA BASELINE to use non-generic phrases but does not operationally
define "non-generic," leaving the judgment subjective (Risk-4: definitional ambiguity —
"easy to use" may be accepted as domain-specific in some contexts). Axis-H closes this
by requiring a NON-GENERIC REQUIREMENT block in Phase 2 that states an explicit
operational definition of the form "a phrase is non-generic if and only if it contains
at least one noun or verb specific to this domain…" and provides a negative-example
list (e.g., "easy to use," "works well," "is fast"). A NON-GENERIC CHECK is added to
the Phase 2 EXIT GATE: each labeled S-term and G-term must individually satisfy the
operational definition before Phase 2 may close. Phase 7 INERTIA ANCHOR CHECK must
explicitly reference "as validated at Phase 2 NON-GENERIC CHECK" to confirm the
propagated phrase is the validated domain-specific term, not a post-hoc generic
substitute introduced during role authoring. Absence of the NON-GENERIC REQUIREMENT
block or failure of any term at the NON-GENERIC CHECK gate is a blocking error.

**C-41 — CROSS-ROLE BASELINE SPREAD: 6th LENS AUDIT item + Phase 7 CROSS-ROLE SPREAD
CHECK** (from V-03 / Axis-F):
C-36 through C-38 ensure the inertia-advocate role propagates INERTIA BASELINE terms
into its own `lens.verify`. The residual risk (Risk-5: baseline silo) is that baseline
terms remain confined to the inertia-advocate role and do not influence non-inertia
roles, weakening cross-role narrative coherence. Axis-F closes this by adding a 6th
LENS AUDIT item in STEP 6.2 for every non-inertia-advocate role: "references INERTIA
BASELINE term (S or G label + phrase): YES/NO + which term." A CROSS-ROLE SPREAD CHECK
is added in Phase 7 requiring that at least one non-inertia-advocate role references an
INERTIA BASELINE term (label + phrase) verbatim. Phase 4 FRAME FILL for non-inertia
roles includes advisory language to consider S/G term references. ROLE-REPLACE
re-evaluation must include CROSS-ROLE SPREAD CHECK. A role-set in which only the
inertia-advocate references INERTIA BASELINE terms fails Phase 7 CROSS-ROLE SPREAD
CHECK.

**Formula updated**: `aspirational_pass / 33 * 10` (was `/30`). Each full pass = 0.303 pts.

---

## Criteria (full table)

### Essential (5)
C-01 All 5 fields | C-02 Inertia-advocate present | C-03 Correct output path |
C-04 Domain specificity | C-05 Minimum 3 roles

### Recommended (3)
C-06 Lens actionability | C-07 Collaborates_with resolves | C-08 Perspective diversity

### Aspirational (33)

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
| C-25 | (v7 criterion — see prior rubric version) | v7 |
| C-26 | (v7 criterion — see prior rubric version) | v7 |
| C-27 | (v8 criterion — see prior rubric version) | v8 |
| C-28 | (v9 criterion — see prior rubric version) | v9 |
| C-29 | (v9 criterion — see prior rubric version) | v9 |
| C-30 | Inertia-first gate | v10 |
| C-31 | Vocab binding column | v10 |
| C-32 | Inline LENS AUDIT | v11 |
| C-33 | PERSPECTIVE AUDIT + CHECK 8 | v11 |
| C-34 | Per-slot Phase 1 source + CHECK 5A/5B | v11 |
| C-35 | ROLE-REPLACE sub-procedure | v11 |
| C-36 | INERTIA BASELINE artifact + Phase 7 INERTIA ANCHOR CHECK | v11 |
| C-37 | INERTIA BASELINE labeled terms + label-prefixed verbatim propagation | v12 / R17 |
| C-38 | EARLY INERTIA ANCHOR CHECK blocking gate after Phase 6.1 | v12 / R17 |
| C-39 | FRAME FILL PRE-ANCHOR CHECK blocking gate in Phase 4 | v13 / R18 |
| C-40 | NON-GENERIC REQUIREMENT block + NON-GENERIC CHECK in Phase 2 EXIT GATE | v13 / R18 |
| C-41 | CROSS-ROLE BASELINE SPREAD: 6th LENS AUDIT item + Phase 7 CROSS-ROLE SPREAD CHECK | v13 / R18 |
```

---

**Notes on v13:**

The three new criteria form a coherent risk-closure layer on top of v12:

- C-39 (Axis-G) moves anchor detection one phase earlier — from role-write to FRAME FILL. The detection point is now before any role text is committed.
- C-40 (Axis-H) makes "non-generic" machine-checkable by requiring an explicit operational definition with negative examples. Closes the subjective interpretation gap in C-37.
- C-41 (Axis-F) extends baseline propagation horizontally across all roles rather than vertically within the inertia-advocate only. The 6th LENS AUDIT item operationalizes this at the per-role level; CROSS-ROLE SPREAD CHECK enforces it at the role-set level.

The V-04 combination (Axis-G + Axis-H) is not a separate criterion — it is the additive effect of C-39 + C-40 together, where Phase 4 FRAME FILL PRE-ANCHOR CHECK explicitly references "as validated at Phase 2 EXIT GATE NON-GENERIC CHECK." No new criterion number is needed for the combination.
