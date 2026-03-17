Written to `simulations/quest/rubrics/org-review-rubric-v3-2026-03-16.md`.

---

**Rubric summary -- org-review v3**

| Tier | Criteria | Points | What they test |
|------|----------|--------|----------------|
| Essential | C-01 to C-05 | 60 | Role manifest, contract cites, CH-ID trace, gate vector, §3 algebra |
| Recommended | C-06 to C-08 | 30 | Artifact-specific scope, CH-ID-sourced register, concrete cross-role signals |
| Aspirational | C-09 to C-14 | **30** | Null hypothesis, role-grounded findings, structural convergence, count constraint, **register pattern**, **role-sequence isolation** |

**Max composite**: 120 (was 110). Golden threshold unchanged: all 5 essential + composite >= 80.

**What changed from v2:**

| New ID | Source | What it tests | Why aspirational |
|--------|--------|---------------|-----------------|
| C-13 | E-4 (V-05 NULL HYPOTHESIS REGISTER) | Pre-section register block + explicit anti-generic prohibition + downstream reference-by-copy converts any "name a concrete X" criterion from execution-dependent to template-determined | Requires a new register block in the template, not a phrasing fix |
| C-14 | E-3 (V-05 LIFECYCLE-before-DOMAIN resequencing) | Physical section order isolates commitment-readiness lens (LIFECYCLE, sees GOpen only) from technical depth lens (DOMAIN, sees G_lifecycle); prevents cross-contamination of findings | E-3 hypothesis -- confirmed at template-design level, not yet confirmed by execution comparison |

**Scoring formula update:**
```
aspirational_pass / 6 * 30   (was: / 4 * 20)
```
Per-criterion value stays at 5 pts; the tier now has six slots instead of four.

**Vacuous conditions added for C-13 and C-14:**
- C-13: register without an explicit anti-generic prohibition = FAIL (no PARTIAL credit)
- C-14: physical section ordering is the test; a note about commitment framing in a DOMAIN-first template does not satisfy C-14
002, ...) assigned in BRACKET OPENING appears in: (a) the DOMAIN CH-ID Response Table, (b) the LIFECYCLE CH-ID Response Table, and (c) the BRACKET CLOSING CH-ID Final Assessment. Missing any row in any table = fail. |
| C-04 | Gate vector table complete | format | GATE VECTOR TABLE has all four gates present: GOpen, G_domain (or G_domain Aggregate), G_lifecycle, GClose. Each gate has a named reviewer, a verdict (PASS / CONDITIONAL / FAIL), and a contract cite. No gate row is missing or blank. |
| C-05 | Disposition algebra applied mechanically | correctness | DISPOSITION section states each of {GOpen, G_domain_agg, G_lifecycle, GClose}, then evaluates the §3 formula explicitly (not editorially), and derives READY / CONDITIONAL / BLOCKED. The stated Overall Disposition is consistent with the formula output. |

### Recommended (output is better with these -- 30 pts total, 10 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Scope enumeration artifact-specific | depth | §1 IN-SCOPE surfaces are concrete and artifact-specific -- not generic ("all sections") or placeholder text. At least two distinct, named surfaces are listed. |
| C-07 | Action item register CH-ID sourced | correctness | Every PARTIAL or HOLDS CH-ID from BRACKET CLOSING Final Assessment has a corresponding row in the ACTION ITEM REGISTER with Disposition Class and Resolution Criterion filled. A HOLDS/PARTIAL CH-ID with no register row = fail. |
| C-08 | Cross-role signals are specific | depth | CROSS-ROLE SIGNALS section: CONVERGENCE names at least one CH-ID or finding echoed by two or more reviewers (not "None detected" if any convergence exists). CONFLICTS identifies any incompatible responses or writes "None detected" with justification. Neither field contains a placeholder. |

### Aspirational (raise the bar -- 30 pts total, 5 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Null hypothesis is specific and challenger-grounded | depth | The null hypothesis names the concrete alternative the team uses today (tool, process, or workaround) rather than a generic phrase like "do nothing" or "status quo". Null hypothesis strength (HIGH / MEDIUM / LOW) is justified in one sentence. |
| C-10 | Domain findings are role-grounded and in-scope | depth | Each Additional Finding in the DOMAIN section names an in-scope surface from §1 and is attributable to the role lens or expertise (not a generic observation any reviewer could make). At least two of three findings meet this bar. |
| C-11 | Convergence detection is structural via verdict-preview tables | structure | Prompt includes a verdict-preview table at one or more section headers (DOMAIN, LIFECYCLE, or BRACKET CLOSING) that pre-prints CH-ID rows with a Verdict column. The presence of this table makes cross-role convergence detection a table-scan operation rather than a synthesis inference. C-08 pass rate is not execution-dependent when this structure is present. Excellence signal: E-1 from Round 1 (V-04 sole discriminator, +10 pts vs all other variations). |
| C-12 | CH-ID forward-trace enforced by count constraint | structure | Prompt includes an explicit count instruction of the form "exactly N rows" (or equivalent numeric constraint) that binds the number of CH-ID rows in each downstream table to the count declared in BRACKET OPENING. A count mismatch is detectable as a numeric violation rather than a structural gap. Excellence signal: E-2 from Round 1 (stronger C-03 enforcement than imperative checkpoint alone). |
| C-13 | Concrete-naming criteria enforced via pre-section register pattern | structure | For at least one criterion requiring a named-concrete value (null hypothesis tool/process, scope surface, CH-ID actor), the prompt includes a dedicated register block that appears before the consuming section, explicitly prohibits generic substitutes ("do nothing", "status quo", "all sections") in the register instructions, and templates the consuming section's field to reference the register by copy (e.g., "from NULL HYPOTHESIS REGISTER -- do not substitute generic language"). The register + prohibition + downstream-reference must be present as a unit. Excellence signal: E-4 from Round 2 (V-05 NULL HYPOTHESIS REGISTER converts C-09 from execution-dependent to template-determined; generalizes to any "name a concrete X" criterion). |
| C-14 | Role-sequence isolation via LIFECYCLE-before-DOMAIN ordering | structure | Prompt sequences the LIFECYCLE reviewer section before the DOMAIN reviewer section. The LIFECYCLE section provides only GOpen as the pre-known gate result and constrains findings to commitment/program-readiness framing. The DOMAIN section receives G_lifecycle as a prior gate result, orienting technical findings toward LIFECYCLE-identified gaps. The resequencing is explicit in the template -- sections are labeled and ordered LIFECYCLE then DOMAIN, not DOMAIN then LIFECYCLE. Excellence signal: E-3 from Round 2 (V-05 structural hypothesis; structurally prevents commitment-readiness concerns from contaminating technical domain review and may improve C-10 role-grounding in execution). |

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 6 * 30)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential + >= 80 | Ready to use as golden prompt |
| Passing | all essential + 60-79 | Structurally sound, depth gaps |
| Borderline | 4 essential + any score | One essential gap -- not usable without fix |
| Failing | <= 3 essential | Contract or CH-ID trace broken -- output not useful |

---

## Vacuous Conditions

- C-07: If BRACKET CLOSING shows all CH-IDs DEFEATED, the register may contain only ADVISORY-OBS
  rows. Pass if register is present and DEFEATED status is consistent with the rows (or lack thereof).
- C-08: If the artifact generates only one CH-ID, CONVERGENCE field may legitimately be
  "None detected" -- do not penalize if single-claim review has no multi-role echo.
- C-10: If --depth deep adds DOMAIN-2 or DOMAIN-3 sections, evaluate C-10 against the
  primary DOMAIN section only.
- C-11: If the prompt uses a different structural mechanism that makes convergence a scan rather
  than inference (e.g., a running tally column in the CROSS-ROLE SIGNALS section), credit C-11
  if the mechanism is pre-printed in the template and not dependent on model synthesis.
- C-12: Count constraint must bind at template generation time (N is filled from the declared
  CH-ID count before the model runs). A post-hoc instruction ("count the rows above") does not
  satisfy C-12.
- C-13: A register that prompts for a concrete value but does not explicitly prohibit generic
  substitutes does not satisfy C-13. The prohibition must be stated; PARTIAL credit is not awarded.
- C-14: A prompt that sequences DOMAIN before LIFECYCLE but adds a note about commitment framing
  does not satisfy C-14. Physical section ordering is the test -- the template must present
  LIFECYCLE first.

---

## Notes for Scorers

- C-03 is the most commonly failed criterion in early runs. Look for CH-ID rows silently dropped
  between BRACKET OPENING and downstream tables.
- C-05 fails when the model writes "Given the findings above, the disposition is CONDITIONAL"
  without evaluating the gate vector formula. The formula must appear explicitly.
- C-09 is aspirational because it requires the model to interpret the artifact domain and
  generate a plausible inertia alternative -- genuine judgment, not template-filling. C-13 is
  the structural mechanism that elevates C-09 from execution-dependent to template-determined.
- C-11 and C-12 are aspirational because they require structural changes to the prompt template
  itself, not phrasing improvements. They are the patterns that elevated V-04 to 100 in Round 2
  and are the primary Round 2 confirmed engineering achievements.
- C-13 generalizes the NULL HYPOTHESIS REGISTER pattern from V-05 Round 2. Any criterion of the
  form "name a concrete X" (tool, surface, actor, process) can be elevated from execution-dependent
  to template-determined by: (1) creating a dedicated register block before the consuming section,
  (2) explicitly prohibiting generic substitutes in the register instructions, and (3) templating
  downstream fields to reference the register by copy. Candidates for this treatment in future
  rounds: C-06 scope surfaces, C-07 CH-ID sourced action items.
- C-14 is the Round 2 structural hypothesis (E-3) not yet confirmed at execution level. It is
  aspirational because V-04-vs-V-05 output comparison at execution time is needed to isolate the
  role-sequence effect from the NULL HYPOTHESIS REGISTER effect (E-4). Confirmed at
  template-design level: the resequencing is present and coherent in V-05.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-16 | Initial rubric -- 10 criteria, max 100 |
| v2 | 2026-03-16 | Add C-11 (verdict-preview tables) and C-12 (count constraint) from Round 1 excellence signals E-1 and E-2; aspirational tier expands to 4 criteria, 20 pts; max composite 110 |
| v3 | 2026-03-16 | Add C-13 (pre-section register pattern) and C-14 (LIFECYCLE-before-DOMAIN ordering) from Round 2 excellence signals E-4 and E-3; aspirational tier expands to 6 criteria, 30 pts; max composite 120 |
