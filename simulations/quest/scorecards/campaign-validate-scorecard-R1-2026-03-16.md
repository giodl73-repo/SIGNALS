## campaign-validate — Quest Score R1

---

### V-01 — Role Sequence

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 sub-skills represented | **PASS** | Phase 1 = listen-adoption, Phase 2 = review-users + listen-feedback, Phase 3 = review-design + review-customers. All 5 explicitly labeled. |
| C-02 | Ranked by adoption impact | **PASS** | Phase 5: "sorted by adoption impact (not severity). P1 findings that block chasm crossing rank above P2." Explicit distinction from severity sort. |
| C-03 | Explicit go/no-go verdict | **PASS** | Requires one of GO / NO-GO / CONDITIONAL GO. "Do not write 'it depends' without naming the condition." |
| C-04 | Blockers attributed to sub-skill | **PASS** | "1. [Blocker] — source: [sub-skill]" format mandated for top 3. |
| C-05 | Artifact written to disk | **PASS** | Output path declared at top; final phase says "Write the complete brief to simulations/{topic}/validate-{date}.md." |
| C-06 | Cross-signal synthesis | **PASS** | Phase 4 is a dedicated synthesis phase, requires at least one cross-sub-skill pattern with format: "Finding X (surfaced by Y) is confirmed/contradicted by Z (surfaced by W)." |
| C-07 | Per-sub-skill labeled sections | **PASS** | Each of the 5 sub-skills gets a named `##` heading. |
| C-08 | Severity tiers | **PASS** | P1/P2/P3 used throughout with definitions per phase. |
| C-09 | Adoption impact quantified | **PARTIAL** | Tags present ("blocks chasm crossing", "impedes majority adoption") but qualitative — no segment percentages or specificity matching the criterion's examples. |
| C-10 | Remediation paths per blocker | **FAIL** | Top Blockers section lists blocker + source only. No remediation column or field. |

**Essential**: 5/5 (60 pts) | **Recommended**: 3/3 (30 pts) | **Aspirational**: 3/10
**V-01 Composite: 93** | Golden: YES (all essential pass, composite >= 80)

---

### V-02 — Output Format (Scoring Tables)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 sub-skills represented | **PASS** | Five numbered sections explicitly called out; table-per-sub-skill structure makes omission visually obvious as a blank table. |
| C-02 | Ranked by adoption impact | **PASS** | Master Ranked Table: "sorted by adoption impact (P1 chasm-blocking first, then P1 majority-blocking, then P2, then P3)." Clear hierarchy. |
| C-03 | Explicit go/no-go verdict | **PASS** | "**Go/No-Go**: [GO | NO-GO | CONDITIONAL GO]" — named field, three explicit options. |
| C-04 | Blockers attributed to sub-skill | **PASS** | Blocker table has a dedicated "Sub-Skill Source" column. |
| C-05 | Artifact written to disk | **PASS** | Path declared at header; final block says "Write complete artifact to simulations/{topic}/validate-{date}.md. Confirm: 'Artifact written: …'" |
| C-06 | Cross-signal synthesis | **PASS** | Dedicated `## Cross-Signal Synthesis` section with format: "**Pattern [N]**: [Finding] appears in [sub-skill A] and [sub-skill B]." |
| C-07 | Per-sub-skill labeled sections | **PASS** | Five numbered `##` sections, each sub-skill isolated. |
| C-08 | Severity tiers | **PASS** | P1/P2/P3 defined inline ("blocking: prevents core use case or chasm crossing / major / minor"). Adoption Impact column separates design quality from adoption consequence. |
| C-09 | Adoption impact quantified | **PARTIAL** | "Impact Magnitude" column (high/medium/low) is present but generic — criterion requires specificity ("blocks innovator segment (5%)"). |
| C-10 | Remediation paths per blocker | **PASS** | Blocker table has explicit "Remediation Path" column. Structure demands it be populated for each listed blocker. |

**Essential**: 5/5 (60 pts) | **Recommended**: 3/3 (30 pts) | **Aspirational**: 8/10
**V-02 Composite: 98** | Golden: YES

---

### V-03 — Lifecycle Emphasis (Incomplete)

Prompt text not provided — only hypothesis available. Partial assessment:

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 sub-skills represented | **LIKELY PASS** | Hypothesis: "each phase must emit a named artifact before the next phase is permitted to begin." Phase-gate structure enforces sequential sub-skill execution. |
| C-02 | Ranked by adoption impact | **UNKNOWN** | Prompt text absent. Phase gates do not inherently address ranking logic. |
| C-03 | Explicit go/no-go verdict | **UNKNOWN** | Absent from hypothesis description. |
| C-04 | Blockers attributed | **UNKNOWN** | Absent from hypothesis description. |
| C-05 | Artifact written to disk | **LIKELY PASS** | Phase gate framing implies each phase writes output. |
| C-06–C-10 | All remaining | **UNKNOWN** | Cannot assess without prompt text. |

**V-03 Composite: Unscored** (insufficient data for R1 evaluation)

---

### Variation Ranking

| Rank | Variation | Composite | Golden | Δ from V-01 |
|------|-----------|-----------|--------|-------------|
| 1 | V-02 — Output Format | 98 | YES | +5 |
| 2 | V-01 — Role Sequence | 93 | YES | baseline |
| 3 | V-03 — Lifecycle Emphasis | unscored | — | — |

---

### Excellence Signals (from V-02)

**EX-1 — Table-format as completeness gate**: Structural tables per sub-skill make omission visible as an empty row, not invisible as missing prose. The model cannot silently skip listen-adoption — the table skeleton is already present.

**EX-2 — Remediation Path as a column**: Embedding remediation inside the blocker table (not as a separate prose section) forces population of each cell. C-10 passes because the answer appears in a defined slot, not as optional commentary.

**EX-3 — Adoption Impact as a named column separate from Severity**: The Adoption Impact column explicitly separates the two axes — a finding can be P3 severity and high adoption impact. The column heading alone communicates that these are different, preventing rank-by-severity errors.

**EX-4 — Explicit confirmation line**: "Confirm: 'Artifact written: …'" closes the C-05 verification loop — the model must emit the confirmation string, giving a detectable signal that the write step executed.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["table-format-as-completeness-gate", "remediation-path-as-structured-column"]}
```
