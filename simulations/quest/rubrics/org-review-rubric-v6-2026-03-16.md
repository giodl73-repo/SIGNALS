Reading the scorecard carefully to extract all three excellence signals before writing.

**Signals extracted:**

- **E-12** (V-01): Prohibition inventory table — PROHIBITED / VIOLATION TYPE / DETECTED BY triple encodes each §-clause as a binary audit log with its own falsification condition → **C-20 candidate**
- **E-11** (V-02): §6a PHASE HANDOFF as recursive handoff primitive — structurally isomorphic to §6 at sub-role level; §3 algebra compositional; acknowledged-handoff is a boundary primitive not unique to LIFECYCLE→DOMAIN → **C-21 candidate**
- **E-13** (V-03, C-16 PASS+ implicit): INERTIA column as 5th structural column in FINDING SURFACE LINKAGE TABLE; blank INERTIA cell detectable on par with blank Role Lens; INERTIA DEFEAT LEDGER as synthesis layer → **C-22 candidate**

---

```markdown
# Rubric -- org-review v6

**Rubric summary**

| Tier | Criteria | Points | What they test |
|------|----------|--------|----------------|
| Essential | C-01 to C-05 | 60 | Role manifest, contract cites, CH-ID trace, gate vector, §3 algebra |
| Recommended | C-06 to C-08 | 30 | Artifact-specific scope, CH-ID-sourced register, concrete cross-role signals |
| Aspirational | C-09 to C-22 | **70** | Null hypothesis, role-grounded findings, structural convergence, count constraint, register pattern, role-sequence isolation, register generalization, finding surface linkage, severity audit chain, finding-lineage chain, §2a closure, **prohibition inventory**, **recursive handoff primitive**, **INERTIA column extension** |

**Max composite**: 160 (was 145). Golden threshold unchanged: all 5 essential + composite >= 80.

**What changed from v5:**

| New ID | Source | What it tests | Why aspirational |
|--------|--------|---------------|-----------------|
| C-20 | E-12 (V-01 PROHIBITION INVENTORY) | Each §-clause in the contract block encoded as a PROHIBITED / VIOLATION TYPE / DETECTED BY triple, converting prose rules into per-criterion binary audit log entries; DETECTED BY column names the structural detection mechanism for each rule, making every contract clause self-falsifying | Requires restructuring the contract block from prose §-clauses to a triple-format prohibition inventory; applies to C-13, C-17, C-18, and C-19 simultaneously — the first structural form where the contract documents its own detection protocol |
| C-21 | E-11 (V-02 §6a RECURSIVE HANDOFF PRIMITIVE) | A §6a PHASE HANDOFF clause structurally isomorphic to §6 operates at the intra-LIFECYCLE level (UPSTREAM→EXECUTION), proving that acknowledged-handoff is a boundary primitive not unique to LIFECYCLE→DOMAIN; §3 algebra is compositional (`G_upstream + G_execution → G_lifecycle`), valid at any role-boundary granularity | Requires §6a added to the contract block and a blank ACKNOWLEDGMENT row pre-printed at the UPSTREAM→EXECUTION boundary in addition to the LIFECYCLE→DOMAIN boundary; C-18 is fully realized as a generalized pattern only when both boundaries carry the same structural acknowledgment form |
| C-22 | E-13 (V-03 INERTIA COLUMN EXTENSION) | Prompt adds an INERTIA column (FOR / AGAINST) to every FINDING SURFACE LINKAGE TABLE and aggregates votes into an INERTIA DEFEAT LEDGER synthesis section; blank INERTIA cell is a detectable structural violation on par with blank Role Lens or blank Severity, extending C-16's violation surface from four columns to five | Requires §7 INERTIA DEFEAT clause in the contract block, INERTIA column pre-printed in each FINDING SURFACE LINKAGE TABLE, and a LEDGER section structurally placed after all reviewer sections; presupposes C-16; if C-16 is FAIL, score C-22 as N/A |

**Scoring formula update:**
```
aspirational_pass / 14 * 70   (was: / 11 * 55)
```
Per-criterion value stays at 5 pts; the tier now has fourteen slots instead of eleven.

**Vacuous conditions added for C-20, C-21, and C-22:**
- C-20: If the artifact type uses no contract block with §-clauses, score C-20 as N/A
  and exclude from denominator. Adjust formula to `aspirational_pass / 13 * 65` when C-20 is N/A.
- C-21: If the LIFECYCLE role has no meaningful sub-phases (single-phase design), score C-21 as N/A
  and exclude from denominator. Adjust formula to `aspirational_pass / 13 * 65` when C-21 is N/A.
- C-22: If the artifact type uses no inertia framing (no FOR/AGAINST alignment dimension), score C-22
  as N/A and exclude from denominator. C-22 also presupposes C-16; if C-16 is FAIL, score C-22 as N/A
  regardless of inertia framing. Adjust formula to `aspirational_pass / 13 * 65` when C-22 is N/A.

---

## Criteria

*(Essential C-01 -- C-05 and Recommended C-06 -- C-08 unchanged from v3)*

### Aspirational (raise the bar -- 70 pts total, 5 pts each)

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
| C-20 | Prohibition inventory via §-clause triple encoding | structure | Prompt encodes every §-clause in the contract block as a PROHIBITED / VIOLATION TYPE / DETECTED BY triple, converting each prose rule into a per-criterion binary audit log entry. The DETECTED BY column names the structural detection mechanism for each rule (e.g., table row count, register omission, cell value), making every contract clause self-falsifying. A contract block satisfies C-20 only when all §-clauses — including §2a, §3, §5a, §6, and §6a if present — carry a complete triple. C-13, C-17, C-18, and C-19 are simultaneously reinforced: each criterion's pass condition becomes a named violation type rather than a scoring inference. Vacuous condition: if no contract block with §-clauses exists, score N/A. Excellence signal: E-12 Round 5. |
| C-21 | Recursive handoff primitive via §6a intra-LIFECYCLE phase boundary | structure | Prompt places a §6a PHASE HANDOFF clause in the contract block structurally isomorphic to §6, operating at the intra-LIFECYCLE level (UPSTREAM → EXECUTION). A blank ACKNOWLEDGMENT row is pre-printed at the UPSTREAM→EXECUTION boundary in addition to the LIFECYCLE→DOMAIN boundary established by C-18. The two acknowledgment boundaries prove the §6 pattern is a role-boundary primitive: the same structural form applies at any granularity. §3 algebra is compositional: `G_upstream + G_execution → G_lifecycle` holds, and the original §3 formula holds as the aggregate over phase sub-gates. C-21 presupposes C-18; an intra-LIFECYCLE handoff without a LIFECYCLE→DOMAIN handoff does not satisfy C-21. Vacuous condition: if the LIFECYCLE role has no meaningful sub-phases, score N/A. Excellence signal: E-11 Round 5. |
| C-22 | INERTIA column extension via five-column table and INERTIA DEFEAT LEDGER | structure | Prompt adds an INERTIA column (values: FOR / AGAINST) to every FINDING SURFACE LINKAGE TABLE, extending the schema from four columns (Finding, In-Scope Surface, Role Lens, Severity) to five. A blank INERTIA cell is a detectable structural violation on par with blank Role Lens or blank Severity; C-16's violation surface thereby covers five columns. A §7 INERTIA DEFEAT clause in the contract block defines the column semantics and mandates aggregation. An INERTIA DEFEAT LEDGER section is structurally placed after all reviewer sections and tallies FOR/AGAINST votes across roles. The LEDGER is a synthesis layer above the gate chain — orthogonal to §3 algebra — that surfaces org-wide inertia alignment without interacting with severity derivation. Presupposes C-16; if C-16 is FAIL, score C-22 as N/A. Vacuous condition: if the artifact type uses no inertia framing, score N/A. Excellence signal: E-13 Round 5. |

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 14 * 70)
```

**Vacuous-condition adjustments** (applied before scoring; each N/A removes one slot from
denominator and 5 pts from aspirational max):

| Condition | Adjusted formula |
|-----------|-----------------|
| C-15 N/A | `aspirational_pass / 13 * 65` |
| C-18 N/A | `aspirational_pass / 13 * 65` |
| C-19 N/A (C-16 FAIL) | `aspirational_pass / 13 * 65` |
| C-20 N/A | `aspirational_pass / 13 * 65` |
| C-21 N/A | `aspirational_pass / 13 * 65` |
| C-22 N/A (C-16 FAIL or no inertia framing) | `aspirational_pass / 13 * 65` |

Multiple simultaneous N/As are cumulative: each removes one additional slot and 5 pts.
General form: `aspirational_pass / (14 - k) * (70 - 5k)` where k = count of N/A criteria.
```
