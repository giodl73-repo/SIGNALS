**v13 written** to `simulations/quest/rubrics/prove-topic-rubric-v13-2026-03-16.md`.

---

## What changed

**Three new criteria extracted from Round 13:**

| ID | Axis | Pattern | Exemplar |
|----|------|---------|---------|
| **C-37** | Gate chain role ordering as dependency declaration | Roles declared in C→B→A execution-dependency order at CAMPAIGN OPEN; the dependency chain is readable from the role sequence itself before the gate block is reached | V-01, V-05 |
| **C-38** | Phrasing template printed verbatim at point of use | SESSION INVARIANT D template echoed verbatim immediately above each INCUMBENT CHECK execution point; deviation is visible before it happens, not only detectable by backward registry lookup | V-04 |
| **C-39** | Dual-site template enforcement: gate obligation and execution obligation | Template appears at both ENTRY CONDITIONS (gate obligation) AND INCUMBENT CHECK headers (execution obligation); phrasing confirmed at two independent structural sites per stage | V-05 |

**Gap anatomy:**

- **C-37** closes the dependency-ordering gap C-35 leaves open: ROLE C exists and produces a gate field, but roles can be declared in any order — the C→B→A dependency is enforced by the gate, not readable from the role sequence. Declaring roles in execution-dependency order encodes the logical priority as structural convention.
- **C-38** closes the detection-proximity gap C-36 leaves open: SESSION INVARIANT D is declared and binding, but referencing it by name at each INCUMBENT CHECK forces deviation detection by backward lookup. Printing the template verbatim above the execution point makes deviation visible before it happens.
- **C-39** closes the single-site gap C-38 leaves open: the template is printed at execution, but stage entry is not conditioned on template confirmation. ENTRY CONDITIONS for each evidence stage must also carry the template, making phrasing a gate obligation as well as an execution obligation.

**Structural grouping:** C-37 extends the Comparator Tracking Depth chain from `C-34/C-35/C-36` (v12) to `C-34/C-35/C-36/C-37/C-38/C-39` (v13) — six criteria covering the full chain from named structural visibility through dual-site phrasing enforcement.

**Weight outcome:** Max rises 192 → 204 (31 aspirational × 4 = 124). Golden threshold unchanged at 80.
