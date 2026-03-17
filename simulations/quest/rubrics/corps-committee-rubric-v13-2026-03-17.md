Here is the complete updated rubric:

---

**Three new aspirational criteria added from R12 signals:**

**C-37 — Dual-enforcement pairing for high-frequency essential criteria**
V-04 is the evidence: combining tier gates + tables achieves PASS+ on C-02 and C-04 where either mechanism alone reaches only PASS. The principle: when a property recurs in every simulation (role voice, action item ownership), two independent structural mechanisms make violations detectable from two angles simultaneously — removing one mechanism degrades coverage. Single-mechanism enforcement of these properties is correct but not redundancy-hardened.

**C-38 — FAILS syntax template enforces `[C-NN]` as a required field**
C-14 was PARTIAL across all four variations in R12. The common gap was identical each time: "no explicit `[C-NN]` tag requirement on FAILS rows." The distinction from C-14: C-14 checks whether annotations exist and are correct; C-38 checks whether the fill-rule template makes omission *structurally detectable* — a FAILS entry missing `[C-NN]` is malformed, not merely suboptimal. Tables (V-04) make it natural; C-38 requires the template to make it required.

**C-39 — Co-dependent criteria declared with `REQUIRES:` annotations**
V-03 exposes the C-35/C-36 co-dependency exactly: vocabulary present, count invariant unenforceable, C-36 PARTIAL(weak). The pattern generalizes: when B's pass condition requires A, a skill that implements B without declaring the A prerequisite creates latent false-positive risk. `REQUIRES: C-35` before C-36's fill rules converts a latent trap into a visible pre-check.

**Denominator:** 28 → 31. **Total criteria:** 36 → 39.
forces the field, so a FAILS entry missing `[C-NN]` is detectable as syntactically
   incomplete rather than merely suboptimal. The distinction: C-14 is a presence-and-
   correctness check; C-38 is a syntax-enforcement check. V-04 PARTIAL+ on C-14 provided
   the clearest signal — tables make citation natural but do not mandate it.

3. **Co-dependent criteria declared with `REQUIRES:` annotations (C-39)** — V-03 exposes
   the C-35/C-36 co-dependency exactly as predicted: C-36 vocabulary (CONSUMED / NOT-
   APPLICABLE / DROPPED) is present, but the count invariant is unenforceable without C-35's
   table structure, producing C-36 PARTIAL(weak). The pattern generalizes: when criterion B's
   pass condition is architecturally unenforceable without criterion A being satisfied, a
   skill that implements B's vocabulary without declaring the A prerequisite creates latent
   false-positive risk. The vocabulary appears present; the structural enforceability is
   absent. C-39 requires an explicit `REQUIRES: C-NN` declaration before each dependent
   criterion's fill rules, converting the latent risk into a visible pre-check.

Aspirational denominator: 25 (v10) -> 28 (v12) -> 31 (v13). Total criteria: 39.

---

## Essential Criteria (60% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Committee type is correctly instantiated** | correctness | Output identifies the committee type (ROB / shiproom / arch-board) and applies the correct framing: ROB produces a product/service review verdict; shiproom produces a go/no-go decision; arch-board produces an architecture decision record (ADR). Wrong type or no type = fail. |
| C-02 | **Each participant speaks from their role** | correctness | Every attendee raises concerns consistent with their role charter. A PM should not raise deployment topology concerns as a primary; an SRE should not lead the product vision discussion. Mismatched role voice on any participant = fail. |
| C-03 | **Decisions are explicitly recorded** | correctness | The minutes contain a clearly labeled **Decisions** section with at least one concrete decision stated as an outcome (approved / rejected / deferred / conditional-approval). Vague summaries without a stated outcome = fail. |
| C-04 | **Action items are captured with owners** | correctness | Each action item names both the action and the responsible party. Action items without owners, or minutes with no action items when open questions were raised, = fail. |
| C-05 | **Dissenting opinion is represented when applicable** | coverage | If any participant's role or position creates tension with the majority outcome, a dissenting opinion must appear. If all participants agree, vacuously satisfied. Minutes that smooth over explicit disagreements = fail. |

---

## Recommended Criteria (30% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Meeting minutes follow a recognizable formal structure** | format | Output uses standard structure: header, agenda items, discussion summary, decisions, action items, next steps. Missing more than two structural sections = fail. |
| C-07 | **Discussion depth reflects committee type norms** | depth | ROB includes feature/metric readiness evidence; shiproom includes a risk register or blocking issues; arch-board includes named architectural trade-offs. A generic discussion that could belong to any committee type = fail. |
| C-08 | **AMEND capability honored when invoked** | behavior | Amendments are reflected in the output. No AMEND invoked = vacuously satisfied. |

---

## Aspirational Criteria (10% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Minutes surface a pre-mortem risk the real committee is likely to miss** | depth | At least one participant raises a non-obvious, role-specific, forward-looking concern. Pass+ gate: risk must represent an outside-in perspective -- if a competent internal reviewer would have predicted it, the criterion is not met. |
| C-10 | **Charter fidelity is traceable** | correctness | At least two charter-specific constraints (quorum, scope, veto, escalation) are visibly honored in the minutes. |
| C-11 | **Injection is treated as default, not exception** | behavior | When the prompt requires injecting a role not in the standing participant list, the output treats injection as the baseline assumption. Claiming the participant is present without evidence that a charter role covers the function is an incorrect affirmation. The model must actively prove a qualifying participant exists. Minutes that assert coverage without basis = fail. Not invoked = vacuously satisfied. |
| C-12 | **Provisional participant annotation appears in Phase 0 when injection is pending** | format | When a participant role is subject to injection or bridge confirmation, the Phase 0 attendee list includes a forward-reference annotation (e.g., `[Note: role is a candidate participant -- confirmed or replaced in Phase 2]`). Not applicable if no injection is pending = vacuously satisfied. |
| C-13 | **Pre-skeleton imperative block commits type-specific obligations before filling begins** | behavior | The skill includes a pre-skeleton block (e.g., "BEFORE YOU START") that states each committee type's primary obligation in direct imperative voice, with at least one explicit natural-language fail condition per type that would catch the most common output defect for that type (e.g., "If there is no metric, you have not done a ROB"). The block must appear before any skeleton filling begins -- not as a fill rule inside the skeleton. A skill that only enforces type discipline through fill-rule validation or gate syntax does not satisfy this criterion. |
| C-14 | **Fill-rule failures are annotated with the criterion ID they would fail** | format | At least three fill-rule FAILS entries reference the rubric criterion ID (C-01 through C-39) that the failure would score as a miss (e.g., "FAILS: section present but no evidence -- C-07 partial"). This creates a self-scoring audit trail that makes gap-to-criterion mapping explicit and auditable. Criterion IDs must be correct -- an annotation that cites the wrong criterion is a false positive and counts against the criterion. |
| C-15 | **Phase-gate architecture surfaces charter constraints as entry preconditions, not post-hoc checks** | behavior | When the skill uses a lifecycle phase structure (Phase 0/1/2 or equivalent), charter constraints must appear as phase entry or exit conditions -- quorum and scope declared in Phase 0 before simulation begins, escalation path committed as a Phase 2 exit option. The test: can Phase 1 simulation begin without the charter constraints having been stated? If yes, the criterion is not met. A phase structure that defers charter validation to prose fill rules, or that embeds charter constraints only inside simulation output rather than as gate preconditions, does not satisfy this criterion. Not applicable if the skill uses no phase structure = vacuously satisfied. |
| C-34 | **Re-COMMIT cycle after AMEND** | behavior | C-30 routes AMEND through the block dependency graph; C-33 marks stale output sites. Re-execution blocks must also emit a versioned RECOMMIT MANIFEST before downstream phases resume. Phase re-entry must gate on manifest currency, not on original v1 seals. AMEND not invoked = vacuously satisfied. A skill where PHASE-N-ENTER can pass on a v1 seal after AMEND has been issued does not satisfy this criterion. |
| C-35 | **COMMIT seal token manifest** | behavior | The COMMIT annotation closing each block must enumerate which tokens are sealed as an explicit closed set. Without an explicit closed set, TOKEN TRACE CONFIRMATION (C-32) can verify tokens it finds but cannot detect tokens dropped without trace. The closed set must be structured such that a dropped token produces a visible absence (empty cell or missing row) rather than a silent omission in prose. A seal annotation that enumerates tokens only in prose narrative does not satisfy this criterion. |
| C-36 | **Three-way CONFIRMATION status** | behavior | Each sealed token in the C-35 manifest receives a completion status -- CONSUMED, NOT-APPLICABLE, or DROPPED -- and the confirmation table row count must equal the manifest token count. Without a C-35 table manifest, the vocabulary may be present but the count invariant is unenforceable: a token never assigned a row cannot be detected as DROPPED. REQUIRES: C-35. A skill that implements CONSUMED/NOT-APPLICABLE/DROPPED vocabulary without C-35's closed-set manifest satisfies this criterion only weakly (PARTIAL) -- count reconciliation is unenforceable regardless of vocabulary presence. |
| C-37 | **Dual-enforcement pairing for high-frequency essential criteria** | behavior | Critical essential criteria that recur in every committee meeting -- specifically role voice discipline (C-02) and action item ownership (C-04) -- must each be backed by at least two independent structural enforcement mechanisms (e.g., tier sequence gate + table row structure, or phase entry check + fill-rule cell validation). Single-mechanism enforcement of C-02 and C-04 achieves correctness but not structural redundancy. Pass condition: at least two of the five essential criteria are enforced by two or more independent structural mechanisms such that a violation produces a detectable signal from both mechanisms independently. A skill where role voice or ownership discipline is enforceable by removing one mechanism without degrading coverage does not satisfy this criterion. |
| C-38 | **FAILS syntax template enforces `[C-NN]` as a required field** | format | The fill-rule section defines a canonical FAILS template where `[C-NN]` is a positional required field, not a convention. The canonical form must be stated explicitly (e.g., `FAILS [C-NN]: <description>`), and the template must specify that a FAILS entry without `[C-NN]` is syntactically malformed -- not merely suboptimal. Pass condition: the template is stated, the canonical form includes `[C-NN]` as required, and at least one example entry demonstrates the correct form. Note: C-14 requires annotations to exist and be accurate; C-38 requires the template to make omission structurally detectable. A skill where `[C-NN]` is encouraged or made natural by table structure (e.g., V-04) but not required by template definition does not satisfy this criterion. |
| C-39 | **Co-dependent criteria declared with `REQUIRES:` annotations** | format | When a criterion's pass condition is architecturally unenforceable without a prerequisite criterion also being satisfied -- specifically when C-36's count invariant requires C-35's table manifest, or any analogous dependency -- the skill preamble or fill-rule section must include an explicit `REQUIRES: C-NN` declaration immediately before the dependent criterion's fill rules. Pass condition: each co-dependent criterion pair has a declared `REQUIRES:` annotation. A skill that implements dependent vocabulary without declaring the prerequisite creates latent false-positive risk: vocabulary presence masks structural unenforceability and the reviewer cannot detect the gap without knowing the dependency in advance. Not applicable if no co-dependent criterion pairs exist in the skill's scope = vacuously satisfied. |
