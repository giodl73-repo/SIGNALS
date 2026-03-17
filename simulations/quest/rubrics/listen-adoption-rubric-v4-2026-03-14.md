Written to `simulations/quest/rubrics/listen-adoption-rubric-v4-2026-03-14.md`.

---

**What changed from v3:**

Two new aspirational criteria from R3 patterns 2 and 4 (patterns 1 and 3 were already captured by C-13 and C-15):

**C-16 -- Self-audit pre-commit for aspirational criteria** (5 pts)
Source: V-05 SA-1/SA-2/SA-3 pattern. The scorecard finding was that structural slots can be filled while content stays semantically thin -- an inertia ID cited in a sentence that never actually names the entry. C-16 requires an explicit, criterion-specific audit block (naming C-13, C-14, C-15 individually) before the output is finalized. Generic "I reviewed my work" fails; "C-13: IDs I-03 and I-07 cited in 3 of 4 sections" passes. C-16 fails automatically if C-13/C-14/C-15 all fail.

**C-17 -- Dedicated structural slot per aspirational criterion** (5 pts)
Source: R3 structural independence finding. V-02 used a 4-column champion table for C-14 but left C-15 in an unstructured column; V-03 did the reverse. Each exposed the other. C-17 requires C-13, C-14, and C-15 to each have a visually separable, independently identifiable structural element. A single shared column or merged section that partially covers two criteria fails even if both underlying criteria pass.

**Max composite: 125 → 135. Golden threshold (80) unchanged.**
separate, visually separable structural element in the output. A combined "Inertia + Champion + Churn" column fails C-17 even if all three criteria pass their individual checks.

**Max composite**: 125 -> 135. Golden threshold (80) unchanged.

---

## Criteria Table

### Essential (must all pass)

| ID | Category | Weight | Criterion | Pass Condition |
|----|----------|--------|-----------|----------------|
| C-01 | correctness | essential (12) | **All 16 stock roles mapped to Rogers archetype** -- output assigns every named persona in the skill contract to one of the five canonical Rogers archetypes (innovators, early-adopters, early-majority, late-majority, laggards). | Output contains a mapping table or list covering all 16 named roles; each role maps to exactly one of the five canonical archetype labels; no role is omitted or duplicated. |
| C-02 | correctness | essential (12) | **Month-by-month adoption sequence** -- output includes a timeline (>=3 months) showing which archetypes / roles adopt in each period, with explicit ordering (who tries first, who follows). | At least 3 distinct time steps are present; innovators and early-adopters appear before early-majority; late-majority before laggards; no inversion of Rogers sequence. |
| C-03 | correctness | essential (12) | **Chasm identification** -- output explicitly names the chasm between early-adopters and early-majority and states what bridging mechanism (or gap risk) applies to this feature. | The word "chasm" (or equivalent: "crossing the chasm", "adoption gap") appears; at least one concrete bridging mechanism or gap risk is stated, tied to this feature's specifics rather than generic advice. |
| C-04 | coverage | essential (12) | **Intervention recommendations ranked by adoption delta** -- output provides >=2 ranked interventions with an estimated adoption delta (quantified or directional: high/medium/low). | At least 2 interventions listed; each has a stated adoption delta (numeric % or H/M/L label); list is in descending delta order or explicitly marked as ranked. |
| C-05 | correctness | essential (12) | **Champion network named** -- output identifies which roles/archetypes form the champion network (the social bridge across the chasm). | At least 2 specific roles or archetype groups are named as champions; the rationale connects their archetype position to why they can bridge into early-majority. |

---

### Recommended (raise quality)

| ID | Category | Weight | Criterion | Pass Condition |
|----|----------|--------|-----------|----------------|
| C-06 | depth | recommended (10) | **Churn risk per archetype** -- output identifies churn risk for at least 2 archetypes, explaining what triggers churn for each. | Churn risks stated for >=2 archetypes; each risk entry names a trigger (not just "may churn") and at least one mitigation or warning signal. |
| C-07 | depth | recommended (10) | **Spread mechanism named per transition** -- for each archetype-to-archetype adoption transition, the output states the spread mechanism (word-of-mouth, demo, mandate, tooling integration, etc.). | Each major transition in the timeline is annotated with a spread mechanism label; generic "word of mouth" alone does not pass -- at least one transition must cite a feature-specific or role-specific mechanism. |
| C-08 | format | recommended (10) | **Tabular or structured month view** -- the month-by-month timeline is presented in a table, numbered list, or clearly structured format (not buried in prose). | Timeline is rendered as a table, structured list, or clearly labeled month headers; a reader can scan to any month and identify adopters without reading surrounding prose. |

---

### Aspirational (raise the bar)

| ID | Category | Weight | Criterion | Pass Condition |
|----|----------|--------|-----------|----------------|
| C-09 | depth | aspirational (5) | **Sensitivity analysis on chasm width** -- output models at least 2 scenarios (optimistic / pessimistic) for chasm crossing, with different adoption velocities or champion counts. | Two named scenarios present; each scenario states a different adoption trajectory and the lever that changes it; a reader can compare the two to understand which factors most affect chasm width. |
| C-10 | correctness | aspirational (5) | **Feedback loop into signal readiness** -- output concludes with an explicit statement of what adoption signals would indicate readiness to proceed (or not proceed) with the feature. | At least 2 measurable adoption signals stated (e.g., ">=3 early-majority teams active after month 2"); signals are concrete enough to track in a real team context. |
| C-11 | depth | aspirational (5) | **Named inertia per archetype** -- output identifies the specific status-quo friction that each archetype must overcome, not generic "resistance to change." Distinct from C-03 bridging: inertia is per-archetype, not just at the chasm. | At least 3 archetypes have a named, feature-specific inertia statement (e.g., "early-majority: existing script library satisfies 80% of use cases today" not "may resist new tooling"); generic labels fail. |
| C-12 | format | aspirational (5) | **No orphan or conditional sections** -- every criterion-mapped section is present and unconditional; no section is qualified with "if applicable," "if confident," "optional," or an equivalent hedge. | All 10 criteria (C-01 through C-10) have a corresponding output section that is explicitly present; output contains no conditional hedges on section inclusion; evaluator can locate evidence for each criterion without searching prose. |
| C-13 | depth | aspirational (5) | **Named inertia as downstream backbone** -- the inertia entries introduced in C-11 are explicitly cited in at least 3 of the 4 downstream sections: chasm bridging (C-03), interventions (C-04), champion rationale (C-05), churn triggers (C-06). Inertia is not a standalone list; it is the causal anchor for the rest of the analysis. | At least 3 of {C-03, C-04, C-05, C-06} sections contain a direct, named reference to a specific inertia entry from C-11 (e.g., "the EM inertia 'existing script library covers 80% of cases' means the chasm bridge must demonstrate incremental -- not replacement -- value"); paraphrase without naming the inertia entry fails. |
| C-14 | correctness | aspirational (5) | **Champion rationale double-anchored** -- each champion role's rationale connects to both (a) the champion's archetype position in Rogers model and (b) a specific named inertia held by the early-majority roles they bridge. Single-anchor rationale (archetype only, or inertia only) does not pass. | Each champion entry states the archetype position reason and names at least one EM inertia entry the champion is positioned to overcome; "well-placed to influence early-majority" without identifying which inertia fails C-14 even if C-05 passes. |
| C-15 | depth | aspirational (5) | **Churn mitigations are concrete actions, not surveillance** -- every churn mitigation in C-06 names a concrete team action; no mitigation is phrased solely as a passive surveillance verb (monitor, track, watch, observe, measure). | Zero churn mitigations consist only of surveillance-only responses; each mitigation names at least one action the team takes (assign a champion, deliver hands-on training, remove a switching cost, bundle with existing workflow, etc.); a mitigation reading only "monitor usage telemetry" fails C-15 even if C-06 passes. |
| C-16 | correctness | aspirational (5) | **Self-audit pre-commit for aspirational criteria** -- the output contains an explicit self-audit block that checks each of C-13, C-14, and C-15 before finalizing, catching semantically thin entries that fill structural slots without satisfying the pass condition. | Output contains a dedicated self-audit or verification block with at least one check per criterion among {C-13, C-14, C-15}; each check either confirms the specific pass condition (e.g., "C-13: inertia IDs I-03 and I-07 cited in chasm, interventions, and champion sections = 3 of 4") or flags a deficiency requiring correction; generic self-assessment ("I have reviewed my work") without criterion-specific verification fails; the audit block must appear before the final output is committed, not as a post-hoc reflection appended after completion. |
| C-17 | format | aspirational (5) | **Dedicated structural slot per aspirational criterion** -- each of C-13, C-14, and C-15 has a separate, visually separable structural element (table column, section header, or numbered step) in the output; no two of the three criteria share a single structural element. | Each of C-13, C-14, and C-15 can be mapped by a reader to a distinct structural element without reading surrounding prose; a combined column or merged section intended to satisfy two or more of these criteria fails C-17; the three structural elements need not be co-located but must each be independently identifiable. |

---

## Scoring Reference

| Outcome | Example composite |
|---------|-------------------|
| Perfect | All 5 essential + all 3 recommended + all 9 aspirational = 135 |
| Golden | All 5 essential pass + composite >= 80 (e.g., 60 + 30 + 0 = 90) |
| Pass | All 5 essential pass + 2/3 recommended = 60 + 20 = 80 |
| Near-miss | All essential pass + 1/3 recommended = 60 + 10 = 70 (below threshold) |
| Fail | Any essential fails = automatic fail regardless of composite |

---

## Notes for Evaluators

- **C-01**: "Stock roles" means the 16 named personas in the skill contract. If the output uses generic archetype labels without mapping specific roles, C-01 fails.
- **C-03**: Bridging mechanism must be feature-specific. Saying "find champions" without connecting to this feature's adoption context does not pass.
- **C-04**: "Adoption delta" may be stated as % increase in adoption rate or as H/M/L if the output explains what H/M/L means in context. Unranked lists fail C-04.
- **C-09**: Scenarios must differ on a named lever (not just "things go well / badly").
- **C-11**: Inertia is per-archetype and pre-chasm, not the same as C-03's chasm bridging mechanism. A good C-11 names what each archetype is already doing that the feature must displace. If the output only names chasm-level friction (one statement for the EA->EM gap), C-11 fails even if C-03 passes.
- **C-12**: Phrases that fail C-12: "if you have enough data, include sensitivity analysis," "optional: signal readiness section," "Step 7 (if confident)." An output that structurally includes every section -- even briefly -- passes C-12. An output that omits any criterion-mapped section or marks it optional fails.
- **C-13**: The test is explicit citation, not implicit connection. Evaluator must be able to point to the specific inertia entry being referenced in each downstream section. If C-11 passes but none of {C-03, C-04, C-05, C-06} name an inertia entry, C-13 fails. C-13 also fails automatically if C-11 fails (no named inertia exists to cite).
- **C-14**: Double-anchor means two distinct claims per champion entry, not a single sentence conflating both. "Senior Dev is an early-adopter who can speak to EM teams [archetype position] because those teams are blocked by the existing script library coverage gap [named EM inertia]" passes. "Senior Dev is influential and understands early-majority concerns" fails -- no inertia named.
- **C-15**: Mitigations that mix action with surveillance can pass. "Assign an onboarding champion to each EM team and watch for reduced session length as a success signal" passes because the concrete action is present. The evaluator checks whether a team action exists, not whether measurement language is absent. A mitigation that is *only* a surveillance verb fails.
- **C-16**: The self-audit must be criterion-specific to pass. An audit block that reads "I verified the champion section has two anchors, checked that all churn mitigations include a team action, and confirmed inertia IDs appear in 3 of 4 downstream sections" passes. "I reviewed all sections for completeness" does not. The audit block may appear as a labeled step, a pre-commit checklist, or an inline GATE checkpoint -- format is not prescribed, but each of C-13/C-14/C-15 must be explicitly named or described. C-16 fails automatically if C-13, C-14, and C-15 all fail (nothing to audit).
- **C-17**: Evaluate by attempting to locate the structural element that addresses each of C-13, C-14, and C-15 independently. If a single table column is cited as evidence for two of these criteria, C-17 fails even if both underlying criteria pass. The intent is that structural independence prevents the failure mode where tightening one criterion loosens an adjacent one.

---

## Excellence Signals by Round

### R1 (source for C-11, C-12)

**C-11 source -- V-04 inertia framing**: The inertia-first variation named status-quo friction per archetype before discussing adoption. Scorecard noted this "forces bridging to explicitly fight named status-quo friction; improves C-03 specificity." The pattern generalised: any output that names archetype-level inertia produces sharper interventions (C-04) and more grounded champion rationale (C-05), even without the inertia-first prompt structure.

**C-12 source -- V-05 GATE checkpoint pattern**: V-05 scored 100/100 by mapping every rubric criterion to a mandatory, named output section with no conditional qualifiers. Scorecard noted: "GATE checkpoint pattern eliminates orphan criteria." V-01 lost 2 pts on C-09 because its Step 7 was qualified "if confident -- model can skip." C-12 rewards outputs that structurally include all sections unconditionally, regardless of prompt design.

### R2 (source for C-13, C-14, C-15)

**C-13 source -- V-02 GATE C + V-04 interventions and churn framing**: V-02 required "EM Named Inertia entries from SECTION A are cited" as a GATE condition for chasm bridging. V-04 required each intervention to "name a specific Named Inertia entry or friction from SECTION A or SECTION C" and framed churn triggers as "event that causes reversion to Named Inertia behavior." Both variations produced the same structural outcome: named inertia propagated through the entire analysis as a traceable anchor, not a standalone section. An output can pass C-11 (inertia list present) while failing C-13 (inertia not cited downstream), making C-13 a distinct test.

**C-14 source -- V-03 C-05 "most explicit requirement across all variations"**: V-03 required champion rationale to connect to "both the champion's archetype position AND the EM roles' named inertia." The scorecard noted V-03 had "the most explicit C-05 requirement across all variations." V-04 also connected champion rationale to EM inertia via its GATE C requirement. The pattern: a champion claim that names only archetype position leaves the inertia-fighting mechanism implicit; double-anchored rationale makes the bridge explicit and evaluable.

**C-15 source -- V-04 C-06 "no 'monitor adoption' mitigation accepted"**: V-04 explicitly blocked surveillance verbs as mitigations. V-02 similarly framed churn triggers as reversion events, implying the mitigation should interrupt that reversion rather than observe it. The pattern: "monitor" is not a mitigation -- it is a signal-watching activity that defers action. Real mitigations name what the team *does* when churn risk materialises. C-15 extracts this as an output-level criterion independent of prompt design.

### R3 (source for C-16, C-17)

**C-16 source -- V-05 GATE + self-audit (SA-1/SA-2/SA-3)**: V-05 and V-04 both hit 125; V-05 uniquely added a self-audit pre-commit step. The scorecard finding: "SA-1/SA-2/SA-3 catches semantically thin entries that fill structural slots correctly but loosely." C-13/C-14/C-15 each have a structural pass condition, but a model can satisfy the structure while writing content too thin to be useful (e.g., an inertia ID appears in a downstream section inside a sentence like "considering relevant inertia factors"). The self-audit pattern surfaces this failure mode before it propagates. C-16 lifts this from a prompt technique into an output-level requirement: the output should demonstrate self-verification, not assume structural completeness implies semantic completeness.

**C-17 source -- R3 pattern "each new criterion needs its own dedicated structural slot"**: V-02 solved C-14 with a 4-column champion table but left C-15 unstructured, exposing the adjacent criterion. V-03 enforced C-15 with a mandatory action-verb column but used a 3-column champion table, exposing C-14. The failure mode is systematic: when two criteria share a single structural element, tightening one leaves the other unguarded. An output that addresses C-14 and C-15 through a single combined "Champion / Mitigation" column cannot reliably satisfy both. C-17 requires structural independence: a reader must be able to point to distinct elements for each of the three aspirational criteria without cross-referencing surrounding prose.
