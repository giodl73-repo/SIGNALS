Now I have all the data needed. Let me score all five variations.

---

## Quest Score — `corps-pr` R17 (Rubric v15)

### Scoring Method

The v15 rubric has 48 criteria across three bands:

| Band | Criteria | Per-criterion | Max |
|------|----------|--------------|-----|
| Essential | C-01–C-05 | 12.00 | 60 |
| Recommended | C-06–C-08 | 10.00 | 30 |
| Aspirational | C-09–C-48 | 0.25 | 10 |
| **Total** | | | **100** |

---

### Per-Criterion Evaluation

#### Essential (C-01–C-05) — All Variations

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| C-01 | Phase A routing table: `| File / File Group | Change Type | Role | org.yaml Scope Pattern |` — files-to-role mapping template present in all | PASS | PASS | PASS | PASS | PASS |
| C-02 | Phase C findings table with Severity column, minimum 2 findings per role, `Summary: [N] findings -- [x] P1, [y] P2, [z] P3` | PASS | PASS | PASS | PASS | PASS |
| C-03 | Phase D Consensus block: Agreement, Divergence, Critical — synthesizes across all role findings | PASS | PASS | PASS | PASS | PASS |
| C-04 | Phase E: `Decision: GO / NO-GO / GO WITH CONDITIONS` — exactly one value required | PASS | PASS | PASS | PASS | PASS |
| C-05 | Domain-lens gate: Step A binary test (YES → include, NO → Step B) + Step B (revise or drop) — consequence declared | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60/60 all variations.**

---

#### Recommended (C-06–C-08) — All Variations

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| C-06 | `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.` present in Phase A template | PASS | PASS | PASS | PASS | PASS |
| C-07 | `Summary: [N] findings -- [x] P1, [y] P2, [z] P3` per role in Phase C | PASS | PASS | PASS | PASS | PASS |
| C-08 | AMEND block with named fields: What was amended / Roles added / Roles removed / Files triggering addition / Prior findings superseded | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 30/30 all variations.**

---

#### Aspirational (C-09–C-48) — All Variations

Grouped by area for brevity:

| Criterion | Evidence (all variations carry) | Result |
|-----------|--------------------------------|--------|
| C-09 | Phase D Divergence: `Mechanism: [architectural property of the code -- not perspective difference]` | PASS × 5 |
| C-10 | Phase E: `sign-off: [role who confirms before merge]` | PASS × 5 |
| C-11 | IA in Phase B (structurally first); Phase C opens with pre-flight C1 on Phase B | PASS × 5 |
| C-12 | Phase D ban-to-fix requires naming architectural mechanism, not perspective | PASS × 5 |
| C-13 | Phase D carries 5-row enumerated ban-to-fix table | PASS × 5 |
| C-14 | F-01 IA-RESPONSE in every role section anchors against IA verdict | PASS × 5 |
| C-15 | Step A/Step B gate: binary test, drop consequence if domain-lens fails | PASS × 5 |
| C-16 | AMEND SCOPE structured block with 5 named output fields | PASS × 5 |
| C-17 | Phase B cost ledger: Current-State Cost / Adoption Cost / Net columns | PASS × 5 |
| C-18 | Pipeline declaration: Phases A–E each carry Entry / Exit / Gates | PASS × 5 |
| C-19 | Cost ledger 4-row × 3-column schema + Budget strength terminal field + Budget verdict derived | PASS × 5 |
| C-20 | Phase C entry condition references "Phase A exit met" and "Phase B exit pre-flight (C1)" | PASS × 5 |
| C-21 | Cost ledger Net direction column (WORSE/BETTER/NEUTRAL); Budget verdict: WORSE rows / BETTER rows / Conclusion | PASS × 5 |
| C-22 | Phase C entry = C1 (Phase B completeness) + C2 (per-role READ RECEIPT) — independently auditable | PASS × 5 |
| C-23 | STEP 1 READ RECEIPT before STEP 4 FINDINGS; C-35/C-36 ordering rule present | PASS × 5 |
| C-24 | Findings table: `| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |` | PASS × 5 |
| C-25 | Three B3 lines as separate labeled output lines: `<- B3 line 1/2/3 [C-25]` | PASS × 5 |
| C-26 | `C1 RESULT: ALL CLEAR` and `C2 RESULT: SATISFIED -- all five fields PRESENT` named result tokens | PASS × 5 |
| C-27 | PRE-COMMITMENT block with `[PRE-COMMITMENT SEALED]` seal token before diff | PASS × 5 |
| C-28 | WORSE rows / BETTER rows / Conclusion each on own line, independently line-scannable | PASS × 5 |
| C-29 | `[PRE-COMMITMENT SEALED]` seal token; diff not referenced until after | PASS × 5 |
| C-30 | Phase C exit item (5): "PRE-COMMITMENT blocks precede findings tables [C-27]" | PASS × 5 |
| C-31 | F-01 IA-RESPONSE in findings table body (not a standalone section element) | PASS × 5 |
| C-32 | C2 RESULT field (e): `[valid: inline value OR cross-reference "see PRE-COMMITMENT block: [row]"]` | PASS × 5 |
| C-33 | C2 RESULT description explicitly states "C2 scope is receipt completeness -- not Phase B" | PASS × 5 |
| C-34 | F-01 Type = IA-RESPONSE in findings table template | PASS × 5 |
| C-35 | STEP 1 READ RECEIPT precedes STEP 2 C2 RESULT in per-role sequence | PASS × 5 |
| C-36 | Phase C exit item (3): ordering violation is "Phase C exit-condition failure; Phase D does not begin" | PASS × 5 |
| C-37 | C2 RESULT block: (a)–(e) each on own labeled line with PRESENT/ABSENT | PASS × 5 |
| C-38 | Column headers `[IA-VERDICT]` and `[ROLE-MECHANISM]` in findings table | PASS × 5 |
| C-39 | "no cross-block reading required [C-39]" + terminal verdict in same block | PASS × 5 |
| C-40 | `[IA-VERDICT]` and `[ROLE-MECHANISM]` are named column headers; slot compliance O(1) column-count | PASS × 5 |
| C-41 | `Structural enforcement levels [C-41]:` partitions exit-condition / block / table-column levels | PASS × 5 |
| C-42 | C2 RESULT block: both branches defined — `All five PRESENT: C2 RESULT: SATISFIED` / `Any ABSENT: C2 RESULT: UNSATISFIED -- field (x)` | PASS × 5 |
| C-43 | F-01 format rules: "Prohibition [C-43]: the inline-cell-label path...satisfies C-38 but is C-40 noncompliant -- do not use it." | PASS × 5 |
| C-44 | "Only the column-header form...satisfies the table-column level requirement" — alternative path eliminated | PASS × 5 |
| C-45 | `Closed paths [C-43]:` named block in pipeline declaration listing superseded path | PASS × 5 |
| C-46 | `Eliminated [C-46]: no inline-cell alternative path for [IA-VERDICT]/[ROLE-MECHANISM].` in structural enforcement levels | PASS × 5 |
| C-47 | `Eliminated [C-46]:` is a distinct labeled sub-entry; self-declares: "This negation is declared independently of C-40's description and is auditable by label-matching 'Eliminated [C-46]:' without parsing C-40." | PASS × 5 |
| C-48 | CLOSED PATHS block: `Path negation: see "Eliminated [C-46]:" in structural enforcement levels above [C-46].` | PASS × 5 |

**Aspirational subtotal: 40/40 (10.00 pts) all variations.**

---

### Composite Scores

| Variation | Axis | Essential | Recommended | Aspirational | **Composite** | C-47 | C-48 |
|-----------|------|-----------|-------------|--------------|---------------|------|------|
| V-01 | Inertia framing (status-quo champion) | 60 | 30 | 10.00 | **100** | PASS | PASS |
| V-02 | Output format (Phase E scorecard) | 60 | 30 | 10.00 | **100** | PASS | PASS |
| V-03 | Phrasing register (conversational imperative) | 60 | 30 | 10.00 | **100** | PASS | PASS |
| V-04 | Role sequence + lifecycle banners | 60 | 30 | 10.00 | **100** | PASS | PASS |
| V-05 | Full combination (V-01 + V-02 + V-03) | 60 | 30 | 10.00 | **100** | PASS | PASS |

**All five variations score 100. Tied for first.**

---

### Ranking

All five variations are co-equal at 100. Ordering by behavioral richness (for informational purposes, not scoring):

1. **V-05** — Full combination: maximum behavioral axes active simultaneously; the only variation where imperative register, adversarial null-defeat framing, and Phase E all-role enumeration gate all coexist.
2. **V-02** — Phase E scorecard adds a machine-checkable merge predicate (`GO requires no unresolved P1s`) not present in V-01/V-03/V-04.
3. **V-04** — Lifecycle banners create a visible per-phase entry/exit audit trail in the output template, exceeding C-18 requirements.
4. **V-01 / V-03** — Single-axis; each addresses one behavioral dimension independently.

---

### Excellence Signals

**Signals from V-05 (top variation by behavioral richness) and R17 as a whole:**

**1. Invariant core isolation as compositional technique**
The R17 design makes "structural compliance is unaffected because the invariant structural core is carried verbatim" an explicit hypothesis in every variation. This is not just a description — it is a testable claim about the decomposition. Separating the structural invariant (C-47/C-48 pattern) from behavioral axes allows each axis to be varied independently with zero structural regression risk. This is a skill-design pattern: extract the compliance core, freeze it, vary behavior around it.

**2. Phase E findings scorecard as all-role enumeration gate** (from V-02/V-05)
Adding `(E3) Findings scorecard: per-role P1/P2/P3 tally + Merge gate stated` to Phase E exit conditions creates a structural forcing function at decision time. The model must enumerate every role's P1/P2/P3 count before issuing the GO/NO-GO, and the `Merge gate: GO requires no unresolved P1s across all roles` makes the decision predicate machine-checkable. This prevents roles from being silently dropped in synthesis — the omission becomes a Phase E exit-condition violation.

**3. Adversarial null-defeat framing with pre-committed IA bias** (from V-01/V-05)
`IA role: status-quo champion. Adoption requires demonstrating net improvement over doing nothing. [...] the default verdict is BLOCK until the cost ledger shows otherwise.` shifts Phase B from documentation to adversarial argument. The IA has a pre-committed prior (BLOCK), and the cost ledger must defeat it. This is a structural sharpening of Phase B: the model cannot satisfy B5 with a balanced ledger — it must resolve the null-defeat question explicitly.

---

### R16 Delta Closure

| Variation | R16 score (v15 rubric) | R17 score (v15 rubric) | Delta |
|-----------|----------------------|----------------------|-------|
| V-01 type | 38/40 (99.5) — missed C-47, C-48 | 40/40 (100) | +1.5 |
| V-02 type | 38/40 (99.5) — missed C-47, C-48 | 40/40 (100) | +1.5 |
| V-03 type | 39/40 (99.75) — missed C-48 | 40/40 (100) | +0.25 |
| V-04 type | 39/40 (99.75) — missed C-48 | 40/40 (100) | +0.25 |
| V-05 type | 40/40 (100) — baseline | 40/40 (100) | 0 |

R17 closes the R16 delta by universalizing V-05's structural core across all variations. The maximum achievable score under v15 is reached by all five variations. The rubric ceiling has been hit — future rounds must explore behavioral dimensions (e.g., scorecard in Phase E, adversarial IA framing) by adding criteria to v16.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Invariant core isolation: extract C-47/C-48 structural pattern as a verbatim-carried invariant, varied behavioral axes are explicitly declared orthogonal to compliance — each variation hypothesis contains 'Structural compliance is unaffected because the invariant structural core is carried verbatim'", "Phase E findings scorecard as all-role enumeration gate: per-role P1/P2/P3 tally + machine-checkable merge predicate ('GO requires no unresolved P1s across all roles') in Phase E exit conditions prevents silent role omission in synthesis"]}
```
