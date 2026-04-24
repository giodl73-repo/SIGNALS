Reading the scorecard carefully to extract the three new patterns before writing.

The three new patterns from V-05:
- **criterion-cascade-by-schema** → C-17
- **required-columns-as-inertia-enforcement** → C-18
- **pre-declared-rows-as-completeness-gate** → C-19

Aspirational expands from 8 criteria (40 pts) to 11 criteria (55 pts). Max moves from 130 to 145. Golden threshold stays at 80.

---

# campaign-validate Rubric — v4

> Updated after R3 scoring (V-01: 90, V-02: 103, V-03: 97, V-04: 95, V-05: 125). Three new
> aspirational criteria added from R3 excellence patterns: criterion-cascade-by-schema (C-17),
> required-columns-as-inertia-enforcement (C-18), pre-declared-rows-as-completeness-gate (C-19).

---

## Quick Reference

**5 essential** (all must pass for golden):
- **C-01** — All 5 sub-skills represented. Common failure: listen-adoption silently skipped.
- **C-02** — Findings ranked by *adoption impact*, not severity.
- **C-03** — Explicit go/no-go verdict. "It depends" without a condition fails.
- **C-04** — Top 3 blockers attributed to source sub-skill (trivially passes on go verdicts).
- **C-05** — Artifact written to `simulations/{topic}/validate-{date}.md`.

**3 recommended** (needed to reach composite >= 80):
- **C-06** — Cross-signal synthesis. Concatenation fails.
- **C-07** — Per-sub-skill labeled sections.
- **C-08** — Severity tiers (P1/P2/P3), not flat list.

**11 aspirational** (5 pts each):
- **C-09** — Adoption impact quantified: `(segment, ~N%)` format.
- **C-10** — Remediation paths per blocker.
- **C-11** *(v2)* — Table skeleton per sub-skill as completeness gate.
- **C-12** *(v2)* — Adoption Impact as dedicated column, separate from Severity.
- **C-13** *(v2)* — `Artifact written: ...` confirmation string.
- **C-14** *(v3)* — Categorical separation declared for listen-feedback vs listen-adoption.
- **C-15** *(v3)* — All five Rogers segments named with % anchors.
- **C-16** *(v3)* — Status-quo workaround cited per blocker.
- **C-17** *(v4)* — Schema designed so one decision satisfies a criterion cluster.
- **C-18** *(v4)* — Switching-cost comparison encoded as required columns, not prose.
- **C-19** *(v4)* — Required rows pre-declared so absent content is a visible blank, not missing prose.

**Max: 145. Golden: all essential pass + composite >= 80.**

---

## What changed in v4

| ID | Pattern | What it encodes |
|----|---------|-----------------|
| C-17 | `criterion-cascade-by-schema` | The table schema is designed so a single structural choice satisfies a cluster of criteria simultaneously. Example: pre-declaring Rogers rows in Table 5 causes C-09 (% per segment), C-14 (listen-adoption as distinct section), and C-15 (all five named segments) to pass by construction. Adding Status-Quo Workaround and Switching Cost columns causes C-16 and C-09 to cascade-pass. Criterion clusters, not single checks, are the unit of schema design. |
| C-18 | `required-columns-as-inertia-enforcement` | "Status-Quo Workaround" and "Switching Cost" are encoded as required table columns, not prose instructions. This makes the switching-cost comparison systematic across all blockers simultaneously — every row must have a workaround, not just the blockers where the author remembered one. The column also makes workaround data machine-readable and enables cross-blocker inertia analysis that prose cannot surface. |
| C-19 | `pre-declared-rows-as-completeness-gate` | Required entries (Rogers segments, sub-skills, severity tiers) are pre-declared as named rows in the table skeleton, not left as prose to fill in. A missing entry appears as a visually detectable blank mandatory row rather than as absent text. Generalizes C-11's table-skeleton pattern: the skeleton applies to *rows* as well as *tables*. Missing row = missing required output, detectable without reading prose. |

**Scoring model** updated: aspirational expands from 40 pts (8 criteria) to 55 pts (11 criteria), max composite moves from 130 to 145. Golden threshold unchanged at 80. V-05 top-pattern example (125/130 on the v3 scale) added to pass/fail table.

---

## Essential Criteria (weight: 12 points each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | All 5 sub-skills represented | completeness | Output contains explicit findings or a confirmed-empty section for all five sub-skills: review-design, review-users, listen-feedback, listen-adoption, review-code. Silent omission of any sub-skill — especially listen-adoption — fails unconditionally. |
| C-02 | Findings ranked by adoption impact | ranking | The ranked findings list orders items by estimated adoption impact, not by severity or effort. A finding that blocks the early majority outranks a P1 usability issue that affects only innovators. Severity may be noted but must not govern rank order. |
| C-03 | Explicit go/no-go verdict | verdict | Output contains an unambiguous go or no-go verdict for the feature. A conditional verdict ("go if X is fixed") passes only if the condition is specific and actionable. "It depends" without a named condition fails. |
| C-04 | Top blockers attributed to source sub-skill | attribution | The top 3 blockers (or all blockers if fewer than 3) are each attributed to the sub-skill that surfaced them. If verdict is go, this criterion passes trivially. |
| C-05 | Artifact written to disk | behavior | Output is written to `simulations/{topic}/validate-{date}.md` following the signal artifact naming convention. File must exist after skill run. |

---

## Recommended Criteria (weight: 10 points each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Cross-signal synthesis | depth | Brief identifies at least one pattern or tension appearing across 2+ sub-skills (e.g., a usability finding from review-users confirmed by a support-ticket prediction from listen-feedback). Not just a concatenation of sub-skill outputs. |
| C-07 | Per-sub-skill labeled sections | format | Each sub-skill's findings appear under a clearly labeled heading. Reader can navigate directly to review-design findings, listen-adoption findings, etc. without reading the whole document. |
| C-08 | Finding severity differentiation | depth | Findings use consistent severity tiers (P1/P2/P3, blocking/major/minor, or equivalent). High-severity findings visually distinct from low-severity. Not a flat undifferentiated list. |

---

## Aspirational Criteria (weight: 5 points each)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Adoption impact quantified per finding | depth | Each ranked finding includes an estimated adoption impact magnitude with segment and %. Format: `(segment, ~N%)` — e.g., "blocks chasm crossing (early majority, ~34%)", "impedes innovators only (~2.5%)". Generic labels ("high impact", "most users") without segment identity and % fail. |
| C-10 | Remediation paths for top blockers | depth | Each top blocker includes a concrete remediation suggestion pointing to a design decision the team can make. Not just "fix this" — specifies what change would resolve the blocker and which sub-skill result supports it. |
| C-11 | Table skeleton per sub-skill as completeness gate | format | Each sub-skill's findings are presented in a structured table (not prose), so that a missing sub-skill appears as an empty table rather than invisible absent text. The table skeleton is present even if the sub-skill found nothing — making omission detectable, not silent. |
| C-12 | Adoption Impact as dedicated column separate from Severity | format | Severity and Adoption Impact appear as distinct columns or fields in the findings output. A finding can be P3 severity and high adoption impact; the two axes are never merged. This structural separation prevents rank-by-severity errors at the layout level. |
| C-13 | Explicit artifact confirmation string | behavior | After writing the artifact, the skill emits a confirmation line: "Artifact written: simulations/{topic}/validate-{date}.md". The confirmation string is machine-detectable, closing the C-05 verification loop with a positive signal rather than relying on absence of error. |
| C-14 | Categorical separation declared for listen-feedback vs listen-adoption | completeness | Output explicitly declares the categorical distinction between listen-feedback and listen-adoption — not just labels them separately, but names what each covers: listen-feedback as pre-ship customer reaction to the design; listen-adoption as post-ship adoption trajectory by segment. The declaration appears as a structural marker (heading note, gate annotation, or explicit statement) before or at the top of the relevant sections. A merged or unlabeled combined section fails unconditionally. |
| C-15 | All five Rogers segments enumerated by name with % anchors | depth | The adoption analysis (listen-adoption findings) enumerates all five Rogers diffusion segments as named distinct entries: innovators (~2.5%), early adopters (~13.5%), early majority (~34%), late majority (~34%), laggards (~16%). A segment absent from the output is detectable as a missing required entry, not invisible as absent prose. Approximate percentage ranges must be cited — a segment named without a % anchor fails. |
| C-16 | Status-quo workaround cited per blocker | depth | Each top blocker includes a reference to the specific workaround users employ today in the absence of this feature — what keeps them at rest. The citation names the behavior and the switching cost: "Users today do X; this feature asks them to give up X because Y." Generic "users have workarounds" without naming the workaround and cost fails. Inertia is zero without a named status-quo anchor. |
| C-17 | Schema designed as criterion-cluster trigger | format | The table schema is designed so that declaring a single structural element (a column type, a row set) causes a *cluster* of criteria to pass by construction — not a single check. Evidence: the schema design rationale, or the observed cascade of passes, must be traceable to a deliberate schema choice. An output that happens to satisfy multiple criteria through independent prose does not pass — the schema must be the forcing function. |
| C-18 | Switching-cost comparison encoded as required columns | depth | "Status-Quo Workaround" and "Switching Cost" (or equivalents) appear as named required columns in the Top Blockers table — not as prose guidance. Every row must supply both fields. An output that mentions workarounds narratively in some rows but not others, or embeds them in a Notes column, fails. The column structure must make per-blocker workaround citation systematic and machine-readable. |
| C-19 | Required entries pre-declared as named rows | format | Entries that are required by the rubric (Rogers segments, sub-skill sections, severity tiers, or equivalent) are pre-declared as named rows in the table skeleton before content is filled in. An absent required entry must appear as a visually detectable blank row — not as missing prose. Generalizes C-11: the skeleton applies to row identity, not just table existence. A table with no pre-declared rows, even if it has correct columns, does not pass. |

---

## Scoring Summary

| Tier | Criteria | Points each | Max |
|------|----------|-------------|-----|
| Essential (C-01–C-05) | 5 | 12 | 60 |
| Recommended (C-06–C-08) | 3 | 10 | 30 |
| Aspirational (C-09–C-19) | 11 | 5 | 55 |
| **Total** | | | **145** |

PASS = full, PARTIAL = half, FAIL = 0. Golden requires all essential PASS + composite >= 80.

---

## Version History

| Version | Trigger | New Criteria | Max |
|---------|---------|--------------|-----|
| v1 | Baseline | C-01–C-10 | 115 |
| v2 | R2 aspirational patterns | C-11 (table skeleton), C-12 (column separation), C-13 (confirmation string) | 115 |
| v3 | R2 excellence patterns | C-14 (categorical separation), C-15 (Rogers segments), C-16 (inertia baseline) | 130 |
| v4 | R3 excellence patterns | C-17 (criterion-cascade-by-schema), C-18 (required-columns-as-inertia-enforcement), C-19 (pre-declared-rows-as-completeness-gate) | 145 |
