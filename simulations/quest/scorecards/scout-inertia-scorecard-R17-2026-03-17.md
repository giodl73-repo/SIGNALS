Now I have everything needed. Let me compose the scorecard.

---

## Quest Score — scout-inertia — Round 17 (v17)

---

### Rubric Orientation

**Denominator**: 46 (v16 base 45 + C-54)
**Formula**: aspirational_pass / 46 × 10
**Essential criteria**: C-01 through C-05
**Criterion under test**: C-54 — per-artifact parenthetical artifact-class annotation in gate body return routing (extends C-53)
**R16 baseline**: V-01/V-02/V-03/V-05 = 45/45; V-04 = 43/45 (C-42 FAIL + C-46 FAIL inherited)

---

### C-54 Criterion Reference

**Pass form**: Each conditional routing clause in the gate body annotates its named return target with a parenthetical artifact-class label. Both clauses carry the annotation, keyed per artifact: `Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N; return to Section 1B (FM->TRIGGER BRIDGE) if Q4 shows N.`

**Fail form** (R16 baseline): Bare return targets with no class annotation. `Return to Section 1A if Q3 shows N; return to Section 1B if Q4 shows N.` passes C-53 (per-artifact decomposition, distinct targets) but fails C-54 (return target carries no artifact-class annotation).

**Key distinctions**:
- C-54 requires the annotation to attach to the return target noun phrase inside the conditional clause. All R17 variations place it there directly — the most restrictive interpretation is satisfied.
- C-54 is register-agnostic: lowercase `(FM->ACTOR BRIDGE)` in V-01/V-02/V-03/V-04 and ALL-CAPS in V-05 are structurally equivalent. The criterion tests presence and placement, not case.
- C-54 is vocabulary-consistent: all variations echo the artifact-class labels already established in the bridge section headings — no new terms introduced.

---

### Variation-by-Variation Evaluation

---

#### V-01 — C-54 on section-based scaffold (Section 1A/1B form)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Essential templates present; all five criteria addressed |
| C-34 through C-53 | PASS (carried) | R16 V-01 = 45/45; single change in R17 is gate body routing annotation — heading criteria, bracket labels, checklist, staging, A-37 schema all unchanged |
| **C-54** | **PASS** | `Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N; return to Section 1B (FM->TRIGGER BRIDGE) if Q4 shows N.` — each conditional clause annotates its return target with a parenthetical artifact-class label. Q3's return target `Section 1A` carries `(FM->ACTOR BRIDGE)`; Q4's return target `Section 1B` carries `(FM->TRIGGER BRIDGE)`. Both classes match the section heading vocabulary established at `SECTION 1A -- Q3 -- FM->ACTOR BRIDGE` and `SECTION 1B -- Q4 -- FM->TRIGGER BRIDGE`. |

**Interaction check — C-53 + C-54 layering**: V-01's C-53 form (`Return to Section 1A if Q3 shows N; return to Section 1B if Q4 shows N.`) provided the per-artifact decomposition and distinct targets. R17 adds `(FM->ACTOR BRIDGE)` / `(FM->TRIGGER BRIDGE)` to each clause. C-53 requirement unchanged; C-54 layered on top without regression.

**Interaction check — C-49 symmetry**: V-01's gate interrogative carries `BOTH Q3 (FM-ACTOR-BRIDGE) AND Q4 (FM-TRIGGER-BRIDGE)` (C-49). The backward routing now carries class annotations matching that vocabulary at the return point. C-49 + C-54 together produce fully annotated bidirectional routing: class visible in the forward question and in each backward return directive.

**Score: 46/46 × 10 = 10.00**

---

#### V-02 — C-54 on stage-based scaffold (Stage 2A/2B reference form)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Essential templates present |
| C-34 through C-53 | PASS (carried) | R16 V-02 = 45/45; stage-based headings, gate heading, bracket labels, checklist all unchanged |
| **C-54** | **PASS** | `Return to Stage 2A (FM->ACTOR BRIDGE) if Q3 shows N; return to Stage 2B (FM->TRIGGER BRIDGE) if Q4 shows N.` — identical structural form to V-01 with stage-based targets. `Stage 2A` annotated with `(FM->ACTOR BRIDGE)`; `Stage 2B` annotated with `(FM->TRIGGER BRIDGE)`. Class labels echo `STAGE 2A -- Q3 -- FM->ACTOR BRIDGE` and `STAGE 2B -- Q4 -- FM->TRIGGER BRIDGE` headings. |

**This is the R17 reference form**: minimal single-axis change on the R16 reference scaffold. The annotated form `(FM->ACTOR BRIDGE)` / `(FM->TRIGGER BRIDGE)` is added at each return target; no other elements altered. Stage 2A/2B naming extended with class annotations independently of the gate heading (A-36/C-50 unchanged).

**Score: 46/46 × 10 = 10.00**

---

#### V-03 — C-54 on phrasing-register scaffold (domain-prefix A-23 style)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Domain-prefix templates prescribe all five essential elements |
| C-34 through C-53 | PASS (carried) | R16 V-03 = 45/45; domain-prefix bracket-suffix style (`INERTIA THREAT RULE [A-16]`, `INERTIA THREAT CITATION RULE [A-19]`, `[BRIDGE Q3 COMMAND]:`, `[BRIDGE Q4 COMMAND]:`) unchanged; per-artifact C-41 authoring commands present in Section 1A/1B unchanged |
| **C-54** | **PASS** | `Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N; return to Section 1B (FM->TRIGGER BRIDGE) if Q4 shows N.` — same Section 1A/1B annotated form as V-01. Domain-prefix register is orthogonal to gate body routing annotation; the parenthetical class labels coexist with domain-prefix bracket-suffix style without interaction. |

**Register-agnosticism confirmation for C-54**: The domain-prefix scaffold uses a distinct bracket-label vocabulary throughout (`INERTIA THREAT RULE [A-16]` vs. standard `[A-16 PRIMARY KEY RULE]`). C-54 is satisfied by adding the parenthetical annotation to the return targets — no interaction with surrounding bracket-label style. C-54 is structurally orthogonal to A-23 register choice, as C-53 was confirmed orthogonal in R16.

**Score: 46/46 × 10 = 10.00**

---

#### V-04 — C-54 on consolidated-bridge scaffold (bracket-prefix A-23 style)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | Templates prescribe all five essential elements |
| C-34, C-35 | PASS | `[A-16 PRIMARY KEY CONSTRAINT]` and `[A-19 CITATION INTEGRITY CONSTRAINT]` bracket labels present at Stage 1 and Stage 5B |
| C-36 | PASS | Four distinct bracket obligations: `[A-31]`, `[A-16]`, `[A-19]`, `[BRIDGE COMPLETION COMMAND]` |
| C-37 through C-41 | PASS (carried) | Combined gate heading `STAGE 2 -- [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL BRIDGE ARTIFACTS COMPLETE?` unchanged; gate body body routing is structurally independent of the heading |
| **C-42** | **FAIL** | **Inherited from R15 V-04 (unchanged through R16/R17).** `[A-31 FAIL-FIRST ORDERING RULE]`, `[A-16 PRIMARY KEY CONSTRAINT]`, `[A-19 CITATION INTEGRITY CONSTRAINT]` — bracket-label text shares only generic structural vocabulary. Domain name (`INCUMBENT WORKAROUND`) appears in stage headings and body prose but is absent from bracket-label text itself. R17 changes touch only gate body routing annotation — bracket-label text unaffected. C-42 failure carries forward. |
| C-43 through C-53 | PASS (carried) | Gate heading criteria, per-artifact routing C-53, staged structure all unchanged from R16 |
| **C-46** | **FAIL** | **Inherited from R15 V-04.** C-46 extends C-42. Bracket labels lack domain threading → C-42 fails → C-46 fails. R17 changes do not address bracket-label vocabulary. |
| **C-54** | **PASS** | `Return to Stage 2A (FM->ACTOR BRIDGE) if Q3 shows N; return to Stage 2B (FM->TRIGGER BRIDGE) if Q4 shows N.` — gate body return routing independently annotated with class labels. The combined gate heading form (A-36) occupies a structurally independent location from the gate body routing; C-54 is satisfied in the body regardless of the heading structure. Confirms C-54 is evaluable independently of A-36/C-50 combined-heading style. |

**Structural independence confirmation**: C-54 annotates gate body routing clauses. The combined heading `STAGE 2 -- [BRIDGE COMPLETION COMMAND]: CONFIRM -- ALL BRIDGE ARTIFACTS COMPLETE?` is the gate heading. These are structurally disjoint locations. C-54 can pass on a consolidated-bridge scaffold where Q3/Q4 are sub-headings within Stage 2 — the annotation attaches to the return targets in the body, not to the heading.

**Score: 44/46 × 10 = 9.57**

---

#### V-05 — C-54 reference form (all-caps, all-axes-combined, artifact-name-based targets)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 through C-05 | PASS | All-caps COMMAND-register templates prescribe all five essential elements |
| C-34 through C-53 | PASS (carried) | R16 V-05 = 45/45; all-caps bracket style, gate heading, per-artifact C-41 authoring commands, checklist all unchanged |
| **C-54** | **PASS (criterion source)** | `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING. IF Q4 SHOWS N, RETURN TO THE Q4 SECTION (FM->TRIGGER BRIDGE) AND COMPLETE THE TRIGGER MAPPING.` — V-05 was the R16 excellence signal that generated C-54. The class annotations `(FM->ACTOR BRIDGE)` and `(FM->TRIGGER BRIDGE)` are embedded within each conditional routing clause at the return target position. Register is all-caps; C-54 is register-agnostic. The criterion's pass definition is directly derived from this form — the minimal requirement is the parenthetical class annotation on the return target; V-05 additionally carries the completion-action clause. |

**Minimum vs. extended form**: V-01 through V-04 satisfy C-54 with the minimum form — parenthetical class annotation on the return target noun phrase. V-05 satisfies C-54 and extends beyond it:
- Minimum (V-01 form): `Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N`
- Extended (V-05 form): `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING`

The extended form carries two additional features beyond the C-54 requirement: (1) artifact-name-as-section-name routing (`THE Q3 SECTION` rather than ordinal `Section 1A`), and (2) a completion-action directive (`AND COMPLETE THE ACTOR MAPPING`) that specifies the work to be done on arriving at the return location. These remain unformal excellence signals.

**Score: 46/46 × 10 = 10.00**

---

### Composite Scores

| Variation | R16 Score | C-54 | R17 Score | Notes |
|-----------|-----------|------|-----------|-------|
| V-01 | 45/45 | PASS | **46/46 = 10.00** | Section 1A/1B annotation form; minimum C-54 pass |
| V-02 | 45/45 | PASS | **46/46 = 10.00** | Stage 2A/2B annotation form; R17 reference form |
| V-03 | 45/45 | PASS | **46/46 = 10.00** | Register-agnostic C-54 confirmation: domain-prefix A-23 scaffold |
| V-04 | 43/45 | PASS | **44/46 = 9.57** | C-42/C-46 failures inherited; C-54 gate body annotation is independent of bracket-label regression |
| V-05 | 45/45 | PASS | **46/46 = 10.00** | Criterion source; extended form with completion-action directive |

---

### Rankings

1. **V-01, V-02, V-03, V-05** — 46/46 = 10.00 (tied)
2. **V-04** — 44/46 = 9.57

---

### V-04 Structural Failure Analysis

V-04's C-42/C-46 failure is unchanged across R15 → R16 → R17. The R17 C-54 fix is correct and independent — the gate body routing annotation and the bracket-label vocabulary occupy separate document locations. Fixing C-42 requires upgrading bracket-label text to carry the domain name:

| Label form | C-36 | C-42 | C-46 |
|------------|------|------|------|
| `[A-31 FAIL-FIRST ORDERING RULE]` (current) | PASS | FAIL | FAIL |
| `INCUMBENT WORKAROUND FAIL-FIRST RULE [A-31]` (corrected) | PASS | PASS | PASS |

V-04 would reach 46/46 if bracket labels are upgraded to carry the competitor domain name. That change does not affect C-54 — the criterion is evaluable from gate body routing content alone.

---

### C-54 Cross-Variation Analysis

| Question | Finding |
|----------|---------|
| Does `(FM->ACTOR BRIDGE)` satisfy C-54, or must annotation match exact section heading vocabulary? | All variations echo section heading vocabulary exactly. `FM->ACTOR BRIDGE` appears in both `SECTION 1A -- Q3 -- FM->ACTOR BRIDGE` and in `(FM->ACTOR BRIDGE)` — vocabulary fidelity confirmed. V-05 uses artifact-name-based targets (`Q3 SECTION`) which have the same vocabulary basis. No tension found. |
| Does C-54 require the annotation to appear inside the conditional clause, attached to the return target? | All variations place the annotation there. The most restrictive interpretation is uniformly satisfied. C-54 does not need to relax position requirements. |
| Is register significant for C-54? | V-01/V-02/V-03/V-04 use lowercase; V-05 uses ALL-CAPS. All five pass. C-54 is register-agnostic, consistent with C-53's established register-agnosticism from R16. |
| Can semicolon-joined two-clause form and separate-sentence form both satisfy C-54? | Yes. V-01 through V-04 use semicolon-joined form; V-05 uses separate sentences with ALL-CAPS. Both carry per-artifact annotation on each return target. C-54 tests annotation presence and placement, not sentence-boundary form. |

---

### Excellence Signals (Top-Variation Patterns Not Yet Formalized)

Both signals originate from V-05 and were identified in R16. C-54 formalized the class annotation itself; these two signals extend beyond C-54 and remain unformal.

**Signal 1 — Completion-action routing directive (V-05)**

V-05's return routing specifies not only where to return but what work to complete on arrival: `IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING`. The clause delivers destination + artifact class + task in a single directive.

- V-01/V-02/V-03/V-04 form (C-54 minimum): `Return to Section 1A (FM->ACTOR BRIDGE) if Q3 shows N` — destination + class, no task
- V-05 form (extended): `RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING` — destination + class + task directive

The completion-action extension eliminates a second lookup for the author: once routed to the section, the work is already named in the routing instruction. The author does not need to read the section heading to determine what must be done.

Candidate criterion: a gate body routing clause that names destination, artifact class, AND completion action at the return point — a self-contained remediation instruction with no external lookup required.

**Signal 2 — Artifact-name-as-section-name routing (V-05)**

V-05 uses the artifact ID itself as the return target section reference: `THE Q3 SECTION`. The artifact ID in the gate table row (`Q3`), the conditional key (`IF Q3 SHOWS N`), and the return target (`THE Q3 SECTION`) share the same base identifier — zero mapping overhead.

- V-01/V-03 form: `Q3 → Section 1A` (author must know the ordinal mapping)
- V-02/V-04 form: `Q3 → Stage 2A` (author must know the ordinal mapping)
- V-05 form: `Q3 → THE Q3 SECTION` (isomorphic — same identifier, no mapping required)

Applicability condition: artifact-name-as-section-name routing requires bridge artifacts to be standalone sections whose primary label is the artifact ID. When artifacts are sub-sections nested within a parent stage (V-02/V-04), ordinal sub-labels (Stage 2A/2B) are necessary to create distinct routing targets.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["Completion-action routing directive (V-05): gate body conditional routing clause extends C-54 by adding an explicit completion task at the return point — IF Q3 SHOWS N, RETURN TO THE Q3 SECTION (FM->ACTOR BRIDGE) AND COMPLETE THE ACTOR MAPPING — delivering destination + artifact class + work directive in a single clause; V-01 through V-04 carry destination + artifact class only (C-54 minimum); V-05's extended form eliminates a second lookup step by naming the work inside the routing instruction, making the clause a self-contained remediation instruction requiring no external section-heading lookup", "Artifact-name-as-section-name routing (V-05): return target shares the same base identifier as the artifact ID in the gate table row (Q3 -> THE Q3 SECTION), creating zero-mapping-overhead routing — the author does not need to mentally map Q3 -> Section 1A or Q3 -> Stage 2A; V-01/V-03 ordinal forms (Q3 -> Section 1A) and V-02/V-04 ordinal forms (Q3 -> Stage 2A) require the author to know the mapping from artifact ID to section label; V-05 form is applicable when bridge artifact sections are standalone sections whose primary label IS the artifact ID; when artifacts are nested sub-sections within a parent stage, ordinal sub-labels are required and the isomorphic form is not available"]}
```
