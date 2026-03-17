Two new criteria extracted and added. Here's what changed:

---

**C-47** — closes the gap above C-33  
C-33 requires the independence gate to *name* the sequential-treatment failure mode. The Round 16 PASS+ cluster (V-01/V-02/V-03) went further: they showed a concrete output example (`'3 rows, columns empty' reads as compliant — this is wrong`). Naming a failure is abstract; the example makes it recognizable by output inspection. V-04 and V-05 both name the failure mode (passing C-33) but provide no output example (missing C-47).

**C-48** — closes the gap above C-29  
C-29 requires a consequence column in the pipeline overview. V-02 and V-05 augmented this with `(→ PCR-NN)` citations — a Phase Consequence Registry where consequence definitions live at a stable ID, with the pipeline overview becoming a citation layer. This is C-23's insight (schema rows carry IDs for gate citation) applied to the consequence column: embedded prose creates a drift channel; a registry with IDs closes it.

**Denominator**: 38 → 40  
**Formula**: `aspirational_pass / 40 × 10`
