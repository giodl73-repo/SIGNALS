Saved to `simulations/quest/golden/corps-achievements-variate-R9-2026-03-17.md`.

---

## Variate R9 — corps-achievements (rubric v9)

**Basis**: V-05 R8 at 100 on rubric v8 (C-01--C-25). Round 9 targets the single new criterion: **C-26 — explicit lifecycle phase barrier language**.

---

### Variation Axes

| V | Axis | C-26 mechanism | Hypothesis |
|---|------|---------------|------------|
| V-01 | Lifecycle emphasis | Terse `STOP. Phase N complete. [C-26]` on its own line | Minimal viable seal — instruction-based, low overhead |
| V-02 | Output format | Pre-printed `--- PHASE N SEALED [C-26] ---` in the artifact template skeleton | Structural guarantee: model transcribes, cannot skip |
| V-03 | Phrasing register | Formal `PHASE N CLOSURE GATE [C-26]` with numbered sub-steps requiring output-set enumeration before proceeding | Verification-based: gate pass requires the model to count and declare Phase N outputs |
| V-04 | V-01 + V-02 | STOP declaration + pre-printed marker | Two independent layers; both must fail simultaneously to miss |
| V-05 | All three | STOP + pre-printed + closure gate | Belt-and-suspenders: each layer addresses a distinct C-26 failure mode |

---

### C-26 Failure Mode Coverage

| Failure Mode | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| Seal omitted entirely | Instruction dep. | Blocked (pre-printed) | Gate-required | Blocked | Blocked |
| Phase N+1 bleeds back retroactively | Declaration only | Structural only | Verified (output-set enumeration) | Partial | Verified |
| Seal present but [C-26] ref missing | Audit catches | Audit catches | Audit catches | Audit catches | Audit catches |
| Wrong phase sealed (order error) | Undetected | Undetected | Detected (closure gate counts items) | Undetected | Detected |

**Predicted top performer**: V-05 — three C-26 layers active. The structural audit gate in V-05 checks all six C-26 evidence points (2 STOP barriers + 2 pre-printed markers + 2 closure gate confirmations), making the seal the most auditable and tamper-resistant.

**Key discriminator V-04 vs V-05**: V-04 has the STOP instruction and pre-printed marker but no closure gate. V-05 adds sub-steps requiring the model to enumerate the Phase N output set before proceeding — directly addressing the retroactive reframing risk that C-26 targets.
