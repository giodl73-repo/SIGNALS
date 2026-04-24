---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 14
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate R14

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R14 design target**: R13 V-05 scored 225/225 on v11 -- perfect. No v11 criterion remains
unsatisfied. R14 explores the next tier of binding discipline, targeting three patterns that
would become v12 criteria. The central insight from R13 is that the §0 NH Dimension Table
has two columns (Current-State / Proposed-State), producing one differential. A challenger
who compares Build against both the Status Quo and the best non-build alternative needs two
differentials -- D1=(Build-StatusQuo) and D2=(Build-BestAlt) -- to assert Build wins the
decision space. With only D1 in the table, the challenger concedes D2 by omission. R14
explores how to add D2 to the table structure and how to bind it into the derivation rule.

| R14 target pattern | What it requires | New mechanism |
|--------------------|-----------------|--------------|
| Three-column NH table | §0 Dimension Table has Status-Quo / Proposed-Build / Best-Non-Build-Alt columns; D1 and D2 as explicit derived columns | §0 column spec change + D1/D2 cells + DIMENSION TABLE LOCKED emits both |
| Two-differential derivation rule | NULL HYPOTHESIS DERIVATION RULE references both D1 and D2 by name; g_null derivable from table cells alone | §0 g_null formula covers D1 and D2; BRACKET OPENING derivation cites both |
| Pre-committed aggregation rule | BRACKET CLOSING NH table aggregation formula pre-stated in §0; challenger, domain, lifecycle scores combined via named rule | §0 PHASE 4 AGGREGATION block; BRACKET CLOSING references it by name |

**R14 axes:**

- V-01: Inertia framing (single axis) -- three-column NH Dimension Table. §0 replaces
  two-column (Current-State / Proposed-State) with three-column (Status-Quo / Proposed-Build /
  Best-Non-Build-Alt). Two explicit derived columns D1=(B-A) and D2=(B-C). g_null derivation
  formula updated to reference both D1 and D2 by name. dimension_count binding unchanged.
  C-23 co-activated: NH Derivation Rule now names both pairings explicitly.

- V-02: Phrasing register (single axis) -- two-differential derivation rule without structural
  table change. §0 keeps two-column NH Dimension Table but the NULL HYPOTHESIS DERIVATION
  RULE adds a second formula arm: D2 sourced from the BRACKET OPENING alternatives comparison
  table (Hybrid column = Best-Non-Build-Alt proxy). Rule states both D1 and D2 sources
  explicitly. g_null requires D1>0 AND D2>0 on majority of dimensions to reach PASS. Tests
  whether C-23 (two-differential coverage) is independently satisfiable without a third table column.

- V-03: Output format (single axis) -- NH TABLE AGGREGATION RULE pre-committed in §0.
  §0 adds PHASE 4 AGGREGATION block: before GClose, BRACKET CLOSING MUST produce an
  aggregated NH table using the pre-stated rule (worst-case per cell across challenger,
  domain, lifecycle scored rows). g_null(final) re-derived from the aggregated table, not
  from the individual re-score. Aggregated dimension_count must equal dimension_count bound
  at §0 PHASE 2a. Tests whether pre-committed aggregation strengthens GClose derivability.

- V-04: Inertia framing + Phrasing register (two-axis) -- V-01 three-column table AND
  V-01's updated derivation rule referencing D1 and D2 from the same three-column table.
  D2 no longer sourced from alternatives table (as in V-02); both differentials are
  table-derivable. Primary candidate for first full C-38 + C-23(v12) pass.

- V-05: Full integration (three-axis) -- V-01 + V-02 + V-03. Three-column NH table +
  two-differential derivation from table columns + pre-committed aggregation rule at BRACKET
  CLOSING. g_null(final) derivable from the aggregated table cells alone; no editorial
  override required for a well-scored artifact. Strongest inertia-framing form.

**Predicted R14 scores under v11:**
- V-01: 225/225 (three-column table strengthens C-35; no v11 criterion changes pass status)
- V-02: 225/225 (two-differential rule strengthens C-23 v11 pass condition, which already passes)
- V-03: 225/225 (aggregation rule is aspirational excellence, not a v11 criterion)
- V-04: 225/225
- V-05: 225/225

**Variation-specific v12 excellence signals:**
- V-01: Three-column NH table; D1 and D2 table-derivable -- could motivate C-38 (NH Dimension
  Table Three-Column Form Pre-committed)
- V-02: Derivation rule names both D1 and D2 sources -- could motivate C-23(v12 upgrade)
  (NH Derivation Rule Names Both Pairwise Differentials)
- V-03: Pre-committed aggregation rule; g_null(final) from aggregated table -- could motivate
  C-39 (NH Table Aggregation Rule Pre-committed at §0)
- V-04: C-38 + C-23(v12) simultaneously
- V-05: C-38 + C-23(v12) + C-39 -- unified inertia-framing discipline

---

## V-01

**Axis**: Inertia framing -- three-column NH Dimension Table with D1 and D2
**Hypothesis**: R13 V-05's §0 NH Dimension Table uses two data columns (Current-State,
Proposed-State) producing one differential. The challenger making a Build vs Status-Quo
decision also implicitly competes against the best alternative to building (the Hybrid or
the most viable workaround). Adding a third column Best-Non-Build-Alt and two explicit
derived columns D1=(B-A) and D2=(B-C) makes the three-way decision structure table-derivable.
The g_null formula then reads: B wins if D1>0 AND D2>0 on majority of dimensions. Both
claims are structural (derivable from cell arithmetic), not editorial. C-23 (multi-alternative
null hypothesis coverage) is co-activated because the derivation rule now explicitly names
the Build-vs-Hybrid pairing alongside Build-vs-StatusQuo. Predicted: 225/225 (C-35 strengthened;
C-23 re-confirmed with richer structure).

---

depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

---

```
==============================================================================
IMMUTABLE PROTOCOL BLOCK -- read all sections before executing any reviewer
==============================================================================

DISPOSITION_CONTRACT v1

§1 -- SCOPE ENUMERATION
[Fill before proceeding. Pre-reviewer gate.]
  IN-SCOPE surfaces (assign [S-NN] key to each row -- referenced in §5.5 and §17a):
    [S-01] [SURFACE_1]
    [S-02] [SURFACE_2]
    [S-03] [SURFACE_3 -- add rows as needed]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
  Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added -- [reason]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY
[Fill immediately after §1 COMPLETE. Derive atomic domain concerns from §1 IN-SCOPE
surfaces. Each domain = one addressable concern for a single reviewer role. Numbered list.
This inventory is the source set for §5.8 gap-check.]
  1. [DOMAIN_1]
  2. [DOMAIN_2]
  3. [DOMAIN_3 -- add rows as needed]
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally and may not be restated at any gate.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR any Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  any Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  If multiple DOMAIN sections: G_domain_agg = worst-case(all G_domain verdicts)
  Worst-case order: FAIL > CONDITIONAL > PASS
  Apply mechanically; do not aggregate editorially.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

==============================================================================

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  (a) Row syntax: | Section | Gate | Verdict | Class |
  (b) Emit at end of each verdict-emitting section, after verdict is stated.
  (c) Assembly rule: copy all local rows to ACTION ITEM REGISTER verbatim.
      Do NOT re-derive Gate Verdict or Class. The register is a copy, not a synthesis.
  Excluded sections (emit NO local ledger row):
    §3.5 Domain-Aggregate Checkpoint -- produces no verdict
    §3.8 CH-ID Saturation Check -- produces no verdict
    §5.5 Scope Coverage Reconciliation -- informational only
    §5.7 Lens Coverage Table -- informational only
    §5.8 Domain Coverage Gap-Check -- produces no verdict

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
  §0 Challenger Pre-Gate -> Role Manifest -> Bracket Opening -> Domain(s) ->
  §3.5 Domain-Aggregate Checkpoint -> §3.8 CH-ID Saturation Check ->
  §5.7 Lens Coverage Table -> §5.8 Domain Coverage Gap-Check ->
  Lifecycle -> Bracket Closing ->
  §5.5 Scope Coverage Reconciliation -> Gate Vector Table ->
  Cross-Role Signals -> Disposition -> Action Item Register
  Reordering is a contract violation.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED      = every CH-ID has >=1 response from a DOMAIN section
                   (verified at §3.8 before LIFECYCLE executes)
  FULLY SATURATED = every CH-ID has domain + lifecycle response
                   (verified at BRACKET CLOSING before GClose is stated)
  §3.8 SATURATION CHECK gate: LIFECYCLE does not begin until SATURATED.
  BRACKET CLOSING: PASS verdict prohibited if any CH-ID is UNSATURATED
  without a stated waiver citing the specific CH-ID and justification.

§8a -- CH-ID COUNT BINDING [IMMUTABLE]
  Immediately after BRACKET OPENING emits all CH-IDs, bind the count as a named variable:
    ch_id_count = M  (M = number of CH-IDs assigned; filled integer required)
    Write: [CH-ID BIND: ch_id_count = M]
  §3.8 CH-ID SATURATION CHECK must open with: "ch_id_count = [M] (bound at BRACKET OPENING)"
  BRACKET CLOSING CH-ID Final Assessment table must have exactly M rows. A table with fewer
  rows than ch_id_count = M is structurally incomplete. Count mismatch detectable without
  re-reading BRACKET OPENING.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial)     = GOpen
  Stage 2: g_null(post-domain) = worst-case(G_domain_agg, g_null(initial))
  Stage 3: g_null(final)       = worst-case(G_lifecycle, g_null(post-domain))
  GClose must equal g_null(final). Deviation requires explicit override with named
  justification. All three g_null values emitted as labeled fields at their respective
  checkpoints and summarized in Cross-Role Signals.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 SCOPE COVERAGE RECONCILIATION executes after BRACKET CLOSING.
  Maps each §1 IN-SCOPE surface to reviewer findings.
  COVERED = surface appears in >=1 finding.
  GAP     = no finding references this surface -> forced LOW advisory ->
            appended to ACTION ITEM REGISTER as ADVISORY-GAP.
  §5.5 emits COVERED/PARTIAL signal (informational only, no ledger row,
  excluded from §3 gate formula).
  §5.5 KEY-CITATION RULE: Each surface row must use its [S-NN] key from §1 index.
  Coverage verdict format: "COVERED -- [S-NN] referenced in F-[x]" or
  "GAP -- [S-NN] not referenced by any finding."

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Every finding row in every reviewer section carries an individual Severity field.
  Section Severity = worst(Severity of F-1, F-2, ...) over all findings in that section.
  Derived mechanically; no editorial section-level severity assignment permitted.
  Local gate ledger row carries the derived Section Severity.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  §5.7 LENS COVERAGE TABLE executes after all DOMAIN sections and before LIFECYCLE.
  For each active reviewer role: ALL lens.verify entries from that role's definition
  must appear in the table.
  Status per entry: ADDRESSED (>=1 finding references this dimension)
                 or OPEN (no finding referenced this dimension).
  OPEN entries -> automatically promoted to ADVISORY-OPEN-LENS items in ACTION ITEM REGISTER.
  §5.7 emits no gate verdict and no local ledger row (excluded from §6).

§15a -- LENS ENTRY COUNT BINDING [IMMUTABLE]
  At ROLE MANIFEST time, immediately after loading each role definition:
  For each active reviewer role [R]:
    Count the number of lens.verify entries in role [R]'s definition.
    Bind this count as a named variable: lens_entry_count_[R] = N
    Write: [LENS BIND: role=[R], lens_entry_count=[N]]
  §5.7 completeness check for role [R] must state:
    "lens_entry_count_[R] = [N] required; [K] rows emitted.
     Status: COMPLETE (K=N) / INCOMPLETE (K<N -- [N-K] entries missing)."
  ADVISORY-OPEN-LENS promotion summary must state:
    "[N] entries loaded at ROLE MANIFEST; [K] ADDRESSED; [N-K] OPEN."
  A §5.7 table for role [R] with fewer than lens_entry_count_[R] rows is structurally
  incomplete. Count mismatch detectable without reading the role definition.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  After all gate verdicts are known, apply the following precedence rules in order:
  Rule 1: If GClose = FAIL -> PRIMARY DRIVER = GClose
  Rule 2: If any other Gi = FAIL -> PRIMARY DRIVER = first FAIL gate in canonical order
  Rule 3: If GClose = CONDITIONAL -> PRIMARY DRIVER = GClose
  Rule 4: If G_lifecycle = CONDITIONAL -> PRIMARY DRIVER = G_lifecycle
  Rule 5: If G_domain_agg = CONDITIONAL -> PRIMARY DRIVER = G_domain_agg
  Rule 6: If GOpen = CONDITIONAL -> PRIMARY DRIVER = GOpen
  Rule 7: If all Gi = PASS -> PRIMARY DRIVER = GClose (final confirming gate)
  PRIMARY DRIVER emitted as labeled field at DISPOSITION.

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  Each row in the LENS COVERAGE TABLE (§5.7) carries an Applicability rating:
    HIGH   = lens dimension directly relevant to artifact's primary concerns
    MEDIUM = partial or indirect relevance
    LOW    = minimal relevance to the artifact type
  Applicability is artifact-specific -- NOT inherited from role definition.
  §17 TYPED ASSERTION BLOCK -- each applicability row uses this 3-field structure:
    {surface_anchor: "[S-NN] -- [verbatim §1 IN-SCOPE text]",
     rating_basis:   "[one sentence explaining why this tier applies]",
     rating:         HIGH / MEDIUM / LOW}
  CITATION VALIDITY RULE: surface_anchor must cite a [S-NN] key that exists in the §1
  index AND whose verbatim text matches. Validity by index lookup, not text-search.
  §17 must be complete before §18 executes.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  After §5.7 is populated (including §17 ratings), execute §5.8 DOMAIN COVERAGE GAP-CHECK:
  Let R(d) = {roles with HIGH applicability to domain d per §5.7}
  Let K(d) = |R(d)|
  K(d) = 0 -> ADVISORY-GAP for domain d
  For each domain in §1a ARTIFACT DOMAIN INVENTORY:
    Compute K(d). COVERED = K(d) >= 1. ADVISORY-GAP = K(d) = 0.
  Each ADVISORY-GAP domain appended to ACTION ITEM REGISTER with:
    Domain name (from §1a), K(d) = 0, R(d) = {}, Disposition class: ADVISORY-GAP
  §5.8 count assertion: "certified [N] domains from §1a; [M] ADVISORY-GAP identified"
  N must equal |§1a inventory|. Count mismatch = protocol error.
  §5.8 emits no gate verdict and no local ledger row (excluded from §6).

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1 -- TABLE POPULATION:
    Complete all dimension rows before writing any NH TESTIMONY prose.
    Columns: Dimension | Status-Quo Score | Proposed-Build Score |
             Best-Non-Build-Alt Score | D1=(Build-StatusQuo) | D2=(Build-BestAlt) |
             Per-Dim Verdict
    Minimum 2 dimensions.
    D1 = (Proposed-Build Score) - (Status-Quo Score). Positive = Build wins D1.
    D2 = (Proposed-Build Score) - (Best-Non-Build-Alt Score). Positive = Build wins D2.
    Per-Dim Verdict:
      BUILD-WINS    = D1 > 0 AND D2 > 0 (Build beats both alternatives on this dimension)
      STATUS-QUO    = D1 <= 0 (Status Quo holds on this dimension regardless of D2)
      BEST-ALT-WINS = D1 > 0 AND D2 <= 0 (Build beats Status Quo but best alt is competitive)
      TIED          = D1 = 0 AND D2 = 0
    Scores: numeric (0-10) or labeled (HIGH/MEDIUM/LOW/NONE).
  PHASE 2 -- TABLE LOCK:
    After all rows complete, emit: DIMENSION TABLE LOCKED
  PHASE 2a -- DIMENSION COUNT BINDING:
    Immediately after DIMENSION TABLE LOCKED, emit:
      dimension_count = N  (N = number of rows in table; filled integer required)
    Referenced by name in g_null derivation rule and NH TESTIMONY opening sentence.
  PHASE 3 -- NH TESTIMONY:
    Must open with: "Based on dimension_count=[bound value] dimension rows..."
    Off-table assessments are structurally inadmissible for g_null derivation.
  g_null(initial) derivation (table values only):
    B_wins = count(Per-Dim Verdict = BUILD-WINS)
    SQ_holds = count(Per-Dim Verdict = STATUS-QUO)
    B_wins > dimension_count/2 -> PASS  (Build wins majority on both D1 and D2)
    SQ_holds > dimension_count/2 -> FAIL (Status Quo holds majority)
    else -> CONDITIONAL
    Formula references dimension_count, B_wins, SQ_holds by name.
    GOpen must equal derivation result or state a named override citing specific dimension(s).

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

Review Parameters:
- Artifact: {{artifact_id}}
- Depth: {{depth}}
- Reviewer set: {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. CHALLENGER positions remain fixed.)*

Lens entry count binding (per §15a -- emit immediately after loading each role definition):
- [LENS BIND: role=[DOMAIN_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[LIFECYCLE_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[CHALLENGER_ROLE], lens_entry_count=[N]]

*(CHALLENGER lens entries counted for completeness but CHALLENGER does not contribute rows
to §5.7. CHALLENGER lens_entry_count is not verified against a §5.7 table.)*

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

*(Per §0 PHASE 1: complete all dimension rows before any NH TESTIMONY.)*

| Dimension | Status-Quo Score | Proposed-Build Score | Best-Non-Build-Alt Score | D1=(Build-SQ) | D2=(Build-Alt) | Per-Dim Verdict |
|-----------|-----------------|---------------------|--------------------------|--------------|----------------|-----------------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [+/-/0] | [BUILD-WINS / STATUS-QUO / BEST-ALT-WINS / TIED] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [+/-/0] | [BUILD-WINS / STATUS-QUO / BEST-ALT-WINS / TIED] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [+/-/0] | [+/-/0] | [BUILD-WINS / STATUS-QUO / BEST-ALT-WINS / TIED] |

**DIMENSION TABLE LOCKED**

**dimension_count = [N]**

**NH TESTIMONY** *(Derived from locked table only)*:
[Opening sentence required: "Based on dimension_count=[N] dimension rows in the locked
table, ...". Do not introduce assessments absent from a named table row.]

**§0 Table derivation**:
- dimension_count = [N]; B_wins (BUILD-WINS rows) = [N]; SQ_holds (STATUS-QUO rows) = [N]
- B_wins > dimension_count/2? [YES/NO] -> g_null candidate PASS
- SQ_holds > dimension_count/2? [YES/NO] -> g_null candidate FAIL
- else -> CONDITIONAL
- **g_null(initial) candidate from §0**: [PASS / CONDITIONAL / FAIL]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table** *(bracket-wide scaffold; re-scored by domain reviewers;
aggregated at BRACKET CLOSING -- per C-16)*:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [ONE_SENTENCE] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [ONE_SENTENCE] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [ONE_SENTENCE] |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed; mechanical application at GOpen)*:
  Apply §0 table derivation result directly as GOpen.
  g_null = PASS if B_wins > dimension_count/2 (Build wins D1 AND D2 on majority of dimensions).
  g_null = FAIL if SQ_holds > dimension_count/2 (Status Quo holds D1 on majority).
  g_null = CONDITIONAL otherwise.
  Override: state specific dimension name and justify departure from formula result.

**Challenge claims** *(assign CH-IDs; carry forward per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [CLAIM_3 -- optional] | [H/M/L] |

[CH-ID BIND: ch_id_count = M]  *(per §8a -- fill M with count of CH-IDs above)*

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
*(Must equal §0 derivation result or state override citing specific dimension(s).)*

**g_null(initial) = GOpen = [PASS / CONDITIONAL / FAIL]**

*Local Gate Ledger Row (per §6b):*
| BRACKET OPENING | GOpen | [PASS/CONDITIONAL/FAIL] | [BLOCKED/CONDITIONAL/ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]

**Alternatives re-scoring** *(same dimensions as BRACKET OPENING; this role's frame)*:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [ONE_SENTENCE] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [ONE_SENTENCE] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [ONE_SENTENCE] |

**CH-ID Response Table** *(mandatory -- PASS prohibited if any row = OPEN)*:

| CH-ID | Challenge Claim (copy) | Technical Response | Status |
|-------|----------------------|--------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings**:

| Finding | Artifact Surface | Severity |
|---------|----------------|---------|
| F-1: [specific finding from this role's lens.verify] | [SURFACE_NAME] | [H/M/L] |
| F-2: [finding] | [SURFACE_NAME] | [H/M/L] |

Section Severity = worst(F-1, F-2, ...) = [H/M/L] *(per §14)*

**Recommendation**: [One concrete action naming what to do and where.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

*Local Gate Ledger Row (per §6b):*
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS/CONDITIONAL/FAIL] | [BLOCKED/CONDITIONAL/ADVISORY] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

*(Per §6: NO local ledger row -- produces no verdict.)*

G_domain verdicts: [list all]
Applying §3a worst-case: **G_domain_agg = [PASS / CONDITIONAL / FAIL]**

g_null(post-domain) = worst-case(G_domain_agg, g_null(initial))
                    = worst-case([_], [_]) = **[PASS / CONDITIONAL / FAIL]**
*(Per §9 Stage 2: labeled field emitted here.)*

---

## §3.8 -- CH-ID SATURATION CHECK

*(Per §6: NO local ledger row. Per §8: LIFECYCLE does not begin until SATURATED.)*

ch_id_count = [M] (bound at BRACKET OPENING per §8a)

| CH-ID | Domain Response | SATURATED? |
|-------|----------------|-----------|
| CH-001 | [ADDRESSED/PARTIAL/OPEN] | [YES/NO] |
| CH-002 | [copy] | [YES/NO] |
| CH-003 | [copy if active] | [YES/NO] |

All SATURATED? [YES / NO -- if NO: state waiver or halt]

**SATURATION GATE**: [PASS -- LIFECYCLE may begin / HALT]

---

## §5.7 -- LENS COVERAGE TABLE

*(Per §6: NO local ledger row. Per §15: ALL lens.verify entries must appear.)*
*(Per §15a: lens_entry_count_[role] binding applied at ROLE MANIFEST.)*
*(Per §17: each row carries typed applicability assertion with [S-NN] key citation.)*

**[DOMAIN_ROLE_NAME]** -- lens_entry_count = [N] (bound at ROLE MANIFEST):

| Lens Dimension | Applicability (§17 typed assertion) | Status |
|---------------|-------------------------------------|--------|
| [lens.verify entry 1] | {surface_anchor: "[S-NN] -- [verbatim §1 text]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED / OPEN] |
| [lens.verify entry 2] | {surface_anchor: "[S-NN] -- [verbatim §1 text]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED / OPEN] |

Completeness check: lens_entry_count_[DOMAIN_ROLE_NAME] = [N] required; [K] rows emitted.
Status: [COMPLETE (K=N) / INCOMPLETE (K<N -- [N-K] entries missing)]
ADVISORY-OPEN-LENS summary: [N] entries loaded; [K] ADDRESSED; [N-K] OPEN.

**[LIFECYCLE_ROLE_NAME]** -- lens_entry_count = [N] (bound at ROLE MANIFEST):

| Lens Dimension | Applicability (§17 typed assertion) | Status |
|---------------|-------------------------------------|--------|
| [lens.verify entry 1] | {surface_anchor: "[S-NN] -- [verbatim §1 text]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED / OPEN] |

Completeness check: lens_entry_count_[LIFECYCLE_ROLE_NAME] = [N] required; [K] rows emitted.
Status: [COMPLETE / INCOMPLETE]
ADVISORY-OPEN-LENS summary: [N] entries loaded; [K] ADDRESSED; [N-K] OPEN.

Tier-based promotion:
- HIGH-applicability OPEN -> ADVISORY-OPEN-LENS (ACTION ITEM REGISTER)
- MEDIUM-applicability OPEN -> ADVISORY-LOW
- LOW-applicability OPEN -> no advisory

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(Per §6: NO local ledger row. Per §18: K(d) = |R(d)|; K(d) = 0 -> ADVISORY-GAP.)*

| Domain (from §1a) | R(d) -- HIGH roles | K(d) | Coverage |
|-------------------|-------------------|------|---------|
| [DOMAIN_1] | {[roles]} | [N] | [COVERED / ADVISORY-GAP] |
| [DOMAIN_2] | {} | 0 | ADVISORY-GAP |

§5.8 count assertion: certified [N] domains from §1a; [M] ADVISORY-GAP identified.
*(N must equal |§1a|. Mismatch = protocol error.)*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]; G_domain_agg: [copy]; g_null(post-domain): [copy from §3.5]

**Alternatives re-scoring** *(same dimensions; lifecycle/commitment frame)*:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [ONE_SENTENCE] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [ONE_SENTENCE] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [ONE_SENTENCE] |

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Commitment-Frame Response | Status |
|-------|----------------------|--------------------------|--------|
| CH-001 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness**: [Sufficient for commitment? One paragraph referencing GOpen and G_domain_agg.]

**Null hypothesis status**: [Given g_null(post-domain) and G_lifecycle evidence, defeated? yes/partial/no]

**Additional Findings**:

| Finding | Artifact Surface | Severity |
|---------|----------------|---------|
| F-1: [finding from this role's lens.verify] | [SURFACE] | [H/M/L] |
| F-2: [finding] | [SURFACE] | [H/M/L] |

Section Severity = worst(F-1, F-2, ...) = [H/M/L] *(per §14)*

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

*Local Gate Ledger Row (per §6b):*
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS/CONDITIONAL/FAIL] | [BLOCKED/CONDITIONAL/ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
Received G_lifecycle: [copy from LIFECYCLE -- labeled field]
Received g_null(post-domain): [copy from §3.5]

**CH-ID Final Assessment** *(ch_id_count = [M] per §8a; table must have M rows)*:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

Fully SATURATED check: [YES / NO -- PASS prohibited if UNSATURATED without waiver]

**Alternatives aggregated re-score**:

| Dimension | Challenger | Domain Agg | Lifecycle | Final |
|-----------|-----------|-----------|----------|-------|
| [DIM_1] | [score] | [score] | [score] | [aggregated] |
| [DIM_2] | [score] | [score] | [score] | [aggregated] |
| [DIM_3] | [score] | [score] | [score] | [aggregated] |

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs DEFEATED."]

g_null(final) = worst-case(G_lifecycle, g_null(post-domain))
              = worst-case([_], [_]) = **[PASS / CONDITIONAL / FAIL]**
*(Per §9 Stage 3.)*

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
*(Must equal g_null(final) or state override justification.)*

**Override invoked**: [YES / NO]

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per §3.

**GClose Rationale**: [2-3 sentences.]

*Local Gate Ledger Row (per §6b):*
| BRACKET CLOSING | GClose | [PASS/CONDITIONAL/FAIL] | [BLOCKED/CONDITIONAL/ADVISORY] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

*(Per §6: NO local ledger row -- informational only. Per §10 KEY-CITATION RULE: cite [S-NN].)*

| §1 Surface Key | Surface Text | Referenced in Finding(s) | Status |
|---------------|-------------|------------------------|--------|
| [S-01] | [verbatim §1 text] | [finding ref or "none"] | [COVERED -- [S-NN] in F-[x] / GAP -- [S-NN] not referenced] |
| [S-02] | [verbatim §1 text] | [finding ref or "none"] | [COVERED / GAP] |

GAP surfaces -> forced LOW advisory -> appended to ACTION ITEM REGISTER as ADVISORY-GAP.

§5.5 signal: [COVERED / PARTIAL -- [N] surfaces are GAP]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|--------------|
| GOpen | [CHALLENGER] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [P/C/F] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [P/C/F] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**g_null progression** *(per §9)*:
- g_null(initial) = [P/C/F] (= GOpen, BRACKET OPENING)
- g_null(post-domain) = [P/C/F] (= worst-case(G_domain_agg, g_null(initial)), §3.5)
- g_null(final) = [P/C/F] (= worst-case(G_lifecycle, g_null(post-domain)), BRACKET CLOSING)
- GClose consistent with g_null(final)? [YES / NO -- if NO: override reason]

**Conflicts**: [Incompatible CH-ID responses or findings across roles. If none: "None."]

**Convergence**: [Concern named by >=2 reviewers independently -- name it.]

**Scope coverage**: [§1 surface not covered by any reviewer. If all covered: "None."]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE above)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not alter the formula; do not reason editorially)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary driver**: [The gate verdict most responsible -- one sentence. Per §16 precedence rules.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*(Per §6c: copy all Local Gate Ledger rows verbatim. Do NOT re-derive.)*
*(CH-ID-indexed synthesis: each PARTIAL or HOLDS CH-ID produces one row.)*
*(ADVISORY-OPEN-LENS items from §5.7 appended. ADVISORY-GAP items from §5.5 and §5.8 appended.)*

| CH-ID | Section | Gate | Verdict | Class | Item Description | Resolution Criterion |
|-------|---------|------|---------|-------|-----------------|---------------------|
| CH-001 | BRACKET OPENING | GOpen | [copy] | [copy] | [What must be done] | [Criterion for closure] |
| CH-002 | [section] | [gate] | [copy] | [copy] | [Item] | [Criterion] |
| -- | BRACKET CLOSING | GClose | [copy] | [copy] | [Item] | [Criterion] |
| -- | ADVISORY-OPEN-LENS | -- | -- | ADVISORY | [lens dim from §5.7 OPEN] | [What would close this item] |
| -- | ADVISORY-GAP | -- | -- | ADVISORY-GAP | [domain from §5.8 / surface from §5.5] | [Criterion] |

---

**Artifact to review:**

{{artifact}}

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
