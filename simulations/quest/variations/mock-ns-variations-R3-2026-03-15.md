Written to `simulations/quest/golden/quest-variate-mock-ns-R3-2026-03-15.md`.

---

## Round 3: mock-ns Variations (V-01 through V-05)

### SPREAD-DESIGN PLAN

**Gap analysis from R2 retro-scores under v3:**

| V (R2) | Retro-score | Fails |
|--------|-------------|-------|
| V-04 | 100 | nothing -- dual-site language present, three-column table present |
| V-03 | ~98.6 | C-13 only (warning not in FIDELITY CONTEXT section) |
| V-01 | ~97.1 | C-13 only (same) |
| V-02 | ~94.3 | C-11, C-14 (auto), C-15 (bracket annotation) |

Round 3 is a **stability round**: C-14 and C-15 are technically reachable (R2 V-04 proves it), but only one variation reliably hits them. The goal is to produce 4–5 stable variations using three distinct C-14 enforcement mechanisms.

---

### V-01 — FLAG Site-Boundary Gate
**axis:** lifecycle-emphasis

**Mechanism:** S-4 *closes* with `FLAG IS FINAL. Do not modify FLAG after this emit.` (at-site finality declaration). A-1 *opens* with `FLAG was finalized in S-4. Do not re-derive it here.` (at-site entry prohibition). Both sites declare their own constraint; neither points ahead or backward generically.

Carries FIDELITY CONTEXT lead section (C-13) and three-column Exclusion table (C-15) from R2 best performers.

---

### V-02 — FLAG RESOLUTION BLOCK
**axis:** output-format

**Mechanism:** FLAG computation is wrapped in a delimited procedural block with explicit open/close markers and `STATUS: LOCKED` as the final line. Header step references "the FLAG RESOLUTION BLOCK" — it cannot silently recompute because there's a named artifact to retrieve from.

Also fixes R2 V-02's C-15 gap (bracket annotation → three-column table).

---

### V-03 — MUST NOT Prohibition Register
**axis:** phrasing-register

**Mechanism:** At compute site: `FLAG is final. MUST NOT modify after this emit. MUST NOT re-derive FLAG in any subsequent step.` At header site: `MUST NOT re-derive FLAG here. Copy verbatim from Step 4.` Upgrades from advisory ("do not") to mandatory ("MUST NOT") at both sites. Also applies MUST NOT to the exclusion row for register consistency.

---

### V-04 — Structural Gate + MUST NOT
**axes:** lifecycle-emphasis + phrasing-register

**Mechanism:** Named `-- S-4 GATE --` and `-- A-1 GATE --` annotations, both using MUST NOT. The gate is visually prominent and cannot be merged with surrounding prose. Strongest C-14 enforcement variation.

---

### V-05 — FLAG RESOLUTION BLOCK + FIDELITY CONTEXT + Inertia Framing
**axes:** output-format + inertia-framing

**Mechanism:** V-02's RESOLUTION BLOCK (C-14) + R2 V-04's FIDELITY CONTEXT lead section (C-13) + R2 V-05's inertia-cost pattern extended into the exclusion row and all three category warnings. The exclusion row names the cost: *"zero new signal, zero readiness advance."* Each fidelity warning has explicit `What you can trust / What you cannot trust / Inertia risk` structure.

---

### Round 4 candidate

V-04's structural gates + MUST NOT merged with V-05's inertia framing = three-axis combination. Main risk: prompt length. An editorial pass trimming redundancy without collapsing the gates is the natural next step.
