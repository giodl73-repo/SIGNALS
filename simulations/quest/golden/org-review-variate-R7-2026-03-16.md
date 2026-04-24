# org-review Variations -- Round 7 (v6 rubric, 2026-03-16)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v6-2026-03-16.md

Prior round summary:
- R1 (v1 rubric): V-05=95, V-04=90.
- R2 (v2 rubric): V-04=110. First Gold.
- R3 (v3 rubric): V-05=125. Aspirational frontier closed.
- R4 (v3->v4 rubric): V-05=135 (C-16+C-17 PASS, C-18 FAIL). Perfect not yet achieved.
- R5 (v4->v5 rubric): V-05=155/155 (Perfect). V-04=150/155 (C-21 FAIL).
- R6 (v5->v6 rubric): V-03=V-04=V-05=160/165. v6 introduces C-22 and C-23.
  V-04: lifecycle §4 before bracket closing §5 -- C-22 PASS. Two-alternative table -- C-23 vacuous. 160/165.
  V-03/V-05: three-alternative table, two-differential rule -- C-23 PASS. Bracket before lifecycle -- C-22 FAIL. 160/165.
  No R6 variant holds both C-22 and C-23 simultaneously. Perfect (165) not yet achieved.

Round 7 strategy:
- Primary objective: combine C-22 (V-04 R6 architecture) + C-23 (V-03/V-05 R6 table design).
- V-01: single axis -- role sequence (lifecycle §4 before bracket §5) PLUS three-alternative table.
        Direct combination. Tests whether the two 160-pt architectures merge cleanly to 165.
- V-02: single axis -- phrasing register (formal attestation language on V-01 architecture).
        Register invariance test on the combined 165 path.
- V-03: single axis -- inertia framing (four-alternative table: Status Quo + Build + Named
        Substitute + Hybrid). Extends C-23 to four alternatives; NULL HYPOTHESIS DERIVATION RULE
        covers all three differentials (B-A, B-C, B-D). Lifecycle §4 before bracket §5.
- V-04: combination -- V-01 architecture + full four-contract preamble with enhanced dimension
        semantics (per-cell scoring guide in preamble) + domain-aggregate formula committed.
- V-05: combination -- V-01 architecture + condensed section format + explicit domain-synthesis
        checkpoint between domain §3 and lifecycle §4 that pre-computes domain-aggregate scores
        so lifecycle §4 and bracket closing §5 receive a clean aggregate input.

Expected score ladder (v6 rubric, 165 pts max):
  V-01: 60+30+75=165  -- Perfect attempt: C-22+C-23 combined
  V-02: 165           -- Register invariance test; same expected score
  V-03: 60+30+75=165  -- Four-alternative C-23; C-22 maintained
  V-04: 60+30+75=165  -- Full pre-commitment + enhanced tables
  V-05: 60+30+75=165  -- Domain-aggregate checkpoint variant

---

## V-01 -- Role Sequence + Three-Alternative Table (Direct 165/165 Attempt)

**Variation axis**: Role sequence + inertia framing combined in minimal change from R6 ancestors.
The only structural changes from V-04 R6: (1) expand the two-column Alternatives Table to three
columns (Status Quo A, Build B, Named Substitute C); (2) expand the NULL HYPOTHESIS DERIVATION
RULE to cover both B-A and B-C differentials; (3) domain reviewers re-score all three
alternatives; (4) bracket closing names both differentials when reassessing. Everything else is
V-04 R6 verbatim -- including lifecycle §4 before bracket closing §5.

**Hypothesis**: V-04 R6 scores 160/165: C-22 PASS (lifecycle before bracket closing), C-23
vacuous (two-alternative table). V-03/V-05 R6 score 160/165: C-23 PASS (three-alternative
table), C-22 FAIL (bracket before lifecycle). Adding a Named Substitute column to V-04 R6 while
keeping lifecycle §4 before bracket §5 satisfies BOTH C-22 and C-23 simultaneously -- the first
time the two conditions co-exist in a single prompt. If this variant scores 165/165, it proves
the combination is architecturally clean and not in tension.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
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

**NULL HYPOTHESIS DERIVATION RULE** (committed before execution; Opening Verdict derives from
BOTH score differentials -- do not assert, derive both):

```
Dimensions (scored 1-5 per alternative):
  D1 -- Switching cost       (1 = prohibitive to adopt artifact, 5 = negligible)
  D2 -- Coverage             (1 = artifact covers far less than status quo, 5 = complete)
  D3 -- Adoption friction    (1 = high friction, 5 = frictionless)
  D4 -- Time-to-value        (1 = months before value, 5 = immediate)

Three alternatives scored per dimension:
  A = Status Quo (what teams do today without this artifact)
  B = This Artifact (the thing under review)
  C = Named Substitute (the most credible non-build alternative; name it explicitly)

Primary differential   = B_total - A_total  (does build beat doing nothing?)
Secondary differential = B_total - C_total  (does build beat the best alternative?)

Opening Verdict derivation (both differentials must satisfy their condition):
  primary >= +4 AND secondary >= 0  -->  Opening Verdict = PASS
  primary >= +1 AND secondary < 0   -->  Opening Verdict = CONDITIONAL  (beats SQ, loses to sub)
  primary >= +4 AND secondary < -3  -->  Opening Verdict = CONDITIONAL  (strong vs SQ, weak vs sub)
  primary <= 0                      -->  Opening Verdict = FAIL           (does not beat SQ)
  (any ambiguous combination)       -->  Opening Verdict = CONDITIONAL
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

Read `.roles/signal/`. No invented roles.

Branch on `{{reviewer_set}}`:
- Not "auto": use exactly those roles. Inertia-advocate must be present for §1.5 and §5;
  lifecycle must be present for §4. Add if missing; note the addition.
- "auto" + "standard": CHALLENGER slot (inertia-advocate archetype), >= 2 DOMAIN slots
  (technical/architecture archetype), LIFECYCLE slot (PM/program archetype). One-sentence
  rationale per role.
- "auto" + "deep": all roles for domain §3. State count.

Inertia-advocate is reserved for §1.5 (bracket opening) and §5 (bracket closing) only.

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "deep run"]
    (inertia-advocate: §1.5 bracket opening + §5 bracket closing)
    (lifecycle reviewer: §4 post-domain, pre-bracket-closing)
    Named Substitute identified: [name the most credible non-build alternative]
```

---

**§1.5 -- Bracket Opening: Challenger Pre-Domain Testimony**

This section runs before domain (§3) and lifecycle (§4) reviewers. Neither has seen it.

```
## §1.5 -- Bracket Opening -- inertia-advocate

**Status quo statement**: [what the team does today instead of building this -- one sentence]
**Named Substitute**: [name the most credible non-build alternative; one sentence justifying
  why this is the strongest alternative to build]

**Three-Alternative Table (challenger frame):**
| Dimension            | (A) Status Quo | (B) This Artifact | (C) Named Substitute |
|----------------------|---------------|-------------------|----------------------|
| D1 Switching cost    | [1-5]         | [1-5]             | [1-5]                |
| D2 Coverage          | [1-5]         | [1-5]             | [1-5]                |
| D3 Adoption friction | [1-5]         | [1-5]             | [1-5]                |
| D4 Time-to-value     | [1-5]         | [1-5]             | [1-5]                |
| **TOTAL**            | [A sum]       | [B sum]           | [C sum]              |

**Primary differential (B - A)**: [B sum] - [A sum] = [+/- n]
**Secondary differential (B - C)**: [B sum] - [C sum] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE applied**: [cite both differentials; state which branch]

**Challenge to domain reviewers**: [one specific question that, if answered, would justify
  revising any dimension score for artifact B or substitute C]

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

For each selected domain reviewer, re-score each dimension for BOTH artifact B and substitute C.
Mark unchanged scores explicitly.

```
## §3 -- Domain Reviewer: [role] ([archetype])

**Domain re-read of three-alternative table**
(Challenger's challenge: "[copy challenge text from §1.5]")

| Dimension            | (A) SQ | (B) Challenger | (B) Revised | (C) Challenger | (C) Revised |
|----------------------|--------|---------------|-------------|---------------|-------------|
| D1 Switching cost    | [A]    | [§1.5 B]      | [1-5]       | [§1.5 C]      | [1-5]       |
| D2 Coverage          | [A]    | [§1.5 B]      | [1-5]       | [§1.5 C]      | [1-5]       |
| D3 Adoption friction | [A]    | [§1.5 B]      | [1-5]       | [§1.5 C]      | [1-5]       |
| D4 Time-to-value     | [A]    | [§1.5 B]      | [1-5]       | [§1.5 C]      | [1-5]       |

**[This role's null hypothesis address]**: [does the technical approach defeat status quo AND
  substitute? One sentence. Must address both differentials.]

**Findings**: [2-4 from this role's lens.verify and expertise.depth; must not echo §1.5]
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

The lifecycle reviewer runs AFTER all §3 domain sections and BEFORE §5 bracket closing.
Access: artifact only. Lifecycle reviewer has not seen §1.5 or §3.

The bracket closing (§5) will receive both domain verdicts (§3) AND g_lifecycle (§4) before
reassessing the null hypothesis.

```
## §4 -- Lifecycle Reviewer: [role] ([archetype])

**Commitment-readiness assessment**: [Is the three-alternative evidence sufficient to support
  a commitment decision? Reference artifact scope, migration cost, adoption plan, and decision
  completeness. One paragraph. Do not reference §1.5 scores directly.]
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
to domain re-reads AND the lifecycle verdict. This is structurally distinct from R6 V-03/V-05
where bracket closing preceded lifecycle testimony.

Question: Do the domain-adjusted dimension scores (for BOTH B and C) AND the lifecycle gate
verdict, taken in aggregate, constitute sufficient evidence to defeat the null hypothesis
stated in §1.5? The challenger must apply the NULL HYPOTHESIS DERIVATION RULE to revised
scores, citing both differentials.

Override authority: if domain re-reads inflate artifact scores without justification, or if
the null hypothesis is not defeated under revised scores, the Bracket Closing may override.

```
## §5 -- Bracket Closing -- inertia-advocate (post-domain-and-lifecycle reassessment)

**Lifecycle verdict received**: g_lifecycle = [value from §4 Local Gate Ledger]; interpretation:
  [one sentence: what does this lifecycle verdict mean for the null hypothesis?]

**Domain re-read aggregation:**
| Reviewer | D1(B) | D2(B) | D3(B) | D4(B) | D1(C) | D2(C) | D3(C) | D4(C) | Challenge Answered? |
|----------|-------|-------|-------|-------|-------|-------|-------|-------|---------------------|
| [role]   | [rev] | [rev] | [rev] | [rev] | [rev] | [rev] | [rev] | [rev] | yes / partial / no  |

**Revised Three-Alternative Table (challenger + domain aggregate + lifecycle context):**
| Dimension            | (A) Status Quo | (B) Opening | (B) Domain Avg | (B) Accepted | (C) Opening | (C) Domain Avg | (C) Accepted |
|----------------------|---------------|-------------|----------------|-------------|-------------|----------------|-------------|
| D1 Switching cost    | [A]           | [§1.5 B]    | [avg]          | [final B]   | [§1.5 C]    | [avg]          | [final C]   |
| D2 Coverage          | [A]           | [§1.5 B]    | [avg]          | [final B]   | [§1.5 C]    | [avg]          | [final C]   |
| D3 Adoption friction | [A]           | [§1.5 B]    | [avg]          | [final B]   | [§1.5 C]    | [avg]          | [final C]   |
| D4 Time-to-value     | [A]           | [§1.5 B]    | [avg]          | [final B]   | [§1.5 C]    | [avg]          | [final C]   |
| **TOTAL**            | [A sum]       |             |                | [B sum]     |             |                | [C sum]     |

**Revised primary differential (B - A)**: [B accepted] - [A sum] = [+/- n]
**Revised secondary differential (B - C)**: [B accepted] - [C accepted] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE re-applied**: [cite both revised differentials; state which
  branch; state if verdict changes from §1.5; reference g_lifecycle as additional signal]

**Closing Verdict**: FAIL | CONDITIONAL | PASS
**Override invoked**: YES | NO
  If YES: "Bracket Closing overrides per DISPOSITION CONTRACT -- DISPOSITION = BLOCKED."
  If NO: domain verdicts stand; Closing Verdict feeds DISPOSITION CONTRACT normally.

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Closing Verdict] | [from CLASS DERIVATION CONTRACT] | §5 / inertia-advocate / [5-word] | [action] |
```

This field is mandatory: emit Override invoked: YES | NO regardless of whether override is
exercised.

---

**§6 -- Master Action Register**

Copy all Local Gate Ledger rows from §1.5, §3 (all domain reviewers), §4, and §5 verbatim.
Do not re-derive Gate Verdict or Class. The register is a copy, not a synthesis.

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
- Name cross-role conflicts (incompatible recommendations from two sections)
- Name convergence areas
- Reference Opening Verdict (§1.5) -- cite both primary and secondary differentials
- Reference Closing Verdict (§5) and g_lifecycle (§4) explicitly by name
- Reference Override invoked field explicitly
- State which DISPOSITION CONTRACT branch applies

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

## V-02 -- Phrasing Register: Formal Attestation Language on V-01 Architecture

**Variation axis**: Phrasing register -- every structural output uses formal attestation
language throughout. Same section ordering, same table structure, same pre-committed contracts
as V-01. The only variable: lexicon shifts from operational to audit-formal register.

**Hypothesis**: V-02 R6 (register variation on non-bracket architecture) was register-invariant
at 140/140. V-01 establishes the 165/165 combined architecture. This variant tests whether
formal attestation language is invariant on the combined architecture -- specifically whether
C-22's "Lifecycle verdict received: g_lifecycle = [value]" labeled field requirement is
satisfied regardless of the surrounding phrasing register.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
```

Emit this block first. Fill in injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below. All reviewer sections use formal
attestation register. Reviewers attest verdicts; they do not narrate them.

Read all four pre-committed contracts before any reviewer section executes. They do not change.

**DISPOSITION CONTRACT** (committed; attested by synthesis section; not re-derived):

```
ATTESTATION DISPOSITION FORMULA:
  Attested: any gate = FAIL              -->  DISPOSITION = BLOCKED
  Attested: Override invoked = YES       -->  DISPOSITION = BLOCKED
  Attested: any gate = CONDITIONAL       -->  DISPOSITION = CONDITIONAL
  Attested: all gates = PASS             -->  DISPOSITION = READY
  Attested: (ambiguous)                  -->  DISPOSITION = CONDITIONAL
```

Gates attesting verdicts: §1.5 (inertia-advocate, opening), §3 (domain reviewers), §4
(lifecycle reviewer), §5 (inertia-advocate, closing).

**CLASS DERIVATION CONTRACT** (attested; classes not re-derived at synthesis):

```
FAIL gate attested        -->  BLOCKED
CONDITIONAL gate attested -->  CONDITIONAL
PASS attested + HIGH      -->  CONDITIONAL
PASS attested + LOW       -->  ADVISORY
```

**NULL HYPOTHESIS DERIVATION RULE** (attested in preamble; both differentials must be cited):

```
Dimension scoring (1-5 per alternative, per section):
  D1 -- Switching cost       (1 = prohibitive, 5 = negligible)
  D2 -- Coverage             (1 = incomplete vs status quo, 5 = complete)
  D3 -- Adoption friction    (1 = high friction, 5 = frictionless)
  D4 -- Time-to-value        (1 = long lag, 5 = immediate)

A = Status Quo | B = This Artifact | C = Named Substitute (named at §1.5)

Attested primary differential   = B_total - A_total
Attested secondary differential = B_total - C_total

Opening Verdict attestation:
  primary >= +4 AND secondary >= 0  -->  PASS        (artifact attests superiority on both)
  primary >= +1 AND secondary < 0   -->  CONDITIONAL (exceeds SQ; does not exceed substitute)
  primary >= +4 AND secondary < -3  -->  CONDITIONAL (strong vs SQ; substitute still preferred)
  primary <= 0                      -->  FAIL         (artifact does not exceed status quo)
```

**LOCAL GATE LEDGER PROTOCOL** (fourth pre-committed attestation contract):

```
Syntax:   one-row table: | Gate Verdict | Class | Source | Action |
Timing:   attested at the END of each reviewer section, immediately after gate verdict
Coverage: MANDATORY attestation for ALL sections -- §1.5, §3 (each domain reviewer),
          §4 (lifecycle), §5 (bracket closing); no section exempt from attestation
Assembly: §6 master register copies all attested Local Gate Ledger rows from §1.5, §3, §4,
          and §5 verbatim. Gate Verdict and Class are NOT re-derived during assembly.
```

**Severity Attestation Semantics:**

| Severity | Attested commit-gate meaning |
|----------|------------------------------|
| HIGH | Attests: blocks commitment to proceed |
| MEDIUM | Attests: commitment conditional on remediation |
| LOW | Attests: advisory; commitment may proceed |

---

**§0 -- Scope Attestation**

```
ATTESTED IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
ATTESTED OUT OF SCOPE:
- [surfaces not attested in this pass]
```

Any surface found mid-review not attested above is a scope gap. Attest it; do not absorb it.

---

**§1 -- Role Selection Attestation**

Read `.roles/signal/`. No invented roles.

```
Depth mode attested: {{depth}}
Reviewer set attested: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "attested explicit" | "attested deep run"]
    (inertia-advocate: §1.5 bracket opening + §5 bracket closing -- attested reserved)
    (lifecycle reviewer: §4 post-domain, pre-bracket-closing -- attested sequenced)
    Named Substitute attested: [name of most credible non-build alternative]
```

---

**§1.5 -- Bracket Opening Attestation: Inertia-Advocate Pre-Domain**

```
## §1.5 -- Bracket Opening -- inertia-advocate (attesting null hypothesis)

**Attested status quo**: [what teams do today without this artifact -- one sentence]
**Attested Named Substitute**: [name; one sentence justifying why this is the strongest
  alternative to building]

**Three-Alternative Dimension Attestation Table:**
| Dimension            | (A) Status Quo | (B) This Artifact | (C) Named Substitute |
|----------------------|---------------|-------------------|----------------------|
| D1 Switching cost    | [1-5]         | [1-5]             | [1-5]                |
| D2 Coverage          | [1-5]         | [1-5]             | [1-5]                |
| D3 Adoption friction | [1-5]         | [1-5]             | [1-5]                |
| D4 Time-to-value     | [1-5]         | [1-5]             | [1-5]                |
| **TOTAL**            | [A sum]       | [B sum]           | [C sum]              |

**Attested primary differential (B - A)**: [+/- n]
**Attested secondary differential (B - C)**: [+/- n]
**Null hypothesis derivation rule attested**: [cite both differentials; state branch]

**Attested challenge to domain reviewers**: [the one evidentiary question that would change
  a dimension score for B or C -- stated as a testable attestation]

**Attested findings**: [2-3 from inertia-advocate lens.verify]
**Severity attested**: HIGH | MEDIUM | LOW
**Verify attestation**: [one from inertia-advocate's lens.verify]
**Opening Verdict attested**: FAIL | CONDITIONAL | PASS
**Override authority attested**: YES -- a FAIL at Bracket Closing overrides all domain PASS.

**Local Gate Ledger (attested):**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Opening Verdict] | [from CLASS DERIVATION CONTRACT] | §1.5 / inertia-advocate / [5-word] | [action] |
```

---

**§3 -- Domain Reviewer Attestation Sections**

Domain reviewers have access to the artifact only. They have not seen §1.5 attestations.

For each selected domain reviewer, attest revised scores for BOTH B and C:

```
## §3 -- Domain Reviewer Attestation: [role] ([archetype])

**Domain re-attestation of three-alternative table**
(Challenge attested by §1.5: "[copy challenge text]")

| Dimension            | (A) SQ | (B) Attested | (B) Re-attested | (C) Attested | (C) Re-attested |
|----------------------|--------|-------------|-----------------|-------------|-----------------|
| D1 Switching cost    | [A]    | [§1.5 B]    | [1-5]           | [§1.5 C]    | [1-5]           |
| D2 Coverage          | [A]    | [§1.5 B]    | [1-5]           | [§1.5 C]    | [1-5]           |
| D3 Adoption friction | [A]    | [§1.5 B]    | [1-5]           | [§1.5 C]    | [1-5]           |
| D4 Time-to-value     | [A]    | [§1.5 B]    | [1-5]           | [§1.5 C]    | [1-5]           |

**Attested null hypothesis position**: [does this domain expertise confirm artifact defeats
  both status quo and substitute? One sentence. Attest; do not narrate.]

**Attested findings**: [2-4 from this role's lens.verify; must not echo §1.5 attestations]
**Severity attested**: HIGH | MEDIUM | LOW
**Recommendation attested**: [one concrete action]
**Verify attestation**: [one from this role's lens.verify]
**Simplify attestation**: [one from this role's lens.simplify]
**Gate Verdict attested**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger (attested):**
| Gate Verdict | Class | Source | Action |
|-------------|-------|--------|--------|
| [verdict] | [from CLASS DERIVATION CONTRACT] | §3 / [role] / [5-word] | [action] |
```

---

**§4 -- Lifecycle Reviewer Attestation (Post-Domain, Pre-Bracket-Closing)**

Lifecycle reviewer attests commitment readiness AFTER domain sections, BEFORE bracket closing.
Access: artifact only. Has not seen §1.5 or §3 attestations.

```
## §4 -- Lifecycle Reviewer Attestation: [role] ([archetype])

**Commitment readiness attested**: [Is evidence sufficient for a commitment decision? Attest
  yes, conditional, or no. Reference scope, migration risk, adoption plan. One paragraph.]
**Attested findings**: [2-3: commitment readiness, decision completeness, program concerns]
**Severity attested**: HIGH | MEDIUM | LOW
**Recommendation attested**: [one concrete action]
**Verify attestation**: [one from this role's lens.verify]
**Simplify attestation**: [one from this role's lens.simplify]
**Gate Verdict attested (g_lifecycle)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger (attested):**
| Gate Verdict   | Class | Source | Action |
|----------------|-------|--------|--------|
| [g_lifecycle]  | [from CLASS DERIVATION CONTRACT] | §4 / [lifecycle role] / [5-word] | [action] |
```

---

**§5 -- Bracket Closing Attestation: Inertia-Advocate Post-Domain-and-Lifecycle**

Inertia-advocate now has access to domain re-attestations AND lifecycle verdict attestation.
This is the first attestation that integrates all gate signals.

```
## §5 -- Bracket Closing Attestation -- inertia-advocate

**Lifecycle verdict attested received**: g_lifecycle = [value from §4 Local Gate Ledger];
  attestation: [one sentence -- what this lifecycle verdict means for null hypothesis]

**Domain re-attestation aggregation:**
| Reviewer | D1(B) | D2(B) | D3(B) | D4(B) | D1(C) | D2(C) | D3(C) | D4(C) | Challenge Attested? |
|----------|-------|-------|-------|-------|-------|-------|-------|-------|---------------------|
| [role]   | [rev] | [rev] | [rev] | [rev] | [rev] | [rev] | [rev] | [rev] | yes / partial / no  |

**Revised Three-Alternative Table (domain-aggregate + lifecycle integration):**
| Dimension            | (A) Status Quo | (B) Opening | (B) Domain Avg | (B) Accepted | (C) Opening | (C) Domain Avg | (C) Accepted |
|----------------------|---------------|-------------|----------------|-------------|-------------|----------------|-------------|
| D1 Switching cost    | [A]           | [§1.5 B]    | [avg]          | [final]     | [§1.5 C]    | [avg]          | [final]     |
| D2 Coverage          | [A]           | [§1.5 B]    | [avg]          | [final]     | [§1.5 C]    | [avg]          | [final]     |
| D3 Adoption friction | [A]           | [§1.5 B]    | [avg]          | [final]     | [§1.5 C]    | [avg]          | [final]     |
| D4 Time-to-value     | [A]           | [§1.5 B]    | [avg]          | [final]     | [§1.5 C]    | [avg]          | [final]     |
| **TOTAL**            | [A sum]       |             |                | [B sum]     |             |                | [C sum]     |

**Attested revised primary differential (B - A)**: [+/- n]
**Attested revised secondary differential (B - C)**: [+/- n]
**Null hypothesis derivation rule re-attested**: [cite both revised differentials and
  g_lifecycle; state which branch; state if verdict changes from §1.5]

**Closing Verdict attested**: FAIL | CONDITIONAL | PASS
**Override invoked attested**: YES | NO
  If YES: "Bracket Closing override attested -- DISPOSITION = BLOCKED per DISPOSITION CONTRACT."
  If NO: domain attestations stand; Closing Verdict attested into DISPOSITION CONTRACT.

**Local Gate Ledger (attested):**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Closing Verdict] | [from CLASS DERIVATION CONTRACT] | §5 / inertia-advocate / [5-word] | [action] |
```

---

**§6 -- Master Action Register (Verbatim Attestation Copy)**

Copy all attested Local Gate Ledger rows from §1.5, §3, §4, §5 verbatim.
No re-derivation. No re-attestation. The register attests to what each section attested.

```
## §6 -- Master Action Register
(Attested verbatim copy from §1.5, §3, §4, §5 -- no re-derivation)

| # | Gate Verdict | Class | Source | Action |
|---|--------------|-------|--------|--------|
```

---

**§7 -- Integrating Synthesis Attestation**

Attest:
- Highest-severity finding across all sections
- Cross-section conflicts (incompatible attestations)
- Convergence (all sections agree on a verdict)
- Opening Verdict (§1.5): both primary and secondary differentials attested
- g_lifecycle (§4): value and interpretation attested
- Closing Verdict (§5): value and Override invoked field attested by name
- DISPOSITION CONTRACT branch attested

```
## §7 -- Synthesis

[5-8 sentences in attestation register]

FORMULA ATTESTED: [which DISPOSITION CONTRACT branch; why]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## V-03 -- Inertia Framing: Four-Alternative Table

**Variation axis**: Inertia framing -- expand from three to four alternatives: Status Quo (A),
This Artifact (B), Named Substitute (C), Hybrid (D). The NULL HYPOTHESIS DERIVATION RULE covers
all three relevant pairwise differentials involving the artifact: B-A, B-C, B-D. The inertia-
advocate must defend BOTH the strongest non-build alternative (C or D, whichever scores higher)
AND the status quo. Role sequencing is identical to V-01 (lifecycle §4 before bracket §5).

**Hypothesis**: C-23 passes when "the alternatives table contains three or more options" and
"the NULL HYPOTHESIS DERIVATION RULE names all relevant pairwise differentials involving the
proposed artifact." Four alternatives extend C-23 beyond the three-alternative minimum. If a
four-alternative table with a three-differential rule satisfies C-23, it validates that the
criterion generalizes beyond the minimal case. Combined with V-01 lifecycle sequencing (C-22),
this variant tests the 165/165 path via a four-alternative framing rather than three.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
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

Read all four pre-committed contracts before any reviewer section executes.

**DISPOSITION CONTRACT** (committed before execution):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL              -->  DISPOSITION = BLOCKED
  elif Override invoked = YES  (see §5)     -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL       -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS             -->  DISPOSITION = READY
  else                                      -->  DISPOSITION = CONDITIONAL
```

**CLASS DERIVATION CONTRACT** (committed before execution):

```
FAIL gate        -->  BLOCKED
CONDITIONAL gate -->  CONDITIONAL
PASS + HIGH      -->  CONDITIONAL
PASS + LOW       -->  ADVISORY
```

**NULL HYPOTHESIS DERIVATION RULE** (four-alternative; all three pairwise differentials
involving artifact B must be evaluated -- committed before execution):

```
Dimension scoring (1-5 per alternative):
  D1 -- Switching cost       (1 = prohibitive to adopt artifact, 5 = negligible)
  D2 -- Coverage             (1 = artifact covers far less than status quo, 5 = complete)
  D3 -- Adoption friction    (1 = high friction, 5 = frictionless)
  D4 -- Time-to-value        (1 = months before value, 5 = immediate)

Four alternatives scored per dimension:
  A = Status Quo (what teams do today)
  B = This Artifact (under review)
  C = Named Substitute (most credible incremental improvement; name it)
  D = Hybrid (a hybrid of Build + Named Substitute; name the specific hybrid approach)

Differential 1 (primary):   dBA = B_total - A_total  (artifact vs doing nothing)
Differential 2 (secondary): dBC = B_total - C_total  (artifact vs increment)
Differential 3 (tertiary):  dBD = B_total - D_total  (artifact vs hybrid)

Opening Verdict derivation (all three differentials evaluated):
  dBA >= +4 AND dBC >= 0 AND dBD >= 0  -->  PASS        (artifact wins on all three)
  dBA >= +1 AND (dBC < 0 OR dBD < 0)  -->  CONDITIONAL (beats SQ; loses to one alternative)
  dBA >= +4 AND (dBC < -3 OR dBD < -3) -->  CONDITIONAL (strong vs SQ; weak vs alternatives)
  dBA <= 0                             -->  FAIL         (does not beat status quo)
  (any ambiguous combination)          -->  CONDITIONAL
```

**LOCAL GATE LEDGER PROTOCOL** (fourth pre-committed contract):

```
Syntax:   one-row table: | Gate Verdict | Class | Source | Action |
Timing:   emitted at the END of each reviewer section, after gate verdict
Coverage: MANDATORY for ALL sections -- §1.5, §3 (each domain reviewer), §4 (lifecycle), §5
Assembly: §6 copies all rows from §1.5, §3, §4, §5 verbatim. No re-derivation.
```

**Severity Semantics:**

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

---

**§1 -- Role Selection**

Read `.roles/signal/`. No invented roles.

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "deep run"]
    (inertia-advocate: §1.5 bracket opening + §5 bracket closing)
    (lifecycle reviewer: §4 post-domain, pre-bracket-closing)
    Named Substitute (C): [name]
    Hybrid alternative (D): [name]
```

---

**§1.5 -- Bracket Opening: Challenger Pre-Domain Testimony**

```
## §1.5 -- Bracket Opening -- inertia-advocate

**Status quo statement**: [what team does today -- one sentence]
**Named Substitute (C)**: [name and one-sentence description of the strongest incremental alternative]
**Hybrid (D)**: [name and one-sentence description of a credible hybrid approach]

**Four-Alternative Table (challenger frame):**
| Dimension            | (A) Status Quo | (B) This Artifact | (C) Named Substitute | (D) Hybrid |
|----------------------|---------------|-------------------|----------------------|-----------|
| D1 Switching cost    | [1-5]         | [1-5]             | [1-5]                | [1-5]     |
| D2 Coverage          | [1-5]         | [1-5]             | [1-5]                | [1-5]     |
| D3 Adoption friction | [1-5]         | [1-5]             | [1-5]                | [1-5]     |
| D4 Time-to-value     | [1-5]         | [1-5]             | [1-5]                | [1-5]     |
| **TOTAL**            | [A sum]       | [B sum]           | [C sum]              | [D sum]   |

**Differential 1 (B - A)**: [+/- n]
**Differential 2 (B - C)**: [+/- n]
**Differential 3 (B - D)**: [+/- n]
**NULL HYPOTHESIS DERIVATION RULE applied**: [cite all three differentials; state branch]

**Challenge to domain reviewers**: [one specific question that would change any dimension
  score for B, C, or D]

**Findings**: [2-3 from challenger's lens.verify]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS
**Override authority**: YES -- FAIL at Bracket Closing overrides all domain PASS.

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Opening Verdict] | [from CLASS DERIVATION CONTRACT] | §1.5 / inertia-advocate / [5-word] | [action] |
```

---

**§3 -- Domain Reviewer Sections**

Domain reviewers re-score all four alternatives (A, B, C, D) from their technical frame.

```
## §3 -- Domain Reviewer: [role] ([archetype])

**Domain re-read of four-alternative table**
(Challenger's challenge: "[copy challenge text from §1.5]")

| Dimension            | (A) SQ | (B) Chal | (B) Rev | (C) Chal | (C) Rev | (D) Chal | (D) Rev |
|----------------------|--------|---------|---------|---------|---------|---------|---------|
| D1 Switching cost    | [A]    | [§1.5]  | [1-5]   | [§1.5]  | [1-5]   | [§1.5]  | [1-5]   |
| D2 Coverage          | [A]    | [§1.5]  | [1-5]   | [§1.5]  | [1-5]   | [§1.5]  | [1-5]   |
| D3 Adoption friction | [A]    | [§1.5]  | [1-5]   | [§1.5]  | [1-5]   | [§1.5]  | [1-5]   |
| D4 Time-to-value     | [A]    | [§1.5]  | [1-5]   | [§1.5]  | [1-5]   | [§1.5]  | [1-5]   |

**Null hypothesis address**: [does this domain expertise support artifact beating ALL three
  alternatives? One sentence citing which differentials this role can evaluate.]

**Findings**: [2-4 from this role's lens.verify and expertise.depth]
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

Lifecycle reviewer runs AFTER all §3 domain sections and BEFORE §5 bracket closing.

```
## §4 -- Lifecycle Reviewer: [role] ([archetype])

**Commitment-readiness assessment**: [Is the four-alternative evidence sufficient to support
  a commitment decision? Does the hybrid option (D) deserve further investigation before
  committing to the build? One paragraph.]
**Findings**: [2-3: commitment readiness, hybrid viability, program concerns]
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

**§5 -- Bracket Closing: Post-Domain-and-Lifecycle Reassessment**

After all §3 and §4 sections. Inertia-advocate reassesses using four-alternative revised scores
AND g_lifecycle. Must cite all three revised differentials.

```
## §5 -- Bracket Closing -- inertia-advocate (post-domain-and-lifecycle)

**Lifecycle verdict received**: g_lifecycle = [value from §4]; interpretation: [one sentence]

**Domain re-read aggregation:**
| Reviewer | D1B | D2B | D3B | D4B | D1C | D2C | D3C | D4C | D1D | D2D | D3D | D4D | Ch? |
|----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| [role]   | ... |

**Revised Four-Alternative Table:**
| Dimension            | (A) SQ | (B) Open | (B) DomAvg | (B) Final | (C) Open | (C) DomAvg | (C) Final | (D) Open | (D) DomAvg | (D) Final |
|----------------------|--------|---------|------------|-----------|---------|------------|-----------|---------|------------|-----------|
| D1 Switching cost    | [A]    | [§1.5]  | [avg]      | [final]   | [§1.5]  | [avg]      | [final]   | [§1.5]  | [avg]      | [final]   |
| D2 Coverage          | [A]    | [§1.5]  | [avg]      | [final]   | [§1.5]  | [avg]      | [final]   | [§1.5]  | [avg]      | [final]   |
| D3 Adoption friction | [A]    | [§1.5]  | [avg]      | [final]   | [§1.5]  | [avg]      | [final]   | [§1.5]  | [avg]      | [final]   |
| D4 Time-to-value     | [A]    | [§1.5]  | [avg]      | [final]   | [§1.5]  | [avg]      | [final]   | [§1.5]  | [avg]      | [final]   |
| **TOTAL**            | [A]    |         |            | [B]       |         |            | [C]       |         |            | [D]       |

**Revised differential 1 (B - A)**: [+/- n]
**Revised differential 2 (B - C)**: [+/- n]
**Revised differential 3 (B - D)**: [+/- n]
**NULL HYPOTHESIS DERIVATION RULE re-applied**: [cite all three revised differentials and
  g_lifecycle; state which branch; state if verdict changes from §1.5]

**Closing Verdict**: FAIL | CONDITIONAL | PASS
**Override invoked**: YES | NO

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Closing Verdict] | [from CLASS DERIVATION CONTRACT] | §5 / inertia-advocate / [5-word] | [action] |
```

---

**§6 -- Master Action Register**

```
## §6 -- Master Action Register
(Verbatim copy from §1.5, §3, §4, §5 -- no re-derivation)

| # | Gate Verdict | Class | Source | Action |
|---|--------------|-------|--------|--------|
```

---

**§7 -- Integrating Summary and Disposition**

```
## §7 -- Synthesis

[5-8 sentences: name highest severity; name conflicts; name convergences; reference
Opening Verdict with all three differentials; reference g_lifecycle; reference Override;
state DISPOSITION CONTRACT branch]

FORMULA APPLIED: [branch]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## V-04 -- Combination: V-01 Architecture + Enhanced Dimension Semantics + Aggregation Formula

**Variation axes**: V-01 base (lifecycle §4 before bracket §5, three-alternative table,
C-22+C-23) combined with: (a) per-dimension scoring guides pre-committed in preamble so each
score has a defined anchor, not just a label; (b) explicit domain-aggregate formula committed
in preamble (median rule) so bracket closing computation is not editorial; (c) full fourth
contract expanded to include the aggregation rule.

**Hypothesis**: V-01 pre-commits the NULL HYPOTHESIS DERIVATION RULE as a formula on B/C
totals, but the "accepted" score for bracket closing (which aggregates domain revisions) is not
pre-committed -- the bracket closing decides editorially how to aggregate. Adding an explicit
aggregation formula (median of domain revised scores per dimension) to the LOCAL GATE LEDGER
PROTOCOL pre-commits the last editorial step, making the full chain from dimension scoring to
final disposition derivable without narrative. This should score 165/165 and may reveal a
new aspiration criterion for Round 8: pre-commitment of the domain aggregation formula.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
```

Emit this block first.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

Read all four pre-committed contracts plus the aggregation formula before any reviewer
section executes. These are locked -- they do not change during execution.

**DISPOSITION CONTRACT** (committed before execution):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL              -->  DISPOSITION = BLOCKED
  elif Override invoked = YES  (see §5)     -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL       -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS             -->  DISPOSITION = READY
  else                                      -->  DISPOSITION = CONDITIONAL
```

Gates: §1.5 (opening), §3 (domain, each reviewer), §4 (lifecycle), §5 (closing).

**CLASS DERIVATION CONTRACT** (committed before execution):

```
FAIL gate        -->  BLOCKED
CONDITIONAL gate -->  CONDITIONAL
PASS + HIGH      -->  CONDITIONAL
PASS + LOW       -->  ADVISORY
```

**NULL HYPOTHESIS DERIVATION RULE** (committed before execution; three-alternative; both
differentials required):

```
Dimension scoring anchors (1-5 per alternative):
  D1 -- Switching cost
    1 = requires full platform migration to adopt artifact
    3 = moderate integration work; reversible within a quarter
    5 = drop-in replacement; no migration required
  D2 -- Coverage
    1 = artifact addresses < 25% of status quo use cases
    3 = artifact addresses 50-75% of status quo use cases
    5 = artifact addresses >= 90% of status quo use cases
  D3 -- Adoption friction
    1 = requires team training, toolchain change, and new review process
    3 = requires toolchain change or new review process, but not both
    5 = teams adopt without training or process change
  D4 -- Time-to-value
    1 = > 6 months before teams see measurable value
    3 = 1-3 months before teams see measurable value
    5 = measurable value within 2 weeks of adoption

Three alternatives:
  A = Status Quo  |  B = This Artifact  |  C = Named Substitute (named at §1.5)

Primary differential   = B_total - A_total
Secondary differential = B_total - C_total

Opening Verdict:
  primary >= +4 AND secondary >= 0  -->  PASS
  primary >= +1 AND secondary < 0   -->  CONDITIONAL
  primary >= +4 AND secondary < -3  -->  CONDITIONAL
  primary <= 0                      -->  FAIL
  (ambiguous)                       -->  CONDITIONAL
```

**LOCAL GATE LEDGER PROTOCOL + AGGREGATION RULE** (fourth pre-committed contract):

```
Gate Ledger Syntax:  | Gate Verdict | Class | Source | Action |
Gate Ledger Timing:  emitted at END of each reviewer section, after gate verdict
Gate Ledger Coverage: MANDATORY for ALL sections -- §1.5, §3 (each), §4, §5; none exempt
Gate Ledger Assembly: §6 copies all rows from §1.5, §3, §4, §5 verbatim. No re-derivation.

DOMAIN-AGGREGATE FORMULA (used in §5 bracket closing -- committed here; not decided at §5):
  For each dimension d, for each alternative x in {B, C}:
    domain_avg(d, x) = median of all §3 domain-revised scores for dimension d, alternative x
    If a domain reviewer marks a dimension "unchanged", their §1.5 score is included in median.
    accepted(d, x) = domain_avg(d, x)  (challenger cannot override without explicit justification)
  Bracket closing computes accepted totals using this formula. If challenger disputes a score,
  the dispute is noted but the formula-derived value is the accepted score unless Override = YES.
```

**Severity Semantics:**

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

---

**§1 -- Role Selection**

Read `.roles/signal/`. No invented roles.

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "deep run"]
    (inertia-advocate: §1.5 + §5)
    (lifecycle reviewer: §4 post-domain, pre-bracket-closing)
    Named Substitute (C): [name the most credible non-build alternative]
```

---

**§1.5 -- Bracket Opening: Challenger Pre-Domain Testimony**

```
## §1.5 -- Bracket Opening -- inertia-advocate

**Status quo statement**: [what teams do today -- one sentence]
**Named Substitute (C)**: [name; one sentence: why this is the strongest alternative to build]

**Three-Alternative Table (challenger frame; use scoring anchors from NULL HYPOTHESIS
  DERIVATION RULE for all scores):**
| Dimension            | (A) Status Quo | (B) This Artifact | (C) Named Substitute |
|----------------------|---------------|-------------------|----------------------|
| D1 Switching cost    | [1-5]         | [1-5]             | [1-5]                |
| D2 Coverage          | [1-5]         | [1-5]             | [1-5]                |
| D3 Adoption friction | [1-5]         | [1-5]             | [1-5]                |
| D4 Time-to-value     | [1-5]         | [1-5]             | [1-5]                |
| **TOTAL**            | [A sum]       | [B sum]           | [C sum]              |

**Primary differential (B - A)**: [+/- n]
**Secondary differential (B - C)**: [+/- n]
**NULL HYPOTHESIS DERIVATION RULE applied**: [cite both differentials; state branch]

**Challenge to domain reviewers**: [one specific question; a correct answer would require
  revising a specific dimension score for B or C]

**Findings**: [2-3 from challenger's lens.verify]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS
**Override authority**: YES -- FAIL at Bracket Closing overrides domain PASS.

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Opening Verdict] | [from CLASS DERIVATION CONTRACT] | §1.5 / inertia-advocate / [5-word] | [action] |
```

---

**§3 -- Domain Reviewer Sections**

For each domain reviewer, re-score B and C using dimension anchors from the NULL HYPOTHESIS
DERIVATION RULE preamble. Reference the scoring anchor when justifying a revised score.

```
## §3 -- Domain Reviewer: [role] ([archetype])

**Domain re-read (challenge: "[copy from §1.5]")**

| Dimension            | (A) SQ | (B) §1.5 | (B) Revised | (B) Anchor justification | (C) §1.5 | (C) Revised | (C) Anchor justification |
|----------------------|--------|---------|-------------|--------------------------|---------|-------------|--------------------------|
| D1 Switching cost    | [A]    | [§1.5]  | [1-5]       | [cite anchor level]      | [§1.5]  | [1-5]       | [cite anchor level]      |
| D2 Coverage          | [A]    | [§1.5]  | [1-5]       | [cite anchor level]      | [§1.5]  | [1-5]       | [cite anchor level]      |
| D3 Adoption friction | [A]    | [§1.5]  | [1-5]       | [cite anchor level]      | [§1.5]  | [1-5]       | [cite anchor level]      |
| D4 Time-to-value     | [A]    | [§1.5]  | [1-5]       | [cite anchor level]      | [§1.5]  | [1-5]       | [cite anchor level]      |

**Null hypothesis address**: [does this domain expertise support defeating both differentials?
  Reference the anchor-justified scores, not just assertions.]

**Findings**: [2-4 from this role's lens.verify and expertise.depth]
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

```
## §4 -- Lifecycle Reviewer: [role] ([archetype])

**Commitment-readiness assessment**: [Is anchor-justified three-alternative evidence sufficient
  for a commitment decision? One paragraph. Reference adoption plan and migration cost against
  D1-D3 anchor levels specifically.]
**Findings**: [2-3: commitment readiness, decision completeness, program concerns]
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

**§5 -- Bracket Closing: Post-Domain-and-Lifecycle Reassessment**

```
## §5 -- Bracket Closing -- inertia-advocate

**Lifecycle verdict received**: g_lifecycle = [value from §4 Local Gate Ledger];
  interpretation: [one sentence on lifecycle implication for null hypothesis]

**DOMAIN-AGGREGATE FORMULA applied (from preamble -- not editorial):**
For each dimension d, for each alternative x in {B, C}:
  domain_avg(d, x) = median of §3 revised scores for (d, x)

| Dimension            | (A) SQ | §3 B scores | B median | B accepted | §3 C scores | C median | C accepted |
|----------------------|--------|------------|----------|-----------|------------|----------|-----------|
| D1 Switching cost    | [A]    | [list]     | [median] | [median]  | [list]     | [median] | [median]  |
| D2 Coverage          | [A]    | [list]     | [median] | [median]  | [list]     | [median] | [median]  |
| D3 Adoption friction | [A]    | [list]     | [median] | [median]  | [list]     | [median] | [median]  |
| D4 Time-to-value     | [A]    | [list]     | [median] | [median]  | [list]     | [median] | [median]  |
| **TOTAL**            | [A]    |            |          | [B acc]   |            |          | [C acc]   |

**Revised primary differential (B - A)**: [B accepted total] - [A] = [+/- n]
**Revised secondary differential (B - C)**: [B accepted total] - [C accepted total] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE re-applied**: [cite both revised differentials and
  g_lifecycle; state which branch; note if verdict changes from §1.5]

**Closing Verdict**: FAIL | CONDITIONAL | PASS
**Override invoked**: YES | NO

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Closing Verdict] | [from CLASS DERIVATION CONTRACT] | §5 / inertia-advocate / [5-word] | [action] |
```

---

**§6 -- Master Action Register**

```
## §6 -- Master Action Register
(Verbatim copy from §1.5, §3, §4, §5 -- no re-derivation)

| # | Gate Verdict | Class | Source | Action |
|---|--------------|-------|--------|--------|
```

---

**§7 -- Integrating Summary and Disposition**

```
## §7 -- Synthesis

[5-8 sentences: highest severity; conflicts; convergences; Opening Verdict with both
differentials; g_lifecycle; Override; DISPOSITION CONTRACT branch]

FORMULA APPLIED: [branch]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## V-05 -- Combination: V-01 Architecture + Domain-Aggregate Checkpoint Before Lifecycle

**Variation axes**: V-01 base (lifecycle §4 before bracket §5, three-alternative table)
combined with an explicit domain-synthesis checkpoint (§3.5) that pre-aggregates domain
dimension scores BEFORE the lifecycle reviewer and bracket closing receive them. The checkpoint
is not a new gate -- it emits no verdict. It is a structural aggregate: it computes the domain
median scores per dimension per alternative and publishes them as a labeled table that §4 and
§5 read verbatim. This removes the inline aggregation computation from §5 bracket closing
(where it could become editorial) and externalizes it into a committed checkpoint step.

**Hypothesis**: V-04 pre-commits the aggregation formula but the computation still happens
inside §5 bracket closing where the inertia-advocate might editorially adjust medians. Moving
the median computation to a neutral §3.5 checkpoint (which runs with no adversarial frame)
separates fact (what domain reviewers actually said) from interpretation (how the challenger
reads it). The lifecycle reviewer (§4) and bracket closing (§5) receive a clean aggregate
input. If this structural change does not affect C-22 or C-23 compliance, it validates that
domain-aggregate externalization is architecturally neutral at 165/165 -- and surfaces a
potential new aspiration criterion for Round 8: pre-aggregate checkpoint as an auditability
contract.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
```

Emit this block first.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

Read all four pre-committed contracts before any reviewer section executes.

**DISPOSITION CONTRACT** (committed before execution):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL              -->  DISPOSITION = BLOCKED
  elif Override invoked = YES  (see §5)     -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL       -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS             -->  DISPOSITION = READY
  else                                      -->  DISPOSITION = CONDITIONAL
```

Gates: §1.5, §3 (each domain reviewer), §4, §5.

Note: §3.5 (domain-aggregate checkpoint) produces NO gate verdict. It is a computation
artifact only. It does not emit a Local Gate Ledger row. It is not included in the
DISPOSITION CONTRACT formula.

**CLASS DERIVATION CONTRACT** (committed before execution):

```
FAIL gate        -->  BLOCKED
CONDITIONAL gate -->  CONDITIONAL
PASS + HIGH      -->  CONDITIONAL
PASS + LOW       -->  ADVISORY
```

**NULL HYPOTHESIS DERIVATION RULE** (three-alternative; both differentials; committed
before execution):

```
Dimensions (1-5 per alternative):
  D1 -- Switching cost       (1 = prohibitive, 5 = negligible)
  D2 -- Coverage             (1 = incomplete, 5 = complete)
  D3 -- Adoption friction    (1 = high friction, 5 = frictionless)
  D4 -- Time-to-value        (1 = long lag, 5 = immediate)

A = Status Quo | B = This Artifact | C = Named Substitute

Primary differential   = B_total - A_total
Secondary differential = B_total - C_total

Opening Verdict:
  primary >= +4 AND secondary >= 0  -->  PASS
  primary >= +1 AND secondary < 0   -->  CONDITIONAL
  primary >= +4 AND secondary < -3  -->  CONDITIONAL
  primary <= 0                      -->  FAIL
  (ambiguous)                       -->  CONDITIONAL
```

**LOCAL GATE LEDGER PROTOCOL** (fourth pre-committed contract):

```
Syntax:    | Gate Verdict | Class | Source | Action |
Timing:    emitted at END of each GATE-emitting section (§1.5, §3 each, §4, §5)
Coverage:  MANDATORY for §1.5, §3 (each domain reviewer), §4, §5
           EXCLUDED: §3.5 (domain-aggregate checkpoint) emits NO ledger row
Assembly:  §6 copies rows from §1.5, §3, §4, §5 verbatim. No re-derivation.

DOMAIN-AGGREGATE CHECKPOINT RULE (applies to §3.5 only):
  For each dimension d, for each alternative x in {B, C}:
    domain_aggregate(d, x) = median of all §3 revised scores for (d, x)
    (unchanged dimensions use §1.5 score in median)
  §3.5 publishes the aggregate table and nothing else. §4 and §5 read from §3.5 verbatim.
  §5 bracket closing does not recompute aggregates; it reads §3.5 output directly.
```

**Severity Semantics:**

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

---

**§1 -- Role Selection**

Read `.roles/signal/`. No invented roles.

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale]
    (inertia-advocate: §1.5 + §5)
    (lifecycle reviewer: §4 post-aggregate-checkpoint, pre-bracket-closing)
    Named Substitute (C): [name]
```

---

**§1.5 -- Bracket Opening: Challenger Pre-Domain Testimony**

```
## §1.5 -- Bracket Opening -- inertia-advocate

**Status quo statement**: [one sentence]
**Named Substitute (C)**: [name; one sentence]

**Three-Alternative Table (challenger frame):**
| Dimension            | (A) Status Quo | (B) This Artifact | (C) Named Substitute |
|----------------------|---------------|-------------------|----------------------|
| D1 Switching cost    | [1-5]         | [1-5]             | [1-5]                |
| D2 Coverage          | [1-5]         | [1-5]             | [1-5]                |
| D3 Adoption friction | [1-5]         | [1-5]             | [1-5]                |
| D4 Time-to-value     | [1-5]         | [1-5]             | [1-5]                |
| **TOTAL**            | [A sum]       | [B sum]           | [C sum]              |

**Primary differential (B - A)**: [+/- n]
**Secondary differential (B - C)**: [+/- n]
**NULL HYPOTHESIS DERIVATION RULE applied**: [cite both differentials; state branch]

**Challenge to domain reviewers**: [one testable question]

**Findings**: [2-3 from lens.verify]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one]
**Opening Verdict**: FAIL | CONDITIONAL | PASS
**Override authority**: YES -- FAIL at Bracket Closing overrides domain PASS.

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Opening Verdict] | [from CLASS DERIVATION CONTRACT] | §1.5 / inertia-advocate / [5-word] | [action] |
```

---

**§3 -- Domain Reviewer Sections**

```
## §3 -- Domain Reviewer: [role] ([archetype])

**Challenge: "[copy from §1.5]"**

| Dimension            | (A) SQ | (B) §1.5 | (B) Revised | (C) §1.5 | (C) Revised |
|----------------------|--------|---------|-------------|---------|-------------|
| D1 Switching cost    | [A]    | [§1.5]  | [1-5]       | [§1.5]  | [1-5]       |
| D2 Coverage          | [A]    | [§1.5]  | [1-5]       | [§1.5]  | [1-5]       |
| D3 Adoption friction | [A]    | [§1.5]  | [1-5]       | [§1.5]  | [1-5]       |
| D4 Time-to-value     | [A]    | [§1.5]  | [1-5]       | [§1.5]  | [1-5]       |

**Null hypothesis address**: [does this domain expertise support defeating both differentials?]

**Findings**: [2-4]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one]
**Simplify**: [one]
**Gate Verdict**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict | Class | Source | Action |
|-------------|-------|--------|--------|
| [verdict] | [from CLASS DERIVATION CONTRACT] | §3 / [role] / [5-word] | [action] |
```

---

**§3.5 -- Domain-Aggregate Checkpoint (No Gate Verdict)**

This section runs after ALL §3 domain sections. It computes the domain-aggregate table
using the DOMAIN-AGGREGATE CHECKPOINT RULE from the LOCAL GATE LEDGER PROTOCOL preamble.
It emits no gate verdict and no Local Gate Ledger row.

§4 (lifecycle reviewer) and §5 (bracket closing) read from this checkpoint verbatim.
They do not re-read §3 scores; they consume §3.5 output only.

```
## §3.5 -- Domain-Aggregate Checkpoint (informational only -- no gate verdict)

**Domain median scores (computed per DOMAIN-AGGREGATE CHECKPOINT RULE):**
| Dimension            | (A) SQ | §3 B scores | B median | §3 C scores | C median |
|----------------------|--------|------------|----------|------------|----------|
| D1 Switching cost    | [A]    | [list all] | [median] | [list all] | [median] |
| D2 Coverage          | [A]    | [list all] | [median] | [list all] | [median] |
| D3 Adoption friction | [A]    | [list all] | [median] | [list all] | [median] |
| D4 Time-to-value     | [A]    | [list all] | [median] | [list all] | [median] |
| **TOTAL**            | [A]    |            | [B agg]  |            | [C agg]  |

**Aggregate primary differential (B_agg - A)**: [+/- n]
**Aggregate secondary differential (B_agg - C_agg)**: [+/- n]

(§4 and §5 read from this table. No commentary. No verdict.)
```

---

**§4 -- Lifecycle Reviewer (Post-Aggregate-Checkpoint, Pre-Bracket-Closing)**

Lifecycle reviewer has access to the artifact and the §3.5 aggregate table.
Does not have access to §1.5 or individual §3 reviewer sections.

```
## §4 -- Lifecycle Reviewer: [role] ([archetype])

**§3.5 aggregate received**: B_total = [§3.5 B agg], C_total = [§3.5 C agg]
  (lifecycle reviewer acknowledges receipt of domain-aggregate checkpoint)

**Commitment-readiness assessment**: [Is the domain-aggregate evidence sufficient for a
  commitment decision? One paragraph. Reference aggregate differentials from §3.5.]
**Findings**: [2-3: commitment readiness, decision completeness, program concerns]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one]
**Simplify**: [one]
**Gate Verdict (g_lifecycle)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict   | Class | Source | Action |
|----------------|-------|--------|--------|
| [g_lifecycle]  | [from CLASS DERIVATION CONTRACT] | §4 / [lifecycle role] / [5-word] | [action] |
```

---

**§5 -- Bracket Closing: Post-Aggregate-and-Lifecycle Reassessment**

Bracket closing reads §3.5 aggregate table (not individual §3 scores) and g_lifecycle from §4.

```
## §5 -- Bracket Closing -- inertia-advocate

**Lifecycle verdict received**: g_lifecycle = [value from §4 Local Gate Ledger];
  interpretation: [one sentence on lifecycle signal for null hypothesis]

**§3.5 aggregate received (verbatim copy):**
| Dimension            | (A) SQ | B median | C median |
|----------------------|--------|----------|----------|
| D1 Switching cost    | [A]    | [§3.5]   | [§3.5]   |
| D2 Coverage          | [A]    | [§3.5]   | [§3.5]   |
| D3 Adoption friction | [A]    | [§3.5]   | [§3.5]   |
| D4 Time-to-value     | [A]    | [§3.5]   | [§3.5]   |
| **TOTAL**            | [A]    | [§3.5 B] | [§3.5 C] |

**Revised primary differential (B - A)**: [§3.5 B_agg] - [A] = [+/- n]
**Revised secondary differential (B - C)**: [§3.5 B_agg] - [§3.5 C_agg] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE re-applied**: [cite both revised differentials and g_lifecycle;
  state branch; note if verdict changes from §1.5 opening verdict]

**Closing Verdict**: FAIL | CONDITIONAL | PASS
**Override invoked**: YES | NO
  If YES: basis for override (challenger disputes aggregate score -- cite dimension and reason).
  If NO: aggregate scores accepted; Closing Verdict feeds DISPOSITION CONTRACT normally.

**Local Gate Ledger:**
| Gate Verdict      | Class | Source | Action |
|-------------------|-------|--------|--------|
| [Closing Verdict] | [from CLASS DERIVATION CONTRACT] | §5 / inertia-advocate / [5-word] | [action] |
```

---

**§6 -- Master Action Register**

```
## §6 -- Master Action Register
(Verbatim copy from §1.5, §3, §4, §5 -- §3.5 excluded; no re-derivation)

| # | Gate Verdict | Class | Source | Action |
|---|--------------|-------|--------|--------|
```

---

**§7 -- Integrating Summary and Disposition**

```
## §7 -- Synthesis

[5-8 sentences: highest severity; conflicts; convergences; Opening Verdict (§1.5) with both
differentials; §3.5 aggregate differentials; g_lifecycle (§4); Closing Verdict (§5) and
Override invoked; DISPOSITION CONTRACT branch applied]

FORMULA APPLIED: [branch]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## Round 7 Scoring Predictions (v6 rubric, 165 pts max)

### Expected scores

| Variant | C-22 | C-23 | v6 predicted | Notes |
|---------|------|------|-------------|-------|
| V-01 | PASS | PASS | **165** | Lifecycle §4 before §5; three-alternative table; both differentials |
| V-02 | PASS | PASS | **165** | Register invariant; formal attestation; same architecture |
| V-03 | PASS | PASS | **165** | Four-alternative table; three differentials; lifecycle §4 before §5 |
| V-04 | PASS | PASS | **165** | V-01 + dimension anchors + pre-committed aggregation formula |
| V-05 | PASS | PASS | **165** | V-01 + domain-aggregate checkpoint (§3.5) externalized |

### Key structural properties per variant

| Property | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| Lifecycle §4 before bracket §5 | YES | YES | YES | YES | YES |
| Three-alternative table | YES | YES | NO | YES | YES |
| Four-alternative table | NO | NO | YES | NO | NO |
| Both B-A and B-C differentials pre-committed | YES | YES | YES (3) | YES | YES |
| Domain aggregation formula pre-committed | NO | NO | NO | YES | YES |
| Aggregation checkpoint (§3.5) | NO | NO | NO | NO | YES |
| Formal attestation register | NO | YES | NO | NO | NO |

### What Round 7 is testing

V-01: Can the two R6 160-pt architectures (V-04 + V-03/V-05) combine cleanly to 165?
V-02: Is the formal attestation register architecturally neutral on the combined path?
V-03: Does C-23 generalize to four-alternative tables with three pairwise differentials?
V-04: Does pre-committing the aggregation formula (in addition to the derivation rule) add a
  new aspiration criterion candidate? Does it affect C-22/C-23 compliance?
V-05: Does externalizing aggregation to a neutral checkpoint (§3.5) improve auditability
  without disrupting the lifecycle-before-bracket-closing sequencing?

### Potential R8 criterion candidates (to be extracted from R7 results)

- C-24 (tentative): Domain-Aggregate Formula Pre-committed Before Bracket Closing
  Source: V-04 -- explicitly commits the median rule in preamble vs V-01 which derives
  aggregation editorially within §5.
- C-25 (tentative): Domain-Aggregate Checkpoint as Structural Artifact
  Source: V-05 -- §3.5 checkpoint separates computation from interpretation; lifecycle and
  bracket closing read from checkpoint verbatim rather than re-computing inline.
- Neither promoted until R7 execution confirms these as genuine structural differences
  with evaluable pass/fail conditions.
