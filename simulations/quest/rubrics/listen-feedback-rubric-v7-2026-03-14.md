**v7 written.** Two new criteria extracted from Round 7 signals:

---

**A-14 — Theme matrix includes per-theme severity distribution counts** (depth, 5 pts)

Source: V-03 R-03 PASS evidence names both `"Highest Severity"` and `"Severity Distribution"` columns. V-01 and V-02 pass R-03 with only the peak column. The distribution (e.g., "1 blocking, 3 major, 2 minor") enables ratio reasoning the peak alone cannot support. R-03 requires the peak; A-14 requires the full distribution.

**A-15 — Sensitivity analysis uses aggregate-contribution framing, not threshold-proximity framing** (depth, 5 pts)

Source: A-02 PARTIAL in both V-01 and V-02. V-02's failure is explicit: "threshold framing, not aggregate-influence framing" — it frames persona selection as "Detractors whose conversion to Passive would push above 7.0" rather than "personas whose scores most drive the aggregate mean." These select different sets when the distribution is skewed. V-03 passes A-02 fully by naming the correct mechanism. A-15 isolates the framing distinction independently of A-02's completeness check.

---

**Score impact:** 13 → 15 aspirational criteria · 65 → 75 pts · max **155 → 165 pts**
ve would push above 7.0" rather than by their mathematical
contribution to the aggregate mean. V-03 PASS: "Name the 2-3 personas whose scores most
drive the aggregate." The distinction matters when the distribution is skewed: threshold
proximity picks personas nearest 7.0; aggregate contribution picks personas with the highest
weight on the mean -- often different sets.

**Score impact:**
- Aspirational: 13 -> 15 criteria, 65 -> 75 pts
- Max score: 155 -> **165 pts**

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
| R-01 | **Blocking issues escalated** | behavior | Any `blocking` severity item is called out in a dedicated summary section (e.g., "Blockers requiring resolution") separate from the per-persona cards. Zero blocking items is acceptable -- section may say "none." |
| R-02 | **PM and UX roles included** | coverage | Output includes a PM read and a UX read in addition to the 12 customer personas. Each provides a short synthesis (2+ sentences) from their professional lens. |
| R-03 | **Theme matrix includes severity annotation** | depth | The cross-persona theme matrix annotates each theme with the highest severity level raised under it (e.g., "Performance -- major, 4 personas"). |

---

## Aspirational Criteria (raise the bar)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| A-01 | **Persona-specific revision recommendations** | depth | For any persona whose NPS prediction is below 6, the card includes at least one concrete, actionable spec change that would raise their score. Recommendations are specific enough to act on (not "improve clarity"). |
| A-02 | **NPS sensitivity analysis** | depth | Output identifies the 2-3 personas whose scores most drive the aggregate NPS and notes what single change would most improve the aggregate. Demonstrates understanding of which personas are leverage points. |
| A-03 | **Inline blocking flags for verification escalation** | format | Blocking-severity feedback items are marked with an inline flag (e.g., `[BLOCKING]`) at the point of occurrence within the persona card, so the dedicated escalation section (R-01) can be assembled as a verification pass over pre-tagged items rather than first-pass discovery. Pass condition: at least one `[BLOCKING]` inline marker present in any card that has a blocking item; escalation section references or collects from those markers. |
| A-04 | **Ascending-NPS persona ordering** | behavior | Persona cards are presented in ascending NPS order (lowest score first), surfacing highest-risk personas at the top of the output. Ordering must be explicit -- not alphabetical or arbitrary. Pass condition: lowest NPS card appears first; highest NPS card appears last. |
| A-05 | **Two-pass revision recommendations** | depth | Revision recommendations for low-NPS personas appear in two places: (1) inline within the persona card immediately following the NPS score, and (2) collected into a dedicated revision summary section at the end. Both passes must be present; the summary may be a reference list back to inline items. |
| A-06 | **Inertia-baseline NPS justification** | depth | Each persona NPS justification is framed as a status-quo comparison -- explicitly addressing whether the spec beats the persona current workflow, tool, or behavior. A description of persona preferences alone does not pass; the justification must include a comparison to the inertia baseline (e.g., "switching cost vs. net benefit"). Pass condition: at least one sentence per card contains an explicit comparison to what the persona currently does or uses. |
| A-07 | **Severity-first within-card ordering** | format | Within each persona card, feedback items are listed in descending severity order (blocking first, then major, minor, cosmetic). The ordering must be deterministic -- not arbitrary or chronological. Pass condition: in any card containing a blocking item, the first feedback item is blocking; in any card containing a major item but no blocking item, the first feedback item is major. A card with only one severity level trivially passes. |
| A-08 | **NPS category-band annotation with aggregate distribution** | depth | Each persona NPS score is annotated with its Detractor/Passive/Promoter band label. Band definitions must encode inertia framing: Detractor = switching cost exceeds net benefit; Passive = marginal net benefit; Promoter = net benefit clearly exceeds switching cost. The aggregate section counts how many personas fall in each band and names the dominant Detractor objection pattern. Pass condition: all 12 NPS scores carry a band label; aggregate section includes Detractor/Passive/Promoter counts and a named dominant-Detractor objection. |
| A-09 | **Named `Current approach:` field per persona card** | format | Each persona card contains a dedicated labeled `Current approach:` field -- not embedded in prose -- naming the persona existing tool, workflow, or behavior before NPS and feedback. Makes the inertia baseline a required structural field rather than optional justification text. Pass condition: every persona card contains a `Current approach:` field with at least one sentence describing what the persona currently does; the field is visually distinct (label + colon format or equivalent). |
| A-10 | **`Dominant Detractor objection:` labeled field in aggregate** | format | The aggregate section contains a dedicated labeled `Dominant Detractor objection:` field that names the specific inertia concern pattern raised by Detractor personas -- not a prose paragraph. The field draws on per-card `Current approach:` data to synthesize a single named pattern (e.g., "setup complexity," "migration cost from existing workflow"). Pass condition: aggregate section contains a `Dominant Detractor objection:` field with a specific pattern name; field is visually distinct (label + colon format or equivalent); restatements of the band definition ("switching cost exceeds net benefit") do not pass. |
| A-11 | **Card header contains id/name/role only; `Current approach:` is first body field** | format | The card header line contains only identifier, name, and role -- no scored data (NPS score must not appear in the header line). Card body field order: `Current approach:` -> `NPS:` -> feedback items. This structural constraint makes A-09 unambiguous regardless of any model tendency to front-load scores into the header. Pass condition: no NPS score appears in the card header line; `Current approach:` is the first labeled field in the card body, preceding `NPS:`; ordering is deterministic across all 12 cards. |
| A-12 | **UX READ precedes PM READ** | format | In outputs containing both role reads (R-02), the UX READ section appears before the PM READ section. UX design perspective establishes the craft framing that PM synthesis builds on; reversing the order weakens the chain of reasoning. Pass condition: UX READ section appears earlier in the output than PM READ section; ordering is deterministic across all variations. Outputs that omit one or both role reads do not fail A-12 -- they fail R-02. |
| A-13 | **Theme matrix as final synthesis section** | format | The cross-persona theme matrix (C-05) appears as the last major section in the output, positioned after both PM READ and UX READ when present. The theme matrix functions as a closing synthesis over all persona and role data -- not an intermediate step between card phases. Pass condition: no PM READ, UX READ, sensitivity analysis, revision summary, or other major analysis section appears after the theme matrix; the theme matrix is the final substantive section before any closing remarks. |
| A-14 | **Theme matrix includes per-theme severity distribution counts** | depth | The cross-persona theme matrix extends beyond R-03's highest-severity annotation to show the count of feedback items at each severity level per theme (e.g., "1 blocking, 3 major, 2 minor" for a given theme row). This enables ratio reasoning that the peak-severity column alone cannot support: a theme with 1 blocking across 12 personas reads differently from a theme with 1 blocking and 8 majors. Pass condition: theme matrix contains a distribution column or equivalent structure showing per-severity item counts for each theme row; showing only the highest severity level does not pass A-14 even if R-03 passes. Format is flexible (a "Distribution" column, a notation like "1B 3M 2m," a separate count row) as long as the per-level counts are readable by inspection. |
| A-15 | **Sensitivity analysis uses aggregate-contribution framing, not threshold-proximity framing** | depth | When identifying high-leverage personas in the A-02 sensitivity analysis, the mechanism must be aggregate-mean contribution -- not threshold proximity. Threshold-proximity framing ("convert these Detractors to Passive and the aggregate clears 7.0") selects the personas nearest the passing line. Aggregate-contribution framing ("these personas most drive the aggregate mean") selects the personas with the greatest mathematical weight on the mean -- a different set when the distribution is skewed. Pass condition: sensitivity section contains explicit aggregate-contribution language referencing "most drives the aggregate," "highest leverage on the mean," "greatest weight on aggregate NPS," or equivalent. Threshold-proximity language may appear alongside aggregate-contribution framing but does not substitute for it. An output that identifies the correct personas solely through threshold proximity fails A-15 even if A-02 passes. |

---

## Weight Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 pts (12 each) |
| Recommended | R-01, R-02, R-03 | 30 pts (10 each) |
| Aspirational | A-01 through A-15 | 75 pts (5 each) |
| **Max score** | | **165 pts** |

> Aspirational criteria are bonus points above the 90-point recommended baseline. A score of 90 means all essential and recommended criteria pass. A score of 165 means the output demonstrates all fifteen excellence patterns.

---

## Notes for Scorers

- A persona card may contain zero feedback items if the persona has no objections -- this is valid as long as NPS and a rationale are still present.
- NPS scores of exactly 7.0 clear the threshold (threshold is >=7.0, not >7.0).
- The theme matrix format is flexible (markdown table, bullet list with persona tags, etc.) as long as the mapping is machine-readable by inspection.
- PM and UX roles (R-02) do not count toward the 12-persona aggregate NPS; they are supplemental lenses only.
- A-03 requires both halves: inline `[BLOCKING]` markers in cards AND an escalation section that draws from them. Either half alone does not pass.
- A-04 ascending order is scored on the final output ordering, not on internal processing order.
- A-05 two-pass: inline recommendation must be actionable (same bar as A-01); the summary section may be a pointer list ("see C-03 card") rather than full duplication.
- A-06 inertia framing: the comparison must be explicit in the text -- "beats their status quo" or "switching cost" framing qualifies; "this persona values X" alone does not.
- A-07 severity-first: a card with a single severity level trivially passes. Cards with zero feedback items are excluded from scoring. The rule applies independently per card -- one out-of-order card fails A-07 for the whole output.
- A-08 band boundaries: Detractor [1-6], Passive [7-8], Promoter [9-10]. Band definitions must encode inertia framing in the rubric or output preamble -- score labels alone do not pass. The named dominant-Detractor objection must be a specific concern pattern (e.g., "setup complexity"), not a restatement of the band definition.
- A-09 field format: `Current approach:` must be a labeled field (label + colon, or equivalent structural marker). It must appear before the NPS score or feedback items within the card. "Currently uses X for Y" qualifies; vague framing like "this persona is familiar with similar tools" does not. A-09 and A-06 are complementary but independent: A-09 requires the structural field; A-06 requires the NPS justification sentence to reference the inertia baseline. An output can pass one without the other.
- A-10 and A-09 are complementary but independent: A-09 requires the per-card `Current approach:` field; A-10 requires the aggregate to synthesize those fields into a named Detractor pattern. An output may pass A-09 without A-10 (cards have the field but aggregate lacks the synthesis), or pass A-10 without A-09 (aggregate names a Detractor pattern but cards embed current approach in prose rather than a labeled field). The `Dominant Detractor objection:` field must be in the aggregate section -- a per-card label alone does not satisfy A-10.
- A-11 is a structural superset of A-09 ordering requirement: a card that passes A-11 (NPS out of header, `Current approach:` first body field) automatically passes A-09 ordering requirement. However, A-09 and A-11 are scored independently -- A-09 still requires every card to have a `Current approach:` field with substantive content; A-11 adds the header-cleanliness constraint.
- A-12 scoring is only active when R-02 passes. An output that omits both role reads cannot be penalized for ordering what was never present. When R-02 passes with only one role read present, A-12 trivially passes.
- A-13 and A-12 are independent: an output may place UX before PM (pass A-12) but insert the theme matrix between the role reads and the sensitivity analysis (fail A-13). The theme matrix must be the terminal major section -- the canonical failure case is a sensitivity analysis or revision summary appearing after it.
- A-14 is additive over R-03: an output that passes A-14 automatically passes R-03 (distribution implies peak). An output may pass R-03 without A-14 (highest-severity column present but no per-level counts). The distribution format is flexible; the requirement is that a reader can determine from the matrix how many items at each severity level contribute to each theme, not just which level is highest.
- A-15 and A-02 are nested: an output that passes A-15 is also more likely to pass A-02 (aggregate-contribution framing satisfies the identification mechanism). However, they are scored independently -- A-02 may receive PARTIAL while A-15 fails (output identifies the right personas via threshold proximity, not aggregate contribution). An output passes A-15 only when aggregate-contribution language is explicit; a correct result through threshold-proximity reasoning does not pass A-15 even if the identified personas happen to be the same.
