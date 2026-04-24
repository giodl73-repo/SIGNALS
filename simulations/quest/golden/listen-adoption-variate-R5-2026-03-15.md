# Variations: listen-adoption — Round 5

**Rubric:** v5 | **Criteria:** C-01 through C-18 | **Max composite:** 100 | **Golden threshold:** all 5 essential pass + composite >= 80

---

## Variation Axes

| Axis | R5 Target | Description |
|------|-----------|-------------|
| Output format | C-17 | The downstream citation contract in the PREAMBLE is restructured as a CITATION CONTRACT TABLE with columns: Section \| Required citation form \| Directive \| Met? A CONTRACT COMPLIANCE AUDIT at the end fills the Met? column, converting the pipe list into a forward-declared, post-verified accountability grid. |
| Inertia framing | C-18 | The DEPENDENCY GRAVITY ASSESSMENT adds a "Derived month range" column giving the gravity-anchored prediction before SECTION 1 is filled. SCHEDULE RECONCILIATION gains a typed gravity citation column requiring the specific format `G[N]: [exact incumbent behavior this role's gravity score captured]` — generic "delayed due to dependency" becomes structurally unacceptable. |
| Lifecycle emphasis | C-18 (chasm propagation) | PHASE 3 opens with a GRAVITY CLUSTER IDENTIFICATION step that names all gravity-4+ roles and declares them the chasm anchor cluster. The chasm table is then built from this cluster: gap, cause, and bridge condition all reference the cluster by score. PHASE 4 entry is gated on bridge addressing at least one gravity-4+ role. |

**Single-axis (V-01, V-02, V-03):** Output format · Inertia framing · Lifecycle emphasis
**Combined (V-04):** Output format + Inertia framing
**Full (V-05):** Output format + Inertia framing + Lifecycle emphasis

---

## Baseline (all five carry from R4 V-05)

| Element | Criterion | Form |
|---------|-----------|------|
| Narrative analyst framing | — | "You are the adoption analyst for {{topic}}..." second-person throughout |
| PREAMBLE — Incumbent Declaration | C-11 | Named incumbent + downstream citation contract (pipe list in R4; upgraded to table in V-01+) |
| DEPENDENCY GRAVITY ASSESSMENT | C-18 | 16-role table with gravity score (1–5) + basis; gravity-to-month anchor |
| SECTION 1 — Archetype Mapping + Committed Adoption Schedule | C-01, C-16 | 16-row table; column labeled "Committed adoption month"; gravity score + note in dependency column |
| SECTION 2 — 5-phase simulation with month blocks | C-02, C-03 | Phase opens by re-citing preceding CLOSE; each month block opens with "Roles committed to M[N]:"; row-numbered tables |
| CHAMPION FORMATION EVENT blocks in PHASE 2 and PHASE 4 | C-14 | Formation month / Role / Bridging mechanism / Incumbent argument targeted |
| Phase closes with "Scheduled roles met:" | C-16 | Confirms committed roles appeared or explains delay — cites gravity where applicable |
| PHASE COMPLIANCE LEDGER after each phase close | — | Per-phase structural gate; FAIL requires upstream correction before next phase |
| SCHEDULE RECONCILIATION in PHASE 5 CLOSE | C-16, C-18 | Role \| Gravity \| Committed month \| Actual month \| Status; deviation reasons cite gravity and incumbent |
| TRACEABILITY AUDIT | C-15 | 16-row table; Row Citation `[PHASE N / Month M / Row K]`; generic citations fail |
| THREE-AXIS GAP AUDIT (Axis A/B/C) | C-13 | Role completeness + temporal completeness + causal specificity; Axis C cites THE INCUMBENT |
| SECTION 3 — Champion Network | C-06, C-09, C-12, C-14 | Derivation rule; "Incumbent argument countered" column; formation phase/month citation |
| SECTION 4 — Interventions ranked by adoption delta | C-04, C-10 | "Displaces from incumbent" + "Adoption delta" + "Deploy before month" columns |
| SECTION 5 — Churn Risk Register | C-05 | "Incumbent pull" column cites THE INCUMBENT by name |
| SECTION 6 — S-Curve Summary | C-07, C-08 | Phase counts + % + Incumbent position |

---

## V-01 — Single Axis: Output Format (Citation Contract Table)

**Variation axis:** Output format — The PREAMBLE's downstream citation contract is restructured
from a pipe-separated list into a CITATION CONTRACT TABLE with four columns: Section name,
Required citation form (what specifically must be cited, and where), Directive (one of: MUST /
REQUIRED / OBLIGATED), and Met? (to be filled by the model in a CONTRACT COMPLIANCE AUDIT after
SECTION 6 closes). The table enumerates at least 5 named downstream sections. A CONTRACT
COMPLIANCE AUDIT block appears at the very end of the artifact; for each row, the model writes
PASS or FAIL and cites the specific cell or field that satisfies or violates the obligation.
All other structural elements carry from R4 V-05 unchanged.

**Hypothesis:** R4 V-01 introduced a downstream citation contract as a pipe list:
`PHASE 3 chasm cause | SECTION 3 champion ... | SECTION 4 ... | SECTION 5 ... | ...`
This satisfies the naming requirement but is only checkable post-hoc by a scorer, not by the
model mid-generation. C-17 requires forward-declared directive language ("must," "required,"
"contract") with at least 4 named sections — the pipe list technically passes this, but without
a structured compliance close, the model can emit the list and then fail to honor it in body
sections without triggering a visible inconsistency. The CONTRACT COMPLIANCE AUDIT row for each
section creates a post-simulation check that forces the model to trace whether it honored each
obligation it declared. If SECTION 3's row returns FAIL, the model must correct. The table
format also makes C-17's "at least 4 named sections with directive language" mechanically
verifiable at setup time, not inferred from prose.

---

You are the adoption analyst for **{{topic}}**. Your simulation follows a structured protocol
with required output blocks. All blocks must be completed in full before advancing. Phase
Compliance Ledgers (PCL) are structural gates — correct any FAIL before writing the next phase.
Reason as the analyst throughout: where the protocol asks for a cause, give the actual cause;
where it asks for a mechanism, describe the mechanism that will actually work for this team.

Produce the artifact below in the order shown.

---

### PREAMBLE — Incumbent Declaration and Citation Contract

Your first task is to name THE INCUMBENT precisely, then declare the citation contract that
binds every downstream section before the simulation runs.

```
THE INCUMBENT:
  [Specific workflow, tool, or habit {{topic}} displaces. Name it precisely — not
   "current process" but the actual named thing.]

What THE INCUMBENT does well for this team:
  - [Advantage 1: which cohorts rely on this and why]
  - [Advantage 2: what {{topic}} does not yet match]

What {{topic}} must prove to displace it:
  - For early majority: [specific proof point]
  - For late majority:  [specific proof point]
```

**CITATION CONTRACT**

The following sections are OBLIGATED to cite THE INCUMBENT by name as specified. This contract
is forward-declared and will be audited in CONTRACT COMPLIANCE AUDIT after SECTION 6.

| Section | Required citation form | Directive | Met? |
|---------|----------------------|-----------|------|
| PHASE 3 — chasm cause | "Cause" row must name THE INCUMBENT by name as the specific advantage blocking EM crossing | MUST | [fill in CONTRACT COMPLIANCE AUDIT] |
| SECTION 3 — champion network | "Incumbent argument countered" column must cite THE INCUMBENT by name for every champion row | MUST | [fill in CONTRACT COMPLIANCE AUDIT] |
| SECTION 4 — interventions | "Displaces from incumbent" column must cite THE INCUMBENT by name for every intervention row | REQUIRED | [fill in CONTRACT COMPLIANCE AUDIT] |
| SECTION 5 — churn risks | "Incumbent pull" column must cite THE INCUMBENT by name for every churn row | REQUIRED | [fill in CONTRACT COMPLIANCE AUDIT] |
| SCHEDULE RECONCILIATION | Deviation reasons where incumbent pull is the stall cause must name THE INCUMBENT explicitly | OBLIGATED | [fill in CONTRACT COMPLIANCE AUDIT] |
| THREE-AXIS GAP AUDIT Axis C | "THE INCUMBENT cited?" column must show "Yes" for every row naming a gap or stall caused by THE INCUMBENT | REQUIRED | [fill in CONTRACT COMPLIANCE AUDIT] |

---

**DEPENDENCY GRAVITY ASSESSMENT**

Rate each role's daily reliance on THE INCUMBENT before declaring committed months.

Gravity scale:
- 5 — Uses THE INCUMBENT daily; no viable workaround; switching requires process change
- 4 — Uses it most days; minor workarounds; switching requires convincing evidence
- 3 — Uses it regularly but not daily; moderate switching friction
- 2 — Uses it occasionally; can adopt {{topic}} without displacing workflow immediately
- 1 — Rarely or never uses THE INCUMBENT; low friction to adopt

| Role | Gravity score (1–5) | Basis: what this role uses THE INCUMBENT for |
|------|--------------------|--------------------------------------------|
| PM | | |
| UX | | |
| C-01 | | |
| C-02 | | |
| C-03 | | |
| C-04 | | |
| C-05 | | |
| C-06 | | |
| C-07 | | |
| C-08 | | |
| C-09 | | |
| C-10 | | |
| C-11 | | |
| C-12 | | |
| Support | | |
| SRE | | |

Gravity-to-committed-month anchor: gravity 1–2 → M1–M2 range; gravity 3 → M3–M4 range;
gravity 4 → M5–M6 range; gravity 5 → M7–M9 range. Deviations from these ranges must be
stated in SECTION 1 with a reason.

---

### SECTION 1 — Archetype Mapping and Committed Adoption Schedule

Before the simulation runs, commit to a schedule. These are binding predictions. Anchor
committed months to gravity scores from the DEPENDENCY GRAVITY ASSESSMENT; state a reason
for any deviation from the anchor range.

| Role | Rogers Archetype | Incumbent dependency (gravity + note) | Committed adoption month |
|------|-----------------|--------------------------------------|------------------------|
| PM | | gravity [N] — [note if deviating from anchor] | M[N] |
| UX | | | M[N] |
| C-01 | | | M[N] |
| C-02 | | | M[N] |
| C-03 | | | M[N] |
| C-04 | | | M[N] |
| C-05 | | | M[N] |
| C-06 | | | M[N] |
| C-07 | | | M[N] |
| C-08 | | | M[N] |
| C-09 | | | M[N] |
| C-10 | | | M[N] |
| C-11 | | | M[N] |
| C-12 | | | M[N] |
| Support | | | M[N] |
| SRE | | | M[N] |

Archetype order must be respected: Innovators first, Laggards last. Non-adopters must state reason.

---

### SECTION 2 — Month-by-Month Simulation

The simulation runs against your committed schedule. Each month block opens by listing the
roles you committed to that month. Row addresses for TRACEABILITY AUDIT: `[PHASE N / Month M / Row K]`.

---

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 adopted. THE INCUMBENT is fully in place.

**Month 1**

Roles committed to M1: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull (why others don't yet) |
|-----|---------------------|-----------|-----------------|--------------------------------------|
| 1 | | Innovator | | [CITE: THE INCUMBENT] still holds because: [...] |

```
Cumulative: [N] of 16
```

**Month 2** (include all roles committed to M2)

Roles committed to M2: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | |

```
PHASE 1 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M1-M2 committed roles appeared or explain delay — cite gravity where applicable]
Incumbent position: [describe]
Signal to EA cohort: [what evidence now exists that {{topic}} works]
```

```
PHASE 1 COMPLIANCE LEDGER
C-01 (archetype mapping present in SECTION 1 — all 16 rows filled): [PASS / FAIL]
C-16a (Month 1 block opened with "Roles committed to M1:" prompt): [PASS / FAIL]
C-16b (Month 2 block opened with "Roles committed to M2:" prompt): [PASS / FAIL]
C-16c (PHASE 1 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]
C-11 (THE INCUMBENT cited by name in at least one Incumbent pull cell): [PASS / FAIL]

If any item is FAIL: correct the upstream phase content before writing PHASE 2.
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

Roles committed to M3: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | [CITE: THE INCUMBENT] still holds for non-adopters because: [...] |
| 2 | | | | |

```
Cumulative: [N] of 16
```

**CHAMPION FORMATION EVENT** — identify the first role emerging this phase that will bridge
early adopters toward early majority. If no champion has formed yet, explain why.

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role — must appear in a simulation row at or before this month]
  Bridging mechanism:        [how this role will accelerate spread to the next cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific advantage this champion counters]
```

**Month 4**

Roles committed to M4: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | |
| 2 | | | | |

```
PHASE 2 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M3-M4 committed roles appeared or explain — cite gravity where applicable]
Incumbent position: [still dominant with which cohorts? why?]
Champion network: [roles from CHAMPION FORMATION EVENT(s) + formation month]
Gap to EM: [what THE INCUMBENT still offers that EM cohort values — CITE: THE INCUMBENT]
```

```
PHASE 2 COMPLIANCE LEDGER
C-14 (CHAMPION FORMATION EVENT fired with all required fields, or "No champion formed — [reason]"): [PASS / FAIL]
C-16a (Month 3 block opened with "Roles committed to M3:"): [PASS / FAIL]
C-16b (Month 4 block opened with "Roles committed to M4:"): [PASS / FAIL]
C-16c (PHASE 2 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]
C-09 (CHAMPION FORMATION EVENT "Incumbent argument targeted" field present, non-generic): [PASS / FAIL / N/A]
C-11 (THE INCUMBENT cited in "Gap to EM" field): [PASS / FAIL]

If any item is FAIL: correct the upstream phase content before writing PHASE 3.
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

As analyst, identify the chasm. Name the specific advantage of THE INCUMBENT that prevents
early-majority crossing.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and [EM roles — name specifically] |
| Cause | [What specific advantage of THE INCUMBENT prevents EM crossing? [CITE: THE INCUMBENT by name] — name the habit or workflow.] |
| Gravity cluster | [Which roles have gravity 4–5? Why their dependency depth makes the chasm wider.] |
| Incumbent win condition | [CITE: THE INCUMBENT] delivers [...] that {{topic}} doesn't yet match for EM |
| Risk if not bridged | [Roles that plateau; [CITE: THE INCUMBENT] entrenches for high-gravity cohort] |
| Bridge condition | [What EM needs to see from {{topic}} to switch] |
| Champion | [Role from CHAMPION FORMATION EVENT + mechanism + THE INCUMBENT argument they counter] |

```
PHASE 3 CLOSE
Bridge condition: [what must be true for PHASE 4 entry]
Incumbent position at chasm: [still dominant / weakening / differentiated]
```

```
PHASE 3 COMPLIANCE LEDGER
C-03 (Gap element names specific EA and EM roles): [PASS / FAIL]
C-03 (Cause element names THE INCUMBENT explicitly — non-generic): [PASS / FAIL]
C-03 (Risk element states what is at risk): [PASS / FAIL]
C-11 (THE INCUMBENT named by name in Cause element — satisfies CITATION CONTRACT row 1): [PASS / FAIL]
C-12 (Champion element cites specific CHAMPION FORMATION EVENT role): [PASS / FAIL]

If any item is FAIL: correct the PHASE 3 table before writing PHASE 4.
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.

**Month 5**

Roles committed to M5: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
Cumulative: [N] of 16
Churn risk?: [role + gravity score + trigger; what [CITE: THE INCUMBENT] behavior reasserts]
```

**CHAMPION FORMATION EVENT** — if a new champion emerges this phase to bridge EM toward LM,
record it. If no new champion: "No new champion this phase."

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [mechanism toward Late Majority cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific argument]
```

**Month 6**

Roles committed to M6: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
PHASE 4 CLOSE
Adopters: [roles, count, %]
Scheduled roles met: [confirm M5-M6 committed roles appeared or explain — cite gravity where applicable]
Incumbent position: [retreating / residual / eliminated in this cohort]
```

```
PHASE 4 COMPLIANCE LEDGER
C-14 (CHAMPION FORMATION EVENT fired or "No new champion this phase"): [PASS / FAIL]
C-16a (Month 5 block opened with "Roles committed to M5:"): [PASS / FAIL]
C-16b (Month 6 block opened with "Roles committed to M6:"): [PASS / FAIL]
C-16c (PHASE 4 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 5.
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

Roles committed to M7–M9: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Late Majority / Laggard | | |
| 2 | | | | |

```
PHASE 5 CLOSE
Final adopters: [N] of 16 ([%])
Non-adopters (if any): [roles; gravity score; reason THE INCUMBENT still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

**SCHEDULE RECONCILIATION**

Reconcile committed schedule against actual outcomes. When THE INCUMBENT is the cause of a
delay, name it and cite the gravity score.

| Role | Gravity | Committed month | Actual month | Status |
|------|---------|----------------|-------------|--------|
| PM | | | | On schedule / Delayed [N months] — gravity [G]: [reason citing THE INCUMBENT if applicable] / Non-adopter |
| UX | | | | |
| C-01 | | | | |
| C-02 | | | | |
| C-03 | | | | |
| C-04 | | | | |
| C-05 | | | | |
| C-06 | | | | |
| C-07 | | | | |
| C-08 | | | | |
| C-09 | | | | |
| C-10 | | | | |
| C-11 | | | | |
| C-12 | | | | |
| Support | | | | |
| SRE | | | | |

```
SCHEDULE RECONCILIATION RESULT
On schedule: [N] of 16
Delayed: [N] — [list with gravity scores and reasons; cite THE INCUMBENT where applicable]
Non-adopters: [list with gravity scores]
Gravity accuracy check: [did high-gravity roles (4–5) cluster in later months as predicted?]
```

---

### TRACEABILITY AUDIT

Complete before the THREE-AXIS GAP AUDIT.

**Row Citation format:** `[PHASE N / Month M / Row K]`. Generic citations fail.
Non-adopters cite `[PHASE 5 CLOSE / non-adopter list]`.

| Role | Adoption month | Archetype cohort | Row Citation |
|------|---------------|-----------------|--------------|
| PM | | | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

```
TRACEABILITY AUDIT RESULT
All 16 roles cited: [PASS] / [FAIL — missing or generic citations: list roles]
Cross-check with SCHEDULE RECONCILIATION: [consistent / discrepancies: list]
```

---

### THREE-AXIS GAP AUDIT

Complete before SECTION 3. All rows are fill contracts.

#### Axis A — Role Completeness

| Role | Adoption month | Archetype cohort | Source (phase + month where named) |
|------|---------------|-----------------|-------------------------------------|
| PM | | | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

#### Axis B — Temporal Completeness

| Event | Month pinned | Type | Source section |
|-------|-------------|------|---------------|
| | | Adoption / Stall / Chasm / Bridge / Intervention | |

#### Axis C — Causal Specificity

| Gap / Risk / Stall | Named cause (non-generic) | THE INCUMBENT cited? | Source section |
|--------------------|--------------------------|---------------------|---------------|
| | | Yes / No | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A (role completeness):    [PASS — all 16 traced] / [FAIL — missing: list]
Axis B (temporal completeness):[PASS — all events pinned] / [FAIL — unpinned: list]
Axis C (causal specificity):   [PASS — all named, incumbent cited] / [FAIL — generic: list]
```

If any axis fails: correct the upstream phases before continuing to SECTION 3.

---

### SECTION 3 — Champion Network

**Derivation rule:** Every champion row must have a corresponding CHAMPION FORMATION EVENT in
the simulation body. Record formation phase and month. A champion without this citation fails.

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Formation phase/month | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|-----------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |

Minimum 2 champions.

---

### SECTION 4 — Intervention Recommendations

Sorted by adoption delta, highest first. Minimum 3 interventions.

| Rank | Intervention | Target roles | Displaces from incumbent | Adoption delta | Deploy before month |
|------|-------------|-------------|--------------------------|---------------|-------------------|
| 1 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 2 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 3 | | | [CITE: THE INCUMBENT] — [habit] | | |

---

### SECTION 5 — Churn Risk Register

Minimum 2 entries. Incumbent pull must cite THE INCUMBENT by name.

| Role | Archetype | Gravity | Churn trigger | Incumbent pull | Intervention to retain |
|------|-----------|---------|--------------|---------------|----------------------|
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |

---

### SECTION 6 — S-Curve Summary

| Phase | Month range | Adopters | % of 16 | Incumbent position |
|-------|------------|----------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

Final count must match 16. Cross-check against TRACEABILITY AUDIT and SCHEDULE RECONCILIATION.
Explain non-adopting roles and whether THE INCUMBENT permanently retains them.

---

### CONTRACT COMPLIANCE AUDIT

Return to the CITATION CONTRACT declared in the PREAMBLE. For each obligated section, verify
whether the citation requirement was met. Fill the Met? column now.

| Section | Required citation form | Met? | Evidence (field or cell that satisfies / violates) |
|---------|----------------------|------|---------------------------------------------------|
| PHASE 3 — chasm cause | THE INCUMBENT named in "Cause" row | [PASS / FAIL] | |
| SECTION 3 — champion network | THE INCUMBENT named in every "Incumbent argument countered" cell | [PASS / FAIL] | |
| SECTION 4 — interventions | THE INCUMBENT named in every "Displaces from incumbent" cell | [PASS / FAIL] | |
| SECTION 5 — churn risks | THE INCUMBENT named in every "Incumbent pull" cell | [PASS / FAIL] | |
| SCHEDULE RECONCILIATION | THE INCUMBENT named in deviation reasons where applicable | [PASS / FAIL] | |
| THREE-AXIS GAP AUDIT Axis C | "THE INCUMBENT cited? = Yes" for every incumbent-caused gap | [PASS / FAIL] | |

```
CONTRACT COMPLIANCE RESULT
Obligations met: [N] of 6
Obligations failed: [list — correction required before artifact is complete]
```

If any obligation failed: correct the relevant section above and re-verify.

---

## V-02 — Single Axis: Inertia Framing (Typed Gravity Citation Mandate)

**Variation axis:** Inertia framing — The DEPENDENCY GRAVITY ASSESSMENT table adds a "Derived
month range" column that mechanically maps each gravity score to its anchor range (1-2 → M1-M2,
3 → M3-M4, 4 → M5-M6, 5 → M7-M9) and is filled before SECTION 1. This makes the gravity-to-
month derivation explicit and checkable at setup time, not just referenced in prose. SCHEDULE
RECONCILIATION's status column adds a mandatory gravity citation sub-template: when a delay is
attributed to incumbent dependency, the reason must use the typed format
`G[N]: [exact behavior THE INCUMBENT had for this role that the gravity score captured]` — e.g.,
`G4: [THE INCUMBENT]'s daily stand-up reporting workflow this role owns, which {{topic}} doesn't
yet replace`. The format is enforced by a note in the SCHEDULE RECONCILIATION header: generic
forms ("delayed due to dependency," "gravity pull," "incumbent friction") are explicitly rejected.
All other structural elements carry from R4 V-05 unchanged.

**Hypothesis:** R4 V-02 introduced gravity scores and a gravity-column in SCHEDULE RECONCILIATION
with the format `gravity [G]: [reason citing THE INCUMBENT if applicable]`. This passes C-18's
structural requirement (score assigned, propagates to SCHEDULE RECONCILIATION) but permits
low-specificity deviation reasons because the format template does not reject them. C-18's pass
condition states that deviation reasons must read "delayed — gravity 4: [specific hold the
incumbent had for this role]" rather than generic assertions. The typed citation format achieves
this: by naming the exact incumbent behavior the gravity score was grounded in (from the basis
column in DEPENDENCY GRAVITY ASSESSMENT), the model produces deviations that trace back to a
specific declared dependency. As a second effect, the "Derived month range" column makes the
DEPENDENCY GRAVITY ASSESSMENT a falsifiable prediction table — if a gravity-5 role is committed
to M3, the deviation from the derived range is visible in the same row, requiring a stated reason
before SECTION 1 is completed. This closes the loop C-18 requires: declared dependency mechanism
→ numeric gravity score → derived month range → committed month deviation explained → simulation
deviation reason citing the specific gravity basis.

---

You are the adoption analyst for **{{topic}}**. Your simulation follows a structured protocol
with required output blocks. All blocks must be completed in full before advancing. Phase
Compliance Ledgers (PCL) are structural gates — correct any FAIL before writing the next phase.
Reason as the analyst throughout: where the protocol asks for a cause, give the actual cause;
where it asks for a mechanism, describe the mechanism that will actually work for this team.

Produce the artifact below in the order shown.

---

### PREAMBLE — Incumbent Declaration and Dependency Gravity Assessment

Your first task is to name THE INCUMBENT precisely. Then assess each role's dependency depth —
this gravity model drives your committed schedule and must be cited in deviation explanations.

```
THE INCUMBENT:
  [Specific workflow, tool, or habit {{topic}} displaces. Name it precisely — not
   "current process" but the actual named thing.]

What THE INCUMBENT does well for this team:
  - [Advantage 1: which cohorts rely on this and why]
  - [Advantage 2: what {{topic}} does not yet match]

What {{topic}} must prove to displace it:
  - For early majority: [specific proof point]
  - For late majority:  [specific proof point]

Downstream citation contract — THE INCUMBENT must appear by name in:
  PHASE 3 chasm cause | SECTION 3 champion "Incumbent argument countered" column |
  SECTION 4 intervention displacement target | SECTION 5 churn risk pull |
  THREE-AXIS GAP AUDIT Axis C | SCHEDULE RECONCILIATION deviation reasons where applicable
```

**DEPENDENCY GRAVITY ASSESSMENT**

Rate each role's daily reliance on THE INCUMBENT. The "Derived month range" column is computed
mechanically from the gravity score — fill it from the anchor table, then use it to anchor
SECTION 1 committed months.

Gravity scale:
- 5 — Uses THE INCUMBENT daily; no viable workaround; switching requires process change
- 4 — Uses it most days; minor workarounds; switching requires convincing evidence
- 3 — Uses it regularly but not daily; moderate switching friction
- 2 — Uses it occasionally; can adopt without displacing workflow immediately
- 1 — Rarely or never uses THE INCUMBENT; low friction to adopt

Derived month range anchor: G1–G2 → M1–M2 | G3 → M3–M4 | G4 → M5–M6 | G5 → M7–M9

| Role | Gravity (1–5) | Basis: specific behavior THE INCUMBENT supports for this role | Derived month range |
|------|--------------|--------------------------------------------------------------|---------------------|
| PM | | | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

If any role's committed month in SECTION 1 falls outside its derived month range, state a
reason in the "Incumbent dependency" column of SECTION 1.

---

### SECTION 1 — Archetype Mapping and Committed Adoption Schedule

Before the simulation runs, commit to a schedule anchored to gravity scores. State a deviation
reason in the dependency column for any committed month outside the derived range.

| Role | Rogers Archetype | Incumbent dependency (gravity + deviation reason if outside range) | Committed adoption month |
|------|-----------------|-------------------------------------------------------------------|------------------------|
| PM | | gravity [N], derived range [M1-M2 / M3-M4 / M5-M6 / M7-M9] — [deviation reason if applicable] | M[N] |
| UX | | | M[N] |
| C-01 | | | M[N] |
| C-02 | | | M[N] |
| C-03 | | | M[N] |
| C-04 | | | M[N] |
| C-05 | | | M[N] |
| C-06 | | | M[N] |
| C-07 | | | M[N] |
| C-08 | | | M[N] |
| C-09 | | | M[N] |
| C-10 | | | M[N] |
| C-11 | | | M[N] |
| C-12 | | | M[N] |
| Support | | | M[N] |
| SRE | | | M[N] |

---

### SECTION 2 — Month-by-Month Simulation

Rows addressable as `[PHASE N / Month M / Row K]` for TRACEABILITY AUDIT citations.

---

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 adopted. THE INCUMBENT is fully in place.

**Month 1**

Roles committed to M1: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull (why others don't yet) |
|-----|---------------------|-----------|-----------------|--------------------------------------|
| 1 | | Innovator | | [CITE: THE INCUMBENT] still holds because: [...] |

```
Cumulative: [N] of 16
```

**Month 2** (include all roles committed to M2)

Roles committed to M2: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | |

```
PHASE 1 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M1-M2 committed roles appeared or explain delay — cite gravity basis where applicable]
Incumbent position: [describe]
Signal to EA cohort: [what evidence now exists that {{topic}} works]
```

```
PHASE 1 COMPLIANCE LEDGER
C-01 (archetype mapping in SECTION 1 — all 16 rows filled): [PASS / FAIL]
C-16a (Month 1 block opened with "Roles committed to M1:"): [PASS / FAIL]
C-16b (Month 2 block opened with "Roles committed to M2:"): [PASS / FAIL]
C-16c (PHASE 1 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]
C-11 (THE INCUMBENT cited in at least one Incumbent pull cell): [PASS / FAIL]
C-18 (Derived month range column filled in DEPENDENCY GRAVITY ASSESSMENT for all 16 roles): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 2.
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

Roles committed to M3: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | [CITE: THE INCUMBENT] still holds for non-adopters because: [...] |
| 2 | | | | |

```
Cumulative: [N] of 16
```

**CHAMPION FORMATION EVENT** — identify the first champion emerging this phase.
If no champion formed yet, explain why.

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role — must appear in a simulation row at or before this month]
  Bridging mechanism:        [how this role will accelerate spread to the next cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific advantage this champion counters]
```

**Month 4**

Roles committed to M4: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | |
| 2 | | | | |

```
PHASE 2 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M3-M4 committed roles appeared or explain — cite gravity basis where applicable]
Incumbent position: [still dominant with which cohorts? why?]
Champion network: [roles from CHAMPION FORMATION EVENT(s) + formation month]
Gap to EM: [what THE INCUMBENT still offers that EM cohort values — CITE: THE INCUMBENT]
```

```
PHASE 2 COMPLIANCE LEDGER
C-14 (CHAMPION FORMATION EVENT fired with all required fields): [PASS / FAIL]
C-16a-c (month blocks opened with committed-roles prompt; phase close includes scheduled roles met): [PASS / FAIL]
C-09 (CHAMPION FORMATION EVENT "Incumbent argument targeted" is non-generic): [PASS / FAIL / N/A]
C-11 (THE INCUMBENT cited in Gap to EM): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 3.
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and [EM roles — name specifically] |
| Cause | [What specific advantage of THE INCUMBENT prevents EM crossing? [CITE: THE INCUMBENT by name] — name the habit or workflow.] |
| Gravity cluster | [Which roles have gravity 4–5? Name them. This cluster is the chasm anchor — why their dependency depth makes crossing harder.] |
| Incumbent win condition | [CITE: THE INCUMBENT] delivers [...] that {{topic}} doesn't yet match for EM |
| Risk if not bridged | [Roles that plateau; THE INCUMBENT entrenches for high-gravity cohort] |
| Bridge condition | [What EM needs to see from {{topic}} to switch] |
| Champion | [Role from CHAMPION FORMATION EVENT + mechanism + THE INCUMBENT argument they counter] |

```
PHASE 3 CLOSE
Bridge condition: [what must be true for PHASE 4 entry]
Incumbent position at chasm: [still dominant / weakening / differentiated]
```

```
PHASE 3 COMPLIANCE LEDGER
C-03 (Gap, Cause, Risk elements each substantive and named): [PASS / FAIL]
C-11 (THE INCUMBENT named in Cause element): [PASS / FAIL]
C-12 (Champion element cites specific CHAMPION FORMATION EVENT role): [PASS / FAIL]
C-18 (Gravity cluster element names specific roles by gravity score): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 4.
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.

**Month 5**

Roles committed to M5: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
Cumulative: [N] of 16
Churn risk?: [role + gravity score + trigger; what [CITE: THE INCUMBENT] behavior reasserts]
```

**CHAMPION FORMATION EVENT** — if a new champion emerges to bridge EM toward LM, record it.
If no new champion: "No new champion this phase."

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [mechanism toward Late Majority cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific argument]
```

**Month 6**

Roles committed to M6: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
PHASE 4 CLOSE
Adopters: [roles, count, %]
Scheduled roles met: [confirm M5-M6 committed roles appeared or explain — cite gravity basis where applicable]
Incumbent position: [retreating / residual / eliminated in this cohort]
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

Roles committed to M7–M9: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Late Majority / Laggard | | |
| 2 | | | | |

```
PHASE 5 CLOSE
Final adopters: [N] of 16 ([%])
Non-adopters (if any): [roles; gravity score; reason THE INCUMBENT still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

**SCHEDULE RECONCILIATION**

Reconcile committed schedule against actual outcomes.

**TYPED GRAVITY CITATION RULE:** When a delay is attributed to incumbent dependency, the
deviation reason MUST use this format: `G[N]: [exact behavior THE INCUMBENT had for this role
that the gravity score captured]`
Generic forms are rejected: "delayed due to dependency," "gravity pull," "incumbent friction,"
and similar non-specific phrases fail C-18 at the row level.

| Role | Gravity | Committed month | Actual month | Status |
|------|---------|----------------|-------------|--------|
| PM | | | | On schedule / Delayed [N months] — G[N]: [exact incumbent behavior for this role] / Non-adopter |
| UX | | | | |
| C-01 | | | | |
| C-02 | | | | |
| C-03 | | | | |
| C-04 | | | | |
| C-05 | | | | |
| C-06 | | | | |
| C-07 | | | | |
| C-08 | | | | |
| C-09 | | | | |
| C-10 | | | | |
| C-11 | | | | |
| C-12 | | | | |
| Support | | | | |
| SRE | | | | |

```
SCHEDULE RECONCILIATION RESULT
On schedule: [N] of 16
Delayed: [N] — [list; each delay reason uses typed gravity format G[N]: [exact behavior]]
Non-adopters: [list with gravity scores]
Gravity accuracy check: [did high-gravity roles (4-5) cluster in later months as predicted by derived ranges?]
Typed citation check: [any deviation reason using generic language? List and correct.]
```

---

### TRACEABILITY AUDIT

**Row Citation format:** `[PHASE N / Month M / Row K]`. Generic citations fail.

| Role | Adoption month | Archetype cohort | Row Citation |
|------|---------------|-----------------|--------------|
| PM | | | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

```
TRACEABILITY AUDIT RESULT
All 16 roles cited: [PASS] / [FAIL — missing or generic citations: list roles]
Cross-check with SCHEDULE RECONCILIATION: [consistent / discrepancies: list]
```

---

### THREE-AXIS GAP AUDIT

#### Axis A — Role Completeness

| Role | Adoption month | Archetype cohort | Source (phase + month where named) |
|------|---------------|-----------------|-------------------------------------|
| PM | | | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

#### Axis B — Temporal Completeness

| Event | Month pinned | Type | Source section |
|-------|-------------|------|---------------|
| | | Adoption / Stall / Chasm / Bridge / Intervention | |

#### Axis C — Causal Specificity

| Gap / Risk / Stall | Named cause (non-generic) | THE INCUMBENT cited? | Source section |
|--------------------|--------------------------|---------------------|---------------|
| | | Yes / No | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A: [PASS / FAIL]
Axis B: [PASS / FAIL]
Axis C: [PASS — all named, incumbent cited] / [FAIL — generic: list]
```

---

### SECTION 3 — Champion Network

**Derivation rule:** Every champion row must have a corresponding CHAMPION FORMATION EVENT.

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Formation phase/month | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|-----------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |

### SECTION 4 — Intervention Recommendations

| Rank | Intervention | Target roles | Displaces from incumbent | Adoption delta | Deploy before month |
|------|-------------|-------------|--------------------------|---------------|-------------------|
| 1 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 2 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 3 | | | [CITE: THE INCUMBENT] — [habit] | | |

### SECTION 5 — Churn Risk Register

| Role | Archetype | Gravity | Churn trigger | Incumbent pull | Intervention to retain |
|------|-----------|---------|--------------|---------------|----------------------|
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |

### SECTION 6 — S-Curve Summary

| Phase | Month range | Adopters | % of 16 | Incumbent position |
|-------|------------|----------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

Final count must match 16. Explain non-adopting roles.

---

## V-03 — Single Axis: Lifecycle Emphasis (Gravity-Cluster Chasm Gate)

**Variation axis:** Lifecycle emphasis — PHASE 3 is restructured around a mandatory GRAVITY
CLUSTER IDENTIFICATION step that must be completed before the chasm table opens. The step names
every role with gravity 4 or 5, declares them the "chasm anchor cluster," and states why their
combined dependency depth makes the chasm wider than individual role resistance would suggest
(cluster inertia effect). The chasm table is then derived from this cluster: the "Gap" row names
the cluster roles specifically, the "Cause" row explains which INCUMBENT behavior the cluster
depends on, and the "Bridge condition" must state what would cause at least one gravity-4+ role
to move. Additionally, the PHASE 4 ENTRY condition is made explicit: Phase 4 does not open until
the bridge condition named in PHASE 3 has been satisfied for at least one gravity-4+ role.
All other structural elements carry from R4 V-05 unchanged.

**Hypothesis:** In all prior rounds, the chasm phase contains a "Gravity cluster" row (added in
R4 V-02) but it is a single table row that can be filled with a brief clause. The gravity cluster
is the structural explanation of why the chasm exists — high-gravity roles are not independent
resistors; they form a social bloc that signals to the adjacent EM cohort that the new tool is
not yet safe to adopt. C-18's chasm table row requirement passes when this row is present and
names the cluster roles; but the criterion's deeper intent — that gravity scores propagate as
numeric anchors mechanically explaining the chasm cause — is only fully realized when the cluster
is first-class simulation state, not a row annotation. A dedicated GRAVITY CLUSTER IDENTIFICATION
block before the chasm table forces the model to (a) enumerate the cluster explicitly before
drawing inferences from it, (b) state the cluster inertia effect as a declared mechanism, and
(c) derive all downstream chasm rows from the cluster rather than generating them independently.
This also strengthens C-09 (cross-archetype influence dynamics): the cluster's eventual movement
in PHASE 4 becomes a simulation event traceable back to the gravity model.

---

You are the adoption analyst for **{{topic}}**. Your simulation follows a structured protocol
with required output blocks. All blocks must be completed in full before advancing. Phase
Compliance Ledgers (PCL) are structural gates — correct any FAIL before writing the next phase.
Reason as the analyst throughout: where the protocol asks for a cause, give the actual cause;
where it asks for a mechanism, describe the mechanism that will actually work for this team.

Produce the artifact below in the order shown.

---

### PREAMBLE — Incumbent Declaration and Dependency Gravity Assessment

Your first task is to name THE INCUMBENT precisely. Then assess each role's dependency depth —
the gravity model drives your committed schedule and defines the chasm anchor cluster.

```
THE INCUMBENT:
  [Specific workflow, tool, or habit {{topic}} displaces. Name it precisely — not
   "current process" but the actual named thing.]

What THE INCUMBENT does well for this team:
  - [Advantage 1: which cohorts rely on this and why]
  - [Advantage 2: what {{topic}} does not yet match]

What {{topic}} must prove to displace it:
  - For early majority: [specific proof point]
  - For late majority:  [specific proof point]

Downstream citation contract — THE INCUMBENT must appear by name in:
  PHASE 3 chasm cause | SECTION 3 champion "Incumbent argument countered" column |
  SECTION 4 intervention displacement target | SECTION 5 churn risk pull |
  THREE-AXIS GAP AUDIT Axis C | SCHEDULE RECONCILIATION deviation reasons where applicable
```

**DEPENDENCY GRAVITY ASSESSMENT**

Rate each role's daily reliance on THE INCUMBENT. Roles scoring 4 or 5 become the chasm anchor
cluster in PHASE 3 — the cluster will be named and analyzed before the chasm table opens.

Gravity scale: 5 = daily, no workaround | 4 = most days, minor workaround |
3 = regular but not daily | 2 = occasional | 1 = rare/never

| Role | Gravity (1–5) | Basis: what this role uses THE INCUMBENT for |
|------|--------------|---------------------------------------------|
| PM | | |
| UX | | |
| C-01 | | |
| C-02 | | |
| C-03 | | |
| C-04 | | |
| C-05 | | |
| C-06 | | |
| C-07 | | |
| C-08 | | |
| C-09 | | |
| C-10 | | |
| C-11 | | |
| C-12 | | |
| Support | | |
| SRE | | |

Gravity-to-committed-month anchor: G1–G2 → M1–M2 | G3 → M3–M4 | G4 → M5–M6 | G5 → M7–M9.

---

### SECTION 1 — Archetype Mapping and Committed Adoption Schedule

| Role | Rogers Archetype | Incumbent dependency (gravity + note) | Committed adoption month |
|------|-----------------|--------------------------------------|------------------------|
| PM | | gravity [N] — [note if deviating] | M[N] |
| UX | | | M[N] |
| C-01 | | | M[N] |
| C-02 | | | M[N] |
| C-03 | | | M[N] |
| C-04 | | | M[N] |
| C-05 | | | M[N] |
| C-06 | | | M[N] |
| C-07 | | | M[N] |
| C-08 | | | M[N] |
| C-09 | | | M[N] |
| C-10 | | | M[N] |
| C-11 | | | M[N] |
| C-12 | | | M[N] |
| Support | | | M[N] |
| SRE | | | M[N] |

---

### SECTION 2 — Month-by-Month Simulation

Rows addressable as `[PHASE N / Month M / Row K]` for TRACEABILITY AUDIT.

---

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 adopted. THE INCUMBENT is fully in place.

**Month 1**

Roles committed to M1: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | [CITE: THE INCUMBENT] still holds because: [...] |

```
Cumulative: [N] of 16
```

**Month 2**

Roles committed to M2: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | |

```
PHASE 1 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M1-M2 committed roles appeared or explain delay — cite gravity where applicable]
Incumbent position: [describe]
Signal to EA cohort: [what evidence now exists that {{topic}} works]
```

```
PHASE 1 COMPLIANCE LEDGER
C-01 (archetype mapping in SECTION 1 — all 16 rows filled): [PASS / FAIL]
C-16a (Month 1 block opened with "Roles committed to M1:"): [PASS / FAIL]
C-16b (Month 2 block opened with "Roles committed to M2:"): [PASS / FAIL]
C-16c (PHASE 1 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]
C-11 (THE INCUMBENT cited in at least one Incumbent pull cell): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 2.
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

Roles committed to M3: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | [CITE: THE INCUMBENT] still holds for non-adopters because: [...] |
| 2 | | | | |

```
Cumulative: [N] of 16
```

**CHAMPION FORMATION EVENT**

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [how this role will accelerate spread to the next cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific advantage this champion counters]
```

**Month 4**

Roles committed to M4: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | |
| 2 | | | | |

```
PHASE 2 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm M3-M4 committed roles appeared or explain — cite gravity where applicable]
Incumbent position: [still dominant with which cohorts? why?]
Champion network: [roles from CHAMPION FORMATION EVENT(s) + formation month]
Gap to EM: [what THE INCUMBENT still offers that EM cohort values — CITE: THE INCUMBENT]
```

```
PHASE 2 COMPLIANCE LEDGER
C-14 (CHAMPION FORMATION EVENT fired with all required fields): [PASS / FAIL]
C-16a-c (month blocks opened with committed-roles prompt; phase close includes scheduled roles met): [PASS / FAIL]
C-11 (THE INCUMBENT cited in Gap to EM): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 3.
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

**GRAVITY CLUSTER IDENTIFICATION** — complete before opening the chasm table. This step is
mandatory and cannot be skipped. If fewer than two roles have gravity 4 or 5, state that and
explain what constitutes the chasm anchor instead.

```
GRAVITY CLUSTER IDENTIFICATION
  Roles with gravity 4-5 (the chasm anchor cluster):
    [Role 1] — gravity [N] — [the specific THE INCUMBENT behavior they depend on from PREAMBLE]
    [Role 2] — gravity [N] — [...]
    [continue for all gravity 4-5 roles]

  Cluster size: [N] roles of 16 total

  Cluster inertia effect:
    These [N] roles collectively signal to the adjacent EM cohort that [THE INCUMBENT] is
    still necessary because: [what the cluster's continued reliance communicates to observers
    who have not yet adopted]

  Bridge requirement for PHASE 4 entry:
    At least one of [list cluster roles] must adopt before PHASE 4 opens.
    What must be true for the first cluster role to move: [specific condition]
```

**CHASM TABLE** — derived from GRAVITY CLUSTER IDENTIFICATION above.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and the chasm anchor cluster: [name cluster roles from GRAVITY CLUSTER IDENTIFICATION] |
| Cause | [CITE: THE INCUMBENT] — the specific behavior the cluster depends on that {{topic}} does not yet replace |
| Cluster inertia | [From GRAVITY CLUSTER IDENTIFICATION: why the cluster's combined resistance amplifies the gap beyond individual role resistance] |
| Incumbent win condition | [CITE: THE INCUMBENT] delivers [...] that {{topic}} doesn't yet match for this cluster |
| Risk if not bridged | [Roles that plateau with the cluster; THE INCUMBENT entrenches for gravity 4-5 cohort] |
| Bridge condition | [From GRAVITY CLUSTER IDENTIFICATION bridge requirement: what must be true for the first cluster role to move] |
| Champion | [Role from CHAMPION FORMATION EVENT + mechanism + THE INCUMBENT argument they counter for this cluster] |

```
PHASE 3 CLOSE
Bridge condition met when: [specific observable event — name the cluster role that must move first]
Incumbent position at chasm: [still dominant / weakening / differentiated]
Cluster status: [N] of [cluster size] cluster roles still on THE INCUMBENT
```

**PHASE 4 ENTRY GATE:** Phase 4 does not open until at least one gravity-4+ role from the
cluster has adopted. If the simulation reaches Month 5 without a cluster role adopting, record
this as a PHASE 3 EXTENDED stall event and explain what was required to unstick it.

```
PHASE 3 COMPLIANCE LEDGER
C-03 (Gap, Cause, Risk elements each substantive): [PASS / FAIL]
C-11 (THE INCUMBENT named in Cause element): [PASS / FAIL]
C-12 (Champion element cites specific CHAMPION FORMATION EVENT role): [PASS / FAIL]
C-18 (GRAVITY CLUSTER IDENTIFICATION block completed; bridge requirement stated): [PASS / FAIL]
PHASE 4 GATE (at least one gravity-4+ role committed to M5 or earlier): [PASS / FAIL / STALL]

If any item is FAIL: correct before writing PHASE 4.
If STALL: write a PHASE 3 EXTENDED block explaining the unlocking event.
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim. PHASE 4 ENTRY GATE cleared: [name the
first gravity-4+ role that adopted and the month they appear in the simulation].

**Month 5**

Roles committed to M5: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
Cumulative: [N] of 16
Cluster progress: [N] of [cluster size] gravity-4+ roles now adopted
Churn risk?: [role + gravity score + trigger; what [CITE: THE INCUMBENT] behavior reasserts]
```

**CHAMPION FORMATION EVENT** — if a new champion emerges to bridge EM toward LM, record it.

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [mechanism toward Late Majority cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific argument]
```

**Month 6**

Roles committed to M6: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
PHASE 4 CLOSE
Adopters: [roles, count, %]
Scheduled roles met: [confirm M5-M6 committed roles appeared or explain — cite gravity where applicable]
Cluster adoption progress: [N] of [cluster size] gravity-4+ roles adopted
Incumbent position: [retreating / residual / eliminated in this cohort]
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

Roles committed to M7–M9: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Late Majority / Laggard | | |
| 2 | | | | |

```
PHASE 5 CLOSE
Final adopters: [N] of 16 ([%])
Cluster final status: [N] of [cluster size] gravity-4+ roles adopted; [N] remain on THE INCUMBENT
Non-adopters (if any): [roles; gravity score; reason THE INCUMBENT still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

**SCHEDULE RECONCILIATION**

| Role | Gravity | Committed month | Actual month | Status |
|------|---------|----------------|-------------|--------|
| PM | | | | On schedule / Delayed [N months] — gravity [G]: [reason citing THE INCUMBENT if applicable] / Non-adopter |
| UX | | | | |
| C-01 | | | | |
| C-02 | | | | |
| C-03 | | | | |
| C-04 | | | | |
| C-05 | | | | |
| C-06 | | | | |
| C-07 | | | | |
| C-08 | | | | |
| C-09 | | | | |
| C-10 | | | | |
| C-11 | | | | |
| C-12 | | | | |
| Support | | | | |
| SRE | | | | |

```
SCHEDULE RECONCILIATION RESULT
On schedule: [N] of 16
Delayed: [N] — [list with gravity scores and reasons; cite THE INCUMBENT where applicable]
Non-adopters: [list with gravity scores]
Gravity accuracy check: [did gravity-4+ cluster roles adopt in M5–M9 as the cluster inertia model predicted?]
```

---

### TRACEABILITY AUDIT

| Role | Adoption month | Archetype cohort | Row Citation |
|------|---------------|-----------------|--------------|
| PM | | | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

```
TRACEABILITY AUDIT RESULT
All 16 roles cited: [PASS] / [FAIL — missing or generic: list]
Cross-check with SCHEDULE RECONCILIATION: [consistent / discrepancies: list]
```

---

### THREE-AXIS GAP AUDIT

#### Axis A — Role Completeness

| Role | Adoption month | Archetype cohort | Source |
|------|---------------|-----------------|--------|
| PM | | | |
| UX | | | |
| C-01 through C-12 | | | |
| Support | | | |
| SRE | | | |

#### Axis B — Temporal Completeness

| Event | Month pinned | Type | Source section |
|-------|-------------|------|---------------|
| | | Adoption / Stall / Chasm / Bridge / Intervention | |

#### Axis C — Causal Specificity

| Gap / Risk / Stall | Named cause (non-generic) | THE INCUMBENT cited? | Source section |
|--------------------|--------------------------|---------------------|---------------|
| | | Yes / No | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A: [PASS / FAIL]
Axis B: [PASS / FAIL]
Axis C: [PASS / FAIL]
```

---

### SECTION 3 — Champion Network

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Formation phase/month | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|-----------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |

### SECTION 4 — Intervention Recommendations

| Rank | Intervention | Target roles | Displaces from incumbent | Adoption delta | Deploy before month |
|------|-------------|-------------|--------------------------|---------------|-------------------|
| 1 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 2 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 3 | | | [CITE: THE INCUMBENT] — [habit] | | |

### SECTION 5 — Churn Risk Register

| Role | Archetype | Gravity | Churn trigger | Incumbent pull | Intervention to retain |
|------|-----------|---------|--------------|---------------|----------------------|
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |

### SECTION 6 — S-Curve Summary

| Phase | Month range | Adopters | % of 16 | Incumbent position |
|-------|------------|----------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

Gravity cluster final outcome: [N] of [cluster size] adopted; explain any that remain on THE INCUMBENT.

---

## V-04 — Combined: Output Format + Inertia Framing (Citation Contract Table + Typed Gravity Citation)

**Variation axes:** Output format (V-01) + Inertia framing (V-02)

**Hypothesis:** V-01's CONTRACT COMPLIANCE AUDIT and V-02's typed gravity citation mandate
operate on independent surfaces: V-01 closes the forward-accountability gap in C-17 (did the
preamble declare which sections must cite, and were those declarations honored?), while V-02
closes the specificity gap in C-18 (do deviation reasons cite the exact gravity basis, not
generic dependency language?). They share no structural overlap — V-01 adds a table to the
PREAMBLE and a compliance audit at close; V-02 modifies the DEPENDENCY GRAVITY ASSESSMENT
and the SCHEDULE RECONCILIATION status format. Combining them produces an artifact where every
incumbent citation obligation is both forward-declared (V-01) and mechanically specific (V-02):
the CITATION CONTRACT enumerates which sections must cite THE INCUMBENT; the typed gravity format
ensures that citations in SCHEDULE RECONCILIATION meet a specificity threshold that distinguishes
gravity-caused delays from other delay types. The combination should produce a clean C-17 PASS
(contract table with directive language) and a clean C-18 PASS (gravity scores in preamble,
derived month range column, typed citation in reconciliation).

---

You are the adoption analyst for **{{topic}}**. Your simulation follows a structured protocol
with required output blocks. All blocks must be completed in full before advancing. Phase
Compliance Ledgers (PCL) are structural gates — correct any FAIL before writing the next phase.
Reason as the analyst throughout.

Produce the artifact below in the order shown.

---

### PREAMBLE — Incumbent Declaration, Citation Contract, and Dependency Gravity Assessment

Your first task is to name THE INCUMBENT precisely, declare the citation contract, and assess
role dependency depth.

```
THE INCUMBENT:
  [Specific workflow, tool, or habit {{topic}} displaces. Name it precisely.]

What THE INCUMBENT does well for this team:
  - [Advantage 1: which cohorts rely on this and why]
  - [Advantage 2: what {{topic}} does not yet match]

What {{topic}} must prove to displace it:
  - For early majority: [specific proof point]
  - For late majority:  [specific proof point]
```

**CITATION CONTRACT**

| Section | Required citation form | Directive | Met? |
|---------|----------------------|-----------|------|
| PHASE 3 — chasm cause | "Cause" row must name THE INCUMBENT by name | MUST | [fill in CONTRACT COMPLIANCE AUDIT] |
| SECTION 3 — champion network | Every "Incumbent argument countered" cell must cite THE INCUMBENT by name | MUST | [fill in CONTRACT COMPLIANCE AUDIT] |
| SECTION 4 — interventions | Every "Displaces from incumbent" cell must cite THE INCUMBENT by name | REQUIRED | [fill in CONTRACT COMPLIANCE AUDIT] |
| SECTION 5 — churn risks | Every "Incumbent pull" cell must cite THE INCUMBENT by name | REQUIRED | [fill in CONTRACT COMPLIANCE AUDIT] |
| SCHEDULE RECONCILIATION | Typed gravity citation required for incumbent-caused delays: `G[N]: [exact behavior]` | OBLIGATED | [fill in CONTRACT COMPLIANCE AUDIT] |
| THREE-AXIS GAP AUDIT Axis C | "THE INCUMBENT cited?" = Yes for all incumbent-caused gaps | REQUIRED | [fill in CONTRACT COMPLIANCE AUDIT] |

**DEPENDENCY GRAVITY ASSESSMENT**

Derived month range anchor: G1–G2 → M1–M2 | G3 → M3–M4 | G4 → M5–M6 | G5 → M7–M9

| Role | Gravity (1–5) | Basis: specific behavior THE INCUMBENT supports for this role | Derived month range |
|------|--------------|--------------------------------------------------------------|---------------------|
| PM | | | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

---

### SECTION 1 — Archetype Mapping and Committed Adoption Schedule

| Role | Rogers Archetype | Incumbent dependency (gravity + deviation reason if outside derived range) | Committed adoption month |
|------|-----------------|---------------------------------------------------------------------------|------------------------|
| PM | | gravity [N], derived range [X] — [reason if outside range] | M[N] |
| UX | | | M[N] |
| C-01 | | | M[N] |
| C-02 | | | M[N] |
| C-03 | | | M[N] |
| C-04 | | | M[N] |
| C-05 | | | M[N] |
| C-06 | | | M[N] |
| C-07 | | | M[N] |
| C-08 | | | M[N] |
| C-09 | | | M[N] |
| C-10 | | | M[N] |
| C-11 | | | M[N] |
| C-12 | | | M[N] |
| Support | | | M[N] |
| SRE | | | M[N] |

---

### SECTION 2 — Month-by-Month Simulation

Rows addressable as `[PHASE N / Month M / Row K]`.

---

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 adopted. THE INCUMBENT is fully in place.

**Month 1**

Roles committed to M1: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | [CITE: THE INCUMBENT] still holds because: [...] |

```
Cumulative: [N] of 16
```

**Month 2**

Roles committed to M2: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | |

```
PHASE 1 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm or explain delay — cite gravity basis where applicable]
Incumbent position: [describe]
Signal to EA cohort: [what evidence now exists that {{topic}} works]
```

```
PHASE 1 COMPLIANCE LEDGER
C-01 (archetype mapping in SECTION 1 — all 16 rows filled): [PASS / FAIL]
C-16a (Month 1 block opened with "Roles committed to M1:"): [PASS / FAIL]
C-16b (Month 2 block opened with "Roles committed to M2:"): [PASS / FAIL]
C-16c (PHASE 1 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]
C-11 (THE INCUMBENT cited in at least one Incumbent pull cell): [PASS / FAIL]
C-18 (Derived month range column filled in DEPENDENCY GRAVITY ASSESSMENT): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 2.
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

Roles committed to M3: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | [CITE: THE INCUMBENT] still holds for non-adopters because: [...] |
| 2 | | | | |

```
Cumulative: [N] of 16
```

**CHAMPION FORMATION EVENT**

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [how this role will accelerate spread to the next cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific advantage this champion counters]
```

**Month 4**

Roles committed to M4: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | |
| 2 | | | | |

```
PHASE 2 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm or explain — cite gravity basis where applicable]
Incumbent position: [still dominant with which cohorts?]
Champion network: [roles from CHAMPION FORMATION EVENT(s) + formation month]
Gap to EM: [what THE INCUMBENT still offers that EM cohort values — CITE: THE INCUMBENT]
```

```
PHASE 2 COMPLIANCE LEDGER
C-14 (CHAMPION FORMATION EVENT fired with all required fields): [PASS / FAIL]
C-16a-c (month blocks opened with committed-roles prompt; scheduled roles met field present): [PASS / FAIL]
C-09 (CHAMPION FORMATION EVENT "Incumbent argument targeted" is non-generic): [PASS / FAIL / N/A]
C-11 (THE INCUMBENT cited in Gap to EM): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 3.
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and [EM roles — name specifically] |
| Cause | [CITE: THE INCUMBENT by name — the specific habit or workflow blocking EM crossing] |
| Gravity cluster | [Roles with gravity 4–5 from PREAMBLE; why their combined dependency depth defines the chasm] |
| Incumbent win condition | [CITE: THE INCUMBENT] delivers [...] that {{topic}} doesn't yet match for EM |
| Risk if not bridged | [Roles that plateau; THE INCUMBENT entrenches for high-gravity cohort] |
| Bridge condition | [What EM needs to see from {{topic}} to switch] |
| Champion | [Role from CHAMPION FORMATION EVENT + mechanism + THE INCUMBENT argument they counter] |

```
PHASE 3 CLOSE
Bridge condition: [what must be true for PHASE 4 entry]
Incumbent position at chasm: [still dominant / weakening / differentiated]
```

```
PHASE 3 COMPLIANCE LEDGER
C-03 (Gap, Cause, Risk substantive and named): [PASS / FAIL]
C-11 (THE INCUMBENT named in Cause element — satisfies CITATION CONTRACT row 1): [PASS / FAIL]
C-12 (Champion element cites specific CHAMPION FORMATION EVENT role): [PASS / FAIL]
C-18 (Gravity cluster element names specific roles and states inertia mechanism): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 4.
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.

**Month 5**

Roles committed to M5: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
Cumulative: [N] of 16
Churn risk?: [role + gravity score + trigger; what [CITE: THE INCUMBENT] behavior reasserts]
```

**CHAMPION FORMATION EVENT** (if new champion; else "No new champion this phase")

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [mechanism toward Late Majority cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific argument]
```

**Month 6**

Roles committed to M6: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
PHASE 4 CLOSE
Adopters: [roles, count, %]
Scheduled roles met: [confirm or explain — cite gravity basis where applicable]
Incumbent position: [retreating / residual / eliminated in this cohort]
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

Roles committed to M7–M9: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Late Majority / Laggard | | |
| 2 | | | | |

```
PHASE 5 CLOSE
Final adopters: [N] of 16 ([%])
Non-adopters (if any): [roles; gravity score; reason THE INCUMBENT still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

**SCHEDULE RECONCILIATION**

**TYPED GRAVITY CITATION RULE:** When delay is attributed to incumbent dependency, use the
mandatory format: `G[N]: [exact behavior THE INCUMBENT had for this role that the gravity
score captured]`. Generic forms ("delayed due to dependency," "gravity pull") are rejected.

| Role | Gravity | Committed month | Actual month | Status |
|------|---------|----------------|-------------|--------|
| PM | | | | On schedule / Delayed [N months] — G[N]: [exact incumbent behavior] / Non-adopter |
| UX | | | | |
| C-01 | | | | |
| C-02 | | | | |
| C-03 | | | | |
| C-04 | | | | |
| C-05 | | | | |
| C-06 | | | | |
| C-07 | | | | |
| C-08 | | | | |
| C-09 | | | | |
| C-10 | | | | |
| C-11 | | | | |
| C-12 | | | | |
| Support | | | | |
| SRE | | | | |

```
SCHEDULE RECONCILIATION RESULT
On schedule: [N] of 16
Delayed: [N] — [list; each delay uses typed gravity format G[N]: [exact behavior]]
Non-adopters: [list with gravity scores]
Gravity accuracy check: [did high-gravity roles cluster in later months as derived ranges predicted?]
Typed citation check: [any generic language used? List and correct.]
```

---

### TRACEABILITY AUDIT

| Role | Adoption month | Archetype cohort | Row Citation |
|------|---------------|-----------------|--------------|
| PM | | | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

```
TRACEABILITY AUDIT RESULT
All 16 roles cited: [PASS / FAIL]
Cross-check with SCHEDULE RECONCILIATION: [consistent / discrepancies]
```

---

### THREE-AXIS GAP AUDIT

#### Axis A — Role Completeness

| Role | Adoption month | Archetype cohort | Source |
|------|---------------|-----------------|--------|
| PM | | | |
| UX | | | |
| C-01 through C-12 | | | |
| Support | | | |
| SRE | | | |

#### Axis B — Temporal Completeness

| Event | Month pinned | Type | Source section |
|-------|-------------|------|---------------|
| | | Adoption / Stall / Chasm / Bridge / Intervention | |

#### Axis C — Causal Specificity

| Gap / Risk / Stall | Named cause (non-generic) | THE INCUMBENT cited? | Source section |
|--------------------|--------------------------|---------------------|---------------|
| | | Yes / No | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A: [PASS / FAIL]
Axis B: [PASS / FAIL]
Axis C: [PASS / FAIL]
```

---

### SECTION 3 — Champion Network

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Formation phase/month | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|-----------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |

### SECTION 4 — Intervention Recommendations

| Rank | Intervention | Target roles | Displaces from incumbent | Adoption delta | Deploy before month |
|------|-------------|-------------|--------------------------|---------------|-------------------|
| 1 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 2 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 3 | | | [CITE: THE INCUMBENT] — [habit] | | |

### SECTION 5 — Churn Risk Register

| Role | Archetype | Gravity | Churn trigger | Incumbent pull | Intervention to retain |
|------|-----------|---------|--------------|---------------|----------------------|
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |

### SECTION 6 — S-Curve Summary

| Phase | Month range | Adopters | % of 16 | Incumbent position |
|-------|------------|----------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

Final count must match 16. Cross-check against TRACEABILITY AUDIT and SCHEDULE RECONCILIATION.

---

### CONTRACT COMPLIANCE AUDIT

Return to the CITATION CONTRACT in the PREAMBLE. Fill the Met? column.

| Section | Required citation form | Met? | Evidence |
|---------|----------------------|------|----------|
| PHASE 3 — chasm cause | THE INCUMBENT named in "Cause" row | [PASS / FAIL] | |
| SECTION 3 — champion network | THE INCUMBENT in every "Incumbent argument countered" cell | [PASS / FAIL] | |
| SECTION 4 — interventions | THE INCUMBENT in every "Displaces from incumbent" cell | [PASS / FAIL] | |
| SECTION 5 — churn risks | THE INCUMBENT in every "Incumbent pull" cell | [PASS / FAIL] | |
| SCHEDULE RECONCILIATION | Typed gravity format `G[N]: [exact behavior]` used for all incumbent-caused delays | [PASS / FAIL] | |
| THREE-AXIS GAP AUDIT Axis C | "THE INCUMBENT cited? = Yes" for all incumbent-caused gaps | [PASS / FAIL] | |

```
CONTRACT COMPLIANCE RESULT
Obligations met: [N] of 6
Obligations failed: [list — correct before artifact is complete]
```

---

## V-05 — Full: Output Format + Inertia Framing + Lifecycle Emphasis

**Variation axes:** Output format (V-01) + Inertia framing (V-02) + Lifecycle emphasis (V-03)

**Hypothesis:** All three R5 axes are non-overlapping and sequentially dependent in the
simulation lifecycle. V-01's CITATION CONTRACT TABLE operates at the preamble and close —
it declares which sections must cite THE INCUMBENT and verifies compliance after the fact.
V-02's typed gravity citation mandate operates at the SCHEDULE RECONCILIATION — it requires
deviation reasons to cite the exact incumbent behavior that the gravity score captured, closing
the specificity gap that generic "gravity pull" language leaves open. V-03's GRAVITY CLUSTER
IDENTIFICATION operates at PHASE 3 — it elevates the gravity cluster from a single chasm table
row into a first-class simulation step that gates PHASE 4 entry. The combination produces a
simulation with three independent accountability mechanisms: forward-declared citation
obligations (C-17), mechanically specific deviation reasoning with numeric anchors (C-18), and
a phase-gated chasm that forces the cluster to be named and unlocked explicitly before
early-majority uptake can begin (C-18 chasm row + C-09 influence dynamics). An artifact passing
all three axes simultaneously should produce C-17 PASS and C-18 PASS with high specificity,
and should generate C-09 PASS naturally through the cluster movement narrative in PHASE 4.

---

You are the adoption analyst for **{{topic}}**. Your simulation follows a structured protocol
with required output blocks. All blocks must be completed in full before advancing. Phase
Compliance Ledgers (PCL) are structural gates — correct any FAIL before writing the next phase.
Reason as the analyst throughout: where the protocol asks for a cause, give the actual cause;
where it asks for a mechanism, describe the mechanism that will actually work for this team.

Produce the artifact below in the order shown.

---

### PREAMBLE — Incumbent Declaration, Citation Contract, and Dependency Gravity Assessment

Your first task is to name THE INCUMBENT precisely, declare the citation contract, assess role
dependency depth, and identify the gravity cluster that will define the chasm in PHASE 3.

```
THE INCUMBENT:
  [Specific workflow, tool, or habit {{topic}} displaces. Name it precisely.]

What THE INCUMBENT does well for this team:
  - [Advantage 1: which cohorts rely on this and why]
  - [Advantage 2: what {{topic}} does not yet match]

What {{topic}} must prove to displace it:
  - For early majority: [specific proof point]
  - For late majority:  [specific proof point]
```

**CITATION CONTRACT**

| Section | Required citation form | Directive | Met? |
|---------|----------------------|-----------|------|
| PHASE 3 — chasm cause | "Cause" row AND "Cluster inertia" row must name THE INCUMBENT by name | MUST | [fill in CONTRACT COMPLIANCE AUDIT] |
| SECTION 3 — champion network | Every "Incumbent argument countered" cell must cite THE INCUMBENT by name | MUST | [fill in CONTRACT COMPLIANCE AUDIT] |
| SECTION 4 — interventions | Every "Displaces from incumbent" cell must cite THE INCUMBENT by name | REQUIRED | [fill in CONTRACT COMPLIANCE AUDIT] |
| SECTION 5 — churn risks | Every "Incumbent pull" cell must cite THE INCUMBENT by name | REQUIRED | [fill in CONTRACT COMPLIANCE AUDIT] |
| SCHEDULE RECONCILIATION | Typed gravity citation for incumbent-caused delays: `G[N]: [exact behavior]` | OBLIGATED | [fill in CONTRACT COMPLIANCE AUDIT] |
| THREE-AXIS GAP AUDIT Axis C | "THE INCUMBENT cited?" = Yes for all incumbent-caused gaps | REQUIRED | [fill in CONTRACT COMPLIANCE AUDIT] |

**DEPENDENCY GRAVITY ASSESSMENT**

Rate each role's daily reliance on THE INCUMBENT. Roles scoring 4 or 5 become the GRAVITY
CLUSTER IDENTIFICATION step in PHASE 3. The "Derived month range" column is filled mechanically
from the gravity score and drives SECTION 1 committed months.

Derived month range anchor: G1–G2 → M1–M2 | G3 → M3–M4 | G4 → M5–M6 | G5 → M7–M9

| Role | Gravity (1–5) | Basis: specific behavior THE INCUMBENT supports for this role | Derived month range |
|------|--------------|--------------------------------------------------------------|---------------------|
| PM | | | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

---

### SECTION 1 — Archetype Mapping and Committed Adoption Schedule

| Role | Rogers Archetype | Incumbent dependency (gravity + deviation reason if outside derived range) | Committed adoption month |
|------|-----------------|---------------------------------------------------------------------------|------------------------|
| PM | | gravity [N], derived range [X] — [reason if outside] | M[N] |
| UX | | | M[N] |
| C-01 | | | M[N] |
| C-02 | | | M[N] |
| C-03 | | | M[N] |
| C-04 | | | M[N] |
| C-05 | | | M[N] |
| C-06 | | | M[N] |
| C-07 | | | M[N] |
| C-08 | | | M[N] |
| C-09 | | | M[N] |
| C-10 | | | M[N] |
| C-11 | | | M[N] |
| C-12 | | | M[N] |
| Support | | | M[N] |
| SRE | | | M[N] |

---

### SECTION 2 — Month-by-Month Simulation

Rows addressable as `[PHASE N / Month M / Row K]`.

---

#### PHASE 1 — Innovator Ignition

**Entry state:** 0 of 16 adopted. THE INCUMBENT is fully in place.

**Month 1**

Roles committed to M1: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | [CITE: THE INCUMBENT] still holds because: [...] |

```
Cumulative: [N] of 16
```

**Month 2**

Roles committed to M2: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Innovator | | |

```
PHASE 1 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm or explain — cite gravity basis where applicable]
Incumbent position: [describe]
Signal to EA cohort: [what evidence now exists that {{topic}} works]
```

```
PHASE 1 COMPLIANCE LEDGER
C-01 (archetype mapping in SECTION 1 — all 16 rows filled): [PASS / FAIL]
C-16a (Month 1 block opened with "Roles committed to M1:"): [PASS / FAIL]
C-16b (Month 2 block opened with "Roles committed to M2:"): [PASS / FAIL]
C-16c (PHASE 1 CLOSE contains "Scheduled roles met:" field): [PASS / FAIL]
C-11 (THE INCUMBENT cited in at least one Incumbent pull cell): [PASS / FAIL]
C-17 (CITATION CONTRACT table with 6 rows and directive language present in PREAMBLE): [PASS / FAIL]
C-18 (Derived month range column filled in DEPENDENCY GRAVITY ASSESSMENT for all 16 roles): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 2.
```

---

#### PHASE 2 — Early-Adopter Spread

**Entry state:** Re-cite PHASE 1 CLOSE verbatim.

**Month 3**

Roles committed to M3: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | [CITE: THE INCUMBENT] still holds for non-adopters because: [...] |
| 2 | | | | |

```
Cumulative: [N] of 16
```

**CHAMPION FORMATION EVENT**

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role — must appear in a simulation row at or before this month]
  Bridging mechanism:        [how this role will accelerate spread to the next cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific advantage this champion counters]
```

**Month 4**

Roles committed to M4: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Adopter | | |
| 2 | | | | |

```
PHASE 2 CLOSE
Adopters: [roles, count]
Scheduled roles met: [confirm or explain — cite gravity basis where applicable]
Incumbent position: [still dominant with which cohorts?]
Champion network: [roles from CHAMPION FORMATION EVENT(s) + formation month]
Gap to EM: [what THE INCUMBENT still offers that EM cohort values — CITE: THE INCUMBENT]
```

```
PHASE 2 COMPLIANCE LEDGER
C-14 (CHAMPION FORMATION EVENT fired with all required fields): [PASS / FAIL]
C-16a-c (month blocks opened with committed-roles prompt; scheduled roles met field present): [PASS / FAIL]
C-09 (CHAMPION FORMATION EVENT "Incumbent argument targeted" is non-generic): [PASS / FAIL / N/A]
C-11 (THE INCUMBENT cited in Gap to EM): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 3.
```

---

#### PHASE 3 — Chasm

**Entry state:** Re-cite PHASE 2 CLOSE verbatim.

**GRAVITY CLUSTER IDENTIFICATION** — mandatory before the chasm table.

```
GRAVITY CLUSTER IDENTIFICATION
  Roles with gravity 4-5 (the chasm anchor cluster):
    [Role 1] — gravity [N] — [the specific THE INCUMBENT behavior they depend on from PREAMBLE]
    [Role 2] — gravity [N] — [...]
    [continue for all gravity 4-5 roles]

  Cluster size: [N] roles

  Cluster inertia effect:
    These [N] roles collectively signal to adjacent EM that [CITE: THE INCUMBENT] is still
    necessary because: [what the cluster's continued reliance communicates to observers]

  Bridge requirement for PHASE 4 entry:
    At least one of [list cluster roles] must adopt before PHASE 4 opens.
    What must be true for the first cluster role to move: [specific condition]
```

**CHASM TABLE** — derived from GRAVITY CLUSTER IDENTIFICATION.

| Element | Content |
|---------|---------|
| Gap | Between [EA roles] and the chasm anchor cluster: [name cluster roles from above] |
| Cause | [CITE: THE INCUMBENT by name] — the specific behavior the cluster depends on that {{topic}} has not yet replaced |
| Cluster inertia | [From GRAVITY CLUSTER IDENTIFICATION: why combined resistance amplifies the gap] |
| Incumbent win condition | [CITE: THE INCUMBENT] delivers [...] that {{topic}} doesn't yet match for the cluster |
| Risk if not bridged | [Roles that plateau with the cluster; THE INCUMBENT entrenches for gravity 4–5 cohort] |
| Bridge condition | [From GRAVITY CLUSTER IDENTIFICATION: what must be true for the first cluster role to move] |
| Champion | [Role from CHAMPION FORMATION EVENT + mechanism + THE INCUMBENT argument they counter for this cluster] |

```
PHASE 3 CLOSE
Bridge condition met when: [specific observable event — name the cluster role that must move first]
Incumbent position at chasm: [still dominant / weakening / differentiated]
Cluster status: [N] of [cluster size] cluster roles still on THE INCUMBENT
```

**PHASE 4 ENTRY GATE:** Phase 4 does not open until at least one gravity-4+ cluster role has
adopted. If Month 5 is reached without a cluster role adopting, record a PHASE 3 EXTENDED
stall event and explain the unlocking event before continuing.

```
PHASE 3 COMPLIANCE LEDGER
C-03 (Gap, Cause, Risk substantive and named): [PASS / FAIL]
C-11 (THE INCUMBENT named in Cause element — satisfies CITATION CONTRACT row 1): [PASS / FAIL]
C-12 (Champion element cites specific CHAMPION FORMATION EVENT role): [PASS / FAIL]
C-17 (CITATION CONTRACT row 1 obligation being tracked): [PASS / FAIL]
C-18 (GRAVITY CLUSTER IDENTIFICATION block completed with bridge requirement): [PASS / FAIL]
PHASE 4 GATE (at least one gravity-4+ role committed to M5 or earlier, or PHASE 3 EXTENDED recorded): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 4.
```

---

#### PHASE 4 — Early-Majority Uptake

**Entry state:** Re-cite PHASE 3 CLOSE verbatim.
PHASE 4 ENTRY GATE cleared: [name the first gravity-4+ role that adopted and their simulation month].

**Month 5**

Roles committed to M5: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
Cumulative: [N] of 16
Cluster progress: [N] of [cluster size] gravity-4+ roles now adopted
Churn risk?: [role + gravity score + trigger; what [CITE: THE INCUMBENT] behavior reasserts]
```

**CHAMPION FORMATION EVENT** (if new champion; else "No new champion this phase")

```
CHAMPION FORMATION EVENT
  Formation month:           Month [N]
  Role becoming champion:    [role]
  Bridging mechanism:        [mechanism toward Late Majority cohort]
  Incumbent argument targeted: [CITE: THE INCUMBENT — specific argument]
```

**Month 6**

Roles committed to M6: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Early Majority | | |
| 2 | | | | |

```
PHASE 4 CLOSE
Adopters: [roles, count, %]
Scheduled roles met: [confirm or explain — cite gravity basis where applicable]
Cluster adoption progress: [N] of [cluster size] gravity-4+ roles adopted
Incumbent position: [retreating / residual / eliminated in this cohort]
```

```
PHASE 4 COMPLIANCE LEDGER
C-14 (CHAMPION FORMATION EVENT fired or "No new champion this phase"): [PASS / FAIL]
C-16a-c (month blocks opened with committed-roles prompt; scheduled roles met present): [PASS / FAIL]
C-18 (Cluster progress field shows numeric count vs cluster size): [PASS / FAIL]

If any item is FAIL: correct before writing PHASE 5.
```

---

#### PHASE 5 — Late-Majority Close

**Entry state:** Re-cite PHASE 4 CLOSE verbatim.

**Month 7–9**

Roles committed to M7–M9: [list from SECTION 1]

| Row | Newly adopting role | Archetype | Adoption trigger | Incumbent pull |
|-----|---------------------|-----------|-----------------|---------------|
| 1 | | Late Majority / Laggard | | |
| 2 | | | | |

```
PHASE 5 CLOSE
Final adopters: [N] of 16 ([%])
Cluster final status: [N] of [cluster size] gravity-4+ roles adopted; [N] remain on THE INCUMBENT
Non-adopters (if any): [roles; gravity score; reason THE INCUMBENT still wins]
Incumbent final position: [fully displaced / residual / niche survival]
```

**SCHEDULE RECONCILIATION**

**TYPED GRAVITY CITATION RULE:** Incumbent-caused delays MUST use:
`G[N]: [exact behavior THE INCUMBENT had for this role that the gravity score captured]`
Generic forms are structurally rejected.

| Role | Gravity | Committed month | Actual month | Status |
|------|---------|----------------|-------------|--------|
| PM | | | | On schedule / Delayed [N months] — G[N]: [exact incumbent behavior for this role] / Non-adopter |
| UX | | | | |
| C-01 | | | | |
| C-02 | | | | |
| C-03 | | | | |
| C-04 | | | | |
| C-05 | | | | |
| C-06 | | | | |
| C-07 | | | | |
| C-08 | | | | |
| C-09 | | | | |
| C-10 | | | | |
| C-11 | | | | |
| C-12 | | | | |
| Support | | | | |
| SRE | | | | |

```
SCHEDULE RECONCILIATION RESULT
On schedule: [N] of 16
Delayed: [N] — [list; each delay uses typed format G[N]: [exact behavior]]
Non-adopters: [list with gravity scores]
Gravity accuracy check: [did gravity-4+ cluster roles adopt in M5-M9 as derived ranges predicted?]
Typed citation check: [any generic language? List and correct.]
```

---

### TRACEABILITY AUDIT

| Role | Adoption month | Archetype cohort | Row Citation |
|------|---------------|-----------------|--------------|
| PM | | | |
| UX | | | |
| C-01 | | | |
| C-02 | | | |
| C-03 | | | |
| C-04 | | | |
| C-05 | | | |
| C-06 | | | |
| C-07 | | | |
| C-08 | | | |
| C-09 | | | |
| C-10 | | | |
| C-11 | | | |
| C-12 | | | |
| Support | | | |
| SRE | | | |

```
TRACEABILITY AUDIT RESULT
All 16 roles cited: [PASS / FAIL]
Cross-check with SCHEDULE RECONCILIATION: [consistent / discrepancies]
```

---

### THREE-AXIS GAP AUDIT

#### Axis A — Role Completeness

| Role | Adoption month | Archetype cohort | Source |
|------|---------------|-----------------|--------|
| PM | | | |
| UX | | | |
| C-01 through C-12 | | | |
| Support | | | |
| SRE | | | |

#### Axis B — Temporal Completeness

| Event | Month pinned | Type | Source section |
|-------|-------------|------|---------------|
| | | Adoption / Stall / Chasm / Bridge / Intervention | |

#### Axis C — Causal Specificity

| Gap / Risk / Stall | Named cause (non-generic) | THE INCUMBENT cited? | Source section |
|--------------------|--------------------------|---------------------|---------------|
| | | Yes / No | |

```
THREE-AXIS GAP AUDIT RESULT
Axis A: [PASS / FAIL]
Axis B: [PASS / FAIL]
Axis C: [PASS / FAIL]
```

---

### SECTION 3 — Champion Network

**Derivation rule:** Every champion row must have a corresponding CHAMPION FORMATION EVENT.
Cluster roles that became champions must note their gravity score.

| Champion role | Bridges from | Bridges to | Bridging mechanism | Incumbent argument countered | Formation phase/month | Influence type |
|--------------|-------------|------------|-------------------|------------------------------|-----------------------|---------------|
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |
| | | | | [CITE: THE INCUMBENT] — specific argument | PHASE N / Month M | Active / Passive |

### SECTION 4 — Intervention Recommendations

Sorted by adoption delta, highest first. Minimum 3 interventions.

| Rank | Intervention | Target roles | Displaces from incumbent | Adoption delta | Deploy before month |
|------|-------------|-------------|--------------------------|---------------|-------------------|
| 1 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 2 | | | [CITE: THE INCUMBENT] — [habit] | | |
| 3 | | | [CITE: THE INCUMBENT] — [habit] | | |

### SECTION 5 — Churn Risk Register

Minimum 2 entries. Incumbent pull must cite THE INCUMBENT by name.

| Role | Archetype | Gravity | Churn trigger | Incumbent pull | Intervention to retain |
|------|-----------|---------|--------------|---------------|----------------------|
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |
| | | | | [CITE: THE INCUMBENT] still offers: [...] | |

### SECTION 6 — S-Curve Summary

| Phase | Month range | Adopters | % of 16 | Incumbent position |
|-------|------------|----------|---------|-------------------|
| Innovator ignition | | | | Fully in place |
| Early-adopter spread | | | | Losing early users |
| Chasm (stall) | | | | Dominant with EM+ |
| Early-majority uptake | | | | Contested |
| Late-majority close | | | | [Displaced / Residual] |

Final count must match 16. Gravity cluster final outcome: [N] of [cluster size] adopted;
explain any cluster roles that remain on THE INCUMBENT.
Cross-check against TRACEABILITY AUDIT and SCHEDULE RECONCILIATION.

---

### CONTRACT COMPLIANCE AUDIT

Return to the CITATION CONTRACT in the PREAMBLE. Fill the Met? column for every row.

| Section | Required citation form | Met? | Evidence (field or cell that satisfies / violates) |
|---------|----------------------|------|---------------------------------------------------|
| PHASE 3 — chasm cause + cluster inertia | THE INCUMBENT named in "Cause" row and "Cluster inertia" row | [PASS / FAIL] | |
| SECTION 3 — champion network | THE INCUMBENT in every "Incumbent argument countered" cell | [PASS / FAIL] | |
| SECTION 4 — interventions | THE INCUMBENT in every "Displaces from incumbent" cell | [PASS / FAIL] | |
| SECTION 5 — churn risks | THE INCUMBENT in every "Incumbent pull" cell | [PASS / FAIL] | |
| SCHEDULE RECONCILIATION | Typed format `G[N]: [exact behavior]` for all incumbent-caused delays | [PASS / FAIL] | |
| THREE-AXIS GAP AUDIT Axis C | "THE INCUMBENT cited? = Yes" for all incumbent-caused gaps | [PASS / FAIL] | |

```
CONTRACT COMPLIANCE RESULT
Obligations met: [N] of 6
Obligations failed: [list — correct before artifact is complete]
```

If any obligation failed: correct the relevant section and re-verify before submitting.
