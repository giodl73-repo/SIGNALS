## Quest Score — org-build Round 6, V-01

### Scoring V-01 (Lifecycle Emphasis)

> **Note:** V-02 through V-05 are referenced in the hypothesis framing but not provided. Scoring V-01 only. Phase T4 is referenced in the hypothesis ("natural home for pre-print skeleton at Phase T4") but absent from the prompt — criteria that depend on org-chart.md content are evaluated on what is present.

---

### Essential Criteria (C-01 – C-05)

| ID | Verdict | Evidence |
|----|---------|----------|
| **C-01** | **FAIL** | `org-chart.md` named as an artifact set but content is unspecified. No Phase T4 instruction for ASCII hierarchy. "Craftworks-format org chart" is not a substitute for explicit format instruction. |
| **C-02** | **PASS** | Phase T3 enumerates all five fields (`orientation`, `lens`, `expertise`, `scope`, `collaborates_with`) and adds `FORBIDDEN: emitting any role file missing any of the five fields` and `FORBIDDEN: merging two fields into one`. |
| **C-03** | **PASS** | `MUST create .craft/roles/{area}/inertia-advocate.md` + `FORBIDDEN: omitting this role under any condition`. Both arms present. |
| **C-04** | **PASS** | 20–30 (standard) and 50+ (deep) bounds both stated. Both underflow and overflow FORBIDDENed. |
| **C-05** | **FAIL** | No instruction for a headcount-by-area table. No mention of `Decides` / `Escalates` columns anywhere in T1–T3. |

**Essential: 3 / 5 → 36 pts**

---

### Recommended Criteria (C-06 – C-08)

| ID | Verdict | Evidence |
|----|---------|----------|
| **C-06** | **PASS** | Phase T3: `MUST group all role files under minimum 2 area subdirectories` + `FORBIDDEN: placing all roles flat`. |
| **C-07** | **FAIL** | Operating rhythm table and committee charters not mentioned in any T1–T3 phase. |
| **C-08** | **PARTIAL** | T2-A/B compute T2-PRESSURE and T2-VERDICT with closed-set values. But no instruction writes `FLAT-CASE-PRESSURE:` to `org-chart.md`. The variables are gate-recorded, not org-chart-emitted. Pass requires the artifact to contain the rating. |

**Recommended: 1 / 3 → 10 pts**

---

### Aspirational Criteria (C-09 – C-22)

| ID | Verdict | Evidence |
|----|---------|----------|
| **C-09** | **FAIL** | Org Evolution Roadmap not present anywhere in T1–T3. |
| **C-10** | **PARTIAL** | T2-D specifies which category codes are required per verdict path using MUST/FORBIDDEN. But no instruction for the `[element name] (cat-N) —` citation syntax in the Anti-Pattern Watch table cells. Imperative register present; format requirement absent. |
| **C-11** | **PASS** | T2-C maps T2-PRESSURE → T2-IA-SCOPE via explicit table. T3 requires `scope = T2-IA-SCOPE verbatim` for inertia-advocate. Cross-phase derivation chain is closed. |
| **C-12** | **PASS** | T2-D explicitly derives T2-CATEGORIES-SET from T2-VERDICT (structural decision) and names the mapping: CAN-OPERATE-FLAT → {cat-2, cat-3}; STRUCTURE-WARRANTED → {cat-1, cat-4}. |
| **C-13** | **PASS** | T2-B: "Only one verdict. Both is an error. Neither is an error." Explicit error framing present. |
| **C-14** | **PASS** | T1 output contract table → T2 input contract names T1-TEAM-SIZE, T1-FLAG-DEEP, T1-DOMAIN with MUST. T2 output contract table → T3 input contract names T2-VERDICT, T2-PRESSURE, T2-IA-SCOPE, T2-CATEGORIES-SET with MUST. At least one producing-consuming pair with named typed variable and MUST declaration. |
| **C-15** | **PASS** | T2-B: `FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED` + `FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED`. Symmetric bidirectional guard. |
| **C-16** | **FAIL** | No Anti-Pattern Watch table in T1–T3. No Mitigation cells to evaluate. |
| **C-17** | **PASS** | T2: `FORBIDDEN: paraphrasing the template text. FORBIDDEN: composing new scope text. FORBIDDEN: adapting or abbreviating.` T3: `MUST set the scope field to T2-IA-SCOPE verbatim. FORBIDDEN: writing any text other than T2-IA-SCOPE.` Multiple layers of verbatim enforcement. |
| **C-18** | **PASS** | T2-D states both the required path and the forbidden path per verdict: CAN-OPERATE-FLAT forbids cat-1/cat-4 by name; STRUCTURE-WARRANTED forbids cat-2/cat-3 by name. |
| **C-19** | **PASS** | Every constraint in T1–T3 uses MUST or FORBIDDEN. No "should", "prefer", "typically", "consider" found in constraint contexts across all three phases. |
| **C-20** | **PARTIAL** | All three phase gates have output contract tables with typed variables ✓. T2 and T3 open with explicit input contracts ✓. Gap: T1-REPO-COUNT is declared in T1's output contract but never appears in T2 or T3 input contracts — dangling output, no consuming phase names it. T2-CATEGORIES-FORBIDDEN produced in T2 but not named in T3's input contract (governed within T2 itself, not downstream). Systematic coverage is not complete. |
| **C-21** | **FAIL** | T1-REPO-COUNT is a named typed output variable with no downstream consuming phase — its governance is unverifiable. T2-CATEGORIES-FORBIDDEN is consumed within T2 itself (T2-D), not in a downstream input contract. The intersection of C-19 and C-20 cannot be verified for either variable. C-21 requires the constraint to appear in the *consuming phase's input contract*; same-phase enforcement does not satisfy "downstream." |
| **C-22** | **FAIL** | Record blocks (`T2-PRESSURE: [value]`) capture gate variable values but are not artifact skeletons. The role file schema is a template, but its `scope:` slot uses descriptive text (`[operational boundaries and decision authority]`) rather than a named gate variable placeholder (`{{T2-IA-SCOPE}}`). No skeleton for `org-chart.md` exists with slots keyed to T2-PRESSURE or T2-VERDICT. |

**Aspirational passes: C-11, C-12, C-13, C-14, C-15, C-17, C-18, C-19 → 8 / 14**

**Aspirational: 8/14 × 10 = 5.71 pts**

---

### Score Summary

```
composite = (3/5 × 60) + (1/3 × 30) + (8/14 × 10)
          = 36 + 10 + 5.71
          = 51.7 → 52
```

| Section | Pass | Weight | Points |
|---------|------|--------|--------|
| Essential | 3/5 | 60 | 36.0 |
| Recommended | 1/3 | 30 | 10.0 |
| Aspirational | 8/14 | 10 | 5.7 |
| **Total** | | | **51.7** |

---

### Excellence Signals from V-01

**Phase-execution ordering constraint** — `FORBIDDEN: beginning a phase before recording all output variables of the preceding phase` is a new temporal enforcement pattern. Prior rounds had gate variable contracts but no explicit prohibition on out-of-order execution. This closes a model compliance gap independently of the contract content.

**Record-block checkpoint** — Requiring the model to emit a named record block (`T1-DOMAIN: [value]`) before any phase transition creates a structural checkpoint artifact. This is distinct from just having input/output contract tables — it forces materialization of gate variable values into text before the next phase reads them, making the gate boundary observable and auditable.

**Symmetric typed input/output contract tables** — Using the same table format (Variable / Type / Description) at both ends of a phase gate creates a typed schema handshake. The producing phase's output table rows should match the consuming phase's input contract rows by variable name. When they do not (T1-REPO-COUNT gap, T2-CATEGORIES-FORBIDDEN gap), the asymmetry is immediately visible — a diagnostic advantage V-01 enables.

---

### Gap Analysis for R7

The two v5 criteria remain unresolved:

**C-21 gap** — T1-REPO-COUNT is a declared output that flows nowhere. Either remove it from T1's output contract or add it to T2's input contract with an explicit MUST/FORBIDDEN governing how it informs T2-VERDICT derivation. T2-CATEGORIES-FORBIDDEN needs a Phase T3 input contract entry with MUST/FORBIDDEN (not just same-phase enforcement in T2-D).

**C-22 gap** — Phase T4 (referenced in V-01's hypothesis but absent) is the natural home. A pre-print skeleton for `org-chart.md` must show named placeholder slots: `FLAT-CASE-PRESSURE: {{T2-PRESSURE}}`, `VERDICT: {{T2-VERDICT}}`, `INERTIA-ADVOCATE SCOPE: {{T2-IA-SCOPE}}`. Record blocks are not artifact skeletons.

**Baseline gaps (C-01, C-05, C-07, C-08, C-09, C-16)** — All require Phase T4 for org-chart.md content, headcount table, rhythm table, inertia assessment block, evolution roadmap, and anti-pattern table. V-01 deliberately stops at T3. A complete prompt needs all four phases.

---

```json
{"top_score": 52, "all_essential_pass": false, "new_patterns": ["phase-execution-ordering-constraint: FORBIDDEN beginning a phase before recording all output variables of the preceding phase — enforces gate temporal order at the process level, not just the schema level", "record-block-checkpoint: explicit materialized record block after each phase gate forces gate variable values into text before the next phase reads them, making gate boundaries auditable and gap-visible"]}
```
