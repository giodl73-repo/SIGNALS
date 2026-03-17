Rubric written to `simulations/quest/rubrics/scout-risk-rubric-v3-2026-03-16.md`.

**5 essential, 3 recommended, 8 aspirational.**

Three new aspirational criteria added from Round 2 excellence signals:

| ID | Source | What it captures |
|----|--------|------------------|
| **C-14** | Signal 1 — V-05 C-12 PASS (IF-THEN token) | Raises C-12 from "trigger-qualified" to "syntactically enforced IF-THEN form" — the literal `IF` token excludes bare probability labels by construction |
| **C-15** | Signal 2 — V-05 C-11 PASS (type taxonomy) | Raises C-11 from "zero-generic" to "positively typed" — every mitigation declares a named type class (Spike/Validate/Gate/Contract/Cut/Instrument), which structurally prevents generic hedges at source |
| **C-16** | Signal 3 — V-03/V-05 (specificity smell-test) | Raises C-13 from >= 2 pairs to >= 3 — the count is an indirect register quality signal; a generic register cannot produce 3 distinct pairings naturally |

**Signal 4** (unified self-check gate) not issued as a criterion — it's a prompt-mechanism insight, not an output-evaluable property. Its output effect is already captured by the co-occurrence of C-11, C-12, C-13 PASS.

**Scoring adjustment**: aspirational pool grows from 5 to 8 criteria. Max composite rises from 100 to 106 (8 × 2 pts). Golden threshold stays at >= 80 — still reachable on essential + recommended alone (90 pts).

**Criterion ladder** (each aspirational explicitly upgrades its anchor):

```
C-05 (fail if 2+ generic)
  -> C-11 (zero-generic — detection/repair)
       -> C-15 (positively typed — prevention at source)

C-07 (>= half trigger-qualified)
  -> C-12 (all entries trigger-qualified)
       -> C-14 (IF-THEN syntactic form on every entry)

C-09 (>= 1 interdependency mentioned)
  -> C-13 (dedicated section, >= 2 pairs)
       -> C-16 (dedicated section, >= 3 pairs — specificity threshold)
```
tegory | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Risks are dimension-labeled** | format | Each risk entry is explicitly tagged with its dimension (e.g., "Technical", "Market", "Compliance", "Dependency", "Timeline"). Pass if >= 80% of risks carry a visible dimension label. |
| C-07 | **Likelihood is qualified beyond binary** | depth | Likelihood expressions go beyond "possible/unlikely" -- they specify a condition, scenario, or rough probability bracket (e.g., "high if team has no prior SDK experience", "~30% given current adoption curve"). Pass if >= half of risks meet this bar. |
| C-08 | **Risks are ordered by priority** | behavior | The register is ordered highest-to-lowest severity (after inertia), or explicitly states a prioritization logic. A randomly ordered flat list fails. Pass if the ordering is defensible by severity or compound impact. |

---

## Aspirational Criteria (weight: 2 pts PASS / 1 pt PARTIAL each, 16 pts max)

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

---

## Scoring Reference

| Outcome | Score Range |
|---------|-------------|
| Golden (all essential pass, composite >= 80) | 80-106 |
| Passing (all essential pass, composite < 80) | 60-79 |
| Failing (any essential fails) | 0-59 |

### Quick Failure Modes

- Inertia risk missing or not first -> C-01 fail -> max score 48 (cannot reach golden)
- Fewer than 3 dimensions covered -> C-02 fail -> cannot reach golden
- Any risk missing severity/likelihood/mitigation -> C-03 fail -> cannot reach golden
- All mitigations are generic -> C-05 fail -> cannot reach golden

---

## Version Notes

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
