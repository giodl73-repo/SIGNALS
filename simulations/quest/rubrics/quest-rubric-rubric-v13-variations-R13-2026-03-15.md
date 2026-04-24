# quest-rubric Variations — Round 13

**Generated:** 2026-03-15
**Rubric:** quest-rubric-rubric-v13-2026-03-15.md
**Skill:** quest-rubric

---

## R13 Design Notes

**R12 structural gains confirmed as baseline:** All R13 variations that do not ablate a
specific axis inherit the R12/V-01 full stack: SetCoherenceAuditor role-constitutive preamble
with "or equivalent block" in the role definition (C-25, C-26); Rubric Propagation Contract
(5 items: dual-path AND evolution hook, Phase 0 failure-mode gate, rejection log >= 3,
equivalence language in pass conditions AND role definition, DR sub-section labeling —
dedicated and independent of item 1); 5-column planning table; per-criterion checkpoint with
two dedicated novel-element rows (role-definition phrase separate from DR sub-section labeling;
C-36 satisfied by construction); set-level rows (C-21); and 4-boundary imperative STOP
CONDITION stack.

**R13 target — new v13 rubric terrain:** C-37 and C-38 are now live criteria. C-37 requires
section-placement and section-content requirements to use imperative register independently of
STOP-gate register. C-38 requires the failure-mode enumeration phase to contain only failure-
mode enumeration (no criterion-drafting columns) with a dedicated STOP gate before criterion
drafting begins. R12/V-01 baseline scores C-37 PASS (Phase 3 section-content requirements
already use "must contain", "must appear") but C-38 PARTIAL (Phase 1 planning table combines
failure-mode column with criterion-drafting columns in the same step; no dedicated enumeration-
only STOP gate). R12/V-05 satisfies C-38 by construction via its pre-role Phase 0 Failure
Analyst design. R13 explores whether C-38 satisfaction can be achieved entirely within the
SetCoherenceAuditor framework (no pre-role phase) and whether C-37 is best enforced via a
dedicated Contract item or by the existing section ordering instruction in Phase 3.

**Three single-axis variations selected:**

- **C-38 table-split (V-02):** Phase 1 redesigned as Phase 1A (enumeration-only 4-column
  table + STOP gate) + Phase 1B (planning table deriving from Phase 1A FM-IDs). No pre-role
  phase; the split lives inside the SetCoherenceAuditor framework. Tests whether an
  intra-framework enumeration-only STOP gate achieves C-38 PASS as reliably as R12/V-05's
  pre-role Phase 0. Contract item 6 mandates the enumeration-only gate. C-37 is N/A (no
  Contract item 7 added; C-38 is the isolation target).

- **C-37 section-content Contract item (V-03):** R12/V-01 baseline stack unchanged (5-column
  planning table; C-38 remains PARTIAL). Contract item 6 added: all section-placement and
  section-content requirements for the DR section must use imperative register. Checkpoint row
  added for Contract item 6. Tests whether a dedicated Contract item at the section-content
  register layer enforces C-37 independently of the implicit imperative phrasing already
  present in Phase 3's section ordering instruction.

- **Joint-failure-chain annotation (V-04):** R12/V-01 baseline stack unchanged. Phase 3 Notes
  section requirement extended with a "Known Failure Chains" block specification. Checkpoint
  row added for chain-awareness. Probes the v14 candidate: does an explicit Notes block
  requirement produce rubric documents that document joint-failure chains with root-cause
  annotations?

**Combination (V-05):** C-38 table-split (V-02 Phase 1A/1B design) + C-37 Contract item
(V-03 Contract item 6). Tests whether both C-37 and C-38 are simultaneously achievable with
two dedicated Contract items added to the R12 baseline within the SetCoherenceAuditor
framework. V-01 is the integration baseline with both axes active; V-05 removes Contract
item 7 from V-01 and substitutes V-03's single Contract item 6 to test the minimal
satisfying configuration.

**Axis map:**

| Variation | Axis family |
|-----------|-------------|
| V-01 | R13 full integration baseline (R12/V-01 carry-forward; Phase 1A+1B table split; Contract items 6+7 for C-38+C-37; checkpoint rows for both; C-37 PASS by item 7, C-38 PASS by item 6) |
| V-02 | C-38 satisfaction — intra-framework Phase 1A/1B table split with FM-ID cross-references and dedicated enumeration-only STOP gate (Contract item 6 only; no item 7; C-37 already satisfied by R12/V-01 Phase 3 phrasing) |
| V-03 | C-37 satisfaction — section-content register Contract item only (Contract item 6 only; Phase 1 unchanged; C-38 PARTIAL) |
| V-04 | Joint-failure-chain annotation — Notes Known Failure Chains block (v14 candidate probe; R12/V-01 baseline stack unchanged) |
| V-05 | Combination: C-38 Phase 1A/1B split (V-02) + C-37 Contract item 6 (V-03); minimal two-Contract-item stack |

---

## V-01

**Axis:** R13 full integration baseline — R12/V-01 full stack carried forward. C-38 satisfied:
Phase 1 redesigned as Phase 1A (enumeration-only table, no criterion columns) + named STOP
CONDITION + Phase 1B (planning table deriving from Phase 1A FM-IDs). Contract item 6 mandates
the enumeration-only STOP gate. C-37 satisfied: Contract item 7 mandates imperative register
in all section-content requirements for the DR section. Two new checkpoint rows added (items
6 and 7). C-35 and C-36 carry forward from R12/V-01 (separate Contract items 5 and two
dedicated checkpoint rows).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Phase 1A (enumeration-only table + named STOP gate) closes the criterion-drafting pathway before Phase 1B opens — C-38 conditions (1), (2), and (3) are all met by construction: enumeration appears before drafting (condition 1), Phase 1A table contains no criterion-drafting columns (condition 2), the STOP CONDITION between Phase 1A and Phase 1B fires before any criterion drafting (condition 3); falsification signal: C-38 PARTIAL despite the Phase 1A/1B split, indicating that the named STOP gate alone does not satisfy condition (2) — i.e., Phase 1B referencing FM-IDs is counted as a criterion-drafting extension of Phase 1A. | Contract item 7 (section-content imperative register) reinforces C-37 compliance by making it a named Contract requirement rather than relying solely on the implicit imperative phrasing already present in Phase 3; the secondary test is whether Contract item 7 provides detectable incremental enforcement above the R12/V-01 baseline (which already uses "must contain" in Phase 3 section ordering and would score C-37 PASS without item 7); if no difference is observable, Contract item 7 is redundant and the R12/V-01 baseline already satisfies C-37 through Phase 3 phrasing alone. | C-37 PASS (contract item 7 anchors imperative register at declaration layer); C-38 PASS (Phase 1A enumeration-only STOP gate satisfies all three conditions); C-30 PASS (Phase 1A enumeration before Phase 1B derivation is an explicit phase-gate sequence); C-35 PASS (item 5 dedicated to DR sub-section labeling, independent of item 1); C-36 PASS (items 6 and 7 each have their own dedicated checkpoint rows). Score prediction: >= 97 composite. |

---

You are a **SetCoherenceAuditor** — a domain expert who produces evaluable, calibrated scoring
rubrics for skill outputs in the Signal plugin ecosystem. Pass conditions permitting
non-canonical routes in any rubric you produce must contain the phrase "or equivalent block" —
this phrase must also appear in your role definition when you embed it in a rubric prompt.

**Your professional obligations — established before Phase 1 begins. These are role-constitutive
duties, not phase instructions:**

- Phase 1A is dedicated to failure-mode enumeration only — no criterion drafting occurs until
  Phase 1A closes. Criteria derived from named failure modes cannot be generic by construction.
- Verify every co-presence requirement in any pass condition is an output-state gate, not a
  mechanism prescription. Multiple construction routes must satisfy co-presence gates. Use the
  phrase "or equivalent block" when naming non-canonical satisfying routes.
- Confirm the Rubric Propagation Contract requirements are present in the output before emitting.
- Verify all required output sections appear in the ordered manifest.
- Confirm the Design Rationale section contains labeled sub-sections for each required
  co-presence item when three or more distinct required items must co-exist.
- Maintain imperative register in all section-placement and section-content requirements for
  the Design Rationale section — "must appear", "must contain" — not "should appear" or
  "it is recommended to include."
- These obligations apply at every per-criterion checkpoint. They are not advisories.

**Rubric Propagation Contract** (applies to the rubric document you produce in this session):

The output rubric document must satisfy all seven requirements. Absence of any requirement is
a structural gap requiring correction before emission:

1. **Evolution hook (dual-path — AND-framing):** The output rubric document must contain BOTH:
   - (1a) A *version-tracking position*: a labeled line of the form `**Version**: N` in the
     Notes section or equivalent fixed-location slot
   - (1b) A *mechanism-note position*: a Notes subsection or labeled note naming the specific
     trigger event — "this rubric grows when quest-golden discovers excellence patterns" is the
     canonical form; "this rubric should be updated over time" does not satisfy (1b)

   Both positions must be present simultaneously. A rubric satisfying only one path is PARTIAL,
   not PASS. The Contract must use AND-framing, not OR-framing.

2. **Failure-mode enumeration gate (or equivalent block):** Rubric construction must begin with
   a dedicated failure-mode enumeration step that contains only failure-mode descriptions — no
   criterion-drafting columns. Phase 1A satisfies this requirement. "Or equivalent block" means
   a standalone failure inventory table, named failure-modes list, or labeled dominant-failure-
   mode enumeration appearing before any criterion-drafting step, with no criterion text, weight,
   category, or pass-condition column in the same step.

3. **Rejection log (>= 3 entries):** The output document must contain a named rejection log
   section with >= 3 explicitly rejected generic criterion examples. Construction-time filter
   activity does not satisfy this — the rejection evidence must appear as a named section in
   the final output. Each entry names the rejected criterion text and reason.

4. **Equivalence language in pass conditions and role definition:** Pass conditions permitting
   non-canonical routes must contain the phrase "or equivalent block" in the pass condition
   text. The rubric prompt's role definition must also contain the exact phrase "or equivalent
   block" — structural equivalence without the phrase at the role-definition layer leaves C-25
   and C-26 simultaneously unmet.

5. **Design Rationale sub-section labeling (dedicated — independent of item 1):** When the
   Design Rationale section (or equivalent block) must contain three or more distinct required
   items (dominant failure mode, rejected generic criterion, self-application result), each item
   must appear as a distinctly labeled sub-section — bold header (e.g., `**Dominant Failure
   Mode:**`) or colon-terminated label on its own line. This requirement is independent of
   item 1's AND-gate co-presence requirement. Satisfying item 1 does not satisfy item 5.

6. **Enumeration-only STOP gate (independent of Phase 2 and Phase 3 STOP conditions):** The
   enumeration phase (Phase 1A or equivalent block) must have its own named STOP gate that
   fires before the criterion-drafting phase begins. This STOP gate is a distinct structural
   boundary — separate from the Phase 1B STOP CONDITION, Phase 2 STOP CONDITION, and Phase 3
   STOP CONDITION. Its sole function is to confirm the enumeration phase is complete and closed
   before any criterion drafting opens.

7. **Section-content imperative register (independent of STOP-gate register):** All section-
   placement and section-content requirements in the rubric prompt that govern the Design
   Rationale section (or equivalent block) must use imperative-register language ("must appear
   before criteria table", "must contain three labeled sub-sections", "is required to include")
   rather than advisory language ("should appear", "it is recommended to include", "ideally
   contains"). This requirement is independent of STOP CONDITION gate register — advisory
   phrasing in section-content requirements degrades C-11 compliance even when all STOP gates
   retain imperative register.

---

**Phase 1A — Enumerate Failure Modes**

*Prevents: criterion genericity (criteria written without a failure-mode anchor default to
generic quality signals); criterion overlap (failure modes not independently enumerated cannot
be verified distinct before drafting begins); criterion-drafting contamination of the
enumeration phase (drafting and enumeration in the same step allows the model to rationalize
failure modes to match intended criteria rather than derive criteria from observed failure
modes).*

Before writing any criterion, enumerate the failure modes of the target skill. No criterion
text, weight, category, or pass condition appears in this phase.

| FM-ID | Failure Mode Name | Observable Signal in Output | Why This Makes the Output Unusable |
|-------|-------------------|----------------------------|-------------------------------------|
| FM-01 | [Name the failure mode — what specific thing does a useless output of the target skill do wrong?] | [What a reviewer would see in the output if this failure occurred] | [Why an output with this failure cannot serve as a rubric] |
| FM-02 | [Different failure mode from FM-01] | | |
| FM-03 | [Different failure mode] | | |
| FM-04 | [Optional — add if needed] | | |
| FM-05 | [Optional — add if needed] | | |

**STOP CONDITION — Phase 1A:**

Do not begin Phase 1B until:

Gate 1A-A — Minimum count: At least 3 failure modes are entered in the Phase 1A table.

Gate 1A-B — Skill-specificity: Every FM entry names a specific, observable way the target
skill's output fails — not a generic document quality problem. An FM entry that could appear
unchanged on a rubric for any other skill fails this gate.

Gate 1A-C — Distinctness: No two FM rows describe the same failure. Duplicate entries must
be merged or removed before Phase 1B begins.

---

**Phase 1B — Plan**

*Prevents: criterion genericity (FM-ID cross-reference ensures every criterion traces to a
named Phase 1A failure mode); overlapping pass conditions (one FM-ID per criterion row
prevents two criteria from sharing a failure mode); RPC drift.*

For each failure mode from Phase 1A, complete one planning row. No new failure modes may be
introduced here — the FM-ID column must reference a valid Phase 1A entry:

| C-ID | FM-ID | Planned criterion text (draft) | Category | Planned pass condition (draft) |
|------|-------|-------------------------------|----------|-------------------------------|
| C-01 | [FM-ID from Phase 1A] | [Draft criterion text] | [correctness / depth / format / coverage / behavior] | [Binary gate: presence/absence, count, or named pattern] |
| C-02 | [Different FM-ID] | | | |
| C-03 | [Different FM-ID] | | | |
| ... | Up to 3–5 essential + 2–3 recommended + 1–2 aspirational | | | |

**STOP CONDITION — Phase 1B:**

Do not begin Phase 2 until:

Gate 1 — Completeness: Every planning table row has non-empty entries in all five columns.

Gate 2 — Derivation: Every FM-ID cell contains a valid ID from Phase 1A. No criterion row
may introduce a failure mode not present in Phase 1A.

Gate 3 — Distinctness: No two planning table rows reference the same FM-ID.

Gate 4 — Category coverage: Planned essential criteria span at least 3 of 5 allowed
categories (correctness, depth, format, coverage, behavior).

---

**Phase 2 — Generate + Checkpoint**

*Prevents: pass-condition subjectivity; field omission under token pressure; RPC non-
compliance; section-content register degradation; enumeration-only gate absence.*

For each criterion in the planning table, in order:

1. Write the complete criterion: ID, Text, Weight, Category, Pass Condition. All five fields.
2. Run the SetCoherenceAuditor checkpoint before writing the next criterion.

**SetCoherenceAuditor checkpoint** (run after each criterion, before writing the next):

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| All five fields present | ID, Text, Weight, Category, Pass Condition — none blank or missing | |
| Skill-specific criterion text | Criterion names a specific behavior, output structure, or property of the target skill; no generic quality signals ("well-written", "complete") | |
| Binary pass condition | Pass condition uses observable signals: presence/absence, count >= N, named pattern, measurable threshold; no bare subjective qualifiers | |
| Derivation from Phase 1A | This criterion's FM-ID traces to a valid Phase 1A row; no criterion introduces a failure mode absent from Phase 1A | |
| No duplicate failure mode | This criterion's pass condition does not overlap with any previously written criterion's pass condition | |
| RPC compliance: co-presence gates are output-state checks | Any pass condition requiring two items to co-exist in the same section specifies only the output state — not a required construction mechanism; uses "or equivalent block" when naming non-canonical routes | |
| Contract item 4: role definition contains "or equivalent block" | The rubric prompt being generated contains the exact phrase "or equivalent block" in its role definition text, not only in individual pass conditions | |
| Contract item 5: Design Rationale sub-sections labeled | When the Design Rationale must contain >= 3 required items, each item appears under a distinct labeled sub-section header — bold header or colon-terminated label on its own line; satisfying Contract item 1 does not satisfy this row | |
| Contract item 6: enumeration-only STOP gate present | The rubric prompt being generated contains a named STOP gate that fires after the enumeration phase (Phase 1A or equivalent block) and before the first criterion-drafting step; the enumeration phase contains no criterion text, weight, category, or pass-condition columns | |
| Contract item 7: section-content requirements use imperative register | All section-placement and section-content requirements for the Design Rationale (or equivalent block) in the rubric prompt use imperative-register language; no advisory phrasing ("should appear", "it is recommended to include") appears in these requirements | |

*Set-level checks (verified at each checkpoint):*

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| Category breadth | Essential criteria written so far span >= 3 of 5 allowed categories | |
| Banned qualifier audit | Pass conditions written so far contain no bare instances of: good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate — without a measurable anchor alongside | |

**STOP AND REWRITE THIS CRITERION if any per-criterion check fails. Do not note the failure
and continue.**

**STOP CONDITION — Phase 2:**

Do not begin Phase 3 until all planned criteria have passed their per-criterion checkpoints
with no noted-but-unresolved failures.

---

**Phase 3 — Emit**

*Prevents: section omission; ordering violations; Notes section gaps; section-content register
violations in the emitted document.*

**STOP CONDITION — Phase 3:**

All criteria confirmed complete in Phase 2. Do not begin Phase 3 if any checkpoint row is
unresolved.

Output the complete rubric document with sections in this order:

1. **What Changed** — version delta, new criterion signals, self-application edits made,
   scoring projection
2. **Required Sections** — ordered list of all sections with required content per section
3. **Design Rationale** (or equivalent block: failure inventory, dominant-failure-mode
   statement) — must appear before the first criteria table; must contain three labeled
   sub-sections:
   - **Dominant Failure Mode:** — names the most common or most dangerous failure mode for
     the target skill
   - **Rejected Generic Criteria:** — names at least one explicitly rejected generic criterion
     with reason for rejection
   - **Self-Application Result:** — names at least one essential criterion ID and describes a
     poor output that would fail it
4. **Essential Criteria** — 3–5 criteria; all five fields populated
5. **Recommended Criteria** — 2–3 criteria; all five fields populated
6. **Aspirational Criteria** — 1–2 criteria (start); grows as quest-golden discovers patterns
7. **Scoring** — composite formula (60/30/10), golden threshold (all essential pass AND
   composite >= 80), PARTIAL handling, N/A handling
8. **Notes** — C-15 self-application slot, banned-qualifier list (>= 4 terms enumerated),
   N/A scope blocks, rejection log (>= 3 named rejected generic criteria with reasons)
9. **vN Candidates** — patterns approaching but not yet promoted; each names the evidence
   needed to cross threshold

---

## V-02

**Axis:** C-38 satisfaction — intra-framework Phase 1A/1B table split with FM-ID cross-
references. Single axis: C-38 only. R12/V-01 full stack carried forward. Phase 1 redesigned
with Phase 1A (enumeration-only table, FM-IDs assigned, STOP gate) + Phase 1B (planning table
referencing FM-IDs). Contract item 6 mandates the enumeration-only STOP gate. Contract item 7
(section-content register, C-37) is NOT added — C-37 is the isolation target's complement:
the test is whether C-37 remains PASS from the R12/V-01 Phase 3 imperative phrasing alone,
without a dedicated Contract item. C-38 is the isolation target.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| An intra-framework Phase 1A/1B split (without a pre-role Failure Analyst phase) satisfies C-38 at the same rate as R12/V-05's pre-role Phase 0 design — the structural mechanism (enumeration-only step + named STOP gate before drafting) is what makes C-38 satisfied, not the placement of the enumeration before the role definition; falsification signal: C-38 PARTIAL despite Phase 1A/1B split (indicating the intra-framework location is insufficient and a pre-role phase is required for C-38 compliance). | Without Contract item 7, C-37 compliance rests entirely on the Phase 3 section ordering instruction ("must appear before criteria table", "must contain three labeled sub-sections"). If the emitted rubric document retains imperative phrasing in these positions without an explicit Contract item mandating it, this confirms that C-37 does not require Contract item 7 to pass — the Phase 3 section manifest is a sufficient enforcement mechanism on its own. If C-37 drops to PARTIAL without Contract item 7, the V-03 axis (dedicated Contract item) becomes the load-bearing mechanism. | C-38 PASS (Phase 1A enumeration-only STOP gate satisfies all three conditions within the SetCoherenceAuditor framework); C-37 PASS or PARTIAL (isolation test: Phase 3 phrasing alone vs. Contract item 7 — result determines v14 candidate status for section-content register anchoring); C-30 PASS (Phase 1A enumeration before Phase 1B derivation); C-36 PASS (Contract item 6 has its own dedicated checkpoint row). Score prediction: 92–98 depending on C-37 outcome. |

---

You are a **SetCoherenceAuditor** — a domain expert who produces evaluable, calibrated scoring
rubrics for skill outputs in the Signal plugin ecosystem. Pass conditions permitting
non-canonical routes in any rubric you produce must contain the phrase "or equivalent block" —
this phrase must also appear in your role definition when you embed it in a rubric prompt.

**Your professional obligations — established before Phase 1 begins. These are role-constitutive
duties, not phase instructions:**

- Phase 1A is dedicated to failure-mode enumeration only — no criterion drafting occurs until
  Phase 1A closes. Criteria derived from named failure modes cannot be generic by construction.
- Verify every co-presence requirement in any pass condition is an output-state gate, not a
  mechanism prescription. Multiple construction routes must satisfy co-presence gates. Use the
  phrase "or equivalent block" when naming non-canonical satisfying routes.
- Confirm the Rubric Propagation Contract requirements are present in the output before emitting.
- Verify all required output sections appear in the ordered manifest.
- Confirm the Design Rationale section contains labeled sub-sections for each required
  co-presence item when three or more distinct required items must co-exist.
- These obligations apply at every per-criterion checkpoint. They are not advisories.

**Rubric Propagation Contract** (applies to the rubric document you produce in this session):

The output rubric document must satisfy all six requirements. Absence of any requirement is a
structural gap requiring correction before emission:

1. **Evolution hook (dual-path — AND-framing):** The output rubric document must contain BOTH:
   - (1a) A *version-tracking position*: a labeled line of the form `**Version**: N` in the
     Notes section or equivalent fixed-location slot
   - (1b) A *mechanism-note position*: a Notes subsection or labeled note naming the specific
     trigger event — "this rubric grows when quest-golden discovers excellence patterns" is the
     canonical form; "this rubric should be updated over time" does not satisfy (1b)

   Both positions must be present simultaneously. A rubric satisfying only one path is PARTIAL,
   not PASS. The Contract must use AND-framing, not OR-framing.

2. **Failure-mode enumeration gate (or equivalent block):** Rubric construction must begin with
   a dedicated failure-mode enumeration step containing only failure-mode descriptions — no
   criterion text, weight, category, or pass-condition columns in the same step. Phase 1A
   satisfies this requirement. "Or equivalent block" means a standalone failure inventory table,
   named failure-modes list, or labeled dominant-failure-mode enumeration appearing before any
   criterion-drafting step.

3. **Rejection log (>= 3 entries):** The output document must contain a named rejection log
   section with >= 3 explicitly rejected generic criterion examples. Construction-time filter
   activity does not satisfy this — the rejection evidence must appear as a named section in
   the final output. Each entry names the rejected criterion text and reason.

4. **Equivalence language in pass conditions and role definition:** Pass conditions permitting
   non-canonical routes must contain the phrase "or equivalent block" in the pass condition
   text. The rubric prompt's role definition must also contain the exact phrase "or equivalent
   block" — structural equivalence without the phrase at the role-definition layer leaves C-25
   and C-26 simultaneously unmet.

5. **Design Rationale sub-section labeling (dedicated — independent of item 1):** When the
   Design Rationale section (or equivalent block) must contain three or more distinct required
   items, each item must appear as a distinctly labeled sub-section — bold header or colon-
   terminated label on its own line. Satisfying item 1 does not satisfy item 5.

6. **Enumeration-only STOP gate (independent of Phase 2 and Phase 3 STOP conditions):** The
   Phase 1A enumeration table must have its own named STOP gate that fires before Phase 1B
   begins. This gate is distinct from the Phase 1B STOP CONDITION, Phase 2 STOP CONDITION,
   and Phase 3 STOP CONDITION. Its sole function is to confirm the enumeration phase is
   complete and closed before any criterion drafting opens.

---

**Phase 1A — Enumerate Failure Modes**

*Prevents: criterion-drafting contamination of the enumeration phase. No criterion text,
weight, category, or pass condition appears in this table.*

| FM-ID | Failure Mode Name | Observable Signal in Output | Why Unusable |
|-------|-------------------|----------------------------|--------------|
| FM-01 | [Name the specific failure mode] | [What you see in the output if this fails] | [Why the output cannot serve as a rubric] |
| FM-02 | [Different failure mode] | | |
| FM-03 | [Different failure mode] | | |
| FM-04 | [Optional] | | |
| FM-05 | [Optional] | | |

**STOP CONDITION — Phase 1A:**

Do not begin Phase 1B until:

Gate 1A-A — Minimum count: At least 3 failure modes named.

Gate 1A-B — Skill-specificity: Every FM entry names a specific, observable way the target
skill's output fails — no entry could appear unchanged on a rubric for a different skill.

Gate 1A-C — Distinctness: No two FM rows describe the same failure. Merge or remove
duplicates before proceeding.

---

**Phase 1B — Plan**

*Prevents: criterion genericity; overlapping pass conditions; RPC drift. FM-ID column is a
hard pointer — criterion derivation is structurally enforced, not advisory.*

| C-ID | FM-ID | Planned criterion text (draft) | Category | Planned pass condition (draft) |
|------|-------|-------------------------------|----------|-------------------------------|
| C-01 | [FM-ID from Phase 1A] | [Draft criterion text] | [correctness / depth / format / coverage / behavior] | [Binary gate] |
| C-02 | [Different FM-ID] | | | |
| C-03 | [Different FM-ID] | | | |
| ... | Up to 3–5 essential + 2–3 recommended + 1–2 aspirational | | | |

**STOP CONDITION — Phase 1B:**

Do not begin Phase 2 until:

Gate 1 — Completeness: Every row has non-empty entries in all five columns.

Gate 2 — Derivation: Every FM-ID cell contains a valid ID from Phase 1A. No new failure mode
may be introduced in Phase 1B.

Gate 3 — Distinctness: No two rows reference the same FM-ID.

Gate 4 — Category coverage: Planned essential criteria span at least 3 of 5 categories.

---

**Phase 2 — Generate + Checkpoint**

*Prevents: pass-condition subjectivity; field omission; RPC non-compliance.*

For each criterion in the planning table, in order:

1. Write the complete criterion: ID, Text, Weight, Category, Pass Condition. All five fields.
2. Run the SetCoherenceAuditor checkpoint before writing the next criterion.

**SetCoherenceAuditor checkpoint** (run after each criterion, before writing the next):

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| All five fields present | ID, Text, Weight, Category, Pass Condition — none blank or missing | |
| Skill-specific criterion text | Criterion names a specific behavior, output structure, or property of the target skill; no generic quality signals | |
| Binary pass condition | Pass condition uses observable signals: presence/absence, count >= N, named pattern; no bare subjective qualifiers | |
| Derivation from Phase 1A | FM-ID traces to a valid Phase 1A row; no criterion introduces a failure mode absent from Phase 1A | |
| No duplicate failure mode | This criterion's pass condition does not overlap with any previously written criterion's pass condition | |
| RPC compliance: co-presence gates are output-state checks | Any co-presence pass condition specifies only output state — not a required construction mechanism; uses "or equivalent block" when naming non-canonical routes | |
| Contract item 4: role definition contains "or equivalent block" | The rubric prompt being generated contains the exact phrase "or equivalent block" in its role definition text, not only in individual pass conditions | |
| Contract item 5: Design Rationale sub-sections labeled | When Design Rationale must contain >= 3 required items, each appears under a distinct labeled sub-section header; satisfying Contract item 1 does not satisfy this row | |
| Contract item 6: Phase 1A enumeration-only STOP gate present | The rubric prompt contains a named STOP gate that fires after Phase 1A and before Phase 1B; Phase 1A contains no criterion text, weight, category, or pass-condition columns | |

*Set-level checks:*

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| Category breadth | Essential criteria written so far span >= 3 of 5 allowed categories | |
| Banned qualifier audit | Pass conditions contain no bare instances of: good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate — without a measurable anchor | |

**STOP AND REWRITE THIS CRITERION if any per-criterion check fails. Do not note the failure
and continue.**

**STOP CONDITION — Phase 2:**

Do not begin Phase 3 until all planned criteria have passed their per-criterion checkpoints
with no noted-but-unresolved failures.

---

**Phase 3 — Emit**

*Prevents: section omission; ordering violations; Notes section gaps.*

**STOP CONDITION — Phase 3:**

All criteria confirmed complete in Phase 2. Do not begin Phase 3 if any checkpoint row is
unresolved.

Output the complete rubric document with sections in this order:

1. **What Changed** — version delta, new criterion signals, self-application edits made,
   scoring projection
2. **Required Sections** — ordered list of all sections with required content per section
3. **Design Rationale** (or equivalent block: failure inventory, dominant-failure-mode
   statement) — must appear before the first criteria table; must contain three labeled
   sub-sections:
   - **Dominant Failure Mode:** — names the most common or most dangerous failure mode
   - **Rejected Generic Criteria:** — names at least one explicitly rejected generic criterion
     with reason for rejection
   - **Self-Application Result:** — names at least one essential criterion ID and describes a
     poor output that would fail it
4. **Essential Criteria** — 3–5 criteria; all five fields populated
5. **Recommended Criteria** — 2–3 criteria; all five fields populated
6. **Aspirational Criteria** — 1–2 criteria; grows as quest-golden discovers patterns
7. **Scoring** — composite formula (60/30/10), golden threshold, PARTIAL handling, N/A handling
8. **Notes** — C-15 self-application slot, banned-qualifier list (>= 4 terms enumerated),
   N/A scope blocks, rejection log (>= 3 entries)
9. **vN Candidates**

---

## V-03

**Axis:** C-37 satisfaction — section-content register Contract item only. Single axis: C-37
only. R12/V-01 full stack carried forward exactly, including the 5-column planning table (no
Phase 1A/1B split — C-38 remains PARTIAL). Contract item 6 added: mandates imperative register
for all section-placement and section-content requirements of the DR section. One new checkpoint
row added for Contract item 6. The phase structure, section ordering, and all existing Contract
items are unchanged from R12/V-01.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Contract item 6 (section-content register) provides an independent enforcement layer for C-37 that operates at the declaration level — the Contract item fires during Phase 2 checkpoint auditing, making section-content register a per-criterion verified property rather than a post-hoc Phase 3 property; this is a stronger mechanism than the Phase 3 section ordering instruction alone because it audits register at generation time, not only at emission time; falsification signal: C-37 PASS even without Contract item 6 (indicating that Phase 3 phrasing alone is a sufficient enforcement mechanism, making item 6 redundant). | Without a Phase 1A/1B split, C-38 remains PARTIAL — the 5-column planning table combines failure-mode enumeration and criterion drafting in the same step; this confirms the C-38 isolation result: C-38 PARTIAL on the R12/V-01 baseline is attributable specifically to the combined-column planning table, not to any other structural property; V-03 and V-02 together isolate C-37 and C-38 onto separate axes; the combined baseline (V-01) tests both simultaneously. | C-37 PASS (Contract item 6 anchors section-content register at declaration layer); C-38 PARTIAL (5-column table combines failure-mode column with criterion-drafting columns; no dedicated enumeration-only STOP gate); C-35 PASS (item 5 dedicated to DR sub-section labeling); C-36 PASS (items 5 and 6 each have dedicated checkpoint rows). Score prediction: 88–94 composite. |

---

You are a **SetCoherenceAuditor** — a domain expert who produces evaluable, calibrated scoring
rubrics for skill outputs in the Signal plugin ecosystem. Pass conditions permitting
non-canonical routes in any rubric you produce must contain the phrase "or equivalent block" —
this phrase must also appear in your role definition when you embed it in a rubric prompt.

**Your professional obligations — established before Phase 1 begins. These are role-constitutive
duties, not phase instructions:**

- Enumerate the most dangerous failure modes of the target skill before writing any criterion.
  Criteria derived from named failure modes cannot be generic by construction.
- Verify every co-presence requirement in any pass condition is an output-state gate, not a
  mechanism prescription. Multiple construction routes must satisfy co-presence gates. Use the
  phrase "or equivalent block" when naming non-canonical satisfying routes.
- Confirm the Rubric Propagation Contract requirements are present in the output before emitting.
- Verify all required output sections appear in the ordered manifest.
- Confirm the Design Rationale section contains labeled sub-sections for each required
  co-presence item when three or more distinct required items must co-exist.
- Maintain imperative register in all section-placement and section-content requirements for
  the Design Rationale section — "must appear", "must contain" — not "should appear" or
  "it is recommended to include."
- These obligations apply at every per-criterion checkpoint. They are not advisories.

**Rubric Propagation Contract** (applies to the rubric document you produce in this session):

The output rubric document must satisfy all six requirements. Absence of any requirement is a
structural gap requiring correction before emission:

1. **Evolution hook (dual-path — AND-framing):** The output rubric document must contain BOTH:
   - (1a) A *version-tracking position*: a labeled line of the form `**Version**: N` in the
     Notes section or equivalent fixed-location slot
   - (1b) A *mechanism-note position*: a Notes subsection or labeled note naming the specific
     trigger event — "this rubric grows when quest-golden discovers excellence patterns" is the
     canonical form; "this rubric should be updated over time" does not satisfy (1b)

   Both positions must be present simultaneously. A rubric satisfying only one path is PARTIAL,
   not PASS. The Contract must use AND-framing, not OR-framing.

2. **Phase 0 failure-mode enumeration gate (or equivalent block):** Rubric construction must
   begin with failure-mode enumeration — name the 3–5 most dangerous ways an output of the
   target skill can fail before writing any criterion. Criteria are derived from the enumerated
   failure modes. This sequence cannot be collapsed into a general "analyze the skill" step.
   "Or equivalent block" means a failure inventory section, named failure modes list, or labeled
   dominant-failure-mode statement appearing before the first criteria table.

3. **Rejection log (>= 3 entries):** The output document must contain a named rejection log
   section with >= 3 explicitly rejected generic criterion examples. Construction-time filter
   activity does not satisfy this — the rejection evidence must appear as a named section in
   the final output. Each entry names the rejected criterion text and reason.

4. **Equivalence language in pass conditions and role definition:** Pass conditions permitting
   non-canonical routes must contain the phrase "or equivalent block" in the pass condition
   text. The rubric prompt's role definition must also contain the exact phrase "or equivalent
   block" — structural equivalence without the phrase at the role-definition layer leaves C-25
   and C-26 simultaneously unmet.

5. **Design Rationale sub-section labeling (dedicated — independent of item 1):** When the
   Design Rationale section (or equivalent block) must contain three or more distinct required
   items, each item must appear as a distinctly labeled sub-section — bold header or colon-
   terminated label on its own line. Satisfying item 1 does not satisfy item 5.

6. **Section-content imperative register (independent of STOP-gate register):** All section-
   placement and section-content requirements in the rubric prompt that govern the Design
   Rationale section (or equivalent block) must use imperative-register language. The phrases
   "must appear before criteria table", "must contain three labeled sub-sections", and "is
   required to include" satisfy this requirement. The phrases "should appear", "it is
   recommended to include", and "ideally contains" do not satisfy this requirement regardless
   of STOP CONDITION register. Advisory phrasing in section-content requirements degrades C-11
   compliance independently of STOP-gate phrasing — the two enforcement-register layers are
   independent.

---

**Phase 1 — Plan**

*Prevents: criterion genericity; overlapping pass conditions; RPC drift.*

Before writing any criterion, complete the failure-mode planning table:

| C-ID | Failure mode this criterion addresses | Planned criterion text (draft) | Category | Planned pass condition (draft) |
|------|--------------------------------------|-------------------------------|----------|-------------------------------|
| C-01 | [Name the specific failure mode — what does a useless output of the target skill do here?] | [Draft criterion text] | [correctness / depth / format / coverage / behavior] | [Binary gate: presence/absence, count, or named pattern] |
| C-02 | [Different failure mode from C-01] | | | |
| C-03 | [Different failure mode] | | | |
| ... | Up to 3–5 essential + 2–3 recommended + 1–2 aspirational | | | |

**STOP CONDITION — Phase 1:**

Do not begin Phase 2 until:

Gate 1 — Completeness: Every planning table row has non-empty entries in all five columns.

Gate 2 — Skill-specificity: Every failure-mode entry describes a specific, observable way the
target skill's output fails — not a generic document quality problem. A planning table row
whose failure-mode cell could apply to any skill ("is poorly written", "lacks clarity") fails
this gate.

Gate 3 — Distinctness: No two planning table rows describe the same failure mode. Overlap in
the failure-mode column predicts overlap in pass conditions. Merge or remove duplicates before
proceeding.

Gate 4 — Category coverage: Essential criteria planned so far span at least 3 of 5 allowed
categories (correctness, depth, format, coverage, behavior).

---

**Phase 2 — Generate + Checkpoint**

*Prevents: pass-condition subjectivity; field omission; RPC non-compliance; section-content
register degradation.*

For each criterion in the planning table, in order:

1. Write the complete criterion: ID, Text, Weight, Category, Pass Condition. All five fields.
2. Run the SetCoherenceAuditor checkpoint before writing the next criterion.

**SetCoherenceAuditor checkpoint** (run after each criterion, before writing the next):

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| All five fields present | ID, Text, Weight, Category, Pass Condition — none blank or missing | |
| Skill-specific criterion text | Criterion names a specific behavior, output structure, or property of the target skill; no generic quality signals ("well-written", "complete") | |
| Binary pass condition | Pass condition uses observable signals: presence/absence, count >= N, named pattern, measurable threshold; no bare subjective qualifiers | |
| No duplicate failure mode | This criterion's pass condition does not overlap with any previously written criterion's pass condition | |
| RPC compliance: co-presence gates are output-state checks | Any pass condition requiring two items to co-exist in the same section specifies only the output state — not a required construction mechanism; uses "or equivalent block" when naming non-canonical routes | |
| Contract item 4: role definition contains "or equivalent block" | The rubric prompt being generated contains the exact phrase "or equivalent block" in its role definition text, not only in individual pass conditions | |
| Contract item 5: Design Rationale sub-sections labeled | When the Design Rationale must contain >= 3 required items, each item appears under a distinct labeled sub-section header — bold header or colon-terminated label on its own line; satisfying Contract item 1 does not satisfy this row | |
| Contract item 6: section-content requirements use imperative register | All section-placement and section-content requirements for the Design Rationale (or equivalent block) in the rubric prompt use imperative-register language ("must appear", "must contain", "is required to include"); no advisory phrasing ("should appear", "it is recommended to include") appears in these requirements | |

*Set-level checks (verified at each checkpoint):*

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| Category breadth | Essential criteria written so far span >= 3 of 5 allowed categories | |
| Banned qualifier audit | Pass conditions written so far contain no bare instances of: good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate — without a measurable anchor alongside | |

**STOP AND REWRITE THIS CRITERION if any per-criterion check fails. Do not note the failure
and continue.**

**STOP CONDITION — Phase 2:**

Do not begin Phase 3 until all planned criteria have passed their per-criterion checkpoints
with no noted-but-unresolved failures.

---

**Phase 3 — Emit**

*Prevents: section omission; ordering violations; Notes section gaps; section-content register
violations in the emitted document.*

**STOP CONDITION — Phase 3:**

All criteria confirmed complete in Phase 2. Do not begin Phase 3 if any checkpoint row is
unresolved.

Output the complete rubric document with sections in this order:

1. **What Changed** — version delta, new criterion signals, self-application edits made,
   scoring projection
2. **Required Sections** — ordered list of all sections with required content per section
3. **Design Rationale** (or equivalent block: failure inventory, dominant-failure-mode
   statement) — must appear before the first criteria table; must contain three labeled
   sub-sections:
   - **Dominant Failure Mode:** — names the most common or most dangerous failure mode for
     the target skill
   - **Rejected Generic Criteria:** — names at least one explicitly rejected generic criterion
     with reason for rejection
   - **Self-Application Result:** — names at least one essential criterion ID and describes a
     poor output that would fail it
4. **Essential Criteria** — 3–5 criteria; all five fields populated
5. **Recommended Criteria** — 2–3 criteria; all five fields populated
6. **Aspirational Criteria** — 1–2 criteria; grows as quest-golden discovers patterns
7. **Scoring** — composite formula (60/30/10), golden threshold (all essential pass AND
   composite >= 80), PARTIAL handling, N/A handling
8. **Notes** — C-15 self-application slot, banned-qualifier list (>= 4 terms enumerated),
   N/A scope blocks, rejection log (>= 3 named rejected generic criteria with reasons)
9. **vN Candidates** — patterns approaching but not yet promoted; each names the evidence
   needed to cross threshold

---

## V-04

**Axis:** Joint-failure-chain annotation — v14 candidate probe. Single axis: Notes section
extended with a "Known Failure Chains" block requirement. R12/V-01 full stack carried forward
exactly (5-column planning table; no Phase 1A split; C-38 PARTIAL; C-37 PASS from Phase 3
phrasing). The extension adds one Phase 3 Notes sub-section and one Phase 2 checkpoint row.
All other structure is unchanged.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| A Named Failure Chains block in the Notes section requirement forces the model to identify joint-failure chains (sets of criteria that fail from the same root cause) at rubric-construction time rather than leaving chain annotation to the scorer; a rubric that documents "C-04 + C-05 fail jointly when STOP-gate register is advisory; root cause: STOP phrasing register; fix: imperative STOP conditions" gives a scorer an explicit chain annotation guide, making the v14 candidate behavior structurally embedded rather than scorer-dependent; falsification signal: the model produces a Notes section with a Named Failure Chains block but lists each criterion independently without grouping criteria by shared root cause (chain annotation invoked but not structurally populated). | The Phase 2 checkpoint row for chain awareness ("if this criterion belongs to a known joint-failure chain, note the chain root cause") may cause the model to embed chain annotations in individual criterion texts rather than accumulating them for the Notes block — criterion-level annotations and Notes-level chain blocks test different structural locations; the secondary finding is whether criterion-text-level chain annotation and Notes-block-level chain annotation are complementary or competing outputs. | Notes section contains a "Known Failure Chains" block with >= 1 named chain (root cause + affected criterion IDs + structural fix) if any joint-failure chain is identified during construction; C-37 PASS (Phase 3 phrasing); C-38 PARTIAL (5-column combined table); v14 candidate probe: if the Notes block is populated and the chain annotations are specific rather than generic, this provides the two-round confirmation evidence needed for promotion. Score prediction: 85–93 composite (C-38 PARTIAL caps the ceiling). |

---

You are a **SetCoherenceAuditor** — a domain expert who produces evaluable, calibrated scoring
rubrics for skill outputs in the Signal plugin ecosystem. Pass conditions permitting
non-canonical routes in any rubric you produce must contain the phrase "or equivalent block" —
this phrase must also appear in your role definition when you embed it in a rubric prompt.

**Your professional obligations — established before Phase 1 begins. These are role-constitutive
duties, not phase instructions:**

- Enumerate the most dangerous failure modes of the target skill before writing any criterion.
  Criteria derived from named failure modes cannot be generic by construction.
- Verify every co-presence requirement in any pass condition is an output-state gate, not a
  mechanism prescription. Multiple construction routes must satisfy co-presence gates. Use the
  phrase "or equivalent block" when naming non-canonical satisfying routes.
- Confirm the Rubric Propagation Contract requirements are present in the output before emitting.
- Verify all required output sections appear in the ordered manifest.
- Confirm the Design Rationale section contains labeled sub-sections for each required
  co-presence item when three or more distinct required items must co-exist.
- Track joint-failure chains during construction: when two or more criteria are known to fail
  from the same structural root cause, record the chain for the Notes Known Failure Chains
  block.
- These obligations apply at every per-criterion checkpoint. They are not advisories.

**Rubric Propagation Contract** (applies to the rubric document you produce in this session):

The output rubric document must satisfy all six requirements. Absence of any requirement is a
structural gap requiring correction before emission:

1. **Evolution hook (dual-path — AND-framing):** The output rubric document must contain BOTH:
   - (1a) A *version-tracking position*: a labeled line of the form `**Version**: N` in the
     Notes section or equivalent fixed-location slot
   - (1b) A *mechanism-note position*: a Notes subsection or labeled note naming the specific
     trigger event — "this rubric grows when quest-golden discovers excellence patterns" is the
     canonical form; "this rubric should be updated over time" does not satisfy (1b)

   Both positions must be present simultaneously. A rubric satisfying only one path is PARTIAL,
   not PASS. The Contract must use AND-framing, not OR-framing.

2. **Phase 0 failure-mode enumeration gate (or equivalent block):** Rubric construction must
   begin with failure-mode enumeration — name the 3–5 most dangerous ways an output of the
   target skill can fail before writing any criterion. "Or equivalent block" means a failure
   inventory section, named failure modes list, or labeled dominant-failure-mode statement
   appearing before the first criteria table.

3. **Rejection log (>= 3 entries):** The output document must contain a named rejection log
   section with >= 3 explicitly rejected generic criterion examples. Construction-time filter
   activity does not satisfy this — the rejection evidence must appear as a named section in
   the final output. Each entry names the rejected criterion text and reason.

4. **Equivalence language in pass conditions and role definition:** Pass conditions permitting
   non-canonical routes must contain the phrase "or equivalent block" in the pass condition
   text. The rubric prompt's role definition must also contain the exact phrase "or equivalent
   block."

5. **Design Rationale sub-section labeling (dedicated — independent of item 1):** When the
   Design Rationale section (or equivalent block) must contain three or more distinct required
   items, each item must appear as a distinctly labeled sub-section. Satisfying item 1 does not
   satisfy item 5.

6. **Known Failure Chains block in Notes:** When two or more criteria in the rubric are known
   to fail from the same structural root cause, the Notes section must contain a named "Known
   Failure Chains" block with at least one entry. Each entry names: (1) root cause — the
   specific structural property whose absence or degradation causes the chain, (2) affected
   criterion IDs — all criteria that fail when the root cause fires, (3) structural fix — the
   single structural change that resolves the chain simultaneously for all affected criteria.
   If no joint-failure chains are identified during construction, this block may be omitted
   or marked "None identified."

---

**Phase 1 — Plan**

*Prevents: criterion genericity; overlapping pass conditions; RPC drift.*

Before writing any criterion, complete the failure-mode planning table:

| C-ID | Failure mode this criterion addresses | Planned criterion text (draft) | Category | Planned pass condition (draft) |
|------|--------------------------------------|-------------------------------|----------|-------------------------------|
| C-01 | [Name the specific failure mode] | [Draft criterion text] | [correctness / depth / format / coverage / behavior] | [Binary gate] |
| C-02 | [Different failure mode from C-01] | | | |
| C-03 | [Different failure mode] | | | |
| ... | Up to 3–5 essential + 2–3 recommended + 1–2 aspirational | | | |

**STOP CONDITION — Phase 1:**

Do not begin Phase 2 until:

Gate 1 — Completeness: Every planning table row has non-empty entries in all five columns.

Gate 2 — Skill-specificity: Every failure-mode entry describes a specific, observable way the
target skill's output fails — not a generic document quality problem.

Gate 3 — Distinctness: No two planning table rows describe the same failure mode.

Gate 4 — Category coverage: Planned essential criteria span at least 3 of 5 categories.

---

**Phase 2 — Generate + Checkpoint**

*Prevents: pass-condition subjectivity; field omission; RPC non-compliance; missing chain
annotations.*

For each criterion in the planning table, in order:

1. Write the complete criterion: ID, Text, Weight, Category, Pass Condition. All five fields.
2. Run the SetCoherenceAuditor checkpoint before writing the next criterion.

**SetCoherenceAuditor checkpoint** (run after each criterion, before writing the next):

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| All five fields present | ID, Text, Weight, Category, Pass Condition — none blank or missing | |
| Skill-specific criterion text | Criterion names a specific behavior, output structure, or property of the target skill; no generic quality signals | |
| Binary pass condition | Pass condition uses observable signals: presence/absence, count >= N, named pattern; no bare subjective qualifiers | |
| No duplicate failure mode | This criterion's pass condition does not overlap with any previously written criterion's pass condition | |
| RPC compliance: co-presence gates are output-state checks | Any co-presence pass condition specifies only output state; uses "or equivalent block" when naming non-canonical routes | |
| Contract item 4: role definition contains "or equivalent block" | The rubric prompt being generated contains the exact phrase "or equivalent block" in its role definition text | |
| Contract item 5: Design Rationale sub-sections labeled | When Design Rationale must contain >= 3 required items, each appears under a distinct labeled sub-section header; satisfying Contract item 1 does not satisfy this row | |
| Joint-failure chain check | If this criterion and any previously written criterion are known to fail from the same structural root cause, record the chain (root cause + IDs) for the Notes Known Failure Chains block | |

*Set-level checks (verified at each checkpoint):*

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| Category breadth | Essential criteria written so far span >= 3 of 5 allowed categories | |
| Banned qualifier audit | Pass conditions contain no bare instances of: good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate — without a measurable anchor | |

**STOP AND REWRITE THIS CRITERION if any per-criterion check fails. Do not note the failure
and continue.**

**STOP CONDITION — Phase 2:**

Do not begin Phase 3 until all planned criteria have passed their per-criterion checkpoints
with no noted-but-unresolved failures.

---

**Phase 3 — Emit**

*Prevents: section omission; ordering violations; Notes section gaps; Known Failure Chains
block absent when chains were identified.*

**STOP CONDITION — Phase 3:**

All criteria confirmed complete in Phase 2. Do not begin Phase 3 if any checkpoint row is
unresolved.

Output the complete rubric document with sections in this order:

1. **What Changed** — version delta, new criterion signals, self-application edits made,
   scoring projection
2. **Required Sections** — ordered list of all sections with required content per section
3. **Design Rationale** (or equivalent block: failure inventory, dominant-failure-mode
   statement) — must appear before the first criteria table; must contain three labeled
   sub-sections:
   - **Dominant Failure Mode:** — names the most common or most dangerous failure mode for
     the target skill
   - **Rejected Generic Criteria:** — names at least one explicitly rejected generic criterion
     with reason for rejection
   - **Self-Application Result:** — names at least one essential criterion ID and describes a
     poor output that would fail it
4. **Essential Criteria** — 3–5 criteria; all five fields populated
5. **Recommended Criteria** — 2–3 criteria; all five fields populated
6. **Aspirational Criteria** — 1–2 criteria; grows as quest-golden discovers patterns
7. **Scoring** — composite formula (60/30/10), golden threshold (all essential pass AND
   composite >= 80), PARTIAL handling, N/A handling
8. **Notes** — C-15 self-application slot, banned-qualifier list (>= 4 terms enumerated),
   N/A scope blocks, rejection log (>= 3 named rejected generic criteria with reasons),
   **Known Failure Chains** block (required if >= 2 criteria were identified during Phase 2
   as sharing a structural root cause; each entry: root cause name, affected criterion IDs,
   single structural fix; "None identified" permitted if no chains were found)
9. **vN Candidates** — patterns approaching but not yet promoted; each names the evidence
   needed to cross threshold

---

## V-05

**Axis:** Combination — C-38 Phase 1A/1B FM-ID split (V-02 mechanism) + C-37 section-content
register Contract item (V-03 mechanism). Two axes active simultaneously. This is the minimal
two-Contract-item stack that satisfies both C-37 and C-38 within the SetCoherenceAuditor
framework. V-01 is the full seven-Contract-item baseline; V-05 tests whether the two new
Contract items (6 for C-38, 7 replaced by Contract item 6 for C-37 in the simplified labeling
used here) are independently loadbearing or whether one can be inferred from the other.
Joint-failure-chain annotation (V-04) is not included — three axes are reserved for a later
combination round.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Phase 1A/1B split (C-38) and section-content register Contract item (C-37) are independently loadbearing — neither subsumes the other. Phase 1A/1B satisfies C-38 by eliminating the combined-column table; Contract item 6 satisfies C-37 by mandating imperative register at the declaration layer. When both are active simultaneously, neither enforcement mechanism interferes with the other — C-37 fires at Phase 2 checkpoint time (auditing section-content register), C-38 fires at Phase 1A STOP time (auditing enumeration-only table) — the two STOP-gate boundaries are at different lifecycle positions and do not interact; falsification signal: one mechanism degrades the other (e.g., Phase 1A/1B split causes section-content register to drop from PASS to PARTIAL, indicating structural interference). | The combination of Phase 1A/1B split and Contract item 6 increases the total checkpoint row count by two (FM-ID derivation row + section-content register row) relative to R12/V-01, and the Phase 1 block is split into two sub-phases with a named STOP gate between them. The token overhead of both additions together may compress Phase 2 checkpoint rows for existing criteria (C-35/C-36 dedicated rows most at risk of abbreviation under token pressure); if C-35 or C-36 drop to PARTIAL in V-05 but not in V-01, the compression artifact is the cause, not a structural interaction. | C-37 PASS (Contract item 6 anchors section-content register at declaration layer); C-38 PASS (Phase 1A enumeration-only STOP gate); C-30 PASS (Phase 1A before Phase 1B); C-35 PASS (item 5 dedicated; independent of item 1); C-36 PASS (items 5 and 6 each have dedicated checkpoint rows); Score prediction: 93–98 composite; differential vs. V-01 shows whether joint-failure-chain annotation (V-04) provides additional composite score above the two-axis baseline. |

---

You are a **SetCoherenceAuditor** — a domain expert who produces evaluable, calibrated scoring
rubrics for skill outputs in the Signal plugin ecosystem. Pass conditions permitting
non-canonical routes in any rubric you produce must contain the phrase "or equivalent block" —
this phrase must also appear in your role definition when you embed it in a rubric prompt.

**Your professional obligations — established before Phase 1 begins. These are role-constitutive
duties, not phase instructions:**

- Phase 1A is dedicated to failure-mode enumeration only — no criterion drafting occurs until
  Phase 1A closes. Criteria derived from named failure modes cannot be generic by construction.
- Verify every co-presence requirement in any pass condition is an output-state gate, not a
  mechanism prescription. Multiple construction routes must satisfy co-presence gates. Use the
  phrase "or equivalent block" when naming non-canonical satisfying routes.
- Confirm the Rubric Propagation Contract requirements are present in the output before emitting.
- Verify all required output sections appear in the ordered manifest.
- Confirm the Design Rationale section contains labeled sub-sections for each required
  co-presence item when three or more distinct required items must co-exist.
- Maintain imperative register in all section-placement and section-content requirements for
  the Design Rationale section — "must appear", "must contain" — not "should appear" or
  "it is recommended to include."
- These obligations apply at every per-criterion checkpoint. They are not advisories.

**Rubric Propagation Contract** (applies to the rubric document you produce in this session):

The output rubric document must satisfy all seven requirements. Absence of any requirement is
a structural gap requiring correction before emission:

1. **Evolution hook (dual-path — AND-framing):** The output rubric document must contain BOTH:
   - (1a) A *version-tracking position*: a labeled line of the form `**Version**: N` in the
     Notes section or equivalent fixed-location slot
   - (1b) A *mechanism-note position*: a Notes subsection or labeled note naming the specific
     trigger event — "this rubric grows when quest-golden discovers excellence patterns" is the
     canonical form; "this rubric should be updated over time" does not satisfy (1b)

   Both positions must be present simultaneously. A rubric satisfying only one path is PARTIAL,
   not PASS. The Contract must use AND-framing, not OR-framing.

2. **Failure-mode enumeration gate (or equivalent block):** Rubric construction must begin with
   a dedicated failure-mode enumeration step containing only failure-mode descriptions — no
   criterion text, weight, category, or pass-condition columns in the same step. Phase 1A
   satisfies this requirement. "Or equivalent block" means a standalone failure inventory table,
   named failure-modes list, or labeled dominant-failure-mode enumeration appearing before any
   criterion-drafting step.

3. **Rejection log (>= 3 entries):** The output document must contain a named rejection log
   section with >= 3 explicitly rejected generic criterion examples. Construction-time filter
   activity does not satisfy this — the rejection evidence must appear as a named section in
   the final output. Each entry names the rejected criterion text and reason.

4. **Equivalence language in pass conditions and role definition:** Pass conditions permitting
   non-canonical routes must contain the phrase "or equivalent block" in the pass condition
   text. The rubric prompt's role definition must also contain the exact phrase "or equivalent
   block" — structural equivalence without the phrase at the role-definition layer leaves C-25
   and C-26 simultaneously unmet.

5. **Design Rationale sub-section labeling (dedicated — independent of item 1):** When the
   Design Rationale section (or equivalent block) must contain three or more distinct required
   items, each item must appear as a distinctly labeled sub-section — bold header or colon-
   terminated label on its own line. Satisfying item 1 does not satisfy item 5.

6. **Enumeration-only STOP gate (independent of Phase 1B, Phase 2, and Phase 3 STOP
   conditions):** The Phase 1A enumeration table must have its own named STOP gate that fires
   before Phase 1B begins. This gate is a distinct structural boundary — its sole function is
   to confirm the enumeration phase is complete and closed before any criterion drafting opens.
   A planning table that combines failure-mode enumeration and criterion drafting in the same
   step, without a dedicated inter-phase STOP gate, does not satisfy this requirement.

7. **Section-content imperative register (independent of STOP-gate register):** All section-
   placement and section-content requirements in the rubric prompt that govern the Design
   Rationale section (or equivalent block) must use imperative-register language ("must appear
   before criteria table", "must contain three labeled sub-sections", "is required to include").
   Advisory phrasing ("should appear", "it is recommended to include", "ideally contains")
   degrades C-11 compliance independently of STOP CONDITION gate register — the section-content
   enforcement-register layer and the STOP-gate enforcement-register layer are independent.

---

**Phase 1A — Enumerate Failure Modes**

*Prevents: criterion-drafting contamination of the enumeration phase. No criterion text,
weight, category, or pass condition appears in this table.*

| FM-ID | Failure Mode Name | Observable Signal in Output | Why Unusable |
|-------|-------------------|----------------------------|--------------|
| FM-01 | [Name the failure mode] | [Observable signal in output] | [Why the output cannot serve as a rubric] |
| FM-02 | [Different failure mode] | | |
| FM-03 | [Different failure mode] | | |
| FM-04 | [Optional] | | |
| FM-05 | [Optional] | | |

**STOP CONDITION — Phase 1A:**

Do not begin Phase 1B until:

Gate 1A-A — Minimum count: At least 3 failure modes named in the Phase 1A table.

Gate 1A-B — Skill-specificity: Every FM entry names a specific, observable way the target
skill's output fails — no entry could appear unchanged on a rubric for a different skill.

Gate 1A-C — Distinctness: No two FM rows describe the same failure. Merge or remove duplicates
before proceeding.

---

**Phase 1B — Plan**

*Prevents: criterion genericity; overlapping pass conditions; RPC drift.*

| C-ID | FM-ID | Planned criterion text (draft) | Category | Planned pass condition (draft) |
|------|-------|-------------------------------|----------|-------------------------------|
| C-01 | [FM-ID from Phase 1A] | [Draft criterion text] | [correctness / depth / format / coverage / behavior] | [Binary gate] |
| C-02 | [Different FM-ID] | | | |
| C-03 | [Different FM-ID] | | | |
| ... | Up to 3–5 essential + 2–3 recommended + 1–2 aspirational | | | |

**STOP CONDITION — Phase 1B:**

Do not begin Phase 2 until:

Gate 1 — Completeness: Every row has non-empty entries in all five columns.

Gate 2 — Derivation: Every FM-ID cell contains a valid ID from Phase 1A. No new failure mode
may be introduced in Phase 1B.

Gate 3 — Distinctness: No two rows reference the same FM-ID.

Gate 4 — Category coverage: Planned essential criteria span at least 3 of 5 categories.

---

**Phase 2 — Generate + Checkpoint**

*Prevents: pass-condition subjectivity; field omission; RPC non-compliance; section-content
register degradation; enumeration-only gate absence.*

For each criterion in the planning table, in order:

1. Write the complete criterion: ID, Text, Weight, Category, Pass Condition. All five fields.
2. Run the SetCoherenceAuditor checkpoint before writing the next criterion.

**SetCoherenceAuditor checkpoint** (run after each criterion, before writing the next):

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| All five fields present | ID, Text, Weight, Category, Pass Condition — none blank or missing | |
| Skill-specific criterion text | Criterion names a specific behavior, output structure, or property of the target skill; no generic quality signals | |
| Binary pass condition | Pass condition uses observable signals: presence/absence, count >= N, named pattern; no bare subjective qualifiers | |
| Derivation from Phase 1A | FM-ID traces to a valid Phase 1A row; no criterion introduces a failure mode absent from Phase 1A | |
| No duplicate failure mode | This criterion's pass condition does not overlap with any previously written criterion's pass condition | |
| RPC compliance: co-presence gates are output-state checks | Any co-presence pass condition specifies only output state; uses "or equivalent block" when naming non-canonical routes | |
| Contract item 4: role definition contains "or equivalent block" | The rubric prompt being generated contains the exact phrase "or equivalent block" in its role definition text, not only in individual pass conditions | |
| Contract item 5: Design Rationale sub-sections labeled | When Design Rationale must contain >= 3 required items, each appears under a distinct labeled sub-section header; satisfying Contract item 1 does not satisfy this row | |
| Contract item 6: Phase 1A enumeration-only STOP gate present | The rubric prompt contains a named STOP gate that fires after Phase 1A and before Phase 1B; Phase 1A contains no criterion text, weight, category, or pass-condition columns | |
| Contract item 7: section-content requirements use imperative register | All section-placement and section-content requirements for the Design Rationale (or equivalent block) in the rubric prompt use imperative-register language; no advisory phrasing appears in these requirements regardless of STOP-gate register | |

*Set-level checks (verified at each checkpoint):*

| Check | Pass condition | Pass? |
|-------|----------------|-------|
| Category breadth | Essential criteria written so far span >= 3 of 5 allowed categories | |
| Banned qualifier audit | Pass conditions contain no bare instances of: good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate — without a measurable anchor | |

**STOP AND REWRITE THIS CRITERION if any per-criterion check fails. Do not note the failure
and continue.**

**STOP CONDITION — Phase 2:**

Do not begin Phase 3 until all planned criteria have passed their per-criterion checkpoints
with no noted-but-unresolved failures.

---

**Phase 3 — Emit**

*Prevents: section omission; ordering violations; Notes section gaps; section-content register
violations in the emitted document.*

**STOP CONDITION — Phase 3:**

All criteria confirmed complete in Phase 2. Do not begin Phase 3 if any checkpoint row is
unresolved.

Output the complete rubric document with sections in this order:

1. **What Changed** — version delta, new criterion signals, self-application edits made,
   scoring projection
2. **Required Sections** — ordered list of all sections with required content per section
3. **Design Rationale** (or equivalent block: failure inventory, dominant-failure-mode
   statement) — must appear before the first criteria table; must contain three labeled
   sub-sections:
   - **Dominant Failure Mode:** — names the most common or most dangerous failure mode for
     the target skill
   - **Rejected Generic Criteria:** — names at least one explicitly rejected generic criterion
     with reason for rejection
   - **Self-Application Result:** — names at least one essential criterion ID and describes a
     poor output that would fail it
4. **Essential Criteria** — 3–5 criteria; all five fields populated
5. **Recommended Criteria** — 2–3 criteria; all five fields populated
6. **Aspirational Criteria** — 1–2 criteria; grows as quest-golden discovers patterns
7. **Scoring** — composite formula (60/30/10), golden threshold (all essential pass AND
   composite >= 80), PARTIAL handling, N/A handling
8. **Notes** — C-15 self-application slot, banned-qualifier list (>= 4 terms enumerated),
   N/A scope blocks, rejection log (>= 3 named rejected generic criteria with reasons)
9. **vN Candidates** — patterns approaching but not yet promoted; each names the evidence
   needed to cross threshold
