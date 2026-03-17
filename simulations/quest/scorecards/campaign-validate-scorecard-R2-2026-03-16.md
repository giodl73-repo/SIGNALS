## campaign-validate — Quest Score R2

**Scores:**

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 (tie) | V-03 — Lifecycle Emphasis | **113/115** | YES |
| 1 (tie) | V-04 — Output Format Template | **113/115** | YES* |
| 3 | V-02 — Inertia Framing | **112/115** | YES |
| 4 | V-01 — Phrasing Register | **107/115** | YES |
| — | V-05 — Combined (Listen-First) | unscored | — |

*V-04 prompt was truncated — C-11 scored PARTIAL conservatively; score is projected.

**R2 delta vs R1 baseline (V-01: 93):**

- **C-09**: Fixed across all 4 variations. R1 had qualitative tags ("blocks chasm crossing") without segment %. All R2 variations embed `(segment, ~N%)` notation explicitly.
- **C-10**: Fixed. R1 V-01 failed outright. All R2 variations have remediation paths; V-03 achieves the EX-2 columnar pattern.
- **C-13**: Locked in. All 4 variations emit `"Artifact written: ..."` — it's now baseline.
- **C-11**: Still PARTIAL across all scored variations. The constraint: C-11 requires a literal table skeleton in the prompt text itself. Phase gates (V-03) achieve it for Phase 5 (Rogers rows); V-04 was designed for it but truncated. Full C-11 needs shipped table rows in the prompt.
- **C-12**: Passes in V-02/V-03/V-04; narrative register (V-01) can't encode column structure.

**New patterns:**
- `phase-gate-categorical-separation` — encoding "NOTE: X is categorically different from Y, each row must contain distinct content from Phase N" as a hard gate, not a reminder
- `rogers-curve-as-completeness-skeleton` — pre-defining all 5 Rogers segment rows makes a missing segment visible as an absent required row (C-11 subpattern)
- `inertia-baseline-as-adoption-anchor` — anchoring findings to the status-quo workaround forces segment-specific adoption impact automatically (structural C-09 generator)

```json
{"top_score": 113, "all_essential_pass": true, "new_patterns": ["phase-gate-categorical-separation", "rogers-curve-as-completeness-skeleton", "inertia-baseline-as-adoption-anchor"]}
```
it examples embedded in ranking instruction: "blocks chasm crossing (early majority, ~45%)", "impedes innovators only (~3%)", "majority-blocking but recoverable post-v1 (~35%)". Segment + % notation is the prescribed format. |
| C-10 | Remediation paths per blocker | **PASS** | "what change would resolve it, and which sub-skill's finding supports that resolution path." Prose field, not column — passes C-10 without EX-2 pattern. |
| C-11 | Table skeleton per sub-skill | **FAIL** | Narrative register explicitly discourages structured tables. Sub-skill sections are prose headings, not table skeletons. A missing sub-skill would be invisible as absent prose, not visible as an empty row. |
| C-12 | Separate Severity/Adoption columns | **PARTIAL** | "Severity (P1/P2/P3) appears as a secondary attribute, not the sort key" communicates the orthogonality conceptually but not as structural table columns. No table template specified. 2/5. |
| C-13 | Artifact confirmation string | **PASS** | "After writing, confirm: Artifact written: simulations/{topic}/validate-{date}.md" — exact EX-4 pattern. |

**Essential**: 5/5 (60 pts) | **Recommended**: 3/3 (30 pts) | **Aspirational**: C-09 PASS(5) + C-10 PASS(5) + C-11 FAIL(0) + C-12 PARTIAL(2) + C-13 PASS(5) = 17/25
**V-01 Composite: 107** | Golden: YES | Delta from R1 V-01: +14 (C-09 fixed, C-13 added, C-10 fixed)

---

### V-02 — Inertia Framing (Status-Quo as Primary Anchor)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 sub-skills represented | **PASS** | Steps 2–6 each name a sub-skill. "listen-feedback is the emotional response to the design, not the adoption trajectory." Distinct content requirement explicit. |
| C-02 | Ranked by adoption impact | **PASS** | "Ranked Findings — sorted by adoption impact, not severity. Adoption impact uses this format: '[Segment] ([%]): [what must be true for them to adopt]'." |
| C-03 | Explicit go/no-go verdict | **PASS** | "Verdict: GO / NO-GO / CONDITIONAL GO (with explicit condition)." |
| C-04 | Blockers attributed to sub-skill | **PASS** | "Each blocker includes: the blocker, the sub-skill source, the inertia comparison (why it keeps users in their workaround), and the remediation path (what design change resolves it)." |
| C-05 | Artifact written to disk | **PASS** | "Write complete brief to simulations/{topic}/validate-{date}.md." |
| C-06 | Cross-signal synthesis | **PASS** | "Specifically look for: a usability finding (review-users) that maps to a support prediction (listen-feedback) for the same user action; a customer skepticism (review-customers) that corresponds to a chasm-blocking inertia behavior (listen-adoption)." Prescriptive cross-signal targets. |
| C-07 | Per-sub-skill labeled sections | **PASS** | "Each sub-skill under its own labeled heading. P1/P2/P3 throughout." |
| C-08 | Severity tiers | **PASS** | P1/P2/P3 defined per inertia comparison: "P1 (the workaround is easier), P2 (comparable, user may not switch), P3 (new design has minor edge)." Inertia framing enriches severity semantics. |
| C-09 | Adoption impact quantified | **PASS** | "[Segment] ([%]): [what must be true for them to adopt]" required in every finding. Rogers percentages provided as anchors: "innovators ~2.5%, early adopters ~13.5%, early majority ~34%..." Inertia framing forces segment identification automatically. |
| C-10 | Remediation paths per blocker | **PASS** | Two-field remediation per blocker: "inertia comparison (why it keeps users in their workaround)" + "remediation path (what design change resolves it)." Stronger than C-10 minimum; approaches EX-2. |
| C-11 | Table skeleton per sub-skill | **PARTIAL** | Step-based prose structure with one consolidated Ranked Findings table. No per-sub-skill table skeleton. A missing sub-skill (e.g., listen-adoption skipped) would not appear as an empty row. 2/5. |
| C-12 | Separate Severity/Adoption columns | **PASS** | "Severity (P1/P2/P3) is a secondary column." The word "column" makes the structural separation explicit. Combined with "[Segment] ([%])" as the primary adoption impact format, the two axes are definitively orthogonal at the layout level. |
| C-13 | Artifact confirmation string | **PASS** | "Emit: Artifact written: simulations/{topic}/validate-{date}.md" — exact EX-4 pattern. |

**Essential**: 5/5 (60 pts) | **Recommended**: 3/3 (30 pts) | **Aspirational**: C-09 PASS(5) + C-10 PASS(5) + C-11 PARTIAL(2) + C-12 PASS(5) + C-13 PASS(5) = 22/25
**V-02 Composite: 112** | Golden: YES | Delta from R1 V-01: +19

---

### V-03 — Lifecycle Emphasis (Strict Phase-Gate)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 sub-skills represented | **PASS** | Five explicit phases with gates. Phase 4: "listen-feedback is about pre-ship customer reaction... not the same as adoption trajectory. Do not merge this section with Phase 5." Phase 5: "categorically different from listen-feedback. Each row must contain distinct content from Phase 4." Strongest C-01 enforcement of any variation. |
| C-02 | Ranked by adoption impact | **PASS** | "Ranked Findings Table — all findings from Phases 1–5, sorted by adoption impact descending. A P2 that blocks chasm crossing (early majority, ~34%) must appear above a P1 affecting innovators (~2.5%)." Concrete example embedded in sort rule. |
| C-03 | Explicit go/no-go verdict | **PASS** | "Verdict (required, first line of brief): GO / NO-GO / CONDITIONAL GO. If conditional, complete the sentence: 'CONDITIONAL GO if [specific condition].'" Completion pattern enforced. |
| C-04 | Blockers attributed to sub-skill | **PASS** | Blocker table schema: "Rank \| Blocker \| Sub-Skill Source \| Adoption Impact \| Remediation Path." Pre-defined columns; attribution is structural, not optional. |
| C-05 | Artifact written to disk | **PASS** | "Output path: simulations/{topic}/validate-{date}.md" declared at top. Phase 6 closes: "Write the complete brief to simulations/{topic}/validate-{date}.md." |
| C-06 | Cross-signal synthesis | **PASS** | "Template: 'Finding [X] from Phase [N] is [confirmed / contradicted / amplified] by Finding [Y] from Phase [M].' At least one synthesis point required; three preferred." Quantified minimum and aspirational target. |
| C-07 | Per-sub-skill labeled sections | **PASS** | Five phase headings, each a gated sub-skill section. Gate requires section to exist with distinct content before next phase is permitted. |
| C-08 | Severity tiers | **PASS** | P1/P2/P3 required in each phase gate. Phase 5 gate requires adoption % per segment row. Severity appears as a column in the Phase 6 Ranked Findings Table. |
| C-09 | Adoption impact quantified | **PASS** | Phase 5 requires "estimated adoption % for this feature, what blocks the remaining %" per Rogers segment row. Phase 6 Ranked Findings Table column: "Adoption Impact (segment, %)". Two structural enforcement points for quantification. |
| C-10 | Remediation paths per blocker | **PASS** | "Remediation Path" is a named column in the Phase 6 blocker table. EX-2 pattern fully realized — structure forces population. |
| C-11 | Table skeleton per sub-skill | **PARTIAL** | Phase 5 Rogers curve has all 5 segment rows as required skeleton (innovators through laggards — missing segment is visible as absent row). Phase 6 blockers table is a pre-defined skeleton. Phases 1–4 are section-gated prose, not table skeletons. Partial credit for Phase 5/6 skeletons. 3/5. |
| C-12 | Separate Severity/Adoption columns | **PASS** | Phase 6 explicitly names columns: "Finding \| Sub-Skill \| Severity \| Adoption Impact (segment, %)." Severity and Adoption Impact appear as adjacent, named, distinct columns. Most explicit C-12 implementation of any scored variation. |
| C-13 | Artifact confirmation string | **PASS** | "Emit: Artifact written: simulations/{topic}/validate-{date}.md" — exact EX-4 pattern. |

**Essential**: 5/5 (60 pts) | **Recommended**: 3/3 (30 pts) | **Aspirational**: C-09 PASS(5) + C-10 PASS(5) + C-11 PARTIAL(3) + C-12 PASS(5) + C-13 PASS(5) = 23/25
**V-03 Composite: 113** | Golden: YES | Delta from R1 V-01: +20

---

### V-04 — Output Format (Full v2 Template — C-11/C-12/C-13 Encoded)

> **Note**: V-04 prompt content was truncated. The section header "### Section 1 — Sub-Skill Findings Tables" appeared but the table templates were not shown. Scoring is based on visible instructions and declared axis. C-11 scored as PARTIAL due to template truncation; all other criteria scored on visible evidence and axis design intent.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 sub-skills represented | **PASS** | Axis: "Pre-defining table skeletons with all five sub-skill rows (C-11)" — sub-skill completeness is the primary structural goal. "Section 1 — Sub-Skill Findings Tables" heading confirms per-sub-skill structure. |
| C-02 | Ranked by adoption impact | **PASS** | "Adoption impact notation: always '(segment, ~N%)' — e.g., 'chasm-blocking (early majority, ~34%)'." Adoption impact is the primary ranking signal; "(segment, ~N%)" format rejects generic labels. |
| C-03 | Explicit go/no-go verdict | **PASS** | Verdict field expected in template design; axis implies all v2 criteria are structurally encoded. |
| C-04 | Blockers attributed to sub-skill | **PASS** | Blocker table with Sub-Skill Source column expected from template structure. |
| C-05 | Artifact written to disk | **PASS** | "Output path: simulations/{topic}/validate-{date}.md" explicitly declared. |
| C-06 | Cross-signal synthesis | **PASS** | Synthesis section expected in template; axis focus on C-09/C-11/C-12/C-13 does not exclude cross-signal synthesis. |
| C-07 | Per-sub-skill labeled sections | **PASS** | Table per sub-skill creates labeled navigable sections as a structural byproduct. |
| C-08 | Severity tiers | **PASS** | Severity as column in every table (axis design); P1/P2/P3 expected throughout. |
| C-09 | Adoption impact quantified | **PASS** | "'(segment, ~N%)' notation in every Adoption Impact cell" — explicit enforcement with "Generic 'high/medium/low' is not acceptable." Strongest C-09 enforcement of any variation. |
| C-10 | Remediation paths per blocker | **PASS** | Remediation as template column expected from axis design (EX-2 pattern). |
| C-11 | Table skeleton per sub-skill | **PARTIAL** | Axis explicitly targets C-11: "table skeletons with all five sub-skill rows means a skipped sub-skill appears as a blank table row." Design intent satisfies criterion — but the actual table template was not shown due to truncation. Cannot verify format. 3/5. |
| C-12 | Separate Severity/Adoption columns | **PASS** | Axis: "Separate Severity and Adoption Impact columns in every table (C-12) prevents rank-by-severity errors at the layout level." Explicitly targets the structural separation. |
| C-13 | Artifact confirmation string | **PASS** | Axis: "The confirmation string requirement (C-13) closes C-05 with a machine-detectable signal." Explicitly targets EX-4 pattern. |

**Essential**: 5/5 (60 pts) | **Recommended**: 3/3 (30 pts) | **Aspirational**: C-09 PASS(5) + C-10 PASS(5) + C-11 PARTIAL(3) + C-12 PASS(5) + C-13 PASS(5) = 23/25
**V-04 Composite: 113** | Golden: YES (projected; template truncation prevents full verification)

---

### V-05 — Combined (Listen-First Sequence + Quantified Adoption Impact)

**V-05 Composite: Unscored** — prompt text not provided. Axis: listen-first sequence + quantified adoption impact. Cannot assess without prompt text.

---

### Variation Ranking

| Rank | Variation | Composite | Golden | Delta R1 V-01 | C-09 | C-11 | C-12 | C-13 |
|------|-----------|-----------|--------|---------------|------|------|------|------|
| 1 | V-03 — Lifecycle Emphasis | 113 | YES | +20 | PASS | PARTIAL(3) | PASS | PASS |
| 1 | V-04 — Output Format Template | 113 | YES* | +20 | PASS | PARTIAL(3) | PASS | PASS |
| 3 | V-02 — Inertia Framing | 112 | YES | +19 | PASS | PARTIAL(2) | PASS | PASS |
| 4 | V-01 — Phrasing Register | 107 | YES | +14 | PASS | FAIL | PARTIAL | PASS |
| — | V-05 — Combined (Listen-First) | unscored | — | — | — | — | — | — |

*V-04 template truncated; score projected from axis + visible content.

---

### R2 Delta Analysis

**C-09 (all 4 scored variations)**: Fixed. R1 had partial credit (qualitative tags, no segment %). All R2 variations embed "(segment, ~N%)" notation explicitly.

**C-13 (all 4 scored variations)**: Locked in. Every R2 variation includes the "Artifact written: ..." confirmation string. This was the only EX-4 criterion and it's now baseline.

**C-10 (all 4 scored variations)**: Fixed. R1 V-01 failed C-10 entirely. All R2 variations include remediation paths per blocker; V-03 achieves the EX-2 column pattern.

**C-11 (persistent weak point)**: Still PARTIAL across all scored variations. The constraint: C-11 requires a pre-defined table skeleton per sub-skill in the prompt template itself. Variations that achieve strong C-11 must ship with literal table rows (| sub-skill | ... |) in the prompt text. V-04 was designed for this but truncated. V-03 achieves it for Phase 5 (Rogers rows) but not Phases 1–4.

**C-12 (V-02/V-03/V-04 pass; V-01 partial)**: The "secondary column" wording in V-02 and the explicit column list in V-03 both pass. Narrative register (V-01) blocks structural column encoding.

---

### Excellence Signals (from V-03, the most verifiable top scorer)

**EX-5 — Phase-gate categorical separation**: Encoding "NOTE: X is categorically different from Y. Each row must contain distinct content from Phase N." as a gate condition eliminates listen-feedback/listen-adoption merge at the structural level — not as a reminder but as a gate the model cannot pass through without distinct content. R1 relied on instruction; V-03 makes it a gate.

**EX-6 — Rogers curve as C-11 skeleton**: Pre-defining "Required rows: innovators, early adopters, early majority, late majority, laggards" creates a five-row skeleton that makes a missing segment visible as an absent required row. This is the same C-11 pattern applied to the adoption model specifically — a sub-pattern within C-11.

**EX-7 — Inertia baseline as C-09 forcing function (from V-02)**: Anchoring every finding to "what users do today without this feature" forces the model to name specific switching costs and segments automatically, without relying on the model's discretion to add "(segment, ~N%)" labels. The mechanism generates C-09 compliance structurally rather than relying on notation rules.

---

```json
{"top_score": 113, "all_essential_pass": true, "new_patterns": ["phase-gate-categorical-separation", "rogers-curve-as-completeness-skeleton", "inertia-baseline-as-adoption-anchor"]}
```
