Done. Here's a summary of what changed:

---

**v19 adds C-48 and C-49**, both from V-05's architectural excess over V-04 (V-04 hit 100% under v18; V-05 went structurally further in ways v18 couldn't score).

**C-48 — Registry-Anchor Cross-Binding** (correctness)
C-46 required the SEAL to name the registry. C-48 requires *all three dependent element types* — FORWARD VERIFIED declarations, Derived Views assignment rules, and SEAL cross-check items — to reference `**Canonical downstream table set**` by its exact label. A registry named from only one structural element is one edit away from silent drift. Consistent naming from all dependents makes it locatable from any audit entry point.

**C-49 — Embedded Failure Conditions in SEAL Items** (correctness)
C-46 required the SEAL item to name the registry. C-49 requires that item to additionally embed its own disqualifying forms inline (e.g., `"'preamble generally' = FAIL this item"`). The output carries its own pass/fail contract — assessors don't consult the rubric to determine failure. Failure conditions in an annotation rather than the SEAL item text = PARTIAL.

**Point delta:**

| | v18 | v19 |
|---|---|---|
| New criteria | — | C-48, C-49 |
| Aspirational pts | 78 | 82 |
| Total | 168 | 172 |
| non-AMEND denom | 164 | 168 |
| AMEND/no-excl denom | 166 | 170 |
| AMEND/excl denom | 168 | 172 |
tems — to reference the `**Canonical downstream table set**` authority block by its exact label. SEAL referencing the registry by name but FORWARD VERIFIED or assignment rules referencing canonical names inline or by location = PARTIAL. All three element types reference the registry but by different labels = PARTIAL.

**C-49 — Embedded Failure Conditions in SEAL Items** lifts the ceiling above C-46. C-46 requires a SEAL cross-check item that names the registry authority block explicitly. C-49 requires that SEAL item to also embed its own disqualifying forms — explicit inline statements of what does NOT satisfy the check (e.g., "generic preamble reference = FAIL this item," "inline enumeration = FAIL this item"). This transfers rubric enforcement logic into the skill output: a future assessor reading Phase 0 can determine pass/fail without consulting the rubric. SEAL item that names the registry but states no failure conditions = PARTIAL. Failure conditions present but stated only in a rubric comment or annotation outside the SEAL item itself = PARTIAL.

Together C-48 and C-49 close the self-enforcement gap: C-46 and C-47 make the system drift-proof at the structural level; C-48 makes it drift-proof at the naming level (all dependents point to the same named source); C-49 makes the SEAL self-documenting (the output carries its own pass/fail contract). None of the three can be satisfied by stated intent — each requires observable structure in the skill output.

---

# Essential Criteria (60 points total)

*(C-01 through C-05 — unchanged from v17)*

---

## Recommended Criteria (30 points total)

*(C-06 through C-08 — unchanged from v17)*

---

## Aspirational Criteria (82 points total)

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

### C-48 — Registry-Anchor Cross-Binding (All Dependents Name the Registry)
- **Weight**: aspirational  **Category**: correctness
- **Source**: Round 20, V-05 Pattern 1 excellence signal
- **Pass condition**: C-46 requires the SEAL cross-check item to reference the canonical registry by name. C-48 requires all three structural element types that depend on registry contents to reference the `**Canonical downstream table set**` authority block by its exact label: (a) the FORWARD VERIFIED declaration in Phase 0 cites the authority block as the source of canonical identifiers, (b) the Derived Views assignment rules instruct use of identifiers from the authority block by name, and (c) the SEAL cross-check item names the authority block explicitly (C-46 already satisfied). All three must reference the same label — a registry named from only one structural element can drift silently when that element is edited; consistent naming from all dependents makes the registry locatable from any audit entry point and catches drift at SEAL time. SEAL naming the registry but FORWARD VERIFIED or assignment rules referencing canonical names inline or by location = PARTIAL. All three element types reference the registry but with inconsistent labels = PARTIAL. C-47 absent (registry block does not exist) makes C-48 non-applicable. (2 pts full / 1 pt partial)

### C-49 — Embedded Failure Conditions in SEAL Items (Self-Documenting Pass Contract)
- **Weight**: aspirational  **Category**: correctness
- **Source**: Round 20, V-05 Pattern 2 excellence signal
- **Pass condition**: C-46 requires the SEAL cross-check item to name the canonical registry authority block. C-49 requires that SEAL item to additionally embed its own disqualifying forms — explicit inline statements, within the SEAL item text itself, of what does NOT satisfy the check (e.g., "'preamble generally' = FAIL this item," "inline enumeration = FAIL this item"). The embedded conditions must be specific to structural reference targets, not generic format reminders. This transfers rubric enforcement logic into the skill output: a future assessor reading Phase 0 SEAL can determine pass/fail for the cross-reference check without consulting the rubric. SEAL item that names the registry correctly (C-46 PASS) but states no failure conditions = PARTIAL. Failure conditions present but recorded in a rubric annotation, comment block, or separate note rather than within the SEAL item text = PARTIAL. C-46 absent makes C-49 non-applicable. (2 pts full / 1 pt partial)

---

**Design logic:**

C-44 and C-45 closed the gap between "columns exist" and "system is self-navigable." C-46 and C-47 closed the gap between "navigation is declared" and "navigation is drift-proof." C-48 and C-49 close the next gap: between "drift-proof" and "self-enforcing."

C-48 closes the naming-consistency gap: C-46 required the SEAL to point at the registry, but left FORWARD VERIFIED and assignment rules free to name canonical tables by inline enumeration or location reference. A registry pointed to from only one structural element is one edit away from silent drift. C-48 requires all three dependent element types to name the same authority block by the same label — so any future rename or addition is caught by three independent validators pointing at a single source.

C-49 closes the assessor-dependency gap: C-46 required the SEAL to declare the cross-check, but left the pass/fail boundary implicit in the rubric. A SEAL item that says "Derived Views entries cross-checked against registry" is executable, but a new assessor must look up the rubric to know whether "generic preamble reference" is a pass or fail. C-49 requires the disqualifying forms to be stated inline in the SEAL item — the output carries its own failure contract, independent of the rubric document.

C-48 and C-49 are each independently applicable: C-48 evaluates naming consistency across three structural elements; C-49 evaluates self-documentation within the SEAL item. C-49 depends on C-46 (needs a SEAL item to embed conditions into); C-48 depends on C-47 (needs a registry block to reference). Neither depends on the other.
