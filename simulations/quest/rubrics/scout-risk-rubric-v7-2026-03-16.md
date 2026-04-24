Reading the scorecard, three new excellence patterns emerge — each grounded in evidence from a specific variation and each escalating an existing criterion rather than duplicating it.

**New patterns identified:**

1. **V-03 — Named repair loops** (`Repair Loop A` / `Repair Loop B` labels): C-21 passes because the count is *unambiguous* — the loops are independently addressable by name. C-21 only requires count-match; it doesn't require naming. Escalation: every repair loop carries a unique label.

2. **V-02 — Complete 6-class taxonomy defined in the prompt**: C-15 requires per-entry sub-field contracts (what appears in each output entry). V-02 also pre-defines all 6 type classes with sub-fields in the prompt itself as a reference taxonomy. C-15 can pass with only the types actually used; C-24 requires all 6 defined upfront.

3. **V-01 — Phase 2b as a standalone named diversity audit step**: C-18 requires the gate and repair loop to exist; it doesn't require the gate to occupy its own isolated step. V-01's Phase 2b separates *generation* from *auditing* into discrete named phases. Escalation: the diversity audit is isolated in a dedicated step.

---

```markdown
# Scout-Risk Rubric — v7

## What This Rubric Evaluates

A scout-risk prompt is evaluated on its ability to produce a well-structured risk register
covering inertia risk, dimensional risks, and interdependencies. This rubric grades the
prompt text — not a trace artifact.

---

## Essential Criteria (weight: 12 pts each, 60 pts total)

Fail any essential → max composite 48 → cannot reach golden.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Inertia risk is mandatory and first** | structure | The prompt explicitly requires an inertia risk entry as the first item in the register. It must be clearly labeled as inertia and the instruction must be non-optional — "include if relevant" or "you may add" fails. Pass if the prompt states the inertia risk is required and must appear before dimensional risks. |
| C-02 | **Dimensional coverage enforced** | structure | The prompt requires risks across multiple dimensions — at minimum three of: technical, market, compliance, dependency, timeline. Fail if fewer than 3 dimensions are represented. |
| C-03 | **Risk anatomy complete** | correctness | Every risk entry includes all three required fields: severity (HIGH/MEDIUM/LOW), likelihood (any meaningful expression of probability or triggering condition), and mitigation (a stated action or control). Fail if any risk is missing one or more fields. |
| C-04 | **Severity uses correct scale** | format | Severity values are drawn exclusively from {HIGH, MEDIUM, LOW}. No numeric scales, percentages, or invented labels. Fail if any severity value deviates from this vocabulary. |
| C-05 | **Mitigations are specific and actionable** | depth | Each mitigation describes a concrete action, owner class, or control — not a generic hedge ("monitor closely", "be careful"). A passing mitigation names what to do or what to watch, not just that something should happen. Fail if two or more mitigations are generic non-actions. |

---

## Recommended Criteria (weight: 10 pts each, 30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Risks are dimension-labeled** | format | Each risk entry is explicitly tagged with its dimension (e.g., "Technical", "Market", "Compliance", "Dependency", "Timeline"). Pass if >= 80% of risks carry a visible dimension label. |
| C-07 | **Likelihood is qualified beyond binary** | depth | Likelihood expressions go beyond "possible/unlikely" — they specify a condition, scenario, or rough probability bracket (e.g., "high if team has no prior SDK experience", "~30% given current adoption curve"). Pass if >= half of risks meet this bar. |
| C-08 | **Risks are ordered by priority** | behavior | The register is ordered highest-to-lowest severity (after inertia), or explicitly states a prioritization logic. A randomly ordered flat list fails. Pass if the ordering is defensible by severity or compound impact. |

---

## Aspirational Criteria (weight: 2 pts PASS / 1 pt PARTIAL / 0 pts FAIL each, 34 pts max)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Risk interdependencies noted** | depth | At least one risk entry notes how it compounds with or unlocks another (e.g., "If dependency risk materializes, timeline risk escalates to HIGH"). Pass if at least one cross-risk dependency is surfaced explicitly. |
| C-10 | **AMEND behavior demonstrated** | behavior | When an AMEND directive is present in the prompt (focus on one dimension, adjust severity thresholds), the output correctly narrows scope or recalibrates without losing inertia or risk anatomy. Pass if AMEND is applied correctly and inertia risk is retained even in a narrowed register. |
| C-11 | **Full mitigation specificity (zero-generic)** | depth | Every mitigation in the register names a concrete action, owner class, or control mechanism — no generic hedge language anywhere. Raises the C-05 bar from "fewer than 2 generic" to zero. Pass if a full scan of all mitigations finds no instance of "monitor closely," "keep an eye on," "revisit later," "consider alternatives," or equivalent non-actions. |
| C-12 | **All likelihoods are trigger-qualified** | depth | Every likelihood expression specifies a concrete triggering condition or scenario (not just "possible/unlikely/high/medium"). Raises the C-07 bar from ">= half" to all entries. Pass if every risk entry has a likelihood framed as a named condition or scenario rather than a bare probability label. |
| C-13 | **Interdependencies structured in a dedicated section** | depth | Risk interdependencies appear in a labeled section (not as inline footnotes or scattered notes), with at least two cross-risk links named. Raises the C-09 bar from "at least one" to "a structured section with >= 2 named dependencies." Pass if a dedicated interdependency section exists and names at least two compound-risk pairings. |
| C-14 | **Likelihoods use IF-THEN syntactic form** | depth | Every likelihood entry is written as "IF [named condition], THEN this risk activates" (or equivalent explicit IF-THEN phrasing). Bare probability labels ("high", "~30%", "possible") are absent from all entries. Raises the C-12 bar from "trigger-qualified" to "syntactically enforced IF-THEN form." Pass if every likelihood entry uses the IF...THEN construct — no bare label survives a full scan. |
| C-15 | **Mitigation type declared for every entry** | depth | Every mitigation begins with or explicitly names its type class (e.g., Spike, Validate, Gate, Contract, Cut, Instrument, or domain-equivalent taxonomy). The type is a positive structural claim, not merely the absence of generic language — a Spike requires a named unknown and time-box, a Gate requires a named criterion. Raises the C-11 bar from "zero-generic" to "positively typed." Pass if every mitigation carries a visible type label with its required sub-field contracts present in the prompt. |
| C-16 | **Interdependency count reaches specificity threshold** | depth | The dedicated interdependency section names at least 3 compound-risk pairings. The count functions as an indirect quality signal for the underlying register — only a sufficiently specific risk register generates 3 distinct pairings naturally. Raises the C-13 bar from >= 2 to >= 3 named pairs. Pass if the interdependency section lists at least 3 explicitly named compound-risk pairs. |
| C-17 | **Interdependency pairs carry severity-transition labels** | depth | Every compound-risk pair in the interdependency section states not only which risks are linked but also the severity transition that activation triggers (e.g., "IF Risk A activates, Risk B escalates from MEDIUM to HIGH"). A bare compound statement ("A compounds B" or "A worsens B") without a named severity transition fails. Raises the C-16 bar from ">= 3 named pairs" to ">= 3 pairs each with an explicit FROM/TO severity label." Pass if every interdependency pair in the section names both the linked risk and its severity escalation. |
| C-18 | **Mitigation type portfolio covers >= 3 distinct classes** | depth | The risk register uses at least 3 distinct type class names (from: Spike, Validate, Gate, Contract, Cut, Instrument) across its entries. A register where every mitigation uses the same type class is type-monoculture — the label is present (C-15 passes) but the taxonomy is not meaningfully applied. Raises the C-15 bar from "every entry has a type" to "the register's type distribution is substantively diverse." Pass if scanning all mitigation entries finds at least 3 distinct type class names in use. |
| C-19 | **Mitigation prohibition uses enumerated forbidden-phrase list** | depth | The prompt's mitigation quality gate names at least 3 specific forbidden hedge-phrases (e.g., "monitor closely", "keep an eye on", "revisit later", "consider alternatives") rather than describing the category conceptually. An enumerated list makes the prohibition testable without judgment; "avoid generic language" does not. Grounded in V-02's C-11 enforcement mechanism vs. V-01's conceptual gate. Raises C-11 from zero-generic-by-concept to zero-generic-by-enumeration. Pass if the prompt lists at least 3 specific forbidden phrases by name in its mitigation quality check. |
| C-20 | **Downstream count failure triggers upstream revision instruction** | depth | When a minimum-count gate (interdependency count, type diversity count) finds fewer items than required, the prompt instructs revision of the upstream section rather than accepting the gap or issuing a warning. "If you find fewer than 3 pairs, note the limitation" fails; "If you find fewer than 3 pairs, revise Step 2" passes. Grounded in V-03's back-pressure pattern: "If you cannot find any... revise Step 2." A prompt with no repair loop is self-reporting failure; a prompt with a repair loop is self-healing. Pass if at least one downstream minimum-count check includes an explicit instruction naming the upstream step to revise. |
| C-21 | **Repair-loop count matches minimum-count gate count** | depth | The prompt contains one repair loop for every minimum-count gate it introduces. A prompt with two gates (e.g., interdependency count + type diversity count) but only one repair loop leaves one gate without self-healing. Grounded in V-02's two-loop structure: a dedicated loop for interdependency count ("return to main register and add or refine entries") and a separate dedicated loop for type diversity ("return to main register and revise mitigations"). V-01, by contrast, has one gate without a corresponding second loop, which is why it fails C-18. Raises C-20 from "at least one repair loop" to "one repair loop per gate." Pass if the number of explicitly named repair instructions equals the number of minimum-count gates in the prompt. |
| C-22 | **Severity-transition columns are type-constrained at cell level** | depth | In the interdependency section, the From and To severity values are each governed by an explicit cell-level vocabulary rule restricting them to {HIGH, MEDIUM, LOW} — not simply illustrated by prose examples or implied by context. Cell-level type constraints make violations mechanically detectable without prose interpretation; a prose FROM/TO label (sufficient for C-17) still allows arbitrary text in the cell. Grounded in V-02's interdependency table where each From and To column "must contain exactly one of HIGH, MEDIUM, LOW" as a stated column rule. Raises C-17 from "prose FROM/TO severity-transition label required" to "typed column constraint with explicit cell-level vocabulary." Pass if the interdependency section defines From and To as vocabulary-constrained fields with the {HIGH, MEDIUM, LOW} set named as their complete allowed value set. |
| C-23 | **Repair loops are explicitly named with unique labels** | depth | Every repair loop in the prompt is assigned a unique human-readable label (e.g., "Repair Loop A", "Repair Loop B", or equivalent named designators) that appears in the prompt text, making each loop independently addressable by name and the total count unambiguous without inference. A prompt where repair loops exist only as unlabeled prose instructions requires a reader to infer their boundaries and count them; a prompt with named labels makes the count trivially verifiable. Grounded in V-03's explicit "Repair Loop A / Repair Loop B" structure, where the scorecard notes "explicit labeling makes count unambiguous." Raises C-21 from "count match" to "named-and-independently-addressable match." Pass if every repair loop carries a unique label that appears verbatim in the prompt text. |
| C-24 | **Complete mitigation type taxonomy pre-defined in the prompt** | depth | The prompt defines all 6 mitigation type classes (Spike, Validate, Gate, Contract, Cut, Instrument) together with their required sub-fields as a reference taxonomy — not just the types that happen to appear in the output. C-15 requires each output entry to carry its type and sub-field contracts; C-24 requires the prompt itself to provide a complete 6-class reference that the model draws from, preventing type omission at the source. A prompt that defines only the types it expects to use is subject to coverage gaps; a prompt with a complete reference taxonomy is closed under the type vocabulary. Grounded in V-02's complete definition: "Spike: Unknown/Time-box; Gate: Criterion; Validate: Assumption/Method; Contract: Party/Commitment; Cut: Element/Scope effect; Instrument: Metric/Alert threshold." Raises C-15 from "per-entry sub-field contracts present" to "full 6-class taxonomy pre-defined in one or more reference blocks." Pass if the prompt explicitly defines all 6 type classes with their sub-fields, regardless of which types appear in any given output. |
| C-25 | **Mitigation type diversity audit occupies a dedicated named step** | depth | The mitigation type diversity gate (C-18's >= 3 distinct class check and its repair loop) is isolated in its own dedicated named phase or step rather than embedded within the main risk-entry generation instructions. Isolation separates the generation concern (write risk entries) from the audit concern (check type distribution), making each step's purpose unambiguous and preventing the diversity check from being skipped when a model satisfies the generation step in one pass. Grounded in V-01's Phase 2b, which is a standalone phase solely for diversity auditing — distinct from the phase that produces risk entries. Raises C-18 from "audit gate exists with repair loop" to "audit gate is isolated in a dedicated named step." Pass if the prompt assigns the mitigation type diversity audit its own step number or phase label, separate from the step that generates risk entries. |

---

## Scoring Reference

| Outcome | Score Range |
|---------|-------------|
| Golden (all essential pass, composite >= 80) | 80–124 |
| Passing (all essential pass, composite < 80) | 60–79 |
| Failing (any essential fails) | 0–59 |

**Max composite**: 60 (essential) + 30 (recommended) + 34 (aspirational) = **124**

**Golden threshold**: all 5 essentials PASS **and** composite >= 80 (unchanged from v6).

### Quick Failure Modes

- Inertia risk missing or not first → C-01 fail → max score 48 (cannot reach golden)
```
