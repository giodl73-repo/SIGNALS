`flow-lifecycle-variate-R14-2026-03-16.md` written. Here's the summary:

---

## Round 14 — What changed and why

**New criteria probed:**
- **C-46** — `STATUS-QUO PROCESS DECLARATION` block before STEP 0A, with FM-01/FM-02 identifiers + inertia driver. FM-IDs become mandatory trace fields in downstream columns.
- **C-47** — Phase Index gains a `Status-Quo Gap` column adjacent to `Entry Trigger`. The two columns audit each other: a generic `DERIVED:rationale` simultaneously produces a vague FM-ID-free gap, making incompleteness visible without an extra gate.

**New defects in the taxonomy (D-09 through D-13):**

| D-ID | Defect | Criterion |
|------|--------|-----------|
| D-09 | Missing SQ Declaration before STEP 0A | C-46 |
| D-10 | FM-ID-free failure mode in SQ Declaration | C-46 |
| D-11 | Unanchored status-quo gap (prose without FM-ID) | C-47 |
| D-12 | DERIVED-only Phase Index (no Status-Quo Gap column) | C-47 |
| D-13 | Gap-column-only Phase Index (no DERIVED:rationale) | C-44, C-47 |

D-12/D-13 are the C-37 dual-mechanism failure variant pair for C-47.

**Hypothesis matrix:**

| V | C-46 | C-47 | Axis |
|---|:----:|:----:|------|
| V-01 | TARGET | HOLD | Inertia Framing — FM-IDs as downstream reference registry via inline column-header enforcement |
| V-02 | HOLD | TARGET | Output Format — Entry Trigger / Status-Quo Gap column adjacency with "these two columns audit each other" language |
| V-03 | TARGET | TARGET | Phrasing Register — imperative "Write FM-01:", "Write the FM-ID" at point-of-use |
| V-04 | TARGET | HOLD | Role Sequence + Inertia Framing — SQ Declaration adds `Incumbent Role Scope`; Role Registry gains `SQ-Scope (IN/NEW/SECONDARY)` field |
| V-05 | TARGET | TARGET | Lifecycle Emphasis + Inertia Framing + Phrasing Register — phase blocks (not table rows) with FM-ID field adjacent to Entry Trigger; R15 floor candidate |
