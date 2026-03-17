Now I have everything. Applying the same elevation logic used for R6:

- **Signal 1** (naming criteria by ID in structural contract) — same class as R6 Pattern 4: it's the prompt design mechanism by which C-21/C-22/C-23 are enforced, not a new observable output property. Not elevated.
- **Signal 2** (falsification counter-example in invariant) — distinct output property extending C-22: the invariant names what falsifies it, not just what passes it. Elevate as **C-24**.
- **Signal 3** (phase-as-structural-lock) — distinct output property extending C-02: named phase headers architecturally enforce Rogers ordering, structural compliance stronger than semantic compliance. Elevate as **C-25**.

Max composite: 165 → **175**. Two new auto-fail chains added.

```markdown
# Rubric: listen-adoption — v8

**Max composite:** 175 | **Golden threshold:** 80

---

**What changed from v7:**

Two new aspirational criteria (C-24, C-25) from R7 Excellence Signals 2 and 3.

Signal 1 (naming rubric criteria by ID in the structural contract) was not elevated — it is the
prompt design mechanism by which C-21/C-22/C-23 are enforced at design time, not a distinct
observable property of the output artifact. Same class as R6 Signal 4 (counter-example in
template cell), which was also not elevated.

---

**C-24 — Self-verifying invariant names its own falsification condition** (5 pts)
Source: V-04's SECTION K invariant stating "Failure mode: a 'Yes' row whose CORRECTION BLOCK
Location points to a section that contains no CORRECTION BLOCK, or whose CORRECTION BLOCK contains
no BEFORE field, falsifies this invariant." C-22 requires that the terminal section contain a
self-verifying invariant (a claim verifiable by reading the document). C-24 extends C-22: the
invariant must also name the exact condition that would falsify it, not only the condition that
passes it. An evaluator can approach the invariant from either direction — confirm it by finding
a CORRECTION BLOCK at every Yes-row location, or refute it by finding a Yes-row pointing to an
empty section or a block missing a BEFORE field. Stating what falsifies a claim is stronger than
stating only what passes it because it names the failure mode the evaluation is designed to detect.
C-24 fails automatically if C-22 fails.

**C-25 — Named phase structure architecturally enforces Rogers adoption sequence** (5 pts)
Source: V-04's PHASE 1 (INNOVATORS) through PHASE 6 (LAGGARDS) document structure, with PHASE 3
named "CHASM" as a non-adoption phase between PHASE 2 (EARLY ADOPTERS) and PHASE 4 (EARLY
MAJORITY). When Rogers phases are used as section or table-row headers rather than as instructed
ordering, the model cannot populate a later-phase row without completing the prior-phase header —
structural compliance is enforced by document architecture rather than semantic instruction. The
chasm phase must be explicitly named as a non-adoption interstitial between early-adopters and
early-majority (a blank gap or prose note does not satisfy the architectural requirement). C-02
tests whether the Rogers sequence is present and correct; C-25 tests whether the document
structure itself makes sequence violation structurally impossible. A correctly ordered timeline
without phase headers passes C-02 but fails C-25. C-25 fails automatically if C-02 fails.

**Max composite: 165 → 175. Golden threshold (80) unchanged.**

Dependency chain:
```
C-16 (audit exists) -> C-18 (correction triggered) -> C-19 (content visible)
C-16 (audit exists) -> C-20 (gate states consolidated)
C-20 (gate states consolidated) -> C-21 (correction content not in terminal section)
C-20 (gate states consolidated) -> C-22 (terminal section has self-verifying invariant)
C-22 (self-verifying invariant exists) -> C-24 (invariant names falsification condition)
C-16 (audit exists) -> C-23 (named verification boundary present)
C-02 (adoption sequence present) -> C-25 (phase headers enforce sequence architecturally)
```

The seven terminal criteria in seven lines:
C-19 tests whether *corrected content is visible in the output*.
C-20 tests whether *gate state is consolidated in a single named terminal location*.
C-21 tests whether *corrected content and gate state occupy separate structural locations*.
C-22 tests whether *the terminal section contains a verifiable claim about the rest of the document*.
C-23 tests whether *a named boundary separates content generation from the audit stage*.
C-24 tests whether *the self-verifying invariant names the condition that would falsify it*.
C-25 tests whether *named phase headers make Rogers sequence violation structurally impossible*.

---

## Essential Criteria (automatic fail if any fails)

| ID | Category | Weight | Criterion | Pass Condition |
|----|----------|--------|-----------|----------------|
| C-01 | correctness | essential (12) | **All 16 stock roles mapped to Rogers archetype** — output assigns every named persona in the skill contract to one of the five canonical Rogers archetypes (innovators, early-adopters, early-majority, late-majority, laggards). | Output contains a mapping table or list covering all 16 named roles; each role maps to exactly one of the five canonical archetype labels; no role is omitted or duplicated. |
| C-02 | correctness | essential (12) | **Month-by-month adoption sequence** — output includes a timeline (>=3 months) showing which archetypes / roles adopt in each period, with explicit ordering (who tries first, who follows). | At least 3 distinct time steps are present; innovators and early-adopters appear before early-majority; late-majority before laggards; no inversion of Rogers sequence. |
| C-03 | correctness | essential (12) | **Chasm identification** — output explicitly names the chasm between early-adopters and early-majority and states what bridging mechanism (or gap risk) applies to this feature. | The word "chasm" (or equivalent: "crossing the chasm", "adoption gap") appears; at least one concrete bridging mechanism or gap risk is stated, tied to this feature's specifics rather than generic advice. |
| C-04 | coverage | essential (12) | **Intervention recommendations ranked by adoption delta** — output provides >=2 ranked interventions with an estimated adoption delta (quantified or directional: high/medium/low). | At least 2 interventions listed; each has a stated adoption delta (numeric % or H/M/L label); list is in descending delta order or explicitly marked as ranked. |
| C-05 | correctness | essential (12) | **Champion network named** — output identifies which roles/archetypes form the champion network (the social bridge across the chasm). | At least 2 specific roles or archetype groups are named as champions; the rationale connects their archetype position to why they can bridge into early-majority. |

---

## Recommended Criteria (raise quality)

| ID | Category | Weight | Criterion | Pass Condition |
|----|----------|--------|-----------|----------------|
| C-06 | depth | recommended (10) | **Churn risk per archetype** — output identifies churn risk for at least 2 archetypes, explaining what triggers churn for each. | Churn risks stated for >=2 archetypes; each risk entry names a trigger (not just "may churn") and at least one mitigation or warning signal. |
| C-07 | depth | recommended (10) | **Spread mechanism named per transition** — for each archetype-to-archetype adoption transition, the output states the spread mechanism (word-of-mouth, demo, mandate, tooling integration, etc.). | Each major transition in the timeline is annotated with a spread mechanism label; generic "word of mouth" alone does not pass — at least one transition must cite a feature-specific or role-specific mechanism. |
| C-08 | format | recommended (10) | **Tabular or structured month view** — the month-by-month timeline is presented in a table, numbered list, or clearly structured format (not buried in prose). | Timeline is rendered as a table, structured list, or clearly labeled month headers; a reader can scan to any month and identify adopters without reading surrounding prose. |

---

## Aspirational Criteria (raise the bar)

| ID | Category | Weight | Criterion | Pass Condition |
|----|----------|--------|-----------|----------------|
| C-09 | depth | aspirational (5) | **Sensitivity analysis on chasm width** — output models at least 2 scenarios (optimistic / pessimistic) for chasm crossing, with different adoption velocities or champion counts. | Two named scenarios present; each scenario states a different adoption trajectory and the lever that changes it; a reader can compare the two to understand which factors most affect chasm width. |
| C-10 | correctness | aspirational (5) | **Feedback loop into signal readiness** — output concludes with an explicit statement of what adoption signals would indicate readiness to proceed (or not proceed) with the feature. | At least 2 measurable adoption signals stated (e.g., ">=3 early-majority teams active after month 2"); signals are concrete enough to track in a real team context. |
| C-11 | depth | aspirational (5) | **Named inertia per archetype** — output identifies the specific status-quo friction that each archetype must overcome, not generic "resistance to change." Distinct from C-03 bridging: inertia is per-archetype, not just at the chasm. | At least 3 archetypes have a named, feature-specific inertia statement (e.g., "early-majority: existing script library satisfies 80% of use cases today" not "may resist new tooling"); generic labels fail. |
| C-12 | format | aspirational (5) | **No orphan or conditional sections** — every criterion-mapped section is present and unconditional; no section is qualified with "if applicable," "if confident," "optional," or an equivalent hedge. | All 10 criteria (C-01 through C-10) have a corresponding output section that is explicitly present; output contains no conditional hedges on section inclusion; evaluator can locate evidence for each criterion without searching prose. |
| C-13 | depth | aspirational (5) | **Named inertia as downstream backbone** — the inertia entries introduced in C-11 are explicitly cited in at least 3 of the 4 downstream sections: chasm bridging (C-03), interventions (C-04), champion rationale (C-05), churn triggers (C-06). Inertia is not a standalone list; it is the causal anchor for the rest of the analysis. | At least 3 of {C-03, C-04, C-05, C-06} sections contain a direct, named reference to a specific inertia entry from C-11 (e.g., "the EM inertia 'existing script library covers 80% of cases' means the chasm bridge must demonstrate incremental — not replacement — value"); paraphrase without naming the inertia entry fails. |
| C-14 | correctness | aspirational (5) | **Champion rationale double-anchored** — each champion role's rationale connects to both (a) the champion's archetype position in Rogers model and (b) a specific named inertia held by the early-majority roles they bridge. Single-anchor rationale (archetype only, or inertia only) does not pass. | Each champion entry states the archetype position reason and names at least one EM inertia entry the champion is positioned to overcome; "well-placed to influence early-majority" without identifying which inertia fails C-14 even if C-05 passes. |
| C-15 | depth | aspirational (5) | **Churn mitigations are concrete actions, not surveillance** — every churn mitigation in C-06 names a concrete team action; no mitigation is phrased solely as a passive surveillance verb (monitor, track, watch, observe, measure). | Zero churn mitigations consist only of surveillance-only responses; each mitigation names at least one action the team takes (assign a champion, deliver hands-on training, remove a switching cost, bundle with existing workflow, etc.); a mitigation reading only "monitor usage telemetry" fails C-15 even if C-06 passes. |
| C-16 | correctness | aspirational (5) | **Self-audit pre-commit for aspirational criteria** — the output contains an explicit self-audit block that checks each of C-13, C-14, and C-15 before finalizing, catching semantically thin entries that fill structural slots without satisfying the pass condition. | Output contains a dedicated self-audit or verification block with at least one check per criterion among {C-13, C-14, C-15}; each check either confirms the specific pass condition (e.g., "C-13: inertia IDs I-03 and I-07 cited in chasm, interventions, and champion sections = 3 of 4") or flags a deficiency requiring correction; generic self-assessment ("I have reviewed my work") without criterion-specific verification fails; the audit block must appear before the final output is committed, not as a post-hoc reflection appended after completion. |
| C-17 | format | aspirational (5) | **Dedicated structural slot per aspirational criterion** — each of C-13, C-14, and C-15 has a separate, visually separable structural element (table column, section header, or numbered step) in the output; no two of the three criteria share a single structural element. | Each of C-13, C-14, and C-15 can be mapped by a reader to a distinct structural element without reading surrounding prose; a combined column or merged section intended to satisfy two or more of these criteria fails C-17; the three structural elements need not be co-located but must each be independently identifiable. |
| C-18 | correctness | aspirational (5) | **Revision obligation on self-audit deficiency** — when the self-audit (C-16) identifies a deficiency in any of C-13, C-14, or C-15, the output must contain evidence of correction before the artifact is committed; the audit block cannot proceed to commit with a flagged deficiency unresolved. | If the self-audit block flags any criterion among {C-13, C-14, C-15} as failing its pass condition, the output must show that the deficient section was revised before finalization — either the section is corrected or the self-audit block explicitly confirms the deficiency was resolved; an audit block that identifies a deficiency (e.g., "C-13: inertia cited in only 2 of 4 sections") and then commits the artifact without revision fails C-18; an audit block that confirms all three criteria pass satisfies C-18 trivially; C-18 fails automatically if C-16 fails. |
| C-19 | correctness | aspirational (5) | **Correction transaction content visible in output** — when C-18 requires a revision, the revised content itself must appear in the output, not merely a statement that revision occurred; a reader must be able to verify the correction satisfies the criterion's pass condition by reading the artifact, without trusting the model's self-report. | If the self-audit identifies a deficiency and C-18 is triggered, the output contains the revised structural content for each corrected criterion — the updated table row, corrected inertia citation, revised mitigation entry, or equivalent; a statement such as "the champion entry was updated" without showing the updated entry fails C-19; C-19 is trivially satisfied when C-18 is satisfied trivially (initial audit shows all-pass, no revision required); C-19 fails automatically if C-18 fails. Evaluator note: two formats satisfy C-19 — (a) inline CORRECTION BLOCK with BEFORE and AFTER content at the correction site, or (b) corrected content placed directly into the terminal section (C-20) cells, provided the cell content shows the full revised entry rather than a summary statement. Format (b) satisfies C-19 but fails C-21. |
| C-20 | format | aspirational (5) | **Single named terminal section consolidates gate states** — the output ends with a dedicated named section that records, for each of C-13, C-14, and C-15: the initial audit result, whether a revision was performed, and the final result; an evaluator verifying C-18 can go to this section alone without tracing the document. | A single named structural section (e.g., "Audit Summary," "Gate State Record," or equivalent) appears after all content sections; it lists initial result (PASS or FAIL), revision performed (yes/no), and final result for each of C-13, C-14, and C-15; if a revision was performed for any criterion, that fact is recorded; this section is distinct from the self-audit block required by C-16 (which performs the check — this section records the outcome); absence of the section or placement before the content sections fails C-20; C-20 fails automatically if C-16 fails. |
| C-21 | format | aspirational (5) | **Correction content not co-located with gate state** — when the self-audit requires revision (C-18 triggered), corrected content appears in inline correction blocks or section-local correction entries earlier in the document; it does not appear in the terminal gate state section (C-20). The terminal section contains only gate state records (initial result, revision performed, final result) and cross-references, not the revised structural content itself. | If any revision is performed: the terminal section (C-20) contains no revised table rows, corrected inertia citations, or revised mitigation entries; corrected content appears earlier in the document in a structurally distinct block; an evaluator reading only the terminal section sees gate records, not corrected content; C-21 is trivially satisfied when C-18 is trivially satisfied (initial audit all-pass, no revision required); C-21 fails automatically if C-20 fails. |
| C-22 | correctness | aspirational (5) | **Terminal section contains a self-verifying cross-reference invariant** — the terminal section (C-20) includes at least one claim whose truth can be verified by reading the rest of the document: the claim names a structural element type in the document, asserts a verifiable property about it, and can be confirmed or refuted without relying on the model's self-report. | The terminal section contains at least one statement of the form "for every [condition], a [structural element] with [property] exists at [location]" or equivalent; the claim must be falsifiable by inspection (an evaluator can check it against the document); a claim such as "all revisions were performed correctly" without naming a structural element or location fails C-22; C-22 fails automatically if C-20 fails. |
| C-23 | format | aspirational (5) | **Named verification boundary separates content from audit stage** — the output contains a named structural marker (section header, labeled divider, or equivalent label) that explicitly signals the transition from content generation to the verification/audit stage; content sections appear before this marker; the self-audit block (C-16) and terminal section (C-20) appear after. | A named structural element explicitly marking the start of the verification/audit stage is present and labeled (a heading such as "VERIFICATION STAGE," "AUDIT SECTION," or equivalent); content sections appear before this marker; the self-audit block and terminal section appear after; a horizontal rule, blank line, or unlabeled separator does not pass; a reader can determine by visual inspection which mode the output is in at any point in the document; C-23 fails automatically if C-16 fails. |
| C-24 | correctness | aspirational (5) | **Self-verifying invariant names its own falsification condition** — the self-verifying invariant required by C-22 must also state the condition that would falsify it, not only the condition that passes it. The pass condition and the falsification condition are distinct: stating both makes the invariant auditable from either direction and names the exact failure mode the evaluation is designed to detect. | The terminal section contains an invariant (C-22 pass condition met) that includes at least one explicit falsification condition — a statement of the form "the following would falsify this invariant: [condition]" or equivalent (e.g., "a 'Yes' row whose CORRECTION BLOCK Location points to a section containing no CORRECTION BLOCK falsifies this invariant"); a pass-condition-only invariant ("for every Yes-row, a CORRECTION BLOCK exists") without a stated falsification condition fails C-24; an evaluator can check the invariant by seeking the failure mode named, not only by seeking the pass condition; C-24 fails automatically if C-22 fails. |
| C-25 | format | aspirational (5) | **Named phase structure architecturally enforces Rogers adoption sequence** — the adoption timeline uses named phase headers (or equivalent named structural boundaries) that enforce Rogers ordering architecturally: the model cannot populate a later-phase row without completing the prior-phase header, and the chasm is represented as a named non-adoption phase between early-adopters and early-majority rather than as a prose note or blank gap. | The output contains named phase boundaries corresponding to Rogers archetypes (e.g., PHASE 1: INNOVATORS through PHASE N: LAGGARDS); at least one named phase or structural boundary explicitly represents the chasm as a non-adoption interstitial between early-adopters and early-majority; a correctly ordered prose timeline or table without named phase headers passes C-02 but fails C-25; a phase header must be a distinct structural element (heading, labeled row header, or equivalent), not inline labeling within a prose column; C-25 fails automatically if C-02 fails. |
```

---

**Elevation decisions recorded:**

Signal 1 not elevated — same logic as R6 Signal 4. It is the design technique by which C-21/C-22/C-23 are enforced in the structural contract, not a new output-observable property.

Signal 2 → **C-24**: The invariant's falsification condition is directly readable from the terminal section; an evaluator checks from both directions. Extends C-22 (invariant exists) with a new observable property (invariant also names failure mode).

Signal 3 → **C-25**: Named phase headers are directly visible in the output structure; a reader can verify at a glance whether Rogers ordering is structurally locked or merely instructed. Extends C-02 (sequence present) with a new observable property (structure makes inversion impossible).
