Looking at Round 18, the differentiators are:

**A-27 (Failure Mode Annotation):** V-05 uniquely passes (5 pts) by naming the CI formula failure mode *within* Step S.1. V-01–V-04 get PARTIAL (3 pts) — structural enforcement present, no failure mode annotation for the CI formula constraint.

**A-29 (CI Formula Present):** V-03/V-04/V-05 pass via derivation-phase enforcement (formula required at generation time); V-01 passes via output-format structure (formula required at inspection time); V-02 gets PARTIAL (weakest template-gap enforcement).

Two new criteria:

- **A-30** — derivation-phase protocol (process-level enforcement, not just output-format)
- **A-31** — CI formula failure mode named at the point of constraint (A-27 applied co-located, parallel to A-25)

---

```markdown
# review-customers Rubric — v17

**v17 written.** Two new criteria extracted from Round 18 excellence signals:

---

**A-30 — CI formula requirement enforced by derivation-phase protocol (generation-time
enforcement)** (depth, 5 pts)

Source: V-03/V-04/V-05 Round 18 A-29 differentiator. V-03 earns the PASS citation "the
formula is required at generation time, not only at output-inspection time" — the derivation
phase (D.1 state formula → D.2 compute SD → D.3 apply → D.4 report) makes formula omission
structurally detectable before output inspection. V-01's two-part labeled output structure
(A-29 pass) requires the formula to be present in the output but does not require it to be
computed first; an evaluator could satisfy the V-01 format by adding the parenthetical after
the fact. Process-level enforcement is more fundamental: the formula is an input to the
computation, not a decoration on the output. V-04 confirms the principle: dual enforcement
(output-level + derivation-phase) makes compliance verifiable at two independent levels.
Pass condition: the protocol contains a derivation phase with formula statement as an
explicit required step prior to computation; an output-format instruction that requires the
formula only at reporting (A-29) does not satisfy A-30.

---

**A-31 — CI formula failure mode named at the point of constraint** (depth, 5 pts)

Source: V-05 Round 18 A-27 differentiator. V-05 uniquely achieves full A-27 compliance by
naming the specific failure mode for the CI formula constraint within Step S.1 itself:
"Without the formula parenthetical (±1.96·[SD_value]/√12) alongside the interval, the CI
annotation cannot be verified against different score inputs — a reader cannot confirm
whether the interval was computed as ±1.96·SD/√12 or via a different method." V-01–V-04
have structural enforcement but do not name this failure mode, yielding PARTIAL on A-27.
The pattern directly parallels A-25: just as A-25 requires the UX-before-PM rationale to be
stated within the ordering instruction (not separately), A-31 requires the CI formula failure
mode to be co-located with the formula constraint instruction. Co-location prevents the
failure mode from being understood only by cross-referencing a separate rationale section —
a reader following the constraint instruction encounters both the rule and its epistemic
grounding in a single pass. Pass condition: the CI formula constraint instruction (whether
derivation-phase, output-format, or both) contains an explicit statement of the failure mode
prevented by requiring the formula; a structural formula requirement without an in-constraint
failure mode statement does not pass A-31 even if a failure mode appears elsewhere in the
protocol.

---

**Score impact:** 29 → 31 aspirational criteria · 145 → 155 pts · max 235 → 245 pts

---

## Essential Criteria (output fails without these)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-01 | **12 persona cards present** | coverage | Output contains exactly 12 persona cards, one per customer persona (C-01 through C-12). Fewer than 12 cards is an automatic fail regardless of other criteria. |
| C-02 | **NPS score and justification per card** | correctness | Each persona card contains a predicted NPS score (1-10) and a 1+ sentence justification linking persona context to the score. |
| C-03 | **Severity-labeled feedback per card** | format | Each persona card lists feedback items with explicit severity labels (blocking / major / minor / cosmetic). At least one feedback item per card unless the persona has no objections, in which case the absence must be stated. |
| C-04 | **Aggregate NPS computed and threshold applied** | correctness | Output computes aggregate NPS as mean of all 12 persona scores. Explicitly states whether threshold of 7.0 is met or not. If below 7.0, output flags spec as needing revision. |
| C-05 | **Cross-persona theme matrix present** | format | Output includes a cross-persona theme matrix (table or equivalent) mapping recurring themes to the personas that raised them. At least one theme is identified. |

---

## Recommended Criteria (output is better with these)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| R-01 | **Blocking issues escalated** | behavior | Any `blocking` severity item is called out in a dedicated summary section (e.g., "Blockers requiring resolution") separate from the per-persona cards. Zero blocking items is acceptable — section may say "none." |
| R-02 | **PM and UX roles included** | coverage | Output includes a PM read and a UX read in addition to the 12 customer personas. Each provides a short synthesis (2+ sentences) from their professional lens. |
| R-03 | **Theme matrix includes severity annotation** | depth | The cross-persona theme matrix annotates each theme with the highest severity level raised under it (e.g., "Performance — major, 4 personas"). |

---

## Aspirational Criteria (raise the bar)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| A-01 | **Persona-specific revision recommendations** | depth | Each persona card includes a targeted revision recommendation (1+ sentence) naming the specific spec change that would improve this persona's NPS. Generic recommendations ("improve onboarding") do not pass; the recommendation must reference a named spec element. |
| A-02 | **NPS sensitivity analysis** | depth | Output includes a sensitivity analysis section identifying the 2–3 personas whose scores most drive the aggregate mean. Each identified persona is named with their NPS and a one-sentence explanation of their disproportionate influence on the aggregate. |
| A-03 | **Inline [BLOCKING] flags** | format | Blocking severity items are flagged inline within the per-persona feedback list (e.g., `[BLOCKING]` prefix or equivalent marker) in addition to any aggregate escalation section. Both inline marking and aggregate escalation must be present for full pass. |
| A-04 | **Ascending-NPS persona ordering** | format | Persona cards are presented in ascending NPS order (lowest score first, highest last) rather than by persona ID (C-01 through C-12). Ties may appear in any order. Pass condition: the card sequence is monotonically non-decreasing by NPS score. |
| A-05 | **Two-pass revision recommendations** | depth | Revision recommendations are generated in two passes: first pass identifies per-persona targeted changes (see A-01); second pass synthesizes a prioritized cross-persona revision summary ranking changes by number of personas affected and maximum severity. Both passes must be present. |
| A-06 | **Inertia-baseline NPS justification** | depth | Each NPS justification explicitly compares the spec's value proposition against the persona's current behavior (inertia baseline). The justification must name what this persona gains or loses relative to their current approach, not merely describe the spec's features. Pass condition: each justification contains at least one sentence referencing the persona's current approach or workflow. |
| A-07 | **Severity-first within-card ordering** | format | Within each persona card's feedback list, items are ordered by descending severity: blocking first, then major, then minor, then cosmetic. Items of equal severity may appear in any order within their tier. Pass condition: no lower-severity item precedes a higher-severity item in the same card's feedback list. |
| A-08 | **NPS category-band annotation with aggregate distribution and Dominant Detractor objection** | depth | Each persona card annotates the NPS score with its category band (Detractor 1–6, Passive 7–8, Promoter 9–10). The aggregate section includes a band distribution count (Promoters / Passives / Detractors). The aggregate section also includes a labeled `Dominant Detractor objection:` field naming the single feedback theme most frequently cited by Detractor-tier personas. All three elements must be present. |
| A-09 | **Named `Current approach:` field per card** | format | Each persona card contains a labeled `Current approach:` field (using that exact label or `**Current approach:**`) as a distinct card entry describing what this persona does today without the spec. The field must be present even if the current approach is "no equivalent workflow exists." |
| A-10 | **`Dominant Detractor objection:` labeled field in aggregate** | format | The aggregate section contains a dedicated labeled `Dominant Detractor objection:` field (using that label or equivalent) as a distinct entry separate from the band distribution counts. The field names the single most common blocking or major objection raised by Detractor-tier personas, with a count of how many Detractors cited it. |
| A-11 | **Card header contains id/name/role only; `Current approach:` is first body field** | format | Each persona card header contains only the persona identifier, name, and role. The first labeled field in the card body (after the header) is `Current approach:`. Fields such as `Persona:` or `Summary:` do not precede `Current approach:` in the card body. |
| A-12 | **UX READ precedes PM READ** | format | In the professional lens section, the UX Read appears before the PM Read. Pass condition: UX Read section header precedes PM Read section header in document order. |
| A-13 | **Persona card uses numbered field manifest with completeness enforcement** | format | Each persona card specifies its fields using an explicit numbered list (1. Current approach: 2. NPS score: … N. Revision recommendation:) and includes a stated completeness enforcement rule that prohibits omitting any numbered field. A labeled-field card template without sequential numbering does not pass A-13 even if all fields are present. |
| A-14 | **Aggregate NPS includes confidence interval or variance annotation** | depth | The aggregate section includes a statistical spread annotation — either a confidence interval (e.g., 95% CI [6.2, 7.8]) or a variance/standard deviation figure — in addition to the mean. Pass condition: a numeric spread measure is explicitly stated alongside the aggregate mean; a mean-only aggregate does not pass A-14. |
| A-15 | **Persona card includes `Willingness to adopt:` field with threshold annotation** | depth | Each persona card contains a labeled `Willingness to adopt:` field (using that label or equivalent) that states a percentage or categorical likelihood and annotates whether it clears a defined adoption threshold. The threshold value must be stated in the evaluation protocol. Pass condition: field present, likelihood stated, and threshold comparison explicit. |
| A-16 | **Step 0 inertia baseline uses structured sub-fields** | format | The evaluation protocol's Step 0 (or equivalent inertia baseline section) specifies the baseline using an explicit set of named sub-fields (e.g., "What it delivers:", "Where it falls short:", "Floor-level switching cost:", "Persona-specific workflow disruption:") rather than a prose description. Pass condition: Step 0 contains at least three distinctly labeled sub-fields; a single prose baseline description does not pass A-16 even if it covers the same content. |
| A-17 | **Gains and losses fields enforce bilateral coverage** | depth | The evaluation protocol's field instructions for gains and losses (Fields 2 and 3 or equivalents) explicitly state that both a gain side and a loss/switching-cost side must be present. Pass condition: the protocol contains an instruction that prohibits completing the gains or losses field without addressing both sides; an instruction that describes gains and losses without an explicit bilateral completeness requirement does not pass A-17. |
| A-18 | **NPS justification references named spec element** | depth | Each persona card's NPS justification names at least one specific element from the spec being evaluated (e.g., a feature name, a workflow step, a stated constraint) as the basis for the score. Generic justifications referencing only persona attributes without linking to a spec element do not pass A-18. |
| A-19 | **Revision recommendations are tiered by implementation cost** | depth | The cross-persona revision summary (see A-05) tiers recommendations by implementation cost or complexity — distinguishing at minimum between low-cost (copy/label changes) and high-cost (architecture or workflow changes) revisions. Pass condition: the summary contains an explicit cost-tier annotation on each recommendation; an untiered list of recommendations does not pass A-19. |
| A-20 | **Sensitivity analysis names the score swing per persona** | depth | The sensitivity analysis section (see A-02) states the numeric impact on the aggregate mean if each identified high-influence persona's score shifts by ±1 point. Pass condition: each named high-influence persona has an explicit delta-to-aggregate figure; a sensitivity analysis that identifies influential personas without numeric swing figures does not pass A-20. |
| A-21 | **Gains and losses field instructions use conjunctive framing** | depth | The evaluation protocol's field instructions for gains (Field 2) and losses (Field 3) are written as conjunctive pairs — the instruction for Field 2 names Field 3 as its complement and vice versa, making explicit that neither field is complete without the other. Pass condition: each of the two field instructions references the other by name or label; field instructions that describe gains and losses independently without mutual reference do not pass A-21. |
| A-22 | **Professional lens section includes a convergence statement** | depth | The professional lens section (PM Read + UX Read) concludes with a convergence statement that explicitly identifies where the PM and UX reads agree and where they diverge. Pass condition: a labeled convergence or synthesis subsection is present after both reads; a protocol that presents PM and UX reads without a cross-read convergence statement does not pass A-22. |
| A-23 | **Persona card numbered field manifest enforces completeness via explicit rule** | format | The numbered field manifest (see A-13) is accompanied by an explicit completeness enforcement rule stating that all numbered fields must be present — e.g., "omitting any numbered field constitutes an incomplete card." The rule must be stated in the protocol, not merely implied by the numbered structure. Pass condition: numbered manifest present AND explicit completeness rule stated; a numbered manifest without an enforcement rule does not pass A-23 even if A-13 passes. |
| A-24 | **Gains and losses field instructions cross-reference named Step 0 inertia sub-fields** | depth | The evaluation protocol's `Gains from this spec:` and `Losses and switching costs:` field instructions each name at least one Step 0 sub-field by label (e.g., "What it delivers," "Where it falls short," "Floor-level switching cost") that the field is required to draw from. The cross-reference converts gains/losses from freeform bilateral assessments into delta computations: the evaluator cannot complete Fields 2 and 3 without consulting the named Step 0 sub-fields, making bilateral coverage structurally enforced rather than instructionally implied. A-17 requires bilateral coverage in prose; A-21 requires conjunctive framing; A-24 adds the third layer — named sub-field dependency that eliminates omission of either side without also suppressing the referenced baseline sub-field. Pass condition: each of the gains and losses field instructions names at least one Step 0 sub-field by its defined label; field instructions that reference gains/losses in general terms without naming specific Step 0 sub-fields do not pass A-24. |
| A-25 | **UX-before-PM role ordering accompanied by an explicit epistemic rationale** | depth | The evaluation protocol specifies UX Read before PM Read (satisfying A-12) AND includes a stated epistemic or procedural reason for that ordering — naming why UX observation should precede PM synthesis — as part of the professional lens section instructions. A rationale that names the failure mode prevented (e.g., "PM framing would anchor UX reading if PM preceded UX") makes the order a principled constraint rather than an arbitrary sequence choice. Without a rationale, the UX-before-PM constraint is positionally verifiable but epistemically arbitrary — a later variation author could reverse it without contradiction. Pass condition: UX Read precedes PM Read in document order AND a stated epistemic or procedural rationale for that ordering is present; a bare ordering instruction without rationale does not pass A-25 even if A-12 passes. |
| A-26 | **Aggregate section uses a numbered field manifest with positional verifiability** | format | The evaluation protocol specifies aggregate section fields using an explicit numbered list (A1, A2, … AN, or an equivalent sequential numbering scheme) and includes a stated completeness enforcement rule that prohibits omitting any numbered aggregate field. A-10 requires the `Dominant Detractor objection:` labeled field to be present and is verified semantically; A-26 makes every aggregate field positionally verifiable: AN is detectable by counting, not by parsing labels. The structural parallel with A-23 means the same verification property holds at both the persona card level and the aggregate summary level, making the entire output positionally auditable without semantic reading. Pass condition: aggregate fields are sequentially numbered AND an explicit completeness enforcement rule is stated; a labeled-field aggregate template without sequential numbering does not pass A-26 even if A-10 passes. |
| A-27 | **Failure mode annotation for structural constraints** | depth | The evaluation protocol names the failure mode prevented by each structural constraint it imposes. A constraint that states only the rule (e.g., "UX Read precedes PM Read") without naming the failure mode it prevents (e.g., "PM framing would anchor UX reading if PM preceded UX") is verifiable but epistemically arbitrary. Naming the failure mode converts a positional rule into a principled constraint: a later variation author cannot reverse or remove the constraint without also explaining why the named failure mode no longer applies. Pass condition: each structural constraint in the protocol is accompanied by a stated failure mode; constraints that lack failure mode annotations satisfy the structural requirement but do not pass A-27. |
| A-28 | **Directional sensitivity separation** | depth | The sensitivity analysis section (see A-02, A-20) separates upward and downward score-swing effects — reporting the aggregate delta if a high-influence persona's score increases by 1 point separately from the delta if it decreases by 1 point, rather than a symmetric ±1 figure. Directional separation matters when NPS band crossings (Detractor/Passive, Passive/Promoter) are asymmetrically distributed around the current score: a +1 move may cross a band threshold while a −1 move stays within band, producing different narrative implications. Pass condition: the sensitivity analysis reports upward and downward score deltas for each named high-influence persona as distinct figures; a symmetric ±delta figure without directional separation does not pass A-28. |
| A-29 | **CI or variance annotation includes the computation formula** | depth | The CI or variance annotation in the aggregate section includes an explicit computation formula or derivation method stated alongside the numeric value. A-14 requires a numeric spread measure; A-29 requires that the computation method be stated alongside the value. The formula matters for three reasons: (1) it allows the evaluator to verify the spread against different score inputs without re-deriving the method; (2) it makes the annotation auditable — a reader can confirm whether the CI was computed as ±1.96·(SD/√n) or via a different method; (3) it converts the statistical annotation from a black-box figure into a transparent computation. A CI that states only "95% CI [6.2, 7.8]" passes A-14 but fails A-29; one that states "95% CI [6.2, 7.8] (±1.96·SD/√12)" passes both. Pass condition: the CI or variance annotation includes an explicit computation formula or derivation method stated alongside the numeric value; a bare interval or SD figure without a stated formula does not pass A-29. |
| A-30 | **CI formula requirement enforced by derivation-phase protocol (generation-time enforcement)** | depth | The protocol contains a derivation phase in which formula statement is an explicit required step prior to CI computation and reporting (e.g., D.1 state formula → D.2 compute SD → D.3 apply → D.4 report). Process-level enforcement is more fundamental than output-format enforcement: the formula is required as an input to the computation, not merely as a decoration on the output. An output-format instruction that requires the formula to appear in the reported CI (A-29) does not satisfy A-30 — an evaluator satisficing on A-29 format could add the parenthetical after the fact, but an evaluator satisficing on A-30 cannot produce the CI at all without first completing the formula step. V-03 in Round 18 earns the citation "the formula is required at generation time, not only at output-inspection time" by requiring D.1 as a phase exit condition before D.2 can be entered. Pass condition: the protocol contains a derivation phase with formula statement as an explicit required step prior to computation; an output-format instruction that requires the formula only at reporting does not satisfy A-30. |
| A-31 | **CI formula failure mode named at the point of constraint** | depth | The CI formula constraint instruction — whether derivation-phase (A-30), output-format (A-29), or both — contains an explicit statement of the failure mode prevented by requiring the formula. The pattern directly parallels A-25: just as A-25 requires the UX-before-PM rationale to be stated within the ordering instruction (not in a separate section), A-31 requires the CI formula failure mode to be co-located with the formula constraint instruction. Co-location prevents the failure mode from being understood only by cross-referencing a separate rationale section — a reader following the constraint instruction encounters both the rule and its epistemic grounding in a single pass. A-27 requires failure mode annotations for structural constraints generally; A-31 requires that the CI formula failure mode specifically be stated at the point of constraint, not elsewhere. V-05 in Round 18 satisfies A-31 (and uniquely satisfies A-27) by naming within Step S.1: "Without the formula parenthetical (±1.96·[SD_value]/√12) alongside the interval, the CI annotation cannot be verified against different score inputs — a reader cannot confirm whether the interval was computed as ±1.96·SD/√12 or via a different method." Pass condition: the CI formula constraint instruction contains an explicit statement of the failure mode prevented by requiring the formula; a structural formula requirement without an in-constraint failure mode statement does not pass A-31 even if a failure mode appears elsewhere in the protocol or if A-27 is otherwise satisfied. |
```
