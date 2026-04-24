Written to `simulations/quest/rubrics/draft-spec-rubric-v15-2026-03-15.md`.

---

**Three new criteria extracted from R15:**

| C | Name | Source | Category | N/A? |
|---|------|--------|----------|------|
| C-44 | Chained ENTER/EXIT phase transition notation | R15 V-01 C-41 evidence | structure | universal |
| C-45 | Structural fail rule in dual form (negative + positive) | R15 V-02 C-37 evidence | depth | N/A without STATUS-QUO-SNAPSHOT |
| C-46 | Invalidity rule scoped to "this phase block" | R15 V-02 C-36 evidence | governance | N/A without STATUS-QUO-SNAPSHOT |

**What changed v14 → v15:**

| | v14 | v15 |
|-|----|-----|
| Aspirational count | 35 | 38 |
| Total criteria | 43 | 46 |
| Formula denominator | 35 | 38 |
| N/A group (STATUS-QUO-SNAPSHOT) | C-36, C-37 | C-36, C-37, C-45, C-46 |

**Key reasoning for each:**

- **C-44** (requires C-41): The R15 V-01 evidence shows each phase EXIT names exactly what the next phase ENTER requires — `table complete → PM-CONTRACT-SEAL → INERTIA-ANALYZED → SPEC-DRAFT-COMPLETE → amendment list`. Phase 4 has no gate token, yet its EXIT still names a named output in the same structural position. This is stronger than C-41 (which only requires blocks to exist at boundaries); C-44 requires the blocks to form a named chain.

- **C-45** (requires C-37): The R15 V-02 C-37 evidence added a second sentence: "Do not leave Gap blank when Alternative is populated." C-37 only requires the negative structural fail declaration. The dual form makes the rule self-contained for a processing agent — no inference required.

- **C-46** (requires C-36): The R15 V-02 C-36 evidence scoped the check to "from this phase block." Without this qualifier, a block defined in a global definitions section or earlier phase could silently satisfy an absence check that was intended to verify in-phase colocation. This is a distinct governance gap from C-36's existence check.
