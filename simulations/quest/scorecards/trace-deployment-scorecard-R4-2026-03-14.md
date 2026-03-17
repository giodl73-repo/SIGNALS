## Quest Score — trace-deployment Round 4

**Rubric**: v4 (135 pts) | All predictions matched.

### Composite Ranking

| Rank | Variation | Score | Golden | Predicted |
|------|-----------|-------|--------|-----------|
| 1 (tie) | V-02: Gate-Free Fields + Front-Loaded Skeleton | **125** | YES | 125 |
| 1 (tie) | V-03: Single-Sentence Prose Saturation | **125** | YES | 125 |
| 1 (tie) | V-04: Adversarial Two-Pass + Gate-Free + Skeleton | **125** | YES | 125 |
| 1 (tie) | V-05: Inertia Framing + Prose Saturation | **125** | YES | 125 |
| 5 | V-01: Gate-Free Fields, No Skeleton | **120** | YES | 120 |

All 5 golden. 5/5 predictions matched.

---

### Three R4 Questions — Answered

**Q1: Can C-14 and C-16 coexist?** YES — V-02 and V-04 both hit C-14 PASS + C-16 PASS simultaneously. The skeleton (C-14) is a commitment device; the gate-free requirement (C-16) targets "GATE N: Do not proceed until..." enforcement blocks specifically. Orthogonal properties. V-01 + skeleton = +5 pts, zero cost to C-16.

**Q2: Does C-17 hold at single-sentence density?** YES — V-03 packs all three C-15 requirements into one sentence per phase via semicolons. Below single-paragraph threshold and still satisfies C-17. Specificity is the floor, not density.

**Q3: Does inertia framing satisfy C-15's disqualifier requirement?** YES — contextual failure-mode disqualifiers ("'someone notices it looks bad' does not pass") satisfy C-15 with equal force to abstract pattern disqualifiers. Disqualifier source is not load-bearing.

---

### New Patterns

- **`skeleton-and-gate-free-orthogonal`** — C-14 (skeleton commitment device) and C-16 (gate-free field scaffolding) test orthogonal structural properties; a front-loaded empty table with a do-not-pre-fill guard is not GATE enforcement text; both pass simultaneously without compromise
- **`inertia-framing-disqualifier-passes-c15`** — contextual failure-mode disqualifiers satisfy C-15's disqualifying-example requirement with equivalent force to abstract pattern disqualifiers; disqualifier source is not load-bearing for C-15 compliance

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["skeleton-and-gate-free-orthogonal", "inertia-framing-disqualifier-passes-c15"]}
```
tment device) and C-16 (gate-free
  field scaffolding) test orthogonal structural properties; a front-loaded empty table with a
  do-not-pre-fill guard is not GATE enforcement text, and both criteria pass simultaneously without
  compromise (V-02, V-04)
- **`inertia-framing-disqualifier-passes-c15`** — contextual failure-mode disqualifiers
  ("'someone notices it looks bad' does not pass") satisfy C-15's disqualifying-example requirement
  with equivalent force to abstract pattern disqualifiers; disqualifier source is not load-bearing
  for C-15 compliance (V-05)

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["skeleton-and-gate-free-orthogonal", "inertia-framing-disqualifier-passes-c15"]}
```

---

### Cross-Variation Criterion Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |
| C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| **C-14** | **FAIL** | **PASS** | FAIL | **PASS** | FAIL |
| **C-15** | FAIL | FAIL | **PASS** | FAIL | **PASS** |
| **C-16** | **PASS** | **PASS** | FAIL | **PASS** | FAIL |
| **C-17** | FAIL | FAIL | **PASS** | FAIL | **PASS** |
| **Score** | **120** | **125** | **125** | **125** | **125** |

Structural split confirmed: C-16 requires template field scaffolding (blocks C-15/C-17); C-15
requires absence of template apparatus (blocks C-16). C-14 and C-16 are compatible. C-15 and C-17
are compatible. The two architectural paths (structural vs. prose) reach identical ceilings at
125/135.

---

### V-01: Gate-Free Fields + Automation Hooks, No Skeleton

**Axis**: Gate markers stripped; automation hook fields restored (Hook-NN in Phase 2 and Phase 3).
Minimal delta from R3 V-01 to add C-16 PASS without skeleton.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Check-01/02/03 fields with Pass and Failure conditions. "(Add Check-04+ as needed)" extends count floor. No GATE text needed -- field presence is sufficient. |
| C-02 | **PASS** | Step-01/02/03/04 fields with Output and Precondition. Count floor met by field scaffolding. |
| C-03 | **PASS** | Validation-01/02 fields with Expected and Failure indicator. "(Add Validation-03+ as needed)" extends floor. |
| C-04 | **PASS** | Trigger field with "not 'if deployment fails'" exclusion; Rollback-01/02 fields; Verification field. All four rollback elements present. |
| C-05 | **PASS** | Gap block (Missing / Fix / Severity) per phase x4. All four phases have gap structure without GATE enforcement. |
| C-06 | **PASS** | "Ordering dependency: Step-X must precede Step-Y: [step numbers -- explicit reason, not sequential position]" -- explicit reason required by field label. |
| C-07 | **PASS** | ROLE block lists 11 Commerce/Operations vocabulary terms. Domain anchoring present. |
| C-08 | **PASS** | "Fix: [Specific change -- not just a label]" per gap. Label-only responses barred by field instruction. |
| C-09 | **PASS** | Gap summary table (Rank / Phase / Gap summary / Severity / Why this rank) + "must compare this gap against the others -- not justify the phase's severity in isolation." |
| C-10 | **PASS** | Hook-01 in Phase 2 (CI gate or pre-deploy script) and Phase 3 (canary assertion or health probe) with Currently field. R3 finding confirmed: restoring hook fields recovers C-10 at zero other cost. |
| C-11 | **PASS** | Named vocabulary list in ROLE block. Role-block placement. |
| C-12 | **PASS** | "Current practice: [...]" and "Known failure mode: [...]" named fields in ROLE with reference instruction. Baseline present before Phase 1. |
| C-13 | **PASS** | Post-trace gap summary table with all required columns. Cross-phase rollup present. |
| C-14 | **FAIL** | No front-loaded skeleton before Phase 1. Gap summary table appears after Phase 4 only. No do-not-pre-fill guard. |
| C-15 | **FAIL** | Named section headers (ROLE, PHASE 1-4), template fields (Check-NN, Step-NN, Validation-NN, Hook-NN), Gap sub-fields constitute structural apparatus. Prose-alone path blocked. |
| C-16 | **PASS** | No GATE enforcement text. Hook-01 in Phase 2 and Phase 3. Field count floors met: >=3 Check-NN, >=4 Step-NN, >=2 Validation-NN, Trigger + Rollback-NN + Verification, gap block per phase. Gate-free architecture with automation hook fields -- C-16 pass condition confirmed. |
| C-17 | **FAIL** | C-15 FAIL -> C-17 cannot pass. |

**Score: 120 / 135** | All essential PASS | **Golden: YES**

*Finding: V-01 is the minimal gate-free structural path. Restoring Hook-NN fields (stripped in R3
V-01) recovers C-10 cleanly. C-16 PASS confirms: field count alone is structurally sufficient for
essential coverage; GATE enforcement text is optional apparatus. C-14 and C-15 both fail for the
same reason as R3 V-01: no skeleton, and template apparatus blocks prose path.*

---

### V-02: Gate-Free Fields + Front-Loaded Skeleton (C-14 + C-16 Ceiling Test)

**Axis**: V-01 + front-loaded GAP PLAN skeleton (empty table before Phase 1, do-not-pre-fill
guard, comparative return instruction). Tests C-14 and C-16 compatibility.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Check-01/02/03 fields with Pass and Failure conditions. Count floor met by field scaffolding. |
| C-02 | **PASS** | Step-01/02/03/04 fields with Output and Precondition. |
| C-03 | **PASS** | Validation-01/02 fields with Expected and Failure indicator. |
| C-04 | **PASS** | Trigger (with "not 'if deployment fails'" exclusion) + Rollback-01/02 + Verification. |
| C-05 | **PASS** | Gap block (Missing / Fix / Severity) per phase x4. |
| C-06 | **PASS** | Ordering dependency field with explicit reason required. |
| C-07 | **PASS** | Vocabulary list in ROLE block. Inertia-framing addition to role persona does not affect C-11 or C-07. |
| C-08 | **PASS** | "Fix: [Specific change -- not just a label]" per gap. |
| C-09 | **PASS** | GAP PLAN table (Rank / Phase / Gap summary / Severity / Why this rank) + comparative mandate in skeleton header and return instruction. |
| C-10 | **PASS** | Hook-01 in Phase 2 and Phase 3. |
| C-11 | **PASS** | Named vocabulary list in ROLE block. |
| C-12 | **PASS** | "Current practice: [...]" and "Known failure mode: [...]" in ROLE. |
| C-13 | **PASS** | Front-loaded GAP PLAN table with required columns, returned to after Phase 4. |
| C-14 | **PASS** | GAP PLAN skeleton placed before PHASE 1. "Leave all rows blank. Do not pre-fill before tracing." (do-not-pre-fill guard). Return instruction: "The 'Why this rank' column must compare this gap against the others across all four phases -- not justify the phase's severity in isolation." (comparative cross-phase mandate). "Proceed to PHASE 1." separator. All three C-14 requirements met. |
| C-15 | **FAIL** | Named section headers (ROLE, GAP PLAN, PHASE 1-4), template fields (Check-NN, Step-NN, Validation-NN, Hook-NN), Gap sub-fields constitute structural apparatus. C-15 requires absence of apparatus. |
| C-16 | **PASS** | No GATE enforcement text. Hook-01 in Phase 2 and Phase 3. Field count floors met. Gate-free confirmed. Critical finding: the front-loaded skeleton is NOT GATE enforcement text -- it is a structural commitment device. C-14 and C-16 pass simultaneously without conflict. |
| C-17 | **FAIL** | C-15 FAIL -> C-17 cannot pass. |

**Score: 125 / 135** | All essential PASS | **Golden: YES**

*Finding: C-14 and C-16 are structurally orthogonal. The "gate-free" requirement in C-16 targets
GATE enforcement text specifically ("GATE N: Do not proceed until..."). The skeleton's do-not-pre-
fill guard and return instruction are commitment architecture, not enforcement text. Both criteria
pass simultaneously. V-02 is the minimal ceiling path for the structural branch: V-01 + skeleton
= +5 pts, zero other cost.*

---

### V-03: Single-Sentence Prose Saturation (C-17 Floor Test)

**Axis**: Pure prose with ONE sentence per phase (semicolon-packed), no template fields, no section
headers. Tests C-17 at sub-paragraph density.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "List at least 3 pre-deploy checks with what is verified and what failure looks like -- 'verify the environment' does not pass; name the specific artifact or state being checked." Count (>=3), dual elements (verified + failure), weak-compliance disqualifier. All in one sentence. |
| C-02 | **PASS** | "Number at least 4 deployment steps with their output and precondition." Count (>=4) and structure specified. |
| C-03 | **PASS** | "List at least 2 post-deploy validation actions with the probe name, expected result, and failure indicator -- 'test that it works' does not pass." Count (>=2), three elements, disqualifier. |
| C-04 | **PASS** | "Name the specific threshold or probe result that triggers rollback -- 'if deployment fails' does not pass; list rollback steps; state the observable outcome that confirms rollback succeeded -- not 'rollback complete'." Trigger, steps, verification, two disqualifiers -- one sentence. |
| C-05 | **PASS** | Each phase instruction ends with a gap directive: identify what the current practice misses, state the fix, rate severity. Four gap instructions, one per phase. |
| C-06 | **PASS** | "name at least one step pair where the second cannot begin until the first fully completes and state why" -- explicit ordering and explicit reason required. |
| C-07 | **PASS** | Role statement followed by vocabulary list with "Use these terms; do not use generic cloud-deploy language." Constitutes the role/persona block without a formal ## header. |
| C-08 | **PASS** | "state the fix" required per gap, plus severity with justification. Actionable fix required throughout. |
| C-09 | **PASS** | "Produce a gap summary table with columns Rank, Phase, Gap summary, Severity, Why this rank -- rank all four gaps by deployment blast radius; a 'Why this rank' cell that only restates the phase's severity without comparing it against the other three gaps does not satisfy this requirement." Column names, cross-comparison mandate, disqualifier. |
| C-10 | **PASS** | "name one CI gate or pre-deploy script that could enforce a check currently done manually" (Phase 2) + "name one canary assertion or health probe that could replace a currently manual check" (Phase 3). Two hook locations via prose. |
| C-11 | **PASS** | Named vocabulary list immediately follows role statement. Confirmed as role/persona block (no formal ## ROLE header required). |
| C-12 | **PASS** | "State the current deployment practice for {topic} and its specific failure mode before tracing -- this is your baseline; reference it in gap analysis where the connection is direct." Named element, required placement before tracing. Passes via C-15 mechanism. |
| C-13 | **PASS** | "Produce a gap summary table with columns Rank, Phase, Gap summary, Severity, Why this rank" -- column names specified in prose. Passes via C-15 mechanism. |
| C-14 | **FAIL** | No structural skeleton table before phases. No pre-printed empty rows. No do-not-pre-fill guard. C-14 requires upfront structural commitment; prose cannot substitute. |
| C-15 | **PASS** | Achieves C-12 and C-13 through explicit prose alone, without template apparatus. Three requirements met: (a) names required output elements (>=3 checks with failure conditions, >=4 steps, >=2 validations, specific trigger, gap table with named columns), (b) states cross-gap comparison requirement ("rank all four gaps by deployment blast radius"), (c) disqualifies weak compliance by example per phase. No named sections, template fields, or gate markers present. |
| C-16 | **FAIL** | No Check-NN, Step-NN, Validation-NN, or Hook-NN template fields. C-16 requires template field scaffolding. |
| C-17 | **PASS** | C-15 PASS. Density: one sentence per phase (semicolon-packed). Below single-paragraph-per-phase threshold (C-17's stated floor). All three C-15 requirements present at single-sentence density: element count + column names, cross-comparison mandate, disqualifying example per phase. Compression floor confirmed lower than C-17's stated threshold implies. |

**Score: 125 / 135** | All essential PASS | **Golden: YES**

*Finding: C-17 holds at single-sentence density -- below R3's confirmed single-paragraph floor.
Semicolon-packing carries all three C-15 requirements per phase in one sentence without expansion.
The specificity floor is the operative constraint; density is not. Single-sentence is sufficient --
even more aggressive compression (single clause per phase) may still pass if specificity holds.*

---

### V-04: Adversarial Two-Pass + Gate-Free Fields + Front-Loaded Skeleton

**Axis**: R3 V-04 (adversarial two-pass + skeleton) with all GATE markers stripped. Tests C-14 +
C-16 coexistence under adversarial design with Source column cross-comparison forcing.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Check-01/02/03 fields in PASS 1 PHASE 1 with Pass and Failure conditions. No GATE needed. |
| C-02 | **PASS** | Step-01/02/03/04 in PASS 1 PHASE 2 with Output and Precondition. |
| C-03 | **PASS** | Validation-01/02 in PASS 1 PHASE 3 with Expected and Failure indicator. |
| C-04 | **PASS** | Trigger + Rollback-01/02 + Verification in PASS 1 PHASE 4. |
| C-05 | **PASS** | Expert gap block (Missing / Fix / Severity) per phase x4; adversarial challenge block per phase x4. All four phases covered at minimum. |
| C-06 | **PASS** | Ordering dependency field in PASS 1 PHASE 2 with explicit reason required. |
| C-07 | **PASS** | Vocabulary list in ROLE (Pass 1) block. |
| C-08 | **PASS** | "Fix: [Specific change -- not just a label]" per expert gap. Adversarial mandate: "Findings must be at least as specific as the expert's gaps. Generic challenges do not pass." Double specificity floor. |
| C-09 | **PASS** | GAP PLAN table (Rank / Phase / Source / Gap summary / Severity / Why this rank) + "compare this gap against the others across both passes." Source column adds attribution. Cross-pass comparison mandate stronger than single-pass V-02. |
| C-10 | **PASS** | Hook-01 in PASS 1 PHASE 2 and PASS 1 PHASE 3. Gate-free -- hook fields present structurally. |
| C-11 | **PASS** | Named vocabulary list in ROLE (Pass 1) block. |
| C-12 | **PASS** | STATUS-QUO BASELINE section: "Current approach: [...]" and "Known risk: [specific failure mode]." Baseline present before GAP PLAN and before PASS 1. |
| C-13 | **PASS** | GAP PLAN table before PASS 1 PHASE 1 with Source column. Required columns (Rank, Severity, Why this rank) present. |
| C-14 | **PASS** | GAP PLAN skeleton before PASS 1 PHASE 1. "Leave all rows blank. Do not pre-fill before tracing." (guard). Return instruction: "compare this gap against the others across both passes." (comparative cross-pass mandate). "Proceed to PASS 1 PHASE 1." separator. The Source column (Expert / adversarial) adds structural cross-source comparison attribution beyond single-pass designs. All three C-14 requirements met. |
| C-15 | **FAIL** | STATUS-QUO BASELINE section, ROLE section, PASS 1/PASS 2 structural headers, template fields (Check-NN, Step-NN, Validation-NN, Hook-NN), adversarial challenge template fields all constitute structural apparatus. Prose-alone path blocked. |
| C-16 | **PASS** | No GATE enforcement text in any phase or pass. Hook-01 in PASS 1 PHASE 2 and PHASE 3. Field count floors met. Gate-free confirmed. STATUS-QUO BASELINE section and adversarial challenge sections are not GATE enforcement text -- they do not contain "Do not proceed until" blocks. |
| C-17 | **FAIL** | C-15 FAIL -> C-17 cannot pass. |

**Score: 125 / 135** | All essential PASS | **Golden: YES**

*Finding: The Source column (Expert / adversarial) in the GAP PLAN provides structural cross-source
comparison forcing with no equivalent in single-pass designs. V-04 achieves the same 125/135 as
V-02 via a richer gap-analysis mechanism -- quality delta is in execution depth, not rubric score.
Gate-free confirmation extends to the STATUS-QUO BASELINE section and adversarial blocks: neither
constitutes GATE enforcement text.*

---

### V-05: Inertia Framing + Prose Saturation (C-15 Disqualifier Source Test)

**Axis**: Pure prose with inertia-framed role (deployment-failure narrative) and contextual
failure-mode disqualifiers anchored to current practice. Tests whether disqualifier source
matters for C-15 compliance.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | "List at least 3 pre-deploy checks; for each, name what is verified and what failure looks like -- a check that says 'confirm environment is ready' does not name a verifiable condition and does not pass." Count, dual elements, contextual disqualifier. |
| C-02 | **PASS** | "Number at least 4 deployment steps with the action and its precondition." Count and structure. |
| C-03 | **PASS** | "List at least 2 post-deploy validation actions with the probe name, expected result, and failure indicator -- 'monitor for errors' does not name a probe or an expected state and does not pass." Contextual disqualifier. |
| C-04 | **PASS** | "Name the specific threshold or probe result that triggers rollback -- 'someone notices it looks bad' does not pass; list rollback steps; state the observable outcome that confirms rollback succeeded -- not 'we redeployed'." Two contextual disqualifiers; all four rollback elements. |
| C-05 | **PASS** | Each phase ends with gap analysis instruction referencing current practice. Four gap directives, one per phase. |
| C-06 | **PASS** | "'schema migration before service restart' passes; 'migration, then restart' does not." Explicit ordering required; contextual disqualifier sets the bar. |
| C-07 | **PASS** | Role block enumerates 11 Commerce/Operations vocabulary terms. |
| C-08 | **PASS** | "state what should replace it" and "state the fix" per gap, plus severity with justification. |
| C-09 | **PASS** | "Produce a gap table with columns Rank, Phase, Gap summary, Severity, Why this rank -- rank all four gaps by deployment blast radius; a severity assignment that does not compare this gap against the baseline failure mode and the other three gaps does not satisfy the ranking requirement." Cross-gap mandate extended to baseline comparison. |
| C-10 | **PASS** | "name one CI gate or pre-deploy script that could enforce a check currently done from memory" (Phase 2) + "name one canary assertion or health probe that could replace the current practice of watching logs" (Phase 3). |
| C-11 | **PASS** | Named vocabulary list in role block. Inertia framing extends persona but does not replace vocabulary list. |
| C-12 | **PASS** | "State the current deployment practice for {topic} and the specific failure mode it carries -- this is your baseline; reference it where gap analysis connects directly." Baseline woven into per-phase gap instructions via "the current practice" references. |
| C-13 | **PASS** | "Produce a gap table with columns Rank, Phase, Gap summary, Severity, Why this rank" -- column names in prose. Passes via C-15 mechanism. |
| C-14 | **FAIL** | No structural skeleton table before phases. No do-not-pre-fill guard. Pure prose cannot satisfy C-14's structural commitment requirement. |
| C-15 | **PASS** | Achieves C-12 and C-13 through explicit prose alone, without template apparatus. Three requirements met: (a) names required output elements, (b) states cross-gap comparison requirement ("compare this gap against the baseline failure mode and the other three gaps"), (c) disqualifies weak compliance by example -- contextual failure-mode disqualifiers in all four phases. Critical finding: contextual disqualifiers ("'someone notices it looks bad' does not pass") satisfy C-15's disqualifying-example requirement with equivalent force to abstract pattern disqualifiers. The disqualifier source is not load-bearing -- the function (ruling out a named weak response form) is what matters. |
| C-16 | **FAIL** | No template fields. C-16 requires template field scaffolding. |
| C-17 | **PASS** | C-15 PASS. Density: one paragraph per phase (~3-4 sentences). Single-paragraph-per-phase density -- exactly C-17's threshold. All three C-15 requirements present at this density. |

**Score: 125 / 135** | All essential PASS | **Golden: YES**

*Finding: Inertia framing unifies C-12 baseline anchoring and C-15 disqualifier functions in the
same prose -- the baseline failure mode recurs naturally as the disqualifier source throughout.
The key finding: C-15 is source-agnostic on disqualifiers. Whether abstract ("'verify the
environment' does not pass") or contextual ("'someone notices it looks bad' does not pass"),
what matters is that the disqualifier targets a named weak form. Inertia framing tightens C-12
integration at no score cost.*

---

### New Patterns (R4)

1. **skeleton-and-gate-free-orthogonal** -- V-02 and V-04 confirm that C-14 (skeleton commitment
   device) and C-16 (gate-free field scaffolding) test orthogonal structural properties and pass
   simultaneously. The skeleton's components -- an empty table, a do-not-pre-fill guard, and a
   comparative return instruction -- do not constitute GATE enforcement text. "Gate-free" targets
   specifically the "GATE N: Do not proceed until..." enforcement blocks, not structural table
   placements. Design implication: the structural ceiling path (C-14 + C-16) is achievable; V-01
   + skeleton is the minimal form (120 -> 125).

2. **inertia-framing-disqualifier-passes-c15** -- V-05 confirms that contextual failure-mode
   disqualifiers anchored to current practice satisfy C-15's "disqualifying weak compliance by
   example" requirement with equivalent force to abstract pattern disqualifiers. "'someone notices
   it looks bad' does not pass" rules out the same class of vague response as "'if deployment
   fails' does not pass". The disqualifier source (abstract vs. contextual) is not load-bearing
   for C-15 compliance. What matters is that the disqualifier targets a named weak form.
   Implication: prompts can use inertia framing to unify C-12 baseline anchoring and C-15
   disqualifier functions in the same prose passage -- tighter integration without score cost.

---

```json
{"top_score": 125, "all_essential_pass": true, "new_patterns": ["skeleton-and-gate-free-orthogonal", "inertia-framing-disqualifier-passes-c15"]}
```
