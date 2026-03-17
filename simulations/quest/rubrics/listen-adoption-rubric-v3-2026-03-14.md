Written to `simulations/quest/rubrics/listen-adoption-rubric-v3-2026-03-14.md`.

---

**What changed from v2:**

Three new aspirational criteria, each from a distinct R2 pattern:

**C-13 — Named inertia as downstream backbone** (5 pts)
Source: V-02 GATE C + V-04 interventions + V-04 churn reversion framing. C-11 can pass while C-13 fails — the list of inertia entries exists but nothing downstream cites them. C-13 tests whether named inertia propagates as a traceable anchor through at least 3 of {C-03, C-04, C-05, C-06}.

**C-14 — Champion rationale double-anchored** (5 pts)
Source: V-03, noted as "most explicit C-05 requirement across all variations." Current C-05 requires archetype-position rationale only. C-14 adds the second anchor: each champion entry must also name the specific EM inertia it is positioned to overcome. Single-anchor entries pass C-05 but fail C-14.

**C-15 — Churn mitigations are concrete actions, not surveillance** (5 pts)
Source: V-04 "no 'monitor adoption' mitigation accepted." Current C-06 passes with any named mitigation. C-15 disqualifies mitigations that consist only of surveillance verbs (monitor, track, watch, observe, measure). Mixed entries (action + measurement signal) pass.

**Max composite**: 110 → 125. Golden threshold (80) unchanged.
ty" without naming which EM inertia they overcome passes C-05 but fails C-14.

**C-15 -- Churn mitigations are actions, not surveillance** (5 pts, from V-04 C-06)
V-04 explicitly stated "no 'monitor adoption' mitigation accepted." C-06 passes today with any named mitigation, including passive surveillance responses. C-15 tightens the standard: every churn mitigation must name a concrete team action (assign a champion, deliver hands-on training, remove a switching cost, bundle the feature with an existing workflow) rather than a surveillance verb (monitor, track, watch, observe, measure). An output with all churn mitigations phrased as "monitor X for signs of churn" passes C-06 but fails C-15.

**Max composite**: 110 -> 125. Golden threshold (80) unchanged.

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

---

## Scoring Reference

| Outcome | Example composite |
|---------|-------------------|
| Perfect | All 5 essential + all 3 recommended + all 7 aspirational = 125 |
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

---

## Excellence Signals by Round

### R1 (source for C-11, C-12)

**C-11 source -- V-04 inertia framing**: The inertia-first variation named status-quo friction per archetype before discussing adoption. Scorecard noted this "forces bridging to explicitly fight named status-quo friction; improves C-03 specificity." The pattern generalised: any output that names archetype-level inertia produces sharper interventions (C-04) and more grounded champion rationale (C-05), even without the inertia-first prompt structure.

**C-12 source -- V-05 GATE checkpoint pattern**: V-05 scored 100/100 by mapping every rubric criterion to a mandatory, named output section with no conditional qualifiers. Scorecard noted: "GATE checkpoint pattern eliminates orphan criteria." V-01 lost 2 pts on C-09 because its Step 7 was qualified "if confident -- model can skip." C-12 rewards outputs that structurally include all sections unconditionally, regardless of prompt design.

### R2 (source for C-13, C-14, C-15)

**C-13 source -- V-02 GATE C + V-04 interventions and churn framing**: V-02 required "EM Named Inertia entries from SECTION A are cited" as a GATE condition for chasm bridging. V-04 required each intervention to "name a specific Named Inertia entry or friction from SECTION A or SECTION C" and framed churn triggers as "event that causes reversion to Named Inertia behavior." Both variations produced the same structural outcome: named inertia propagated through the entire analysis as a traceable anchor, not a standalone section. An output can pass C-11 (inertia list present) while failing C-13 (inertia not cited downstream), making C-13 a distinct test.

**C-14 source -- V-03 C-05 "most explicit requirement across all variations"**: V-03 required champion rationale to connect to "both the champion's archetype position AND the EM roles' named inertia." The scorecard noted V-03 had "the most explicit C-05 requirement across all variations." V-04 also connected champion rationale to EM inertia via its GATE C requirement. The pattern: a champion claim that names only archetype position leaves the inertia-fighting mechanism implicit; double-anchored rationale makes the bridge explicit and evaluable.

**C-15 source -- V-04 C-06 "no 'monitor adoption' mitigation accepted"**: V-04 explicitly blocked surveillance verbs as mitigations. V-02 similarly framed churn triggers as reversion events, implying the mitigation should interrupt that reversion rather than observe it. The pattern: "monitor" is not a mitigation -- it is a signal-watching activity that defers action. Real mitigations name what the team *does* when churn risk materialises. C-15 extracts this as an output-level criterion independent of prompt design.
