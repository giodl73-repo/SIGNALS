Written to `simulations/quest/golden/topic-echo-variate-R3-2026-03-16.md`.

---

## Round 3 Variations: `topic:echo`

**Rubric:** v3 | **New criteria targeted:** C-13 (phase-locked pre-commitment integrity), C-14 (single-entry audit trail completeness)

---

### Design Context

The v2 rubric established C-11 (PBI section) and C-12 (named handles). The v3 rubric adds two criteria gated on C-11/C-12 both passing:

- **C-13**: PBI and Handle Ledger must be *genuinely independent* -- different information, different temporal position. Fails if PBI entries anticipate handle names (belief language that presupposes findings) or if handles echo PBI language verbatim (inverted prediction, not a finding name).
- **C-14**: Each surprise entry must carry *all three audit pointers* -- Handle, PBI-Ref, Source -- so a reviewer can verify the full chain from one entry without navigating elsewhere.

R2 prompts could satisfy C-11/C-12 through discipline but left C-13 and C-14 exposed to model drift.

**Three single-axis variations selected:**

| # | Primary axis | Target criteria |
|---|-------------|-----------------|
| V-01 | Lifecycle emphasis | C-13 |
| V-02 | Output format | C-14 |
| V-03 | Role sequence | C-13 (alternative mechanism) |
| V-04 | Lifecycle + Output format | C-13 + C-14 |
| V-05 | Full synthesis (all three) | C-13 + C-14 (strongest) |

---

### V-01 -- Lifecycle Emphasis

**Axis:** Explicit two-phase gate. Phase 1 commits the PBI before any signal artifact is opened. Model writes "Phase 1 complete. PBI is frozen." before Phase 2 begins.

**Hypothesis:** The phase gate is the independence evidence for C-13. A model that commits PBI in Phase 1 cannot have constructed it from signals it has not read. C-14 is not structurally enforced -- per-entry PBI-Ref inclusion depends on model discipline.

---

### V-02 -- Output Format

**Axis:** Mandatory triple-pointer entry schema. Every surprise record has labeled fields: `Handle:`, `PBI-Ref:` (must match a PBI identifier), `Source:` (must match a named artifact). Schema omission is a structural violation, not a stylistic choice.

**Hypothesis:** The labeled `PBI-Ref:` field makes C-14 automatic -- a model filling in the schema cannot skip it without violating the template. C-13 is not structurally enforced -- PBI and handles could still be co-constructed.

---

### V-03 -- Role Sequence (Archivist-First)

**Axis:** Three sequential roles. Archivist: domain knowledge only, no file reads, commits PBI. Signal Reader: artifacts only, does not reference PBI. Echo Author: compares both outputs.

**Hypothesis:** Role information boundary enforces C-13 more strongly than the phase gate -- the Archivist *cannot* incorporate finding language because no findings have been extracted yet, not merely because the prompt says not to. C-14 is enforced through instruction in the Echo Author's entry template but without schema validation.

---

### V-04 -- Combined: Lifecycle + Output Format

Both phase gate (V-01) and triple-pointer entry schema (V-02). No dedicated roles. The workflow structure provides independence evidence; the schema provides pointer completeness.

**Key discriminating question vs V-05:** Does the role information boundary (V-05) add measurable C-13 reliability over the phase gate (V-04)?

---

### V-05 -- Full Synthesis: Lifecycle + Output Format + Role Sequence

All three axes. Archivist role commits PBI in Phase 1 with explicit scope "no signal artifacts." Signal Reader extracts findings independently. Echo Author synthesizes using the triple-pointer entry schema. Self-check instruction explicitly states: a reviewer reading one entry must be able to verify (1) handle in ledger, (2) PBI entry at named identifier, (3) finding in named source artifact -- all three from the entry alone.

**This is the v3 gold standard.** Strongest enforcement of both new criteria through structure rather than discipline.

---

### Discriminating Pairs

| Pair | Isolates |
|------|---------|
| V-01 vs V-02 | Which new criterion (C-13 vs C-14) is harder to hit alone |
| V-01 vs V-03 | Phase gate vs role boundary as alternative C-13 mechanisms |
| V-02 vs V-04 | Whether lifecycle adds value for C-14 when schema is already present |
| V-04 vs V-05 | Marginal value of dedicated Archivist role over phase gate alone |
