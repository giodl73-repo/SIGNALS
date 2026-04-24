Reading the scorecard, I identify three new excellence patterns from Round 11:

- **V-01**: ANTI-PATTERN REGISTRY CA-1 FIRING AUDIT closure (two-endpoint execution record for AP suppression)
- **V-02**: TABLE_5 SOURCE-LINK provenance columns (mechanically verifiable C-11 compliance by column scan)
- **V-03**: CRITERION-PHASE-MAP with PHASE-LATE terminal verdict (phase-ordering of criterion verification auditable from CA-1)

These become C-33, C-34, C-35. Aspirational tier grows from 125 → 140 pts; total from 215 → 230.

---

# trace-permissions Rubric — v11

**Three new criteria from Round 11 (sourced from V-01, V-02, V-03):**

| ID | Name | What it formalizes |
|----|------|--------------------|
| C-33 | ANTI-PATTERN REGISTRY CA-1 FIRING AUDIT closure | C-21 requires the declaration side of anti-pattern suppression: each AP-identifier carries a violation condition and reactive marker token in Phase 0. C-33 requires the closure side: CA-1 closes every declared AP-identifier with a FIRED / NOT-FIRED terminal verdict. A NOT-FIRED result names the exact SE section where the reactive marker was expected to appear. This converts anti-pattern suppression from a one-endpoint declaration into a two-endpoint execution record — a reviewer confirms suppression by reading the CA-1 FIRING AUDIT, not the SE section body. C-21 makes anti-patterns declared; C-33 makes their suppression auditable without re-reading SE prose. |
| C-34 | TABLE_5 SOURCE-LINK provenance columns | C-11 requires findings to be registered inline at the point of discovery — enforced by a RULE block and Phase 0 gate prose. These are timing claims, readable only in context. C-34 requires TABLE_5 to carry three provenance columns (`Source Table \| Source Row \| Discovery Phase`) so that C-11 compliance is mechanically verifiable by column scan: a Discovery Phase value outside the "PHASE 2 SE-N" pattern is a deferred-registration violation detectable without reading prose timing context. CA-1 SOURCE-LINK AUDIT enforces that no TABLE_5 row carries a Discovery Phase outside this pattern. C-11 makes registration timing a prose commitment; C-34 makes it a structurally scannable inter-table property. |
| C-35 | CRITERION-PHASE-MAP with PHASE-LATE terminal verdict | C-20 requires CA-1 to carry PASS / FAIL terminal verdicts per registry table. C-35 requires a CRITERION-PHASE-MAP declared at Phase 0 pre-committing each tracked criterion to the SE phase where its evidence will appear, and extends CA-1 with a PHASE-LATE terminal verdict that fires when criterion evidence first appears in an SE section later than declared in the map. C-20 makes criterion verification binary; C-35 makes phase-ordering of verification commitments auditable — a reviewer detects phase discipline failures from CA-1 PHASE-LATE verdicts without reading SE section bodies. C-20 tracks whether criteria were satisfied; C-35 tracks whether they were satisfied on schedule. |

**Three prior criteria from Round 10 (carried forward unchanged):**

| ID | Name | What it formalizes |
|----|------|--------------------|
| C-30 | Criterion-ID-bearing column headers | Column headers of enforcement tables (e.g., PROTOCOL REGISTRY) embed criterion IDs — "Field Name (C-NN: rubric phrase)" — so a scorer verifies C-28/C-29 by reading the column header without opening the rubric. C-27 operates at instruction-text granularity; C-30 operates at table-column granularity. |
| C-31 | Formal activation-class tokens | Activation class expressed as a formal two-value constant (DEFERRED-PENDING / IMMEDIATELY-ACTIVE) threading identically through all four sites: REGISTRY column value, ACTIVATED token suffix, per-consumption-site annotation suffix, LOG table column. C-28 requires correct semantics; C-31 requires machine-scannable constants — making C-28 compliance mechanically greppable across documents. |
| C-32 | Per-activation-site REGISTRY-ID embedding | Resolves C-28's "all activation points by name" requirement for unbounded ACTIVE-class protocols. Instead of statically pre-listing unknown instances at Phase 0 declaration, the REGISTRY-ID is embedded in the annotation form at each consumption site — so each FLS ENTRY block, when instantiated, carries the ID at execution time. This is why V-01–V-04 scored 195/200 (class description, no per-site ID) while V-05 scored 200/200. |

**Tier totals:**

| Tier | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-35 | 140 |
| **Total** | | **230** |

**Design notes:**

- **C-28 vs C-26**: C-26 requires both protocols to carry "an explicit PENDING state" in the ACTIVATION STATE LOG. R9 variations show that Per-Stage Chain-Reminder is immediately active from Phase 0 and correctly carries `ACTIVE` state rather than `PENDING` — and still pass C-26 because the body block and lifecycle machinery exist. C-28 formalizes what C-26 treats as acceptable variation: the state assigned to a body block must match the protocol's activation timing, and the broken-obligation semantics must be drawn from the correct state-class template. C-26 makes obligations trackable. C-28 makes obligation state semantically accurate by class, and broken-obligation wording operationally appropriate.

- **C-29 vs C-26**: C-26 requires the broken-obligation note to convey that an unresolved PENDING equals a broken obligation. C-29 requires the note to additionally name the trace phase where the broken state becomes visible. The difference is operational: a C-26-compliant note tells a reviewer what broken means; a C-29-compliant note tells a reviewer where to look. A prompt can satisfy C-26 with "unresolved PENDING at trace close = broken obligation" and fail C-29 because no phase identifier anchors the detection point.

- **C-28 and C-29 are independent**: A variation can satisfy C-28 (correct state-class assignment and semantics for both protocols) without satisfying C-29 (no phase-anchored broken-obligation note for the PENDING protocol). A variation can satisfy C-29 (STEP-1-CLOSE-TOKEN note names Phase 5b) without satisfying C-28 (Per-Stage still uses PENDING with wrong broken-obligation wording). V-04 satisfies both.

- **C-33 vs C-21**: C-21 requires the declaration side of each anti-pattern entry — unique identifier, violation condition, and reactive marker token. A variation satisfying C-21 commits AP identifiers at Phase 0 but makes no structural promise about whether those markers fired. C-33 requires the closure side: CA-1 must carry a FIRING AUDIT that closes every declared AP-identifier with FIRED / NOT-FIRED. A NOT-FIRED verdict without naming the specific SE section = fail. C-21 makes anti-patterns declared; C-33 makes their suppression a two-endpoint execution record.

- **C-34 vs C-11**: C-11 requires inline registration — findings must be entered at the point of discovery, enforced via Phase 0 gate prose and RULE blocks. These mechanisms are prose-level: compliance requires reading the SE section in context to verify timing. C-34 requires TABLE_5 provenance columns that make C-11 compliance mechanically verifiable by column scan — Discovery Phase "PHASE 2 SE-N" or violation. CA-1 SOURCE-LINK AUDIT closes the loop. C-11 makes timing a commitment; C-34 makes it a structurally scannable property.

- **C-35 vs C-20**: C-20 requires CA-1 to carry PASS / FAIL terminal verdicts per registry table — binary outcome per criterion. C-35 requires a Phase 0 CRITERION-PHASE-MAP pre-committing each criterion to a named SE phase, and extends CA-1 with PHASE-LATE as a third terminal state alongside PASS / FAIL. PHASE-LATE fires when evidence appears in a later phase than declared. A variation can pass C-20 (all verdicts present, correct PASS/FAIL) and fail C-35 (no map, no PHASE-LATE state). C-20 makes verification auditable; C-35 makes phase discipline auditable.

- **C-33, C-34, C-35 are independent**: Each formalizes a different closure mechanism — AP suppression audit, finding-provenance inter-table linkage, and criterion phase-ordering commitment. A variation can implement any combination independently. All three were observed simultaneously in Round 11 because variations carried the full R10-V-05 core and added one structural closure each.

**Tier totals after v11:**

| Tier | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-35 | 140 |
| **Total** | | **230** |

Golden threshold unchanged: all Essential pass + composite >= 80.

---

## Essential Criteria (60 pts)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Roles named by Dataverse system names with record scope** | correctness | essential | Every role in the output is named using its Dataverse system name (e.g., `Basic User`, `System Customizer`). Display names alone = fail. Record scope (Organization / Business Unit / Team / User) must be stated per role per entity. A row without a scope value is an incomplete row, not a pass. No scope distinction at all = fail. |
| C-02 | **FLS analyzed for every sensitive entity** | correctness | essential | Field-Level Security is analyzed for each entity that contains sensitive fields (PII, financial, regulated). Analysis must name the field, state the FLS profile applied (or absence of one), and note the access result per role. Entities present in the permission model but absent from FLS analysis = fail. |
| C-03 | **OWD established per entity with scope distinction** | correctness | essential | Object-level defaults are stated for every entity in scope. OWD must include the access level (None / Read / Read-Write) and the scope (Organization / Business Unit / Owner). Missing OWD for any entity in scope = fail. OWD stated without scope distinction = fail. |
| C-04 | **At least one gap or risk flagged** | correctness | essential | Output identifies at least one privilege escalation path, missing FLS entry, team membership gap, or sharing rule conflict. Generic "review your settings" without specifics = fail. |

---

## Recommended Criteria (30 pts)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Sharing rule conflicts traced with a specific named rule** | depth | recommended | Names the rule, names the role receiving unintended access, and explains why the overreach is unintended. Unnamed rules or abstract references = fail. |
| C-06 | **Team membership gap identified in a non-obvious scenario** | depth | recommended | Names the role, names the team, states whether self-addition is possible and why. Generic team gap without scenario specifics = fail. |
| C-07 | **Privilege escalation path described end-to-end** | depth | recommended | Chain format: `role → action available → elevated access reached`. If no path exists, the null-path is explicitly ruled out by naming the blocking mechanism. Partial mention without full chain = fail. |

---

## Aspirational Criteria (140 pts)

### Added in v1 (original)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Remediation recommended per finding** | behavior | aspirational | Each identified gap or conflict includes a concrete remediation action. Ideal form: `Change [privilege/FLS/sharing rule/OWD] on [role/field/entity] in [solution location] from [current state] to [target state]. After fix: [behavioral delta].` Generic advice = fail. |
| C-09 | **Cross-role interaction analyzed** | depth | aspirational | Output analyzes at least one case where two roles interact (e.g., user holds multiple roles, or one role's sharing exposes records to another). Both roles and the mechanism must be named. Single-role-only analysis = fail. |

### Added in v2–v10 (Rounds 1–10)

*C-10 through C-29 retained verbatim from v10. C-30 through C-32 reproduced below from v10 header.*

### Added in v10 (Round 10)

| ID | Criterion | Category | Weight | Pass Condition | Source signal |
|----|-----------|----------|--------|----------------|---------------|
| C-30 | **Criterion-ID-bearing column headers** | structure | aspirational | Column headers of enforcement tables embed criterion IDs in the form "Field Name (C-NN: rubric phrase)" so a scorer can verify C-28/C-29 by reading the column header without opening the rubric. A table whose headers carry no criterion IDs = fail. A table whose header embeds a criterion ID without the rubric phrase = fail. C-27 operates at instruction-text granularity; C-30 operates at table-column granularity. | V-05 (R10): PROTOCOL REGISTRY column headers — first variation to embed C-28/C-29 IDs in column header text |
| C-31 | **Formal activation-class tokens** | structure | aspirational | Activation class expressed as a formal two-value constant (DEFERRED-PENDING / IMMEDIATELY-ACTIVE) that threads identically through all four sites: REGISTRY column value, ACTIVATED token suffix, per-consumption-site annotation suffix, LOG table column. C-28 requires correct semantics; C-31 requires machine-scannable constants — making C-28 compliance mechanically greppable. Using prose descriptions of activation class at any of the four sites = fail. | V-05 (R10): DEFERRED-PENDING / IMMEDIATELY-ACTIVE constant pair — first variation to express activation class as a formal two-value token |
| C-32 | **Per-activation-site REGISTRY-ID embedding** | structure | aspirational | REGISTRY-ID embedded in the annotation form at each consumption site rather than statically pre-listed at Phase 0 declaration. Each FLS ENTRY block, when instantiated, carries the ID at execution time. A Phase 0 declaration that lists ACTIVE-class protocol instances (violating the unbounded-list problem) rather than embedding the REGISTRY-ID at the consumption-site annotation = fail. An annotation form without an embedded REGISTRY-ID = fail. | V-05 (R10): annotation form carries REGISTRY-ID at each FLS ENTRY site — resolves the gap that held V-01–V-04 to 195/200 |

### Added in v11 (Round 11)

| ID | Criterion | Category | Weight | Pass Condition | Source signal |
|----|-----------|----------|--------|----------------|---------------|
| C-33 | **ANTI-PATTERN REGISTRY CA-1 FIRING AUDIT closure** | structure | aspirational | CA-1 contains a FIRING AUDIT section with one row per AP-identifier declared in Phase 0. Each row carries a FIRED / NOT-FIRED terminal verdict. A NOT-FIRED row names the specific SE section (e.g., "SE-2") that failed to open with its assigned reactive marker token. An AP-identifier present in Phase 0 but absent from the FIRING AUDIT = fail. A FIRED / NOT-FIRED verdict without a named SE section on NOT-FIRED rows = fail. A CA-1 without a FIRING AUDIT section = fail. C-21 requires declaration-side reactive marker tokens; C-33 requires the CA-1 closure that converts AP suppression into a two-endpoint execution record. | V-01 (R11): ANTI-PATTERN REGISTRY with CA-1 FIRING AUDIT — first variation to close every AP-identifier with a FIRED/NOT-FIRED verdict naming the SE section |
| C-34 | **TABLE_5 SOURCE-LINK provenance columns** | structure | aspirational | TABLE_5 schema includes `Source Table`, `Source Row`, and `Discovery Phase` columns. Every TABLE_5 row carries values for all three. Discovery Phase values follow the pattern "PHASE 2 SE-N" where N is the SE section number. CA-1 contains a SOURCE-LINK AUDIT confirming no TABLE_5 row carries a Discovery Phase value outside this pattern. A TABLE_5 without the three provenance columns = fail. A TABLE_5 row with a blank or non-conforming Discovery Phase = fail. A CA-1 without the SOURCE-LINK AUDIT = fail. C-11 makes registration timing a prose commitment; C-34 makes it a mechanically scannable inter-table property. | V-02 (R11): TABLE_5 SOURCE-LINK columns with CA-1 SOURCE-LINK AUDIT — first variation to make C-11 compliance verifiable by column scan rather than prose timing context |
| C-35 | **CRITERION-PHASE-MAP with PHASE-LATE terminal verdict** | structure | aspirational | Phase 0 contains a CRITERION-PHASE-MAP with at least one row per tracked criterion, naming the expected SE phase where that criterion's evidence will first appear. CA-1 carries PHASE-LATE as a third terminal verdict alongside PASS / FAIL. A PHASE-LATE verdict fires whenever criterion evidence first appears in an SE section later than the CRITERION-PHASE-MAP declared for that criterion. A Phase 0 without a CRITERION-PHASE-MAP = fail. A CA-1 that carries only PASS / FAIL (no PHASE-LATE state) = fail. A PHASE-LATE verdict without naming the declared phase and the actual phase = fail. C-20 makes criterion verification binary; C-35 makes phase-ordering of verification commitments auditable. | V-03 (R11): CRITERION-PHASE-MAP at Phase 0 with CA-1 PHASE-LATE terminal state — first variation to make criterion phase discipline auditable without reading SE section bodies |
