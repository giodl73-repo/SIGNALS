Reading the v5 rubric and the R5 scorecard carefully to identify what V-05's 12/12 achievement demonstrates beyond what C-18/C-19/C-20 already capture.

Three new patterns emerge from V-05's excellence:

1. **Phase 3 advocate gen-anchoring** — V-05's Advocate cites Phase 0 Gen-IDs in committed best readings, creating a Phase 0→Phase 3→Phase 4 chain. C-20 only requires the Phase 4 Gap field to cite Gen-IDs; the Phase 3 anchor is the new layer.

2. **Logician global binding with reclassification prohibition** — V-05's Logician names all downstream specialists and prohibits reclassification globally ("no subsequent specialist may reclassify logical structure"). C-19 requires named identity at each handoff; the global immutability constraint is the new pattern.

3. **CP audit three-way verdict** — V-05's Phase 4 CP audit uses CONFIRMED/DISCONFIRMED/CONFIRMED-ELSEWHERE. C-18 requires a per-step audit loop; the third category (fault exists but landed off the CP step) is the new structural precision.

---

```markdown
---
skill: simulate-argument
version: v6
date: 2026-03-19
pool: 15
golden_threshold: 96
---

# simulate-argument Rubric — v6

## v6 delta

**Three new aspirational criteria (C-21, C-22, C-23)** extracted from V-05's
12/12 achievement in R5 — the first perfect aspirational score across all rounds.

| ID | Pattern | Enforcement |
|----|---------|------------|
| C-21 | advocate-phase3-gen-anchoring | Phase 3 committed best readings cite Phase 0 Gen-IDs wherever a generalization is assumed. Creates a Phase 0 → Phase 3 → Phase 4 accountability chain. A best reading that implicitly assumes a generalization without citing its Gen-ID does not pass. |
| C-22 | logician-global-binding | Logician's closure names all downstream specialists (Advocate, Reviewer, Chair) and includes an explicit reclassification prohibition: "No subsequent specialist may reclassify logical structure." A handoff naming only the next specialist, or lacking a prohibition, does not pass. |
| C-23 | cp-audit-three-verdict | Phase 4 CP audit delivers a three-way verdict per step: CONFIRMED (P1 fault landed on this CP step), DISCONFIRMED (no fault; prediction was wrong), CONFIRMED-ELSEWHERE (fault exists but landed at a non-CP step). A binary YES/NO verdict does not pass — CONFIRMED-ELSEWHERE must be used where applicable. |

**Boundary cases:**
- C-21 is not a duplicate of C-20: C-20 requires the Fault Register Gap field to cite a Gen-ID anchor. C-21 requires the Advocate's Phase 3 committed best reading to cite the Gen-ID *before* a fault is even raised — the anchor must precede the Gap, not accompany it.
- C-22 is not a duplicate of C-19: C-19 requires named-specialist identity at each role boundary. C-22 requires the *first* specialist (Logician) to bind all subsequent ones in a single global commitment with explicit prohibition on reclassification. Identity at every boundary passes C-19; only the Logician's global-binding closure with a prohibition passes C-22.
- C-23 is not a duplicate of C-18: C-18 requires a per-CP-step accountability report (prediction + outcome). C-23 requires the outcome vocabulary to include a third category — CONFIRMED-ELSEWHERE — that distinguishes "fault caught elsewhere" from "fault absent." A report using only CONFIRMED/DISCONFIRMED passes C-18 but not C-23.

**Score formula:** `aspirational_pass / 15 * 10` (pool grows from 12 to 15).
Golden threshold unchanged.

---

## Criteria Summary

- **C-01--C-05** essential correctness/coverage
- **C-06--C-08** recommended depth/format
- **C-09** detects term drift pinpointed to a C-ID
- **C-10** ensures the P1/P2 fault is non-obvious and reviewer-worthy
- **C-11** *(R1)* falsification target in Phase 0 sharpens structural fault detection
- **C-12** *(R1)* inline reviewer hook inside every WEAK/BROKEN verdict
- **C-13** *(R1, tightened v3)* fault-pattern closure names a structural fault class, not a depth tier
- **C-14** *(R2)* enumerated Class column makes C-13 mechanical at insertion time
- **C-15** *(R2)* reviewer depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) with domain comparison per WEAK/BROKEN step
- **C-16** *(R3)* null-hypothesis binary verdict — H0 in Phase 0, mechanically derived reject/fail-to-reject at Phase 4 close
- **C-17** *(R3)* dedicated form-identification sub-pass before validity checks — pre-commitment, not post-hoc labeling
- **C-18** *(R4)* critical-path pre-commitment — Phase 0 names load-bearing steps; Phase 4 audits whether P1 faults landed on them
- **C-19** *(R4)* named specialist handoff — named role identities with closure language enforce temporal separation via identity
- **C-20** *(R4)* advocate-commitment gap accounts — Gap fields say "needed X, found only Y" relative to Phase 0 pre-committed generalizations
- **C-21** *(R5)* advocate phase 3 gen-anchoring — Phase 3 best readings cite Phase 0 Gen-IDs, creating Phase 0→Phase 3→Phase 4 chain
- **C-22** *(R5)* logician global binding — Logician's closure names all downstream specialists and prohibits reclassification globally
- **C-23** *(R5)* CP audit three-way verdict — CONFIRMED/DISCONFIRMED/CONFIRMED-ELSEWHERE per CP step; third category is required

---

## Essential Criteria (60 pts)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Claim map present and populated** | correctness | essential | Output contains a Claim Map table with at least 6 rows. Each row has a C-ID, claim text, and a valid type (premise / inference / empirical / definition / conclusion). |
| C-02 | **Dependency graph is complete** | correctness | essential | Every claim with type=inference lists at least one C-ID in Depends on. Every C-ID referenced as a dependency exists in the table. No dangling references. |
| C-03 | **Section coverage satisfied** | coverage | essential | At least one claim is drawn from each major section of the source paper. If the paper has N sections, at least N distinct sections are represented across all claims. |
| C-04 | **Every inference step is traced** | correctness | essential | For every claim with type=inference, a STEP block exists with: logical form (named or stated), all three validity checks answered (YES/WEAK/NO or YES/CITED/ASSUMED/UNSUPPORTED/YES/DRIFT), and a verdict of SOUND, WEAK, or BROKEN. |
| C-05 | **Fault register matches verdicts** | correctness | essential | Every claim whose STEP verdict is BROKEN or WEAK appears in the Fault Register with a non-empty Gap, Fix required, and Severity (P1/P2/P3). No BROKEN/WEAK steps are absent from the register. |

---

## Recommended Criteria (30 pts)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Logical forms are named, not just restated** | depth | recommended | Each STEP block names a logical structure (e.g., modus ponens, abduction, analogy, inductive generalization) rather than only writing "if X and Y then Z". At least 50% of inference steps have a named form. |
| C-07 | **AMEND section provides ordered, actionable fixes** | depth | recommended | AMEND contains exactly 3 fixes ordered P1 -> P2 -> P3. Each fix references the F-ID or C-ID it addresses and specifies what claim, evidence, or definition change would close the gap — not just "add more evidence." |
| C-08 | **Artifact written with complete frontmatter** | format | recommended | Output file contains YAML frontmatter with all six required fields: skill, topic, date, claims_mapped (integer), broken_steps (integer), p1_count (integer). Values are consistent with the body (claims_mapped equals the row count in the Claim Map table). |

---

## Aspirational Criteria (10 pts)

*Scored as aspirational_pass / 15 * 10. All fifteen criteria are equal weight.*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Term drift detected and pinpointed** | depth | aspirational | At least one validity check reports "DRIFT: [description]" and the AMEND section's P3 fix names the specific definition claim (C-ID) where drift originates and proposes a stable replacement wording. |
| C-10 | **Fault exposes a structural weakness reviewers would flag** | behavior | aspirational | At least one P1 or P2 fault identifies a gap that is non-obvious (not a missing citation on a trivially true premise) and that a domain reviewer would plausibly raise. The Gap field explains *why* the inference fails, not just *that* it fails. |
| C-11 | **Falsification target stated before tracing begins** | depth | aspirational | Phase 0 (or equivalent preamble) contains an explicit best-case statement of the argument — what it would look like if fully sound — so the trace has a concrete target to disprove rather than only a vague mandate to find faults. The statement is referenced or refuted in at least one fault in the register. |
| C-12 | **Inline reviewer hook present on every WEAK/BROKEN verdict** | behavior | aspirational | Every STEP block whose verdict is WEAK or BROKEN includes a parenthetical or tagged line asking "Would a domain reviewer flag this?" with a YES/NO answer and one-sentence justification. The hook is inside the STEP block, not added retroactively in AMEND. |
| C-13 | **Fault pattern synthesized against Phase 0 at close** | depth | aspirational | Phase 4 (Fault Register) or a closing synthesis section explicitly asks whether the accumulated fault pattern confirms or refutes the Phase 0 best-case statement. The answer names the dominant fault class using structural vocabulary (e.g., definitional drift, unsupported generalization, circular dependency, invalid logical form). Naming only a depth tier (OBVIOUS/NOTABLE/SIGNIFICANT) or confirming Phase 0 without a class name does not pass. |
| C-14 | **Fault class taxonomy column in Fault Register** | depth | aspirational | The Fault Register contains a `Class` column. Every row carries exactly one of four codes: DEF-DRIFT / UNSUPPORTED-GEN / CIRCULAR-DEP / INVALID-FORM. Phase 4 closing identifies the dominant fault class by citing the most frequent code in the column — no post-hoc invented label required. |
| C-15 | **Reviewer depth tier annotated per WEAK/BROKEN step** | behavior | aspirational | Every STEP block whose verdict is WEAK or BROKEN includes a reviewer depth classification (OBVIOUS / NOTABLE / SIGNIFICANT) with a one-sentence domain comparison explaining why a specialist would rate the gap at that tier. The tier tag also appears in the Fault Register Gap field for the corresponding fault. |
| C-16 | **Null-hypothesis binary verdict at Phase 4 close** | depth | aspirational | Phase 0 states an explicit null hypothesis of the form "This argument is structurally sound and requires no revision" (or equivalent). Phase 4 closing delivers a binary verdict mechanically derived from fault counts: at least one P1 fault → "H0 is rejected"; zero P1 faults → "H0 is not rejected". The closing also states an inertia defensibility conclusion ("Inertia is [defensible/not defensible]"). A prose judgment that reaches the same conclusion without deriving it from counts does not pass. |
| C-17 | **Dedicated form-identification sub-pass before validity checks** | depth | aspirational | Phase 3 opens with a Logician sub-pass (3A) that names the logical form of every inference step before the Empirical Reviewer's validity checks (3B) begin. Named role handoff with a closure statement at the boundary. A single pass that interleaves form identification and validity checking does not pass. |
| C-18 | **Critical-path priority audit loop** | depth | aspirational | Phase 0 identifies 2–3 steps as critical-path (CP) by structural argument (load-bearing, high fan-in, or no redundant path). Phase 4 closing iterates per CP-flagged step: states the pre-committed prediction, reports the fault outcome, and gives an accountability verdict. The audit loop between structural priority and fault severity is the pass condition — a binary "CP intersection: YES/NO" verdict does not pass. |
| C-19 | **Named specialist handoff with identity closure** | behavior | aspirational | Each role boundary (Logician → Reviewer, Reviewer → Chair, etc.) carries a first-person closure statement from the outgoing specialist: "I, [Role], commit the above [outputs]." The incoming specialist is named and bound to those outputs. Anonymous closure language ("The Logician's pass is closed") or section labels alone do not pass — identity is the enforcement mechanism. |
| C-20 | **Advocate-commitment gap accounts** | depth | aspirational | Every UNSUPPORTED-GEN fault's Gap field cites a Phase 0 Gen-ID: "Needed [Gen-N: exact pre-committed generalization], found only [Y]." The Phase 0 Gen-registry must exist for this to be possible. An assertion-only gap ("no empirical support") or a gap citing a Phase 3 Advocate assumption rather than a Phase 0 Gen-ID does not pass. |
| C-21 | **Advocate Phase 3 gen-anchoring** | depth | aspirational | In Phase 3, the Advocate's committed best reading cites the relevant Phase 0 Gen-ID inline ("Gen-ID reference: [Gen-NN]") wherever a pre-committed generalization is being assumed. This creates a Phase 0 → Phase 3 → Phase 4 accountability chain. A best reading that implicitly assumes a generalization without citing its Gen-ID does not pass; citing a Gen-ID only in the Fault Register Gap (C-20) does not satisfy C-21. |
| C-22 | **Logician global binding with reclassification prohibition** | behavior | aspirational | The Logician's form-identification closure (end of Phase 3A) names all downstream specialists — Advocate, Empirical Reviewer, and Committee Chair — and includes an explicit reclassification prohibition: "No subsequent specialist may reclassify logical structure" or equivalent. A handoff that names only the next specialist, or that omits the prohibition, does not pass. Identity at every boundary satisfies C-19 but not C-22. |
| C-23 | **CP audit three-way verdict** | depth | aspirational | The Phase 4 CP audit delivers a three-way verdict per CP step: CONFIRMED (P1 fault landed on this step), DISCONFIRMED (no fault; the prediction was falsified), CONFIRMED-ELSEWHERE (a fault exists but landed at a non-CP step). The CONFIRMED-ELSEWHERE category must be used where applicable and explained — it distinguishes structural detection from structural absence. A report using only binary YES/NO or CONFIRMED/DISCONFIRMED passes C-18 but not C-23. |

---

## Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 15 * 10)

golden = composite >= 96
```

## Round History

| Round | Top Score | New Criteria | Pool |
|-------|-----------|-------------|------|
| R1 | — | C-11, C-12, C-13 | 9 |
| R2 | — | C-14, C-15 | — |
| R3 | — | C-16, C-17 | — |
| R4 | — | C-18, C-19, C-20 | 12 |
| R5 | 100 (V-05, first 12/12) | C-21, C-22, C-23 | 15 |
```
