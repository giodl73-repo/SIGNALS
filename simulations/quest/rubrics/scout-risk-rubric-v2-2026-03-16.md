Rubric written to `simulations/quest/rubrics/scout-risk-rubric-v2-2026-03-16.md`.

**5 essential, 3 recommended, 5 aspirational.**

Three new aspirational criteria added from Round 1 excellence signals:

| ID | Source | What it captures |
|----|--------|------------------|
| **C-11** | V-03 C-05 PASS | Zero-generic mitigations — raises C-05's "fewer than 2" bar to zero tolerance across the full register |
| **C-12** | V-03 C-07 PASS | All likelihoods trigger-qualified — raises C-07's ">= half" bar to every entry |
| **C-13** | V-02 C-09 PARTIAL | Interdependencies in a dedicated section with >= 2 named links — raises C-09's single-mention bar to structured section |

Each new criterion is explicitly anchored to the existing criterion it upgrades, so the ladder is clear: pass the essential/recommended bar, then earn the aspirational upgrade. The score formula self-adjusts (aspirational pool is now 10 points split across 5 criteria at 2 points each).
 is absent or buried. |
| C-02 | **Multi-dimensional coverage** | coverage | Output includes risks from at least 3 of the 5 required dimensions: technical, market, compliance, dependency, timeline. Fail if fewer than 3 dimensions are represented. |
| C-03 | **Risk anatomy complete** | correctness | Every risk entry includes all three required fields: severity (HIGH/MEDIUM/LOW), likelihood (any meaningful expression of probability or triggering condition), and mitigation (a stated action or control). Fail if any risk is missing one or more fields. |
| C-04 | **Severity uses correct scale** | format | Severity values are drawn exclusively from {HIGH, MEDIUM, LOW}. No numeric scales, percentages, or invented labels. Fail if any severity value deviates from this vocabulary. |
| C-05 | **Mitigations are specific and actionable** | depth | Each mitigation describes a concrete action, owner class, or control — not a generic hedge ("monitor closely", "be careful"). A passing mitigation names what to do or what to watch, not just that something should happen. Fail if two or more mitigations are generic non-actions. |

---

## Recommended Criteria (weight: 30 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Risks are dimension-labeled** | format | Each risk entry is explicitly tagged with its dimension (e.g., "Technical", "Market", "Compliance", "Dependency", "Timeline"). Pass if >= 80% of risks carry a visible dimension label. |
| C-07 | **Likelihood is qualified beyond binary** | depth | Likelihood expressions go beyond "possible/unlikely" — they specify a condition, scenario, or rough probability bracket (e.g., "high if team has no prior SDK experience", "~30% given current adoption curve"). Pass if >= half of risks meet this bar. |
| C-08 | **Risks are ordered by priority** | behavior | The register is ordered highest-to-lowest severity (after inertia), or explicitly states a prioritization logic. A randomly ordered flat list fails. Pass if the ordering is defensible by severity or compound impact. |

---

## Aspirational Criteria (weight: 10 points total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Risk interdependencies noted** | depth | At least one risk entry notes how it compounds with or unlocks another (e.g., "If dependency risk materializes, timeline risk escalates to HIGH"). Pass if at least one cross-risk dependency is surfaced explicitly. |
| C-10 | **AMEND behavior demonstrated** | behavior | When an AMEND directive is present in the prompt (focus on one dimension, adjust severity thresholds), the output correctly narrows scope or recalibrates without losing inertia or risk anatomy. Pass if AMEND is applied correctly and inertia risk is retained even in a narrowed register. |
| C-11 | **Full mitigation specificity (zero-generic)** | depth | Every mitigation in the register names a concrete action, owner class, or control mechanism — no generic hedge language anywhere. Raises the C-05 bar from "fewer than 2 generic" to zero. Pass if a full scan of all mitigations finds no instance of "monitor closely," "keep an eye on," "revisit later," "consider alternatives," or equivalent non-actions. |
| C-12 | **All likelihoods are trigger-qualified** | depth | Every likelihood expression specifies a concrete triggering condition or scenario (not just "possible/unlikely/high/medium"). Raises the C-07 bar from ">= half" to all entries. Pass if every risk entry has a likelihood framed as a named condition or scenario rather than a bare probability label. |
| C-13 | **Interdependencies structured in a dedicated section** | depth | Risk interdependencies appear in a labeled section (not as inline footnotes or scattered notes), with at least two cross-risk links named. Raises the C-09 bar from "at least one" to "a structured section with >= 2 named dependencies." Pass if a dedicated interdependency section exists and names at least two compound-risk pairings. |

---

## Scoring Reference

| Outcome | Score Range |
|---------|-------------|
| Golden (all essential pass, composite >= 80) | 80-100 |
| Passing (all essential pass, composite < 80) | 60-79 |
| Failing (any essential fails) | 0-59 |

### Quick Failure Modes

- Inertia risk missing or not first → C-01 fail → max score 48 (cannot reach golden)
- Fewer than 3 dimensions covered → C-02 fail → cannot reach golden
- Any risk missing severity/likelihood/mitigation → C-03 fail → cannot reach golden
- All mitigations are generic → C-05 fail → cannot reach golden

---

## Version Notes

**v2 (2026-03-16)**: Added C-11, C-12, C-13 from Round 1 excellence signals.

- **C-11** traces to V-03 C-05 PASS — the explicit re-read gate with multiple named negative examples demonstrated that zero-generic is achievable when a prompt enforces it. C-11 captures that bar as an aspirational output target (raises C-05's "fewer than 2" to zero).
- **C-12** traces to V-03 C-07 PASS — trigger-condition framing ("what specific condition or scenario triggers this risk") reliably produces fully qualified likelihoods across all entries, not just half. C-12 raises the C-07 ceiling from the half-threshold to all entries.
- **C-13** traces to V-02 C-09 PARTIAL — the optional dedicated interdependency section is structurally superior to scattered inline notes and enables downstream risk-chain analysis. C-13 rewards section-level structure and requires >= 2 named dependencies (raises C-09's single-link bar).
