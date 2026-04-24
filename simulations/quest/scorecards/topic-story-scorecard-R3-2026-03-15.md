# Quest Score — `topic-story` Round 3

## Scoring Notes

**Trace artifact**: placeholder (no output to score against). Scoring is on **prompt design quality** — how reliably each variation's structure forces compliance with each criterion.

**V-04 and V-05**: Not provided in this round's input. Referenced in rubric preamble as prior-round exemplars for Pattern A (C-13) and Pattern B (C-10/C-14). Scored as N/A below.

**Scoring convention**: PASS = prompt structure strongly forces criterion | PARTIAL = criterion addressed but leaves AI interpretive latitude | FAIL = criterion not addressed

---

## V-01 — Template with explicit slot placeholders

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Recommendation block appears first in template, above first horizontal rule, with "complete this before writing anything else" |
| C-02 | **PASS** | All five beat headers present verbatim in template slots |
| C-03 | **PASS** | Pattern slot requires claim that "only becomes visible when the signals are read together — not what any single signal shows alone" |
| C-04 | **PASS** | Pattern slot explicitly prohibits summary: "not a collection of findings… must name a synthetic claim" |
| C-05 | **PASS** | "Minimum three distinct signal namespaces or artifact types must appear" as a hard bullet rule |
| C-06 | **PASS** | Uncertainty bullets require "(a) specific question AND (b) what resolving it would change about the recommendation verb" with directional example |
| C-07 | **PARTIAL** | Verb options (proceed/pause/pivot/abandon) listed but no proportionality calibration check enforced |
| C-08 | **PARTIAL** | Template structure follows intent→signals→pattern→uncertainty→recommendation arc, but slot fills may produce mechanical outputs without narrative connective tissue |
| C-09 | **FAIL** | No "we expected X but found Y" instruction present |
| C-10 | **PASS** | Pattern block is a discrete labeled sentence: "The pattern: [claim]." explicitly placed as named element |
| C-11 | **PASS** | Recommendation section: "Cite the pattern by name or by summary as the explicit reason for this verb" |
| C-12 | **PASS** | Uncertainty bullets require "if X resolves to Y, this moves from pause to proceed" — direction is mandatory |
| C-13 | **PASS** | Opening slot example: "A product lead deciding whether to staff this feature in Q3 should proceed." Role + constraint + verb required |
| C-14 | **PASS** | "This sentence must be readable without consulting the bullets above or the recommendation below" — explicit forward/backward reference prohibition |

**Essential**: 4/4 → 60  
**Recommended**: 2.5/3 → 25  
**Aspirational**: 5.5/7 → 7.9  
**Composite**: **92.9**  
**Golden**: ✓ (all essential pass, composite ≥ 80)

---

## V-02 — Imperative/command phrasing

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | **PASS** | STEP 1: "WRITE THE OPENING RECOMMENDATION FIRST… Do not write any context, setup, or hedging before this sentence" |
| C-02 | **PASS** | STEP 2 provides exact headers; "Do not rename them. Do not merge them. Do not reorder them." |
| C-03 | **PASS** | Pattern must "Name a relationship, tension, or gap that requires at least two signals to be true simultaneously" |
| C-04 | **PASS** | Same requirement as C-03; "requires at least two signals" bars single-signal derivation |
| C-05 | **PASS** | STEP 4: "At minimum, reference three distinct signal types" |
| C-06 | **PASS** | STEP 5: each uncertainty must state "if this resolves one way, the recommendation moves to [verb]" |
| C-07 | **PARTIAL** | STEP 7 verification list does not include evidence-verb proportionality check |
| C-08 | **PARTIAL** | Seven numbered steps produce procedural output; arc framing is implicit, not instructed |
| C-09 | **FAIL** | No contrastive/discovery framing instruction |
| C-10 | **PASS** | STEP 3: "BEFORE WRITING SECTION 3, STOP AND NAME THE PATTERN" — forced analytic pre-composition pause |
| C-11 | **PASS** | STEP 6: "Write: 'Because [restate the pattern in brief], the recommendation is [verb].'" — explicit bridge formula |
| C-12 | **PASS** | STEP 5: "if this resolves one way, the recommendation moves to [verb]; if the other way, stays at [verb] or moves to [verb]. Name the direction." |
| C-13 | **PASS** | STEP 6: "Name the role who is deciding. Name the constraint they face… write it as a decision ('a [role] deciding [X] should [verb]')" |
| C-14 | **PASS** | "Be readable on its own… Contain no phrases like 'as described above', 'as shown below'" — explicit prohibition list |

**Essential**: 4/4 → 60  
**Recommended**: 2.5/3 → 25  
**Aspirational**: 5.5/7 → 7.9  
**Composite**: **92.9**  
**Golden**: ✓ (all essential pass, composite ≥ 80)

---

## V-03 — Lifecycle emphasis / analytic pre-pass

**Note**: Prompt text not provided — only hypothesis visible. Scored conservatively from hypothesis description only.

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | **PARTIAL** | Pre-pass approach does not guarantee BLUF placement unless explicit; hypothesis does not name BLUF as a pre-pass output |
| C-02 | **PARTIAL** | Five beats implied but not enforced with exact headers in hypothesis description |
| C-03 | **PASS** | "identify the pattern" as analytic step before writing implies cross-signal synthesis requirement |
| C-04 | **PASS** | Analytic pre-pass for pattern identification forces naming relationship over summarizing |
| C-05 | **PASS** | "map signal coverage" is an explicit pre-pass step |
| C-06 | **PASS** | "list uncertainties with decision-costs" is an explicit pre-pass step |
| C-07 | **PARTIAL** | Not addressed in hypothesis description |
| C-08 | **PARTIAL** | Pre-pass may improve arc coherence but not directly instructed |
| C-09 | **FAIL** | Not mentioned in hypothesis |
| C-10 | **PASS** | Core hypothesis target: "the pattern was named analytically, not discovered mid-prose" |
| C-11 | **PARTIAL** | Pattern pre-composition supports traceability but explicit bridge formula not described |
| C-12 | **PASS** | "list uncertainties with decision-costs" maps to C-12 |
| C-13 | **PARTIAL** | Not mentioned in hypothesis |
| C-14 | **PASS** | Core hypothesis target: pre-composition independence is the design goal |

**Essential**: C-01 PARTIAL, C-02 PARTIAL → **not all essential pass**  
**Recommended**: 2.5/3 → 25  
**Composite**: (3/4 × 60) + (2.5/3 × 30) + (4.5/7 × 10) = 45 + 25 + 6.4 = **76.4**  
**Golden**: ✗ (essential C-01, C-02 not confirmed pass)

---

## V-04 / V-05

Not provided in this round's scoring input. Per rubric preamble, these were prior-round exemplars for:
- C-13: Named decision-maker + time constraint + accountability ("10 minutes and must decide")
- C-10/C-14: "Strongest mechanism — both structural independence and sequencing enforced"

**Scores**: N/A — cannot evaluate without prompt text.

---

## Rankings

| Rank | Variation | Composite | All Essential Pass | Status |
|------|-----------|-----------|-------------------|--------|
| 1 | **V-02** | 92.9 | ✓ | Golden |
| 1 | **V-01** | 92.9 | ✓ | Golden |
| 3 | V-03 | 76.4 | ✗ | Partial |

**V-02 is top** by marginal edge: C-11 pattern-to-recommendation bridge is more explicit ("Because [pattern], the recommendation is [verb]" formula), reducing AI drift on the most architecturally important link.

---

## Excellence Signals from V-02 (top variation)

**Pattern C — Post-composition verification gate**: V-02's STEP 7 is a self-audit checklist mapped to specific structural criteria, required before submission. The gate is sequential (not parallel to writing), making it a catch layer for failures the initial steps could not prevent. The output property: structural compliance is checked twice — once during generation (steps 1–6) and once after (step 7).

**Pattern D — Mid-composition labeled pause**: V-02's STEP 3 requires a complete stop and a named labeled artifact ("The pattern: [claim]") before writing the section prose. The pause is architectural: the section cannot begin until the pre-composition artifact exists. This forces C-10 structurally rather than editorially — the pattern label is not a style choice but a precondition for continuing.

---

```json
{"top_score": 93, "all_essential_pass": true, "new_patterns": ["Post-composition verification gate: a self-audit checklist anchored to specific criteria required before submission creates a second compliance layer that catches structural failures the generation steps could not prevent", "Mid-composition labeled pause: requiring a fully labeled named artifact (the pattern statement) as a precondition before section prose begins prevents pattern-discovery-mid-prose and forces C-10 structurally rather than editorially"]}
```
