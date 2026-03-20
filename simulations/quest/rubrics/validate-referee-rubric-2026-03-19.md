Rubric written to `simulations/quest/rubrics/validate-referee-rubric-2026-03-19.md`.

**5 essential, 3 recommended, 2 aspirational.** Key design decisions:

- **C-01/C-03**: Structure completeness — the skill's value is entirely in the three-report + verdict format; partial output is not useful
- **C-02**: Archetype alignment is the core differentiator from generic review; a PNAS paper reviewed by phenomenologists is a correctness failure
- **C-04**: Specificity of concerns separates real simulation from vague hedging — the spec explicitly models this with examples like "effect size d = X is not reported"
- **C-05**: Artifact persistence is a first-class requirement (the skill's output contract)
- **C-06/C-07/C-08** (recommended): Depth of journal fidelity and differentiation — the skill works without these but is substantially weaker
- **C-09/C-10** (aspirational): Editorial dynamics knowledge and minority dissent — these raise the simulation from competent to genuinely useful for revision strategy
ecision (one of ACCEPT/MAJOR REVISION/MINOR REVISION/REJECT), confidence level, P1 blockers (reject conditions), P2 conditions (consensus issues), strongest referee with stated reason |
| C-04 | Major concerns are specific and citable | depth | Every major concern names a concrete gap, missing analysis, or logical flaw — not vague ("the paper needs more rigor") but targeted ("Effect size d is not reported in Table 2; practical significance cannot be assessed") |
| C-05 | Artifact written with required frontmatter | format | File exists at signals/validate/referee/{topic}-referee-{date}.md (or --output path); frontmatter includes: skill, topic, date, journal, verdict fields |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Journal-specific language enforced in at least one report | depth | At least one referee report uses vocabulary and standards specific to the target journal (e.g., PNAS: mentions effect sizes, p-values, N; JCS: mentions phenomenological grounding, first/third-person distinction; NeurIPS: mentions ablations, SOTA, reproducibility) |
| C-07 | Referee recommendations are differentiated | correctness | Not all three referees give identical recommendations — at least two distinct recommendation levels appear across the three reports (simulates real review variance) |
| C-08 | Phase 5 fixes ordered by blocking severity and mapped to P1/P2 | coverage | Three pre-submission fixes are listed, ordered from most blocking to least; Fix 1 addresses the P1 blocker; Fix 2 addresses the P2 consensus; Fix 3 addresses journal formatting or evidence standards |

---

## Aspirational Criteria (10 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Strongest referee rationale reflects journal editorial dynamics | depth | The "strongest referee" designation cites a reason grounded in how that journal's editorial process actually weights concerns (e.g., "Referee 2's statistical objections carry most weight at PNAS because editors routinely desk-reject on power analysis grounds") rather than a generic statement |
| C-10 | At least one referee takes a contrarian position | behavior | One referee's summary or major concerns visibly diverges from the other two in valence or emphasis — a genuine minority view is represented, not three paraphrases of the same critique |
