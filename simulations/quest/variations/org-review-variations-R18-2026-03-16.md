Written to `simulations/quest/golden/crew-review-variate-R18-v11-2026-03-17.md`.

---

# org-review -- Variate R18 (rubric v11)

5 complete prompt body variations targeting **225/225** -- V-05 R11's base (C-30+C-31+C-32 PASS at 210) combined with C-33+C-34+C-35 PASS simultaneously.

**Gap analysis from V-05 R11 (210/225):**

| Criterion | V-05 R11 | Gap |
|-----------|----------|-----|
| C-33 LENS APPLICABILITY RATING | FAIL | C-31 PASS but no Applicability column schema pre-committed |
| C-34 ADVISORY-GAP DOMAIN COVERAGE | vacuous | C-33 FAIL means no HIGH-applicability tier to gap-check against |
| C-35 NH CHALLENGER DIMENSION TABLE | FAIL | Challenger uses prose testimony, not structured dimension comparison table |

**Why V-02 R12 scores ~215 not 225**: achieved C-33/C-34/C-35 PASS but in a domain-first variant architecture that weakened C-16/C-30/C-32 relative to V-05 R11. R18 grafts the three new criterion patterns onto V-05 R11's intact bracket scaffold.

---

## Variation axes

| Variant | Axes | C-33 path | C-34 path | C-35 path | Predicted |
|---------|------|-----------|-----------|-----------|-----------|
| **V-01** | Output format | Pre-§§ LENS OUTPUT SCHEMA block | Pre-§§ LENS OUTPUT SCHEMA mandate | §3 NH table requirement | **225/225** |
| **V-02** | Phrasing register | Dense behavioral §13 with violation conditions | Dense behavioral §13 with gap-check enforcement | §3 NH table requirement | **225/225** |
| **V-03** | Inertia framing | §13 standard Applicability protocol | §13 standard gap-check | §3 scope-anchored dimensions (strongest C-35) | **225/225** |
| **V-04** | Output format + Phrasing register | Schema block + behavioral §13 (dual path) | Schema block + behavioral §13 (dual path) | §3 | **225/225** |
| **V-05** | All three | Schema + behavioral + scope alignment | Schema + behavioral + scope alignment | Scope-anchored (strongest) | **225/225** |

---

## Key structural differences

**V-01** introduces a standalone `LENS OUTPUT SCHEMA` pre-§§ block -- structurally parallel to the §§ contracts -- that pre-declares the row schema with the `Applicability` column and mandates the `DOMAIN COVERAGE GAP-CHECK`. §13 references this block. The schema is auditable without reading §13.

**V-02** has no pre-§§ block. §13 carries two independent enforcement paths: a violation condition for the missing Applicability field (C-33) and a protocol-violation declaration for omitting the gap-check (C-34). An auditor reading §13 alone can verify both requirements without the schema block.

**V-03** adds scope-anchored NH dimensions: after `SCOPE DECLARATION`, the §3 contract directs the prompt to group IN-SCOPE surfaces into 3-5 evaluation dimensions before BRACKET OPENING runs. The challenger enters with a pre-committed dimension set derived from the declared artifact scope -- not ad hoc choice. This produces the most auditable g_null (table values trace directly to declared scope surfaces).

**V-04** = V-01 schema block + V-02 behavioral §13. Both enforcement paths for C-33/C-34 are simultaneously active and independently auditable.

**V-05** = all three. The domain registry for C-34's gap-check and the NH dimensions for C-35's table share the same provenance: the SCOPE DECLARATION. Scope alignment reinforces the inter-criterion chain.
