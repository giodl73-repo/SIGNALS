The rubric content was fully provided inline in the prompt — I have everything I need. Let me extract the new excellence patterns from the scorecard and write v5.

**New patterns grounded in Round 4 evidence:**

- **C-19**: V-02's C-11 enforcement used an enumerated forbidden-phrase list ("monitor closely", "keep an eye on", "revisit later", "consider alternatives") rather than a conceptual description. V-01's gate said "replace if ≥2 generic" but never named the phrases — so a LLM must infer what "generic" means. Enumeration makes the prohibition machine-testable.

- **C-20**: V-03's C-09 PASS was grounded in back-pressure language — "If you cannot find any... **revise Step 2**." This is structurally different from detection: the prompt compels upstream revision when a downstream count fails, rather than accepting the gap. No v4 criterion required this repair-loop pattern.

Both extend existing chains cleanly. Now writing the complete v5 rubric:

---

# Scout-Risk Rubric — v5

## What This Rubric Evaluates

A scout-risk prompt is evaluated on its ability to produce a well-structured risk register covering inertia risk, dimensional risks, and interdependencies. This rubric grades the prompt text — not a trace artifact.

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

## Aspirational Criteria (weight: 2 pts PASS / 1 pt PARTIAL / 0 pts FAIL each, 24 pts max)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Risk interdependencies noted** | depth | At least one risk entry notes how it compounds with or unlocks another (e.g., "If dependency risk materializes, timeline risk escalates to HIGH"). Pass if at least one cross-risk dependency is surfaced explicitly. |
| C-10 | **AMEND behavior demonstrated** | behavior | When an AMEND directive is present in the prompt (focus on one dimension, adjust severity thresholds), the output correctly narrows scope or recalibrates without losing inertia or risk anatomy. Pass if AMEND is applied correctly and inertia risk is retained even in a narrowed register. |
| C-11 | **Full mitigation specificity (zero-generic)** | depth | Every mitigation in the register names a concrete action, owner class, or control mechanism — no generic hedge language anywhere. Raises the C-05 bar from "fewer than 2 generic" to zero. Pass if a full scan of all mitigations finds no instance of "monitor closely," "keep an eye on," "revisit later," "consider alternatives," or equivalent non-actions. |
| C-12 | **All likelihoods are trigger-qualified** | depth | Every likelihood expression specifies a concrete triggering condition or scenario (not just "possible/unlikely/high/medium"). Raises the C-07 bar from ">= half" to all entries. Pass if every risk entry has a likelihood framed as a named condition or scenario rather than a bare probability label. |
| C-13 | **Interdependencies structured in a dedicated section** | depth | Risk interdependencies appear in a labeled section (not as inline footnotes or scattered notes), with at least two cross-risk links named. Raises the C-09 bar from "at least one" to "a structured section with >= 2 named dependencies." Pass if a dedicated interdependency section exists and names at least two compound-risk pairings. |
| C-14 | **Likelihoods use IF-THEN syntactic form** | depth | Every likelihood entry is written as "IF [named condition], THEN this risk activates" (or equivalent explicit IF-THEN phrasing). Bare probability labels ("high", "~30%", "possible") are absent from all entries. Raises the C-12 bar from "trigger-qualified" to "syntactically enforced IF-THEN form." Pass if every likelihood entry uses the IF...THEN construct — no bare label survives a full scan. |
| C-15 | **Mitigation type declared for every entry** | depth | Every mitigation begins with or explicitly names its type class (e.g., Spike, Validate, Gate, Contract, Cut, Instrument, or domain-equivalent taxonomy). The type is a positive structural claim, not merely the absence of generic language — a Spike requires a named unknown and time-box, a Gate requires a named criterion. Raises the C-11 bar from "zero-generic" to "positively typed." Pass if every mitigation carries a visible type label. |
| C-16 | **Interdependency count reaches specificity threshold** | depth | The dedicated interdependency section names at least 3 compound-risk pairings. The count functions as an indirect quality signal for the underlying register — only a sufficiently specific risk register generates 3 distinct pairings naturally. Raises the C-13 bar from >= 2 to >= 3 named pairs. Pass if the interdependency section lists at least 3 explicitly named compound-risk pairs. |
| C-17 | **Interdependency pairs carry severity-transition labels** | depth | Every compound-risk pair in the interdependency section states not only which risks are linked but also the severity transition that activation triggers (e.g., "IF Risk A activates, Risk B escalates from MEDIUM to HIGH"). A bare compound statement ("A compounds B" or "A worsens B") without a named severity transition fails. Raises the C-16 bar from ">= 3 named pairs" to ">= 3 pairs each with an explicit FROM/TO severity label." Pass if every interdependency pair in the section names both the linked risk and its severity escalation. |
| C-18 | **Mitigation type portfolio covers >= 3 distinct classes** | depth | The risk register uses at least 3 distinct type class names (from: Spike, Validate, Gate, Contract, Cut, Instrument) across its entries. A register where every mitigation uses the same type class is type-monoculture — the label is present (C-15 passes) but the taxonomy is not meaningfully applied. Raises the C-15 bar from "every entry has a type" to "the register's type distribution is substantively diverse." Pass if scanning all mitigation entries finds at least 3 distinct type class names in use. |
| C-19 | **Mitigation prohibition uses enumerated forbidden-phrase list** | depth | The prompt's mitigation quality gate names at least 3 specific forbidden hedge-phrases (e.g., "monitor closely", "keep an eye on", "revisit later", "consider alternatives") rather than describing the category conceptually. An enumerated list makes the prohibition testable without judgment; "avoid generic language" does not. Grounded in V-02's C-11 enforcement mechanism vs. V-01's conceptual gate. Raises C-11 from zero-generic-by-concept to zero-generic-by-enumeration. Pass if the prompt lists at least 3 specific forbidden phrases by name in its mitigation quality check. |
| C-20 | **Downstream count failure triggers upstream revision instruction** | depth | When a minimum-count gate (interdependency count, type diversity count) finds fewer items than required, the prompt instructs revision of the upstream section rather than accepting the gap or issuing a warning. "If you find fewer than 3 pairs, note the limitation" fails; "If you find fewer than 3 pairs, revise Step 2" passes. Grounded in V-03's back-pressure pattern: "If you cannot find any... revise Step 2." A prompt with no repair loop is self-reporting failure; a prompt with a repair loop is self-healing. Pass if at least one downstream minimum-count check includes an explicit instruction naming the upstream step to revise. |

---

## Scoring Reference

| Outcome | Score Range |
|---------|-------------|
| Golden (all essential pass, composite >= 80) | 80–114 |
| Passing (all essential pass, composite < 80) | 60–79 |
| Failing (any essential fails) | 0–59 |

**Max composite**: 60 (essential) + 30 (recommended) + 24 (aspirational) = **114**

**Golden threshold**: all 5 essentials PASS **and** composite >= 80 (unchanged from v4).

### Quick Failure Modes

- Inertia risk missing or not first → C-01 fail → max score 48 (cannot reach golden)
- Fewer than 3 dimensions covered → C-02 fail → cannot reach golden
- Any risk missing severity/likelihood/mitigation → C-03 fail → cannot reach golden
- All mitigations are generic → C-05 fail → cannot reach golden

---

## Criterion Ladder

Criteria are organized into escalating chains. Each level raises the bar of the one before it.

```
Mitigation specificity:
  C-05 → C-11 → C-19 → C-15 → C-18
  (≤1 generic) → (zero generic) → (enumerated prohibition) → (typed) → (type-diverse)

Likelihood precision:
  C-07 → C-12 → C-14
  (qualified ≥ half) → (all trigger-qualified) → (IF-THEN syntactic form)

Interdependency depth:
  C-09 → C-13 → C-16 → C-17 → C-20
  (≥1 mentioned) → (dedicated section ≥2 pairs) → (≥3 pairs) → (severity-labeled FROM/TO) → (self-repairing repair loop)
```

---

## v5 Changelog

**New criteria: C-19 and C-20**

**C-19 — Mitigation prohibition uses enumerated forbidden-phrase list**

Grounded in V-02 C-11 PARTIAL evidence: V-01's gate required replacement of generic mitigations but described the category conceptually — a LLM must infer what counts as generic. V-02 enumerated specific phrases ("monitor closely", "keep an eye on", "revisit later", "consider alternatives"), making the prohibition mechanically testable. C-11 tests whether generic language is absent; C-19 tests whether the prompt's *enforcement mechanism* is strong enough to produce that absence reliably. Raises C-11 from zero-generic-by-concept to zero-generic-by-enumeration.

**C-20 — Downstream count failure triggers upstream revision instruction**

Grounded in V-03 C-09 PASS evidence: "If you cannot find any [interdependencies]... revise Step 2." This formulation is structurally different from detection-only gates — it compels the model to revise upstream output rather than accept a sparse result. A prompt that says "note the limitation if fewer than 3 pairs" is self-reporting failure; a prompt that says "revise the register if fewer than 3 pairs" is self-healing. No v4 criterion required a repair-loop pattern. Extends the interdependency chain at C-17, applying back-pressure as the final quality mechanism.

**Updated ladder**:
```
C-05 → C-11 → C-19 → C-15 → C-18  (C-19 inserted between C-11 and C-15)
C-09 → C-13 → C-16 → C-17 → C-20  (C-20 extends chain beyond C-17)
C-07 → C-12 → C-14                  (unchanged)
```

**Scoring**: aspirational pool 10→12 criteria, max aspirational 20→24 pts, max composite 110→114. Golden threshold stays >= 80.
