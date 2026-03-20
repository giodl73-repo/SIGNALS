```markdown
---
skill: simulate-argument
version: v7
date: 2026-03-19
pool: 18
golden_threshold: 96
---

# simulate-argument Rubric — v7

## v7 delta

**Three new aspirational criteria (C-24, C-25, C-26)** extracted from R6 excellence
signals — the first round where all five variations achieved golden and three
reached 15/15 aspirational.

| ID | Pattern | Enforcement |
|----|---------|------------|
| C-24 | advocate-form-independent-gen-anchoring | The Advocate's Gen-ID anchor trigger fires on the *semantic content* of the best reading — whether the assumption extends beyond the studied population — not on the Logician's form label. A two-field check is required: `Generalization assumed: YES/NO` followed by `Gen-ID anchor`. A best reading that cites a Gen-ID only when the Logician labeled the step "inductive generalization" does not pass — causal inference and analogy steps that assume universal mechanism applicability must also trigger the anchor. |
| C-25 | logician-cross-phase-immutability | The Logician's reclassification prohibition extends across phases, not only specialists. The Logician's closure must explicitly state that no subsequent *phase* may reclassify logical structure. Phase 4 verdicts of INVALID-FORM must derive from the Phase 3A committed form; re-examination of form assignment at Phase 4 is structurally prohibited. A closure that names specialists but does not extend the prohibition to phases does not pass. |
| C-26 | cp-audit-forced-adjacency-search | Before DISCONFIRMED may be written in the Phase 4 CP audit, the analyst must complete and document a Step 2 adjacency search — identifying which non-CP step the fault landed on (or confirming none). DISCONFIRMED is an active documented conclusion, not a passive absence of evidence. A CP audit that writes DISCONFIRMED without documenting the adjacency search does not pass. |

**Boundary cases:**
- C-24 is not a duplicate of C-21: C-21 requires Phase 3 best readings to cite Phase 0 Gen-IDs. C-24 requires the *trigger* to be content-conditional — decoupled from the Logician's form vocabulary. A best reading that cites Gen-ID only when the Logician labeled the step "inductive generalization" passes C-21 but fails C-24.
- C-25 is not a duplicate of C-22: C-22 requires the Logician's closure to name all downstream specialists and prohibit reclassification globally. C-25 requires that prohibition to extend explicitly to phases, and Phase 4 to derive INVALID-FORM exclusively from the Phase 3A committed form. A global specialist-binding closure without phase-level extension passes C-22 but not C-25.
- C-26 is not a duplicate of C-23: C-23 requires the outcome vocabulary to include CONFIRMED-ELSEWHERE as a distinct category. C-26 requires DISCONFIRMED to be written only after a documented adjacency search. A CP audit using all three verdict categories passes C-23 but not C-26 unless the adjacency search is explicitly documented before each DISCONFIRMED verdict.

**Score formula:** `aspirational_pass / 18 * 10` (pool grows from 15 to 18).
Golden threshold unchanged at 96.

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
- **C-24** *(R6)* advocate form-independent gen-anchoring — Gen-ID anchor trigger fires on content of best reading, not Logician's form label; two-field check required
- **C-25** *(R6)* logician cross-phase immutability — reclassification prohibition extends to phases; Phase 4 INVALID-FORM derives from Phase 3A committed form only
- **C-26** *(R6)* CP audit forced adjacency search — DISCONFIRMED requires documented Step 2 adjacency search; passive omission does not pass

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
| C-06 | **Logical form vocabulary** | depth | recommended | Logician names form from an enumerated vocabulary (modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism, argument from analogy, inductive generalization, inference to the best explanation, causal inference, etc.) in each FORM block. Ad-hoc or post-hoc labels do not pass. |
| C-07 | **Phase 5 repair instructions** | format | recommended | Phase 5 repair plan orders faults P1→P2→P3, references F-ID, C-ID, and Class for each, and provides exact repair instructions sufficient to re-run Phase 3. |
| C-08 | **Frontmatter complete** | format | recommended | All six frontmatter fields present and populated: skill, topic, date, claims_mapped, broken_steps, p1_count. |

---

## Aspirational Criteria (10 pts)

Pool = 18. Score = `aspirational_pass / 18 * 10`.

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-09 | **Term-drift detection** | DRIFT check in 3B-CRITIC names the term, originating C-ID, and shift in meaning. AMEND P3 DEF-DRIFT in the Fault Register names the originating C-ID and proposes stable replacement wording. |
| C-10 | **Non-obvious P1 fault** | The primary fault (highest-severity BROKEN step) targets a structural gap that a domain-literate reviewer would flag in written review — not an obvious logical slip. The Fault Register entry demonstrates this with a domain comparison. |
| C-11 | **Phase 0 falsification target** | Phase 0 includes a pre-committed falsification target: a condition under which the argument's central claim would be falsified. Phase 4 returns to this target and delivers a binary verdict (falsified / not falsified). |
| C-12 | **Inline reviewer hook** | Every WEAK or BROKEN VERDICT block contains a first-person reviewer hook: "As committee chair, would I flag this in a written review? YES/NO" with a one-sentence rationale. |
| C-13 | **Fault-pattern closure** | Phase 4 closing step 1 names the dominant fault class by structural code (UNSUPPORTED-GEN, DEF-DRIFT, SCOPE-OVERREACH, CAUSAL-LEAP, etc.) — not a depth tier (NOTABLE, SIGNIFICANT). |
| C-14 | **Enumerated Class column** | Fault Register includes a Class column with an enumerated code per entry. Phase 4 step 1 counts per code and names the dominant class mechanically from those counts. |
| C-15 | **Reviewer depth tier** | Chair assigns a depth tier (OBVIOUS / NOTABLE / SIGNIFICANT) with a domain comparison per WEAK or BROKEN step. |
| C-16 | **Null-hypothesis binary verdict** | Phase 0 states an explicit H0. Phase 4 step 2 derives a count-based binary verdict (reject H0 / fail to reject H0). Phase 4 step 3 pairs H0 verdict with inertia verdict. |
| C-17 | **Form-identification sub-pass** | Logician (3A) completes a dedicated form-identification pass before any validity checks begin. Form label is a pre-commitment — not post-hoc labeling after validity is assessed. |
| C-18 | **Critical-path pre-commitment** | Phase 0 names load-bearing CP steps. Phase 4 closing step 4 audits each CP step: prediction + trace outcome + verdict (CONFIRMED / DISCONFIRMED / CONFIRMED-ELSEWHERE) + "Structural risk distribution" sentence. |
| C-19 | **Named specialist handoff** | All four specialists (Logician, Advocate, Reviewer, Chair) make first-person identity commitments with closure language at each role boundary. Logician's closure names all three subsequent specialists simultaneously. |
| C-20 | **Advocate-commitment gap accounts** | Gen-registry in Phase 0. Advocate's "Gen-ID anchor" field commits the Phase 0 Gen-ID in the best reading before any fault is raised. UNSUPPORTED-GEN Gap template cites the Gen-ID. Phase 4 step 5 delivers a generalization accountability verdict per Gen-ID. |
| C-21 | **Advocate phase 3 gen-anchoring** | Phase 3 committed best readings cite Phase 0 Gen-IDs wherever a generalization is assumed. Creates a Phase 0→Phase 3→Phase 4 accountability chain. A best reading that implicitly assumes a generalization without citing its Gen-ID does not pass. |
| C-22 | **Logician global binding** | Logician's closure names all downstream specialists (Advocate, Reviewer, Chair) and includes an explicit reclassification prohibition: "No subsequent specialist may reclassify logical structure." A handoff naming only the next specialist, or lacking a prohibition, does not pass. |
| C-23 | **CP audit three-way verdict** | Phase 4 CP audit delivers a three-way verdict per step: CONFIRMED (P1 fault landed on this CP step), DISCONFIRMED (no fault; prediction was wrong), CONFIRMED-ELSEWHERE (fault exists but landed at a non-CP step). A binary YES/NO verdict does not pass — CONFIRMED-ELSEWHERE must be used where applicable. |
| C-24 | **Advocate form-independent gen-anchoring** | The Advocate block implements a content-conditional trigger: `Generalization assumed: YES/NO` scans whether the assumption extends beyond the studied population, independent of the Logician's form label. `Gen-ID anchor` follows when YES. Advocate closure attests that every best reading was scanned by content, not by form label. A trigger that fires only on "inductive generalization" form labels does not pass. |
| C-25 | **Logician cross-phase immutability** | The Logician's closure explicitly extends the reclassification prohibition to phases: "No subsequent phase may reclassify logical structure." Phase 4 must derive any INVALID-FORM verdict exclusively from the Phase 3A committed form. A closure with specialist-level prohibition but no phase-level extension does not pass. |
| C-26 | **CP audit forced adjacency search** | DISCONFIRMED in the Phase 4 CP audit requires a documented Step 2 adjacency search: which non-CP step did the fault land on, or a documented confirmation that no adjacent step absorbed it. DISCONFIRMED written without a documented adjacency search does not pass — passive absence of evidence is insufficient. |
```
