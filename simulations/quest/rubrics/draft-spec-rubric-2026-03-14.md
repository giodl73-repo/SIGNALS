Rubric written to `simulations/quest/rubrics/draft-spec-rubric-2026-03-14.md`.

**Summary of v1 criteria:**

**Essential (5, 60 pts):**
- **C-01** Structure — all guided sections present and not reordered
- **C-02** Scout status table — LOADED/NOT FOUND before any spec content
- **C-03** P0 coverage — explicit count, waiver stated when no artifact
- **C-04** Self-review findings — at least one finding type, or written "none found"
- **C-05** Frontmatter — naming convention + all required fields

**Recommended (3, 30 pts):**
- **C-06** Secondary role invoked (not just listed)
- **C-07** Contradiction detection + resolution or flagging
- **C-08** Numbered amendment list with ≥2 actionable items

**Aspirational (2, 10 pts):**
- **C-09** No-scout-context fallback documented as a named conditional
- **C-10** Cross-namespace coherence — one decision traced to a non-requirements signal

Golden threshold: all 5 essential pass + composite ≥ 80.
 the status table is a fail even if artifacts were used |
| C-03 | P0 requirement coverage | essential | coverage | Every P0 requirement from a loaded scout-requirements artifact maps to a named spec entry; coverage count is stated explicitly (e.g., "8/8 P0 requirements covered"); criterion is waived — not silently skipped — when no scout-requirements artifact exists, and the waiver is stated |
| C-04 | Self-review findings present | essential | behavior | A findings section explicitly addresses at least one of: contradictions, gaps, ambiguities, or hotspots; stating "none found" as a written claim is a pass; absence of the section, or producing an empty section without a written claim, is a fail |
| C-05 | Artifact frontmatter complete | essential | correctness | Output artifact follows `{topic}-spec-{date}.md` naming convention; frontmatter includes all required fields: skill, topic, item, date, skill_version, input |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | Secondary role validation | recommended | behavior | At least one secondary role (PM, Strategy, Compliance, or Design) is explicitly invoked to validate a named section and records PASS or a finding; listing role names without invoking them does not satisfy |
| C-07 | Contradiction detection and resolution | recommended | depth | Any conflicting requirements between loaded scout artifacts are identified by name (e.g., "R-06 vs R-10") and resolved or flagged with a proposed amendment; detection without resolution or flagging does not satisfy |
| C-08 | Actionable amendment list | recommended | depth | Phase 4 (Amend) produces a numbered list of at least 2 specific, actionable items that address gaps or ambiguities surfaced in the findings phase; vague items ("improve section 2") do not satisfy |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | No-scout-context fallback documented | aspirational | coverage | Spec explicitly documents behavior when no prior scout context is available (e.g., "ask 3–5 sentence description" or equivalent fallback prompt); fallback must appear as a named conditional in the spec, not implied by absence |
| C-10 | Cross-namespace coherence | aspirational | depth | At least one spec decision (constraint, design choice, or naming convention) is explicitly traced to a signal from a namespace other than scout-requirements (e.g., feasibility score, compliance posture, positioning differentiator), with the source artifact named |

---

## Scoring

- Essential criteria C-01..C-05: 12 pts each, 60 pts total
- Recommended criteria C-06..C-08: 10 pts each, 30 pts total
- Aspirational criteria C-09..C-10: 5 pts each, 10 pts total
- **Grand total: 100 pts**
- All criteria are binary pass/fail at the stated weight

**Composite score formula**:
```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.
