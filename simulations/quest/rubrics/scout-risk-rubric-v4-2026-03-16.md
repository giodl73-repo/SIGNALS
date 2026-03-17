v4 written. Here's the complete picture:

---

## New criteria: C-17 and C-18

**C-17 — Interdependency pairs carry severity-transition labels**

Grounded in V-01 C-09 PASS evidence: *"If dependency risk materializes, timeline risk escalates to HIGH"* — that formulation isn't just naming a link, it's stating the FROM/TO severity transition. V-01's backward pressure reliably produces pairs of this quality; no v3 criterion required it. Raises C-16 from ≥3 named pairs to ≥3 pairs each with an explicit severity escalation.

**C-18 — Mitigation type portfolio covers ≥ 3 distinct classes**

Grounded in V-03 C-15 PASS: type labels are present but nothing in v3 tests whether the taxonomy does classification work or just label work. A register with 5 Spikes and 1 Gate passes C-15 — C-18 catches that. Raises C-15 from "every entry has a type" to "at least 3 distinct type classes in use."

---

## Updated ladder

```
C-05 → C-11 → C-15 → C-18  (generic → zero-generic → typed → type-diverse)

C-07 → C-12 → C-14          (binary → qualified → IF-THEN syntactic)

C-09 → C-13 → C-16 → C-17  (mentioned → dedicated section → ≥3 pairs → severity-labeled pairs)
```

**Scoring**: aspirational pool 8→10, max composite 106→110, golden threshold stays ≥80.
compliance, dependency, timeline. Fail if fewer than 3 dimensions are represented. |
| C-03 | **Risk anatomy complete** | correctness | Every risk entry includes all three required fields: severity (HIGH/MEDIUM/LOW), likelihood (any meaningful expression of probability or triggering condition), and mitigation (a stated action or control). Fail if any risk is missing one or more fields. |
| C-04 | **Severity uses correct scale** | format | Severity values are drawn exclusively from {HIGH, MEDIUM, LOW}. No numeric scales, percentages, or invented labels. Fail if any severity value deviates from this vocabulary. |
| C-05 | **Mitigations are specific and actionable** | depth | Each mitigation describes a concrete action, owner class, or control — not a generic hedge ("monitor closely", "be careful"). A passing mitigation names what to do or what to watch, not just that something should happen. Fail if two or more mitigations are generic non-actions. |

---

## Recommended Criteria (weight: 10 pts each, 30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Risks are dimension-labeled** | format | Each risk entry is explicitly tagged with its dimension (e.g., "Technical", "Market", "Compliance", "Dependency", "Timeline"). Pass if >= 80% of risks carry a visible dimension label. |
| C-07 | **Likelihood is qualified beyond binary** | depth | Likelihood expressions go beyond "possible/unlikely" -- they specify a condition, scenario, or rough probability bracket (e.g., "high if team has no prior SDK experience", "~30% given current adoption curve"). Pass if >= half of risks meet this bar. |
| C-08 | **Risks are ordered by priority** | behavior | The register is ordered highest-to-lowest severity (after inertia), or explicitly states a prioritization logic. A randomly ordered flat list fails. Pass if the ordering is defensible by severity or compound impact. |

---

## Aspirational Criteria (weight: 2 pts PASS / 1 pt PARTIAL / 0 pts FAIL each, 20 pts max)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Risk interdependencies noted** | depth | At least one risk entry notes how it compounds with or unlocks another (e.g., "If dependency risk materializes, timeline risk escalates to HIGH"). Pass if at least one cross-risk dependency is surfaced explicitly. |
| C-10 | **AMEND behavior demonstrated** | behavior | When an AMEND directive is present in the prompt (focus on one dimension, adjust severity thresholds), the output correctly narrows scope or recalibrates without losing inertia or risk anatomy. Pass if AMEND is applied correctly and inertia risk is retained even in a narrowed register. |
| C-11 | **Full mitigation specificity (zero-generic)** | depth | Every mitigation in the register names a concrete action, owner class, or control mechanism -- no generic hedge language anywhere. Raises the C-05 bar from "fewer than 2 generic" to zero. Pass if a full scan of all mitigations finds no instance of "monitor closely," "keep an eye on," "revisit later," "consider alternatives," or equivalent non-actions. |
| C-12 | **All likelihoods are trigger-qualified** | depth | Every likelihood expression specifies a concrete triggering condition or scenario (not just "possible/unlikely/high/medium"). Raises the C-07 bar from ">= half" to all entries. Pass if every risk entry has a likelihood framed as a named condition or scenario rather than a bare probability label. |
| C-13 | **Interdependencies structured in a dedicated section** | depth | Risk interdependencies appear in a labeled section (not as inline footnotes or scattered notes), with at least two cross-risk links named. Raises the C-09 bar from "at least one" to "a structured section with >= 2 named dependencies." Pass if a dedicated interdependency section exists and names at least two compound-risk pairings. |
| C-14 | **Likelihoods use IF-THEN syntactic form** | depth | Every likelihood entry is written as "IF [named condition], THEN this risk activates" (or equivalent explicit IF-THEN phrasing). Bare probability labels ("high", "~30%", "possible") are absent from all entries. Raises the C-12 bar from "trigger-qualified" to "syntactically enforced IF-THEN form." Pass if every likelihood entry uses the IF...THEN construct -- no bare label survives a full scan. |
| C-15 | **Mitigation type declared for every entry** | depth | Every mitigation begins with or explicitly names its type class (e.g., Spike, Validate, Gate, Contract, Cut, Instrument, or domain-equivalent taxonomy). The type is a positive structural claim, not merely the absence of generic language -- a Spike requires a named unknown and time-box, a Gate requires a named criterion. Raises the C-11 bar from "zero-generic" to "positively typed." Pass if every mitigation carries a visible type label. |
| C-16 | **Interdependency count reaches specificity threshold** | depth | The dedicated interdependency section names at least 3 compound-risk pairings. The count functions as an indirect quality signal for the underlying register -- only a sufficiently specific risk register generates 3 distinct pairings naturally. Raises the C-13 bar from >= 2 to >= 3 named pairs. Pass if the interdependency section lists at least 3 explicitly named compound-risk pairs. |
| C-17 | **Interdependency pairs carry severity-transition labels** | depth | Every compound-risk pair in the interdependency section states not only which risks are linked but also the severity transition that activation triggers (e.g., "IF Risk A activates, Risk B escalates from MEDIUM to HIGH"). A bare compound statement ("A compounds B" or "A worsens B") without a named severity transition fails. Raises the C-16 bar from ">= 3 named pairs" to ">= 3 pairs each with an explicit FROM/TO severity label." Pass if every interdependency pair in the section names both the linked risk and its severity escalation. |
| C-18 | **Mitigation type portfolio covers >= 3 distinct classes** | depth | The risk register uses at least 3 distinct type class names (from: Spike, Validate, Gate, Contract, Cut, Instrument) across its entries. A register where every mitigation uses the same type class is type-monoculture -- the label is present (C-15 passes) but the taxonomy is not meaningfully applied. Raises the C-15 bar from "every entry has a type" to "the register's type distribution is substantively diverse." Pass if scanning all mitigation entries finds at least 3 distinct type class names in use. |

---

## Scoring Reference

| Outcome | Score Range |
|---------|-------------|
| Golden (all essential pass, composite >= 80) | 80-110 |
| Passing (all essential pass, composite < 80) | 60-79 |
| Failing (any essential fails) | 0-59 |

### Quick Failure Modes

- Inertia risk missing or not first -> C-01 fail -> max score 48 (cannot reach golden)
- Fewer than 3 dimensions covered -> C-02 fail -> cannot reach golden
- Any risk missing severity/likelihood/mitigation -> C-03 fail -> cannot reach golden
- All mitigations are generic -> C-05 fail -> cannot reach golden

---

## Criterion Ladder

Each aspirational criterion explicitly upgrades its anchor:

```
C-05 (fail if 2+ generic)
  -> C-11 (zero-generic -- detection/repair)
       -> C-15 (positively typed -- prevention at source)
            -> C-18 (diverse type portfolio -- no monoculture)

C-07 (>= half trigger-qualified)
  -> C-12 (all entries trigger-qualified)
       -> C-14 (IF-THEN syntactic form on every entry)

C-09 (>= 1 interdependency mentioned)
  -> C-13 (dedicated section, >= 2 pairs)
       -> C-16 (dedicated section, >= 3 pairs -- specificity threshold)
            -> C-17 (>= 3 pairs, each with severity-transition label)
```

---

## Version Notes

**v4 (2026-03-16)**: Added C-17, C-18 from Round 3 excellence signals. Aspirational pool expands
from 8 to 10 criteria (20 pts max). Max composite rises from 106 to 110; golden threshold stays
at >= 80.

- **C-17** traces to Signal 1 -- V-01 C-09 PASS evidence contains the formulation "If dependency
  risk materializes, timeline risk escalates to HIGH." The pass evidence for C-09 already
  demonstrates severity-transition labeling as the natural output of mandatory interdependency
  phases; no R3 variant has a criterion that requires this notation across all pairs. C-17 raises
  C-16 from ">= 3 named pairs" to ">= 3 pairs each stating a FROM/TO severity transition." A
  register that produces bare compound statements ("A compounds B") after V-01's backward
  pressure is leaving output quality on the table -- the same specificity that generates 3 pairs
  naturally also generates severity-labeled transitions naturally. The count (C-16) is an indirect
  register quality signal; the severity label is the direct quality signal.

- **C-18** traces to Signal 2 -- the R3 scorecard reveals that C-15 (positively typed mitigations)
  can be satisfied by a register where every entry uses the same type class. V-03 achieves C-15
  PASS via sub-field obligations but nothing in the rubric tests whether the six available type
  classes (Spike, Validate, Gate, Contract, Cut, Instrument) are applied discriminately. A risk
  register with 5 Spikes and 1 Gate is type-monoculture: the label field is populated (C-15 passes)
  but the taxonomy is not doing classification work. C-18 raises C-15 by requiring that at least
  3 distinct type classes appear, which forces the type selection to track the actual mitigation
  strategy (not all unknowns require a Spike; not all decisions require a Gate). Three classes is
  the minimum for meaningful taxonomy coverage given typical 5-7 entry registers.

**v3 (2026-03-16)**: Added C-14, C-15, C-16 from Round 2 excellence signals. Aspirational pool
expands from 5 to 8 criteria (16 pts max). Max composite rises from 100 to 106; golden threshold
stays at >= 80.

- **C-14** traces to Signal 1 (V-05, C-12 PASS via IF-THEN syntactic token) -- requiring the
  literal "IF" token at the start of every likelihood entry is a structural enforcer, not a
  semantic request. The model cannot produce "high" or "~30%" when the field must begin with
  "IF [condition], THEN this risk activates." C-14 raises C-12 from "trigger-qualified" to
  "syntactically enforced IF-THEN form."

- **C-15** traces to Signal 2 (V-05, C-11 PASS via mitigation type taxonomy) -- requiring
  selection of a named type (Spike/Validate/Gate/Contract/Cut/Instrument) before writing the
  mitigation sentence eliminates generic text at generation time. Each type carries a structural
  obligation: a Spike has a named unknown and time-box, a Gate has a named criterion. "Monitor
  closely" is incompatible with any of the six types. C-15 raises C-11 from "zero-generic" to
  "positively typed."

- **C-16** traces to Signal 3 (V-03/V-05, specificity smell-test) -- the rule "if you find only
  1 pairing after reviewing all rows, your risks are too generic -- revise them" ties the
  interdependency count to the underlying risk specificity. Specific risks produce specific
  pairings; generic risks cannot. C-16 raises C-13 from >= 2 pairs to >= 3, making the
  interdependency section a quality signal for the entire register.

- **Signal 4** (unified self-check gate) -- noted but not issued as a criterion. The observation
  that a single post-generation verification pass covering all enforcement dimensions catches
  violations that per-field reminders miss is a prompt-mechanism insight, not an output-evaluable
  property. Its effect is visible as the co-occurrence of C-11, C-12, C-13 PASS in V-05; those
  criteria already capture the quality dimension it produces.

**v2 (2026-03-16)**: Added C-11, C-12, C-13 from Round 1 excellence signals.

- **C-11** traces to V-03 C-05 PASS -- the explicit re-read gate with multiple named negative
  examples demonstrated that zero-generic is achievable when a prompt enforces it. Raises C-05
  from "fewer than 2" to zero.
- **C-12** traces to V-03 C-07 PASS -- trigger-condition framing reliably produces fully
  qualified likelihoods across all entries, not just half. Raises C-07 from ">= half" to all
  entries.
- **C-13** traces to V-02 C-09 PARTIAL -- the optional dedicated interdependency section is
  structurally superior to scattered inline notes and enables downstream risk-chain analysis.
  Raises C-09 from single-link to structured section with >= 2 named dependencies.

**v1 (2026-03-16)**: Initial rubric. 5 essential, 3 recommended, 2 aspirational (C-09, C-10).
