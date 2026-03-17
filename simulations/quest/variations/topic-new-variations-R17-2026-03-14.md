Here are the 5 complete Round 17 variations, targeting v15 (40 criteria, denominator 40).

---

## Variation Map

| ID | Axis | Core Change |
|----|------|-------------|
| **V-01** | C-47 as named FER-NN registry | Elevates the C-47 inline example into a pre-pipeline **FAILURE EXAMPLE REGISTRY** (FER-01, FER-02) with stable IDs; gate cites `FER-01` by reference, not by reproducing text; parallel registry architecture (IR / FER / PCR) makes all named failure modes auditable by ID |
| **V-02** | PCR temporal layering | Extends each PCR row to **Immediate / Downstream** consequence columns (mirrors C-20 in FIELD SCHEMA); C-47 satisfied by inline gate example rather than FER block — tests whether registry-free inline example suffices when the failure description is concrete enough |
| **V-03** | Inertia-first block order + expanded failure table | INERTIA REGISTER leads all pre-pipeline blocks with header: "These are the defaults this skill overrides. Every schema that follows exists to prevent these from applying"; C-47 expanded to a full **BEFORE/AFTER comparison table** showing the exact sequential-path output vs. independent-path output |
| **V-04** | Combined: FER-NN + PCR temporal layering | PCR-01 downstream effect cites FER-01 ("skip failure recognizable by FER-01 output inspection"); two independent paths reach the failure example — PCR path (via overview) and gate-instruction path (Phase 1 exit); redundant citation makes C-47 robust to single-path skips |
| **V-05** | Combined: V-03 inertia-first + imperative phrasing | Command-register phrasing throughout ("Stop. Before you write: read IR-01. Here is what wrong looks like."); BEFORE/AFTER comparison block from V-03 formatted as labeled states the model must explicitly distinguish before advancing |

**C-47 coverage**: V-01 uses FER-NN ID citation; V-02 uses inline prose; V-03 uses BEFORE/AFTER visual table; V-04 uses FER-NN + PCR cross-citation; V-05 uses BEFORE/AFTER + imperative framing.

**C-48 coverage**: All five variations have a named PHASE CONSEQUENCE REGISTRY with PCR-01 through PCR-04; pipeline overview consequence column carries `→ PCR-NN` IDs only — no embedded prose.

**Key diagnostic axis**: V-01 vs V-04 tests whether the cross-registry citation in PCR-01 (pointing to FER-01) adds measurable C-47 compliance over plain FER-NN citation. V-02 vs V-03 tests whether a structured BEFORE/AFTER table outperforms a prose failure description for independence gate compliance. V-05 isolates whether imperative phrasing combined with visual state comparison is the dominant factor.
