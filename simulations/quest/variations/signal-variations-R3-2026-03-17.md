Written to `simulations/quest/golden/signal-variate-R3-2026-03-17.md`.

---

## Round 3 -- 5 Variations

**R3 context**: Two new aspirational criteria added from R2 excellence signals. All variations carry the R2 V-01 base (domain noun table + char-count alignment + verbatim catalog). Single-axis variations test each new criterion in isolation before combining.

| Variation | Axis | New mechanism | C-14 | C-15 |
|-----------|------|--------------|------|------|
| **V-01** | C-14 single | Restart gate for **both** bare AND filter modes | FULL | PARTIAL |
| **V-02** | C-15 single | Precomputed namespace-by-namespace **width table** | FAIL | FULL |
| **V-03** | Phrasing register | Conversational/user-facing framing | FAIL | PARTIAL |
| **V-04** | C-14 + C-15 | Both gates + width table (minimal R3 champion) | FULL | FULL |
| **V-05** | Full integration | V-04 + "example pad" column, purpose-phrase headers | FULL | FULL |

**Key design decisions:**

- **V-01** uses the exact restart language proven in R2 (`"MODE: BARE is violated. Restart."`), extended to cover filter mode with a symmetric gate.
- **V-02** introduces a 12-row width table with a worked numeric example (`/scout-naming (13) needs 7 spaces`), replacing the single-section example from R2 V-01. This gives the model a lookup rather than a counting task.
- **V-03** isolates the phrasing register axis cleanly — no gates, no table — to measure what conversational framing alone contributes to C-07/C-08.
- **V-04** is the minimal combination: both new criteria, no phrasing changes, so any score lift over V-01 is attributable purely to C-15.
- **V-05** adds an `example pad` column to the width table (one concrete example per namespace row) and ensures headers explicitly state purpose in plain words — addressing C-08 more directly than any prior variation.
