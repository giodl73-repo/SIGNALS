Written to `simulations/quest/golden/quest-rubric-variate-v17-R17-2026-03-16.md`.

---

## quest-rubric Variate — Round 17

**Target criteria:** C-45 (per-quotation in-gate failure-mode argument) and C-46 (criterion-indexed competitor architecture). Denominator /38.

---

### Variation Map

| Variation | Axis | C-45 | C-46 | Design |
|-----------|------|------|------|--------|
| **V-01** | Role sequence | **Strong** — Phase 8.5 notes gain failure-mode argument clause ("if this path absent, X passes unchallenged") | Ablated — STATUS QUO foil items generic, no criterion IDs | Single-axis isolation for C-45 |
| **V-02** | Inertia framing | Ablated — Phase 8.5 notes name path + phase only | **Strong** — STATUS QUO foil items named "C-43 failure" and "C-44 failure" at criterion-class precision | Single-axis isolation for C-46 |
| **V-03** | Lifecycle emphasis | Partial (predicted FAIL) — Phase 8.5 preamble describes the value of failure-mode justification; notes state no specific failure | Partial (predicted FAIL) — STATUS QUO extended with rich description of criterion-indexing concept, no criterion IDs | Ablation control; description richness ≠ structural implementation |
| **V-04** | Role sequence + Inertia framing | **Strong** (V-01) | **Strong** (V-02) | First simultaneous probe; predicts both PASS |
| **V-05** | Full stack + Phrasing register | **Strong + criterion-ID** — each failure-mode argument explicitly names "C-43 is unenforced at Phase 8.5 entry if this path absent" | **Strong + failure-class precision** — STATUS QUO foil items state "passes C-42 while failing C-44 at criterion-class precision" | Ceiling; ES-R17-1 candidate: criterion-ID annotation in per-note failure arguments |

---

### Key structural differences

**Phase 8.5 Quotation note form progression:**
- V-02/V-03 base: `"This quotation confirms path 1. A reviewer reading only this quotation can verify..."` — C-43 satisfies, C-45 fails
- V-01/V-04: adds `"If this path were absent, [specific failure] would pass Phase 8.5 unchallenged: [mechanism]."` — C-45 activates
- V-05: further adds `"Absent path 1, C-43 is unenforced at Phase 8.5 entry for construction-phase compliance."` — ES-R17-1 candidate

**STATUS QUO foil item form progression:**
- V-01/V-03 base: `"Fails to include per-quotation path attribution notes in the pre-emit gate."` — generic; C-46 fails
- V-02/V-04: `"...in the pre-emit gate (C-43 failure): ...will fail C-43 at criterion-class precision."` — C-46 activates
- V-05: `"...passes C-41 and C-42 while failing C-43 at criterion-class precision: ...the enforcement-path attribution that C-43 measures is absent."` — maximum discrimination precision

**Predicted independence establishment:** V-01 PASS C-45 / FAIL C-46; V-02 FAIL C-45 / PASS C-46 — independence confirmed from both directions before V-04 joint probe.
