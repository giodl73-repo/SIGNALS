Written to `simulations/quest/rubrics/review-design-variate-R13-2026-03-14.md`.

---

## Round 13 Variations — review-design

**Rubric**: v12 (C-01 through C-40, denominator 33)
**Baseline carried into all 5**: C-36 (Section-first BLOCK 2), C-37 (inline corrective actions), C-38 (Amendment Cost column), C-39 (Priority Rank column), C-40 (Preservation Principle declaration)

---

### Single-axis variations

**V-01 | Cross-block Cost Continuity — Priority Rank Derivation Formula**
BLOCK 5 carries an explicit 3-input point formula: BLOCK 0 Amendment Cost (H=3/M=2/L=1) + BLOCK 3 consensus (AGREE=+2) + reviewer count (+1 each). Priority Rank assignment becomes arithmetic-verifiable rather than qualitative. New feature candidate: a rank inconsistent with formula inputs is a structural violation.

**V-02 | Section-Anchored BLOCK 5**
Extends the Section-first column convention (C-36) from BLOCK 2 into BLOCK 5. Column order becomes `Section | Priority Rank | P1 Finding | Action | Re-run Scope`. New feature candidate: a Section value in BLOCK 5 that does not appear in any BLOCK 2 finding table indicates the amend plan is acting on an unreviewed design location — a cross-block traceability violation.

**V-03 | BLOCK 3 Consensus as BLOCK 5 Elevation Gate**
BLOCK 3 gains an Elevation Record sub-table (P1 Finding | Consensus Status = ELEVATED/BASELINE). BLOCK 5 carries a Consensus Elevation Rule: all ELEVATED findings SHALL receive lower Priority Rank integers than all BASELINE findings. New feature candidate: a non-consensus finding outranking a consensus finding fires a conformance signal.

---

### Combination variations

**V-04 | Declarative Constraint Register + Cost Continuity Formula**
Block headers shift to declarative output-framing ("This block produces…"). F-IDs shift from audit triggers ("fires when") to constraint-violation language ("CONSTRAINT VIOLATED: … Populate. Halt. (F-XX)"). V-01's derivation formula is also carried. Tests whether declarative register interacts with formula compliance differently than R12's imperative register (V-04).

**V-05 | Section-Anchored BLOCK 5 + Consensus Gate + Derivation Formula**
All three single-axis features converge: Section-first in both BLOCK 2 and BLOCK 5, BLOCK 3 Elevation Record feeding BLOCK 5 rank ordering, and explicit point formula within each tier. BLOCK 5 adds a Section Traceability rule as a named constraint. Tests whether three-axis coherence surfaces a novel enforcement class where the evidence chain from signal → finding → consensus → section → priority is fully traceable and mechanically verifiable.
