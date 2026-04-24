Reading the scorecard carefully, the R19 excellence signals come from **V-05's C-44 and C-45 evidence**:

- **C-44 V-05**: SEAL item 8 cross-checks Derived Views names against the preamble canonical set — stronger than C-44 alone because it catches drift that escaped both VERIFIED declarations and assignment rules
- **C-45 V-05**: Preamble gains an explicit **Canonical downstream table set** authority block — preamble becomes both navigation guide and canonical name registry

These become **C-46** and **C-47**.

---

# topic-retro Rubric v18 — 2026-03-17

**What changed in v18:**

| | v17 | v18 |
|---|---|---|
| New criteria | -- | C-46, C-47 |
| Aspirational pts | 74 (C-09–C-45) | 78 (C-09–C-47) |
| Total | 164 | 168 |
| non-AMEND denom | 160 | 164 |
| AMEND/no-excl denom | 162 | 166 |
| AMEND/excl denom | 164 | 168 |

**C-46 — SEAL-Preamble Cross-Reference Integrity Check** lifts the ceiling above C-44. C-44 requires the Phase 0 SEAL to enforce exact canonical names and directional check statements. C-46 requires an additional SEAL item that explicitly cross-checks manifest Derived Views entries against the canonical set declared in the ASSESSOR NAVIGATION PREAMBLE. C-44 PASS without this cross-check item = PARTIAL. Cross-check present but referencing an implicit or inline canonical set rather than the named preamble declaration = PARTIAL.

**C-47 — Preamble as Canonical Name Registry (Downstream Table Authority)** lifts the ceiling above C-45. C-45 requires a structured ASSESSOR NAVIGATION PREAMBLE naming three entry points. C-47 requires the preamble to additionally serve as the authoritative name registry: an explicit named declaration block (e.g., **Canonical downstream table set**) enumerating all downstream tables by their exact identifiers. C-45 PASS with entry point 2 listing tables in prose but no standalone authority block = PARTIAL. Authority block present but unlabeled or embedded inline in entry point 2 prose = PARTIAL.

Together C-46 and C-47 close the drift gap: C-46 enforces that the SEAL actively validates names against the registry, and C-47 ensures the registry itself is a first-class structural artifact rather than implicit list content. Neither can be satisfied by prose description of intent.

---

# Essential Criteria (60 points total)

*(C-01 through C-05 — unchanged from v17)*

---

## Recommended Criteria (30 points total)

*(C-06 through C-08 — unchanged from v17)*

---

## Aspirational Criteria (78 points total)

*(C-09 through C-43 — unchanged from v17)*

### C-44 — SEAL-Enforced Bidirectional Navigation Completeness
- **Weight**: aspirational  **Category**: correctness
- **Source**: Round 18, V-05 C-42 excellence signal
- **Pass condition**: C-42 requires the structural columns for both citation directions to be present. C-44 requires the Phase 0 SEAL to verify three additional properties that prevent PARTIAL degradation over time: (a) each Derived Views entry names the exact downstream table identifier rather than a generic label, (b) a forward navigation check statement is present in Phase 0 explicitly declaring the manifest → downstream direction as verified, and (c) a backward navigation check statement is present in Phase 0 explicitly declaring the downstream → manifest direction as verified. A SEAL that checks structural column presence (C-42) but does not enforce exact naming or directional check statements = PARTIAL. A SEAL that covers both directional check statements but accepts generic Derived Views entries = PARTIAL. (2 pts full / 1 pt partial)

### C-45 — Assessor Navigation Preamble (Three-Entry-Point Declaration)
- **Weight**: aspirational  **Category**: format
- **Source**: Round 18, V-05 C-43 excellence signal
- **Pass condition**: C-43 requires a `Manifest column` field mapping each contract row to the exact AUDIT MANIFEST column that evidences it. C-45 requires the contract to be prefaced by an explicit assessor navigation preamble — a structured block (not prose) naming all valid audit entry points: (1) contract row → manifest column via the `Manifest column` field, (2) manifest row → downstream table via the `Derived Views` column, (3) phase section header → manifest source via the `[DERIVED FROM]` declaration. Fewer than three entry points = PARTIAL. Three entry points in prose rather than a structured block = PARTIAL. (2 pts full / 1 pt partial)

### C-46 — SEAL-Preamble Cross-Reference Integrity Check
- **Weight**: aspirational  **Category**: correctness
- **Source**: Round 19, V-05 C-44 excellence signal
- **Pass condition**: C-44 requires the Phase 0 SEAL to enforce exact canonical names and bidirectional check statements. C-46 requires an additional SEAL item that explicitly cross-checks Derived Views entries in the manifest against the canonical downstream table set declared in the ASSESSOR NAVIGATION PREAMBLE (C-47 block). The cross-check must reference the preamble declaration by name — not an implicit inline list. C-44 PASS without this cross-check item = PARTIAL. Cross-check present but referencing an inline or implicit canonical set rather than the named preamble authority block = PARTIAL. Preamble absent (C-47 N/A) makes C-46 non-applicable. (2 pts full / 1 pt partial)

### C-47 — Preamble as Canonical Name Registry (Downstream Table Authority)
- **Weight**: aspirational  **Category**: format
- **Source**: Round 19, V-05 C-45 excellence signal
- **Pass condition**: C-45 requires a structured ASSESSOR NAVIGATION PREAMBLE block naming three entry points. C-47 requires the preamble to additionally serve as the authoritative canonical name registry: a standalone named declaration block (e.g., **Canonical downstream table set**) positioned below the three-entry-point block, enumerating all downstream tables by their exact canonical identifiers. This block is the single source of truth referenced by SEAL cross-check items (C-46) and VERIFIED declarations (C-44). C-45 PASS with entry point 2 listing table names in its row but no standalone authority block = PARTIAL. Authority block present but unlabeled, prose-embedded, or merged into entry point 2 text rather than a separate named structure = PARTIAL. (2 pts full / 1 pt partial)

---

**Design logic:**

C-44 and C-45 closed the gap between "columns exist" and "system is self-navigable." C-46 and C-47 close the next gap: between "navigation is declared" and "navigation is drift-proof." C-47 promotes the canonical name list from implicit entry-point content to an explicit first-class registry block. C-46 requires the SEAL to actively validate against that registry — so any future drift (a renamed table, a new downstream phase) is caught at SEAL time rather than discovered during audit. The two criteria are interdependent by design: C-46 is non-applicable without C-47's registry block, and C-47's registry is only structurally enforced when C-46 wires the SEAL to it.
