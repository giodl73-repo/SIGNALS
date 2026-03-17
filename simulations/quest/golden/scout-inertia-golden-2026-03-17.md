Written to `simulations/quest/golden/scout-inertia-golden-2026-03-17.md`.

**Document structure:**
- Frontmatter: all required fields (rounds: 20, rubric_final: v21, score: 10.0, status: GOLDEN)
- Source note: R20 V-04 + QU5 simplification (777 words, PASS)
- **What Made It Golden** — 5 patterns:
  1. Q-ID coherence loop fully closed (C-59)
  2. Audit-traceable domain-prefix labels with distinct `[A-NN]` citations (C-60)
  3. Per-position label distinctness via Q-IDs (C-61) — contrasts with V-01 and V-02 failure modes
  4. Two-population structural design (bridge vs domain-prefix populations)
  5. Simplification left all 53 criteria intact (QU5 PASS)
- Exact simplified prompt body (verbatim from QU5 output)
- Rubric criteria summary: bridge-command chain (C-41/C-58/C-61/C-59), domain-prefix chain (C-42/C-46/C-58/C-60), and R20 score table
ring-point label (C-59). An author at any position can locate the Q-ID in the label notation
alone without reading surrounding context.

**2. Audit-traceable domain-prefix labels (C-60)**
Each non-bridge domain-prefix label carries a distinct trailing `[A-NN]` citation:
`INERTIA THREAT FAIL-FIRST RULE [A-31]` / `INERTIA THREAT RULE [A-16]` /
`INERTIA THREAT CITATION RULE [A-19]`. An evaluator scanning for the governing rule finds it in
the label bracket without reading the label body. The three citations are distinct across all three
labels.

**3. Per-position label distinctness (C-61)**
`[BRIDGE Q3 COMMAND]:` and `[BRIDGE Q4 COMMAND]:` are inherently distinct (Q3 != Q4), satisfying
C-61 automatically. This separates the golden form from V-01's generic `[BRIDGE COMMAND]:` (C-61
FAIL) and V-02's class-vocab `[BRIDGE ACTOR COMMAND]:` / `[BRIDGE TRIGGER COMMAND]:` (C-61 PASS,
C-59 FAIL). Q-ID labels are the only form satisfying all four bridge-command criteria simultaneously:
C-41 (count) + C-58 (vocabulary class) + C-61 (per-position distinctness) + C-59 (Q-ID
incorporation).

**4. Two-population structural design**
Bridge positions use `[BRIDGE Qn COMMAND]:` labels (satisfying C-41/C-58/C-61/C-59). Non-bridge
positions use `INERTIA THREAT ... [A-NN]` domain-prefix labels (satisfying C-42/C-46/C-58/C-60).
The two populations are positionally segregated and structurally non-overlapping. No label crosses
its population boundary.

**5. Simplification did not touch any structural criterion (QU5 PASS)**
The 196-word reduction (20.1%) removed only prose with zero criterion dependency: FAIL-FIRST body
prose, bridge artifact listing in the FAIL-FIRST section, `(closes ...)` annotations, VERIFY and
QUANTIFY guidance clauses, gate trailing sentence, `[UNIT RULE]` block, "home-field advantage"
phrase, redundant DO NOT clause, `(current workaround)` parenthetical, and example in the
Failure description column header. All 53 criteria pass at the same score (10.00) after
simplification.

---

## Prompt Body

```
## FAIL-FIRST DECLARATION -- THE INERTIA THREAT

INERTIA THREAT FAIL-FIRST RULE [A-31]: The failure surface comes first. Failure modes
before defeat conditions.

---

## SECTION 1 -- FAILURE MODE INVENTORY

> [C-05 COMMAND]: NAME every specific failure mode where the inertia threat
> breaks, produces errors, causes rework, or hits a scale ceiling. ASSIGN an
> FM-[N] identifier to each row. MINIMUM 2 rows. REJECT generic descriptions -- "slow" or
> "manual" alone fails; "CSV export silently truncates rows at 65,536 with no error message"
> passes.

> **INERTIA THREAT RULE [A-16]**: ASSIGN all FM-[N] identifiers here first. NO FM-[N]
> reference may appear in any later section without a corresponding row assigned in this
> table. The failure surface inventory is the sole source of FM identifiers.

| FM-[N] | Failure description | Actor / role (e.g., data-ops team) | Trigger (e.g., file > 10MB) | Frequency (e.g., 2x/sprint) |
|--------|--------------------|------------------------------------|-----------------------------|------------------------------|
| FM-1   |                    |                                    |                             |                              |
| FM-2   |                    |                                    |                             |                              |

---

## Q3 -- FM->ACTOR BRIDGE

[BRIDGE Q3 COMMAND]: MAP each FM-[N] to the specific role experiencing the failure.

| FM-[N] | Actor / role (e.g., data-ops team) | Role-level impact |
|--------|------------------------------------|-------------------|
| FM-1   |                                    |                   |
| FM-2   |                                    |                   |

---

## Q4 -- FM->TRIGGER BRIDGE

[BRIDGE Q4 COMMAND]: MAP each FM-[N] to its triggering condition.

| FM-[N] | Triggering condition (e.g., pipeline ingests file > 10MB) | Measurable threshold (e.g., >10MB, >3 failures/week) |
|--------|-----------------------------------------------------------|------------------------------------------------------|
| FM-1   |                                                           |                                                      |
| FM-2   |                                                           |                                                      |

---

## BRIDGE COMPLETION GATE -- PASS BEFORE ADVANCING -- HAVE BOTH Q3 (FM->ACTOR BRIDGE) AND Q4 (FM->TRIGGER BRIDGE) BEEN POPULATED?

[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING SECTIONS 2
THROUGH 5. IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE
ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE
THE TRIGGER MAPPING.

| Bridge artifact          | Populated? (Y / N) |
|--------------------------|--------------------|
| Q3 -- FM->Actor bridge   |                    |
| Q4 -- FM->Trigger bridge |                    |

---

## SECTION 2 -- WORKAROUND PROFILE

> [C-01 COMMAND]: NAME the specific inertia threat -- the exact tool name, file type, or
> procedure. NOT "a manual process." NAME the role performing it. QUANTIFY the ongoing cost
> with a number and a unit.

| Workaround name (specific: tool / file type / procedure) | Role performing it | Ongoing cost (e.g., 2 hours/week) | Duration in active use (e.g., 18 months) |
|----------------------------------------------------------|--------------------|-----------------------------------|------------------------------------------|
|                                                          |                    |                                   |                                          |

---

## SECTION 3 -- SWITCHING COST

> [C-02 COMMAND]: IDENTIFY at least two switching cost categories. QUANTIFY each with a
> number and a unit. NAME the role bearing each cost. REJECT any estimate without a number
> and unit.

| Cost category          | Description | Estimate (e.g., 3 days) | Role bearing it (e.g., data-ops team) |
|------------------------|-------------|-------------------------|---------------------------------------|
| Migration effort       |             |                         |                                       |
| Training overhead      |             |                         |                                       |
| Process disruption     |             |                         |                                       |
| In-flight work at risk |             |                         |                                       |

---

## SECTION 4 -- THREAT ASSESSMENT

> [C-03 COMMAND]: DECLARE the inertia threat score. DEFAULT IS HIGH. IF deviating from HIGH,
> STATE a specific quantified condition; a qualitative judgment ("low friction") is REJECTED.

| Inertia threat score (HIGH / MEDIUM / LOW) | Justification if not HIGH |
|--------------------------------------------|---------------------------|
|                                            |                           |

---

## SECTION 5 -- DEFEAT CONDITIONS

> [C-04 COMMAND]: DERIVE at least two specific, falsifiable defeat conditions from the Q4
> trigger mapping. CITE the FM-[N] driving each condition. EVERY DC row must name a testable,
> measurable condition -- "teams switch when they see the value" is REJECTED.

> **INERTIA THREAT CITATION RULE [A-19]**: EVERY FM-[N] cited in this table MUST have an
> assigned row in Section 1 (FM Inventory). VERIFY before filling each row.

| DC-[N] | Defeat condition (falsifiable) | FM-[N] driving it | Measurable threshold (e.g., >10MB, >3 failures/week) | Team type or segment |
|--------|-------------------------------|-------------------|------------------------------------------------------|----------------------|
| DC-1   |                               |                   |                                                      |                      |
| DC-2   |                               |                   |                                                      |                      |

---

## COMPLETENESS CHECK

| Criterion                                                                                      | Check (Y / N) |
|------------------------------------------------------------------------------------------------|---------------|
| C-01: Workaround named specifically with role and ongoing cost (number + unit)                 |               |
| C-02: At least two switching cost categories, each quantified with number and unit             |               |
| C-03: Inertia threat score declared (HIGH by default; deviation requires quantified condition) |               |
| C-04: At least two defeat conditions, each falsifiable, each citing FM-[N] from Section 1     |               |
| C-05: At least two specific, non-generic failure modes in Section 1                            |               |
```

---

## Final Rubric Criteria Summary

**Rubric**: v21 | **Denominator**: 53 | **Formula**: `aspirational_pass / 53 * 10`

### Bridge-command label chain (4 criteria)

| Criterion | Requirement | Golden form |
|-----------|-------------|-------------|
| C-41 | One bracket command per artifact at each artifact's bridge authoring position | `[BRIDGE Q3 COMMAND]:` at Q3 section; `[BRIDGE Q4 COMMAND]:` at Q4 section |
| C-58 | Bridge-command vocabulary at bridge positions; domain-prefix vocabulary confined to non-bridge positions | `[BRIDGE ...]` labels at Q3/Q4 sections; `INERTIA THREAT ...` labels at sections 1/3/5 |
| C-61 | Bridge-command labels at distinct authoring positions are distinct from each other by notation | `Q3` != `Q4` -- inherently distinct |
| C-59 | Bridge-command label at each artifact's authoring position incorporates the artifact's Q-ID | `[BRIDGE Q3 COMMAND]:` contains `Q3`; `[BRIDGE Q4 COMMAND]:` contains `Q4` |

### Domain-prefix label chain (4 criteria)

| Criterion | Requirement | Golden form |
|-----------|-------------|-------------|
| C-42 | `INERTIA THREAT` domain vocabulary threads through all non-bridge domain-prefix labels | All three non-bridge labels share the `INERTIA THREAT` prefix |
| C-46 | Compound domain-axis vocabulary (domain prefix + structural-role axis) | `INERTIA THREAT` (domain) + `FAIL-FIRST RULE` / `RULE` / `CITATION RULE` (role axis) |
| C-58 | Domain-prefix labels confined to non-bridge positions (shared with bridge-command chain above) | Domain-prefix labels at sections 1/3/5 only |
| C-60 | Three distinct trailing `[A-NN]` citations on three vocabulary-threaded domain-prefix labels | `[A-31]` / `[A-16]` / `[A-19]` -- distinct across all three labels |

### Gate criteria (C-37, C-41, C-43--C-57): all carried from R19 V-04 baseline, unchanged.

### Content criteria (C-01--C-05): all five essential section commands present with full text.

### R20 score table

| V | v21 (53) | Score | Failure |
|---|----------|-------|---------|
| **V-04** | **53/53** | **10.00** | none |
| V-02 | 52/53 | 9.81 | C-59: class-vocab labels, no Q-ID |
| V-03 | 52/53 | 9.81 | C-60: absent trailing citations |
| V-01 | 51/53 | 9.62 | C-59 + C-61: generic identical labels |
| V-05 | 50/53 | 9.43 | C-59 + C-60 + C-61: triple fail |
