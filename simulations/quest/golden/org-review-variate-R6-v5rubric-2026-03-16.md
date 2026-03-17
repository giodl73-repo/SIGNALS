# org-review Variations — Round 6 (v5 rubric, 2026-03-16)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v5-2026-03-16.md

Prior round summary:
- R1 (v1 rubric): V-05=95 (C-09+C-10+C-11+C-12), V-04=90 (C-13).
- R2 (v2 rubric): V-04=110 (C-12+C-13+C-14+C-15). First Gold.
- R3 (v3 rubric): V-05=125 (full aspirational stack). Aspirational frontier closed.
- R4 (v3→v4 rubric): V-05=135 (C-16+C-17 PASS, C-18 FAIL). Perfect (140) requires all three R4
  patterns simultaneously; no R4 variant achieved all three.
- R5 (v4→v5 rubric): V-04=150/155 (C-21 FAIL: lifecycle excluded from ledger assembly).
  V-05=155/155 (Perfect). V-05 R5 is the first Perfect across all rounds.

Round 6 strategy:
- v5 is saturated (V-05 R5 = 155/155). R6 explores ALTERNATIVE paths to high scores via
  fresh structural axes.
- Three single-axis variants against different Gold-path baselines; two combinations targeting 155.
- V-01: single axis -- role sequence (lifecycle gate runs BETWEEN domain and bracket closing)
        No bracket, full pre-commitment chain. Tests whether three-gate non-bracket structure
        (g_null → g_domain × N → g_lifecycle) achieves 140 without bracket overhead.
- V-02: single axis -- phrasing register (formal audit/attestation language throughout).
        Same structure as V-01; lexicon is the only variable. Register invariance test.
- V-03: single axis -- inertia framing (three-alternative challenger: Status Quo + Artifact +
        Named Substitute). Bracket architecture with extended Alternatives Table. Null
        hypothesis derivation rule covers all three alternatives. Targets 155.
- V-04: combination -- V-01 lifecycle sequence + full pre-commitment stack including bracket.
        Lifecycle runs §4 (after domain §3, before bracket closing §5). Tests whether
        lifecycle-before-bracket-closing with universal ledger achieves 155.
- V-05: combination -- V-03 three-alternative challenger + V-05 R5 full mechanism stack.
        Extended Alternatives Table feeds bracket; domain reviewers re-score all three
        alternatives; bracket closing aggregates. Targets 155.

Expected score ladder (v5 rubric, 155 pts max):
  V-01: 60+30+5(C-10)+5(C-12)+5(C-13)+5(C-14)+5(C-15)+5(C-17)+5(C-18)+5(C-19)+5(C-20)+5(C-21)=140
        (no bracket -- C-09 FAIL, C-11 vac, C-16 vac)
  V-02: 140 same as V-01 -- register invariance test
  V-03: 60+30+65=155  -- Perfect attempt via three-alternative challenger + bracket
  V-04: 60+30+65=155  -- Perfect attempt via lifecycle-before-bracket-closing + full stack
  V-05: 60+30+65=155  -- Perfect attempt via three-alternative + V-05 R5 full stack

---

## V-01 -- Role Sequence: Lifecycle Gate Runs After Domain, Before Bracket Closing

**Variation axis**: Role sequence -- the lifecycle/program reviewer runs as a named structural
gate AFTER domain reviewers but BEFORE synthesis; the architecture produces three distinct gate
verdicts in sequence: g_null (§2 challenger), g_domain (§3 domain reviewers), g_lifecycle (§4
lifecycle gate); synthesis applies the DISPOSITION CONTRACT to all three; no adversarial bracket
used; the LOCAL GATE LEDGER PROTOCOL requires lifecycle emission at §4, making C-21 compliance
structural.

**Hypothesis**: Prior non-bracket variants treat lifecycle as a domain reviewer with no special
structural position -- it runs in the domain sequence and produces one verdict among many.
Declaring lifecycle as a named post-domain pre-synthesis gate creates a commit sequence where
decision readiness is verified AFTER technical quality has been established. This is the
natural dependency order (domain confirms the artifact is sound; lifecycle confirms the team
is ready to commit to it). If the lifecycle section at §4 emits a Local Gate Ledger row and
the LOCAL GATE LEDGER PROTOCOL explicitly names §4 as a required emitter, C-21 compliance is
enforced without bracket architecture overhead. A 140-pt score validates this as a clean
alternative path for artifact types where adversarial override is not required.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first, before §0. Fill in the injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

Read all four pre-committed contracts before any reviewer section executes. They do not change.

**DISPOSITION CONTRACT** (the synthesis applies this formula -- it does not produce a new one):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL              -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL       -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS             -->  DISPOSITION = READY
  else                                      -->  DISPOSITION = CONDITIONAL  (ambiguous; treat as conditional)
```

Gates that produce verdicts: §2 (g_null), §3 (g_domain, one per domain reviewer), §4 (g_lifecycle).

**CLASS DERIVATION CONTRACT** (action item classes derive mechanically from gate verdicts; do
not re-assign class at synthesis time):

```
FAIL gate        -->  BLOCKED      (must resolve before any commitment)
CONDITIONAL gate -->  CONDITIONAL  (must resolve before proceeding)
PASS + HIGH      -->  CONDITIONAL  (HIGH finding preserved even at PASS gate)
PASS + LOW       -->  ADVISORY     (may defer)
```

**NULL HYPOTHESIS DERIVATION RULE** (g_null derives from the score differential -- do not
assert, derive):

```
Dimensions (scored 1-5 per alternative):
  D1 -- Switching cost       (1 = prohibitive to adopt artifact, 5 = negligible)
  D2 -- Coverage             (1 = artifact covers far less than status quo, 5 = complete)
  D3 -- Adoption friction    (1 = high friction, 5 = frictionless)
  D4 -- Time-to-value        (1 = months before value, 5 = immediate)

Score differential = Artifact total - Status Quo total

g_null derivation:
  differential >= +6   -->  g_null = PASS         (artifact clearly superior)
  differential +1..+5  -->  g_null = CONDITIONAL  (marginal; named gaps must be addressed)
  differential <= 0    -->  g_null = FAIL          (no case for building over status quo)
```

**LOCAL GATE LEDGER PROTOCOL** (fourth pre-committed contract; applies to every reviewer
section without exception):

```
Syntax:   one-row table: | Gate Verdict | Class | Source | Action |
Timing:   emitted at the END of each reviewer section, immediately after the gate verdict
Coverage: MANDATORY for ALL sections -- §2 (inertia-advocate), §3 (each domain reviewer),
          §4 (lifecycle reviewer); no section is exempt
Assembly: §5 master action register copies all Local Gate Ledger rows from §2, §3, and §4
          verbatim. Do NOT re-derive Gate Verdict or Class during assembly.
```

**Severity Semantics** (applies throughout; commit-gate meaning):

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

---

**§0 -- Scope Declaration**

Before any reviewer section:

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Any surface discovered mid-review not listed above is a scope gap. Flag it; do not absorb it.

---

**§1 -- Role Selection**

Read `.craft/roles/signal/`. No invented roles.

Branch on `{{reviewer_set}}`:
- Not "auto": use those roles exactly. If inertia-advocate or lifecycle role is missing, add it
  and note the addition.
- "auto" + "standard": select CHALLENGER slot (inertia-advocate archetype), >= 2 DOMAIN slots
  (technical/architecture archetype) relevant to the artifact type, and LIFECYCLE slot
  (PM/program archetype). One-sentence rationale per role.
- "auto" + "deep": all roles in the directory. State total count. Lifecycle slot must be filled.

Emit the manifest before any reviewer section:

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "all roles"]  SLOT: CHALLENGER | DOMAIN | LIFECYCLE
```

---

**§2 -- Null Hypothesis Gate (Inertia-Advocate)**

This section runs before domain (§3) and lifecycle (§4) reviewers. Neither has seen this section.

Populate the Alternatives Table. Apply the NULL HYPOTHESIS DERIVATION RULE. Do not assert
g_null -- derive it from the score differential.

```
## §2 -- Null Hypothesis Gate -- [challenger role]

**Status quo statement**: [what the team does today instead of building this -- one sentence]

**Alternatives Table (challenger frame):**
| Dimension            | Status Quo | This Artifact | Rationale                |
|----------------------|-----------|---------------|--------------------------|
| D1 Switching cost    | [1-5]     | [1-5]         | [one sentence per cell]  |
| D2 Coverage          | [1-5]     | [1-5]         | [one sentence]           |
| D3 Adoption friction | [1-5]     | [1-5]         | [one sentence]           |
| D4 Time-to-value     | [1-5]     | [1-5]         | [one sentence]           |
| **TOTAL**            | [sum]     | [sum]         |                          |

**Score differential**: [artifact total] - [status quo total] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE applied**: [which branch; cite the score differential]

**Findings**: [2-3 from challenger's lens.verify supporting the table scores]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from challenger's lens.verify]
**Gate Verdict (g_null)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict | Class | Source | Action |
|-------------|-------|--------|--------|
| [g_null] | [from CLASS DERIVATION CONTRACT] | §2 / inertia-advocate / [5-word summary] | [synthesis action] |
```

Domain (§3) and lifecycle (§4) sections begin only after g_null is emitted.

---

**§3 -- Domain Reviewer Sections**

Domain reviewers have access to the artifact only. They have not seen §2 (null hypothesis gate).

For each selected domain reviewer:
1. Load role file from `.craft/roles/signal/{role}.md`.
2. Apply `orientation.frame` to the artifact.
3. Re-score each dimension from this role's technical frame. Mark unchanged dimensions explicitly.
4. Keep findings distinct per reviewer -- cross-role homogeneity is a structural defect.

```
## §3 -- Domain Reviewer: [role] ([archetype])

**Domain re-read of alternatives table:**
| Dimension            | Challenger Score | Revised Score | Justification or "unchanged" |
|----------------------|-----------------|---------------|------------------------------|
| D1 Switching cost    | [§2 score]      | [1-5]         | [sentence]                   |
| D2 Coverage          | [§2 score]      | [1-5]         | [sentence]                   |
| D3 Adoption friction | [§2 score]      | [1-5]         | [sentence]                   |
| D4 Time-to-value     | [§2 score]      | [1-5]         | [sentence]                   |

**Findings**: [2-4 from this role's lens.verify and expertise.depth; must not echo §2 framing
  or other domain reviewer framing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action from this role's frame]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_domain)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict | Class | Source | Action |
|-------------|-------|--------|--------|
| [g_domain] | [from CLASS DERIVATION CONTRACT] | §3 / [role] / [5-word summary] | [synthesis action] |
```

One row per FAIL or CONDITIONAL verdict minimum. Advisory rows optional.

---

**§4 -- Lifecycle Gate (Post-Domain)**

The lifecycle reviewer runs after all §3 domain sections. Domain reviewers have not seen §2
or §3 findings -- they received only the artifact. The lifecycle reviewer also receives only
the artifact.

The lifecycle reviewer answers: is the team in a position to make a commitment decision? Assess
scope completeness, dependency declaration, risk ownership, and program readiness. Do not
evaluate technical quality -- that is domain's scope.

```
## §4 -- Lifecycle Gate: [lifecycle role] ([archetype])

**Commitment-readiness assessment**: [2-3 sentences: is the artifact complete enough for a
  commitment decision? Are scope, risks, and dependencies sufficiently declared?]
**Findings**: [2-3 findings: scope completeness, risk declaration, dependency readiness]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_lifecycle)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict   | Class | Source | Action |
|----------------|-------|--------|--------|
| [g_lifecycle]  | [from CLASS DERIVATION CONTRACT] | §4 / [lifecycle role] / [5-word summary] | [synthesis action] |
```

---

**§5 -- Master Action Register (Consolidation)**

Copy all Local Gate Ledger rows from §2, §3, and §4 into the master table verbatim. Do not
re-derive Gate Verdict or Class. Copy from each local row exactly as written.

```
## §5 -- Master Action Register
(Consolidated from Local Gate Ledger rows in §2, §3, §4 -- no re-derivation)

| # | Gate Verdict | Class | Source | Action |
|---|--------------|-------|--------|--------|
```

Minimum: one row per FAIL or CONDITIONAL gate verdict across §2, §3, and §4.

---

**§6 -- Synthesis and Disposition**

Write 5-8 sentences:
- Name the highest-severity finding across all sections
- Name cross-role conflicts (incompatible recommendations from two sections)
- Name convergence areas (multiple reviewers flagging the same gap independently)
- Reference g_null (§2) explicitly -- include score differential
- Reference g_lifecycle (§4) explicitly
- State which branch of the DISPOSITION CONTRACT applies and why

Apply the DISPOSITION CONTRACT from the preamble. State the branch.

```
## §6 -- Synthesis

[5-8 sentences]

FORMULA APPLIED: [which DISPOSITION CONTRACT branch and why]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## V-02 -- Phrasing Register: Formal Audit/Attestation Language

**Variation axis**: Phrasing register -- all structural mechanisms of V-01 (three-gate
sequence: g_null → g_domain × N → g_lifecycle; three-contract preamble + LOCAL GATE LEDGER
PROTOCOL; Local Gate Ledger at every section; master register assembled verbatim) are
preserved unchanged; the language register is rewritten from instructional imperative to formal
audit/attestation style: third-person passive ("the reviewer shall attest"), labeled
ATTESTATION blocks, DETERMINATION labels for gate verdicts, LEDGER ENTRY headers for local
ledger rows, and RULING field for the final disposition.

**Hypothesis**: R4-V-01 tested conversational imperative vs formal instructional; register made
no difference in that round. Audit/attestation language has not been tested. Attestation
vocabulary makes the chain-of-custody metaphor explicit at the lexical level: "The reviewer
attests..." maps directly to "this claim is staked and traceable." If audit language increases
compliance with C-05 (traceable action items), C-14 (gate verdict preserved), and C-18 (ledger
at origin) by activating commit-gate semantics at the word level, it is the preferred register
for high-auditability prompts. If scores match V-01, register is confirmed as a free variable
across instructional, conversational, and attestation styles.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this acknowledgment block first, before §0. Fill in the injected values.

```
## Audit Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

The following review constitutes a formal org-review attestation for `{{artifact_id}}`.

Each section of this audit shall attest to the findings within its declared scope. All gate
verdicts shall be derived from the stated pre-committed contracts. No editorial judgment shall
substitute for a contract derivation.

**DISPOSITION CONTRACT** (committed prior to execution; the synthesis section shall apply
this formula and shall not produce a new one):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL              -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL       -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS             -->  DISPOSITION = READY
  else                                      -->  DISPOSITION = CONDITIONAL  (ambiguous; treat as conditional)
```

Gates attesting verdicts: §2 (g_null), §3 (g_domain, one per domain reviewer), §4 (g_lifecycle).

**CLASS DERIVATION CONTRACT** (committed prior to execution; action item classes shall be
derived mechanically from gate verdicts and shall not be re-assigned at synthesis time):

```
FAIL gate        -->  BLOCKED      (must be resolved before any commitment)
CONDITIONAL gate -->  CONDITIONAL  (must be resolved before proceeding)
PASS + HIGH      -->  CONDITIONAL  (HIGH finding retained even at PASS gate)
PASS + LOW       -->  ADVISORY     (may be deferred)
```

**NULL HYPOTHESIS DERIVATION RULE** (committed prior to execution; g_null shall be derived
from the score differential -- the reviewer does not assert g_null, derives it):

```
Dimensions (scored 1-5 per alternative; applied by the inertia-advocate in §2):
  D1 -- Switching cost       (1 = prohibitive to adopt artifact, 5 = negligible)
  D2 -- Coverage             (1 = artifact covers far less than status quo, 5 = complete)
  D3 -- Adoption friction    (1 = high friction, 5 = frictionless)
  D4 -- Time-to-value        (1 = months before value, 5 = immediate)

Score differential = Artifact total - Status Quo total

g_null derivation:
  differential >= +6   -->  g_null = PASS         (artifact clearly superior)
  differential +1..+5  -->  g_null = CONDITIONAL  (marginal; named gaps must be addressed)
  differential <= 0    -->  g_null = FAIL          (no case for building over status quo)
```

**LOCAL GATE LEDGER PROTOCOL** (fourth pre-committed contract; all reviewer sections shall
comply without exception):

```
Syntax:   one-row table: | DETERMINATION | Class | Attestor | Action |
Timing:   emitted at the END of each reviewer section, immediately after the DETERMINATION
          is stated; the section is not complete until the LEDGER ENTRY is emitted
Coverage: MANDATORY for ALL sections -- §2 (inertia-advocate), §3 (each domain reviewer),
          §4 (lifecycle reviewer); no section is exempt from this protocol
Assembly: §5 master action register shall copy all LEDGER ENTRY rows from §2, §3, and §4
          verbatim. Re-derivation of DETERMINATION or Class during assembly is prohibited.
```

**Severity Semantics** (applies throughout; commit-gate meaning):

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

---

**§0 -- Scope Attestation**

The following scope is declared prior to any reviewer section. All findings shall be
constrained to in-scope surfaces. Any surface discovered mid-audit not enumerated below
shall be flagged as a scope gap -- it shall not be silently incorporated.

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not being attested to in this pass]
```

---

**§1 -- Reviewer Roster**

The reviewer roster shall be drawn exclusively from `.craft/roles/signal/`. No roles shall
be invented.

Branch on `{{reviewer_set}}`:
- Not "auto": those roles shall be used exactly as specified. If the inertia-advocate or
  lifecycle role is absent, it shall be added; the addition shall be noted.
- "auto" + "standard": the roster shall include the CHALLENGER slot (inertia-advocate
  archetype), >= 2 DOMAIN slots (technical/architecture archetype), and the LIFECYCLE slot
  (PM/program archetype). One-sentence rationale shall be provided per role.
- "auto" + "deep": all roles in the directory shall attest. Total count shall be stated.

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Attesting roster:
  - [role]: [archetype] -- [rationale | "as specified" | "full directory"]  SLOT: CHALLENGER | DOMAIN | LIFECYCLE
```

---

**§2 -- Null Hypothesis Attestation (Inertia-Advocate)**

The inertia-advocate shall attest prior to domain and lifecycle sections. Neither §3 nor §4
reviewers shall have access to §2.

The inertia-advocate shall populate the Alternatives Table and apply the NULL HYPOTHESIS
DERIVATION RULE. The g_null DETERMINATION shall be derived from the score differential.

```
## §2 -- Null Hypothesis Attestation -- [challenger role]

**Status quo statement**: [what the team does today instead of building this -- one sentence]

**Alternatives Table (inertia-advocate frame):**
| Dimension            | Status Quo | This Artifact | Attestor's Rationale     |
|----------------------|-----------|---------------|--------------------------|
| D1 Switching cost    | [1-5]     | [1-5]         | [one sentence per cell]  |
| D2 Coverage          | [1-5]     | [1-5]         | [one sentence]           |
| D3 Adoption friction | [1-5]     | [1-5]         | [one sentence]           |
| D4 Time-to-value     | [1-5]     | [1-5]         | [one sentence]           |
| **TOTAL**            | [sum]     | [sum]         |                          |

**Score differential**: [artifact total] - [status quo total] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE applied**: [which branch; cite differential]

**ATTESTATION**:
  Finding 1: [switching cost observation] | Severity: HIGH | MEDIUM | LOW
  Finding 2: [workaround viability observation] | Severity: HIGH | MEDIUM | LOW
  Finding 3: [adoption friction observation] | Severity: HIGH | MEDIUM | LOW
**Verify Question**: [one from challenger's lens.verify]
**DETERMINATION (g_null)**: FAIL | CONDITIONAL | PASS

**LEDGER ENTRY:**
| DETERMINATION | Class | Attestor | Action |
|--------------|-------|----------|--------|
| [g_null] | [from CLASS DERIVATION CONTRACT] | §2 / inertia-advocate / [5-word] | [action] |
```

§3 and §4 shall not begin until DETERMINATION (g_null) has been emitted.

---

**§3 -- Domain Reviewer Attestations**

Each domain reviewer shall attest from the artifact alone. They shall not have access to §2.

For each selected domain reviewer, the following attestation structure applies:

```
## §3 -- Domain Attestation: [role] ([archetype])

**Domain re-read of alternatives table:**
| Dimension            | Challenger Score | Attested Score | Justification or "unchanged" |
|----------------------|-----------------|----------------|------------------------------|
| D1 Switching cost    | [§2 score]      | [1-5]          | [sentence]                   |
| D2 Coverage          | [§2 score]      | [1-5]          | [sentence]                   |
| D3 Adoption friction | [§2 score]      | [1-5]          | [sentence]                   |
| D4 Time-to-value     | [§2 score]      | [1-5]          | [sentence]                   |

**ATTESTATION**:
  Finding 1: [technical finding from this role's lens] | Severity: HIGH | MEDIUM | LOW
  Finding 2: [finding] | Severity: HIGH | MEDIUM | LOW
  [Finding 3-4 if applicable] | Severity: HIGH | MEDIUM | LOW
  [Findings shall not echo §2 attestation or other domain attestation.]
**Recommendation**: [one concrete action from this role's frame]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**DETERMINATION (g_domain)**: FAIL | CONDITIONAL | PASS

**LEDGER ENTRY:**
| DETERMINATION | Class | Attestor | Action |
|--------------|-------|----------|--------|
| [g_domain] | [from CLASS DERIVATION CONTRACT] | §3 / [role] / [5-word] | [action] |
```

One LEDGER ENTRY row per FAIL or CONDITIONAL DETERMINATION, minimum.

---

**§4 -- Lifecycle Attestation (Post-Domain)**

The lifecycle reviewer shall attest after all §3 domain attestations are complete. The
lifecycle reviewer shall receive the artifact only; they shall not have access to §2 or §3.

The lifecycle attestation answers: is the team in a position to commit? The lifecycle reviewer
shall attest to decision readiness, not technical quality.

```
## §4 -- Lifecycle Attestation: [lifecycle role] ([archetype])

**Commitment-readiness attestation**: [2-3 sentences: attestation of the artifact's fitness
  for a commitment decision; scope completeness, risk ownership, and dependency declaration
  are the attested surfaces]
**ATTESTATION**:
  Finding 1: [scope completeness] | Severity: HIGH | MEDIUM | LOW
  Finding 2: [risk declaration] | Severity: HIGH | MEDIUM | LOW
  Finding 3: [dependency readiness] | Severity: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**DETERMINATION (g_lifecycle)**: FAIL | CONDITIONAL | PASS

**LEDGER ENTRY:**
| DETERMINATION  | Class | Attestor | Action |
|----------------|-------|----------|--------|
| [g_lifecycle]  | [from CLASS DERIVATION CONTRACT] | §4 / [lifecycle role] / [5-word] | [action] |
```

---

**§5 -- Consolidated Attestation Register**

All LEDGER ENTRY rows from §2, §3, and §4 shall be copied verbatim into the register below.
Re-derivation of DETERMINATION or Class during assembly is explicitly prohibited. The register
is a copy, not a synthesis.

```
## §5 -- Consolidated Attestation Register
(Verbatim copy of LEDGER ENTRY rows from §2, §3, §4 -- no re-derivation)

| # | DETERMINATION | Class | Attestor | Action |
|---|---------------|-------|----------|--------|
```

Minimum: one row per FAIL or CONDITIONAL DETERMINATION across §2, §3, and §4.

---

**§6 -- Integrating Ruling**

The following synthesis shall apply the DISPOSITION CONTRACT. The synthesis shall not produce
a new formula; it shall state which branch applies and why.

Write 5-8 sentences:
- Name the highest-severity finding across all sections
- Name cross-attestor conflicts (incompatible recommendations from two sections)
- Name convergence (multiple attestors flagging the same gap independently)
- Reference g_null (§2) explicitly -- cite score differential
- Reference g_lifecycle (§4) explicitly
- State which branch of the DISPOSITION CONTRACT governs the RULING

```
## §6 -- Integrating Ruling

[5-8 sentences]

CONTRACT BRANCH APPLIED: [which DISPOSITION CONTRACT branch and why]

RULING: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to audit:**

{{artifact_id}} content:

{{artifact}}

---

## V-03 -- Inertia Framing: Three-Alternative Challenger Comparison

**Variation axis**: Inertia framing -- the challenger's Alternatives Table is extended from
two alternatives (Status Quo vs This Artifact) to three: (A) Status Quo, (B) This Artifact,
(C) Named Substitute. The challenger MUST name a specific competing tool, approach, or
workflow as alternative C -- not a generic placeholder. The NULL HYPOTHESIS DERIVATION RULE
covers all three comparisons: the artifact must outperform both the status quo AND the named
substitute to pass. Domain reviewers re-score all three alternatives on all four dimensions.
Bracket closing aggregates all three. The Alternatives Table and bracket architecture are
retained; the single-axis change is the third alternative.

**Hypothesis**: Current variants compare only two alternatives, making the null hypothesis
evaluation structurally binary: artifact vs status quo. Teams often face a three-way choice:
continue current practice, adopt this artifact, or adopt a named competing solution. A
three-alternative Alternatives Table forces the challenger to name a specific competing
approach (not just abstract status quo) and forces domain reviewers to evaluate whether the
artifact also outperforms the named substitute. The null hypothesis derivation rule covers
both comparisons, requiring a double advantage for PASS. If this produces more rigorous null
hypothesis evaluation (C-03), stronger alternatives table anchor (C-16), and richer integrating
narrative (C-07) without degrading other criteria, the three-alternative frame is a structural
improvement over the binary frame.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first, before §0. Fill in injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

Read all four pre-committed contracts before any reviewer section executes. They do not change.

**DISPOSITION CONTRACT** (the synthesis applies this formula -- it does not produce a new one):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL              -->  DISPOSITION = BLOCKED
  elif Override invoked = YES  (see §3)     -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL       -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS             -->  DISPOSITION = READY
  else                                      -->  DISPOSITION = CONDITIONAL  (ambiguous)
```

Gates that produce verdicts: Bracket Opening (§1.5), domain reviewers (§2), Bracket Closing (§3).

**CLASS DERIVATION CONTRACT** (action item classes derive mechanically from gate verdicts; no
editorial re-assignment at synthesis time):

```
FAIL gate        -->  BLOCKED
CONDITIONAL gate -->  CONDITIONAL
PASS + HIGH      -->  CONDITIONAL
PASS + LOW       -->  ADVISORY
```

**NULL HYPOTHESIS DERIVATION RULE** (Opening Verdict derives from both score differentials --
do not assert, derive; the challenger must name Alternative C before scoring):

```
Alternatives:
  (A) Status Quo          -- what the team does today
  (B) This Artifact       -- what is being evaluated
  (C) Named Substitute    -- challenger MUST name a specific competing tool, approach, or
                             workflow (not "TBD" or generic placeholder)

Dimensions (scored 1-5 per alternative):
  D1 -- Switching cost       (1 = prohibitive to adopt B, 5 = negligible)
  D2 -- Coverage             (1 = B covers far less than A, 5 = B covers fully)
  D3 -- Adoption friction    (1 = high friction for B, 5 = frictionless)
  D4 -- Time-to-value        (1 = months before value from B, 5 = immediate)

Primary differential   = B_total - A_total
Secondary differential = B_total - C_total

Opening Verdict derivation:
  B_total > A_total by >= +6  AND  B_total > C_total  -->  PASS  (artifact dominates both)
  B_total > A_total by >= +6  BUT  B_total <= C_total -->  CONDITIONAL  (substitute competitive)
  B_total > A_total by +1..+5                         -->  CONDITIONAL  (marginal primary advantage)
  B_total <= A_total                                   -->  FAIL  (no case for building)
```

**LOCAL GATE LEDGER PROTOCOL** (fourth pre-committed contract):

```
Syntax:   one-row table: | Gate Verdict | Class | Source | Action |
Timing:   emitted at the END of each reviewer section, immediately after the gate verdict
Coverage: MANDATORY for ALL sections -- §1.5 (bracket opening), §2 (each domain reviewer),
          §4 (lifecycle reviewer), §3 (bracket closing); no section is exempt
Assembly: §5 master action register copies all Local Gate Ledger rows from §1.5, §2, §4,
          and §3 verbatim. Do NOT re-derive Gate Verdict or Class during assembly.
```

**Severity Semantics** (applies throughout):

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

---

**§0 -- Scope Declaration**

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Any surface found mid-review not listed above is a scope gap. Flag it; do not absorb it.

---

**§1 -- Role Selection**

Read `.craft/roles/signal/`. No invented roles.

Branch on `{{reviewer_set}}`:
- Not "auto": use exactly those roles. Inertia-advocate must be present for §1.5 and §3;
  lifecycle must be present for §4. Add if missing; note the addition.
- "auto" + "standard": CHALLENGER slot (inertia-advocate archetype), >= 2 DOMAIN slots
  (technical/architecture archetype), LIFECYCLE slot (PM/program archetype). One-sentence
  rationale per role.
- "auto" + "deep": all roles. State count.

Inertia-advocate is reserved for §1.5 (bracket opening) and §3 (bracket closing).

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "deep run"]
    (inertia-advocate: §1.5 and §3 only)
    (lifecycle reviewer: §4 only)
```

---

**§1.5 -- Bracket Opening: Three-Alternative Challenger Frame**

This section runs before domain (§2) and lifecycle (§4) reviewers. Neither has seen it.

The challenger MUST name a specific Alternative C (competing tool, workaround, or approach).
Populate all three alternatives for all four dimensions. Apply the NULL HYPOTHESIS DERIVATION
RULE. Do not assert Opening Verdict -- derive it from both differentials.

```
## §1.5 -- Bracket Opening -- inertia-advocate

**Status quo statement (A)**: [what the team does today -- one sentence]
**Named substitute (C)**: [SPECIFIC competing tool, approach, or workflow -- name it explicitly]

**Three-Alternative Table (challenger frame):**
| Dimension            | (A) Status Quo | (B) This Artifact | (C) Named Substitute | Rationale |
|----------------------|---------------|------------------|---------------------|-----------|
| D1 Switching cost    | [1-5]         | [1-5]            | [1-5]               | [one sentence per row explaining all three scores] |
| D2 Coverage          | [1-5]         | [1-5]            | [1-5]               | [sentence] |
| D3 Adoption friction | [1-5]         | [1-5]            | [1-5]               | [sentence] |
| D4 Time-to-value     | [1-5]         | [1-5]            | [1-5]               | [sentence] |
| **TOTAL**            | [sum]         | [sum]            | [sum]               |           |

**Primary differential (B - A)**: [B total] - [A total] = [+/- n]
**Secondary differential (B - C)**: [B total] - [C total] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE applied**: [which branch; cite both differentials]

**Challenge to domain reviewers**: [one specific question that domain reviewers must address
  to change any of the B-column scores; this is the anchor all downstream reviewers respond to]

**Findings**: [2-3 narrative findings from challenger's lens.verify supporting the table scores]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict     | Class | Source | Action |
|-----------------|-------|--------|--------|
| [Opening Verdict] | [from CLASS DERIVATION CONTRACT] | §1.5 / inertia-advocate / [5-word] | [action] |
```

Domain sections (§2) begin only after Opening Verdict is emitted.

---

**§2 -- Domain Reviewer Sections**

Domain reviewers have access to the artifact only. They have not seen §1.5.

For each selected domain reviewer, re-score all three alternatives on all four dimensions
from this role's technical frame. Mark unchanged scores explicitly. The challenge question
from §1.5 must be addressed in at least one finding.

```
## §2 -- Domain Reviewer: [role] ([archetype])

**Three-alternative re-read**
(Challenger's challenge: "[copy challenge text from §1.5]")

| Dimension            | (A) SQ Challenger | (B) Artifact Challenger | (C) Sub Challenger | (B) Revised | (C) Revised | Justification |
|----------------------|------------------|------------------------|-------------------|------------|------------|---------------|
| D1 Switching cost    | [§1.5]           | [§1.5]                 | [§1.5]            | [1-5]      | [1-5]      | [sentence or "unchanged"] |
| D2 Coverage          | [§1.5]           | [§1.5]                 | [§1.5]            | [1-5]      | [1-5]      | [sentence] |
| D3 Adoption friction | [§1.5]           | [§1.5]                 | [§1.5]            | [1-5]      | [1-5]      | [sentence] |
| D4 Time-to-value     | [§1.5]           | [§1.5]                 | [§1.5]            | [1-5]      | [1-5]      | [sentence] |

**[This role's null hypothesis address]**: [does the technical approach make both (A) and (C)
  obsolete from this domain's frame? One sentence. Must differ from §1.5 framing.]

**Findings**: [2-4 findings from this role's lens.verify and expertise.depth; must not echo
  §1.5 framing or other domain reviewers]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_domain)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict | Class | Source | Action |
|-------------|-------|--------|--------|
| [g_domain] | [from CLASS DERIVATION CONTRACT] | §2 / [role] / [5-word] | [action] |
```

---

**§4 -- Lifecycle Reviewer**

The lifecycle reviewer runs after all §2 domain sections. Access: artifact only.

```
## §4 -- Lifecycle Reviewer: [role] ([archetype])

**Commitment-readiness assessment**: [Is the three-alternative comparison sufficient basis for
  a commitment decision? Reference that the artifact is being compared against both a status
  quo (A) and a named substitute (C). One paragraph.]
**Findings**: [2-3 findings: commitment readiness, decision sufficiency, program concerns]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_lifecycle)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict   | Class | Source | Action |
|----------------|-------|--------|--------|
| [g_lifecycle]  | [from CLASS DERIVATION CONTRACT] | §4 / [lifecycle role] / [5-word] | [action] |
```

---

**§3 -- Bracket Closing: Challenger Post-Domain Reassessment**

After all §2 and §4 sections. The inertia-advocate now has access to domain re-reads.

Question: Do the domain-adjusted scores, across all three alternatives, constitute sufficient
evidence to defeat the null hypothesis stated in §1.5?

Override authority: if domain re-reads inflate B-column scores without technical justification,
or if the adjusted verdict still fails the null hypothesis, the Bracket Closing may override.

```
## §3 -- Bracket Closing -- inertia-advocate (post-domain reassessment)

**Domain re-read aggregation:**
| Reviewer | D1(B) | D2(B) | D3(B) | D4(B) | D1(C) | D2(C) | D3(C) | D4(C) | Challenge Answered? |
|----------|-------|-------|-------|-------|-------|-------|-------|-------|---------------------|
| [role]   | [rev] | [rev] | [rev] | [rev] | [rev] | [rev] | [rev] | [rev] | yes / partial / no  |

**Revised Three-Alternative Table (challenger vs domain-aggregate):**
| Dimension            | (A) Status Quo | (B) Challenger | (B) Domain Avg | (B) Accepted | (C) Challenger | (C) Domain Avg | (C) Accepted |
|----------------------|---------------|---------------|----------------|-------------|---------------|----------------|-------------|
| D1 Switching cost    | [A]           | [§1.5 B]      | [domain avg]   | [final B]   | [§1.5 C]      | [domain avg]   | [final C]   |
| D2 Coverage          | [A]           | [§1.5 B]      | [domain avg]   | [final B]   | [§1.5 C]      | [domain avg]   | [final C]   |
| D3 Adoption friction | [A]           | [§1.5 B]      | [domain avg]   | [final B]   | [§1.5 C]      | [domain avg]   | [final C]   |
| D4 Time-to-value     | [A]           | [§1.5 B]      | [domain avg]   | [final B]   | [§1.5 C]      | [domain avg]   | [final C]   |
| **TOTAL**            | [A sum]       |               |                | [B sum]     |               |                | [C sum]     |

**Revised primary differential (B - A)**: [B accepted sum] - [A sum] = [+/- n]
**Revised secondary differential (B - C)**: [B accepted sum] - [C accepted sum] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE re-applied**: [which branch; cite both revised differentials;
  state if verdict changes from §1.5]

**Assessment**: [Does the domain-adjusted table change the verdict? What gaps remain?]
**Override authority**: [state explicitly if invoked and the basis]

**Closing Verdict**: FAIL | CONDITIONAL | PASS
**Override invoked**: YES | NO
  If YES: "Bracket Closing overrides per DISPOSITION CONTRACT -- DISPOSITION = BLOCKED."
  If NO: domain verdicts stand; Closing Verdict feeds DISPOSITION CONTRACT normally.

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Closing Verdict] | [from CLASS DERIVATION CONTRACT] | §3 / inertia-advocate / [5-word] | [action] |
```

This field is mandatory: emit Override invoked: YES | NO regardless of whether override is
exercised.

---

**§5 -- Master Action Register**

Copy all Local Gate Ledger rows from §1.5, §2, §4, and §3 into the master table verbatim.
Do not re-derive Gate Verdict or Class. The register is a copy, not a synthesis.

```
## §5 -- Master Action Register
(Consolidated from Local Gate Ledger rows in §1.5, §2, §4, §3 -- no re-derivation)

| # | Gate Verdict | Class | Source | Action |
|---|--------------|-------|--------|--------|
```

If Override invoked = YES in §3: add row: `§3 / inertia-advocate / override invoked --> BLOCKED`.

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**§6 -- Integrating Summary and Disposition**

Write 5-8 sentences:
- Name the highest-severity finding across all sections
- Name cross-role conflicts (incompatible recommendations from two sections)
- Name convergence areas
- Reference Opening Verdict (§1.5) -- cite both differentials (B-A and B-C)
- Reference Closing Verdict (§3) and Override invoked field explicitly
- Reference g_lifecycle (§4) explicitly
- State which DISPOSITION CONTRACT branch applies

Apply the DISPOSITION CONTRACT from the preamble. State the branch.

```
## §6 -- Synthesis

[5-8 sentences]

FORMULA APPLIED: [which DISPOSITION CONTRACT branch and why]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## V-04 -- Combination: Lifecycle-Before-Bracket-Closing + Full Pre-commitment Stack

**Variation axes**: Role sequence (lifecycle runs §4, AFTER domain reviewers §3 but BEFORE
bracket closing §5) combined with the full V-05 R5 pre-commitment stack -- DISPOSITION
CONTRACT + CLASS DERIVATION CONTRACT + NULL HYPOTHESIS DERIVATION RULE + LOCAL GATE LEDGER
PROTOCOL as fourth contract; adversarial bracket (C-09); Alternatives Table bracket anchor
(C-16); inline local ledger at ALL sections including lifecycle §4 (C-18 + C-21); verbatim
assembly prohibition (C-20); three template variables (C-13 + C-15); Gate Verdict column (C-14)

**Hypothesis**: V-05 R5 achieves Perfect (155/155) with the lifecycle reviewer at §5 (after
bracket closing). V-04 R5 fails C-21 because its lifecycle reviewer at §4 (after bracket
closing) was not included in ledger assembly. This variant puts lifecycle BETWEEN domain and
bracket closing: architecture is §1.5 Bracket Opening → §3 Domain → §4 Lifecycle → §5 Bracket
Closing → §6 Action Register → §7 Synthesis. The LOCAL GATE LEDGER PROTOCOL explicitly covers
§1.5 (bracket opening), §3 (domain reviewers), §4 (lifecycle), and §5 (bracket closing).
The master register assembly instruction names all four sections verbatim. Bracket closing
has access to both domain AND lifecycle verdicts -- a structural change from V-05 R5 where
bracket closing precedes lifecycle. If this variant scores 155/155, it validates that the
lifecycle position within the sequence is a free variable as long as ledger coverage is
universal and the assembly instruction is explicit.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first. Fill in injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

Read all four pre-committed contracts before any reviewer section executes. They do not change.

**DISPOSITION CONTRACT** (committed before execution; synthesis applies this formula):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL              -->  DISPOSITION = BLOCKED
  elif Override invoked = YES  (see §5)     -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL       -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS             -->  DISPOSITION = READY
  else                                      -->  DISPOSITION = CONDITIONAL  (ambiguous)
```

Gates that produce verdicts: Bracket Opening (§1.5), domain reviewers (§3), Lifecycle (§4),
Bracket Closing (§5). The formula is the evaluator. Editorial judgment at summary time does
not override it.

**CLASS DERIVATION CONTRACT** (committed before execution; no editorial re-assignment):

```
FAIL gate        -->  BLOCKED
CONDITIONAL gate -->  CONDITIONAL
PASS + HIGH      -->  CONDITIONAL
PASS + LOW       -->  ADVISORY
```

**NULL HYPOTHESIS DERIVATION RULE** (committed before execution; Opening Verdict derived from
score differential -- do not assert, derive):

```
Dimensions (scored 1-5 per alternative):
  D1 -- Switching cost       (1 = prohibitive to adopt artifact, 5 = negligible)
  D2 -- Coverage             (1 = artifact covers far less than status quo, 5 = complete)
  D3 -- Adoption friction    (1 = high friction, 5 = frictionless)
  D4 -- Time-to-value        (1 = months before value, 5 = immediate)

Score differential = Artifact total - Status Quo total

Opening Verdict derivation:
  differential >= +6   -->  Opening Verdict = PASS
  differential +1..+5  -->  Opening Verdict = CONDITIONAL
  differential <= 0    -->  Opening Verdict = FAIL
```

**LOCAL GATE LEDGER PROTOCOL** (fourth pre-committed contract):

```
Syntax:   one-row table: | Gate Verdict | Class | Source | Action |
Timing:   emitted at the END of each reviewer section, immediately after gate verdict
Coverage: MANDATORY for ALL sections -- §1.5 (bracket opening / inertia-advocate),
          §3 (each domain reviewer), §4 (lifecycle reviewer), §5 (bracket closing /
          inertia-advocate post-domain); no section is exempt
Assembly: §6 master action register copies all Local Gate Ledger rows from §1.5, §3, §4,
          and §5 verbatim. Do NOT re-derive Gate Verdict or Class during assembly.
```

**Severity Semantics** (applies throughout):

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

---

**§0 -- Scope Declaration**

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Any surface found mid-review not listed above is a scope gap. Flag it; do not absorb it.

---

**§1 -- Role Selection**

Read `.craft/roles/signal/`. No invented roles.

Branch on `{{reviewer_set}}`:
- Not "auto": use exactly those roles. Inertia-advocate must be present for §1.5 and §5;
  lifecycle must be present for §4. Add if missing; note the addition.
- "auto" + "standard": CHALLENGER slot (inertia-advocate archetype), >= 2 DOMAIN slots
  (technical/architecture archetype), LIFECYCLE slot (PM/program archetype). One-sentence
  rationale per role.
- "auto" + "deep": all roles for domain §3. State count.

Inertia-advocate is reserved for §1.5 and §5 (bracket positions) only.

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "deep run"]
    (inertia-advocate: §1.5 bracket opening + §5 bracket closing)
    (lifecycle reviewer: §4 post-domain, pre-bracket-closing)
```

---

**§1.5 -- Bracket Opening: Challenger Pre-Domain Testimony**

This section runs before domain (§3) and lifecycle (§4) reviewers. Neither has seen it.

```
## §1.5 -- Bracket Opening -- inertia-advocate

**Status quo statement**: [what the team does today instead of building this -- one sentence]

**Alternatives Table (challenger frame):**
| Dimension            | Status Quo | This Artifact | Rationale                |
|----------------------|-----------|---------------|--------------------------|
| D1 Switching cost    | [1-5]     | [1-5]         | [one sentence per cell]  |
| D2 Coverage          | [1-5]     | [1-5]         | [one sentence]           |
| D3 Adoption friction | [1-5]     | [1-5]         | [one sentence]           |
| D4 Time-to-value     | [1-5]     | [1-5]         | [one sentence]           |
| **TOTAL**            | [sum]     | [sum]         |                          |

**Score differential**: [artifact total] - [status quo total] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE applied**: [which branch]

**Challenge to domain reviewers**: [one specific question domain and lifecycle reviewers must
  address to change any of these dimension scores]

**Findings**: [2-3 from challenger's lens.verify supporting the table scores]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Opening Verdict] | [from CLASS DERIVATION CONTRACT] | §1.5 / inertia-advocate / [5-word] | [action] |
```

Domain sections (§3) begin only after Opening Verdict is emitted.

---

**§3 -- Domain Reviewer Sections**

Domain reviewers have access to the artifact only. They have not seen §1.5.

For each selected domain reviewer, re-score each dimension from this role's technical frame.
Mark unchanged dimensions explicitly. Keep findings distinct.

```
## §3 -- Domain Reviewer: [role] ([archetype])

**Domain re-read of alternatives table**
(Challenger's challenge: "[copy challenge text from §1.5]")

| Dimension            | Challenger Score | Revised Score | Justification or "unchanged" |
|----------------------|-----------------|---------------|------------------------------|
| D1 Switching cost    | [§1.5]          | [1-5]         | [sentence]                   |
| D2 Coverage          | [§1.5]          | [1-5]         | [sentence]                   |
| D3 Adoption friction | [§1.5]          | [1-5]         | [sentence]                   |
| D4 Time-to-value     | [§1.5]          | [1-5]         | [sentence]                   |

**[This role's null hypothesis address]**: [does the technical approach defeat the status quo?
  One sentence. Must differ from §1.5 framing and other domain reviewers.]

**Findings**: [2-4 from this role's lens.verify and expertise.depth; must not echo §1.5
  framing or other domain reviewer framing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict | Class | Source | Action |
|-------------|-------|--------|--------|
| [verdict] | [from CLASS DERIVATION CONTRACT] | §3 / [role] / [5-word] | [action] |
```

---

**§4 -- Lifecycle Reviewer (Post-Domain, Pre-Bracket-Closing)**

The lifecycle reviewer runs after all §3 domain sections and before §5 bracket closing.
Access: artifact only. The lifecycle reviewer has not seen §1.5 or §3.

The bracket closing (§5) will have access to both domain (§3) AND lifecycle (§4) verdicts.

```
## §4 -- Lifecycle Reviewer: [role] ([archetype])

**Commitment-readiness assessment**: [Is the alternatives table evidence sufficient to support
  a commitment decision? Reference the artifact's scope, risk declaration, and dependency
  completeness. One paragraph. Do not reference §1.5 scores directly -- lifecycle reviewer
  has not seen §1.5.]
**Findings**: [2-3 findings: commitment readiness, decision sufficiency, program concerns]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_lifecycle)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict   | Class | Source | Action |
|----------------|-------|--------|--------|
| [g_lifecycle]  | [from CLASS DERIVATION CONTRACT] | §4 / [lifecycle role] / [5-word] | [action] |
```

---

**§5 -- Bracket Closing: Challenger Post-Domain-and-Lifecycle Reassessment**

After all §3 domain sections and §4 lifecycle section. The inertia-advocate now has access
to domain re-reads AND the lifecycle verdict.

Question: Do the domain-adjusted dimension scores AND the lifecycle gate verdict, taken in
aggregate, constitute sufficient evidence to defeat the null hypothesis stated in §1.5?

Override authority: if domain re-reads inflate artifact scores without justification, or if
the aggregate evidence still fails to defeat the status quo, the Bracket Closing may override.

```
## §5 -- Bracket Closing -- inertia-advocate (post-domain-and-lifecycle reassessment)

**Domain re-read aggregation:**
| Reviewer | D1 | D2 | D3 | D4 | Null Hypothesis Address | Challenge Answered? |
|----------|----|----|----|----|-----------------------|---------------------|
| [role]   | [rev] | [rev] | [rev] | [rev] | [one sentence] | yes / partial / no |

**Lifecycle verdict received**: g_lifecycle = [value from §4]; interpretation: [one sentence
  on what the lifecycle finding implies for the null hypothesis challenge]

**Revised Alternatives Table (challenger vs domain-aggregate):**
| Dimension            | Status Quo | Artifact (challenger) | Artifact (domain avg) | Accepted Score |
|----------------------|-----------|----------------------|----------------------|----------------|
| D1 Switching cost    | [SQ]      | [§1.5]               | [domain avg]         | [final]        |
| D2 Coverage          | [SQ]      | [§1.5]               | [domain avg]         | [final]        |
| D3 Adoption friction | [SQ]      | [§1.5]               | [domain avg]         | [final]        |
| D4 Time-to-value     | [SQ]      | [§1.5]               | [domain avg]         | [final]        |
| **TOTAL**            | [SQ sum]  |                      |                      | [final sum]    |

**Revised score differential**: [final artifact sum] - [SQ sum] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE re-applied**: [which branch; state if verdict changes from §1.5]

**Assessment**: [Does the domain-adjusted table + lifecycle verdict change the verdict?
  What remains unaddressed?]
**Override authority**: [state explicitly if invoked and why]

**Closing Verdict**: FAIL | CONDITIONAL | PASS
**Override invoked**: YES | NO
  If YES: "Bracket Closing overrides per DISPOSITION CONTRACT -- DISPOSITION = BLOCKED."
  If NO: all verdicts from §1.5, §3, §4, and §5 feed DISPOSITION CONTRACT normally.

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Closing Verdict] | [from CLASS DERIVATION CONTRACT] | §5 / inertia-advocate / [5-word] | [action] |
```

This field is mandatory: emit Override invoked: YES | NO regardless.

---

**§6 -- Master Action Register**

Copy all Local Gate Ledger rows from §1.5, §3, §4, and §5 into the master table verbatim.
Do not re-derive Gate Verdict or Class. Copy exactly from each local row.

```
## §6 -- Master Action Register
(Consolidated from Local Gate Ledger rows in §1.5, §3, §4, §5 -- no re-derivation)

| # | Gate Verdict | Class | Source | Action |
|---|--------------|-------|--------|--------|
```

If Override invoked = YES in §5: add row: `§5 / inertia-advocate / override invoked --> BLOCKED`.

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**§7 -- Integrating Summary and Disposition**

Write 5-8 sentences:
- Name the highest-severity finding across all sections
- Name cross-role conflicts (incompatible recommendations)
- Name convergence areas
- Reference Opening Verdict (§1.5) -- include score differential
- Reference Closing Verdict (§5) and Override invoked field explicitly
- Reference g_lifecycle (§4) explicitly -- bracket closing had access to this verdict
- State which DISPOSITION CONTRACT branch applies and why

Apply the DISPOSITION CONTRACT from the preamble. State the branch.

```
## §7 -- Synthesis

[5-8 sentences]

FORMULA APPLIED: [which DISPOSITION CONTRACT branch and why]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## V-05 -- Combination: Three-Alternative Challenger + Full Pre-commitment Stack

**Variation axes**: Inertia framing (three-alternative challenger: Status Quo / This Artifact
/ Named Substitute, from V-03) combined with the full V-05 R5 mechanism stack -- DISPOSITION
CONTRACT + CLASS DERIVATION CONTRACT + NULL HYPOTHESIS DERIVATION RULE (extended to three
alternatives) + LOCAL GATE LEDGER PROTOCOL as fourth contract; adversarial bracket (C-09);
labeled override field (C-11); three-alternative Alternatives Table (C-16 extended); all three
algebraic contracts in preamble (C-17); local ledger at ALL sections (C-18); protocol in
preamble (C-19); verbatim assembly prohibition (C-20); universal archetype coverage including
lifecycle (C-21); three template variables (C-13 + C-15).

**Hypothesis**: V-03 tests three-alternative inertia framing as a single axis. V-05 combines
it with the complete mechanism stack from V-05 R5 (which proved 155/155). The key question:
does the extended three-alternative Alternatives Table (three columns instead of two) degrade
any of the criteria that V-05 R5 passed? Specifically, the NULL HYPOTHESIS DERIVATION RULE
now maps two score differentials (B-A and B-C) to one Opening Verdict -- does this more
complex derivation rule still satisfy C-17's pre-commitment requirement? Does domain re-scoring
of three alternatives per section still produce distinct findings per reviewer (C-01)? If
V-05 scores 155/155, the three-alternative frame is a drop-in replacement for the binary frame
at no cost to structural integrity.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first, before §0. Fill in injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

Read all four pre-committed contracts before any reviewer section executes. They do not change.

**DISPOSITION CONTRACT** (committed before execution; synthesis applies this formula):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL              -->  DISPOSITION = BLOCKED
  elif Override invoked = YES  (see §3)     -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL       -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS             -->  DISPOSITION = READY
  else                                      -->  DISPOSITION = CONDITIONAL  (ambiguous)
```

Gates that produce verdicts: Bracket Opening (§1.5), domain reviewers (§2), Bracket Closing
(§3), Lifecycle Reviewer (§5). The formula is the evaluator; editorial judgment does not
override it.

**CLASS DERIVATION CONTRACT** (committed before execution; no editorial re-assignment):

```
FAIL gate        -->  BLOCKED
CONDITIONAL gate -->  CONDITIONAL
PASS + HIGH      -->  CONDITIONAL
PASS + LOW       -->  ADVISORY
```

**NULL HYPOTHESIS DERIVATION RULE** (committed before execution; Opening Verdict derived from
both score differentials -- do not assert, derive; challenger MUST name Alternative C):

```
Alternatives:
  (A) Status Quo          -- what the team does today instead of building this
  (B) This Artifact       -- the artifact under review
  (C) Named Substitute    -- a SPECIFIC competing tool, approach, or workflow named by the
                             challenger; "TBD" or generic labels are not acceptable

Dimensions (scored 1-5 per alternative):
  D1 -- Switching cost       (1 = prohibitive to adopt B, 5 = negligible)
  D2 -- Coverage             (1 = B covers far less than A/C, 5 = B covers fully)
  D3 -- Adoption friction    (1 = high friction to adopt B, 5 = frictionless)
  D4 -- Time-to-value        (1 = months before value from B, 5 = immediate)

Primary differential   = B_total - A_total   (artifact vs status quo)
Secondary differential = B_total - C_total   (artifact vs named substitute)

Opening Verdict derivation:
  B_total > A_total by >= +6  AND  B_total > C_total  -->  PASS  (artifact dominates both)
  B_total > A_total by >= +6  BUT  B_total <= C_total -->  CONDITIONAL  (substitute competitive)
  B_total > A_total by +1..+5                         -->  CONDITIONAL  (marginal primary advantage)
  B_total <= A_total                                   -->  FAIL  (no case; status quo not beaten)
```

**LOCAL GATE LEDGER PROTOCOL** (fourth pre-committed contract; all sections without exception):

```
Syntax:   one-row table: | Gate Verdict | Class | Source | Action |
Timing:   emitted at the END of each reviewer section, immediately after the gate verdict
Coverage: MANDATORY for ALL sections -- §1.5 (bracket opening), §2 (each domain reviewer),
          §3 (bracket closing), §5 (lifecycle reviewer); no section is exempt
Assembly: §4 master action register copies all Local Gate Ledger rows from §1.5, §2, §3,
          and §5 verbatim. Do NOT re-derive Gate Verdict or Class during assembly.
```

**Severity Semantics** (applies throughout):

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

---

**§0 -- Scope Declaration**

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Any surface found mid-review not listed above is a scope gap. Flag it; do not absorb it.

---

**§1 -- Role Selection**

Read `.craft/roles/signal/`. No invented roles.

Branch on `{{reviewer_set}}`:
- Not "auto": use exactly those roles. Inertia-advocate must be present for §1.5 and §3;
  lifecycle must be present for §5. Add if missing; note the addition.
- "auto" + "standard": CHALLENGER slot (inertia-advocate archetype), >= 2 DOMAIN slots
  (technical/architecture archetype), LIFECYCLE slot (PM/program archetype). Rationale per role.
- "auto" + "deep": all roles. State count.

Inertia-advocate is reserved for §1.5 (bracket opening) and §3 (bracket closing) only.

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "deep run"]
    (inertia-advocate: §1.5 bracket opening + §3 bracket closing)
    (lifecycle reviewer: §5 post-bracket-closing)
```

---

**§1.5 -- Bracket Opening: Three-Alternative Challenger**

This section runs before all domain (§2) and lifecycle (§5) reviewers. None has seen it.

Name Alternative C explicitly. Populate all three alternatives for all four dimensions. Apply
the NULL HYPOTHESIS DERIVATION RULE using both differentials. Do not assert Opening Verdict.

```
## §1.5 -- Bracket Opening -- inertia-advocate

**Status quo statement (A)**: [what the team does today -- one sentence]
**Named substitute (C)**: [SPECIFIC competing tool, approach, or workflow -- name explicitly;
  "TBD" is not acceptable]

**Three-Alternative Alternatives Table (challenger frame):**
| Dimension            | (A) Status Quo | (B) This Artifact | (C) Named Substitute | Rationale |
|----------------------|---------------|------------------|---------------------|-----------|
| D1 Switching cost    | [1-5]         | [1-5]            | [1-5]               | [sentence] |
| D2 Coverage          | [1-5]         | [1-5]            | [1-5]               | [sentence] |
| D3 Adoption friction | [1-5]         | [1-5]            | [1-5]               | [sentence] |
| D4 Time-to-value     | [1-5]         | [1-5]            | [1-5]               | [sentence] |
| **TOTAL**            | [sum]         | [sum]            | [sum]               |           |

**Primary differential (B-A)**: [B total] - [A total] = [+/- n]
**Secondary differential (B-C)**: [B total] - [C total] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE applied**: [which branch; cite both differentials]

**Challenge to domain reviewers**: [one specific question domain reviewers must address to
  change any B-column or C-column scores; this is the anchor all downstream reviewers
  respond to]

**Findings**: [2-3 from challenger's lens.verify supporting the table scores]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Opening Verdict] | [from CLASS DERIVATION CONTRACT] | §1.5 / inertia-advocate / [5-word] | [action] |
```

Domain sections (§2) begin only after Opening Verdict is emitted.

---

**§2 -- Domain Reviewer Sections**

Domain reviewers have access to the artifact only. They have not seen §1.5.

For each selected domain reviewer, re-score B and C on all four dimensions from this role's
technical frame. A-column scores are not re-scored (status quo is the challenger's frame to
set). Mark unchanged scores explicitly. Challenge from §1.5 must be addressed.

```
## §2 -- Domain Reviewer: [role] ([archetype])

**Three-alternative re-read**
(Challenger's challenge: "[copy challenge text from §1.5]")

| Dimension            | (A) SQ [§1.5] | (B) Artifact Challenger | (B) Revised | (C) Sub Challenger | (C) Revised | Justification |
|----------------------|--------------|------------------------|------------|-------------------|------------|---------------|
| D1 Switching cost    | [§1.5 A]     | [§1.5 B]               | [1-5]      | [§1.5 C]          | [1-5]      | [or "unchanged"] |
| D2 Coverage          | [§1.5 A]     | [§1.5 B]               | [1-5]      | [§1.5 C]          | [1-5]      | [or "unchanged"] |
| D3 Adoption friction | [§1.5 A]     | [§1.5 B]               | [1-5]      | [§1.5 C]          | [1-5]      | [or "unchanged"] |
| D4 Time-to-value     | [§1.5 A]     | [§1.5 B]               | [1-5]      | [§1.5 C]          | [1-5]      | [or "unchanged"] |

**[This role's null hypothesis address]**: [from this domain frame, does (B) outperform both
  (A) and (C)? One sentence. Must differ from §1.5 framing and other domain reviewers.]

**Findings**: [2-4 from this role's lens.verify and expertise.depth; must not echo §1.5
  framing or other domain reviewer framing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_domain)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict | Class | Source | Action |
|-------------|-------|--------|--------|
| [g_domain] | [from CLASS DERIVATION CONTRACT] | §2 / [role] / [5-word] | [action] |
```

---

**§3 -- Bracket Closing: Challenger Post-Domain Reassessment**

After all §2 domain sections. The inertia-advocate now has access to domain re-reads.

Question: Do the domain-adjusted scores, for all three alternatives, constitute sufficient
evidence to defeat the null hypothesis stated in §1.5?

Override authority: if domain re-reads inflate B-column or undervalue C-column scores without
technical justification, or if the adjusted verdict still fails the null hypothesis, the
Bracket Closing may override.

```
## §3 -- Bracket Closing -- inertia-advocate (post-domain reassessment)

**Domain re-read aggregation:**
| Reviewer | D1(B) rev | D2(B) rev | D3(B) rev | D4(B) rev | D1(C) rev | D2(C) rev | D3(C) rev | D4(C) rev | Challenge Answered? |
|----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|---------------------|
| [role]   | [val]     | [val]     | [val]     | [val]     | [val]     | [val]     | [val]     | [val]     | yes / partial / no  |

**Revised Three-Alternative Table (challenger vs domain-aggregate):**
| Dimension            | (A) SQ | (B) Challenger | (B) Domain Avg | (B) Accepted | (C) Challenger | (C) Domain Avg | (C) Accepted |
|----------------------|--------|---------------|----------------|-------------|---------------|----------------|-------------|
| D1 Switching cost    | [A]    | [§1.5 B]      | [dom avg]      | [final B]   | [§1.5 C]      | [dom avg]      | [final C]   |
| D2 Coverage          | [A]    | [§1.5 B]      | [dom avg]      | [final B]   | [§1.5 C]      | [dom avg]      | [final C]   |
| D3 Adoption friction | [A]    | [§1.5 B]      | [dom avg]      | [final B]   | [§1.5 C]      | [dom avg]      | [final C]   |
| D4 Time-to-value     | [A]    | [§1.5 B]      | [dom avg]      | [final B]   | [§1.5 C]      | [dom avg]      | [final C]   |
| **TOTAL**            | [A sum]|               |                | [B sum]     |               |                | [C sum]     |

**Revised primary differential (B-A)**: [B accepted] - [A sum] = [+/- n]
**Revised secondary differential (B-C)**: [B accepted] - [C accepted] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE re-applied**: [which branch; cite both revised differentials;
  state if verdict changes from §1.5]

**Assessment**: [Does the domain-adjusted table change the verdict? What gaps remain?]
**Override authority**: [state explicitly if invoked and the basis for invoking]

**Closing Verdict**: FAIL | CONDITIONAL | PASS
**Override invoked**: YES | NO
  If YES: "Bracket Closing overrides per DISPOSITION CONTRACT -- DISPOSITION = BLOCKED."
  If NO: all verdicts from §1.5, §2, §3, and §5 feed DISPOSITION CONTRACT normally.

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Closing Verdict] | [from CLASS DERIVATION CONTRACT] | §3 / inertia-advocate / [5-word] | [action] |
```

This field is mandatory: emit Override invoked: YES | NO regardless.

---

**§4 -- Master Action Register**

Copy all Local Gate Ledger rows from §1.5, §2, §3, and §5 into the master table verbatim.
Do not re-derive Gate Verdict or Class. The register is a copy, not a synthesis.

(§5 lifecycle rows are added after §5 executes. The register is assembled after §5 completes.)

```
## §4 -- Master Action Register
(Consolidated from Local Gate Ledger rows in §1.5, §2, §3, §5 -- no re-derivation)

| # | Gate Verdict | Class | Source | Action |
|---|--------------|-------|--------|--------|
```

If Override invoked = YES in §3: add row: `§3 / inertia-advocate / override invoked --> BLOCKED`.

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**§5 -- Lifecycle Reviewer**

After all §2 domain sections and §3 bracket closing. Access: artifact only.

```
## §5 -- Lifecycle Reviewer: [role] ([archetype])

**Commitment-readiness assessment**: [Is the three-alternative comparison evidence sufficient
  to support a commitment decision? Reference that (B) is being compared against both (A) and
  a named substitute (C). One paragraph.]
**Findings**: [2-3 findings: commitment readiness, decision sufficiency, program concerns]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_lifecycle)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict   | Class | Source | Action |
|----------------|-------|--------|--------|
| [g_lifecycle]  | [from CLASS DERIVATION CONTRACT] | §5 / [lifecycle role] / [5-word] | [action] |
```

After §5 completes: add the §5 Local Gate Ledger row to the Master Action Register (§4).

---

**§6 -- Integrating Summary and Disposition**

Write 5-8 sentences:
- Name the highest-severity finding across all sections
- Name cross-role conflicts (incompatible recommendations from two sections)
- Name convergence areas (multiple reviewers flagging the same gap independently)
- Reference Opening Verdict (§1.5) -- cite both differentials (B-A and B-C)
- Reference Closing Verdict (§3) and Override invoked explicitly
- Reference g_lifecycle (§5) explicitly
- State which DISPOSITION CONTRACT branch applies and why

Apply the DISPOSITION CONTRACT from the preamble. State the branch.

```
## §6 -- Synthesis

[5-8 sentences]

FORMULA APPLIED: [which DISPOSITION CONTRACT branch and why]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}
