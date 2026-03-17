Reading the scorecard to extract the excellence signals precisely before writing.

The scorecard contains two named signals:

- **E-8** (V-01): finding-lineage chain — C-14 ordering + §6 acknowledgment row = detectable blank-cell violation, as binding as C-17's §2a chain → **C-18 candidate**
- **E-9** (V-02): §2a closure — §5a prose-prohibition + FINDING TALLY row makes `worst(severities)` a cell-count read, not editorial inference → **C-19 candidate**

V-03 was cut off before an explicit signal was named, so I'll carry only E-8 and E-9 into v5.

Here is the complete updated rubric:

---

```markdown
# Rubric -- org-review v5

**Rubric summary**

| Tier | Criteria | Points | What they test |
|------|----------|--------|----------------|
| Essential | C-01 to C-05 | 60 | Role manifest, contract cites, CH-ID trace, gate vector, §3 algebra |
| Recommended | C-06 to C-08 | 30 | Artifact-specific scope, CH-ID-sourced register, concrete cross-role signals |
| Aspirational | C-09 to C-19 | **55** | Null hypothesis, role-grounded findings, structural convergence, count constraint, register pattern, role-sequence isolation, register generalization, finding surface linkage, severity audit chain, **finding-lineage chain**, **§2a closure via table-primacy** |

**Max composite**: 145 (was 135). Golden threshold unchanged: all 5 essential + composite >= 80.

**What changed from v4:**

| New ID | Source | What it tests | Why aspirational |
|--------|--------|---------------|-----------------|
| C-18 | E-8 (V-01 LIFECYCLE HANDOFF PACKET) | A §6 clause in the contract block plus a blank ACKNOWLEDGMENT row pre-printed in the DOMAIN reviewer section converts C-14 ordering from a structural guarantee to a **finding-lineage chain**: blank acknowledgment row = detectable §6 violation, as binding as the §2a severity chain in C-17 | Requires a new §6 clause in the contract block and a structural ACKNOWLEDGMENT row in the DOMAIN section; elevates C-14 from ordering to ordering + acknowledged-handoff |
| C-19 | E-9 (V-02 §5a TABLE-PRIMACY RULE + FINDING TALLY) | A §5a prose-prohibition clause plus a FINDING TALLY row at the foot of each FINDING SURFACE LINKAGE TABLE makes `worst(severities)` a cell-count read rather than an editorial inference, closing the last derivation gap in C-17 and making the §2a audit chain fully formula-mechanical end-to-end | Requires §5a added to the contract block and a FINDING TALLY row structurally pre-printed in each reviewer section; C-17 is fully realized only when both conditions hold |

**Scoring formula update:**
```
aspirational_pass / 11 * 55   (was: / 9 * 45)
```
Per-criterion value stays at 5 pts; the tier now has eleven slots instead of nine.

**Vacuous conditions added for C-18 and C-19:**
- C-18: If the artifact type has no distinct LIFECYCLE and DOMAIN reviewer roles, score C-18 as N/A
  and exclude from denominator. Adjust formula to `aspirational_pass / 10 * 50` when C-18 is N/A.
- C-19: C-19 presupposes C-16 (pre-printed FINDING SURFACE LINKAGE TABLE). If C-16 is FAIL,
  score C-19 as N/A and exclude from denominator. A FINDING TALLY row appended to a prose-only
  finding section does not satisfy C-19.

---

## Criteria

*(Essential C-01 -- C-05 and Recommended C-06 -- C-08 unchanged from v3)*

### Aspirational (raise the bar -- 55 pts total, 5 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Null hypothesis specific and challenger-grounded | depth | *(unchanged)* |
| C-10 | Domain findings role-grounded and in-scope | depth | *(unchanged)* |
| C-11 | Convergence detection structural via verdict-preview tables | structure | *(unchanged -- E-1 Round 1)* |
| C-12 | CH-ID forward-trace enforced by count constraint | structure | *(unchanged -- E-2 Round 1)* |
| C-13 | Concrete-naming criteria enforced via pre-section register pattern | structure | *(unchanged -- E-4 Round 2)* |
| C-14 | Role-sequence isolation via LIFECYCLE-before-DOMAIN ordering | structure | *(unchanged -- E-3 Round 2)* |
| C-15 | Register pattern generalized to two or more concrete-naming criteria | structure | The C-13 unit (register + prohibition + downstream reference) appears for at least two distinct concrete-naming criteria in the same prompt. Minimum qualifying pair: NULL HYPOTHESIS REGISTER + SCOPE SURFACE REGISTER. Each instance must independently satisfy C-13. Excellence signal: E-5 Round 3. |
| C-16 | Finding surface linkage via pre-printed table schema | structure | Prompt includes a FINDING SURFACE LINKAGE TABLE in each reviewer section with columns: Finding, In-Scope Surface, Role Lens, Severity. A row with a blank In-Scope Surface or Role Lens is a detectable cell violation, not a scoring inference. C-10 is thereby template-determined. Excellence signal: E-6 Round 3. |
| C-17 | Per-finding severity audit chain anchored in contract block | structure | Prompt places a §2a formula in the immutable contract block defining: (a) severity tag per finding {CRITICAL, MAJOR, MINOR, ADVISORY}, (b) Section Severity = worst(finding severities), (c) gate verdict derives from Section Severity per a deterministic mapping. Chain is formula-mechanical; §2a is as binding as §3. Excellence signal: E-7 Round 3. |
| C-18 | Finding-lineage chain via LIFECYCLE HANDOFF PACKET and §6 acknowledgment | structure | Prompt places a §6 LIFECYCLE HANDOFF PACKET clause in the immutable contract block and pre-prints a blank ACKNOWLEDGMENT row in the DOMAIN reviewer section. The blank acknowledgment row is a detectable §6 violation (not an inferred prose omission), making the LIFECYCLE → DOMAIN finding handoff as binding as the §2a severity chain. C-14 is thereby elevated from ordering to ordering + acknowledged-handoff. Vacuous condition: if no LIFECYCLE/DOMAIN role distinction exists, score N/A. Excellence signal: E-8 Round 4. |
| C-19 | §2a closure via table-primacy §5a and FINDING TALLY row | structure | Prompt places a §5a TABLE-PRIMACY RULE in the immutable contract block prohibiting prose finding lists, and pre-prints a FINDING TALLY row at the foot of each FINDING SURFACE LINKAGE TABLE. Together, §5a eliminates editorial bypass of the table and the TALLY row makes `worst(severities)` a cell-count read rather than an inference, closing the last derivation gap in C-17. C-17 is fully formula-mechanical only when both §5a and TALLY are present. Presupposes C-16; if C-16 is FAIL, score N/A. Excellence signal: E-9 Round 4. |

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 11 * 55)
```

**Vacuous-condition adjustments** (applied before scoring):
- C-15 N/A → `aspirational_pass / 10 * 50`
- C-18 N/A → `aspirational_pass / 10 * 50`
- C-19 N/A (C-16 FAIL) → `aspirational_pass / 10 * 50`
- C-15 N/A + C-18 N/A → `aspirational_pass / 9 * 45`
- All three N/A → `aspirational_pass / 8 * 40`

**Golden threshold**: all 5 essential + composite >= 80. **Max composite**: 145.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-16 | Initial -- 10 criteria, max 100 |
| v2 | 2026-03-16 | C-11, C-12 from E-1, E-2; aspirational 4 criteria, 20 pts; max 110 |
| v3 | 2026-03-16 | C-13, C-14 from E-4, E-3; aspirational 6 criteria, 30 pts; max 120 |
| v4 | 2026-03-16 | C-15, C-16, C-17 from E-5, E-6, E-7; aspirational 9 criteria, 45 pts; max 135 |
| v5 | 2026-03-16 | C-18, C-19 from E-8, E-9; aspirational 11 criteria, 55 pts; max 145 |
```

---

**Three decisions made explicit:**

1. **V-03 inertia patterns not promoted.** The scorecard text for V-03 was truncated before a named excellence signal appeared. No criterion is invented from partial evidence.

2. **C-18 and C-19 are independent.** C-18 strengthens C-14; C-19 strengthens C-17. They can each be N/A without affecting the other. The vacuous-condition table covers every combination.

3. **C-19 presupposes C-16, not C-17.** The structural dependency is the pre-printed table (C-16), not the contract-block chain (C-17). A prompt with C-17 but no pre-printed table still fails C-19.
