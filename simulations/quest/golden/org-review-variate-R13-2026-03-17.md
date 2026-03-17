---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 13
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate R13

5 complete prompt body variations. Single-axis first (V-01 through V-03), then
two-axis and three-axis combinations (V-04, V-05).

**R13 design target**: R12 V-04 and V-05 both achieved 225/225 under v11 -- the first
round to reach perfect score. No unsatisfied v11 criteria remain. R13 applies the three
excellence patterns extracted from R12 to protocol elements that are currently enforced
only by instruction (not by named-variable binding or structural key-citation):

| Excellence pattern (from R12) | R13 target | New mechanism |
|-------------------------------|-----------|--------------|
| Named-variable binding after sentinel creates propagation chain | C-31 lens exhaustion -- §5.7 row count is instructed but not counted | `lens_entry_count_[role] = N` bound at ROLE MANIFEST; §5.7 completeness check verifies count by name |
| Typed assertion block with verbatim-match makes provenance structural | C-33 surface_anchor -- verbatim text match requires text search | `[S-NN]` key labels on §1 IN-SCOPE surfaces; surface_anchor must cite key; lookup is index-based not text-search-based |
| Count assertion as enumeration forcing function | C-27 CH-ID saturation -- saturation verified by table scan but no bound count | `ch_id_count = M` bound after BRACKET OPENING's last CH-ID; §3.8 and BRACKET CLOSING must state `ch_id_count` by name |

**R13 axes:**

- V-01: Role sequence (single axis) -- §15a LENS ENTRY COUNT BINDING. At ROLE MANIFEST
  time, after reading each role definition, bind `lens_entry_count_[role] = N` as a named
  variable where N = number of `lens.verify` entries in that role's definition. §5.7 LENS
  COVERAGE TABLE for role [R] must emit a completeness check citing `lens_entry_count_[R]`
  by name. A table with fewer rows than the bound count is structurally incomplete -- count
  mismatch detectable without reading the role definition.

- V-02: Output format (single axis) -- §1 SURFACE KEY LABELS + §17a KEY-CITATION.
  §1 IN-SCOPE surfaces carry index keys `[S-01]`, `[S-02]`, etc. §17a TYPED ASSERTION
  BLOCK surface_anchor format changes from verbatim-only to key-and-verbatim:
  `"[S-NN] -- [verbatim §1 text]"`. CITATION VALIDITY RULE updated: surface_anchor must
  contain a §1 key that resolves to the cited text. Traceability becomes bidirectional:
  §1 assigns keys (forward), §17a cites by key (backward lookup by index, not text-search).

- V-03: Lifecycle emphasis (single axis) -- §8a CH-ID COUNT BINDING. Immediately after
  BRACKET OPENING emits all CH-IDs, bind `ch_id_count = M` as a named variable where M =
  number of CH-IDs assigned. §3.8 CH-ID SATURATION CHECK opening must state
  `ch_id_count = [M]`. BRACKET CLOSING saturation table must have exactly M rows. Named
  variable propagates: BRACKET OPENING → §3.8 → BRACKET CLOSING, parallel to
  dimension_count's propagation chain.

- V-04: Role sequence + Output format (two-axis) -- V-01 lens entry count binding +
  V-02 §1 surface key labels. Both C-31 enforcement (count-bound §5.7 completeness)
  and C-33 enforcement (key-indexed §17a traceability) upgraded to named-variable/
  structural form. C-35 count-binding pattern now applied at three protocol levels:
  dimension table (§0), lens table (§15a), alternatives table (C-16).

- V-05: Full integration (three-axis) -- V-01 + V-02 + V-03. Named-variable binding
  discipline applied to all four populated-list verification points: dimension_count (§0,
  C-35), lens_entry_count_[role] (§15a, C-31 upgrade), surface key index (§1/§17a, C-33
  upgrade), ch_id_count (§8a, C-27 upgrade). Four propagation chains; each independently
  verifiable without reading the generating section.

**Predicted R13 scores under v11:**
- V-01: 225/225 (lens count binding strengthens C-31 enforcement but does not change pass condition)
- V-02: 225/225 (key citation is a stronger form of C-33 surface_anchor; verbatim-match still present)
- V-03: 225/225 (CH-ID count binding strengthens C-27 saturation; pass condition unchanged)
- V-04: 225/225
- V-05: 225/225

**Variation-specific v12 excellence signals:**
- V-01: `lens_entry_count_[role]` bound at ROLE MANIFEST; §5.7 completeness check cites
  count by name -- could motivate C-36 (Lens Entry Count Binding Pre-committed)
- V-02: `[S-NN]` keys on §1 surfaces; §17a surface_anchor cites key for index-based
  lookup -- could motivate C-37 (§1 Surface Key Labels with §17a Key-Citation)
- V-03: `ch_id_count = M` bound after BRACKET OPENING; §3.8 and BRACKET CLOSING both
  reference the bound variable -- could motivate C-38 (CH-ID Count Binding Pre-committed)
- V-04: C-36 + C-37 simultaneously
- V-05: C-36 + C-37 + C-38 -- unified count/key binding discipline across all protocol lists

---

## V-01

**Axis**: Role sequence (single axis) -- §15a LENS ENTRY COUNT BINDING
**Hypothesis**: C-31 requires ALL `lens.verify` entries for each active reviewer role to
appear in §5.7 with ADDRESSED/OPEN status. The mechanism says "ALL entries must appear"
but the model can silently drop a lens.verify entry without producing a detectable
structural error. Adding `lens_entry_count_[role] = N` bound at ROLE MANIFEST time, and
requiring §5.7 to emit a completeness check that cites this count by name, closes the gap:
a table with N-1 rows fails the completeness check `lens_entry_count_[R] = N required; K
rows emitted` because K != N is machine-inspectable. All other mechanisms unchanged from
R12 V-05. Predicted: 225/225 (C-31 now count-enforced; no other criterion changes status).

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
  IN-SCOPE surfaces: [enumerate exhaustively -- these rows are cited in §5.5]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
  Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added -- [reason]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY
[Fill immediately after §1 COMPLETE. Derive atomic domain concerns from §1
IN-SCOPE surfaces. Each domain = one addressable concern for a single reviewer role.
Numbered list. This inventory is the source set for §5.8 gap-check.]
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
      Do NOT re-derive Gate Verdict or Class. The register is a copy, not
      a synthesis.
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

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial)     = GOpen
  Stage 2: g_null(post-domain) = worst-case(G_domain_agg, g_null(initial))
  Stage 3: g_null(final)       = worst-case(G_lifecycle, g_null(post-domain))
  GClose must equal g_null(final). Deviation requires explicit override with
  named justification. All three g_null values emitted as labeled fields at
  their respective checkpoints and summarized in Cross-Role Signals.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 SCOPE COVERAGE RECONCILIATION executes after BRACKET CLOSING.
  Maps each §1 IN-SCOPE surface to reviewer findings.
  COVERED = surface appears in >=1 finding.
  GAP     = no finding references this surface -> forced LOW advisory ->
            appended to ACTION ITEM REGISTER as ADVISORY-GAP.
  §5.5 emits COVERED/PARTIAL signal (informational only, no ledger row,
  excluded from §3 gate formula).

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Every finding row in every reviewer section carries an individual
  Severity field (HIGH / MEDIUM / LOW).
  Section Severity = worst(Severity of F-1, F-2, ...) over all findings
  in that section. Derived mechanically; no editorial section-level
  severity assignment permitted.
  Local gate ledger row carries the derived Section Severity.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  §5.7 LENS COVERAGE TABLE executes after all DOMAIN sections and before
  LIFECYCLE. For each active reviewer role: ALL lens.verify entries from
  that role's definition must appear in the table.
  Status per entry: ADDRESSED (>=1 finding references this dimension)
                 or OPEN (no finding referenced this dimension).
  OPEN entries -> automatically promoted to ADVISORY-OPEN-LENS items in
  ACTION ITEM REGISTER.
  §5.7 emits no gate verdict and no local ledger row (excluded from §6).

§15a -- LENS ENTRY COUNT BINDING [IMMUTABLE]
  At ROLE MANIFEST time, immediately after loading each role definition:
  For each active reviewer role [R]:
    Count the number of lens.verify entries in role [R]'s definition.
    Bind this count as a named variable: lens_entry_count_[R] = N
    Write: [LENS BIND: role=[R], lens_entry_count=[N]]
  This binding is named and referenced in §5.7:
    - §5.7 completeness check for role [R] must state:
      "lens_entry_count_[R] = [N] required; [K] rows emitted.
       Status: COMPLETE (K=N) / INCOMPLETE (K<N -- [N-K] entries missing)."
    - ADVISORY-OPEN-LENS promotion summary must state:
      "[N] entries loaded at ROLE MANIFEST; [K] ADDRESSED; [N-K] OPEN."
  A §5.7 table for role [R] with fewer than lens_entry_count_[R] rows is
  structurally incomplete. Count mismatch is detectable without reading
  the role definition -- lens_entry_count_[R] is the authoritative source.
  A placeholder [N] does not satisfy this requirement; the bound value
  must be a filled integer emitted at ROLE MANIFEST time.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  After all gate verdicts are known, apply the following precedence rules
  in order to select exactly one gate as PRIMARY DRIVER of DISPOSITION:
  Rule 1: If GClose = FAIL -> PRIMARY DRIVER = GClose
  Rule 2: If any other Gi = FAIL -> PRIMARY DRIVER = first FAIL gate in
          canonical order (GOpen, G_domain_agg, G_lifecycle)
  Rule 3: If GClose = CONDITIONAL -> PRIMARY DRIVER = GClose
  Rule 4: If G_lifecycle = CONDITIONAL -> PRIMARY DRIVER = G_lifecycle
  Rule 5: If G_domain_agg = CONDITIONAL -> PRIMARY DRIVER = G_domain_agg
  Rule 6: If GOpen = CONDITIONAL -> PRIMARY DRIVER = GOpen
  Rule 7: If all Gi = PASS -> PRIMARY DRIVER = GClose (final confirming gate)
  PRIMARY DRIVER emitted as labeled field at DISPOSITION.

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  Each row in the LENS COVERAGE TABLE (§5.7) carries an Applicability rating
  specific to the artifact under review:
    HIGH   = lens dimension directly relevant to artifact's primary concerns
    MEDIUM = partial or indirect relevance
    LOW    = minimal relevance to the artifact type
  Applicability is artifact-specific -- NOT inherited from role definition.
  Rating assigned at table-population time based on the artifact under review.
  Coverage expectation by tier:
    HIGH-applicability: ADDRESSED required; OPEN -> ADVISORY-OPEN-LENS
    MEDIUM-applicability: ADDRESSED preferred; OPEN -> ADVISORY-LOW
    LOW-applicability: OPEN acceptable; no ADVISORY-OPEN-LENS triggered
  §17 TYPED ASSERTION BLOCK -- each applicability row uses this 3-field structure:
    {surface_anchor: "[verbatim §1 IN-SCOPE text]",
     rating_basis:   "[one sentence explaining why this tier applies]",
     rating:         HIGH / MEDIUM / LOW}
  CITATION VALIDITY RULE: surface_anchor must contain text that appears verbatim
  in the §1 IN-SCOPE surface list. Generic archetype text fails by construction.
  §17 must be complete before §18 executes.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  After §5.7 LENS COVERAGE TABLE is populated (including §17 Applicability
  ratings), execute §5.8 DOMAIN COVERAGE GAP-CHECK:
  Let R(d) = {roles with HIGH applicability to domain d per §5.7}
  Let K(d) = |R(d)|
  K(d) = 0 -> ADVISORY-GAP for domain d
  For each domain in §1a ARTIFACT DOMAIN INVENTORY:
    Compute K(d). COVERED = K(d) >= 1. ADVISORY-GAP = K(d) = 0.
  Each ADVISORY-GAP domain appended to ACTION ITEM REGISTER with:
    - Domain name (from §1a), K(d) = 0, R(d) = {}, Disposition class: ADVISORY-GAP
  §5.8 count assertion: "certified [N] domains from §1a; [M] ADVISORY-GAP identified"
  N must equal |§1a inventory|. Count mismatch = protocol error.
  §5.8 emits no gate verdict and no local ledger row (excluded from §6).

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1 -- TABLE POPULATION:
    Complete all dimension rows before writing any NH TESTIMONY prose.
    Columns: Dimension | Current-State Score | Proposed-State Score |
             Differential | Per-Dim Verdict
    Minimum 2 dimensions. Per-Dim Verdict: BUILD-WINS / STATUS-QUO-WINS / TIED.
    Scores: numeric (0-10) or labeled (HIGH/MEDIUM/LOW/NONE).
  PHASE 2 -- TABLE LOCK:
    After all rows complete, emit: DIMENSION TABLE LOCKED
  PHASE 2a -- DIMENSION COUNT BINDING:
    Immediately after DIMENSION TABLE LOCKED, emit:
      dimension_count = N  (N = number of rows in table; filled integer required)
    Referenced by name in g_null derivation rule and NH TESTIMONY opening sentence.
  PHASE 3 -- NH TESTIMONY:
    Structurally subordinate to locked table.
    Must open with: "Based on dimension_count=[bound value] dimension rows..."
    Off-table assessments are structurally inadmissible for g_null derivation.
  g_null(initial) derivation (table values only):
    B = count of BUILD-WINS; S = count of STATUS-QUO-WINS
    B > dimension_count/2 -> PASS
    S > dimension_count/2 -> FAIL
    else -> CONDITIONAL
    Formula references dimension_count by name. GOpen must equal derivation
    result or state a named override citing specific dimension(s).

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

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

*(CHALLENGER lens entries are counted for completeness but CHALLENGER does not contribute
rows to §5.7. CHALLENGER lens_entry_count is not verified against a §5.7 table.)*

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

*(Per §0 PHASE 1: complete all dimension rows before any NH TESTIMONY.)*

| Dimension | Current-State Score | Proposed-State Score | Differential | Per-Dim Verdict |
|-----------|--------------------|--------------------|--------------|-----------------|
| [DIM_1] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_3] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**DIMENSION TABLE LOCKED**

**dimension_count = [N]**

**NH TESTIMONY** *(Derived from locked table only)*:
[Opening sentence required: "Based on dimension_count=[N] dimension rows in the locked
table, ..." Do not introduce assessments absent from a named table row.]

**§0 Table derivation**:
- B (BUILD-WINS count) = [N]; S (STATUS-QUO-WINS count) = [N]; dimension_count = [N]
- B > dimension_count/2? [YES/NO] -> g_null candidate PASS
- S > dimension_count/2? [YES/NO] -> g_null candidate FAIL
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
  g_null = PASS if Build beats Status Quo on >50% of dimensions AND Build beats Hybrid
           on majority of dimensions.
  g_null = FAIL if Status Quo beats Build on >50% of dimensions.
  g_null = CONDITIONAL otherwise.

**Challenge claims** *(assign CH-IDs; carry forward per §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [CLAIM_3 -- optional] | [H/M/L] |

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

**[DOMAIN_ROLE_NAME]** -- lens_entry_count = [N] (bound at ROLE MANIFEST):

| Lens Dimension | Applicability (§17 typed assertion) | Status |
|---------------|-------------------------------------|--------|
| [lens.verify entry 1] | {surface_anchor: "[verbatim §1 text]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED / OPEN] |
| [lens.verify entry 2] | {surface_anchor: "[verbatim §1 text]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED / OPEN] |

Completeness check: lens_entry_count_[DOMAIN_ROLE_NAME] = [N] required; [K] rows emitted.
Status: [COMPLETE (K=N) / INCOMPLETE (K<N -- [N-K] entries missing)]
ADVISORY-OPEN-LENS summary: [N] entries loaded; [K] ADDRESSED; [N-K] OPEN.

**[LIFECYCLE_ROLE_NAME]** -- lens_entry_count = [N] (bound at ROLE MANIFEST):

| Lens Dimension | Applicability (§17 typed assertion) | Status |
|---------------|-------------------------------------|--------|
| [lens.verify entry 1] | {surface_anchor: "[verbatim §1 text]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED / OPEN] |

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

**CH-ID Final Assessment**:

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

*(Per §6: NO local ledger row -- informational only. Per §10.)*

| §1 Surface | Referenced in Finding(s) | Status |
|-----------|------------------------|--------|
| [SURFACE_1] | [finding ref or "none"] | [COVERED / GAP] |
| [SURFACE_2] | [finding ref or "none"] | [COVERED / GAP] |

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

Gate vector:
- GOpen = [copy]; G_domain_agg = [copy]; G_lifecycle = [copy]; GClose = [copy]

Apply §3 formula:
```
GClose = FAIL? --> BLOCKED
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary Driver** *(per §16 formula -- state which rule fired)*:
Rule [N] fired: [gate] = [verdict] -> PRIMARY DRIVER = [gate]

**Conditions** *(if CONDITIONAL)*: [What must be resolved per gate order.]

**Blocker** *(if BLOCKED)*: [Specific finding. If GClose = FAIL: lead with challenger override.]

---

## ACTION ITEM REGISTER

*Assembly per §6c: copy local ledger rows verbatim. Do NOT re-derive.*

**Local gate ledger rows**:

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**CH-ID action items** *(PARTIAL or HOLDS from BRACKET CLOSING)*:

| CH-ID | Item | Gate Verdict | Class | Owner | Resolution Criterion |
|-------|------|-------------|-------|-------|---------------------|
| CH-001 | [what must be done] | [verdict] | [BLOCKED/CONDITIONAL/ADVISORY] | [ROLE] | [specific criterion] |

**ADVISORY-OPEN-LENS items** *(HIGH-applicability OPEN entries from §5.7)*:

| Role | Lens Dimension | lens_entry_count binding | Class |
|------|---------------|------------------------|-------|
| [ROLE] | [entry] | lens_entry_count_[ROLE]=[N]; this entry counted in binding | ADVISORY-OPEN-LENS |

**ADVISORY-GAP items** *(K(d)=0 domains from §5.8)*:

| Domain | K(d) | R(d) | Class |
|--------|------|------|-------|
| [DOMAIN] | 0 | {} | ADVISORY-GAP |

**ADVISORY-GAP items** *(uncovered §1 surfaces from §5.5)*:

| Surface | Status | Class |
|---------|--------|-------|
| [SURFACE] | GAP | ADVISORY-GAP |

---

**Artifact to review:**

{{artifact}}

---

## V-02

**Axis**: Output format (single axis) -- §1 SURFACE KEY LABELS + §17a KEY-CITATION
**Hypothesis**: C-33's typed assertion block requires surface_anchor to contain verbatim
text from §1 IN-SCOPE. This is a text-search test -- the inspector must locate the exact
string in §1's enumeration. If §1 surface descriptions are long or overlapping, the match
is ambiguous. Adding `[S-NN]` key labels to each §1 IN-SCOPE surface, and requiring
surface_anchor to cite the key (`"[S-01] -- [verbatim text]"`), shifts the provenance test
from text-search to index lookup: inspector checks whether the cited `[S-NN]` key exists
in §1 and matches the verbatim text. Bidirectional traceability: §1 assigns keys (forward
reference), §17a cites by key (backward lookup). A surface_anchor with a key that does not
appear in §1 is invalid by inspection -- no text-search required. All other mechanisms
unchanged from R12 V-05. Predicted: 225/225 (C-33 surface_anchor passes under strengthened
form; all other criteria unchanged).

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
  IN-SCOPE surfaces (assign sequential key labels [S-01], [S-02], ...
  to each surface at enumeration time; keys are cited in §17a surface_anchor fields):
    [S-01] [SURFACE_1]
    [S-02] [SURFACE_2]
    [S-03] [SURFACE_3 -- add rows as needed]
  (These keys are cited in §5.5 reconciliation and in §17a surface_anchor fields.)
  OUT-OF-SCOPE: [surface -- reason, or "None"]
  Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added as [S-NN] -- [reason]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY
[Fill immediately after §1 COMPLETE. Derive atomic domain concerns from §1 surfaces.]
  1. [DOMAIN_1]
  2. [DOMAIN_2]
  3. [DOMAIN_3 -- add rows as needed]
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  OR any Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  any Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst-case(all G_domain verdicts): FAIL > CONDITIONAL > PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  PASS verdict prohibited if any CH-ID row shows OPEN status.

==============================================================================

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  (a) Row syntax: | Section | Gate | Verdict | Class |
  (b) Emit at end of each verdict-emitting section, after verdict is stated.
  (c) Copy all local rows to ACTION ITEM REGISTER verbatim. Do NOT re-derive.
  Excluded: §3.5, §3.8, §5.5, §5.7, §5.8 -- these produce no verdict.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  §0 -> Role Manifest -> Bracket Opening -> Domain(s) ->
  §3.5 -> §3.8 -> §5.7 -> §5.8 -> Lifecycle -> Bracket Closing ->
  §5.5 -> Gate Vector Table -> Cross-Role Signals -> Disposition ->
  Action Item Register
  Reordering is a contract violation.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED      = every CH-ID has >=1 DOMAIN response (verified at §3.8)
  FULLY SATURATED = every CH-ID has domain + lifecycle response (verified at BRACKET CLOSING)
  LIFECYCLE does not begin until SATURATED.
  BRACKET CLOSING PASS prohibited if any CH-ID UNSATURATED without waiver.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial)     = GOpen
  Stage 2: g_null(post-domain) = worst-case(G_domain_agg, g_null(initial))
  Stage 3: g_null(final)       = worst-case(G_lifecycle, g_null(post-domain))
  GClose must equal g_null(final) or state named override.
  All three g_null values emitted as labeled fields at their checkpoints.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 executes after BRACKET CLOSING. Maps each §1 [S-NN] surface to findings.
  COVERED = surface in >=1 finding. GAP = no finding -> ADVISORY-GAP in register.
  §5.5 informational only; no ledger row.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Every finding row carries individual Severity (H/M/L).
  Section Severity = worst(all finding severities) -- derived, not assigned.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  §5.7 after all DOMAIN sections and before LIFECYCLE.
  ALL lens.verify entries for each role must appear with ADDRESSED/OPEN.
  OPEN -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.
  §5.7 emits no ledger row.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Rules 1-7 in order (same as V-01). PRIMARY DRIVER = labeled field at DISPOSITION.

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  Each §5.7 row carries an Applicability rating: HIGH / MEDIUM / LOW.
  Artifact-specific; not inherited from role definition.
  §17 TYPED ASSERTION BLOCK -- each applicability row structure:
    {surface_anchor: "[S-NN] -- [verbatim §1 IN-SCOPE text]",
     rating_basis:   "[one sentence]",
     rating:         HIGH / MEDIUM / LOW}
  SURFACE KEY REQUIREMENT:
    surface_anchor must cite the §1 key label ([S-NN]) that identifies the
    verbatim text. Format: "[S-NN] -- [verbatim §1 text]".
    A surface_anchor that contains verbatim text but no [S-NN] key is INVALID.
    A surface_anchor with a [S-NN] key that does not appear in §1 is INVALID.
    Invalid rows fail the citation validity test by index lookup -- no
    text-search interpretation required.
  CITATION VALIDITY RULE: surface_anchor valid iff:
    (1) contains a [S-NN] key that exists in §1, AND
    (2) verbatim text after "--" matches the text of that §1 surface.
  §17 must be complete before §18 executes.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  R(d) = {roles with HIGH applicability to domain d per §5.7}
  K(d) = |R(d)|; K(d) = 0 -> ADVISORY-GAP
  §5.8 count assertion: "certified [N] domains; [M] ADVISORY-GAP"
  N must equal |§1a|. Mismatch = protocol error.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  (Same as V-01: PHASE 1 table, PHASE 2 LOCK, PHASE 2a dimension_count binding,
  PHASE 3 NH TESTIMONY subordinate to locked table, g_null derivation formula
  referencing dimension_count by name.)

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters:
- Artifact: {{artifact_id}}
- Depth: {{depth}}
- Reviewer set: {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

*(Same structure as V-01: dimension table -> DIMENSION TABLE LOCKED -> dimension_count = N -> NH TESTIMONY.)*

| Dimension | Current-State | Proposed-State | Differential | Per-Dim Verdict |
|-----------|--------------|----------------|--------------|-----------------|
| [DIM_1] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |
| [DIM_2] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS / STATUS-QUO-WINS / TIED] |

**DIMENSION TABLE LOCKED**
**dimension_count = [N]**

**NH TESTIMONY**: "Based on dimension_count=[N] dimension rows in the locked table, ..."

**§0 Table derivation**: B=[N], S=[N], dimension_count=[N] -> **g_null(initial) = [P/C/F]**

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [one sentence]
**Null hypothesis strength**: [H/M/L]

**Alternatives comparison table**:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [note] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [note] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [note] |

**NULL HYPOTHESIS DERIVATION RULE**: [same formula as V-01]

**Challenge claims**:

| CH-ID | Claim | Severity |
|-------|-------|---------|
| CH-001 | [CLAIM] | [H/M/L] |
| CH-002 | [CLAIM] | [H/M/L] |

**GOpen**: [P/C/F] -- **g_null(initial) = GOpen = [P/C/F]**

*Local Gate Ledger Row:*
| BRACKET OPENING | GOpen | [P/C/F] | [class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**Alternatives re-scoring**: [same table structure as V-01]

**CH-ID Response Table**: [same structure as V-01]

**Additional Findings**:

| Finding | Surface | Severity |
|---------|---------|---------|
| F-1: [finding] | [SURFACE] | [H/M/L] |
| F-2: [finding] | [SURFACE] | [H/M/L] |

Section Severity = worst(F-1, F-2, ...) = [H/M/L]

**G_domain Verdict**: [P/C/F]

*Local Gate Ledger Row:*
| DOMAIN -- [ROLE] | G_domain | [P/C/F] | [class] |

---

## §3.5, §3.8

*(Same structure as V-01. §3.5 emits G_domain_agg and g_null(post-domain). §3.8 verifies saturation.)*

---

## §5.7 -- LENS COVERAGE TABLE

*(Per §15: ALL lens.verify entries. Per §17: TYPED ASSERTION BLOCK with KEY-CITATION.)*

**[DOMAIN_ROLE_NAME]**:

| Lens Dimension | Applicability (§17 key-citation typed assertion) | Status |
|---------------|--------------------------------------------------|--------|
| [entry 1] | {surface_anchor: "[S-01] -- [verbatim §1 text for S-01]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED/OPEN] |
| [entry 2] | {surface_anchor: "[S-02] -- [verbatim §1 text for S-02]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED/OPEN] |

*(CITATION VALIDITY: inspect [S-NN] key against §1 index. Key must exist. Verbatim text must match
the [S-NN] surface. No text-search required -- key lookup is sufficient.)*

**[LIFECYCLE_ROLE_NAME]**: [same structure]

Tier-based promotion: HIGH OPEN -> ADVISORY-OPEN-LENS; MEDIUM OPEN -> ADVISORY-LOW; LOW OPEN -> none.

---

## §5.8, LIFECYCLE, BRACKET CLOSING, §5.5, GATE VECTOR TABLE, CROSS-ROLE SIGNALS, DISPOSITION, ACTION ITEM REGISTER

*(Same structure as V-01. §5.8 uses K(d)=|R(d)| with count assertion. Lifecycle receives g_null(post-domain).
Bracket Closing aggregates alternatives table; g_null(final) = worst-case(G_lifecycle, g_null(post-domain)).
Disposition applies §3 formula mechanically. §16 PRIMARY DRIVER rule fires in order.
Action Item Register: verbatim copy of local ledger rows; CH-ID items; ADVISORY-OPEN-LENS; ADVISORY-GAP.)*

**Artifact to review:**

{{artifact}}

---

## V-03

**Axis**: Lifecycle emphasis (single axis) -- §8a CH-ID COUNT BINDING
**Hypothesis**: C-27 requires SATURATED/FULLY SATURATED tiers with a dedicated §3.8 gate
and BRACKET CLOSING prohibition. The saturation check verifies that every CH-ID has a
domain response, but the count of CH-IDs to verify is determined by scanning the BRACKET
OPENING table at §3.8 execution time -- there is no bound variable to check against. If
the model miscounts or silently omits a CH-ID at §3.8, the error is detectable only by
re-reading BRACKET OPENING. Adding `ch_id_count = M` bound immediately after BRACKET
OPENING emits all CH-IDs -- and requiring §3.8 and BRACKET CLOSING to each state
`ch_id_count = [M]` by name -- creates a propagation chain parallel to dimension_count:
BRACKET OPENING emits the count, §3.8 references it, BRACKET CLOSING verifies exactly M
rows exist in the saturation table. Count mismatch is detectable without re-reading
BRACKET OPENING. All other mechanisms unchanged from R12 V-05. Predicted: 225/225.

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
  IN-SCOPE surfaces: [enumerate exhaustively -- cited in §5.5]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY [derive from §1; source for §5.8]
  1. [DOMAIN_1]; 2. [DOMAIN_2]; 3. [DOMAIN_3]
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst-case(all G_domain): FAIL > CONDITIONAL > PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  BRACKET OPENING assigns CH-IDs. Every downstream section: mandatory CH-ID response table.
  PASS prohibited if any CH-ID = OPEN.

==============================================================================

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Syntax: | Section | Gate | Verdict | Class |
  Emit after each verdict. Copy verbatim to ACTION ITEM REGISTER. Do NOT re-derive.
  Excluded: §3.5, §3.8, §5.5, §5.7, §5.8 (no verdict emitted).

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  §0 -> Role Manifest -> Bracket Opening -> Domain(s) -> §3.5 -> §3.8 ->
  §5.7 -> §5.8 -> Lifecycle -> Bracket Closing -> §5.5 -> Gate Vector Table ->
  Cross-Role Signals -> Disposition -> Action Item Register
  Reordering is a contract violation.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED      = every CH-ID has >=1 DOMAIN response (verified §3.8)
  FULLY SATURATED = every CH-ID has domain + lifecycle response (verified BRACKET CLOSING)
  LIFECYCLE does not begin until SATURATED.
  BRACKET CLOSING PASS prohibited if any CH-ID UNSATURATED without waiver.

§8a -- CH-ID COUNT BINDING [IMMUTABLE]
  Immediately after BRACKET OPENING emits all CH-IDs:
    Count the number of CH-IDs assigned. Bind as: ch_id_count = M
    Write: [CH-ID BIND: ch_id_count = M]  (M = filled integer; not a placeholder)
  This binding is named and referenced in:
    - §3.8 SATURATION CHECK opening line:
        "Verifying ch_id_count=[M] CH-IDs from BRACKET OPENING."
      §3.8 saturation table must have exactly M rows. Fewer rows = protocol error.
    - BRACKET CLOSING saturation table:
        "Fully SATURATED check: ch_id_count=[M] CH-IDs; [M] rows in table."
      Table must have exactly ch_id_count rows. Count mismatch = UNSATURATED protocol error.
  Propagation chain: BRACKET OPENING (bind) -> §3.8 (verify M rows) ->
  BRACKET CLOSING (verify M rows again). Named variable is the authority at each step.
  A §3.8 or BRACKET CLOSING table with fewer than ch_id_count rows fails by count
  comparison without re-reading BRACKET OPENING.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen
  Stage 2: g_null(post-domain) = worst-case(G_domain_agg, g_null(initial))
  Stage 3: g_null(final) = worst-case(G_lifecycle, g_null(post-domain))
  GClose must equal g_null(final) or state named override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 after BRACKET CLOSING. COVERED/GAP per §1 surface. GAP -> ADVISORY-GAP. Informational.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Individual Severity per finding row. Section Severity = worst(). Derived mechanically.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  §5.7 after all DOMAIN, before LIFECYCLE. ALL lens.verify entries: ADDRESSED/OPEN.
  OPEN -> ADVISORY-OPEN-LENS. No ledger row.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Rules 1-7 in order. PRIMARY DRIVER = labeled field at DISPOSITION.

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  §5.7 rows carry typed assertion: {surface_anchor, rating_basis, rating}.
  surface_anchor: verbatim §1 IN-SCOPE text. Generic archetype text = INVALID.
  §17 complete before §18.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  R(d) = {roles with HIGH applicability to domain d}; K(d) = |R(d)|; K(d)=0 -> ADVISORY-GAP.
  §5.8 count assertion: N domains certified, M ADVISORY-GAP; N must equal |§1a|.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1 table -> PHASE 2 DIMENSION TABLE LOCKED -> PHASE 2a dimension_count = N ->
  PHASE 3 NH TESTIMONY (subordinate; opens with "Based on dimension_count=[N]...").
  g_null derivation: B > dimension_count/2 -> PASS; S > dimension_count/2 -> FAIL; else CONDITIONAL.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters:
- Artifact: {{artifact_id}}; Depth: {{depth}}; Reviewer set: {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

---

## §0 -- CHALLENGER PRE-GATE

*(Same structure as V-01: table -> LOCKED -> dimension_count = N -> NH TESTIMONY -> derivation.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [one sentence]. **Strength**: [H/M/L]

**Alternatives comparison table**:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [note] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [note] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [note] |

**NULL HYPOTHESIS DERIVATION RULE**: [same formula as V-01]

**Challenge claims**:

| CH-ID | Claim | Severity |
|-------|-------|---------|
| CH-001 | [CLAIM] | [H/M/L] |
| CH-002 | [CLAIM] | [H/M/L] |
| CH-003 | [optional] | [H/M/L] |

*(Per §8a: CH-ID assignment is now complete. Bind count immediately below.)*

**[CH-ID BIND: ch_id_count = [M]]**

*(M = number of CH-IDs assigned above; filled integer required. This value is referenced
by name at §3.8 and BRACKET CLOSING.)*

**GOpen**: [P/C/F] -- **g_null(initial) = [P/C/F]**

*Local Gate Ledger Row:*
| BRACKET OPENING | GOpen | [P/C/F] | [class] |

---

## DOMAIN -- [ROLE_NAME]

*(Same structure as V-01. CH-ID Response Table; findings with per-row Severity; G_domain verdict.)*

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

*(Same as V-01. G_domain_agg and g_null(post-domain) emitted.)*

---

## §3.8 -- CH-ID SATURATION CHECK

*(Per §6: NO ledger row. Per §8: LIFECYCLE blocked until SATURATED.)*
*(Per §8a: ch_id_count = [M] from BRACKET OPENING. This section must verify M CH-IDs.)*

**Verifying ch_id_count = [M] CH-IDs from BRACKET OPENING (§8a binding):**

| CH-ID | Domain Response | SATURATED? |
|-------|----------------|-----------|
| CH-001 | [ADDRESSED/PARTIAL/OPEN] | [YES/NO] |
| CH-002 | [copy] | [YES/NO] |
| CH-003 | [copy if active] | [YES/NO] |

Row count in this table: [K]. ch_id_count = [M]. K must equal M. [MATCH / MISMATCH -- protocol error]

All SATURATED? [YES / NO]

**SATURATION GATE**: [PASS -- LIFECYCLE may begin / HALT]

---

## §5.7 -- LENS COVERAGE TABLE

*(Same structure as V-01: typed assertion blocks with surface_anchor verbatim, no lens count binding.)*

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(Same as V-01: K(d)=|R(d)|, count assertion.)*

---

## LIFECYCLE -- [ROLE_NAME]

*(Same structure as V-01.)*

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
Received G_lifecycle: [copy]; g_null(post-domain): [copy from §3.5]

**CH-ID Final Assessment**:
*(Per §8a: ch_id_count = [M] from BRACKET OPENING. This table must have exactly M rows.)*

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|---------|------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |

Fully SATURATED check: ch_id_count = [M] CH-IDs; [K] rows in table.
K must equal ch_id_count. [MATCH -- FULLY SATURATED / MISMATCH -- protocol error]

**Alternatives aggregated re-score**: [same structure as V-01]

**Remaining gaps**: [none or list]

g_null(final) = worst-case(G_lifecycle, g_null(post-domain)) = **[P/C/F]**

**GClose**: [P/C/F]. **Override invoked**: [YES/NO].

*Local Gate Ledger Row:*
| BRACKET CLOSING | GClose | [P/C/F] | [class] |

---

## §5.5, GATE VECTOR TABLE, CROSS-ROLE SIGNALS, DISPOSITION, ACTION ITEM REGISTER

*(Same structure as V-01.)*

**Artifact to review:**

{{artifact}}

---

## V-04

**Axis**: Role sequence + Output format (two-axis) -- §15a LENS ENTRY COUNT BINDING + §1 SURFACE KEY LABELS
**Hypothesis**: V-01 demonstrates that lens_entry_count_[role] bound at ROLE MANIFEST
enables §5.7 completeness to be verified by count comparison rather than by reading the
role definition. V-02 demonstrates that [S-NN] key labels on §1 surfaces shift §17a
provenance from text-search to index lookup. Combining both upgrades applies the
named-variable/structural-key discipline to C-31 enforcement (lens count) and C-33
enforcement (surface key) simultaneously. No shared dependency: lens count binding
operates on role definitions at load time; surface key labels operate on §1 surfaces at
enumeration time. Both upgrades are additive to the R12 V-05 base. C-35 count-binding
pattern now applied at three levels: dimension table (§0), alternatives table (C-16 bracket
scaffold), lens table (§15a). Predicted: 225/225.

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
  IN-SCOPE surfaces (assign key labels [S-01], [S-02], ... to each surface;
  keys cited in §17a surface_anchor fields and in §5.5 reconciliation):
    [S-01] [SURFACE_1]
    [S-02] [SURFACE_2]
    [S-03] [SURFACE_3 -- add rows as needed]
  Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added as [S-NN] -- [reason]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY
  1. [DOMAIN_1]; 2. [DOMAIN_2]; 3. [DOMAIN_3]
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst-case: FAIL > CONDITIONAL > PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]

==============================================================================

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  (a) | Section | Gate | Verdict | Class |
  (b) Emit after each verdict.
  (c) Copy verbatim to ACTION ITEM REGISTER. No re-derivation.
  Excluded: §3.5, §3.8, §5.5, §5.7, §5.8.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  §0 -> Role Manifest -> Bracket Opening -> Domain(s) -> §3.5 -> §3.8 ->
  §5.7 -> §5.8 -> Lifecycle -> Bracket Closing -> §5.5 -> Gate Vector Table ->
  Cross-Role Signals -> Disposition -> Action Item Register

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED = every CH-ID has >=1 DOMAIN response. FULLY SATURATED = domain + lifecycle.
  §3.8 gate before LIFECYCLE. BRACKET CLOSING PASS prohibited if UNSATURATED.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial)=GOpen; Stage 2: worst-case(G_domain_agg, g_null(initial));
  Stage 3: worst-case(G_lifecycle, g_null(post-domain)). GClose=g_null(final) or override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 after BRACKET CLOSING. [S-NN] keys used in surface-to-finding mapping.
  GAP -> ADVISORY-GAP. Informational only.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Individual Severity per finding. Section Severity = worst(). Derived.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  §5.7 after DOMAIN, before LIFECYCLE. ALL lens.verify entries: ADDRESSED/OPEN.
  OPEN -> ADVISORY-OPEN-LENS. No ledger row.

§15a -- LENS ENTRY COUNT BINDING [IMMUTABLE]
  At ROLE MANIFEST time, for each active reviewer role [R]:
    Bind: lens_entry_count_[R] = N  (N = count of lens.verify entries in [R]'s definition)
    Write: [LENS BIND: role=[R], lens_entry_count=[N]]
  Referenced in §5.7 completeness check:
    "lens_entry_count_[R] = [N] required; [K] rows emitted.
     COMPLETE (K=N) / INCOMPLETE (K<N -- [N-K] entries missing)."
  Count mismatch detectable without reading role definition.
  ADVISORY-OPEN-LENS summary must state bound value: "[N] loaded; [K] ADDRESSED; [N-K] OPEN."

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE] [rules 1-7 as in V-01]

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  §5.7 typed assertion: {surface_anchor, rating_basis, rating}.
  SURFACE KEY REQUIREMENT (V-04 addition):
    surface_anchor format: "[S-NN] -- [verbatim §1 text]"
    [S-NN] must be a key that exists in §1.
    Verbatim text must match the §1 [S-NN] surface.
    CITATION VALIDITY RULE: valid iff key exists AND text matches.
    Invalid surface_anchor fails by index lookup -- no text-search required.
  §17 complete before §18.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  R(d) = {HIGH roles}; K(d) = |R(d)|; K(d)=0 -> ADVISORY-GAP.
  §5.8 count assertion: N domains, M ADVISORY-GAP; N = |§1a|.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1 table -> LOCKED -> dimension_count = N -> NH TESTIMONY subordinate.
  g_null derivation references dimension_count by name.

==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters:
- Artifact: {{artifact_id}}; Depth: {{depth}}; Reviewer set: {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

Lens entry count binding (per §15a):
- [LENS BIND: role=[DOMAIN_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[LIFECYCLE_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[CHALLENGER_ROLE], lens_entry_count=[N]]

---

## §0 -- CHALLENGER PRE-GATE

*(dimension table -> LOCKED -> dimension_count = N -> NH TESTIMONY. Same as V-01.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [one sentence]. **Strength**: [H/M/L]

**Alternatives comparison table**: [same 3-option Dimension/Status Quo/Build/Hybrid structure]

**NULL HYPOTHESIS DERIVATION RULE**: [same formula]

**Challenge claims**:

| CH-ID | Claim | Severity |
|-------|-------|---------|
| CH-001 | [CLAIM] | [H/M/L] |
| CH-002 | [CLAIM] | [H/M/L] |

**GOpen**: [P/C/F] -- **g_null(initial) = [P/C/F]**

*Local Gate Ledger Row:*
| BRACKET OPENING | GOpen | [P/C/F] | [class] |

---

## DOMAIN -- [ROLE_NAME]

*(Same structure as V-01.)*

---

## §3.5, §3.8

*(Same structure as V-01.)*

---

## §5.7 -- LENS COVERAGE TABLE

*(Per §15a: lens_entry_count binding; per §17 V-04: key-citation typed assertion.)*

**[DOMAIN_ROLE_NAME]** -- lens_entry_count = [N] (bound at ROLE MANIFEST):

| Lens Dimension | Applicability (key-citation typed assertion) | Status |
|---------------|---------------------------------------------|--------|
| [entry 1] | {surface_anchor: "[S-01] -- [verbatim §1 text for S-01]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED/OPEN] |
| [entry 2] | {surface_anchor: "[S-02] -- [verbatim §1 text for S-02]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED/OPEN] |

Completeness check: lens_entry_count_[DOMAIN_ROLE] = [N] required; [K] rows emitted.
[COMPLETE (K=N) / INCOMPLETE]
ADVISORY-OPEN-LENS summary: [N] entries loaded; [K] ADDRESSED; [N-K] OPEN.

**[LIFECYCLE_ROLE_NAME]** -- lens_entry_count = [N]: [same structure]

*(Citation validity: [S-NN] key must exist in §1; verbatim text must match that surface.
Both conditions required. Index lookup is sufficient -- no text-search needed.)*

---

## §5.8, LIFECYCLE, BRACKET CLOSING, §5.5, GATE VECTOR TABLE, CROSS-ROLE SIGNALS, DISPOSITION, ACTION ITEM REGISTER

*(Same structure as V-01. §5.8 K(d) predicate + count assertion. Lifecycle receives g_null(post-domain).
Bracket Closing aggregates table; g_null(final). Disposition by §3 formula. §16 PRIMARY DRIVER.
Action Item Register: verbatim ledger copy; CH-ID items; ADVISORY-OPEN-LENS with lens_entry_count
cited in promotion summary; ADVISORY-GAP items from §5.8 and §5.5.)*

**Artifact to review:**

{{artifact}}

---

## V-05

**Axis**: Full integration (three-axis) -- §15a LENS ENTRY COUNT BINDING + §1 SURFACE KEY LABELS + §8a CH-ID COUNT BINDING
**Hypothesis**: V-01, V-02, V-03 each apply the named-variable binding pattern to one
protocol list verification point. V-05 unifies all three simultaneously, extending the
count-binding discipline to every protocol checkpoint where a populated list must be
verified for completeness:

| Protocol list | Binding variable | Verification point | Introduced in |
|---------------|----------------|--------------------|--------------|
| NH dimension table rows | dimension_count | §0 PHASE 2a; g_null formula; NH opening | R12 (C-35) |
| lens.verify entries per role | lens_entry_count_[role] | §5.7 completeness check | V-01 R13 |
| Challenge claims (CH-IDs) | ch_id_count | §3.8 and BRACKET CLOSING saturation table | V-03 R13 |
| §1 IN-SCOPE surfaces (key-citation) | [S-NN] index | §17a surface_anchor validity | V-02 R13 |

The four bindings are independent: no binding depends on another. A model that mishandles
one list (e.g., produces a §5.7 table with fewer rows than lens_entry_count_[role]) fails
at that checkpoint specifically; the other three bindings are unaffected. The architecture
provides granular fault isolation: any verification failure is attributable to exactly one
list without reading other sections. Predicted: 225/225.

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
  IN-SCOPE surfaces (assign key labels [S-01], [S-02], ... at enumeration time;
  keys cited in §17a surface_anchor fields and in §5.5 reconciliation):
    [S-01] [SURFACE_1]
    [S-02] [SURFACE_2]
    [S-03] [SURFACE_3 -- add rows as needed]
  Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added as [S-NN] -- [reason]
  OUT-OF-SCOPE: [surface -- reason, or "None"]
§1 COMPLETE

§1a -- ARTIFACT DOMAIN INVENTORY [derive from §1; source for §5.8]
  1. [DOMAIN_1]; 2. [DOMAIN_2]; 3. [DOMAIN_3]
§1a COMPLETE

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst-case(all G_domain): FAIL > CONDITIONAL > PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  BRACKET OPENING assigns CH-IDs. Every downstream section: CH-ID response table.
  PASS prohibited if any CH-ID = OPEN.

==============================================================================

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  (a) | Section | Gate | Verdict | Class |
  (b) Emit at end of each verdict-emitting section.
  (c) Copy verbatim to ACTION ITEM REGISTER. Do NOT re-derive.
  Excluded: §3.5, §3.8, §5.5, §5.7, §5.8 (no verdict).

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  §0 -> Role Manifest -> Bracket Opening -> Domain(s) -> §3.5 -> §3.8 ->
  §5.7 -> §5.8 -> Lifecycle -> Bracket Closing -> §5.5 -> Gate Vector Table ->
  Cross-Role Signals -> Disposition -> Action Item Register
  Reordering is a contract violation.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED      = every CH-ID has >=1 DOMAIN response (§3.8 before LIFECYCLE)
  FULLY SATURATED = domain + lifecycle response (BRACKET CLOSING before GClose)
  LIFECYCLE blocked until SATURATED. BRACKET CLOSING PASS prohibited if UNSATURATED.

§8a -- CH-ID COUNT BINDING [IMMUTABLE]
  Immediately after BRACKET OPENING emits all CH-IDs:
    Bind: ch_id_count = M  (M = number of CH-IDs assigned; filled integer)
    Write: [CH-ID BIND: ch_id_count = M]
  Referenced by name in:
    §3.8 opening: "Verifying ch_id_count=[M] CH-IDs from BRACKET OPENING."
    §3.8 table: must have exactly M rows. Fewer rows = protocol error.
    BRACKET CLOSING saturation table: "ch_id_count=[M]; [K] rows emitted; K must = M."
  Propagation chain: BRACKET OPENING -> §3.8 -> BRACKET CLOSING.
  Count mismatch detectable at each step without re-reading BRACKET OPENING.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = GOpen
  Stage 2: g_null(post-domain) = worst-case(G_domain_agg, g_null(initial))
  Stage 3: g_null(final) = worst-case(G_lifecycle, g_null(post-domain))
  GClose must equal g_null(final) or state named override.
  All three g_null values emitted as labeled fields.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 after BRACKET CLOSING. Maps each §1 [S-NN] surface to findings.
  GAP -> ADVISORY-GAP. Informational only; no ledger row.

§14 -- PER-FINDING SEVERITY CHAIN [IMMUTABLE]
  Individual Severity per finding row. Section Severity = worst(). Derived mechanically.

§15 -- LENS EXHAUSTION PROTOCOL [IMMUTABLE]
  §5.7 after all DOMAIN, before LIFECYCLE. ALL lens.verify entries: ADDRESSED/OPEN.
  OPEN -> ADVISORY-OPEN-LENS. No ledger row.

§15a -- LENS ENTRY COUNT BINDING [IMMUTABLE]
  At ROLE MANIFEST time, for each active reviewer role [R]:
    Bind: lens_entry_count_[R] = N  (count of lens.verify entries in [R]'s definition)
    Write: [LENS BIND: role=[R], lens_entry_count=[N]]
  Referenced in §5.7 completeness check:
    "lens_entry_count_[R] = [N] required; [K] rows emitted.
     COMPLETE (K=N) / INCOMPLETE (K<N -- [N-K] entries missing)."
  ADVISORY-OPEN-LENS summary cites bound value: "[N] loaded; [K] ADDRESSED; [N-K] OPEN."
  Count mismatch detectable without reading role definition.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Rule 1: GClose=FAIL -> PRIMARY DRIVER=GClose
  Rule 2: Any other Gi=FAIL -> PRIMARY DRIVER=first FAIL in canonical order
  Rule 3: GClose=CONDITIONAL -> PRIMARY DRIVER=GClose
  Rule 4: G_lifecycle=CONDITIONAL -> PRIMARY DRIVER=G_lifecycle
  Rule 5: G_domain_agg=CONDITIONAL -> PRIMARY DRIVER=G_domain_agg
  Rule 6: GOpen=CONDITIONAL -> PRIMARY DRIVER=GOpen
  Rule 7: All PASS -> PRIMARY DRIVER=GClose
  PRIMARY DRIVER = labeled field at DISPOSITION.

§17 -- LENS APPLICABILITY PROTOCOL [IMMUTABLE]
  §5.7 rows carry typed assertion: {surface_anchor, rating_basis, rating}.
  SURFACE KEY REQUIREMENT:
    surface_anchor format: "[S-NN] -- [verbatim §1 text]"
    [S-NN] must exist as a key in §1 IN-SCOPE. Verbatim text must match that surface.
    CITATION VALIDITY RULE: valid iff (key exists in §1) AND (verbatim text matches).
    Invalid row fails by index lookup -- no text-search required.
  HIGH-applicability OPEN -> ADVISORY-OPEN-LENS. MEDIUM OPEN -> ADVISORY-LOW.
  §17 complete before §18.

§18 -- DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]
  R(d) = {roles with HIGH applicability to domain d per §5.7}
  K(d) = |R(d)|; K(d) = 0 -> ADVISORY-GAP
  §5.8 count assertion: "certified [N] domains from §1a; [M] ADVISORY-GAP"
  N must equal |§1a|. Count mismatch = protocol error.
  §5.8 emits no verdict; no ledger row.

§0 -- CHALLENGER NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  PHASE 1: complete all dimension rows (Dimension | Current | Proposed | Diff | Per-Dim Verdict).
  PHASE 2: emit DIMENSION TABLE LOCKED sentinel.
  PHASE 2a: bind dimension_count = N (filled integer). Referenced in g_null formula and NH opening.
  PHASE 3: NH TESTIMONY subordinate. Opens: "Based on dimension_count=[N] dimension rows..."
  g_null derivation: B>dimension_count/2->PASS; S>dimension_count/2->FAIL; else CONDITIONAL.
  GOpen must equal derivation or state named override citing specific dimension(s).

==============================================================================
NAMED-VARIABLE BINDING SUMMARY [informational -- lists all four binding points]
  dimension_count   : bound at §0 PHASE 2a; referenced in g_null formula + NH opening
  lens_entry_count_[R]: bound at ROLE MANIFEST per §15a; referenced in §5.7 completeness check
  ch_id_count       : bound after BRACKET OPENING per §8a; referenced in §3.8 + BRACKET CLOSING
  [S-NN] keys       : assigned at §1 enumeration; referenced in §17a surface_anchor fields
  These four bindings are independent. Failure at one binding point does not affect others.
==============================================================================
END IMMUTABLE PROTOCOL BLOCK
==============================================================================
```

---

## ROLE MANIFEST

Review Parameters:
- Artifact: {{artifact_id}}; Depth: {{depth}}; Reviewer set: {{reviewer_set}}

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For --depth deep: add DOMAIN-2, DOMAIN-3.)*

Lens entry count binding (per §15a -- emit after loading each role):
- [LENS BIND: role=[DOMAIN_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[LIFECYCLE_ROLE], lens_entry_count=[N]]
- [LENS BIND: role=[CHALLENGER_ROLE], lens_entry_count=[N]]

---

## §0 -- CHALLENGER PRE-GATE: NULL HYPOTHESIS DIMENSION TABLE

Contract: DISPOSITION_CONTRACT v1

| Dimension | Current-State | Proposed-State | Differential | Per-Dim Verdict |
|-----------|--------------|----------------|--------------|-----------------|
| [DIM_1] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS/STATUS-QUO-WINS/TIED] |
| [DIM_2] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS/STATUS-QUO-WINS/TIED] |
| [DIM_3] | [SCORE] | [SCORE] | [+/-/0] | [BUILD-WINS/STATUS-QUO-WINS/TIED] |

**DIMENSION TABLE LOCKED**
**dimension_count = [N]**

**NH TESTIMONY**: "Based on dimension_count=[N] dimension rows in the locked table, ..."

**§0 derivation**: B=[N], S=[N], dimension_count=[N]
-> **g_null(initial) = [PASS / CONDITIONAL / FAIL]**

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [one sentence]. **Strength**: [H/M/L]

**Alternatives comparison table** *(bracket-wide scaffold; re-scored by all reviewers)*:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [note] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [note] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [note] |

**NULL HYPOTHESIS DERIVATION RULE**:
  g_null = PASS if Build beats Status Quo AND Hybrid on >50% of dimensions.
  g_null = FAIL if Status Quo beats Build on >50% of dimensions.
  g_null = CONDITIONAL otherwise.

**Challenge claims**:

| CH-ID | Claim | Severity |
|-------|-------|---------|
| CH-001 | [CLAIM_1] | [H/M/L] |
| CH-002 | [CLAIM_2] | [H/M/L] |
| CH-003 | [CLAIM_3 -- optional] | [H/M/L] |

*(Per §8a: CH-ID assignment complete. Bind count immediately.)*

**[CH-ID BIND: ch_id_count = [M]]**

**GOpen**: [P/C/F] *(consistent with §0 derivation or override stated)*

**g_null(initial) = GOpen = [P/C/F]**

*Local Gate Ledger Row (per §6b):*
| BRACKET OPENING | GOpen | [P/C/F] | [BLOCKED/CONDITIONAL/ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**Alternatives re-scoring** *(same dimensions; this role's frame)*:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [note] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [note] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [note] |

**CH-ID Response Table**:

| CH-ID | Claim (copy) | Response | Status |
|-------|-------------|---------|--------|
| CH-001 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |
| CH-003 | [copy if active] | [response] | [ADDRESSED/PARTIAL/OPEN] |

**Additional Findings**:

| Finding | Surface | Severity |
|---------|---------|---------|
| F-1: [finding from this role's lens.verify] | [SURFACE] | [H/M/L] |
| F-2: [finding] | [SURFACE] | [H/M/L] |

Section Severity = worst(F-1, F-2, ...) = [H/M/L] *(per §14)*

**G_domain Verdict**: [P/C/F]. **Reason**: [one sentence.]

*Local Gate Ledger Row:*
| DOMAIN -- [ROLE] | G_domain | [P/C/F] | [class] |

---

## §3.5 -- DOMAIN-AGGREGATE CHECKPOINT

*(No ledger row.)*

G_domain_agg = worst-case([all G_domain]) = **[P/C/F]**

g_null(post-domain) = worst-case(G_domain_agg, g_null(initial)) = **[P/C/F]** *(per §9 Stage 2)*

---

## §3.8 -- CH-ID SATURATION CHECK

*(No ledger row. §8a binding applied here.)*

**Verifying ch_id_count = [M] CH-IDs from BRACKET OPENING (§8a binding):**

| CH-ID | Domain Response | SATURATED? |
|-------|----------------|-----------|
| CH-001 | [status] | [YES/NO] |
| CH-002 | [status] | [YES/NO] |
| CH-003 | [if active] | [YES/NO] |

Row count: [K]. ch_id_count = [M]. [MATCH (K=M) / MISMATCH -- protocol error]

**SATURATION GATE**: [PASS / HALT]

---

## §5.7 -- LENS COVERAGE TABLE

*(No ledger row. §15a count binding + §17 key-citation typed assertion -- both axes active.)*

**[DOMAIN_ROLE_NAME]** -- lens_entry_count = [N] (bound at ROLE MANIFEST per §15a):

| Lens Dimension | Applicability (§17 key-citation typed assertion) | Status |
|---------------|--------------------------------------------------|--------|
| [entry 1] | {surface_anchor: "[S-01] -- [verbatim §1 text for S-01]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED/OPEN] |
| [entry 2] | {surface_anchor: "[S-02] -- [verbatim §1 text for S-02]", rating_basis: "[sentence]", rating: H/M/L} | [ADDRESSED/OPEN] |

Completeness check: lens_entry_count_[DOMAIN_ROLE] = [N] required; [K] rows emitted.
[COMPLETE (K=N) / INCOMPLETE (K<N -- [N-K] entries missing)]
ADVISORY-OPEN-LENS summary: [N] entries loaded (lens_entry_count bound at ROLE MANIFEST); [K] ADDRESSED; [N-K] OPEN.

**[LIFECYCLE_ROLE_NAME]** -- lens_entry_count = [N]: [same structure]

*(§17 key-citation validity: [S-NN] key must exist in §1; verbatim text must match that surface.)*

---

## §5.8 -- DOMAIN COVERAGE GAP-CHECK

*(No ledger row. §18 predicate applied.)*

| Domain (from §1a) | R(d) -- HIGH roles | K(d) | Coverage |
|-------------------|-------------------|------|---------|
| [DOMAIN_1] | {[roles]} | [N] | [COVERED / ADVISORY-GAP] |
| [DOMAIN_2] | {} | 0 | ADVISORY-GAP |

§5.8 count assertion: certified [N] domains from §1a; [M] ADVISORY-GAP identified.
*(N must equal |§1a|.)*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]; G_domain_agg: [copy]; g_null(post-domain): [copy from §3.5]

**Alternatives re-scoring**:

| Dimension | Status Quo | Build | Hybrid | Notes |
|-----------|-----------|-------|--------|-------|
| [DIM_1] | [SCORE] | [SCORE] | [SCORE] | [note] |
| [DIM_2] | [SCORE] | [SCORE] | [SCORE] | [note] |
| [DIM_3] | [SCORE] | [SCORE] | [SCORE] | [note] |

**CH-ID Response Table**:

| CH-ID | Claim (copy) | Commitment-Frame Response | Status |
|-------|-------------|--------------------------|--------|
| CH-001 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |
| CH-002 | [copy] | [response] | [ADDRESSED/PARTIAL/OPEN] |
| CH-003 | [if active] | [response] | [ADDRESSED/PARTIAL/OPEN] |

**Decision-readiness**: [paragraph referencing GOpen and G_domain_agg]

**Null hypothesis status**: [g_null(post-domain) context -- defeated/partial/no -- one sentence]

**Additional Findings**:

| Finding | Surface | Severity |
|---------|---------|---------|
| F-1: [finding] | [SURFACE] | [H/M/L] |
| F-2: [finding] | [SURFACE] | [H/M/L] |

Section Severity = worst(F-1, F-2, ...) = [H/M/L]

**G_lifecycle Verdict**: [P/C/F]. **Reason**: [one sentence.]

*Local Gate Ledger Row:*
| LIFECYCLE -- [ROLE] | G_lifecycle | [P/C/F] | [class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
Received G_lifecycle: [copy]; g_null(post-domain): [copy]

**CH-ID Final Assessment** *(per §8a: ch_id_count = [M]; table must have M rows)*:

| CH-ID | G_domain | G_lifecycle | Final Status | Notes |
|-------|---------|------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-002 | [copy] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |
| CH-003 | [if active] | [copy] | [DEFEATED/PARTIAL/HOLDS] | [note] |

Fully SATURATED check: ch_id_count = [M]; [K] rows in table.
[MATCH (K=M) -- FULLY SATURATED / MISMATCH -- protocol error]

**Alternatives aggregated re-score** *(compile all reviewer re-scores; §3a worst-case)*:

| Dimension | Challenger | Domain Agg | Lifecycle | Aggregated |
|-----------|-----------|-----------|----------|-----------|
| [DIM_1] | [score] | [score] | [score] | [worst-case] |
| [DIM_2] | [score] | [score] | [score] | [worst-case] |
| [DIM_3] | [score] | [score] | [score] | [worst-case] |

**Remaining gaps**: [none or list]

g_null(final) = worst-case(G_lifecycle, g_null(post-domain)) = **[P/C/F]** *(per §9 Stage 3)*

**GClose**: [P/C/F]. **Override invoked**: [YES/NO].

**GClose override authority**: GClose = FAIL overrides all prior verdicts per §3.

**GClose Rationale**: [2-3 sentences.]

*Local Gate Ledger Row:*
| BRACKET CLOSING | GClose | [P/C/F] | [class] |

---

## §5.5 -- SCOPE COVERAGE RECONCILIATION

*(No ledger row. Maps §1 [S-NN] surfaces to findings.)*

| §1 Surface | Referenced in Finding(s) | Status |
|-----------|------------------------|--------|
| [S-01] [SURFACE_1] | [ref or "none"] | [COVERED / GAP] |
| [S-02] [SURFACE_2] | [ref or "none"] | [COVERED / GAP] |

GAP -> ADVISORY-GAP in ACTION ITEM REGISTER.
§5.5 signal: [COVERED / PARTIAL -- [N] GAP]

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
- g_null(initial) = [P/C/F] (GOpen, BRACKET OPENING)
- g_null(post-domain) = [P/C/F] (§3.5)
- g_null(final) = [P/C/F] (BRACKET CLOSING)
- GClose consistent with g_null(final)? [YES / NO -- override reason if NO]

**Binding summary** *(informational)*:
- dimension_count = [N] (§0); ch_id_count = [M] (BRACKET OPENING)
- lens_entry_count_[DOMAIN_ROLE] = [N]; lens_entry_count_[LIFECYCLE_ROLE] = [N]

**Conflicts**: [incompatible CH-ID responses or findings across roles; or "None."]

**Convergence**: [concern named by >=2 reviewers independently]

**Scope coverage**: [§1 surface uncovered; or "None."]

---

## DISPOSITION

Gate vector:
- GOpen = [copy]; G_domain_agg = [copy]; G_lifecycle = [copy]; GClose = [copy]

Apply §3 formula:
```
GClose = FAIL? --> BLOCKED
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Primary Driver** *(per §16 -- state which rule fired)*:
Rule [N] fired: [gate] = [verdict] -> PRIMARY DRIVER = [gate]

**Conditions** *(if CONDITIONAL)*: [per gate order]

**Blocker** *(if BLOCKED)*: [if GClose=FAIL: lead with "Challenger override: [GClose rationale]"]

---

## ACTION ITEM REGISTER

*Assembly per §6c: copy all local gate ledger rows verbatim. Do NOT re-derive.*

**Local gate ledger rows** *(verbatim copy)*:

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**CH-ID action items** *(PARTIAL or HOLDS from BRACKET CLOSING)*:

| CH-ID | Item | Gate Verdict | Class | Owner | Resolution Criterion |
|-------|------|-------------|-------|-------|---------------------|
| CH-001 | [what must be done] | [verdict] | [class] | [ROLE] | [criterion] |

**ADVISORY-OPEN-LENS items** *(HIGH-applicability OPEN entries from §5.7)*:

| Role | Lens Dimension | Binding Evidence | Class |
|------|---------------|-----------------|-------|
| [ROLE] | [entry] | lens_entry_count_[ROLE]=[N]; entry [K] of [N] in binding | ADVISORY-OPEN-LENS |

**ADVISORY-GAP items** *(K(d)=0 from §5.8)*:

| Domain | K(d) | R(d) | Class |
|--------|------|------|-------|
| [DOMAIN] | 0 | {} | ADVISORY-GAP |

**ADVISORY-GAP items** *(GAP surfaces from §5.5)*:

| Surface ([S-NN]) | Status | Class |
|-----------------|--------|-------|
| [S-NN] [SURFACE] | GAP | ADVISORY-GAP |

---

**Artifact to review:**

{{artifact}}
