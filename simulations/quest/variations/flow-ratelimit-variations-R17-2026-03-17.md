Saved to `simulations/quest/golden/flow-ratelimit-variate-R17-2026-03-17.md`.

---

# flow-ratelimit — Variate R17

**Target criteria: C-39, C-40**

## Variation Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **Axis** | Role sequence | Output format | Lifecycle emphasis | Seq + Format | Full integration |
| **C-39 technique** | Inline prose, component names | Inline prose, component names | Component-name slot placeholders | Inline prose | Inline prose |
| **C-40 technique** | Three schemas, inline prose | Three schemas, subsection headers | Three schemas + role-mapping table | Subsection headers | Subsection headers + CHECK (e) |

---

## Key Design Decisions

**C-39 implementation across all variations:**
The Format Contract's SCHEMA-A defines BASELINE as "connector API call volume at the burst-path source endpoint identified by Finding ID in Role 3 (BP-xx), before concurrency controls or mitigations from Role 8c are applied." This names the Role 3 component directly — it is not generic ("current state before mitigation"). A reader of only the Format Contract knows which component BASELINE refers to without reading any other section.

**C-40 implementation across all variations:**
Three distinct schemas with different column structures:
- **SCHEMA-A / SCHEMA 1** (Primary Analysis): `BASELINE | PROTECTED | DERIVATION CHAIN` — for cascade tables and quantified impact
- **SCHEMA-V / SCHEMA 2** (Volume Mapping): `VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta` — for volume-to-behavior tables
- **SCHEMA-M / SCHEMA 3** (Mitigation Record): `FINDING ID | BEFORE STATE | AFTER STATE | Addresses` — for per-finding mitigation tables

A single universal schema cannot serve all three table types — column structures differ by purpose.

---

## Variation Hypotheses

**V-01** — Burst-path-first + inline prose Format Contract. Scenario-anchored definitions as flowing prose within each schema block. The simplest C-39/C-40 implementation that preserves all R16 structure.

**V-02** — Three schemas as headed subsections (`#### SCHEMA 1`, `#### SCHEMA 2`, `#### SCHEMA 3`). C-40's three-schema decomposition is scan-time verifiable from heading structure alone, independent of reading column definitions. Parallels C-36's standalone-heading requirement for FNMI.

**V-03** — Format Contract expanded with an explicit role-to-schema assignment table and component-name slot placeholders in BASELINE/PROTECTED definitions (`[connector endpoint identified as BP-xx primary burst source in Role 3]`). The slot syntax makes C-39 compliance a production-time commitment, not a post-hoc interpretation.

**V-04** — Combination of V-01 (burst-path-first role sequence) + V-02 (subsection-headed schemas). Both C-40 scan-time verifiability and burst-path classification integrity enforced structurally.

**V-05** — Full integration: V-04 features + V-03's role-to-schema mapping table + new **CHECK (e)** in the Terminal Reconciler. CHECK (e) audits that each assigned role produced a table with the correct schema type, creating an end-to-end closed compliance chain for C-40 analogous to CHECK (a)'s chain for Verdict revision currency.
