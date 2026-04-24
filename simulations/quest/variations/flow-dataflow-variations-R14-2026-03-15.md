Here are the 5 complete R14 variations targeting **C-25** and **C-26** in rubric v11:

---

## R14 Variation Summary

| Variation | Axis | Scenario | Key C-25/C-26 Mechanism |
|-----------|------|----------|------------------------|
| **V-01** | Single: C-25 scaffold subtable | Operations — retail replenishment ETL (3 roles) | STEP 0 split: Block A = stage-to-role assignment map; Block B = output table inventory. Assignment map precedes output declarations. |
| **V-02** | Single: FM-NN two-level contract | Finance — SaaS revenue recognition | FM-NN identifiers at prediction time only; resolved post-trace to LP-NN/NH-NN (CONFIRMED/EXONERATED/NEW). Resolution section is T-NN scaffold artifact. |
| **V-03** | Single: Consolidated post-trace resolution | Operations — cross-dock distribution | Inline stage acknowledgment (defer, do not resolve); full FM-NN resolution audit in dedicated post-trace Section 5. Enables cross-pipeline evidence revision. |
| **V-04** | Combined: C-25 + C-26, 3 roles | MDM sync (Commerce + Operations + Finance) | Stage assignment map in STEP 0-A; Commerce predicts FM-NN; Finance owns C-26 resolution section as audit authority. Role-separated resolution hypothesis. |
| **V-05** | Combined: FM-NN contract + scaffold authority | Finance — dual-write AR pipeline | R11 V-01 proven scaffold-first design with FM-NN register declared as T-01 foundational artifact. Every cross-table citation — including resolution section evidence — governed by T-NN scaffold contract. |

**Key structural decisions in R14:**

- **Two-level identifier discipline** (V-02, V-04, V-05): FM-NN prediction tokens never appear in Recovery Audit or Closure Gate — only LP-NN/NH-NN. This enforces C-26's contract that the prediction register is a hypothesis layer, not a designation layer.
- **Resolution section placement**: V-02/V-05 use a numbered section; V-03 explicitly defers inline acknowledgments to a post-trace audit to catch distributed failure modes; V-04 assigns resolution ownership to Finance.
- **C-25 guard**: both multi-role variations (V-01, V-04) use the Block A / Block B scaffold split so stage coverage is verified before output tables are committed.
