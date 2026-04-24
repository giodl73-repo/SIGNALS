Written to `simulations/quest/golden/trace-migration-variate-R18-2026-03-15.md`.

---

## Round 18 — trace-migration Variations (V-01 through V-05)

### Variation map

| V | Axis | C-46 | C-47 | Design logic |
|---|------|------|------|-------------|
| **V-01** | Role sequence | Expected PASS | Expected PASS | Operations-as-substrate framing; compound annotation at both anchors follows naturally from the substrate-declaration register; manifest structured as a verification contract |
| **V-02** | Output format | Expected PASS | Expected PASS | Table schema specifies `(BINARY FIELD)` token at both gate positions; manifest completeness rule is a required table field |
| **V-03** | Lifecycle emphasis | Expected PASS | Expected PARTIAL | Per-phase vocabulary + coverage floors anchor the gate chain; manifest rule present but emergent, not required by directive |
| **V-04** | Role sequence + Phrasing register | Expected PASS | Expected PASS | DIRECTIVE B-1 explicitly prohibits omitting `(BINARY FIELD)` at ENTRY REFERENCE; DIRECTIVE B-3 requires the self-referential rule as a named assertion |
| **V-05** | Combined (all three single axes) | Expected PASS | Expected PASS | Three independent structural pressures converge — designed for the 285-point ceiling |

---

### What makes R18 new

**C-46 mechanism** — every variation carries the `(BINARY FIELD)` compound annotation at the ENTRY REFERENCE position, not only the EXIT BLOCK. The annotation is framed as "independently load-bearing at this position" — a reader verifying Phase B's opening sees the binary constraint type without cross-referencing Phase A. V-04's DIRECTIVE B-1 is the most explicit: it names the asymmetric form (`PARSE GATE = OPEN required`) and prohibits it.

**C-47 mechanism** — every variation except V-03 includes the self-referential completeness rule as a named structural assertion in the PROTOCOL COUNT MANIFEST: *"A gate named in any block but absent from this manifest = incomplete registry."* V-04's DIRECTIVE B-3 elevates it from an embedded note to a required labeled statement. V-03 includes the rule but does not require it — expected PARTIAL.

---

### Key structural choices per variation

**V-01 (Role sequence)** — the three-artifact alignment (COST LEDGER row (a) / Operations Q1 / B2 substrate) is declared in an ALIGNMENT STATE BINDING section before Q1. The substrate class pre-committed there propagates to the ENTRY REFERENCE annotation and the manifest. The role ordering is the engine; everything else follows.

**V-02 (Output format)** — every analytical layer is a named table with explicit column schemas and fill rules. The gate tables at both boundary positions carry the `(BINARY FIELD)` column, making annotation omission a visible table-structure gap rather than a prose oversight.

**V-03 (Lifecycle emphasis)** — per-phase vocabulary lists (`Phase A vocabulary: ...`, `Phase B vocabulary: ...`) and per-phase coverage requirements dominate the framing. The BOUNDARY PROTOCOL vocabulary list includes `BINARY FIELD` and `compound annotation` as named terms, which naturally propagates annotation symmetry. But the manifest completeness rule is not a DIRECTIVE — making C-47 PARTIAL the expected outcome.

**V-04 (Role sequence + Phrasing register)** — 10 Phase A DIRECTIVES and 6 Phase B DIRECTIVES replace prose instructions entirely. DIRECTIVE A-10 establishes the compound annotation principle and foreshadows DIRECTIVE B-1. DIRECTIVE B-3 requires the completeness rule as a "structural assertion, not a comment." This is the highest-explicitness variation for C-46 and C-47.

**V-05 (Combined)** — Operations-first role sequence + table schemas that embed `(BINARY FIELD)` as a column + per-phase vocabulary lists that name `ENTRY REFERENCE` and `PROTOCOL COUNT MANIFEST` as Phase B terms + inertia-inversion table in B2. Three structural pressures converge on C-46 and C-47; designed to overdetermine both passes.
