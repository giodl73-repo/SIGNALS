Written to `simulations/quest/golden/trace-skill-variate-R16-2026-03-15.md`.

---

## R16 Variations Summary

**Entry state**: R15 V-05 — C-01 through C-47 all PASS.

**Three variation axes explored**:

| Axis | What changes | Where |
|------|-------------|-------|
| V-01 | TCR row 5 carries `(C-47)` criterion citation in Component column | TCR only |
| V-02 | ANNOTATION SCOPE REGISTRY self-lists its own `Column name (TypeName)` as row 29; count gate = 29 | ASR + count gate |
| V-03 | SCORER HEURISTIC (C-43) names C-47 explicitly in step (b): "TCR row 5 (C-47) names the ANNOTATION SCOPE REGISTRY" | CONFORMANCE-COLLAPSE CLAIM only |

**Combined**:
- **V-04**: V-01 + V-02 — self-citing TCR row + self-complete registry (29 rows)
- **V-05**: V-01 + V-02 + V-03 — all three; SCORER HEURISTIC explicitly names C-47 as the lookup path for step (b) and (c)

**Excellence signal hypothesis** (potential C-48): The strongest discriminator in this round is likely V-05's SCORER HEURISTIC split of step (b) into "TCR rows 1-4 canonical" + "TCR row 5 (C-47) scope registry", making C-47 a named, cited confirmation step rather than an implied consequence of "rows 1-5". This parallels how C-45 upgraded the SCORER HEURISTIC label from anonymous to self-citing (`(C-43)`), and how C-39 required STRUCTURAL MANDATE headers to carry `(C-XX)`. V-02's self-complete registry (row 29) is the second candidate — a registry that omits its own typed column has a closed-world gap about itself.
