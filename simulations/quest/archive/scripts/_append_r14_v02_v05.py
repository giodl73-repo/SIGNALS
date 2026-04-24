target = r"C:\src\sim\simulations\quest\golden\org-review-variate-R14-2026-03-17.md"

V02 = r"""
---

## V-02

**Axis**: Phrasing register -- two-differential derivation rule (D1 from NH table, D2 from alternatives table)
**Hypothesis**: The NH Dimension Table keeps two data columns (Current-State / Proposed-State)
but the NULL HYPOTHESIS DERIVATION RULE is extended to name both D1 and D2. D1 is sourced
from the NH Dimension Table differential (Build - StatusQuo). D2 is sourced from the BRACKET
OPENING alternatives comparison table Hybrid column (Build - Hybrid per dimension row). The
rule states both sources by name and requires both D1 and D2 majorities for PASS. Tests
whether C-23 two-differential coverage is independently satisfiable without a three-column
NH table. Predicted: 225/225 (C-23 v11 already passes; derivation rule richer).

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK
==============================================================================

DISPOSITION_CONTRACT v1

§1 -- SCOPE ENUMERATION
  IN-SCOPE (assign [S-NN] key per row):
    [S-01] [SURFACE_1]
    [S-02] [SURFACE_2]
    [S-03] [SURFACE_3]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY
  1. [DOMAIN_1]
  2. [DOMAIN_2]
  3. [DOMAIN_3]
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks. MEDIUM=Conditions. LOW=Advisory. Universal; not restatable.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst-case(all G_domain). Order: FAIL>CONDITIONAL>PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  BRACKET OPENING assigns CH-IDs. Downstream sections carry CH-ID response tables.
  PASS prohibited if any CH-ID=OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Syntax: | Section | Gate | Verdict | Class |
  Emit at verdict-emitting sections. Copy verbatim to ACTION ITEM REGISTER.
  Excluded: §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  §0->Role Manifest->Bracket Opening->Domain(s)->§3.5->§3.8->§5.7->§5.8->
  Lifecycle->Bracket Closing->§5.5->Gate Vector Table->Cross-Role Signals->
  Disposition->Action Item Register. Reordering is a contract violation.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED=every CH-ID has >=1 domain response (§3.8 gate).
  FULLY SATURATED=domain+lifecycle (BRACKET CLOSING gate).

§8a -- CH-ID COUNT BINDING [IMMUTABLE]
  After BRACKET OPENING CH-IDs: ch_id_count=M. Write: [CH-ID BIND: ch_id_count=M]
  §3.8 opens with "ch_id_count=[M]". BRACKET CLOSING table has exactly M rows.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  g_null(initial)=GOpen; g_null(post-domain)=worst(G_domain_agg,g_null(initial));
  g_null(final)=worst(G_lifecycle,g_null(post-domain)). GClose=g_null(final) or named override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 after BRACKET CLOSING. KEY-CITATION: cite [S-NN] per row.
  Format: "COVERED--[S-NN] in F-x" or "GAP--[S-NN] not referenced."

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Per-finding Severity. Section Severity=worst(all). Mechanical, not editorial.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  §5.7 after DOMAIN sections. ALL lens.verify entries per role. OPEN->ADVISORY-OPEN-LENS.

§15a -- LENS ENTRY COUNT BINDING [IMMUTABLE]
  At ROLE MANIFEST per active reviewer [R]:
    lens_entry_count_[R]=N. Write: [LENS BIND: role=[R], lens_entry_count=[N]]
  §5.7 completeness: "lens_entry_count_[R]=[N] required; [K] emitted. COMPLETE/INCOMPLETE"

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Precedence: GClose FAIL > any Gi FAIL > GClose COND > G_lifecycle COND >
  G_domain_agg COND > GOpen COND > all PASS (GClose confirming).

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  Each §5.7 row: {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L}
  CITATION VALIDITY: [S-NN] key must resolve in §1 index.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  K(d)=0->ADVISORY-GAP. §5.8 certifies all §1a domains.
  Count assertion: "certified [N] domains; [M] ADVISORY-GAP."

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1 -- TABLE POPULATION (two-column; D2 sourced from alternatives table):
    Columns: Dimension | Current-State Score | Proposed-State Score |
             D1=(Build-SQ) | Per-Dim Verdict
    Minimum 2 dimensions. D1=(Proposed)-(Current). BUILD-WINS=D1>0; SQ-WINS=D1<0; TIED=0.
  PHASE 2 -- TABLE LOCK: DIMENSION TABLE LOCKED
  PHASE 2a -- COUNT BINDING: dimension_count=N (filled integer)
  PHASE 3 -- NH TESTIMONY: opens "Based on dimension_count=[N] rows..."
  g_null derivation (two-source formula):
    D1 source: NH Dimension Table. B1_wins=count(BUILD-WINS rows).
    D2 source: BRACKET OPENING alternatives table. B2_wins=count(Build>Hybrid rows).
    g_null=PASS if B1_wins>dimension_count/2 AND B2_wins>dimension_count/2.
    g_null=FAIL if (dimension_count-B1_wins)>dimension_count/2.
    g_null=CONDITIONAL otherwise.
    Formula names both sources: "NH Dimension Table (B1_wins=[N])" and
    "Alternatives Table Hybrid column (B2_wins=[N])". Both by name.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters: {{artifact_id}} / {{depth}} / {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

Lens entry count binding:
- [LENS BIND: role=[DOMAIN_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[LIFECYCLE_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[CHALLENGER_ROLE], lens_entry_count=[N]]

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

| Dimension | Current-State Score | Proposed-State Score | D1=(Build-SQ) | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS/SQ-WINS/TIED] |
| [DIM_2] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS/SQ-WINS/TIED] |
| [DIM_3] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS/SQ-WINS/TIED] |

**DIMENSION TABLE LOCKED**
**dimension_count = [N]**

NH TESTIMONY: "Based on dimension_count=[N] rows and the alternatives table Hybrid column
as D2 source..." [Two-source derivation cited explicitly.]

§0 derivation:
- dimension_count=[N]; B1_wins=[N]
- B2_wins=[N] (Build>Hybrid on D2 from alternatives table)
- B1_wins>[N]/2 AND B2_wins>[N]/2? -> PASS candidate
- (N-B1_wins)>[N]/2? -> FAIL candidate
- **g_null(initial) from §0**: [PASS/CONDITIONAL/FAIL]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH/MEDIUM/LOW]

**Alternatives comparison table** *(D2 source: Build vs Hybrid column)*:

| Dimension | Status Quo | Build | Hybrid | D2=(Build-Hybrid) | Notes |
|-----------|-----------|-------|--------|------------------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [sentence] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [sentence] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [sentence] |

**NULL HYPOTHESIS DERIVATION RULE** (two-source; pre-committed):
  D1 source: NH Dimension Table (dimension_count=[N]; B1_wins=[N]).
  D2 source: this alternatives table Hybrid column (B2_wins=[N] Build>Hybrid rows).
  g_null=PASS if B1_wins>dimension_count/2 AND B2_wins>dimension_count/2.
  g_null=FAIL if (dimension_count-B1_wins)>dimension_count/2.
  g_null=CONDITIONAL otherwise. Both sources named explicitly.

**Challenge claims**:

| CH-ID | Claim | Severity |
|-------|-------|---------|
| CH-001 | [CLAIM_1] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [optional] | [H/M/L] |

[CH-ID BIND: ch_id_count = M]

**GOpen Verdict**: [PASS/CONDITIONAL/FAIL]
**g_null(initial) = GOpen = [P/C/F]**

*Local Gate Ledger Row:*
| BRACKET OPENING | GOpen | [P/C/F] | [Class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**Alternatives re-scoring**:

| Dimension | SQ | Build | Hybrid | D2=(B-H) | Notes |
|-----------|----|----|--------|---------|-------|
| [DIM_1] | [S] | [S] | [S] | [+/-/0] | [sentence] |
| [DIM_2] | [S] | [S] | [S] | [+/-/0] | [sentence] |

**CH-ID Response Table**:

| CH-ID | Claim (copy) | Response | Status |
|-------|-------------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Additional Findings**:

| Finding | Surface | Severity |
|---------|---------|---------|
| F-1: [finding] | [SURFACE] | [H/M/L] |
| F-2: [finding] | [SURFACE] | [H/M/L] |

Section Severity = worst(F-1,F-2) = [H/M/L] *(§14)*

**G_domain Verdict**: [P/C/F]
**G_domain Reason**: [sentence]

*Local Gate Ledger Row:*
| DOMAIN -- [ROLE_NAME] | G_domain | [P/C/F] | [Class] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

G_domain_agg = [P/C/F] (§3a worst-case)
g_null(post-domain) = worst([G_domain_agg],[g_null(initial)]) = **[P/C/F]**

---

## §3.8 -- CH-ID SATURATION CHECK

ch_id_count=[M] (bound at BRACKET OPENING per §8a)

| CH-ID | Domain Response | SATURATED? |
|-------|----------------|-----------|
| CH-001 | [status] | [YES/NO] |
| CH-002 | [status] | [YES/NO] |

**SATURATION GATE**: [PASS/HALT]

---

## §5.7 -- LENS COVERAGE TABLE

**[DOMAIN_ROLE]** -- lens_entry_count=[N] (ROLE MANIFEST):

| Lens Dimension | §17 Assertion | Status |
|---------------|--------------|--------|
| [entry 1] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |
| [entry 2] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |

Completeness: lens_entry_count_[DOMAIN_ROLE]=[N] required; [K] emitted. [COMPLETE/INCOMPLETE]
ADVISORY-OPEN-LENS: [N] loaded; [K] ADDRESSED; [N-K] OPEN.

**[LIFECYCLE_ROLE]** -- lens_entry_count=[N] (ROLE MANIFEST):

| Lens Dimension | §17 Assertion | Status |
|---------------|--------------|--------|
| [entry 1] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |

Completeness: lens_entry_count_[LIFECYCLE_ROLE]=[N] required; [K] emitted. [COMPLETE/INCOMPLETE]

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

| Domain (§1a) | R(d) HIGH | K(d) | Coverage |
|-------------|----------|------|---------|
| [DOMAIN_1] | {[roles]} | [N] | [COVERED/ADVISORY-GAP] |
| [DOMAIN_2] | {} | 0 | ADVISORY-GAP |

§5.8 count assertion: certified [N] domains; [M] ADVISORY-GAP.

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen:[copy]; G_domain_agg:[copy]; g_null(post-domain):[copy]

**Alternatives re-scoring**:

| Dimension | SQ | Build | Hybrid | D2=(B-H) | Notes |
|-----------|----|----|--------|---------|-------|
| [DIM_1] | [S] | [S] | [S] | [+/-/0] | [sentence] |
| [DIM_2] | [S] | [S] | [S] | [+/-/0] | [sentence] |

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Decision-readiness**: [Paragraph citing GOpen and G_domain_agg.]
**Null hypothesis status**: [Defeated? yes/partial/no]

**Additional Findings**:

| Finding | Surface | Severity |
|---------|---------|---------|
| F-1: [finding] | [SURFACE] | [H/M/L] |

Section Severity = worst(F-1) = [H/M/L]

**G_lifecycle Verdict**: [P/C/F]
**G_lifecycle Reason**: [sentence]

*Local Gate Ledger Row:*
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [P/C/F] | [Class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
Received G_lifecycle:[copy]; g_null(post-domain):[copy]

**CH-ID Final Assessment** (ch_id_count=[M]; table must have M rows):

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|---------|------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |

Fully SATURATED: [YES/NO]

**Alternatives aggregated re-score**:

| Dimension | Challenger | Domain Agg | Lifecycle | Final |
|-----------|-----------|-----------|----------|-------|
| [DIM_1] | [S] | [S] | [S] | [agg] |
| [DIM_2] | [S] | [S] | [S] | [agg] |

**Remaining gaps**: [none / list]

g_null(final) = worst([G_lifecycle],[g_null(post-domain)]) = **[P/C/F]**

**GClose Verdict**: [P/C/F]
**Override invoked**: [YES/NO]
**GClose Rationale**: [2-3 sentences.]

*Local Gate Ledger Row:*
| BRACKET CLOSING | GClose | [P/C/F] | [Class] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

| §1 Key | Surface | Finding Ref | Status |
|--------|---------|------------|--------|
| [S-01] | [text] | [F-x / none] | [COVERED--[S-01] in F-x / GAP--[S-01] not referenced] |
| [S-02] | [text] | [F-x / none] | [COVERED/GAP] |

§5.5 signal: [COVERED/PARTIAL--[N] GAP]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract |
|------|----------|---------|---------|
| GOpen | [CHALLENGER] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [P/C/F] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

g_null progression: initial=[P/C/F]; post-domain=[P/C/F]; final=[P/C/F]. GClose consistent?[YES/NO]
Conflicts: [None/description]
Convergence: [concern from >=2 reviewers]
Scope coverage: [None/gaps]

---

## DISPOSITION

Gate vector: GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]

```
GClose=FAIL? BLOCKED. Any Gi=FAIL? BLOCKED. Any CONDITIONAL? CONDITIONAL. All PASS? READY.
```

**Overall Disposition**: [READY/CONDITIONAL/BLOCKED]
**Primary driver**: [§16 precedence -- one sentence]
**Conditions/Blocker**: [if applicable]

---

## ACTION ITEM REGISTER

| CH-ID | Section | Gate | Verdict | Class | Item | Resolution |
|-------|---------|------|---------|-------|------|-----------|
| CH-001 | [section] | [gate] | [copy] | [copy] | [item] | [criterion] |
| -- | ADVISORY-OPEN-LENS | -- | -- | ADVISORY | [lens dim] | [criterion] |
| -- | ADVISORY-GAP | -- | -- | ADVISORY-GAP | [domain/surface] | [criterion] |

---

**Artifact to review:**

{{artifact}}
"""

V03 = r"""
---

## V-03

**Axis**: Output format -- NH TABLE AGGREGATION RULE pre-committed in §0
**Hypothesis**: BRACKET CLOSING currently produces an alternatives aggregated re-score table
but uses no pre-committed formula -- the aggregation is editorial. Pre-committing the
aggregation rule in §0 as an IMMUTABLE section (§0 PHASE 4 AGGREGATION RULE) makes
g_null(final) re-derivable from the aggregated table cells alone, not from editorial
combination of three separate verdicts. The rule: for each dimension row, Aggregated
Status-Quo = max(SQ scores across challenger, domain, lifecycle); Aggregated Build =
min(Build scores) [conservative]; Aggregated D1_agg = Build_agg - SQ_agg; Per-Dim Verdict
from D1_agg using same BUILD-WINS/SQ-WINS/TIED thresholds. g_null(final) applies the §0
B_wins formula to the aggregated table. This tests whether pre-committed aggregation
strengthens GClose derivability and constitutes a new excellence pattern. Predicted: 225/225.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK
==============================================================================

DISPOSITION_CONTRACT v1

§1 -- SCOPE ENUMERATION
  IN-SCOPE (assign [S-NN] key per row):
    [S-01] [SURFACE_1]
    [S-02] [SURFACE_2]
    [S-03] [SURFACE_3]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY
  1. [DOMAIN_1]  2. [DOMAIN_2]  3. [DOMAIN_3]
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks. MEDIUM=Conditions. LOW=Advisory. Universal.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg=worst-case(all G_domain). FAIL>CONDITIONAL>PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each section opens: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  CH-IDs assigned at BRACKET OPENING. All sections carry CH-ID response tables.
  PASS prohibited if any CH-ID=OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Syntax: | Section | Gate | Verdict | Class |
  Emit at verdict-emitting sections. Copy verbatim to ACTION ITEM REGISTER.
  Excluded: §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  §0->Role Manifest->Bracket Opening->Domain(s)->§3.5->§3.8->§5.7->§5.8->
  Lifecycle->Bracket Closing->§5.5->Gate Vector Table->Cross-Role Signals->
  Disposition->Action Item Register.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED at §3.8. FULLY SATURATED at BRACKET CLOSING.

§8a -- CH-ID COUNT BINDING [IMMUTABLE]
  After BRACKET OPENING: ch_id_count=M. Write: [CH-ID BIND: ch_id_count=M]
  §3.8 opens "ch_id_count=[M]". BRACKET CLOSING table has M rows.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  g_null(initial)=GOpen; g_null(post-domain)=worst(G_domain_agg,g_null(initial));
  g_null(final)=worst(G_lifecycle,g_null(post-domain)).
  GClose=g_null(final) or named override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 KEY-CITATION: cite [S-NN] per row. "COVERED--[S-NN] in F-x" or "GAP--[S-NN] not referenced."

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Per-finding Severity. Section Severity=worst(all). Mechanical.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  §5.7 ALL lens.verify entries per role. OPEN->ADVISORY-OPEN-LENS.

§15a -- LENS ENTRY COUNT BINDING [IMMUTABLE]
  At ROLE MANIFEST: lens_entry_count_[R]=N per role. Write: [LENS BIND: role=[R], lens_entry_count=[N]]
  §5.7 completeness: "lens_entry_count_[R]=[N] required; [K] emitted."

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Precedence: GClose FAIL > Gi FAIL > GClose COND > G_lifecycle COND >
  G_domain_agg COND > GOpen COND > all PASS.

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  §5.7 rows: {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L}
  CITATION VALIDITY: [S-NN] resolves in §1 index.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  K(d)=0->ADVISORY-GAP. §5.8 certifies §1a domains.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1 -- TABLE POPULATION:
    Columns: Dimension | Current-State Score | Proposed-State Score |
             Differential D1=(Build-SQ) | Per-Dim Verdict
    Minimum 2 dimensions. BUILD-WINS=D1>0; SQ-WINS=D1<0; TIED=D1=0.
  PHASE 2 -- TABLE LOCK: DIMENSION TABLE LOCKED
  PHASE 2a -- DIMENSION COUNT BINDING: dimension_count=N
  PHASE 3 -- NH TESTIMONY: opens "Based on dimension_count=[N] rows..."
  g_null derivation:
    B_wins=count(BUILD-WINS); SQ_holds=count(SQ-WINS)
    PASS if B_wins>dimension_count/2; FAIL if SQ_holds>dimension_count/2; else CONDITIONAL.
  PHASE 4 -- BRACKET CLOSING AGGREGATION RULE [IMMUTABLE]:
    Before GClose is stated, BRACKET CLOSING must produce an AGGREGATED NH TABLE.
    For each dimension row (same rows as §0 table; dimension_count rows required):
      Agg_SQ_score  = max(SQ score from challenger, domain, lifecycle) [conservative: worst SQ]
      Agg_Build_score = min(Build score from challenger, domain, lifecycle) [conservative: weakest Build claim]
      D1_agg = Agg_Build_score - Agg_SQ_score
      Per-Dim Verdict_agg: BUILD-WINS if D1_agg>0; SQ-WINS if D1_agg<0; TIED if D1_agg=0.
    B_wins_agg = count(BUILD-WINS in aggregated table)
    g_null_agg = PASS if B_wins_agg>dimension_count/2; FAIL if (dimension_count-B_wins_agg)>dimension_count/2; else CONDITIONAL.
    GClose must equal g_null_agg OR state override citing specific aggregated row.
    This pre-committed rule ensures GClose is derivable from aggregated table cells alone.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters: {{artifact_id}} / {{depth}} / {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

Lens entry count binding:
- [LENS BIND: role=[DOMAIN_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[LIFECYCLE_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[CHALLENGER_ROLE], lens_entry_count=[N]]

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

| Dimension | Current-State Score | Proposed-State Score | D1=(Build-SQ) | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS/SQ-WINS/TIED] |
| [DIM_2] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS/SQ-WINS/TIED] |
| [DIM_3] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS/SQ-WINS/TIED] |

**DIMENSION TABLE LOCKED**
**dimension_count = [N]**

NH TESTIMONY: "Based on dimension_count=[N] rows..."

§0 derivation: B_wins=[N]; SQ_holds=[N]; dimension_count=[N]
-> **g_null(initial) from §0**: [PASS/CONDITIONAL/FAIL]

*(§0 PHASE 4 AGGREGATION RULE will be applied at BRACKET CLOSING using dimension_count=[N] rows.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH/MEDIUM/LOW]

**Alternatives comparison table**:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [sentence] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [sentence] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [sentence] |

**NULL HYPOTHESIS DERIVATION RULE** (pre-committed):
  Apply §0 derivation result. g_null=PASS if B_wins>dimension_count/2.
  g_null=FAIL if SQ_holds>dimension_count/2. g_null=CONDITIONAL otherwise.

**Challenge claims**:

| CH-ID | Claim | Severity |
|-------|-------|---------|
| CH-001 | [CLAIM_1] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [optional] | [H/M/L] |

[CH-ID BIND: ch_id_count = M]

**GOpen Verdict**: [P/C/F]
**g_null(initial) = GOpen = [P/C/F]**

*Local Gate Ledger Row:*
| BRACKET OPENING | GOpen | [P/C/F] | [Class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**Alternatives re-scoring** *(same dimensions; captures SQ and Build scores for §0 aggregation)*:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SQ_score] | [Build_score] | [SCORE] | [sentence] |
| [DIM_2] | [SQ_score] | [Build_score] | [SCORE] | [sentence] |
| [DIM_3] | [SQ_score] | [Build_score] | [SCORE] | [sentence] |

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Additional Findings**:

| Finding | Surface | Severity |
|---------|---------|---------|
| F-1: [finding] | [SURFACE] | [H/M/L] |
| F-2: [finding] | [SURFACE] | [H/M/L] |

Section Severity = worst(F-1,F-2) = [H/M/L]

**G_domain Verdict**: [P/C/F]
**G_domain Reason**: [sentence]

*Local Gate Ledger Row:*
| DOMAIN -- [ROLE_NAME] | G_domain | [P/C/F] | [Class] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

G_domain_agg = [P/C/F]
g_null(post-domain) = worst([G_domain_agg],[g_null(initial)]) = **[P/C/F]**

---

## §3.8 -- CH-ID SATURATION CHECK

ch_id_count=[M] (§8a)

| CH-ID | Domain Response | SATURATED? |
|-------|----------------|-----------|
| CH-001 | [status] | [YES/NO] |
| CH-002 | [status] | [YES/NO] |

**SATURATION GATE**: [PASS/HALT]

---

## §5.7 -- LENS COVERAGE TABLE

**[DOMAIN_ROLE]** -- lens_entry_count=[N]:

| Lens Dimension | §17 Assertion | Status |
|---------------|--------------|--------|
| [entry 1] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |
| [entry 2] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |

Completeness: lens_entry_count_[DOMAIN_ROLE]=[N]; [K] emitted. [COMPLETE/INCOMPLETE]

**[LIFECYCLE_ROLE]** -- lens_entry_count=[N]:

| Lens Dimension | §17 Assertion | Status |
|---------------|--------------|--------|
| [entry 1] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |

Completeness: lens_entry_count_[LIFECYCLE_ROLE]=[N]; [K] emitted. [COMPLETE/INCOMPLETE]

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

| Domain (§1a) | R(d) HIGH | K(d) | Coverage |
|-------------|----------|------|---------|
| [DOMAIN_1] | {[roles]} | [N] | [COVERED/ADVISORY-GAP] |

§5.8 count assertion: certified [N] domains; [M] ADVISORY-GAP.

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen:[copy]; G_domain_agg:[copy]; g_null(post-domain):[copy]

**Alternatives re-scoring** *(captures SQ and Build scores for §0 aggregation)*:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SQ_score] | [Build_score] | [SCORE] | [sentence] |
| [DIM_2] | [SQ_score] | [Build_score] | [SCORE] | [sentence] |

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Decision-readiness**: [Paragraph.]
**Null hypothesis status**: [Defeated? yes/partial/no]

**Additional Findings**:

| Finding | Surface | Severity |
|---------|---------|---------|
| F-1: [finding] | [SURFACE] | [H/M/L] |

Section Severity = worst(F-1) = [H/M/L]

**G_lifecycle Verdict**: [P/C/F]
**G_lifecycle Reason**: [sentence]

*Local Gate Ledger Row:*
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [P/C/F] | [Class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
Received G_lifecycle:[copy]; g_null(post-domain):[copy]

**CH-ID Final Assessment** (ch_id_count=[M]):

| CH-ID | G_domain | G_lifecycle | Final | Notes |
|-------|---------|------------|-------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |

Fully SATURATED: [YES/NO]

**§0 PHASE 4 AGGREGATION TABLE** *(per §0 PHASE 4 AGGREGATION RULE; dimension_count=[N] rows required)*:

| Dimension | Agg_SQ (max SQ) | Agg_Build (min Build) | D1_agg=(Agg_Build-Agg_SQ) | Per-Dim Verdict_agg |
|-----------|-----------------|----------------------|--------------------------|---------------------|
| [DIM_1] | max([Chal_SQ],[Dom_SQ],[Life_SQ]) | min([Chal_B],[Dom_B],[Life_B]) | [+/-/0] | [BUILD-WINS/SQ-WINS/TIED] |
| [DIM_2] | max([...]) | min([...]) | [+/-/0] | [BUILD-WINS/SQ-WINS/TIED] |
| [DIM_3] | max([...]) | min([...]) | [+/-/0] | [BUILD-WINS/SQ-WINS/TIED] |

B_wins_agg = [N] / dimension_count = [N]
g_null_agg derivation: B_wins_agg>[N]/2? [YES/NO] -> [PASS/CONDITIONAL/FAIL]
**g_null_agg = [PASS/CONDITIONAL/FAIL]**

**Remaining gaps**: [none / list]

g_null(final) = worst([G_lifecycle],[g_null(post-domain)]) = **[P/C/F]**

**GClose Verdict**: [P/C/F]
*(Must equal g_null_agg per §0 PHASE 4 rule, or state override citing specific aggregated row.)*
**Override invoked**: [YES/NO]
**GClose Rationale**: [2-3 sentences. If using aggregation result: cite B_wins_agg/dimension_count.]

*Local Gate Ledger Row:*
| BRACKET CLOSING | GClose | [P/C/F] | [Class] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

| §1 Key | Surface | Finding Ref | Status |
|--------|---------|------------|--------|
| [S-01] | [text] | [F-x/none] | [COVERED--[S-01] in F-x / GAP--[S-01] not referenced] |
| [S-02] | [text] | [F-x/none] | [COVERED/GAP] |

§5.5 signal: [COVERED/PARTIAL]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract |
|------|----------|---------|---------|
| GOpen | [CHALLENGER] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [P/C/F] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

g_null progression: initial=[P/C/F]; post-domain=[P/C/F]; final=[P/C/F]. GClose consistent?[YES/NO]
Conflicts: [None/description]. Convergence: [concern]. Scope coverage: [None/gaps].

---

## DISPOSITION

Gate vector: GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]

```
GClose=FAIL?->BLOCKED. Gi=FAIL?->BLOCKED. Any COND?->CONDITIONAL. All PASS?->READY.
```

**Overall Disposition**: [READY/CONDITIONAL/BLOCKED]
**Primary driver**: [§16 -- one sentence]

---

## ACTION ITEM REGISTER

| CH-ID | Section | Gate | Verdict | Class | Item | Resolution |
|-------|---------|------|---------|-------|------|-----------|
| CH-001 | [section] | [gate] | [copy] | [copy] | [item] | [criterion] |
| -- | ADVISORY-OPEN-LENS | -- | -- | ADVISORY | [lens dim] | [criterion] |
| -- | ADVISORY-GAP | -- | -- | ADVISORY-GAP | [domain/surface] | [criterion] |

---

**Artifact to review:**

{{artifact}}
"""

V04 = r"""
---

## V-04

**Axis**: Inertia framing + Phrasing register (two-axis)
**Hypothesis**: V-01 introduces the three-column NH Dimension Table with D1 and D2 as
explicit derived columns. V-02 extends the derivation rule to name both D1 and D2 sources.
V-04 merges both: the three-column NH table provides D1 AND D2 from the same table (no need
to source D2 from the alternatives table). The derivation rule becomes: B_wins = count
of BUILD-WINS rows (D1>0 AND D2>0); SQ_holds = count of STATUS-QUO rows (D1<=0).
g_null = PASS if B_wins > dimension_count/2; FAIL if SQ_holds > dimension_count/2; else CONDITIONAL.
Both differentials derivable from a single table; no cross-table sourcing needed.
Primary candidate for satisfying both the three-column-table criterion (C-38 v12) and the
two-differential-rule criterion (C-23 v12) simultaneously. Predicted: 225/225 on v11.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK
==============================================================================

DISPOSITION_CONTRACT v1

§1 -- SCOPE ENUMERATION
  IN-SCOPE (assign [S-NN] key per row):
    [S-01] [SURFACE_1]
    [S-02] [SURFACE_2]
    [S-03] [SURFACE_3]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY
  1. [DOMAIN_1]  2. [DOMAIN_2]  3. [DOMAIN_3]
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks. MEDIUM=Conditions. LOW=Advisory. Universal.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg=worst-case(all G_domain). FAIL>CONDITIONAL>PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each section: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  CH-IDs at BRACKET OPENING. All sections carry CH-ID tables. PASS blocked if any OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Syntax: | Section | Gate | Verdict | Class |. Copy verbatim to register.
  Excluded: §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  §0->Role Manifest->Bracket Opening->Domain(s)->§3.5->§3.8->§5.7->§5.8->
  Lifecycle->Bracket Closing->§5.5->Gate Vector Table->Cross-Role Signals->
  Disposition->Action Item Register.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED at §3.8. FULLY SATURATED at BRACKET CLOSING.

§8a -- CH-ID COUNT BINDING [IMMUTABLE]
  After BRACKET OPENING: ch_id_count=M. [CH-ID BIND: ch_id_count=M]
  §3.8 opens "ch_id_count=[M]". BRACKET CLOSING table has M rows.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  g_null stages 1-3. GClose=g_null(final) or named override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 KEY-CITATION: [S-NN] per row.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Section Severity=worst(all finding severities). Mechanical.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  §5.7 ALL lens.verify entries per role.

§15a -- LENS ENTRY COUNT BINDING [IMMUTABLE]
  At ROLE MANIFEST: lens_entry_count_[R]=N per active reviewer.
  §5.7 completeness check cites count by name.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Precedence: GClose FAIL > Gi FAIL > GClose COND > G_lifecycle COND >
  G_domain_agg COND > GOpen COND > all PASS.

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  §5.7 rows: {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L}

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  K(d)=0->ADVISORY-GAP. §5.8 certifies §1a domains.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1 -- TABLE POPULATION (three-column form):
    Columns: Dimension | Status-Quo Score | Proposed-Build Score |
             Best-Non-Build-Alt Score | D1=(Build-SQ) | D2=(Build-Alt) |
             Per-Dim Verdict
    Minimum 2 dimensions.
    D1=(Proposed-Build)-(Status-Quo). D2=(Proposed-Build)-(Best-Non-Build-Alt).
    Per-Dim Verdict:
      BUILD-WINS    = D1>0 AND D2>0
      STATUS-QUO    = D1<=0
      BEST-ALT-WINS = D1>0 AND D2<=0
      TIED          = D1=0 AND D2=0
  PHASE 2 -- TABLE LOCK: DIMENSION TABLE LOCKED
  PHASE 2a -- DIMENSION COUNT BINDING: dimension_count=N
  PHASE 3 -- NH TESTIMONY: opens "Based on dimension_count=[N] rows..."
  g_null derivation (both differentials from table):
    B_wins=count(BUILD-WINS rows; D1>0 AND D2>0)
    SQ_holds=count(STATUS-QUO rows; D1<=0)
    PASS if B_wins>dimension_count/2
    FAIL if SQ_holds>dimension_count/2
    CONDITIONAL otherwise
    Formula references dimension_count, B_wins, SQ_holds by name.
    Both D1 and D2 named explicitly in the derivation rule.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters: {{artifact_id}} / {{depth}} / {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

Lens entry count binding:
- [LENS BIND: role=[DOMAIN_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[LIFECYCLE_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[CHALLENGER_ROLE], lens_entry_count=[N]]

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

| Dimension | Status-Quo Score | Proposed-Build Score | Best-Non-Build-Alt Score | D1=(B-SQ) | D2=(B-Alt) | Per-Dim Verdict |
|-----------|-----------------|---------------------|--------------------------|----------|-----------|-----------------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [+/-/0] | [BUILD-WINS/STATUS-QUO/BEST-ALT-WINS/TIED] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [+/-/0] | [BUILD-WINS/STATUS-QUO/BEST-ALT-WINS/TIED] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [+/-/0] | [BUILD-WINS/STATUS-QUO/BEST-ALT-WINS/TIED] |

**DIMENSION TABLE LOCKED**
**dimension_count = [N]**

NH TESTIMONY: "Based on dimension_count=[N] rows, B_wins (D1>0 AND D2>0) = [N],
SQ_holds (D1<=0) = [N]..."

§0 derivation:
- dimension_count=[N]; B_wins=[N]; SQ_holds=[N]
- B_wins>[N]/2? -> PASS; SQ_holds>[N]/2? -> FAIL; else CONDITIONAL
- **g_null(initial) from §0**: [PASS/CONDITIONAL/FAIL]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH/MEDIUM/LOW]

**Alternatives comparison table** *(bracket-wide scaffold; re-scored by reviewers)*:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [sentence] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [sentence] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [sentence] |

**NULL HYPOTHESIS DERIVATION RULE** (three-column table; both D1 and D2 from §0):
  From §0 table (three-column form; dimension_count=[N]):
    B_wins=[N] (BUILD-WINS rows: D1>0 AND D2>0)
    SQ_holds=[N] (STATUS-QUO rows: D1<=0)
  g_null=PASS if B_wins>dimension_count/2 (Build wins D1 AND D2 majority).
  g_null=FAIL if SQ_holds>dimension_count/2 (Status Quo holds D1 majority).
  g_null=CONDITIONAL otherwise.
  Both D1 and D2 named in this rule. Override requires citing specific dimension row.

**Challenge claims**:

| CH-ID | Claim | Severity |
|-------|-------|---------|
| CH-001 | [CLAIM_1] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [optional] | [H/M/L] |

[CH-ID BIND: ch_id_count = M]

**GOpen Verdict**: [P/C/F]
**g_null(initial) = GOpen = [P/C/F]**

*Local Gate Ledger Row:*
| BRACKET OPENING | GOpen | [P/C/F] | [Class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**Alternatives re-scoring**:

| Dimension | SQ | Build | Hybrid | Notes |
|-----------|----|----|--------|-------|
| [DIM_1] | [S] | [S] | [S] | [sentence] |
| [DIM_2] | [S] | [S] | [S] | [sentence] |
| [DIM_3] | [S] | [S] | [S] | [sentence] |

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Additional Findings**:

| Finding | Surface | Severity |
|---------|---------|---------|
| F-1: [finding] | [SURFACE] | [H/M/L] |
| F-2: [finding] | [SURFACE] | [H/M/L] |

Section Severity = worst(F-1,F-2) = [H/M/L]

**G_domain Verdict**: [P/C/F]
**G_domain Reason**: [sentence]

*Local Gate Ledger Row:*
| DOMAIN -- [ROLE_NAME] | G_domain | [P/C/F] | [Class] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

G_domain_agg = [P/C/F]
g_null(post-domain) = worst([G_domain_agg],[g_null(initial)]) = **[P/C/F]**

---

## §3.8 -- CH-ID SATURATION CHECK

ch_id_count=[M] (§8a)

| CH-ID | Domain Response | SATURATED? |
|-------|----------------|-----------|
| CH-001 | [status] | [YES/NO] |
| CH-002 | [status] | [YES/NO] |

**SATURATION GATE**: [PASS/HALT]

---

## §5.7 -- LENS COVERAGE TABLE

**[DOMAIN_ROLE]** -- lens_entry_count=[N]:

| Lens Dimension | §17 Assertion | Status |
|---------------|--------------|--------|
| [entry 1] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |
| [entry 2] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |

Completeness: lens_entry_count_[DOMAIN_ROLE]=[N]; [K] emitted. [COMPLETE/INCOMPLETE]

**[LIFECYCLE_ROLE]** -- lens_entry_count=[N]:

| Lens Dimension | §17 Assertion | Status |
|---------------|--------------|--------|
| [entry 1] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |

Completeness: lens_entry_count_[LIFECYCLE_ROLE]=[N]; [K] emitted. [COMPLETE/INCOMPLETE]

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

| Domain (§1a) | R(d) HIGH | K(d) | Coverage |
|-------------|----------|------|---------|
| [DOMAIN_1] | {[roles]} | [N] | [COVERED/ADVISORY-GAP] |

§5.8 count assertion: certified [N] domains; [M] ADVISORY-GAP.

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen:[copy]; G_domain_agg:[copy]; g_null(post-domain):[copy]

**Alternatives re-scoring**:

| Dimension | SQ | Build | Hybrid | Notes |
|-----------|----|----|--------|-------|
| [DIM_1] | [S] | [S] | [S] | [sentence] |
| [DIM_2] | [S] | [S] | [S] | [sentence] |

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Decision-readiness**: [Paragraph.]
**Null hypothesis status**: [yes/partial/no]

**Additional Findings**:

| Finding | Surface | Severity |
|---------|---------|---------|
| F-1: [finding] | [SURFACE] | [H/M/L] |

Section Severity = [H/M/L]

**G_lifecycle Verdict**: [P/C/F]
**G_lifecycle Reason**: [sentence]

*Local Gate Ledger Row:*
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [P/C/F] | [Class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
Received G_lifecycle:[copy]; g_null(post-domain):[copy]

**CH-ID Final Assessment** (ch_id_count=[M]):

| CH-ID | G_domain | G_lifecycle | Final | Notes |
|-------|---------|------------|-------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |

Fully SATURATED: [YES/NO]

**Alternatives aggregated re-score**:

| Dimension | Challenger | Domain Agg | Lifecycle | Final |
|-----------|-----------|-----------|----------|-------|
| [DIM_1] | [score] | [score] | [score] | [agg] |
| [DIM_2] | [score] | [score] | [score] | [agg] |
| [DIM_3] | [score] | [score] | [score] | [agg] |

**Remaining gaps**: [none / list]

g_null(final) = worst([G_lifecycle],[g_null(post-domain)]) = **[P/C/F]**

**GClose Verdict**: [P/C/F]
**Override invoked**: [YES/NO]
**GClose Rationale**: [2-3 sentences.]

*Local Gate Ledger Row:*
| BRACKET CLOSING | GClose | [P/C/F] | [Class] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

| §1 Key | Surface | Finding Ref | Status |
|--------|---------|------------|--------|
| [S-01] | [text] | [F-x/none] | [COVERED--[S-01]/GAP--[S-01]] |
| [S-02] | [text] | [F-x/none] | [COVERED/GAP] |

§5.5 signal: [COVERED/PARTIAL]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract |
|------|----------|---------|---------|
| GOpen | [CHALLENGER] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [P/C/F] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

g_null progression: initial=[P/C/F]; post-domain=[P/C/F]; final=[P/C/F]. GClose consistent?[YES/NO]
Conflicts:[None]. Convergence:[concern]. Scope coverage:[None/gaps].

---

## DISPOSITION

Gate vector: GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]

```
GClose=FAIL?->BLOCKED. Gi=FAIL?->BLOCKED. Any COND?->CONDITIONAL. All PASS?->READY.
```

**Overall Disposition**: [READY/CONDITIONAL/BLOCKED]
**Primary driver**: [§16 -- one sentence]

---

## ACTION ITEM REGISTER

| CH-ID | Section | Gate | Verdict | Class | Item | Resolution |
|-------|---------|------|---------|-------|------|-----------|
| CH-001 | [section] | [gate] | [copy] | [copy] | [item] | [criterion] |
| -- | ADVISORY-OPEN-LENS | -- | -- | ADVISORY | [lens dim] | [criterion] |
| -- | ADVISORY-GAP | -- | -- | ADVISORY-GAP | [domain/surface] | [criterion] |

---

**Artifact to review:**

{{artifact}}
"""

V05 = r"""
---

## V-05

**Axis**: Full integration (three-axis) -- V-01 + V-02 + V-03
**Hypothesis**: V-04 provides the strongest single-pass C-38+C-23(v12) form: three-column NH
table with D1 and D2 both table-derivable and named in the derivation rule. V-05 adds V-03's
§0 PHASE 4 AGGREGATION RULE, making GClose derivable from a pre-committed formula applied to
an aggregated table rather than from editorial combination of three separately stated verdicts.
The combined form yields: (1) three-column NH table with D1 and D2 (inertia framing axis),
(2) derivation rule naming both differentials from the same table (phrasing register axis),
(3) pre-committed aggregation formula making BRACKET CLOSING GClose structurally derivable
(output format axis). Four independent protocol contracts pre-committed at §0: dimension table
spec, count binding, g_null derivation formula (two-differential), aggregation rule. Each
downstream section that re-scores the NH table contributes to the §0 PHASE 4 aggregation.
GClose is the final application of the pre-committed formula. Predicted: 225/225 on v11.

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. If a field cannot be
filled, write `[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK
==============================================================================

DISPOSITION_CONTRACT v1

§1 -- SCOPE ENUMERATION
  IN-SCOPE (assign [S-NN] key per row):
    [S-01] [SURFACE_1]
    [S-02] [SURFACE_2]
    [S-03] [SURFACE_3]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY
  1. [DOMAIN_1]  2. [DOMAIN_2]  3. [DOMAIN_3]
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]  HIGH=Blocks. MEDIUM=Conditions. LOW=Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]  G_domain_agg=worst-case. FAIL>CONDITIONAL>PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]  Each section: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]  CH-IDs assigned; PASS blocked if any OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  | Section | Gate | Verdict | Class | per verdict-emitting section. Copy verbatim.
  Excluded: §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  §0->Role Manifest->Bracket Opening->Domain(s)->§3.5->§3.8->§5.7->§5.8->
  Lifecycle->Bracket Closing->§5.5->Gate Vector Table->Cross-Role Signals->
  Disposition->Action Item Register.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]  SATURATED at §3.8; FULLY SATURATED at BRACKET CLOSING.

§8a -- CH-ID COUNT BINDING [IMMUTABLE]
  After BRACKET OPENING: ch_id_count=M. [CH-ID BIND: ch_id_count=M]
  §3.8 opens "ch_id_count=[M]". BRACKET CLOSING table has M rows.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  g_null stages 1-3. GClose=g_null(final) (or from §0 PHASE 4 aggregation, or named override).

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]  §5.5 KEY-CITATION: [S-NN] per row.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]  Section Severity=worst(all). Mechanical.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]  §5.7 ALL lens.verify entries per role.

§15a -- LENS ENTRY COUNT BINDING [IMMUTABLE]
  At ROLE MANIFEST: lens_entry_count_[R]=N. Write: [LENS BIND: role=[R], lens_entry_count=[N]]
  §5.7 completeness check cites count by name.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Precedence: GClose FAIL > Gi FAIL > GClose COND > G_lifecycle COND >
  G_domain_agg COND > GOpen COND > all PASS.

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  §5.7: {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L}

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]  K(d)=0->ADVISORY-GAP.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1 -- TABLE POPULATION (three-column form):
    Columns: Dimension | Status-Quo Score | Proposed-Build Score |
             Best-Non-Build-Alt Score | D1=(Build-SQ) | D2=(Build-Alt) |
             Per-Dim Verdict
    Minimum 2 dimensions.
    D1=(Proposed-Build)-(Status-Quo). D2=(Proposed-Build)-(Best-Non-Build-Alt).
    Per-Dim Verdict:
      BUILD-WINS    = D1>0 AND D2>0
      STATUS-QUO    = D1<=0
      BEST-ALT-WINS = D1>0 AND D2<=0
      TIED          = D1=0 AND D2=0
  PHASE 2 -- TABLE LOCK: DIMENSION TABLE LOCKED
  PHASE 2a -- DIMENSION COUNT BINDING: dimension_count=N (filled integer)
  PHASE 3 -- NH TESTIMONY: opens "Based on dimension_count=[N] rows..."
  g_null derivation (two-differential; both from three-column table):
    B_wins=count(BUILD-WINS; D1>0 AND D2>0)
    SQ_holds=count(STATUS-QUO; D1<=0)
    PASS if B_wins>dimension_count/2
    FAIL if SQ_holds>dimension_count/2
    CONDITIONAL otherwise
    Both D1 and D2 named explicitly. dimension_count referenced by name.
  PHASE 4 -- BRACKET CLOSING AGGREGATION RULE [IMMUTABLE]:
    Before GClose, BRACKET CLOSING produces an AGGREGATED NH TABLE (same three columns;
    dimension_count rows required):
      Agg_SQ  = max(SQ score from challenger, domain, lifecycle) [conservative worst SQ]
      Agg_Build = min(Build score from challenger, domain, lifecycle) [conservative weakest Build]
      Agg_Alt = max(Best-Alt score from challenger, domain, lifecycle) [conservative strongest Alt]
      D1_agg = Agg_Build - Agg_SQ
      D2_agg = Agg_Build - Agg_Alt
      Per-Dim Verdict_agg: BUILD-WINS if D1_agg>0 AND D2_agg>0; STATUS-QUO if D1_agg<=0;
                           BEST-ALT-WINS if D1_agg>0 AND D2_agg<=0; TIED otherwise.
    B_wins_agg=count(BUILD-WINS_agg); SQ_holds_agg=count(STATUS-QUO_agg)
    g_null_agg: PASS if B_wins_agg>dimension_count/2; FAIL if SQ_holds_agg>dimension_count/2; else CONDITIONAL.
    GClose must equal g_null_agg OR state override citing specific aggregated row.
    GClose is derivable from aggregated table cells alone. No editorial override needed
    for a well-scored artifact.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters: {{artifact_id}} / {{depth}} / {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

Lens entry count binding:
- [LENS BIND: role=[DOMAIN_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[LIFECYCLE_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[CHALLENGER_ROLE], lens_entry_count=[N]]

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

| Dimension | Status-Quo | Proposed-Build | Best-Non-Build-Alt | D1=(B-SQ) | D2=(B-Alt) | Per-Dim Verdict |
|-----------|-----------|---------------|-------------------|----------|-----------|-----------------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [+/-/0] | [BUILD-WINS/STATUS-QUO/BEST-ALT-WINS/TIED] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [+/-/0] | [BUILD-WINS/STATUS-QUO/BEST-ALT-WINS/TIED] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [+/-/0] | [BUILD-WINS/STATUS-QUO/BEST-ALT-WINS/TIED] |

**DIMENSION TABLE LOCKED**
**dimension_count = [N]**

NH TESTIMONY: "Based on dimension_count=[N] rows: B_wins=[N] (D1>0 AND D2>0),
SQ_holds=[N] (D1<=0)..."

§0 derivation: dimension_count=[N]; B_wins=[N]; SQ_holds=[N]
- B_wins>[N]/2? -> PASS; SQ_holds>[N]/2? -> FAIL; else CONDITIONAL
- **g_null(initial) from §0**: [PASS/CONDITIONAL/FAIL]

*(§0 PHASE 4 AGGREGATION RULE applies at BRACKET CLOSING: dimension_count=[N] rows,
three-column aggregation using max(SQ)/min(Build)/max(Alt) per row.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [One sentence.]
**Null hypothesis strength**: [HIGH/MEDIUM/LOW]

**Alternatives comparison table** *(bracket-wide; re-scored by all reviewers)*:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [sentence] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [sentence] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [sentence] |

**NULL HYPOTHESIS DERIVATION RULE** (three-column table; D1 and D2 named; §0 PHASE 3):
  B_wins=[N] (BUILD-WINS: D1>0 AND D2>0); SQ_holds=[N] (D1<=0); dimension_count=[N].
  PASS if B_wins>dimension_count/2. FAIL if SQ_holds>dimension_count/2. Else CONDITIONAL.
  Both D1 and D2 named. Override: cite specific dimension row.

**Challenge claims**:

| CH-ID | Claim | Severity |
|-------|-------|---------|
| CH-001 | [CLAIM_1] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [optional] | [H/M/L] |

[CH-ID BIND: ch_id_count = M]

**GOpen Verdict**: [P/C/F]
**g_null(initial) = GOpen = [P/C/F]**

*Local Gate Ledger Row:*
| BRACKET OPENING | GOpen | [P/C/F] | [Class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**Alternatives re-scoring** *(captures SQ, Build, Best-Alt scores for §0 PHASE 4 aggregation)*:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SQ_score] | [Build_score] | [Alt_score] | [sentence] |
| [DIM_2] | [SQ_score] | [Build_score] | [Alt_score] | [sentence] |
| [DIM_3] | [SQ_score] | [Build_score] | [Alt_score] | [sentence] |

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Additional Findings**:

| Finding | Surface | Severity |
|---------|---------|---------|
| F-1: [finding] | [SURFACE] | [H/M/L] |
| F-2: [finding] | [SURFACE] | [H/M/L] |

Section Severity = worst(F-1,F-2) = [H/M/L]

**G_domain Verdict**: [P/C/F]
**G_domain Reason**: [sentence]

*Local Gate Ledger Row:*
| DOMAIN -- [ROLE_NAME] | G_domain | [P/C/F] | [Class] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

G_domain_agg = [P/C/F]
g_null(post-domain) = worst([G_domain_agg],[g_null(initial)]) = **[P/C/F]**

---

## §3.8 -- CH-ID SATURATION CHECK

ch_id_count=[M] (§8a)

| CH-ID | Domain Response | SATURATED? |
|-------|----------------|-----------|
| CH-001 | [status] | [YES/NO] |
| CH-002 | [status] | [YES/NO] |

**SATURATION GATE**: [PASS/HALT]

---

## §5.7 -- LENS COVERAGE TABLE

**[DOMAIN_ROLE]** -- lens_entry_count=[N]:

| Lens Dimension | §17 Assertion | Status |
|---------------|--------------|--------|
| [entry 1] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |
| [entry 2] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |

Completeness: lens_entry_count_[DOMAIN_ROLE]=[N]; [K] emitted. [COMPLETE/INCOMPLETE]

**[LIFECYCLE_ROLE]** -- lens_entry_count=[N]:

| Lens Dimension | §17 Assertion | Status |
|---------------|--------------|--------|
| [entry 1] | {surface_anchor:"[S-NN]--[verbatim]",rating_basis:"[sentence]",rating:H/M/L} | [ADDRESSED/OPEN] |

Completeness: lens_entry_count_[LIFECYCLE_ROLE]=[N]; [K] emitted. [COMPLETE/INCOMPLETE]

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

| Domain (§1a) | R(d) HIGH | K(d) | Coverage |
|-------------|----------|------|---------|
| [DOMAIN_1] | {[roles]} | [N] | [COVERED/ADVISORY-GAP] |

§5.8 count assertion: certified [N] domains; [M] ADVISORY-GAP.

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen:[copy]; G_domain_agg:[copy]; g_null(post-domain):[copy]

**Alternatives re-scoring** *(captures SQ, Build, Best-Alt scores for §0 PHASE 4 aggregation)*:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SQ_score] | [Build_score] | [Alt_score] | [sentence] |
| [DIM_2] | [SQ_score] | [Build_score] | [Alt_score] | [sentence] |

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|---------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED/PARTIAL/OPEN] |

**Decision-readiness**: [Paragraph citing GOpen and G_domain_agg.]
**Null hypothesis status**: [yes/partial/no]

**Additional Findings**:

| Finding | Surface | Severity |
|---------|---------|---------|
| F-1: [finding] | [SURFACE] | [H/M/L] |

Section Severity = [H/M/L]

**G_lifecycle Verdict**: [P/C/F]
**G_lifecycle Reason**: [sentence]

*Local Gate Ledger Row:*
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [P/C/F] | [Class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
Received G_lifecycle:[copy]; g_null(post-domain):[copy]

**CH-ID Final Assessment** (ch_id_count=[M]):

| CH-ID | G_domain | G_lifecycle | Final | Notes |
|-------|---------|------------|-------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |

Fully SATURATED: [YES/NO]

**§0 PHASE 4 AGGREGATION TABLE** *(dimension_count=[N] rows; three-column form)*:

| Dimension | Agg_SQ (max) | Agg_Build (min) | Agg_Alt (max) | D1_agg | D2_agg | Verdict_agg |
|-----------|-------------|----------------|--------------|--------|--------|-------------|
| [DIM_1] | max([C],[D],[L]) | min([C],[D],[L]) | max([C],[D],[L]) | [+/-/0] | [+/-/0] | [BUILD-WINS/STATUS-QUO/BEST-ALT-WINS/TIED] |
| [DIM_2] | max([...]) | min([...]) | max([...]) | [+/-/0] | [+/-/0] | [...] |
| [DIM_3] | max([...]) | min([...]) | max([...]) | [+/-/0] | [+/-/0] | [...] |

B_wins_agg=[N]; SQ_holds_agg=[N]; dimension_count=[N]
g_null_agg: B_wins_agg>[N]/2? -> [PASS/CONDITIONAL/FAIL]
**g_null_agg = [PASS/CONDITIONAL/FAIL]**

**Remaining gaps**: [none / list]

g_null(final) = worst([G_lifecycle],[g_null(post-domain)]) = **[P/C/F]**

**GClose Verdict**: [P/C/F]
*(Must equal g_null_agg per §0 PHASE 4 rule, or state override citing specific aggregated row.)*
**Override invoked**: [YES/NO]
**GClose Rationale**: [2-3 sentences. Cite B_wins_agg=[N]/dimension_count=[N] if using aggregation.]

*Local Gate Ledger Row:*
| BRACKET CLOSING | GClose | [P/C/F] | [Class] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

| §1 Key | Surface | Finding Ref | Status |
|--------|---------|------------|--------|
| [S-01] | [text] | [F-x/none] | [COVERED--[S-01] in F-x / GAP--[S-01] not referenced] |
| [S-02] | [text] | [F-x/none] | [COVERED/GAP] |

§5.5 signal: [COVERED/PARTIAL]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract |
|------|----------|---------|---------|
| GOpen | [CHALLENGER] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [P/C/F] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

g_null progression: initial=[P/C/F]; post-domain=[P/C/F]; final=[P/C/F]. GClose consistent?[YES/NO]
Conflicts:[None/description]. Convergence:[concern]. Scope coverage:[None/gaps].

---

## DISPOSITION

Gate vector: GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]

```
GClose=FAIL?->BLOCKED. Gi=FAIL?->BLOCKED. Any COND?->CONDITIONAL. All PASS?->READY.
```

**Overall Disposition**: [READY/CONDITIONAL/BLOCKED]
**Primary driver**: [§16 -- one sentence]

---

## ACTION ITEM REGISTER

| CH-ID | Section | Gate | Verdict | Class | Item | Resolution |
|-------|---------|------|---------|-------|------|-----------|
| CH-001 | [section] | [gate] | [copy] | [copy] | [item] | [criterion] |
| -- | ADVISORY-OPEN-LENS | -- | -- | ADVISORY | [lens dim] | [criterion] |
| -- | ADVISORY-GAP | -- | -- | ADVISORY-GAP | [domain/surface] | [criterion] |

---

**Artifact to review:**

{{artifact}}
"""

with open(target, 'a', encoding='utf-8') as f:
    f.write(V02)
    f.write(V03)
    f.write(V04)
    f.write(V05)

print("done")
