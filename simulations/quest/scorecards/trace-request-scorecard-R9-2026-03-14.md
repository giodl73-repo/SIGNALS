# Quest Score — trace-request | Round 9 | Rubric v8

> Trace artifact: placeholder. Scoring derived from variation descriptions as authoritative ground-truth.

---

## Round Summary

| Rank | Variation | Essential | Rec | Asp | Score | Golden? |
|------|-----------|-----------|-----|-----|-------|---------|
| 1 | V-03 Scope-gap Rem# propagation | 60/60 | 30/30 | 90/90 | **180/180** | YES |
| 1 | V-04 Vocabulary conformance gate | 60/60 | 30/30 | 90/90 | **180/180** | YES |
| 1 | V-05 Two-axis combination | 60/60 | 30/30 | 90/90 | **180/180** | YES |
| 4 | V-01 C-24 advisory | 60/60 | 30/30 | 85/90 | **175/180** | YES |
| 4 | V-02 C-25 advisory | 60/60 | 30/30 | 85/90 | **175/180** | YES |

---

## Regression Tests: C-24 and C-25 Load-Bearing Confirmed

Both new criteria confirmed at -5 each, non-cascading:

- **V-01 (C-24 FAIL):** Advisory table is insufficient. Gate integers present (C-22 PASS) but not derivable from a visible EC# x TRow# table. C-22 format contract and C-24 verifiability contract are orthogonal.
- **V-02 (C-25 FAIL):** Advisory scope enumeration table is insufficient. Re-walk findings present (C-11 PASS) but not preceded by a required structured table. C-11 discovery contract and C-25 exhaustiveness-surface contract are orthogonal.

---

## Excellence Signals

**ES-1 (V-03/V-05) — C-26a: Scope-gap Rem# three-way cross-link.** Every Gap?=Y row in Step 8a must cite a dedicated Rem# in Step 11 with exact scope string as Parameters. When the gap boundary is the same Seq# as the adversarial divergence or error origination boundary, the link Step 8a → Step 11 → Step 7/9 is fully traceable. Scope gap without Rem# citation is half an audit — the problem is named without committing to the fix string.

**ES-2 (V-04/V-05) — C-26b: Vocabulary conformance gate.** VT# assignment at Step 0 makes each committed term individually addressable. Step 3a produces a per-term conformance table; D=0 gate summary is required before Step 4. D > 0 triggers a correction cycle back to Step 3. Converts C-02's narrative forward-binding claim into a computable structural check.

**ES-3 (V-05 only) — C-27 design surface.** When both axes combine, the exact VT# scope string propagates across Step 3 Auth Check (verified by Step 3a), Step 8a Scope/Role Invoked, and Step 11 Permission Fix Parameters for the same Gap?=Y boundary. Full vocabulary coherence across scope declaration, scope audit, and scope remediation — not yet a criterion, but defines the next design surface.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["Scope-gap Rem# propagation closes the auth audit loop: every Gap?=Y row in the scope enumeration table must cite a dedicated Rem# in the Remediation Register with the exact scope string as Parameters, making the three-way cross-link Step 8a -> Step 11 -> Step 7/9 fully traceable and computable", "Vocabulary conformance gate converts C-02 forward-binding declaration into a structurally verifiable D=0 integer: VT# terms assigned at Step 0 are checked against Step 3 cells in a per-term table; D > 0 is a correction block, not a note"]}
```
