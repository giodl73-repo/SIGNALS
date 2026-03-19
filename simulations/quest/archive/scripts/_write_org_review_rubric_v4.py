content = r"""# Rubric -- org-review v4

**Rubric summary**

| Tier | Criteria | Points | What they test |
|------|----------|--------|----------------|
| Essential | C-01 to C-05 | 60 | Role manifest, contract cites, CH-ID trace, gate vector, §3 algebra |
| Recommended | C-06 to C-08 | 30 | Artifact-specific scope, CH-ID-sourced register, concrete cross-role signals |
| Aspirational | C-09 to C-17 | **45** | Null hypothesis, role-grounded findings, structural convergence, count constraint, register pattern, role-sequence isolation, **register generalization**, **finding surface linkage**, **severity audit chain** |

**Max composite**: 135 (was 120). Golden threshold unchanged: all 5 essential + composite >= 80.

**What changed from v3:**

| New ID | Source | What it tests | Why aspirational |
|--------|--------|---------------|-----------------|
| C-15 | E-5 (V-01 SCOPE SURFACE REGISTER) | Pre-section register + anti-generic prohibition + downstream-reference-by-copy applied to two or more distinct concrete-naming criteria simultaneously; confirms the pattern is a reusable structural primitive, not a one-off for null hypothesis | Requires two complete register units in the same template, not a phrasing fix or single-instance reuse |
| C-16 | E-6 (V-02 FINDING SURFACE LINKAGE TABLE) | A pre-printed table in each reviewer section with columns Finding / In-Scope Surface / Role Lens / Severity converts C-10 role-grounded findings from execution-dependent (reviewer inference) to template-determined (blank-cell violation) | Requires a structural table schema added to each reviewer section; elevates C-10 to template-determined |
| C-17 | E-7 (V-03 PER-FINDING SEVERITY AGGREGATION) | A §2a formula in the immutable contract block creates a formula-mechanical audit chain: individual finding severity tag -> worst(severities) aggregation -> Section Severity -> gate verdict; the chain is as binding as §3 | Requires a new §2a clause in the contract block and severity tags in every finding row |

**Scoring formula update:**
```
aspirational_pass / 9 * 45   (was: / 6 * 30)
```
Per-criterion value stays at 5 pts; the tier now has nine slots instead of six.

**Vacuous conditions added for C-15, C-16, and C-17:**
- C-15: If the artifact type has fewer than two concrete-naming criteria, score C-15 as N/A and exclude from denominator. Two qualifying criteria are required; a single register instance satisfies C-13 only.
- C-16: Structure (columns) must be pre-printed in the template. A prose-only finding section with inline severity tags does not satisfy C-16 even if role lens is mentioned.
- C-17: The §2a gate-verdict mapping must be stated explicitly in the contract block. An editorial instruction ("Section Severity informs the reviewer's judgment") = FAIL; no PARTIAL credit.

---

## Criteria

### Essential (output is invalid without these -- 60 pts total, 12 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Role manifest present | format | BRACKET OPENING names a distinct reviewer for each gate section: one LIFECYCLE reviewer and one or more DOMAIN reviewers. Each reviewer has a named role title (not a placeholder). |
| C-02 | Contract cites appear in findings | correctness | At least one CH-ID response in DOMAIN and at least one in LIFECYCLE cites a contract clause (§1, §2, §3, or a named gate) as the basis for PASS / CONDITIONAL / FAIL. A finding that states a verdict without any contract reference = fail. |
| C-03 | CH-ID forward-trace complete | correctness | Every CH-ID (CH-001, CH-002, ...) assigned in BRACKET OPENING appears in: (a) the DOMAIN CH-ID Response Table, (b) the LIFECYCLE CH-ID Response Table, and (c) the BRACKET CLOSING CH-ID Final Assessment. Missing any row in any table = fail. |
| C-04 | Gate vector table complete | format | GATE VECTOR TABLE has all four gates present: GOpen, G_domain (or G_domain Aggregate), G_lifecycle, GClose. Each gate has a named reviewer, a verdict (PASS / CONDITIONAL / FAIL), and a contract cite. No gate row is missing or blank. |
| C-05 | Disposition algebra applied mechanically | correctness | DISPOSITION section states each of {GOpen, G_domain_agg, G_lifecycle, GClose}, then evaluates the §3 formula explicitly (not editorially), and derives READY / CONDITIONAL / BLOCKED. The stated Overall Disposition is consistent with the formula output. |

### Recommended (output is better with these -- 30 pts total, 10 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Scope enumeration artifact-specific | depth | §1 IN-SCOPE surfaces are concrete and artifact-specific -- not generic ("all sections") or placeholder text. At least two distinct, named surfaces are listed. |
| C-07 | Action item register CH-ID sourced | correctness | Every PARTIAL or HOLDS CH-ID from BRACKET CLOSING Final Assessment has a corresponding row in the ACTION ITEM REGISTER with Disposition Class and Resolution Criterion filled. A HOLDS/PARTIAL CH-ID with no register row = fail. |
| C-08 | Cross-role signals are specific | depth | CROSS-ROLE SIGNALS section: CONVERGENCE names at least one CH-ID or finding echoed by two or more reviewers (not "None detected" if any convergence exists). CONFLICTS identifies any incompatible responses or writes "None detected" with justification. Neither field contains a placeholder. |

### Aspirational (raise the bar -- 45 pts total, 5 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Null hypothesis is specific and challenger-grounded | depth | The null hypothesis names the concrete alternative the team uses today (tool, process, or workaround) rather than a generic phrase like "do nothing" or "status quo". Null hypothesis strength (HIGH / MEDIUM / LOW) is justified in one sentence. |
| C-10 | Domain findings are role-grounded and in-scope | depth | Each Additional Finding in the DOMAIN section names an in-scope surface from §1 and is attributable to the role lens or expertise (not a generic observation any reviewer could make). At least two of three findings meet this bar. |
| C-11 | Convergence detection is structural via verdict-preview tables | structure | Prompt includes a verdict-preview table at one or more section headers (DOMAIN, LIFECYCLE, or BRACKET CLOSING) that pre-prints CH-ID rows with a Verdict column. The presence of this table makes cross-role convergence detection a table-scan operation rather than a synthesis inference. C-08 pass rate is not execution-dependent when this structure is present. Excellence signal: E-1 from Round 1 (V-04 sole discriminator, +10 pts vs all other variations). |
| C-12 | CH-ID forward-trace enforced by count constraint | structure | Prompt includes an explicit count instruction of the form "exactly N rows" (or equivalent numeric constraint) that binds the number of CH-ID rows in each downstream table to the count declared in BRACKET OPENING. A count mismatch is detectable as a numeric violation rather than a structural gap. Excellence signal: E-2 from Round 1 (stronger C-03 enforcement than imperative checkpoint alone). |
| C-13 | Concrete-naming criteria enforced via pre-section register pattern | structure | For at least one criterion requiring a named-concrete value (null hypothesis tool/process, scope surface, CH-ID actor), the prompt includes a dedicated register block that appears before the consuming section, explicitly prohibits generic substitutes ("do nothing", "status quo", "all sections") in the register instructions, and templates the consuming section's field to reference the register by copy (e.g., "from NULL HYPOTHESIS REGISTER -- do not substitute generic language"). The register + prohibition + downstream-reference must be present as a unit. Excellence signal: E-4 from Round 2 (V-05 NULL HYPOTHESIS REGISTER converts C-09 from execution-dependent to template-determined; generalizes to any "name a concrete X" criterion). |
| C-14 | Role-sequence isolation via LIFECYCLE-before-DOMAIN ordering | structure | Prompt sequences the LIFECYCLE reviewer section before the DOMAIN reviewer section. The LIFECYCLE section provides only GOpen as the pre-known gate result and constrains findings to commitment/program-readiness framing. The DOMAIN section receives G_lifecycle as a prior gate result, orienting technical findings toward LIFECYCLE-identified gaps. The resequencing is explicit in the template -- sections are labeled and ordered LIFECYCLE then DOMAIN, not DOMAIN then LIFECYCLE. Excellence signal: E-3 from Round 2 (V-05 structural hypothesis; structurally prevents commitment-readiness concerns from contaminating technical domain review and may improve C-10 role-grounding in execution). |
| C-15 | Register pattern generalized to two or more concrete-naming criteria | structure | The pre-section register + anti-generic prohibition + downstream-reference-by-copy unit (defined in C-13) appears for at least two distinct concrete-naming criteria in the same prompt. The minimum qualifying pair is a NULL HYPOTHESIS REGISTER (satisfying C-13) and a SCOPE SURFACE REGISTER (or equivalent register for any second criterion requiring a named-concrete value). Each instance must independently satisfy the C-13 unit test. Excellence signal: E-5 from Round 3 (V-01 SCOPE SURFACE REGISTER confirms the register pattern is a reusable structural primitive, not a single-use mechanism; first demonstration that two simultaneous register instances co-exist without conflict). |
| C-16 | Finding surface linkage via pre-printed table schema | structure | Prompt includes a FINDING SURFACE LINKAGE TABLE (or equivalently structured table) in each reviewer section with at least the columns: Finding, In-Scope Surface, Role Lens, Severity. The table is pre-printed as a template; a row with a blank In-Scope Surface or blank Role Lens cell is a detectable template violation rather than a scoring inference. C-10 is thereby elevated from execution-dependent to template-determined. Excellence signal: E-6 from Round 3 (V-02 FINDING SURFACE LINKAGE TABLE makes role-grounding a cell-completeness check; Role Lens column binds reviewer attribution to table schema; In-Scope Surface column creates explicit finding-to-scope-surface traceability). |
| C-17 | Per-finding severity audit chain anchored in contract block | structure | Prompt places a §2a formula in the immutable contract block that defines: (a) each finding carries a severity tag drawn from {CRITICAL, MAJOR, MINOR, ADVISORY}, (b) Section Severity = worst(finding severities) over all findings in the section, (c) gate verdict derives from Section Severity per a stated deterministic mapping. The chain -- individual finding severity tag to Section Severity to gate verdict -- is formula-mechanical and auditable without editorial judgment. §2a in the contract block makes this chain as binding as §3. Excellence signal: E-7 from Round 3 (V-03 per-finding severity aggregation converts gate verdicts from editorial to contractually-enforced; first demonstration that the immutable contract block can anchor a multi-step aggregation formula upstream of §3). |

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 9 * 45)
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
- C-15: If the artifact type has fewer than two concrete-naming criteria (e.g., no scope surface
  enumeration requirement), score C-15 as N/A and exclude from the aspirational denominator.
  Adjust formula to aspirational_pass / 8 * 40 when C-15 is N/A.
- C-16: Structure (columns) must be pre-printed in the template as a header row or instruction
  table. A prose finding section that mentions role lens inline does not satisfy C-16, even if
  all findings happen to be role-grounded. Blank cells are the detection mechanism; prose does
  not produce blank cells.
- C-17: The §2a severity-to-verdict mapping must be stated as a deterministic rule in the
  contract block (e.g., "CRITICAL finding in any section = FAIL gate; MAJOR = CONDITIONAL").
  An editorial instruction ("high-severity findings may warrant CONDITIONAL") = FAIL; no
  PARTIAL credit.

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
  form "name a concrete X" (tool, surface, actor, process) can be elevated from
  execution-dependent to template-determined by: (1) creating a dedicated register block before
  the consuming section, (2) explicitly prohibiting generic substitutes in the register
  instructions, and (3) templating downstream fields to reference the register by copy.
- C-14 is the Round 2 structural hypothesis (E-3) not yet confirmed at execution level. It is
  aspirational because V-04-vs-V-05 output comparison at execution time is needed to isolate the
  role-sequence effect from the NULL HYPOTHESIS REGISTER effect (E-4). Confirmed at
  template-design level: the resequencing is present and coherent in V-05.
- C-15 is the first Round 3 confirmation. E-5 (V-01) shows that two simultaneous register
  instances (NULL HYPOTHESIS REGISTER + SCOPE SURFACE REGISTER) co-exist without conflict and
  each independently satisfies the C-13 unit test. This confirms the pattern is a structural
  primitive, not a single-criterion accommodation. Future candidates for a third register
  instance: CH-ID actor (C-07 sourcing), convergence anchor (C-08).
- C-16 is the finding-side complement to C-11 (convergence side). C-11 makes cross-role
  aggregation structural; C-16 makes individual finding attribution structural. Together they
  close the gap between "findings exist" and "findings are traceable to role + scope surface".
  The blank-cell detection mechanism is what makes C-16 template-determined: a model cannot
  skip the In-Scope Surface column without producing a visible empty cell.
- C-17 introduces a second formula anchor in the contract block (§2a, upstream of §3). The
  design principle is that any judgment call that can be expressed as a deterministic function
  of tagged inputs should be placed in the immutable contract block. §2a is to gate verdicts
  what §3 is to disposition: it removes editorial variance at the derivation step.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-16 | Initial rubric -- 10 criteria, max 100 |
| v2 | 2026-03-16 | Add C-11 (verdict-preview tables) and C-12 (count constraint) from Round 1 excellence signals E-1 and E-2; aspirational tier expands to 4 criteria, 20 pts; max composite 110 |
| v3 | 2026-03-16 | Add C-13 (pre-section register pattern) and C-14 (LIFECYCLE-before-DOMAIN ordering) from Round 2 excellence signals E-4 and E-3; aspirational tier expands to 6 criteria, 30 pts; max composite 120 |
| v4 | 2026-03-16 | Add C-15 (register pattern generalization) from E-5 (V-01 Round 3), C-16 (finding surface linkage table) from E-6 (V-02 Round 3), C-17 (per-finding severity audit chain) from E-7 (V-03 Round 3); aspirational tier expands to 9 criteria, 45 pts; max composite 135 |
"""

with open('C:/src/sim/simulations/quest/rubrics/org-review-rubric-v4-2026-03-16.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
