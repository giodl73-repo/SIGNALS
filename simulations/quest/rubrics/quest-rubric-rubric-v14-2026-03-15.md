Here is the complete v14 rubric:

---

## quest-rubric Rubric v14

**Formula:** `(E/5 × 60) + (R/3 × 30) + (A/32 × 10)` — denominator /30 → /32

---

### Essential criteria (C-01–C-05) — carried from earlier rounds

Binary pass/fail. A single essential FAIL floors the score regardless of E/R/A components.

*(C-01 through C-05 text preserved verbatim from prior versions.)*

---

### Recommended criteria (C-06–C-08) — carried from earlier rounds

PARTIAL on a recommended criterion scores 0.5.

*(C-06 through C-08 text preserved verbatim from prior versions.)*

---

### Aspirational criteria (C-09–C-22) — carried from earlier rounds

*(C-09 through C-22 text preserved verbatim from prior versions.)*

---

### Round 7–11 criteria (C-23–C-35) — carried forward

*(C-23–C-28 and C-30, C-32, C-34–C-35 text preserved verbatim; C-29, C-31, C-33 text shown in v13 file.)*

---

### Three criteria from Round 12 (C-36–C-38) — carried forward

*(Full criterion text preserved verbatim from v13.)*

---

### Two criteria from Round 13 excellence signals

Both target **DFM traceability** — the structural property that the pre-role DFM block required by C-38 propagates into the construction phase (C-39) and forward into the emitted artifact (C-40), rather than remaining a local orientation block.

---

**C-39 — Scope Gatekeeper cross-reference to DFM block**

*Source signal: ES-R13-1 / V-03.*

V-03's Scope Gatekeeper threshold escalation prohibition contains: *"This prohibition is the primary defense against the Dominant Failure Mode named in the pre-role block above."* This creates a cross-role coupling: the in-role prohibition derives its rationale from the named pre-role block, making the DFM block's removal detectable at the construction gate most directly responsible for the failure mode it describes. C-38 requires the DFM block to exist; C-39 requires it to be cited by downstream construction roles. A DFM block never cited by any construction role can be removed without breaking any gate — the cross-reference closes that window.

**Criterion:** The Scope Gatekeeper's threshold escalation prohibition explicitly names the pre-role DFM block as the threat it defends against. The cross-reference must appear in the prohibition text itself (not as an outside annotation or comment). The naming must be specific: "the failure mode described above" does not pass; the DFM block must be identified by its structural label (e.g., "Dominant Failure Mode" or the name the block uses).

**PARTIAL condition:** The Scope Gatekeeper references the failure mode concept by content description but does not name the pre-role block itself as the structural source.

**Independence from C-38:** C-38 tests DFM block existence at the pre-role position. C-39 tests whether the block is cited by name at the threshold escalation gate. V-02 baseline demonstrates PASS C-38 / FAIL C-39 (DFM block present, no Scope Gatekeeper cross-reference).

---

**C-40 — Output instruction DFM propagation to emitted artifact**

*Source signal: ES-R13-2 / V-03.*

V-03's output instruction says: *"purpose statement (2-3 sentences, including reference to the Dominant Failure Mode named in the pre-role block)"*. This propagates the DFM from ephemeral construction-phase context into the permanent artifact record. Without this requirement, the DFM block's influence is local to the construction phase: it orients the roles but leaves no trace in the emitted rubric. A rubric reader navigating the artifact has no indication that a construction-time calibration anchor exists.

**Criterion:** The output instruction (or equivalent emit-phase directive) explicitly requires the emitted rubric's purpose statement to name the DFM block. "Name" means: the purpose statement must carry the failure mode's label as it appears in the pre-role DFM block — not a paraphrase. A purpose statement describing the concept without using the block's specific label does not satisfy this criterion.

**PARTIAL condition:** The output instruction requires the purpose statement to reference the DFM concept but does not require use of the block's specific label; paraphrase reference is permitted but structural linkage is implicit rather than explicit.

**Independence from C-38:** C-38 tests DFM block existence; C-40 tests whether the block's label is carried into the emitted artifact's purpose statement. V-02 baseline demonstrates PASS C-38 / FAIL C-40.

**Independence from C-39:** C-39 tests propagation to the Scope Gatekeeper (construction phase); C-40 tests propagation to the emitted artifact (output phase). The two paths are orthogonal.

---

### Scoring

```
Essential:    (sum of essential values) / 5 × 60      max 60
Recommended:  (sum of recommended values) / 3 × 30    max 30
Aspirational: (sum of aspirational values) / 32 × 10  max 10
Composite = Essential + Recommended + Aspirational    max 100
```

**Essential floor:** single essential FAIL → score = 0.  
**Golden threshold:** all essential PASS AND composite ≥ 90.  
**Aspirational denominator:** /32 (C-09–C-40 = 27 prior + C-36/37/38 from R12 + C-39/40 from R13).

---

Saved to `simulations/quest/rubrics/quest-rubric-rubric-v14-2026-03-16.md`.

**What was extracted and why:**

| New criterion | Source signal | Pattern | What C-38 doesn't cover |
|---|---|---|---|
| **C-39** | ES-R13-1 / V-03 | Scope Gatekeeper cites DFM block by label | C-38 tests presence; C-39 tests that the block is *cited at the construction gate it defends* |
| **C-40** | ES-R13-2 / V-03 | Output instruction requires purpose statement to name DFM label | C-38 tests pre-role block presence; C-40 tests *artifact-level propagation* |

V-03 is the only variation that achieves 100.0 in R13. Both C-39 and C-40 are structural choices present in V-03 and absent in all other variations — the round confirms them as independent observable properties beyond C-38's base requirement.
